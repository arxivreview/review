# WACV2026 · 低比特Transformer与视觉Transformer量化方向论文汇编

> 本方向共 2 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Universal Self-Attention Enhancement for Bridging Low-bit Quantization and Vision Transformers ｜量化感知多头自注意力增强

研究机构：中国科学院、中国科学院大学

作者：Jiahe Qian、Peisong Wang、Zhengyang Zhuge 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2dc9afde6c8)

> 低比特量化下的视觉Transformer（ViT）常因多头自注意力（MHSA）模块的分布特性而精度骤降。现有全局平滑或旋转方法难以精准处理注意力图内部稀疏的高幅值长尾分布及量化引发的头间表征发散。本文提出Q-MHSA模块，通过跨头融合与可学习平滑控制器在训练阶段直接修正MHSA内部数据分布。该方案在极低比特下显著提升了ViT的量化鲁棒性，但其效果高度依赖量化感知训练（QAT）流程，且未验证在纯后训练量化（PTQ）场景下的泛化能力。

】

---

【IPTQ-ViT: Post-Training Quantization of Non-linear Functions for Integer-only Vision Transformers ｜视觉Transformer非线性算子的整数化后训练量化

研究机构：韩国电子通信研究院

作者：Gihwan Kim、Jemin Lee、Hyungshin Kim

论文原文见 [arXiv](https://arxiv.org/abs/2511.15369)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.15369)

> 视觉Transformer（ViT）部署的核心瓶颈在于Softmax、GELU等非线性算子无法直接映射至整数域，导致现有训练后量化（PTQ）方法要么保留浮点运算，要么因近似误差导致精度崩塌。本文切入点在于发现量化感知训练（QAT）中设计的近似函数在PTQ场景下因缺乏重训练补偿而失效，进而提出针对视觉数据分布优化的近似函数与逐层分配机制。通过构建融合敏感度、扰动与计算成本的统一度量，IPTQ-ViT实现了无需重训练的全整数推理。该方法在W8A8下接近全精度，但在极低比特下的泛化能力仍存疑。

】
