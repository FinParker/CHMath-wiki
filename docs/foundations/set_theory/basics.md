---
title: 集合的基本概念
tags:
  - 集合论
---

# 集合的基本概念

集合是数学中最基本的概念之一：它把"一些确定对象的整体"作为对象本身来研究。本页建立集合的语言（属于、子集、空集、表示法），并通过 Russell 悖论说明为什么最终需要公理化（见 [ZFC 公理系统](zfc.md)）。

## 从朴素直觉出发

Cantor 在 1895 年给出集合的朴素定义："把我们的直观或思维中的一些确定的、彼此有区别的对象看成一个整体，便称为一个集合。" 这个定义直观，但"整体"与"对象"都没有严格界定。现代数学不再定义"集合是什么"，而是用公理规定哪些收集是集合、哪些运算合法（见 [zfc.md](zfc.md)）。本页先建立直觉与记号。

!!! note "要点：集合是原始概念"
    在 ZFC 中，"集合"与"属于"（$\in$）是仅有的原始概念，其余一切（数、函数、序、空间）都最终归结为集合。因此本页的许多"定义"其实是在描述直觉，严格的依据在 zfc.md。

## 元素与属于关系

**定义 1（元素与属于）** 若对象$a$是集合$A$的一个成员，称$a$属于$A$，记$a \in A$；否则记$a \notin A$。

朴素集合的三个直观约定：

- **确定性**：对任意对象$a$与集合$A$，$a \in A$与$a \notin A$恰有一个成立；
- **互异性**：集合中的元素不重复计数；
- **无序性**：集合中的元素没有先后顺序。

**例 1** $\{1,2,3\}$、$\{3,1,2\}$、$\{1,1,2,3\}$三个写法表示同一个集合。

!!! note "要点：$\in$与$\subseteq$的区别"
    $a \in A$表示"元素$a$属于集合$A$"；$A \subseteq B$表示"集合$A$的每个元素都属于$B$"。例如$\{1\} \in \{\{1\}, 2\}$成立，而$1 \in \{\{1\}, 2\}$不成立——元素与集合是两个层次的对象。

## 外延公理：相等由元素决定

**公理 1（外延公理）** 两个集合相等，当且仅当它们有完全相同的元素：

$$
A = B \iff \forall x\, (x \in A \leftrightarrow x \in B).
$$

直观地说，集合由它的元素**唯一决定**——与书写方式、元素排列顺序、重复次数都无关。

**推论 1** 若$A \subseteq B$且$B \subseteq A$，则$A = B$。

这给出证明集合相等的标准方法——**双向包含**：先证$A \subseteq B$，再证$B \subseteq A$。

**例 2** $\{x \in \mathbb{R} : x^2 = 1\} = \{-1, 1\}$；$\{n \in \mathbb{N} : n \text{ 是偶数}\} = \{0, 2, 4, \dots\}$。同一集合可以有不同的描述方式，外延公理保证它们相等。

## 子集与真子集

**定义 2（子集）** 若$A$的每个元素都是$B$的元素，称$A$是$B$的子集，记$A \subseteq B$：

$$
A \subseteq B \iff \forall x\, (x \in A \to x \in B).
$$

**定义 3（真子集）** 若$A \subseteq B$且$A \ne B$，称$A$是$B$的真子集，记$A \subsetneq B$。

**性质 1（子集关系）** 对任意集合$A, B, C$：

- 自反性：$A \subseteq A$；
- 传递性：$A \subseteq B \land B \subseteq C \Rightarrow A \subseteq C$；
- 外延性：$A \subseteq B \land B \subseteq A \Rightarrow A = B$。

!!! warning "易错点：$\subset$记号的分歧"
    不同教材中$\subset$含义不同：有的表示子集（允许相等），有的表示真子集。本 wiki 统一用$\subseteq$表示子集、$\subsetneq$表示真子集，不使用有歧义的$\subset$。

## 空集

**定义 4（空集）** 不含任何元素的集合称为空集，记$\varnothing$（或$\emptyset$）。

**定理 1（空集唯一）** 空集是唯一的。

**证明** 设$\varnothing_1, \varnothing_2$都是空集。由"空真"论证，$\varnothing_1 \subseteq \varnothing_2$且$\varnothing_2 \subseteq \varnothing_1$（"$\varnothing$的每个元素都属于另一个集合"是空真的命题），由外延公理$\varnothing_1 = \varnothing_2$。

**性质 2** 对任意集合$A$，$\varnothing \subseteq A$恒成立；$\varnothing$是"包含"关系下的最小集合。

!!! warning "易错点：$\varnothing$与$\{\varnothing\}$不是一回事"
    $\varnothing$没有元素；$\{\varnothing\}$有一个元素（即$\varnothing$）。二者不同：$\varnothing \ne \{\varnothing\}$；$\varnothing \in \{\varnothing\}$且$\varnothing \subseteq \{\varnothing\}$，但$\{\varnothing\} \nsubseteq \varnothing$。注意$\subseteq$与$\in$在此同时成立，却表达不同的层次。

## 全集

