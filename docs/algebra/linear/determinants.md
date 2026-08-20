---
title: 行列式
tags:
  - 线性代数
---

# 行列式

行列式是方阵的一个标量不变量，其几何意义是**有向体积**：线性变换把单位方块映成
平行多面体，行列式度量的正是体积被缩放了多少倍（连同定向的符号）。它把"矩阵是否
可逆"这个代数问题化为"一个数是否为零"，同时也是特征多项式与谱理论的入口。

## 几何直觉

**2 × 2 情形**：$\det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$ 是
以两列为边的平行四边形的**有向面积**（两列逆时针排列时为正）。

**3 × 3 情形**：$\det A$ 是列向量张成的平行六面体的**有向体积**；当 $A$ 的列为
$\mathbf{u}, \mathbf{v}, \mathbf{w}$ 时，$\det A = \mathbf{u} \cdot (\mathbf{v}
\times \mathbf{w})$（混合积）。

!!! note "体积缩放因子"

    若 $T : \mathbf{v} \mapsto A\mathbf{v}$，则任意可测集 $S$ 的体积满足
    $\operatorname{vol}(T(S)) = |\det A| \cdot \operatorname{vol}(S)$；符号
    $\det A$ 携带定向信息（手性反转时为负）。体积解释是行列式最重要的动机，它同时
    说明了为什么行列式对"列"是多重线性的、交换两列要变号。

## 公理化定义

**定义 1（行列式）**：行列式是满足以下三条公理的唯一函数 $\det : \mathrm{M}_n
(\mathbb{F}) \to \mathbb{F}$：

1. **多重线性**：对每一列线性。即把第 $j$ 列换成 $c\mathbf{u} + d\mathbf{v}$
   时，$\det(\dots, c\mathbf{u} + d\mathbf{v}, \dots) = c \det(\dots,
   \mathbf{u}, \dots) + d \det(\dots, \mathbf{v}, \dots)$；
2. **交错**：交换任意两列，行列式变号；
3. **归一化**：$\det I_n = 1$。

这三条公理其实已经唯一决定了行列式；其显式表达式由下面的 Leibniz 公式给出。

**定理 1（Leibniz 公式）**：设 $A = (a_{ij})$，则

$$
\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\,
a_{1\,\sigma(1)} a_{2\,\sigma(2)} \cdots a_{n\,\sigma(n)},
$$

其中 $S_n$ 是 $n$ 元置换群，$\operatorname{sgn}(\sigma)$ 是置换的符号（偶置换为
$+1$，奇置换为 $-1$）。

**例**：$n = 2$ 时恰有两项，$S_2 = \{\mathrm{id}, (12)\}$，得 $a_{11}a_{22} -
a_{12}a_{21}$，即 $ad - bc$。$n = 3$ 时是 6 项（Sarrus 法则的记忆图形），项数随
$n$ 增长为 $n!$，故 Leibniz 公式适合理论推导，不适合直接计算。

## Laplace 展开（递归计算）

**定义 2（代数余子式）**：划去 $A$ 的第 $i$ 行第 $j$ 列所得 $n-1$ 阶矩阵的行列式
记作 $M_{ij}$（余子式），代数余子式为 $C_{ij} = (-1)^{i+j} M_{ij}$。

**定理 2（Laplace 展开）**：按第 $i$ 行展开：$\det A = \sum_{j=1}^{n} a_{ij}
C_{ij}$；按第 $j$ 列展开：$\det A = \sum_{i=1}^{n} a_{ij} C_{ij}$。展开可递归
进行，最终归结为 2 × 2 行列式的计算。

!!! warning "符号与计算技巧"

    代数余子式的符号 $(-1)^{i+j}$ 呈棋盘形（$+ - + \cdots$），务必核对。实际计算时
    应沿含零最多的行或列展开，以大幅减少项数。

**例 1（3 × 3 展开）**：按第一行展开

$$
\det \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}
= 1 \cdot \det\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}
- 2 \cdot \det\begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}
+ 0 \cdot \det\begin{pmatrix} 3 & 1 \\ 0 & 1 \end{pmatrix}
= (2 - 1) - 2 \cdot 6 = 1 - 12 = -11 .
$$

