---
title: 微分学
tags:
  - 实分析
---

# 微分学

导数刻画函数在一点附近的变化率,其本质是"用线性函数局部逼近"。本页从差商极限出发,

依次建立中值定理(微分学的核心工具)、L'Hôpital 法则与 Taylor 展开,最后介绍凸函数与

Jensen 不等式。微分学的结构可以概括为:定义 → 中值定理 → 应用。

## 导数:定义与几何意义

**定义 1（导数）** 设 $f$ 在 $x_0$ 的某邻域内有定义。若极限

$$f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

存在,称 $f$ 在 $x_0$ 可导,极限值称为 $f$ 在 $x_0$ 的导数。

**定义 2（左、右导数）** $f'_-(x_0)$、$f'_+(x_0)$ 分别是 $x \to x_0^-$、$x \to x_0^+$ 的差商

极限。$f$ 在 $x_0$ 可导当且仅当左右导数存在且相等。

**命题 1（线性化）** $f$ 在 $x_0$ 可导当且仅当存在常数 $A$ 使

$$f(x) = f(x_0) + A(x - x_0) + o(x - x_0) \quad (x \to x_0),$$

此时 $A = f'(x_0)$。

证明思路:把差商极限改写成"误差项除以 $x - x_0$ 趋于 0",即 $o$ 小 o 记号的定义。几何意义:

图像在 $(x_0, f(x_0))$ 处有切线 $y = f(x_0) + f'(x_0)(x - x_0)$,导数即切线斜率。若记

$\mathrm{d}x = x - x_0$、$\mathrm{d}y = f'(x_0)\,\mathrm{d}x$,则"微分" $\mathrm{d}y$ 是

$f$ 在 $x_0$ 处的最好线性近似,这正是 $f(x) \approx f(x_0) + \mathrm{d}y$ 的严格含义。

**定理 1（可导 ⟹ 连续）** 若 $f$ 在 $x_0$ 可导,则 $f$ 在 $x_0$ 连续。

证明:由命题 1,$f(x) - f(x_0) = f'(x_0)(x - x_0) + o(x - x_0) \to 0$。

!!! note "连续不蕴含可导"

    反向不成立:$f(x) = |x|$ 在 $0$ 连续但不可导(左右导数分别为 $-1$ 与 $1$);Weierstrass

    构造了处处连续、处处不可导的函数,说明"可导"是远比"连续"苛刻的条件。

## 求导法则

**定理 2（四则与复合）** 若 $f, g$ 在 $x_0$ 可导,则

$$(f \pm g)' = f' \pm g', \qquad (fg)' = f'g + fg', \qquad \Big(\frac{f}{g}\Big)' = \frac{f'g - fg'}{g^2},$$

且若 $g$ 在 $x_0$ 可导、$f$ 在 $g(x_0)$ 可导,则链式法则 $(f \circ g)'(x_0) = f'(g(x_0))\,g'(x_0)$。

证明要点:积法则来自分解 $f(x)g(x) - f(x_0)g(x_0) = \big(f(x)-f(x_0)\big)g(x) +

f(x_0)\big(g(x)-g(x_0)\big)$;链式法则利用线性化:$f(g(x)) - f(g(x_0)) = f'(g(x_0))

\big(g(x)-g(x_0)\big) + o\big(g(x)-g(x_0)\big)$,再除以 $x - x_0$。

**定义 3（高阶导数）** $f$ 的 $n$ 阶导数 $f^{(n)}$ 递归定义为 $f^{(n)} = (f^{(n-1)})'$;约定

$f^{(0)} = f$。$f$ 称为 $C^n$ 类,若 $f^{(n)}$ 存在且连续。

**定理 3（Leibniz 公式）** 若 $f, g$ $n$ 阶可导,则

$$(fg)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k)} g^{(n-k)},$$

与二项式定理形式一致。证明思路:对 $n$ 归纳,归纳步用到组合恒等式

$\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$。

## Fermat 定理

**定理 4（Fermat）** 设 $f$ 在 $x_0$ 的某邻域内有定义,在 $x_0$ 处可导,且 $x_0$ 是 $f$ 的

