---
title: 复数
tags:
  - 复分析
---

# 复数

方程 $x^2 + 1 = 0$ 在实数范围内无解。复数域 $\mathbb{C}$ 的引入让这个方程(事实上是任意

多项式方程)有解,并由此发展出数学中最优美的理论之一——复分析。本页从 $\mathbb{R}^2$ 上的

乘法构造出发,建立复数的代数、度量与几何结构,为 [全纯函数](holomorphic_functions.md)

做好准备。

## 复数的定义

**定义 1（复数域）** 在集合 $\mathbb{R}^2$ 上定义加法与乘法:

$$(a, b) + (c, d) = (a + c, b + d), \qquad (a, b)\cdot(c, d) = (ac - bd, ad + bc).$$

连同这两种运算,$\mathbb{R}^2$ 构成域,称为复数域,记作 $\mathbb{C}$。

**定理 1** $\mathbb{C}$ 是域:加法与乘法都满足结合律、交换律与分配律,零元为 $(0,0)$,

幺元为 $(1,0)$,且非零元可逆。

证明要点:结合律与分配律按定义直接验证(乘法公式展开后整理);可逆性见命题 1。把 $(a, b)$

记作 $a + bi$,其中 $i = (0, 1)$,则

$$i^2 = (0,1)\cdot(0,1) = (-1, 0) = -1,$$

即 $i$ 是方程 $x^2 + 1 = 0$ 的根。$a$ 称为 $z = a + bi$ 的实部 $\operatorname{Re} z$,$b$ 称为

虚部 $\operatorname{Im} z$;虚部为零的复数即实数,故 $\mathbb{R}$ 以 $a \mapsto (a, 0)$ 嵌入

$\mathbb{C}$,成为子域。作为实数域上的向量空间,$\mathbb{C}$ 与 $\mathbb{R}^2$ 同构,基为

$\{1, i\}$。

!!! note "为什么乘法这样定义"

    形式地要求 $(a + bi)(c + di) = ac + ad\,i + bc\,i + bd\,i^2$,再代入 $i^2 = -1$,就得

    $ac - bd + (ad + bc)i$。定义 1 不过是把这个形式运算严格化——"先形式地算,再严格地定义"

    是数学构造的常用手法。

## 共轭与模

**定义 2（共轭与模）** 对 $z = a + bi$,共轭 $\bar{z} = a - bi$,模 $|z| = \sqrt{a^2 + b^2}$。

**命题 1（基本恒等式）**

$$z\bar{z} = |z|^2, \qquad \overline{z + w} = \bar{z} + \bar{w}, \qquad \overline{zw} = \bar{z}\,\bar{w}, \qquad |zw| = |z||w|,$$

且对 $z \ne 0$,

$$\frac{1}{z} = \frac{\bar{z}}{|z|^2},$$

于是 $\mathbb{C}$ 中除法可行:$\dfrac{w}{z} = \dfrac{w\bar{z}}{|z|^2}$。这一"分母有理化"技巧

是复数运算的基本功。

**例 1** $\dfrac{1}{1+i} = \dfrac{1-i}{(1+i)(1-i)} = \dfrac{1-i}{2} = \dfrac{1}{2} - \dfrac{1}{2}i$;

$(1+i)^2 = 2i$。

**定理 2（三角不等式）** $|z + w| \le |z| + |w|$,且等号成立当且仅当 $z$ 与 $w$ 同向(一者为

另一者的非负实数倍)。

证明思路:$|z+w|^2 = (z+w)(\bar{z}+\bar{w}) = |z|^2 + |w|^2 + 2\operatorname{Re}(z\bar{w}) \le

|z|^2 + |w|^2 + 2|z\bar{w}| = (|z|+|w|)^2$。几何上,$|z - w|$ 是复平面上两点间的距离,三角

不等式即"两边之和大于第三边"。

**命题 2（复数域不是有序域）** $\mathbb{C}$ 上不存在与加法和乘法相容的全序。

证明思路:若存在这样的序,则 $0 < 1$,故 $0 < 1^2 + i^2 \cdot (-1)$ 导出矛盾。更直接地,

有序域中任何非零元的平方为正,但 $i^2 = -1 < 0$。因此复数的比较(如 $z < w$)无意义,

复分析只能依赖模与几何。

## 极坐标与 Euler 公式

**定义 3（辐角）** 对 $z \ne 0$,存在 $\theta$ 使 $z = r(\cos\theta + i\sin\theta)$,其中

$r = |z|$;$\theta$ 称为 $z$ 的辐角。辐角不唯一(可加 $2\pi$ 的整数倍),落在 $(-\pi, \pi]$

中的那个记为 $\operatorname{Arg} z$。

**定理 3（Euler 公式）** 对 $\theta \in \mathbb{R}$,

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

证明思路(级数):把 $e^{i\theta}$ 定义为 $\sum_{n=0}^{\infty}\frac{(i\theta)^n}{n!}$,按实部

与虚部分离,恰得 $\cos\theta$ 与 $\sin\theta$ 的幂级数展开。由此定义复指数

$$e^{z} = e^{a+bi} = e^a(\cos b + i\sin b),$$

它满足 $e^{z+w} = e^z e^w$(对任意复数成立)。特别地,$e^{i\pi} + 1 = 0$,把 $e$、$i$、$\pi$、

