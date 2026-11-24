# ICLR2026 · 基于图的LLM推理方向论文汇编

> 本方向共 10 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Explore-on-Graph: Incentivizing Autonomous Exploration of Large Language Models on Knowledge Graphs with Path Refined Reward Modeling ｜探索图上的自主推理：基于路径精炼奖励的大语言模型强化学习框架

研究机构：清华大学

作者：Shiqi Yan、Yubo Chen、Ruiqi Zhou 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60347428)

> 导读 大语言模型在知识图谱问答中常因模仿训练数据的分布限制而失效于分布外推理模式。现有规则约束或模仿学习范式无法覆盖未见过的关系组合，导致复杂多跳任务泛化能力不足。本文提出EoG框架，通过两阶段强化学习驱动模型在图结构上自主探索未知路径，并引入路径精炼奖励优化探索效率。该方法在五个基准上超越闭源模型，但RL训练的高计算成本与静态图假设限制了其实际部署的灵活性。

】

---

【G-reasoner: Foundation Models for Unified Reasoning over Graph-structured Knowledge ｜统一图结构推理基础模型

研究机构：澳大利亚莫纳什大学、南京大学

作者：Linhao Luo、Zicheng Zhao、Junnan Liu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24276)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24276)

> 大语言模型（LLM）在处理知识密集型任务时，因参数化知识的静态性导致多跳推理断裂，而现有图增强检索生成（GraphRAG）方法依赖特定图结构或高延迟智能体，难以跨域泛化。G-reasoner 提出 QuadGraph 统一接口与 34M 参数图基础模型（GFM），将图推理从“启发式检索”转化为“端到端预测”。该方法在六个基准上超越基线，但依赖预训练文本编码器作为教师，且未验证动态图场景下的鲁棒性。

】

---

【Knowledge Reasoning Language Model: Unifying Knowledge and Language for Inductive Knowledge Graph Reasoning ｜知识推理语言模型：统一知识与语言的归纳式知识图谱推理

研究机构：合肥工业大学、南京大学

作者：Xingrui Zhuo、Jiapu Wang、Gongqing Wu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13909)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13909)

> 归纳式知识图谱推理（Inductive KGR）旨在处理包含未见实体和关系的开放域知识图谱，核心挑战在于模型如何泛化到陌生结构。现有基于大语言模型（LLM）的知识图谱基础模型（KGFM）直接将稀疏图谱上下文注入提示词，导致LLM内在的稠密知识被稀疏证据覆盖，引发不可逆的“知识扭曲”。KRLM通过设计知识推理语言（KRL）指令格式与KRL分词器，将实体与关系映射为统一Token，并在注意力层引入动态知识记忆机制，实现了LLM内在知识与图谱结构知识的端到端协调。该方法在28个归纳式KGR数据集上验证了零样本与微调场景下的优越性，但其静态前向推理机制在长程多跳任务中的有效性仍存疑。

】

---

【PLAN-ANSWER-REFINE ON-GRAPH: STRUCTURED - PLANNING AND SELF-REFINEMENT FOR LARGE LAN GUAGE MODEL REASONING ON KNOWLEDGE GRAPHS ｜计划-回答-精炼图推理

研究机构：浙江大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19717879)

> 知识图谱（KG）增强的大语言模型（LLM）推理旨在解决多跳查询中的逻辑断裂与幻觉问题，但现有线性遍历方法常因过早剪枝导致正确实体丢失，且过度依赖检索证据会放大错误。本文切入点在于利用 SPARQL 结构化监督训练小模型生成组合式规划，并引入“先答后修”机制以隔离参数知识与外部证据。通过 Llama-3.1-8B 规划器与 GPT-4 推理器的协同，PARoG 在 WebQSP 等基准上超越了 PoG 等基线，但其性能仍低于 2026 年最新 SOTA，且对 KG 覆盖率依赖较高。

】

---

【QUERY-AWARE FLOW DIFFUSION FOR GRAPH-BASED RAG WITH RETRIEVAL GUARANTEES ｜查询感知流扩散图检索

作者：Zhuoping Zhou、Davoud Ataee Tarzanagh、Sima Didari 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26588181)

> 图增强检索生成（GraphRAG）旨在利用知识图谱（KG）的拓扑结构缓解大语言模型（LLM）在多跳推理中的幻觉，但现有方法多采用静态社区检测或邻域提取，忽略了查询语义对子图质量的动态约束。本文切入点在于将子图检索重构为查询感知的流扩散优化问题，通过动态边权引导质量沿语义对齐路径传播。具体做法是引入基于嵌入相似度的查询感知边权重，结合Push-Relabel算法求解对偶问题，实现训练-free的自适应检索。该框架提供了子图恢复的统计保证，但在训练-free设定下，其性能上限显著低于训练式方法，且对逻辑否定等复杂语义的处理能力存疑。

