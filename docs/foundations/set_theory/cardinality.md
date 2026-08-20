---
title: 基数与势
tags:
  - 集合论
---

# 基数与势

势（基数）衡量集合的"大小"。有限集合按元素个数比较；Cantor 的重大发现是：**无限集合也有大小，而且大小有无穷多层**。本页建立等势、可数性、不可数性，并给出对角线论证与 Cantor 定理这两个核心工具。

## 等势

**定义 1（等势）** 集合$A$与$B$等势（equinumerous），记$A \sim B$或$|A| = |B|$，若存在双射$f: A \to B$。

**例 1**

- $\mathbb{N} \sim \mathbb{Z}$：交错列举$0, -1, 1, -2, 2, \dots$（$f(n) = n/2$若$n$偶，$f(n) = -(n+1)/2$若$n$奇）；
- $\mathbb{N} \sim \{0, 2, 4, \dots\}$：$n \mapsto 2n$；
- $\mathbb{N} \sim \mathbb{Q}$：见下文定理 2。

!!! note "要点：等势是等价关系"
    $A \sim A$（恒等映射）、$A \sim B \Rightarrow B \sim A$（逆映射）、$A \sim B \sim C \Rightarrow A \sim C$（复合，见 [函数](functions.md)）。势就是等势类共享的"大小"。

## 有限与无限

**定义 2（有限/无限/可数无限）**

- $A$有限：存在$n \in \mathbb{N}$与双射$A \to \{0, 1, \dots, n-1\}$，此时$|A| = n$；
- $A$无限：不是有限；
- $A$可数无限：$|A| = |\mathbb{N}|$。

**定义 3（Dedekind 无限）** $A$是 Dedekind 无限的，若$A$与它的某个真子集等势。

**例 2** $\mathbb{N}$与偶数集$\{0, 2, 4, \dots\}$等势——无限集的标志性现象：可与自身真子集等势。有限集则不可能（抽屉原理：$n$个对象放进$n$个位置必须占满）。

!!! note "要点：两种'无限'的关系"
    在 ZFC 中，"无限"与"Dedekind 无限"等价（无限集必含可数子集，可用最小元显式选取）。在 ZF 中（不用选择公理）二者可能分离：存在 Dedekind 有限但无限的集合与 ZF 相容（见 [选择公理](axiom_of_choice.md)）。

## 可数集

**定义 4（可数）** $A$可数（countable）：$A$有限或$|A| = \aleph_0$。记$\aleph_0$（读作"阿列夫零"）为自然数集的势：$\aleph_0 = |\mathbb{N}|$。

**定理 1** 可数集的有限并、可数并、有限积、子集、有限个可数集的积仍可数。

**定理 2** $\mathbb{Q}$可数：$|\mathbb{Q}| = \aleph_0$。

**证明思路（Cantor 之字形列举）** 把正有理数写成既约分数$m/n$，按分母分子之和$m + n$分组：和$= 2$的组$\{1/1\}$，和$= 3$的组$\{1/2, 2/1\}$，和$= 4$的组$\{1/3, 2/2, 3/1\}$，……组内按$m$从小到大（既约性保证每个正有理数恰出现一次）。这给出$\mathbb{N}$与正有理数的双射，再穿插$0$与负有理数即可。等价地：$\mathbb{Q}$是$\mathbb{Z} \times \mathbb{Z}$的可数子集的像，而$\mathbb{Z} \times \mathbb{Z}$可数（定理 1）。

!!! note "要点：可数的直觉"
    可数集就是"能排成一列"的集合：$a_0, a_1, a_2, \dots$。有理数比自然数"稠密得多"，但依然能排成一列——"稠密"是序性质，"可数"是大小性质，二者无关。

## 不可数集与 Cantor 对角线论证

**定理 3（Cantor）** $\mathbb{R}$不可数。

**证明（对角线论证）** 只需证$[0, 1]$不可数。设$f: \mathbb{N} \to [0, 1]$是任意函数，构造一个不在值域中的实数。把$f(n)$写成十进制小数$0.d_{n1}d_{n2}d_{n3}\cdots$，令$x = 0.c_1 c_2 c_3 \cdots$，其中

