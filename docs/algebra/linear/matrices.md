---
title: 矩阵
tags:
  - 线性代数
---

# 矩阵

矩阵是线性映射的"坐标账本"：选定基之后，线性映射的一切信息浓缩进一张矩形数表。
矩阵乘法之所以那样定义，正是为了精确对应线性映射的复合。矩阵把抽象的线性代数
变成具体的、可计算的算术——从解方程组到特征值计算，都围绕矩阵展开。

## 定义与记号

**定义 1（矩阵）**：$m \times n$ **矩阵**是排成 $m$ 行 $n$ 列的数表 $A =
(a_{ij})$，其中 $a_{ij} \in \mathbb{F}$。$m \times n$ 矩阵的全体记作
$\mathrm{M}_{m \times n}(\mathbb{F})$；$m = n$ 时称为**方阵**，记作
$\mathrm{M}_n(\mathbb{F})$。

记法约定：$A$ 的第 $i$ 行为行向量 $(a_{i1}, \dots, a_{in})$，第 $j$ 列为列向量
$(a_{1j}, \dots, a_{mj})^{\mathsf{T}}$。特殊矩阵：零矩阵 $O$（元素全为零）、对角
矩阵（非对角元为零）、上三角/下三角矩阵、单位矩阵 $I_n = (\delta_{ij})$
（$\delta$ 为 Kronecker 记号：$i = j$ 时为 $1$，否则为 $0$）。

## 矩阵运算

**定义 2（加法与数乘）**：同尺寸矩阵按分量相加、数乘：$(A + B)_{ij} = a_{ij} +
b_{ij}$，$(cA)_{ij} = c\, a_{ij}$。

**命题 1**：$\mathrm{M}_{m \times n}(\mathbb{F})$ 关于加法与数乘构成 $\mathbb{F}$
上的向量空间，$\dim = mn$；一组基是 $E_{ij}$——第 $(i, j)$ 个位置为 $1$、其余
位置为 $0$ 的矩阵（见 [向量空间](vector_spaces.md)）。

**定义 3（转置与共轭转置）**：$A$ 的**转置** $A^{\mathsf{T}}$ 满足
$(A^{\mathsf{T}})_{ij} = a_{ji}$（行列互换）。当 $\mathbb{F} = \mathbb{C}$ 时，
**共轭转置** $A^{*} = \overline{A^{\mathsf{T}}}$（先转置再逐元素共轭）。

**命题 2**：$(A^{\mathsf{T}})^{\mathsf{T}} = A$，$(A + B)^{\mathsf{T}} =
A^{\mathsf{T}} + B^{\mathsf{T}}$，$(cA)^{\mathsf{T}} = c A^{\mathsf{T}}$，
$(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$（**顺序反转**）；对共轭转置
同样成立。

**注（次序反转的验证）**：取 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$、
$B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$，则 $AB = \begin{pmatrix} 2 & 1
\\ 4 & 3 \end{pmatrix}$，$(AB)^{\mathsf{T}} = \begin{pmatrix} 2 & 4 \\ 1 & 3
\end{pmatrix}$；而 $B^{\mathsf{T}} A^{\mathsf{T}} = \begin{pmatrix} 0 & 1 \\ 1 & 0
\end{pmatrix} \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} = \begin{pmatrix} 2 & 4
\\ 1 & 3 \end{pmatrix}$，二者相等。

**定义 4（特殊对称性）**：$A$ 对称 $\iff A = A^{\mathsf{T}}$；反对称 $\iff A =
-A^{\mathsf{T}}$；在 $\mathbb{C}$ 上，$A$ 厄米 $\iff A = A^{*}$。

## 矩阵乘法

**定义 5（矩阵乘法）**：设 $A$ 是 $m \times n$ 矩阵，$B$ 是 $n \times p$ 矩阵，
则 $AB$ 是 $m \times p$ 矩阵，其第 $(i, k)$ 个元素为

$$
(AB)_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk},
$$

即 $A$ 的第 $i$ 行与 $B$ 的第 $k$ 列的"点积"。要求 $A$ 的列数等于 $B$ 的行数。

**为什么这样定义？** 因为要精确对应线性映射的复合。设 $f : \mathbb{F}^{p} \to
\mathbb{F}^{n}$ 由 $A$（$n \times p$）表示，$g : \mathbb{F}^{n} \to
\mathbb{F}^{m}$ 由 $B$（$m \times n$）表示，即 $f(\mathbf{v}) = A\mathbf{v}$、
$g(\mathbf{w}) = B\mathbf{w}$。则复合 $g \circ f$ 的矩阵 $C$ 应满足 $C\mathbf{v}
= B(A\mathbf{v})$ 对一切 $\mathbf{v}$。逐分量计算：

$$
(B A \mathbf{v})_i = \sum_j b_{ij} (A\mathbf{v})_j
= \sum_j b_{ij} \sum_k a_{jk} v_k
= \sum_k \Big(\sum_j b_{ij} a_{jk}\Big) v_k,
$$

故 $C = BA$。于是：**线性映射的复合 = 矩阵乘法**，而乘法的结合律 $(AB)C =
A(BC)$ 自动来自复合的结合律。