**定义 5（全集）** 在某个具体讨论中，把所涉及的一切对象装进去的集合称为全集，常记$U$。

全集是**相对的**：讨论自然数时$U = \mathbb{N}$，讨论实数时$U = \mathbb{R}$。补集等运算（见 [集合运算](operations.md)）都相对所选的全集而言。

!!! warning "不存在'一切集合的全集'"
    若存在包含一切集合的集合$U$，则由分离公理可构造$\{x \in U : x \notin x\}$，重演 Russell 悖论（见下文）。因此"所有集合的集合"在 ZFC 中不是集合，而是**真类**。

## 常见数集

| 记号 | 名称 | 说明 |
| --- | --- | --- |
| $\mathbb{N}$ | 自然数集 | 本 wiki 约定含$0$（见下方要点） |
| $\mathbb{Z}$ | 整数集 | $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$ |
| $\mathbb{Q}$ | 有理数集 | $\mathbb{Q} = \{m/n : m, n \in \mathbb{Z}, n \ne 0\}$ |
| $\mathbb{R}$ | 实数集 | 有理数的完备化（Dedekind 割） |
| $\mathbb{C}$ | 复数集 | $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$ |

这些数集形成包含链

$$
\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C},
$$

每一步都是上一步的扩张：自然数添加负元得整数，整数作比得有理数，有理数完备化得实数，实数添加虚数单位$i$得复数。这条链的起点$\mathbb{N}$在 ZFC 中由无穷公理构造（见 [zfc.md](zfc.md)）。

!!! note "要点：$\mathbb{N}$是否含 0"
    不同教材约定不同。本 wiki 采用$\mathbb{N} = \{0, 1, 2, \dots\}$；需要排除 0 时写$\mathbb{N}^+$或$\mathbb{N} \setminus \{0\}$，避免歧义。

## 集合的表示法

1. **列举法**：把元素逐一列出，如$\{1, 2, 3\}$、$\{a, b, c\}$。适合元素少且有明确写法的集合。
2. **描述法**：用性质刻画元素，$\{x \in A : P(x)\}$表示"$A$中满足性质$P$的元素全体"，也记$\{x \in A \mid P(x)\}$。

描述法是列举法的推广：区间$[0, 1] = \{x \in \mathbb{R} : 0 \le x \le 1\}$无法列举，只能用性质刻画。

!!! warning "易错点：无限制的描述法$\{x : P(x)\}$是危险的"
    朴素概括原则"对任意性质$P$，$\{x : P(x)\}$都是集合"会导致 Russell 悖论。公理化集合论用**分离公理模式**修正：只能从已有集合$A$中分离出$\{x \in A : P(x)\}$，不能凭空定义集合（详见 [zfc.md](zfc.md)）。

## 证明集合相等的标准模式

集合相等（$A = B$）通常分两步：

1. 任取$x \in A$，推出$x \in B$，得$A \subseteq B$；
2. 任取$x \in B$，推出$x \in A$，得$B \subseteq A$。

**例 3** 证明$A \cap (A \cup B) = A$（吸收律，见 [集合运算](operations.md)）：

- $x \in A \cap (A \cup B) \Rightarrow x \in A$，故$\subseteq$；
- $x \in A \Rightarrow x \in A$且$x \in A \cup B$，故$x \in A \cap (A \cup B)$，得$\supseteq$。

双向包含是集合论中最常用的一招，几乎所有集合等式都这样证。

**例 4** 证明$A \subseteq A \cup B$（并集定义见 [集合运算](operations.md)）：任取$x \in A$，由"或"的定义$x \in A \cup B$，故$A \subseteq A \cup B$。注意这里只需一个方向的包含——"子集"只需单向论证，而"相等"必须双向。

## Russell 悖论与公理化动机

**悖论（Russell, 1901/1902）** 考虑"所有不含自身的集合"组成的收集$R = \{x : x \notin x\}$。问：$R \in R$是否成立？

- 若$R \in R$，由$R$的定义（$R$中的元素都不含自身），应有$R \notin R$，矛盾；
- 若$R \notin R$，则$R$满足"$x \notin x$"，按定义应属于$R$，即$R \in R$，矛盾。

两种情形都导出矛盾，说明$\{x : x \notin x\}$不是集合——朴素概括原则失效。

!!! note "要点：悖论的意义"
    Russell 悖论（以及 Cantor 悖论、Burali-Forti 悖论，后者见 [序数](ordinals.md)）表明"任何性质都定义集合"不能成立。现代数学的出路是**公理化集合论**：不再试图定义"集合是什么"，而是用一组公理（ZFC）规定集合的合法构造，把$\{x : x \notin x\}$这类对象排除在集合之外。整个 ZFC 系统的动机与内容见 [ZFC 公理系统](zfc.md)。

## 延伸阅读

- [集合运算](operations.md) —— 由给定集合构造新集合的运算与运算律
- [关系](relations.md) —— 元素之间的联系与序结构
- [ZFC 公理系统](zfc.md) —— 公理化集合论：集合论的严格基础
- [数学基础](../index.md) —— 数学基础章节导览
- [符号表](../../notation/index.md) —— 数学记号速查
