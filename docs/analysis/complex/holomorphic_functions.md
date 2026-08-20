---
title: 全纯函数
tags:
  - 复分析
---

# 全纯函数

复可导是一个远比实可导苛刻的条件:它迫使函数具有幂级数展开、无穷可导、由边界值完全决定等

"刚性"性质。本页介绍全纯函数的定义、Cauchy–Riemann 方程,以及复分析的三座大厦:Cauchy

积分理论、Liouville 定理与留数定理,最后以唯一性定理与最大模原理收束。

## 复导数与全纯函数

**定义 1（复导数）** 设 $U \subseteq \mathbb{C}$ 为开集,$f : U \to \mathbb{C}$,$z_0 \in U$。

若极限

$$f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}$$

存在,称 $f$ 在 $z_0$ 复可导。若 $f$ 在 $U$ 的每一点复可导,称 $f$ 在 $U$ 上全纯(或解析),

记 $f \in \mathcal{O}(U)$。

复导数与实导数的定义形式相同,但本质区别在于:这里的 $z \to z_0$ 是复平面上的二维极限,

要求从所有方向趋近时差商都趋于同一个数。这使"复可导"远比"实可导"强硬。

**例 1** $f(z) = z^2$ 全纯,$f'(z) = 2z$;多项式处处全纯。$f(z) = \bar{z}$ 处处连续但处处

不可导:沿实轴方向差商为 1,沿虚轴方向差商为 $-1$。

## Cauchy–Riemann 方程

记 $f = u + iv$,即 $u(x, y) = \operatorname{Re} f(x+iy)$、$v(x, y) = \operatorname{Im} f(x+iy)$。

**定理 1（CR 方程,必要性）** 若 $f$ 在 $z_0 = x_0 + iy_0$ 复可导,则 $u, v$ 在 $(x_0, y_0)$ 的

一阶偏导数存在,且

$$u_x = v_y, \qquad u_y = -v_x.$$

证明思路:设 $f'(z_0) = \alpha + i\beta$。沿实方向 $z = z_0 + t$($t \in \mathbb{R}$,$t \to 0$):

$$f'(z_0) = \lim_{t \to 0} \frac{f(z_0 + t) - f(z_0)}{t} = u_x(x_0, y_0) + i\, v_x(x_0, y_0);$$

沿虚方向 $z = z_0 + it$:

$$f'(z_0) = \lim_{t \to 0} \frac{f(z_0 + it) - f(z_0)}{it} = v_y(x_0, y_0) - i\, u_y(x_0, y_0).$$

两个方向给出同一个数,比较实部虚部即得 $u_x = v_y$、$u_y = -v_x$。

**定理 2（CR 方程,充分性）** 若 $u, v$ 在开集 $U$ 上连续可微且处处满足 CR 方程,则 $f$ 在 $U$

上全纯,且

$$f' = u_x + i v_x = v_y - i u_y.$$

证明思路:由 $u, v$ 的可微性,

$$\Delta f = (u_x + iv_x)\Delta x + (u_y + iv_y)\Delta y + o(|\Delta z|).$$

代入 CR 方程 $u_y = -v_x$、$v_y = u_x$,得

$$\Delta f = (u_x + iv_x)(\Delta x + i\Delta y) + o(|\Delta z|) = f'(z_0)\,\Delta z + o(|\Delta z|),$$

恰为复可导的定义。

!!! note "CR 方程是复可导的"全息图""

    实部 $u$ 与虚部 $v$ 不是独立的:给定其中一个(以及少许正则性),另一个由 CR 方程决定。

    例如 $u = x^2 - y^2$ 对应的全纯函数必为 $z^2 + c$。CR 方程还蕴含 $u, v$ 都是调和函数

    ($u_{xx} + u_{yy} = 0$ 等),这使全纯函数与位势理论深度关联。

## 全纯函数的例子

**例 2（多项式与有理函数）** 多项式处处全纯;有理函数在分母零点之外全纯。

