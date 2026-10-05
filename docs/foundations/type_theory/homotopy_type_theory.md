---
title: 同伦类型论
tags:
  - 类型论
  - 拓扑
---

# 同伦类型论

> 同伦类型论（Homotopy Type Theory, HoTT）把类型看成空间、项看成点、等同证明看成路径，并以 univalence 将“等价的结构可以相互替换”提升为基础原则。

## 1. 等同类型的高维解释

在强度 Martin-Löf 类型论中，对 $x,y:A$ 有等同类型

$$
x=_A y.
$$

HoTT 采用下面的同伦解释（homotopical interpretation）：

| 类型论 | 同伦理论 |
| --- | --- |
| 类型 $A$ | 空间或 $\infty$-群胚 |
| 项 $x:A$ | 空间中的点 |
| $p:x=_A y$ | 从 $x$ 到 $y$ 的路径 |
| $\operatorname{refl}_x$ | 常值路径 |
| $p=q$ | 路径之间的同伦 |
| 函数 $f:A\to B$ | 连续映射的类型论对应物 |

等同证明不必是无结构的“证书”。两个点之间可以有多条不同路径，两条路径之间还可以有二维路径，如此无限延伸。这正是高阶群胚结构。

## 2. Path induction

等同类型的消去原则称为 **path induction**，也记作 $J$ eliminator。若要证明

$$
\prod_{x,y:A}\prod_{p:x=y}C(x,y,p),
$$

只需对每个 $x:A$ 构造

$$
c(x):C(x,x,\operatorname{refl}_x).
$$

由 path induction 可以定义路径逆 $p^{-1}:y=x$、路径复合 $p\mathbin{\cdot}q:x=z$，并证明相应的单位律和结合律。结合律本身通常是一个更高路径，而不是定义相等。

## 3. 函数与等价

**定义 1（可收缩类型，contractible type）** 类型 $A$ 可收缩，如果存在中心 $a:A$，且每个 $x:A$ 都有路径 $a=x$：

$$
\operatorname{isContr}(A)
\;\equiv\;
\sum_{a:A}\prod_{x:A}(a=x).
$$

**定义 2（等价，equivalence）** 函数 $f:A\to B$ 是等价，如果它的每个 homotopy fiber

$$
\operatorname{fib}_f(b)\equiv\sum_{a:A}(f(a)=b)
$$

都是可收缩的。记类型等价为 $A\simeq B$。

等价比“存在双向函数”更强，因为它还携带两个方向互为逆的同伦数据。对集合层次的类型，这一概念退化为通常的双射。

## 4. Univalence

对任意路径 $p:A=_\mathcal U B$，沿路径运输可得到一个等价

$$
\operatorname{idtoequiv}_{A,B}:(A=B)\to(A\simeq B).
$$

**公理 1（同伦等价公理，univalence axiom）** 映射 $\operatorname{idtoequiv}_{A,B}$ 本身是一个等价。直观地说：

$$
(A=_\mathcal U B)\simeq(A\simeq B).
$$

Univalence 并非说“等价类型在元语言中严格相等”，而是说宇宙中的等同类型具有与等价类型相同的结构。因此，任何对类型定义的性质都能沿等价运输。

**推论 1（函数外延性，function extensionality）** 在含 univalence 的 HoTT 中，逐点相等的函数相等：

$$
\left(\prod_{x:A}f(x)=g(x)\right)\to(f=g).
$$

**结构同一原则**（structure identity principle）进一步表达：适当定义的数学结构若同构，则它们在相应结构类型中相等。这样“同构对象不可区分”成为可在理论内部使用的原则。

## 5. 同伦层级

**定义 3（截断层级，homotopy level / truncation level）** 类型按其等同类型的复杂程度分层：

| 层级 | 名称 | 条件 |
| --- | --- | --- |
| $-2$ | 可收缩类型（contractible type） | 恰有一个点，连同唯一性路径 |
| $-1$ | 命题（mere proposition） | 任意两个项相等 |
| $0$ | 集合（set） | 任意两个项之间的等同类型是命题 |
| $1$ | 群胚型（groupoid type） | 等同类型是集合 |
| $n$ | $n$-type | 等同类型是 $(n-1)$-type |

在这个术语中，“集合”是一种类型的性质，而不是所有数学对象的唯一基础形态。高于集合层级的类型保留非平凡的路径信息。

## 6. 高阶归纳类型

**定义 4（高阶归纳类型，higher inductive type, HIT）** HIT 除了点构造子，还允许路径构造子以及更高路径构造子。

圆周 $S^1$ 可以由两个构造子生成：

$$
\mathsf{base}:S^1,
\qquad
\mathsf{loop}:\mathsf{base}=\mathsf{base}.
$$

它的递归原则说：要定义 $f:S^1\to X$，只需给出一个点 $x:X$ 和一条环路 $p:x=x$。这与拓扑中从圆周映出的函数由基点与基本环路控制的直觉一致。

常见 HIT 还包括 suspension、pushout、truncation 和 quotient。它们让拓扑构造直接成为类型构造。

## 7. 基本群的示例

HoTT 中可以证明

$$
\pi_1(S^1)\cong\mathbb Z.
$$

证明使用 encode–decode method：把 $S^1$ 上的路径编码为整数，再证明编码与解码互逆。与传统代数拓扑相比，这个证明完全发生在类型论内部，路径归纳和 univalence 参与构造覆盖族。

## 8. HoTT、Univalent Foundations 与证明助理

**同伦类型论**侧重类型及其高维等同结构；**单价基础**（Univalent Foundations, UF）强调以 univalence 为核心的数学基础方案。二者经常并称，但侧重点不同。

在普通强度类型论中把 univalence 作为公理加入时，它未必带来直接的归约规则。项可以在逻辑上存在，却不能由内核计算到规范形式。[立方类型论](cubical_type_theory.md)通过 interval、path type 与 composition operation 为 univalence 提供计算意义。

## 9. 常见误解

1. HoTT 不是“把拓扑定理翻译成程序”的单一技巧，而是一套基础语言。
2. 路径不是预先存在的外部拓扑路径；它由等同类型的规则给出，同伦模型解释其几何意义。
3. Univalence 识别的是**等价**类型，不是任意存在双向函数的类型。
4. “所有类型都是集合”会抹去高阶路径；HoTT 刻意不默认 uniqueness of identity proofs (UIP)。
5. 命题截断 $\lVert A\rVert$ 只保留 $A$ 是否有项的信息，不提供从中任意提取见证的能力。

## 10. 参考资料

- The Univalent Foundations Program, [*Homotopy Type Theory: Univalent Foundations of Mathematics*](https://homotopytypetheory.org/book/)：HoTT 的标准开放教材。
- Homotopy Type Theory community, [HoTT Book resources](https://homotopytypetheory.org/book/)：PDF、勘误与持续更新版本。
- Martín Escardó, [*Introduction to Univalent Foundations of Mathematics with Agda*](https://arxiv.org/abs/1911.00580)：用 Agda 形式化展开 univalent mathematics。

## 延伸阅读

- [类型论](index.md)：$\Pi$/$\Sigma$ 类型、等同类型与宇宙
- [立方类型论](cubical_type_theory.md)：可计算的路径与 univalence
- [范畴逻辑与类型论](../category_theory/categorical_logic.md)：从群胚语义到高维语义
- [拓扑空间](../../topology/topological_spaces.md)：经典拓扑语言
