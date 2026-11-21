# ACL2026最新论文 ｜FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents ｜文件系统驱动的深度研究智能体

研究机构：中国科学技术大学

作者：Chiwei Zhu、Benfeng Xu、Mingxuan Du 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.01566)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b16d18c04d2e)

> 深度研究智能体在处理长周期、开放式任务时，常因模型上下文窗口限制导致证据丢失与报告质量下降。现有方法通过压缩观察或子智能体卸载来缓解此问题，但受限于硬性的上下文边界，且中间状态无法持久化，阻碍了测试时扩展。FS-Researcher 提出基于文件系统工作区的双智能体框架，将证据积累与报告生成解耦，利用外部持久化存储突破上下文限制。该框架在 DeepResearch Bench 上取得 53.94 的 RACE 分数，验证了架构优化对长程任务的有效性，但其对骨干模型能力的依赖及缺乏强化学习训练的路径选择，使其在通用泛化性上存在争议。

## 研究背景

深度研究任务要求智能体在开放网络环境中自主检索、整合海量碎片化信息并生成结构化报告。这一过程涉及长程决策，智能体需维持目标一致性并处理噪声信息。然而，大语言模型的上下文长度存在硬性限制，当任务轨迹超过此限制时，早期关键证据会被截断，导致推理路径偏离，即执行漂移。为解决此问题，ReAct 范式确立了“推理-行动-观察”的交互循环，但仅靠提示工程无法突破底层模型的能力边界。

当前领域存在两条主要技术路线：架构派与训练派。架构派通过多智能体协作或层级规划显式管理记忆，如 WebWeaver 采用双智能体框架解决证据结构化难题；训练派则通过强化学习优化策略，如 ASearcher 利用大规模端到端 RL 提升长程搜索能力。然而，架构派方法通常受限于上下文窗口的物理边界，中间状态（如思考过程、工具观察）在智能体循环终止后即被丢弃，无法进行跨会话的迭代优化。FS-Researcher 的切入点在于借鉴编码智能体的文件系统工作区范式，将外部存储作为持久化记忆介质，从而在架构层面突破上下文限制，实现测试时扩展。

## 核心方法

### 双智能体解耦架构

FS-Researcher 将深度研究任务解耦为证据积累与报告合成两个阶段，分别由 Context Builder 和 Report Writer 执行。这种设计源于单智能体在长轨迹中因上下文膨胀导致的工具调用低效与信息丢失。Context Builder 作为“数字图书馆员”，负责浏览互联网、提取关键事实并归档至分层知识库；Report Writer 则基于该知识库逐节撰写报告，将知识库作为唯一事实来源。这种解耦使得证据收集过程可以独立扩展，而不受报告生成阶段的上下文压力影响。

### 文件系统持久化工作区

文件系统工作区是 FS-Researcher 的核心创新，它替代了传统的上下文窗口作为智能体的记忆介质。工作区包含交付物（Deliverables）和控制文件（Control Files）。交付物包括 `index.md`（知识库目录）、`knowledge_base/`（结构化笔记）和 `sources/`（原始网页存档）。控制文件包括 `todos`（任务状态列表）、`checklist`（验收标准）和 `logs`（执行轨迹日志）。

智能体通过文件 I/O 工具（如 `read_file`, `insert`）与文件系统交互。Context Builder 在浏览过程中动态更新 `index.md` 和 `knowledge_base/`，并在每个会话结束时根据 `checklist` 进行审查，标记未完成项为 `[IN-PROGRESS]`。这种机制允许智能体跨会话迭代优化知识库，直到达到预算限制或无问题发现。

$$
\text{KB}_{t+1} = \text{Update}(\text{KB}_t, \text{Observations}_t, \text{Checklist}_t)
$$

该公式表示知识库在 $t+1$ 轮会话后的状态，由当前知识库、本轮观察结果及检查清单共同决定。其物理含义是，文件系统作为外部记忆，通过显式的状态更新机制，实现了长程任务中信息的持久化与增量优化，避免了上下文窗口中信息的被动截断。

### 迭代审查与测试时扩展

FS-Researcher 支持多会话工作流，每个会话开始时智能体检查工作区状态，制定计划并执行。这种设计使得计算资源可以灵活分配给 Context Builder，实现测试时扩展。实验表明，增加 Context Builder 的会话轮数（从 3 到 10）能显著提升报告质量，但存在边际收益递减现象。

$$
Q_{final} = f(\text{KB}_{final}, \text{ReportWriter})
$$

