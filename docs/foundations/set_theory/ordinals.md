---
title: 序数
tags:
  - 集合论
---

# 序数

序数（ordinal number）度量**良序的长度**。基数回答"集合有多大"（见 [基数与势](cardinality.md)），序数回答"排在第几位、排了多长"。von Neumann 的天才构造让序数本身就是集合，从而把"长度"纳入集合论的宇宙。

## 良序回顾

**定义 1（良序）** 全序$(A, <)$是良序，若$A$的每个非空子集都有最小元。

**例 1** $(\mathbb{N}, <)$、$(\{0, 1, 2\}, <)$是良序；$(\mathbb{Z}, <)$、$(\mathbb{R}, <)$不是（$\mathbb{Z}$无最小元；$(0, 1) \subseteq \mathbb{R}$无最小元）。

**定义 2（序同构）** 良序$(A, <)$与$(B, <)$序同构，若存在保序双射$f: A \to B$（$a_1 < a_2 \Rightarrow f(a_1) < f(a_2)$）。

**定理 1（比较定理）** 任意两个良序可以比较：必有一个与另一个的真前段序同构。这是"良序的长度可比"的精确表述，也是序数理论的起点。

## von Neumann 序数

核心思想：**让序数$\alpha$恰好等于"所有比$\alpha$小的序数"组成的集合**：

$$
\alpha = \{\beta : \beta \text{ 是序数} \land \beta < \alpha\}.
$$

**定义 3（传递集）** 集合$x$是传递的（transitive），若$y \in x \Rightarrow y \subseteq x$（$x$的每个元素都是$x$的子集）。

**定义 4（序数）** 传递集$\alpha$称为（von Neumann）序数，若$(\alpha, \in)$是良序。

**例 2**

- $0 = \varnothing$：传递，且空集按$\in$是（平凡）良序；
- $1 = \{\varnothing\}$，$2 = \{\varnothing, \{\varnothing\}\}$，一般$n + 1 = n \cup \{n\}$；
- $\omega = \{0, 1, 2, \dots\}$：所有有限序数的集合（存在性由 [zfc.md](zfc.md) 的无穷公理保证），是最小的无限序数。

**定理 2（序数基本性质）**

1. 序数的元素都是序数；
2. $\alpha = \{\beta : \beta \text{ 是序数} \land \beta \in \alpha\}$；
3. 序数按$\in$全序：任意两个序数$\alpha, \beta$，$\alpha \in \beta$、$\alpha = \beta$、$\beta \in \alpha$恰有一个成立；
4. 所有序数的收集$\mathrm{On}$不是集合（Burali-Forti 悖论，见下文），而是真类。

**记号** 约定$\alpha < \beta \iff \alpha \in \beta$。于是序数就是"由更小序数组成的良序集"，每个序数$\alpha$恰好有$\alpha$个前驱——"第$\alpha$个长度由更短的长度构成"，递归地建立一切。

!!! note "要点：长度 = 集合"
    von Neumann 的洞见：不必发明额外的"长度"对象，直接让长度$\alpha$就是集合$\{\beta : \beta < \alpha\}$。由此$\alpha$的元素个数就是$|\alpha| = \alpha$的势，"$\alpha$有$\alpha$个前驱"字面成立。

## 后继与极限序数

**定义 5（后继序数）** 序数$\alpha$的后继是$\alpha + 1 = \alpha \cup \{\alpha\}$，它是大于$\alpha$的最小序数。非零且形如$\beta + 1$的序数称为后继序数。

**定义 6（极限序数）** 非零且不是后继序数的序数称为极限序数。$\omega$是最小的极限序数。

**例 3** $1 = 0 + 1$，$2 = 1 + 1$，$\dots$都是后继序数；$\omega = \bigcup_{n < \omega} n$是极限序数；$\omega + 1$是后继序数；$\omega \cdot 2$（即$\omega + \omega$）、$\omega^2$都是极限序数。

!!! note "要点：三种序数形态"
    序数分为三种形态：$0$、后继序数、极限序数。超限归纳的三情形（基步/后继步/极限步，见下节）正与这三种形态一一对应；极限步的存在是超限归纳区别于普通归纳的本质。

