# Others2026 · 多智能体协调与对手建模方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Probing Dec-POMDP Reasoning in Cooperative MARL ｜合作多智能体强化学习基准的决策过程诊断

研究机构：英国爱丁堡大学、意大利米兰理工大学

作者：Kale-ab Tessera、Leonard Hinckeldey、Riccardo Zamboni 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20804)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20804)

> 合作多智能体强化学习（Cooperative MARL）旨在解决部分可观测马尔可夫决策过程（Dec-POMDP）下的协同决策，但现有基准测试往往仅关注最终回报，掩盖了策略是否真正利用了历史记忆与私有信息。主流算法如 MAPPO 在多个环境中取得高胜率，却可能依赖反应式捷径而非深层推理，导致对智能体能力的评估存在系统性偏差。本文提出一套基于信息论的诊断框架，通过量化历史依赖、私有信息流及动作耦合，审计 37 个标准场景中的策略行为。该工作揭示了当前基准测试的有效性盲区，但受限于仅使用 IPPO/MAPPO 基线，其结论对值分解等复杂策略的普适性存疑。

】
