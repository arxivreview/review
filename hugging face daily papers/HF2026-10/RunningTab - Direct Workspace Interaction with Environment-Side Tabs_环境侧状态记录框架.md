# HuggingFace最新推荐论文 ｜RunningTab: Direct Workspace Interaction with Environment-Side Tabs ｜环境侧状态记录框架

作者：Jinheon Baek、Soyeong Jeong、Yumin Choi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.10444)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.10444)

> 导读 在长程工作区任务中，LLM 智能体需从分散文件中提取信息以生成新交付物，但上下文窗口的有限容量导致早期读取的关键信息被后续观察覆盖，造成“已读未用”或“已列未开”的状态丢失。现有方法依赖模型自反思或外部编排器，未能解决环境侧状态持久化问题，导致交付物内容缺失。本文提出 RunningTab 框架，由环境维护包含需求、读取日志和候选文件的任务状态记录，并在交付前强制审查。该框架在 Workspace-Bench 等基准上显著优于基线，证明了环境侧记录在长程任务中的有效性。然而，固定 Tab 结构是否限制了复杂依赖关系的表达，以及环境自动捕获是否引入噪声，仍需进一步验证。

## 研究背景

当智能体面对包含数千个异构文件的工作区时，其核心挑战并非文件访问，而是长程状态管理。直接语料交互（Direct Corpus Interaction, DCI）允许智能体通过终端工具直接操作原始文件，无需预建索引，解决了文件可达性问题。然而，当任务目标从短答案检索转变为多文件内容聚合的交付物生成时，DCI 暴露出严重缺陷：智能体在数十轮交互中读取的信息仅存在于不断增长的上下文流中，早期提取的关键数值或事实极易被后续观察挤出，导致最终交付物遗漏已获取的内容。

这一现象在 Workspace-Bench 基准上被量化：在 DCI 失败案例中，51.1% 的失分源于“提取失败”，其中 12.3% 属于“已展示但缺失”，即智能体已读取正确文件并看到目标内容，但交付物中未包含该信息。此外，17.6% 的失败源于“发现失败”，即智能体列出了包含目标文件的目录却未打开。现有基线如 TODO 列表或 Self-Refine 依赖模型自身在上下文内维护任务状态，但在长轨迹中同样受限于上下文窗口容量，无法有效防止状态丢失。因此，亟需一种独立于模型上下文、由环境维护的持久化状态记录机制，以确保任务需求、已读内容和未开文件在交付前始终可查。

## 核心方法

### 直接工作区交互与状态缺失

本文的问题设定为直接工作区交互（Direct Workspace Interaction, DWI），即智能体在给定工作区 $\mathcal{W}$ 和任务 $t$ 下，通过终端工具多轮交互生成交付物 $\mathcal{D}$。与通用工作流编排不同，DWI 的关键差异在于其输出是聚合多文件内容的复杂交付物，而非单一答案，这要求智能体在长程执行中保持对分散信息的持续追踪。在标准 DWI 中，任务状态完全依赖模型上下文，缺乏外部持久化记录，导致状态随上下文截断而丢失。

### 环境侧 Tab 的结构化定义

RunningTab 的核心创新在于引入环境侧 Tab（Environment-Side Tab），由环境而非模型维护。Tab 被形式化为三元组 $\mathcal{T}_t = (\mathcal{R}, \mathcal{L}, \mathcal{C})$，分别对应需求（Requirements）、读取日志（Read Log）和候选文件（Candidates）。

$$
\mathcal{T}_t = (\mathcal{R}, \mathcal{L}, \mathcal{C})
$$

该公式定义了 Tab 的组成结构。$\mathcal{R}$ 记录任务分解后的原子需求（如“2024 年专利数”），状态分为“开放”“已完成”或“不可用”；$\mathcal{L}$ 记录智能体每次读取文件时的确切文本片段及其来源路径，确保内容可追溯；$\mathcal{C}$ 记录智能体在目录列表中看到但未打开的文件，作为潜在信息源。这一设计将状态管理从模型内部移至环境侧，避免了上下文窗口容量限制导致的遗忘。

### 交付前的强制审查与完成检查

Tab 的价值在任务结束前通过审查（Review）和完成检查（Finish Check）机制释放。当智能体尝试停止时，环境返回一个完成检查，列出所有未解决的需求及对应的最佳匹配读取日志片段。智能体需通过引用读取日志条目来将需求标记为“已完成”，或说明其“不可用”的原因。

