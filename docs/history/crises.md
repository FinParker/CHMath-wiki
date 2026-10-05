---
title: 数学危机
tags: [数学史, 数学基础]
---

# 数学危机

> “三次数学危机”是常见的教学概括。真实历史更连续、更复杂，但这个框架有助于理解数学如何通过修正概念和证明标准继续发展。

## 第一次危机：不可公度量

传统叙述把第一次数学危机与 $\sqrt2$ 的无理性联系起来。若正方形边长为 $1$，对角线长为 $\sqrt2$；假设 $\sqrt2=p/q$ 且分数最简，可推出 $p,q$ 同为偶数，矛盾。

这说明整数比不足以表示全部几何长度。希腊数学以 Eudoxus 比例论等方式处理不可公度量，几何量与数的关系由此变得更精细。把事件描述为某个瞬间的“发现与封锁”缺乏可靠史料支持。

## 第二次危机：无穷小与微积分严格化

Newton、Leibniz 的微积分极其有效，但早期“无穷小量”缺少统一严格定义。导数计算中既把增量视为非零以便相除，又令其消失，容易引起逻辑质疑。

十九世纪的 Cauchy、Bolzano、Weierstrass 等用极限、$\varepsilon$–$\delta$ 语言重建分析；Dedekind 分割与 Cauchy 序列给出实数的严格构造。危机的结果不是抛弃微积分，而是澄清其对象和推理规则。二十世纪的非标准分析又给无穷小提供了另一种严格模型。

## 第三次危机：集合论悖论与基础之争

Cantor 集合论为分析和现代数学提供统一语言，但朴素概括原则会产生 Russell 悖论：令

$$R=\{x:x\notin x\},$$

则 $R\in R\iff R\notin R$。回应包括 Zermelo–Fraenkel 公理化集合论、Russell 类型论，以及对数学基础的三种代表性立场：

- 逻辑主义（logicism）：数学可还原为逻辑；
- 形式主义（formalism）：研究符号系统并证明其一致性；
- 直觉主义（intuitionism）：强调构造，限制排中律的使用。

Gödel 不完备定理表明，足够强且一致的可有效公理化系统不能在内部证明自身一致性，也不能判定其语言中的所有命题。这阻止了 Hilbert 原计划的完整实现，但没有使公理化方法失效，反而开辟了模型论、证明论和可计算性理论。

## 后续影响

这些危机具有共同结构：新对象或方法先产生强大结果，随后暴露概念缺口，最终通过更精确的语言得到重建。现代类型论、HoTT 与形式化证明仍在延续对“数学对象是什么、证明为何可信”的探索。

## 资料

- [Stanford Encyclopedia of Philosophy: Hilbert's Program](https://plato.stanford.edu/entries/hilbert-program/)
- [MacTutor: Beginnings of Set Theory](https://mathshistory.st-andrews.ac.uk/HistTopics/Beginnings_of_set_theory/)
- [ZFC 公理系统](../foundations/set_theory/zfc.md)与[证明论](../foundations/logic/proof_theory.md)
