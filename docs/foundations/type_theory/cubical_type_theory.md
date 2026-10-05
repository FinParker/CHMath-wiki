---
title: 立方类型论（CuTT）
tags:
  - 类型论
  - 拓扑
---

# 立方类型论（CuTT）

> 立方类型论（Cubical Type Theory，常缩写为 CTT 或 CuTT）用显式区间维度描述路径，使函数外延性、univalence 和高阶归纳类型具有可执行的计算规则。

## 1. 为什么需要立方结构

在公理化 HoTT 中，可以向强度 Martin-Löf 类型论加入 univalence axiom，但公理本身通常不会归约。这造成一个张力：理论能够证明更多命题，闭项却未必仍能计算到预期的规范形式。

立方类型论的目标是同时保留：

- HoTT 的高维路径解释；
- univalence 与 higher inductive types；
- 典范性（canonicity）和可执行计算；
- 构造性元理论（constructive metatheory）。

其核心做法是把“路径的维度”显式加入语法。

## 2. 区间与路径

**定义 1（区间，interval）** 立方类型论引入形式区间 $\mathbb I$，带两个端点 $0,1:\mathbb I$。区间变量常写作 $i,j:\mathbb I$。

**定义 2（路径类型，path type）** 对可能依赖区间变量的类型族 $A(i)$，若 $a_0:A(0)$、$a_1:A(1)$，则

$$
\operatorname{PathP}(A,a_0,a_1)
$$

的项可看成一个区间函数 $p(i):A(i)$，并满足端点条件

$$
p(0)=a_0,\qquad p(1)=a_1.
$$

当 $A$ 不依赖 $i$ 时，写作 $\operatorname{Path}_A(a_0,a_1)$ 或 $a_0\equiv a_1$。路径抽象和应用分别类似

$$
\langle i\rangle t
\qquad\text{与}\qquad
p\,r.
$$

这里 $r$ 是维度表达式。路径因而是可以在端点求值的对象，而不只是一个无归约规则的归纳类型项。

## 3. 面公式与立方体

多个区间变量形成方形、立方体和更高维立方体：

$$
(i,j)\in\mathbb I^2,
\qquad
(i,j,k)\in\mathbb I^3.
$$

约束 $i=0$、$j=1$ 描述立方体的面。**面格**（face lattice）用这些约束的合取与析取描述部分边界。

CCHM 立方类型论采用带连接和反转的 De Morgan interval；Cartesian cubical systems 强调 weakening、exchange、contraction 对维度同样可用，因而允许对角线。不同 CuTT 在区间代数和 composition 的具体形式上有所不同，但共同目标是让边界填充成为计算操作。

## 4. Kan composition 与填充

**定义 3（composition operation）** 给定一个开放盒（open box）的若干面以及缺失面的目标方向，composition operation 计算缺失面的值。相应的 filling operation 构造整个填充立方体。

从同伦角度看，这对应 Kan filling condition；从类型论角度看，它提供：

- 路径复合与路径逆；
- 依赖路径上的 transport；
- 依赖函数和依赖对的路径结构；
- 高维边界的一致填充。

在 Cubical Agda 中，核心操作常分解为：

- `transp`：沿类型路径运输；
- `hcomp`：homogeneous composition；
- `hfill`：构造 composition 对应的填充。

## 5. Glue type 与可计算的 univalence

**定义 4（Glue type）** Glue 是一种沿面公式把一个类型与另一个等价类型粘合起来的类型构造。它让等价能够被提升为宇宙中的路径，同时保留端点的计算行为。

**定理 1（可计算的同伦等价，computational univalence）** 在适当的立方类型论中，univalence 可由 Glue 构造证明，并且沿该路径的 transport 会计算为给定等价的正向函数。

这比仅把 univalence 声明为常量更强：univalence 参与程序求值，因而可以与 normalization 和 canonicity 一起研究。

## 6. 高阶归纳类型的计算

圆周可以直接声明点构造子和路径构造子：

```agda
data S¹ : Type where
  base : S¹
  loop : base ≡ base
```

在 cubical setting 中，匹配 `loop i` 时可以对维度变量 $i$ 进行计算。类似机制支持 suspension、pushout、propositional truncation 等 higher inductive types。

## 7. CCHM 与 Cartesian Cubical Computational Type Theory

“CuTT”不是唯一固定系统的专名，下面两条主要路线也不穷尽所有 cubical systems；阅读文献时必须确认作者采用的 cube category、interval algebra 与 composition operations。

### 7.1 CCHM Cubical Type Theory

Cyril Cohen、Thierry Coquand、Simon Huber 与 Anders Mörtberg 提出的系统基于 cubical set model 和 De Morgan cube category。它构造性地验证 function extensionality 与 univalence，并讨论圆周和命题截断等 HIT。

### 7.2 Cartesian Cubical Computational Type Theory

Angiuli、Hou (Favonia) 与 Harper 的 Cartesian Cubical Computational Type Theory 使用 Cartesian cubes，并以 operational/computational semantics 为中心。其 two-level 版本同时包含：

- fibrant types：支持路径与 univalence；
- non-fibrant types：支持满足 equality reflection 的严格等同。

该系统证明了布尔类型的 canonicity：闭布尔项会求值为 `true` 或 `false`。

## 8. 与普通等同类型的差别

| 强度 MLTT | 立方类型论 |
| --- | --- |
| equality 由 `refl` 归纳生成 | path 由区间函数表示 |
| $J$ 是主要消去器 | 路径应用、transport、composition 是基本操作 |
| univalence 常作为公理加入 | univalence 可具有计算规则 |
| HIT 的计算规则较难表达 | 路径构造子可对维度计算 |

不同 cubical system 仍可能同时保留一个 inductive identity type；因此阅读实现文档时要确认 `Path` 与 `Id` 是否为同一个概念。

## 9. Cubical Agda

Agda 的 cubical mode 实现的是 **CCHM 路线的一个变体**，并非 Cartesian Cubical Computational Type Theory 的直接实现。它把 CCHM 的 Kan composition 分解为 homogeneous composition 与 generalized transport。最小入口为：

```agda
{-# OPTIONS --cubical #-}

open import Cubical.Core.Everything
```

官方 `agda/cubical` 库包含 univalence、HIT、同伦群和大量 univalent mathematics 的形式化结果。实践时应让 Agda 版本与 cubical library 的兼容版本保持一致。

## 10. 参考资料

- Cyril Cohen、Thierry Coquand、Simon Huber、Anders Mörtberg, [*Cubical Type Theory: A Constructive Interpretation of the Univalence Axiom*](https://doi.org/10.4230/LIPIcs.TYPES.2015.5)：CCHM cubical type theory 的核心论文。
- Carlo Angiuli、Kuen-Bang Hou (Favonia)、Robert Harper, [*Cartesian Cubical Computational Type Theory*](https://doi.org/10.4230/LIPIcs.CSL.2018.6)：Cartesian CuTT 与 two-level computational semantics。
- [Agda Cubical 官方文档](https://agda.readthedocs.io/en/latest/language/cubical.html)：interval、Path、transport、composition 与 Glue 的实现说明。
- [agda/cubical](https://github.com/agda/cubical)：Cubical Agda 标准研究库及课程资料。

## 延伸阅读

- [同伦类型论](homotopy_type_theory.md)：univalence 与 higher inductive types
- [类型论](index.md)：等同类型、宇宙与典范性
- [Lambda Cube](lambda_cube.md)：CuTT 之前的依赖类型系统分类
