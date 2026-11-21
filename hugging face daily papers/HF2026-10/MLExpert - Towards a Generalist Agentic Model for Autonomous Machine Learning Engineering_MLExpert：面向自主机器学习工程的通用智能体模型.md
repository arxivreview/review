# HuggingFace最新推荐论文 ｜MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering ｜MLExpert：面向自主机器学习工程的通用智能体模型

作者：Shangheng Du、Jinxin Shi、Shuaiyu Zhang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.22344)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22344)

> 导读 自主机器学习工程（Machine Learning Engineering, MLE）旨在让大语言模型（Large Language Model, LLM）通过长周期交互自主优化代码与模型，以逼近递归自我改进（Recursive Self-Improvement, RSI）的目标。现有系统多依赖外部编排或单步决策，难以处理长周期实验中反馈延迟与策略不匹配的问题。本文提出 MLExpert，通过分层代理监督微调（Supervised Fine-Tuning, SFT）与窗口化交互强化学习（Windowed Interaction Reinforcement Learning, WIRL），将执行反馈转化为多轮决策的联合优化信号。该工作证明了 35B 参数模型经后训练后可在 MLE 任务上媲美前沿大模型，但其泛化边界与安全性验证仍存疑。

## 研究背景

当 LLM 从辅助科研转向自主开发 AI 系统时，MLE 成为检验其长周期优化能力的具体场景。MLE 要求模型在给定时间预算内，通过反复执行代码、分析反馈并修正方案来寻找最优解，而非一次性生成。这一过程涉及数据预处理、特征工程、模型训练等多个阶段，任何单步失误都可能导致后续优化偏离轨道。传统的 MLE 系统通常采用外部编排，由预定义的工作流或搜索规则控制实验顺序，LLM 仅在指定步骤生成或调试代码。这种架构将复杂的决策逻辑外包给人工设计的控制流，限制了模型根据实验状态动态调整策略的能力。

随着模型能力的提升，研究重心转向模型主导的交互，允许模型自主组织实验。然而，长周期 MLE 训练面临三大挑战：首先，开放环境需要保留实验状态并允许模型自由选择动作；其次，高质量监督数据稀缺，长轨迹中混杂着有效探索与无效退化；最后，昂贵的实验反馈往往滞后于决策，在线强化学习（Reinforcement Learning, RL）需利用中间信号并处理异步收集中的策略不匹配。现有方法如 ML-Agent 仅训练单步决策，Frontis-MA1 则依赖外部进化框架，均未解决模型自主组织长周期实验的核心难题。

## 核心方法

### 方法参照系：模型主导的长周期交互

本文方法置于模型主导的 MLE 优化框架下，区别于外部编排。标准流程中，模型通过 ReAct 风格的循环与环境交互，但通常缺乏对长周期实验状态的结构化管理。本文引入 Interaction Harness，将实验状态存储为包含代码、日志和元数据的解决方案节点，形成可回溯的实验树。模型通过工具调用（如 `execute_code`）启动实验，并根据执行反馈决定继续、回溯或改变方向。这一架构为后续的分层 SFT 和 WIRL 提供了可执行的任务环境与状态管理基础。

### 分层代理监督微调与结果引导筛选

为解决长轨迹中噪声干扰问题，本文采用两阶段分层 SFT。第一阶段利用通用编码与工具使用轨迹建立基础能力；第二阶段针对 MLE 领域，使用教师轨迹进行域适应。关键创新在于结果引导的监督选择机制。长轨迹中，模型可能在达到最佳性能后继续退化。本文定义锚点为轨迹中首个最佳提交，若后续性能下降超过阈值，则截断至锚点前的完整工具交互边界。

$$
\text{Loss}_{SFT} = -\sum_{t \in \mathcal{T}_{new}} \log \pi_\theta(a_t | c_t)
$$

该公式表示仅对新产生的推理、文本响应和工具调用令牌计算损失，工具反馈和继承的历史交互仅作为条件上下文被掩码。这一设计保留了峰值前的有效探索与失败恢复，剔除了退化尾部，确保监督信号的质量。

### 窗口化交互强化学习（WIRL）

在 SFT 基础上，WIRL 利用模型自身探索的执行反馈优化策略。针对反馈延迟问题，WIRL 将连续两次实验结果之间的多轮决策划分为一个执行窗口 $u_m$。每个窗口共享基于执行结果的奖励，允许在轨迹结束前进行策略更新。

$$
R_m = \begin{cases}
-1.0, & \text{execution error} \\
-0.6, & \text{no scorable submission} \\
-0.4 + T_m, & \text{below medal threshold} \\
1.0 + T_m, & \text{bronze/silver medal} \\
2.0 + T_m, & \text{gold medal}
\end{cases}
$$

