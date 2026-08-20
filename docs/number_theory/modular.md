---
title: 模运算
tags:
  - 数论
---

# 模运算

模运算("取余数"的算术)把整数按余数分类,使得"无穷多个整数"的问题化为"有限多个剩余类"的问题。它是数论通向算法、密码学与代数的枢纽:同余、逆元、Euler 定理与中国剩余定理都建立在本页。前置内容见 [初等数论基础](basic.md)。

## 同余:把余数当作相等

**定义 1(同余)** 设 $m$ 是正整数,$a, b \in \mathbb{Z}$。若 $m \mid (a - b)$,则称 $a$ 与 $b$ **模 $m$ 同余**,记作

$$
a \equiv b \pmod{m},
$$

并称 $m$ 为**模数**。等价地,$a$ 与 $b$ 除以 $m$ 的余数相同。

!!! note "钟面直觉"

    模 $12$ 的算术就是钟表算术:13 点即 1 点,因为 $13 = 12 + 1$。星期几、月份、24 小时制都是模运算的日常实例。同余把"相差一个模数的整数倍"视为"相等"。

**例 1** $17 \equiv 3 \pmod{7}$($17 - 3 = 14$ 被 $7$ 整除);$-3 \equiv 11 \pmod{7}$;同余是等价关系:自反、对称、传递,其等价类称为**剩余类**,每个剩余类恰含一个 $0 \le r < m$ 的代表元 $r$。

**定理 1(同余保持四则运算中的加、减、乘)** 若 $a \equiv b \pmod{m}$ 且 $c \equiv d \pmod{m}$,则

$$
a + c \equiv b + d \pmod{m}, \qquad a - c \equiv b - d \pmod{m}, \qquad ac \equiv bd \pmod{m}.
$$

*证明*:由 $a - b = mk$、$c - d = ml$,得 $(a + c) - (b + d) = m(k + l)$;而 $ac - bd = a(c - d) + d(a - b) = m(al + dk)$。∎

**推论 1(幂运算保持同余)** 若 $a \equiv b \pmod{m}$,则对任意正整数 $n$ 有 $a^n \equiv b^n \pmod{m}$。

**例 2** 计算 $7^{100} \bmod 5$:先看 $7 \equiv 2 \pmod{5}$,而 $2^4 = 16 \equiv 1 \pmod{5}$,故 $7^{100} \equiv 2^{100} = (2^4)^{25} \equiv 1^{25} \equiv 1 \pmod{5}$。策略是"边算边取余",避免构造天文数字。

**算法 1(快速幂,平方-乘)** 计算 $a^n \bmod m$ 只需 $O(\log n)$ 次乘法:把 $n$ 写成二进制,按位平方累乘。例如 $n = 13 = 1101_2$:依次计算 $a^1, a^2, a^4, a^8$(每次平方取模),再乘起二进制位为 $1$ 的项 $a^8 \cdot a^4 \cdot a^1$。这是 RSA 等密码算法的基础运算。

**例 3** 求 $3^{100} \bmod 7$:$\gcd(3, 7) = 1$,$\varphi(7) = 6$,而 $100 = 6 \cdot 16 + 4$,故 $3^{100} \equiv 3^4 = 81 \equiv 4 \pmod{7}$。也可用快速幂逐步验证。又如 $10^6 \bmod 7$:$10 \equiv 3$,而 $3^6 = 729 = 7 \cdot 104 + 1 \equiv 1$,故 $7 \mid 10^6 - 1 = 999999$——这个整除关系是"$1/7$ 的小数循环节为 $6$ 位"的算术根源。

!!! warning "除法不总是可行"

    从 $ac \equiv bc \pmod{m}$ **不能**推出 $a \equiv b \pmod{m}$。例如 $2 \cdot 3 \equiv 2 \cdot 5 \pmod{4}$,但 $3 \not\equiv 5 \pmod{4}$。何时可以"约去" $c$ 是本节的核心问题,答案是:当且仅当 $\gcd(c, m) = 1$(见定理 4)。

## 模 $m$ 的环结构:$\mathbb{Z}/m\mathbb{Z}$

同余把 $\mathbb{Z}$ 分成 $m$ 个剩余类,记全体剩余类为

$$
\mathbb{Z}/m\mathbb{Z} = \{\overline{0}, \overline{1}, \dots, \overline{m-1}\}.
$$

由定理 1,加法和乘法在剩余类上有良定义:

$$
\overline{a} + \overline{b} = \overline{a + b}, \qquad \overline{a} \cdot \overline{b} = \overline{ab}.
$$