局部极值点(局部最大或最小),则 $f'(x_0) = 0$。

证明思路:若 $x_0$ 是局部极大点,则 $x_0$ 左侧差商 $\ge 0$、右侧差商 $\le 0$;取左、右极限

得 $f'(x_0) \ge 0$ 且 $f'(x_0) \le 0$,故 $f'(x_0) = 0$。

!!! warning "条件是内点"

    $f(x) = x$ 在 $[0,1]$ 上的最大值在端点 $x = 1$ 取得,但 $f'(1) = 1 \ne 0$。Fermat 定理

    只对定义域内部的极值点成立——这正是 Rolle 定理要求"端点函数值相等"的原因。

## 中值定理

**定理 5（Rolle）** 设 $f$ 在 $[a,b]$ 连续、在 $(a,b)$ 可导,且 $f(a) = f(b)$,则存在

$c \in (a,b)$ 使 $f'(c) = 0$。

证明思路:由最值定理(见 [连续函数](continuity.md)),$f$ 在 $[a,b]$ 上有最大值与最小值。

若都在端点取到,则由 $f(a) = f(b)$ 知 $f$ 为常数,$f' \equiv 0$;否则至少一个极值在内部

取到,由 Fermat 定理 $f'(c) = 0$。

**定理 6（Lagrange 中值定理）** 设 $f$ 在 $[a,b]$ 连续、在 $(a,b)$ 可导,则存在 $c \in (a,b)$

使

$$f(b) - f(a) = f'(c)(b - a).$$

证明思路:构造辅助函数

$$F(x) = f(x) - \frac{f(b) - f(a)}{b - a}(x - a),$$

它满足 $F(a) = F(b) = f(a)$,由 Rolle 定理存在 $c$ 使 $F'(c) = 0$,即

$f'(c) = \dfrac{f(b) - f(a)}{b - a}$。几何意义:曲线上存在一点,其切线平行于连接两端点的弦。

"构造一个满足 Rolle 条件的辅助函数"是中值定理证明的通用手法。

**推论 1（单调性的导数判别）** 若 $f' \ge 0$(或 $> 0$、$\le 0$)于 $(a,b)$,则 $f$ 单调递增

(严格递增、单调递减);若 $f' \equiv 0$,则 $f$ 为常数。

**例 1** 由 Lagrange 中值定理,$|\sin x - \sin y| = |\cos \xi|\,|x - y| \le |x - y|$;

$\arctan x$ 同理满足 $|\arctan x - \arctan y| \le |x - y|$。

**定理 7（Cauchy 中值定理）** 设 $f, g$ 在 $[a,b]$ 连续、在 $(a,b)$ 可导,且 $g'$ 在 $(a,b)$

内不为零,则存在 $c \in (a,b)$ 使

$$\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)}.$$

证明思路:由 $g' \ne 0$ 与 Rolle 定理先得 $g(b) \ne g(a)$。作辅助函数

$$\Phi(x) = f(x) - \frac{f(b) - f(a)}{g(b) - g(a)}(g(x) - g(a)),$$

则 $\Phi(a) = \Phi(b) = f(a)$,由 Rolle 定理得 $\Phi'(c) = 0$,展开即得结论。Cauchy 中值定理

是 Lagrange 定理的"参数化"形式,也是 L'Hôpital 法则与带 Lagrange 余项的 Taylor 定理的

证明基石。

## 达布性质

**定理 8（Darboux 定理）** 设 $f$ 在 $[a,b]$ 上可导,则 $f'$ 具有介值性:对任意 $\lambda$ 介于

$f'(a)$ 与 $f'(b)$ 之间,存在 $c \in (a,b)$ 使 $f'(c) = \lambda$。

证明思路:不妨设 $f'(a) < \lambda < f'(b)$,考虑 $g(x) = f(x) - \lambda x$。由 $g'(a) < 0$

知 $a$ 的右侧存在点使 $g$ 更小;由 $g'(b) > 0$ 知 $b$ 的左侧存在点使 $g$ 更小,故 $g$ 在

