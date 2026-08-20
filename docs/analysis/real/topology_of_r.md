---
title: 实数的拓扑
tags:
  - 实分析
---

# 实数的拓扑

[实数公理](real_numbers.md) 给出了"数"的代数与序结构,而分析学还需要一个描述"接近"

与"极限"的语言——拓扑。实数的拓扑研究 $\mathbb{R}$ 上由绝对值距离导出的开集、闭集、

紧致与连通等概念。它们把极限过程从序列推广到集合层面,是 [连续函数](continuity.md)

与后续所有分析内容的舞台。

本页贯穿始终的问题是:哪些性质只依赖"距离",不依赖坐标的细节?答案是拓扑性质。

紧致性与连通性就是其中最重要的两个,它们分别刻画"有限性"与"整体性"。

## 绝对值与距离

**定义 1（绝对值）** 对 $x \in \mathbb{R}$,$|x| = \max\{x, -x\}$。它满足:

- 非负性:$|x| \ge 0$,且 $|x| = 0 \iff x = 0$;
- 齐次性:$|xy| = |x||y|$;
- 三角不等式:$|x + y| \le |x| + |y|$。

**定义 2（度量）** 映射 $d(x, y) = |x - y|$ 称为 $\mathbb{R}$ 上的欧氏度量(距离)。度量公理:

非负性($d \ge 0$,等号当且仅当 $x = y$)、对称性($d(x,y) = d(y,x)$)、三角不等式

($d(x,z) \le d(x,y) + d(y,z)$)。由三角不等式可得反向不等式 $|d(x,z) - d(y,z)| \le d(x,y)$,

它是"距离函数的连续性"的雏形。

**定义 3（开球与邻域）** 以 $x$ 为中心、半径 $r > 0$ 的开区间 $B(x, r) = (x - r, x + r)$

称为开球。包含某个开球 $B(x, r)$ 的集合称为 $x$ 的一个邻域。$x$ 的 $\varepsilon$-邻域指

开球 $B(x, \varepsilon)$。

!!! note "为什么是 $\varepsilon$-邻域"

    $\varepsilon$ 可以被任意取小:凡涉及"充分接近"的命题,都表述为"对任意 $\varepsilon > 0$

    存在…"。这正是 $\varepsilon$-$\delta$ 语言的空间形式。

## 序列与收敛

**定义 4（收敛）** 序列 $(x_n)$ 收敛于 $x$,若对任意 $\varepsilon > 0$ 存在 $N$ 使

$n \ge N$ 时 $|x_n - x| < \varepsilon$,记 $x_n \to x$。用邻域语言:每个 $\varepsilon$-邻域

都含有 $(x_n)$ 的"尾巴"。

**命题 1（极限的性质）** 收敛序列的极限唯一;收敛序列有界;若 $x_n \to x$、$y_n \to y$,

则 $x_n \pm y_n \to x \pm y$、$x_n y_n \to xy$,且当 $y \ne 0$ 时 $x_n / y_n \to x / y$。

证明思路:唯一性用"两个极限之间取 $\varepsilon$ 太小"的三角不等式;和的极限用 $\varepsilon/2$;

积的极限先证有界再分解 $|x_n y_n - xy| \le |x_n - x||y_n| + |x||y_n - y|$。

## 开集与闭集

**定义 5（开集）** 集合 $E \subseteq \mathbb{R}$ 称为开集,若 $E$ 中每一点都是内点:对每个

$x \in E$ 存在 $r > 0$ 使 $B(x, r) \subseteq E$。

**定义 6（闭集）** $E$ 称为闭集,若其补集 $E^c = \mathbb{R} \setminus E$ 是开集。

**例 3** 开区间是开集,闭区间是闭集;$(a, b]$ 既不开也不闭;$\varnothing$ 与 $\mathbb{R}$

既开又闭。

**命题 2（开闭集的基本运算）**

- 任意个开集的并是开集;有限个开集的交是开集;
- 任意个闭集的交是闭集;有限个闭集的并是闭集。

证明思路:两条都由定义直接验证;并的情形取半径,交的情形取半径的最小值。注意"任意"与

"有限"不能互换:$\bigcap_{n=1}^{\infty}(-1/n, 1/n) = \{0\}$ 不是开集。

**定理 1（$\mathbb{R}$ 中开集的结构）** $\mathbb{R}$ 中每个非空开集都是至多可数个互不相交

开区间的并。

证明思路:对 $x \in E$,取包含 $x$ 的最大开区间 $I_x$(所有含 $x$ 的开子区间之并);两个

这样的最大区间要么相同要么不相交,故它们构成两两不交的开区间族,且由 $\mathbb{Q}$ 的稠密性

知该族至多可数(每个区间各含一个有理数)。

## 聚点、孤立点与闭包