**定理 2(环结构)** $(\mathbb{Z}/m\mathbb{Z}, +, \cdot)$ 是交换环:加法构成循环群,乘法满足结合律与分配律。$m$ 是素数当且仅当 $\mathbb{Z}/m\mathbb{Z}$ 是**域**(每个非零元都有乘法逆元)。

*证明思想*:"当且仅当"的实质是:$\overline{a}$ 可逆当且仅当 $\gcd(a, m) = 1$(定理 4)。$m$ 为素数时,所有 $1 \le a < m$ 都与 $m$ 互素,故每个非零元可逆;若 $m$ 合数,取 $a$ 为 $m$ 的素因子则 $\gcd(a, m) > 1$。∎

**例 4** $\mathbb{Z}/6\mathbb{Z}$ 中 $\overline{2} \cdot \overline{3} = \overline{0}$:非零元相乘得零元,这是"零因子",在域中不会出现。$\mathbb{Z}/5\mathbb{Z}$ 中 $\overline{2}^{-1} = \overline{3}$,因为 $2 \cdot 3 = 6 \equiv 1$。环与域的一般理论见 [环](../algebra/structures/ring.md) 与 [域](../algebra/structures/field.md)。

**定义 2(单位群)** $\mathbb{Z}/m\mathbb{Z}$ 中所有可逆元组成乘法群,记作 $(\mathbb{Z}/m\mathbb{Z})^\times$,其阶恰为 $\varphi(m)$(Euler 函数,见下文)。例如 $(\mathbb{Z}/10\mathbb{Z})^\times = \{\overline{1}, \overline{3}, \overline{7}, \overline{9}\}$,阶为 $4$。

## 线性同余方程

**定义 3(线性同余方程)** 形如

$$
ax \equiv b \pmod{m}
$$

的方程称为**线性同余方程**。解的存在性与个数完全由 $\gcd(a, m)$ 决定。

**定理 3(线性同余方程的解)** 设 $d = \gcd(a, m)$。方程 $ax \equiv b \pmod{m}$ 有解,当且仅当 $d \mid b$。若有解,则恰有 $d$ 个模 $m$ 两两不同余的解。

*证明*:$ax \equiv b \pmod{m}$ 等价于存在整数 $y$ 使 $ax - my = b$。由 Bezout 恒等式(见 [初等数论基础](basic.md) 定理 3),$ax - my$ 的取值恰是 $d$ 的一切倍数,故 $d \mid b$ 是充要条件。有解时,先求出特解 $x_0$,则全部解为

$$
x = x_0 + \frac{m}{d} t, \qquad t = 0, 1, \dots, d - 1,
$$

它们模 $m$ 两两不同余。∎

**例 5** 解 $6x \equiv 4 \pmod{10}$:$\gcd(6, 10) = 2 \mid 4$,有解。先解 $3x \equiv 2 \pmod{5}$,得 $x_0 = 4$(因 $3 \cdot 4 = 12 \equiv 2$);全部解为 $x = 4 + 5t$,$t = 0, 1$,即 $x \equiv 4, 9 \pmod{10}$。检验:$6 \cdot 4 = 24 \equiv 4$,$6 \cdot 9 = 54 \equiv 4$。

**例 6(无解的情形)** $2x \equiv 1 \pmod{4}$:$\gcd(2, 4) = 2 \nmid 1$,无解——$2x$ 模 $4$ 只能是 $0$ 或 $2$,永远不是 $1$。直观上,约数不整除常数项时,方程"失配"。

## 逆元与 Euler 定理

**定义 4(模逆元)** 若 $ax \equiv 1 \pmod{m}$,则称 $x$ 是 $a$ **模 $m$ 的逆元**,记作 $a^{-1} \pmod{m}$。

**定理 4(逆元存在性)** $a$ 模 $m$ 有逆元,当且仅当 $\gcd(a, m) = 1$。

*证明*:由定理 3 取 $b = 1$,解存在当且仅当 $\gcd(a, m) \mid 1$。∎

逆元可由**扩展 Euclid 算法**求出:解 Bezout 恒等式 $ax + my = 1$,则 $x$ 即 $a^{-1} \pmod{m}$。

**例 7** 求 $7^{-1} \pmod{11}$:Euclid 链 $11 = 7 + 4$、$7 = 4 + 3$、$4 = 3 + 1$,回代得 $1 = 4 - 3 = 4 - (7 - 4) = 2 \cdot 4 - 7 = 2 \cdot (11 - 7) - 7 = 2 \cdot 11 - 3 \cdot 7$,故 $7 \cdot (-3) \equiv 1 \pmod{11}$,即 $7^{-1} \equiv -3 \equiv 8 \pmod{11}$。检验:$7 \cdot 8 = 56 \equiv 1 \pmod{11}$。

