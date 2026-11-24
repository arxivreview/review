# ACL-Findings2026 · 知识蒸馏方法与理论方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Stable On-Policy Distillation through Adaptive Target Reformulation ｜稳定在线策略蒸馏的目标重构

研究机构：韩国首尔大学

作者：Ijun Jang、Jewon Yeom、Juan Yeo 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07155)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07155)

> 在线策略蒸馏（On-Policy Distillation, OPD）旨在通过让学生模型在自身生成的轨迹上学习，解决传统监督蒸馏中训练与推理分布不匹配导致的暴露偏差。然而，早期学生策略的高噪声特性使得直接匹配教师分布时，前向KL散度引发梯度爆炸，反向KL散度则导致模式坍塌，现有数据层面的混合策略未能解决优化目标本身的几何不稳定性。本文提出Veto，通过在Logit空间构建师生分布的几何插值目标，以单一参数$\beta$统一调控梯度抑制与多样性保留。该方法在低资源设定下显著提升了数学推理与代码生成性能，但其对超参数$\beta$的敏感性及小数据规模下的泛化能力仍存疑。

】
