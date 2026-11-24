# ACL-Findings2026 · 联邦参数高效微调方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Federated LoRA Fine-Tuning with Pipelined Error-Mitigated Aggregation and Matrix-Wise Freezing ｜联邦低秩适配微调中的流水线误差缓解聚合与矩阵级冻结

研究机构：武汉大学、华中科技大学

作者：Haoran Wang、Xiong Wang、Yuqing Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22e6b757e603)

> 联邦大语言模型微调面临聚合偏差与边缘设备算力瓶颈的双重制约，直接平均低秩因子导致全局更新失真，而现有冻结策略粒度粗糙或计算开销过大。iFLoRA通过重构局部更新矩阵并执行SVD分解来消除代数误差，同时引入流水线机制隐藏服务器端计算延迟，并基于更新稳定性实施自适应矩阵级冻结。该方法在保持模型精度的前提下显著提升了训练效率，但其SVD近似误差在极端非独立同分布数据下的鲁棒性仍缺乏充分验证。

】
