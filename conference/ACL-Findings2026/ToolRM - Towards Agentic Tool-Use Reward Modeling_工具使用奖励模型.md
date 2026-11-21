# ACL-Findings2026最新论文 ｜ToolRM: Towards Agentic Tool-Use Reward Modeling ｜工具使用奖励模型

研究机构：澳门大学、澳大利亚新南威尔士大学

作者：Renhao Li、Jianhong Tu、Yang Su 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26167)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26167)

> 工具增强大语言模型（Tool-Augmented LLMs）的强化学习训练依赖可靠的奖励信号，但现有方法多依赖人工标注轨迹或简单规则，难以泛化至未见工具场景。本文切入点在于构建无需 ground-truth 标签、具备因果推理能力的专用奖励模型（Reward Model, RM）。通过规则基评分与平衡多维采样构建偏好数据，训练轻量级生成式与判别式 RM。该工作填补了工具使用领域专用 RM 的空白，但其规则基评分在复杂非结构化 API 返回下的鲁棒性存疑。

## 研究背景

当智能体执行多步工具调用时，中间步骤的错误会级联传播，导致最终任务失败。解决此问题的主流范式是基于可验证奖励的强化学习（Reinforcement Learning from Verifiable Rewards, RLVR），其核心假设是环境反馈可替代人工标注。然而，RLVR 的有效性高度依赖奖励模型（RM）对工具调用质量的精确评估。当前 RM 多针对通用对话或数学推理设计，缺乏对工具调用参数正确性、依赖顺序及执行可行性的细粒度判别能力，导致 RL 训练中出现奖励稀疏或噪声干扰。

工具使用领域的 RM 构建面临三个关键挑战：高质量偏好对构造、超越表面匹配的批判能力、以及专用评估基准缺失。现有工作如 Tool-R1 依赖环境执行验证，限制了在无标注领域的扩展；Agarwal et al. (2025) 虽评估了函数调用 RM，但数据对过于简单，无法区分强模型。本文提出 ToolRM，通过规则基评分自动构造细粒度偏好对，并引入 TRBenchBFCL 基准，旨在解决 RM 在工具使用场景下的泛化性与评估标准化问题。

## 核心方法

### 方法参照系

标准 RLVR 流程中，RM 通常通过 Bradley-Terry 模型在人工标注偏好对上训练，输出标量奖励以指导策略优化。本文的关键差异在于：不依赖人工标注，而是利用规则基评分自动构造偏好对，并采用生成式目标（GRPO）训练 RM 以获取可解释的批判能力，而非仅输出标量分数。

### 规则基评分与偏好对构造

针对偏好对构造中人工标注成本高且分布外泛化差的问题，本文设计规则基评分函数 $\hat{s}$ 自动评估采样响应 $y_{\hat{}}$ 与 ground-truth 响应 $y_{*}$ 的匹配度。该函数优先评估工具调用内容正确性而非格式严格性，以适配下游多样化调用结构。

$$
\hat{s} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[c_{\hat{l}}^{name} = c_{*i}^{name}] \cdot \text{sim}(c_{\hat{l}}^{args}, c_{*i}^{args})
$$

其中 $\text{sim}(\cdot)$ 计算参数字典中相同键值对的比例，字符串比较不区分大小写。若工具调用数量不匹配或存在重复调用，$\hat{s}$ 直接置为 0。基于 $\hat{s}$，从候选池 $D_{cand}$ 中选取分数不同的响应构成偏好对 $(y_{+}, y_{-})$，其中 $y_{+}$ 分数高于 $y_{-}$。此设计解决了传统 RM 训练依赖人工标注导致的分布外泛化瓶颈，通过规则验证确保偏好信号的客观性与细粒度。

### 平衡多维采样与生成式训练

为提升 RM 在复杂任务上的批判能力，本文采用平衡多维采样（Balanced Multi-Dimensional Sampling, BMDS）策略从偏好对候选池 $D_{pair-cand}$ 中选取数据。BMDS 以数据源、偏好强度（分数差）、任务复杂度为复合键，优先选取样本数最少的组，确保多样性与挑战性。