$$
\text{Resolve}(r_i) \rightarrow \begin{cases} \text{done} & \text{if } \exists \ell_j \in \mathcal{L}, \text{content}(r_i) \subseteq \text{excerpt}(\ell_j) \\ \text{unavailable} & \text{if } \neg \exists \ell_j \in \mathcal{L}, \text{with reason} \end{cases}
$$

该公式描述了需求解决逻辑。审查机制将每个开放需求与其最佳匹配的读取日志片段并列展示，使智能体无需重新搜索即可确认内容是否已获取。这一设计解决了“已读未用”问题，因为即使内容在上下文中被挤出，Tab 中的日志片段仍可供审查。

## 实验评估

实验在 Workspace-Bench、TheAgentCompany 和 OfficeQA Pro 三个基准上进行，对比 DCI、TODO、Self-Refine 和 Self-Tracking 基线。RunningTab 在所有基准和模型上均取得最佳性能。在 Workspace-Bench 上，使用 GPT-5.4 nano 时，RunningTab 的 Pass Rate 为 44.73%，较 DCI 的 41.63% 提升 3.1 个百分点；TCR@70 从 20.67% 提升至 25.67%。在 OfficeQA Pro 上，Acc@0% 从 53.53% 提升至 60.58%。

| 方法 | Workspace-Bench Pass Rate (%) | Workspace-Bench TCR@70 (%) | OfficeQA Pro Acc@0% (%) |
| :--- | :--- | :--- | :--- |
| DCI | 41.63 | 20.67 | 53.53 |
| TODO | 41.67 | 23.33 | 54.81 |
| Self-Refine | 41.32 | 22.33 | 54.17 |
| Self-Tracking | 42.93 | 23.00 | 55.13 |
| RunningTab | 44.73 | 25.67 | 60.58 |

消融实验表明，环境自动捕获（Environmental Capture）是性能提升的主要来源。移除该组件后，Pass Rate 降至 41.36%，接近 DCI 水平，说明 Tab 的价值主要源于环境对读取日志和候选文件的自动记录，而非模型自反思。审查机制（Review）次之，移除后 Pass Rate 降至 41.87%，表明将捕获内容与需求并列展示对智能体决策至关重要。

| 消融变体 | Pass Rate (%) | TCR@70 (%) |
| :--- | :--- | :--- |
| RunningTab (Full) | 44.73 | 25.67 |
| No Environmental Capture | 41.36 | 22.33 |
| No Review | 41.87 | 20.33 |
| No Evidence Check | 42.89 | 24.33 |
| No Finish Check | 42.89 | 23.00 |

评估边界方面，论文未与多智能体协作方法对比，可能因单代理加 Tab 在特定场景下已足够。此外，Tab 内容随任务复杂度增长，在读取密集型任务中增益更大，但环境自动捕获是否引入噪声导致审查效率下降，论文未深入分析。

## 关联研究分析

从问题动机看，RunningTab 与 AgenTracer 均关注长轨迹失败归因，但 AgenTracer 侧重事后诊断，通过反事实重放定位失败步骤；RunningTab 侧重事中预防，通过环境侧记录防止状态丢失。这一差异源于任务特性：AgenTracer 适用于调试已失败的工作流，而 RunningTab 适用于实时执行中的状态维护。RunningTab 未探索事后诊断能力，其 Tab 结构是否支持回溯性故障分析，论文未给出回答。

从方法设计看，RunningTab 与 LEGOMem 均解决长程记忆问题，但 LEGOMem 依赖模块化程序记忆，将任务分解为可复用的程序片段；RunningTab 依赖环境侧结构化 Tab，记录原始读取内容。LEGOMem 在 OfficeBench 上达到 85.0% 成功率，但基准不同无法直接比较。RunningTab 的固定 Tab 结构（需求-日志-候选）是否限制了复杂依赖关系的表达，例如当需求间存在逻辑依赖时，Tab 无法自动推导，这一局限在论文中未讨论。

## 总结

RunningTab 针对长程工作区任务中上下文窗口导致的状态丢失问题，提出环境侧 Tab 机制，通过自动记录读取日志和候选文件，并在交付前强制审查，有效缓解了“已读未用”现象。在 Workspace-Bench 上，RunningTab 将 Pass Rate 从 41.63% 提升至 44.73%，证明了环境侧记录在长程任务中的有效性。然而，该框架采用固定 Tab 结构，未涉及工作流拓扑动态优化，且环境自动捕获可能引入噪声。当任务需求间存在复杂逻辑依赖时，固定 Tab 结构是否足以表达这些依赖，以及环境捕获的噪声是否会降低审查效率，仍需进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.10444)