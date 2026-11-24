# ACL-Findings2026 · 大语言模型中的心智理论与元认知方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Can Small LLMs Learn a Robust Theory of Mind via RLVR? Investigating Generalization through the False-Belief Task ｜强化学习可验证奖励能否赋予小模型通用心智理论？

研究机构：加拿大麦吉尔大学、美国纽约大学

作者：Sneheel Sarangi、Hanan Salam

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a5ede7f18be1)

> 该方向旨在验证大语言模型（LLMs）能否通过强化学习可验证奖励（RLVR）习得可泛化的心智理论（ToM），而非仅依赖统计捷径。现有RLVR在逻辑推理中表现优异，但在社交推理中是否同样有效尚存争议，且小模型在ToM基准上普遍存在分布外泛化失效问题。本文通过系统消融实验，训练7B参数模型在多种ToM数据集组合上进行RLVR，并评估其在保留基准上的迁移能力。研究揭示了RLVR在ToM任务中导致窄域过拟合而非抽象能力习得的机制，对“RL万能论”提出了关键反证，但其结论是否适用于更大规模模型仍存疑。

】

---

【Decision Biases and Intent-Irony Decoupling in Large Language Models ｜意图-反讽解耦：LLM语用推理的机制诊断

研究机构：浙江大学

作者：Kewei Guo、Lingyun Sun、Manhao Guan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8db6928373c2)

> 大语言模型在反讽理解中表现出高敏感度但低准确率的矛盾现象，现有基准仅能评估最终分类结果，无法区分模型是依赖深层心理模拟还是表面统计启发式。本文通过构建基于认知理论的多维评估框架，将反讽理解拆解为信念、意图、听众反应等五个子任务，并引入信号检测理论分离敏感度与决策偏差。实验揭示了LLM存在“意图-反讽解耦”现象，即能提取语用线索却无法将其整合进最终判断。该研究提供了机制诊断的新范式，但其结论是否可推广至其他高阶心智理论任务尚存疑问。

】

---

【Does Theory of Mind Improvement Really Benefit Human-AI Interactions? Empirical Findings from Interactive Evaluations ｜从静态问答到动态交互：心智理论增强技术的人机协同效用评估

研究机构：美国亚利桑那州立大学、香港科技大学

作者：Nanxu Gong、Zixin Chen、Haotian Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15205)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15205)

> 大语言模型的心智理论（Theory of Mind, ToM）旨在推断他人心理状态，但现有评估多依赖静态故事问答，无法反映真实人机交互（Human-AI Interaction, HAI）中的动态性与开放性。本文指出静态基准成绩提升未必转化为实际交互收益，提出将ToM评估从第三人称视角转向第一人称动态对话。通过对比四种增强技术在目标导向与体验导向任务中的表现，发现其在体验任务中有效但在目标任务中失效，且用户感知差异极小。这一发现揭示了当前ToM增强方法在功能转化上的局限，其结论对依赖静态指标优化模型社交能力的研究路径构成直接挑战。

】

---

【Infusing Theory of Mind into Socially Intelligent LLM Agents ｜目标导向社交推理中的心智理论集成

研究机构：加拿大不列颠哥伦比亚大学、加拿大向量研究所

作者：EunJeong Hwang、Yuwei Yin、Giuseppe Carenini 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6a7fd957c401)

> 导读 社交智能的核心在于理解对话伙伴的心理状态并据此调整策略，但现有大语言模型（LLM）往往将心智理论（Theory of Mind, ToM）推理与话语生成割裂，导致模型虽能回答关于他人信念的问题，却无法在动态交互中利用这些推断达成社交目标。本文指出，仅优化话语以达成目标会引发奖励黑客问题，而忽略显式心理状态建模则使模型缺乏策略性。为此，作者提出 ToMAgent (TOMA)，一种结合 ToM 预测与对话结果前瞻模拟的训练框架，通过筛选高效用的“心理状态-话语”对进行微调。该方法在 Sotopia 基准上显著提升了小模型的社交表现，验证了显式 ToM 建模对社交智能的关键作用，但其依赖 LLM 作为评估器的机制是否引入系统性偏差仍存疑。

】

---

【Modeling Multi-Dimensional Cognitive States in Large Language Models under Cognitive Crowding ｜多维认知状态建模中的几何瓶颈与双曲解耦

研究机构：哈尔滨工业大学、澳门大学

作者：Lin Zhong、Siyu Zhu、Zizhen Yuan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17174)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7ccc80b9eb1)

> 现有大语言模型在处理情感、思维、立场与意图等多维心理状态时，往往陷入单维任务的高准确率与联合预测的低准确率之间的割裂。这种割裂源于欧氏嵌入空间无法承载认知状态固有的层级结构，导致不同维度的语义表征发生重叠。本文提出 HyCoLLM 框架，利用庞加莱球模型的双曲几何特性解耦认知维度，并通过语义-认知拓扑损失对齐语言模型内部表征。该方法在自建基准上使 8B 参数模型超越 GPT-4o，但其对静态文本的依赖及维度独立假设限制了其在动态交互场景中的适用性。

】

---

【ToM-Synth: Scaling Robust Theory of Mind in LLMs via 6,912 Structured Social Units ｜结构化社交单元合成与强化学习微调

研究机构：浙江大学、阿里巴巴集团

作者：Guiyang Hou、Xiang Huang、Shangke Lyu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_952fd1eb91fb)

> 大语言模型在社交互动中缺乏鲁棒的心智理论（ToM）能力，现有方法依赖评估基准作为训练数据导致窄域过拟合。本文通过构建6,912个结构化社交单元，系统合成27,648条训练数据，利用Group Relative Policy Optimization (GRPO) 微调模型，将ToM能力内化至参数。该方法在开源模型中达到SOTA，但合成数据的分布覆盖度与生成模型的风格偏好是否引入新偏差，仍存疑。

】