**定义 5(Euler 函数)** 对正整数 $n$,$\varphi(n)$ 表示 $1$ 到 $n$ 中与 $n$ 互素的整数个数,即 $\mathbb{Z}/n\mathbb{Z}$ 中可逆元的个数。若 $n = \prod p_i^{e_i}$,则

$$
\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right).
$$

**例 8** $\varphi(10) = 10 \cdot (1 - 1/2)(1 - 1/5) = 4$,$1, 3, 7, 9$ 恰是与 $10$ 互素的四个数;$\varphi(p) = p - 1$ 对素数 $p$ 成立;$\varphi(12) = 12 \cdot (1 - 1/2)(1 - 1/3) = 4$。

**命题 1(积性)** 若 $\gcd(m, n) = 1$,则 $\varphi(mn) = \varphi(m)\varphi(n)$。例如 $\varphi(15) = \varphi(3)\varphi(5) = 2 \cdot 4 = 8$(与 $15$ 互素的是 $1, 2, 4, 7, 8, 11, 13, 14$)。积性由中国剩余定理的环同构 $\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ 直接得出:两边可逆元的个数相乘。

**定理 5(Euler 定理)** 设 $\gcd(a, n) = 1$。则

$$
a^{\varphi(n)} \equiv 1 \pmod{n}.
$$

*证明*:设 $\mathbb{Z}/n\mathbb{Z}$ 中可逆元的全体为 $U = \{u_1, \dots, u_{\varphi(n)}\}$。因 $a$ 可逆,映射 $u \mapsto au$ 是 $U$ 上的双射(若 $au_i = au_j$,两边乘 $a^{-1}$ 得 $u_i = u_j$),故

$$
\prod_{i=1}^{\varphi(n)} u_i \equiv \prod_{i=1}^{\varphi(n)} (a u_i) \equiv a^{\varphi(n)} \prod_{i=1}^{\varphi(n)} u_i \pmod{n}.
$$

两边"约去" $\prod u_i$(它在模 $n$ 下可逆),得 $a^{\varphi(n)} \equiv 1$。∎

*证明的关键思想*:**乘法群上的平移是双射**——把"所有可逆元乘一遍"与"先乘 $a$ 再乘一遍"比较,乘积不变,从而消去。这正是 Lagrange 定理(群的阶与元素的阶的关系)在单位群上的体现,参见 [群](../algebra/structures/group.md)。

**推论 2(Fermat 小定理)** 取 $n = p$ 素数,则 $\varphi(p) = p - 1$,得 $a^{p-1} \equiv 1 \pmod{p}$($p \nmid a$)。Euler 定理是 Fermat 小定理的直接推广。

**例 9** 求 $7^{222} \bmod 10$:$\gcd(7, 10) = 1$,$\varphi(10) = 4$,$222 = 4 \cdot 55 + 2$,故 $7^{222} \equiv 7^2 = 49 \equiv 9 \pmod{10}$。$7$ 的幂模 $10$ 以 $4$ 为周期:$7, 9, 3, 1, 7, \dots$。

**推论 3(幂的化简)** 若 $\gcd(a, n) = 1$,则 $a^k \bmod n$ 只依赖 $k \bmod \varphi(n)$。这是 RSA 密码体制的数学基础:加密 $c \equiv m^e \pmod{n}$,解密 $m \equiv c^d \pmod{n}$,其中 $ed \equiv 1 \pmod{\varphi(n)}$。

## 中国剩余定理

**定理 6(中国剩余定理)** 设 $m_1, m_2, \dots, m_k$ **两两互素**,则对任意整数 $b_1, \dots, b_k$,同余方程组

$$
x \equiv b_1 \pmod{m_1}, \quad x \equiv b_2 \pmod{m_2}, \quad \dots, \quad x \equiv b_k \pmod{m_k}
$$

在模 $M = m_1 m_2 \cdots m_k$ 下有**唯一**解。

*证明(构造性)*:令 $M_i = M / m_i$。因 $m_i$ 与 $M_i$ 互素,$M_i$ 模 $m_i$ 有逆元 $y_i$($M_i y_i \equiv 1 \pmod{m_i}$)。构造

$$
x = \sum_{i=1}^k b_i M_i y_i.
$$

