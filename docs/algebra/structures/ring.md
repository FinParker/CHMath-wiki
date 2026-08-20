---
title: 环
tags:
  - 代数
---

# 环

环是同时具有两种运算——加法与乘法——的代数结构：加法构成 Abel 群，乘法构成半群，
乘法对加法满足分配律。整数环 $\mathbb{Z}$ 是环的原型；多项式、矩阵、模 $n$ 剩余类
都天然地带有环的结构。环论的语言（理想、商环、同态）是代数数论与代数几何的基石。

## 环的定义

**定义 1（环）**：设 $\langle R, +, \cdot \rangle$ 是含有两个二元运算的代数系统。
若满足：

1. $\langle R, + \rangle$ 构成 Abel 群；
2. $\langle R, \cdot \rangle$ 构成半群（封闭且结合）；
3. 乘法对加法满足分配律：$\forall a, b, c \in R$，

$$
a(b + c) = ab + ac, \qquad (b + c)a = ba + ca,
$$

则称 $\langle R, +, \cdot \rangle$ 为**环**。

**环中的术语与记号**：

- $+$ 称为环的**加法**，$\cdot$ 称为环的**乘法**（常省略不写，记 $ab$）；
- 加法单位元记作 $0$，称为**零元**；加法逆元称为**负元**，记作 $-x$；
- 乘法单位元（若存在）记作 $1$；$x$ 的乘法逆元（若存在）记作 $x^{-1}$；
- 记号约定：$0, 1, -x, x^{-1}, nx, x^n, x - y$。

!!! note "加法单位元是乘法的零元"

    环中加法单位元 $0$ 恰好是乘法的零元：由 $a \cdot 0 = a(0 + 0) = a \cdot 0 +
    a \cdot 0$，两边同加 $-(a \cdot 0)$ 得 $a \cdot 0 = 0$（详见定理 1）。因此"$0$"
    一身二任：作为加法单位元，它吸收一切乘法。

**例 1（常见环）**：

- 整数环 $\mathbb{Z}$、有理数环 $\mathbb{Q}$、实数环 $\mathbb{R}$、复数环
  $\mathbb{C}$（通常加法与乘法）；
- **模 n 整数环** $\mathbb{Z}_n$（模 $n$ 加乘，$n \ge 2$）；
- **n 阶矩阵环** $M_n(R)$（$R$ 是环，矩阵加法与乘法；$n \ge 2$ 时乘法不交换）；
- **多项式环** $R[x]$（系数在 $R$ 的多项式，见 [多项式](polynomial.md)）；
- 幂集环 $\langle P(B), \oplus, \cap \rangle$（$\oplus$ 为对称差，$\cap$ 为交）。

**定理 1（环的运算性质）**：设 $R$ 是环，$a, b, c \in R$，$m, n \in \mathbb{Z}$，则

1. $a \cdot 0 = 0 \cdot a = 0$；
2. $(-a)b = a(-b) = -(ab)$；
3. $(-a)(-b) = ab$；
4. $a(b - c) = ab - ac$，$(b - c)a = ba - ca$；
5. $(na)b = a(nb) = n(ab)$；
6. $\left(\sum_{i=1}^{n} a_i\right)\left(\sum_{j=1}^{m} b_j\right) =
   \sum_{i=1}^{n}\sum_{j=1}^{m} a_i b_j$（二重和公式）。

**证明**：(1) $a \cdot 0 = a(0 + 0) = a \cdot 0 + a \cdot 0$，两边加 $-a \cdot 0$
即得；其余由分配律直接推出。$\square$

## 特殊环

**定义 2（交换环与含幺环）**：乘法满足交换律的环称为**交换环**；有乘法单位元 $1$
的环称为**含幺环**（单位环）。下文如无特别说明，"含幺交换环"指 $1 \neq 0$ 且乘法
交换的环。

**定义 3（零因子与无零因子环）**：设 $R$ 是环，$a, b \in R$，$a, b \neq 0$。若
$ab = 0$，则称 $a$（及 $b$）为 $R$ 的**零因子**。不含零因子的环称为**无零因子环**，
即

$$
ab = 0 \Rightarrow a = 0 \ \text{或}\ b = 0.
$$

**定义 4（整环）**：无零因子的含幺交换环称为**整环**。（约定：平凡环 $\{0\}$ 也是
整环。）

**定义 5（除环）**：设 $R$ 是含幺环且 $|R| > 1$（保证 $R^* = R \setminus \{0\}$
非空）。若 $\langle R^*, \cdot \rangle$ 构成群，则称 $R$ 为**除环**（体）。

**定义 6（域）**：可交换的除环称为**域**。域的完整讨论见 [域](field.md)。

