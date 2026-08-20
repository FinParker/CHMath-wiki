---
title: 向量空间
tags:
  - 线性代数
---

# 向量空间

向量空间是线性代数的基本研究对象。它把中学里"带方向的线段"抽象为满足八条公理的
代数结构，使得关于直线、平面、高维空间乃至函数集合的几何直觉，都能用同一套加法
与数乘的语言来表达。线性代数中的一切概念——子空间、基、维数、线性映射、矩阵、
行列式、特征值——都建立在向量空间之上。

## 域与向量空间

线性代数中"数"的集合是一个**域**。粗略地说，域是能做加、减、乘、除（除数非零）
的集合，如实数域 $\mathbb{R}$、复数域 $\mathbb{C}$、有理数域 $\mathbb{Q}$ 以及模
素数 $p$ 的有限域 $\mathbb{F}_p$。下文固定一个域 $\mathbb{F}$，所有向量空间都默认
定义在 $\mathbb{F}$ 上。

**定义 1（向量空间）**：设 $V$ 是非空集合，其元素称为**向量**。若在 $V$ 上定义了
加法 $+ : V \times V \to V$ 与数乘 $\cdot : \mathbb{F} \times V \to V$，并且满足
以下八条公理，则称 $V$ 是域 $\mathbb{F}$ 上的**向量空间**（或线性空间）。

**加法公理**（对任意 $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$）：

1. **结合律**：$(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v}
   + \mathbf{w})$；
2. **交换律**：$\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$；
3. **零元**：存在零向量 $\mathbf{0} \in V$，使 $\mathbf{v} + \mathbf{0} =
   \mathbf{v}$；
4. **逆元**：对每个 $\mathbf{v}$ 存在 $-\mathbf{v} \in V$，使 $\mathbf{v} +
   (-\mathbf{v}) = \mathbf{0}$。

**数乘公理**（对任意 $a, b \in \mathbb{F}$，$\mathbf{v} \in V$）：

5. **结合律**：$a(b\mathbf{v}) = (ab)\mathbf{v}$；
6. **单位元**：$1\mathbf{v} = \mathbf{v}$；
7. **分配律（向量加法）**：$a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} +
   a\mathbf{v}$；
