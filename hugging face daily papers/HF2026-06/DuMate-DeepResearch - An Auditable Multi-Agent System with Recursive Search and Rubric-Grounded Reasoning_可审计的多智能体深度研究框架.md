# HuggingFace最新推荐论文 ｜DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning ｜可审计的多智能体深度研究框架

作者：Lingyong Yan、Can Xu、Yukun Zhao 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.07299)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.07299)

> 深度研究智能体（Deep Research Agent, DRA）旨在解决开放式长周期任务中证据碎片化与推理路径漂移的矛盾。现有单体架构或线性流水线难以兼顾全局规划视野与局部执行稳定性，导致长程任务中噪声级联与幻觉累积。本文提出解耦认知核心与工具生态的多智能体框架，通过图结构动态规划与递归嵌套执行实现可审计的闭环研究。该框架在报告质量基准上刷新了架构派SOTA，但其对底层模型能力的依赖及缺乏强化学习（RL）训练的泛化边界仍存疑。

## 研究背景

当智能体面对“评估某技术栈在特定行业的应用前景”这类模糊查询时，传统的检索增强生成（RAG）仅能执行单次静态检索，无法处理证据随时间演变的动态性。为突破此局限，ReAct 范式引入了“推理-行动-观察”循环，赋予模型主动探索能力。然而，ReAct 本质上是短视的局部最优策略，它缺乏对全局研究路径的宏观表征，导致智能体在长程任务中容易陷入无限探索或过早收敛，且无法在工具失败时有效回溯。

深度研究任务的核心挑战在于长程规划与动态范围定义的耦合。早期单体架构（如 OpenAI Deep Research）将所有模块紧密集成，虽控制流统一但扩展性差；流水线架构虽利于组件复用，却难以处理复杂迭代与全局反馈。当前主流架构派试图通过多智能体协作解决此问题，但多数方案仍采用线性或简单层级结构，未能有效隔离底层检索噪声与高层策略决策。DuMate-DeepResearch 的切入点在于将“认知”与“执行”彻底解耦，并引入递归嵌套机制，旨在通过结构化的隔离防止局部失败向全局轨迹级联，同时通过图结构规划维持长程视野。

## 核心方法

### 状态转移形式化

DuMate-DeepResearch 将研究会话建模为可审计的状态转移系统。给定查询 $q$，系统维护状态 $s_t = \langle z, p_t, e_t, \rho_t \rangle$，其中 $z=(x, O)$ 为固定任务上下文（主题 $x$ 与大纲 $O$），$p_t$ 为当前研究计划，$e_t$ 为累积证据库，$\rho_t$ 为指导信号。

$$ s_{t+1} = T(s_t, a_t, \Delta e_t) $$

该公式表明，每轮迭代通过执行动作 $a_t$ 获取增量证据 $\Delta e_t$，并更新状态。这一形式化确保了研究路径的每一步都是基于累积证据的显式转移，而非黑盒生成，为后续的可审计性奠定了数学基础。

### 图结构动态规划

针对 ReAct 短视性导致的执行漂移，本文提出图结构动态规划器。它将研究路线图表示为有向无环图（DAG），支持从粗到细的扩展。

$$ p_{t+1} = \text{Plan}(p_t, e_t, \rho_t) \cup \text{Branch}(p_t) $$

该设计动机在于解决单一策略无法同时处理全局分解与局部噪声的问题。通过引入反思、重规划、回溯及并行分支机制，规划器能在工具失败或新证据推翻假设时动态修订策略。与线性规划不同，DAG 结构允许智能体在保持全局视野的同时，对特定子任务进行局部修正，避免了局部失败对整体轨迹的污染。

### 递归两级执行与 Rubric 引导

为隔离检索噪声，本文采用递归两级执行设计。外层 Research Agent 将复杂搜索子任务委托给内层 Search Agent，后者作为独立的 Foundry Agent 运行自己的规划-执行循环。

$$ \text{Score}(y) = \sum_{i=1}^{N} w_i \cdot \mathbb{1}[\text{Claim}_i \in E_{\text{retrieved}}] $$

