# HuggingFace最新推荐论文 ｜The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks ｜面向真实世界任务“最后一公里”的 Agent-Native Primitives 与 HEELO 框架

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Haibo Jin、Peng Kuang、Xiaopeng Yuan 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.07461)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.07461)

> 导读
> LLM 智能体在真实世界任务中面临的核心困境是“最后一公里”问题，即模型能够检索到外部资源，却难以在复杂上下文中正确应用、组合这些资源，并在失败时进行精准修正。现有方法多依赖单体 Agent 或静态多智能体框架，将资源应用的能力完全交由调用方处理，导致长程任务中错误累积且难以定位。本文提出 Agent-Native Primitives（具备常驻 LLM 的可复用资源单元）与 HEELO 框架，将资源与其应用逻辑封装为独立单元，通过动态图编排与基于证据的局部修正机制，实现资源应用能力的解耦与复用。该框架在 Terminal-Bench、SWE-bench 等基准上显著提升了任务解决率，但其依赖常驻 LLM 带来的推理开销与框架复杂度，在极端复杂逻辑任务上的上限仍有待验证。

## 研究背景

当 LLM 智能体面对真实世界任务时，其核心挑战已从“能否获取资源”转向“能否正确应用资源”。这一转变源于模型能力的提升与任务复杂度的增加：智能体可以通过检索或 API 调用获取代码、文档或工具，但这些资源往往需要结合任务的具体上下文进行适配。例如，一个工具调用的参数可能需要锚定在早期调用的输出上，或者一段检索到的代码需要适应目标仓库的依赖结构。这种从资源可达性到资源正确应用的鸿沟，被称为“最后一公里”问题。

现有主流方法在解决这一问题时存在结构性缺陷。提示工程（Prompt Engineering）和单体 Agent 架构（如 ReAct）将资源应用的逻辑完全内化于调用方的上下文中，导致上下文窗口迅速爆炸，且长轨迹中的微小错误会随步骤增加而放大。多智能体框架（如 AutoGen）虽然通过角色分工缓解了部分压力，但基于文本消息的通信机制存在序列化开销大、状态不一致等问题，且缺乏对资源应用能力的模块化封装。强化学习（RL）方法试图通过训练优化整体策略，但面临训练数据稀缺和信用分配难题，且难以直接复用已有的高质量资源。因此，领域内缺乏一种能够将“资源”与“应用资源的能力”解耦，并支持动态组合与局部修正的通用框架。

## 核心方法

### 方法参照系：从单体调用到资源封装

在传统的 LLM 智能体架构中，资源（如 API、代码片段、证明方法）被视为被动工件，其应用逻辑由中央 Agent 在推理时动态生成。这种模式的问题在于，中央 Agent 必须在其有限的上下文窗口中同时维护任务状态、资源细节以及应用逻辑，导致认知负荷过载。HEELO 框架将问题重新定义为 Harness Engineering（框架工程），即构建一个围绕模型的执行环境，该环境由可复用的 Agent-Native Primitives 组成。每个 Primitive 不仅包含资源本身，还包含一个常驻 LLM，该 LLM 负责在特定上下文中应用资源并与其他 Primitive 通信。

### Agent-Native Primitives：资源与应用的解耦

Agent-Native Primitive 是 HEELO 的核心创新，它将可复用资源 $a_i$ 与一个常驻 LLM $\mathcal{M}$ 绑定，并暴露一个接口 $d_i$ 供框架调用。当被调用时，常驻 LLM 根据资源 $a_i$、上下文 $c_i$ 和自然语言请求 $x_i$ 应用资源，并返回结果 $r_i$ 及发送给其他 Primitive 的消息 $m_i$。其形式化定义为：

$$
(r_i, m_i) = P_i(x_i; c_i) = \mathcal{M}[a_i; c_i; x_i]
$$

这一设计的动机在于解决传统方法中“资源应用逻辑与调用方耦合”的问题。常驻 LLM 充当了资源的自然语言接口，使得调用方无需在自身上下文中持有资源的具体细节（如复杂的 API 模式或代码依赖），从而大幅降低了上下文消耗。同时，消息 $m_i$ 允许 Primitive 之间直接传递需求或任务相关信息，实现了资源间的主动通信，而非被动等待中央 Agent 的调度。

### HEELO 框架：动态图编排与证据驱动修正

HEELO 框架通过三个机制构建并运行任务特定的执行图。首先，Library Selection and Composition 机制通过接口检索或相关性评估，从库 $\mathcal{L}$ 中选择必要的 Primitive，并构建一个任务特定的图 $\Pi_t$，其中包含激活集 $\mathcal{A}_t$ 和依赖关系 $\mathcal{E}_t$：

$$
\Pi_t = \text{COMPOSE}(q, \mathcal{C}_t; \mathcal{L}) = \{(i, x_i)\}_{i \in \mathcal{A}_t}, \mathcal{E}_t \subseteq \mathcal{A}_t \times \mathcal{A}_t
$$

其次，Evidence-Based Execution and Improvement 机制在任务环境中运行该图，并验证结果。如果验证失败，框架会追踪失败证据 $\varphi_t$，识别出涉及的 Primitive $\mathcal{I}_t$，并仅重做受影响的部分，而非整个任务：

