---
title: 积分
tags:
  - 微积分
---

# 积分

> 积分累加无穷多个微小量：面积、路程、总量，都由定积分给出。

## 概述

如果导数是"拆细看变化"，积分就是"加总看总量"。曲线下的面积、变速运动的位移、变力做的功，本质都是同一件事：把一个量**分割成无穷多个小份再求和**。定积分把这一过程严格化，而微积分基本定理揭示了它与导数的互逆关系——这是牛顿与莱布尼茨最重要的发现，也是"微积分"二字的由来。

## 定积分的定义

### 动机：面积与路程

求曲线 $y = f(x) \ge 0$ 在 $[a, b]$ 上围成的面积：把 $[a, b]$ 分成 $n$ 段，每段上用一个细长矩形近似（高取该段某一点的函数值），所有矩形面积之和就是对面积的近似。段数越多越精确，令最大段长趋于零，极限就是面积。变速运动同理：把时间细分，每段内近似匀速，$\sum v(t_i)\Delta t_i$ 的极限就是位移。

### Riemann 和

**定义 1（定积分）** 设 $f$ 在 $[a, b]$ 上有界。取分划 $a = x_0 < x_1 < \cdots < x_n = b$，在每段 $[x_{i-1}, x_i]$ 上任取 $\xi_i$，作 Riemann 和
$$
\sum_{i=1}^{n} f(\xi_i) \Delta x_i, \qquad \Delta x_i = x_i - x_{i-1}.
$$
若当 $\lambda = \max_i \Delta x_i \to 0$ 时，上述和式**对任意取法**都趋于同一极限 $I$，则称 $f$ 在 $[a, b]$ 上可积，记
$$
\int_a^b f(x) \, \mathrm{d}x = I.
$$
$a$、$b$ 称为积分下限与上限，$f$ 称为被积函数，$x$ 是哑变量（$\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(t)\,\mathrm{d}t$）。

**可积性**：$[a, b]$ 上连续的函数必可积；只有有限个第一类间断点的有界函数也可积。完整的可积性刻画需要更精细的工具（见[实分析](../real/index.md)）。

!!! note "要点"
    定义中"对任意取法"是关键：取点方式不能影响极限值。这也解释了为何要求最大段长 $\lambda \to 0$ 而非简单取 $n \to \infty$——段数再多，若取点只落在少数位置上，和式仍可能偏离真实面积。

## 定积分的性质

以下设 $f, g$ 可积。

**定理 1（线性）** $\displaystyle \int_a^b [\alpha f(x) + \beta g(x)]\,\mathrm{d}x = \alpha \int_a^b f(x)\,\mathrm{d}x + \beta \int_a^b g(x)\,\mathrm{d}x$。

**定理 2（区间可加性）** 对 $a < c < b$，$\displaystyle \int_a^b f = \int_a^c f + \int_c^b f$。补充约定 $\int_b^a f = -\int_a^b f$、$\int_a^a f = 0$ 后，对端点任意排列也成立。

**推论 1（对称区间上的积分）** 若 $f$ 在 $[-a, a]$ 上连续且为奇函数，则 $\int_{-a}^{a} f = 0$；若为偶函数，则 $\int_{-a}^{a} f = 2\int_0^a f$。这一结论常与换元 $t = -x$ 联用，用来简化对称区间的积分。

**定理 3（保序性）** 若 $f(x) \le g(x)$ 于 $[a, b]$，则 $\int_a^b f \le \int_a^b g$；特别地，$\left| \int_a^b f \right| \le \int_a^b |f|$。

**估值定理** 若 $m \le f(x) \le M$，则 $m(b - a) \le \int_a^b f \le M(b - a)$。

**定理 4（积分中值定理）** 若 $f$ 在 $[a, b]$ 上连续，则存在 $\xi \in [a, b]$ 使
$$
\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b - a).
$$
几何意义：曲线下的面积等于某个"平均高度" $f(\xi)$ 乘以底边长。

## 微积分基本定理

