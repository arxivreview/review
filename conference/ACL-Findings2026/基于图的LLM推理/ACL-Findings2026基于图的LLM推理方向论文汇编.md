# ACL-Findings2026 · 基于图的LLM推理方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Breaking the Static Graph: Context-Aware Traversal for Graph-Based RAG ｜打破静态图：基于上下文感知遍历的图增强检索

研究机构：香港科技大学、香港中文大学

作者：Kwun Hang Lau、Fangyuan Zhang、Boyu Ruan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_63e9a74eab77)

> 多跳问答中，基于知识图谱的检索常因静态边权导致随机游走陷入高度枢纽节点，造成证据链断裂。HippoRAG 2 等现有方法虽引入图结构，但索引期固定的转移矩阵无法响应查询意图，导致召回率虚高而推理完整性不足。CatRAG 通过引入符号锚定、查询感知动态边权及关键事实段落增强，将静态图转化为查询自适应导航结构。该方法在 MuSiQue 等基准上显著提升了全链检索率，但下游问答 F1 提升有限，且动态边权依赖 LLM 推理，其效率与复杂路径回溯能力存疑。

】

---

【Colorful Talks with Graphs: Human-Interpretable Graph Encodings for Large Language Models ｜色彩化图结构编码

作者：Angelo Zangari、Peyman Baghershahi、Sourav Medya

论文原文见 [arXiv](https://arxiv.org/abs/2602.10386)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.10386)

> 大语言模型（LLM）在处理图结构任务时，常因将图线性化为文本序列而丢失拓扑信息，导致多跳推理失效。现有方法多采用任意数值ID或连续嵌入，这些符号对LLM而言语义不透明，无法利用其预训练的语言先验。本文提出基于有序Weisfeiler-Leman（WL）精炼的结构编码，将节点标签映射为人类可解释的颜色词，以弥合图结构与LLM语言空间的鸿沟。该方法在节点分类与图算法任务上显著优于基线，但其性能依赖于颜色粒度与图规模的匹配，且未验证在大规模动态图上的泛化能力。

】

---

【FlowRAG: Synergizing Explicit Reasoning via Frequency-Aware Multi-Granularity Graph Flow ｜频率感知多粒度图流检索增强生成

研究机构：华东师范大学、丰田研究所

作者：Bihao Zhan、Zongsheng Cao、Jie Zhou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.17856)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.17856)

> 现有图检索增强生成（GraphRAG）方法在处理抽象查询时面临实体稀疏导致的检索不足，且在多跳推理中易受噪声干扰导致路径断裂。本文指出，隐式拓扑评分无法有效区分核心实体与偶然提及，且缺乏宏观语义锚点。FlowRAG 通过构建四级异构图并引入频率感知加权流算法，将隐式随机游走转化为显式逻辑骨架提取。该方法在复杂多跳基准上超越了 LinearRAG 和 HippoRAG，但其性能提升主要依赖于静态图结构的优化，未解决动态知识更新下的实时性问题。

】

---

【Graph Explorer: Training Faithful KG Agents with Visibility-Grounded Supervision ｜可见性接地监督下的知识图谱智能体训练

研究机构：美国波士顿大学、美国华盛顿大学

作者：Yifeng Chen、Sicheng Wan、Tianyi Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f56700b99c2c)

> 知识图谱问答（KGQA）智能体在探索图结构时，常因上下文窗口限制而面临“幻觉参数”问题，即模型试图调用未在提示中出现的实体标识符。现有提示工程方法无法提供可靠的步骤级监督，而直接转换专家查询又因全局视图与局部视图的冲突导致监督失效。本文提出一种自动数据合成管线，将专家SPARQL编译为线性工具计划，并通过“可见性检查”过滤不可执行轨迹，实现动作中心微调。该方法在严格协议下显著提升了小模型的工具调用可靠性，但其对数据分布的潜在偏差及跨域泛化能力尚存疑。

】

---

【Graph-Assisted Large Language Models: A Perspective on Mitigating Intrinsic Limitations ｜图辅助大语言模型：从能力缺陷修复视角的系统性综述

研究机构：中国科学院、中国科学院大学

作者：Haitong Luo、Fali Wang、Weiyao Zhang 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4de848f22274)

> 大语言模型（LLM）在知识时效性、线性推理局限及多智能体协作僵化上存在固有缺陷，现有研究多聚焦于单一维度的图应用，缺乏对图结构如何系统性缓解这些局限的统一视角。本文切入点在于将图结构视为修复LLM内在缺陷的通用工具，而非仅作为外部检索源。通过构建涵盖参数化知识增强、非参数化检索、推理规划及协作优化的五维分类体系，本文整合了从知识注入到动态智能体编排的全链路方法。该综述提供了领域全景地图，但其分类边界在动态协作场景下的量化评估标准仍显模糊。

】

---

【Thought-Action Graph Reasoning: Faithful and Efficient Reasoning of Large Language Models via Reusing Past Experience ｜思维-行动图推理

研究机构：清华大学、北京邮电大学

作者：Zhixiao Qi、Feng Huang、Yunqi Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f11bc27dbf52)

> 知识图谱问答（KGQA）的核心矛盾在于大语言模型（LLM）在线探索知识图谱（KG）时的高延迟与错误累积。现有检索方法泛化差，智能体方法效率低，均忽略了从历史交互中复用推理逻辑的可能性。本文提出思维-行动图（Thought-Action Graph, TAG），将成功的LLM-KG交互轨迹蒸馏为可检索的操作蓝图，通过离线检索替代在线试错。该范式在WebQSP上达到93.2%的Hits@1，但GrailQA上的46.3%暴露了其在复杂泛化场景下的局限。

】
