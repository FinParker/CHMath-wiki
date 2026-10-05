---
title: 证明论
tags:
  - 数理逻辑
  - 证明论
---

# 证明论

> 证明论（proof theory）把形式证明本身当作数学对象，研究证明的结构、变换、复杂度以及一个形式系统能够证明到什么程度。

## 1. 句法视角

模型论（model theory）主要问公式在什么结构中为真；证明论主要问公式能否由规则推出，以及证明怎样被化简。基本判断写作

$$
\Gamma\vdash A,
$$

表示在假设集合或上下文 $\Gamma$ 下可以推导 $A$。符号 $\vdash$ 表示句法可证性，与语义蕴涵 $\vDash$ 不同。

证明论关心的问题包括：

- 证明系统是否可靠（sound）和完备（complete）；
- 是否能消去多余的引理或迂回步骤；
- 系统是否一致；
- 证明搜索是否可判定、复杂度多高；
- 一个算术理论需要多强的归纳原理才能证明其一致性。

## 2. 三类证明系统

### 2.1 Hilbert 系统

Hilbert-style system 只有少量推理规则，但有若干公理模式。典型规则是 modus ponens：

$$
\frac{A\to B\qquad A}{B}.
$$

它适合元理论研究，但实际证明往往很长，证明结构也不直观。

### 2.2 自然演绎

自然演绎（natural deduction）为每个逻辑联结词给出引入规则与消去规则。例如：

$$
\frac{\Gamma\vdash A\qquad\Gamma\vdash B}{\Gamma\vdash A\land B}(\land I)
\qquad
\frac{\Gamma\vdash A\land B}{\Gamma\vdash A}(\land E_1).
$$

蕴含引入会解除假设：

$$
\frac{\Gamma,A\vdash B}{\Gamma\vdash A\to B}(\to I).
$$

“引入后立刻消去”形成 proof detour，可以通过 normalization 消除。

### 2.3 序列演算

**定义 1（序列，sequent）** 序列

$$
\Gamma\vdash\Delta
$$

由左侧前件（antecedent）和右侧后件（succedent）组成。经典序列演算 LK 允许右侧有多个公式；直觉主义序列演算 LJ 通常限制右侧至多一个公式。

逻辑规则按联结词出现在左侧或右侧分别给出。例如合取规则的一部分为

$$
\frac{\Gamma,A,B\vdash\Delta}{\Gamma,A\land B\vdash\Delta}(\land L)
\qquad
\frac{\Gamma\vdash A,\Delta\qquad\Gamma\vdash B,\Delta}
{\Gamma\vdash A\land B,\Delta}(\land R).
$$

序列演算把证明上下文显式写入判断，因此非常适合结构归纳和 proof search。

## 3. 结构规则

结构规则（structural rules）控制公式如何在上下文中使用：

- **交换**（exchange）：改变假设顺序；
- **弱化**（weakening）：加入未使用的假设；
- **收缩**（contraction）：把重复假设合并；
- **切割**（cut）：使用一个中间引理。

Cut rule 写作

$$
\frac{\Gamma\vdash A,\Delta\qquad\Pi,A\vdash\Lambda}
{\Gamma,\Pi\vdash\Delta,\Lambda}(\mathrm{cut}).
$$

公式 $A$ 出现在两个前提中，却从结论消失，因此它代表一个可能很复杂的中间引理。

## 4. Cut elimination

**定理 1（Gentzen 切割消去定理，Gentzen's cut-elimination theorem / Hauptsatz）** 在经典序列演算 LK 和直觉主义序列演算 LJ 中，每个使用 cut rule 的证明都可以转化为不使用 cut rule 的证明。

这个定理不表示数学实践中不该使用引理，而是说在纯逻辑演算中，引理可以原则上展开。

重要推论包括：

1. **子公式性质**（subformula property）：cut-free proof 中出现的公式基本由结论及假设的子公式构成；
2. **一致性**（consistency）：空序列不能有 cut-free proof；
3. **可判定性结果**：对命题逻辑，可以把 proof search 限制在有限的子公式空间；
4. **保守性**（conservativity）：某些扩张不会产生关于旧语言的新定理。

## 5. 自然演绎的归一化

**定理 2（归一化定理，normalization theorem）** 自然演绎证明可以通过局部约化消去最大公式和 detour，转化为 normal form。