**例 3（指数函数）** $e^z = e^x(\cos y + i\sin y)$ 处处全纯,且 $(e^z)' = e^z$。验证:实部

$u = e^x\cos y$、虚部 $v = e^x\sin y$ 满足 $u_x = e^x\cos y = v_y$、$u_y = -e^x\sin y = -v_x$。

**例 4（幂级数）** 幂级数 $\sum_{n=0}^{\infty} a_n (z - z_0)^n$ 在其收敛圆 $|z - z_0| < R$ 内

全纯,且可逐项求导。收敛半径由 Cauchy–Hadamard 公式 $1/R = \limsup \sqrt[n]{|a_n|}$ 给出。

由 Euler 公式(见 [复数](complex_numbers.md)),$e^z = \sum_{n=0}^{\infty} z^n / n!$ 在全平面

收敛,故 $e^z$ 是整函数。

## 全纯 = 局部幂级数

**定理 3（全纯函数的幂级数展开）** 设 $f$ 在开集 $U$ 上全纯,$z_0 \in U$。则 $f$ 在 $z_0$ 附近

等于其 Taylor 级数:存在 $R > 0$ 使对 $|z - z_0| < R$,

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!}(z - z_0)^n.$$

证明思路:这是 Cauchy 积分公式(定理 5)的直接推论:把 $f(z) = \frac{1}{2\pi i}\oint

\frac{f(\zeta)}{\zeta - z}\,\mathrm{d}\zeta$ 中的核 $\frac{1}{\zeta - z}$ 按几何级数展开,

再交换求和与积分。

!!! note "与实分析的巨大差异"

    实函数可以 $C^\infty$ 光滑却不解析(如 $e^{-1/x^2}$ 在 $0$ 处的 Taylor 级数恒为零);全纯

    函数则"可导一次即可展开成幂级数"。全纯 = 局部幂级数是复分析一切"刚性"结论的源头。

## Cauchy 积分定理与积分公式

**定义 2（围道积分）** 设 $\gamma : [a,b] \to \mathbb{C}$ 为分段光滑曲线,$f$ 在 $\gamma$ 的像

附近连续,定义

$$\int_{\gamma} f(z)\,\mathrm{d}z = \int_a^b f(\gamma(t))\,\gamma'(t)\,\mathrm{d}t.$$

**定理 4（Cauchy 积分定理）** 设 $U$ 为单连通开集,$f$ 在 $U$ 上全纯,$\gamma$ 为 $U$ 内闭曲线,

则

$$\oint_{\gamma} f(z)\,\mathrm{d}z = 0.$$

直观与证明思路:若假定 $f'$ 连续,把 $f\,\mathrm{d}z = (u\,\mathrm{d}x - v\,\mathrm{d}y) + i(v\,

\mathrm{d}x + u\,\mathrm{d}y)$ 代入 Green 公式,两项积分中的被积函数都含 $u_x \mp v_y$ 型因子,

CR 方程使它们恒为零。Goursat 定理去掉了 $f'$ 连续这一假设——全纯本身足够。

!!! note "直觉:旋度为零"

    复可导意味着复平面上的向量场 $(u, v)$ 处处无旋(由 CR 方程),因此沿闭路做功为零。这正是

    积分定理的物理直觉:全纯函数描述的场没有涡旋。

**定理 5（Cauchy 积分公式）** 设 $U$ 单连通,$f$ 在 $U$ 上全纯,$\gamma$ 为 $U$ 内正向简单闭

曲线,$z_0$ 在 $\gamma$ 内部,则

$$f(z_0) = \frac{1}{2\pi i} \oint_{\gamma} \frac{f(z)}{z - z_0}\,\mathrm{d}z.$$

证明思路:在 $z_0$ 附近挖去小圆 $|z - z_0| = \varepsilon$,两条曲线围成的环域上被积函数全纯,

由积分定理该环域上的积分为零;令 $\varepsilon \to 0$,在圆周上用 $f(z) \to f(z_0)$ 一致逼近,

