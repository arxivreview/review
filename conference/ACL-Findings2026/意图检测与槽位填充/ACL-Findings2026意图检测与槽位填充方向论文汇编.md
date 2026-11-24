# ACL-Findings2026 · 意图检测与槽位填充方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【HiCoLoRA: Addressing Context-Prompt Misalignment via Hierarchical Collaborative LoRA for Zero-Shot DST ｜层级协作低秩适配

研究机构：上海交通大学、北京航空航天大学

作者：Shuyu Zhang、Yifan Wei、Xinru Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.19742)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.19742)

> 零样本对话状态追踪（zs-DST）旨在让任务导向对话系统无需目标域标注数据即可泛化至新领域，其核心障碍在于动态对话上下文与静态槽位提示间的语义错位。现有参数高效微调方法（如DualLoRA）统一处理Transformer各层，忽视了低层捕获局部语义原子、高层整合全局意图的层级特性，导致跨域干扰与灾难性遗忘。HiCoLoRA通过层级协作架构、谱聚类解耦及语义增强SVD初始化，在MultiWOZ和SGD上实现了零样本JGA的显著提升。该框架在PEFT范式下有效缓解了上下文-提示错位，但其性能仍低于依赖合成数据的SOTA方法，且对高特异性槽域的处理能力有限。

】
