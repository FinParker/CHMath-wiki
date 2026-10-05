---
title: Galois 理论
tags: [代数, Galois理论]
---

# Galois 理论

> Galois 理论（Galois theory）用群描述多项式根之间的对称性，把域扩张问题转化为群论问题。

## 域扩张与最小多项式

$K\subseteq L$ 称为域扩张（field extension）。若 $L$ 作为 $K$-向量空间维数有限，则扩张次数记为 $[L:K]$。元素 $\alpha$ 在 $K$ 上代数，当且仅当它是某个非零 $K[x]$ 多项式的根；首一不可约的最低次多项式称为最小多项式。

## 分裂域与 Galois 群

多项式 $f\in K[x]$ 的分裂域是包含其全部根的最小扩张。保持 $K$ 中元素不动的域自同构组成 Galois 群 $\operatorname{Gal}(L/K)$，它通过置换根揭示方程的对称。

## 基本定理

有限 Galois 扩张中，中间域与 Galois 群的子群之间存在反向对应：更大的子群固定更小的域。正规子群对应 Galois 中间扩张，商群描述剩余对称。

## 根式可解性

特征为 $0$ 时，多项式能用根式求解，当且仅当其 Galois 群是可解群（solvable group）。一般五次方程不存在统一根式公式，是因为一般五次方程的 Galois 群 $S_5$ 不可解。

## 延伸阅读

- [群](group.md)与[域](field.md)：先修概念。
- [MIT OCW: Algebra II](https://ocw.mit.edu/courses/18-702-algebra-ii-spring-2011/)：域论和 Galois 理论课程。