$1$、$0$ 五个常数联结在一个等式中。

**推论 1（极坐标与指数形式）** $z = re^{i\theta}$,$r = |z|$。辐角满足 $\operatorname{Arg}(zw)

\equiv \operatorname{Arg} z + \operatorname{Arg} w \pmod{2\pi}$——这正来自指数法则

$e^{i\theta_1}e^{i\theta_2} = e^{i(\theta_1+\theta_2)}$。

**定理 4（de Moivre 公式）** 对 $n \in \mathbb{N}$,

$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta).$$

证明:由 Euler 公式,左边 $= (e^{i\theta})^n = e^{in\theta}$。推论:取实部虚部即得倍角公式

$\cos 2\theta = \cos^2\theta - \sin^2\theta$、$\sin 2\theta = 2\sin\theta\cos\theta$,以及

$\cos 3\theta = 4\cos^3\theta - 3\cos\theta$ 等。

**例 2** $(1+i)^{10} = (\sqrt{2}\,e^{i\pi/4})^{10} = 2^5 e^{i 10\pi/4} = 32 e^{i\pi/2} = 32i$。

## 复数的几何

把 $z = a + bi$ 看作平面上的点 $(a, b)$:

- 加法 $z + w$ = 向量的平移:点 $z$ 沿向量 $w$ 移动;
- 共轭 $\bar{z}$ = 关于实轴的反射;
- 模 $|z|$ = 到原点的距离;乘法 $zw$ = 旋转 + 伸缩:由 $|zw| = |z||w|$ 与辐角相加,乘以

  $z = re^{i\theta}$ 把每个点绕原点旋转 $\theta$ 并放大 $r$ 倍。

**例 3** 乘以 $i$ 是绕原点逆时针旋转 $90^\circ$;乘以 $e^{i\theta}$ 是旋转 $\theta$。因此复数的

乘法统一了保向相似变换:任何一个旋转-伸缩复合都可写成 $z \mapsto az + b$($a \ne 0$)。

**例 4** 集合 $\{z : |z - z_0| = r\}$ 是以 $z_0$ 为圆心、$r$ 为半径的圆;$\{z : |z - z_0|

< r\}$ 是开圆盘。复数的语言让圆的方程变为一个简洁的模等式。

!!! note "旋转与三角恒等式"

    $e^{i\theta}$ 的几何意义让三角恒等式有了直观:两个旋转的复合仍是旋转,角度相加。这也是

    Euler 公式被称为"最美丽的数学公式"的几何来源。

## 单位根

**定义 4（单位根）** 方程 $z^n = 1$ 的 $n$ 个复数解称为 $n$ 次单位根:

$$\omega_k = e^{2\pi i k / n} = \cos\frac{2\pi k}{n} + i\sin\frac{2\pi k}{n}, \qquad k = 0, 1, \ldots, n-1.$$

它们在单位圆上均匀分布,构成正 $n$ 边形的顶点;在乘法下成群(循环群),生成元为

$\omega_1 = e^{2\pi i/n}$。$z^n = 1$ 的解中,$\omega_k$ 称为本原根若 $\omega_k^m \ne 1$ 对所有

$1 \le m < n$ 成立(即 $k$ 与 $n$ 互素)。

**命题 3** 设 $\omega = \omega_1$。则 $\sum_{k=0}^{n-1} \omega^k = 0$($n \ge 2$)。

证明思路:等比求和 $\sum_{k=0}^{n-1} \omega^k = \dfrac{\omega^n - 1}{\omega - 1} = 0$,因

$\omega^n = 1$ 且 $\omega \ne 1$。

**例 5** 三次单位根为 $1, \omega, \omega^2$,其中 $\omega = -\dfrac{1}{2} + \dfrac{\sqrt{3}}{2}i$,

满足 $1 + \omega + \omega^2 = 0$;它们正是 $x^3 = 1$ 的三个根,在复平面上构成等边三角形。

四次单位根为 $1, i, -1, -i$,是单位圆内接正方形。

## 代数基本定理

**定理 5（代数基本定理）** 每个非常数复系数多项式

$$P(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_0 \quad (a_n \ne 0,\ n \ge 1)$$

在 $\mathbb{C}$ 中至少有一个根。

**推论 2** $n$ 次复系数多项式恰有 $n$ 个根(计重数),即在 $\mathbb{C}$ 上可完全分解:

$P(z) = a_n\prod_{j=1}^{n}(z - z_j)$。展开比较系数得 Vieta 公式,如两根之和

$z_1 + z_2 = -a_{n-1}/a_n$ 等。

!!! note "证明的工具在复分析里"

    代数基本定理的第一个严格证明由 Gauss 于 1799 年给出。现代最优雅的证明利用 Liouville 定理

    (有界整函数为常数),详见 [全纯函数](holomorphic_functions.md)。它表明 $\mathbb{C}$ 是

    代数封闭域——这是引入复数最深刻的理由。

## 延伸阅读

- [全纯函数](holomorphic_functions.md):复可导函数,代数基本定理的现代证明
- [分析](../index.md):从实数到复数的分析框架
- [符号表](../../notation/index.md):$\mathbb{C}$、共轭与模的记号约定
