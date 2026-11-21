# HuggingFace最新推荐论文 ｜Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights ｜预训练权重邻域的“灌木丛”现象与随机优化算法

研究机构：美国麻省理工学院

作者：Yulu Gan、Phillip Isola

论文原文见 [arXiv](https://arxiv.org/abs/2603.12228)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12228)

> 导读 大语言模型后训练的核心矛盾在于模仿学习的稳定性与探索学习的泛化性之间的张力，现有方法如监督微调（Supervised Fine-Tuning, SFT）和强化学习（Reinforcement Learning from Human Feedback, RLHF）均依赖迭代优化来寻找最优解。然而，这些方法隐含假设预训练权重处于损失景观的局部极小值，需通过梯度下降逐步逃离。本文指出，随着模型规模扩大，预训练权重邻域内任务改进解的密度急剧增加，形成“灌木丛”（Thicket）区域，使得随机猜测成为可能。本文提出RandOpt算法，通过并行采样高斯权重扰动并集成Top-K模型预测，实现无梯度后训练。该研究挑战了后训练必须依赖迭代优化的传统范式，揭示了预训练对损失景观几何结构的重塑作用，但其有效性是否随模型规模无限扩展仍存疑。

## 研究背景

当大语言模型（Large Language Model, LLM）完成预训练后，其参数向量通常被视为一个固定的起点，后续通过SFT或RL进行迭代优化以适配下游任务。这一过程隐含了一个关键假设：预训练权重位于损失景观的局部极小值或平坦区域，必须通过结构化搜索（如梯度下降）才能找到性能更优的解。然而，Schmidhuber等人（2001）曾指出，若解空间足够密集，随机猜测即可有效。在早期小规模模型中，这一观点被视为基准测试的缺陷，因为解的密度极低，属于“大海捞针”（needle in a haystack）状态。

随着模型规模从百万参数扩展至千亿参数，损失景观的几何结构发生根本性变化。主流后训练路线如PPO、GRPO等，均通过顺序更新策略来探索解空间，计算成本高且易受分布偏移影响。本文提出，在大规模预训练模型中，权重邻域内存在大量任务特定的“专家”解，其密度随模型规模呈幂律增长。这一现象被称为“灌木丛”（Thicket）区域。在此区域内，随机采样即可高效发现高性能解，且这些解具有高度多样性，表现为不同扰动在不同任务上表现互补。这一发现挑战了“后训练必须依赖迭代优化”的共识，为无梯度并行后训练提供了理论依据。

## 核心方法

### 方法参照系：从迭代优化到并行采样

传统后训练方法如SFT和RL，均属于顺序优化范式，通过计算梯度并逐步更新参数以最大化奖励或最小化损失。本文提出的RandOpt算法完全摒弃了梯度计算和顺序更新，转而采用并行随机采样与集成策略。其核心差异在于：传统方法寻找单一全局最优解，而RandOpt利用预训练权重邻域内解的密度与多样性，通过采样多个局部最优解并集成其预测，实现性能提升。这一方法将计算负担从训练时的迭代更新转移至推理时的集成计算，属于进化策略（Evolutionary Strategies, ES）的并行化变体，但去除了变异与交叉算子，仅保留采样与选择步骤。

### 核心创新：灌木丛现象的量化与RandOpt算法

本文首先量化了预训练权重邻域内解的密度与多样性。定义解密度 $\delta(m)$ 为随机高斯扰动使模型性能提升至少 $m$ 的概率：

$$
\delta(m) = \mathbb{P}_{\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})} [s(\boldsymbol{\theta} + \sigma \boldsymbol{\epsilon}) \geq s(\boldsymbol{\theta}) + m]
$$

其中 $s(\cdot)$ 为性能评估指标，$\sigma$ 为噪声尺度。实验表明，$\delta(m)$ 随模型规模单调增加，证实了“灌木丛”现象的存在。同时，定义谱不一致性（Spectral Discordance）$D$ 来衡量解的多样性：

$$
D = \frac{1}{M(M-1)} \sum_{j \neq k} (1 - C_{jk})
$$

其中 $C_{jk}$ 为任务 $j$ 和 $k$ 性能排名的Pearson相关系数。$D$ 随模型规模增加，表明扰动解是“专家”而非“通才”，即提升某任务性能往往损害其他任务性能。