得 $\oint = 2\pi i\, f(z_0)$。

**推论 1（导数公式与无穷可导）** 全纯函数无穷可导,且

$$f^{(n)}(z_0) = \frac{n!}{2\pi i}\oint_{\gamma} \frac{f(z)}{(z - z_0)^{n+1}}\,\mathrm{d}z.$$

证明思路:对积分公式关于 $z_0$ 求导(核函数可逐次求导)。实分析中"可导一次"远不能推出

"可导两次";复分析中一次可导蕴含任意阶可导——刚性再次体现。

## Liouville 定理与代数基本定理

**定理 6（Liouville 定理）** 有界整函数(全平面上的有界全纯函数)必为常数。

证明思路:由 Cauchy 估计 $|f'(z_0)| \le \dfrac{M_R}{R}$($M_R$ 为 $|f|$ 在圆周

$|z - z_0| = R$ 上的上界),对有界函数取 $M_R \le M$ 后令 $R \to \infty$,得 $f' \equiv 0$,

故 $f$ 为常数。

**定理 7（代数基本定理的复分析证明）** 每个非常数复多项式都有根。

证明思路:反证。设 $P(z) = a_n z^n + \cdots + a_0$($a_n \ne 0$,$n \ge 1$)无根,则 $1/P$

是整函数。由 $|P(z)| \to \infty$($|z| \to \infty$ 时主项 $a_n z^n$ 占优),$1/P$ 有界,

Liouville 定理迫使 $1/P$ 为常数,与 $P$ 非常数矛盾。

!!! note "至此回顾"

    代数基本定理在 [复数](complex_numbers.md) 中只作陈述,本页给出完整证明:复分析三大工具

    (积分公式 → Cauchy 估计 → Liouville)一次配齐。

## 留数定理

**定义 3（孤立奇点与留数）** 若 $f$ 在 $z_0$ 的去心邻域内全纯而在 $z_0$ 处不(全纯),称 $z_0$

为孤立奇点。$f$ 在 $z_0$ 附近有 Laurent 展开 $f(z) = \sum_{n=-\infty}^{\infty} c_n (z - z_0)^n$,

其中系数 $c_{-1}$ 称为 $f$ 在 $z_0$ 的留数,记 $\operatorname{Res}(f, z_0)$。孤立奇点按展开的

负幂项分类:无负幂项为可去奇点;有限个负幂项为极点;无穷多个负幂项为本性奇点。对一阶极点可

简单计算:$\operatorname{Res}(f, z_0) = \lim_{z \to z_0}(z - z_0)f(z)$。

**例 6** $e^{1/z} = \sum_{n=0}^{\infty} \frac{1}{n! z^n}$ 在 $0$ 有本性奇点(Casorati–Weierstrass

定理:本性奇点邻域内函数值稠密);$1/z^2$ 在 $0$ 有二阶极点;$\sin z / z$ 在 $0$ 有可去奇点

(补充定义 $f(0) = 1$ 后全纯)。

**定理 8（留数定理）** 设 $f$ 在区域 $U$ 内除有限个孤立奇点 $z_1, \ldots, z_k$ 外全纯,

$\gamma$ 为 $U$ 内正向简单闭曲线且不经过奇点,则

$$\oint_{\gamma} f(z)\,\mathrm{d}z = 2\pi i \sum_{j=1}^{k} \operatorname{Res}(f, z_j),$$

其中求和只取 $\gamma$ 内部的奇点。

证明思路:在 $\gamma$ 内以每个 $z_j$ 为心挖去小圆 $\gamma_j$,环域上 $f$ 全纯,由 Cauchy 积分

定理 $\oint_\gamma f = \sum_j \oint_{\gamma_j} f$;在每个小圆上用 Laurent 展开,除 $n = -1$ 项

