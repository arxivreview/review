# ACL-Findings2026 · 蛋白质语言模型与生成设计方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ProtoCycle: Reflective Tool-Augmented Planning for Text-Guided Protein Design ｜文本引导蛋白质设计的反思式工具增强规划

研究机构：上海交通大学、中国科学技术大学

作者：Yutang Ge、Guojiang Zhao、Sihang Li 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16896)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16896)

> 文本引导蛋白质设计旨在将自然语言功能需求直接转化为满足特定生物属性的氨基酸序列，但现有端到端模型依赖海量配对数据且存在“计划-执行差距”，即模型能生成合理的文本规划却难以将其转化为高质量的残基序列。ProtoCycle 将设计过程重构为多轮“规划-工具调用-评估-反思”循环，由大语言模型（LLM）担任高层规划器，将序列生成委托给轻量级专用工具，并通过监督微调与强化学习优化规划策略。该方法以极少的训练数据实现了与大规模端到端模型相当甚至更优的语言对齐性能，但其依赖外部工具环境的架构是否限制了序列生成的全局探索能力，仍需进一步审视。

】

---

【STELLA: A Multimodal LLM for Protein Functional Annotation via Unified Sequence-Structure Encoding ｜蛋白质功能注释的多模态大语言模型

研究机构：北京大学、中国人民大学

作者：Hongwang Xiao、Wenjun Lin、Xi Chen 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4782ac22af63)

> 蛋白质功能注释面临结构数据爆发但功能标签滞后的矛盾，现有纯序列语言模型缺乏高分辨率结构信息，分离式多模态架构又引入冗余融合开销。STELLA 切入点在于利用统一编码的 ESM3 替代分离编码器，直接对接 LLM 生成自然语言功能描述。其核心做法是构建“ESM3 编码器 + 线性投影 + Llama-3.1-8B”的两阶段指令微调框架。该方案在酶反应预测上刷新了 SOTA，但功能描述生成的语义鲁棒性仍受限于 NLP 指标的代理性质，且对分布外结构的泛化能力尚未完全解决。

】
