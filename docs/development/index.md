---
title: 项目开发
tags:
  - 开发
---

# 项目开发

本页面向维护者，记录项目的技术栈、目录结构与发布流程。

## 技术栈

| 组件   | 版本/说明                                          |
| ------ | -------------------------------------------------- |
| 静态站 | mkdocs + mkdocs-material（`mkdocs.yml` 配置）      |
| 数学   | MathJax 3 + pymdownx.arithmatex（`$...$` / `$$...$$`） |
| 搜索   | 内置搜索，`language: zh`（中文分词 + 拼音）        |
| 部署   | GitHub Actions（`.github/workflows/deploy-docs.yml`）→ GitHub Pages |
| Python | 3.9+（CI 使用 3.12）                               |

## 目录结构

```
docs/
  index.md                  # 首页
  tags.md                   # 标签索引（tags 插件自动填充）
  intro/                    # 关于、路线图、贡献、写作规范
  notation/                 # 符号表
  foundations/              # 数学基础: logic / set_theory / category_theory
  algebra/                  # 代数: structures / linear
  analysis/                 # 分析: calculus / real / complex
  geometry/  topology/      # 几何、拓扑
  number_theory/            # 数论
  discrete_mathematics/     # 离散数学
  probability_statistics/   # 概率与统计
  applied_math/             # 应用数学（占位）
  tricks/                   # 解题技巧
  elementary/               # 初等数学（草稿）
  development/              # 项目开发文档
```

## 常用命令

```bash
pip install -r requirements.txt   # 安装依赖
mkdocs serve                      # 本地预览
mkdocs build --strict             # 严格构建（CI 同款）
mkdocs gh-deploy --force          # 部署到 gh-pages（或由 CI 自动完成）
```

> 若构建日志出现 mkdocs-material 关于 MkDocs 2.0 的横幅噪音，
> 可设置环境变量 `NO_MKDOCS_2_WARNING=true` 抑制（CI 已默认设置）。

## 发布流程

推送到 `main` 分支后，GitHub Actions 自动执行：

1. 检出代码（`fetch-depth: 0`，保留完整历史，供 git-revision 插件使用）。
2. 安装 Python 3.12 与依赖。
3. `mkdocs build --strict` 严格构建校验。
4. `mkdocs gh-deploy --force` 部署到 `gh-pages` 分支。

## 约定

- 新增页面必须登记到 `mkdocs.yml` 的 `nav` 中。
- 移动/删除页面时，在 `plugins.redirects.redirect_maps` 中登记旧链接重定向。
- 每个新页面带 front matter（`title`、`tags`），遵守[写作规范](../intro/writing-guide.md)。
- 重要变更写入 [CHANGELOG.md](https://github.com/FinParker/CHMath-wiki/blob/main/CHANGELOG.md)。
