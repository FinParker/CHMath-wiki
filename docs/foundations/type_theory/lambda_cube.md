---
title: Lambda Cube
tags:
  - 类型论
  - 数理逻辑
---

# Lambda Cube

> Lambda Cube（$\lambda$-cube）由 Henk Barendregt 提出，用三个彼此独立的依赖方向统一组织八种有类型 Lambda 演算。

## 1. 从简单类型 Lambda 演算出发

简单类型 Lambda 演算（simply typed lambda calculus, STLC）的类型由基本类型和函数类型生成：

$$
A,B::=\alpha\mid A\to B.
$$

项包括变量、抽象和应用：

$$
t,u::=x\mid\lambda x:A.t\mid t\,u.
$$

它允许“项依赖于项”：函数体可以使用参数 $x$。Lambda Cube 问的是，还可以允许哪些层次之间发生依赖？

## 2. 三个扩展方向

令 $*$ 表示项的类型所在的 sort，$\square$ 表示类型构造子的 sort。除基础维度 $(*,*)$ 外，三个扩展轴为：

1. **多态性**（polymorphism，$(\square,*)$）：项可以依赖于类型，例如 System F 的
   $$
   \Lambda A.\lambda x:A.x:\prod_{A:*}A\to A.
   $$
2. **依赖类型**（dependent types，$(*,\square)$）：类型可以依赖于项，例如长度索引向量 $\operatorname{Vec}(A,n)$；
3. **类型算子**（type operators，$(\square,\square)$）：类型可以依赖于类型，例如 $F:*\to*$。

三个开关的每种组合给出立方体的一个顶点，共八个系统。

## 3. 八个顶点

| 系统 | 多态 | 依赖类型 | 类型算子 | 常见名称或定位 |
| --- | --- | --- | --- | --- |
| $\lambda_\to$ | 否 | 否 | 否 | simply typed lambda calculus |
| $\lambda_2$ | 是 | 否 | 否 | System F，二阶多态 Lambda 演算 |
| $\lambda_P$ | 否 | 是 | 否 | 一阶依赖类型，接近 LF 核心 |
| $\lambda_\omega$ | 否 | 否 | 是 | 高阶类型算子 |
| $\lambda_{P2}$ | 是 | 是 | 否 | 依赖类型 + 多态 |
| $\lambda_{2\omega}$ | 是 | 否 | 是 | System $F_\omega$ |
| $\lambda_{P\omega}$ | 否 | 是 | 是 | 依赖类型 + 类型算子 |
| $\lambda_C$ | 是 | 是 | 是 | Calculus of Constructions (CoC) |

从一个顶点沿边移动，就是加入一种新的依赖规则；最强顶点 $\lambda_C$ 同时拥有三个方向。

## 4. Pure Type System 表示

**定义 1（纯类型系统，pure type system, PTS）** 一个 PTS 由三部分数据 $(\mathcal S,\mathcal A,\mathcal R)$ 指定：

- $\mathcal S$：sort 的集合；
- $\mathcal A\subseteq\mathcal S\times\mathcal S$：公理，规定某个 sort 属于哪个更高 sort；
- $\mathcal R\subseteq\mathcal S^3$：乘积规则，规定何时可以形成 $\Pi$-type。

Lambda Cube 使用两个 sort $*、\square$，通常包含公理

$$
*: \square
$$

以及基础规则 $(*,*,*)$。三个可选方向分别由规则

$$
(\square,*,*),\qquad(*,\square,\square),\qquad(\square,\square,\square)
$$

控制。

一般的乘积形成规则写为

$$
\frac{\Gamma\vdash A:s_1\qquad\Gamma,x:A\vdash B:s_2}
{\Gamma\vdash\prod_{x:A}B:s_3}
\quad (s_1,s_2,s_3)\in\mathcal R.
$$

这种表示把八个系统的语法差异集中到一张很小的规则表里。

## 5. 三条轴各自解决什么问题

### 5.1 System F：对所有类型编程

在 $\lambda_2$ 中，恒等函数不必为每个类型重复定义：

$$
\operatorname{id}=\Lambda A.\lambda x:A.x.
$$

它具有多态类型 $\forall A.A\to A$。参数多态（parametric polymorphism）限制程序只能以统一方式处理未知类型。

### 5.2 依赖类型：让命题进入类型

在 $\lambda_P$ 方向中，函数的结果类型可以依赖输入：

$$
\prod_{n:\mathbb N}\operatorname{Vec}(A,n)\to\operatorname{Vec}(A,n).
$$

长度约束成为类型的一部分，类型检查器因而能够排除长度不匹配的程序。

### 5.3 高阶类型算子：对类型构造子抽象

在 $\lambda_\omega$ 方向中，可以讨论 $F:*\to*$ 这样的类型构造子，并对它们进行 Lambda 抽象。这是 higher-kinded types 的理论原型。

## 6. Calculus of Constructions

**定义 2（构造演算，Calculus of Constructions, CoC）** $\lambda_C$ 是 Lambda Cube 的最强顶点，同时允许多态、依赖类型和高阶类型算子。其项和类型由同一种依赖函数机制 $\Pi$ 统一表达。

CoC 把高阶直觉主义逻辑与强类型函数式计算统一起来，并成为 Coq 等证明助理理论核心的重要来源。实际系统通常还加入归纳类型、宇宙层级和终止性检查。

## 7. 归一化与逻辑一致性

**定理 1（强归一化，strong normalization）** Lambda Cube 八个系统中的良类型项都没有无限 $\beta$-归约序列。

强归一化带来两个关键后果：程序求值不会因纯粹的 $\beta$-归约而无限进行；在 propositions-as-types 解释下，不可能通过一个永不停止的伪“证明”构造任意命题。

!!! warning "不要加入无分层的 Type : Type"

    若允许同一个宇宙既包含自身又可在所有位置自由依赖，即 $*:*$，会出现 Girard 悖论，导致逻辑不一致。现代依赖类型论通常采用累积宇宙层级（cumulative universe hierarchy）。

## 8. Lambda Cube 的边界

Lambda Cube 分类的是一组纯依赖函数系统，并不直接包含：

- 归纳类型及其递归原理；
- quotient type、subtyping 或 effect；
- HoTT 的 univalence 与 higher inductive type；
- 立方类型论的 interval、composition 与 Glue type。

因此它更像“类型依赖关系的坐标系”，不是现代类型系统的完整分类表。

## 9. 参考资料

- Henk Barendregt, [*An Introduction to Generalized Type Systems*](https://homepages.inf.ed.ac.uk/wadler/papers/barendregt/pure-type-systems.pdf), *Journal of Functional Programming* 1(2), 1991：Lambda Cube 与 generalized type systems 的经典论文。
- Henk Barendregt, [Foundational Papers](https://www.cs.ru.nl/~henk/papers.html)：作者维护的论文入口。
- Thierry Coquand 与 Gérard Huet, [*The Calculus of Constructions*](https://www.asc.ohio-state.edu/pollard.4/type/readings/coc88.pdf)：CoC 的原始文献。
- Rob Nederpelt 与 Herman Geuvers, [*Type Theory and Formal Proof*](https://doi.org/10.1017/CBO9781139567725)：按 Lambda Cube 的维度系统讲解各种演算。

## 延伸阅读

- [类型论](index.md)：判断、$\Pi$/$\Sigma$ 类型与等同类型
- [同伦类型论](homotopy_type_theory.md)：从等同类型走向高维路径
- [证明论](../logic/proof_theory.md)：归一化的证明论意义
