# ACL-Findings2026 · 长上下文大语言模型推理与评估方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ARC: Active and Reflection-driven Context Management for Long-Horizon Information Seeking Agents ｜主动反思驱动上下文管理

研究机构：北京大学、北京航空航天大学

作者：Yilun Yao、Shan Huang、Elsie Dai 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12030)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12030)

> 长时域信息检索智能体在交互历史增长后普遍出现性能退化，即上下文腐烂，现有方案仅通过原始累积或被动压缩控制长度，无法修复早期错误与失焦。本文提出 ARC 框架，将上下文视为动态内部状态，通过解耦的上下文管理器执行增量摘要与反思驱动的重组织。该设计在 BrowseComp-ZH 上较被动压缩基线提升 11% 绝对准确率，但反思触发机制的泛化边界与训练数据依赖仍未完全揭示。

】

---

【Budget-Aware Routing for Long Clinical Text ｜预算感知临床长文本上下文构建

研究机构：美国麻省理工学院、美国康奈尔大学

作者：Khizar Qureshi、Geoffrey Martin、Yifan Peng

论文原文见 [arXiv](https://arxiv.org/abs/2605.00336)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.00336)

> 临床部署中，长文档的Token成本与延迟直接制约模型可用性，而现有长上下文研究多聚焦于模型内部注意力机制优化，忽略了输入侧的预算约束。本文切入点在于将上下文构建视为背包约束下的子集选择问题，而非模型能力扩展。通过引入RCD目标函数与预算感知路由层，在固定Token预算下动态选择最优提取策略。该工作验证了评估范式对策略选择的决定性影响，但其结论局限于抽取式与生成式摘要任务，对复杂推理场景的泛化性存疑。

】

---

【From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models ｜检索头掩码优化长上下文大语言模型

研究机构：日本东京科学大学

作者：Youmi Ma、Naoaki Okazaki

论文原文见 [arXiv](https://arxiv.org/abs/2601.11020)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9e8f8877f3d9)

> 长上下文大语言模型面临标称窗口长度与有效推理能力脱节的困境，现有后训练方法依赖外部奖励模型或人工标准，难以精准定位性能瓶颈。RetMask 利用机制可解释性发现的“检索头”作为对比信号源，通过屏蔽特定注意力头生成负样本，构建直接偏好优化训练对。该方法在 Llama-3.1-8B 上实现了 128K 上下文下 2.28 分的提升，验证了机制洞察转化为性能增益的可行性，但其效果高度依赖模型内部检索分数的稀疏度分布。

】

---

【Incentivizing In-depth Reasoning over Long Contexts with Process Advantage Shaping ｜长上下文推理中的过程优势整形

研究机构：香港科技大学、阿里巴巴集团

作者：Miao Peng、Weizhou Shen、Nuo Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12465)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12465)

> 长上下文大语言模型在复杂推理任务中普遍面临“几乎正确”轨迹被稀疏奖励无效惩罚的问题，导致模型难以从部分正确的推理路径中提取学习信号。现有基于结果奖励的强化学习（RLVR）方法无法区分中间步骤的正确性与最终答案的错误性，尤其在长文档信息分散场景下失效。本文通过知识图谱（KG）驱动的多跳问答合成与过程优势整形（Process Advantage Shaping），将步骤级有效性（Validity）与相关性（Relevance）信号融入优势估计，实现细粒度信用分配。该方法在小参数模型上显著提升了长程推理稳定性，但其对参考轨迹生成成本的依赖及跨基准性能差异仍存疑。

】

---

【InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents ｜文件中心状态抽象

研究机构：香港理工大学

作者：Chenglin Yu、Yuchen Wang、Songmiao Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03204)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03204)

> 长时域智能体（Long-Horizon Agent）面临的核心困境是上下文窗口的无限增长导致推理稳定性崩塌。现有方案依赖截断或摘要，但无法解决状态与推理上下文的纠缠问题。InfiAgent 提出将持久状态外化为文件系统，通过有界上下文重建实现无限时域执行。该框架在 20B 模型上实现了与大型专有模型相当的 DeepResearch 性能，但其串行执行架构带来的延迟开销限制了实时场景的适用性。

】

---

【LLM Multi-Agent Systems for Long Triple Set Data-to-Text Generation ｜长结构化数据到文本生成的多智能体协同控制

作者：Chinonso Cynthia Osuji、Simon Mille、Mark Andrade 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b41760fecd9)

> 数据到文本（Data-to-Text, D2T）生成旨在将结构化数据转化为连贯自然语言，但现有基准多聚焦短文本，难以评估大语言模型（LLM）在长输入下的语义完整性与话语连贯性。随着模型上下文窗口扩展至32k以上，单步生成在长序列中易出现信息遗漏与幻觉，且缺乏对中间推理过程的有效控制。本文提出一种模块化多智能体框架，通过内容排序、文本结构化与表面实现的角色分工，结合监督与校验机制，解决长结构化数据生成的控制难题。该框架在英语与爱尔兰语上展示了连贯性优势，但统计显著性不足，且LLM评估在长文本与低资源场景下可靠性存疑。

】

---

【Lost in Decomposition: Analyzing and Mitigating the Limitations of Long Context Methods via Context Dependency ｜上下文依赖感知路由

作者：Jiayuan Guo、Yueyang Su、Yuyao Ge 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b61b72636c68)

> 长上下文工作流方法在特定数据集上表现优异，但跨数据集泛化能力存疑，现有研究默认其普适有效。本文指出，RAG、多智能体等方法因内部分解机制破坏了文档的上下文依赖结构，导致在强依赖文档上性能反而低于全上下文基线。通过提出文档上下文依赖得分（DCDS）量化依赖强度，并设计免训练自适应路由策略CoDaR，仅对弱依赖文档调用工作流方法。该策略显著提升了鲁棒性，但DCDS计算依赖大语言模型评估器，其推理成本与延迟是否抵消路由收益尚待验证。

】

---

【When Thoughts Meet Facts: Reusable Reasoning for Long-Context LMs ｜思维模板增强长上下文语言模型

研究机构：韩国科学技术院、美国明尼苏达大学

作者：Soyeong Jeong、Taehee Jung、Sung Ju Hwang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07499)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07499)

> 长上下文语言模型（LCLM）虽能容纳海量文档，但缺乏连接分散证据的结构化推理策略，导致多跳推理性能瓶颈从检索转移至逻辑组合。现有方法或依赖昂贵的模型微调，或使用一次性、查询特定的思维链提示，无法实现推理模式的复用与迭代优化。本文提出TOTAL框架，将推理过程抽象为可复用的“思维模板”，并通过自然语言反馈模拟梯度更新机制，在不修改模型权重的前提下迭代优化这些外部参数。该方法在免训练设定下显著优于基线，但绝对性能仍低于经过强化学习训练的前沿模型，且模板的泛化边界尚待明确。

】
