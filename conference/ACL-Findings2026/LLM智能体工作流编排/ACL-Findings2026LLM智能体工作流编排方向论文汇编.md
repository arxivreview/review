# ACL-Findings2026 · LLM智能体工作流编排方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ComfyFlow: Benchmarking LLMs for AIGC Workflow Generation ｜COMFYFLOW：AIGC工作流生成的基准与后训练范式

研究机构：哈尔滨工业大学、阿里巴巴集团

作者：Zhenran Xu、Yiyu Wang、Yunxin Li 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_575ea5a240f6)

> 导读

】

---

【Do We Always Need Query-Level Workflows? Rethinking Agentic Workflow Generation for Multi-Agent Systems ｜任务级工作流生成的低成本评估框架

研究机构：中国科学院、中国科学院大学

作者：Zixu Wang、Bingbing Xu、Yige Yuan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11147)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11147)

> 多智能体系统（MAS）的工作流生成面临高昂的计算开销，任务级方法需对每个候选工作流执行全量验证集评估，而查询级方法则为每个输入生成独立工作流，两者均存在显著的资源浪费。本文指出，任务级方法中全量执行评估既昂贵又不可靠，且查询级生成并非总是必要。SCALE 框架通过引入“自预测+少样本校准”机制替代全量执行，在保持性能的同时大幅降低 Token 消耗。该研究揭示了现有评估范式的低效性，但其结论是否适用于所有任务分布仍需进一步验证。

】

---

【Evolving Agentic Workflow Driven by Human-Agent Collaboration ｜人机协作驱动的进化式智能体工作流优化

研究机构：上海交通大学、华东师范大学

作者：Yuxin Liu、Jinxuan Zhang、Yuezhang Peng 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c5f50a9c7ff)

> 智能体工作流编排旨在通过协调多个大语言模型（LLM）调用解决长程复杂任务，但现有自动化方法面临高设计成本、搜索低效及对人类偏好适应差三大瓶颈。HFlow 提出一种由人机协作（Human-Agent Collaboration, HAC）引导的进化算法框架，通过交叉与变异操作在结构、提示词与模型骨干构成的搜索空间中生成多样化工作流种群。该方法利用分层经验记忆实现跨任务策略迁移，在数学与代码基准上超越自动基线最高 27.34%，且成本仅为 o1-preview 的四分之一。尽管在绝对性能上未超越当前领域 SOTA，但其将人类偏好显式纳入多目标优化函数的范式为低成本自适应编排提供了新路径，其进化搜索在离散空间中的收敛效率仍存疑。

】