!!! note "几个等价刻画"

    - 域 $\iff$ 每个非零元都有乘法逆元的整环；
    - 有限整环一定是域（见定理 2）；
    - 除环未必交换：四元数体 $\mathbb{H}$ 是最经典的例子。

**定理 2（有限整环是域）**：至少含有两个元素的无零因子有限环是除环；有限整环是域。

**证明思路**：设 $R = \{0, a_1, \ldots, a_n\}$ 是无零因子环。对非零元 $a_i$，左乘映射
$x \mapsto a_i x$ 由无零因子性（$a_i x = a_i y \Rightarrow a_i(x - y) = 0
\Rightarrow x = y$）是单射，有限集合上的单射是双射，故对任意 $b$ 方程 $a_i x = b$
有解，$R^*$ 对乘法成群。$\square$

**例 2（$\mathbb{Z}_p$ 是域当且仅当 $p$ 是素数）**：设 $p$ 为素数。$\mathbb{Z}_p$
关于模 $p$ 乘法可交换，单位元是 1。对 $i \neq 0$，由 $p \mid i(j - k)$ 与素数性质得
$p \mid (j - k)$，即消去律在 $\mathbb{Z}_p^*$ 中成立；又 $\mathbb{Z}_p^*$ 是有限
半群，由定理 2 知 $\mathbb{Z}_p$ 是域。

反之，$n$ 合数时 $\mathbb{Z}_n$ 有零因子（如 $2 \cdot 3 \equiv 0 \pmod 6$），不是
整环更不是域。

!!! warning "易错点"

    1. 含幺环中 $0$ 与 $1$ 不同（平凡环 $\{0\}$ 除外）：$0$ 吸收一切乘法，$1$ 是乘法
       单位元，二者身份不能混淆。
    2. 无零因子性对"域"是必要的：$ab = 0$ 且 $a, b \neq 0$ 的环（如 $\mathbb{Z}_6$）
       中无法做除法。

## 环的特征

**定理 3（无零因子环的特征）**：设 $R$ 是无零因子环，则 $R$ 中一切非零元的加法阶
相等，且这个加法阶或者是无穷大，或者是一个素数 $p$。

**定义 7（特征）**：设 $R$ 是无零因子环，称 $R$ 中非零元的加法阶为 $R$ 的**特征**
（characteristic），记作 $\operatorname{char} R$：非零元加法阶为无穷大时，
$\operatorname{char} R = 0$；为素数 $p$ 时，$\operatorname{char} R = p$。

等价地，$\operatorname{char} R$ 是使 $n \cdot 1 = 0$ 的最小正整数 $n$（不存在则为
0）。特征的理论在 [域](field.md) 一节展开。

**定理 4（Freshman's dream）**：设 $R$ 是特征为 $p$ 的交换环，则对一切
$a, b \in R$，

$$
(a + b)^p = a^p + b^p.
$$

**证明**：由二项式定理，$(a + b)^p = \sum_{k=0}^{p} \binom{p}{k} a^k b^{p-k}$；
对 $1 \le k \le p - 1$，$\binom{p}{k}$ 被 $p$ 整除，故中间各项在特征 $p$ 下为零。
$\square$

## 子环与理想

**定义 8（子环）**：设 $R$ 是环，$S$ 是 $R$ 的非空子集。若 $S$ 关于 $R$ 的加法与
乘法构成环，则称 $S$ 为 $R$ 的**子环**。子环就是 $R$ 的子代数；平凡子环 $\{0\}$ 与
$R$ 本身总是存在。

**定理 5（子环判定）**：设 $R$ 是环，$S$ 是 $R$ 的非空子集。则 $S$ 是 $R$ 的子环
当且仅当

1. $\forall a, b \in S$，$a - b \in S$（加法子群判定）；
2. $\forall a, b \in S$，$ab \in S$（乘法子半群判定）。

**定义 9（理想）**：设 $I$ 是环 $R$ 的非空子集。若

1. $\langle I, + \rangle$ 是 $\langle R, + \rangle$ 的子群（即
   $\forall a, b \in I$，$a - b \in I$）；
2. $\forall r \in R$，$rI \subseteq I$ 且 $Ir \subseteq I$（吸收 $R$ 的乘法），

则称 $I$ 为 $R$ 的**理想**（双边理想）。只满足 $rI \subseteq I$ 的称为**左理想**，
只满足 $Ir \subseteq I$ 的称为**右理想**。$\{0\}$ 与 $R$ 本身称为**平凡理想**。

!!! note "理想与子环的区别"

    理想是子环，但要求"吸收外部的乘法"（$rI \subseteq I$），这是构造商环的关键：
    商环的乘法 $[a][b] = [ab]$ 需要把"代表元换掉"的差吸收进 $I$，只有理想能做到。
    子环一般不能造商环。

**定理 6（理想的性质）**：