基于此，RandOpt算法分为训练与推理两阶段。训练阶段，从预训练权重 $\boldsymbol{\theta}$ 出发，采样 $N$ 个高斯扰动 $\boldsymbol{\theta}_i = \boldsymbol{\theta} + \sigma_i \boldsymbol{\epsilon}_i$，评估其在训练集上的性能，选择Top-K模型。推理阶段，对这K个模型的预测结果进行多数投票集成：

$$
\hat{y} = \text{majority\_vote}(\{f_{\boldsymbol{\theta}_i}(x) \mid i \in I_{\text{top}}\})
$$

该设计动机在于利用邻域内解的多样性，通过集成互补的“专家”模型，避免单一解的过拟合风险，同时实现 $O(1)$ 的训练时间复杂度。

## 实验评估

本文在Qwen、Llama、OLMo3等模型（0.5B–8B参数）上，针对数学（GSM8K, MATH-500）、代码（MBPP）、写作（ROCStories）及化学（USPTO）任务进行评估。基线包括PPO、GRPO、进化策略（ES）及测试时多数投票（Test-Time Majority Vote, TT-MV）。

| 模型 | 方法 | GSM8K (%) | 备注 |
| :--- | :--- | :--- | :--- |
| Qwen2.5-3B-Instruct | Base | 56.1 | 基线 |
| Qwen2.5-3B-Instruct | GRPO | 82.0 | 迭代优化基线 |
| Qwen2.5-3B-Instruct | RandOpt (K=50) | 86.7 | 本文方法 |

在同等训练FLOPs下，RandOpt在多数任务上匹配或超越PPO和GRPO。例如，在Qwen2.5-3B-Instruct上，RandOpt达到86.7%的GSM8K准确率，高于GRPO的82.0%。值得注意的是，RandOpt的性能增益部分源于格式修正（Format Thicket）和推理能力提升（Reasoning Thicket），这与GRPO类似。消融实验显示，集成大小K对性能有显著影响，K=50时性能最佳。此外，RandOpt在视觉语言模型（VLM）上同样有效，在GQA数据集上提升12.4%准确率。

评估边界方面，本文未报告70B以上超大模型的实验结果，且未对比DPO等偏好优化方法。可复现性方面，代码已开源，但超参数（如噪声尺度 $\sigma$）的敏感性分析有限。

## 关联研究分析

从方法设计看，RandOpt与进化策略（ES）最为接近，但ES通常采用顺序变异与选择，而RandOpt完全并行化，且引入Top-K集成以利用解的多样性。与测试时计算（Test-Time Compute）方法如Best-of-N相比，RandOpt在权重空间而非输出空间进行采样，理论上能探索更广泛的模型变体。然而，RandOpt的推理成本随K线性增加，这与Best-of-N类似，但RandOpt通过蒸馏（Distillation）可降低推理成本，这一思路在论文中仅作为概念验证。

从问题动机看，本文挑战了RLHF和SFT作为后训练唯一有效路径的共识。传统观点认为RL提供探索能力，SFT提供模仿先验，两者互补。但RandOpt表明，在“灌木丛”区域，随机采样即可替代RL的探索功能，且无需奖励模型。这一发现暗示，预训练本身已隐式完成了部分“元学习”（Meta-Learning）任务，使得权重邻域内存在大量可快速适配的解。然而，这一结论是否适用于所有任务类型，特别是需要复杂逻辑推理的任务，仍需进一步验证。

## 总结

本文揭示了大规模预训练模型权重邻域内解密度与多样性的“灌木丛”现象，并提出RandOpt算法，通过并行随机采样与集成实现无梯度后训练。实验表明，在0.5B–8B模型上，RandOpt在同等FLOPs下匹配或超越PPO和GRPO，如在Qwen2.5-3B上GSM8K准确率达86.7%。其核心价值在于挑战了后训练必须依赖迭代优化的传统范式，揭示了预训练对损失景观几何结构的重塑作用。然而，本文未验证70B以上超大模型的有效性，且推理成本随集成大小K线性增加，限制了其实际应用。当模型规模进一步扩大时，“灌木丛”密度是否持续增加，以及随机采样是否仍能高效发现高性能解，是亟待验证的关键问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12228)