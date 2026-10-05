---
title: 类型论
tags:
  - 类型论
  - 数理逻辑
---

# 类型论

> 类型论（type theory）同时是一种数学基础、形式逻辑和程序语言理论：每个表达式都带有类型，而证明本身可以作为可检查、可执行的对象。

## 1. 类型论研究什么

集合论通常从“$x$ 是否属于集合 $A$”出发；类型论把“$a$ 是类型 $A$ 的项”写成基本判断

$$
a:A.
$$

类型不是附加在无类型对象上的标签。一个项从形成之初就属于某个类型，不同类型中的项原则上不能直接混用。类型论常见于三个相互联系的领域：

1. **数学基础**（foundations of mathematics）：用类型、项与构造规则组织数学；
2. **证明论**（proof theory）：把证明表示为具有归约行为的形式对象；
3. **程序语言**（programming languages）：类型规定程序可以接受什么输入以及产生什么输出。

## 2. 四种基本判断

Martin-Löf 类型论常以判断（judgment）而非单独的公式为起点。典型判断包括：

$$
\begin{aligned}
A\ \mathsf{type} &\quad && A\text{ 是类型},\\
a:A &&& a\text{ 是 }A\text{ 的项},\\
A\equiv B\ \mathsf{type} &&& A,B\text{ 定义相等},\\
a\equiv b:A &&& a,b\text{ 在 }A\text{ 中定义相等}.
\end{aligned}
$$

判断总是在一个**上下文**（context）中作出。上下文

$$
\Gamma\equiv x_1:A_1,\ x_2:A_2(x_1),\ldots,x_n:A_n(x_1,\ldots,x_{n-1})
$$

记录当前可用的变量；后面的类型可以依赖前面的变量。

## 3. 类型构造的四类规则

一个类型构造通常由四类规则说明：

- **形成规则**（formation rule）：何时可以形成该类型；
- **引入规则**（introduction rule）：怎样构造该类型的项；
- **消去规则**（elimination rule）：怎样使用该类型的项；
- **计算规则**（computation rule）：先构造再使用时如何化简。

以函数类型 $A\to B$ 为例：Lambda 抽象 $\lambda x.t$ 是引入规则，应用 $f\,a$ 是消去规则，而

$$
(\lambda x.t)\,a\;\longrightarrow_\beta\;t[a/x]
$$

是 $\beta$-计算规则。它说明类型论不只判断命题是否可证，还规定证明如何计算。

## 4. 核心类型构造

### 4.1 依赖积类型

**定义 1（依赖积类型，dependent product type）** 若在上下文 $x:A$ 中有类型 $B(x)$，则

$$
\prod_{x:A}B(x)
$$

的项是对每个 $x:A$ 给出一个 $B(x)$ 项的函数。若 $B$ 不依赖 $x$，它退化为普通函数类型 $A\to B$。

作为逻辑，$\Pi$-type 对应全称量词；作为程序，它对应依赖函数（dependent function）。

### 4.2 依赖和类型

**定义 2（依赖和类型，dependent sum type）**

$$
\sum_{x:A}B(x)
$$

的项是有序对 $(a,b)$，其中 $a:A$ 且 $b:B(a)$。若 $B$ 不依赖 $x$，它退化为积类型 $A\times B$。

作为逻辑，$\Sigma$-type 对应存在量词，但其项不仅断言见证存在，还携带见证 $a$ 和证明 $b$。

### 4.3 等同类型

**定义 3（等同类型，identity type）** 对 $a,b:A$，类型

$$
\operatorname{Id}_A(a,b)
$$

表示 $a$ 与 $b$ 相等。每个 $a:A$ 都有反身性项

$$
\operatorname{refl}_a:\operatorname{Id}_A(a,a).
$$

等同类型的核心消去规则称为 **path induction** 或 **$J$ eliminator**：要证明关于任意等同证明的性质，只需处理反身性情形。

### 4.4 归纳类型

自然数类型 $\mathbb N$ 由构造子

$$
0:\mathbb N,\qquad \operatorname{succ}:\mathbb N\to\mathbb N
$$

生成。它的消去规则是数学归纳法，同时也是递归程序的定义原则。列表、树和有限和类型都可用类似方式给出。

### 4.5 宇宙

