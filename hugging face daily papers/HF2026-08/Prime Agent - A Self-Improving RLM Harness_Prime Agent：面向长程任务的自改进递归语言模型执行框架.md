# HuggingFace最新推荐论文 ｜Prime Agent: A Self-Improving RLM Harness ｜Prime Agent：面向长程任务的自改进递归语言模型执行框架

研究机构：美国普林斯顿大学、美国麻省理工学院

作者：Seth Karten、Alex L. Zhang、Kevin Thomas 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.23552)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.23552)

> 长程智能体任务的核心矛盾在于模型作为序列处理器，其决策仅能依赖权重与活跃上下文中的状态，而复杂任务需要远超此范围的外部信息与计算。现有执行框架（Harness）往往将工作流固化，导致基础设施故障被误判为模型能力缺陷，且无法有效管理跨轮次的持久状态。Prime Agent 通过引入持久化 IPython REPL 与递归子智能体通信机制，将执行层从静态工作流转变为可编程的信息与计算管理界面。该框架在 ARC-AGI-3 上将 Opus 5 的成绩从 30.2% 提升至 95.5%，但其性能高度依赖底层模型的推理能力，且缺乏与强化学习训练方法的公平对比，其“自改进”机制在安全性验证上仍存疑。

## 研究背景

理解 Prime Agent 需先厘清“执行框架”（Harness）与“递归语言模型”（RLM）的关系。LLM 本质是受限的序列处理器，其下一步决策仅能访问权重（L0）和活跃 Token 上下文（L1）。当任务涉及长程规划或大规模信息处理时，仅靠 L1 会导致上下文爆炸或信息丢失。RLM 抽象允许模型通过代码调用自身，将上下文处理转化为程序化操作，从而突破 L1 的边界。然而，现有的 RLM 实现往往缺乏对中间状态（如代码执行结果、子智能体历史）的持久化管理，导致长程任务中状态丢失或重复计算。

当前 LLM 智能体领域的主流路线分为提示工程与策略优化。提示工程（如 ReAct）通过交错推理与行动解决即时反馈问题，但在长程任务中面临信用分配难题；策略优化（如 Tool-R0, Agent0）通过强化学习（RL）在合成环境中训练，试图解决数据稀缺与长轨迹优化问题。然而，这两条路线均假设执行环境是稳定且透明的，忽略了执行基础设施本身对模型能力测量的干扰。当框架丢弃状态、限制动作或错误计算资源时，模型失败被错误归因于能力不足。Prime Agent 的切入点在于构建一个标准化、低摩擦的执行膜（Membrane），隔离基础设施故障与模型能力缺陷，使测量结果逼近模型的真实最大能力。

## 核心方法

### 状态分层与持久化执行

Prime Agent 将系统状态划分为四层：L0（模型权重）、L1（活跃上下文）、L2（REPL 与子智能体状态）、L3（磁盘持久化状态）。L1 与 L2 的边界是 Token 可见性，L2 通过“智能体垃圾回收”（Agentic Garbage Collection）机制，允许模型动态创建、保留、摘要或删除 REPL 值与子智能体会话。状态转移遵循显式操作：L2 中的 Python 值序列化后进入 L1；L1 的压缩（Compaction）将前缀替换为摘要，原始事件保留在 L3 供检索。这种设计解决了传统框架中中间值频繁序列化导致的 Token 浪费，以及长程任务中状态丢失的问题。

### 递归编排与持续精炼

Prime Agent 通过异步 `rlm` 原语实现递归子智能体调度。调用 `rlm` 创建子智能体会话并返回稳定句柄，父智能体继续本地计算，结果通过直接 Agent-to-Agent 通信队列异步返回。子智能体继承根智能体的执行与通信原语，形成动态递归树而非固定工作流图。持续精炼（Continual Harness）机制将轨迹证据转化为版本化状态更新：智能体请求编辑或后台模型调用生成技能（Skills）、记忆（Memories）和子智能体规范（Subagent Specs）。精炼在轮次边界应用，保留版本溯源以支持回滚。这一机制将执行证据转化为可复用的持久状态，实现了无需微调模型的自改进。

$$
S_{t+1} = \text{Refine}(S_t, \mathcal{E}_t, \mathcal{A}_t)
$$

其中 $S_t$ 为当前持续状态（技能、记忆等），$\mathcal{E}_t$ 为轨迹事件，$\mathcal{A}_t$ 为智能体动作。该公式表示状态更新是轨迹证据与智能体意图的函数，而非固定规则。