**例 1（具体计算）**：

$$
\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
= \begin{pmatrix} 1\cdot 0 + 2\cdot 1 & 1\cdot 1 + 2\cdot 0 \\
3\cdot 0 + 4\cdot 1 & 3\cdot 1 + 4\cdot 0 \end{pmatrix}
= \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix} .
$$

**命题 3（运算律）**：分配律 $A(B + C) = AB + AC$、$(A + B)C = AC + BC$；数乘
结合 $(cA)B = A(cB) = c(AB)$；结合律 $(AB)C = A(BC)$；$I_n A = A = A I_n$。

**注（对角矩阵的效果）**：左乘 $\operatorname{diag}(c_1, \dots, c_m)$ 把 $A$ 的
第 $i$ 行放大 $c_i$ 倍；右乘 $\operatorname{diag}(d_1, \dots, d_n)$ 把第 $j$ 列
放大 $d_j$ 倍。对角矩阵表示"按坐标缩放"，这也是 [特征值与特征向量](eigenvalues.md)
中"对角化使线性变换化为缩放"的直观来源。

!!! warning "乘法不交换、无零因子"

    矩阵乘法一般**不可交换**：如 $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，
    $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$，则 $AB = \begin{pmatrix} 1
    & 0 \\ 0 & 0 \end{pmatrix} \neq \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} =
    BA$。而且**非零矩阵的乘积可以为零**（上例 $A^2 = O$），故不能随意"消去"：
    $AB = AC$ 推不出 $B = C$，除非 $A$ 可逆。

!!! note "块矩阵"

    把矩阵按纵横线分成若干小块（块矩阵）后，只要各块尺寸相容，乘法仍按"块点积"进行。
    例如 $\begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}
    \begin{pmatrix} B_{11} \\ B_{21} \end{pmatrix} = \begin{pmatrix} A_{11}B_{11}
    + A_{12}B_{21} \\ A_{21}B_{11} + A_{22}B_{21} \end{pmatrix}$。块运算在理论推导
    与分治算法（如 Strassen 乘法）中极其有用。

## 单位矩阵与逆矩阵

**定义 6（逆矩阵）**：方阵 $A \in \mathrm{M}_n(\mathbb{F})$ 称为**可逆**（非奇异），
若存在 $B$ 使 $AB = BA = I_n$；此时 $B$ 唯一，记作 $A^{-1}$。

**命题 4**：逆矩阵若存在必唯一；对 $n$ 阶方阵，左逆即右逆：由 $AB = I$ 可推出
$BA = I$。

**命题 5（逆的运算）**：$(AB)^{-1} = B^{-1} A^{-1}$（顺序反转）；
$(A^{\mathsf{T}})^{-1} = (A^{-1})^{\mathsf{T}}$；$(A^{-1})^{-1} = A$；
$(cA)^{-1} = c^{-1} A^{-1}$（$c \neq 0$）。

**例 2（2 × 2 逆矩阵公式）**：若 $ad - bc \neq 0$，则

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1}
= \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} .
$$

直接相乘即可验证（对角线交换、副对角线变号）。

**定理 1（可逆的等价刻画）**：对 $n$ 阶方阵 $A$，下列条件等价：

1. $A$ 可逆；
2. $\operatorname{rank} A = n$（满秩）；
3. $\det A \neq 0$（见 [行列式](determinants.md)）；
4. $A$ 的列（行）向量线性无关；
5. 对任意 $\mathbf{b} \in \mathbb{F}^n$，方程 $A\mathbf{x} = \mathbf{b}$ 有唯一解。

## 初等行变换与 Gauss 消元

**定义 7（初等行变换）**：以下三种变换称为初等行变换：

1. **交换**两行；
2. 某行乘以**非零**常数；
3. 把某行的倍数**加到**另一行。

**定义 8（初等矩阵）**：对单位矩阵 $I$ 施行一次初等行变换得到的矩阵称为初等矩阵
$E$。关键性质：对 $A$ 施行某次初等行变换，等价于**左乘**对应的初等矩阵 $EA$。
因此初等矩阵都可逆（其逆是施行逆变换所得），且任意可逆矩阵可分解为初等矩阵的乘积。

**Gauss 消元**：用初等行变换把增广矩阵 $[A \mid \mathbf{b}]$ 化为**行阶梯形**（每行
首个非零元逐行右移），再化为**行最简形**（RREF，首元为 $1$ 且所在列其余元素为零）。
主要用途：

- **解方程组**：从阶梯形回代得解；若出现形如 $[0 \cdots 0 \mid c]$（$c \neq 0$）
  的行则无解；
- **求秩**：阶梯形的非零行数即 $\operatorname{rank} A$；
- **求逆**：当 $A$ 可逆时，对增广矩阵 $[A \mid I]$ 做行变换至 $[I \mid A^{-1}]$。