这是整个微积分的核心定理，把求导与积分两个方向打通。

**定理 5（基本定理第一形式，原函数存在性）** 若 $f$ 在 $[a, b]$ 上连续，则变上限积分
$$
F(x) = \int_a^x f(t)\,\mathrm{d}t
$$
在 $[a, b]$ 上可导，且 $F'(x) = f(x)$。即连续函数必有原函数，且原函数由变上限积分显式给出。

**证明（思想）** 对 $h \ne 0$，
$$
\frac{F(x + h) - F(x)}{h} = \frac{1}{h} \int_x^{x+h} f(t)\,\mathrm{d}t.
$$
由积分中值定理，上式等于 $f(\xi_h)$（$\xi_h$ 介于 $x$ 与 $x + h$ 之间）；令 $h \to 0$，由 $f$ 的连续性得 $\xi_h \to x$、$f(\xi_h) \to f(x)$。直觉：小段 $[x, x+h]$ 上"面积增量 ≈ 高度 × 宽度"，故面积对宽度的变化率就是高度本身——**面积函数在边界的导数等于被积函数在该点的值**。

**定理 6（基本定理第二形式，Newton–Leibniz 公式）** 若 $f$ 在 $[a, b]$ 上连续，$F$ 是 $f$ 的任意一个原函数（$F' = f$），则
$$
\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a).
$$
**证明（思想）** 令 $\Phi(x) = \int_a^x f(t)\,\mathrm{d}t - [F(x) - F(a)]$。由第一形式，$\Phi'(x) = f(x) - f(x) = 0$，故 $\Phi$ 为常数；又 $\Phi(a) = 0$，所以 $\Phi(b) = 0$，即 $\int_a^b f = F(b) - F(a)$。这里用到"导数为零 ⟹ 常数"（Lagrange 中值定理的推论，见[导数](derivatives.md)）。

!!! note "要点"
    基本定理把"求面积"这个几何问题转化为"求原函数"这个代数问题：微分与积分互为逆运算。这也是"微积分"（differential and integral calculus）命名的由来。

## 不定积分

**定义 2（不定积分）** $f$ 的全部原函数记为
$$
\int f(x)\,\mathrm{d}x = F(x) + C,
$$
其中 $F' = f$，$C$ 为任意常数。不定积分是函数的**集合**（彼此相差一个常数），定积分是一个**数**。

**基本积分表**（由导数表反推）：

$$
\int x^\alpha\,\mathrm{d}x = \frac{x^{\alpha+1}}{\alpha + 1} + C \ (\alpha \ne -1), \qquad
\int \frac{\mathrm{d}x}{x} = \ln|x| + C,
$$
$$
\int e^x\,\mathrm{d}x = e^x + C, \qquad
\int \sin x\,\mathrm{d}x = -\cos x + C, \qquad
\int \cos x\,\mathrm{d}x = \sin x + C,
$$
$$
\int \frac{\mathrm{d}x}{1 + x^2} = \arctan x + C, \qquad
\int \frac{\mathrm{d}x}{\sqrt{1 - x^2}} = \arcsin x + C.
$$

### 换元积分法

**定理 7（换元法）** 若 $\int f(u)\,\mathrm{d}u = F(u) + C$，则
$$
\int f(\varphi(x))\,\varphi'(x)\,\mathrm{d}x = F(\varphi(x)) + C.
$$
实际使用分两种方向：

- **第一类换元（凑微分）**：把被积表达式拼成 $f(\varphi(x))\varphi'(x)\,\mathrm{d}x = f(u)\,\mathrm{d}u$ 的形式，如 $\int \sin 2x\,\mathrm{d}x = \dfrac{1}{2}\int \sin 2x\,\mathrm{d}(2x) = -\dfrac{1}{2}\cos 2x + C$；
- **第二类换元**：令 $x = \psi(t)$ 消去根号或复杂结构，如 $\int \sqrt{1 - x^2}\,\mathrm{d}x$ 令 $x = \sin t$。

