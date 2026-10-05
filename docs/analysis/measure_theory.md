---
title: 测度论与 Lebesgue 积分
tags: [分析, 测度论]
---

# 测度论与 Lebesgue 积分

> 测度论（measure theory）回答“哪些集合可以测量、大小如何相加”，并为现代积分、概率论和泛函分析提供共同基础。

## 测度空间

$\sigma$-代数（sigma-algebra）$\mathcal F$ 对补集和可数并封闭。测度（measure）$\mu:\mathcal F\to[0,\infty]$ 满足 $\mu(\varnothing)=0$ 与可数可加性。三元组 $(X,\mathcal F,\mu)$ 称为测度空间。

实直线上的 Lebesgue 测度把区间长度推广到广泛的集合，但并非 $\mathbb R$ 的每个子集都可测。

## 可测函数与积分

若所有 $\{x:f(x)>a\}$ 都可测，则 $f$ 是可测函数（measurable function）。Lebesgue 积分先定义示性函数和简单函数，再用单调逼近定义非负函数，最后处理正负部分：

$$\int f\,d\mu=\int f^+\,d\mu-\int f^-\,d\mu.$$

它按“函数值的层级”组织求和，比 Riemann 积分更适合极限过程。

## 三大收敛定理

- 单调收敛定理（monotone convergence theorem）：$0\le f_n\uparrow f$ 时，积分极限可交换。
- Fatou 引理（Fatou's lemma）：给出非负函数列的下极限估计。
- 控制收敛定理（dominated convergence theorem）：若 $f_n\to f$ 且 $|f_n|\le g\in L^1$，则 $\int f_n\to\int f$。

Tonelli 定理适用于非负函数，Fubini 定理适用于可积函数，二者说明何时能够交换积分次序。

## $L^p$ 空间

对 $1\le p<\infty$，定义

$$\|f\|_p=\left(\int|f|^p\,d\mu\right)^{1/p}.$$

$L^p$ 是 Banach 空间；$L^2$ 还是 Hilbert 空间，内积为 $\langle f,g\rangle=\int f\overline g\,d\mu$。Hölder 不等式和 Minkowski 不等式分别保证乘积可积性与三角不等式。

## 与概率论的关系

概率空间就是满足 $\mu(X)=1$ 的测度空间。随机变量是可测函数，期望是 Lebesgue 积分，概率收敛定理因此是测度论收敛定理的具体应用。

## 资料

- [MIT OCW: Measure and Integration](https://ocw.mit.edu/courses/18-125-measure-and-integration-fall-2003/)：覆盖 Lebesgue 积分、$L^p$、Radon–Nikodym 与 Fubini 定理。
- [概率论基础](../probability_statistics/basics.md)：概率测度的入门。
- [泛函分析](functional_analysis.md)：把函数空间作为几何对象研究。
