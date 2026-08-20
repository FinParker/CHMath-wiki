---
title: Riemann 积分
tags:
  - 实分析
---

# Riemann 积分

Riemann 积分回答的问题是:如何严格定义"曲线下的面积"?本页用分割与达布上下和构造积分,

给出可积性的判别,并证明微积分基本定理——微分与积分互逆的精确表述。与导数"局部线性逼近"

不同,积分是"整体求和"的极限,二者的桥梁正是微积分基本定理。

## 动机与定义

考虑 $f : [a,b] \to \mathbb{R}$ 非负。几何上,$\int_a^b f(x)\,\mathrm{d}x$ 应等于曲线下的面积。

物理上,若 $v(t)$ 是速度,则 $\int_a^b v(t)\,\mathrm{d}t$ 是位移——这是"把变化率累积起来"

的模型。粗糙的做法是:把 $[a,b]$ 切成小区间,用矩形近似每一条,再让分割无限变细。Riemann

积分的严格化在于:无论矩形取法如何(在每个小区间内取哪一点的函数值),极限必须一致。

**定义 1（分割）** $[a,b]$ 的一个分割是有限点集 $P = \{x_0, x_1, \ldots, x_n\}$,其中

$a = x_0 < x_1 < \cdots < x_n = b$。记 $\Delta x_i = x_i - x_{i-1}$,并称 $\|P\| = \max_i \Delta x_i$

为分割的模。

**定义 2（达布和）** 设 $f$ 有界,$m_i = \inf_{[x_{i-1}, x_i]} f$、$M_i = \sup_{[x_{i-1}, x_i]} f$。

称

$$L(f, P) = \sum_{i=1}^{n} m_i \Delta x_i, \qquad U(f, P) = \sum_{i=1}^{n} M_i \Delta x_i$$

分别为 $f$ 关于 $P$ 的达布下和与达布上和。

直观上,$L(f,P)$ 是所有"矮矩形"面积之和,$U(f,P)$ 是所有"高矩形"面积之和,真实面积夹在

两者之间。

**定义 3（加细）** 分割 $P^*$ 称为 $P$ 的加细,若 $P \subseteq P^*$。加细不减小下和、不增大

上和:

$$L(f, P) \le L(f, P^*) \le U(f, P^*) \le U(f, P).$$

**定义 4（Riemann 可积）** $f$ 在 $[a,b]$ 上 Riemann 可积,若

$$\underline{\int_a^b} f(x)\,\mathrm{d}x := \sup_P L(f,P) = \inf_P U(f,P) =: \overline{\int_a^b} f(x)\,\mathrm{d}x,$$

公共值记为 $\int_a^b f(x)\,\mathrm{d}x$,称为 $f$ 在 $[a,b]$ 上的定积分。

**定理 1（可积的判别条件）** 有界函数 $f$ 可积当且仅当对任意 $\varepsilon > 0$ 存在分割 $P$

使

$$U(f, P) - L(f, P) < \varepsilon.$$

证明思路:若 $U - L$ 可任意小,则上下积分之差被任意小的正数控制,故相等;反之若可积,对

$\varepsilon$ 分别取逼近上、下积分的分割,用两者的公共加细把差拆开。

!!! note "可积要求有界"

    达布和的定义需要 $m_i, M_i$ 存在,故 Riemann 积分只对(局部)有界函数定义。无界函数

    (如 $1/\sqrt{x}$ 在 $0$ 附近)不属于 Riemann 可积的范畴,需要广义积分处理。

**定理 2（Riemann 和的等价定义）** 有界函数 $f$ 可积当且仅当:存在 $I$ 使对任意取点

$\xi_i \in [x_{i-1}, x_i]$,当 $\|P\| \to 0$ 时 Riemann 和 $\sum_{i=1}^{n} f(\xi_i)\Delta x_i \to I$,

此时 $I = \int_a^b f$。

证明思路:$(\Rightarrow)$ 对任意取点,$L(f,P) \le \sum f(\xi_i)\Delta x_i \le U(f,P)$,而

$L, U$ 都趋近积分,夹逼得 Riemann 和趋近积分。$(\Leftarrow)$ 取 $f$ 的上下确界逼近点,把

Riemann 和夹在 $L$ 与 $U$ 之间,反推 $U - L$ 可任意小。

**例 1（按定义计算）** 对 $f(x) = x$ 取等分分割 $\Delta x_i = 1/n$,在小区间右端点取点,

