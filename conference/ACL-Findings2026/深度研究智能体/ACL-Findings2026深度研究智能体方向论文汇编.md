# ACL-Findings2026 · 深度研究智能体方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Benchmarking Agentic Newswriting via Journalistic Workflows ｜新闻智能体写作基准

作者：Yen-Che Chien、Kuang-Da Wang、Wei-Yao Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ba8b61ebf6cc)

> 深度研究智能体（DRA）旨在让大语言模型自主处理开放式、长周期的高复杂度信息检索与整合任务，其核心价值在于突破静态检索的局限。现有方法多聚焦通用问答或报告生成，缺乏对时间敏感、需主动发现缺失背景的真实新闻工作流的评估。本文切入点在于将新闻写作形式化为受发布时间约束的迭代式搜索-编辑-重述过程，通过双层评估协议分离证据选择对齐度与最终写作质量。该基准揭示了当前智能体在规划与叙事整合上的显著短板，但其评估依赖单一参考文章，泛化性存疑。

】

---

【Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation ｜动态图思维驱动的认知智能体框架

作者：Chen Lifan、Wei Ding、Jingwen Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a79cbcf5c9b5)

> 金融报告生成要求在开放且充满噪声的环境中，将碎片化数据重构为逻辑严密的专业叙事，传统静态推理架构无法应对实时市场中的“未知未知”。现有方法要么依赖预定义工作流导致适应性不足，要么缺乏垂直领域的深度专业知识。Cogito 通过引入动态图思维（Dy-GoT）实现推理拓扑的运行时演化，并结合社会协作机制协调多智能体分工。该框架在自建金融基准上超越了闭源商业系统，但其依赖高算力消耗且缺乏通用基准验证，泛化能力存疑。

】

---

【CriticSearch: Fine-Grained Credit Assignment for Search Agents via a Retrospective Critic ｜回顾性批评家驱动的细粒度信用分配

作者：Yaocheng Zhang、Haohuan Huang、Zijun Song 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b3306c177224)

> 深度研究智能体在长程搜索任务中面临稀疏结果奖励导致的训练不稳定与策略收敛缓慢问题，现有强化学习方法难以区分轨迹内关键决策与冗余步骤。CriticSearch 引入回顾性批评家机制，利用训练时独有的金标答案与完整轨迹特权信息，对每个搜索动作进行事后评估，生成密集的回合级奖励信号。该方法将全局优势与回合级优势混合，替代传统稀疏奖励，显著提升了多跳问答任务的训练效率与最终性能。尽管在标准基准上表现优异，但其对金标答案的强依赖限制了在开放式无标准答案任务中的直接适用性。

】

---

【DeepPlanner: Scaling Planning Capability for Deep Research Agents via Advantage Shaping ｜深度规划器：通过优势整形扩展深度研究智能体的规划能力

研究机构：香港科技大学、美国加州大学圣迭戈分校

作者：Wei Fan、Wenlin Yao、Zheng Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12979)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12979)

> 深度研究智能体在长程任务中常因规划阶段的不确定性而陷入执行漂移，现有强化学习方法难以将规划阶段的高熵转化为性能提升。本文指出规划Token在训练中持续保持高熵，表明其优化潜力未被挖掘。DEEPPLANNER通过熵基优势整形与选择性优势加权，在更少训练资源下实现了SOTA性能。其价值在于证明了针对性优势整形比单纯扩大数据规模更有效，但评估局限于多跳问答，未验证在开放式报告生成中的泛化性。

】

---

【DeepSynth-Eval: Objectively Evaluating Information Consolidation in Deep Survey Writing ｜深度合成评估基准

作者：Hongzhi Zhang、Yuanze Hu、Tinghai Zhang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_07078d88d367)

