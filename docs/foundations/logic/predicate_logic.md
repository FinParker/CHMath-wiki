---
title: 谓词逻辑
tags:
  - 数理逻辑
---

# 谓词逻辑

[命题逻辑](propositional_logic.md)把"苏格拉底会死"当作一个不可再分的原子命题，因此无法表达"凡人皆死"这种涉及**个体**与**性质**的普遍陈述，也解释不了三段论"凡人皆死；苏格拉底是人；所以苏格拉底会死"为什么必然有效。谓词逻辑（又称一阶逻辑，first-order logic）把命题拆开：**个体**（对象）与**谓词**（性质、关系），并用**量词**刻画"所有"与"存在"。现代数学的公理系统（如 ZFC 集合论）几乎全部建立在一阶逻辑之上，因此一阶逻辑常被称为"数学的公共语言"。

## 从命题逻辑到谓词逻辑

把上述三段论符号化：设 $M(x)$ 表示"$x$ 会死"，$H(x)$ 表示"$x$ 是人"，$s$ 表示苏格拉底。三段论的形式是

$$
\forall x\,(H(x) \rightarrow M(x)),\quad H(s) \quad \therefore \quad M(s).
$$

这个推理的有效性依赖"所有"（$\forall$）对个体结构的分析，在命题逻辑中无法表达。这正是命题逻辑需要扩展为谓词逻辑的根本动机。

## 谓词与个体词

**定义 1（个体与谓词）** 被谈论的具体对象（人、数、集合……）称为**个体**（individual），用个体变元 $x, y, z, \dots$ 表示；具体个体用**常量符号**（如 $s$）表示。表示"个体具有某种性质"或"若干个体之间具有某种关系"的符号称为**谓词**（predicate）。

- **一元谓词**描述性质：$P(x)$ 读作"$x$ 具有性质 $P$"，如 $P(x)$：$x$ 是素数；
- **二元及多元谓词**描述关系：$R(x, y)$ 读作"$x$ 与 $y$ 具有关系 $R$"，如 $R(x, y)$：$x < y$。

**例 1** 设论域为整数。$P(x)$：$x$ 是偶数；$R(x, y)$：$x$ 整除 $y$。则 $P(4)$ 为真，$P(5)$ 为假，$R(2, 6)$ 为真，$R(3, 2)$ 为假。

把 $P(x)$ 中的 $x$ 换成具体个体 $c$ 得到 $P(c)$，仍是一个命题。**谓词本身没有真值**，只有把变元代之以个体、或用量词约束之后，表达式才有真假。

## 量词

**定义 2（全称量词与存在量词）** 设论域（domain）$D$ 非空：

- **全称量词** $\forall$：$\forall x\,P(x)$ 表示"对 $D$ 中**每一个** $x$，$P(x)$ 为真"；
- **存在量词** $\exists$：$\exists x\,P(x)$ 表示"$D$ 中**存在**（至少有一个）$x$，$P(x)$ 为真"。

**例 2** 论域取实数集 $\mathbb{R}$：

- $\forall x\,(x^2 \ge 0)$ 为真；
- $\exists x\,(x^2 = -1)$ 为假（在 $\mathbb{R}$ 中）；
- $\forall x\,(x^2 = 4)$ 为假（并非每个实数的平方都是 4）；
- $\exists x\,(x^2 = 4)$ 为真。

!!! note "要点：真值依赖论域"
    同一公式在不同论域下真假可以不同：$\exists x\,(x^2 = 2)$ 在有理数域 $\mathbb{Q}$ 中为假，在 $\mathbb{R}$ 中为真。因此讨论量词公式的真值必须先指明论域。常写 $\forall x \in S\,P(x)$ 表示"$S$ 中所有 $x$ 满足 $P$"，其精确含义是 $\forall x\,(x \in S \rightarrow P(x))$；相应地 $\exists x \in S\,P(x)$ 意为 $\exists x\,(x \in S \land P(x))$。

