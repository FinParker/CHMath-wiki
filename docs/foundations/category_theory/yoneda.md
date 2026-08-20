---
title: Yoneda 引理
tags:
  - 范畴论
---

# Yoneda 引理

Yoneda 引理是范畴论最深刻的"平凡定理"：它断言一个对象完全由"它与其他对象的态射关系"决定。它的证明只有几行，但推论覆盖整个现代数学——从 Cayley 定理到表示论。范畴论的哲学"态射比对象更重要"在此达到精确表述。

## 准备：Hom 函子与函子范畴

设 $\mathcal{C}$ 是局部小范畴。对每个对象 $A$：

- **协变 Hom 函子** $h_A = \operatorname{Hom}(A, -): \mathcal{C} \to \mathbf{Set}$（见 [函子](functors.md)）；
- **反变 Hom 函子** $h^A = \operatorname{Hom}(-, A): \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$。

函子范畴 $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$（见 [自然变换](natural_transformations.md)）的对象称为 $\mathcal{C}$ 上的**预层**。对函子 $F, G$，用 $\operatorname{Nat}(F, G)$ 记 $F$ 到 $G$ 的自然变换的集合。

## 定理 1（Yoneda 引理）

**定理 1（Yoneda 引理）** 设 $\mathcal{C}$ 是局部小范畴，$A \in \mathcal{C}$，$F: \mathcal{C} \to \mathbf{Set}$ 是函子。则映射
$$
\Phi: \operatorname{Nat}(h_A, F) \to F(A), \qquad \alpha \mapsto \alpha_A(\operatorname{id}_A)
$$
是**双射**。而且这个双射在 $A$（反变地）与 $F$（协变地）中都是自然的。

换句话说：
$$
\operatorname{Nat}(\operatorname{Hom}(A, -), F) \cong F(A)
$$

**直观** 自然变换 $\alpha: h_A \Rightarrow F$ 的组件 $\alpha_B$ 把"从 $A$ 出发的箭头 $f: A \to B$"送到 $F(B)$ 的元素。自然性说"先复合再送 = 先送再走 $F(f)$"：
$$
\alpha_B(f) = F(f)(\alpha_A(\operatorname{id}_A))
$$
因此整个 $\alpha$ 由它在**恒等箭头** $\operatorname{id}_A$ 上的取值唯一决定。$\operatorname{id}_A$ 是 $h_A$ 的"万能元素"：从它出发，通过复合 $f \mapsto f \circ \operatorname{id}_A$ 可以得到 $h_A$ 的一切元素。

**证明** 构造 $\Phi$ 的逆。给定 $x \in F(A)$，定义自然变换 $\Psi(x) = \alpha$，其组件为
$$
\alpha_B: \operatorname{Hom}(A, B) \to F(B), \qquad f \mapsto F(f)(x)
$$

分三步验证：

1. **$\alpha$ 是自然变换**：对 $g: B \to C$，需要 $F(g) \circ \alpha_B = \alpha_C \circ h_A(g)$。两边作用在 $f: A \to B$ 上：
   $$
   F(g)(\alpha_B(f)) = F(g)(F(f)(x)) = F(g \circ f)(x) = \alpha_C(g \circ f) = \alpha_C(h_A(g)(f))
   $$
   其中第二个等号用了函子性 $F(g) \circ F(f) = F(g \circ f)$。

2. **$\Phi \circ \Psi = \operatorname{id}$**：$\Phi(\Psi(x)) = \alpha_A(\operatorname{id}_A) = F(\operatorname{id}_A)(x) = x$。

3. **$\Psi \circ \Phi = \operatorname{id}$**：设 $x = \alpha_A(\operatorname{id}_A)$，则对任意 $f: A \to B$，
   $$
   \Psi(x)_B(f) = F(f)(x) = F(f)(\alpha_A(\operatorname{id}_A)) = \alpha_B(h_A(f)(\operatorname{id}_A)) = \alpha_B(f)
   $$
   其中第三个等号是 $\alpha$ 的自然性（$h_A(f)(\operatorname{id}_A) = f \circ \operatorname{id}_A = f$）。故 $\Psi(x) = \alpha$。$\blacksquare$

**关于"在 $A$ 与 $F$ 中自然"** 双射 $\Phi$ 不只是逐点双射，它还与 $A$ 和 $F$ 的变化相容：

