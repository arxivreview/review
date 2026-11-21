# HuggingFace最新推荐论文 ｜Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning ｜电子表格智能体强化学习框架

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Banghao Chi、Yining Xie、Mingyuan Wu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22642)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22642)

> 电子表格操作涉及长程依赖与复杂状态，现有基于提示工程的智能体难以可靠执行多步工作流。本文指出，缺乏领域特定的模型侧训练是性能瓶颈，而非单纯依赖通用大模型能力。Spreadsheet-RL 通过构建自动化数据管道与异步强化学习（RL）环境，对开源小模型进行后训练。该框架验证了结果导向的 RL 在电子表格领域的有效性，但其绝对性能仍显著落后于闭源前沿模型，且泛化能力在特定领域存在局限。

## 研究背景

电子表格任务的核心难点在于状态不可见性与操作序列的长程依赖。LLM 无法直接感知 Excel 内存中的完整数据状态，导致基于错误假设继续执行。这种状态盲区使得传统的“静态提示”范式失效，因为智能体缺乏对中间步骤正确性的实时反馈机制。为了解决这一问题，需要引入能够与环境实时交互、并通过执行结果验证操作正确性的闭环架构。

数据科学智能体（DSA）领域的主流路线多聚焦于推理时设计，如 ReAct 范式与多智能体协作，旨在通过角色分工缓解长上下文注意力稀释。然而，这些方法在电子表格这一特定场景中面临瓶颈：现有工作如 SheetCopilot 和 SheetAgent 主要依赖 GPT-4o 等专有模型的通用能力与提示工程，缺乏针对电子表格操作语义的模型侧优化。这导致智能体在处理复杂公式、布局调整等多步任务时，错误率随步骤增加而累积。Spreadsheet-RL 的切入点在于，将电子表格操作形式化为部分可观测马尔可夫决策过程，通过强化学习直接优化策略模型，而非仅依赖提示技巧。

## 核心方法

### 方法参照系

本文问题归属于结构化编排与状态管理类别，但关键差异在于训练范式。传统 DSA 方法（如 Data Interpreter）采用推理时工具调用，模型参数冻结；而 Spreadsheet-RL 引入模型侧 RL 微调，将电子表格环境交互纳入训练循环，以解决弱初始策略下的长程任务学习难题。

### 自动化任务构建与 Oracle 生成

设计动机在于解决 RL 训练数据稀缺问题。传统方法依赖人工标注或 LLM 合成，成本高且分布失真。本文提出 Spreadsheet Data Agent，从 ExcelForum 收集真实讨论帖，利用编码智能体（如 Claude Code）生成可执行的操作序列，并通过规则过滤验证 Oracle 的正确性。该过程将原始论坛数据转化为包含初始表格 $D_i$、指令 $T$ 和 Oracle 最终表格 $D_O$ 的训练对。

### 异步 RL 训练与结果导向奖励

设计动机在于克服长程任务中稀疏终端奖励导致的训练不稳定。本文采用 GRPO（Group Relative Policy Optimization）算法，结合结果导向奖励函数。奖励计算基于预测表格 $D_{pred}$ 与 Oracle $D_O$ 在操作区域 $M$ 上的全单元格匹配：

$$ R(D_i, T, D_O) = \text{allcellsmatch}(D_{pred}, D_O, M) $$

该公式通过精确匹配数值与公式，提供可验证的监督信号。训练目标最小化策略 $\pi_\theta$ 与参考模型 $\pi_{ref}$ 的 KL 散度，同时最大化期望奖励：

$$ \max_{\pi_\theta} \mathbb{E}_{[D_i,T] \sim D, y \sim \pi_\theta} [ R(D_i, T, D_O) ] - \beta D_{KL}[\pi_\theta(\cdot | D_i, T; G) \| \pi_{ref}(\cdot | D_i, T; G)] $$

此设计避免了 Critic 模型的高昂开销，并通过异步提交-轮询验证器实现 Excel 环境下的并行奖励计算，提升了训练效率。

## 实验评估

实验在 SpreadsheetBench（912 任务）和自建 Domain-Spreadsheet（1660 任务）上进行。基线覆盖闭源模型（GPT-4o, o3, ChatGPT Agent）和开源 Qwen3 系列。本文方法在开源模型中表现最优，但绝对性能仍落后于闭源前沿模型。

| 模型/方法 | 环境 | Pass@1 (%) |
| :--- | :--- | :--- |
| Qwen3-4B-Thinking-2507 (Base) | Spreadsheet Gym | 12.0 |
| + Native Harness | Spreadsheet Gym | 15.6 |
| + Full Tools | Spreadsheet Gym | 19.3 |
| + Spreadsheet-RL | Spreadsheet Gym | 23.4 |
| ChatGPT Agent | OSX, LibreOffice | 45.5 |
| Copilot Agent Mode | Windows, Excel | 57.7 |

消融实验显示，从基础模型到最终 RL 模型，性能提升分为三个阶段：原生交互框架贡献 3.6 个百分点，全面工具访问贡献 3.7 个百分点，RL 后训练贡献 4.1 个百分点。这表明工具接口设计对初始策略至关重要，而 RL 进一步提升了长程任务的鲁棒性。在 Domain-Spreadsheet 上，整体 Pass@1 从 8.4% 提升至 17.2%，其中金融领域提升最显著，但房地产领域保持 1.1% 不变，表明当前 4B 模型在特定领域泛化能力有限。

评估边界方面，本文主要依赖精确匹配指标，未报告置信区间或计算成本（如 Token 消耗）的详细对比。可复现性方面，代码与数据已开源，但 RL 训练依赖 Windows 与 Excel 环境，限制了跨平台复现的便捷性。

## 关联研究分析

从问题动机看，本文与 Data Interpreter 等单体智能体方法的核心差异在于优化目标。Data Interpreter 依赖通用 LLM 的推理能力，通过提示工程引导工具调用，而 Spreadsheet-RL 通过 RL 直接优化模型参数，使其内化电子表格操作语义。这一差异源于电子表格任务的长程依赖特性：提示工程难以覆盖所有可能的操作组合，而 RL 可通过环境交互探索更优策略。然而，本文未探索多智能体协作架构，这与 DSA 领域“多智能体更优”的共识相悖。这可能是因为电子表格操作具有强顺序性，角色分工可能引入通信开销，但论文未提供定量证据支持这一假设。

从方法设计看，本文与 SheetCopilot 等提示工程方法相比，引入了模型侧训练。SheetCopilot 依赖 GPT-4o 的通用能力，而 Spreadsheet-RL 证明在 4B 小模型上，通过领域特定 RL 可显著提升性能。这一发现挑战了“大模型必然更优”的假设，表明领域特定训练对小模型至关重要。然而，本文的 RL 训练数据来自论坛讨论，可能存在分布偏差，导致在 Domain-Spreadsheet 部分领域（如房地产）泛化失败。这暗示了数据多样性对 RL 泛化能力的关键作用，但论文未深入分析数据分布与性能之间的具体关系。

## 总结

Spreadsheet-RL 解决了电子表格智能体在长程任务中状态不可见与策略弱初始化的矛盾。通过构建自动化数据管道与异步 RL 框架，本文证明结果导向的 RL 可显著提升开源小模型的性能，将 Qwen3-4B 在 SpreadsheetBench 上的 Pass@1 从 12.0% 提升至 23.4%。然而，其绝对性能仍远低于闭源模型（如 Copilot 的 57.7%），且在房地产等特定领域泛化能力停滞。当训练数据分布与目标领域存在显著差异时，RL 的泛化边界究竟由数据多样性还是模型容量决定，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22642)