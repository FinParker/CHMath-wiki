---
title: 代数系统
tags:
  - 代数
---

# 代数系统

代数系统是代数学最基本的框架：一个集合，配上若干运算，再加上这些运算满足的公理。
群、环、域等具体结构都可以看作"代数系统 + 额外公理"的特例。理解代数系统，就等于
理解了同态、同构、子代数、商代数这些贯穿全部代数的核心概念。

## 运算

### n 元运算

**定义 1（n 元运算）**：设 $A$ 是非空集合，映射 $f : A^n \to A$ 称为 $A$ 上的一个
**n 元运算**。常用的特例有：

- $n = 0$：**0 元运算** $f : \{\emptyset\} \to A$，效果是从 $A$ 中选出一个固定元素
  （常量）；
- $n = 1$：**一元运算** $f : A \to A$，如取补、取负；
- $n = 2$：**二元运算** $f : A \times A \to A$，如加法、乘法、集合交并。

**定义 2（封闭性）**：由 $f : A^n \to A$ 的定义，$A$ 中任意 $n$ 个元素运算的结果仍在
$A$ 中，这一性质称为 $A$ 对运算 $f$ **封闭**。封闭性是讨论"$A$ 上的运算"的前提：
若结果跑出 $A$，运算就不能定义在 $A$ 上。

!!! note "二元运算的两种写法"

    二元运算常用中缀记号 $x \circ y$ 代替 $f(x, y)$。当运算由上下文清楚时，也直接写
    $xy$（乘法记号）或 $x + y$（加法记号）。

**例 1**：实数集 $\mathbb{R}$ 上的二元运算

$$
x \circ y = x + y - 2xy.
$$

容易验证 $\circ$ 满足交换律。进一步，若取 $x = y = 1$，则 $1 \circ 1 = 0$，可见这里的
$\circ$ 与通常的加法、乘法都不同——运算由公理刻画，而不由记号决定。

**例 2（运算表）**：设 $A = P(\{a, b\})$ 为集合 $\{a, b\}$ 的幂集，其上的二元运算
$\oplus$ 取对称差 $X \oplus Y = (X \setminus Y) \cup (Y \setminus X)$，一元运算
$\sim$ 取补集。它们可以用运算表表示：

| $\oplus$      | $\varnothing$ | $\{a\}$ | $\{b\}$   | $\{a, b\}$ |
| ------------- | ------------- | ------- | --------- | ---------- |
| $\varnothing$ | $\varnothing$ | $\{a\}$ | $\{b\}$   | $\{a, b\}$ |
| $\{a\}$       | $\{a\}$       | $\varnothing$ | $\{a, b\}$ | $\{b\}$ |
| $\{b\}$       | $\{b\}$       | $\{a, b\}$ | $\varnothing$ | $\{a\}$ |
| $\{a, b\}$    | $\{a, b\}$    | $\{b\}$ | $\{a\}$   | $\varnothing$ |

| $X$        | $\sim X$   |
| ---------- | ---------- |
| $\varnothing$ | $\{a, b\}$ |
| $\{a\}$    | $\{b\}$    |
| $\{b\}$    | $\{a\}$    |
| $\{a, b\}$ | $\varnothing$ |

运算表是有限集合上二元运算的完整描述：第 $i$ 行第 $j$ 列交叉处就是 $a_i \circ a_j$
的结果。

### 运算律

设 $\circ$、$*$ 是集合 $A$ 上的二元运算，常见的运算律如下：

| 运算律 | 表达式 |
| ------ | ------ |
| 交换律 | $\forall a, b \in A,\ a \circ b = b \circ a$ |
| 结合律 | $\forall a, b, c \in A,\ (a \circ b) \circ c = a \circ (b \circ c)$ |
| 幂等律 | $\forall a \in A,\ a \circ a = a$ |
| 左分配律 | $\forall a, b, c \in A,\ a \circ (b * c) = (a \circ b) * (a \circ c)$ |
| 右分配律 | $\forall a, b, c \in A,\ (b * c) \circ a = (b \circ a) * (c \circ a)$ |
| 吸收律 | $\circ$、$*$ 可交换时，$\forall a, b \in A,\ a \circ (a * b) = a$ 且 $a * (a \circ b) = a$ |
| 消去律 | $\forall a, b, c \in A,\ a \circ b = a \circ c \Rightarrow b = c$ 且 $b \circ a = c \circ a \Rightarrow b = c$ |