1. 理想一定是子环；
2. 若含幺环 $R$ 的理想 $I$ 含有乘法单位元 $1$，则 $I = R$；
3. 理想之交集仍是理想。

**例 3**：交换环 $R$ 中，$x \neq 0$ 时 $Rx = \{ rx \mid r \in R \}$ 是理想；
$x = 0$ 时 $\langle 0 \rangle = \{0\}$。

**例 4**：$F[x]$ 是数域 $F$ 上的多项式环，$I = \{ a_1 x + a_2 x^2 + \cdots + a_n
x^n \mid a_i \in F,\ n \in \mathbb{N} \}$（常数项为 0 的多项式全体）是 $F[x]$ 的
理想，即主理想 $\langle x \rangle$。

**定义 10（生成理想与主理想）**：设 $R$ 是环，$T$ 是 $R$ 的非空子集，$R$ 中一切
包含 $T$ 的理想的交集

$$
\langle T \rangle = \bigcap \{ I \mid I \text{ 是 } R \text{ 的理想，} I \supseteq T \}
$$

称为由 $T$ **生成的理想**，是包含 $T$ 的最小理想。$T = \{\alpha\}$ 时记作
$\langle \alpha \rangle$，称为由 $\alpha$ 生成的**主理想**。

**定理 7（主理想的结构）**：设 $R$ 是环，$\alpha \in R$，则

$$
\langle \alpha \rangle = \left\{ \sum_{i=1}^{m} x_i \alpha y_i + s\alpha + \alpha t
+ n\alpha \ \middle|\ x_i, y_i, s, t \in R,\ m \in \mathbb{N},\ n \in \mathbb{Z}
\right\}.
$$

**推论**：

1. $R$ 交换时，$\langle \alpha \rangle = \{ s\alpha + n\alpha \mid s \in R,\ n
   \in \mathbb{Z} \}$；
2. $R$ 含幺时，$\langle \alpha \rangle = \{ \sum_{i=1}^{m} x_i \alpha y_i \mid
   x_i, y_i \in R \}$；
3. $R$ 含幺交换时，$\langle \alpha \rangle = R\alpha = \{ r\alpha \mid r \in R
   \} = \alpha R$。

!!! warning "易错点"

    含幺交换环中 $\langle \alpha \rangle = R\alpha$；但**不含 $1$ 的环**中 $\alpha$
    未必属于 $R\alpha$。例如偶数环 $2\mathbb{Z}$ 中 $\langle 2 \rangle = 2\mathbb{Z}$
    （包含 $2$ 的最小理想），而 $R \cdot 2 = 4\mathbb{Z}$ 不含 $2$，故此时
    $\langle 2 \rangle \supsetneq R \cdot 2$。

## 商环

**定义 11（商环）**：设 $I$ 是环 $R$ 的理想。对 $x \in R$，记 $x$ 的加法陪集为
$\bar{x} = I + x = \{ i + x \mid i \in I \}$。定义

$$
R/I = \{ I + x \mid x \in R \},
$$

其中加法与乘法按陪集进行：

$$
(I + x) + (I + y) = I + (x + y), \qquad
(I + x)(I + y) = I + xy.
$$

则 $\langle R/I, +, \cdot \rangle$ 是环，称为 $R$ 关于 $I$ 的**商环**。

**良定义性**：乘法的良定义恰需 $I$ 是理想：若 $x' = x + i$，$y' = y + j$，则
$x'y' - xy = xj + iy + ij \in I$（由 $rI \subseteq I$ 与 $Ir \subseteq I$），故
$I + x'y' = I + xy$。

**定义 12（素理想与极大理想）**：设 $R$ 是含幺交换环。

1. 理想 $P \neq R$ 称为**素理想**，若 $ab \in P \Rightarrow a \in P$ 或 $b \in P$；
2. 理想 $M \neq R$ 称为**极大理想**，若除 $M$ 与 $R$ 外不存在包含 $M$ 的理想。

**例 5（$\mathbb{Z}$ 中的素理想与极大理想）**：$\mathbb{Z}$ 中由素数 $p$ 生成的主
理想 $\langle p \rangle = p\mathbb{Z}$ 既是素理想又是极大理想。

**证明**：若 $ab \in \langle p \rangle$，则 $p \mid ab$；由 $p$ 素数，$p \mid a$ 或
$p \mid b$，故 $\langle p \rangle$ 是素理想。又 $1 \notin \langle p \rangle$；设
$I$ 是包含 $\langle p \rangle$ 的理想且 $I \neq \langle p \rangle$，则存在
$q \in I \setminus \langle p \rangle$，$p$ 与 $q$ 互素，存在 $s, t$ 使
$sp + tq = 1$；因 $p, q \in I$ 而 $I$ 是理想，$1 \in I$，由定理 6 得 $I = R$，故
$\langle p \rangle$ 是极大理想。$\square$

