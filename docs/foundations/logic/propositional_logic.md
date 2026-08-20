---
title: 命题逻辑
tags:
  - 数理逻辑
---

# 命题逻辑

命题逻辑是数理逻辑的起点：它把"一个断言要么为真、要么为假"这一朴素直觉精确化，研究如何用**联结词**把简单命题组装成复合命题、两个命题何时在真值上等价、哪些推理形式保证"前提真则结论真"。它不分析命题的内部结构——"苏格拉底会死"与"2 是偶数"在命题逻辑看来都是不可再分的基本单元。这正是[谓词逻辑](predicate_logic.md)要补充的内容。

## 命题与真值

**定义 1（命题）** 能唯一判定真假的陈述句称为**命题**（proposition）。命题要么为真（记 $T$ 或 $\top$），要么为假（记 $F$ 或 $\bot$），二者必居其一——这称为**二值原则**。

**例 1**

- "2 是素数" 是命题，为真；
- "$1 + 1 = 3$" 是命题，为假；
- "$x > 3$" 不是命题：$x$ 没有取值，无法判定真假；
- "请关上门！" 不是命题：祈使句没有真假。

!!! note "要点：命题与语句的差别"
    同一命题可用不同语句表达（"天下雨"与 "It is raining"），同一语句在不同语境下也可能表达不同命题（"今天是星期三"在周一与周四说的不是同一件事）。命题逻辑只关心命题的**真值**，不关心语句的语法细节。

命题通常用小写字母 $p, q, r, \dots$ 表示，称为**命题变元**（propositional variable）。给每个命题变元指定一个真值，称为一次**赋值**（truth assignment）。命题逻辑的一切概念都以"在赋值下取真值"为基础。

## 五个联结词

**定义 2（联结词）** 从已有命题构造新命题的符号称为联结词。命题逻辑使用五个基本联结词：否定 $\lnot$、合取 $\land$、析取 $\lor$、蕴含 $\rightarrow$、等值 $\leftrightarrow$。

| 联结词 | 名称 | 读法 | 自然语言 |
| --- | --- | --- | --- |
| $\lnot p$ | 否定 | 非 p | "并非 p" |
| $p \land q$ | 合取 | p 且 q | "p 并且 q" |
| $p \lor q$ | 析取 | p 或 q | "p 或者 q" |
| $p \rightarrow q$ | 蕴含 | 若 p 则 q | "如果 p，那么 q" |
| $p \leftrightarrow q$ | 等值 | p 当且仅当 q | "p 与 q 同真同假" |

它们的真值表如下。

**否定**

| $p$ | $\lnot p$ |
| --- | --- |
| $T$ | $F$ |
| $F$ | $T$ |

**合取与析取**

| $p$ | $q$ | $p \land q$ | $p \lor q$ |
| --- | --- | --- | --- |
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $T$ |
| $F$ | $T$ | $F$ | $T$ |
| $F$ | $F$ | $F$ | $F$ |

**蕴含与等值**

| $p$ | $q$ | $p \rightarrow q$ | $p \leftrightarrow q$ |
| --- | --- | --- | --- |
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $F$ |
| $F$ | $T$ | $T$ | $F$ |
| $F$ | $F$ | $T$ | $T$ |

!!! warning "易错点：蕴含的"空真""
    当 $p$ 为假时，$p \rightarrow q$ 一律为真，称为**空真**（vacuous truth）。"如果太阳从西边出来，那么 $1 + 1 = 3$" 在真值表意义下为真。"若 p 则 q" 是**真值函数**：它只由 $p, q$ 的真假决定，与因果、时间无关——"如果明天下雨，我就带伞"只承诺"天下雨 $\Rightarrow$ 我带伞"，并不承诺下雨本身。

!!! warning "易错点："或者"的歧义"
    自然语言的"或者"有时是**可兼或**（$p$ 或 $q$ 或二者都成立，即 $\lor$），有时是**异或**（恰好一个成立）。命题逻辑的 $\lor$ 一律取可兼或："$1 + 1 = 2$ 或地球是方的"为真。

## 合式公式

把命题变元与联结词按规则拼成的合法表达式称为**合式公式**（well-formed formula，wff）。不合规则的字符串（如 $p \land \lor q$、$\rightarrow p$）不是公式。