$$
c_n = \begin{cases} 5, & d_{nn} \ne 5, \\ 4, & d_{nn} = 5. \end{cases}
$$

即$c_n$取一个既不是$d_{nn}$也不是$9$的数字。则$x \in [0, 1]$，且对每个$n$，$x$与$f(n)$在第$n$位不同；由于$c_n$刻意不取$9$，这不涉及$0.4999\cdots = 0.5000\cdots$式的表示歧义。故$x \notin \operatorname{ran} f$，$f$不是满射。$\blacksquare$

**推论 1** $|\mathbb{N}| < |\mathbb{R}|$，记$|\mathbb{R}| = \mathfrak{c}$（连续统的势，continuum）。

!!! warning "易错点：小数表示的歧义"
    $0.5000\cdots = 0.4999\cdots$，对角线构造必须避开"尾数全 9"的歧义（本证明的策略是$c_n \in \{4, 5\}$），否则构造出的$x$可能只是与某个$f(n)$表示不同而数值相同。

## Cantor 定理

**定理 4（Cantor）** 对任意集合$A$：$|A| < |\mathcal{P}(A)|$。即不存在从$A$到$\mathcal{P}(A)$的满射。

**证明** 单射存在（$a \mapsto \{a\}$），只需证无满射。设$f: A \to \mathcal{P}(A)$任意，构造**对角集**

$$
B = \{x \in A : x \notin f(x)\}.
$$

若$f$是满射，则$B = f(b)$对某个$b \in A$。于是

$$
b \in B \iff b \notin f(b) \iff b \notin B,
$$

矛盾。故$f$非满射。$\blacksquare$

**思路** 把$x$与"$x$的像$f(x)$是否含$x$"排成一张清单，$B$通过"取反"与清单每一行都不同——这是实数对角线论证的抽象版，把"第$n$位取反"推广为"$x \notin f(x)$"。

**推论 2** $\aleph_0 < 2^{\aleph_0} < 2^{2^{\aleph_0}} < \cdots$——势的层级永无止境。

**定理 5** $|\mathbb{R}| = |\mathcal{P}(\mathbb{N})| = 2^{\aleph_0}$。

**证明思路** 用 CBS 定理（下）两个方向各造一个单射：

- $\mathcal{P}(\mathbb{N}) \hookrightarrow \mathbb{R}$：把$X \subseteq \mathbb{N}$映到三进制小数$0.c_0 c_1 c_2 \cdots$，其中$c_n = 2$若$n \in X$，否则$c_n = 0$（只出现数字 0 与 2，无歧义），是单射；
- $\mathbb{R} \hookrightarrow \mathcal{P}(\mathbb{N})$：实数由 Dedekind 割（$\mathbb{Q}$的子集）唯一确定，而$\mathbb{Q}$可数，$\mathcal{P}(\mathbb{Q}) \sim \mathcal{P}(\mathbb{N})$。$\blacksquare$

## Cantor–Bernstein–Schroeder 定理

**定理 6（CBS 定理）** 若存在单射$f: A \to B$与单射$g: B \to A$，则存在双射$h: A \to B$。

**证明** 思路：$A$中有一部分元素"追溯不到$B$的像"，从那里出发交替应用$g \circ f$生成长链，把$A$分成两块：一块沿$f$走，另一块沿$g^{-1}$走。

令$A_0 = A \setminus g(B)$（"没有$B$来源"的元素），递归$A_{n+1} = g(f(A_n))$，$A^* = \bigcup_{n=0}^{\infty} A_n$。定义

$$
h(a) = \begin{cases} f(a), & a \in A^*, \\ g^{-1}(a), & a \notin A^*. \end{cases}
$$

$g^{-1}(a)$有意义：$a \notin A^*$蕴含$a \notin A_0$，故$a \in g(B)$，而$g$单射保证原像唯一。

