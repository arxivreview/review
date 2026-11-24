# Others2026 · 事件视觉与神经形态感知方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Generative Event Pretraining with Foundation Model Alignment ｜生成式事件预训练

研究机构：瑞士苏黎世大学

作者：Jianwen Cao、Jiaxu Xing、Nico Messikommer 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.23032)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23032)

> 事件相机数据因缺乏纹理与大规模标注，导致传统视觉模型难以直接迁移，且现有预训练方法往往忽略其异步时序动态。本文切入点在于将视觉基础模型的语义先验与自回归时序建模解耦为两个独立阶段，先对齐再预测。通过冻结 DINOv2 教师进行特征对齐，随后在混合模态序列上执行因果 Transformer 自回归预训练，实现了语义与时间的联合表征。该方法在仅 24 个预训练 epoch 下超越了多数基线，但其性能仍低于使用状态空间模型（SSM）的最新分割 SOTA，且未验证在神经形态硬件上的部署可行性。

】