**唯一性量词** $\exists!$ 表示"存在**唯一**的 $x$"：$\exists! x\,P(x)$ 可定义为 $\exists x\,\big(P(x) \land \forall y\,(P(y) \rightarrow y = x)\big)$。

## 自由变元、约束变元与辖域

**定义 3（辖域、约束与自由）** 量词 $\forall x$ 或 $\exists x$ 之后紧跟的公式称为该量词的**辖域**（scope，通常延伸到括号结束）。变元 $x$ 出现在量词 $\forall x$ 或 $\exists x$ 之内时称为**约束出现**（bound occurrence），相应的变元称为**约束变元**；不在任何量词辖域内的出现称为**自由出现**（free occurrence），相应的变元称为**自由变元**。

**例 3** 在公式 $\exists x\,(P(x) \land Q(y))$ 中：$x$ 的两次出现都是约束的，$y$ 是自由变元。在 $\forall x\,P(x) \rightarrow Q(x)$ 中（$\rightarrow$ 优先级最低，故它读作 $(\forall x\,P(x)) \rightarrow Q(x)$），$P$ 里的 $x$ 是约束的，$Q$ 里的 $x$ 是自由的。

**定义 4（句子）** 不含自由变元的公式称为**句子**（sentence，闭公式）。句子的真值不依赖变元的取值，可以直接谈论"为真/为假"；带自由变元的**开公式**必须给定变元赋值才有真值。

!!! warning "易错点：同名变元的冲突"
    一个公式中同一个字母可以既有自由出现又有约束出现（如例 3 第二个公式）。为避免歧义，可把约束变元**换名**（$\alpha$-等价）：$\forall x\,P(x)$ 与 $\forall y\,P(y)$ 是同一个公式的两种写法，只要新变元不与原公式中的自由变元冲突。

## 一阶语言

一阶逻辑的**语言**（language）由两部分组成：固定的**逻辑符号**（变元、联结词、量词、等号、括号）与可选的**非逻辑符号**（该语言特有的常量、函数、关系）。

**定义 5（一阶语言 $\mathcal{L}$ 的符号集）** 语言 $\mathcal{L}$ 由下列非逻辑符号组成：

- **常量符号**：$c_0, c_1, \dots$（表示特定个体）；
- **函数符号**：$f_0, f_1, \dots$，每个函数符号带有**元数**（arity，自变量的个数）；
- **关系符号**：$R_0, R_1, \dots$，每个关系符号也带有元数；零元关系符号就是命题符号。

**定义 6（项）** 项的归纳定义：

1. 变元与常量符号都是项；
2. 若 $t_1, \dots, t_n$ 是项，$f$ 是 $n$ 元函数符号，则 $f(t_1, \dots, t_n)$ 是项；
3. 项恰由 1、2 有限次生成。

项表示"个体"，如 $f(x, c)$；项本身没有真值。

**定义 7（公式）** 公式的归纳定义：

1. 若 $t_1, t_2$ 是项，则 $t_1 = t_2$ 是（原子）公式；若 $R$ 是 $n$ 元关系符号且 $t_1, \dots, t_n$ 是项，则 $R(t_1, \dots, t_n)$ 是（原子）公式；
2. 若 $\varphi, \psi$ 是公式，则 $\lnot\varphi$、$\varphi \land \psi$、$\varphi \lor \psi$、$\varphi \rightarrow \psi$、$\varphi \leftrightarrow \psi$ 是公式；
3. 若 $\varphi$ 是公式，$x$ 是变元，则 $\forall x\,\varphi$、$\exists x\,\varphi$ 是公式；
4. 公式恰由 1–3 有限次生成。

**例 4（常见一阶语言）**

