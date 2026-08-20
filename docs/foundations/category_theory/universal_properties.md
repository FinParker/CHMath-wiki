---
title: 泛性质与极限
tags:
  - 范畴论
---

# 泛性质与极限

数学对象的定义有两种风格：**内部构造**（"积是所有 $(a, b)$ 组成的集合"）与**泛性质**（"积是使得投影存在且唯一的那个对象"）。泛性质的好处是：它不依赖具体构造、抓住对象在范畴中的本质角色，并且**唯一决定对象（到唯一同构）**。始对象、终对象、积、余积、极限与余极限是泛性质的核心案例。

## 始对象与终对象

**定义 1（始对象与终对象）** 范畴 $\mathcal{C}$ 中：

- **始对象**（initial object）：对象 $0$ 使得对每个对象 $X$，$\operatorname{Hom}(0, X)$ 恰有一个元素；
- **终对象**（terminal object）：对象 $1$ 使得对每个对象 $X$，$\operatorname{Hom}(X, 1)$ 恰有一个元素。

**定理 1（唯一性到同构）** 若始对象存在，则任意两个始对象之间有唯一的同构；终对象同理。

**证明** 设 $0, 0'$ 都是始对象。由始性，存在唯一态射 $f: 0 \to 0'$ 与 $g: 0' \to 0$。复合 $g \circ f: 0 \to 0$ 与 $\operatorname{id}_0: 0 \to 0$ 都是 $0$ 的自态射，由唯一性 $g \circ f = \operatorname{id}_0$；同理 $f \circ g = \operatorname{id}_{0'}$。故 $f$ 是同构。$\blacksquare$

**例子**：

- $\mathbf{Set}$：$\varnothing$ 是始对象（唯一的空函数），$\{*\}$ 是终对象；
- $\mathbf{Grp}$、$\mathbf{Ab}$、$\mathbf{Ring}$：平凡群/平凡环既是始对象又是终对象（称为**零对象**）；
- $\mathbf{Vect}_K$：零空间也是零对象；
- 偏序集范畴（[范畴](categories.md)）：最小元是始对象，最大元是终对象；
- 带基点的集合范畴 $\mathbf{Set}_*$：单点集是零对象；
- 有至少两个对象的离散范畴既没有始对象也没有终对象——始/终对象不必存在。

## 积与余积

**定义 2（积）** 对象 $A, B$ 的**积**是三元组 $(A \times B, \pi_1, \pi_2)$，其中 $\pi_1: A \times B \to A$、$\pi_2: A \times B \to B$ 是投影，满足泛性质：对任意 $f: X \to A$、$g: X \to B$，存在**唯一**态射 $\langle f, g \rangle: X \to A \times B$ 使得
$$
\pi_1 \circ \langle f, g \rangle = f, \qquad \pi_2 \circ \langle f, g \rangle = g
$$

```
        X
       / \
      /   \
   f /     \ g
    ▼       ▼
    A       B
    ▲       ▲
     \     /
  π₁  \   /  π₂
       A × B
```

**定义 3（余积）** 对偶地，$A, B$ 的**余积**是三元组 $(A \sqcup B, i_1, i_2)$，$i_1: A \to A \sqcup B$、$i_2: B \to A \sqcup B$ 是注入，满足泛性质：对任意 $f: A \to X$、$g: B \to X$，存在唯一态射 $[f, g]: A \sqcup B \to X$ 使 $[f, g] \circ i_1 = f$、$[f, g] \circ i_2 = g$。

**例子**：

- $\mathbf{Set}$：积 = 笛卡尔积 $A \times B$；余积 = 不相交并 $A \sqcup B$；
- $\mathbf{Grp}$：积 = 直积（$G \times H$ 与投影满足泛性质，唯一态射是 $x \mapsto (f(x), g(x))$）；余积 = **自由积** $A * B$（与直积不同！）；
- $\mathbf{Ab}$：积 = 余积 = 直和（有限时 $A \times B \cong A \oplus B$）；
- $\mathbf{Top}$：积空间与余积空间；
- 偏序集范畴：积 = 下确界（meet），余积 = 上确界（join）。

**对偶原理**：余积就是反范畴中的积（[范畴](categories.md)）。一切关于积的命题经对偶自动给出关于余积的命题。积与余积可以推广到任意指标族 $\prod_{i \in I} A_i$ 与 $\coprod_{i \in I} A_i$。

**记号说明**：唯一态射 $\langle f, g \rangle$ 读作"$f$ 与 $g$ 的配对"；$[f, g]$ 读作"$f$ 与 $g$ 的余配对"。投影 $\pi_1, \pi_2$ 与注入 $i_1, i_2$ 分别是积与余积的"读出"与"写入"接口。

## 等化子与余等化子

**定义 4（等化子）** 平行态射 $f, g: A \to B$ 的**等化子**是态射 $e: E \to A$，满足 $f \circ e = g \circ e$，且对任意 $h: X \to A$，若 $f \circ h = g \circ h$，则存在唯一 $\bar{h}: X \to E$ 使 $e \circ \bar{h} = h$。

**例** 在 $\mathbf{Set}$ 中，$f, g$ 的等化子是 $E = \{a \in A \mid f(a) = g(a)\}$ 与包含映射。

**定义 5（余等化子）** 对偶：余等化子是使 $q \circ f = q \circ g$ 且泛的态射 $q: B \to Q$。在 $\mathbf{Set}$ 中，余等化子是商 $B / {\sim}$，其中 $\sim$ 是包含 $f(a) \sim g(a)$（$\forall a \in A$）的最小等价关系。

直觉：等化子"挑出两个态射相等的位置"，余等化子"把相等的位置粘合起来"。

## 极限与余极限