**定理 8（商环刻画素理想与极大理想）**：设 $R$ 是含幺交换环，则

1. $M$ 是 $R$ 的极大理想当且仅当 $R/M$ 是域；
2. $P$ 是 $R$ 的素理想当且仅当 $R/P$ 是整环。

**推论**：$\mathbb{Z}_p$（$p$ 素数）是域，正是 $\mathbb{Z}/\langle p \rangle$ 是
域的特例。

## 环同态与同态基本定理

**定义 13（环同态）**：设 $R_1, R_2$ 是环，映射 $f : R_1 \to R_2$ 若满足

$$
f(x + y) = f(x) + f(y), \qquad f(xy) = f(x) f(y),
$$

则称 $f$ 为**环同态**。同态核定义为

$$
\ker f = \{ x \in R_1 \mid f(x) = 0 \}.
$$

**例 6**：$f_c : \mathbb{Z} \to \mathbb{Z}$，$f_c(x) = cx$ 是环同态当且仅当
$c = 0$ 或 $c = 1$（$c = 1$ 时要求 $f(1) = 1$，是含幺环同态）。$\varphi :
\mathbb{Z} \to \mathbb{Z}_n$，$\varphi(x) = x \bmod n$ 是满同态，且
$\ker\varphi = n\mathbb{Z} = \langle n \rangle$。

**定理 9（环同态的性质）**：设 $f : R_1 \to R_2$ 是环同态。

1. $f(0) = 0$，$f(-x) = -f(x)$；若 $x$ 可逆，则 $f(x^{-1}) = f(x)^{-1}$；
2. $S$ 是 $R_1$ 的子环 $\Rightarrow f(S)$ 是 $R_2$ 的子环；$T$ 是 $R_2$ 的子环
   $\Rightarrow f^{-1}(T)$ 是 $R_1$ 的子环；
3. $I$ 是 $R_1$ 的理想 $\Rightarrow f(I)$ 是 $f(R_1)$ 的理想；$J$ 是 $R_2$ 的理想
   $\Rightarrow f^{-1}(J)$ 是 $R_1$ 的理想；
4. $\ker f$ 是 $R_1$ 的理想。

**定理 10（环同态基本定理）**：设 $f : R \to R'$ 是环同态，则

$$
R / \ker f \ \cong \ f(R).
$$

特别地，对 $R$ 的任意理想 $I$，自然映射 $\pi : R \to R/I$，$x \mapsto \bar{x}$ 是
满同态，故**环的任何商环都是它的同态像**。

**证明**：与群同态基本定理（见 [群](group.md) 定理 19）完全平行：定义
$\bar{f} : R/\ker f \to f(R)$，$\bar{f}(x + \ker f) = f(x)$，验证良定义、双射与
同态性。$\square$

**定理 11（分式域）**：每个整环 $R$ 都可以嵌入某个域 $Q$（$R$ 是 $Q$ 的子环），
称为 $R$ 的**分式域**（商域）。

**构造**：令

$$
Q = \left\{ \frac{b}{a} \ \middle|\ a, b \in R,\ a \neq 0 \right\},
$$

并约定 $a = a/1$，$0/a = 0$，$bc/ac = b/a$；在 $Q$ 上定义

$$
\frac{b}{a} + \frac{d}{c} = \frac{bc + ad}{ac}, \qquad
\frac{b}{a} \cdot \frac{d}{c} = \frac{bd}{ac} \quad (a, c \neq 0),
$$

则 $Q$ 是域，$R \hookrightarrow Q$，$a \mapsto a/1$。整数环 $\mathbb{Z}$ 的分式域
就是有理数域 $\mathbb{Q}$。

**定理 12（中国剩余定理，环论版本）**：设 $R$ 是含幺交换环，$I, J$ 是 $R$ 的理想且
$I + J = R$（互素），则

$$
R / (I \cap J) \ \cong \ R/I \times R/J.
$$

**推论**：$\gcd(m, n) = 1$ 时，$\mathbb{Z}_{mn} \cong \mathbb{Z}_m \times
\mathbb{Z}_n$。数论中的中国剩余定理（同余方程组可解性）正是此结论在
$\mathbb{Z}$ 上的体现，见 [数论](../../number_theory/index.md)。

## 延伸阅读

- [群](group.md) — 环的加法结构是 Abel 群，子环、商环、同态基本定理均沿用群论框架。
- [域](field.md) — 交换除环，每个非零元可逆的环。
- [多项式](polynomial.md) — 多项式环 $F[x]$ 是最重要的环论例子。
- [数论](../../number_theory/index.md) — $\mathbb{Z}_n$、素理想与中国剩余定理。