- **自然数算术语言** $\mathcal{L}_{\mathrm{ar}} = \{0, S, +, \cdot, <\}$：常量 $0$、一元函数 $S$（后继）、二元函数 $+$ 与 $\cdot$、二元关系 $<$。"任何自然数都有后继"写作 $\forall x\,\exists y\,(y = S(x))$；
- **集合论语言** $\mathcal{L}_{\in} = \{\in\}$：只有二元关系 $\in$。ZFC 的全部公理都是这个语言的一阶句子（见下文）；
- **群论语言** $\mathcal{L}_{\mathrm{g}} = \{e, \cdot\}$：常量 $e$ 与二元函数 $\cdot$。

## 量词的否定

**定理 1（量词 De Morgan 律）** 对任意公式 $\varphi(x)$：

$$
\lnot \forall x\,\varphi(x) \equiv \exists x\,\lnot\varphi(x), \qquad
\lnot \exists x\,\varphi(x) \equiv \forall x\,\lnot\varphi(x).
$$

"并非所有 $x$ 都满足 $\varphi$"等价于"存在 $x$ 不满足 $\varphi$"；"不存在 $x$ 满足 $\varphi$"等价于"所有 $x$ 都不满足 $\varphi$"。把 $\lnot$ 移过量词时，量词翻转。

**例 5** 设论域为人，$L(x)$：$x$ 喜欢逻辑。"并非所有人都喜欢逻辑" 等价于 "存在一个人不喜欢逻辑"：$\lnot\forall x\,L(x) \equiv \exists x\,\lnot L(x)$。

**例 6** 反复应用可处理多个量词：$\lnot\forall x\,\exists y\,R(x, y) \equiv \exists x\,\forall y\,\lnot R(x, y)$。每移过一个量词，$\forall$ 与 $\exists$ 互换一次。

## 量词辖域的扩张与收缩

若变元 $x$ 在公式 $\psi$ 中**不自由出现**，则量词可以从 $\psi$ 中"提取出来"或"放进去"而不改变真值，例如：

$$
\forall x\,(\varphi(x) \land \psi) \equiv \forall x\,\varphi(x) \land \psi, \qquad
\exists x\,(\varphi(x) \lor \psi) \equiv \exists x\,\varphi(x) \lor \psi.
$$

量词与 $\land$、$\lor$ 还有部分分配关系：$\forall x\,(\varphi \land \psi) \equiv \forall x\,\varphi \land \forall x\,\psi$ 与 $\exists x\,(\varphi \lor \psi) \equiv \exists x\,\varphi \lor \exists x\,\psi$ 成立；但 $\forall x\,\varphi \lor \forall x\,\psi \Rightarrow \forall x\,(\varphi \lor \psi)$ 只在一个方向成立，一般不可逆。

**定理 2（量词交换）** 同类量词可交换：$\forall x\,\forall y\,\varphi \equiv \forall y\,\forall x\,\varphi$，$\exists x\,\exists y\,\varphi \equiv \exists y\,\exists x\,\varphi$。异类量词**不可**交换：$\forall x\,\exists y\,\varphi$ 与 $\exists y\,\forall x\,\varphi$ 一般不等价。

**例 7** 设论域为自然数 $\mathbb{N}$，$\varphi(x, y)$ 为 $x < y$：

- $\forall x\,\exists y\,(x < y)$："每个数都有比它大的数"——真；
- $\exists y\,\forall x\,(x < y)$："存在一个数大于一切数"——假。

顺序颠倒，真值改变。量词的次序是语义信息的一部分。

## 前束范式

**定义 8（前束范式）** 若公式形如

$$
Q_1 x_1\, Q_2 x_2\, \cdots\, Q_n x_n\, \varphi,
$$

其中每个 $Q_i$ 是 $\forall$ 或 $\exists$，且 $\varphi$ 是**无量词**公式，则称该公式为**前束范式**（prenex normal form）：一串量词（**前束词**）后跟一个无量词部分（**母式**）。

**定理 3（前束范式存在）** 每个一阶公式都逻辑等价于某个前束范式。

