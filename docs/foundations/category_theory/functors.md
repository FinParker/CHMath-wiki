---
title: 函子
tags:
  - 范畴论
---

# 函子

函子是范畴之间的"结构保持映射"：它把对象映到对象、态射映到态射，并保持复合与恒等。如果说范畴编码结构，函子则编码结构之间的"翻译"——遗忘、自由、对偶、表示等一切重要构造都是函子。

## 定义

**定义 1（协变函子）** 设 $\mathcal{C}, \mathcal{D}$ 是范畴。**协变函子** $F: \mathcal{C} \to \mathcal{D}$ 由以下数据构成：

- **对象映射**：每个对象 $A \in \mathcal{C}$ 映到一个对象 $F(A) \in \mathcal{D}$；
- **态射映射**：每个态射 $f: A \to B$ 映到一个态射 $F(f): F(A) \to F(B)$。

并且满足：

- $F(\operatorname{id}_A) = \operatorname{id}_{F(A)}$（保持恒等）；
- $F(g \circ f) = F(g) \circ F(f)$（保持复合）。

**定义 2（反变函子）** **反变函子** $F: \mathcal{C} \to \mathcal{D}$ 反转箭头：$f: A \to B$ 映到 $F(f): F(B) \to F(A)$，且 $F(g \circ f) = F(f) \circ F(g)$。等价地，反变函子就是协变函子 $F: \mathcal{C}^{\mathrm{op}} \to \mathcal{D}$（见 [范畴](categories.md) 的反范畴一节）。

- 协变：$f: A \to B \ \longmapsto\ F(f): F(A) \to F(B)$；
- 反变：$f: A \to B \ \longmapsto\ F(f): F(B) \to F(A)$。

## 基本例子

**例 1（恒等函子）** $\operatorname{id}_{\mathcal{C}}: \mathcal{C} \to \mathcal{C}$ 把对象与态射原样返回。它是函子复合的单位元。

**例 2（遗忘函子）** 忘记结构、保留底层集合：

- $U: \mathbf{Grp} \to \mathbf{Set}$：群 ↦ 其底集，群同态 ↦ 底函数；
- $U: \mathbf{Top} \to \mathbf{Set}$：拓扑空间 ↦ 底集，连续映射 ↦ 底函数；
- 类似地有 $U: \mathbf{Ab} \to \mathbf{Grp}$、$U: \mathbf{Ring} \to \mathbf{Set}$、$U: \mathbf{Vect}_K \to \mathbf{Set}$ 等。

遗忘函子都是忠实的（见下文定义 3）。

**例 3（自由函子）** 遗忘函子的"逆过程"：$F: \mathbf{Set} \to \mathbf{Grp}$ 把集合 $S$ 映到以 $S$ 为自由生成元的自由群 $F(S)$，把函数 $f: S \to T$ 映到相应的自由群同态。自由群的泛性质见 [泛性质与极限](universal_properties.md)：自由函子与遗忘函子构成伴随对。

**例 4（Hom 函子）** 固定对象 $A$：

- **协变 Hom 函子** $\operatorname{Hom}(A, -): \mathcal{C} \to \mathbf{Set}$：$B \mapsto \operatorname{Hom}(A, B)$，态射 $g: B \to C$ 映到"复合" $g \circ (-): \operatorname{Hom}(A, B) \to \operatorname{Hom}(A, C)$；
- **反变 Hom 函子** $\operatorname{Hom}(-, B): \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$：$f: A \to C$ 映到 $(-) \circ f: \operatorname{Hom}(C, B) \to \operatorname{Hom}(A, B)$。

在 $\mathbf{Set}$ 中，$\operatorname{Hom}(A, B) = B^A$（从 $A$ 到 $B$ 的一切函数）。Hom 函子是 [Yoneda 引理](yoneda.md) 的主角。

**例 5（幂集函子）** 幂集有两种函子化：

- **协变** $\mathcal{P}: \mathbf{Set} \to \mathbf{Set}$：$A \mapsto \mathcal{P}(A)$，$f: A \to B$ 映到直接像 $f(-): \mathcal{P}(A) \to \mathcal{P}(B)$；
- **反变** $\mathcal{P}^{\mathrm{op}}: \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}$：$f: A \to B$ 映到原像 $f^{-1}(-): \mathcal{P}(B) \to \mathcal{P}(A)$。

注意原像把方向反转，所以 $\mathcal{P}^{\mathrm{op}}$ 是反变函子。同一个"直觉构造"（幂集）可以同时给出协变与反变两个函子，这提醒我们函子化的方式并不唯一。

**例 6（对偶函子）** 向量空间的对偶 $(-)^*: \mathbf{Vect}_K^{\mathrm{op}} \to \mathbf{Vect}_K$：$V \mapsto V^* = \operatorname{Hom}_K(V, K)$，线性映射 $f: V \to W$ 映到对偶映射 $f^*: W^* \to V^*$，$f^*(\varphi) = \varphi \circ f$。它是反变函子；双重对偶 $V \to V^{**}$ 的自然性见 [自然变换](natural_transformations.md)。

