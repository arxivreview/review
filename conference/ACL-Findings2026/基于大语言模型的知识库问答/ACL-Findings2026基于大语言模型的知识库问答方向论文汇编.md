# ACL-Findings2026 · 基于大语言模型的知识库问答方向论文汇编

> 本方向共 17 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Dynamic Graph Navigation via Triplet Chains for Structure-Aware Retrieval-Augmented Generation ｜结构感知检索增强生成

作者：Feng Zhao、Yufei Wu、Xianggan Liu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e4de6fdb08b0)

> 检索增强生成（RAG）旨在通过外部知识缓解大语言模型（LLM）的幻觉，但传统RAG在简单问题上引入噪声，在复杂问题上缺乏结构。现有方法往往孤立处理文本或图谱，未能有效协同。本文提出Trig-Nav，通过三元组链分解问题并动态构建子图，实现多视角知识检索。该方法在开放域问答上优于基线，但其对动态子图构建质量的依赖及在多跳推理中的局限尚存疑。

】

---

【EHRAG: Bridging Semantic Gaps in Lightweight GraphRAG via Hybrid Hypergraph Construction and Retrieval ｜高效超图检索增强生成

研究机构：香港科技大学

作者：Yifan Song、Xingjian Tao、Zhicheng Yang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17458)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17458)

> 多跳问答中，轻量级图检索方法因仅依赖实体共现而忽略语义关联，导致推理链在跨文档同义实体间断裂。EHRAG 通过构建融合结构共现与语义聚类的混合超图，并采用扩散激活机制，在保持线性索引复杂度的同时弥补了这一语义缺口。该方法在 2WikiMultiHop 上较最强基线提升 6.9% 的 LLM 准确率，但其在复杂领域语料中的泛化能力及超图参数自适应机制仍存疑。

】

---

【EvoMemKG: An Evolvable Memory Agent for Multi-hop Knowledge Graph Reasoning ｜可进化记忆智能体：多跳知识图谱推理中的状态压缩与策略复用

研究机构：北京邮电大学

作者：Shiyu Tian、Shuyue Xing、Zhuoxin Han 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1aadeeb98d61)

> 多跳知识图谱问答（KGQA）面临的核心矛盾是LLM有限上下文窗口与图搜索空间指数级增长之间的冲突，导致推理链断裂或信息丢失。现有智能体框架多采用静态记忆，无法在长轨迹中维持全局状态，且各查询独立处理，缺乏跨任务经验复用。EvoMemKG通过引入双层动态记忆架构，将工作记忆用于单任务内的关系压缩，经验记忆用于跨任务的策略蒸馏，实现了推理过程的持续进化。该方法在零样本设置下显著提升了复杂多跳查询的准确性，但其性能增益对骨干模型能力的依赖程度及在稀疏本体上的鲁棒性仍存疑。

】

---

【Interactive Semantic Parsing with Reinforcement Learning for Knowledge Graph Reasoning ｜交互式语义解析与距离引导强化学习

研究机构：南京大学、中国科学院大学

作者：Yurun Song、Xiangqing Shen、Jianfei Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6e2bb63410ae)

> 知识图谱问答（KBQA）的核心矛盾在于大语言模型（LLM）的语义泛化能力与知识图谱（KG）的事实精确性之间的张力。现有智能体方法依赖预定义工具进行图遍历，导致拓扑导航与逻辑约束（如时间过滤、聚合）解耦，造成检索不精确与后处理负担；传统语义解析虽能生成可执行逻辑形式，却严重依赖稀缺的金标准标注。本文切入点是将推理重构为可执行逻辑子句的序列生成，并通过基于KG拓扑距离的稠密过程奖励实现无标注强化学习。该方法在WebQSP与CWQ上取得SOTA性能，但其3B小模型在复杂多跳任务上的表现仍低于部分2025-2026年基于大模型的基线，且距离奖励对长程推理的信用分配效果缺乏跨域验证。

】

---

【Iterative Knowledge Graph Refinement and Integration for Medical Question Answering ｜迭代知识图谱精炼与整合用于医疗问答