**定积分换元**：若 $\varphi$ 单调可导，$\varphi(\alpha) = a$、$\varphi(\beta) = b$，则
$$
\int_a^b f(x)\,\mathrm{d}x = \int_\alpha^\beta f(\varphi(t))\,\varphi'(t)\,\mathrm{d}t.
$$
换元的同时必须**更换积分限**，换元后不必回代。

!!! warning "易错点"
    定积分换元时，积分限的对应是"$t$ 的取值对应 $x$ 的取值"，不要把方向搞反；且要求 $\varphi$ 单调，以保证 $t$ 与 $x$ 一一对应。

### 分部积分法

**定理 8（分部积分）** 由乘积法则 $(uv)' = u'v + uv'$ 两边积分得
$$
\int u\,\mathrm{d}v = uv - \int v\,\mathrm{d}u, \qquad
\int_a^b u\,\mathrm{d}v = [uv]_a^b - \int_a^b v\,\mathrm{d}u.
$$
选取原则：把较难积的因子放进 $\mathrm{d}v$，让新积分比原积分简单。典型配对：多项式 × 指数/三角（令多项式为 $u$）；多项式 × 对数/反三角（令对数或反三角为 $u$）。

**例 1** $\int x e^x\,\mathrm{d}x = x e^x - \int e^x\,\mathrm{d}x = (x - 1)e^x + C$（令 $u = x$、$\mathrm{d}v = e^x\,\mathrm{d}x$）。

**例 2（递推）** $I_n = \int \sin^n x\,\mathrm{d}x$ 经分部积分可得递推公式 $I_n = -\dfrac{1}{n}\sin^{n-1}x\cos x + \dfrac{n-1}{n} I_{n-2}$。

**常见三角换元**（针对二次根式结构）：

| 被积结构 | 换元 | 化简 |
| --- | --- | --- |
| $\sqrt{a^2 - x^2}$ | $x = a\sin t$ | $a\cos t$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan t$ | $a\sec t$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec t$ | $a\tan t$ |

换元后通常出现三角函数的积分，可再配合例 2 的递推公式完成。

## 定积分的应用

以下设 $f, g$ 在相关区间上连续。

**平面图形面积**：曲线 $y = f(x)$ 与 $y = g(x)$ 在 $[a, b]$ 之间围成的面积为
$$
A = \int_a^b |f(x) - g(x)|\,\mathrm{d}x.
$$
极坐标下，曲线 $r = r(\theta)$ 与射线 $\theta = \alpha$、$\theta = \beta$ 围成的面积为 $A = \dfrac{1}{2}\int_\alpha^\beta r(\theta)^2\,\mathrm{d}\theta$。

**旋转体体积**：$y = f(x)$（$f(x) \ge 0$）绕 $x$ 轴旋转一周所得旋转体体积为
$$
V = \pi \int_a^b f(x)^2\,\mathrm{d}x
$$
（圆盘法）；绕 $y$ 轴可用壳层法 $V = 2\pi \int_a^b x\,f(x)\,\mathrm{d}x$。

