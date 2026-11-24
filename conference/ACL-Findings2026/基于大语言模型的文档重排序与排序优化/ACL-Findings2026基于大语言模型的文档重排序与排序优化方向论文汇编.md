# ACL-Findings2026 · 基于大语言模型的文档重排序与排序优化方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GroupRank: A Groupwise Paradigm for Effective and Efficient Passage Reranking with LLMs ｜GroupRank：分组式重排范式

研究机构：中山大学

作者：Meixiu Long、Duolin Sun、Dan Yang 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.11653)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11653)

> 导读 LLM 文档重排旨在利用大语言模型的上下文理解能力，将检索系统中的文档排序任务从静态相关性匹配升级为动态效用优化，其核心价值在于突破传统交叉编码器在长上下文与全局依赖建模上的瓶颈。现有 Listwise 方法虽能捕捉全局依赖，但受限于上下文窗口与自回归解码的高延迟，难以在大规模候选集下实时部署；Pointwise 方法虽高效，却因缺乏文档间比较导致排序精度次优。本文提出 GroupRank，通过将候选文档划分为独立小组并行评分，结合无答案数据合成与专用强化学习奖励，在保持 Listwise 精度的同时实现 Pointwise 级别的低延迟。该范式在推理密集型任务上显著优于基线，但其随机分组策略对组内高相关文档的区分能力存疑，且未验证在通用语义任务上的鲁棒性。

】

---

【ProRank: Prompt Warmup via Reinforcement Learning for Small Language Models Reranking ｜小语言模型文档重排中的提示预热与细粒度评分

研究机构：香港理工大学

作者：Xianming LI、Aamir Shakir、Rui Huang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_206d3e9d9499)

> 文档重排旨在优化检索结果顺序以提升下游生成质量，但主流大语言模型（LLM）方案因参数量大导致推理延迟高，难以满足实时性要求。现有小语言模型（SLM）方案虽具备效率优势，却受限于表征空间狭窄及零样本提示理解能力弱，导致排序精度不足。本文提出 ProRank，通过强化学习提示预热与基于 Logit 差值的细粒度评分两阶段训练，解决 SLM 的上述瓶颈。该方法在 BEIR 基准上以 0.5B 参数超越了 32B 规模的微调 LLM，验证了小型化重排器的潜力，但其对 Listwise 全局依赖建模的缺失及特定基准上的表现波动仍存疑。

】
