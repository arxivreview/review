# ACL-Findings2026 · 低资源机器翻译方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Kumatigi: Quality-Driven Data Augmentation for Low-Resource Machine Translation ｜质量驱动的双数据集生成与正字法增强

作者：Cheick Tidiani Cissé

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_db5c46c5b615)

> 低资源机器翻译在极端数据稀缺场景下面临的核心矛盾是：单语数据丰富但平行语料匮乏，且现有资源缺乏质量元数据导致模型无法区分高质与噪声样本。传统回译方法虽能扩充数据量，但引入的噪声与语义漂移在形态丰富语言中尤为致命，而通用数据增强策略又忽略了班巴拉语特有的正字法变异。本文切入点在于将回译过程改造为“知识提取”信号源，通过往返翻译差异与模型内部置信度联合评分，实现质量驱动的双数据集生成与针对性正字法增强。其价值在于为极端低资源场景提供了一套可复现的语料构建与增强范式，但该方法对非形态丰富语言的泛化性尚未验证，且依赖单一母语者标注的质量评分体系存在主观性风险。

】

---

【Layer-aware Dual-directional Modulation for Low-resource Machine Translation ｜层感知双向调制

作者：Siqi Zhang、Ran Song、Shuting Jiang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_67d40b8a436b)

> 低资源机器翻译（LRMT）中，大语言模型（LLM）在微调时面临预训练偏差与任务特异性信号争夺优化资源的困境，导致性能提升受限。现有参数高效微调（PEFT）方法对所有层施加均匀更新，忽略了不同层在低资源场景下功能分化的事实。本文通过量化层间激活差异，识别出需放大的任务自适应层与需抑制的遗留惯性层，并设计双向调制机制动态调节其贡献。该框架在多个骨干网络上验证了有效性，但其在特定模型架构上的极端敏感性暗示了泛化边界的存在。

】

---

【ManCC: A Task-Anchored Benchmark for Manchu–Classical Chinese Cross-Lingual Modeling ｜满文-古典中文跨语言建模基准

研究机构：美国堪萨斯大学、四川大学

作者：Meiqi Wang、Xiaoxin Sun、Dongjie Wang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f450e1b8ded1)

> 历史濒危语言缺乏标准化评估基础设施，导致模型性能无法横向比较且自动指标失效。现有低资源翻译基准多针对现代语言，难以捕捉历史文本的规范性与文化特异性。本文构建了首个满文-古典中文双向翻译基准，结合专家验证语料与三维人工评估协议。该工作填补了历史语言NLP评估空白，但人工评估的高成本限制了其在大规模模型迭代中的复用性。

】

---

【NSL-MT: Linguistically Informed Negative Samples for Efficient Machine Translation in African Low-Resource Languages ｜负空间学习机器翻译

研究机构：美国罗切斯特理工学院

作者：Mamadou K. Keita、Christopher Homan、Huy Le

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ade4fc7ad12a)

> 低资源机器翻译面临的核心困境是平行语料极度稀缺，导致模型无法通过隐式分布学习区分合法与非法输出。现有数据增强方法仅扩充正样本，未提供关于“什么不该生成”的显式约束，且在缺乏反向翻译模型时失效。本文提出负空间学习机器翻译（Negative Space Learning Machine Translation, NSL-MT），通过规则生成语言学违规负样本并修改损失函数进行惩罚。该方法在极端低资源场景下显著提升了数据效率，但其效果高度依赖人工规则的质量与覆盖率，对规则缺失的语言泛化能力存疑。

】

---

【Syntax as a Rosetta Stone: Universal Dependencies for In-Context Coptic Translation ｜句法作为罗塞塔石碑：通用依存关系用于科普特语上下文翻译

研究机构：美国乔治城大学

作者：Abhishek Purushothama、Emma Thronson、Alexia Guo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18758)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6d214fa1335c)

> 低资源机器翻译（Low-Resource Machine Translation, LRMT）的核心困境在于，大语言模型（LLM）对缺乏数字足迹的语言（如科普特语）缺乏隐式建模能力，导致零样本翻译产生流畅但语义错误的输出。现有基于词典的上下文学习（In-Context Learning, ICL）方法仅能解决词汇映射问题，无法约束复杂的句法结构，导致模型在生成目标句时依赖概率猜测而非语法逻辑。本文提出将通用依存关系（Universal Dependencies, UD）解析结果作为提示工程中的显式语法资源，通过词汇与句法信息的联合注入，在无需参数更新的情况下提升翻译的结构准确性。该方法在科普特语到英语的翻译任务上实现了新的最先进（State-of-the-Art, SOTA）性能，但其效果高度依赖于自动句法解析的准确性，且未验证在数据更丰富语言上的泛化性。

】