**证明思路（构造算法）**

1. 用 $p \rightarrow q \equiv \lnot p \lor q$、$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$ 消去 $\rightarrow$ 与 $\leftrightarrow$；
2. 用命题 De Morgan 律、双重否定律与量词 De Morgan 律（定理 1）把 $\lnot$ 向内移到原子公式之前；
3. 必要时对约束变元换名，避免量词移动时"捕获"自由变元；
4. 用辖域的扩张与收缩律，把量词依次提到整个公式的最前面。

**例 8** 求 $\lnot(\forall x\,P(x) \rightarrow \exists y\,Q(y))$ 的前束范式：

$$
\begin{aligned}
\lnot(\forall x\,P(x) \rightarrow \exists y\,Q(y))
&\equiv \lnot(\lnot\forall x\,P(x) \lor \exists y\,Q(y)) && \text{消去} \rightarrow \\
&\equiv \forall x\,P(x) \land \lnot\exists y\,Q(y) && \text{De Morgan} \\
&\equiv \forall x\,P(x) \land \forall y\,\lnot Q(y) && \text{量词 De Morgan} \\
&\equiv \forall x\,\forall y\,(P(x) \land \lnot Q(y)). && \text{辖域扩张}
\end{aligned}
$$

最后一步中，$x$ 不在 $\lnot Q(y)$ 中自由出现、$y$ 不在 $P(x)$ 中自由出现，故两个量词可直接提到前面。

## 一阶逻辑的推演规则

自然演绎在[命题逻辑](propositional_logic.md)的规则基础上增加四条量化规则（设 $c$ 是**新常量**——不出现在前提与已证公式中）：

- **全称消去**（全称例化）：若 $\Gamma \vdash \forall x\,\varphi(x)$，则 $\Gamma \vdash \varphi(c)$；
- **全称引入**：若 $\Gamma \vdash \varphi(c)$ 且 $c$ 未在 $\Gamma$ 中出现，则 $\Gamma \vdash \forall x\,\varphi(x)$；
- **存在引入**：若 $\Gamma \vdash \varphi(c)$，则 $\Gamma \vdash \exists x\,\varphi(x)$；
- **存在消去**：若 $\Gamma \vdash \exists x\,\varphi(x)$，且从假设 $\varphi(c)$（$c$ 为新常量）能推出 $\psi$（$c$ 不在 $\psi$ 中出现），则 $\Gamma \vdash \psi$。

**例 9（全称消去与引入）** 证明 $\forall x\,(P(x) \rightarrow Q(x)),\ \forall x\,P(x) \vdash \forall x\,Q(x)$：

1. 由 $\forall x\,(P(x) \rightarrow Q(x))$ 用全称消去得 $P(c) \rightarrow Q(c)$；
2. 由 $\forall x\,P(x)$ 用全称消去得 $P(c)$；
3. 由 1、2 用蕴含消去得 $Q(c)$；
4. 因 $c$ 未在任何前提中出现，用全称引入得 $\forall x\,Q(x)$。

!!! note "要点：$c$ 的"新鲜性""
    全称引入与存在消去要求 $c$ 是**新常量**（不出现于前提和结论），否则会从"某个个体满足 $\varphi$"错误地推出"所有个体满足 $\varphi$"。这四条规则配合命题逻辑的规则，就是下文 Gödel 完备性定理所论"证明系统"的直观原型。

## 语义：结构、可满足性与有效性

**定义 9（结构）** 语言 $\mathcal{L}$ 的一个**结构**（structure）是二元组 $\mathfrak{A} = (A, I)$：$A$ 是非空集合（**论域**），$I$ 是**解释**，把每个常量符号映为 $A$ 中元素、每个 $n$ 元函数符号映为函数 $A^n \rightarrow A$、每个 $n$ 元关系符号映为 $A^n$ 上的关系。