作者：Haochen Zou、Yongli Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_11cf0445b7f4)

> 医疗问答中，大语言模型（LLM）常因缺乏外部事实约束而产生幻觉，而现有图检索增强生成（Graph-based RAG）方法在检索子图时易引入冗余噪声，导致推理链断裂。本文提出一种迭代式框架，通过“选择性检索+GNN剪枝+充分性判断”循环，构建简洁且信息丰富的证据子图。该方法在三个医疗基准上取得SOTA性能，但其对长文本问题的敏感性以及缺乏通用KBQA基准的对比，限制了其泛化性的验证。

】

---

【LLM-KT: Enhancing Large Language Models with Knowledge Tracing via Multi-Level Plug-and-Play Alignment ｜知识追踪中的多模态对齐

研究机构：华东师范大学

作者：Ziwei Wang、Jie Zhou、Qin Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b9cecb9d0677)

> 知识追踪（Knowledge Tracing, KT）旨在基于学生历史作答记录预测其未来表现，传统方法依赖题目ID序列建模行为动态，但缺乏对题目文本语义与前置概念的深层推理能力。现有LLM直接微调或提示方案因无法有效捕捉ID序列的时序依赖及长文本上下文而失效。本文提出LLM-KT，通过“行为动力学投影器”与“语义历史投影器”将传统序列模型嵌入与压缩文本嵌入注入LLM，实现多模态对齐。该框架在四个基准上取得SOTA，但依赖外部序列模型作为编码器，其独立泛化能力存疑。

】

---

【Momoka-RAG: MCTS-Organized Mapping of Knowledge Associations for Long-Document Retrieval Augmented Generation ｜Momoka-RAG：基于蒙特卡洛树搜索的长文档检索增强生成

研究机构：华南理工大学

作者：Wenyu Tao、Xiaofen Xing、Zeliang Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3baf3e966179)

> 长文档检索增强生成（Retrieval-Augmented Generation, RAG）旨在解决大语言模型（LLM）在处理超长文本时因上下文窗口限制与噪声干扰导致的事实幻觉问题。现有主流框架如RAPTOR与GraphRAG依赖固定规则或统计特征构建知识结构，仅能捕捉表层关联，无法挖掘跨段落的深层语义依赖。Momoka-RAG将蒙特卡洛树搜索（MCTS）从检索阶段迁移至索引阶段，以语义补全为目标主动探索Chunk间的最优信息路径，并在检索时通过混合粒度扩展与重排序获取精准上下文。该框架在长文档任务上实现了精度与召回率的平衡，但其预计算路径机制牺牲了对特定查询的动态适应性，且未验证跨文档场景下的有效性。

】

---

【Q2EI: Query-to-Entity Inference for Semantic Condensation in Domain-Specific Retrieval ｜生成式查询压缩（GQC）：从现象描述到实体锚点的检索对齐

作者：Yixuan Sun、Zhenqin Xu、HanFeng Zhai 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f36cf04c76b7)

> 领域特定检索面临的核心矛盾是用户非专业查询（Lay Query）与专业文档间的语义空间错位，导致稀疏与稠密检索器均难以建立有效映射。现有生成式查询扩展（GQE）方法通过补充上下文弥合差距，但在垂直领域易引入冗余噪声并引发语义漂移。本文提出生成式查询压缩（GQC）策略，将重写过程从“加法”转为“减法”，通过推断核心实体生成高密度查询表示。该策略在医疗与法律基准上显著优于扩展基线，但其对LLM参数化知识准确性的依赖及在复杂多跳场景下的适用性仍存疑。

】

---

【Query-Aware Graph Attention for Precise Subgraph Retrieval in Knowledge-Augmented Reasoning ｜查询感知图注意力子图检索

研究机构：西北工业大学

作者：Yuanye Xu、Linyi Guo、Yue Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_81c772ea6e1c)

