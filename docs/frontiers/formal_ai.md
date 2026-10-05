---
title: 形式化数学与 AI
tags: [前沿数学, 类型论, 形式化证明]
---

# 形式化数学与 AI

## 从可读证明到机器可检验证明

证明助理（proof assistant）把定义、定理和证明编码在形式系统中，由很小的 trusted kernel 检查每一步。Lean、Coq、Isabelle 和 Agda 使用不同的逻辑与类型论基础。

形式化的价值不仅是“查错”。大型库把数学知识变成可组合的软件接口，使定义依赖、定理复用和重构都可被工具管理。代价是必须显式处理许多人类论文省略的条件、强制转换和低层引理。

## 大型形式化工程

代表性项目包括 Four Color Theorem、Feit–Thompson odd order theorem、Kepler conjecture 的 Flyspeck，以及 Liquid Tensor Experiment。后者围绕 condensed mathematics 中的定理展开，展示了研究级新数学也能与 Lean 社区并行形式化。

mathlib 已形成覆盖代数、分析、拓扑、概率和数论的大型 Lean 库。前沿问题包括库结构、自动化、数学知识检索、跨证明助理互操作和长期维护。

## AI theorem proving

机器学习可用于选择引理、生成 tactic、翻译自然语言陈述和搜索证明。形式语言的优势是候选证明能被 kernel 确定性验证；难点是搜索空间巨大，且高质量形式化训练数据远少于自然语言文本。

AlphaProof 在 2024 年 IMO 题目上结合 Lean 与 reinforcement learning，并与 AlphaGeometry 2 合计解决 6 题中的 4 题，达到银牌分数。Google DeepMind 随后报告 2025 年系统达到 IMO 金牌水平；这些是竞赛数学的重要进展，但不能直接推出系统已经能够独立完成一般研究数学。

## 当前研究方向

- autoformalization：把自然语言定义和证明可靠翻译成形式语言；
- premise selection：从大型库选择相关定理；
- proof search：结合符号搜索、语言模型和强化学习；
- conjecture generation：提出有意义且可验证的新猜想；
- human–AI collaboration：让系统承担检索、计算和局部证明，同时保留研究者对概念与目标的判断；
- benchmark design：避免数据污染，并衡量超出已有题库的真实能力。

## 应保持的区分

形式验证只保证“给定形式陈述的证明通过了指定 kernel”，不自动保证形式陈述准确表达原问题。AI 找到一个证明也不等于它理解了证明的动机、推广方向或数学价值。

## 资料

- [Lean theorem prover](https://lean-lang.org/)
- [mathlib](https://mathlib.org/)
- [DeepMind: AlphaProof and AlphaGeometry 2](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)
- [DeepMind: 2025 IMO 与后续数学研究系统](https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think/)
- [形式化 Nöbeling 定理与 condensed mathematics](https://arxiv.org/abs/2309.07252)
- [类型论](../foundations/type_theory/index.md)与[证明论](../foundations/logic/proof_theory.md)
