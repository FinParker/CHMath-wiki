# 贡献指南

感谢你对 CHMath-wiki 感兴趣！本页说明如何为这个 wiki 贡献内容。

## 贡献什么

- **新内容**：按[内容路线图](roadmap.md)编写缺失的页面。
- **改进**：修正错误、补充证明细节、改进措辞、增加例子。
- **结构**：改善信息架构、交叉链接、标签体系。

## 工作流程

1. Fork 本仓库，创建功能分支（如 `docs/set-theory`）。
2. 在 `docs/` 下按章节结构新建或修改 Markdown 文件。
3. 本地构建验证（见下文），确保无警告、无坏链接。
4. 提交并推送，发起 Pull Request。
5. 维护者 review 后合并，GitHub Actions 会自动部署到 GitHub Pages。

## 内容要求

1. **精准**：定义、定理、证明必须严格正确；引用他人内容请注明来源。
2. **简洁**：删除冗余；一个概念讲清楚即可，不要堆砌。
3. **抓住本质**：每个定义尽量交代"为什么这样定义"；每个定理交代证明的关键思想。
4. **遵循写作规范**：请先阅读[写作规范](writing-guide.md)。

## 本地构建

```bash
# 1. 创建虚拟环境（Python 3.9+）
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 本地预览（http://127.0.0.1:8000）
mkdocs serve

# 4. 严格构建检查（与 CI 相同）
mkdocs build --strict
```

## 编码约定

- 文件一律 **UTF-8** 编码，**LF** 换行。
- 文件名使用英文小写蛇形命名（如 `set_theory.md`），中文只出现在标题与正文中。
- 交叉链接使用**相对路径**的 Markdown 链接（`[集合](../foundations/set_theory/basics.md)`），
  这样在 Obsidian 与 mkdocs 中都能正常跳转。
- 每个页面的 front matter 至少包含 `title` 与 `tags`。

## 提交规范

- 提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/)：
  - `docs: 新增集合论-关系页面`
  - `fix: 修正群定义中的笔误`
  - `chore: 更新依赖`
- 重要变更同步更新 [CHANGELOG.md](https://github.com/FinParker/CHMath-wiki/blob/main/CHANGELOG.md)。
