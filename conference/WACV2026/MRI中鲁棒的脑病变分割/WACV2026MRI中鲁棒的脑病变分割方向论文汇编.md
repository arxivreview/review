# WACV2026 · MRI中鲁棒的脑病变分割方向论文汇编

> 本方向共 1 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Multi-Agent Diffusion Approach for MRI Anomaly Segmentation via Modality-Specific LoRA Specialization ｜多模态MRI无监督异常分割中的LoRA路由与潜频掩码机制

研究机构：阿联酋扎耶德大学

作者：Wafa Al Ghallabi、Muhammad Zaigham Zaheer、Ritesh Thawkar 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a6b6bde83ee2)

> 脑病变无监督异常检测旨在摆脱像素级标注依赖，通过重构健康解剖先验来定位病灶，但现有扩散模型方法在多模态场景下往往需要为每种序列训练独立模型，或依赖配对的跨模态数据，导致计算开销大且泛化受限。本文切入点在于利用参数高效微调与可学习频率正则化，在单一共享骨干上实现模态特异性适配。具体做法是两阶段训练：先全量微调扩散骨干建立共享解剖先验，再冻结骨干仅训练LoRA适配器与潜空间频率掩码。该方法在BraTS2021上以87.8%的Dice系数超越IterMask2，且将可训练参数降低53%，但其性能上限仍显著低于全监督方法，且未验证在极端低对比度病灶上的鲁棒性。

】
