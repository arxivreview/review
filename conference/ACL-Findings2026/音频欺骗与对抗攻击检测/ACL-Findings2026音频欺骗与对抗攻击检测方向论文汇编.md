# ACL-Findings2026 · 音频欺骗与对抗攻击检测方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【When depth is redundant: Efficient transformer-based speech anti-spoofing ｜浅层对齐Transformer反欺骗检测

研究机构：法国国家科学研究中心

作者：Hoan My Tran、Damien Lolive、Aghilas Sini 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45bfd653a2df)

> 反欺骗检测的核心痛点在于深层Transformer分类器在域外场景下泛化能力不足，且计算开销随深度增加呈二次方增长。现有方法通过增加模型深度或引入复杂后端（如AASIST、MoE）提升域内性能，但往往加剧过拟合并导致浅层特征利用不足。本文切入点在于利用神经坍缩理论揭示的层间表征冗余，提出一种角度距离正则化策略，强制浅层与最终层表征几何对齐。该方法通过2-4层浅层Transformer配合多头部时间潜在注意力机制，在保持域内性能的同时显著提升了域外鲁棒性与推理效率。其价值在于以极低的参数量实现了与深层模型相当的检测性能，但其在复杂信道效应下的长期稳定性及与SASV任务的兼容性尚待验证。

】
