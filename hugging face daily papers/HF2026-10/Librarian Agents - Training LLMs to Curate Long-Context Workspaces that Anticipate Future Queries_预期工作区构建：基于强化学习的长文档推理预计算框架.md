# HuggingFace最新推荐论文 ｜Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries ｜预期工作区构建：基于强化学习的长文档推理预计算框架

作者：Anikait Singh、Teresa Zhang、Yoonho Lee 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.22273)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22273)

> 导读 长文档推理中，传统检索增强生成（RAG）每次查询需重新发现跨文档关系，导致计算冗余；预计算结构（如知识图谱）虽能加速检索，但依赖刚性启发式规则，难以适应多样化查询。本文提出 Librarian Agents，将工作区构建建模为马尔可夫决策过程（MDP），通过强化学习（RL）训练构建者智能体生成可导航的文件系统结构。该框架在 BrowseComp-Plus 上显著超越基线，并实现零样本迁移。其价值在于将推理成本前置并摊销，但预计算结构的泛化边界与构建成本权衡仍需验证。

## 研究背景

当智能体面对超出上下文窗口的企业知识库或软件仓库时，所需信息分散于多个文档中。传统 RAG 通过检索原始文档片段并合成答案，但每次查询都需重新执行搜索与推理，无法复用已发现的跨文档关联。为缓解此问题，预计算方法如 GraphRAG 在推理前构建知识图谱，将计算成本前置。然而，此类方法依赖固定的实体抽取规则，当查询需要新的任务特定中间产物时，刚性结构反而成为检索瓶颈。

深度研究智能体（Deep Research Agents, DRA）领域正从被动检索转向自主探索，核心挑战在于长程信息整合与噪声过滤。现有架构派通过多智能体协作显式管理记忆，训练派则依赖端到端 RL 优化搜索策略。两者均聚焦于推理时的动态决策，却忽视了推理前的结构构建能力。本文抓住这一空白，提出“预期工作区”概念：训练智能体在查询到达前，主动将非结构化语料重组为面向答案的文件系统，使下游回答者能高效导航。

## 核心方法

### 方法参照系：从静态索引到动态工作区

本文问题属于预计算结构构建，但与 GraphRAG 等静态索引的关键差异在于：工作区不是固定图结构，而是由智能体动态生成的文件系统，包含合成文件、目录及指向原始文档的引用链接。构建者智能体（Builder Agent）通过编辑操作重组语料，回答者智能体（Answering Agent）通过文件列表与读取操作导航工作区。

### 预期工作区的 MDP 建模与密集奖励

构建过程被形式化为有限视野 MDP。状态为当前文件系统 $\mathcal{F}_t$，动作包括 CreateFile、MergeFiles、Delete 和 Stop。奖励函数需平衡下游回答准确率与导航效率。定义下游效用为：

$$U(\mathcal{F}) := S(\mathcal{F}) - \lambda_{\text{tok}} C_{\text{tok}}(\mathcal{F}) - \lambda_{\text{read}} C_{\text{read}}(\mathcal{F})$$

其中 $S(\mathcal{F})$ 为期望回答成功率，$C_{\text{tok}}$ 和 $C_{\text{read}}$ 分别为合成内存 token 成本与文件读取成本。稀疏奖励仅评估最终工作区，信用分配粗糙。本文引入密集奖励，通过定期探针（Probes）评估工作区变化对回答能力的影响：

$$r_{\text{dense}}^t := U(\mathcal{F}_t) - U(\mathcal{F}_{t-1}) - \alpha \text{Cost}_{\text{build}}(\mathcal{A}_t)$$

该公式将轨迹级监督转化为步骤级密集信号，使构建者能区分每个编辑操作对最终结果的边际贡献，解决了传统 RL 在长序列编辑中信用分配失效的问题。

### 基于 GRPO 的策略优化与摊销机制

构建者策略通过 GRPO（Group Relative Policy Optimization）优化。训练时，每 8 步执行一次探针，结合终端回答正确性计算优势函数。回答者智能体保持冻结，确保学习信号仅反映工作区质量。该设计将构建成本摊销至多次查询：一次构建的工作区可服务多个问题，降低单次查询的边际成本。

## 实验评估

实验在 BrowseComp-Plus（680 训练/50 测试任务）和 BRIGHT（零样本迁移）上进行。基线覆盖 Embedding、Reranker、GraphRAG、Agentic RAG 及 AutoCompaction。回答者使用冻结的 Qwen3.5-4B 和 Gemini 3.1 Flash Lite。

| 方法 | 准确率 (Qwen3.5-4B) | 准确率 (Gemini 3.1 Flash Lite) | 构建成本 (tokens) |
| :--- | :--- | :--- | :--- |
| GraphRAG | 0.36 | — | 11,923 |
| AutoCompaction | 0.04 | — | 501,637 |
| Builder (No FT) | 0.28 | — | 127,683 |
| Librarian Agents (Ours) | 0.75 | 0.77 | 178,926 |

Librarian Agents 在 BrowseComp-Plus 上比最佳基线 GraphRAG 高 39 个百分点（0.75 vs 0.36），证明 RL 优化构建策略的有效性。消融实验显示，无 RL 微调的构建者准确率仅 0.28，表明基础模型无法自发学习面向答案的结构组织。

| 方法 | AOPS pass@1 | Biology pass@1 | Stack Overflow pass@1 | 平均 pass@1 |
| :--- | :--- | :--- | :--- | :--- |
| BM25 | 30.5 | 17.5 | 9.0 | 19.0 |
| Dense | 31.5 | 19.5 | 11.5 | 20.8 |
| Graph | 12.5 | 5.0 | 1.5 | 6.3 |
| Librarian | 36.0 | 34.5 | 85.5 | 52.0 |

在 BRIGHT 零样本迁移中，Librarian Agents 平均 pass@1 达 52.0%，比 Dense 基线高 31.2 个百分点，尤其在 Stack Overflow 任务上达 85.5%，显示其学到的结构组织策略具有跨域泛化性。

评估边界方面，论文未报告置信区间，且构建成本（178K tokens）显著高于 GraphRAG（11.9K tokens），摊销收益依赖查询复用率。代码未开源，复现性受限。

## 关联研究分析

从问题动机看，Librarian Agents 与 Search-R1 均使用 RL 优化智能体行为，但优化目标截然不同。Search-R1 优化推理时的搜索策略，通过多跳导航获取证据；Librarian Agents 优化推理前的结构构建，通过预计算降低查询时导航成本。两者互补：前者解决“如何找”，后者解决“如何存”。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，Librarian Agents 与 GraphRAG 同属预计算路线，但结构生成机制不同。GraphRAG 依赖 LLM 抽取实体与关系构建固定图，结构刚性且易受抽取错误影响；Librarian Agents 通过 RL 学习文件系统编辑策略，结构动态且可导航。该差异源于任务特性：GraphRAG 假设查询与实体对齐，而 Librarian Agents 假设查询需要多粒度中间产物。当查询分布与训练分布偏差较大时，RL 学到的结构是否仍具鲁棒性，论文未充分验证。

## 总结

本文针对长文档推理中计算冗余与结构刚性矛盾，提出预期工作区构建框架。通过 MDP 建模与密集奖励 RL 优化，训练构建者智能体生成可导航文件系统，在 BrowseComp-Plus 上准确率提升 39 个百分点，零样本迁移提升 31 个百分点。其边界在于构建成本高昂且依赖查询复用摊销，预计算结构的泛化性仅在 BRIGHT 上有限验证。当查询分布与训练分布存在显著偏移时，RL 学到的结构组织策略是否会失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22273)