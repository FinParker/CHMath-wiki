---
title: 高阶、导出与凝聚数学
tags: [前沿数学, 范畴论, 代数几何]
---

# 高阶、导出与凝聚数学

## 高阶范畴

普通范畴有对象和态射；$2$-范畴还允许态射之间的态射。$\infty$-范畴（infinity-category）把这种结构继续到任意层级，并要求足够高阶的复合只在 coherent homotopy 意义下成立。

它提供了一种同时保存对象、映射和全部高阶同伦信息的语言，已成为现代 homotopy theory、derived algebraic geometry 和 topological field theory 的基础设施。研究难点不仅是证明定理，还包括选择可计算模型以及在不同模型间运输结构。

## Derived algebraic geometry

经典代数几何中的交集可能“不横截”，从而丢失重数和变形信息。导出代数几何（derived algebraic geometry, DAG）用 chain complexes、simplicial rings 或 $E_\infty$-rings 替代普通交换环，把隐藏的 higher Tor 数据保留下来。

导出交（derived intersection）能统一处理 deformation theory、moduli problems、virtual fundamental classes 与 shifted symplectic structures。当前方向包括 derived stacks、spectral algebraic geometry、Donaldson–Thomas theory 和量子化。

## Condensed mathematics

Dustin Clausen 与 Peter Scholze 提出的凝聚数学（condensed mathematics）用定义在 profinite sets 上的 sheaves 重新组织拓扑代数。它旨在改善传统 topological groups、topological vector spaces 和 functional analysis 中不良的范畴性质。

后续的 solid modules、liquid vector spaces 与 analytic geometry 尝试建立一个能同时容纳实、复和 $p$-adic 分析的同调代数框架。该领域仍很年轻：基础理论、经典分析的重建、与几何表示论的应用都在发展。

2026 年发布的稳定讲义版本使早期课程材料有了更便于引用的文本，但这不意味着整个计划已经完成。

## 三者为何相遇

高阶范畴负责记录 coherent homotopy，derived 方法保存非横截和变形信息，condensed 方法改善带拓扑对象的代数行为。现代算术几何和几何表示论经常需要同时使用这三层语言。

## 资料

- [Toën: Derived Algebraic Geometry survey](https://arxiv.org/abs/1401.1044)
- [Scholze: Lectures on Condensed Mathematics](https://arxiv.org/abs/2605.03658)
- [Scholze 的凝聚数学与解析几何讲义](https://www.math.uni-bonn.de/people/scholze/Notes.html?language=en)
- [范畴论](../foundations/category_theory/index.md)与[代数拓扑](../topology/algebraic_topology.md)