- **满射**：设$b \in B$。若$g(b) \in A^*$，则$g(b) \in A_n$（$n \ge 1$），由$A_n = g(f(A_{n-1}))$得$b = f(a)$对某$a \in A_{n-1} \subseteq A^*$，故$b = h(a)$；若$g(b) \notin A^*$，则$b = h(g(b))$。
- **单射**：若$a_1, a_2$同在$A^*$或同在$A^*$之外，由$f$或$g^{-1}$的单射性即得$a_1 = a_2$。若$a_1 \in A^*$、$a_2 \notin A^*$而$f(a_1) = g^{-1}(a_2)$，则$g(f(a_1)) = a_2$；但$a_1 \in A_n$给出$g(f(a_1)) \in A_{n+1} \subseteq A^*$，与$a_2 \notin A^*$矛盾。$\blacksquare$

**意义** 比较大小只需在两个方向各构造一个单射——这是最实用的大小比较工具（定理 5 正是这样完成的）。

!!! note "要点：CBS 不需要选择公理"
    $h$的构造是显式的（$g^{-1}$由单射性唯一确定，$A^*$由递归确定），因此 CBS 在 ZF 中成立。它把"存在双射"归结为"两个方向都有单射"，让等势的验证变得容易。

## 基数算术

**定义 5（基数运算）** 对基数$\kappa = |A|$、$\lambda = |B|$：

$$
\kappa + \lambda = |A \sqcup B| \quad (\text{不相交并}), \qquad
\kappa \cdot \lambda = |A \times B|, \qquad
\kappa^{\lambda} = |A^B|.
$$

**例 3** $\aleph_0 + \aleph_0 = \aleph_0$，$\aleph_0 \cdot \aleph_0 = \aleph_0$（$\mathbb{Q}$可数）；$\mathfrak{c} \cdot \mathfrak{c} = \mathfrak{c}$，因为$(2^{\aleph_0})^2 = 2^{\aleph_0 \cdot 2} = 2^{\aleph_0}$，即$|\mathbb{R} \times \mathbb{R}| = |\mathbb{R}|$。

!!! warning "易错点：无限基数的算术不同于有限"
    对无限基数，$\kappa + \lambda = \max\{\kappa, \lambda\}$，$\kappa \cdot \lambda = \max\{\kappa, \lambda\}$，但幂$\kappa^{\lambda}$可能严格更大。$2^{\aleph_0}$到底多大，正是连续统假设的问题。

## 连续统假设

**定义 6（连续统假设, CH）** 不存在基数$\kappa$使得$\aleph_0 < \kappa < 2^{\aleph_0}$。等价地，$2^{\aleph_0} = \aleph_1$，其中$\aleph_1$是大于$\aleph_0$的最小基数（其存在由 ZFC 中的良序保证，见 [序数](ordinals.md)）。**广义连续统假设（GCH）**：对一切序数$\alpha$，$2^{\aleph_\alpha} = \aleph_{\alpha+1}$。

**定理 7（CH 的独立性）** CH（以及 GCH）在 ZFC 中**不可判定**：

- **Gödel（1938/1940）**：若 ZFC 一致，则 ZFC + GCH 一致（在可构造宇宙$L$中 GCH 成立）；
- **Cohen（1963）**：用**力迫法**证明 ZFC + ¬CH 一致（可构造$2^{\aleph_0} \ge \aleph_2$的模型）。

因此 CH 既不真也不假于 ZFC——它是 ZFC 的独立命题，$2^{\aleph_0}$的值不由 ZFC 决定。

!!! note "要点：CH 的地位"
    CH 自 1878 年 Cantor 提出以来一直是数学基础的核心问题。独立性结果并非说 CH"无法知道"，而是说 ZFC 的公理不足以裁决它。选择公理在 ZF 中的独立性是同一套力迫方法的成果（见 [选择公理](axiom_of_choice.md)）。

## 延伸阅读

- [函数](functions.md) —— 单射/满射/双射与像、原像
- [序数](ordinals.md) —— $\aleph_\alpha$的严格定义与超限归纳
- [ZFC 公理系统](zfc.md) —— 幂集公理与无穷公理：势的存在性
- [选择公理](axiom_of_choice.md) —— 基数比较与 AC 的关系
- [数学基础](../index.md) —— 数学基础章节导览
