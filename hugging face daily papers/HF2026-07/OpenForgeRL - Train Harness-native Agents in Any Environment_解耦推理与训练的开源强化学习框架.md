# HuggingFace最新推荐论文 ｜OpenForgeRL: Train Harness-native Agents in Any Environment ｜解耦推理与训练的开源强化学习框架

研究机构：美国哥伦比亚大学、美国达特茅斯学院

作者：Xiao Yu、Baolin Peng、Ruize Xu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.21557)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.21557)

> 现代智能体依赖复杂的推理框架（Inference Harness）来管理多轮交互与工具调用，但现有开源强化学习（RL）基础设施无法原生支持这种有状态、多进程的执行流程，导致训练与部署环境严重脱节。本文提出 OPENFORGE RL，通过轻量级代理拦截框架内的模型调用，并利用 Kubernetes 在云端远程容器中执行 Rollout，实现了任意推理框架与任意环境的端到端 RL 训练。该框架在工具使用与 GUI 操作基准上显著提升了开源模型性能，但其对部分 Rollout 错误处理的粗糙策略及代理引入的潜在延迟，仍是制约其收敛效率与鲁棒性的关键疑点。

## 研究背景

当智能体在复杂环境中执行长程任务时，其推理过程不再局限于简单的“观察-行动”循环，而是被包裹在包含子智能体、技能库和复杂控制流的推理框架（Inference Harness）中。这种框架改变了模型的有效上下文，使得传统的基于原始交互历史的强化学习（RL）训练失效。为了解决这一矛盾，研究者需要一种能够抽象框架内部复杂性、同时保持训练与部署一致性的基础设施。

当前主流开源 RL 框架（如 veRL, Slime）假设 Rollout 在本地训练节点内运行，且仅支持单轮生成或轻量级工具调用。然而，工业级推理框架（如 Claude Code, Codex）需要独立的容器化环境，且其内部状态不向训练器暴露。这种架构假设的断裂导致开源社区不得不重新实现简化版框架进行训练，造成了严重的训练-部署不一致（Train-Deploy Mismatch）。本文的切入点在于，不修改 RL 算法本身，而是通过解耦推理与训练的物理位置，构建一个通用的“框架-环境”训练接口，使开源模型能在真实部署环境中进行端到端优化。

## 核心方法

### 方法参照系

标准 RL 训练流程假设训练器直接控制模型生成过程，Rollout 在本地执行并直接返回轨迹。本文问题的关键差异在于，推理框架（Harness）内部封装了复杂的控制流，训练器无法直接访问其内部状态，且 Rollout 需要独立的计算资源，无法与训练节点共置。

### 轻量级代理与轨迹重构

传统 RL 框架直接调用模型 API 生成动作，而本文在推理服务器与框架之间插入一个轻量级代理（Proxy）。代理拦截框架发出的所有生成请求，将其路由至 RL 框架的推理引擎，并记录交换的输入输出对。当 Rollout 结束时，代理收集终端奖励 $r_T$ 和提示-响应对 $(s_{[H]}, a)$，重构为标准训练样本。这一设计解决了框架内部状态不可见导致的训练信号缺失问题，使得任何复杂框架都能作为黑盒接入 RL 训练。

$$ \tau = \langle (H(s_0), a_0), (H(s_1), a_1), \dots, (H(s_T), a_T) \rangle $$

该公式表示重构后的轨迹 $\tau$ 是框架处理后的状态-动作对的无序集合，其中 $H(s_t)$ 代表框架内部处理后的有效上下文，而非原始环境观察。

### 远程容器化 Rollout 编排

针对框架 Rollout 需要独立 CPU/内存资源的问题，本文基于 Kubernetes 构建编排器，在云端（如 Azure）为每个 Rollout 启动独立的容器 Pod。为解决远程 Rollout 可能阻塞训练批次的异步问题，本文摒弃了不可靠的“轮次限制”，转而采用宽松的墙钟超时（Wall-clock Timeout）机制。当任务超时或发生非策略错误（如网络故障）时，直接丢弃该轨迹，避免部分 Rollout 引入误导性训练信号。

$$ A_i = \frac{r_i - \text{mean}(r_{\text{group}})}{\text{std}(r_{\text{group}})} $$

