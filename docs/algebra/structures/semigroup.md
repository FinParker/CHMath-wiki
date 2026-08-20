---
title: 半群与幺半群
tags:
  - 代数
---

# 半群与幺半群

半群是只要求"运算封闭且结合"的代数系统，是群的最弱前提；幺半群（又称独异点）在半群
之上再要求存在单位元。它们虽然结构简单，却是计算机科学（字符串、自动机、形式语言）
与代数学（矩阵乘法、变换合成）中最常见的代数对象。

## 半群

**定义 1（半群）**：设 $S$ 是非空集合，$\circ$ 是 $S$ 上的二元运算。若

1. $\circ$ 在 $S$ 上封闭：$\forall a, b \in S$，$a \circ b \in S$；
2. $\circ$ 满足结合律：$\forall a, b, c \in S$，$(a \circ b) \circ c = a \circ
   (b \circ c)$，

则称 $\langle S, \circ \rangle$ 为**半群**。

**定义 2（交换半群）**：若半群 $\langle S, \circ \rangle$ 的运算还满足交换律，称其为
**交换半群**。

**例 1（正整数乘法半群）**：$\langle \mathbb{Z}^+, \cdot \rangle$ 是交换半群；由于
$1$ 是单位元，它同时是幺半群。$\langle \mathbb{Z}^+, + \rangle$ 也是交换半群，但
没有单位元（$0 \notin \mathbb{Z}^+$），故不是幺半群。

**例 2（字符串拼接幺半群）**：设 $\Sigma$ 是字母表，$\Sigma^*$ 是 $\Sigma$ 上一切
有限字符串的集合。拼接运算 $\cdot$ 封闭且结合，空串 $\varepsilon$ 是单位元，故
$\langle \Sigma^*, \cdot \rangle$ 是幺半群（一般非交换）。

**例 3（矩阵乘法幺半群）**：设 $R$ 是含幺环（如 $\mathbb{R}$），$M_n(R)$ 是 $n$ 阶
实（或 $R$ 上）矩阵全体。矩阵乘法封闭且结合，单位矩阵 $I_n$ 是单位元，故
$\langle M_n(R), \cdot \rangle$ 是幺半群；$n \geq 2$ 时矩阵乘法不交换。

**例 4（变换半群）**：集合 $A$ 上一切映射的集合 $A^A$ 关于映射合成构成半群（有恒等
映射时是幺半群）。这是"最一般"的半群之一，其意义见下文表示定理。

## 幺半群

**定义 3（幺半群）**：设 $\langle S, \circ \rangle$ 是半群。若存在单位元 $e \in S$
使 $\forall a \in S$ 有 $a \circ e = e \circ a = a$，则称 $\langle S, \circ, e
\rangle$ 为**幺半群**（monoid，旧译"独异点"）。

由 [代数系统](algebraic_system.md) 定理 1，单位元若存在必唯一。

!!! note "半群与幺半群的关系"

    每个幺半群当然是半群；反过来，任何半群都可以扩张为幺半群：若 $S$ 已有单位元则
    无需改动，否则添加一个新元素 $e$，规定 $e \circ a = a \circ e = a$ 对一切
    $a \in S$ 成立。因此"半群"与"幺半群"的差别只在是否把单位元纳入结构。

**定理 1（扩张为幺半群）**：设 $\langle S, \circ \rangle$ 是半群，$e \notin S$ 为
新元素。在 $S \cup \{e\}$ 上把 $\circ$ 扩张为

$$
a \circ b = \begin{cases}
a \circ b, & a, b \in S, \\
a, & b = e, \\
b, & a = e,
\end{cases}
$$

则 $\langle S \cup \{e\}, \circ, e \rangle$ 是幺半群，且 $S$ 是其子半群。

**证明**：新运算封闭、有单位元 $e$；结合律只需检查涉及 $e$ 的情形，均直接由定义
成立。$\square$

