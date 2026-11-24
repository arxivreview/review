# WACV2026 · AI生成视频评估与编辑方向论文汇编

> 本方向共 2 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GeneVA: A Dataset of Human Annotations for Generative Text to Video Artifacts ｜生成视频时空伪影人工标注数据集

研究机构：美国纽约大学

作者：Jenna Kang、Maria Silva、Patsorn Sangkloy 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.08818)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.08818)

> 扩散模型生成的视频常出现物理违背与时序断裂，但现有评估指标无法定位具体缺陷。本文通过众包收集带时空边界框与文本描述的伪影标注，构建了首个视频伪影定位基准。其价值在于提供了细粒度数据基础设施，但检测器性能有限，且标注协议存在覆盖盲区。

】

---

【Training-free Detection of Text-to-video Generations via Over-coherence ｜基于时间过度连贯性的无训练文本到视频生成检测

作者：Jonathan Brokman、Oren Rachmil、Omer Hofman 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_59d0e065eebd)

> 文本到视频（Text-to-Video, T2V）生成模型日益逼真，导致现有依赖监督学习的检测器在面对未见过的生成器时泛化能力骤降，陷入“盲测失效”困境。本文指出视频生成模型为维持时序平滑而过度约束帧间变化，产生非自然的“时间过度连贯性”，这一物理特性是区分真伪的关键信号。通过冻结CLIP编码器计算相邻帧嵌入的余弦相似度极值，构建自适应标量判据，实现了无需任何生成数据训练的盲测检测。该方法在54.4K视频数据集上平均AUC提升10.6%，但仅依赖时间维度，对空间伪影显著的生成器可能存在盲区。

】
