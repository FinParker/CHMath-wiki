---
title: 分形
tags: [几何, 分形, 动力系统]
---

# 分形

> 分形（fractal）研究在不同尺度下仍呈现精细结构的集合、图形与测度。它连接几何、动力系统、概率论、复分析和自然形态建模。

## 什么是分形

“分形”没有覆盖所有研究对象的单一公理化定义。常见特征包括自相似性（self-similarity）、任意小尺度上的精细结构，以及非整数维数；但具体对象可能只满足其中一部分。随机分形通常只在统计意义上自相似，某些分形的维数也可以是整数。

经典例子由不断重复的规则产生：

- Cantor 集（Cantor set）：每步删去各区间的中间三分之一；
- Koch 曲线（Koch curve）：把每条线段替换为四条长度为原来 $1/3$ 的线段；
- Sierpiński 三角形（Sierpiński triangle）：把三角形分成四个相似小三角形并删去中央一个。

这些例子同时说明：长度、面积、连通性和“维数”在极限过程中可以表现得很反直觉。

## 相似维数

若一个集合由 $N$ 个互不重叠的相似副本组成，每个副本的缩放比为 $r$，相似维数（similarity dimension）$d$ 满足

$$
Nr^d=1,\qquad d=\frac{\log N}{\log(1/r)}.
$$

因此 Cantor 集、Koch 曲线和 Sierpiński 三角形的相似维数分别是

$$
\frac{\log 2}{\log 3},\qquad
\frac{\log 4}{\log 3},\qquad
\frac{\log 3}{\log 2}.
$$

相似维数并非总等于 Hausdorff 维数（Hausdorff dimension）。对由相似压缩映射生成的集合，在开集条件（open set condition）等分离条件下，两者才有经典的一致性结论。

## Hausdorff 维数与盒维数

对 $E\subseteq\mathbb R^n$，用直径不超过 $\delta$ 的集合 $U_i$ 覆盖 $E$，定义

$$
\mathcal H^s_\delta(E)
=\inf\left\{\sum_i(\operatorname{diam}U_i)^s:
E\subseteq\bigcup_iU_i,\ \operatorname{diam}U_i\leq\delta\right\}.
$$

令 $\delta\to0$ 得到 $s$ 维 Hausdorff 测度（Hausdorff measure）。当 $s$ 经过某个临界值时，$\mathcal H^s(E)$ 通常从 $\infty$ 跳到 $0$；这个临界值就是 $\dim_H E$。

盒计数维数（box-counting dimension）更适合计算。若覆盖 $E$ 所需的边长为 $\varepsilon$ 的盒子数是 $N(\varepsilon)$，则在极限存在时

$$
\dim_B E=\lim_{\varepsilon\to0}
\frac{\log N(\varepsilon)}{\log(1/\varepsilon)}.
$$

Hausdorff 维数具有更好的理论性质；盒维数较容易数值估计，但极限可能不存在，而且两种维数不必相等。

## 迭代函数系统

迭代函数系统（iterated function system, IFS）是一组压缩映射 $f_1,\ldots,f_m$。在完备度量空间中，Hutchinson 定理（Hutchinson's theorem）保证存在唯一非空紧集 $K$ 满足

$$K=\bigcup_{i=1}^m f_i(K).$$

$K$ 称为 IFS 的吸引子（attractor）。Cantor 集与 Sierpiński 三角形都可由简单 IFS 构造。给每个映射配置概率后，还可得到自相似测度（self-similar measure）。

## 复动力系统

考虑二次迭代

$$z_{n+1}=f_c(z_n)=z_n^2+c.$$

充满 Julia 集（filled Julia set）$K_c$ 是轨道保持有界的初值集合，Julia 集（Julia set）为其边界 $J_c=\partial K_c$；Fatou 集（Fatou set）则是迭代族局部行为稳定的区域。参数平面中的 Mandelbrot 集（Mandelbrot set）定义为

$$
\mathcal M=\{c\in\mathbb C:(f_c^n(0))_{n\ge0}\text{ 有界}\}.
$$

对二次多项式，这也等价于 $K_c$ 连通。Mandelbrot 集是参数空间，Julia 集是固定参数下的动力平面，二者不应混为一谈。

## 分形与混沌

混沌（chaos）描述动力对初值的敏感依赖等时间演化性质；分形描述集合或测度的尺度结构。奇异吸引子（strange attractor）可能兼具混沌动力和分形几何，但“混沌”与“分形”不是同义词。Lyapunov 指数（Lyapunov exponent）刻画邻近轨道的平均指数分离率，维数则刻画吸引子的空间复杂度。

研究还包括随机分形（random fractal）、多重分形（multifractal）、渗流簇、分枝过程以及粗糙界面。多重分形不以单一维数概括全部尺度，而研究局部标度指数的谱。

## 资料

- [MIT OCW: Nonlinear Dynamics—Fractal Dimension](https://live.ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec23.pdf)
- [Cornell: Fractal Dimension and the Cantor Set](https://pi.math.cornell.edu/~numb3rs/baker/409.html)
- [Stony Brook: Introduction to Fatou–Julia Theory](https://www.math.stonybrook.edu/~scott/Papers/India/Fatou-Julia.pdf)
- [微分方程与动力系统](../applied_math/differential_equations.md)
- [测度论](../analysis/measure_theory.md)与[复分析](../analysis/complex/index.md)
