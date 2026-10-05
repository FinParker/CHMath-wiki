---
title: 数理统计
tags: [概率与统计, 数理统计]
---

# 数理统计

> 数理统计（mathematical statistics）研究如何从有限样本推断未知总体或生成机制。

## 统计模型与估计

参数模型写成分布族 $\{P_\theta:\theta\in\Theta\}$。统计量（statistic）是样本的函数。估计量常按偏差、方差和均方误差评价：

$$\operatorname{MSE}(\hat\theta)=\operatorname{Var}(\hat\theta)+\operatorname{Bias}(\hat\theta)^2.$$

极大似然估计（maximum likelihood estimation, MLE）选择使观测数据最可能的参数；矩估计（method of moments）则令样本矩匹配总体矩。

## 充分性与信息

充分统计量（sufficient statistic）保留样本中关于参数的全部信息。Fisher–Neyman 因子分解定理给出常用判据。Fisher 信息衡量似然对参数的敏感程度，Cramér–Rao 下界限制无偏估计量可能达到的方差。

## 置信区间与假设检验

置信区间（confidence interval）的覆盖率是重复抽样意义下的长期比例。假设检验区分第一类错误和第二类错误；$p$ 值是在原假设下观察到当前或更极端数据的概率，并不是“原假设为真的概率”。

## Bayesian 推断

Bayes 方法通过

$$p(\theta\mid x)\propto p(x\mid\theta)p(\theta)$$

把先验分布与似然结合成后验分布。频率学派与 Bayesian 学派对概率和未知参数的解释不同，但共享概率模型与计算工具。

## 回归

线性模型 $Y=X\beta+\varepsilon$ 的最小二乘估计在 $X^TX$ 可逆时为

$$\hat\beta=(X^TX)^{-1}X^Ty.$$

模型诊断必须检查残差、异方差、异常值和模型设定；预测相关不自动意味着因果关系。

## 资料

- [MIT OCW: Statistics for Applications](https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/)：估计、检验、回归与 Bayesian 方法。
- [概率极限定理](limit_theorems.md)：统计渐近理论的基础。
