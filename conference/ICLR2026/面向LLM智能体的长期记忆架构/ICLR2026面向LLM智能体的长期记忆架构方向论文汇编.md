# ICLR2026 · 面向LLM智能体的长期记忆架构方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Embodied Agents Meet Personalization: Investigating Challenges and Solutions through the Lens of Memory Utilization ｜具身智能体个性化记忆利用评估框架

研究机构：韩国延世大学、美国德州农工大学

作者：Taeyoon Kwon、Dongwook Choi、Hyojun Kim 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2505.16348)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_96646082)

> 具身智能体在执行个性化辅助任务时，面临无法将历史交互中的用户特定知识（如“最爱的杯子”）有效转化为当前动作规划的问题。现有评估基准多聚焦于静态指令跟随，缺乏对动态记忆利用能力的量化手段，导致无法区分智能体是真正利用了记忆还是依赖参数化常识。本文构建了MEMENTO两阶段评估框架，通过对比指令明确与指令模糊场景下的性能差异，量化记忆效用，并设计分层知识图谱用户画像模块以解决多记忆协调失败问题。该工作揭示了当前LLM智能体在具身个性化任务中的记忆瓶颈，但受限于单一场景与特定检索策略，其结论在复杂动态环境中的泛化性尚存疑。

】

---

【FROM SINGLE TO MULTI-GRANULARITY: TOWARD LONG-TERM MEMORY ASSOCIATION AND SELECTION OF CONVERSATIONAL AGENTS ｜多粒度记忆关联与自适应选择

研究机构：中国科学技术大学、香港城市大学

作者：Derong Xu、Yi Wen、Pengyue Jia 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_93827102)

> 长期对话智能体面临上下文窗口限制导致的跨会话状态丢失，现有检索增强生成（RAG）方法依赖单一粒度记忆切分，无法捕捉跨会话的深层语义关联，导致部分检索或噪声干扰。MemGAS 通过构建会话、轮次、关键词、摘要四级记忆单元，利用高斯混合模型（GMM）建立跨粒度关联图，并引入基于熵的路由器动态选择最优检索粒度。该方法在四个基准上优于单粒度及固定结构基线，但其性能提升主要源于检索策略优化，而非记忆内容的根本性重构，且缺乏对记忆遗忘机制的探讨。

】