$(a,b)$ 内部某点 $c$ 取得最小值(最值定理保证存在,端点被排除)。由 Fermat 定理 $g'(c) = 0$,

即 $f'(c) = \lambda$。

!!! note "导函数没有跳跃间断"

    由 Darboux 定理,导函数 $f'$ 即使不连续,也不可能具有第一类间断点(跳跃)。例如符号函数

    $s(x) = \operatorname{sgn} x$ 不是任何函数的导数。这是实分析中最反直觉的经典结论之一。

## L'Hôpital 法则

**定理 9（L'Hôpital,0/0 型）** 设 $f, g$ 在 $x_0$ 的去心邻域内可导,$g'(x) \ne 0$,且

$$\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0, \qquad \lim_{x \to x_0} \frac{f'(x)}{g'(x)} = L \in \mathbb{R} \cup \{\pm\infty\},$$

则 $\displaystyle \lim_{x \to x_0} \frac{f(x)}{g(x)} = L$。对 $\infty/\infty$ 型以及

$x \to \pm\infty$ 的情形有同样结论。

证明思路(0/0 型):补充定义 $f(x_0) = g(x_0) = 0$ 使 $f, g$ 在 $x_0$ 连续。对 $x$ 接近 $x_0$,

由 Cauchy 中值定理,存在 $\xi_x$ 介于 $x$ 与 $x_0$ 之间使

$$\frac{f(x)}{g(x)} = \frac{f(x) - f(x_0)}{g(x) - g(x_0)} = \frac{f'(\xi_x)}{g'(\xi_x)},$$

由 $\xi_x \to x_0$ 与 $f'/g'$ 的极限存在即得结论。$\infty/\infty$ 型需要更精细的估计

(对分子做分层),此处从略。

**例 2**

$$\lim_{x \to 0} \frac{\sin x}{x} = 1, \qquad \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}, \qquad \lim_{x \to +\infty} \frac{\ln x}{x} = 0, \qquad \lim_{x \to 0^+} x^x = 1.$$

最后一个例子:$\ln(x^x) = x \ln x \to 0$,故 $x^x = e^{x \ln x} \to 1$。此外 $0 \cdot \infty$

型可化为 $0/0$ 型:$\lim_{x \to 0^+} x\ln x = \lim \dfrac{\ln x}{1/x}$,再对后者用 L'Hôpital。

!!! warning "使用条件必须逐条检查"

    1. 法则的对象是 $\dfrac{f}{g}$,前提是 $\lim f'/g'$ 存在——不能对 $f$ 与 $g$ 分别求导后

       想当然;
    2. $g'$ 在去心邻域内不能为零(否则 Cauchy 中值定理不可用);
    3. 反例:$\lim_{x \to \infty} \dfrac{x + \sin x}{x} = 1$ 存在,但 $\lim (1 + \cos x)$ 不存在,

       说明"分母分子分别可导"不等于"法则适用"。

## Taylor 定理

**定理 10（Taylor 定理,Peano 余项）** 设 $f$ 在 $x_0$ 处 $n$ 阶可导,则

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k + o\big((x - x_0)^n\big) \quad (x \to x_0).$$

证明思路:反复使用 L'Hôpital 法则 $n-1$ 次,把余项与 $(x - x_0)^n$ 的比值化成含 $f^{(n)}$

的差商极限,从而趋于 0。Peano 余项只保证"在 $x_0$ 附近"的逼近精度,不含点的具体位置。

**定理 11（Taylor 定理,Lagrange 余项）** 设 $f$ 在 $[a,b]$ 上 $n+1$ 阶可导,则对 $x \in [a,b]$

存在 $\xi$ 介于 $x_0$ 与 $x$ 之间使

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}.$$

证明思路:固定 $x$,取定常数 $R$ 使辅助函数

$$\varphi(t) = f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(t)}{k!}(x - t)^k - \frac{(x - t)^{n+1}}{(x - x_0)^{n+1}} R$$

