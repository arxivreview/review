# AAAI2026 · 高效视觉Transformer压缩与加速方向论文汇编

> 本方向共 2 篇（AAAI2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Steering Sparse Autoencoder Latents to Control Dynamic Head Pruning in Vision Transformers (Student Abstract) ｜稀疏自编码器引导的动态头剪枝

研究机构：韩国科学技术院

作者：Yousung Lee、Dongsoo Har

论文原文见 [arXiv](https://arxiv.org/abs/2603.26743)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26743)

> 视觉Transformer（ViT）中冗余注意力头的动态剪枝虽能降低计算量，但决策过程依赖残差嵌入，缺乏潜空间层面的可解释性与可控性。现有框架如AdaViT仅输出黑盒掩码，无法解释为何特定输入触发特定头的保留。本文切入点在于引入稀疏自编码器（Sparse Autoencoder, SAE）解耦残差嵌入，通过放大类特定潜变量来引导剪枝决策。该方法在CIFAR-100上验证了潜空间引导能揭示类特异性头子集，但受限于小数据集与单层实验，其通用性存疑。

】

---

【Stratified Knowledge-Density Super-Network for Scalable Vision Transformers ｜分层知识密度超网络

研究机构：东南大学

作者：Longhua Li、Lei Qi、Xin Geng

论文原文见 [arXiv](https://arxiv.org/abs/2511.11683)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11683)

> 视觉Transformer（ViT）部署面临资源约束多样性，传统多模型训练或静态剪枝难以兼顾灵活性与精度。现有弹性网络依赖手动扩展规则，导致小模型知识保留不足。本文提出分层知识密度超网络，通过加权主成分分析（WPAC）与渐进重要性感知Dropout（PIAD）实现任意尺寸子网的O(1)成本提取。该方法在同等压缩比下优于静态剪枝，但依赖30 epoch微调，其“免重训练”优势存疑。

】
