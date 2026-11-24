# ACL2026 · 高效Transformer架构与训练方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【SSA: Improving Performance With a Better Scoring Function ｜缩放符号平均（SSA）：破解Softmax饱和导致的上下文学习泛化失效

作者：Omar Naim、Swarnadeep Bhar、Jerome Bolte 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2508.14685)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_63961aaf5021)

> 上下文学习（In-Context Learning, ICL）旨在让模型在推理时通过提示中的示例即时学习新任务，无需更新参数。然而，当测试数据分布与训练分布存在偏移时，标准Transformer中的Softmax注意力机制会因数值饱和而将权重坍缩至单一Token，导致模型忽略其他关键上下文信息，从而系统性失败。本文指出Softmax饱和是这一失效的架构根源，并提出缩放符号平均（Scaled Signed Averaging, SSA）作为可训练的替代评分函数，通过多项式增长特性抑制权重坍缩。该方案在受控ICL任务及小规模NLP基准上显著优于Softmax，但其在大模型长序列推理中的实际收益及与混合架构的兼容性尚存疑。

】

---

【科学院团队新研究：Polymorphic Universal Transformer

研究机构：中国科学院、中国科学院大学

作者：Yilong Chen、Zitian Gao、Yihao Xiao 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_31bb0ca26272)

> 递归Transformer通过权重共享解耦参数与深度，但静态算子导致表示秩坍缩与计算分布偏斜，限制了深层推理能力。现有方案如UTMoE仅缓解而未根治功能同质性，本文切入点在于引入条件稀疏子空间实现算子动态多态。具体做法是结合SiLU注意力、局部深度卷积与熵引导的深度稀疏调度，在共享参数框架内重构递归动态。该架构在156M规模下显著优于标准UT，但其在更大规模下的泛化能力及与混合架构的竞争力仍存疑。

】