**定义 7（聚点）** 设 $E \subseteq \mathbb{R}$。$x$ 称为 $E$ 的聚点,若对任意 $r > 0$,去心

邻域 $B(x, r) \setminus \{x\}$ 与 $E$ 相交。聚点全体记作 $E'$。

**定义 8（孤立点）** $x \in E$ 称为孤立点,若 $x$ 不是 $E$ 的聚点,即存在 $r > 0$ 使

$B(x, r) \cap E = \{x\}$。

**定义 9（闭包）** $E$ 的闭包定义为 $\overline{E} = E \cup E'$。

**定理 2（闭包的序列刻画）** $x \in \overline{E}$ 当且仅当存在 $E$ 中的序列 $(x_n)$ 收敛到 $x$。

证明思路:必要性:若 $x \in E$ 取常值序列;否则对每个 $n$ 取 $x_n \in E \cap B(x, 1/n)$

(聚点定义保证存在)。充分性:若 $x_n \to x$ 且 $x_n \in E$,则对任意 $r > 0$ 存在

$x_n \in B(x, r)$,故 $x \in E \cup E'$。

**命题 3（闭包的运算性质）** 闭包是包含 $E$ 的最小闭集;内部 $\operatorname{int} E$ 是含于 $E$

的最大开集;且 $A \subseteq B \implies \overline{A} \subseteq \overline{B}$。

**命题 4（闭集的刻画）** 以下等价:(i) $E$ 是闭集;(ii) $E = \overline{E}$;(iii) $E' \subseteq E$;

(iv) $E$ 中收敛序列的极限仍在 $E$ 中。

证明思路:由定义与定理 2 直接推出;第 (iv) 条是"闭集对取极限封闭"这一直观的精确表述,

它把拓扑语言与序列语言缝合在一起。

**定义 10（内部与边界）** $E$ 的内部 $\operatorname{int} E$ 是 $E$ 的所有内点之集;边界

$\partial E = \overline{E} \setminus \operatorname{int} E$。$x \in \partial E$ 当且仅当 $x$ 的每个

邻域都与 $E$ 及其补集相交。

**例 4** 对 $E = (0, 1]$:$\operatorname{int} E = (0,1)$、$\overline{E} = [0,1]$、

$\partial E = \{0, 1\}$、聚点集 $E' = [0,1]$、孤立点集为空。对 $E = \mathbb{Z}$:每点都是

孤立点,$E' = \varnothing$、$\overline{E} = E$。对 $E = \mathbb{Q}$:$\operatorname{int} E = \varnothing$、

$\overline{E} = \mathbb{R}$(稠密性!)、$\partial E = \mathbb{R}$。

## 紧致子集与 Heine–Borel 定理

**定义 11（开覆盖）** 一族开集 $\{U_\lambda\}_{\lambda \in \Lambda}$ 覆盖集合 $K$,若

$K \subseteq \bigcup_\lambda U_\lambda$。

**定义 12（紧致）** $K$ 称为紧致的,若 $K$ 的每个开覆盖都有有限子覆盖。

紧致性是"有限性"在无限世界中的化身:无论覆盖多细,总能从中挑出有限个仍盖住 $K$。

在 $\mathbb{R}$ 中,紧致性有一个简单到惊人的刻画:

**定理 3（Heine–Borel）** $K \subseteq \mathbb{R}$ 紧致当且仅当 $K$ 有界且闭。

证明思路分两步。

$(\Rightarrow)$ 有界:用开覆盖 $\{(-n, n)\}_{n \in \mathbb{N}}$,$K$ 的有限子覆盖给出界。闭:

设 $x \notin K$。对每个 $y \in K$,取以 $y$ 为中心、半径 $< |x-y|/2$ 的开区间 $U_y$

(不含 $x$);有限子覆盖 $U_{y_1}, \ldots, U_{y_n}$ 给出 $\delta = \min_i |x - y_i|/2 > 0$。

若 $z \in B(x, \delta) \cap K$,则 $z \in U_{y_i}$ 对某个 $i$ 成立,而

$$|x - y_i| \le |x - z| + |z - y_i| < \frac{|x-y_i|}{2} + \frac{|x-y_i|}{2} = |x - y_i|,$$

矛盾,故 $B(x, \delta) \cap K = \varnothing$,$K^c$ 是开集。

$(\Leftarrow)$ 设 $K \subseteq [a, b]$ 且 $K$ 闭。反证:若某开覆盖 $\mathcal{U}$ 没有有限子覆盖,

把 $[a,b]$ 二等分,至少一半的闭区间被 $\mathcal{U}$ 覆盖时无有限子覆盖,取这一半继续二分,

得闭区间套 $[a_n, b_n]$(每个都无有限子覆盖,长度 $\to 0$)。由闭区间套定理存在

