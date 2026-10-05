---
title: 数学与生命科学及医学
tags: [交叉学科, 数学生物学, 医学统计, 流行病学]
---

# 数学与生命科学及医学

## 种群与生态动力学

指数增长 $N'=rN$ 忽略资源限制。Logistic model

$$
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
$$

加入环境容纳量（carrying capacity）$K$。Lotka–Volterra equations 用耦合 ODE 描述捕食、竞争或互利关系；年龄结构模型、分枝过程和空间生态则需要矩阵、随机过程或 PDE。

$r$ 和 $K$ 是模型参数，不一定是跨环境不变的生物常数。若观测时间不足，不同增长模型可能几乎无法区分。

## 流行病模型

基本 SIR model 把人口分为易感者、感染者和移出者：

$$
\dot S=-\beta\frac{SI}{N},\qquad
\dot I=\beta\frac{SI}{N}-\gamma I,\qquad
\dot R=\gamma I.
$$

在该齐次混合模型中，基本再生数（basic reproduction number）为 $R_0=\beta/\gamma$。现实中的接触网络、潜伏期、年龄结构、行为变化和空间流动会改变阈值与预测，因此不能脱离模型定义比较不同研究报告的 $R_0$。

传染病建模结合动力系统、分枝过程、Bayesian inference、网络和 optimal control，用于比较干预情景。情景模拟是“给定假设会怎样”，不等同于无条件预言。

## 分子、生物信息与系统生物学

序列比对使用动态规划，隐 Markov 模型（hidden Markov model, HMM）描述不可直接观测的生物状态，系统发育（phylogenetics）用树与随机替换模型重建演化关系。基因调控、代谢和蛋白相互作用可表示为网络或随机反应系统。

高通量实验常出现“变量数远大于样本数”，需要稀疏性、降维、multiple testing correction 和严格的训练/验证划分。批次效应（batch effect）若与研究组别混杂，算法无法仅靠增加复杂度消除因果歧义。

## 医学成像与生理系统

CT、MRI、超声和显微成像涉及 Fourier analysis、Radon transform、PDE 与 inverse problem。心脏电活动、神经元放电、药代动力学和肿瘤生长则使用 ODE/PDE、随机过程与多尺度模型。

成像重建中的正则化会在噪声抑制与细节保留之间折中；图像看起来更清晰不等于诊断信息必然更准确。

## 临床试验、因果与风险

随机对照试验（randomized controlled trial, RCT）利用随机化平衡潜在混杂。观察性研究需要明确 estimand，并使用匹配、加权、工具变量或因果图等方法处理假设。生存分析使用生存函数 $S(t)$、hazard function 和 censoring 机制。

统计显著性、效应大小、临床意义和个体风险是不同概念。预测模型还应报告校准、区分度、外部验证与适用人群。

## 延伸阅读

- [概率与统计](../probability_statistics/index.md)、[随机过程](../probability_statistics/stochastic_processes.md)与[微分方程](../applied_math/differential_equations.md)
- [NIH/PMC: Mathematical Models for Pathogens and Infectious Diseases](https://pmc.ncbi.nlm.nih.gov/articles/PMC8961237/)
- [MIT OCW: Principles of Applied Mathematics](https://ocw.mit.edu/courses/18-311-principles-of-applied-mathematics-spring-2014/pages/syllabus/)
