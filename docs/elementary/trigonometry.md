---
title: 三角函数
tags:
  - 初等数学
---

# 三角函数

> 三角函数（trigonometric functions）从直角三角形的边长比出发，经单位圆推广到任意实数，成为描述旋转、振动和周期现象的基本工具。

## 1. 角与弧度制

**定义 1（弧度，radian）** 在半径为 $r$ 的圆中，长度为 $l$ 的圆弧所对圆心角的弧度数为

$$
\theta=\frac lr.
$$

一周为 $2\pi$ 弧度，因此

$$
180^\circ=\pi\ \text{rad},
\qquad
1^\circ=\frac\pi{180}\ \text{rad}.
$$

使用公式 $l=r\theta$ 和扇形面积 $S=\frac12r^2\theta$ 时，$\theta$ 必须采用弧度制。

## 2. 单位圆定义

在单位圆 $x^2+y^2=1$ 上，从正 $x$ 轴逆时针旋转角 $\theta$ 到点 $P$，定义

$$
P=(\cos\theta,\sin\theta).
$$

当 $\cos\theta\ne0$ 时，

$$
\tan\theta=\frac{\sin\theta}{\cos\theta}.
$$

单位圆定义使三角函数适用于任意实数角，并直接给出符号、周期与对称性。

## 3. 基本性质

| 函数 | 定义域 | 值域 | 最小正周期 | 奇偶性 |
| --- | --- | --- | --- | --- |
| $\sin x$ | $\mathbb R$ | $[-1,1]$ | $2\pi$ | 奇函数 |
| $\cos x$ | $\mathbb R$ | $[-1,1]$ | $2\pi$ | 偶函数 |
| $\tan x$ | $x\ne\frac\pi2+k\pi$ | $\mathbb R$ | $\pi$ | 奇函数 |

基本恒等式为

$$
\sin^2x+\cos^2x=1,
$$

以及

$$
1+\tan^2x=\frac1{\cos^2x}.
$$

诱导公式可以从单位圆的对称性理解，例如

$$
\sin(-x)=-\sin x,
\qquad
\cos(-x)=\cos x.
$$

## 4. 和差公式

**定理 1（三角函数和差公式，angle addition formulas）**

$$
\begin{aligned}
\sin(\alpha+\beta)
&=\sin\alpha\cos\beta+\cos\alpha\sin\beta,\\
\cos(\alpha+\beta)
&=\cos\alpha\cos\beta-\sin\alpha\sin\beta,\\
\tan(\alpha+\beta)
&=\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}.
\end{aligned}
$$

令 $\beta=\alpha$ 得二倍角公式：

$$
\sin2\alpha=2\sin\alpha\cos\alpha,
$$

$$
\cos2\alpha=\cos^2\alpha-\sin^2\alpha
=2\cos^2\alpha-1
=1-2\sin^2\alpha.
$$

## 5. 辅助角公式

对不全为零的 $a,b$，令

$$
R=\sqrt{a^2+b^2},
\qquad
\cos\varphi=\frac aR,
\qquad
\sin\varphi=\frac bR,
$$

则

$$
a\sin x+b\cos x=R\sin(x+\varphi).
$$

因此

$$
|a\sin x+b\cos x|\le\sqrt{a^2+b^2}.
$$

**例 1**

$$
\sin x+\cos x=\sqrt2\sin\left(x+\frac\pi4\right),
$$

所以其最大值为 $\sqrt2$，最小值为 $-\sqrt2$。

## 6. 三角函数图象

函数

$$
y=A\sin(\omega x+\varphi)+b
$$

中：

- $|A|$ 是振幅（amplitude）；
- 周期为 $T=\dfrac{2\pi}{|\omega|}$；
- $\varphi$ 控制相位（phase）；
- $b$ 控制竖直平移。

分析图象时，先把 $\omega x+\varphi$ 写成 $\omega(x-x_0)$，再判断水平平移方向。

## 7. 解三角形

设三角形三边 $a,b,c$ 分别对应角 $A,B,C$。

**定理 2（正弦定理，law of sines）**

$$
\frac a{\sin A}=\frac b{\sin B}=\frac c{\sin C}=2R,
$$

其中 $R$ 是外接圆半径。

**定理 3（余弦定理，law of cosines）**

$$
c^2=a^2+b^2-2ab\cos C.
$$

余弦定理在 $C=90^\circ$ 时退化为勾股定理。

三角形面积还可写成

$$
S=\frac12ab\sin C.
$$

## 8. 常见错误

1. 角度制和弧度制混用；
2. 忘记 $\tan x$ 的定义域限制；
3. 把 $\sin(\alpha+\beta)$ 错拆成 $\sin\alpha+\sin\beta$；
4. 用平方变形解方程后不验根；
5. 只记诱导公式符号，不回到单位圆判断象限；
6. 由正弦定理处理 SSA 条件时忽略可能存在两个三角形。

## 延伸阅读

- [高中数学](senior_high.md)：高中知识结构
- [函数](functions.md)：周期性、奇偶性与图象变换
- [初等几何](../geometry/elementary.md)：三角形与圆
- [导数](../analysis/calculus/derivatives.md)：三角函数的变化率
