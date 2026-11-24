# Others2026 · 智能体搜索与生成式信息检索方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【QueStER: Query Specification for Generative keyword-based Retrieval ｜生成式查询规格检索

研究机构：法国巴黎萨克雷大学、法国国家科学研究中心

作者：Arthur Satouf、Yuxuan Zong、Habiboulaye Amadou-Boubacar 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.05301)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.05301)

> 信息检索模型需在语义理解与计算效率间取得平衡，传统词汇匹配模型受限于词汇不匹配问题，而神经检索器因索引维护成本高难以动态更新。现有基于大语言模型的查询重写方法虽提升了效果，但依赖庞大参数与复杂提示，导致推理延迟高且结果不稳定。QUESTER 将生成式检索的目标从文档标识符转向关键词查询规格，利用强化学习微调轻量级大语言模型生成检索指令，由标准倒排索引执行。该方法在保持毫秒级检索延迟的同时，显著超越了基线词汇模型，但在域内绝对精度上仍低于专用神经检索器，其泛化边界尚待复杂查询场景验证。

】

---

【Retrieval as Generation: A Unified Framework with Self-Triggered Information Planning ｜检索即生成：基于自触发信息规划的统一框架

研究机构：北京大学

作者：Bo Li、Mingda Wang、Gexiang Fang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11407)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11407)

> 智能体搜索旨在解决静态检索增强生成（RAG）在多步推理中无法动态调整查询的局限，但现有方法多依赖外部控制器或启发式规则，导致检索时机与生成过程割裂。GRIP 提出“检索即生成”范式，将检索决策内化为模型解码过程中的控制令牌，实现端到端的自主规划。该方法通过结构化监督与规则奖励强化学习，在五个问答基准上超越了同规模基线，但其性能仍受限于骨干模型规模，且未验证其在长程复杂任务中相比多智能体架构的稳定性。

】