**注（沿零最多的行或列展开）**：$\det \begin{pmatrix} 1 & 0 & 2 \\ 3 & 0 & 1 \\ 0
& 2 & 4 \end{pmatrix}$ 按第二列展开只需一项：$0 + 0 + 2 \cdot (-1)^{3+2} \det
\begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix} = -2 \cdot (1 - 6) = 10$。

**例 2（三角矩阵）**：上三角矩阵的行列式等于对角元之积：$\det \begin{pmatrix} a
& * & * \\ 0 & b & * \\ 0 & 0 & c \end{pmatrix} = abc$。事实上对任意三角矩阵，
连续按第一列（或第一行）展开即可逐项剥掉对角元。

**例 3（行加法化三角阵）**：对 $A = \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & 1 \\ 0
& 1 & 2 \end{pmatrix}$，把第二行减去第一行的 3 倍、再把第三行加上新第二行的
$\tfrac{1}{5}$ 倍，化为上三角阵；行加法不改变行列式，故 $\det A$ 等于三角阵对角
元之积，同样得到 $-11$。这是数值计算行列式的常规路线（结合行交换与倍乘的符号
调整）。

## 基本性质

**定理 3（行运算）**：设 $A$ 是方阵，则

1. 交换两行（或两列），行列式**变号**；
2. 某一行（列）乘以 $c$，行列式乘以 $c$；
3. 把某一行（列）的倍数加到另一行（列），行列式**不变**；
4. 若某行（列）全为零，或两行（列）成比例，则 $\det A = 0$。

其中性质 3 的证明：把"第 $i$ 行加上第 $j$ 行的 $c$ 倍"按第 $i$ 行展开，利用多重
线性拆成两项，第二项含两行成比例，由性质 4（交错性）为零。

**定理 4（转置不变）**：$\det A^{\mathsf{T}} = \det A$。因此所有"行性质"对列
同样成立。

**证明思路**：由 Leibniz 公式，$\det A^{\mathsf{T}}$ 的求和项对应置换 $\sigma$
的项 $a_{\sigma(1)\,1} \cdots a_{\sigma(n)\,n}$；重排因子（按第一指标升序）后它
对应置换 $\sigma^{-1}$，而 $\operatorname{sgn}(\sigma^{-1}) =
\operatorname{sgn}(\sigma)$，故两个求和逐项相等。$\square$

**定理 5（三角矩阵）**：上三角或下三角矩阵的行列式等于对角元之积。推论：
$\det(cA) = c^n \det A$。

**定理 6（乘性）**：对同阶方阵 $A, B$，$\det(AB) = \det A \cdot \det B$。

**证明思路**：固定 $B$，考察函数 $A \mapsto \det(AB)$。它对 $A$ 的每一列多重线性
且交错（交换 $A$ 的两列即交换 $AB$ 的两列，变号），由公理化定义它必为 $\det A$
的常数倍：$\det(AB) = c \det A$。代入 $A = I_n$ 得 $c = \det B$。$\square$

**例 4（数值验证）**：$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$（$\det A
= -2$），$B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$（$\det B = -1$），
$AB = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}$，$\det(AB) = 6 - 4 = 2 =
(-2)(-1)$，一致。

**推论**：$\det(A^{-1}) = (\det A)^{-1}$；若 $B = P^{-1}AP$（相似，见 [特征值与
特征向量](eigenvalues.md)），则 $\det B = \det A$——行列式是**相似不变量**。

这也解释了 $\det(A^n) = (\det A)^n$：把 $A^n = A \cdots A$ 反复用乘性公式即可，
与"行列式度量体积缩放"的几何解释完全吻合。

!!! warning "乘性不是加法性"

    一般地 $\det(A + B) \neq \det A + \det B$。行列式只对"单独一行（列）"是线性的：
    每拆开一行，其余行必须保持不变，且要同时拆开所有行。

## 伴随矩阵与逆矩阵

**定义 3（伴随矩阵）**：设 $C_{ij}$ 是 $A$ 的代数余子式，则 $A$ 的**伴随矩阵**
$\operatorname{adj} A$ 定义为 $(\operatorname{adj} A)_{ji} = C_{ij}$（即代数余子
式矩阵的转置）。

