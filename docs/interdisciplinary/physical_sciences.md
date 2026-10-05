---
title: 数学与物理、化学及材料
tags: [交叉学科, 数学物理, 化学, 材料]
---

# 数学与物理、化学及材料

## 物理定律的数学结构

经典力学可由 Newton 方程、Hamilton 系统或作用量的驻值原理表达。连续介质、流体和电磁场通常由偏微分方程（partial differential equation, PDE）描述；相对论使用流形与张量；量子理论则依赖复 Hilbert 空间、算子和谱理论。

例如 Schrödinger 方程

$$
i\hbar\frac{\partial\psi}{\partial t}=\widehat H\psi
$$

把量子态的演化写成 Hilbert 空间中的线性动力学。可观测量对应算子，但“算子的特征值就是可能测量值”等说法还需要指定算子的自伴性、定义域与谱类型。

## 对称性、群与守恒律

旋转、平移和内部对称性由群（group）及其表示（representation）组织。Noether 定理（Noether's theorem）把作用量的连续对称性与守恒量联系起来。晶体的空间群（space group）、分子的点群（point group）和量子态的表示论都使用同一种对称语言。

对称性可以限制允许的方程与跃迁，却不能单独确定材料的全部动力学；边界、尺度和相互作用强度仍然重要。

## 化学反应与反应扩散

质量作用定律（law of mass action）把反应网络转成 ODE。若组分还能在空间扩散，常得到反应扩散方程（reaction–diffusion equation）

$$
\frac{\partial u}{\partial t}=D\Delta u+f(u).
$$

$D\Delta u$ 描述扩散，$f(u)$ 描述局部反应。不同扩散率与非线性反应可能导致 Turing pattern、传播前沿和化学振荡。方程中的连续浓度近似在分子数很少时可能失效，此时要使用 chemical master equation 或 stochastic simulation。

## 统计力学与多尺度

统计力学从大量微观自由度推导宏观量。正则系综中状态 $i$ 的权重为

$$
p_i=\frac{e^{-\beta E_i}}{Z},\qquad
Z=\sum_i e^{-\beta E_i},
$$

其中 $Z$ 是配分函数（partition function）。自由能、相变和响应函数可由 $Z$ 的导数得到。这里的概率来自对微观状态的统计描述，其解释依赖所用系综与极限过程。

材料科学跨越电子、原子、介观组织到宏观结构多个尺度，常结合 density functional theory、molecular dynamics、phase-field model、有限元和 homogenization。多尺度模型必须说明不同层级怎样传递参数与误差。

## 反问题与实验数据

散射、谱学、断层成像和材料表征经常从间接测量 $y$ 反推结构 $x$：

$$y=F(x)+\varepsilon.$$

若小测量误差会造成巨大解误差，问题就是不适定的（ill-posed）。正则化（regularization）、Bayesian inverse problem 与不确定性量化用于约束可能解；正则化得到的是在给定先验和损失下稳定的解，不保证恢复唯一“真实结构”。

## 延伸阅读

- [数学物理方法](../applied_math/mathematical_physics_methods.md)
- [数学物理与量子结构](../frontiers/mathematical_physics.md)
- [微分几何](../geometry/differential_geometry.md)与[泛函分析](../analysis/functional_analysis.md)
- [SIAM: Mathematical Modeling and Computation](https://epubs.siam.org/doi/pdf/10.1137/1.9781611973549.fm)：物理、化学、材料与生命科学中的建模主题。