$$
\mathcal{C}_{t+1} = \mathcal{C}_t \cup \{\varphi_t\}, \quad \Pi_{t+1} = \text{COMPOSE}(q, \mathcal{C}_{t+1}; \mathcal{L}, \Pi_t, \varphi_t)
$$

这一机制解决了长程任务中的信用分配难题。传统方法在任务失败时往往需要重新生成整个轨迹，而 HEELO 通过环境证据（如测试失败、编译错误）精确定位到具体的 Primitive，实现了局部修正，显著提高了执行效率和鲁棒性。

## 实验评估

### 实验设置与主结果

论文在 Terminal-Bench 4.0、SWE-bench Verified、ToolBench 等多个基准上评估了 HEELO 框架及其八个 Primitive 家族。基线覆盖了 Codex、Claude Code、ReAct、DFSDT 等主流单体 Agent 和多智能体方法。在 Terminal-Bench 4.0 上，HEELO 显著提升了任务解决率，特别是在 GPT-5.6 Sol 骨干上，从 Codex 的 37.3% 提升至 55.5%。在 SWE-bench Verified 上，STITCH（基于 HEELO 的 Harness Primitives）将 Pass@1 从种子 Harness 的 73.0% 提升至 80.5%，超越了 Codex 的 79.0%。

| 基准 | 方法 | 指标 | 数值 (%) |
| :--- | :--- | :--- | :--- |
| Terminal-Bench 4.0 | Codex (GPT-5.6 Sol) | Resolution | 37.3 |
| Terminal-Bench 4.0 | HEELO (GPT-5.6 Sol) | Resolution | 55.5 |
| SWE-bench Verified | Codex | Pass@1 | 79.0 |
| SWE-bench Verified | STITCH (HEELO) | Pass@1 | 80.5 |
| ToolBench | DFSDT (Qwen3-8B) | Pass Rate | 55.8 |
| ToolBench | HEART (HEELO) | Pass Rate | 75.1 |

### 消融与设计决策验证

消融实验表明，HEELO 的性能增益主要来源于 Primitive 的接口封装和基于证据的修正机制。在 ToolBench 上，移除 ToolFace 和 Tool Primitives 后，Pass Rate 从 75.1% 骤降至 16.1%，证明常驻 LLM 接口在参数解析和调用中的关键作用。在 SWE Refactor Bench 上，移除诊断反馈（Diagnosis）导致复合分数从 31.0 降至 20.0，说明将失败追踪至具体组件的机制对长程代码修改任务至关重要。

| 变体 | ToolBench Pass (%) | NESTFUL Full Acc. |
| :--- | :--- | :--- |
| HEART (Full) | 75.1 | 0.44 |
| w/o ToolFace & Tool Primitives | 16.1 | 0.06 |
| w/o Validation | 47.6 | 0.15 |
| w/o Decomposition | 57.2 | 0.26 |

### 评估边界与可复现性

论文在 heelo.dev 平台上进行了 46 个真实世界任务的端到端评估，显示 Claude Code 和 Codex 在连接 HEELO 后，任务完成数从 9 个分别提升至 39 和 35 个。然而，评估主要依赖公开基准和自建平台，缺乏对极端对抗性环境或资源极度稀缺场景的测试。代码方面，论文提供了 heelo.dev 网站，但未明确提供完整的开源代码仓库，可能影响复现性。

## 关联研究分析

从问题动机看，HEELO 与 ReAct 范式存在本质差异。ReAct 通过交错生成推理轨迹与执行动作，确立了“推理-行动-观察”的基础架构，但其核心假设是模型自身具备应用资源的能力。HEELO 则指出，在复杂真实世界任务中，资源应用本身是一个独立的、可复用的能力，不应完全依赖中央模型的推理。这一观点与 Toolformer 等通过自监督学习内化工具调用格式的方法不同，HEELO 更强调在推理时通过常驻 LLM 动态适配资源，而非在训练时固化调用模式。

从方法设计看，HEELO 与 CaveAgent 等多智能体框架在通信机制上形成对比。CaveAgent 通过共享状态通信取代文本消息，解决了序列化开销问题，但其状态同步仍依赖于中央协调器。HEELO 的 Agent Primitives 通过 KV Cache 通信和消息传递，实现了去中心化的资源间协作。然而，HEELO 的常驻 LLM 机制引入了额外的推理开销，论文虽指出在 Qwen3-8B 上成本较低，但在高复杂度任务中，多个常驻 LLM 的并行调用是否会导致延迟瓶颈，论文未给出极端场景下的量化分析。

## 总结

本文针对 LLM 智能体在真实世界任务中的“最后一公里”问题，提出 Agent-Native Primitives 与 HEELO 框架，将资源与其应用逻辑解耦为可复用的独立单元，并通过动态图编排与基于证据的局部修正机制，显著提升了长程任务的解决率。在 Terminal-Bench 4.0 上，HEELO 将 GPT-5.6 Sol 的任务解决率从 37.3% 提升至 55.5%，证明了资源封装与局部修正的有效性。然而，该框架依赖常驻 LLM 带来的推理开销与框架复杂度，在极端复杂逻辑任务上的上限仍有待验证。当任务所需的资源数量极大且相互依赖关系高度动态时，常驻 LLM 的通信开销是否会抵消应用效率的提升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.07461)