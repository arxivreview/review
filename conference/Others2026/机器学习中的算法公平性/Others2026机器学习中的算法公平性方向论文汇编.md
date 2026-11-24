# Others2026 · 机器学习中的算法公平性方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Causal Pre-training Under the Fairness Lens: An Empirical Study of TabPFN ｜因果预训练基础模型的公平性边界

研究机构：挪威卑尔根大学、英国牛津大学

作者：Qinyi Liu、Mohammad Khalil、Naman Goel

论文原文见 [arXiv](https://arxiv.org/abs/2601.17912)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17912)

> 算法公平性研究旨在消除机器学习模型在信贷、司法等高风险决策中因历史数据偏见导致的系统性歧视，其核心张力在于数学上互斥的公平性定义与不可完全观测的真实世界约束之间的冲突。现有后处理或预处理干预手段依赖集中式数据或模型内部访问，难以在隐私敏感或分布偏移场景下保持鲁棒性，而因果推断框架虽强调过程正义，但缺乏对基础模型内生公平性的实证检验。本文通过系统评估基于结构因果模型（Structural Causal Model, SCM）预训练的表格数据基础模型 TabPFN 及其微调变体 FT-TabPFN，在虚假相关与缺失非随机（Missing-Not-At-Random, MNAR）协变量偏移下的表现，揭示了因果预训练在提升预测精度的同时，对群体公平性的改善有限且不一致。这一发现挑战了“因果预训练自动缓解偏见”的潜在假设，为部署此类模型提供了关键的实证警示。

】

---

【反事实平均公平预测

作者：Irina Arévalo、Marcos Oliva

论文原文见 [arXiv](https://arxiv.org/abs/2604.07009)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07009)

> 算法公平性研究旨在消除机器学习模型在信贷、司法等高风险决策中因历史数据偏见导致的系统性歧视，其核心张力在于数学上互斥的公平性定义与不可完全观测的真实世界约束之间的冲突。现有后处理方案多依赖阈值调整或群体标签，在隐私敏感的黑盒部署场景中因需访问敏感属性或模型内部而失效。本文提出反事实平均公平预测（Counterfactual Averaging for Fair Predictions, CAFP），通过内部查询事实与反事实属性下的预测并取均值，实现无需重训练、无需测试时群体标签的公平性修正。该方法在理论上消除了属性直接依赖，但在基础率差异显著的现实中，其人口统计均等保证面临前提失效风险，实际公平性增益有限。

】
