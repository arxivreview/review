# ACL2026 · 面向临床决策支持的LLM智能体方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【From Answers to Arguments: Toward Trustworthy Clinical Diagnostic Reasoning with Toulmin-Guided Curriculum Goal-Conditioned Learning ｜基于图尔敏论证模型的临床诊断推理课程学习

作者：Chen Zhan、Xiaoyu Tan、Gengchen Ma 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11137)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11137)

> 临床大语言模型常陷入“答案正确但推理错误”的陷阱，现有评估仅关注结果准确率，训练则依赖不稳定的强化学习，导致模型缺乏可解释性与鲁棒性。本文切入点在于将图尔敏论证模型同时作为评估标尺与训练目标，通过三阶段课程目标条件学习（Curriculum Goal-Conditioned Learning, CGCL）替代在线强化学习。该方法以离线模仿学习构建结构化诊断论证，在3B小模型上以更低计算成本达到与强化学习相当的推理质量。其价值在于提供了稳定且可解释的训练范式，但7B模型上性能略低于强化学习基线，且评估依赖大语言模型裁判，泛化边界尚存疑。

】

---

【MedEinst: Benchmarking the Einstellung Effect in Medical LLMs through Counterfactual Differential Diagnosis ｜医疗大语言模型中的思维定势效应（Einstellung Effect）基准与因果推理智能体

研究机构：美国斯坦福大学、深圳大学

作者：Wenting Chen、Zhongrui Zhu、Guolin Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06636)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06636)

> 导读 临床诊断依赖对细微鉴别证据的敏感捕捉，但大语言模型（LLM）常陷入“思维定势效应”，即过度依赖统计捷径而忽略患者特异性证据，导致非典型病例误诊。现有基准仅评估静态知识或标准流程，无法暴露这种在反事实场景下的推理失效。本文构建首个反事实诊断基准 MedEinst，并提出基于循证医学（EBM）的因果推理智能体 ECR-Agent，通过结构化证据验证抑制统计偏差。该工作揭示了前沿模型“能力越强、盲点越深”的悖论，但其单智能体架构在复杂多病共存场景下的泛化能力仍存疑。

】