**定义 10（满足与模型）** 设 $\mathfrak{A}$ 是 $\mathcal{L}$ 的结构，$s$ 是给每个变元指定 $A$ 中元素的一个**赋值**。"公式 $\varphi$ 在 $\mathfrak{A}$ 中按赋值 $s$ 为真"记 $\mathfrak{A} \vDash \varphi[s]$，归纳定义如下：

- $\mathfrak{A} \vDash R(t_1, \dots, t_n)[s]$ 当且仅当 $(\bar{t}_1, \dots, \bar{t}_n) \in R^{\mathfrak{A}}$（$\bar{t}_i$ 为项在 $s$ 下的值）；
- $\lnot$ 与 $\land, \lor, \rightarrow$ 按命题逻辑的真值表处理，如 $\mathfrak{A} \vDash \lnot\varphi[s]$ 当且仅当 $\mathfrak{A} \nvDash \varphi[s]$；
- $\mathfrak{A} \vDash \forall x\,\varphi[s]$ 当且仅当对 $A$ 中每个元素 $a$，$\mathfrak{A} \vDash \varphi[s(x|a)]$，其中 $s(x|a)$ 是把 $x$ 的值改为 $a$ 的赋值；
- $\mathfrak{A} \vDash \exists x\,\varphi[s]$ 当且仅当存在 $a \in A$ 使 $\mathfrak{A} \vDash \varphi[s(x|a)]$。

若句子 $\sigma$ 在结构 $\mathfrak{A}$ 中为真，称 $\mathfrak{A}$ 是 $\sigma$ 的**模型**（model）。例如在群论语言 $\mathcal{L}_{\mathrm{g}} = \{e, \cdot\}$ 中，一个结构就是一个带指定单位元与乘法的非空集合；群的结合律、单位元、逆元三条公理都是句子，因此"$G$ 是群"恰等于"$G$ 是群公理集的模型"。

**定义 11（可满足性、有效性与逻辑蕴含）**

- 公式集 $\Gamma$ **可满足**（satisfiable），指存在结构 $\mathfrak{A}$ 与赋值 $s$ 使 $\Gamma$ 中每个公式都为真；单个句子可满足指它有模型；
- 句子 $\sigma$ **有效**（valid，逻辑有效），指 $\sigma$ 在**一切**结构中为真，记 $\vDash \sigma$；
- 句子集 $\Gamma$ **逻辑蕴含** $\sigma$，记 $\Gamma \vDash \sigma$，指 $\sigma$ 在 $\Gamma$ 的一切模型中为真。

**例 10** $\forall x\,P(x) \rightarrow P(c)$ 是有效式：若 $\forall x\,P(x)$ 为真，则 $P$ 对论域中每个个体（包括 $c$ 所指的个体）成立。而 $\exists x\,P(x) \rightarrow \forall x\,P(x)$ 不是有效式：在论域 $\{a, b\}$ 中令 $P$ 只在 $a$ 上成立，则前件真而后件假。

!!! note "要点：可满足、有效、蕴含的关系"
    $\sigma$ 有效当且仅当 $\lnot\sigma$ 不可满足；$\Gamma \vDash \sigma$ 当且仅当 $\Gamma \cup \{\lnot\sigma\}$ 不可满足。因此"证明蕴含"与"证明不可满足"是一回事，这是反证法（归谬法）在语义层面的根据。与[命题逻辑](propositional_logic.md)不同，一阶逻辑的**可满足性判定问题不可判定**（Church 定理, 1936）：不存在算法能对任意一阶句子判定其是否可满足。

## 一阶逻辑的完备性与紧致性

命题逻辑的可靠完备性（见[命题逻辑](propositional_logic.md)）可推广到一阶逻辑，但证明远为深刻。

**定理 4（Gödel 完备性定理, 1929）** 一阶逻辑的证明系统（自然演绎或 Hilbert 系统）是可靠且完备的：对任意公式集 $\Gamma$ 与公式 $\varphi$，