!!! note "用运算表检验运算律"

    交换律、幂等律可以直接从运算表读出：交换律要求表关于主对角线对称。结合律无法一眼
    看出，需对一切 $a, b, c$ 验证 $(a \circ b) \circ c = a \circ (b \circ c)$，
    相当于核对 $n^3$ 次等式。

## 单位元、零元与逆元

**定义 3（单位元）**：设 $\circ$ 是 $A$ 上的二元运算，若存在 $e \in A$ 使对一切
$a \in A$ 有 $a \circ e = e \circ a = a$，则称 $e$ 为 $\circ$ 的**单位元**。

**定义 4（零元）**：若存在 $\theta \in A$ 使对一切 $a \in A$ 有
$a \circ \theta = \theta \circ a = \theta$，则称 $\theta$ 为 $\circ$ 的**零元**。

**定理 1（单位元与零元的唯一性）**：二元运算的单位元若存在则唯一；零元若存在则唯一。

**证明**：若 $e_1, e_2$ 都是单位元，则 $e_1 = e_1 \circ e_2 = e_2$。零元同理。$\square$

**定义 5（逆元）**：设 $\circ$ 有单位元 $e$。对 $x \in A$，若存在 $y \in A$ 使
$x \circ y = y \circ x = e$，则称 $y$ 是 $x$ 的**逆元**，记作 $x^{-1}$（加法记号下记作
$-x$）。

**定理 2（逆元唯一性）**：设 $\circ$ 是 $A$ 上可结合的二元运算，$e$ 是单位元。若
$x \in A$ 存在左逆 $y_l$ 与右逆 $y_r$，使 $y_l \circ x = x \circ y_r = e$，则
$y_l = y_r$，且 $x$ 的逆元唯一。

**证明**：由结合律，

$$
y_l = y_l \circ e = y_l \circ (x \circ y_r) = (y_l \circ x) \circ y_r = e \circ y_r = y_r.
$$

若 $y_1, y_2$ 都是 $x$ 的逆元，则 $y_1 = y_1 \circ e = y_1 \circ (x \circ y_2) =
(y_1 \circ x) \circ y_2 = y_2$。$\square$

!!! warning "易错点"

    逆元的唯一性依赖结合律。若运算不结合，同一元素可能有多于一个逆元。例如在
    $A = \{e, a, b\}$ 上定义：$e$ 是单位元（$e \circ x = x \circ e = x$），且
    $a, b$ 之间的一切乘积都等于 $e$（$a \circ a = a \circ b = b \circ a = b \circ
    b = e$）。则 $a \circ a = e$ 且 $b \circ a = e$，故 $a$ 与 $b$ 都是 $a$ 的
    逆元；而 $(a \circ a) \circ b = e \circ b = b$，$a \circ (a \circ b) = a
    \circ e = a$，结合律不成立。

**定理 3（消去律与零元）**：设 $\circ$ 是 $A$ 上的二元运算。

1. 若 $\circ$ 满足消去律且 $|A| > 1$，则 $A$ 中不存在零元；
2. 若 $\theta$ 是 $\circ$ 的零元且 $|A| > 1$，则 $\circ$ 不满足消去律。

**证明**：若 $\theta$ 是零元，则对任意 $b, c \in A$ 都有 $\theta \circ b = \theta =
\theta \circ c$；当 $|A| > 1$ 时取 $b \neq c$，消去律即被破坏。反之，若消去律成立，
零元的存在会使 $\theta \circ b = \theta \circ c$ 迫使 $b = c$，矛盾。$\square$

!!! note "含零元的代数系统不能是群"

    群要求消去律成立（见 [群](group.md) 定理 5），故非平凡群不含零元。例如
    $\langle \mathbb{Z}_5, \otimes \rangle$（模 5 乘法）因含零元 $0$ 而不是群。

## 代数系统、子代数与积代数

**定义 6（代数系统）**：由集合 $A$ 与 $A$ 上若干运算 $o_1, o_2, \ldots, o_r$（连同
它们满足的公理）组成的整体 $\mathbf{V} = \langle A, o_1, o_2, \ldots, o_r \rangle$
称为**代数系统**，其中 $o_i$ 是 $k_i$ 元运算。

两个代数系统若对应运算的元数相同，称为**同类型**的；若还满足相同的公理，称为
**同种**的。代数系统的"成分 + 公理"两要素决定了结构的性质。

