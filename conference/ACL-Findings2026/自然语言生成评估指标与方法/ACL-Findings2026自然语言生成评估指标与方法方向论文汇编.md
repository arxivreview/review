# ACL-Findings2026 · 自然语言生成评估指标与方法方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MATCHA: Matching Text via Contrastive Semantic Alignment ｜对比语义对齐指标

研究机构：德国图宾根大学

作者：Siran Li、Ece Sena Etoglu、Carsten Eickhoff 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc512962911f)

> 自然语言生成评估的核心困境在于，现有主流指标无法有效区分语义一致与语义矛盾的文本。BERTScore等基于预训练嵌入的指标因嵌入空间的聚类效应，常对事实错误文本赋予高分，导致评估结果与人类判断脱节。本文提出MATCHA，通过引入对抗性反事实样本进行对比学习训练，显式惩罚与参考文本矛盾的输出。该方法在多个基准上显著提升了正确与错误文本的区分度，但其依赖参考文本的设定限制了在开放生成任务中的直接适用性。

】
