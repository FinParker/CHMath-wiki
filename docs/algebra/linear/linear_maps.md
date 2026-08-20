---
title: 线性映射
tags:
  - 线性代数
---

# 线性映射

线性映射是保持向量空间结构的映射：它把加法映成加法、把数乘映成数乘。如果说向量
空间是线性代数的"房屋"，线性映射就是房屋之间唯一的"结构通道"。矩阵不过是线性映射
在选定基下的坐标账本；而维数定理（rank-nullity 定理）则给出了映射"压缩信息"的
基本账目。

## 定义与例子

**定义 1（线性映射）**：设 $V, W$ 是域 $\mathbb{F}$ 上的向量空间。映射 $f : V
\to W$ 称为**线性映射**，若对任意 $\mathbf{u}, \mathbf{v} \in V$ 与 $a \in
\mathbb{F}$ 有

1. $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$（保持加法）；
2. $f(a\mathbf{u}) = a f(\mathbf{u})$（保持数乘）。

等价地，$f$ 保持一切线性组合：$f(a\mathbf{u} + b\mathbf{v}) = a f(\mathbf{u})
+ b f(\mathbf{v})$ 对任意 $a, b \in \mathbb{F}$ 成立。

**例 1（旋转）**：$\mathbb{R}^2$ 上绕原点逆时针旋转角 $\theta$ 的映射
$f(x, y) = (x\cos\theta - y\sin\theta,\ x\sin\theta + y\cos\theta)$ 是线性映射
——旋转不改变向量加法的平行四边形法则与伸缩。

**例 2（投影）**：$\mathbb{R}^3$ 到坐标平面 $xOy$ 的正交投影 $(x, y, z) \mapsto
(x, y, 0)$ 是线性映射；一般的"斜投影"亦然。

**例 3（微分算子）**：$D : \mathbb{F}[x] \to \mathbb{F}[x]$，$D(p) = p'$（求导）
是线性映射，因为 $(p + q)' = p' + q'$、$(ap)' = ap'$。注意 $D$ 把次数 $n$ 的
多项式映为次数 $n - 1$ 的多项式（常数项映射为零）。

!!! warning "与中学「线性函数」的区别"

    中学的 $y = kx + b$（$b \neq 0$）**不是**线性映射：它不经过原点，也不保持加法。
    线性映射必须满足 $f(\mathbf{0}) = \mathbf{0}$。

**例 4（积分算子）**：$J : C[0, 1] \to \mathbb{R}$，$f \mapsto \int_0^1 f(x)\,
dx$ 是线性映射（定积分是线性的）。

**例 5（矩阵给出的映射）**：每个 $m \times n$ 矩阵 $A$ 定义线性映射 $f_A :
\mathbb{F}^n \to \mathbb{F}^m$，$\mathbf{v} \mapsto A\mathbf{v}$（列向量）。这是
最重要的例子，见 [矩阵](matrices.md)。例如 $f(x, y) = (x + y,\ x - y)$ 对应的
矩阵是 $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$。

**定义 2（线性变换）**：从 $V$ 到自身的线性映射 $f : V \to V$ 称为**线性变换**
（自同态）。

**命题 1（基本性质）**：线性映射满足 $f(\mathbf{0}) = \mathbf{0}$、
$f(-\mathbf{v}) = -f(\mathbf{v})$、$f(\sum_i a_i \mathbf{v}_i) = \sum_i a_i
f(\mathbf{v}_i)$。线性映射的复合仍是线性映射：$g \circ f$ 线性。

**命题 2（映射空间）**：全体线性映射 $\operatorname{Hom}(V, W)$ 在逐点加法与数乘
下是向量空间；$V \to V$ 的线性变换全体 $\operatorname{End}(V)$ 在加法与复合下
构成环（复合一般不可交换）。

## 核与像

**定义 3（核与像）**：设 $f : V \to W$ 线性。定义

$$
\ker f = \{\mathbf{v} \in V : f(\mathbf{v}) = \mathbf{0}\} \subseteq V,
\qquad
\operatorname{im} f = \{f(\mathbf{v}) : \mathbf{v} \in V\} \subseteq W .
$$

**定理 1（核与像是子空间）**：$\ker f$ 是 $V$ 的子空间，$\operatorname{im} f$
是 $W$ 的子空间。

**证明**：若 $\mathbf{u}, \mathbf{v} \in \ker f$，则 $f(\mathbf{u} +
\mathbf{v}) = \mathbf{0} + \mathbf{0} = \mathbf{0}$，$f(a\mathbf{u}) =
a\mathbf{0} = \mathbf{0}$；像的封闭性同理。$\square$

**定理 2（单射的刻画）**：$f$ 是单射当且仅当 $\ker f = \{\mathbf{0}\}$。

**证明**：若 $\ker f = \{\mathbf{0}\}$ 且 $f(\mathbf{u}) = f(\mathbf{v})$，则
$f(\mathbf{u} - \mathbf{v}) = \mathbf{0}$，故 $\mathbf{u} - \mathbf{v} \in
\ker f$，$\mathbf{u} = \mathbf{v}$。反之，单射且 $f(\mathbf{0}) =
\mathbf{0}$，核中只能有 $\mathbf{0}$。$\square$

