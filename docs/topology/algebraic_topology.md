---
title: 代数拓扑
tags: [拓扑, 代数拓扑]
---

# 代数拓扑

> 代数拓扑（algebraic topology）把空间映射为群、环等代数不变量，从而判断空间能否连续变形为彼此。

## 同伦与基本群

同伦（homotopy）是映射之间的连续变形。以基点为端点的闭路按同伦分类，并以路径拼接为乘法，形成基本群 $\pi_1(X)$。例如

$$\pi_1(S^1)\cong\mathbb Z,$$

而 $S^n$ 在 $n\ge2$ 时单连通。基本群能够区分圆与球面，并控制覆盖空间。

## 同调

同调群（homology group）$H_n(X)$ 把 $n$ 维“洞”编码成 Abel 群。边界算子满足 $\partial^2=0$，所以

$$H_n(X)=\ker\partial_n/\operatorname{im}\partial_{n+1}.$$

同调具有同伦不变性、长正合列和 Mayer–Vietoris 序列等强大计算工具。

## 上同调

上同调（cohomology）不仅给出群，还带有杯积（cup product），形成上同调环，因此能识别同调群看不到的乘法结构。

## 资料

- [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html)：免费开放的经典教材，覆盖基本群、同调、上同调与同伦论。
- [同伦类型论](../foundations/type_theory/homotopy_type_theory.md)：拓扑与类型论的另一座桥梁。
