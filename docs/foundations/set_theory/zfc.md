---
title: ZFC 公理系统
tags:
  - 集合论
---

# ZFC 公理系统

ZFC（Zermelo–Fraenkel 集合论 + 选择公理）是现代数学的标准基础。它不再试图定义"集合是什么"，而是用一组公理规定**哪些收集是集合、哪些构造合法**，从而避开朴素集合论的悖论。本页逐一列出并解释十条公理，并用 ZFC 构造自然数。

## 为什么需要公理化

朴素集合论允许"任意性质定义一个集合"（朴素概括原则），Russell 悖论（见 [基本概念](basics.md)）与 Burali-Forti 悖论（见 [序数](ordinals.md)）表明这条原则自相矛盾。公理化方案的回答是：

> **集合只能由公理允许的构造产生。** 分离公理、并集公理、幂集公理、替换公理等，每一条都是对"某种构造合法"的许可；不属于任何构造的收集（如$\{x : x \notin x\}$）就不是集合。

ZFC 的选择保证了：全部主流数学（数、分析、代数、拓扑）都能在其中展开，而 Russell 类、$\mathrm{On}$类被排除在集合之外。

## 形式语言

ZFC 是一阶谓词逻辑中的理论：

- 唯一非逻辑符号是二元谓词$\in$；$=$是逻辑符号（带等词的一阶逻辑）；
- 一切数学对象都是集合，没有"原子对象"（urelement）——数、函数、序数最终都是集合；
- $\subseteq$、$\varnothing$、$\{a, b\}$、$(a, b)$等是定义出的缩写。

**公理模式（schema）**：下面第 6、9 条是"模式"——对每个一阶公式$\varphi$给出一条公理，因此各代表**无穷多条**公理。

!!! note "要点：公理 vs 公理模式"
    分离与替换无法用单条公理表达（它们要涵盖"所有可能的性质$\varphi$"，而性质由一阶公式给出，无穷多），所以是模式。这是 ZFC 语言能力的关键来源。

## 十条公理

### 1. 外延公理（Extensionality）

$$
\forall x\, \forall y\, \big( \forall z\, (z \in x \leftrightarrow z \in y) \to x = y \big).
$$

**含义**：集合由元素唯一决定——元素相同的两个集合相等。**作用**：使"集合相等"成为可验证的性质；空集唯一、$\{a,b\}$唯一等。

### 2. 空集公理（Empty Set）

$$
\exists x\, \forall y\, (y \notin x).
$$

**含义**：存在不含任何元素的集合。**注**：它可由无穷公理 + 分离模式推出，但习惯上仍单列。

### 3. 配对公理（Pairing）

$$
\forall a\, \forall b\, \exists c\, \forall x\, \big( x \in c \leftrightarrow (x = a \lor x = b) \big).
$$

**含义**：任意$a, b$构成集合$\{a, b\}$；取$a = b$得单点集$\{a\}$。**作用**：有序对（Kuratowski 有序对$(a,b) = \{\{a\}, \{a,b\}\}$）由此存在，进而笛卡尔积存在。

### 4. 并集公理（Union）

$$
\forall \mathcal{F}\, \exists A\, \forall x\, \big( x \in A \leftrightarrow \exists Y \in \mathcal{F}\, (x \in Y) \big).
$$

**含义**：对集合族$\mathcal{F}$，并$A = \bigcup \mathcal{F}$存在。**注**：配对公理只给出二元并（如$A \cup B = \bigcup\{A, B\}$），并集公理把并推广到任意族（见 [集合运算](operations.md)）。

### 5. 幂集公理（Power Set）

$$
\forall a\, \exists P\, \forall x\, (x \in P \leftrightarrow x \subseteq a).
$$

**含义**：$P = \mathcal{P}(a)$存在。**作用**：函数空间、$2^A = \{0,1\}^A$、实数构造（Dedekind 割是$\mathbb{Q}$的子集）都依赖它；与无穷公理配合得到不可数集（见 [基数与势](cardinality.md)）。

### 6. 分离公理模式（Separation / Aussonderung）

对每个公式$\varphi(x, p_1, \dots, p_n)$：