**弧长**：曲线 $y = f(x)$ 从 $a$ 到 $b$ 的弧长为
$$
s = \int_a^b \sqrt{1 + f'(x)^2}\,\mathrm{d}x;
$$
参数方程 $\begin{cases} x = x(t) \\ y = y(t) \end{cases}$（$t \in [\alpha, \beta]$）下为 $s = \int_\alpha^\beta \sqrt{x'(t)^2 + y'(t)^2}\,\mathrm{d}t$。

**平均值**：连续函数 $f$ 在 $[a, b]$ 上的平均值为
$$
\bar{f} = \frac{1}{b - a} \int_a^b f(x)\,\mathrm{d}x,
$$
它是积分中值定理中 $f(\xi)$ 的直接解释，也常用于"平均速度""平均功率"等物理量。

!!! note "要点"
    这些公式的共同逻辑是**微元法**：把整体量切成微元——面积微元 $|f - g|\,\mathrm{d}x$、体积微元 $\pi f^2\,\mathrm{d}x$、弧长微元 $\sqrt{1 + f'^2}\,\mathrm{d}x$——再用定积分求和。微元的一阶近似（"以直代曲"）是误差可忽略的关键。

## 广义积分

定积分要求有限区间与有界函数，两条限制各放宽一条就得到两类广义积分。

**定义 3（无穷区间上的积分）** 若对任意 $b > a$，$\int_a^b f$ 存在，则定义
$$
\int_a^{+\infty} f(x)\,\mathrm{d}x = \lim_{b \to +\infty} \int_a^b f(x)\,\mathrm{d}x,
$$
极限存在则称广义积分收敛，否则发散。$\int_{-\infty}^b$ 与 $\int_{-\infty}^{+\infty}$ 类似（后者定义为两个单侧极限之和，且两个极限分别存在）。

**定义 4（瑕积分）** 若 $f$ 在 $b$ 附近无界（$b$ 称为瑕点），则定义
$$
\int_a^b f(x)\,\mathrm{d}x = \lim_{\varepsilon \to 0^+} \int_a^{b - \varepsilon} f(x)\,\mathrm{d}x,
$$
极限存在则收敛。瑕点也可能在区间内部或左端点。

**例 3（p-积分）** $\int_1^{+\infty} \dfrac{\mathrm{d}x}{x^p}$ 当且仅当 $p > 1$ 时收敛（$p \le 1$ 时发散）；$\int_0^1 \dfrac{\mathrm{d}x}{x^p}$ 当且仅当 $p < 1$ 时收敛。这两组 p-积分的结论是判别其他广义积分的基本参照。

**收敛判别（简述）** 若 $|f(x)| \le g(x)$ 且 $\int g$ 收敛，则 $\int f$ 收敛（比较判别法，比较对象常用 p-积分）；绝对收敛的广义积分必收敛。**注意**：$\int_0^{+\infty} \dfrac{\sin x}{x}\,\mathrm{d}x$ 收敛但不绝对收敛——绝对收敛与条件收敛的区分在广义积分中同样出现（参照[数列与级数](sequences_series.md)）。

!!! warning "易错点"
    对无界函数不能直接套用 Newton–Leibniz 公式。例如 $\int_{-1}^{1} \dfrac{1}{x^2}\,\mathrm{d}x$：若形式上取原函数 $-1/x$ 会得到 $-2$，纯属错误——正确做法是分瑕点分别计算，两侧极限都不存在，积分发散。

## 例子

- 例 4：$\int_0^1 x e^{x^2}\,\mathrm{d}x = \dfrac{1}{2}\int_0^1 e^{x^2}\,\mathrm{d}(x^2) = \dfrac{1}{2}(e - 1)$（凑微分并换限）。
- 例 5：$\int_0^{+\infty} e^{-x}\,\mathrm{d}x = \lim_{b \to +\infty} \left[ -e^{-x} \right]_0^b = 1$。
- 例 6：$\int_0^1 \ln x\,\mathrm{d}x = [x \ln x - x]_0^1 = -1$（分部积分；在瑕点 $0$ 处 $\lim_{x \to 0^+} x \ln x = 0$）。
- 例 7：$\int_0^1 \ln(1 + x)\,\mathrm{d}x = [(1 + x)\ln(1 + x) - x]_0^1 = 2\ln 2 - 1$（分部积分）。
- 例 8：$\int_1^{+\infty} \dfrac{\mathrm{d}x}{x^2} = \lim_{b \to +\infty} \left( 1 - \dfrac{1}{b} \right) = 1$（p-积分，$p = 2 > 1$，收敛）。

## 延伸阅读

- [导数](derivatives.md)：微分与积分的互逆关系。
- [数列与级数](sequences_series.md)：级数与积分的联系（如积分判别法）。
- [实分析](../real/index.md)：Riemann 积分的严格理论。
- [符号表](../../notation/index.md)：$\int$、$\mathrm{d}x$ 记号约定。
