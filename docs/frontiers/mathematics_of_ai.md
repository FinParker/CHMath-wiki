---
title: AI 中的数学
tags: [前沿数学, 人工智能, 机器学习]
---

# AI 中的数学

> 本页讨论人工智能模型内部使用的数学（mathematics of AI）。若关心 AI 如何寻找和验证数学证明，请阅读[形式化数学与 AI](formal_ai.md)。

## 统一视角

机器学习（machine learning）把数据、模型、损失函数和算法组合起来：模型表示可选函数族，损失衡量预测误差，优化算法从数据中选择参数，概率论则描述噪声、不确定性和泛化。常见的正则化经验风险最小化（regularized empirical risk minimization）写成

$$
\min_\theta\left[
\frac1n\sum_{i=1}^n\ell(f_\theta(x_i),y_i)
+\lambda R(\theta)
\right].
$$

这个公式背后同时涉及函数逼近、统计推断、数值优化与计算复杂性。

## 线性代数与张量

向量表示（embedding）把离散对象映射到连续空间，矩阵和张量（tensor）表达批量线性运算。奇异值分解（singular value decomposition, SVD）支撑主成分分析、低秩近似和压缩；谱结构也用于图神经网络和训练动力学。

Transformer 的缩放点积注意力（scaled dot-product attention）为

$$
\operatorname{Attention}(Q,K,V)
=\operatorname{softmax}\!\left(\frac{QK^\mathsf T}{\sqrt{d_k}}\right)V.
$$

矩阵乘法给出相似度和加权组合；softmax 把每行分数归一化。多头注意力（multi-head attention）在不同子空间重复这一结构。

## 微积分、自动微分与反向传播

深度网络是函数复合。反向传播（backpropagation）本质上是链式法则在计算图上的高效组织；自动微分（automatic differentiation, AD）精确应用基本运算的导数规则，不等同于符号化简或有限差分。

反向模式 AD（reverse-mode AD）适合“许多参数、一个标量损失”的情形。梯度、Jacobian、Hessian 及 Hessian–vector product 决定优化、敏感度分析和不确定性近似的计算代价。

## 优化与训练动力学

随机梯度下降（stochastic gradient descent, SGD）用小批量梯度近似全数据梯度。动量、自适应步长、预条件和二阶信息用于改善尺度不均衡与曲率问题。

神经网络训练通常是高维非凸优化。训练误差低并不解释测试性能；研究还要分析损失地形（loss landscape）、过参数化（overparameterization）、隐式正则化（implicit regularization）以及算法与模型参数化之间的关系。

## 概率、统计与信息论

最大似然估计（maximum likelihood estimation, MLE）和 Bayesian inference 为参数学习与不确定性提供基础。泛化理论研究训练样本上的表现如何迁移到总体分布，涉及容量、稳定性、间隔和数据分布假设。分布漂移（distribution shift）下的结论需要额外条件。

信息论中的熵（entropy）、交叉熵（cross-entropy）、Kullback–Leibler 散度（KL divergence）和互信息（mutual information）用于表达编码代价和分布差异。例如离散分布的

$$
D_{\mathrm{KL}}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}\ge0.
$$

KL 散度通常不对称，也不满足三角不等式，因此不是度量（metric）。交叉熵损失可解释为条件模型的负对数似然。

## 几何、对称性与图结构

流形学习（manifold learning）假设高维数据集中在较低维结构附近；信息几何（information geometry）把概率分布族看作带度量的流形。等变性（equivariance）表示输入经群作用后，输出按可预测方式变换；卷积利用平移等变性，几何深度学习则研究图、流形和一般群作用上的模型。

这种归纳偏置（inductive bias）能减少必须从数据重新学习的结构，但只有当选定对称性与问题相符时才有效。

## 动力系统、控制与生成模型

残差网络的更新 $x_{k+1}=x_k+hF(x_k)$ 可看作 ODE 的 Euler 离散化，由此连接 neural ODE、稳定性和最优控制。扩散模型（diffusion model）通过逐步加噪的随机过程与学习到的逆向生成过程连接随机微分方程、score matching 和数值采样。

强化学习（reinforcement learning）结合 Markov 决策过程、动态规划和随机逼近。折扣 Bellman 最优方程为

$$
V^*(s)=\max_a\mathbb E\left[r+\gamma V^*(S')\mid s,a\right].
$$

在函数逼近和离策略学习中，收敛不能从表格型算法直接推得。

## 逼近、核方法与频率视角

通用逼近定理（universal approximation theorem）说明某些网络族在给定条件下能逼近广泛的函数，但不保证有限数据下能学到目标函数，也不保证训练算法高效找到参数。核方法（kernel methods）、Gaussian process 和 neural tangent kernel 提供线性化或概率视角；Fourier 与调和分析则研究模型对不同频率成分的表达和学习偏好。

## 活跃研究问题

- 大模型的 scaling laws 能在多大范围外推，其机制是什么；
- 过参数化模型为何仍能泛化，以及数据重复和污染如何影响评估；
- 表征学习（representation learning）何时恢复可迁移或可组合的结构；
- 如何得到校准良好的不确定性、因果推断和分布外鲁棒性；
- 如何严格描述可解释性、对齐和多智能体博弈；
- scientific machine learning 如何可靠结合守恒律、PDE 和观测数据。

这些问题横跨统计学习理论、优化、概率、几何、动力系统、博弈论和计算复杂性。经验上的成功可以提出数学问题，但不能代替定理的假设、证明和适用范围。

## 学习路线与资料

建议路线是：[线性代数](../algebra/linear/index.md) + [多元微积分](../analysis/multivariable.md) → [概率统计](../probability_statistics/index.md) + [最优化](../applied_math/optimization.md) → 数值分析、信息论、学习理论与具体模型。

- [Deep Learning（Goodfellow, Bengio, Courville）](https://www.deeplearningbook.org/)：线性代数、概率、数值计算、优化与深度模型的开放教材。
- [Stanford CS229: Machine Learning](https://cs229.stanford.edu/syllabus-summer2020.html)：线性代数、矩阵微积分、概率、MLE 与优化复习材料。
- [数据的数学](data_mathematics.md)：高维统计、随机矩阵、TDA 与学习理论。
- [形式化数学与 AI](formal_ai.md)：证明助理和 AI theorem proving。