$$
\mathcal{L}_{GRPO} = \mathbb{E}_{q \sim D_{pref}} \left[ \frac{1}{G} \sum_{i=1}^{G} \left( \frac{\pi_{\theta}(o_i|q)}{\pi_{old}(o_i|q)} r_i - \log \sum_{j=1}^{G} \exp(\log \pi_{\theta}(o_j|q) + r_j) \right) \right]
$$

其中 $r_i$ 为二元奖励，取决于模型是否正确提取并选择了更优响应。生成式 ToolRM 通过 GRPO 训练，输出包含 `<evaluation>` 和 `<choice>` 标签的文本批判，而非标量分数。此设计解决了判别式 RM 仅输出分数缺乏可解释性、难以用于自纠正的问题，使 RM 能生成紧凑且高质量的批判反馈，支持推理时扩展。

## 实验评估

实验在 TRBenchBFCL 上评估 RM 判别能力，在 ACEBench 上评估下游自纠正效果。基线覆盖前沿 LLM（Claude-4-Sonnet, GPT-4o）及专用 RM（Skywork-Reward, RRM），但未对比知识库中提到的 TRM 或 PROVE 等细粒度过程奖励模型，可能遗漏强基线。

| 模型 | W-Avg. Acc (%) |
| :--- | :--- |
| Claude-4-Sonnet (w/ thinking) | 75.18 |
| ToolRM-Gen-Qwen3-4B-Thinking-2507 | 71.87 |
| ToolRM-Disc-Qwen3-4B-Instruct-2507 | 77.61 |
| Skywork-Reward-V2-Qwen3-4B | 80.28 |

ToolRM-Disc 在 TRBenchBFCL 上取得 77.61% 准确率，高于 Claude-4-Sonnet 的 75.18%，但低于 Skywork-Reward-V2 的 80.28%。在 ACEBench 自纠正任务中，ToolRM-Gen 使 Qwen3-4B 准确率从 63.4% 提升至 74.8%（+11.4 点），且平均输出长度从 3,211 降至 1,111 tokens，验证了生成式 RM 在效率与质量间的平衡。

消融实验显示，移除 BMDS 策略导致 W-Avg. Acc 下降 4.63 点（71.87% → 67.24%），移除难度感知采样（DDS）下降 3.23 点，表明数据多样性与难度控制对 RM 性能贡献最大。使用通用偏好数据（NormalPref）训练仅提升 4.15 点，而工具专用数据（ToolPref）提升 7.18 点，证明领域特定数据的关键作用。

评估边界方面，TRBenchBFCL 基于 BFCL 构建，可能引入对 ToolRM 训练分布的过拟合偏差。可复现性上，论文提供代码与数据，但仅报告单 epoch 训练结果，未提供置信区间或多随机种子平均，数值比较需谨慎。

## 关联研究分析

从问题动机看，ToolRM 与 Tool-R1 均致力于解决 RLVR 中的奖励信号问题，但 Tool-R1 依赖环境执行验证，而 ToolRM 通过规则基评分替代环境反馈。这一差异源于任务特性：Tool-R1 面向可执行环境，而 ToolRM 旨在覆盖无执行环境的领域。然而，规则基评分在 API 返回非结构化数据时如何保证准确性，论文未给出回答。

从方法设计看，ToolRM 与 Skywork-Reward 同属偏好学习框架，但 Skywork 使用通用对话数据，而 ToolRM 使用工具调用专用数据。实验显示 ToolRM 在工具任务上优于 Skywork，但在通用任务上可能泛化性受限。这种领域特异性是否导致 RM 在跨域工具使用中的性能下降，论文未探索。

## 总结

本文核心矛盾在于 RLVR 依赖可靠 RM，但现有 RM 缺乏工具使用领域的细粒度判别能力。切入点在于利用规则基评分自动构造偏好对，避免人工标注瓶颈。方法上，通过 BMDS 策略与 GRPO 训练生成式/判别式 RM，在 TRBenchBFCL 上取得 77.61% 准确率，在 ACEBench 自纠正中提升 11.4 点。边界在于规则基评分对非结构化 API 返回的鲁棒性未验证，且未对比 TRM 等过程奖励模型。当 API 返回包含噪声或模糊描述时，规则基评分的准确性是否仍能支撑 RM 的有效训练，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26167)