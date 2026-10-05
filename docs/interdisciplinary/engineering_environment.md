---
title: 数学与工程、控制及地球环境
tags: [交叉学科, 工程数学, 控制论, 气候数学]
---

# 数学与工程、控制及地球环境

## 状态空间与反馈控制

线性时不变系统常写成

$$
\dot x=Ax+Bu,\qquad y=Cx+Du,
$$

其中 $x$ 是状态，$u$ 是输入，$y$ 是观测。特征值决定无输入线性系统的局部稳定性；可控性（controllability）和可观性（observability）分别判断输入能否驱动状态、观测能否恢复状态。

反馈 $u=-Kx$ 改变闭环矩阵 $A-BK$。最优控制（optimal control）在动力学约束下最小化性能指标，例如

$$
J(u)=\int_0^T\bigl(x^\mathsf TQx+u^\mathsf TRu\bigr)\,dt.
$$

稳定性、性能、能耗与鲁棒性往往不能同时无限改善；控制器还必须考虑执行器饱和、延迟和模型误差。

## 信号、估计与反问题

Fourier/Laplace transform、卷积和谱分析把信号分解到频率或模态。Kalman filter 在给定线性 Gaussian 状态空间模型下递推融合预测与观测；非线性、非 Gaussian 情形需要扩展、ensemble 或 particle 方法。

雷达、遥感、通信和医学成像都包含从含噪观测恢复信号的反问题。采样定理的条件、传感器响应和正则化偏差共同决定可恢复的信息，而不只是采样点数量。

## 结构、流体与运输

固体力学使用张量、变分法和有限元；流体力学使用守恒律和 Navier–Stokes equations；交通、物流和电力系统使用图、网络流、排队论与优化。

数值模拟需要区分一致性（consistency）、稳定性（stability）和收敛性（convergence）。网格加密后的数值收敛也只说明算法逼近所写模型，不保证模型完整描述现实。

## 气候与地球系统

气候模型从简单能量平衡到耦合大气—海洋环流。一个零维能量平衡模型可写成

$$
C\frac{dT}{dt}=\frac{S_0}{4}(1-\alpha)-\varepsilon\sigma T^4,
$$

分别表示吸收的太阳辐射与向外长波辐射。更完整模型使用旋转流体 PDE、辐射传输、化学循环、冰冻圈和生物地球化学过程。

天气是具体初值下的短期状态，气候是分布与长期统计性质。数据同化（data assimilation）用动力模型与观测共同估计状态；极端事件分析使用极值理论和空间统计。模式集合的不确定性既来自初值，也来自参数、结构和未来情景。

## 运筹、可靠性与数字孪生

工程设计结合连续/离散优化、多目标决策、reliability theory 和 uncertainty quantification。数字孪生（digital twin）把模型、传感器和在线更新结合起来；其可靠性取决于状态估计、模型校准、数据质量和适用域，而非实时可视化本身。

## 延伸阅读

- [数学物理方法](../applied_math/mathematical_physics_methods.md)、[数值分析](../applied_math/numerical_analysis.md)与[最优化](../applied_math/optimization.md)
- [MIT OCW: Dynamic Systems and Control](https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/)
- [MIT OCW: Principles of Optimal Control](https://ocw.mit.edu/courses/16-323-principles-of-optimal-control-spring-2008/pages/syllabus/)
- [SIAM: Mathematics and Climate](https://epubs.siam.org/doi/book/10.1137/1.9781611978889)
