---
title: 微分几何
tags: [几何, 微分几何]
---

# 微分几何

> 微分几何（differential geometry）用微积分研究曲线、曲面和流形的局部与整体性质。

## 流形与切空间

$n$ 维流形（manifold）局部看起来像 $\mathbb R^n$，坐标图之间用光滑映射粘合。点 $p$ 的切空间 $T_pM$ 收集所有切向量；余切空间 $T_p^*M$ 则承载微分形式。

## Riemann 度量

Riemann 度量在每个切空间上平滑指定内积 $g_p$，从而定义长度、角度、体积和测地线（geodesic）。Levi-Civita 联络是唯一与度量相容且无挠的联络。

## 曲率

曲线曲率描述切向量改变速度；曲面的 Gaussian 曲率是主曲率之积。Gauss 绝妙定理（Theorema Egregium）说明 Gaussian 曲率完全由内蕴度量决定。Gauss–Bonnet 定理把曲率积分与 Euler 示性数联系：

$$\int_M K\,dA=2\pi\chi(M)$$

（闭、可定向曲面情形）。这是局部几何与整体拓扑相遇的典范。

## 延伸阅读

- [多元微积分](../analysis/multivariable.md)：局部计算工具。
- [拓扑空间](../topology/topological_spaces.md)：流形的拓扑基础。
