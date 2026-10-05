---
title: 微分方程
tags: [应用数学, 微分方程]
---

# 微分方程

> 微分方程（differential equation）用未知函数及其导数表达变化规律，是连续动力系统的基本语言。

## 常微分方程

一阶初值问题写成 $y'=f(t,y),y(t_0)=y_0$。Picard–Lindelöf 定理（existence and uniqueness theorem）在 $f$ 连续且对 $y$ 局部 Lipschitz 时保证局部解存在唯一。

可分离变量方程 $y'=g(t)h(y)$ 可形式化为

$$\int\frac{dy}{h(y)}=\int g(t)\,dt.$$

一阶线性方程 $y'+p(t)y=q(t)$ 使用积分因子 $\mu(t)=e^{\int p(t)dt}$。

## 高阶线性方程

常系数齐次方程

$$a_ny^{(n)}+\cdots+a_1y'+a_0y=0$$

通过特征多项式求解。复根产生振荡，重根带来多项式因子。非齐次方程可用待定系数法、常数变易法或 Green 函数。

## 动力系统

系统 $x'=F(x)$ 的平衡点满足 $F(x)=0$。线性化的 Jacobian 特征值决定双曲平衡点附近的稳定性；相图（phase portrait）展示轨道的整体结构。Lyapunov 函数则可在不显式求解时证明稳定性。

## 偏微分方程

三类原型是：Laplace 方程 $\Delta u=0$（椭圆型）、热方程 $u_t=\kappa\Delta u$（抛物型）、波方程 $u_{tt}=c^2\Delta u$（双曲型）。边界条件、初值、正则性和弱解共同决定问题是否适定。

## 资料

- [MIT OCW: Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/)：解析、数值和相平面方法。
- [数值分析](numerical_analysis.md)：无法显式求解时的近似方法。
