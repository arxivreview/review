# ACL-Findings2026 · 序列推荐建模方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【HORIZON: A Benchmark for In-the-wild User Behaviour Modeling ｜HORIZON：跨域长时序用户行为建模基准

研究机构：美国卡内基梅隆大学、微软研究院

作者：Arnav Goel、Pranjal A Chitale、Bhawna Paliwal 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17259)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17259)

> 序列推荐领域长期依赖单域、短窗口的下一项预测任务，导致模型在真实多平台、长周期场景下的泛化能力被高估。现有基准如Amazon Reviews按类别隔离交互，无法捕捉跨域转移，且Leave-One-Out评估存在时间泄漏，掩盖了分布偏移下的性能衰减。HORIZON通过合并Amazon Reviews全类别构建54.51M用户的统一历史，并引入全局时间截断与用户可见性解耦的四象限评估协议，系统量化了模型在时间外推与未见用户场景下的鲁棒性边界。该基准揭示了Transformer骨干在分布偏移下的显著退化及LLM零样本建模的局限，但其评估协议对计算效率的忽视及基线覆盖的缺失，限制了其对工业部署可行性的全面判断。

】
