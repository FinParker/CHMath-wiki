---
title: 特征值与特征向量
tags:
  - 线性代数
---

# 特征值与特征向量

特征向量是线性变换作用下**方向不变**的向量——变换在它上面只是把向量拉长或缩短
（特征值）。对角化的全部意义在于：找到一组特征向量作新基，把复杂的线性变换化为
对角矩阵，使"作用在向量上"变成"作用在标量上"。这是解差分方程、分析 Markov 链、
主成分分析等一切应用的公共起点。

## 定义

**定义 1（特征值与特征向量）**：设 $A \in \mathrm{M}_n(\mathbb{F})$。若非零向量
$\mathbf{v} \in \mathbb{F}^n$ 与标量 $\lambda \in \mathbb{F}$ 满足

$$
A\mathbf{v} = \lambda \mathbf{v},
$$

则称 $\lambda$ 为 $A$ 的**特征值**，$\mathbf{v}$ 为属于 $\lambda$ 的**特征向量**。

要点：特征向量**必须非零**；特征值可以为 $0$（此时 $A\mathbf{v} = \mathbf{0}$，
特征向量属于核）。属于同一特征值的特征向量连同零向量构成子空间。

**定义 2（特征空间）**：$\lambda$ 的特征空间为

$$
E_\lambda = \ker(A - \lambda I_n) = \{\mathbf{v} : A\mathbf{v} = \lambda \mathbf{v}\} .
$$

$\lambda$ 是特征值 $\iff E_\lambda \neq \{\mathbf{0}\}$ $\iff$ $A - \lambda I_n$
不可逆 $\iff$ $\det(A - \lambda I_n) = 0$（见 [行列式](determinants.md)）。

**例 1**：对角阵 $\operatorname{diag}(\lambda_1, \dots, \lambda_n)$ 的特征值是
$\lambda_1, \dots, \lambda_n$，对应特征向量为标准基向量 $\mathbf{e}_1, \dots,
\mathbf{e}_n$。

**例 2（投影）**：投影到 $x$ 轴的矩阵 $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$
的特征值为 $1$（$x$ 轴方向不动）与 $0$（$y$ 轴方向被压掉）。

**例 3（旋转）**：$\mathbb{R}^2$ 上旋转 $90^\circ$ 的矩阵 $\begin{pmatrix} 0 & -1
\\ 1 & 0 \end{pmatrix}$ 在 $\mathbb{R}$ 上**没有**特征值（任何非零向量的方向都变了）；
在 $\mathbb{C}$ 上特征值为 $\pm i$。一般地，旋转 $\theta$ 的特征值为 $e^{\pm i\theta}$。

## 特征多项式与求法

**定义 3（特征多项式）**：$p_A(\lambda) = \det(A - \lambda I_n)$，它是 $\lambda$ 的
$n$ 次多项式。

**求特征值与特征向量的步骤**：

1. 计算 $\det(A - \lambda I_n)$，写出特征多项式；
2. 解特征方程 $p_A(\lambda) = 0$，得特征值；
3. 对每个特征值 $\lambda$，解齐次方程组 $(A - \lambda I_n)\mathbf{v} = \mathbf{0}$，
   求出特征空间 $E_\lambda$ 的一组基。

!!! warning "特征向量必须非零"

    解 $(A - \lambda I_n)\mathbf{v} = \mathbf{0}$ 时，零向量恒为解，但不算特征向量。
    特征向量是 $E_\lambda$ 中的非零向量。

**例 4**：求 $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ 的特征值与特征向量。

解：$p_A(\lambda) = \det\begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix}
= (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3)$，特征值
为 $1, 3$。

- $\lambda = 1$：$A - I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$，解得
  $E_1 = \operatorname{span}\{(1, -1)\}$；
- $\lambda = 3$：$A - 3I = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$，解得
  $E_3 = \operatorname{span}\{(1, 1)\}$。

!!! note "特征值的存在性"

    当 $\mathbb{F} = \mathbb{C}$ 时，由代数基本定理，$n$ 次特征多项式总有 $n$ 个复根
    （计重数），故复数域上每个矩阵都有特征值。当 $\mathbb{F} = \mathbb{R}$ 时可能一个
    实特征值都没有（如例 3 的旋转）。求根通常依赖数值方法（如 QR 算法），手工计算只
    适合低阶或系数特殊的情形。

## 基本性质

**定理 1（互异特征值的特征向量线性无关）**：属于互异特征值 $\lambda_1, \dots,
\lambda_k$ 的特征向量 $\mathbf{v}_1, \dots, \mathbf{v}_k$ 线性无关。

