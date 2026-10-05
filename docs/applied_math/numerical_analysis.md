---
title: 数值分析
tags: [应用数学, 数值分析]
---

# 数值分析

> 数值分析（numerical analysis）研究怎样在有限精度计算机上稳定、有效地近似数学对象。

## 误差与稳定性

绝对误差为 $|x-\hat x|$，相对误差为 $|x-\hat x|/|x|$。总误差通常来自建模误差、截断误差和舍入误差。问题对输入扰动的敏感程度称为条件性（conditioning）；算法是否放大计算误差称为稳定性（stability）。

## 非线性方程

二分法在连续函数异号区间上可靠收敛。Newton 方法

$$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$$

在单根附近通常二次收敛，但依赖初值且可能失稳。

## 插值与数值积分

多项式插值可用 Lagrange 或 Newton 形式；高次等距插值可能出现 Runge 现象，分段样条与 Chebyshev 节点更稳健。梯形公式、Simpson 公式和 Gaussian quadrature 用有限个函数值近似积分。

## 线性代数与微分方程

求解 $Ax=b$ 时，通常用带主元的 LU 分解或迭代法，而不显式计算 $A^{-1}$。Euler 法是 ODE 的最简单一步法，Runge–Kutta 方法在计算量和精度之间取得更好平衡。

## 资料

- [MIT OCW: Introduction to Numerical Analysis](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/)：插值、求根、数值积分、ODE 与频谱方法。
- [线性代数](../algebra/linear/index.md)：矩阵计算基础。
