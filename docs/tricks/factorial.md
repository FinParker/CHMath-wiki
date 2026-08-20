---
title: 阶乘
tags:
  - 技巧
---

# 阶乘

> 阶乘 $n!$ 是"从 1 连乘到 $n$"，是最基本的计数工具，也是排列、组合与伽马函数的共同起点。
> 掌握它的增长、素因子分解与近似，能处理大量估计与整除性问题。

## 定义

**定义 1（阶乘）** 对非负整数 $n$，
$$n! = 1 \times 2 \times \cdots \times n$$
并规定 $0! = 1$。阶乘也可递归定义：
$$0! = 1, \qquad (n+1)! = (n+1) \cdot n!$$

**例 1** $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$。

!!! note
    规定 $0! = 1$ 是为了让公式自洽：$n$ 元集恰有 1 种空排列，且组合公式 $C(n, 0) = n!/(0!\, n!) = 1$ 成立。

**基本性质** 由递归定义可直接得到：

- $(n+1)! = (n+1) \cdot n!$，即 $n! = (n+1)!/(n+1)$；
- 阶乘严格递增：$0! < 1! < 2! < \cdots$；
- 对 $n \ge 4$ 有 $n! > 2^n$（数学归纳法）；
- $n!$ 是 $1, 2, \ldots, n$ 的最小公倍数的倍数，因而是其中每一个的倍数。

**例 2** $7! = 5040$，且 $7! > 2^7 = 128$。

## 组合意义

**定理 1** $n$ 个不同元素的全排列数为 $n!$；$n$ 个元素的有序 $r$ 排列数为
$$P(n, r) = \frac{n!}{(n - r)!}$$
若 $n$ 个元素中有重复（$a_i$ 出现 $n_i$ 次，$\sum n_i = n$），全排列数为
$$\frac{n!}{n_1! \, n_2! \cdots n_k!}$$

**例 3** 5 名选手竞争金、银、铜牌，领奖台排法有 $P(5, 3) = 5!/2! = 60$ 种；
从 10 人中选 4 人组成委员会（无序）有 $C(10, 4) = 10!/(4!\, 6!) = 210$ 种。

**例 4** 单词 BOOKKEEPER 的 10 个字母（O 出现 2 次、K 出现 2 次、E 出现 3 次）的全排列数为
$10!/(2! \cdot 2! \cdot 3!) = 151200$。

!!! note
    组合数 $C(n, k) = \dfrac{n!}{k!(n-k)!}$ 必为整数——它本身就是计数结果。
    这是"三个阶乘相除得到整数"这类整除结论的典型来源。

## 双阶乘

**定义 2（双阶乘）** 对正整数 $n$，
$$n!! = \begin{cases} n \cdot (n-2) \cdots 4 \cdot 2, & n \text{ 为偶数} \\ n \cdot (n-2) \cdots 3 \cdot 1, & n \text{ 为奇数} \end{cases}$$
并规定 $0!! = 1$。

**例 5** $7!! = 7 \cdot 5 \cdot 3 \cdot 1 = 105$，$6!! = 6 \cdot 4 \cdot 2 = 48$，$8!! = 8 \cdot 6 \cdot 4 \cdot 2 = 384$。

奇偶双阶乘可用阶乘表示：
$$(2n)!! = 2^n \, n!, \qquad (2n-1)!! = \frac{(2n)!}{2^n \, n!}$$
例如 $8!! = 2^4 \cdot 4! = 16 \times 24 = 384$。

## 增长与 Stirling 公式

**定理 2（Stirling 公式）** 当 $n \to \infty$ 时，
$$n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$
即两者之比趋于 1。

**证明思路** 对 $\ln n! = \sum_{k=1}^{n} \ln k$ 作积分比较（$\ln x$ 单调递增），可得
$$\ln n! = n \ln n - n + O(\ln n)$$
再以 Euler–Maclaurin 公式精细估计余项，便得到含 $\sqrt{2\pi n}$ 的渐近式。积分比较还给出常用的下界 $n! \ge (n/e)^n$。

