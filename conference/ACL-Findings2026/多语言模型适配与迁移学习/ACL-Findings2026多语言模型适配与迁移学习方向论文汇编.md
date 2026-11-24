# ACL-Findings2026 · 多语言模型适配与迁移学习方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adapting Where It Matters: Depth-Aware Adaptation for Efficient Multilingual Speech Recognition in Low-Resource Languages ｜深度感知模型适配

研究机构：澳大利亚墨尔本大学

作者：Yang Xiao、Eun-Jung Holden、Ting Dang

论文原文见 [arXiv](https://arxiv.org/abs/2602.01008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01008)

> 多语言语音识别（ASR）模型在低资源语言上性能骤降，核心矛盾在于全参数微调导致的灾难性遗忘与计算开销，而现有参数高效微调（PEFT）方法忽略模型内部层级功能差异，导致适应效率低下。本文切入点在于揭示语音基础模型中存在的“U型”层级可塑性模式，即中间层保留语言无关语义，首尾层承载语言特异性特征。通过提出深度感知模型适配（DAMA）框架，结合深度感知秩调度、SVD初始化与基保护投影，实现了对中间层语义空间的严格保护。该方法在极低资源场景下显著优于基线，但其对中间层“冻结”策略在复杂音素变化下的泛化边界尚存疑。

】

---

【Disentangling Continued Pre-Training: Attention-Driven Routing and Semantic Hub Preservation in Language Adaptation ｜持续预训练中的注意力路由与语义枢纽保持机制

作者：Khanh-Tung Tran、Vinh-Khanh Tran、Barry O’Sullivan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bf82e7a97a59)

> 多语言大语言模型在低资源语言适应中面临核心矛盾：全参数更新易导致灾难性遗忘，而冻结主干又阻碍新知识注入。现有研究多聚焦于训练后的参数高效微调或架构隔离，忽视了持续预训练（CPT）过程中内部组件的动态演化机制。本文通过层交换与组件手术实验，揭示CPT通过“接口层”适应新语言分布，同时保持“语义枢纽”层语义不变的选择性适应机制。该工作提供了CPT机制的因果证据，但未验证该机制能否直接转化为更高效的微调策略。

】