$$
\Gamma \vdash \varphi \iff \Gamma \vDash \varphi.
$$

即"可证明"与"逻辑蕴含"完全一致：凡是逻辑上必然成立的，都能在系统内形式地证明出来。

**定理 5（紧致性定理）** 公式集 $\Gamma$ 可满足，当且仅当 $\Gamma$ 的**每个有限子集**都可满足。

**推论 1** 若句子集 $\Gamma$ 有任意大的有限模型，则 $\Gamma$ 有无穷模型。

**证明** 对每个 $n$，令 $\sigma_n$ 为句子"论域中至少有 $n$ 个不同的元素"（即 $\exists x_1 \cdots \exists x_n \bigwedge_{1 \le i < j \le n} x_i \ne x_j$）。对任意有限子集 $\Delta \subseteq \Gamma \cup \{\sigma_n : n \ge 1\}$，取足够大的有限模型即可满足 $\Delta$；由紧致性，$\Gamma \cup \{\sigma_n : n \ge 1\}$ 整体可满足，其模型必为无穷。

紧致性定理是**模型论**的基石，可用来证明非标准模型的存在（如非标准分析中的超实数）以及许多代数构造的合法性。与之相关的还有 **Löwenheim–Skolem 定理**：可数语言的可满足句子集必有**可数模型**——"一阶逻辑不能区分可数与不可数"，这也说明一阶逻辑的表达能力有限。

!!! warning "完备性 ≠ 完全性"
    完备性定理说的是**逻辑本身**：一阶逻辑的推演规则足以推出一切逻辑有效式。这**不**意味着任何足够丰富的公理系统（如 Peano 算术 PA、ZFC）都完全：Gödel 第二不完全性定理（1931）表明，任何能表示算术的一致公理系统都存在既不能证明也不能否证的句子。完备性是逻辑的性质，不完全性是**个别公理系统**的性质，二者并不矛盾——正是完备性定理保证了 ZFC 中"模型论意义下的真"与"证明论意义下的可证"在逻辑推理层面的一致。

## 与 ZFC 的联系

集合论的公理——ZFC——全部写在**集合论语言** $\mathcal{L}_{\in} = \{\in\}$ 中，即 $\{\in\}$ 上的一阶公理（与公理模式）的集合。例如**外延公理**写作

$$
\forall x\,\forall y\,\big(\forall z\,(z \in x \leftrightarrow z \in y) \rightarrow x = y\big),
$$

**选择公理**（AC）也是一阶句子。而**分离公理**与**替换公理**是一阶公理**模式**（schema）：对每个公式 $\varphi$ 各给出一条公理，因为"$\{x \in A : \varphi(x)\}$ 是集合"这类陈述要遍历一切 $\varphi$。这是 ZFC 用一阶语言表述时特有的结构（公理内容见[集合论](../set_theory/index.md)）。

完备性与紧致性反过来深刻地约束着集合论：由紧致性可推出存在非标准自然数模型；由 Löwenheim–Skolem 定理，ZFC 若有模型则有**可数模型**，而 ZFC 又能证明不可数集合存在（**Skolem 悖论**——其消解在于"可数"是相对模型的）。此外，一阶逻辑无法表达"良序"、"有限"等二阶性质，这也是 ZFC 用公理模式与无穷公理弥补表达能力的原因。逻辑为集合论提供推理规则，集合论又为逻辑提供语义与元理论，二者共同构成现代数学的[数学基础](../index.md)。

## 延伸阅读

- [命题逻辑](propositional_logic.md) —— 命题、联结词与推理规则（一阶逻辑的子逻辑）
- [数理逻辑](index.md) —— 本部分导览
- [集合论](../set_theory/index.md) —— ZFC：建立在一阶逻辑之上的公理系统
- [符号表](../../notation/index.md) —— $\forall, \exists, \land, \lor, \rightarrow$ 等记号
