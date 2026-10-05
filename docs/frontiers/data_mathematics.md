---
title: 数据的数学
tags: [前沿数学, 数理统计, 应用数学]
---

# 数据的数学

> 数据科学带来的数学问题不仅是“应用已有公式”，也在推动高维概率、几何、拓扑、优化和统计理论形成新方向。

## 高维统计

经典渐近理论常固定维数 $p$、令样本量 $n\to\infty$；现代问题中 $p$ 可能与 $n$ 同阶甚至远大于 $n$。研究依靠 sparsity、low rank、manifold structure 等结构假设，使推断仍然可能。

代表问题包括 Lasso 的变量选择、矩阵补全、multiple testing、因果推断、分布漂移和 uncertainty quantification。Minimax rate 用来刻画任何估计方法都无法超越的误差尺度。

## 随机矩阵与高维概率

当矩阵维数同时增长时，特征值不再围绕有限维直觉波动，而可能收敛到 Marchenko–Pastur、semicircle 等分布。随机矩阵理论连接数论、量子混沌、无线通信、统计学习与神经网络。

高维概率研究 concentration of measure、随机过程上确界和非渐近误差界，为 compressed sensing、randomized algorithms 和统计估计提供统一工具。

## Topological data analysis

拓扑数据分析（topological data analysis, TDA）用形状信息研究点云和复杂数据。Persistent homology 在尺度 $r$ 变化时跟踪连通分支、环和高维洞，并把它们表示为 barcode 或 persistence diagram。

前沿问题包括多参数 persistence、统计置信度、稳定而可微的拓扑表示、动态图与时间序列，以及与神经网络的结合。TDA 已用于材料、分子、图像、机器人和气候数据，但解释性与可扩展性仍是研究重点。

## 学习理论与优化

统计学习理论研究 generalization：训练误差小为何有时能推出新数据误差小。经典工具包括 VC dimension、Rademacher complexity 与 PAC-Bayes bounds；深度网络则带来 overparameterization、implicit bias、neural tangent limits 和 feature learning 等新问题。

非凸优化在最坏情形很困难，但实际神经网络训练常能找到有效解。理解数据结构、参数化、随机梯度动力学与泛化之间的关系，是概率、优化和动力系统的交叉前沿。

## 资料

- [AMS: Topological Data Analysis session](https://meetings.ams.org/math/jmm2025/meetingapp.cgi/Session/11567)
- [AMS: Persistence Theory](https://www.ams.org/books/surv/209/)
- [数理统计](../probability_statistics/mathematical_statistics.md)与[最优化](../applied_math/optimization.md)