**例 7（包含函子）** 子范畴 $\mathcal{D} \subseteq \mathcal{C}$ 的包含函子 $\mathcal{D} \hookrightarrow \mathcal{C}$（对象与态射原样返回）总是忠实的；它是满的当且仅当 $\mathcal{D}$ 是 $\mathcal{C}$ 的**全子范畴**（即 $\operatorname{Hom}_{\mathcal{D}}(A, B) = \operatorname{Hom}_{\mathcal{C}}(A, B)$）。例如 $\mathbf{Ab} \hookrightarrow \mathbf{Grp}$ 忠实但不满。

**例 8（单对象范畴之间的函子）** 幺半群 $M, N$ 作为单对象范畴，函子 $M \to N$ 恰好就是幺半群同态 $\varphi: M \to N$：它在唯一的对象上平凡作用，在态射上作用为 $\varphi$，复合的保持就是 $\varphi(g \cdot f) = \varphi(g) \cdot \varphi(f)$。这再次印证"群、幺半群就是单对象范畴"（[范畴](categories.md) 例 7）。此时"忠实/满"的判定也简化了：$\varphi$ 对应的函子忠实 ⟺ $\varphi$ 单射，满 ⟺ $\varphi$ 满射（都归结为唯一的 Hom 集 $M \to N$ 的映射），且恒为本质满（唯一对象 $*$ 被映到 $*$）。

**例 9（对合与对偶）** 反变函子复合两次给出协变函子。例如双重对偶 $(-)^{**}: \mathbf{Vect}_K \to \mathbf{Vect}_K$ 是协变函子（先反变再反变）；在有限维情形它与恒等函子自然同构（[自然变换](natural_transformations.md) 例 1）。

## 函子的复合与恒等律

函子可以复合：$G \circ F: \mathcal{C} \to \mathcal{E}$（对象 $A \mapsto G(F(A))$，态射 $f \mapsto G(F(f))$）仍是函子；恒等函子 $\operatorname{id}_{\mathcal{C}}$ 是复合的单位元。于是：

**命题 1（范畴 $\mathbf{Cat}$）** 以所有小范畴为对象、函子为态射、函子复合为复合，构成一个范畴 $\mathbf{Cat}$。$\mathbf{Cat}$ 不是小范畴。

!!! note "要点"
    函子的复合满足结合律与单位律，其验证逐项落在对象与态射上，与 [范畴](categories.md) 中范畴公理完全一致。函子"把范畴映到范畴"——这正是"范畴的范畴" $\mathbf{Cat}$ 的由来。

**命题 3（函子保持同构）** 若 $f$ 是同构，则 $F(f)$ 是同构，且 $F(f)^{-1} = F(f^{-1})$。

**证明** 由函子性：
$$
F(f^{-1}) \circ F(f) = F(f^{-1} \circ f) = F(\operatorname{id}) = \operatorname{id}, \qquad F(f) \circ F(f^{-1}) = \operatorname{id}
$$
故 $F(f)$ 可逆。$\blacksquare$

**推论** 同构的对象被映到同构的对象：$A \cong B \implies F(A) \cong F(B)$。这是"函子是不变量的载体"这一事实的起点（例如基本群 $\pi_1$ 把同胚的空间映到同构的群）。

## 忠实、满与本质满函子

**定义 3（忠实/满/本质满）** 函子 $F: \mathcal{C} \to \mathcal{D}$：

- 称为**忠实**（faithful）的，若对每对对象 $A, B$，映射 $\operatorname{Hom}_{\mathcal{C}}(A, B) \to \operatorname{Hom}_{\mathcal{D}}(F(A), F(B))$，$f \mapsto F(f)$ 是**单射**；
- 称为**满**（full）的，若上述映射是**满射**；
- 称为**本质满**（essentially surjective）的，若每个 $D \in \mathcal{D}$ 同构于某个 $F(A)$；
- 既忠实又满的函子称为**全忠实**（fully faithful）的。

**例子**：

- 遗忘函子 $\mathbf{Grp} \to \mathbf{Set}$ 忠实但不满（并非每个函数都是群同态）；
- 包含函子 $\mathbf{Ab} \to \mathbf{Grp}$ 忠实、不满、非本质满（存在非交换群）；
- 对偶函子 $(-)^*: \mathbf{Vect}_K^{\mathrm{fd}} \to (\mathbf{Vect}_K^{\mathrm{fd}})^{\mathrm{op}}$（有限维向量空间范畴）是全忠实且本质满的（每个有限维空间同构于其对偶空间），因此是范畴等价。

| 函子 | 忠实 | 满 | 本质满 |
|---|---|---|---|
| $U: \mathbf{Grp} \to \mathbf{Set}$（遗忘） | ✓ | ✗ | ✗ |
| $\mathbf{Ab} \hookrightarrow \mathbf{Grp}$（包含） | ✓ | ✗ | ✗ |
| $(-)^*: \mathbf{Vect}_K^{\mathrm{fd}} \to (\mathbf{Vect}_K^{\mathrm{fd}})^{\mathrm{op}}$ | ✓ | ✓ | ✓ |