**例 3（消元求逆）**：对 $A = \begin{pmatrix} 1 & 1 \\ 2 & 4 \end{pmatrix}$ 施以
行变换：$[A \mid I] = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 2 & 4 & 0 & 1
\end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & 2 & -2 & 1
\end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & 2 & -\tfrac{1}{2} \\ 0 & 1
& -1 & \tfrac{1}{2} \end{pmatrix}$，故 $A^{-1} = \begin{pmatrix} 2 & -\tfrac{1}{2}
\\ -1 & \tfrac{1}{2} \end{pmatrix}$。

!!! note "行变换保持什么与代价"

    行变换不改变方程组的解集，不改变矩阵的秩，也不改变行列式的"是否为零"；但会改变
    行列式的具体值（交换变号、倍乘放大、行加法不变），见 [行列式](determinants.md)。
    Gauss 消元的计算量约为 $O(n^3)$ 次算术运算，是数值线性代数的基本算法。

## 矩阵的秩

**定义 9（秩）**：$A$ 的**列秩**是列向量在 $\mathbb{F}^m$ 中张成空间的维数，**行秩**
是行向量在 $\mathbb{F}^n$ 中张成空间的维数。

**定理 2（行秩 = 列秩）**：对任意矩阵，行秩等于列秩，统称为 $A$ 的**秩**
$\operatorname{rank} A$。且 $\operatorname{rank} A = \dim \operatorname{im} f_A$，
其中 $f_A : \mathbf{v} \mapsto A\mathbf{v}$。

**证明思路**：初等行变换不改变行空间（每一新行都是原行的线性组合，反之亦然），故
行秩不变；化为行最简形后，非零行数 = 主元列数 = 行秩；主元列线性无关且张成列空间，
故列秩也等于主元列数。二者相等。$\square$

!!! note "秩与维数定理"

    由 $\operatorname{rank} A = \dim \operatorname{im} f_A$ 与 [线性映射](linear_maps.md)
    的维数定理可得 $\dim \ker f_A = n - \operatorname{rank} A$
    ——"零空间维数 + 秩 = 列数"，这是矩阵版本的核心计数恒等式。

**命题 6（秩的不等式）**：$\operatorname{rank}(AB) \le \min\{\operatorname{rank} A,
\operatorname{rank} B\}$；$\operatorname{rank}(A + B) \le \operatorname{rank} A +
\operatorname{rank} B$；$\operatorname{rank} A = \operatorname{rank}
A^{\mathsf{T}}$；对可逆 $P, Q$ 有 $\operatorname{rank}(PAQ) =
\operatorname{rank} A$（初等变换不改变秩）。

**例 4（求秩）**：$A = \begin{pmatrix} 1 & 2 & 3 & 1 \\ 2 & 4 & 6 & 2 \\ 1 & 0
& 1 & 0 \end{pmatrix}$。第二行是第一行的 2 倍，消元后得阶梯形
$\begin{pmatrix} 1 & 2 & 3 & 1 \\ 0 & -2 & -2 & -1 \\ 0 & 0 & 0 & 0
\end{pmatrix}$，非零行数为 2，故 $\operatorname{rank} A = 2$。

## 矩阵与线性方程组

**定理 3（解的存在性）**：方程 $A\mathbf{x} = \mathbf{b}$（$A$ 为 $m \times n$）
有解，当且仅当 $\mathbf{b}$ 属于 $A$ 的列空间，当且仅当 $\operatorname{rank} A =
\operatorname{rank}[A \mid \mathbf{b}]$（增广矩阵）。

**定理 4（解的唯一性）**：若 $A\mathbf{x} = \mathbf{b}$ 有解，则解唯一当且仅当
$\ker A = \{\mathbf{0}\}$，即 $\operatorname{rank} A = n$（未知量个数）。

**解的结构**：非齐次方程的通解 = 一个**特解** + 齐次方程 $A\mathbf{x} =
\mathbf{0}$ 的**通解**（即 $\ker A$）。齐次解集是 $\mathbb{F}^n$ 的子空间，维数
为 $n - \operatorname{rank} A$。

!!! note "方阵的情形"

    当 $m = n$ 时，定理 3 与 4 合并为：$A$ 可逆当且仅当对每个 $\mathbf{b}$，
    $A\mathbf{x} = \mathbf{b}$ 有唯一解，此时解为 $\mathbf{x} =
    A^{-1}\mathbf{b}$（与定理 1 一致）。

**例 5**：解方程组 $\begin{cases} x + y = 3 \\ 2x + 4y = 8 \end{cases}$。对增广
矩阵 $\begin{pmatrix} 1 & 1 & 3 \\ 2 & 4 & 8 \end{pmatrix}$ 施以行变换（第二行
减去第一行的 2 倍）得 $\begin{pmatrix} 1 & 1 & 3 \\ 0 & 2 & 2 \end{pmatrix}$，
回代得 $y = 1$，$x = 2$。唯一解源于 $\operatorname{rank} A = 2$（满秩）。

## 延伸阅读

- [线性映射](linear_maps.md) — 矩阵所表示对象的抽象理论：核、像、维数定理。
- [行列式](determinants.md) — 方阵可逆的行列式判据，Cramer 法则。
- [特征值与特征向量](eigenvalues.md) — 方阵的对角化与矩阵幂的计算。
- [符号表](../../notation/index.md) — 转置、共轭转置与矩阵记号约定。
