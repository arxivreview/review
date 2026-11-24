# ACL-Findings2026 · 实体链接与对齐方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AnchorAlign: A Novel Anchor Alignment-enhanced Generative Method for Joint Named Entity Recognition and Relation Extraction ｜锚点对齐生成式联合抽取

研究机构：哈尔滨工业大学

作者：Xiaolong Weng、Yuanyun Zhou、Boyu Qiu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0f6f1d74e668)

> 联合命名实体识别与关系抽取（Joint NER/RE）旨在从非结构化文本中同步提取实体及其关系，但现有生成式方法常因实体与关系在生成序列中位置错位或语义脱节，导致抽取结果内部不一致。本文指出，既有对齐机制仅关注跨任务依赖而忽略任务内依赖，且存在“一对多”匹配偏差。为此，AnchorAlign 提出锚点实体选择机制与双层级对齐模块，在概率空间强制实体-关系及关系-关系的语义一致性。该方法在五个基准上刷新了关系抽取的严格 F1 与边界 F1 纪录，但其对判别式模型在复杂依赖场景下的优势仍存疑，且未验证锚点机制在低资源或长尾实体上的鲁棒性。

】

---

【Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate ｜基于两阶段多智能体辩论的可靠实体对齐框架

作者：Cunda Wang、Ziying Ma、Po Hu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_60121fdb2f97)

> 实体对齐（Entity Alignment, EA）旨在识别不同知识图谱（KG）中指向同一现实世界对象的实体，其核心难点在于跨库异构性导致的语义歧义。现有基于大语言模型（LLM）的方法虽提升了语义理解能力，但受限于单次推理的不可逆性与候选检索的上限约束，难以在复杂歧义场景下保证决策可靠性。AgentEA 通过引入直接偏好优化（DPO）增强嵌入判别力，并设计轻量级辩论验证与深度辩论对齐的两阶段多智能体机制，实现了决策透明化与效率平衡。该框架在跨语言基准上达到了 SOTA 水平，但其对闭源模型的依赖及辩论轮次的固定设置，限制了其在零样本泛化场景下的适用性评估。

】

---

【ThinkLinker: From Low-Rank Interaction to Knowledge-Aware Verification for Multimodal Entity Linking ｜多模态实体链接中的低秩交互与知识驱动验证

研究机构：东南大学

作者：Yingyao Ma、Yuanyuan Zhou、Congyu Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0f4431da2cbb)

> 多模态实体链接旨在利用图文联合信息消解文本提及的歧义，但现有方法在特征交互上依赖独立模块，难以显式建模跨粒度、跨模态的联合依赖，且在弱上下文场景下缺乏基于候选实体的反向验证机制。ThinkLinker 通过低秩融合塔统一处理多级特征交互，并引入 LLM 双向对话验证以精炼提及表示，解决了上述两个瓶颈。该方法在 WikiMEL 和 WikiDiverse 上均取得 SOTA 性能，但其第二阶段依赖 LLM 多轮生成，计算开销随数据集规模线性甚至超线性增长，且验证过程目前仅作用于文本模态，限制了其在大规模实时场景中的适用性。

】
