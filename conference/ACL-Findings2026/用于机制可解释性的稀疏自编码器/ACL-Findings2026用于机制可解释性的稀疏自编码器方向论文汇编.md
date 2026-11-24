# ACL-Findings2026 · 用于机制可解释性的稀疏自编码器方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations ｜自适应TopK稀疏自编码器

研究机构：浙江大学

论文原文见 [arXiv](https://arxiv.org/abs/2508.17320)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2508.17320)

> 导读 稀疏自编码器（Sparse Autoencoder, SAE）旨在将大语言模型（LLM）中叠加的密集激活分解为稀疏、单义的特征，但现有架构普遍采用固定稀疏度约束，导致简单输入过度激活而复杂输入特征不足。本文指出这种“一刀切”的稀疏策略忽视了文本语义复杂度的差异，提出基于线性探针预测复杂度并动态调整激活特征数量的AdaptiveK SAE。该方法通过复杂度驱动的动态稀疏分配，在多个模型规模上实现了优于固定基线的重构保真度与解释方差。尽管在Pareto前沿上表现优异，但缺乏与门控SAE等强基线的直接标量对比，其是否真正超越现有架构上限仍存疑。

】

---

【Towards Understanding the Robustness of Sparse Autoencoders ｜稀疏自编码器作为推理时对抗鲁棒性瓶颈

研究机构：美国弗吉尼亚大学

作者：Ahson Saiyed、Sabrina Sadiekh、Chirag Agarwal

论文原文见 [arXiv](https://arxiv.org/abs/2604.18756)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18756)

> 大语言模型（LLM）易受基于梯度优化的越狱攻击，现有防御多聚焦于输入扰动或解码约束，忽视了内部表示几何结构对攻击优化的影响。本文切入点在于将稀疏自编码器（Sparse Autoencoder, SAE）作为推理时插入的不可微分瓶颈，通过重构残差流改变对抗优化的景观。具体做法是在Transformer中间层插入预训练SAE，保持梯度穿透以隔离表示效应。该研究证实了SAE能显著降低攻击成功率，但其防御效果依赖于稀疏度与层深的精细权衡，且缺乏与随机投影基线的对比，其防御上限存疑。

】