**定义 3（合式公式，归纳定义）**

1. **基础**：命题变元 $p, q, r, \dots$ 是合式公式，称为**原子公式**；
2. **归纳**：若 $\varphi, \psi$ 是合式公式，则 $\lnot\varphi$、$(\varphi \land \psi)$、$(\varphi \lor \psi)$、$(\varphi \rightarrow \psi)$、$(\varphi \leftrightarrow \psi)$ 都是合式公式；
3. **极小性**：除由 1、2 两步有限次生成的字符串外，没有别的合式公式。

**例 2** 下列是合式公式：$p$、$\lnot p$、$(p \land q)$、$((p \lor q) \rightarrow \lnot r)$。下列不是：$p \land q \lor$（联结词位置错误）、$(p \rightarrow$（括号不配对）、$pq$（两个变元直接相连）。

为减少括号，约定**优先级**从高到低为 $\lnot > \land > \lor > \rightarrow > \leftrightarrow$，且 $\rightarrow$、$\leftrightarrow$ 右结合。于是 $p \land q \rightarrow r$ 表示 $(p \land q) \rightarrow r$，$\lnot p \land q$ 表示 $(\lnot p) \land q$。

!!! note "要点：为什么用归纳定义"
    归纳定义保证每个公式都有**唯一读解**（unique readability）：一个合式公式的"分析树"唯一确定。这使后面所有对公式的论证（如按结构归纳证明性质）都有坚实的立足点。

## 逻辑等价

**定义 4（逻辑等价）** 若两个公式 $\varphi, \psi$ 在**一切赋值**下真值相同，称 $\varphi$ 与 $\psi$ 逻辑等价，记 $\varphi \equiv \psi$。

**定理 1（蕴含与等值的改写）**

$$
p \rightarrow q \equiv \lnot p \lor q, \qquad
p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p), \qquad
p \rightarrow q \equiv \lnot q \rightarrow \lnot p.
$$

第三条称为**逆否律**（contraposition）。由蕴含改写立得：$p \rightarrow q$ 为假当且仅当 $p$ 真而 $q$ 假——这正是真值表的最后一行。

**常用等价式**（$p, q, r$ 为任意公式）：

| 等价式 | 名称 |
| --- | --- |
| $\lnot\lnot p \equiv p$ | 双重否定律 |
| $p \lor p \equiv p,\quad p \land p \equiv p$ | 幂等律 |
| $p \lor q \equiv q \lor p,\quad p \land q \equiv q \land p$ | 交换律 |
| $(p \lor q) \lor r \equiv p \lor (q \lor r)$ | 结合律 |
| $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ | 分配律（$\lor$ 对 $\land$） |
| $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ | 分配律（$\land$ 对 $\lor$） |
| $\lnot(p \land q) \equiv \lnot p \lor \lnot q$ | De Morgan 律 |
| $\lnot(p \lor q) \equiv \lnot p \land \lnot q$ | De Morgan 律 |
| $p \lor (p \land q) \equiv p,\quad p \land (p \lor q) \equiv p$ | 吸收律 |
| $p \lor \lnot p \equiv \top,\quad p \land \lnot p \equiv \bot$ | 排中律 / 矛盾律 |
| $p \lor \bot \equiv p,\quad p \land \top \equiv p$ | 恒等律 |
| $p \lor \top \equiv \top,\quad p \land \bot \equiv \bot$ | 支配律 |

**例 3** 用等价变换化简 $(p \rightarrow q) \land (p \rightarrow \lnot q)$：

$$
(p \rightarrow q) \land (p \rightarrow \lnot q)
\equiv (\lnot p \lor q) \land (\lnot p \lor \lnot q)
\equiv \lnot p \lor (q \land \lnot q)
\equiv \lnot p \lor \bot
\equiv \lnot p.
$$

它等价于 $\lnot p$，说明"由 $p$ 既推出 $q$ 又推出 $\lnot q$"与"$p$ 为假"是一回事——这正是**归谬法**的原理（见下文自然演绎）。