其中 $T_m \in \{-0.2, 0, 0.2\}$ 表示相对于上一次有效提交的性能趋势。不同于标准 GRPO 的组内归一化，WIRL 直接使用可验证的执行奖励作为共享优化权重 $\hat{A}_m = R_m$。为解决异步收集中的策略不匹配，引入令牌级策略校正：

$$
c_{m,j,t} = \text{sg}\left( \exp(\ell^{old}_{m,j,t} - \ell^{roll}_{m,j,t}) \cdot \mathbb{1}[q_{min} \le q_{m,j,t} \le q_{max}] \right)
$$

该公式通过记录收集时的对数概率，对当前训练策略与滚动策略之间的偏差进行加权校正，超出界限的令牌被排除在策略梯度更新之外。这一机制使模型能利用中间反馈，在长周期任务中实现稳定的在线学习。

## 实验评估

实验在 MLE-Bench Lite（22 个 Kaggle 竞赛任务）和 NatureBench Lite 上进行。基线覆盖同规模模型（Qwen3.6-35B-A3B 等）及前沿模型（Kimi-K3, GLM-5.3 等）。MLExpert 在 MLE-Bench Lite 上的奖牌率（Any Medal）达到 72.7%，较基座模型 Qwen3.6-35B-A3B 的 37.9% 提升显著，并接近 Kimi-K3 的 72.7%。在通用编码框架 Claude Code 下，MLExpert 仍保持 69.7% 的奖牌率，证明其能力不依赖于特定 Harness。

| 方法 | 骨干模型 | MLE-Bench Lite 奖牌率 (%) | NatureBench Lite Surpass-SOTA (%) |
| :--- | :--- | :--- | :--- |
| Qwen3.6-35B-A3B | Qwen3.6-35B-A3B | 37.9 | 0.0 |
| Nex-N2.5-mini | Nex-N2.5-mini | 47.0 | 20.0 |
| GLM-5.3 | GLM-5.3 | 72.7 | 50.0 |
| Kimi-K3 | Kimi-K3 | 72.7 | 70.0 |
| **MLExpert** | **Qwen3.6-35B-A3B** | **72.7** | **50.0** |

消融实验显示，分层 SFT 将奖牌率从 37.9% 提升至 62.1%，WIRL 进一步提升至 72.7%。移除趋势奖励或策略校正的 WIRL 变体分别降至 66.7% 和 65.2%，表明局部趋势奖励与策略校正对最终性能均有贡献。标准 GRPO 和 PPO 风格优化仅达到 56.1% 和 60.6%，低于 MLE-SFT，验证了窗口化反馈机制的有效性。

评估边界方面，MLE-Bench Lite 任务分布可能限制泛化性结论。实验未报告置信区间，且未对比 Darwin Gödel Machine 等纯进化式基线。代码未开源，复现依赖特定硬件配置（单 NVIDIA H200 GPU）。

## 关联研究分析

从问题动机看，MLExpert 与 EvolveR 均致力于经验内化，但路径不同。EvolveR 采用定期将非参数化文本经验蒸馏为参数的离线方式，而 MLExpert 通过 WIRL 实现在线异步 RL，直接利用执行反馈优化策略。这种差异源于 MLE 任务对实时反馈的依赖：离线蒸馏无法捕捉实验过程中的动态状态变化，而在线 RL 能即时修正策略。然而，MLExpert 未讨论 EvolveR 所关注的长期知识固化与灾难性遗忘问题，其在线更新是否会导致旧任务能力退化尚不明确。

从方法设计看，MLExpert 与 Darwin Gödel Machine 形成互补。Darwin Gödel Machine 通过外部进化机制优化智能体结构，属于非参数化或结构进化路线；MLExpert 则通过参数更新内化优化策略。在 SWE-bench 上，Darwin Gödel Machine 达到 50.0% 的解决率，而 MLExpert 在 MLE-Bench 上达到 72.7% 的奖牌率。由于任务不同，直接比较数值无意义，但两者揭示了“结构进化”与“参数进化”在不同任务复杂度下的适用性差异。MLExpert 未探索结构进化，其固定架构是否限制了在更复杂软件工程任务中的表现，是一个潜在的盲区。

## 总结

MLExpert 针对长周期 MLE 任务中反馈延迟与策略不匹配的核心矛盾，提出分层 SFT 与 WIRL 框架，通过执行窗口机制将中间反馈转化为多轮决策的联合优化信号。实验证明，35B 模型经后训练后在 MLE-Bench Lite 上达到 72.7% 的奖牌率，媲美前沿大模型。然而，其评估局限于特定基准，未验证在更广泛软件工程任务中的泛化性，且缺乏对进化安全性的讨论。当模型在开放环境中自主生成代码时，如何确保其优化策略不偏离人类意图，仍是该路线尚未解决的隐患。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.22344)