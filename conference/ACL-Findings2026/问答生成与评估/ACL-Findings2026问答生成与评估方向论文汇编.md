# ACL-Findings2026 · 问答生成与评估方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DiFRa: A Unified Framework for Harmonizing Semantic Diversity and Factual Consistency in Question-Answer Generation ｜问答生成中的语义多样性与事实一致性调和框架

研究机构：澳门大学

作者：Zhenqin Li、ShengYong Ding、Shuangyin Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d8330da61917)

> 问答生成（QAG）旨在为垂直领域大语言模型（LLM）后训练提供高质量数据，但现有方法往往陷入“保守复制”导致的语义贫乏或“自由生成”引发的幻觉风险。本文指出，单纯追求多样性或一致性均无法解决训练数据中“信息增益”与“事实兼容”的内在张力。DiFRa 框架通过连续概念扩散与离散知识图谱约束的动态融合，在冻结 LLM 骨干的前提下实现了两者的平衡。该框架在 SQuAD 和 DROP 上优于多种基线，但其对 LLM 自身构建知识图谱的依赖，可能引入闭环幻觉风险。

】

---

【From Conversation to Evaluation: Benchmarking LLMs on Development Knowledge via SimpleDevQA ｜软件开发知识问答基准

研究机构：中山大学、澳大利亚莫纳什大学

作者：Jing Zhang、Lianghong Guo、Yanlin Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c284f16cad4c)

> 软件开发场景中的知识问答任务长期缺乏基于真实用户查询的评估基准，现有基准多聚焦代码片段理解，无法覆盖系统设计、数据库管理等广泛开发知识。本文从 WildChat 真实对话中筛选并转化出 5,529 个多语言、单一可验证答案的问答对，构建了 SimpleDevQA 基准。通过 21 个主流大语言模型（LLM）的评估，揭示了开源模型在开发知识上的显著差距及检索增强生成（RAG）对缩小规模差距的作用。该基准填补了垂直领域事实性评估空白，但其“模型中心”难度定义可能随模型迭代而失效。

】

---

【Large-Scale Diverse Synthesis for Mid-Training ｜中期训练数据合成框架 BoostQA

研究机构：北京大学、美团

作者：Xuemiao Zhang、Chengying Tu、Can Ren 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70b419ca60a5)

> 中期训练（Mid-training）旨在通过注入高质量合成数据提升大语言模型（LLM）的知识密度与推理能力，但现有合成方法常生成同质化且难度退化的问答对，导致模型在STEM领域及高难度任务上表现受限。BoostQA 通过引入模型探针诊断弱点，并采用多等级角色模拟与难度增强策略，实现了从单一种子到多样、高难问答对的一比多扩展。该框架在 Llama-3 8B 上验证了仅用 20B token 数据即可带来显著性能提升，但其效果高度依赖种子数据质量与特定领域分布，通用性边界尚存疑。

】

---

【Who is the richest club in the championship? Detecting and Rewriting Underspecified Questions Improve QA Performance ｜欠定问题检测与重写对问答性能的影响

研究机构：荷兰阿姆斯特丹大学

作者：Yunchong Huang、Gianni Barlacchi、Sandro Pezzelle

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9854582901ed)

> 问答基准中大量问题因指代不明或标准缺失而无法唯一确定答案，导致模型性能被系统性低估。现有评估体系默认问题良定，忽略了这种“欠定”（Underspecified, UND）现象对指标造成的混淆。本文通过构建LLM分类器识别UND问题，并采用Oracle重写实验量化其对性能的影响。该工作揭示了基准设计的隐性缺陷，但重写实验依赖金标答案，其结论在真实开放域场景中的外推性存疑。

】
