# ACL-Findings2026 · 基于对比方法的句子嵌入学习方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【SemPA: Improving Sentence Embeddings of Large Language Models through Semantic Preference Alignment ｜语义偏好对齐

研究机构：深圳大学

作者：Ziyang Chen、Zhenxuan Huang、Yile Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d8ad570de534)

> 句子嵌入学习旨在将变长文本映射为固定维度稠密向量，以支撑语义相似度评估与信息检索等下游任务，其核心价值在于弥合离散符号与连续语义空间之间的鸿沟。现有基于大语言模型（LLM）的嵌入方法面临两难：提示工程法性能受限，架构修改法往往牺牲生成能力。本文切入点在于利用直接偏好优化（DPO）在改写任务上微调LLM，使其在保留生成能力的前提下提升语义区分度。该方法通过轻量级参数更新实现句级偏好对齐，理论上统一了对比学习与DPO的优化目标。其价值在于提供了一种不破坏模型内部计算机制的嵌入增强路径，但其在大规模检索基准上的泛化能力仍存疑。

】

---

【Uncertainty-Aware Contrastive Sentence Embedding With Local Context Representation for Text Classification ｜不确定性感知对比句嵌入

研究机构：深圳大学

作者：Han Liu、Jiaqing Zhan、Zhichao Chen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa8503eb9017)

> 句子嵌入学习旨在将变长文本映射为固定维度稠密向量，以支撑语义相似度评估与信息检索等下游任务，其核心价值在于弥合离散符号与连续语义空间之间的鸿沟。现有基于大语言模型（LLM）的嵌入方法多采用确定性输出，难以区分语义清晰与模糊文本，导致模型在歧义样本上过拟合。本文切入点在于引入不确定性量化机制，通过高斯分布建模表示方差，并结合标签驱动对比学习优化分类几何结构。该方法冻结骨干网络，仅训练轻量级局部上下文提取模块，在文本分类任务上实现了小模型超越大模型的效果，但其对检索任务及生成能力保留的适用性尚存疑。

】