**定义 4（类型宇宙，universe）** 宇宙 $\mathcal U$ 是其项可被解释为类型的类型。为避免 Girard 悖论（Girard's paradox），通常采用分层宇宙

$$
\mathcal U_0:\mathcal U_1:\mathcal U_2:\cdots
$$

而不允许无条件的 $\mathcal U:\mathcal U$。

## 5. 命题即类型

Curry–Howard correspondence 把逻辑构造与类型构造联系起来：

| 逻辑 | 类型 | 项的含义 |
| --- | --- | --- |
| $A\land B$ | $A\times B$ | 两个证明组成的对 |
| $A\lor B$ | $A+B$ | 带左右标签的证明 |
| $A\Rightarrow B$ | $A\to B$ | 把 $A$ 的证明变成 $B$ 的证明 |
| $\forall x:A.B(x)$ | $\prod_{x:A}B(x)$ | 对每个 $x$ 给出证明 |
| $\exists x:A.B(x)$ | $\sum_{x:A}B(x)$ | 见证与其正确性证明 |
| 真 $\top$ | 单位类型 $\mathbf 1$ | 唯一平凡项 |
| 假 $\bot$ | 空类型 $\mathbf 0$ | 没有项 |

于是“证明命题 $P$”就是“构造类型 $P$ 的一个项”。类型检查器只需验证这个项是否具有声明的类型。

## 6. 两种相等

**定义相等**（definitional equality，也称 judgmental equality）由计算直接判定，例如

$$
(\lambda x.x+1)\,2\equiv3.
$$

它是类型检查器内部的判断，通常没有独立的证明项。

**命题相等**（propositional equality）由等同类型表达：

$$
p:\operatorname{Id}_A(a,b).
$$

它是可在理论内部量化、传递和研究的对象。强度类型论不把所有命题相等自动反射为定义相等，因为那通常会破坏类型检查的可判定性或良好的计算性质。

## 7. 元理论性质

类型系统通常希望具有下列性质：

- **保持性**（subject reduction）：项归约后类型不变；
- **强归一化**（strong normalization）：每条归约序列都终止；
- **合流性**（confluence）：不同归约路径可以汇合；
- **典范性**（canonicity）：闭的自然数项最终计算为某个数码；
- **一致性**（consistency）：空类型没有闭项；
- **类型检查可判定性**（decidability of type checking）：存在算法判断给定项是否具有给定类型。

这些性质彼此相关但并不等价。加入新公理可能保持逻辑一致性，却让闭项不再归约到规范形式；[立方类型论](cubical_type_theory.md)的重要动机之一，就是为 univalence 提供计算内容。

## 8. 内容地图

- [Lambda Cube](lambda_cube.md)：用三个依赖维度组织八种有类型 Lambda 演算。
- [同伦类型论](homotopy_type_theory.md)：把类型解释为空间、等同解释为路径。
- [立方类型论](cubical_type_theory.md)：用区间、路径与 Kan composition 赋予 univalence 计算意义。
- [范畴逻辑与类型论](../category_theory/categorical_logic.md)：CCC、LCCC 与 CwF 语义。
- [证明论](../logic/proof_theory.md)：自然演绎、序列演算、归一化与 cut elimination。

## 9. 参考资料

- Per Martin-Löf, [*Intuitionistic Type Theory*](https://archive-pml.github.io/martin-lof/pdfs/Bibliopolis-Book-retypeset-1984.pdf)：直觉主义类型论的经典原始教材。
- Bengt Nordström、Kent Petersson、Jan M. Smith, [*Programming in Martin-Löf's Type Theory*](https://www.cse.chalmers.se/research/group/logic/book/book.pdf)：从编程和构造数学角度展开 MLTT。
- Rob Nederpelt、Herman Geuvers, [*Type Theory and Formal Proof*](https://doi.org/10.1017/CBO9781139567725)：从无类型 Lambda 演算一直讲到 Calculus of Constructions。
- The Univalent Foundations Program, [*Homotopy Type Theory: Univalent Foundations of Mathematics*](https://homotopytypetheory.org/book/)：HoTT 与 univalent foundations 的标准教材。

## 延伸阅读

- [命题逻辑](../logic/propositional_logic.md)：自然演绎的逻辑起点
- [谓词逻辑](../logic/predicate_logic.md)：量词与形式语义
- [范畴论](../category_theory/index.md)：类型论的结构语义