**命题 2（忠实函子反映单/满态射）** 函子把单态射（满态射）映为单态射（满态射）；忠实函子还**反映**单态射与满态射：若 $F(f)$ 是单态射（满态射），则 $f$ 也是。

**证明** 以单态射为例：若 $f \circ g = f \circ h$，则 $F(f) \circ F(g) = F(f) \circ F(h)$；$F(f)$ 单 ⟹ $F(g) = F(h)$；$F$ 忠实 ⟹ $g = h$。$\blacksquare$

!!! note "补充"
    全忠实函子还**反映同构**：若 $F(f)$ 是同构，则 $f$ 是同构（由满性取 $F(g) = F(f)^{-1}$，再由忠实性验证逆的等式）。但全忠实并不保证本质满：例如包含函子 $\mathbf{Ab} \to \mathbf{Grp}$ 全忠实但非本质满。这一点在 [Yoneda 引理](yoneda.md) 中"嵌入是忠实的"论断中会被反复使用。

## 范畴等价

**定义 4（范畴等价）** 函子 $F: \mathcal{C} \to \mathcal{D}$ 称为**等价**，若存在函子 $G: \mathcal{D} \to \mathcal{C}$ 与自然同构
$$
G \circ F \cong \operatorname{id}_{\mathcal{C}}, \qquad F \circ G \cong \operatorname{id}_{\mathcal{D}}
$$
此时称 $\mathcal{C}$ 与 $\mathcal{D}$ **等价**，记 $\mathcal{C} \simeq \mathcal{D}$。

等价比同构（对象一一对应）弱得多：它只要求两个范畴"含有的信息相同"。范畴论中"本质相同"的概念是等价而非同构。

**定理 1（等价的刻画）** $F$ 是等价当且仅当 $F$ 全忠实且本质满。

**证明思路** 本质满给出对象层面的"拟逆"：对每个 $D$ 选 $A_D$ 与同构 $\varepsilon_D: F(A_D) \cong D$；全忠实给出态射层面的对应与唯一性，从而拼出 $G$ 与两个自然同构。细节略。$\blacksquare$

**例子**：对偶函子给出 $\mathbf{Vect}_K^{\mathrm{fd}} \simeq (\mathbf{Vect}_K^{\mathrm{fd}})^{\mathrm{op}}$（由双重对偶 $V \cong V^{**}$，见 [自然变换](natural_transformations.md)）；选择公理下，$\mathbf{Set}$ 等价于其骨架（由基数构成的全子范畴）。

## 函子与对偶

反变函子可统一看作"从反范畴来的协变函子"，因此对偶原理（[范畴](categories.md)）使反变函子的性质全部由协变情形自动给出。例如，反变 Hom 函子 $\operatorname{Hom}(-, B): \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ 就是 $\mathcal{C}^{\mathrm{op}}$ 上的协变 Hom 函子 $\operatorname{Hom}(-, B)$（把 $\mathcal{C}^{\mathrm{op}}$ 中的对象 $A$ 映到 $\operatorname{Hom}_{\mathcal{C}}(A, B)$）。

## 函子为什么重要

- **表达不变量**：把复杂的数学对象映到更简单范畴中的对象。基本群 $\pi_1: \mathbf{Top}_* \to \mathbf{Grp}$、同调 $H_n: \mathbf{Top} \to \mathbf{Ab}$ 都是函子；"同胚的空间有同构的基本群"就是命题 3 的特例。
- **统一"翻译"**：遗忘（丢掉结构）、自由（生成结构）、对偶（反转方向）、表示（用 Hom 观察对象）——它们都是函子，且常常成对出现（遗忘与自由构成伴随，见 [泛性质与极限](universal_properties.md)）。
- **比较范畴**：忠实函子保证不丢失信息，全忠实函子把 $\mathcal{C}$ 完整地嵌入 $\mathcal{D}$，等价则宣布两个范畴"本质相同"。
- **通往 Yoneda**：Hom 函子把每个对象 $A$ 映到"所有对象眼中的 $A$"，这一观察在 [Yoneda 引理](yoneda.md) 中达到顶峰。

## 本页小结

- 协变函子保持复合与恒等；反变函子反转箭头（= 反范畴上的协变函子）；
- 遗忘、自由、Hom、幂集、对偶——最重要的函子都来自"从对象提取/附加信息"；
- 函子保持同构；忠实函子反映单态射与满态射；
- 全忠实 + 本质满 ⟺ 范畴等价：两个范畴"本质相同"的精确含义；
- $\mathbf{Cat}$：小范畴与函子构成的范畴。

## 延伸阅读

- [范畴论导览](index.md)：本目录的内容地图。
- [自然变换](natural_transformations.md)：函子之间的映射。
- [Yoneda 引理](yoneda.md)：Hom 函子如何决定对象。
- [范畴](categories.md)：范畴与反范畴。
- [泛性质与极限](universal_properties.md)：自由函子与遗忘函子之间的伴随关系。
- [符号表](../../notation/index.md)。