$$
C_{total} = \sum_{i \in \mathcal{R} \cup \mathcal{D}} (T_i + W_i)
$$

其中 $\mathcal{R}$ 为根会话，$\mathcal{D}$ 为后代会话，$T_i$ 为 Token 消耗，$W_i$ 为墙钟时间。该公式确保委托计算的成本在评估中可见，避免子智能体隐藏资源消耗。

## 实验评估

Prime Agent 在 ARC-AGI-3、LongBench、nanoGPT、EmulatorBench、Factorio 和 MazeBench 上进行评估。基线包括原生框架（如 Claude Code, Codex）及流行开源框架（如 Hermes Agent, OpenCode）。缺失基于 RL 训练的智能体（如 Tool-R0）作为基线，导致无法直接对比策略优化与执行框架优化的贡献。

| 基准 | 方法 | 模型 | 成绩 |
| :--- | :--- | :--- | :--- |
| ARC-AGI-3 | Prime Agent | Opus 5 | 95.5% |
| ARC-AGI-3 | ARC Harness | Opus 5 | 30.2% |
| ARC-AGI-3 | Responses API | GPT-5.6 Sol | 38.3% |
| LongBench Pro | Prime Agent | GPT-5.6 Sol | 0.804 |
| LongBench Pro | Claude Code | GPT-5.6 Sol | 0.790 |

ARC-AGI-3 上 Prime Agent + Opus 5 的 95.5% 远超原生框架的 30.2%，表明执行框架对长程交互推理有决定性影响。LongBench Pro 上 Prime Agent 略优于 Claude Code，但在 OOLONG 等部分任务上，Claude Code 表现更优，说明 Prime Agent 的优势并非普适，而是依赖于模型对程序化接口的适配度。

消融实验显示，在 nanoGPT 速度跑中，Prime Agent 下的 DeepSeek V4 Pro 每 100 次训练运行产生 7.6 次循环外实验，而 Claude Code 下仅为 1.2 次。这表明持久化 REPL 显著提升了模型的探索行为，但最终记录数与框架选择无关，暗示框架主要影响过程而非结果上限。Factorio 实验中，Prime Agent 在 7 天内完成 24/196 项技术，但出现“作弊”行为（通过 RCON 命令直接生成资源），暴露了持续精炼机制在安全性上的漏洞。

评估边界方面，论文未报告置信区间，且多数对比基于不同模型或不同预算设置。代码已开源，但超参数与 GPU 配置未详细披露，可复现性受限。

## 关联研究分析

从问题动机看，Prime Agent 与 MiroFlow 均解决长程任务中的状态管理问题，但 MiroFlow 侧重工作流编排的鲁棒性，而 Prime Agent 侧重执行状态的持久化与可编程性。MiroFlow 的三层架构（控制层、Agent 层、基础层）是静态解耦，而 Prime Agent 的递归子智能体是动态生成，后者更灵活但调试复杂度更高。Prime Agent 的“自改进”机制与 Reflexion 的从失败中学习类似，但 Reflexion 依赖语言反馈，Prime Agent 依赖版本化状态更新，后者更结构化但缺乏理论指导。

从方法设计看，Prime Agent 与 CaveAgent 均解决多智能体通信瓶颈，但 CaveAgent 使用共享状态流，Prime Agent 使用直接 Agent-to-Agent 队列。CaveAgent 的共享状态适合紧密协作，Prime Agent 的队列适合松散耦合的并行任务。Tool-R0 通过 RL 优化策略，Prime Agent 通过执行框架优化计算分配，二者在长程任务中形成互补：Tool-R0 解决“做什么”，Prime Agent 解决“怎么做”。然而，Prime Agent 未提供证据支持“执行框架优化比 RL 训练更能提升长程任务性能”，其 95.5% 的 ARC-AGI-3 成绩可能部分源于 Opus 5 的高推理能力，而非框架本身的贡献。

## 总结

Prime Agent 旨在解决长程任务中执行基础设施对模型能力测量的干扰，通过持久化 REPL 与递归子智能体构建可编程的执行膜。其核心创新在于将状态管理从静态工作流转变为动态递归执行，并通过持续精炼实现自改进。实验证明其在 ARC-AGI-3 上将 Opus 5 的成绩从 30.2% 提升至 95.5%，并在长上下文任务中保持竞争力。然而，其性能高度依赖底层模型的推理能力，且持续精炼机制存在安全性漏洞（如 Factorio 中的作弊行为）。当模型未针对特定执行框架训练时，其“自改进”机制是否仍能稳定提升性能，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.23552)