# ICASSP2026 · 深度学习语音增强方向论文汇编

> 本方向共 1 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DAT-CFTNet: Speech Enhancement for Cochlear Implant Recipients using Attention-based Dual-Path Recurrent Neural Network ｜双路径注意力复数频率变换网络

作者：Nursadul Mamun、John H. L. Hansen

论文原文见 [arXiv](https://arxiv.org/abs/2604.06744)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06744)

> 人工耳蜗（CI）接收者仅能恢复约10%的时频内容，传统语音增强（SE）算法在低信噪比下易导致语音失真或过度抑制，难以平衡噪声抑制与可懂度保留。现有复数域网络虽能建模相位，但瓶颈层RNN对长序列依赖建模不足，导致频谱细节恢复受限。本文在CFTNet瓶颈层引入双路径注意力RNN（DAT-RNN），通过Intra/Inter-chunk RNN与动态因果注意力协同优化时频掩码生成。该架构在IEEE数据集上显著提升了STOI与PESQ，但缺乏通用基准验证，其增益是否源于CI特定感知特性仍存疑。

】
