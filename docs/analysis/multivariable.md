---
title: 多元微积分
tags: [分析, 高等数学]
---

# 多元微积分

> 多元微积分（multivariable calculus）把一元函数的极限、导数和积分推广到 $\mathbb R^n$，并把局部线性近似与空间几何联系起来。

## 微分

对 $f:\mathbb R^n\to\mathbb R$，偏导数（partial derivative）只改变一个坐标。若存在向量 $\nabla f(a)$ 使

$$f(a+h)=f(a)+\nabla f(a)\cdot h+o(\|h\|),$$

则 $f$ 在 $a$ **可微**（differentiable），$\nabla f$ 是梯度（gradient）。沿单位向量 $u$ 的方向导数为

$$D_uf(a)=\nabla f(a)\cdot u.$$

梯度指向函数增长最快的方向，并垂直于等值面。向量值映射的导数由 Jacobian 矩阵表示；复合映射满足链式法则（chain rule）。

## 多元极值

内部局部极值的必要条件通常是 $\nabla f=0$。二阶信息由 Hessian 矩阵给出：正定对应严格局部极小，负定对应严格局部极大，不定对应鞍点。

带约束 $g(x)=c$ 的极值可用 **Lagrange 乘子法**（method of Lagrange multipliers）：

$$\nabla f(x)=\lambda\nabla g(x).$$

它表达了极值点处目标函数与约束面的法向量平行。

## 重积分与换元

二重、三重积分把“分割—求和—取极限”推广到区域与体积。Fubini 定理（Fubini's theorem）在适当条件下允许化为累次积分。变量代换时必须乘 Jacobian 行列式：

$$\int_{T(U)}f(x)\,dx=\int_U f(T(u))\,|\det DT(u)|\,du.$$

极坐标中的面积元是 $r\,dr\,d\theta$；球坐标中的体积元是 $\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$。

## 向量分析

向量场 $F$ 的散度（divergence）与旋度（curl）分别描述局部源汇和旋转。三个核心积分定理统一了“边界上的积分”和“内部的导数”：

- Green 定理（Green's theorem）：平面区域与其边界；
- Stokes 定理（Stokes' theorem）：曲面与其边界曲线；
- Gauss 散度定理（divergence theorem）：体积与其边界曲面。

现代观点把它们统一为广义 Stokes 定理 $\int_M d\omega=\int_{\partial M}\omega$。

## 资料

- [MIT OCW: Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/)：含视频、讲义、习题和考试。
- [线性代数](../algebra/linear/index.md)：Jacobian、Hessian 和线性近似的语言。
- [微分几何](../geometry/differential_geometry.md)：流形上的微积分。
