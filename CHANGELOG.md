# CHANGELOG

本文件记录 CHMath-wiki 的每次重要变更，格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added

- 新增 LICENSE（CC BY-SA 4.0）并重写 README。
- CI 升级：Python 3.12 + 依赖缓存 + 部署前严格构建校验（`.github/workflows/deploy-docs.yml`）。

## [0.2.0] - 2025-06-11

### Added

- 重构为新信息架构(IA)：按现代数学学科脉络组织内容 —— 数学基础（数理逻辑/集合论/范畴论）、
  代数（代数结构/线性代数）、分析（微积分/实分析/复分析）、几何、拓扑、数论、离散数学、
  概率与统计、应用数学、解题技巧、初等数学（草稿区）。
- 为每个章节建立索引页（MOC，Map of Content），并重写首页为卡片式导航。
- 新增入门文档：关于本项目、内容路线图、贡献指南、写作规范；新增项目开发文档。
- 建立统一内容模板与写作规范（front matter、数学公式排版、交叉链接约定）。

### Changed

- 技术栈现代化（仍为 mkdocs-material，但整体升级）：
  - MathJax 2.7 → MathJax 3（CDN 加载，配合 pymdownx.arithmatex）；
  - 移除过时的 mkdocs-video、mkdocs-gitbook 依赖；
  - 搜索启用中文分词（`language: zh`）；主题支持浅色/深色切换；
  - 新增标签系统（mkdocs-material 9.7 listings 语法）；
  - 移除对 Google Fonts 的依赖（`font: false`，中文系统字体渲染）。
- 目录重组：全部页面迁移到新路径（旧 URL 通过 mkdocs-redirects 重定向，链接不失效）。
  中文文件名迁移为英文蛇形命名（如 `tricks/阶乘.md` → `tricks/factorial.md`）。
- 依赖版本精确锁定（requirements.txt 固定版本，保证 CI 可复现）。
- 符号表扩充：合并离散数学旧概念表，新增常用集合/幂集/函数集/关系集记号。

### Fixed

- 移除对构建产物 `site/` 的误追踪（见 0.1.0，此处补充说明：含 64 个文件）。
- 修正符号表中 `\Reftarrow` 等 LaTeX 笔误（合并过程中一并处理）。

## [0.1.0] - 2025-06-11

### Added

- 建立 CHANGELOG.md，开始按语义化版本记录变更。
- 新增 `.gitignore`：忽略构建产物 `site/`、本地编辑器配置 `.obsidian/` 与 `.vscode/`、Python 虚拟环境等。
- 将 `site/`（mkdocs 构建输出）与 `.obsidian/` 从 Git 追踪中移除（此前被误提交）。

### Changed

- （重构进行中，详见后续版本条目）

### Fixed

- 移除对构建产物的误追踪。

[0.1.0]: https://github.com/FinParker/CHMath-wiki/releases/tag/v0.1.0
