# ACL-Findings2026 · AI驱动的平面图与布局生成方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Generative Floor Plan Design with LLMs via Reinforcement Learning with Verifiable Rewards ｜基于可验证奖励强化学习的LLM平面图生成

研究机构：加拿大蒙特利尔大学

作者：Luis Lara、Aristides Milios、Zhi Hao Luo 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14117)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14117)

> 建筑平面图生成需在满足严格拓扑连通性的同时，精确控制房间尺寸与面积，现有方法多依赖光栅图像或仅关注邻接关系，导致输出难以直接用于CAD且缺乏数值约束控制。本文切入点在于将平面图表示为JSON多边形结构，并引入强化学习以可验证奖励（RLVR）机制，迫使大语言模型（LLM）在生成过程中显式消除重叠并满足面积约束。通过两阶段微调Llama-3.3-70B-Instruct，该方法在八房间任务上将拓扑兼容性误差降低94%，证明了结构化数据到结构化数据生成范式在硬约束满足上的可行性，但其推理成本与单层住宅数据的局限性仍存疑。

】