## 幂运算

**定义 4（幂）**：设 $\langle S, \circ \rangle$ 是半群，$a \in S$，定义 $a$ 的
**正整数次幂**为

$$
a^1 = a, \qquad a^{n+1} = a^n \circ a \quad (n \geq 1).
$$

若 $\langle S, \circ, e \rangle$ 是幺半群，还定义 $a^0 = e$。

**定理 2（幂运算规则）**：设 $\langle S, \circ \rangle$ 是半群，则对一切正整数
$m, n$ 有

$$
a^m \circ a^n = a^{m+n}, \qquad (a^m)^n = a^{mn}.
$$

在幺半群中对非负整数 $m, n$ 同样成立。

**证明**：对 $n$ 作归纳即可，结合律保证乘法的次序无关紧要。$\square$

!!! note "幂运算能定义到哪一步"

    半群中只能定义正整数次幂（"非零次幂"）；幺半群中可以定义零次幂（$a^0 = e$）；
    只有群（见 [群](group.md)）中才能定义负整数次幂 $a^{-n} = (a^{-1})^n$。这是三个
    结构层层递进的直观体现。

## 子半群与生成子半群

**定义 5（子半群）**：设 $\langle S, \circ \rangle$ 是半群，$B$ 是 $S$ 的非空子集。
若 $B$ 对 $\circ$ 封闭，则 $\langle B, \circ \rangle$ 是 $S$ 的**子半群**。若
$\langle S, \circ, e \rangle$ 是幺半群且 $e \in B$，则 $\langle B, \circ, e
\rangle$ 是**子幺半群**。

**定理 3（子半群判定）**：$S$ 的非空子集 $B$ 是子半群，当且仅当

$$
\forall a, b \in B, \quad a \circ b \in B.
$$

结合律由 $S$ 遗传给 $B$，故只需验证封闭性。

**性质**：若干子半群的非空交集仍是子半群；若干子幺半群的交集仍是子幺半群。

**定义 6（生成子半群）**：设 $\langle S, \circ \rangle$ 是半群，$B \subseteq S$。
包含 $B$ 的一切子半群的交集

$$
B' = \bigcap \{ A \mid A \text{ 是 } S \text{ 的子半群，} B \subseteq A \}
$$

是包含 $B$ 的最小子半群，称为由 $B$ **生成的子半群**。它恰由 $B$ 中元素的一切有限
乘积构成：

$$
B' = \bigcup_{n \geq 1} B^n, \qquad
B^n = \{ b_1 \circ b_2 \circ \cdots \circ b_n \mid b_i \in B \}.
$$

## 可消去半群

**定义 7（可消去半群）**：设 $\langle S, \circ \rangle$ 是半群。若对一切
$a, b, c \in S$，

$$
a \circ b = a \circ c \Rightarrow b = c, \qquad
b \circ a = c \circ a \Rightarrow b = c,
$$

即左、右消去律都成立，则称 $S$ 为**可消去半群**（满足消去律的半群）。

!!! note "消去律与零元"

    由 [代数系统](algebraic_system.md) 定理 3，满足消去律的运算不含零元（除非
    $|S| = 1$）。直观地说，消去律说明"乘以 $a$"这一操作不丢失信息。

**定理 4（有限可消去半群是群）**：设 $\langle S, \circ \rangle$ 是有限半群且满足
消去律，则 $S$ 是群。

**证明思路**：对固定的 $a \in S$，左乘映射 $x \mapsto a \circ x$ 由消去律是单射，
有限集合上的单射是双射，故方程 $a x = b$ 恒有解；右乘同理。再由 [群](group.md)
定理 4 知 $S$ 是群。$\square$

## 半群的同态与同构

**定义 8（半群同态）**：设 $\langle S, \circ \rangle$、$\langle T, * \rangle$ 是
半群，映射 $f : S \to T$ 若满足