- 在 $F$ 中协变：对自然变换 $\eta: F \Rightarrow G$，方块
  $$
  \operatorname{Nat}(h_A, F) \xrightarrow{\ \eta \circ (-)\ } \operatorname{Nat}(h_A, G), \qquad F(A) \xrightarrow{\ \eta_A\ } G(A)
  $$
  交换；
- 在 $A$ 中反变：对 $f: A' \to A$，方块
  $$
  \operatorname{Nat}(h_A, F) \to \operatorname{Nat}(h_{A'}, F), \qquad F(A) \xrightarrow{\ F(f)\ } F(A')
  $$
  交换（第一行由"复合 $(-) \circ f$"给出）。

这两条交换性保证同构 $\operatorname{Nat}(h_A, F) \cong F(A)$ 是函子范畴中的自然同构，而不只是集合之间的对应。

!!! note "要点"
    Yoneda 引理的证明"只是把恒等态射 $\operatorname{id}_A$ 传来传去"，但力量在于：**自然变换 $\operatorname{Hom}(A, -) \Rightarrow F$ 完全由它在 $\operatorname{id}_A$ 处的取值决定**。自然变换看起来是一族映射，实际上只含 $F(A)$ 一个元素的信息。

## 推论：Yoneda 嵌入

**推论 1（Yoneda 嵌入）** 反变 Yoneda 嵌入
$$
y: \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}], \qquad A \mapsto h^A = \operatorname{Hom}(-, A)
$$
是**全忠实**函子：$\operatorname{Nat}(h^A, h^B) \cong \operatorname{Hom}(A, B)$。

**证明** 在 Yoneda 引理中取 $F = h^B$（此时 $h_B(A) = \operatorname{Hom}(B, A)$）得 $\operatorname{Nat}(h_A, h_B) \cong \operatorname{Hom}(B, A)$；交换 $A, B$ 即得协变版本，反变版本同理。$\blacksquare$

**推论 2（对象由其 Hom 函子决定）** 对 $A, B \in \mathcal{C}$：
$$
A \cong B \iff h_A \cong h_B \iff h^A \cong h^B
$$
其中 $h_A \cong h_B$ 指 Hom 函子自然同构。特别地：若两个对象在一切对象"眼中"给出同构的 Hom 集，则它们同构。

!!! note "反变版本"
    许多教材把 Yoneda 引理写成反变形式：对 $F: \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ 与 $A \in \mathcal{C}$，
    $$
    \operatorname{Nat}(h^A, F) \cong F(A)
    $$
    这由协变版本应用于 $\mathcal{C}^{\mathrm{op}}$ 得到（$h^A$ 在 $\mathcal{C}^{\mathrm{op}}$ 中就是协变 Hom 函子）。两种形式等价，使用时注意 $h_A$（协变）与 $h^A$（反变）的记号区别。

**实用准则**：要证明 $A \cong B$，可以（a）直接构造互逆的态射；或者（b）构造 Hom 函子的自然同构 $h_A \cong h_B$，再由推论 2 得出结论。后者在"对象由泛性质定义"时特别有用（见下文表示函子一节）。

## 例子

**例 1（$\mathbf{Set}$ 中）** 对集合 $A, B$：$\operatorname{Hom}(-, A) \cong \operatorname{Hom}(-, B) \implies A \cong B$。这个结论平凡（取 $X = \{*\}$ 立得 $A \cong B$），但它展示了普遍原理：对象由它与其他对象的关系决定。

**例 2（偏序集）** 偏序集 $P$ 作为范畴（[范畴](categories.md)），$h_a(x) = \{*\} \iff a \le x$（否则 $\varnothing$）。Yoneda 嵌入 $a \mapsto h_a$ 是全忠实的：对象 $a$ 完全由集合 $\{x \mid a \le x\}$（$a$ 的"上方"）决定。"对象由它与所有其他对象的关系决定"在这里是最直观的：$a$ 由"谁在它上面"决定，而 $a = \bigwedge\{x \mid a \le x\}$ 的上方交集即自身。

**例 3（Cayley 定理）** 群 $G$ 作为单对象范畴 $\mathbf{B}G$。Yoneda 嵌入把唯一的对象 $*$ 映到 Hom 函子 $h^*$，而 $h^*$ 的自同构群正是 $G$ 通过左乘作用在自身上的**左正则表示**：$g \mapsto (x \mapsto gx)$。于是 Cayley 定理"$G$ 同构于某个对称群的子群"是 Yoneda 嵌入忠实性的特例。

