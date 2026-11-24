# ACL-Findings2026 · 多语言多模态机器翻译与评估方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【FTibSuite: A Comprehensive Resource Suite for Tibetan Vision-Language Modeling ｜藏语视觉-语言模型资源套件

研究机构：上海交通大学、中国科学院

作者：Guixian Xu、Yide Liang、Zeli Su 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.26601)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.26601)

> 低资源语言的多模态研究长期受困于训练数据与评估基准的双重缺失，导致模型能力无法被公平量化与复现。现有方案多聚焦于英语或高资源语言，针对藏语等极小语种的系统性基础设施几乎空白。本文切入点在于构建一套包含数据、基准与基线模型的完整闭环，通过三阶段适配流水线在强骨干上实现藏语能力的可复现迁移。其价值在于填补了藏语多模态研究的基建空白，但实验仅对比无适配基线，缺乏与同类低资源适配方法的横向比较，泛化结论的边界尚存疑。

】

---

【MPTc-Bench: Measuring Cross-market Generative Ability of Vision-Language Models via Movie Poster Transcreation ｜电影海报跨市场转创基准

研究机构：日本京都大学

作者：Youyuan Lin、Yuan Li、Yahan Yu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc82a23ef819)

> 导读 多模态机器翻译长期聚焦于利用视觉上下文消解文本歧义，但现有方法在处理营销资产时往往忽略目标市场的隐性设计偏好，导致译文虽语义正确却缺乏文化契合度。本文切入点在于将“转创”概念引入电影海报领域，指出通用视觉语言模型在保持电影身份的同时难以执行市场特定的排版与风格调整。作者构建了包含582个跨市场样本的MPTc-Bench基准，并提出两阶段Planner-Editor框架以分离决策与执行。该工作揭示了当前模型在本地化文本渲染上的显著缺陷，但缺乏专用图像内翻译模型的对比，其结论的普适性存疑。

】

---

【Recovered in Translation: Efficient Pipeline for Automated Translation of Benchmarks and Datasets ｜推理时计算扩展下的多语言基准翻译框架

研究机构：瑞士苏黎世联邦理工学院

作者：Hanna Yukhymenko、Anton Alexandrov、Martin Vechev

论文原文见 [arXiv](https://arxiv.org/abs/2602.22207)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22207)

> 多语言大语言模型（LLM）评估的可靠性受制于翻译基准的质量，现有资源常因语义漂移和上下文丢失导致性能指标失真。传统机器翻译工具缺乏指令遵循能力，且将问题与选项分离翻译破坏了语法一致性，而简单的单次生成无法捕捉中资源语言的细微错误。本文提出一个自动化框架，通过测试时计算扩展策略（Test-time Compute Scaling），特别是多轮竞争性排序方法 T-RANK，在无需训练的情况下提升翻译保真度。该框架在八个东欧及南欧语言上验证了有效性，但其对长文本复杂结构的处理能力及开源模型适配性仍存疑。

】

---

【Worldwide LiveVQA: Real-Time Visual Knowledge Seeking and Updating Across Languages ｜全球实时视觉知识获取与更新

研究机构：华中科技大学

作者：Xuanao Huang、Xingjia Liu、Zetong Zhou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18e7e87e4909)

> 多模态大语言模型（MLLMs）在视觉事实检索中面临“全球知识鸿沟”，即非英语地区的实时视觉信息被系统性排除在主流评估与训练数据之外。现有基准局限于静态英语语境，无法量化模型对跨语言、时效性视觉实体的感知能力。本文构建了首个动态更新的多语言视觉知识数据集 LIVEVQA-W，并揭示了搜索增强模型在低资源语言下的检索瓶颈。该工作填补了全球视觉事实评估的空白，但注入知识的跨语言泛化能力依然脆弱。

】