$$
f(x \circ y) = f(x) * f(y) \quad (\forall x, y \in S),
$$

则称 $f$ 为**半群同态**。双射的半群同态称为**半群同构**。

**定义 9（幺半群同态）**：设 $\langle S, \circ, e \rangle$、$\langle T, *, e'
\rangle$ 是幺半群，半群同态 $f$ 若还满足 $f(e) = e'$，称为**幺半群同态**。

!!! warning "半群同态未必保持单位元"

    一般的半群同态不必把单位元映到单位元。例如 $f : \mathbb{Z} \to \mathbb{Z}$，
    $f(x) = 0$ 是乘法幺半群 $\langle \mathbb{Z}, \cdot \rangle$ 到自身的半群同态
    （$f(xy) = 0 = f(x)f(y)$），但 $f(1) = 0 \neq 1$。因此在幺半群范畴中，同态的定义
    必须显式要求 $f(e) = e'$。

**定理 5（表示定理）**：设 $\langle S, *, e \rangle$ 是幺半群，$S^S$ 是 $S$ 上一切
映射（关于合成 $\circ$ 构成幺半群）。定义

$$
\varphi : S \to S^S, \qquad \varphi(a) = f_a, \quad f_a(x) = a * x,
$$

则 $\varphi$ 是单射幺半群同态，故 $\langle S, *, e \rangle$ 同构于 $\langle S^S,
\circ \rangle$ 的某个子幺半群（即 $S$ 上的一个**变换幺半群**）。

**证明**：若 $f_a = f_b$，取 $x = e$ 得 $a = b$，故 $\varphi$ 单射。又

$$
\varphi(a * b)(x) = (a * b) * x = a * (b * x) = f_a(f_b(x)) =
\varphi(a) \circ \varphi(b)(x),
$$

且 $f_e = I_S$ 是恒等映射，故 $\varphi$ 保持乘法与单位元。$\square$

!!! note "Cayley 定理的半群版本"

    每个幺半群都能"忠实"地实现为某个变换幺半群的子幺半群——与群论中 Cayley 定理
    （每个群同构于一个变换群，见 [群](group.md)）完全平行。对不含单位元的半群，先按
    定理 1 扩张为幺半群再表示，可知每个半群同构于某个变换半群的子半群。

## 直积与商

**定理 6（直积）**：半群的直积仍是半群；幺半群的直积仍是幺半群。具体地，设
$\langle S_1, \circ_1 \rangle$、$\langle S_2, \circ_2 \rangle$ 是半群，在
$S_1 \times S_2$ 上定义

$$
(a_1, a_2) \circ (b_1, b_2) = (a_1 \circ_1 b_1,\ a_2 \circ_2 b_2),
$$

则 $\langle S_1 \times S_2, \circ \rangle$ 是半群；若两个因子都是幺半群，则
$(e_1, e_2)$ 是直积的单位元。

**商半群与商幺半群**：设 $R$ 是半群 $\langle A, \circ \rangle$ 上的同余关系（见
[代数系统](algebraic_system.md) 定义 11），则

- $\langle A/R, \bar{\circ} \rangle$ 是半群，称为**商半群**，其中
  $\bar{\circ}([a], [b]) = [a \circ b]$；
- 若 $A$ 是幺半群，则 $\langle A/R, \bar{\circ}, [e] \rangle$ 是**商幺半群**。

由同态基本定理，商半群是原半群的同态像；反之，半群的任何同态像都同构于某个商半群。

## 延伸阅读

- [代数系统](algebraic_system.md) — 半群定义所依赖的运算、封闭性与同态概念。
- [群](group.md) — 半群添加单位元与逆元公理后的完整结构。
- [集合论](../../foundations/set_theory/index.md) — 半群的载体是集合，直积与商集
  构造来自集合论。
- [符号表](../../notation/index.md) — $\circ$、$\oplus$ 等运算记号约定。
