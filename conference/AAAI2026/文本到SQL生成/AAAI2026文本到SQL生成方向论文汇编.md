# AAAI2026 · 文本到SQL生成方向论文汇编

> 本方向共 1 篇（AAAI2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Schema on the Inside: A Two-Phase Fine-Tuning Method for High-Efficiency Text-to-SQL at Scale ｜两阶段微调实现Schema内化的高效Text-to-SQL

作者：Chinmay Soni、Shivam Chourasia、Gaurav Kumar 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24023)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24023)

> 工业级Text-to-SQL应用面临长上下文提示导致的API成本与延迟瓶颈，现有提示工程方法在固定Schema场景下无法兼顾精度与效率。本文切入点在于将Schema从推理时的显式输入转化为训练时的参数化记忆。通过两阶段LoRA微调，模型在仅含ID触发的极简提示下实现高精度SQL生成。该方法在私有域内显著优于基线，但缺乏跨域泛化验证，其通用性存疑。

】
