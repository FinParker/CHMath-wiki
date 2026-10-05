---
title: 数学与经济、金融及社会系统
tags: [交叉学科, 数理经济, 金融数学, 社会网络]
---

# 数学与经济、金融及社会系统

## 选择、均衡与优化

消费者理论把偏好表示为效用函数，并研究预算约束下的选择：

$$
\max_x u(x)\quad\text{s.t.}\quad p\cdot x\le w.
$$

凸分析和 Lagrange multiplier 给出局部与全局最优条件。一般均衡理论使用不动点定理证明某些条件下价格与供需可以同时协调。存在性定理并不保证均衡唯一、稳定或容易计算。

运筹学把生产、运输、匹配和排程写成线性规划、整数规划、网络流或随机优化问题。影子价格（shadow price）解释约束边际放松的价值，但只在相应模型和敏感度范围内有效。

## 博弈与机制设计

博弈论（game theory）研究多个决策者相互影响时的策略。Nash equilibrium 是每个参与者对其他人策略的最佳回应组合。有限博弈在混合策略中存在 Nash 均衡，但均衡可能多重，也不自动代表公平、有效或会被学习过程选中。

重复博弈、Bayesian game、auction theory 和 mechanism design 进一步研究信息不完全、激励和规则设计。这里结合概率、优化、不动点、凸对偶和动态规划。

## 计量经济与因果推断

计量经济学（econometrics）用统计模型估计经济关系。线性模型

$$Y=X\beta+\varepsilon$$

只有在外生性、抽样和模型条件成立时，系数才有相应解释。遗漏变量、反向因果、选择偏差和测量误差会破坏简单回归的因果含义。

随机实验、difference-in-differences、regression discontinuity 和 instrumental variables 各依赖不同的可识别性假设。因果结论来自研究设计与假设，不是由某个算法名称自动保证。

## 金融数学

金融数学使用随机过程、随机微积分、PDE 和数值方法描述价格、利率与风险。几何 Brownian motion 的理想化模型为

$$dS_t=\mu S_t\,dt+\sigma S_t\,dW_t.$$

在无套利、可交易、连续对冲等假设下，衍生品定价可转化为风险中性期望或 Black–Scholes 型 PDE。现实中的跳跃、流动性、交易成本和模型误设会造成 model risk。

风险管理还使用 value at risk、expected shortfall、极值理论和 stress testing。历史相关性在危机期可能改变，因此参数不确定性与情景分析不可省略。

## 社会与经济网络

家庭、企业、银行和信息传播形成网络。中心性、社群、同配性、扩散和级联用于研究影响力、系统性风险与观点传播。博弈与网络结合后，个体激励会反过来改变网络结构。

由网络数据发现相关结构，不足以证明社会机制。缺失边、平台推荐机制和隐私保护处理都会改变观测网络。

## 延伸阅读

- [最优化](../applied_math/optimization.md)、[概率统计](../probability_statistics/index.md)与[图论](../discrete_mathematics/graph_theory.md)
- [MIT OCW: Game Theory](https://ocw.mit.edu/courses/14-126-game-theory-spring-2016/)
- [MIT OCW: Mathematics with Applications in Finance](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/)
- [MIT OCW: Networks, Complexity and Its Applications](https://ocw.mit.edu/courses/mas-961-networks-complexity-and-its-applications-spring-2011/pages/syllabus/)