**定义 6（图与锥）** 设 $J$ 是小范畴（**指标范畴**）。函子 $D: J \to \mathcal{C}$ 称为 $\mathcal{C}$ 中的**图**（diagram）。$D$ 的**锥**是 $(N, \{p_j: N \to D(j)\}_{j \in J})$，使得对每个态射 $u: j \to k$ 有 $p_k = D(u) \circ p_j$（与图兼容）。

**定义 7（极限）** 图 $D$ 的**极限**是 $D$ 的**终锥**：任意锥 $(N, p)$ 到它有唯一的锥态射。记 $\varprojlim D$ 或 $\lim_j D(j)$。

**定义 8（余极限）** 对偶：$D$ 的**余极限**是 $D$ 的**始余锥**，记 $\varinjlim D$。

**统一视角**（极限论是泛性质的总纲）：

| 图的形状 | 极限 | 余极限 |
|---|---|---|
| 空图 | 终对象 | 始对象 |
| 离散图（只有恒等态射） | 积 | 余积 |
| 平行对 $A \rightrightarrows B$ | 等化子 | 余等化子 |
| $B \to D \leftarrow C$ | 拉回（纤维积） | 推出 |

- **拉回**：$B \to D \leftarrow C$ 的极限，也称**纤维积**（fibered product）：沿着两个态射"取公共原像"。$\mathbf{Set}$ 中 $B \times_D C = \{(b, c) \mid f(b) = g(c)\}$；
- **推出**：对偶。$\mathbf{Grp}$ 中的融合积 $H *_{f(G)} H$（见 [态射与同构](morphisms.md)）就是推出。

**例（偏序集中的极限）** 偏序集范畴（[范畴](categories.md) 例 4）中，图 $D$ 的锥恰好是 $D$ 的一个**下界**，极限就是**最大下界**（下确界，inf）；余极限就是**最小上界**（上确界，sup）。这解释了"极限 = 逼近对象的最优下界"这一直觉：在序结构中，极限就是下确界。

极限不必存在；所有小极限都存在（小完备）的范畴称为完备范畴（如 $\mathbf{Set}$、$\mathbf{Grp}$）。

## 泛性质唯一决定对象

**定理 2（极限的唯一性）** 若图 $D$ 存在极限，则任意两个极限之间唯一同构；余极限同理。

**证明** 极限是终锥：任意两个极限锥之间存在唯一的锥态射（双向都有），其复合是恒等（由终性），故是同构。这与定理 1 的论证完全相同——始/终对象不过是"空图"的（余）极限。$\blacksquare$

!!! note "要点"
    泛性质**不保证存在**，只保证**本质唯一**：只要对象满足同一泛性质，它们之间就有唯一同构。存在性必须由显式构造（如 $\mathbf{Set}$ 中的笛卡尔积）或公理另行保证。

**例（$\mathbf{Set}$ 中极限的显式构造）** 图 $D: J \to \mathbf{Set}$ 的极限可以显式构造为"兼容族"的集合：
$$
\varprojlim D = \left\{ (x_j)_{j \in J} \in \prod_j D(j) \ \middle|\ D(u)(x_j) = x_k \ \text{对一切 } u: j \to k \right\}
$$
投影 $p_j$ 取第 $j$ 个坐标。这统一了笛卡尔积（$J$ 离散）与等化子（$J$ 为平行对）的构造。

## 为什么叫"泛"性质

"泛"（universal）指条件对**一切**对象与态射都成立：积的泛性质对一切 $f: X \to A$、$g: X \to B$ 要求存在**唯一**的 $\langle f, g \rangle$。正是"对一切 + 唯一性"这两个词保证了：

1. 满足泛性质的对象在范畴中是"最优"的（其他对象都唯一穿过它）；
2. 泛性质完全刻画对象，不需要任何内部构造信息。

## 泛性质举例

**例 1（自由群）** 对集合 $S$，自由群 $F(S)$ 满足：对任意群 $G$，
$$
\operatorname{Hom}_{\mathbf{Grp}}(F(S), G) \cong \operatorname{Hom}_{\mathbf{Set}}(S, U(G))
$$
（自然同构，$U$ 是遗忘函子）。即"$S$ 上的任意赋值唯一扩张成群同态"。这正是 [函子](functors.md) 中自由函子的泛性质；它也可表述为：自由函子 $F$ 与遗忘函子 $U$ 构成伴随 $F \dashv U$。

**例 2（张量积）** 双线性映射与线性映射的对应：
$$
\operatorname{Bilin}(V \times W, U) \cong \operatorname{Hom}_K(V \otimes W, U)
$$
张量积 $V \otimes W$ 是"把双线性映射线性化"的泛对象。

**例 3（商）** 正规子群 $N \trianglelefteq G$ 的商 $G/N$ 是一种余等化子：它是使 $q \circ p = q \circ e$（$p: N \to G$ 为包含、$e$ 为平凡同态）的泛态射。商的泛性质是群论"第一同构定理"的范畴论根源；类似地，环的理想商、模的子模商都是某种余等化子。

**表示函子视角**：每个泛性质都可以改写为"某个 Hom 函子被表示"——例如积的泛性质等价于自然同构
$$
\operatorname{Hom}(X, A \times B) \cong \operatorname{Hom}(X, A) \times \operatorname{Hom}(X, B) \quad (\text{对 } X \text{ 自然})
$$
这一视角在 [Yoneda 引理](yoneda.md) 中展开。

## 延伸阅读

- [范畴论导览](index.md)：本目录的内容地图。
- [Yoneda 引理](yoneda.md)：泛性质与表示函子。
- [范畴](categories.md)：反范畴与对偶原理。
- [函子](functors.md)：自由函子与遗忘函子。
- [态射与同构](morphisms.md)：融合积与推出。
- [数学基础](../index.md)与[符号表](../../notation/index.md)。