$$\sum_{i=1}^{n} f(\xi_i)\Delta x_i = \sum_{i=1}^{n} \frac{i}{n} \cdot \frac{1}{n} = \frac{n(n+1)}{2n^2} \to \frac{1}{2},$$

故 $\int_0^1 x\,\mathrm{d}x = 1/2$。同样的手法配合 $\sum i^2 = n(n+1)(2n+1)/6$ 可得

$\int_0^1 x^2\,\mathrm{d}x = 1/3$——这是"积分是求和极限"的最直接体现。

## 可积函数类

**定理 3（连续函数可积）** $[a,b]$ 上的连续函数可积。

证明思路:由 Heine–Cantor 定理(见 [连续函数](continuity.md)),$f$ 一致连续:对

$\varepsilon > 0$ 存在 $\delta > 0$,只要分割满足 $\|P\| < \delta$,每个小区间上振幅

$M_i - m_i < \varepsilon/(b-a)$,于是 $U - L < \varepsilon$。

**定理 4（单调函数可积）** $[a,b]$ 上的单调函数可积。

证明思路:设 $f$ 单调递增。取等距分割 $\Delta x_i = (b-a)/n$,则每个小区间上 $M_i = f(x_i)$、

$m_i = f(x_{i-1})$,振幅沿单调方向"首尾抵消":

$$U - L = \frac{b-a}{n}\sum_{i=1}^{n}\big(f(x_i) - f(x_{i-1})\big) = \frac{b-a}{n}\big(f(b) - f(a)\big) \to 0.$$

!!! note "可积与连续的关系"

    由 Riemann–Lebesgue 定理(陈述不证明):有界函数可积当且仅当其不连续点集为零测度。连续

    函数的不连续点集为空;单调函数的不连续点集至多可数。这从"不连续点不能太多"的角度统一了

    上述两个定理。

## 定积分的性质

**定理 5（基本性质）** 设 $f, g$ 在 $[a,b]$ 上可积,$c \in \mathbb{R}$,$a < c < b$,则:

1. 线性:$\int_a^b (f + g) = \int_a^b f + \int_a^b g$,$\int_a^b cf = c\int_a^b f$;
2. 区间可加:$\int_a^b f = \int_a^c f + \int_c^b f$;
3. 保序:$f \le g \implies \int_a^b f \le \int_a^b g$;
4. 绝对可积:$|f|$ 可积,且 $\big|\int_a^b f\big| \le \int_a^b |f|$;
5. 约定 $\int_a^a f = 0$、$\int_b^a f = -\int_a^b f$。

证明思路:线性与区间可加由达布和的定义与加细直接验证;保序用 $m_i, M_i$ 的逐点比较;绝对

可积用 $\big||u| - |v|\big| \le |u - v|$ 控制振幅。

**定理 6（积分中值定理）** 设 $f$ 在 $[a,b]$ 上连续,则存在 $\xi \in [a,b]$ 使

$$\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b - a).$$

证明思路:由最值定理,$m \le f \le M$;保序给出 $m(b-a) \le \int_a^b f \le M(b-a)$;由介值

定理,平均值 $\dfrac{1}{b-a}\int_a^b f$ 在 $f$ 的取值范围内被取到。

## 微积分基本定理

**定理 7（FTC,第一形式）** 设 $f$ 在 $[a,b]$ 上可积,则变上限函数

$$F(x) = \int_a^x f(t)\,\mathrm{d}t$$

在 $[a,b]$ 上连续;若 $f$ 在 $x_0$ 处连续,则 $F$ 在 $x_0$ 处可导且 $F'(x_0) = f(x_0)$。

证明思路:连续性用 $|F(x+h) - F(x)| = \big|\int_x^{x+h} f\big| \le M|h|$($f$ 有界);可导性用

$f$ 的连续性:对 $\varepsilon > 0$ 取 $\delta$ 使 $|t - x_0| < \delta \Rightarrow

|f(t) - f(x_0)| < \varepsilon$,则

$$\Big|\frac{F(x_0+h) - F(x_0)}{h} - f(x_0)\Big| = \Big|\frac{1}{h}\int_{x_0}^{x_0+h}\big(f(t) - f(x_0)\big)\,\mathrm{d}t\Big| \le \varepsilon.$$

**定理 8（FTC,第二形式 / Newton–Leibniz 公式）** 设 $f$ 在 $[a,b]$ 上连续,$F$ 是 $f$ 在

