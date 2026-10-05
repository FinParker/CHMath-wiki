---
title: 最优化
tags: [应用数学, 最优化]
---

# 最优化

> 最优化（optimization）是在约束下寻找使目标函数最小或最大的变量。凸性使局部信息能够控制全局解。

## 基本形式

$$\min_x f_0(x)\quad\text{s.t.}\quad f_i(x)\le0,\ h_j(x)=0.$$

若目标和不等式约束均凸、等式约束仿射，就得到凸优化问题（convex optimization）。凸函数满足

$$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y).$$

可微凸函数的任意驻点都是全局最小点。

## 最优性与对偶

无约束可微问题的一阶必要条件是 $\nabla f(x^*)=0$。带约束问题由 Lagrangian

$$L(x,\lambda,\nu)=f_0(x)+\sum_i\lambda_if_i(x)+\sum_j\nu_jh_j(x)$$

统一表达。KKT 条件（Karush–Kuhn–Tucker conditions）在适当正则条件下刻画凸问题的最优解。

对偶问题给出原问题最优值的下界；Slater 条件常保证强对偶（strong duality）。

## 算法

梯度下降按 $x_{k+1}=x_k-\alpha_k\nabla f(x_k)$ 迭代；Newton 法利用 Hessian 的曲率信息；投影梯度处理简单约束；内点法适合线性、二次与一般凸规划。

## 资料

- [Boyd–Vandenberghe: Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/)：开放教材、讲义与习题。
- [多元微积分](../analysis/multivariable.md)：梯度、Hessian 与 Lagrange 乘子。