**定理 7（伴随矩阵求逆）**：$A \cdot \operatorname{adj} A = \det A \cdot I_n =
\operatorname{adj} A \cdot A$。因此当 $\det A \neq 0$ 时

$$
A^{-1} = \frac{1}{\det A} \operatorname{adj} A .
$$

**证明思路**：$(A \operatorname{adj} A)_{ik} = \sum_j a_{ij} C_{kj}$ 是"第 $i$
行与第 $k$ 行的代数余子式相乘"：$i = k$ 时是 Laplace 展开得 $\det A$；$i \neq k$
时相当于把第 $k$ 行换成第 $i$ 行后展开（两行相同），由交错性为零。$\square$

!!! note "伴随矩阵的定位"

    该公式理论价值高（显式给出逆），但计算 $n^2$ 个代数余子式代价高昂；数值上求逆
    应使用 Gauss 消元（见 [矩阵](matrices.md)）。

## 可逆性与行列式

**定理 8（可逆判据）**：方阵 $A$ 可逆当且仅当 $\det A \neq 0$。

**证明思路**：用初等行变换把 $A$ 化为行阶梯形。由定理 3，行变换只把 $\det A$ 变成
非零倍数（交换变号、倍乘放大、行加法不变），故 $\det A \neq 0$ 当且仅当阶梯形对角
元全非零，即阶梯形无零行，即 $\operatorname{rank} A = n$，即 $A$ 可逆（见 [矩阵](matrices.md)
定理 1）。$\square$

**推论**：$A$ 的列（行）向量线性无关 $\iff$ $\det A \neq 0$；$A$ 的特征值之积为
$\det A$（见 [特征值与特征向量](eigenvalues.md)），故 $0$ 是特征值 $\iff$ $A$ 不
可逆。

!!! note "理论与计算的取舍"

    行列式判据在理论上极其简洁；但数值上判定可逆性应使用 Gauss 消元（$O(n^3)$），
    而按定义递归展开行列式是指数级 $O(n!)$ 的。

## Cramer 法则

**定理 9（Cramer 法则）**：设 $A$ 可逆，$A_j$ 是把 $A$ 的第 $j$ 列换成 $\mathbf{b}$
所得的矩阵。则方程组 $A\mathbf{x} = \mathbf{b}$ 的唯一解为

$$
x_j = \frac{\det A_j}{\det A}, \qquad j = 1, \dots, n .
$$

**证明思路**：记 $A$ 的第 $j$ 列为 $\mathbf{a}^{(j)}$，由 $\mathbf{b} = \sum_j
x_j \mathbf{a}^{(j)}$。把 $\det A_j$ 按第 $j$ 列展开，利用多重线性与交错性，除
$x_j \mathbf{a}^{(j)}$ 所在项外其余项均有重复列而为零，得 $\det A_j = x_j
\det A$。$\square$

!!! note "Cramer 法则的定位"

    它给出解的显式公式，理论价值大于计算价值：求解大方程组仍应使用 Gauss 消元。

## 行列式与特征多项式

**定义 4（特征多项式）**：方阵 $A$ 的**特征多项式**为

$$
p_A(\lambda) = \det(A - \lambda I_n) .
$$

（部分教材用 $\det(\lambda I_n - A)$，二者相差因子 $(-1)^n$，根完全相同。）

- $\lambda$ 是 $A$ 的特征值 $\iff p_A(\lambda) = 0$；
- 常数项 $p_A(0) = \det A$；
- 在 $\mathbb{C}$ 上把特征值（计重数）记为 $\lambda_1, \dots, \lambda_n$，则
  $\det A = \lambda_1 \cdots \lambda_n$，$\operatorname{tr} A = \lambda_1 + \cdots
  + \lambda_n$（特征值之积与之和）。

特征多项式与对角化、谱理论的完整讨论见 [特征值与特征向量](eigenvalues.md)。

## 延伸阅读

- [特征值与特征向量](eigenvalues.md) — 特征多项式、对角化与谱定理。
- [矩阵](matrices.md) — 初等行变换、秩与逆矩阵，行列式的计算上下文。
- [线性映射](linear_maps.md) — 行列式作为 $\Lambda^n V$ 上的不变量（同构判据）。
- [代数](../index.md) — 从多重线性代数与交错张量的角度看待行列式。
