---
title: 数学与计算机、信息及密码
tags: [交叉学科, 计算机科学, 信息论, 密码学]
---

# 数学与计算机、信息及密码

## 算法与复杂性

算法（algorithm）不仅要输出正确答案，还要评估时间、空间、通信和随机性成本。渐近记号 $O(f(n))$ 给出增长上界；复杂性理论（complexity theory）则按资源限制研究哪些问题可有效计算。

离散数学提供图、组合结构、逻辑和有限域，概率方法分析随机算法，线性代数支撑数值计算和大规模数据处理。连续问题在计算机中还要经过离散化，并分析舍入误差、条件数和稳定性。

## 信息论与编码

离散随机变量的 Shannon entropy 为

$$
H(X)=-\sum_xp(x)\log_2p(x).
$$

它刻画最优无损编码的平均长度尺度。互信息（mutual information）衡量两个随机变量共享的信息；信道容量（channel capacity）给出指定噪声模型下可靠通信率的上限。

纠错码（error-correcting code）在冗余与传输效率之间权衡，连接有限域、线性代数、组合设计和概率。编码定理是渐近结论，不表示任意有限长度码都能达到容量。

## 密码学

现代密码学把安全性写成计算困难性和攻击者能力下的精确定义。RSA 关联整数分解，Diffie–Hellman 与椭圆曲线密码关联离散对数，后量子密码（post-quantum cryptography）则使用格、纠错码和 hash function 等结构。

密码方案的安全不能只凭“底层问题看起来很难”。还要指定安全模型、参数、实现和侧信道。NIST 在 2024 年发布的首批后量子标准包括基于 module lattice 的 ML-KEM、ML-DSA，以及基于 hash 的 SLH-DSA。

## 图、网络与分布式系统

互联网、依赖关系和通信拓扑可建模为图 $G=(V,E)$。最短路、最大流、谱图论和随机图分别回答路由、容量、聚类和鲁棒性问题。分布式系统还需要研究一致性、故障模型、共识和通信复杂度。

网络中的局部规则可能产生全局涌现，但从观测网络推断生成机制通常不是唯一的；抽样偏差也会改变度分布和社群结构。

## 数据、机器学习与形式化方法

统计学习结合函数逼近、优化与概率，数据库和信息检索使用集合、逻辑、索引和随机算法。形式化验证（formal verification）把程序规范写入逻辑系统，由模型检查、SAT/SMT solver 或 proof assistant 检验。

机器学习系统还涉及泛化、鲁棒性、校准和因果识别。高预测准确率不自动意味着解释正确或干预有效。

## 延伸阅读

- [AI 中的数学](../frontiers/mathematics_of_ai.md)与[形式化数学与 AI](../frontiers/formal_ai.md)
- [图论](../discrete_mathematics/graph_theory.md)、[自动机理论](../discrete_mathematics/automata_theory.md)与[数论](../number_theory/index.md)
- [NIST: What Is Post-Quantum Cryptography?](https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography)
- [MIT OCW: Introduction to Network Models](https://ocw.mit.edu/courses/1-022-introduction-to-network-models-fall-2018/pages/syllabus/)
