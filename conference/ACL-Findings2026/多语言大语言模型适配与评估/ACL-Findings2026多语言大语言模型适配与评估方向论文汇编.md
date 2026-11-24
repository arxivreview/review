# ACL-Findings2026 · 多语言大语言模型适配与评估方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Data-Centric Continual Pre-training for 500+ Languages: A New Bilingual Translation Corpus and Multilingual Models ｜大规模多语言持续预训练中的双语平行语料效能

研究机构：芬兰图尔库大学、芬兰赫尔辛基大学

作者：Shaoxiong Ji、Zihao Li、Jaakko Paavola 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_20dbcac609a8)

> 多语言大语言模型在低资源语言上性能稀释，源于预训练数据分布不均与分词器碎片化。现有持续预训练（Continual Pre-training, CPT）方法多依赖单语数据，缺乏对平行语料贡献的量化评估，导致高资源语言遗忘与低资源提升的权衡机制不明。本文构建覆盖2500+语言对的双语翻译语料MaLA，通过消融实验验证双语数据在大规模CPT中的具体增益。该工作证实了平行数据对翻译任务的显著优势，但暴露了高资源语言性能下降的结构性矛盾，其全参数训练的高算力门槛限制了社区部署的可行性。

】

---

【Exploring Two-Phase Continual Instruction Fine-tuning for Multilingual Adaptation in Large Language Models ｜两阶段持续指令微调中的指令相似性对英语能力保持的影响

研究机构：微软研究院

作者：Divyanshu Aggarwal、Sankarshan Damle、Navin Goyal 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.16006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ece602ea5ce7)

> 多语言大语言模型在提升非英语指令跟随能力时，常因灾难性遗忘导致英语能力显著退化，现有混合训练或盲目回放策略难以在资源受限下平衡双语性能。本文指出，阶段间指令数据集的语义相似性是决定英语能力是否保持的关键变量，而非单纯的数据量或训练步数。通过引入数据集嵌入相似度与模型参数差异度量，结合生成式回放与启发式层冻结策略，该研究在 MISTRAL-7B 和 LLAMA-3-8B 上验证了相似指令集可提升英语能力，而错位指令集则引发表示漂移。这一发现为低资源语言适配提供了基于数据结构的预测机制，但其全参数微调的高算力成本限制了在边缘设备上的直接部署。

】