8. **分配律（域加法）**：$(a + b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$。

!!! note "八条公理的意义"

    公理的价值不在于"恰好八条"，而在于把几何向量的运算规律完整抽象出来：任何满足
    这八条规律的对象（点、多项式、函数、矩阵……）都自动共享同一套线性理论。由公理
    还可推出常规事实：$0\mathbf{v} = \mathbf{0}$、$(-1)\mathbf{v} = -\mathbf{v}$、
    $a\mathbf{0} = \mathbf{0}$、$a\mathbf{v} = \mathbf{0} \Rightarrow a = 0$ 或
    $\mathbf{v} = \mathbf{0}$。

## 例子

**例 1（坐标空间 $\mathbb{F}^n$）**：$\mathbb{F}^n = \{(x_1, \dots, x_n) : x_i
\in \mathbb{F}\}$ 按分量相加、分量数乘构成向量空间。$n = 2, 3$ 时即为中学的平面
与空间向量；$n > 3$ 时几何直觉仍然适用，只是"看不见"。

**例 2（多项式空间）**：系数在 $\mathbb{F}$ 的多项式全体 $\mathbb{F}[x]$ 按通常
加法与数乘构成向量空间；次数不超过 $n$ 的多项式全体 $\mathbb{P}_n$ 也是向量空间。

**例 3（函数空间）**：从集合 $S$ 到 $\mathbb{F}$ 的一切函数 $\mathbb{F}^S = \{f
: S \to \mathbb{F}\}$，按逐点定义 $(f + g)(s) = f(s) + g(s)$、$(af)(s) = a
f(s)$ 构成向量空间。例如闭区间上的连续函数空间 $C[0, 1]$。

**例 4（矩阵空间）**：$m \times n$ 矩阵全体 $\mathrm{M}_{m \times n}(\mathbb{F})$
按矩阵加法与数乘构成向量空间（见 [矩阵](matrices.md)）。

**例 5（序列空间）**：一切序列 $(x_0, x_1, x_2, \dots)$（$x_i \in \mathbb{F}$）
按逐项运算构成向量空间，它是无限维的典型例子。

**例 6（零空间）**：$\{\mathbf{0}\}$ 是唯一的零维向量空间。

## 子空间

**定义 2（子空间）**：若 $V$ 的非空子集 $U$ 在 $V$ 的加法与数乘下本身构成向量
空间，则称 $U$ 是 $V$ 的**子空间**。

**定理 1（子空间判定）**：$V$ 的非空子集 $U$ 是子空间，当且仅当 $U$ 对加法和
数乘封闭：对任意 $\mathbf{u}, \mathbf{w} \in U$ 与 $a \in \mathbb{F}$，有
$\mathbf{u} + \mathbf{w} \in U$ 且 $a\mathbf{u} \in U$。等价地，对任意 $a, b
\in \mathbb{F}$ 与 $\mathbf{u}, \mathbf{w} \in U$ 有 $a\mathbf{u} + b\mathbf{w}
\in U$。

**证明**：必要性显然。充分性：封闭性保证 $\mathbf{0} = 0\mathbf{u} \in U$、
$-\mathbf{u} = (-1)\mathbf{u} \in U$，其余公理由 $V$ 直接继承，故 $U$ 自身是
向量空间。$\square$

!!! warning "常见误区"

    必须要求 $U$ **非空**且含 $\mathbf{0}$。过原点的直线、平面才是 $\mathbb{R}^3$
    的子空间；不过原点的"平移直线"不是子空间（不含零向量、加法不封闭）。

**例 7**：齐次线性方程组 $A\mathbf{x} = \mathbf{0}$ 的解集是 $\mathbb{F}^n$ 的
子空间（解的线性组合仍为解）；非齐次 $A\mathbf{x} = \mathbf{b} \neq \mathbf{0}$
的解集则不是（若 $\mathbf{x}, \mathbf{y}$ 都是解，则 $\mathbf{x} + \mathbf{y}$
一般不再是解）。

**命题 1（子空间的交与和）**：子空间族 $\{U_i\}_{i \in I}$ 的交 $\bigcap_i U_i$
仍是子空间；子空间 $U, W$ 的**和** $U + W = \{\mathbf{u} + \mathbf{w} : \mathbf{u}
\in U, \mathbf{w} \in W\}$ 是包含 $U \cup W$ 的最小子空间。而并集 $U \cup W$ 一般
**不是**子空间（除非一个包含另一个）。

**定理 2（Grassmann 维数公式）**：设 $U, W$ 是有限维空间 $V$ 的子空间，则
$\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$。

**证明思路**：取 $U \cap W$ 的基并分别扩展为 $U$ 的基与 $W$ 的基，合并所得向量组
张成 $U + W$；用两次线性无关性验证它线性无关，即得维数公式。$\square$

**例 8**：在 $\mathbb{R}^3$ 中取 $U$ 为 $xy$ 平面、$W$ 为 $xz$ 平面，则
$U \cap W$ 是 $x$ 轴（$\dim = 1$），$U + W = \mathbb{R}^3$（$\dim = 3$），公式
给出 $2 + 2 - 1 = 3$，一致。

## 线性组合与张成空间

**定义 3（线性组合）**：称 $\mathbf{v} = a_1 \mathbf{v}_1 + \dots + a_k
\mathbf{v}_k$（$a_i \in \mathbb{F}$）为向量组 $\mathbf{v}_1, \dots, \mathbf{v}_k$
的**线性组合**。

**定义 4（张成空间）**：集合 $S \subseteq V$ 的一切有限线性组合构成 $V$ 的子空间，
记作 $\operatorname{span}(S)$，称为 $S$ 的**张成空间**。若 $\operatorname{span}(S)
= V$，则称 $S$ **张成** $V$。

**命题 2**：$\operatorname{span}(S)$ 是包含 $S$ 的最小子空间（按包含关系）：任何
包含 $S$ 的子空间必包含 $\operatorname{span}(S)$。

**例 9**：在 $\mathbb{R}^3$ 中，$\operatorname{span}\{(1, 0, 0), (0, 1, 0)\}$ 是
$xy$ 平面；$\operatorname{span}\{(1, 1, 0), (2, 2, 0)\}$ 只是过原点的一条直线
（两个向量共线，只贡献一个自由度）。

## 线性无关与线性相关

**定义 5（线性无关）**：$S \subseteq V$ 称为**线性无关**的，若 $S$ 中任意有限个
互异向量 $\mathbf{v}_1, \dots, \mathbf{v}_k$ 都满足：由 $a_1 \mathbf{v}_1 +
\dots + a_k \mathbf{v}_k = \mathbf{0}$ 可推出 $a_1 = \dots = a_k = 0$。否则称
$S$ **线性相关**。

**命题 3（相关的等价刻画）**：有限集 $S = \{\mathbf{v}_1, \dots, \mathbf{v}_k\}$
线性相关，当且仅当其中某个向量可表示为其余向量的线性组合。

**证明**：若 $a_1 \mathbf{v}_1 + \dots + a_k \mathbf{v}_k = \mathbf{0}$ 且某个
$a_i \neq 0$，则 $\mathbf{v}_i = -\sum_{j \neq i} (a_j / a_i)\, \mathbf{v}_j$；
反之显然。$\square$

!!! warning "易错点"

    含零向量的集合必线性相关（$1 \cdot \mathbf{0} = \mathbf{0}$）；空集是线性无关
    的；单元素集 $\{\mathbf{v}\}$ 无关当且仅当 $\mathbf{v} \neq \mathbf{0}$；无关
    集的任意子集仍无关。

**例 10**：$\mathbb{R}^n$ 中标准基 $\mathbf{e}_1, \dots, \mathbf{e}_n$ 线性无关；
$\{(1, 1), (1, -1)\}$ 线性无关（$\mathbb{R}^2$ 中任意两个不共线的向量都无关）；
$\{(1, 1), (2, 2)\}$ 线性相关。

## 基与维数

**定义 6（基）**：$B \subseteq V$ 称为 $V$ 的**基**（Hamel 基），若 $B$ 线性无关
且张成 $V$。等价地，$B$ 是极大的线性无关组，也是极小的张成组。

**定理 3（基的存在性）**：每个向量空间都有基。

!!! note "选择公理"

    有限维情形可由归纳构造证明。对无限维空间，存在性依赖选择公理；事实上在 ZF 集合
    论中，"每个向量空间都有基"与选择公理等价（Blass, 1984）。故实践中接受该定理即可。

**定理 4（基的等势性）**：有限维向量空间 $V$ 的任意两个基所含向量的个数相同。

**证明思路**：这是 Steinitz 替换引理的推论：若 $A$ 线性无关、$B$ 张成 $V$，则可
把 $A$ 的元素逐个"替换"进 $B$，每次保持张成性，故 $|A| \le |B|$。对两个基互相
替换即得等势。$\square$

**定义 7（维数）**：有限维空间 $V$ 的**维数** $\dim V$ 定义为任取一个基所含向量
的个数；若 $V$ 没有有限基，则称 $V$ 是**无限维**的。

**例 11**：$\dim \mathbb{F}^n = n$（标准基 $\mathbf{e}_1, \dots, \mathbf{e}_n$）；
$\dim \mathbb{P}_n = n + 1$（基 $1, x, \dots, x^n$）；$\dim \mathrm{M}_{m \times
n}(\mathbb{F}) = mn$（基为恰有一个位置为 $1$ 的矩阵 $E_{ij}$）；$\mathbb{F}[x]$
是无限维的；有限集 $S$ 上 $\dim \mathbb{F}^S = |S|$（基为 $\delta_s$：在 $s$ 处
取 $1$、其余取 $0$ 的函数）。

**例 12（求基）**：设 $S = \{(1, 1, 0), (1, 0, 1), (0, 1, -1), (2, 1, 1)\}
\subseteq \mathbb{R}^3$。观察到前三个向量张成 $\mathbb{R}^3$（其行列式非零，见
[行列式](determinants.md)），而 $(2, 1, 1) = (1, 1, 0) + (1, 0, 1)$ 冗余，故可取
基 $\{(1, 1, 0), (1, 0, 1), (0, 1, -1)\}$。一般做法：把向量排成矩阵，用初等行
变换（见 [矩阵](matrices.md)）挑出主元列对应的向量。

## 坐标表示

**定义 8（有序基与坐标）**：设 $B = (\mathbf{v}_1, \dots, \mathbf{v}_n)$ 是 $V$
的有序基。每个 $\mathbf{v} \in V$ 有唯一表示 $\mathbf{v} = a_1 \mathbf{v}_1 +
\dots + a_n \mathbf{v}_n$，称

$$
[\mathbf{v}]_B = (a_1, \dots, a_n)^{\mathsf{T}} \in \mathbb{F}^n
$$

为 $\mathbf{v}$ 在 $B$ 下的**坐标向量**。

!!! note "坐标依赖基的选取"

    坐标是"相对基而言"的数表：换一个有序基，同一向量的坐标一般会改变；基的次序也
    影响坐标（交换基中两个向量，坐标的对应分量随之交换）。坐标映射 $\mathbf{v}
    \mapsto [\mathbf{v}]_B$ 是 $V$ 与 $\mathbb{F}^n$ 之间的双射，且保持加法和数乘
    ——这正是 [线性映射](linear_maps.md) 中"同构"的原型。

**例 13**：$\mathbb{R}^2$ 中取有序基 $B = ((1, 1), (1, -1))$，则 $(3, 1) =
2(1, 1) + 1(1, -1)$，坐标 $[(3, 1)]_B = (2, 1)$；而在标准基下其坐标是 $(3, 1)$。
同一向量，坐标随基而变。

## 直和

**定义 9（直和）**：设 $U, W$ 是 $V$ 的子空间。若每个 $\mathbf{v} \in V$ 都可
**唯一**地写成 $\mathbf{v} = \mathbf{u} + \mathbf{w}$（$\mathbf{u} \in U$，
$\mathbf{w} \in W$），则称 $V$ 是 $U$ 与 $W$ 的**直和**，记作 $V = U \oplus W$。

**定理 5（直和判定）**：若 $V = U + W$（即 $V$ 由 $U, W$ 张成），则 $V = U
\oplus W$ 当且仅当 $U \cap W = \{\mathbf{0}\}$。

**证明**：若 $V = U \oplus W$ 且 $\mathbf{v} \in U \cap W$，则 $\mathbf{v} =
\mathbf{v} + \mathbf{0} = \mathbf{0} + \mathbf{v}$ 是同一向量的两种分解，唯一性
迫使 $\mathbf{v} = \mathbf{0}$。反之，若 $\mathbf{u} + \mathbf{w} = \mathbf{u}'
+ \mathbf{w}'$，则 $\mathbf{u} - \mathbf{u}' = \mathbf{w}' - \mathbf{w} \in
U \cap W = \{\mathbf{0}\}$，故分解唯一。$\square$

**推论**：$\dim(U \oplus W) = \dim U + \dim W$。

**例 14**：$\mathbb{R}^2$ 中两条过原点的直线 $L_1, L_2$（互不重合）满足
$\mathbb{R}^2 = L_1 \oplus L_2$；对称矩阵与反对称矩阵的全体满足
$\mathrm{M}_n(\mathbb{F}) = \mathrm{Sym} \oplus \mathrm{Skew}$（当
$\operatorname{char} \mathbb{F} \neq 2$）。

!!! note "直和与并集"

    子空间之并 $U \cup W$ 一般**不是**子空间（见命题 1）。"直和"是比"并"更自然的
    构造，它把两个子空间"互不干扰"地拼成一个大空间。

## 延伸阅读

- [线性映射](linear_maps.md) — 保持向量空间结构的映射，同构与维数定理。
- [矩阵](matrices.md) — 线性映射的坐标表示，$\mathbb{F}^n$ 上的一切线性代数。
- [代数](../index.md) — 向量空间是"域上的模"，可联系环与群等代数结构。
- [集合论](../../foundations/set_theory/index.md) — 线性无关、基等概念用集合语言
  表述；基的存在性与选择公理。
