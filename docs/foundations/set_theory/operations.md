---
title: 集合运算
tags:
  - 集合论
---

# 集合运算

集合运算从已有集合构造新集合：并、交、差、补、对称差、幂集、笛卡尔积。它们的本质是与逻辑联结词的一一对应（并$\leftrightarrow$或、交$\leftrightarrow$且、补$\leftrightarrow$非），这使集合等式可以用逻辑推理来验证。

## 并集与交集

**定义 1（并集）** $A$与$B$的并集是"属于$A$或属于$B$"的元素全体：

$$
A \cup B = \{x : x \in A \lor x \in B\}.
$$

**定义 2（交集）** $A$与$B$的交集是"同时属于$A$和$B$"的元素全体：

$$
A \cap B = \{x : x \in A \land x \in B\}.
$$

**例 1** 设$A = \{1, 2, 3\}$，$B = \{2, 3, 4\}$，则$A \cup B = \{1, 2, 3, 4\}$，$A \cap B = \{2, 3\}$。

Venn 图直觉：两个圆分别表示$A, B$；并集是两个圆覆盖的全部区域，交集是两圆重叠的区域。若$A \cap B = \varnothing$，称$A$与$B$ **不相交**（disjoint）。

**定义 3（族并）** 对集合族$\mathcal{F}$（以集合为成员的集合）：

$$
\bigcup \mathcal{F} = \{x : \exists A \in \mathcal{F},\, x \in A\}, \qquad
\bigcap \mathcal{F} = \{x : \forall A \in \mathcal{F},\, x \in A\}.
$$

当$\mathcal{F} = \{A_1, A_2, \dots\}$时也写$\bigcup_{i} A_i$、$\bigcap_{i} A_i$。

**例 2** $\bigcup_{n=1}^{\infty} [0, n] = [0, \infty)$；$\bigcap_{n=1}^{\infty} (0, 1/n) = \varnothing$——族运算把并、交从"两个集合"推广到"任意多个集合"。

## 差集与补集

**定义 4（差集）** $A$与$B$的差集是"属于$A$但不属于$B$"的元素全体：

$$
A \setminus B = \{x : x \in A \land x \notin B\}.
$$

**定义 5（补集）** 固定全集$U$，$A$的（相对）补集是$A^c = U \setminus A$，也记$\overline{A}$。

**例 3** $A = \{1, 2, 3\}$，$B = \{2, 3, 4\}$：$A \setminus B = \{1\}$，$B \setminus A = \{4\}$。若$U = \{1, 2, 3, 4, 5\}$，则$A^c = \{4, 5\}$。

**性质 1** $(A^c)^c = A$；$A \subseteq B \iff B^c \subseteq A^c$；$A \setminus B = A \cap B^c$。

!!! note "要点：补集是相对的"
    补集依赖所选全集$U$，离开$U$谈补集没有意义。这正是 [基本概念](basics.md) 中"全集是相对概念"的原因。

## 对称差

**定义 6（对称差）** $A$与$B$的对称差是"恰属于其中一个"的元素全体：

$$
A \triangle B = (A \setminus B) \cup (B \setminus A).
$$

**例 4** 沿用上例，$A \triangle B = \{1, 4\}$。

**性质 2（对称差的运算律）**

- $A \triangle B = (A \cup B) \setminus (A \cap B)$；
- 交换律：$A \triangle B = B \triangle A$；
- 结合律：$(A \triangle B) \triangle C = A \triangle (B \triangle C)$；
- 对$\cap$的分配律：$A \cap (B \triangle C) = (A \cap B) \triangle (A \cap C)$。

直觉：$\triangle$对应逻辑**异或**（$\oplus$）——"恰好一个成立"，因此有结合律这一异或的典型性质。

## 幂集

**定义 7（幂集）** $A$的幂集是$A$的所有子集组成的集合：

$$
\mathcal{P}(A) = \{X : X \subseteq A\}.
$$

**例 5** $\mathcal{P}(\varnothing) = \{\varnothing\}$；$\mathcal{P}(\{1, 2\}) = \{\varnothing, \{1\}, \{2\}, \{1, 2\}\}$。注意$\mathcal{P}(\varnothing) \ne \varnothing$：空集的幂集含一个元素（空集本身）。

**定理 1** 若$A$有$n$个元素（$n$有限），则$|\mathcal{P}(A)| = 2^n$。

**证明** 对$A$的每个元素，一个子集$X$中它要么出现、要么不出现，共两种选择；$n$个元素独立选择，得$2^n$个子集。等价地：映射$X \mapsto \chi_X$（特征函数）把$\mathcal{P}(A)$与$\{0, 1\}^A$一一对应，故$|\mathcal{P}(A)| = |\{0,1\}^A| = 2^n$。无限情形的推广（$|A| < |\mathcal{P}(A)|$）见 [基数与势](cardinality.md) 的 Cantor 定理。

!!! warning "易错点：$\varnothing$与$A$总是幂集元素"
    对任意$A$，$\varnothing \subseteq A$且$A \subseteq A$恒成立，故$\varnothing, A \in \mathcal{P}(A)$。此外$\varnothing \in \mathcal{P}(A)$而$\varnothing \subseteq \mathcal{P}(A)$——$\in$与$\subseteq$并存且层次不同。