!!! note "要点：$\equiv$ 是元语言符号"
    $\equiv$ 不是命题逻辑的联结词，而是关于公式的**元语言**断言："$\varphi \equiv \psi$" 的意思就是 $\varphi \leftrightarrow \psi$ 是重言式（见下节）。类似地，推理规则中的 $\Rightarrow$ 与证明系统中的 $\vdash$ 也处于元语言层次，不应与联结词 $\rightarrow$ 混用。

## 重言式、矛盾式与可满足式

**定义 5（按真值分类）** 设 $\varphi$ 是合式公式：

- 若 $\varphi$ 在一切赋值下均为真，称 $\varphi$ 为**重言式**（tautology），记 $\vDash \varphi$；
- 若 $\varphi$ 在一切赋值下均为假，称 $\varphi$ 为**矛盾式**（contradiction）；
- 若存在赋值使 $\varphi$ 为真，称 $\varphi$ **可满足**（satisfiable）。

**例 4** $p \lor \lnot p$ 是重言式（排中律）；$p \land \lnot p$ 是矛盾式；$p \land q$ 既非重言式也非矛盾式，但可满足（取 $p = q = T$ 即可）。

**定理 2（等价与重言式的联系）** $\varphi \equiv \psi$ 当且仅当 $\varphi \leftrightarrow \psi$ 是重言式。

**证明** 由定义：$\varphi \leftrightarrow \psi$ 在一切赋值下为真，当且仅当 $\varphi$ 与 $\psi$ 在一切赋值下真值相同，当且仅当 $\varphi \equiv \psi$。

判断公式是否重言式，最直接的方法是**真值表法**：公式含 $n$ 个变元，就检查 $2^n$ 种赋值。这是完全机械的过程——命题逻辑的判定问题是**可判定**的。

## 蕴含与推理规则

**定义 6（有效论证）** 设 $p_1, \dots, p_n, q$ 是命题公式。若每当 $p_1, \dots, p_n$ 都为真时 $q$ 必为真，即

$$
(p_1 \land p_2 \land \cdots \land p_n) \rightarrow q
$$

是重言式，则称论证 $p_1, \dots, p_n \therefore q$ **有效**（valid）。$p_1, \dots, p_n$ 称为**前提**，$q$ 称为**结论**。有效的论证模式也叫**推理规则**。

**常用的推理规则**：

| 规则 | 名称 |
| --- | --- |
| $p \rightarrow q,\ p \therefore q$ | 肯定前件（modus ponens） |
| $p \rightarrow q,\ \lnot q \therefore \lnot p$ | 否定后件（modus tollens） |
| $p \rightarrow q,\ q \rightarrow r \therefore p \rightarrow r$ | 假言三段论（hypothetical syllogism） |
| $p \lor q,\ \lnot p \therefore q$ | 析取三段论（disjunctive syllogism） |
| $p,\ q \therefore p \land q$ | 合取引入 |
| $p \land q \therefore p$ | 合取消去 |
| $p \therefore p \lor q$ | 析取引入（附加） |

**例 5**

- 如果天下雨，则地是湿的；天下雨了；所以地是湿的。——肯定前件。
- 如果天下雨，则地是湿的；地不是湿的；所以天没下雨。——否定后件。
- 如果明天下雨，则路面湿滑；如果路面湿滑，则比赛推迟；所以如果明天下雨，则比赛推迟。——假言三段论。

经典三段论"凡人皆死；苏格拉底是人；所以苏格拉底会死"表面上也形如 $p \rightarrow q,\ p \therefore q$，但它的有效性依赖"凡"（全称量词）对个体结构的分析，命题逻辑无法表达，见[谓词逻辑](predicate_logic.md)。

!!! warning "易错点：推理规则不是逆命题"
    "$p \rightarrow q$ 真、$q$ 真，所以 $p$ 真"是**无效**的，这是"肯定后件"谬误（affirming the consequent）；"$p \rightarrow q$ 真、$\lnot p$ 真，所以 $\lnot q$ 真"是"否定前件"谬误。有效性只要求"前提全真则结论必真"，并不要求前提或结论本身为真。

## 形式证明系统（自然演绎）

上面的推理规则只是"单个"有效论证。形式证明系统提供一组**规则**，允许从前提出发按规则逐步推导结论，把多步推理也严格化。这里简述**自然演绎**（natural deduction）的一个核心片段。

