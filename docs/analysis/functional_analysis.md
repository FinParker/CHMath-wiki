---
title: 泛函分析
tags: [分析, 泛函分析]
---

# 泛函分析

> 泛函分析（functional analysis）把函数看作无限维向量，研究赋范空间、算子与收敛。它连接偏微分方程、量子力学和优化。

## Banach 与 Hilbert 空间

完备赋范空间称为 Banach 空间（Banach space）。带内积且在内积诱导范数下完备的空间称为 Hilbert 空间（Hilbert space）。典型例子包括 $\ell^p$、$L^p$、连续函数空间 $C(K)$；其中 $\ell^2$ 和 $L^2$ 是 Hilbert 空间。

Hilbert 空间中的投影定理（projection theorem）说明，闭凸集中的最佳逼近存在且唯一；对闭子空间尤其得到正交分解。

## 有界线性算子

线性映射 $T:X\to Y$ 连续当且仅当存在 $C$ 使 $\|Tx\|\le C\|x\|$。最小的 $C$ 是算子范数

$$\|T\|=\sup_{\|x\|\le1}\|Tx\|.$$

连续线性泛函组成对偶空间 $X^*$。Hahn–Banach 定理（Hahn–Banach theorem）允许在保持范数的同时延拓泛函。

## 三个基本定理

- 一致有界原理（uniform boundedness principle）；
- 开映射定理（open mapping theorem）；
- 闭图像定理（closed graph theorem）。

它们都依赖 Banach 空间的完备性，并常用 Baire 类定理证明。

## 谱理论

有限维的特征值理论在无限维推广为谱（spectrum）。对 Hilbert 空间上的有界自伴算子，谱定理（spectral theorem）把算子表示成“连续版本的对角化”。紧算子的非零谱则保持类似矩阵的离散结构。

## 资料

- [MIT OCW: Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2009/)：涵盖 Hahn–Banach、对偶、Hilbert 空间与谱定理。
- [测度论](measure_theory.md)：$L^p$ 空间的基础。
- [线性代数](../algebra/linear/index.md)：有限维原型。
