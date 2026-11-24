# ACL-Findings2026 · 上下文感知与专业领域机器翻译方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CEMT:Controllable Element-Oriented Machine Translation via Structured Linguistic Reasoning ｜可控元素导向机器翻译

研究机构：厦门大学

作者：Lingling Shi、Haoyu Jin、Ruiyu Fang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3cc459587b81)

> 导读 现有大语言模型在翻译含URL、俚语等特定元素时，常因缺乏显式约束而产生幻觉或遗漏，导致关键细节失真。通用思维链推理虽能提升分析深度，但奖励机制仅关注最终译文质量，存在信用分配模糊问题，无法确保中间推理步骤的准确性。CEMT通过前置元素检测模块与双轨结构化推理，将翻译重构为可控决策过程，并引入过程级监督解决推理质量评估难题。该方法在句级元素控制上表现有效，但其对文档级连贯性的影响及低资源语言泛化能力尚待验证。

】

---

【Context-Driven and Reference-Guided Data Augmentation for Subtitle Translation ｜上下文驱动与参考引导的数据增强

作者：Hitoshi Ito、Naoto Shirai、Kazutaka Kinugawa 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fcd883589cd)

> 字幕翻译面临单作品双语数据稀缺与风格保持的双重困境，传统数据增强方法难以兼顾世界观一致性与角色语调。本文切入点在于利用角色描述引导源句重写，并借助原句人工译文作为One-shot参考生成目标语，从而在低资源条件下构建风格对齐的平行数据。该方法通过QLoRA微调通用LLM，实现了特定电影翻译质量的提升。其价值在于降低了人工数据准备成本，但One-shot参考对目标语创造性的潜在限制尚未被充分验证。

】

---

【GlossaGen: Making Academic Translation Smarter with Glossing ｜面向学术学习的注释式翻译

研究机构：阿联酋扎耶德大学、中国人民大学

作者：Zixiao Wang、Duzhen Zhang、Juntian Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0edf328e8bd5)

> 学术翻译需解决非母语读者在理解专业文献时因术语缺失导致的认知断层。现有机器翻译系统往往将关键术语直译或替换为通俗词汇，破坏了术语习得的脚手架；而面向大众的简化策略则过度删减技术细节，无法满足学术进阶需求。GlossaGen 通过定义“注释式学术翻译”任务，利用多智能体流水线合成层级化数据，并采用动态适配器合并策略，在保留英文术语的同时生成符合读者认知水平的中文解释。该方法在自建基准上优于强基线，但其效果局限于计算机领域且依赖合成数据质量，跨领域泛化能力存疑。

】

---

【Learning to Translate by Translating: Stabilizing the Dual Loop via Semantic-Aware Self-Evolution ｜通过双向翻译循环实现无平行数据自进化机器翻译

研究机构：武汉大学

作者：Kui Liu、Mingming Yin、Zuoli Tang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d6c1569ca482)

> 机器翻译长期依赖大规模人工标注平行语料，其获取成本构成扩展性瓶颈。现有无监督方法因优化不稳定或奖励黑客问题难以在LLM时代落地，本文切入点在于将循环一致性原则适配生成范式，并引入语义感知奖励机制。具体做法是构建双向翻译闭环，利用Group Relative Policy Optimization (GRPO) 结合防作弊奖励进行策略优化。该方法在8B参数规模下实现了接近强监督基线的性能，但其对专业领域术语一致性及文档级连贯性的有效性尚未验证。

】

---

【Redefining Machine Simultaneous Interpretation: From Incremental Translation to Human-Like Strategies ｜动作基同步机器翻译

研究机构：香港中文大学

作者：Qianen Zhang、Zeyu Yang、Satoshi Nakamura

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_188650380d2b)

> 同步机器翻译（Simultaneous Machine Translation, SiMT）的核心矛盾在于增量生成过程中的延迟与质量权衡，传统READ/WRITE策略无法捕捉人类译员的重构、省略与简化行为。现有基于固定策略或隐式等待标记的方法在长句重排和口语冗余处理上存在刚性瓶颈。本文通过扩展LLM动作空间，将人类口译策略显式化为动态决策过程，实现了质量与延迟的更优平衡。该方法在ACL60/60基准上验证了动作引导推理的有效性，但其依赖开发集统计注入的机制是否导致分布过拟合，尚存疑。

】