例如，先用 $\to I$ 构造函数再立即用 $\to E$ 应用：

$$
(\lambda x.t)\,u\longrightarrow t[u/x].
$$

在 Curry–Howard correspondence 下，这正是 Lambda 演算的 $\beta$-reduction。于是：

| 证明论 | 类型论或程序 |
| --- | --- |
| cut elimination | substitution / evaluation |
| normalization | 程序归约到 normal form |
| formula | type |
| proof | term / program |
| consistency | empty type 没有闭项 |

## 6. 可靠性、完备性与一致性

三个概念必须区分：

- **可靠性**：$\Gamma\vdash A$ 蕴含 $\Gamma\vDash A$；
- **完备性**：$\Gamma\vDash A$ 蕴含 $\Gamma\vdash A$；
- **一致性**：不存在 $\vdash\bot$ 的证明。

可靠性和完备性比较句法与语义；一致性只说某个矛盾在系统内部不可证。Gödel completeness theorem 针对一阶逻辑，而 Gödel incompleteness theorems 针对足够强的具体算术理论，二者讨论的层次不同。

## 7. 序数分析

证明论不只化简单个逻辑证明，还比较形式理论的强度。**证明论序数**（proof-theoretic ordinal）用良序上的超限归纳刻画理论可证明的归纳强度。

Gentzen 对 Peano arithmetic (PA) 的一致性证明使用了小于 $\varepsilon_0$ 的序数记号和超限归纳。它表明：在一个能够认可相应良序性的元理论中，可以证明 PA 一致。

!!! warning "与 Gödel 第二不完全性定理并不矛盾"

    PA 若一致，就不能在自身内部证明自身的一致性。Gentzen 证明使用了 PA 本身不能完整证明其良基性的超限归纳原则，因此是相对一致性与理论强度分析，而不是 PA 内部的自证。

现代 ordinal analysis 研究更强理论对应的序数表示系统；proof mining 则从非构造证明中提取显式界或算法。

## 8. 资源敏感逻辑

普通经典和直觉主义逻辑允许 weakening 与 contraction，所以一个假设可以不用或重复使用。在线性逻辑（linear logic）中，这些规则受到控制：假设被视为资源，必须精确追踪使用次数。

这说明结构规则不是无关紧要的排版规则。改变它们会改变逻辑本身，并连接到并发、资源管理和程序语义。

## 9. 与类型论和范畴论的关系

- 自然演绎 normalization 对应 Lambda 项求值；
- 序列演算 cut elimination 对应显式代换的消除；
- cartesian closed category 为直觉主义命题逻辑提供语义；
- dependent type theory 把量词和证明对象统一为 $\Pi$/$\Sigma$ 类型；
- HoTT 与 CuTT 继续研究等同证明的高维结构及计算行为。

因此证明论、类型论与范畴逻辑不是三个孤立主题，而是从句法、计算和语义观察同一组结构。

## 10. 参考资料

- A. S. Troelstra 与 H. Schwichtenberg, [*Basic Proof Theory*](https://doi.org/10.1017/CBO9781139168717)：结构证明论的标准教材，覆盖 Gentzen systems、cut elimination 与 normalization。
- Gerhard Gentzen, [*Investigations into Logical Deduction*](https://github.com/ProofSystem/Encyclopedia/blob/master/papers/Gentzen%201935%20-%20Investigations%20into%20Logical%20Deduction.pdf)：自然演绎、LK/LJ 与 Hauptsatz 的奠基论文英译。
- Dag Prawitz, [*Natural Deduction: A Proof-Theoretical Study*](https://books.google.com/books?id=sJj3DQAAQBAJ)：自然演绎归一化与 proof-theoretic semantics 的经典专著。
- Per Martin-Löf, [*Intuitionistic Type Theory*](https://archive-pml.github.io/martin-lof/pdfs/Bibliopolis-Book-retypeset-1984.pdf)：证明论解释与依赖类型论的连接。

## 延伸阅读

- [命题逻辑](propositional_logic.md)：自然演绎规则
- [谓词逻辑](predicate_logic.md)：可靠性、完备性与不完全性
- [类型论](../type_theory/index.md)：proofs as programs
- [范畴逻辑与类型论](../category_theory/categorical_logic.md)：证明系统的范畴语义