## 笛卡尔积

**定义 8（有序对）** $(a, b)$称为有序对：$a$是第一分量，$b$是第二分量。有序对的相等判据是

$$
(a, b) = (c, d) \iff a = c \land b = d.
$$

（集合论中的实现：Kuratowski 有序对$(a, b) = \{\{a\}, \{a, b\}\}$，其存在性由配对公理保证，见 [zfc.md](zfc.md)。）

**定义 9（笛卡尔积）** $A$与$B$的笛卡尔积是所有有序对组成的集合：

$$
A \times B = \{(a, b) : a \in A, b \in B\}.
$$

**例 6** $A = \{1, 2\}$，$B = \{x, y\}$：$A \times B = \{(1,x), (1,y), (2,x), (2,y)\}$。

**定理 2** 有限集$A, B$：$|A \times B| = |A| \cdot |B|$。

**证明** 乘法原理：第一分量有$|A|$种选择，第二分量有$|B|$种选择，两两组合。

**性质 3（笛卡尔积的分配律）**

- $A \times (B \cup C) = (A \times B) \cup (A \times C)$；
- $A \times (B \cap C) = (A \times B) \cap (A \times C)$；
- $A \times \varnothing = \varnothing$。

一般地$A \times B \ne B \times A$（除非$A = B$或某边为空）：$(1, x) \ne (x, 1)$。

!!! note "要点：为什么需要有序对"
    集合$\{a, b\}$不区分顺序（$\{a,b\} = \{b,a\}$），而$a \ne b$时$(a,b) \ne (b,a)$。笛卡尔积的用途正是"有序"地组合元素——这是定义关系（[关系](relations.md)）与函数（[函数](functions.md)）的基础。

## 运算律一览

以下等式对任意集合$A, B, C$成立（$U$为全集，补集相对$U$）：

| 名称 | 等式 |
| --- | --- |
| 交换律 | $A \cup B = B \cup A$；$A \cap B = B \cap A$ |
| 结合律 | $(A \cup B) \cup C = A \cup (B \cup C)$；$(A \cap B) \cap C = A \cap (B \cap C)$ |
| 分配律 | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$；$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ |
| De Morgan 律 | $(A \cup B)^c = A^c \cap B^c$；$(A \cap B)^c = A^c \cup B^c$ |
| 幂等律 | $A \cup A = A$；$A \cap A = A$ |
| 吸收律 | $A \cup (A \cap B) = A$；$A \cap (A \cup B) = A$ |
| 空集与全集 | $A \cup \varnothing = A$；$A \cap \varnothing = \varnothing$；$A \cup U = U$；$A \cap U = A$ |
| 互补律 | $A \cup A^c = U$；$A \cap A^c = \varnothing$ |

!!! note "要点：这些是'同一件事'的两种写法"
    上表每一行都可以逐元素验证，也可以看作对应逻辑恒等式：如$(A \cup B)^c = A^c \cap B^c$就是$\neg(p \lor q) \iff \neg p \land \neg q$。把集合语言翻译成逻辑语言后，许多"运算律"是显然的。

## 一个典型证明：De Morgan 律

**定理 3（De Morgan 律）** 固定全集$U$：$(A \cup B)^c = A^c \cap B^c$。

**证明** 用双向包含。

- $(\subseteq)$设$x \in (A \cup B)^c$。则$x \notin A \cup B$，故$x \notin A$且$x \notin B$，即$x \in A^c$且$x \in B^c$，所以$x \in A^c \cap B^c$。
- $(\supseteq)$设$x \in A^c \cap B^c$。则$x \notin A$且$x \notin B$，故$x \notin A \cup B$，即$x \in (A \cup B)^c$。

两方向都成立，故相等。$\blacksquare$

**思路**：把"元素属于左边"翻译成关于$x$的命题，用逻辑推理（这里是命题逻辑的 De Morgan：$\neg(p \lor q) \iff \neg p \land \neg q$）完成推导，再翻译回集合语言。几乎所有集合恒等式都遵循这个模式。

## 与逻辑的对应

集合运算不过是用另一套语言写出的逻辑运算：

| 集合运算 | 逻辑联结词 |
| --- | --- |
| $\cup$ | 或$\lor$ |
| $\cap$ | 与$\land$ |
| 补$^c$ | 非$\neg$ |
| $\triangle$ | 异或$\oplus$ |
| $\subseteq$ | 蕴含$\to$ |
| 集合相等 | 双向蕴含$\leftrightarrow$ |

因此集合代数（$\cup, \cap, ^c$）构成一个**布尔代数**：逻辑恒等式逐条对应集合恒等式。这是"集合论是逻辑的几何化"这一直觉的来源。

## 延伸阅读

- [基本概念](basics.md) —— 元素、属于、子集、空集等基础概念
- [关系](relations.md) —— 笛卡尔积的子集：关系
- [函数](functions.md) —— 关系中全定义且单值的一类
- [基数与势](cardinality.md) —— 幂集与笛卡尔积在无限情形下的大小
- [符号表](../../notation/index.md) —— 数学记号速查
