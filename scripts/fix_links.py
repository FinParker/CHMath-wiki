#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CHMath-wiki 链接修复脚本（集成阶段一次性使用）

策略：
1. 扫描 docs/ 下所有 .md 文件中的相对 Markdown 链接 (path)（跳过 http/mailto/# 等）。
2. 按 mkdocs 规则（相对源文件目录）解析目标；存在则跳过。
3. 若不存在：
   a. 对非 index.md：在 docs/ 全树查找同 basename 文件，唯一候选则改写为正确相对路径；
      多个候选则选与当前目录公共前缀最长的那个。
   b. 对 index.md 或 basename 无候选：把链接目标去掉前导 "../" 后的路径成分依次
      （从最长开始）在 docs/ 中查找存在的文件，命中则改写。
4. 仍无法解析的链接输出"死链"报告（人工处理）。
"""
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EXCLUDE_PREFIX = ("http://", "https://", "mailto:", "tel:", "#", "ftp://")


def all_md_files():
    for dirpath, _dirnames, filenames in os.walk(DOCS):
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def build_index():
    basename_index = defaultdict(list)
    for f in all_md_files():
        rel = os.path.relpath(f, DOCS).replace("\\", "/")
        basename_index[os.path.basename(rel)].append(rel)
    return basename_index


def resolve(rel_dir, target):
    """mkdocs 语义解析: 相对源文件目录; 返回 docs 相对路径, 越界返回 None"""
    joined = os.path.normpath(os.path.join(rel_dir, target)).replace("\\", "/")
    if joined == ".." or joined.startswith("../"):
        return None
    return joined


def correct_link(rel_dir, target, basename_index):
    """尝试为死链找到正确目标, 返回 (docs相对路径 | None)"""
    base = os.path.basename(target)
    if base != "index.md":
        cands = basename_index.get(base, [])
        if len(cands) == 1:
            return cands[0]
        if len(cands) > 1:
            return max(cands, key=lambda c: len(os.path.commonpath([rel_dir, c])))
    # index.md 或 basename 无候选: 用去掉前导 .. 的路径成分做后缀匹配
    parts = [p for p in target.split("/") if p not in ("", ".", "..")]
    for i in range(len(parts)):
        cand = "/".join(parts[i:])
        if os.path.exists(os.path.join(DOCS, cand)):
            return cand
    return None


def main():
    basename_index = build_index()
    fixed, dead = [], []
    for f in all_md_files():
        rel = os.path.relpath(f, DOCS).replace("\\", "/")
        rel_dir = os.path.dirname(rel)
        with open(f, encoding="utf-8") as fh:
            content = fh.read()
        original = content

        def fix(match):
            target = match.group(1).strip()
            target_path = target.split("#")[0]
            if not target_path or target_path.startswith(EXCLUDE_PREFIX):
                return match.group(0)
            resolved = resolve(rel_dir, target_path)
            if resolved and os.path.exists(os.path.join(DOCS, resolved)):
                return match.group(0)
            correct = correct_link(rel_dir, target_path, basename_index)
            if not correct:
                dead.append((rel, target))
                return match.group(0)
            new_target = os.path.relpath(
                os.path.join(DOCS, correct), os.path.join(DOCS, rel_dir)
            ).replace("\\", "/")
            if "#" in target:
                new_target += "#" + target.split("#", 1)[1]
            fixed.append((rel, target, new_target))
            return match.group(0).replace(target, new_target)

        content = LINK_RE.sub(fix, content)
        if content != original:
            with open(f, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(content)

    print(f"=== 修复 {len(fixed)} 处链接 ===")
    for rel, old, new in fixed:
        print(f"  {rel}: {old} -> {new}")
    print(f"=== 死链 {len(dead)} 处 ===")
    for rel, target in dead:
        print(f"  {rel}: {target}")


if __name__ == "__main__":
    main()