自然演绎除前提外，还允许引入**假设**并在之后**消去**（假设—消去配对）。设 $\Gamma \vdash \varphi$ 表示"从公式集 $\Gamma$ 可推导出 $\varphi$"，基本规则包括：

- **合取引入**：若 $\Gamma \vdash \varphi$ 且 $\Gamma \vdash \psi$，则 $\Gamma \vdash \varphi \land \psi$；
- **合取消去**：若 $\Gamma \vdash \varphi \land \psi$，则 $\Gamma \vdash \varphi$ 且 $\Gamma \vdash \psi$；
- **蕴含消去**（即肯定前件）：若 $\Gamma \vdash \varphi \rightarrow \psi$ 且 $\Gamma \vdash \varphi$，则 $\Gamma \vdash \psi$；
- **蕴含引入**（条件证明）：若 $\Gamma \cup \{\varphi\} \vdash \psi$，则 $\Gamma \vdash \varphi \rightarrow \psi$；
- **归谬法**（否定引入）：若 $\Gamma \cup \{\varphi\} \vdash \bot$，则 $\Gamma \vdash \lnot\varphi$；
- **排中律**：$\Gamma \vdash \varphi \lor \lnot\varphi$（经典逻辑特有，直觉主义逻辑不采用）。

**例 6（自然演绎证明假言三段论）** 证明 $\vdash (p \rightarrow q) \rightarrow \big((q \rightarrow r) \rightarrow (p \rightarrow r)\big)$：

1. 假设 $p \rightarrow q$；
2. 假设 $q \rightarrow r$；
3. 假设 $p$；
4. 由 1、3 用蕴含消去得 $q$；
5. 由 2、4 用蕴含消去得 $r$；
6. 由 3–5 用蕴含引入消去假设 $p$，得 $p \rightarrow r$；
7. 由 2–6 消去假设 $q \rightarrow r$，得 $(q \rightarrow r) \rightarrow (p \rightarrow r)$；
8. 由 1–7 消去假设 $p \rightarrow q$，得所要的公式。

!!! note "要点：可靠性与完备性"
    证明系统是**可靠**（sound）的，指凡能证明的都有效：$\Gamma \vdash \varphi \Rightarrow \Gamma \vDash \varphi$；是**完备**（complete）的，指凡有效的都能证明：$\Gamma \vDash \varphi \Rightarrow \Gamma \vdash \varphi$。命题逻辑的证明系统（自然演绎、Hilbert 风格公理系统均可）既可靠又完备（Post, 1921）。完备性把"语义上的真"与"句法上的可证"统一起来，它在谓词逻辑层面的推广正是 [Gödel 完备性定理](predicate_logic.md)。

## 与集合运算的联系

把 $T$ 看成 $1$、$F$ 看成 $0$，命题公式就成为 $\{0, 1\}$ 上的布尔函数。若把"使公式 $\varphi$ 为真的全部赋值"看作一个集合 $[\varphi]$，则联结词与集合运算一一对应：

| 命题逻辑 | 集合运算 |
| --- | --- |
| $\lnot\varphi$ | 补集（相对赋值全集） |
| $\varphi \land \psi$ | 交集 $[\varphi] \cap [\psi]$ |
| $\varphi \lor \psi$ | 并集 $[\varphi] \cup [\psi]$ |
| $\varphi \rightarrow \psi$ 为重言式 | 包含 $[\varphi] \subseteq [\psi]$ |

于是命题逻辑的等价式对应集合恒等式：De Morgan 律 $\lnot(p \land q) \equiv \lnot p \lor \lnot q$ 对应 $(A \cap B)^c = A^c \cup B^c$，分配律对应 $(A \cap B) \cup C = (A \cup C) \cap (B \cup C)$。两边的结构都是**布尔代数**（相关运算见[集合论](../set_theory/index.md)）——这正是布尔代数同时服务于逻辑与集合的原因。

## 延伸阅读

- [谓词逻辑](predicate_logic.md) —— 打开命题的内部结构：个体、谓词与量词
- [数理逻辑](index.md) —— 本部分导览
- [集合论](../set_theory/index.md) —— 联结词与集合运算的对应、布尔代数
- [符号表](../../notation/index.md) —— $\lnot, \land, \lor, \rightarrow, \leftrightarrow$ 等记号