$$
\forall A\, \forall p_1 \cdots \forall p_n\, \exists B\, \forall x\, \big( x \in B \leftrightarrow (x \in A \land \varphi(x, p_1, \dots, p_n)) \big).
$$

**含义**：从已有集合$A$中"筛选"出满足$\varphi$的元素，$B = \{x \in A : \varphi(x)\}$。**这是对朴素概括原则的修正**：概括必须限制在已有集合之内。Russell 类$\{x : x \notin x\}$无法写成$\{x \in A : x \notin x\}$吗？可以写，但对任意$A$这个集合都等于$\varnothing$的一部分——矛盾需要的是"不借助$A$的概括"，而这被禁止了。

!!! warning "易错点：分离公理不创造新元素"
    分离只能从$A$中筛选，不能"长出"新集合。要得到比$A$更大的对象，必须借助并、幂、替换等构造公理。这是朴素概括原则与公理化之间的本质差别。

### 7. 无穷公理（Infinity）

$$
\exists X\, \big( \varnothing \in X \land \forall y \in X\, (y \cup \{y\} \in X) \big).
$$

**含义**：存在一个包含$\varnothing$且对"后继$y \mapsto y \cup \{y\}$"封闭的集合。**作用**：保证$\mathbb{N} = \omega$存在——没有它，任何构造都只能得到有限集合。

### 8. 正则公理（Foundation / Regularity）

$$
\forall x\, \big( x \ne \varnothing \to \exists y \in x\, (y \cap x = \varnothing) \big).
$$

**含义**：每个非空集合都有一个与自身不相交的元素（$\in$-极小元）。**推论**：

- 不存在$x \ni x$（否则$\{x\}$无$\in$-极小元）；
- 不存在无限下降的$\in$链$x_0 \ni x_1 \ni x_2 \ni \cdots$；
- 每个集合都出现在 von Neumann 层级$V_\alpha$中（$V_0 = \varnothing$，$V_{\alpha+1} = \mathcal{P}(V_\alpha)$，极限序数时取并）——集合论宇宙是"分层累积"的。

### 9. 替换公理模式（Replacement）

对每个公式$\varphi(x, y, p_1, \dots, p_n)$：

$$
\forall A\, \forall p_1 \cdots \forall p_n\, \Big( \forall x \in A\, \exists! y\, \varphi(x, y, p_1, \dots, p_n) \to \exists B\, \forall y\, \big( y \in B \leftrightarrow \exists x \in A\, \varphi(x, y, p_1, \dots, p_n) \big) \Big).
$$

**含义**：若$\varphi$在$A$上定义了一个（类）函数，则它的值域$B$是集合——"把$A$中每个元素换成另一个对象，结果仍是集合"。**作用**：得到可数并$\bigcup_{n} A_n$、超限递归的每一步取值、序数$\omega + \omega$等的存在性，这些是分离模式做不到的（分离只能筛选，不能"扩张"）。

!!! note "要点：分离与替换的关系"
    在并集公理等配合下，分离模式可由替换模式推出（$B = \{x \in A : \varphi(x)\} = \bigcup \{\{x\} : x \in A \land \varphi(x)\}$，其中花括号集合由配对给出，并由并集公理完成）。但分离作为独立公理更清楚地表达了"限制概括"的思想，故仍单列。

### 10. 选择公理（Axiom of Choice）

$$
\forall \mathcal{F}\, \Big( \forall A \in \mathcal{F}\, (A \ne \varnothing) \to \exists f\, \big( \operatorname{dom} f = \mathcal{F} \land \forall A \in \mathcal{F}\, (f(A) \in A) \big) \Big).
$$

**含义**：非空集合族存在**选择函数**——同时从每个成员中挑一个元素。**等价形式**：良序定理、Zorn 引理、Tychonoff 定理等（详见 [选择公理](axiom_of_choice.md)）。

!!! warning "易错点：选择公理是非构造性的"
    选择函数的存在不给出"如何挑选"的规则。对无穷族，通常不存在显式的选择函数——这正是 AC 的争议根源。凡能用显式规则（如取最小元、取唯一元素）完成的选取，都不需要 AC。

## 由公理推出的基本事实

