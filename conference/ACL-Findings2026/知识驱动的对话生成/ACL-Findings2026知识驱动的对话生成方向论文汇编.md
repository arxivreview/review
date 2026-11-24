# ACL-Findings2026 · 知识驱动的对话生成方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Decomposed Prompting Does Not Fix Knowledge Gaps, But Helps Models Say “I Don’t Know ｜分歧即弃权：闭卷问答中的推理一致性审计

研究机构：美国亚利桑那州立大学、美国宾夕法尼亚大学

作者：Dhruv Madhwal、Lyuxin David Zhang、Dan Roth 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_036e313fe917)

> 闭卷多跳问答要求模型在无外部检索条件下回答事实性问题，但模型常因内部知识缺失产生自信幻觉。现有不确定性估计方法依赖自报告置信度或多次采样，前者不可靠，后者计算开销大且无法区分“稳定错误”与“随机幻觉”。本文切入点在于利用语义等价的不同提示路径（直接回答 vs 分解回答）之间的输出分歧作为可靠性信号。具体做法是提出分歧弃权（Disagreement-Based Abstention, DBA），当直接回答与分解回答语义不一致时触发弃权。该方法无需训练或检索，在前沿模型上显著提升了错误检测的F1与AUROC，但其有效性高度依赖模型规模，且无法捕获跨路径一致的错误。

】

---

【Frame of Reference: Addressing the Challenges of Common Ground Representation in Situational Dialogs ｜情境对话中的共同基础表示与关系性指代解析

研究机构：美国卡内基梅隆大学

作者：Biswesh Mohapatra、Théo Charlot、Giovanni Duca 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09365)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09365)

> 具身情境对话要求系统在长时程内维护共享的空间、时间及实体关系，以支持后续指代消解，但现有大语言模型（LLM）常陷入“接地幻觉”，即表面确认理解却无法在后续轮次中有效调用该信息。本文切入点在于将“关系性指代”的解析能力作为衡量共同基础（Common Ground）持久性的核心指标，并构建了IndiRef基准。通过本体论结构化表示与基于合成数据的强化学习（GRPO）训练，本文验证了外部结构化记忆对提升多跳推理准确性的必要性。该工作填补了具身对话中复杂指代消解的评估空白，但其方法在跨数据集泛化性上仍显脆弱。

】

---

【Structured Dialogue Refinement: Building Retrieval-Augmented Question Answering on Goal-Oriented Dialogues ｜结构化对话精炼

研究机构：英国伦敦大学学院

作者：Bin Wu、Sawan Kumar、Prasetya Ajie Utama 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f0e9727b8242)

> 目标导向对话（Goal-Oriented Dialogue, GOD）中，用户与助手间的共同基础错位导致问题线索稀疏、分散且动态演化，使得标准检索增强生成（RAG）在检索与生成两端均失效。现有文档导向的RAG假设证据显式且局部连贯，无法处理对话中增量揭示的信息结构。本文提出结构化对话精炼（Structured Dialogue Refinement, SDR），通过离线预处理将对话转化为意图对齐的双视角索引与问题-解决方案有向图，在不改变RAG架构的前提下提升问答性能。该方法在Ubuntu语料上显著缩小了检索覆盖缺口，但图构建对LLM分割质量的依赖及单一数据集的验证范围，限制了其通用性结论。

】

---

【The PROPER Approach to Proactivity: Benchmarking and Advancing Knowledge Gap Navigation ｜主动式代理中的知识缺口导航

研究机构：美国华盛顿大学

作者：Kirandeep Kaur、Vinayak Gupta、Aditya Gupta 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09926)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09926)

> 现有主动式对话系统往往陷入“过度提问”或“盲目推测”的困境，无法精准识别用户未表达的认知盲区。本文提出 PROPER 框架，将主动协助形式化为对“未知未知”维度的校准激活问题，通过解耦维度生成与响应生成，在预算约束下选择性填补用户知识缺口。该框架在医疗等高风险领域显著提升了任务效用，但在结构化编码任务中增益有限，且其依赖的静态维度分布能否适应动态变化的用户认知状态尚存疑问。

】
