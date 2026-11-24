# ICLR2026 · 三维点云Transformer与鲁棒学习方向论文汇编

> 本方向共 1 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【3DSMT: A HYBRID SPIKING MAMBA-TRANSFORMER FOR POINT CLOUD ANALYSIS ｜脉冲混合架构

研究机构：安徽大学、天津大学

作者：zhiming Zhou、Yong He、Qiaoyun Wu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66519055)

> 导读 3D点云分析在边缘设备部署时面临计算能耗与精度的双重约束，传统人工神经网络（ANN）的浮点运算导致能耗过高，而现有脉冲神经网络（SNN）方案在精度上存在显著差距。本文切入点在于将Transformer的局部建模能力与Mamba的全局线性复杂度优势，共同嵌入到SNN的事件驱动框架中，以稀疏脉冲计算替代高能耗的浮点乘累加。具体做法是构建包含脉冲局部偏移注意力与脉冲Mamba块的混合架构。该方案在SNN类别中实现了精度与能效的平衡，但其精度上限仍低于顶级ANN模型，且未验证其在对抗攻击下的鲁棒性。

】