- **有序对与笛卡尔积**：Kuratowski 有序对$(a, b) = \{\{a\}, \{a, b\}\}$（配对公理）；$A \times B \subseteq \mathcal{P}(\mathcal{P}(A \cup B))$（并 + 幂集 + 分离）。
- **函数**：$f: A \to B$是$A \times B$的特殊子集，函数空间$B^A \subseteq \mathcal{P}(A \times B)$是集合（见 [函数](functions.md)）。
- **关系**：$A \times B$的子集（见 [关系](relations.md)）。
- **自然数**：见下节。
- **序数与超限递归**：无穷公理给出$\omega$，替换公理给出$\omega + \omega$、$\aleph_\alpha$等（见 [序数](ordinals.md)）。

## 用 ZFC 构造自然数

**定义（von Neumann 自然数）** 递归：

$$
0 = \varnothing, \quad 1 = \{0\}, \quad 2 = \{0, 1\}, \quad \dots, \quad n + 1 = n \cup \{n\}.
$$

每个自然数$n$就是"所有小于$n$的自然数"组成的集合。无穷公理保证所有$n$的全体$\omega = \{0, 1, 2, \dots\}$是集合（否则只能得到每个单独的自然数，得不到"自然数全体"）。

**定理（Peano 公理成为定理）** 在$(\omega, S)$上，其中后继函数$S(n) = n \cup \{n\}$：

1. $S$是$\omega \to \omega$的单射，且$0 \notin \operatorname{ran} S$；
2. 归纳原理：若$X \subseteq \omega$满足$0 \in X$且$n \in X \Rightarrow S(n) \in X$，则$X = \omega$。

**证明思路** 单射性：$S(m) = S(n)$即$m \cup \{m\} = n \cup \{n\}$，用$\in$的良基性（正则公理）排除$m \ne n$的情形。归纳原理是"$\omega$是传递良序集"的直接推论。$\blacksquare$于是数学归纳法、递归定义（加法、乘法）在 ZFC 内成为**定理**而非公设——算术被还原为集合论。

!!! note "要点：自然数也是序数"
    von Neumann 自然数同时是序数（见 [序数](ordinals.md)）：$n < m \iff n \in m$。有限时"基数角色"与"序数角色"重合；无限时二者分道扬镳（$\omega$与$\aleph_0$是同一集合的两种角色）。

## 选择公理属于 ZFC 吗？

约定有分歧，本 wiki 采用：

> **ZF = 公理 1–9（含分离、替换两个模式），ZFC = ZF + 选择公理。**

有的书把选择公理列为 ZFC 的第十条公理，而把"不含选择"的系统称为 ZF；也有的书把 ZF 定义为含选择。无论哪种写法，"C" 都指 Choice（选择）。

!!! note "要点：何时需要 AC"
    凡涉及"无穷多个任意选择"的证明通常需要 AC：每个向量空间有基、紧致空间的任意乘积紧致（Tychonoff）、不可测集的存在等。凡能显式给出规则（取最小元、取唯一元素）的证明不需要。详见 [选择公理](axiom_of_choice.md)。

## 元数学：ZFC 能做什么、不能做什么

- **一致性与不完备**：若 ZFC 一致，则它不能证明自身的一致性（Gödel 第二不完备定理）。数学共同体普遍假定 ZFC 一致，并认为它足以描述全部主流数学。
- **独立命题**：CH 与 GCH 独立于 ZFC（Gödel + Cohen，见 [基数与势](cardinality.md)）；AC 独立于 ZF（见 [选择公理](axiom_of_choice.md)）。
- **定位**：ZFC 是"默认框架"而非"唯一真理"。构造性数学、类型论提供替代基础，但大多数数学实践在 ZFC（或其温和扩张）内进行。

## 延伸阅读

- [基本概念](basics.md) —— Russell 悖论与朴素集合论
- [序数](ordinals.md) —— 无穷公理与替换公理的应用；Burali-Forti 悖论
- [选择公理](axiom_of_choice.md) —— 第十条公理的等价形式与独立性
- [基数与势](cardinality.md) —— 幂集公理与无穷公理的"大小"后果
- [数学基础](../index.md) —— 数学基础章节导览
