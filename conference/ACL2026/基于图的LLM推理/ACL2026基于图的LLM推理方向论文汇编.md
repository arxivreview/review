# ACL2026 · 基于图的LLM推理方向论文汇编

> 本方向共 7 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CoG: Controllable Graph Reasoning via Relational Blueprints and Failure-Aware Refinement over Knowledge Graphs ｜基于关系蓝图与失败感知修正的知识图谱可控推理

研究机构：浙江大学

作者：Yuanxiang Liu、Songze Li、Xiaoke Guo 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11047)

> 知识图谱增强的大语言模型（LLM）智能体在多跳推理中常因邻域噪声导致轨迹震荡，现有方法缺乏自适应策略调节，即“认知刚性”。CoG 通过离线构建关系蓝图作为软结构先验，结合在线失败感知回溯，在零训练条件下稳定了推理路径。该框架在 WebQSP 和 CWQ 上显著优于现有智能体基线，但其对训练集分布的依赖及在动态图谱下的泛化能力仍存疑。

】

---

【Collision to Cognition: Hash-Driven Graph Construction for Efficient RAG ｜基于哈希碰撞的轻量级图构建框架

研究机构：香港理工大学、澳大利亚莫纳什大学

作者：Chuang Zhou、Zheng Yuan、Linhao Luo 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_33ac5eaef204)

> 检索增强生成（RAG）在处理多跳推理时，常因文本扁平化导致逻辑链条断裂，而现有图增强方法依赖大语言模型（LLM）提取三元组或密集向量聚类，构建成本高且缺乏可解释性。本文提出 MeshRAG，利用局部敏感哈希（LSH）替代神经嵌入，通过哈希碰撞自动构建双层语义图，以位运算实现高效检索。该框架在 HotpotQA 等基准上取得 64.2% 的匹配准确率，优于 HippoRAG2 等基线，但其哈希机制对细粒度语义区分度的影响及长尾实体召回能力尚存疑。

】

---

【Constructing coherent spatial memory in LLM agents through graph rectification ｜基于版本控制与影响评分的LLM导航图修复框架

研究机构：德国慕尼黑工业大学

作者：Puzhen Zhang、Xuyang Chen、Yu Feng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04195)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04195)

> 长程文本导航中，LLM增量构建的空间拓扑图常因早期感知错误累积导致结构冲突，现有方法缺乏对因果错误的时间溯源能力。本文切入点在于引入版本控制机制记录图编辑历史，结合边影响评分定位低风险修复点。通过冲突检测、错误定位与影响感知修正的三阶段流水线，实现导航图的自洽性维护。该方法在MANGO基准上显著提升了结构完整性，但其修复准确率仍受限于LLM对空间语义的底层理解偏差。

】

---

【Evaluating LLMs on Large-Scale Graph Property Estimation via Random Walks ｜基于随机游走统计的大规模图属性估计基准

研究机构：日本东京大学

作者：Sunil Kumar Maurya、Xin Liu

论文原文见 [arXiv](https://arxiv.org/abs/2605.01484)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.01484)

> 现有 LLM 图推理基准受限于上下文窗口，仅能处理 20-50 个节点的小图，无法评估模型在真实世界百万级节点图上的能力。本文切入点在于将任务从“全图精确算法执行”转变为“局部访问下的全局属性统计估计”，通过随机游走统计量替代全图编码，将提示长度压缩 559 倍。实验表明，推理型 LLM 在节点数估计上的中位相对误差可低于 20%，部分场景优于经典无偏采样基线，但其对复杂拓扑结构的捕捉能力仍存疑。

】

---

【LogosKG: Hardware-Optimized Scalable and Interpretable Knowledge Graph Retrieval ｜硬件对齐的知识图谱高跳检索框架

作者：He Cheng、Yifu Wu、Saksham Khatwani 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18913)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b2cf3e28fdef)

> 大语言模型（LLM）在知识密集型任务中依赖外部知识图谱（KG）提供结构化证据，但现有检索系统在处理十亿级边图的高跳查询时，面临内存指数级膨胀与路径重建缺失的双重瓶颈。LogosKG 将图遍历转化为稀疏矩阵连乘，结合度感知分区与按需缓存，在单设备硬件上实现确定性的高跳检索。该框架解决了“检索效率”与“可解释性”难以兼得的系统级矛盾，但其静态矩阵假设是否适配动态图更新场景，仍存疑。

】

---

【Query-Aware Knowledge Retrieval via Hyperbolic Structuring ｜查询中心双曲图检索生成

研究机构：香港理工大学、美国史蒂文斯理工学院

作者：Chuang Zhou、Junnan Dong、Yilin Xiao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_edf4bd201a51)

> 多跳问答中，静态知识图谱常因缺乏查询特定的逻辑路径而导致推理断裂。现有GraphRAG方法依赖预定义的实体共现或聚类启发式，无法动态捕捉复杂查询所需的隐式关系。HyperRAG通过分解查询生成隐式边，并将融合后的图嵌入双曲空间以保留层级结构，实现了查询中心的动态图构建。该方法在三个基准上超越了静态基线，但其性能增益主要源于隐式边的引入，且双曲距离计算效率仍低于欧氏空间检索。

】

---

【TH-RAG : Topic-Based Hierarchical Knowledge Graphs for Robust Multi-hop Reasoning in Graph-based RAG Systems ｜层级知识图谱检索框架

研究机构：韩国汉阳大学

作者：JungHyoun Kim、Soohyeong Kim、Seok Jun Hwang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f9164f5de4f)

> 图增强检索生成（GraphRAG）旨在通过结构化知识缓解大语言模型（LLM）的多跳推理断裂与幻觉问题，但现有基于三元组的图构建常因连通性不足导致推理路径中断，而社区检测等增强手段又引入高计算成本与语义失真。本文切入点在于利用 LLM 一次性提取三元组、子主题与主题，构建三层语义层级图，以近零额外成本提升图连通性。该方法通过主题引导的自顶向下遍历与句子级证据过滤，在多个基准上超越了主流图检索基线。其价值在于平衡了结构完整性与计算效率，但层级标注的语义一致性依赖 LLM 的提取质量，跨域泛化能力仍受限于语料库的覆盖度。

】