满足 $\varphi(x_0) = 0$;对 $\varphi$ 与 $(x-t)^{n+1}$ 用 Cauchy 中值定理(或反复 Rolle),

得 $\varphi'(\xi) = 0$,展开整理即得。$n = 0$ 时退化为 Lagrange 中值定理。

**例 3（麦克劳林展开）** 在 $x_0 = 0$ 处:

$$e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}, \qquad \sin x = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k}}{(2k)!},$$

$$\ln(1+x) = \sum_{k=1}^{\infty} \frac{(-1)^{k+1} x^k}{k} \quad (|x| < 1), \qquad (1+x)^\alpha = \sum_{k=0}^{\infty} \binom{\alpha}{k} x^k \quad (|x| < 1).$$

**推论 2（极值判定）** 若 $f'(x_0) = \cdots = f^{(n-1)}(x_0) = 0$ 而 $f^{(n)}(x_0) \ne 0$:当 $n$

为偶数时 $x_0$ 是极值点($f^{(n)}(x_0) > 0$ 为极小,$< 0$ 为极大);当 $n$ 为奇数时 $x_0$ 是

拐点。理由来自 Peano 余项:余项 $o((x-x_0)^n)$ 与主项相比可忽略,符号由

$f^{(n)}(x_0)(x-x_0)^n$ 决定。

## 凸函数与 Jensen 不等式

**定义 6（凸函数）** $f$ 称为区间 $I$ 上的凸函数,若对任意 $x, y \in I$、$\lambda \in [0,1]$,

$$f(\lambda x + (1-\lambda) y) \le \lambda f(x) + (1-\lambda) f(y).$$

几何意义:图像上任意两点的弦位于图像之上方。等价的"三点弦不等式":对 $x_1 < x_2 < x_3$,

$\dfrac{f(x_2) - f(x_1)}{x_2 - x_1} \le \dfrac{f(x_3) - f(x_1)}{x_3 - x_1} \le \dfrac{f(x_3) - f(x_2)}{x_3 - x_2}$

(弦的斜率单调)。

**定理 12（凸性的导数刻画）** 若 $f$ 二阶可导,则 $f$ 在 $I$ 上凸当且仅当 $f'' \ge 0$ 于 $I$。

证明思路:$(\Rightarrow)$ 用 $f'$ 的单调性:$f$ 凸当且仅当 $f'$ 单调递增(由三点弦不等式与

Lagrange 中值定理),故 $f'' \ge 0$。$(\Leftarrow)$ 对 $x < y$ 与 $\lambda$,在

$\lambda x + (1-\lambda)y$ 两侧分别对 $x$ 与 $y$ 用 Lagrange 中值定理,由 $f'$ 单调性比较。

**定理 13（Jensen 不等式）** 若 $f$ 在 $I$ 上凸,则对 $x_1, \ldots, x_n \in I$ 与权重

$\lambda_i \ge 0$、$\sum_i \lambda_i = 1$,

$$f\Big(\sum_{i=1}^{n} \lambda_i x_i\Big) \le \sum_{i=1}^{n} \lambda_i f(x_i).$$

证明思路:对 $n$ 归纳;归纳步把 $\sum_{i=1}^{n+1} \lambda_i x_i$ 写成

$\mu \cdot x_{n+1} + (1-\mu)\sum_{i=1}^{n} \frac{\lambda_i}{1-\mu} x_i$ 的形式,套用凸性定义。

**例 4** $\ln$ 是凹函数,故 $\ln\big(\tfrac{1}{n}\sum x_i\big) \ge \tfrac{1}{n}\sum \ln x_i$,

即算术平均不小于几何平均:

$$\frac{x_1 + \cdots + x_n}{n} \ge \sqrt[n]{x_1 \cdots x_n} \quad (x_i > 0).$$

## 延伸阅读

- [连续函数](continuity.md):最值定理与介值定理,中值定理证明的地基
- [Riemann 积分](integration.md):微积分基本定理把微分与积分联结起来
- [分析](../index.md):微分学在分析整体框架中的定位
- [符号表](../../notation/index.md):$o$ 记号与极限记号汇总