**证明**：取满足 $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k = \mathbf{0}$ 的**极小**
线性关系（$k$ 最小）。左乘 $A$ 得 $\sum_i c_i \lambda_i \mathbf{v}_i =
\mathbf{0}$。用它消去原关系的末项：$\sum_{i<k} c_i (\lambda_i - \lambda_k)
\mathbf{v}_i = \mathbf{0}$，得到更短的非平凡关系，矛盾。故所有 $c_i = 0$。$\square$

**推论**：$n$ 阶矩阵若有 $n$ 个互异特征值，则可对角化（见下）。

**常用性质**：

- $A$ 与 $A^{\mathsf{T}}$ 有相同的特征多项式与特征值；
- 三角矩阵的特征值恰为对角元；
- $A$ 可逆 $\iff$ $0$ 不是 $A$ 的特征值；
- 特征值（计重数）之积 $= \det A$，之和 $= \operatorname{tr} A$；可由特征多项式
  $p_A(\lambda) = \lambda^n - (\operatorname{tr} A)\lambda^{n-1} + \cdots + (-1)^n
  \det A$（用 $\det(\lambda I - A)$ 时）读出；
- 若 $\mathbf{v} \in E_\lambda$，则 $A\mathbf{v} = \lambda \mathbf{v} \in
  E_\lambda$——特征空间是 $A$ 的**不变子空间**。

**例 5（幂零矩阵）**：$N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ 满足
$N^2 = O$。其特征多项式为 $\lambda^2$，唯一特征值 $0$，代数重数 $2$；但 $E_0 =
\ker N = \operatorname{span}\{(1, 0)\}$ 只有一维，几何重数 $1 \ne 2$，故 $N$ 不可
对角化。这是"几何重数严格小于代数重数"的典型。

## 代数重数与几何重数

**定义 4（重数）**：特征值 $\lambda$ 在特征多项式中的重根数 $m_\lambda$ 称为**代数
重数**；$\dim E_\lambda$ 称为**几何重数**。

**定理 2（几何重数 ≤ 代数重数）**：对每个特征值 $\lambda$，$1 \le \dim E_\lambda
\le m_\lambda$。

**证明思路**：取 $E_\lambda$ 的基并扩展为 $\mathbb{F}^n$ 的基，$A$ 在该基下的矩阵
形如 $\begin{pmatrix} \lambda I_g & * \\ O & B \end{pmatrix}$（$g = \dim E_\lambda$），
其特征多项式被 $(\lambda - t)^g$ 整除，故 $m_\lambda \ge g$。$\square$

!!! note "重数之和"

    在 $\mathbb{C}$ 上，代数重数之和恰为 $n$；几何重数之和 $\le n$，等号成立当且仅当
    $A$ 可对角化（见下）。

## 对角化

**定义 5（可对角化）**：$A \in \mathrm{M}_n(\mathbb{F})$ 称为**可对角化**的，若存在
可逆矩阵 $P$ 使

$$
P^{-1} A P = D
$$

为对角矩阵。此时 $D$ 的对角元恰为 $A$ 的特征值（按序），$P$ 的列恰为对应的特征向量。

**定理 3（对角化的充要条件）**：$A$ 可对角化 $\iff$ $A$ 有 $n$ 个线性无关的特征向量
$\iff$ 每个特征值的几何重数等于代数重数。

**求法步骤**：(1) 求出全部特征值；(2) 对每个特征值求出 $E_\lambda$ 的一组基；(3)
把所有特征向量按列拼成 $P$，相应特征值按列写成 $D$。

**例 6**：承接例 4，取 $P = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$（列为
$(1,-1)$ 与 $(1,1)$），则 $P^{-1}AP = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$。
由此 $A^n = P \begin{pmatrix} 1 & 0 \\ 0 & 3^n \end{pmatrix} P^{-1}$——对角化把
**矩阵幂**化为**标量幂**。

!!! warning "互异特征值是充分条件，不是必要条件"

    $n$ 个互异特征值 $\Rightarrow$ 可对角化，但反过来不必：$I_n$ 可对角化而特征值
    $1$ 是 $n$ 重根。有重根也可能可对角化；判据是几何重数 = 代数重数。如
    $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ 的代数重数 $2$、几何重数 $1$，
    不可对角化。

## 相似矩阵

**定义 6（相似）**：$B$ 与 $A$ **相似**（记 $B \sim A$）若存在可逆 $P$ 使 $B =
P^{-1}AP$。直观上，$B$ 是同一线性变换在另一组基下的矩阵。

**命题 1（相似不变量）**：相似矩阵有相同的特征多项式，从而有相同的特征值、行列式、
迹与秩。