】

---

【RAS: RETRIEVAL-AND-STRUCTURING FOR KNOWLEDGE-INTENSIVE LLM GENERATION ｜检索与结构化：动态构建问题特定知识图谱

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、谷歌DeepMind

作者：Pengcheng Jiang、Lang Cao、Ruike Zhu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2502.10996)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94391141)

> 大语言模型（LLM）在处理知识密集型任务时，常因检索到的非结构化文本缺乏显式逻辑连接而产生幻觉。现有检索增强生成（RAG）方法依赖静态全局知识图谱或一次性文本检索，前者构建成本高昂且引入无关噪声，后者难以支撑多跳推理。本文提出检索与结构化（Retrieval-And-Structuring, RAS）框架，在推理时动态构建问题特定知识图谱，通过迭代规划与三元组提取实现结构化推理。RAS在七个基准上取得最高8.7%的提升，但其对全局结构一致性的牺牲及在标准知识图谱问答（KGQA）任务上的表现仍存疑。

】

---

【Topology of Reasoning: Retrieved Cell Complex-Augmented Generation for Textual Graph Question Answering ｜拓扑增强检索生成

研究机构：重庆大学

作者：Sen Zhao、Lincheng Zhou、Yue Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19240)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19240)

> 导读 文本图问答任务中，传统检索增强生成（RAG）仅依赖节点与边等低维结构，导致涉及闭环依赖的复杂推理出现逻辑断裂。现有图检索方法忽略了高维拓扑结构，无法捕捉实体间的循环关系。本文提出 TopoRAG，通过将文本图提升为细胞复形并引入多维拓扑推理，显式建模 2-维循环结构以增强推理忠实性。该方法在特定复杂查询上表现优异，但整体性能略低于当前静态图问答的最先进方法，且计算开销较高。

】

---

【VOG: ENHANCING LLM REASONING THROUGH STEP WISE VERIFICATION ON KNOWLEDGE GRAPHS ｜基于逐步验证与自适应上下文选择的图推理框架

研究机构：香港科技大学、日本筑波大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_96819363)

> 大语言模型（LLM）在知识密集型多跳推理中常因缺乏外部事实校验而产生幻觉与错误累积。现有图增强框架多采用静态检索或固定参数探索，无法在推理过程中动态修正中间步骤的逻辑偏差。本文提出 Verify-on-Graph (VoG) 框架，通过引入逐步验证机制与多臂老虎机（MAB）驱动的自适应上下文选择，实现推理计划的迭代修正。该框架在多个基准上优于现有智能体基线，但其性能提升主要依赖于特定骨干模型，且未解决大规模动态图下的实时性瓶颈。

】

---

【WHEN TO USE GRAPHS IN RAG: A COMPREHENSIVE - ANALYSIS FOR GRAPH RETRIEVAL-AUGMENTED GEN ERATION ｜图检索增强生成的适用边界诊断

研究机构：厦门大学、香港理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_98327036)

> 图检索增强生成（GraphRAG）旨在通过显式图结构弥补传统检索增强生成（RAG）在复杂逻辑推理中的断裂，但实证研究显示其在许多真实任务中性能反而低于基础RAG。现有基准因缺乏任务复杂度分级与领域语料密度控制，无法量化图结构的实际收益边界。本文构建了包含四级任务难度与双域语料的GraphRAG-Bench，通过全流程阶段特异性指标系统评估了图结构的增益条件。该工作提供了重要的诊断工具，但其结论受限于静态图评估，未涵盖动态探索机制对性能边界的潜在修正。

】

---

【YOUTU-GRAPHRAG: VERTICALLY UNIFIED AGENTS FOR GRAPH RETRIEVAL-AUGMENTED COMPLEX REASONING ｜垂直统一智能体图检索增强生成

研究机构：澳大利亚莫纳什大学、香港理工大学

作者：Junnan Dong、Siyu An、Yifei Yu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_76906286)

> 图检索增强生成（GraphRAG）旨在通过结构化图知识解决大语言模型（LLM）在多跳推理中的幻觉与逻辑断裂问题。现有方法通常将图构建与图检索作为独立模块优化，导致结构语义割裂，难以在域迁移时保持鲁棒性。本文提出 Youtu-GraphRAG，通过共享图模式（Graph Schema）垂直统一构建与检索流程，并引入双感知社区检测构建层级知识树。该框架在严格评估下显著提升了检索忠实性，但其依赖预定义模式扩展机制，在长尾知识捕获与动态图适应上存在潜在局限。

】