**推论**：$f$ 是满射当且仅当 $\operatorname{im} f = W$。

**例 6**：微分算子 $D : \mathbb{P}_n \to \mathbb{P}_{n-1}$ 是满射（任意 $n - 1$
次多项式都是某 $n$ 次多项式的导数），其核是常数多项式构成的子空间，$\dim \ker D
= 1$，与维数定理一致。

**例 7（投影的核与像）**：$f(x, y) = (x, 0)$（投影到 $x$ 轴）满足 $f^2 = f$
（幂等）。$\ker f$ 是 $y$ 轴（$\dim = 1$），$\operatorname{im} f$ 是 $x$ 轴
（$\dim = 1$），$\mathbb{R}^2 = \ker f \oplus \operatorname{im} f$，维数定理给出
$1 + 1 = 2$，与 $\dim \mathbb{R}^2$ 一致。

## 维数定理（rank-nullity 定理）

**定理 3（维数定理）**：设 $V$ 有限维，$f : V \to W$ 线性。则

$$
\dim V = \dim \ker f + \dim \operatorname{im} f .
$$

**证明**：取 $\ker f$ 的基 $\mathbf{v}_1, \dots, \mathbf{v}_k$，扩展为 $V$ 的基
$\mathbf{v}_1, \dots, \mathbf{v}_k, \mathbf{v}_{k+1}, \dots, \mathbf{v}_n$。断言
$f(\mathbf{v}_{k+1}), \dots, f(\mathbf{v}_n)$ 是 $\operatorname{im} f$ 的基：

1. **张成**：任意 $\mathbf{v} = \sum_i a_i \mathbf{v}_i$ 的像为 $f(\mathbf{v})
   = \sum_{i > k} a_i f(\mathbf{v}_i)$（前 $k$ 项落在核中，贡献为零）；
2. **无关**：若 $\sum_{i > k} c_i f(\mathbf{v}_i) = \mathbf{0}$，则 $\sum_{i
   > k} c_i \mathbf{v}_i \in \ker f$，可由 $\mathbf{v}_1, \dots, \mathbf{v}_k$
   线性表示；而 $\mathbf{v}_1, \dots, \mathbf{v}_n$ 线性无关，故 $c_{k+1} =
   \dots = c_n = 0$。

于是 $\dim \operatorname{im} f = n - k$。$\square$

!!! note "定理的名字"

    称 $f$ 的**秩**为 $\operatorname{rank} f = \dim \operatorname{im} f$，**零度**
    为 $\operatorname{null} f = \dim \ker f$，则维数定理写作 $\dim V =
    \operatorname{null} f + \operatorname{rank} f$。它是线性代数中最常用的计数恒等式。

**推论 1**：若 $\dim V = \dim W < \infty$，则 $f$ 单射 $\iff$ $f$ 满射 $\iff$
$f$ 是同构。

**证明**：由维数定理，$\dim \operatorname{im} f = \dim V - \dim \ker f$；单射等价
于 $\dim \ker f = 0$，即 $\dim \operatorname{im} f = \dim W$，即满射。$\square$

**推论 2**：若 $V$ 有限维，则 $\dim \operatorname{im} f \le \min\{\dim V, \dim
W\}$，且 $\dim \operatorname{Hom}(V, W) = \dim V \cdot \dim W$（由定理 4 的
"基上取值"一一对应直接计数）。

!!! warning "无限维的例外"

    推论 1 在无限维不成立。反例：序列空间 $\mathbb{F}^{\mathbb{N}}$ 上的算子
    $S(x_0, x_1, x_2, \dots) = (x_1, x_2, \dots)$ 是满射（任给 $(y_0, y_1,
    \dots)$ 取原像 $(0, y_0, y_1, \dots)$），但 $\ker S = \{(x_0, 0, 0, \dots)\}
    \neq \{\mathbf{0}\}$，不是单射。

## 由基上的取值决定

**定理 4（基上取值唯一决定线性映射）**：设 $\mathbf{v}_1, \dots, \mathbf{v}_n$
是 $V$ 的基，$\mathbf{w}_1, \dots, \mathbf{w}_n \in W$ 任意。则存在唯一的线性
映射 $f : V \to W$ 满足 $f(\mathbf{v}_i) = \mathbf{w}_i$（$i = 1, \dots, n$）。

**证明**：存在性：对 $\mathbf{v} = \sum_i a_i \mathbf{v}_i$ 定义 $f(\mathbf{v})
= \sum_i a_i \mathbf{w}_i$，直接验证线性。唯一性：若 $g$ 也满足条件，则 $f - g$
在所有基元上取值为零，由线性在 $V$ 上恒为零，故 $f = g$。$\square$

这一命题是"线性映射完全由它在基上的表现决定"的抽象版本，也是推论 3 的依据。