在采用 GRPO 算法时，优势函数 $A_i$ 通过比较同一组内不同轨迹的平均奖励计算，这种组内相对评估机制在远程异步 Rollout 场景下能有效缓解奖励稀疏问题。

## 实验评估

实验在 ClawEval、QwenClawBench、MCPAtlas（工具使用）及 OSWorld-Verified、Online-Mind2Web、WebVoyager（GUI）六个基准上进行。基线对比涵盖了同规模开源模型（如 OpenCUA, UI-TARS, MolmoWeb）及未训练的骨干模型（Qwen3-30B-A3B-Thinking, Qwen3-VL-8B-Thinking），但缺失闭源前沿模型（如 Claude Code）的直接对比，限制了绝对性能的评估。

| 基准 | 模型 | 指标 | 数值 |
| :--- | :--- | :--- | :--- |
| ClawEval | OpenForge-Claw (SFT+RL) | pass@3 | 55.9 |
| ClawEval | OpenForge-Claw (SFT+RL) | pass[3] | 31.7 |
| QwenClawBench | OpenForge-Claw (SFT+RL) | pass@1 | 33.7 |
| OSWorld-Verified | OpenForge-GUI (SFT+RL) | pass@1 | 37.7 |
| Online-Mind2Web | OpenForge-GUI (SFT+RL) | pass@1 | 63.0 |
| WebVoyager | OpenForge-GUI (SFT+RL) | pass@1 | 72.3 |

OpenForge-Claw 在 ClawEval 上达到 55.9% (pass@3)，显著优于未训练骨干模型的 39.8%；OpenForge-GUI 在 WebVoyager 上达到 72.3%，超越了使用 20 万任务训练的 MolmoWeb，表明该框架在数据高效性上具有优势。

消融实验揭示了框架选择对训练难度的影响。在 ClawEval 上，支持自定义工具的 ReACT* 和 ZeroClaw 表现最佳，而复杂的 Codex 框架虽然基线低，但经 SFT+RL 训练后提升幅度最大（+20.3）。这表明更简单、与模型能力对齐的框架更容易学习，但多框架联合训练能提升跨框架泛化能力。RL 训练还改变了工具使用模式，将通用 Shell 调用比例从 22.6% 降至 13.9%，提升了专用工具的使用率。

评估协议存在局限：GUI 任务依赖 GPT-4.1 作为评估器，可能存在评估偏差；部分 Rollout 错误处理采用直接丢弃策略，未探索细粒度信用分配。代码与数据将开源，但代理引入的网络延迟对 RL 收敛速度的影响未在文中量化。

## 关联研究分析

从问题动机看，本文与 SWE-Agent 等早期工作不同，后者聚焦于设计特定的智能体-计算机接口以提升任务成功率，而本文聚焦于如何训练这些已存在的复杂接口。SWE-Agent 等框架通常作为评测对象，而 OPENFORGE RL 将其作为训练对象，解决了“训练环境简化”与“部署环境复杂”之间的鸿沟。这种差异源于任务特性的变化：早期任务相对静态，而现代智能体任务涉及动态的多进程交互，使得传统的本地 Rollout 假设失效。

从方法设计看，本文与 veRL 等开源 RL 框架共享底层算法（如 GRPO），但在 Rollout 机制上存在根本差异。veRL 假设 Rollout 在本地执行，而本文通过 Kubernetes 远程容器化解决了资源隔离问题。与 Polar 等并发工作相比，本文覆盖了更广泛的场景（文本工具与 GUI），并深入分析了框架选择对行为的影响。Polar 聚焦于软件工程任务，而本文的通用性设计使其能适配任意框架与环境，但这也带来了更高的工程复杂度，如代理拦截可能引入的延迟和状态同步问题。

## 总结

本文旨在解决复杂推理框架与开源 RL 基础设施之间的架构断裂，通过解耦推理与训练，使模型能在真实部署环境中进行端到端优化。OPENFORGE RL 利用轻量级代理重构轨迹，并通过远程容器化 Rollout 实现了可扩展训练，在 ClawEval 和 WebVoyager 等基准上显著提升了开源模型性能。然而，实验暴露出框架复杂度与可学习性之间的权衡，以及部分 Rollout 错误处理的粗糙性。当代理引入的网络延迟与远程 Rollout 的异步性叠加时，RL 策略的收敛稳定性是否会受到显著影响，论文未给出定量回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.21557)