> 深度研究智能体（Deep Research Agents, DRA）的核心瓶颈已从信息检索转移至海量证据的结构化整合，但现有评估体系因混淆检索噪声与合成能力、依赖主观评分而失效。本文通过逆向工程高质量综述，构建隔离检索的“Oracle Context”与细粒度清单指标，将开放式报告评估转化为可验证的客观任务。实验表明，多轮智能体工作流显著优于单轮生成，但百篇级文献的综合仍是当前模型的硬瓶颈。该基准填补了“检索后合成”的评估空白，但其封闭世界设定是否高估了开放环境下的真实能力，尚存争议。

】

---

【HiRAS: A Hierarchical Multi-Agent Framework for Paper-to-Code Generation and Execution ｜层级监督多智能体框架

作者：Hanhua Hong、Yizhi LI、Jiaoyan Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d47401e236b)

> 科研复现任务要求智能体从论文文本生成可执行代码并验证结果，但现有顺序流水线缺乏全局纠错机制，导致早期错误在后续阶段不可逆地传播。HIRAS 通过引入主动检查中间产物的层级管理器，将固定调用序列改造为动态监督循环，解决了执行阶段因依赖关系错误导致的崩溃问题。该框架在开源模型上实现了超越专有模型基线的复现准确率，但其评估协议修正与计算开销的权衡仍需进一步审视。

】

---

【PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers ｜PaperScope：面向大规模科学文档的多模态智能体深度研究基准

研究机构：中国人民大学

作者：Lei Xiong、Huaying Yuan、Zheng Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11307)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11307)

> 深度研究智能体在开放网络文本上的评估已相对成熟，但真实科研流程依赖本地存储的海量多模态文档（论文、报告），现有基准无法覆盖跨文档、跨模态的证据整合。本文通过知识图谱引导的随机游走采样构建大规模本地语料，并设计四类任务评估智能体在科学深度研究中的检索、推理与生成能力。实验显示，即便最先进的智能体在复杂多模态推理上仍表现不佳，揭示了当前系统在长上下文科学文档处理上的显著局限。

】

---

【Rerank Before You Reason: Analyzing Reranking Tradeoffs through Effective Token Cost in Deep Search Agents ｜重排优先于推理：深度搜索智能体中的有效Token成本分析

研究机构：加拿大滑铁卢大学

作者：Sahel Sharifymoghaddam、Jimmy Lin

论文原文见 [arXiv](https://arxiv.org/abs/2601.14224)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_30116f5662b4)

> 深度研究智能体在迭代检索与推理中面临测试时计算开销激增的困境，单纯增加推理预算往往导致边际收益递减且成本高昂。现有效率优化多聚焦于上下文压缩，却忽视了检索阶段重排对下游推理质量的杠杆作用。本文在BrowseComp-Plus基准上引入有效Token成本（Effective Token Cost, ETC）指标，量化重排深度与推理预算的权衡，证明适度重排能以更低成本实现更高准确率。该结论在固定语料库下成立，但向动态Web环境的泛化能力仍存疑。

】

---

【Table-as-Search: Agentic Information Seeking is Table Completion ｜表格化搜索（TaS）：将长程信息检索重构为表格补全任务

作者：Tian Lan、Felix Henry、Bin Zhu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19cc84e6eb7b)

> 长程智能体信息检索面临的核心困境是：在追踪数千条搜索结果与规划步骤时，非结构化文本上下文导致关键证据丢失与状态失真。现有基于 ReAct 范式的多智能体框架虽通过上下文摘要或隔离缓解压力，但本质上仍依赖有限的文本窗口管理海量状态，无法从根本上解决“中间迷失”问题。本文提出 Table-as-Search (TaS) 框架，将信息检索任务显式重构为外部数据库中的表格补全问题，以结构化单元格状态替代自由文本轨迹。该架构在 DeepSearch 与 WideSearch 基准上超越了同等算力下的多智能体基线，但其对复杂非结构化证据的整合能力及与端到端强化学习方法的相对优势仍存疑。

】
