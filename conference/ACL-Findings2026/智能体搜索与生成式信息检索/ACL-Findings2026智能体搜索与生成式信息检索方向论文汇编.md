# ACL-Findings2026 · 智能体搜索与生成式信息检索方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agentic Conversational Search with Contextualized Reasoning via Reinforcement Learning ｜对话式智能体搜索中的上下文推理强化学习

研究机构：美国马萨诸塞大学阿默斯特分校、美国圣母大学

作者：Fengran Mo、Yifan Gao、Sha Li 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13115)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5536d5c36014)

> 多轮对话中用户意图随历史交互演化，传统静态“重写-检索-生成”管道因模块独立优化而难以捕捉动态依赖，且现有深度搜索智能体仅针对单轮自包含查询设计，缺乏对历史上下文的去语境化处理与混合主动性交互能力。本文切入点在于将强化学习奖励分解为结果、信息增益与混合主动性三部分，在单一智能体框架内联合优化查询生成、证据利用与交互决策。该方法通过中间过程奖励缓解多轮场景下的稀疏监督信号问题，在四个对话基准上超越了单轮智能体基线，但其性能增益是否完全源于奖励分解而非骨干模型规模，仍需更严格的控制实验验证。

】

---

【Agentic-R: Learning to Retrieve for Agentic Search ｜面向智能体搜索的检索器训练框架

作者：Wenhan Liu、Xinyu Ma、Yutao Zhu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c50d6cebe2a4)

> 智能体搜索（Agentic Search）中，检索器长期作为静态黑盒存在，其基于语义相似度的匹配目标与智能体多轮推理中对“证据效用”的动态需求存在根本错位。现有单轮检索增强生成（RAG）的效用优化方法无法处理中间查询缺乏金标准答案、且局部相关不等于全局正确的问题。本文切入点在于将检索器训练重构为与智能体双向迭代的闭环过程，通过联合建模局部相关性与全局答案正确性来定义段落效用。该框架在七个问答基准上验证了检索器对智能体性能的显著提升，但其迭代收敛性与跨智能体泛化能力仍受限于特定的训练数据分布。

】

---

【AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning ｜自适应搜索深度强化学习框架

研究机构：中国科学院、中国科学院大学

作者：Jingbo Sun、Wenyue Chong、Songjun Tu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17337)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17337)

> 智能体检索增强生成（Agentic RAG）系统在处理复杂查询时，往往陷入冗余搜索，导致计算成本与延迟激增。现有方法通过固定步数或外部模型判断来限制搜索深度，但前者导致复杂问题探索不足，后者引入额外延迟且无法适应模型自身能力。本文提出AutoSearch，一种基于自生成中间答案的强化学习框架，通过动态识别“最小充分搜索深度”来平衡准确率与效率。该框架在低参数量骨干上实现了帕累托改进，但其自评估机制在极长程任务或高噪声环境下的鲁棒性尚存疑。

】

---

【Beneficial Reasoning Behaviors in Agentic Search and Effective Training Methods to Obtain Them ｜行为预植：解锁智能体搜索强化学习潜力的训练范式

研究机构：美国卡内基梅隆大学

作者：Jiahe Jin、Abhijay Sai Paladugu、Chenyan Xiong

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f45aa315e75f)

> 智能体搜索（Agentic Search）旨在让大语言模型（LLM）通过多步交互解决复杂信息需求，但直接应用强化学习（RL）常因策略熵坍缩导致训练不稳定。现有SFT-then-RL范式依赖结果正确性或随机蒸馏，忽略了中间推理过程的质量差异，导致模型缺乏探索基础。本文提出行为预植（Behavior Priming），通过筛选包含特定推理行为的轨迹进行SFT，再行RL，以建立探索基础。该方法在Web基准上相对直接RL提升37.2%，验证了推理行为比结果正确性更关键，但其对多智能体架构的适用性尚存疑。

】

---

【Characterizing Web Search in The Age of Generative AI ｜生成式搜索输出特性表征

作者：Elisabeth Kirsten、Jost Grosse Perdekamp、Mihir Upadhyay 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11560)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11560)

> 生成式搜索将传统排名列表转化为单一合成文本，但现有评估指标无法捕捉其源选择偏差与内部知识依赖度。本文通过对比传统与生成式引擎的源重叠率及概念覆盖度，量化了这种范式转换对信息暴露的影响。其价值在于揭示了“低引用高覆盖”现象，但缺乏对幻觉风险的直接度量。

】

---

【Data-Centric Perspectives on Agentic Retrieval-Augmented Generation: A Survey ｜智能体检索增强生成的数据生命周期

研究机构：北京大学

作者：Jingwen Deng、Jihao Huang、Zhen Hao Wong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5272b768a4fd)

> 智能体检索增强生成（Agentic RAG）旨在让大语言模型（LLM）通过多步推理与工具调用主动获取外部知识，以突破静态检索增强生成（RAG）在复杂任务上的局限。然而，该领域面临的核心瓶颈并非算法设计，而是缺乏包含规划、检索与多步决策的高质量交互式轨迹数据，现有静态语料无法支撑此类模型的训练与评估。本文从数据工程视角切入，系统梳理了从数据收集、任务构建到评估与训练增强的完整生命周期，提出了“生成-验证-过滤/精炼”管道及难度增强框架。这一工作为构建可扩展的智能体搜索基准提供了方法论基础，但其对数据质量指标的量化验证仍显不足，且未直接解决长程任务中的信用分配难题。

】

---

【From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning ｜从经验到技能：基于可复用策略学习的多智能体生成式引擎优化

研究机构：中南大学、中山大学

作者：Beining Wu、Fuyou Mao、Jiong Lin 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19516)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19516)

> 生成式引擎（GEs）将信息获取从链接排序转变为带引用的答案生成，但现有生成式引擎优化（GEO）方法仅针对单实例进行启发式修改，无法跨任务积累有效策略。本文指出，缺乏策略复用机制导致优化过程陷入重复试错，且现有指标分离了可见性与引用忠实度。MAGEO 通过多智能体执行层与技能库学习层的双层架构，将验证过的编辑模式蒸馏为可复用的引擎特定技能。该框架在因果归因协议下显著提升了内容可见性与引用准确性，但其策略泛化能力受限于静态检索列表的假设，且高计算成本是否抵消长期收益仍存疑。

】

---

【IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization ｜冲突感知指令融合的多查询生成式引擎优化

研究机构：中国科学技术大学

作者：Heyang Zhou、JiaJia Chen、Xiaolu Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13938)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13938)

> 生成式引擎优化（GEO）旨在通过修改文档内容提升其在生成式搜索答案中的引用可见性。现有方法将多查询优化视为单维问题，导致针对单一查询的修改往往损害其他查询的可见性，形成竞争性失衡。IF-GEO 提出“发散-收敛”框架，通过挖掘潜在查询并执行冲突感知的指令融合，生成全局修订蓝图以协调竞争需求。该方法在稳定性指标上显著优于基线，但其依赖模拟引擎且未解决真实商业环境下的对抗性风险。

】
