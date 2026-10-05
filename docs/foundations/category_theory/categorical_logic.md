---
title: 范畴逻辑与类型论
tags:
  - 范畴论
  - 类型论
  - 数理逻辑
---

# 范畴逻辑与类型论

> 范畴逻辑（categorical logic）把逻辑系统的公式、证明与代换解释为范畴中的对象、态射与复合；类型论则为这种对应提供了计算语言。

## 1. 从“真值”到“证明的结构”

在集合论语义中，一个命题通常被解释为真或假；在范畴逻辑中，我们进一步保留证明之间的结构。可以先采用下面的对应：

| 逻辑或类型论 | 范畴论 |
| --- | --- |
| 命题或类型 $A$ | 对象 $A$ |
| 从 $A$ 得到 $B$ 的证明 | 态射 $f:A\to B$ |
| 证明的顺序使用 | 态射复合 |
| 不改变假设的证明 | 恒等态射 |
| 两个证明可相互转换 | 同构或更高层次的等价 |

这不是把所有证明都压成“真”这一比特，而是研究证明如何组合、哪些构造具有泛性质，以及语法如何产生一个自由的范畴结构。

## 2. 笛卡尔闭范畴

**定义 1（笛卡尔闭范畴，cartesian closed category, CCC）** 一个范畴 $\mathcal C$ 称为笛卡尔闭的，如果它具有有限积，并且对每个对象 $A$，函子

$$
-\times A:\mathcal C\to\mathcal C
$$

有右伴随 $(-)^A$。换言之，对任意 $B,C$ 存在关于变量自然的双射

$$
\operatorname{Hom}_{\mathcal C}(C\times A,B)
\cong
\operatorname{Hom}_{\mathcal C}(C,B^A).
$$

对象 $B^A$ 称为**指数对象**（exponential object）。这个双射是函数“柯里化”（currying）的抽象形式：一个接受二元输入的函数，等价于一个返回函数的函数。

CCC 的内部语言（internal language）与直觉主义命题逻辑的对应为：

| 逻辑构造 | CCC 中的构造 |
| --- | --- |
| 真命题 $\top$ | 终对象 $1$ |
| 合取 $A\land B$ | 积 $A\times B$ |
| 蕴含 $A\to B$ | 指数对象 $B^A$ |
| 证明代入 | 态射复合 |

若还存在适当的余积和始对象，则可以解释析取 $A\lor B$ 与假命题 $\bot$。

**定理 1（Curry–Howard–Lambek 对应，Curry–Howard–Lambek correspondence）** 简单类型 Lambda 演算（simply typed lambda calculus）的语法范畴是自由笛卡尔闭范畴；反过来，每个笛卡尔闭范畴都给出简单类型 Lambda 演算的一个模型。

这里“自由”意味着：语法只满足变量、抽象、应用以及相应等式所强制的关系，没有额外等式。Lambda 项的 $\beta$-约化对应评价态射，$\eta$-规则对应指数对象的泛性质。

## 3. 依赖类型的范畴语义

简单类型不允许类型依赖于项；依赖类型论（dependent type theory）则允许在上下文 $x:A$ 中形成类型 $B(x)$。范畴语义中，上下文通常解释为对象 $\Gamma$，上下文扩张解释为态射

$$
p:\Gamma.B\longrightarrow\Gamma.
$$

类型的代换就是沿态射 $\sigma:\Delta\to\Gamma$ 的拉回（pullback）。

**定义 2（局部笛卡尔闭范畴，locally cartesian closed category, LCCC）** 若范畴 $\mathcal C$ 的每个切片范畴 $\mathcal C/\Gamma$ 都是笛卡尔闭范畴，则称 $\mathcal C$ 局部笛卡尔闭。

在适当的范畴模型中，依赖和类型与依赖积类型分别表现为拉回函子的伴随：

$$
\Sigma_f\dashv f^*\dashv\Pi_f.
$$

- $f^*$ 是**重索引**（reindexing）或代换；
- $\Sigma_f$ 解释依赖和类型（dependent sum type）；
- $\Pi_f$ 解释依赖积类型（dependent product type）。

这说明 $\Sigma$ 与 $\Pi$ 不只是类似存在量词和全称量词：它们是代换函子的左右伴随，因此自动携带一整套自然性与泛性质。

## 4. Category with Families

**定义 3（带族范畴，category with families, CwF）** CwF 是一种直接编码类型论语法的范畴结构，基本数据包括：

- 上下文及上下文代换构成的范畴；
- 每个上下文 $\Gamma$ 上的类型集合 $\operatorname{Ty}(\Gamma)$；
- 每个 $A\in\operatorname{Ty}(\Gamma)$ 的项集合 $\operatorname{Tm}(\Gamma,A)$；
- 类型和项沿代换的重索引；
- 上下文扩张 $\Gamma.A$ 及其泛性质。

CwF、contextual category、category with attributes 等框架都试图解决同一问题：怎样让“上下文、类型、项、代换”的句法规则成为可比较的数学结构。

## 5. 命题即类型，证明即程序

在 Curry–Howard correspondence 下，逻辑规则与程序构造一一对应：

$$
\frac{\Gamma,x:A\vdash t:B}{\Gamma\vdash \lambda x.t:A\to B}
\qquad
\frac{\Gamma\vdash f:A\to B\quad\Gamma\vdash a:A}
{\Gamma\vdash f\,a:B}.
$$

第一条同时是蕴含引入和函数抽象，第二条同时是 modus ponens 和函数应用。证明归一化（proof normalization）对应程序求值，cut elimination 对应消去中间证明。

!!! note "三个层次"

    Curry–Howard 连接逻辑与类型，Lambek 的范畴语义再把二者连接到范畴：命题、类型、对象是一组对应；证明、程序、态射是另一组对应。这里的“对应”保留结构，但不表示三套理论在所有细节上完全相同。

## 6. 等同性为何通向 HoTT

普通一范畴把态射之间的等式视为外部判断。强度类型论（intensional type theory）则把等同性本身做成类型 $\operatorname{Id}_A(x,y)$，其证明之间还可以继续比较。于是出现路径、路径之间的路径以及更高路径。

群胚模型（groupoid model）和无穷群胚（$\infty$-groupoid）观点表明，强度等同类型天然具有高维结构。这条路线通向[同伦类型论](../type_theory/homotopy_type_theory.md)；要让 univalence 和高阶归纳类型具有直接计算规则，则进一步通向[立方类型论](../type_theory/cubical_type_theory.md)。

## 7. 参考资料

- Tom Leinster, [*Basic Category Theory*](https://arxiv.org/abs/1612.09375)：以泛性质、伴随和可表函子为主线的开放教材。
- Emily Riehl, [*Category Theory in Context*](https://emilyriehl.github.io/files/context.pdf)：带有大量数学实例的系统教材。
- J. Lambek 与 P. J. Scott, [*Introduction to Higher-Order Categorical Logic*](https://books.google.com/books?id=6PY_emBeGjUC)：高阶逻辑、类型 Lambda 演算与 CCC 之间关系的经典著作。
- Simon Castellan、Pierre Clairambault、Peter Dybjer, [*Categories with Families: Unityped, Simply Typed, and Dependently Typed*](https://arxiv.org/abs/1904.00827)：系统比较 CwF 与多种范畴逻辑结构。

## 延伸阅读

- [泛性质与极限](universal_properties.md)：积、拉回与伴随思想
- [函子](functors.md)：函子与自然性
- [类型论](../type_theory/index.md)：判断、依赖类型与等同类型
- [证明论](../logic/proof_theory.md)：归一化与 cut elimination
