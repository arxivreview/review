# ACL2026最新论文 ｜Mnemis: Dual-Route Retrieval on Hierarchical Graphs for Long-Term LLM Memory ｜双路由层级图检索的长期记忆框架

作者：Zihao Tang、Xin Yu、Ziyu Xiao 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7789ca44ea8c)

> 长期交互中，LLM 需从海量历史消息中精准召回相关片段以维持上下文连贯性，但现有检索增强生成（RAG）方法依赖局部相似度匹配，在全局推理或枚举型查询中常因语义距离远而漏检关键信息。Mnemis 针对这一失效，提出融合 System-1 相似度搜索与 System-2 全局选择的双路由机制，通过构建层级图支持自上而下的刻意遍历。该框架在 LoCoMo 与 LongMemEval-S 基准上取得领先性能，但其层级图的周期性重建策略与 System-2 在时间推理上的局限性，使其在动态更新场景下的鲁棒性仍存疑。

## 研究背景

当 LLM 处理跨越数月或数年的对话历史时，其原生上下文窗口（如 128K tokens）无法容纳全部交互记录，直接输入全量文本会导致计算成本激增且注意力分散。为解决此问题，检索增强生成（RAG）范式通过存储历史消息片段（Episodes）并仅检索最相关部分来压缩输入，但其有效性高度依赖检索质量。传统 RAG 及基于图的 RAG（Graph-RAG）方法主要依赖嵌入相似度或 BM25 文本匹配，这种机制类似于人类认知中的 System-1 快速直觉反应，在处理局部语义匹配时高效，但在需要全局视角或综合覆盖所有相关信息的查询中表现乏力。

现有 Graph-RAG 方法（如 Nemori, Mem0）虽通过提取实体与边构建结构化图，提升了检索的语义丰富度，但其检索过程仍受限于“查询-片段”的局部相似度计算。例如，当用户询问“Dave 2023 年去了哪些城市”时，若某条消息中提及“在底特律参加了一个会议”，该消息与查询的语义相似度可能较低，导致被相似度阈值过滤掉。这种局部视角的盲区使得模型难以捕捉那些语义距离远但结构上关键的信息。Mnemis 的切入点在于引入 System-2 式的刻意推理机制，通过构建层级图（Hierarchical Graph）提供全局结构化视图，使模型能够进行自上而下的遍历，从而弥补相似度检索在全局覆盖上的不足。

## 核心方法

### 方法参照系

Mnemis 建立在 Graph-RAG 的基础流程之上，即从历史文本中提取实体（Entities）、边（Edges）和片段（Episodes）构建基础图（Base Graph），并支持基于嵌入和文本的相似度检索。与标准 Graph-RAG 的关键差异在于，Mnemis 额外构建了一个层级图，并引入了双路由检索机制，将被动相似度匹配与主动层级遍历相结合。

### 基础图与层级图构建

基础图存储原始历史消息及其结构化信息，支持 System-1 相似度搜索。其核心组件包括片段（Episodes）、实体（Entities）、边（Edges）和情景边（Episodic Edges）。实体提取采用增量式流程，新输入首先格式化为片段，基于时间戳检索近期片段作为上下文，LLM 识别实体名称并进行去重，随后提取实体的摘要、标签及关联片段。边则描述实体间可验证的关系，包含事实嵌入及有效时间范围。

层级图旨在支持 System-2 全局选择，将实体（Layer 0）抽象为多层类别（Categories）。构建过程遵循三个原则：最小概念抽象（Minimum Concept Abstraction），确保类别具体且信息丰富；多对多映射（Many-to-Many Mapping），允许一个子节点属于多个父类别以覆盖不同语义侧面；压缩效率约束（Compression Efficiency Constraint），规定每个类别至少包含 $n$ 个子节点，且高层节点数不超过低层。层级图的构建公式可表示为：

$$
C_i = \text{Abstract}(N_{i-1}, \text{Constraints})
$$

其中 $C_i$ 为第 $i$ 层类别集合，$N_{i-1}$ 为第 $i-1$ 层节点，$\text{Abstract}$ 为 LLM 驱动的抽象过程，$\text{Constraints}$ 包含压缩效率规则。这一设计解决了传统树状结构无法表达实体多重语义属性的问题，使全局遍历能沿多条路径检索信息。

### 双路由检索与重排序

检索阶段包含 System-1 相似度搜索与 System-2 全局选择。System-1 通过计算查询嵌入与片段/实体/边嵌入的余弦相似度，结合 BM25 全文搜索，使用倒数排名融合（RRF）合并结果：

