# ACL-Findings2026 · Muon优化器变体与分析方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【HTMuon: Improving Muon via Heavy-Tailed Spectral Correction ｜重尾谱修正优化器

研究机构：美国达特茅斯学院、美国国际计算机科学研究所

作者：Tianyu Pang、Yujie Fang、Zihang Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10067)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10067)

> Muon 优化器通过正交化实现谱均匀化，但其将动量矩阵所有奇异值归一化为 1 的操作抑制了权重矩阵经验谱密度（ESD）的重尾特性，违背了重尾自正则化（HT-SR）理论中“重尾谱与模型质量正相关”的结论，导致泛化性能受限。本文切入点在于识别出正交化对噪声主导方向的过度加权及谱尾部抑制效应，提出 HTMuon 通过奇异值幂次变换恢复重尾性。该方法在 LLaMA 预训练中显著降低困惑度，但 p 值选取缺乏自适应机制，且在小样本视觉任务上未超越基线，其泛化边界尚待厘清。

】