**定义 7（子代数）**：设 $\mathbf{V} = \langle A, o_1, \ldots, o_r \rangle$ 是代数
系统，$B$ 是 $A$ 的非空子集。若 $B$ 对 $\mathbf{V}$ 中一切运算（含 0 元运算）封闭，
则 $\mathbf{V}' = \langle B, o_1, \ldots, o_r \rangle$ 是 $\mathbf{V}$ 的**子代数**；
若 $B \subsetneq A$，称为**真子代数**。

!!! note "0 元运算与子代数"

    0 元运算选出的是一个常量元素。子代数要求对 0 元运算封闭，即该常量必须属于 $B$。
    例如子群必须包含单位元，正是这个道理。

**定义 8（积代数）**：设 $\mathbf{V}_1 = \langle A, o_1, \ldots, o_r \rangle$ 与
$\mathbf{V}_2 = \langle B, o_1', \ldots, o_r' \rangle$ 是同类型的代数系统，在直积
$A \times B$ 上按分量定义运算：

$$
o_i''\big((a_1, b_1), \ldots, (a_{k_i}, b_{k_i})\big) =
\big(o_i(a_1, \ldots, a_{k_i}),\ o_i'(b_1, \ldots, b_{k_i})\big),
$$

得到的代数系统称为 $\mathbf{V}_1$ 与 $\mathbf{V}_2$ 的**积代数**。

**性质**：

1. 积代数与因子代数同类型；若公理不含消去律，积代数与因子代数同种；
2. **消去律不一定保持**：例如 $\langle \mathbb{Z}, \cdot \rangle$ 满足消去律，但
   $\mathbb{Z} \times \mathbb{Z}$ 中 $(1, 0) \cdot (a, b) = (a, 0)$ 抹去了第二分量，
   消去律失效；
3. 积代数可以推广到有限多个同类型代数系统的直积；
4. 直积分解是研究代数结构的常用手段：把一个复杂结构拆成简单结构的积。

## 同态与同构

**定义 9（同态）**：设 $\mathbf{V}_1 = \langle A, o_1, \ldots, o_r \rangle$ 与
$\mathbf{V}_2 = \langle B, o_1', \ldots, o_r' \rangle$ 是同类型的代数系统，映射
$f : A \to B$ 若对每个 $k_i$ 元运算都满足

$$
f\big(o_i(a_1, \ldots, a_{k_i})\big) =
o_i'\big(f(a_1), \ldots, f(a_{k_i})\big),
$$

则称 $f$ 是 $\mathbf{V}_1$ 到 $\mathbf{V}_2$ 的**同态**。对二元运算，同态条件即
"先运算后映射等于先映射后运算"：$f(a \circ b) = f(a) \circ' f(b)$。

**定义 10（同态的强弱）**：

- 单射的同态称为**单同态**；满射的同态称为**满同态**，记作 $\mathbf{V}_1 \sim
  \mathbf{V}_2$；
- 双射的同态称为**同构**，记作 $\mathbf{V}_1 \cong \mathbf{V}_2$；
- 同构意义下相同的代数系统具有完全相同的结构性质；
- 到自身的同态（同构）称为**自同态**（**自同构**）。

**例 3**：考虑 $\mathbf{V} = \langle \mathbb{Z}_6, \oplus \rangle$（模 6 加法），
$f_p : \mathbb{Z}_6 \to \mathbb{Z}_6$，$f_p(x) = px \pmod 6$，$p = 0, 1, \ldots, 5$。
因

$$
f_p(x \oplus y) = p(x \oplus y) \equiv px \oplus py \pmod 6 = f_p(x) \oplus f_p(y),
$$

每个 $f_p$ 都是自同态。其中 $f_0$ 是零同态；$f_1$ 是恒等映射，为自同构；$f_5$（取负）
也是自同构；其余不是双射，只是自同态。推广之，$\mathbb{Z}_n$ 恰好有 $n$ 个自同态
$f_p(x) = px \pmod n$，其中自同构对应于与 $n$ 互素的 $p$。

**定理 4（同态的性质）**：设 $f$ 是 $\mathbf{V}_1$ 到 $\mathbf{V}_2$ 的同态。

1. 同态的合成仍是同态；
2. 同态像 $f(A)$ 是 $\mathbf{V}_2$ 的子代数；
3. 若 $f$ 是满同态，则 $f$ 保持 $\mathbf{V}_1$ 的交换律、结合律、幂等律、分配律、
   吸收律，以及单位元、零元、逆元（$[f(a)]^{-1} = f(a^{-1})$）；**消去律不一定保持**
   （例如 $\mathbb{Z}_6$ 的零同态像只有 $\{0\}$，消去律不成立）。

## 同余关系与商代数

**定义 11（同余关系）**：设 $\mathbf{V} = \langle A, o_1, \ldots, o_r \rangle$ 是
代数系统，$R$ 是 $A$ 上的等价关系。若对每个 $k_i$ 元运算 $o_i$，由
$a_j R b_j$（$j = 1, \ldots, k_i$）总能推出

$$
o_i(a_1, \ldots, a_{k_i}) \ R \ o_i(b_1, \ldots, b_{k_i}),
$$

则称 $R$ 对运算 $o_i$ 具有**置换性质**。若 $R$ 对 $\mathbf{V}$ 的一切运算都有置换
性质，称 $R$ 为 $\mathbf{V}$ 上的**同余关系**，其等价类称为**同余类**。

恒等关系与全域关系都是同余关系，因此任何代数系统都存在同余关系。

**定义 12（商代数）**：设 $R$ 是 $\mathbf{V} = \langle A, o_1, \ldots, o_r \rangle$
上的同余关系，则

$$
\mathbf{V}/R = \langle A/R,\ \bar{o}_1, \ldots, \bar{o}_r \rangle,
\quad
\bar{o}_i([a_1], \ldots, [a_{k_i}]) = [o_i(a_1, \ldots, a_{k_i})],
$$

称为 $\mathbf{V}$ 关于 $R$ 的**商代数**。只有同余关系（而非任意等价关系）才能保证
$\bar{o}_i$ 的**良定义性**——即运算结果不依赖代表元的选取。

**定理 5（商代数的性质）**：设 $R$ 是 $\mathbf{V}$ 上的同余关系。

1. $\mathbf{V}/R$ 保持 $\mathbf{V}$ 的交换律、结合律、幂等律、分配律、吸收律；
2. $\mathbf{V}/R$ 保持 $\mathbf{V}$ 的单位元、零元与逆元：$[e]$ 是单位元，
   $[\theta]$ 是零元，$[a]^{-1} = [a^{-1}]$；
3. 消去律不一定保持。例如 $\langle \mathbb{Z}, \cdot \rangle$ 有消去律，取模 4
   同余关系 $x R y \iff x \equiv y \pmod 4$，商代数 $\mathbb{Z}/R$ 中
   $[2] \cdot [2] = [0] \cdot [2]$，但 $[2] \neq [0]$。

## 同态基本定理

同态与同余关系通过"核"相互对应：

1. 每个同态 $f$ 都导出一个同余关系：$x R y \iff f(x) = f(y)$；
2. 商代数通过**自然映射** $\pi : A \to A/R$，$a \mapsto [a]$，是原代数的同态像；
3. 反过来，每个同余关系都是其自然映射的核。

**定理 6（同态基本定理）**：设 $\mathbf{V}_1 = \langle A, o_1, \ldots, o_r \rangle$
与 $\mathbf{V}_2 = \langle B, o_1', \ldots, o_r' \rangle$ 是同类型的代数系统，
$f : A \to B$ 是满同态，$R$ 是 $f$ 导出的同余关系（$x R y \iff f(x) = f(y)$），则

$$
\mathbf{V}_1 / R \ \cong \ \langle f(A), o_1', \ldots, o_r' \rangle = \mathbf{V}_2.
$$

**证明思路**：定义 $h : \mathbf{V}_1/R \to f(A)$，$h([a]) = f(a)$。先证 $h$ 良定义
（同余类中元素同像），再证 $h$ 是双射（满性由 $f$ 满射，单性由 $R$ 的定义），最后由
同态条件验证 $h$ 是同态。$\square$

由同态基本定理得到两个对偶的结论：

- **任何商代数都是同态像**（自然映射是满同态）；
- **任何同态像在同构意义下都是商代数**（同态像同构于由该同态导出的商代数）。

因此，刻画一个代数系统的全部同态像，等价于找出它的全部同余关系——这正是群论中
"同态像对应正规子群"（见 [群](group.md)）的雏形。

## 延伸阅读

- [半群与幺半群](semigroup.md) — 只保留结合律的代数系统，是群的最弱前提。
- [群](group.md) — 在代数系统上添加单位元与逆元公理，得到最经典的代数结构。
- [集合论](../../foundations/set_theory/index.md) — 代数系统的载体是集合，等价关系
  与商集概念来自集合论。
- [符号表](../../notation/index.md) — $\circ$、$\oplus$、$\otimes$ 等运算记号的约定。