$[a,b]$ 上的一个原函数($F' = f$),则

$$\int_a^b f(x)\,\mathrm{d}x = F(b) - F(a).$$

证明思路:令 $G(x) = \int_a^x f$,由第一形式 $G' = f$;故 $(F - G)' = f - f = 0$,由中值定理

的推论 $F - G$ 为常数,取 $x = a$ 定出常数,再取 $x = b$ 即得。

!!! note "本质:微分与积分互逆"

    第一形式说"先积后微"还原被积函数;第二形式说"求出原函数后代入端点"即可算出积分。它把

    求面积的问题转化为求导的逆运算,是微积分的灵魂。例如 $\int_0^\pi \sin x\,\mathrm{d}x =

    [-\cos x]_0^\pi = 2$。

## 换元与分部积分

**定理 9（换元公式）** 设 $\varphi \in C^1([\alpha, \beta])$,$f$ 在 $\varphi([\alpha, \beta])$

上连续,则

$$\int_{\alpha}^{\beta} f(\varphi(t))\,\varphi'(t)\,\mathrm{d}t = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x)\,\mathrm{d}x.$$

证明思路:设 $F$ 为 $f$ 的原函数,左边被积函数恰是 $(F \circ \varphi)'(t) =

f(\varphi(t))\,\varphi'(t)$;由 FTC 第二形式,两边都等于 $F(\varphi(\beta)) - F(\varphi(\alpha))$。

**定理 10（分部积分公式）** 设 $u, v \in C^1([a,b])$,则

$$\int_a^b u(x)\,v'(x)\,\mathrm{d}x = \big[u(x)v(x)\big]_a^b - \int_a^b u'(x)\,v(x)\,\mathrm{d}x.$$

证明思路:由 $(uv)' = u'v + uv'$ 两边积分,再用 FTC 第二形式。

**例 2** 换元:$\displaystyle \int_0^1 \sqrt{1-x^2}\,\mathrm{d}x = \frac{\pi}{4}$(令

$x = \sin t$);分部积分:$\displaystyle \int_0^1 x e^x \,\mathrm{d}x = \big[x e^x\big]_0^1 -

\int_0^1 e^x \,\mathrm{d}x = 1$;$\int_0^\infty x e^{-x}\,\mathrm{d}x = 1$ 的求法同型。

!!! note "广义积分的预告"

    换元与分部积分把积分运算变成"程序化"的步骤。当区间无界或被积函数无界时,需要先取极限

    再积分,即广义积分:$\int_0^\infty e^{-x}\,\mathrm{d}x = \lim_{b \to \infty}(-e^{-x})|_0^b = 1$。

## 可积与不连续:两个经典例子

**例 3（Dirichlet 函数不可积）** 设 $D(x) = 1$(若 $x$ 为有理数)、$0$(若 $x$ 为无理数)。

对任意分割 $P$,由有理数与无理数的稠密性,每个小区间上 $M_i = 1$、$m_i = 0$,故

$U(f,P) = b - a$、$L(f,P) = 0$,上下积分不等,$D$ 不可积。这个例子说明:处处不连续的函数

完全无法用 Riemann 积分度量。

**例 4（Thomae 函数可积）** 设

$$T(x) = \begin{cases} \dfrac{1}{q}, & x = \dfrac{p}{q}\ \text{既约},\\ 0, & x\ \text{为无理数}, \end{cases}$$

则 $T$ 在无理点连续、在有理点间断,但 $T$ 在 $[0,1]$ 上可积且 $\int_0^1 T = 0$。

证明思路:对给定 $\varepsilon > 0$,满足 $T(x) \ge \varepsilon$ 的点只有有限多个(它们形如

$p/q$ 且 $q \le 1/\varepsilon$)。用若干小开区间盖住这些点,使总长 $< \varepsilon$;其余部分上

$T$ 的振幅 $< \varepsilon$。取包含这些区间的分割,可使 $U - L$ 任意小。这个例子说明:不连续点

即使稠密(有理数集),只要"整体很小",函数仍可积——与 Riemann–Lebesgue 定理相呼应。

!!! note "Riemann 积分的局限"

    Dirichlet 函数在 Lebesgue 积分意义下可积且积分为 $0$(有理数集是零测集)。Riemann 积分

    无法处理这类"不连续点太多"的函数,这是推动 Lebesgue 积分诞生的直接动因。

## 延伸阅读

- [微分学](differentiation.md):中值定理与 Taylor 展开,微分与积分的另一面
- [连续函数](continuity.md):一致连续与最值定理,可积性证明的工具
- [分析](../index.md):实分析整体框架
- [符号表](../../notation/index.md):$\int$、$\mathrm{d}x$ 等记号约定