> 知识图谱问答（KGQA）的核心矛盾在于大语言模型（LLM）的语义泛化能力与知识图谱（KG）事实精确性之间的张力，现有检索增强生成（RAG）方法因忽视查询语义与关系类型的交互，导致多跳证据检索不精确。本文切入点在于将查询嵌入与关系嵌入直接注入图注意力机制，实现三元组级别的细粒度评分。QSRAG通过查询-关系图注意力网络（QR-GAT）构建高置信度子图，仅需单次LLM调用即可提升推理准确性。该方法在检索指标上确立了新基准，但其单次推理范式在极高复杂度查询下的鲁棒性仍存疑。

】

---

【RiTeK: A Dataset for Large Language Models Complex Reasoning over Textual Knowledge Graphs in Medicine ｜医疗文本知识图谱复杂推理基准

研究机构：美国康涅狄格大学、美国亚利桑那州立大学

作者：Jiatan Huang、Mingchen Li、Zonghai Yao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.13987)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9c02b56f1cec)

> 医疗场景下的复杂问答要求模型同时满足结构化关系约束与非结构化文本语义约束，而现有知识图谱问答（KBQA）基准多局限于纯关系路径或稀疏文本，无法评估这种联合推理能力。通用检索增强生成（RAG）方法在缺乏丰富文本描述与多样拓扑结构时，难以处理医疗领域特有的约束满足与多跳依赖。本文构建了包含6种拓扑结构与专家验证文本属性的医疗文本知识图谱（TKG）基准RiTeK，并系统评估了11种检索方法。该工作填补了医疗TKG复杂推理的评估空白，但现有方法在文本-关系联合约束下的低性能揭示了当前检索范式的根本局限。

】

---

【RouteRAG: Efficient Retrieval-Augmented Generation from Text and Graph via Reinforcement Learning ｜路由增强生成

研究机构：中国科学院、中国科学院大学

作者：Yucan Guo、Miao Su、Saiping Guan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09487)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09487)

> 检索增强生成（RAG）旨在通过外部知识缓解大语言模型（LLM）的事实幻觉，但现有图基RAG系统通常采用一次性检索，无法适应多跳推理中动态变化的信息需求，且图检索计算开销远高于文本检索。本文切入点在于利用强化学习（RL）训练统一策略，使模型自主决定何时、从何种知识源（文本、图或混合）检索证据。RouteRAG通过两阶段组相对策略优化（GRPO）框架，先优化答案准确性，再引入效率奖励抑制冗余检索。该方法在五个问答基准上显著超越基线，但其有效性依赖于特定骨干模型与训练数据分布，在结构化知识图谱查询（KBQA）场景下的逻辑可执行性尚未验证。

】

---

【Subgraph-Guided Executable Logical Form Generation for Knowledge Base Question Answering ｜子图引导的可执行逻辑形式生成

研究机构：北京理工大学、澳大利亚国立大学

作者：Yuhang Tian、Dandan Song、Zhijing Wu 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_498c2d850d43)

> 知识库问答（KBQA）的核心矛盾在于大语言模型（LLM）强大的语义泛化能力与知识图谱（KG）事实精确性之间的张力，现有检索增强方法因孤立检索实体与关系而丢失了图谱的拓扑结构信息，导致生成的逻辑形式不可执行。本文提出 SELF-KBQA 框架，通过预测核心推理模式（CRP）并检索结构对齐的子图，为 LLM 提供拓扑完整的证据上下文以生成可执行逻辑形式。该方法在 GrailQA 上实现了 82.33 的整体精确匹配（EM），但受限于两跳以内的 CRP 模式覆盖，对长程推理的显式建模能力存疑。

】

---

【TagRAG: Tag-guided Hierarchical Knowledge Graph Retrieval-Augmented Generation ｜标签引导层级知识图谱检索增强生成

研究机构：华东师范大学

作者：Wenbiao Tao、Xinyuan Li、Yunshi Lan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05254)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_24024a03b6d9)

> 现有图检索增强生成（GraphRAG）方法依赖大规模大语言模型（LLM）进行社区检测与摘要，导致构建成本高昂且难以支持增量更新，无法在低资源场景下实现高效的全局知识推理。本文切入点在于将图构建从“自底向上的社区发现”重构为“自顶向下的标签链组织”，通过预定义领域标签挂载与层级融合，解耦了LLM对全局图结构的端到端依赖。TagRAG通过提取对象标签并挂载至预定义根领域标签形成有向无环图（DAG），在推理时检索领域中心摘要以生成全局答案。该方法在低资源小模型上实现了优于主流基线的性能与效率，但其依赖预定义标签体系，在开放域泛化能力上存在未验证的边界。

