# ACL-Findings2026 · 类增量学习方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GROLE: Instance-Level Group Relative Optimization for LoRA Experts in Incremental Learning ｜实例级LoRA专家路由的增量学习框架

作者：Yongyi Liao、Wencan Lai、Jun Fang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d15b28a003d)

> 在线增量学习（Incremental Learning, IL）旨在让单一模型在数据流中持续获取新任务知识，同时避免灾难性遗忘（Catastrophic Forgetting, CF）并促进知识转移（Knowledge Transfer, KT）。现有基于低秩适应（Low-Rank Adaptation, LoRA）的方法要么通过正则化共享专家导致模糊边界下的遗忘，要么依赖任务ID路由独立专家从而阻断实例级知识复用。GROLE通过构建冻结的LoRA专家池，并利用基于群组相对优化（Group Relative Optimization, GRPO）的轻量级选择器，在推理时无需任务标签即可动态合并专家。该框架在文本分类基准上超越了多任务上界，但其对强化学习选择器在超长任务流下的可扩展性缺乏验证。

】
