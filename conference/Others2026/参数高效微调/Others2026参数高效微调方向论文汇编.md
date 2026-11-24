# Others2026 · 参数高效微调方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【医疗文本摘要中的参数高效微调对比研究

作者：Ulugbek Shernazarov、Rostislav Svitsov、Bin Shi

论文原文见 [arXiv](https://arxiv.org/abs/2603.21970)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21970)

> 医疗文本摘要任务面临全参数微调算力成本高昂的困境，而现有参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）方法在特定领域任务上的相对优势缺乏系统性实证。本文切入点在于通过多规模模型与多随机种子的严格统计对比，检验低秩适配（Low-Rank Adaptation, LoRA）是否能在医疗摘要任务上超越全参数微调。作者通过在 Flan-T5 系列模型上实施 LoRA、提示微调（Prompt Tuning）与全参数微调的对照实验，发现低秩约束在特定条件下提供了有益的正则化效应。这一发现挑战了“参数越多性能越好”的常规假设，但其结论局限于编码器-解码器架构与单一数据集，对解码器-only 模型的普适性存疑。

】
