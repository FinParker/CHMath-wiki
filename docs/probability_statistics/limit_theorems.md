---
title: 概率极限定理
tags: [概率与统计]
---

# 概率极限定理

> 极限定理解释大量随机效应为何会呈现稳定规律。

## 收敛方式

随机变量列常见的收敛概念包括几乎处处收敛（almost sure convergence）、依概率收敛（convergence in probability）、$L^p$ 收敛与依分布收敛（convergence in distribution）。一般有

$$L^p\Rightarrow P,\qquad \text{a.s.}\Rightarrow P\Rightarrow d,$$

逆向蕴含通常不成立。

## 大数定律

若 $X_i$ 独立同分布且 $E|X_1|<\infty$，强大数定律（strong law of large numbers）给出

$$\frac{X_1+\cdots+X_n}{n}\to E[X_1]\quad\text{几乎处处}.$$

它说明样本均值为何能估计总体均值。

## 中心极限定理

若 $X_i$ 独立同分布，均值为 $\mu$、方差为 $0<\sigma^2<\infty$，则

$$\frac{\sum_{i=1}^nX_i-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1).$$

中心极限定理（central limit theorem）解释了正态分布的普遍性。它描述的是标准化误差的分布，而大数定律描述样本均值本身的稳定。

## 特征函数

特征函数（characteristic function）$\varphi_X(t)=E(e^{itX})$ 总是存在，并唯一确定分布。独立随机变量之和对应特征函数相乘，因此它是证明中心极限定理的重要工具。

## 资料

- [Harvard Stat 110](https://stat110.hsites.harvard.edu/)：大数定律与中心极限定理的直观和计算。
- [测度论](../analysis/measure_theory.md)：严格处理几乎处处收敛和积分换序。