**序数算术（简述）** 由超限递归定义（见下节）：

$$
\alpha + 0 = \alpha, \qquad \alpha + (\beta + 1) = (\alpha + \beta) + 1, \qquad \alpha + \lambda = \bigcup_{\beta < \lambda} (\alpha + \beta) \; (\lambda \text{ 极限});
$$

乘法、幂类似地递归。

!!! warning "易错点：序数加法不交换"
    $1 + \omega = \omega$（在$\omega$长链**前面**接一个元素仍是$\omega$长），而$\omega + 1 > \omega$（在$\omega$长链**后面**再接一个元素更长）。故$1 + \omega \ne \omega + 1$。序数是"顺序"的量而不是"数量"的量——这正是它与基数算术的根本区别（见 [基数与势](cardinality.md)）。

## 超限归纳与递归

**定理 3（超限归纳原理）** 设$P$是关于序数的性质。若对每个序数$\alpha$，

$$
(\forall \beta < \alpha\, P(\beta)) \Rightarrow P(\alpha),
$$

则$P(\alpha)$对一切序数$\alpha$成立。

**证明** 若存在反例，取最小的反例$\alpha$（序数按$\in$良序，反例的收集若有元素必有最小元）。则所有$\beta < \alpha$满足$P(\beta)$，由假设得$P(\alpha)$，矛盾。$\blacksquare$

**等价形式（三情形归纳）** 归纳步骤可拆为：

1. **基步**：$P(0)$；
2. **后继步**：$P(\alpha) \Rightarrow P(\alpha + 1)$；
3. **极限步**：$(\forall \beta < \lambda\, P(\beta)) \Rightarrow P(\lambda)$（$\lambda$极限）。

**定理 4（超限递归定义）** 若$F$是"以序数为参数、由先前值决定"的规则，则存在唯一的序列$x_\alpha$（$\alpha \in \mathrm{On}$）满足递归方程。（序数加法、von Neumann 层级$V_\alpha$的定义都由它保证合法。）

**例 4（超限递归的应用）**

- **von Neumann 层级**：$V_0 = \varnothing$，$V_{\alpha+1} = \mathcal{P}(V_\alpha)$，$V_\lambda = \bigcup_{\alpha < \lambda} V_\alpha$（$\lambda$极限）。由正则公理，每个集合都出现在某个$V_\alpha$中（见 [zfc.md](zfc.md)）——集合论宇宙是分层累积的；
- **序数算术**：本节开头的加法、乘法由超限递归定义；
- **$\aleph$阶梯**：$\aleph_{\alpha+1}$与极限$\aleph_\lambda$由超限递归定义（见 [基数与势](cardinality.md)）。

!!! note "要点：数学归纳法是特例"
    普通数学归纳法是超限归纳在$\omega$上的情形（没有极限步）。超限归纳把归纳法从$\mathbb{N}$推广到任意良序；而良序定理（见下文）保证在 ZFC 中**每个**集合都能沿某个良序被归纳。

## 序数与基数

**定义 7（基数）** 集合$A$的基数$|A|$是与$A$等势的最小序数（在 ZFC 中良序定理保证这样的序数存在）。

序数与基数共享同样的集合：$\omega$与$\aleph_0$是同一个集合，只是角色不同——$\aleph_0$强调"大小"，$\omega$强调"次序"。

**例 5** $|\omega| = \aleph_0$；$|\omega + 1| = \aleph_0$；$|\omega \cdot 2| = \aleph_0$——序数$\omega + 1$、$\omega \cdot 2$都比$\omega$长，但元素个数相同（在无限链后面接有限段或接一段$\omega$都不改变大小）。"序数讲顺序、基数讲大小"在这里一目了然。序数之间比较用$\in$（$\alpha < \beta \iff \alpha \in \beta$），基数之间比较用单射存在性（见 [基数与势](cardinality.md)）。

## 良序定理

**定理 5（Zermelo 良序定理, 1904）** 每个集合都可以被良序化。

