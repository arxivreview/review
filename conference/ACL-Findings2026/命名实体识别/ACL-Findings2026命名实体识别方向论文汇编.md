# ACL-Findings2026 · 命名实体识别方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ReCoT-NER: Enhancing Zero-Shot Named Entity Recognition through Chain-of-Thought Prompting and Recall-Oriented Loss Optimization ｜链式思维提示与召回导向损失增强零样本命名实体识别

研究机构：美国麻省理工学院

作者：Dabin Fu、Fanghong Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9da604b28764)

> 零样本命名实体识别（Zero-Shot Named Entity Recognition, ZS-NER）旨在无标注数据条件下识别开放集实体，但生成式模型常因解码偏差导致实体漏检与边界模糊。现有指令微调方法多采用单步生成，隐式耦合跨度检测与类型分类，加剧了模型对稀疏实体信号的忽略。本文提出ReCoT-NER，通过链式思维（Chain-of-Thought, CoT）提示显式分解推理步骤，并设计召回导向损失（Recall-Oriented Loss, RCLoss）强化边界起始信号。该方法在77M参数模型上实现了跨域泛化提升，但其性能上限受限于小模型容量，且未验证与动态指令优化方法的直接对比。

】
