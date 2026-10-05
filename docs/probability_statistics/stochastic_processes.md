---
title: 随机过程
tags: [概率与统计, 随机过程]
---

# 随机过程

> 随机过程（stochastic process）是一族按时间或空间索引的随机变量 $\{X_t:t\in T\}$，用来描述随时间随机演化的系统。

## Bernoulli 与 Poisson 过程

Bernoulli 过程由独立的成功/失败试验组成。Poisson 过程 $N(t)$ 满足独立平稳增量，且

$$N(t)\sim\operatorname{Poisson}(\lambda t).$$

相邻到达时间独立且服从参数为 $\lambda$ 的指数分布；其无记忆性对应“从现在重新开始”。

## Markov 链

离散时间 Markov 链满足 Markov 性质：给定现在，未来与过去条件独立。有限状态链由转移矩阵 $P$ 描述，$n$ 步转移矩阵为 $P^n$。平稳分布（stationary distribution）满足

$$\pi P=\pi.$$

不可约、非周期的有限链会收敛到唯一平稳分布。

## 鞅

适应信息流 $\mathcal F_t$ 的过程若满足

$$E(|X_t|)<\infty,\qquad E[X_{t+1}\mid\mathcal F_t]=X_t,$$

则称为鞅（martingale）。它刻画“公平游戏”，也是随机积分、金融数学和集中不等式的核心语言。

## Brownian 运动

标准 Brownian 运动 $B_t$ 从 $0$ 出发，具有连续路径、独立平稳增量，并且 $B_t-B_s\sim N(0,t-s)$。它是扩散极限和 Itô 随机微积分的基本对象。

## 资料

- [MIT OCW: Random Processes](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/pages/unit-iii/)：Bernoulli、Poisson 与 Markov 链。
- [条件期望](joint_distributions.md)：Markov 性与鞅的语言基础。
