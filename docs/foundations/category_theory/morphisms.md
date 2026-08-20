---
title: 态射与同构
tags:
  - 范畴论
---

# 态射、单态射、满态射与同构

态射是范畴的"过程"：结构保持的映射的抽象。本页研究态射的三类基本性质——**同构**（可逆）、**单态射**（左可消）、**满态射**（右可消）——并回答一个基本问题：这些范畴论概念在 $\mathbf{Set}$ 中对应集合论中的什么？

## 态射：范畴中的"过程"

回顾 [范畴](categories.md) 中的定义：态射 $f: A \to B$ 从对象 $A$ 指向 $B$，$A$ 是定义域，$B$ 是陪域；复合 $g \circ f$ 仅在 $\operatorname{cod}(f) = \operatorname{dom}(g)$ 时有定义；$\operatorname{id}_A$ 是复合的单位元。本页所有概念都在这一框架内定义，不依赖对象"内部"的元素。

## 集合论 vs 范畴论：函数的两种定义

本节对比两种对"函数"的看法。这是理解"为什么陪域是态射身份的一部分"的关键（内容整理自本目录早期的旧笔记）。

**集合论（ZFC）的定义**：函数 $f: A \to B$ 是序偶集合（graph）$f \subseteq A \times B$，满足：

- **完全性**（totality）：$\forall a \in A$，存在 $b \in B$ 使 $(a, b) \in f$；
- **单值性**（functionality）：若 $(a, b) \in f$ 且 $(a, b') \in f$，则 $b = b'$。

函数的值域是 $\operatorname{im}(f) = \{b \in B \mid \exists a \in A,\ (a, b) \in f\}$。

**关键后果**：在集合论中，两个函数相等当且仅当它们的 graph 相等，**与陪域无关**。例如恒等 $\operatorname{id}_{\mathbb{N}}: \mathbb{N} \to \mathbb{N}$ 与包含 $\iota: \mathbb{N} \to \mathbb{Z}$（$n \mapsto n$）有相同的 graph $\{(n, n) \mid n \in \mathbb{N}\}$，集合论中把它们视为同一个函数。

**范畴论（$\mathbf{Set}$ 中）的定义**：态射 $f: A \to B$ 的**陪域 $B$ 是态射身份的一部分**。graph 相同但陪域不同的两个箭头是**不同的态射**：$\operatorname{id}_{\mathbb{N}}: \mathbb{N} \to \mathbb{N}$ 与 $\iota: \mathbb{N} \to \mathbb{Z}$ 是 $\mathbf{Set}$ 中不同的箭头。

**为什么陪域重要**：

- **复合**：箭头只在 $\operatorname{cod}(f) = \operatorname{dom}(g)$ 时可复合。取 $g: \mathbb{Z} \to \mathbb{Z}$，$g(x) = x + 1$，则复合 $g \circ \iota: \mathbb{N} \to \mathbb{Z}$ 合法，而 $g \circ \operatorname{id}_{\mathbb{N}}$ 无定义（$\operatorname{cod}(\operatorname{id}_{\mathbb{N}}) = \mathbb{N} \neq \mathbb{Z}$）。
- **结构角色**：陪域指定"输出所在的位置"；诸如满射性一类的性质依赖指定的陪域（见下文的定理 2）。

!!! note "要点"
    在 $\mathbf{Set}$ 中，态射 $f: A \to B$ 同时编码**映射规则（graph）**与**上下文信息**（定义域 $A$、陪域 $B$）。陪域不能由 graph 推出，而是态射身份的固有部分。

## 同构

**定义 1（同构）** 态射 $f: A \to B$ 称为**同构**，若存在 $g: B \to A$ 使得
$$
g \circ f = \operatorname{id}_A, \qquad f \circ g = \operatorname{id}_B
$$
此时 $g$ 称为 $f$ 的（双侧）逆，记 $g = f^{-1}$；若存在同构 $A \to B$，称 $A$ 与 $B$ **同构**，记 $A \cong B$。

**命题 1（逆的唯一性）** 同构的逆若存在则唯一。

**证明** 设 $g, g'$ 都是 $f$ 的逆，则
$$
g = g \circ \operatorname{id}_B = g \circ (f \circ g') = (g \circ f) \circ g' = \operatorname{id}_A \circ g' = g'
$$
其中用到了结合律与单位律。$\blacksquare$

同构关系是等价关系：自反（$\operatorname{id}_A$）、对称（取逆）、传递（复合）。

**例子**：$\mathbf{Set}$ 中同构 = 双射；$\mathbf{Grp}$ 中同构 = 群同构；$\mathbf{Top}$ 中同构 = 同胚；偏序集范畴中同构 = 序同构。可见"同构"就是"结构相同"的精确说法。

## 单态射与满态射

**定义 2（单态射）** 态射 $f: A \to B$ 称为**单态射**（monomorphism），若对任意对象 $C$ 与任意 $g, h: C \to A$，
$$
f \circ g = f \circ h \implies g = h
$$
即 $f$ 满足**左可消**。

**定义 3（满态射）** 态射 $f: A \to B$ 称为**满态射**（epimorphism），若对任意对象 $C$ 与任意 $g, h: B \to C$，
$$
g \circ f = h \circ f \implies g = h
$$
即 $f$ 满足**右可消**。

直觉：

- 单态射：$f$ 不丢失"来源信息"——若两条路径在 $f$ 之后重合，则它们本就相同；
- 满态射：$f$ 的输出决定一切后续——任何在 $f$ 之后的区分都来自 $f$ 本身。

两个定义都不引用元素，因此适用于任意范畴。这正是范畴论的意义：把集合论中"单射/满射"的概念推广到没有元素概念的场合。

## 定理：$\mathbf{Set}$ 中单态射 ⟺ 单射

**定理 1（$\mathbf{Set}$ 中的单态射）** 在 $\mathbf{Set}$ 中，$f: A \to B$ 是单态射当且仅当 $f$ 是单射。

**证明**

（$\Leftarrow$）设 $f$ 单射，且 $f \circ g = f \circ h$。对任意 $c \in C$，$f(g(c)) = f(h(c))$，由单射性 $g(c) = h(c)$，故 $g = h$。

（$\Rightarrow$）反证。若 $f$ 非单射，存在 $a_1 \neq a_2$ 使 $f(a_1) = f(a_2)$。取单点集 $C = \{*\}$，定义 $g(*) = a_1$、$h(*) = a_2$，则 $f \circ g = f \circ h$ 但 $g \neq h$，与单态射矛盾。$\blacksquare$

## 定理：$\mathbf{Set}$ 中满态射 ⟺ 满射

**定理 2（$\mathbf{Set}$ 中的满态射）** 在 $\mathbf{Set}$ 中，$f: A \to B$ 是满态射当且仅当 $f$ 是满射（即 $f(A) = B$）。

**证明**（思路与论证整理自旧笔记）

（$\Leftarrow$）设 $f$ 满射，且 $g \circ f = h \circ f$。任取 $b \in B$，由满射性存在 $a \in A$ 使 $f(a) = b$。于是
$$
g(b) = g(f(a)) = h(f(a)) = h(b)
$$
由 $b$ 的任意性，$g = h$。

（$\Rightarrow$）反证。设 $f$ 非满射，则存在 $b_0 \in B$ 使对所有 $a \in A$ 都有 $f(a) \neq b_0$。取 $C = \{0, 1\}$，定义
$$
g(b) = 0 \ (\forall b \in B), \qquad h(b) = \begin{cases} 0 & b \neq b_0 \\ 1 & b = b_0 \end{cases}
$$
则对任意 $a \in A$，因 $f(a) \neq b_0$，有 $h(f(a)) = 0 = g(f(a))$，故 $g \circ f = h \circ f$；但 $g(b_0) = 0 \neq 1 = h(b_0)$，故 $g \neq h$，与满态射矛盾。$\blacksquare$

!!! note "要点"
    上述证明中"不满"是相对于**陪域** $B$ 而言的——这正是本页开头"陪域是态射身份的一部分"的用武之地：若改换陪域（例如把 $f: \mathbb{N} \to \mathbb{N}$，$n \mapsto n+1$ 换成 $f: \mathbb{N} \to \mathbb{N} \setminus \{0\}$），同一个 graph 可以从非满射变为满射。

**推论** 在 $\mathbf{Set}$ 中：单态射 ⟺ 单射，满态射 ⟺ 满射，同构 ⟺ 双射。

## 在其他范畴中：$\mathbf{Grp}$ 与 $\mathbf{Top}$

**定理 3（$\mathbf{Grp}$ 中的满态射）** 在 $\mathbf{Grp}$ 中，态射是满态射当且仅当它是满射的群同态。

说明：$\mathbf{Grp}$ 中单态射 ⟺ 单射同态是平凡的（底集函子忠实，见 [函子](functors.md)）；但"满态射 ⟺ 满射"是 $\mathbf{Grp}$ 的著名性质，**并非显然**。证明思路：若 $f: G \to H$ 不是满射，把 $H$ 沿子群 $f(G)$ 做**融合积**（amalgamated free product）$H *_{f(G)} H$，两个典范嵌入 $H \to H *_{f(G)} H$ 在 $f(G)$ 上一致、在 $H \setminus f(G)$ 上不同，从而 $f$ 不是满态射。该结果的非平凡点在于两个嵌入确实不同（可用词的正规形式证明）。$\mathbf{Ab}$ 中同理，且可用余核给出更简单的证明：若 $f$ 不满，余核 $q: B \to B / f(A)$ 满足 $q \circ f = 0 \circ f$ 但 $q \neq 0$。

**定理 4（$\mathbf{Top}$ 中的满态射）** 在 $\mathbf{Top}$ 中，满态射恰为连续满射。

**证明** 连续满射显然是满态射（底集函数右可消，加上 $\mathbf{Top} \to \mathbf{Set}$ 忠实）。反过来，若 $f: X \to Y$ 不满，取 $y_0 \notin f(X)$，把 $Y$ 的两个副本沿 $f(X)$ 粘合得到商空间 $Y \sqcup_{f(X)} Y$；两个包含 $Y \to Y \sqcup_{f(X)} Y$ 在 $f(X)$ 上一致、在 $y_0$ 处不同（$y_0 \notin f(X)$，其两个副本未被粘合），故 $f$ 不是满态射。$\blacksquare$

!!! warning "易错点"
    常有人说"拓扑空间范畴中满态射不必是满射，例如稠密子集的包含"。这个说法只对 **Hausdorff 空间范畴 $\mathbf{Haus}$** 成立：$\mathbf{Haus}$ 中的满态射恰为**具有稠密像**的连续映射，因此包含 $\mathbb{Q} \to \mathbb{R}$（$\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密）是 $\mathbf{Haus}$ 中的满态射，却不是满射。在完整的 $\mathbf{Top}$ 中，满态射就是连续满射。可见"满态射"由整个范畴决定，不能简单等同于集合意义的满射。

**单 + 满 ≠ 同构**：$\mathbb{Q} \to \mathbb{R}$ 在 $\mathbf{Haus}$ 中既是单态射（单射）又是满态射（稠密像），但不是同构（不是双射，也没有连续逆）。故"单且满"不保证同构。

## 分裂单态射与分裂满态射

**定义 4（分裂单/满态射）** 态射 $f: A \to B$：

- 称为**分裂单态射**（split mono），若存在 $r: B \to A$ 使 $r \circ f = \operatorname{id}_A$（$r$ 称为左逆或收缩）；
- 称为**分裂满态射**（split epi），若存在 $s: B \to A$ 使 $f \circ s = \operatorname{id}_B$（$s$ 称为右逆或截面）。

**命题 2** 分裂单态射必是单态射；分裂满态射必是满态射。

**证明** 若 $f \circ g = f \circ h$，则 $g = r \circ f \circ g = r \circ f \circ h = h$，故 $f$ 是单态射；满态射同理。$\blacksquare$

逆命题一般不成立：在 $\mathbf{Set}$ 中，"每个满射都是分裂满态射"以及"每个非空定义域的单射都有左逆"都等价于选择公理。

## 同构与"结构保持"

- 同构 = 存在双侧逆：两个对象在范畴的意义下"结构相同"，一切范畴论性质都被同构保持。
- 例如：若 $A \cong B$，则对任意 $C$ 有 $\operatorname{Hom}(C, A) \cong \operatorname{Hom}(C, B)$ 且 $\operatorname{Hom}(A, C) \cong \operatorname{Hom}(B, C)$（由复合诱导的双射）。这为 [Yoneda 引理](yoneda.md) 埋下伏笔：对象由它与其他对象的态射关系决定。

## 延伸阅读

- [范畴](categories.md)：范畴与态射的基本定义。
- [函子](functors.md)：函子保持并（忠实时）反映单态射与满态射。
- [泛性质与极限](universal_properties.md)：始/终对象与极限是态射泛性质的集中体现。
- [数学基础](../index.md)与[符号表](../../notation/index.md)。