外各项积分为零(几何级数型的 $\oint (z-z_0)^n\,\mathrm{d}z$ 在 $n \ne -1$ 时为 $0$、在

$n = -1$ 时为 $2\pi i$),每项得 $2\pi i\, c_{-1}$。

**例 7（计算实积分）** 计算 $\displaystyle \int_{-\infty}^{\infty} \frac{\mathrm{d}x}{1 + x^2} = \pi$。

用半圆围道:取 $\gamma_R$ 为 $[-R, R]$ 与上半圆 $|z| = R$($\operatorname{Im} z > 0$)组成的闭路,

$R > 1$。被积函数在 $\gamma_R$ 内唯一的奇点为 $z = i$(一阶极点),其留数为

$$\operatorname{Res}\Big(\frac{1}{1+z^2}, i\Big) = \lim_{z \to i}\frac{z - i}{(z - i)(z + i)} = \frac{1}{2i},$$

故 $\oint_{\gamma_R} = 2\pi i \cdot \dfrac{1}{2i} = \pi$。上半圆弧上的积分按模估计:当 $R > 1$

时 $|1 + z^2| \ge R^2 - 1$,故

$$\Big|\int_{\text{半圆弧}} \frac{\mathrm{d}z}{1 + z^2}\Big| \le \frac{\pi R}{R^2 - 1} \to 0 \quad (R \to \infty),$$

于是 $\pi = \lim_{R \to \infty} \oint_{\gamma_R} = \displaystyle \int_{-\infty}^{\infty}

\frac{\mathrm{d}x}{1+x^2}$。

!!! note "留数定理的价值"

    一类本需繁复换元与分部积分的实积分,被归结为"找奇点、算留数"两步。这是复分析对实分析

    最著名的馈赠之一,也是留数定理名字的由来。

## 唯一性定理:全纯函数的刚性

**定理 9（唯一性定理）** 设 $f, g$ 在区域(连通开集)$U$ 上全纯。若 $f = g$ 于 $U$ 内某个在

$U$ 中有聚点的集合 $E$(例如含聚点的序列、非空开集、或实轴上的一段),则 $f \equiv g$ 于 $U$。

证明思路:令 $h = f - g$。设 $z_0$ 为 $E$ 在 $U$ 内的聚点,由连续性 $h(z_0) = 0$;由幂级数

展开,若 $h$ 不恒为零,其 Taylor 展开在 $z_0$ 有首个非零项 $c_m(z - z_0)^m$,则 $h$ 在 $z_0$

的去心邻域内无零点——与 $E$ 的聚点性矛盾。故 $z_0$ 的邻域内 $h \equiv 0$,再由连通性沿

"小圆链"逐步推广到整个 $U$。

**推论 2（解析延拓的唯一性）** 若两个全纯函数在实轴的一段上相等,则在其整个定义域上相等。

**定理 10（最大模原理）** 设 $f$ 在有界区域 $U$ 上全纯、在 $\overline{U}$ 上连续,则 $|f|$ 在

$\overline{U}$ 上的最大值在边界 $\partial U$ 上取得;若 $|f|$ 在 $U$ 内部某点达到最大值,

则 $f$ 为常数。

证明思路:由 Cauchy 积分公式的推论,$f(z_0)$ 等于圆周上的平均值(中值性质),故 $|f(z_0)|$ 不

超过圆周上的最大模;若内部取到最大模,反复用中值性质推出邻域内为常数,再由连通性推广到全

区域。这是"刚性"在模意义下的又一体现。

!!! note "刚性的极致"

    实分析中,两个 $C^\infty$ 函数可以在一个区间之外完全无关;复分析中,全纯函数在一个小集合

    (哪怕只是聚点序列)上的取值决定了一切。这种"局部决定整体"的刚性,是复分析最深刻也最

    优雅的特色。

## 延伸阅读

- [复数](complex_numbers.md):Euler 公式、单位根与代数基本定理的陈述
- [分析](../index.md):实分析与复分析的整体框架
- [符号表](../../notation/index.md):围道积分与复分析记号