$$
\text{RRF}(d) = \sum_{r \in R(d)} \frac{1}{k + \text{rank}_r(d)}
$$

其中 $R(d)$ 为包含文档 $d$ 的检索结果集，$k$ 为常数。System-2 则从层级图顶层开始，LLM 根据查询选择相关类别，逐层向下遍历至底层实体，再检索关联的片段与边。由于 System-2 产生无序结果，无法直接应用 RRF，而是与 System-1 结果合并后，使用重排序模型（如 Qwen3-Reranker-8B）进行统一排序。该机制解决了单一相似度检索在全局推理中的失效，通过结构驱动的选择捕捉语义距离远但关系重要的信息。

## 实验评估

实验在 LoCoMo 和 LongMemEval-S 两个长期记忆基准上进行，使用 GPT-4.1-mini 作为后端模型，对比 LangMem、MemOS、Mem0、Zep、Nemori、EMem-G 等基线。LoCoMo 包含约 2,000 个问题，平均上下文 16K tokens；LongMemEval-S 包含 500 个会话，平均上下文 115K tokens。评估指标为 LLM-as-a-Judge 分数（0/1）。

| 方法 | LoCoMo Overall | LongMemEval-S Overall |
| :--- | :--- | :--- |
| Full Context (GPT-4.1-mini) | 80.6 | 65.6 |
| RAG (GPT-4.1-mini) | 73.8 | 72.6 |
| Nemori (GPT-4.1-mini) | 79.5 | 74.6 |
| EMem-G (GPT-4.1-mini) | 85.3 | 84.9 |
| Mnemis (GPT-4.1-mini) | 93.3 | 91.6 |
| Mnemis (k=30) (GPT-4.1-mini) | 93.9 | - |

Mnemis 在两个基准上均显著优于基线，尤其在 LoCoMo 上以 93.3 分领先 EMem-G 的 85.3 分。在 LongMemEval-S 上，Mnemis 的 91.6 分略低于 EverMemOS 的 92.3 分，但高于其他所有方法。消融实验显示，System-2 全局选择在枚举型问题上表现优异，但在时间推理问题上较弱，因为查询在遍历过程中保持不变，难以捕捉完整的时间序列。结合双路由后，所有类别性能均提升，验证了互补性。

评估边界方面，LLM-as-a-Judge 的评分稳定性可能影响微小差距的可靠性，如 Mnemis 与 EverMemOS 在 LongMemEval-S 上仅差 0.7 分。此外，层级图的周期性重建策略可能导致实时性损失，论文未提供增量更新机制。代码已开源，但超参数（如压缩比 $n$）对性能的影响未详细讨论。

## 关联研究分析

从问题动机看，Mnemis 与 Nemori 和 Mem0 等 Graph-RAG 方法同属结构化记忆检索路线，但核心差异在于检索机制。Nemori 和 Mem0 依赖局部相似度匹配，适用于语义相近的查询，但在需要全局覆盖的枚举型问题中易漏检。Mnemis 引入层级图支持自上而下遍历，解决了这一盲区。这一差异源于任务特性：长期记忆中的查询往往涉及跨会话、跨主题的综合推理，局部相似度无法捕捉全局结构。Mnemis 的层级图设计使模型能沿语义层级探索，从而在枚举型问题上取得显著优势。

从方法设计看，Mnemis 与 EMem-G 同属图结构记忆框架，但 EMem-G 侧重于动态图更新与实体关系维护，而 Mnemis 侧重于静态层级抽象与全局选择。EMem-G 在 LongMemEval-S 上表现接近 Mnemis，但在 LoCoMo 上落后，可能因其图结构未提供足够的全局抽象层级。Mnemis 的层级图通过最小概念抽象和多对多映射，提供了更丰富的检索路径，增强了召回率。然而，Mnemis 的层级图构建依赖 LLM 的抽象能力，若 LLM 抽象错误，可能导致层级结构偏差，影响全局选择准确性。

## 总结

Mnemis 旨在解决长期 LLM 记忆中局部相似度检索在全局推理中的失效问题，通过构建层级图支持 System-2 全局选择，弥补了 Graph-RAG 方法的盲区。该框架在 LoCoMo 上取得 93.3 分，在 LongMemEval-S 上取得 91.6 分，显著优于多数基线。其边界在于层级图的周期性重建导致实时性损失，且 System-2 在时间推理问题上表现较弱。当对话历史频繁更新时，层级图的增量更新机制能否在不牺牲全局结构完整性的前提下保持检索效率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7789ca44ea8c)