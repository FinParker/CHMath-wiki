# CHMath-wiki

一个旨在通过提供**精准、简洁且抓住问题本质**的数学内容，来提升数学理解能力的中文资料库。

面向高中以上学力、对数学研究感兴趣的学习者，按现代数学的学科脉络组织内容。

## 内容结构

| 章节         | 内容                                            |
| ------------ | ----------------------------------------------- |
| 数学基础     | 数理逻辑 · 集合论 · 范畴论                      |
| 代数         | 代数结构（群/环/域/多项式）· 线性代数           |
| 分析         | 微积分 · 实分析 · 复分析                        |
| 几何 · 拓扑  | 初等几何 · 拓扑空间/连通性/紧致性               |
| 数论         | 初等数论 · 素数 · 模运算                        |
| 离散数学     | 组合数学 · 图论 · 自动机理论                    |
| 其他         | 概率与统计 · 解题技巧 · 初等数学（草稿）        |

## 技术栈

- **文档站**：[mkdocs-material](https://squidfunk.github.io/mkdocs-material/)（Material for MkDocs）
- **数学渲染**：MathJax 3（`$...$` / `$$...$$`）
- **部署**：GitHub Actions → GitHub Pages

## 本地构建

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # 本地预览 http://127.0.0.1:8000
mkdocs build --strict # 严格构建检查
```

## 参与贡献

阅读 [贡献指南](docs/intro/contribute.md) 与 [写作规范](docs/intro/writing-guide.md)。
重要变更请同步更新 [CHANGELOG.md](CHANGELOG.md)。

## 许可证

[CC BY-SA 4.0](LICENSE)