$x \in \bigcap_n [a_n, b_n]$;因 $K$ 闭,必有 $x \in K$(否则 $x$ 在开集 $K^c$ 中,而区间套

收缩到 $x$,矛盾)。取 $U \in \mathcal{U}$ 含 $x$,则 $U$ 含某个 $[a_n, b_n]$ 的邻域,单个 $U$

就覆盖 $[a_n, b_n]$,与"无有限子覆盖"矛盾。

**推论 1** 闭区间 $[a, b]$ 紧致;$\mathbb{R}$ 本身不紧致(开覆盖 $\{(-n, n)\}$ 无有限子覆盖)。

!!! note "Heine–Borel 定理的名字"

    定理得名于 Eduard Heine 与 Émile Borel。"有界 + 闭"是 $\mathbb{R}$ 中的具体刻画;在一般

    度量空间中,完备且全有界等价于紧致,是它的抽象推广。

## Bolzano–Weierstrass 定理

**定理 4（Bolzano–Weierstrass）** $\mathbb{R}$ 中每个有界序列都有收敛子列。

证明思路:与 [实数公理](real_numbers.md) 中 $3 \Rightarrow 4$ 相同:把有界序列放进闭区间,

反复二等分,保留含无穷多项的一半,得到收敛子列。改用聚点语言,还有:

**推论 2（聚点定理）** 每个有界无限集都有聚点。

证明思路:从无限集中取出互异的点列(有界),由 Bolzano–Weierstrass 有收敛子列,其极限即

聚点。

!!! note "三种语言的同一件事"

    紧致性(覆盖语言)、Bolzano–Weierstrass(序列语言)与"有界闭集"(序语言)在 $\mathbb{R}$

    中彼此等价,正如完备性公理的五种表述等价一样。它们为 [连续函数](continuity.md) 中的

    最值定理提供了两条证明路线:覆盖语言与序列语言。

## 连通性与区间

**定义 13（分离与连通）** 集合 $E \subseteq \mathbb{R}$ 称为不连通的,若存在非空集合 $A, B$

使得 $E = A \cup B$、$A \cap B = \varnothing$,且 $A, B$ 都相对 $E$ 开(即各为某个开集与

$E$ 之交);否则称 $E$ 连通。

直观上,连通集合是"一整块"。在 $\mathbb{R}$ 中,连通集合恰是我们最熟悉的形状:

**定理 5（连通子集 = 区间）** $E \subseteq \mathbb{R}$ 连通当且仅当 $E$ 是区间:对任意

$x < z < y$,若 $x, y \in E$ 则 $z \in E$。

证明思路分两步。

$(\Rightarrow)$ 反证:若 $E$ 不是区间,存在 $x < z < y$,$x, y \in E$ 而 $z \notin E$。令

$A = E \cap (-\infty, z)$、$B = E \cap (z, \infty)$,则 $A, B$ 非空、不相交、相对开且并为

$E$,与连通矛盾。

$(\Leftarrow)$ 设 $E$ 是区间但 $E = A \cup B$ 是分离分解。取 $a \in A$、$b \in B$ 且

$a < b$(必要时交换 $A, B$),令 $c = \sup(A \cap [a, b])$。由 $E$ 是区间知 $c \in E$。

若 $c \in A$:因 $A$ 相对开,存在 $\delta > 0$ 使 $(c - \delta, c + \delta) \cap E \subseteq A$;

取 $t \in (c, \min(c + \delta, b)) \cap E$(由 $E$ 是区间,非空),则 $t \in A$ 且 $t > c$,

与 $c$ 是上界矛盾。若 $c \in B$:因 $B$ 相对开,存在 $\delta > 0$ 使

$(c - \delta, c + \delta) \cap E \subseteq B$;但 $c = \sup(A \cap [a,b])$ 保证存在

$s \in A \cap (c - \delta, c) \cap E \subseteq B$,与 $A \cap B = \varnothing$ 矛盾。

!!! note "区间套与连通性"

    两个方向分别体现两种典型技巧:反向用"中间掏空一点"制造分离;正向用上确界(完备性)

    找到"卡在 $A$ 与 $B$ 之间"的点。完备性又一次是核心——若把讨论搬进 $\mathbb{Q}$,

    区间 $E = \mathbb{Q} \cap [0, \sqrt{2}]$ 的类似论证就会失败。

## 延伸阅读

- [实数公理](real_numbers.md):完备性公理与闭区间套定理,本页一切定理的源头
- [连续函数](continuity.md):紧致性与连通性在连续映射下的保持,介值定理与最值定理
- [拓扑空间](../../topology/index.md):把 $\mathbb{R}$ 上的开集公理化,抽象拓扑的起点
- [符号表](../../notation/index.md):集合与拓扑记号汇总