**推论 3**：线性映射 $f : V \to W$ 完全由它在任一基上的取值决定。选定基后，
"$f$"与"$n$ 个列向量 $\mathbf{w}_1, \dots, \mathbf{w}_n$"一一对应——这正是矩阵
概念的由来，见 [矩阵](matrices.md)。

**例 8（线性泛函与对偶空间）**：当 $W = \mathbb{F}$ 时，线性映射 $f : V \to
\mathbb{F}$ 称为**线性泛函**，全体线性泛函构成 $V$ 的**对偶空间** $V^{*} =
\operatorname{Hom}(V, \mathbb{F})$。有限维时 $\dim V^{*} = \dim V$，且 $V$ 的基
$\mathbf{v}_1, \dots, \mathbf{v}_n$ 对应 $V^{*}$ 的**对偶基** $\varphi_1, \dots,
\varphi_n$：$\varphi_i(\mathbf{v}_j) = \delta_{ij}$。

换言之，$\varphi_i$ 的作用是"提取第 $i$ 个坐标"：$\varphi_i(\mathbf{v}) = a_i$。
对偶空间在微分几何、泛函分析与物理学（如张量）中扮演核心角色。

## 同构

**定义 4（同构）**：双射的线性映射 $f : V \to W$ 称为**同构**；若存在同构，则称
$V$ 与 $W$ **同构**，记作 $V \cong W$。

**定理 5（有限维空间的分类）**：设 $\dim V = n < \infty$，则 $V \cong
\mathbb{F}^n$。更一般地，两个有限维空间同构当且仅当它们维数相等。

**证明**：取有序基 $B = (\mathbf{v}_1, \dots, \mathbf{v}_n)$，坐标映射
$\mathbf{v} \mapsto [\mathbf{v}]_B$ 是双射且保持加法和数乘，故为同构。$\square$

**注（同构的例子）**：$\mathbb{C}$ 作为 $\mathbb{R}$ 上的向量空间（基 $1, i$，
$\dim = 2$）同构于 $\mathbb{R}^2$；$\mathbb{P}_n$ 同构于 $\mathbb{R}^{n+1}$
（多项式与系数向量一一对应）。这些同构把"抽象空间"翻译成"坐标空间"，从而可借用
矩阵理论。

!!! note "同构的意义"

    同构的空间"结构完全相同，只是记号不同"。把 $V$ 与 $\mathbb{F}^n$ 等同（固定基）
    后，线性映射即化为矩阵，线性代数于是"一切皆矩阵"。因此**维数**是有限维向量空间
    在同构意义下唯一的完全不变量。

**定理 6（同态基本定理）**：设 $f : V \to W$ 线性。则 $f$ 诱导同构
$\overline{f} : V / \ker f \cong \operatorname{im} f$，其中 $V / \ker f$ 是商空间
（把 $\ker f$ 的陪集 $\mathbf{v} + \ker f$ 视作向量，加法与数乘逐陪集定义）。

**证明要点**：先验证 $\overline{f}$ 良定义：若 $\mathbf{u} - \mathbf{v} \in
\ker f$ 则 $f(\mathbf{u}) = f(\mathbf{v})$；再验证单射：$\overline{f}$ 的核是零
陪集 $\ker f$ 本身；满射显然。$\square$

## 线性变换的复合

- **复合**：$(g \circ f)(\mathbf{v}) = g(f(\mathbf{v}))$ 仍是线性映射；复合对应
  矩阵乘法（见 [矩阵](matrices.md) 中乘法的定义动机）。
- **可逆线性变换**：$f : V \to V$ 可逆当且仅当 $f$ 是双射（此时逆映射自动线性）。
  有限维时，可逆等价于 $\ker f = \{\mathbf{0}\}$（推论 1）。
- **幂等算子**：满足 $f^2 = f$ 的线性变换称为幂等的，如投影算子；此时 $V = \ker f
  \oplus \operatorname{im} f$（见 [向量空间](vector_spaces.md) 的直和）。
- **一般线性群**：$V$ 上所有可逆线性变换在复合下构成群，记作 $\mathrm{GL}(V)$，
  称为一般线性群。它是"变换的对称性"这一主题的起点。

**例 9（旋转的复合）**：旋转 $\theta$ 与旋转 $\varphi$ 的复合是旋转 $\theta +
\varphi$。由矩阵乘法

$$
\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi
\end{pmatrix}
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta
\end{pmatrix}
= \begin{pmatrix} \cos(\theta+\varphi) & -\sin(\theta+\varphi) \\
\sin(\theta+\varphi) & \cos(\theta+\varphi) \end{pmatrix},
$$

逐项比较即得三角函数的和角公式。这展示了"复合对应矩阵乘法"带来的实际收益。

## 延伸阅读

- [向量空间](vector_spaces.md) — 线性映射的出发空间与到达空间，基与维数。
- [矩阵](matrices.md) — 线性映射的坐标表示；复合对应矩阵乘法。
- [行列式](determinants.md) — 用行列式判断线性映射是否可逆（$\det \neq 0$）。
- [代数](../index.md) — 从模与范畴的角度看同态、同构与同态基本定理。