】

---

【TopoRAG: Graph-based RAG via Topology-aware Approximate Nearest Neighbor Search ｜拓扑感知检索增强生成

研究机构：新加坡南洋理工大学

作者：Tianhao Wu、Siqiang Luo

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_65f972bca120)

> 图结构检索增强生成（Graph-RAG）旨在利用实体间关系提升大语言模型（LLM）的事实准确性，但现有两阶段“先检索后扩展”范式常引入噪声与高枢纽节点，导致上下文冗余与语义偏离。TopoRAG 指出该失效源于检索阶段未整合图拓扑，进而提出直径约束近似最近邻搜索（DC-ANNS），将结构连贯性作为硬约束嵌入检索过程。该方法通过单阶段联合评估嵌入相似度与图直径，直接获取紧致子图，避免了启发式扩展的副作用。尽管其在多跳问答基准上表现优于基线，但缺乏具体数值披露与延迟对比，其实际部署效率与长尾实体召回能力存疑。

】

---

【TRACE: An Experiential Framework for Coherent Multi-hop Knowledge Graph Question Answering ｜轨迹感知推理与自适应上下文

研究机构：阿联酋扎耶德大学、香港城市大学

作者：Yingxu Wang、Jiaxin Huang、Mengzhu Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_37dd064c7f6b)

> 多跳知识图谱问答（KGQA）要求模型在关系路径上维持语义连贯，但现有智能体方法常将每步决策孤立处理，导致推理漂移与重复探索。TRACE 通过动态生成自然语言叙事维持上下文一致性，并将历史探索轨迹抽象为可复用先验，以双反馈重排序机制融合局部语义与全局经验。该框架在 WebQSP 上取得 91.6 的 Hits@1，但在 CWQ 复杂组合推理上落后于最新记忆优化方法，其经验先验机制的泛化边界尚待验证。

】

---

【Which bird does not have wings: Negative-constrained KGQA with Schema-guided Semantic Matching and Self-directed Refinement ｜负约束知识图谱问答

研究机构：韩国延世大学

作者：Midan Shim、Seokju Hwang、Kaehyun Um 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14749)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14749)

> 知识图谱问答（KGQA）旨在利用结构化知识回答自然语言问题，其核心价值在于缓解大语言模型（LLM）语义泛化能力与知识图谱（KG）事实精确性之间的张力。现有语义解析（SP）方法在处理包含否定逻辑的复杂约束时，常因逻辑形式表达力不足或生成不可执行查询而失效。本文提出NEST KGQA任务与CUCKOO框架，通过Python格式逻辑形式（PyLF）显式建模负约束，并引入模式引导语义匹配与自导向精炼机制确保查询可执行性。该工作填补了负约束评估空白，但在通用基准上的性能仍落后于最新检索增强生成（RAG）方法，其泛化边界有待进一步验证。

】

---

【ZoomRAG: Hierarchical Random-walk Zooming across Multi-scale Information Graphs for Fast and Accurate RAG ｜多尺度图随机游走检索增强生成

研究机构：华东师范大学、复旦大学

作者：Xianming Hu、Jingyang Chen、Bin Tang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f81481820a62)

> 检索增强生成（RAG）旨在通过外部知识缓解大语言模型（LLM）的幻觉，但现有方法在构建紧凑离线索引与实现低延迟在线检索间存在矛盾。主流图结构RAG依赖昂贵的知识图谱（KG）构建或复杂的树状摘要，导致离线成本高且难以并行处理高并发查询。本文提出ZoomRAG，通过多尺度图上的分层随机游走实现粗到细的证据定位，并引入算法并行机制。该方法在保持SOTA准确率的同时，将在线检索延迟降至0.019秒，但其在缺乏显式关系语义的轻量图结构下对复杂逻辑推理的鲁棒性尚存疑。

】