良序定理与选择公理在 ZF 中等价：Zermelo 1904 年从 AC 推出良序定理（这是 AC 的第一次应用，也是其争论的开端），反之良序定理显然蕴含 AC（沿良序取最小元即可构造选择函数）。因此良序定理是 ZF 的独立命题：接受 AC 则成立，否则存在不可良序化的集合。

!!! note "要点：良序定理的用途"
    良序定理是超限归纳与超限递归的"通行证"：它让任意集合上的构造（例如证明每个向量空间有基）都能沿良序进行。等价性与应用详见 [选择公理](axiom_of_choice.md)。

## Burali-Forti 悖论

**悖论（Burali-Forti, 1897）** 假设所有序数组成一个集合$\mathrm{On}$。$\mathrm{On}$传递（序数的元素是序数）且按$\in$良序，故由定义 4，$\mathrm{On}$自身是一个序数。于是$\mathrm{On} \in \mathrm{On}$，即$\mathrm{On} < \mathrm{On}$，矛盾。

**出路** 与 Russell 悖论同理（见 [基本概念](basics.md)）：$\mathrm{On}$不是集合，而是**真类**——"太大而不能成为集合"的收集。ZFC 中没有"一切序数的集合"，但"小于$\alpha$的序数全体"是集合，而且就是$\alpha$自己。

!!! note "要点：集合与真类"
    类（class）是比集合更宽松的收集概念；ZFC 只允许由公理保证的收集成为集合。$\mathrm{On}$（所有序数）与$V$（所有集合）都是真类。区分"集合"与"真类"是公理化集合论的关键纪律，详见 [ZFC 公理系统](zfc.md)。

## 良序的序型：每个良序都"是"一个序数

**定理 6（良序表示定理）** 每个良序$(A, <)$与唯一的序数序同构。该序数称为$A$的序型，记$\operatorname{ot}(A)$。

**证明思路** 沿良序$(A, <)$超限递归地定义$f(a)$为"不在$\{f(b) : b < a\}$中的最小序数"。递归不可能永不终止：否则由替换公理（见 [zfc.md](zfc.md)）得到与$\mathrm{On}$序同构的集合，与 Burali-Forti 悖论矛盾。终止于某个序数$\alpha$时，$f$是$A \to \alpha$的序同构；唯一性由比较定理（定理 1）。$\blacksquare$

**例 6** $\operatorname{ot}(\{0, 1, 2\}, <) = 3$；$\operatorname{ot}(\mathbb{N}, <) = \omega$。若把$\mathbb{N}$重排为"偶数全部在前、奇数全部在后"（$0 < 2 < 4 < \cdots < 1 < 3 < 5 < \cdots$），序型是$\omega \cdot 2$——同一个集合，不同的良序给出不同的序型。

## 可数序数与第一个不可数序数

所有可数序数的收集$\omega_1 = \{\alpha : |\alpha| = \aleph_0\}$本身是序数且不可数，称为**第一个不可数序数**，$|\omega_1| = \aleph_1$。它的存在性由替换公理保证（可数良序的序型构成一个集合）。$\omega_1$是极限序数。

**例 7** $\omega + 1$、$\omega \cdot 2$、$\omega^2$、$\omega^{\omega}$都是可数序数——可数个可数序数之上仍是可数序数；$\omega_1$是"所有可数序数之上"的第一个不可数序数。连续统假设（见 [基数与势](cardinality.md)）问的正是$2^{\aleph_0}$是否等于$\aleph_1$。

!!! note "要点：$\aleph$的阶梯由序数给出"
    $\aleph_{\alpha+1}$定义为大于$\aleph_\alpha$的最小基数，极限时$\aleph_\lambda = \sup_{\beta < \lambda} \aleph_\beta$——没有序数理论就没有$\aleph$的阶梯。基数以序数为骨架，这是"序数先于基数"的结构性原因。

## 延伸阅读

- [基数与势](cardinality.md) —— 序数的"大小"版本：基数与$\aleph_\alpha$
- [关系](relations.md) —— 良序的定义、全序与 Hasse 图
- [ZFC 公理系统](zfc.md) —— 无穷公理、替换公理与序数的存在性
- [选择公理](axiom_of_choice.md) —— 良序定理与 AC 等价
- [数学基础](../index.md) —— 数学基础章节导览
