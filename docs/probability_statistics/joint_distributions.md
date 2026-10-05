---
title: 多维随机变量与条件期望
tags: [概率与统计]
---

# 多维随机变量与条件期望

## 联合分布

随机向量 $X=(X_1,\ldots,X_n)$ 的联合分布（joint distribution）同时描述各分量及其依赖关系。二维连续情形中，联合密度 $f_{X,Y}$ 满足

$$P((X,Y)\in A)=\iint_A f_{X,Y}(x,y)\,dx\,dy.$$

边缘密度（marginal density）通过积分消去另一变量：$f_X(x)=\int f_{X,Y}(x,y)\,dy$。若联合密度可分解为 $f_Xf_Y$，则 $X,Y$ 独立。

## 协方差与相关系数

$$\operatorname{Cov}(X,Y)=E[(X-EX)(Y-EY)],$$

$$\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.$$

独立通常推出不相关，但不相关一般不推出独立；联合正态情形是重要例外。

## 条件期望

$E[X\mid\mathcal G]$ 是关于信息 $\mathcal G$ 可测、并在每个 $G\in\mathcal G$ 上保持积分的随机变量。它可视为“已知信息下对 $X$ 的最佳预测”。塔式性质（tower property）为

$$E(E[X\mid\mathcal G])=E[X].$$

全期望公式、全方差公式与 Bayes 公式都可由条件期望统一表达。

## 变量变换

若 $(U,V)=T(X,Y)$ 且变换可逆，则密度变换公式为

$$f_{U,V}(u,v)=f_{X,Y}(T^{-1}(u,v))\left|\det D T^{-1}(u,v)\right|.$$

这里的 Jacobian 修正描述坐标变换造成的面积伸缩。

## 资料

- [Harvard Stat 110](https://stat110.hsites.harvard.edu/)：概率论课程、视频与开放教材。
- [多元微积分](../analysis/multivariable.md)：重积分和 Jacobian。
