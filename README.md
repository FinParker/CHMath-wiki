# CHMath-wiki

一个旨在通过提供**精准、简洁且抓住问题本质**的数学内容，来提升数学理解能力的中文资料库。

面向初中以上学力、对数学感兴趣的学习者，兼顾中学自学路线与现代数学的学科脉络。

在线阅读：[CHMath-wiki GitHub Pages](https://finparker.github.io/CHMath-wiki/)

学习导航：[数学领域地图](docs/intro/mathematics-map.md)

课程覆盖审计：[本科与研究生数学内容对照](docs/intro/curriculum-gap-analysis.md)

## 内容结构

| 章节         | 内容                                            |
| ------------ | ----------------------------------------------- |
| 初等数学     | 初中数学 · 高中数学 · 函数 · 三角函数 · 数列   |
| 数学基础     | 数理逻辑/证明论 · 集合论 · 范畴论 · 类型论       |
| 代数         | 代数结构 · 线性代数 · Galois 理论               |
| 分析         | 微积分 · 多元微积分 · 实/复分析 · 测度/泛函分析 |
| 几何 · 拓扑  | 初等/微分/分形几何 · 点集/代数拓扑              |
| 数论         | 初等数论 · 素数 · 模运算                        |
| 离散数学     | 组合数学 · 图论 · 自动机理论                    |
| 概率与应用   | 概率统计 · 随机过程 · 微分方程 · 数学物理方法 · 优化 |
| 交叉学科     | 物理材料 · 计算信息 · 生命医学 · 经济社会 · 工程环境 |
| 数学史       | 发展简史 · 数学危机 · Hilbert 问题 · 著名难题   |
| 前沿数学     | Langlands · 导出/凝聚数学 · SPDE · TDA · AI 数学 · 形式化数学 |

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
