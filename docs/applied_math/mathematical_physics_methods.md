---
title: 数学物理方法
tags: [应用数学, 数学物理, 偏微分方程]
---

# 数学物理方法

> 数学物理方法（mathematical methods in physics）是一套把物理定律转化为可分析、可近似和可计算模型的工具。它侧重解题方法；关于量子场论、镜像对称等研究方向，见[数学物理与量子结构](../frontiers/mathematical_physics.md)。

## 从建模开始

建模时先明确状态量、参数、守恒律、对称性、初边值条件和观测尺度。量纲分析（dimensional analysis）用于检查方程并寻找无量纲组合；无量纲化（nondimensionalization）还能揭示真正控制行为的参数，例如 Reynolds number。

一个典型流程是：

1. 由守恒律或变分原理建立方程；
2. 利用对称性、尺度和线性结构化简；
3. 选择变换、特征函数或 Green 函数求解；
4. 无闭式解时使用渐近或数值方法；
5. 检查量纲、边界条件、稳定性和适用范围。

## Fourier 与 Laplace 方法

Fourier 变换（Fourier transform）把微分转为频域乘法。一种常见约定是

$$
\widehat f(k)=\int_{-\infty}^{\infty}f(x)e^{-ikx}\,dx,
\qquad
f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\widehat f(k)e^{ikx}\,dk.
$$

它适合平移不变的线性方程、波动和信号分析。Laplace 变换（Laplace transform）尤其适合带初值的演化问题。不同资料的归一化约定可能不同，但正逆变换必须配套。

复分析（complex analysis）中的留数定理（residue theorem）、解析延拓（analytic continuation）与围道积分（contour integration）可计算变换反演、响应函数和渐近积分。

## 分离变量与 Sturm–Liouville 理论

对规则区域上的线性 PDE，分离变量法（separation of variables）把 $u(x,t)$ 写成 $X(x)T(t)$，将 PDE 化为若干 ODE。空间部分常形成 Sturm–Liouville 问题

$$
-(p(x)y')'+q(x)y=\lambda w(x)y.
$$

在适当边界条件下，该算子的特征函数具有正交性与完备性，可展开初值和外力。Fourier 级数正是这种特征函数展开（eigenfunction expansion）的典型例子。

## Green 函数与分布

对线性算子 $L$，Green 函数（Green's function）形式上满足

$$L_xG(x,y)=\delta(x-y),$$

并同时编码边界或辐射条件。若 $Lu=f$，解可写成


$$u(x)=\int G(x,y)f(y)\,dy,$$

必要时还需加入边界项。Dirac delta 是分布（distribution）而非普通函数；这一语言允许点源、瞬时冲击和弱导数被统一处理。

## 变分原理、对称性与守恒量

若作用量 $S[q]=\int L(q,\dot q,t)\,dt$ 在固定端点变分下取驻值，则 Euler–Lagrange 方程（Euler–Lagrange equation）为

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q}
-\frac{\partial L}{\partial q}=0.
$$

Noether 定理（Noether's theorem）在适当光滑性和变分假设下，把作用量的连续对称性对应到守恒量：时间平移对应能量，空间平移对应动量，旋转对应角动量。群（group）与表示（representation）进一步组织简并、选择定则和正常模态。

## 微扰与渐近方法

当问题含小参数 $\varepsilon$ 时，可尝试正则微扰展开（regular perturbation expansion）

$$u=u_0+\varepsilon u_1+\varepsilon^2u_2+\cdots.$$

若最高阶导数前含小参数，极限可能改变方程阶数，形成奇异微扰（singular perturbation）；此时需要边界层（boundary layer）、匹配渐近展开（matched asymptotic expansions）或多重尺度法（multiple scales）。WKB 方法（Wentzel–Kramers–Brillouin method）适合短波或半经典极限。渐近级数不必收敛，它要求截断误差在指定极限中受控。

## 典型方程与方法

| 问题 | 常用结构与方法 |
| --- | --- |
| 热方程 | Fourier 变换、特征函数、热核、最大值原理 |
| 波方程 | 特征线、d'Alembert 公式、正常模态、能量估计 |
| Poisson / Laplace 方程 | Green 函数、调和函数、变分法、有限元 |
| Schrödinger 方程 | 谱理论、Fourier 方法、微扰论、WKB |
| 流体方程 | 无量纲化、守恒律、涡量、稳定性与数值模拟 |
| 振动与波导 | Sturm–Liouville 理论、特殊函数、模态展开 |

实际问题还会用积分方程（integral equation）、算子与谱理论（operator and spectral theory）、有限差分（finite difference）、有限元（finite element）和谱方法（spectral method）。解析方法揭示结构，数值方法处理复杂区域和非线性，两者需要误差与稳定性分析连接。

## 资料

- [MIT OCW: Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/pages/syllabus/)
- [MIT OCW: Introduction to Partial Differential Equations](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/pages/calendar/)
- [MIT OCW: Integral Equations](https://ocw.mit.edu/courses/18-307-integral-equations-spring-2006/pages/readings/)
- [微分方程](differential_equations.md)、[数值分析](numerical_analysis.md)与[最优化](optimization.md)
