# ACL-Findings2026 · 医学视觉-语言预训练方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BioVLM: Routing Prompts, Not Parameters, for Cross-Modality Generalization in Biomedical VLMs ｜生物医学视觉语言模型中的动态提示路由

研究机构：美国卡内基梅隆大学、印度理工学院孟买分校

作者：Mainak Singha、Tanisha Gupta、Ankit Jha 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17629)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17629)

> 生物医学视觉语言模型在跨模态泛化时，常因单一提示向量无法覆盖多模态下的视觉多样性而失效。现有提示学习方法多依赖静态平均或固定阈值，难以在少样本与分布偏移场景下动态筛选高置信度语义。BioVLM 通过构建多提示池并引入基于熵的动态选择机制，结合 LLM 属性蒸馏，实现了冻结骨干下的自适应路由。该框架在 2D 医学影像上提升了泛化性能，但其对 3D 体数据空间稀疏性的适用性仍存疑。

】

---

【HeteroRAG: A Heterogeneous Retrieval-Augmented Generation Framework for Medical Vision Language Tasks ｜异构检索增强生成框架

作者：Zhe Chen、Yusheng Liao、Zhiyuan Zhu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2508.12778)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_022f07e10b76)

> 医学大型视觉语言模型（Med-LVLMs）在临床诊断中面临事实性错误与输出不可靠的严峻挑战，直接威胁诊疗安全。现有单模态或单一来源的检索增强生成（RAG）系统无法有效处理缺乏直接视觉语义且语言风格多样的异构医学语料，导致检索结果与查询特征错位。本文通过构建多模态报告库与多源文本语料库，提出包含模态特定检索器、多语料查询生成器及异构知识偏好调优的闭环框架。该框架在11个基准上实现了SOTA性能，但其在极端分布外（OOD）场景下的泛化边界及检索数据泄露风险仍需进一步审视。

】

---

【MedLayBench-V: A Large-Scale Benchmark for Expert-Lay Semantic Alignment in Medical Vision Language Models ｜医学视觉-语言模型中的专家-通俗语义对齐基准

作者：Han Jang、Junhyeok Lee、Heeseong Eum 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05738)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_010726e88ede)

> 医学视觉-语言模型（Med-VLMs）在诊断影像解读上已具备专家级能力，但其训练数据局限于专业术语，导致模型无法将视觉证据转化为患者可理解的通俗语言。现有文本简化研究虽已成熟，但缺乏多模态场景下的平行数据与评估标准，使得模型在通俗语域上的表现无法被量化。本文通过构建结构化概念接地精炼（SCGR）管线生成79,793对专家-通俗平行数据，填补了这一空白。该基准揭示了当前主流VLM在通俗对齐上的显著性能缺口，但其评估协议对生成质量的捕捉仍显单薄。

】
