# 关于本项目

**CHMath-wiki** 是一个面向初中以上学力、对数学感兴趣的学习者的中文数学资料库。
它的目标是提供**精准、简洁、抓住问题本质**的内容——不堆砌公式，而是讲清楚每个概念
"是什么、为什么、怎么用"。

## 内容定位

- 初等数学部分面向初中与高中学习者；进阶部分逐步覆盖本科高年级的现代数学基石。
- 每条内容强调**本质**：定义背后的动机、定理之间的逻辑关系、证明的关键思路。
- 内容按**现代数学的学科脉络**组织，而非按教材章节组织，便于长期生长为大型 wiki。

## 项目历史

本项目最初是作者的数学笔记集合（mkdocs 搭建），内容以离散数学笔记为主。
2025 年 6 月进行了大规模重构：重新设计信息架构、升级数学渲染引擎、引入标签系统与
旧链接重定向，并开始系统性扩充集合论、范畴论、线性代数、分析等学科内容。
完整的变更记录见 [CHANGELOG](https://github.com/FinParker/CHMath-wiki/blob/main/CHANGELOG.md)。

## 技术栈

| 组件   | 选择                                                    |
| ------ | ------------------------------------------------------- |
| 文档站 | [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) |
| 数学   | MathJax 3（配合 pymdownx.arithmatex，支持 `$...$` / `$$...$$`） |
| 搜索   | mkdocs-material 内置搜索（中文分词 + 拼音）              |
| 部署   | GitHub Actions → GitHub Pages                           |

详见[项目开发文档](../development/index.md)。

## 学习入口

- [初中数学](../elementary/junior_high.md)
- [高中数学](../elementary/senior_high.md)
- [内容路线图](roadmap.md)

## 版权

本站内容采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 协议发布。