其中 $Q_{final}$ 为最终报告质量，$\text{KB}_{final}$ 为最终知识库状态。该公式表明，报告质量是知识库状态与报告生成能力的函数。通过增加 Context Builder 的计算投入，$\text{KB}_{final}$ 的信息密度和完整性提升，从而直接提升 $Q_{final}$。这种正相关性验证了文件系统范式下测试时扩展的有效性。

## 实验评估

FS-Researcher 在 DeepResearch Bench 和 DeepConsult 两个开放式基准上进行评估，基线包括 OpenAI Deep Research、Gemini-2.5-Pro-DeepResearch 等闭源系统，以及 LangChain-Open-DeepResearch、WebWeaver 等开源架构。值得注意的是，实验未包含 ASearcher 或 ABSeeker 等强化学习训练派基线，这可能影响对架构派与训练派相对优势的全面评估。

| 方法 | RACE | FACT | Comp. | Insight |
| :--- | :--- | :--- | :--- | :--- |
| Gemini-2.5-Pro-DeepResearch | 49.51 | 49.45 | 50.12 | 50.00 |
| WebWeaver (Qwen3-235B) | 51.45 | 51.39 | 50.26 | 48.98 |
| FS-Researcher (Claude-Sonnet-4.5) | 53.94 | 55.85 | 52.47 | 51.54 |

FS-Researcher 使用 Claude-Sonnet-4.5 作为骨干模型时，RACE 分数达到 53.94，比最强基线 RhinoInsight 高 3.02 分。在 DeepConsult 上，其胜率（Win Rate）达到 80.00%，平均分 8.33，显著优于 Gemini-2.5-Pro-DeepResearch 的 61.27% 胜率。

消融实验显示，移除持久化工作区导致 RACE 分数从 52.76 降至 48.69，其中 Insight 维度下降最显著（-7.95），表明结构化知识库对深度推理至关重要。增加 Context Builder 轮数从 3 到 10，Comprehensiveness 提升，但 Readability 在 10 轮时略降（51.93 至 51.66），这是因为更大的知识库导致报告风格更密集、技术化，影响了可读性。

评估协议主要依赖 LLM-as-a-judge，可能存在主观偏差。代码已开源，但实验未报告计算成本细节，仅提及文件 I/O 延迟占总时间 <0.03%。在 BrowseComp 上，FS-Researcher (GPT-5) 准确率为 68.0%，高于官方 harness 的 54.9%，验证了框架在可验证任务上的优势。

## 关联研究分析

从问题动机看，FS-Researcher 与 WebWeaver 均属于架构派，旨在解决长程任务中的信息整合问题。WebWeaver 侧重证据的结构化表示，而 FS-Researcher 侧重证据的持久化存储与迭代优化。两者的核心差异在于对“记忆”的处理方式：WebWeaver 依赖模型上下文内的结构化提示，而 FS-Researcher 依赖外部文件系统。这种差异源于任务特性的不同：WebWeaver 针对的是证据的逻辑连贯性，而 FS-Researcher 针对的是证据的容量限制与可追溯性。

从方法设计看，FS-Researcher 与 ASearcher 形成了鲜明对比。ASearcher 通过强化学习优化智能体的搜索策略，属于训练派；FS-Researcher 通过架构优化扩展智能体的记忆容量，属于架构派。ASearcher 证明了端到端 RL 在长程搜索中的有效性，但依赖大规模训练数据；FS-Researcher 无需训练，直接利用现有模型能力，但受限于骨干模型的推理上限。这种“训练 vs 架构”的路线之争，反映了领域内对长程能力来源的不同理解：是模型内在策略的优化，还是外部记忆介质的扩展。

## 总结

FS-Researcher 旨在解决深度研究智能体在长程任务中因上下文限制导致的证据丢失与执行漂移问题。现有方法通过压缩观察或子智能体卸载缓解此问题，但受限于硬性的上下文边界，且中间状态无法持久化。FS-Researcher 借鉴编码智能体的文件系统工作区范式，提出双智能体框架，将证据积累与报告生成解耦，利用外部持久化存储突破上下文限制。实验表明，该框架在 DeepResearch Bench 上取得 53.94 的 RACE 分数，比最强基线高 3.02 分，并验证了测试时扩展的有效性。然而，其性能高度依赖骨干模型能力，且未结合强化学习训练，可能在通用泛化性上存在天花板。当骨干模型能力达到瓶颈时，文件系统工作区能否通过更复杂的迭代机制继续提升报告质量，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_b16d18c04d2e)