对固定的 $j$:当 $i \ne j$ 时 $M_i$ 被 $m_j$ 整除,故模 $m_j$ 下 $x \equiv b_j M_j y_j \equiv b_j$。即 $x$ 满足每个方程。唯一性:若 $x, x'$ 都是解,则 $m_i \mid (x - x')$ 对每个 $i$ 成立,两两互素推出 $M \mid (x - x')$。∎

*证明的关键思想*:**正交化**——构造"第 $i$ 项只在第 $i$ 个方程中起作用"的基元 $M_i y_i$,像坐标分解一样把方程逐条解耦。

**例 10** 解 $x \equiv 2 \pmod{3}$,$x \equiv 3 \pmod{5}$,$x \equiv 2 \pmod{7}$。

$M = 105$,$M_1 = 35$,$M_2 = 21$,$M_3 = 15$。求逆:$35 \equiv 2 \pmod{3}$,$2^{-1} \equiv 2$;$21 \equiv 1 \pmod{5}$,$y_2 = 1$;$15 \equiv 1 \pmod{7}$,$y_3 = 1$。故

$$
x = 2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1 = 140 + 63 + 30 = 233 \equiv 23 \pmod{105}.
$$

检验:$23 \equiv 2 \pmod{3}$,$23 \equiv 3 \pmod{5}$,$23 \equiv 2 \pmod{7}$。✓

**例 11(应用)** 求满足"除以 3 余 2、除以 5 余 3"的所有正整数:解 $x \equiv 2 \pmod{3}$,$x \equiv 3 \pmod{5}$,得 $x \equiv 8 \pmod{15}$,即 $8, 23, 38, \dots$。这是古代"物不知数"问题的核心。

**例 12(逆元不全为 1 的情形)** 解 $x \equiv 1 \pmod{4}$,$x \equiv 2 \pmod{3}$:$M = 12$,$M_1 = 3$,$M_2 = 4$。$3$ 模 $4$ 的逆元是 $3$(因 $3 \cdot 3 = 9 \equiv 1$),$4$ 模 $3$ 的逆元是 $1$。故 $x = 1 \cdot 3 \cdot 3 + 2 \cdot 4 \cdot 1 = 9 + 8 = 17 \equiv 5 \pmod{12}$。检验:$5 \equiv 1 \pmod{4}$,$5 \equiv 2 \pmod{3}$。✓

!!! note "中国剩余定理的意义"

    它把"模一个大数"分解成"模若干个互素的小数",反之亦然:求解、取幂、比较大小都可以按分量进行。在算法与密码学中,它使大数运算快数倍(如 RSA 的 CRT 加速);在代数学中,它给出环同构 $\mathbb{Z}/M\mathbb{Z} \cong \prod \mathbb{Z}/m_i\mathbb{Z}$。若模数不两两互素,方程组有解当且仅当"相容条件" $b_i \equiv b_j \pmod{\gcd(m_i, m_j)}$ 对所有 $i, j$ 成立,此时解模 $\operatorname{lcm}$ 唯一。

## 原根(简介)

**定义 6(原根)** 设 $\gcd(g, n) = 1$。若 $g$ 的幂 $g^0, g^1, \dots, g^{\varphi(n)-1}$ 模 $n$ 跑遍所有与 $n$ 互素的剩余类,则称 $g$ 是模 $n$ 的**原根**。

原根存在当且仅当 $n = 2, 4, p^k, 2p^k$($p$ 为奇素数)。例如模 $7$ 的原根是 $3$:$3^1, 3^2, \dots, 3^6 \equiv 3, 2, 6, 4, 5, 1 \pmod{7}$,恰好是所有非零剩余类。原根使模 $p$ 的乘法群成为循环群,是离散对数问题与 Diffie–Hellman 密钥交换的基础:给定 $g$ 与 $g^x \bmod p$,恢复 $x$(离散对数)在 $p$ 很大时被认为计算上不可行。

## 小结

模运算把整数算术投影到有限环 $\mathbb{Z}/m\mathbb{Z}$ 上:同余保持加减乘,除法被"逆元"取代(定理 4),Euler 定理给出幂的周期性,中国剩余定理把复合模数分解为互素分量。它们是数论与密码学的共同基石。

## 延伸阅读

- [初等数论基础](basic.md):整除、Euclid 算法与 Bezout 恒等式
- [素数](primes.md):Fermat 小定理、Wilson 定理与素数判定
- [环](../algebra/structures/ring.md):$\mathbb{Z}/m\mathbb{Z}$ 的代数背景
- [群](../algebra/structures/group.md):$\mathbb{Z}/m\mathbb{Z}$ 中单位群的群论结构
