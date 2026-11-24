# ACL-Findings2026 · 大语言模型训练的优化算法方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection ｜分层零一阶混合优化

研究机构：北京大学

作者：Feihu Jin、Ying Tan

论文原文见 [arXiv](https://arxiv.org/abs/2601.05501)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05501)

> 大语言模型微调面临一阶优化易陷局部极小值与零阶优化在生成任务中因输出空间扩张导致方差爆炸的双重困境。现有纯零阶方法在复杂生成任务中性能崩溃，而纯一阶方法缺乏探索能力，导致泛化受限。本文提出Hi-ZFO，通过基于FLOPs预算的动态规划将参数分层，对高敏感层执行一阶更新，对低敏感层执行零阶扰动，以“有益随机性”平衡精度与探索。该方法在生成与推理任务上超越全参数微调，但受限于静态分区策略，未解决训练过程中参数敏感性的动态演化问题。

】

---

【SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization ｜嵌入层自适应阻尼优化器

作者：Wooin Lee、Hyun-Tae Kim

论文原文见 [arXiv](https://arxiv.org/abs/2604.07663)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07663)

> 大语言模型预训练面临内存墙，传统AdamW优化器需存储与参数量等大的二阶矩状态，导致显存开销翻倍。现有轻量级优化器（如Lion、SinkGD）虽能压缩状态，但在处理嵌入层稀疏且高方差的梯度时稳定性不足，往往被迫回退至AdamW，抵消了内存收益。本文提出SAGE，通过引入一个$O(d)$维度的自适应阻尼器替代静态缩放，在保持单动量状态的前提下稳定嵌入层更新。该设计在1.3B模型上实现了24.33的测试困惑度，优于所有对比基线，但其有效性局限于中小规模模型，且未验证在更大规模或不同数据分布下的泛化能力。

】

---

【Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling ｜自适应层级零阶优化

研究机构：华南理工大学、中山大学

作者：Fei Wang、Li Shen、Liang Ding 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18264)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18264)

> 大语言模型微调中，零阶优化（ZO）虽能消除反向传播的激活内存开销，但全参数均匀扰动导致计算延迟高且梯度估计方差大，严重制约收敛效率。现有改进多聚焦于算法层面的动量或子空间约束，却忽视了扰动生成与参数更新本身带来的线性系统瓶颈及层间敏感度异质性。本文提出AdaLeZO，将层选择建模为非平稳多臂老虎机问题，通过逆概率加权实现稀疏无偏梯度估计。该方法在6.7B至30B模型上实现了1.7至3.0倍的墙钟加速，但其在复杂推理任务上的精度仍略低于一阶方法，且未验证多模态场景下的泛化能力。

】
