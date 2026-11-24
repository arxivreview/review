# ACL-Findings2026 · 大型语言模型的领域适配方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Balancing Knowledge Breadth and Task Depth for Effective Domain Adaptation Fine-Tuning ｜二维课程学习框架

研究机构：中山大学

作者：Mu Zhang、Yuxiang Chu、Guangya Yu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0a64a8a62ee3)

> 大语言模型在垂直领域微调时，常因灾难性遗忘导致通用能力退化，而现有单维课程学习难以同时兼顾知识广度与任务深度。本文提出一种二维课程学习框架，通过语义聚类与Bloom分类法构建正交的知识-任务排序结构，并配合指数混合调度实现平滑过渡。该方法在医疗与金融基准上取得SOTA，但缺乏与参数解耦方法的同骨干对比，其遗忘缓解效果是否优于架构级方案仍存疑。

】

---

【SParK-Eval: Evaluating Structure-Aware Knowledge Acquisition in LLMs for Domain Adaptation to Industrial Records ｜结构感知参数化知识评估

作者：Ekant Muljibhai Amin、Yuta Koreeda、Yasuhiro Sogawa

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_15084115e976)

> 工业领域适配面临语料规模小且结构非自然（如表格、实体列表）的困境，传统持续预训练（CPT）方法难以区分是领域知识缺失还是数据结构阻碍了学习。现有数据转换方法仅关注下游任务性能，无法量化不同结构对参数化知识获取的具体贡献。SParK-Eval通过从训练数据生成带结构标签的探针查询，并结合输入归一化对照，实现了结构效应的隔离分析。该方法揭示了非自然结构导致的知识获取显著下降，为工业数据预处理提供了诊断工具，但其结论受限于单一私有数据集，跨域泛化性存疑。

】

---

【SplitThenMerge: Token-Level Skill-Compositional Sparse Mixture-of-Experts for Complex Domain-Specific Tasks ｜技能组合式稀疏混合专家

研究机构：浙江大学

作者：Yuting Huang、Jiawen Zhang、Yiquan Wu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_07b772ed6ceb)

> 复杂领域生成任务要求模型在单句内频繁切换结构、推理、数值等异构能力，传统单一目标微调导致技能间梯度干扰与性能瓶颈。现有参数高效微调方法将领域能力视为整体，忽略了Token级的技能交织特性。本文提出SplitThenMerge框架，通过自动标注将领域语料分解为原子技能，独立训练LoRA专家并合并为Token级稀疏MoE模型。该方法在同等参数量下显著优于基线，但缺乏通用能力保持的验证，其技能解耦是否真正规避了灾难性遗忘仍存疑。

】
