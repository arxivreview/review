# ICASSP2026 · 鲁棒说话人验证与嵌入学习方向论文汇编

> 本方向共 1 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Hyperbolic Additive Margin Softmax with Hierarchical Information for Speaker Verification ｜双曲加性边际Softmax

研究机构：清华大学

作者：Zhihua Fang、Liang He

论文原文见 [arXiv](https://arxiv.org/abs/2601.19709)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19709)

> 说话人验证（Speaker Verification, SV）的核心挑战在于如何从变长语音中提取兼具判别力与泛化性的嵌入，而现有主流方法均基于欧氏空间构建损失函数，难以充分捕捉说话人特征中固有的树状层级结构。本文指出，欧氏空间的扁平几何特性限制了嵌入对复杂声学分布的表达能力，导致类间可分性不足。为此，作者提出将嵌入投影至双曲空间，并设计基于双曲距离的Softmax变体损失，以显式建模层级信息并增强类间分离。该方法在ECAPA-TDNN骨干上验证了双曲几何的有效性，但在缺乏自监督预训练特征的条件下，其绝对性能仍显著落后于当前基于大规模预训练模型的SOTA，其价值更多体现在几何建模的理论贡献而非工程部署的领先性。

】
