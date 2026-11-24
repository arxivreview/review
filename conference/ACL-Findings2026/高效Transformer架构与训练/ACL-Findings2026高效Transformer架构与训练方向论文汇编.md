# ACL-Findings2026 · 高效Transformer架构与训练方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Do Transformers Grok Succinct Algorithms? Mechanistic Evidence for Counting Circuits ｜简洁性假设下的Transformer算法发现机制

作者：Yizheng Zhao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3b0ae634621f)

> 现有理论认为固定精度Transformer能以多项式参数表示指数状态空间，但梯度训练常陷入启发式捷径而非收敛至理论预测的简洁电路。本文通过LARGECOUNTER任务验证这一“表达力-可学习性”鸿沟，发现高权重衰减诱导的Grokking相变是模型放弃记忆、发现算法电路的关键。实验证实2层Transformer完美泛化而LSTM彻底失败，但结论局限于合成计数任务，其在自然语言复杂推理中的普适性仍存疑。

】

---

【Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity ｜工作记忆约束下的Transformer归纳偏置

研究机构：英国艾伦·图灵研究所

作者：Pranava Madhyastha、Dagmar Adamcova

论文原文见 [arXiv](https://arxiv.org/abs/2604.20789)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20789)

> 高效Transformer架构研究长期聚焦于算力与参数预算下的效率优化，但忽视了模型内部表征与人类认知机制的结构性错位。现有线性注意力或混合架构虽降低了计算复杂度，却未解决小数据场景下语法表征学习低效及心理语言学对齐度不足的问题。本文切入点在于将人类工作记忆（Working Memory, WM）的容量限制与衰减特性直接编码为注意力机制的硬约束，通过从头训练验证其作为归纳偏置的有效性。该方法在10M词数据规模下显著提升了BLiMP语法准确率，但在100M词规模下优势收窄，且未报告计算效率指标，其“认知效率”与“计算效率”的权衡关系尚存疑。

】

---

【清华等团队提出零令牌Transformer：解耦首尾层并引入虚拟零令牌，实现自适应早期退出

研究机构：清华大学、南方科技大学

作者：Guanghao Li、Wenhao Jiang、Li Shen 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9c6eb8902b0e)

> 在固定参数预算下提升大语言模型（LLM）的推理深度，是突破算力限制的关键路径。现有参数循环方法往往强制所有层共享权重，导致功能冲突且缺乏动态停止机制，难以平衡计算效率与精度。本文提出零令牌Transformer（Zero Token Transformer, ZTT），通过解耦首尾层并引入虚拟零令牌作为注意力控制信号，实现自适应早期退出。该架构在60M至7B参数规模上验证了有效性，但其优势是否随模型规模扩大而衰减，以及零令牌阈值在不同任务间的迁移性，仍存疑。

】

---

【科学院团队新研究：Sparse Growing Transformer: Training-Time Sparse Depth Allocation via Progressive Attention Looping

研究机构：中国科学院、中国科学院大学

作者：Yao Chen、Yilong Chen、Yinqi Yang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6db3261f249a)

> 大语言模型在扩展深度以提升推理能力时，面临参数规模与计算成本的同步膨胀，而现有递归架构采用静态拓扑与块级复用，导致训练阶段产生大量冗余计算。本文指出，深度分配不应是预设的静态结构，而应是随训练进程动态生长的稀疏过程。通过引入注意力熵作为结构生长信号，SGT实现了从深层到浅层的渐进式头级递归，将额外训练FLOPs开销从16-20%压缩至1-3%。该方法在中小规模模型上验证了效率-性能权衡的显著优势，但其熵值信号在超大规模或长序列下的鲁棒性仍存疑。

】
