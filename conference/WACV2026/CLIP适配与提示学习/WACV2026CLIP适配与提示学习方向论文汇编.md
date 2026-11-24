# WACV2026 · CLIP适配与提示学习方向论文汇编

> 本方向共 2 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CLIP's Visual Embedding Projector is a Few-shot Cornucopia ｜正则化线性投影适配

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_af3d0e8049aa)

> 大规模视觉-语言模型在少样本适配中常因超参数敏感与验证集依赖而失效，导致模型难以在缺乏调参资源时保持稳健。现有提示学习与适配器方法虽能提升精度，但往往引入复杂的架构搜索或依赖外部参数，限制了其在通用场景下的部署。ProLIP 通过仅微调视觉编码器的投影矩阵并引入基于样本量的动态 Frobenius 范数正则化，实现了无需验证集的稳定适配。该方法在验证集缺失设定下提供了比传统适配器更鲁棒的基线，但其绝对精度未超越 2025 年后的最新 SOTA，且对极端少样本下的新颖类泛化能力缺乏深入探讨。

】

---

【Zero-Shot Domain Generalisation via Prompt-Driven Feature Refinement ｜提示驱动特征精炼实现零样本域泛化

研究机构：新西兰奥克兰大学

作者：Tingrui Qiao、Di Zhao、Caroline Walker 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f576ede84660)

> 域泛化旨在让模型从源域泛化至未见目标域，但现有方法多依赖源域数据或额外训练，在隐私受限或数据不可得场景下失效。Prefer 提出零样本域泛化（Zero-Shot Domain Generalisation, ZSDG）设定，彻底移除源数据、目标数据及训练环节。该方法利用大语言模型生成域特定提示，通过计算特征通道的相似度与方差筛选鲁棒通道，在推理时实现特征精炼。这一“无训练”策略在标准基准上超越了现有源自由方法，但其性能上限仍低于依赖源域微调的强基线，且对 LLM 生成提示的质量依赖尚未被充分量化。

】