!!! tip "Cayley 定理 = Yoneda 引理的特例"
    群 = 单对象范畴；Yoneda 引理把"对象由 Hom 函子决定"应用到单对象范畴，就得到"群由左乘作用决定"，即 Cayley 定理。Yoneda 引理常被称为 Cayley 定理对一切范畴的推广。

**例 4（表示论一瞥）** 有限群 $G$ 的线性表示就是函子 $\mathbf{B}G \to \mathbf{Vect}_{\mathbb{C}}$（单对象范畴 $\mathbf{B}G$，见 [范畴](categories.md) 例 7）；两个表示之间的同态（$G$-等变线性映射）正是它们之间的自然变换。因此表示论可以看作"函子范畴的研究"——这解释了为什么 Yoneda 引理在表示论中无处不在。

## 哲学意义：关系决定对象

- 对象本身"没有内部"：$A$ 的所有信息都编码在预层 $h^A$ 中；
- 结构主义纲领：数学对象 = 它与所有其他对象的关系的总和；
- 范畴论由此回答"什么是同构"：两个对象不可区分（同构）⟺ 它们在其他对象眼中完全相同。

## Yoneda 嵌入与完备化

预层范畴 $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ 是**完备且余完备**的（一切小极限与余极限存在，逐点计算）。Yoneda 嵌入 $y: \mathcal{C} \to [\mathcal{C}^{\mathrm{op}}, \mathbf{Set}]$ 把 $\mathcal{C}$ 全忠实地嵌入这个"大得多的"范畴，且是**自由余完备化**：$\mathcal{C}$ 中每个对象被嵌入，而每个预层都可以表示为表示函子的余极限（这是 Yoneda 嵌入的基本性质，细节超出本页）。换句话说：范畴论通过 Yoneda 嵌入，把任意范畴"补全"成一个极限行为良好的范畴。

## 表示函子与泛性质

**定义 4（表示函子）** 函子 $F: \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$（或 $F: \mathcal{C} \to \mathbf{Set}$）称为**可表示**的，若存在对象 $A$ 与自然同构 $F \cong h^A$（或 $F \cong h_A$）；$A$ 称为 $F$ 的**表示对象**。

由 Yoneda 引理，表示对象若存在则**唯一到同构**：若 $F \cong h^A \cong h^B$，由嵌入的忠实性 $A \cong B$。这给出了 [泛性质与极限](universal_properties.md) 中"泛性质唯一决定对象"的抽象证明：

- **积**：泛性质 ⟺ 自然同构 $\operatorname{Hom}(X, A \times B) \cong \operatorname{Hom}(X, A) \times \operatorname{Hom}(X, B)$，即函子 $X \mapsto \operatorname{Hom}(X, A) \times \operatorname{Hom}(X, B)$ 被 $A \times B$ 表示；
- **自由群**：$\operatorname{Hom}_{\mathbf{Grp}}(F(S), G) \cong \operatorname{Hom}_{\mathbf{Set}}(S, U(G))$ 说明函子 $G \mapsto \operatorname{Hom}_{\mathbf{Set}}(S, U(G))$（协变版本）被 $F(S)$ 表示。

**小结**：泛性质 = 表示函子；表示对象唯一到同构——这正是 Yoneda 引理对"结构由关系决定"的定量版本。

把本页与 [泛性质与极限](universal_properties.md) 对照，可以得到一张"对应表"：

| 泛性质 | 被表示的函子 | 表示对象 |
|---|---|---|
| 终对象 | 常值函子 $X \mapsto \{*\}$ | 终对象 $1$ |
| 积 | $X \mapsto \operatorname{Hom}(X, A) \times \operatorname{Hom}(X, B)$ | $A \times B$ |
| 自由群 | $G \mapsto \operatorname{Hom}_{\mathbf{Set}}(S, U(G))$ | $F(S)$ |
| 张量积 | $U \mapsto \operatorname{Bilin}(V \times W, U)$ | $V \otimes W$ |

每一行的"表示对象存在且唯一到同构"都由 Yoneda 引理保证——这就是"泛性质"与"Yoneda 引理"交汇的地方。

## 延伸阅读

- [范畴论导览](index.md)：本目录的内容地图。
- [自然变换](natural_transformations.md)：Yoneda 引理的语言。
- [函子](functors.md)：Hom 函子与全忠实函子。
- [泛性质与极限](universal_properties.md)：表示函子与泛性质的联系。
- [范畴](categories.md)：单对象范畴与 Cayley 定理。
- [数学基础](../index.md)与[符号表](../../notation/index.md)。