**例 6** 用 Stirling 公式估计 $10! = 3628800$：$\sqrt{20\pi}\,(10/e)^{10} \approx 3598696$，相对误差不足 1%。

**例 7** 由 $n!/n^n \sim \sqrt{2\pi n}\, e^{-n} \to 0$ 可知级数 $\sum_{n=1}^{\infty} n!/n^n$ 收敛
（相邻项之比 $\to 1/e < 1$）。

## 伽马函数推广

**定义 3（伽马函数）** 对 $x > 0$，
$$\Gamma(x) = \int_0^\infty t^{\,x-1} e^{-t}\, dt$$

**定理 3** 对一切非负整数 $n$ 有 $\Gamma(n+1) = n!$；一般地 $\Gamma(x+1) = x\,\Gamma(x)$。

**证明（分部积分）** 对 $x > 0$，
$$\Gamma(x+1) = \int_0^\infty t^x e^{-t}\, dt = \left[-t^x e^{-t}\right]_0^\infty + x\int_0^\infty t^{x-1} e^{-t}\, dt = x\,\Gamma(x)$$
边界项为 0：$t = 0$ 处 $t^x \to 0$，$t \to \infty$ 处指数衰减占优。反复使用即得 $\Gamma(n+1) = n!$。

**例 8** $\Gamma(1) = 1 = 0!$，且 $\Gamma(1/2) = \sqrt{\pi}$。伽马函数把阶乘从整数延拓到实数与复数，
例如 $\frac{1}{2}! = \Gamma(3/2) = \sqrt{\pi}/2$。

## 素因子分解与 Legendre 公式

**定理 4（Legendre 公式）** 设 $p$ 为素数，则 $n!$ 中 $p$ 的指数为
$$v_p(n!) = \sum_{k \ge 1} \left\lfloor \frac{n}{p^k} \right\rfloor = \left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor + \left\lfloor \frac{n}{p^3} \right\rfloor + \cdots$$

**证明思路** $1$ 到 $n$ 中恰有 $\lfloor n/p^k \rfloor$ 个数含有因子 $p^k$，逐项累加即得每个数所含 $p$ 的总次数。

**例 9** $v_2(10!) = \lfloor 10/2 \rfloor + \lfloor 10/4 \rfloor + \lfloor 10/8 \rfloor = 5 + 2 + 1 = 8$；
$v_3(10!) = \lfloor 10/3 \rfloor + \lfloor 10/9 \rfloor = 3 + 1 = 4$。

**推论** 对所有不超过 $n$ 的素数求和，即得标准分解式：
$$n! = \prod_{p \le n} p^{\,v_p(n!)}$$

## 末尾零的个数

$n!$ 十进制末尾零的个数等于 $n!$ 中因子 $10 = 2 \times 5$ 的个数。由于 2 的指数总不少于 5 的指数
（$v_2(n!) \ge v_5(n!)$），末尾零数即
$$z(n) = v_5(n!) = \sum_{k \ge 1} \left\lfloor \frac{n}{5^k} \right\rfloor$$

**例 10** $100!$ 末尾零的个数：
$$z(100) = \left\lfloor \frac{100}{5} \right\rfloor + \left\lfloor \frac{100}{25} \right\rfloor + \left\lfloor \frac{100}{125} \right\rfloor = 20 + 4 + 0 = 24$$
$25!$ 的末尾零数为 $\lfloor 25/5 \rfloor + \lfloor 25/25 \rfloor = 5 + 1 = 6$。

!!! warning
    求末尾零数时只需数因子 5 的个数，不要逐个分解每个数——直接对 5 套用 Legendre 公式即可。

## 延伸阅读

- [解题技巧索引](index.md)：其他常用计算与变形技巧。
- [组合数学](../discrete_mathematics/combinatorics.md)：阶乘是排列组合的基础。
- [数论](../number_theory/index.md)：Legendre 公式与素数指数。
- [符号表](../notation/index.md)：$n!$、$\Gamma$ 等记号约定。