!!! note "相似与等价"

    "相似"是同一线性变换换基的表示；与矩阵的（相抵）等价不同。特征值相同推不出相似：
    $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ 与 $I_2$ 的特征值都是 $1$，但不相似
    （前者不可对角化）。

## 实对称矩阵的谱定理

**定理 4（谱定理，实情形）**：设 $A$ 是实对称矩阵（$A^{\mathsf{T}} = A$），则

1. $A$ 的特征值全为**实数**；
2. 属于不同特征值的特征向量彼此**正交**；
3. 存在正交矩阵 $Q$（$Q^{\mathsf{T}}Q = I$，即 $Q^{-1} = Q^{\mathsf{T}}$）使
   $Q^{\mathsf{T}} A Q$ 为对角矩阵——称 $A$ 可**正交对角化**。

**证明要点**（性质 2）：对内积 $\langle \cdot, \cdot \rangle$ 与 $A\mathbf{v}_1 =
\lambda_1\mathbf{v}_1$、$A\mathbf{v}_2 = \lambda_2\mathbf{v}_2$（$\lambda_1 \neq
\lambda_2$）：

$$
\lambda_1 \langle \mathbf{v}_1, \mathbf{v}_2 \rangle
= \langle A\mathbf{v}_1, \mathbf{v}_2 \rangle
= \langle \mathbf{v}_1, A^{\mathsf{T}}\mathbf{v}_2 \rangle
= \langle \mathbf{v}_1, A\mathbf{v}_2 \rangle
= \lambda_2 \langle \mathbf{v}_1, \mathbf{v}_2 \rangle,
$$

故 $(\lambda_1 - \lambda_2)\langle \mathbf{v}_1, \mathbf{v}_2 \rangle = 0$，
$\langle \mathbf{v}_1, \mathbf{v}_2 \rangle = 0$。性质 1、3 的完整证明可用归纳或谱
分解，此处陈述。$\square$

!!! note "正交对角化 ⟹ 对角化，反之不然"

    $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ 可对角化（特征值 $1, 2$ 互异）但
    不实对称，不可正交对角化。谱定理是量子力学（自伴算子）、主成分分析（协方差矩阵
    对称，主成分即其特征向量）与振动分析的理论基石。

## 应用：Fibonacci 数列

Fibonacci 数列 $F_0 = 0$，$F_1 = 1$，$F_{n+2} = F_{n+1} + F_n$。把它写成矩阵迭代：
令 $\mathbf{w}_n = \begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix}$，则

$$
\mathbf{w}_{n+1} = A \mathbf{w}_n, \qquad A = \begin{pmatrix} 1 & 1 \\ 1 & 0
\end{pmatrix},
$$

于是 $\mathbf{w}_n = A^n \mathbf{w}_0$，其中 $\mathbf{w}_0 = \begin{pmatrix} F_1
\\ F_0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$。

$A$ 的特征多项式为 $\det(A - \lambda I) = \lambda^2 - \lambda - 1$，特征值为黄金比
$\varphi = \frac{1+\sqrt{5}}{2}$ 与 $\psi = \frac{1-\sqrt{5}}{2}$，对应特征向量
$(\varphi, 1)$、$(\psi, 1)$。把 $\mathbf{w}_0 = (1, 0)$ 在特征基下分解：
$\mathbf{w}_0 = \alpha(\varphi, 1) + \beta(\psi, 1)$，由第二分量得 $\alpha + \beta
= 0$，由第一分量得 $\alpha\varphi + \beta\psi = 1$，解得 $\alpha = \tfrac{1}{\sqrt
{5}}$、$\beta = -\tfrac{1}{\sqrt{5}}$。应用 $A^n$（化为 $\varphi^n, \psi^n$ 的标量
幂）后取第二个分量，即得 **Binet 公式**：

$$
F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}} .
$$

!!! note "同一技巧的其他应用"

    二阶线性差分方程 $x_{n+2} = p\,x_{n+1} + q\,x_n$ 由特征方程 $t^2 - pt - q = 0$
    同样可解。对 **Markov 链**，转移矩阵的（左）特征值 $1$ 对应**平稳分布**
    $\boldsymbol{\pi}$（满足 $\boldsymbol{\pi}P = \boldsymbol{\pi}$）：系统长期演化后
    概率分布不再改变，这是 PageRank 等算法的数学基础。

## 延伸阅读

- [行列式](determinants.md) — 特征多项式 $\det(A - \lambda I_n)$ 的定义基础。
- [矩阵](matrices.md) — 矩阵幂、可逆性与秩。
- [线性映射](linear_maps.md) — 特征向量是线性变换的不变方向，核与像的语言。
- [符号表](../../notation/index.md) — 转置、内积与矩阵记号。