Rubric-based Test-Time Optimization 机制动态生成任务特定的评估标准（Rubric），作为推理时的脚手架。该公式表示最终报告得分取决于生成声明与检索证据的匹配程度。这一机制解决了长文本合成中的幻觉问题，通过实时校准每个断言的证据基础，并提供自适应终止准则，确保仅在证据充分时停止探索，而非依赖固定预算或事后验证。

## 实验评估

实验在 DeepResearch Bench (DRB) 和 DRB II 上进行，基线涵盖 ZTE Nebula、MS-Agent 等商业系统及开源模型。值得注意的是，对比组中缺失了 ASearcher、ABSeeker 等基于 RL 训练的代表性方法，这使得结果主要反映架构优化在报告生成质量上的优势，而非长程搜索策略的泛化能力。

| 方法 | DRB Overall (%) | DRB II Overall (%) |
| :--- | :--- | :--- |
| DuMate-DeepResearch | 58.03 | 61.95 |
| ZTE Nebula DeepResearch | 57.27 | - |
| MS-Agent DeepResearch | 55.31 | - |
| iFlowResearcher | - | 59.91 |

在 DRB 上，DuMate-DeepResearch 以 58.03% 的总分超越 ZTE Nebula 的 57.27%，尤其在 Comprehensiveness (59.48%) 和 Insight (61.48%) 维度领先。在 DRB II 上，其 61.95% 的总分优于 iFlowResearcher 的 59.91%，并在 Information Recall (57.58%) 和 Analysis (71.70%) 上排名第一。

| 消融变体 | Overall (%) | Insight (%) |
| :--- | :--- | :--- |
| Full System | 58.03 | 61.48 |
| w/o Rubric (Report Stage) | 57.61 | 60.73 |
| w/o Rubric (Full Pipeline) | 57.53 | 60.78 |
| DeepSeek V4 Pro (Report Model) | 57.21 | 60.66 |

消融实验显示，移除报告阶段的 Rubric 导致 Overall 下降 0.42%，Insight 下降 0.75%，表明 Rubric 的主要价值在于报告合成阶段的事实接地。相比之下，替换报告生成模型的影响更大，DeepSeek V4 Pro 替换后 Overall 下降 0.82%，且 Readability 显著降低 1.70%，证实了合成模型是流水线中最敏感的组件。

评估协议依赖 LLM-as-a-judge 和专家 Rubric，虽提升了细粒度评估能力，但缺乏对计算效率（如 Token 消耗、延迟）的报告。代码已开源，但超参数（如最大迭代次数 15）的敏感性分析未提供，限制了跨硬件环境的可复现性比较。

## 关联研究分析

从问题动机看，DuMate-DeepResearch 与 WebWeaver 同属架构派，均试图通过多智能体协作解决证据结构化难题。然而，WebWeaver 侧重于双智能体间的证据交换与整合，而本文引入了递归嵌套，将内层 Search Agent 视为独立实体。这一差异源于对“噪声隔离”的不同理解：WebWeaver 假设智能体间通信可过滤噪声，而本文认为必须通过物理隔离（独立规划循环）才能防止局部失败级联。这种设计选择暗示了架构派内部对“稳定性来源”的分歧：是依赖智能体间的协商，还是依赖结构性的边界约束。

从方法设计看，本文与 ASearcher 代表了“架构优化”与“训练优化”的两条路线。ASearcher 通过大规模端到端 RL 挖掘模型潜力，简化架构；而 DuMate-DeepResearch 依赖复杂的图规划与递归结构，未使用 RL。在 DRB 上，本文超越了部分 RL 方法，但这可能归因于 DRB 侧重报告质量而非搜索效率。在 GAIA 等更侧重长程导航的基准上，纯架构方案是否仍能保持优势，取决于底层模型的推理能力是否足以支撑复杂的图操作，论文未提供此对比，留下了架构与训练边界模糊的疑问。

## 总结

DuMate-DeepResearch 旨在解决深度研究中长程规划短视与执行噪声级联的矛盾。通过解耦认知核心与工具生态，并引入图结构动态规划与递归两级执行，该框架实现了可审计的闭环研究，在 DeepResearch Bench 上以 58.03% 的总分刷新了架构派 SOTA。然而，其性能高度依赖底层报告生成模型的能力，且缺乏与 RL 训练派在长程搜索效率上的直接对比。当底层模型推理能力有限时，复杂的图规划是否会增加计算开销而非提升效果，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.07299)