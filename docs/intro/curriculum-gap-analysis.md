---
title: 本科与研究生数学内容对照
tags: [入门, 学习路线, 课程体系]
---

# 本科与研究生数学内容对照

> 本页在 **2026 年 10 月**对照国内外数学专业培养方案，检查 CHMath-wiki 的覆盖范围。它是一份内容建设审计，不是一套适用于所有学校的统一培养方案。

## 对照依据

不同学校对课程的拆分方式不同，但核心结构相当稳定：本科阶段建立分析、代数、几何拓扑与概率计算基础；研究生阶段在这些基础上进入现代分析、高等代数、几何拓扑和专业方向。

本次主要参照：

- [北京大学数学系本科培养方案](https://math.pku.edu.cn/puremath/bkspy/pyfa/index.htm)：以数学分析、高等代数、几何、抽象代数、复变函数、常微分方程和概率论等构成基础；
- [Princeton 数学专业要求](https://www.math.princeton.edu/undergraduate/requirements)：高年级核心覆盖 real analysis、complex analysis、algebra 以及 geometry/topology/discrete mathematics；
- [UC Berkeley 博士预备考试](https://math.berkeley.edu/graduate/phd-program/preliminary-exam)：用 calculus、real analysis、complex analysis、linear algebra 和 abstract algebra 检查本科基础；
- [MIT 数学专业方向路线](https://math.mit.edu/academics/undergrad/roadmaps.html)：除纯数学主线外，还系统列出 probability、statistics、computation 和应用方向；
- [University of Chicago 研究生一年级课程](https://math.uchicago.edu/graduate2/first-year-courses/)：覆盖测度与泛函分析、复分析、代数拓扑、微分拓扑、微分几何、表示论、交换代数与代数几何；
- [复旦大学数学研究生培养方向](https://math.fudan.edu.cn/f4/f8/c30376a324856/page.htm)：将培养方向概括为基础数学、应用数学、计算数学、概率统计、运筹与控制。

这里使用三个状态：

- **已有体系**：有连续的基础页面，足以形成第一轮学习路线；
- **有入口，需深化**：已有定义或概览，但还不能代替一门完整课程；
- **缺独立专题**：只有零散提及，或者完全没有专页。

## 本科数学核心对照

| 课程领域 | 当前状态 | 已有内容 | 确实需要补充的主体 |
| --- | --- | --- | --- |
| 微积分与数学分析 | 已有体系 | 极限、微分、Riemann 积分、级数、多元微积分 | 一致收敛、函数项级数、反函数与隐函数定理、向量分析的严格版本 |
| 线性代数 | 有入口，需深化 | 向量空间、线性映射、矩阵、行列式、特征值 | 内积空间、伴随算子、谱定理、Jordan/有理标准形、双线性与二次型 |
| 抽象代数 | 有入口，需深化 | 群、环、域、多项式和 Galois 理论概览 | 群作用与 Sylow 理论的系统应用、模（module）、PID 上有限生成模、域扩张与 Galois 对应的完整课程 |
| 实分析与测度 | 有入口，需深化 | 实数、连续、微分、Riemann 积分、测度与 Lebesgue 积分概览 | $L^p$ 空间、收敛定理、乘积测度、Radon–Nikodym 定理、函数空间中的收敛 |
| 复分析 | 已有主体，需深化 | Cauchy 理论、幂级数、奇点、留数和最大模原理 | 共形映射、正规族、调和函数、亚纯函数与 Riemann 曲面入口 |
| 点集拓扑 | 有入口，需深化 | 拓扑空间、连通性、紧致性 | 基、乘积与商拓扑、可分与可数性公理、分离公理、度量化与完备化 |
| 几何与流形 | 有入口，需深化 | 初等、圆锥曲线、微分几何概览 | 光滑流形、切丛与余切丛、微分形式、Lie 导数、de Rham 理论入口 |
| 常微分方程 | 有概览 | 一阶方程、线性方程、存在唯一性和动力系统入口 | 线性系统、边值问题、相平面、稳定性、分岔与严格存在理论 |
| 偏微分方程 | 缺独立专题 | 在微分方程和数学物理方法中有原型 | 一阶 PDE、Laplace/heat/wave 方程、弱解、能量法、Sobolev 空间入口 |
| 概率论 | 有入口，需深化 | 随机变量、联合分布、条件期望、极限定理 | 概率测度、特征函数、条件期望的测度论版本、大数律与中心极限定理的证明体系 |
| 数理统计 | 有概览 | 估计、检验等入口 | 充分性、完备性、指数族、似然比、渐近理论、Bayesian 统计与回归 |
| 离散数学 | 有入口，需深化 | 组合计数、生成函数、图论、有限自动机 | 组合设计、偏序集、匹配与网络流、概率方法、Ramsey theory、计算复杂性 |
| 数值与计算数学 | 有概览 | 误差、插值、求根、线性系统和 ODE 数值法入口 | 数值线性代数、条件数、稳定性、有限差分/有限元、迭代法与科学计算实践 |
| 优化与运筹 | 有概览 | 凸性、KKT、对偶和基本算法 | 线性/整数规划、网络优化、非线性优化、随机优化、排队论与决策模型 |

本科层面最需要优先处理的不是再增加宽泛概览，而是把表中“有入口，需深化”的课程补成连续章节。其中 **高等线性代数、抽象代数 II、点集拓扑、ODE/PDE、测度概率和数值线性代数** 是连接本科与研究生内容的关键瓶颈。

## 研究生基础与方向对照

研究生课程没有唯一清单。下表把多数纯数学博士项目的一年级基础与应用数学常见主干合并，避免把某一学校的方向设置误当成统一标准。

| 研究生领域 | 当前状态 | 建议建立的核心专题 |
| --- | --- | --- |
| 现代分析 | 有概览，深度不足 | $L^p$ 与 Banach/Hilbert 空间、弱拓扑、紧算子、谱理论、分布与 Sobolev 空间 |
| 调和分析（harmonic analysis） | 缺独立专题 | Fourier 级数与变换、卷积、最大函数、奇异积分、Littlewood–Paley 理论入口 |
| 偏微分方程（PDE） | 缺独立专题 | 弱解、能量估计、椭圆/抛物/双曲方程、正则性和变分方法 |
| 交换代数（commutative algebra） | 缺独立专题 | Noether 环、局部化、整扩张、维数、primary decomposition、同调方法入口 |
| 表示论与 Lie 理论 | 缺独立专题 | 有限群表示、特征标、Lie 群与 Lie 代数、最高权理论入口 |
| 同调代数（homological algebra） | 缺独立专题 | chain complex、函子、Ext/Tor、导出函子与谱序列入口 |
| 代数几何（algebraic geometry） | 缺基础专题 | affine/projective varieties、scheme、sheaf、divisor、cohomology 的学习阶梯 |
| 代数拓扑 | 只有概览 | 基本群与覆盖空间、singular/cellular homology、cohomology、纤维丛与特征类 |
| 微分拓扑 | 缺独立专题 | Sard 定理、横截性、映射度、Morse 理论、向量丛、de Rham theorem |
| 微分与 Riemann 几何 | 只有概览 | connection、curvature、Jacobi field、完备性、Gauss–Bonnet 与几何分析入口 |
| 代数数论 | 缺独立专题 | 数域、整数环、理想分解、赋值与局部域、类群、单位定理 |
| 解析数论 | 缺独立专题 | Dirichlet 级数、素数定理、角色与 $L$-函数、筛法和圆法入口 |
| 随机分析 | 缺独立专题 | martingale convergence、Brownian motion、Itô 积分、SDE、Markov semigroup |
| 动力系统与遍历论 | 缺独立专题 | flow/map、稳定性、分岔、symbolic dynamics、ergodic theorem 与熵 |
| 数学逻辑四支柱 | 部分覆盖 | 在证明论与集合论之外补模型论（model theory）和可计算性理论（computability theory） |
| 控制、博弈与信息 | 缺独立专题 | 最优控制、可控性、动态博弈、信息论、编码与率失真 |
| 反问题与科学计算 | 缺独立专题 | ill-posedness、regularization、数值 PDE、inverse problems 与 uncertainty quantification |

前沿栏目中的 arithmetic geometry、geometric analysis 或 formal AI 不能代替这些基础课程。例如在学习 prismatic cohomology 之前，需要交换代数和代数几何；在学习 SPDE 之前，需要测度概率、泛函分析、PDE 与随机分析。

## 建设优先级

### P0：补齐本科到研究生的断层

1. **高等线性代数**：内积、谱定理、标准形和二次型；
2. **抽象代数 II**：模、域扩张、Galois 理论和交换环基础；
3. **点集拓扑与代数拓扑基础**：商空间、基本群、覆盖空间和同调；
4. **ODE、PDE 与 Fourier 分析**：从经典解过渡到弱解和谱方法；
5. **测度概率与数理统计**：补足定理条件、证明和统计推断体系；
6. **数值线性代数与数值 PDE**：使应用数学形成可计算的完整链条。

### P1：建立研究生共同语言

1. 交换代数、表示论与 Lie 理论；
2. 光滑流形、微分拓扑和 Riemann 几何；
3. 调和分析、泛函分析深化和 PDE；
4. 代数数论、解析数论；
5. 随机分析、动力系统与遍历论；
6. 模型论、可计算性理论。

### P2：形成专业方向

- 代数几何、同调代数与更高范畴；
- 几何分析、辛几何（symplectic geometry）与几何测度论；
- 算子代数、随机 PDE 与数学物理；
- 控制论、博弈论、信息论、运筹学与反问题；
- 组合优化、极值/概率组合和理论计算机科学；
- 生物数学、金融数学、密码学和 scientific machine learning。

P2 并不表示价值较低，而是这些专题依赖 P0/P1 的语言。按这个顺序建设，读者才能从本科基础连续进入研究生与前沿内容。

## 对当前站点的结论

本站已经覆盖本科数学的主要门类，也建立了若干研究前沿入口；缺口集中在两处：

1. **已有页面过于概览**：代数拓扑、微分方程、泛函分析、概率统计、数值分析和优化还不足以构成完整课程；
2. **研究生主干缺页**：交换代数、表示论、Lie 理论、同调代数、代数几何、微分拓扑、PDE、调和分析、代数/解析数论、随机分析和遍历论尚未形成专题。

因此，后续建设应先补 P0 的课程链，再沿 P1 建立研究生共同基础；前沿专题则与对应基础页双向链接。
