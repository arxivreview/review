# ACL-Findings2026 · 大语言模型的低位量化方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation ｜大规模SFT模型增量参数压缩

研究机构：哈尔滨工业大学、香港理工大学

作者：Junlin Li、Shuangyong Song、Guodong Du 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16940)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16940)

> 多模型部署场景下，存储全量微调模型导致内存开销呈线性增长，增量压缩旨在仅存储基座模型与压缩后的差值（Delta）以解决此问题。现有方法在处理大规模数据微调产生的高幅度Delta参数时，因量化误差与低秩近似误差随数值尺度放大而失效。本文提出D-QRELO，通过先进行1-bit量化缩小残差数值范围，再对残差执行SVD低秩近似，实现训练与数据无关的压缩。该方法在强SFT模型上显著优于基线，但其压缩率存在物理下限，且对早期层敏感性的处理尚未完全解决。

】

---

【FAQ: Mitigating Quantization Error via Regenerating Calibration Data with Family-Aware Quantization ｜家族感知量化校准

研究机构：中国科学院

作者：Haiyang Xiao、Weiqing Li、Jinyue Guo 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11200)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11200)

> 大语言模型（LLM）部署中，训练后量化（PTQ）的精度瓶颈常被归因于权重或激活的离群值，但校准数据与目标模型激活分布的失配这一数据源问题长期被算法优化所掩盖。现有PTQ方法通过二阶补偿或旋转缩放重塑分布，却默认静态校准集能代表推理时的复杂激活模式，导致量化参数偏差。本文提出FAQ框架，利用同族大模型重生成校准数据，从源头平滑激活分布。该策略在INT4量化下将精度损失降低28.5%，但其有效性高度依赖模型家族内部的激活一致性，跨家族泛化能力存疑。

】

---

【From Signal Degradation to Computation Collapse: Uncovering the Two Failure Modes of LLM Quantization ｜量化失效的机制诊断：信号退化与计算崩塌

研究机构：中国科学院大学、中国科学院

作者：Chenxi Zhou、Pengfei Cao、Jiang Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19884)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19884)

> 大语言模型（LLM）低比特量化在2-bit区间常出现性能断崖，但现有研究多将其视为数值误差的累积，缺乏对内部机制失效的系统解释。本文切入点在于区分“信号退化”与“计算崩塌”两种定性不同的失效模式，通过因果追踪与表征拓扑分析揭示其本质差异。实验证明4-bit失效可通过无训练策略修复，而2-bit失效需结构重建。该框架提供了量化失效的诊断基础，但其结论是否适用于旋转类量化方法尚存疑。

】

---

【pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training ｜pQuant：解耦线性量化感知训练

研究机构：北京大学、复旦大学

作者：Wenzheng Zhang、Bingzheng Liu、Yang Hu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22592)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22592)

> 极低位大语言模型（LLM）在从随机初始化进行量化感知训练（QAT-Scratch）时，面临精度停滞与扩展性失效的双重瓶颈。现有1-bit模型因权重敏感度均匀化导致表达力受限，无法有效区分关键参数。本文提出pQuant，通过解耦线性层将敏感权重隔离至高精度分支，并利用特征缩放引导模型动态分配重要性。该方法在1.3B规模下以1.35-bit精度逼近2-bit模型性能，但仅验证至2.6B规模，其在大模型上的泛化能力存疑。

】
