# ICLR2026最新论文 ｜Training Large Reasoning Models Efficiently via Progressive Thought Encoding ｜渐进思维编码

研究机构：美国罗切斯特大学、微软研究院

作者：Zeliang Zhang、Xiaodong Liu、Hao Cheng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16839)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16839)

> 大推理模型（Large Reasoning Models, LRMs）在强化学习（Reinforcement Learning, RL）后训练中面临长思维链（Chain-of-Thought, CoT）导致的显存瓶颈，传统滑动窗口缓存虽能限制内存但会切断长程依赖，导致推理能力退化。本文切入点在于将被驱逐的Token信息动态编码进轻量级LoRA适配器，以参数更新替代上下文丢弃。该方法在严格内存预算下实现了训练与推理的双重效率提升，但其对复杂逻辑链条的保真度及跨任务泛化能力仍存疑。

## 研究背景

大推理模型（LRMs）依赖长思维链（CoT）解决复杂数学与代码任务，其核心机制是思维链（Chain-of-Thought, CoT）将多步推理显式化。然而，RL后训练中的结果奖励（Outcome-based Reward）具有稀疏性，仅在序列末尾提供信号，迫使模型生成极长的轨迹以最大化通过概率。这种长轨迹在自回归解码阶段导致键值（Key-Value, KV）缓存无限增长，成为训练与部署的主要内存瓶颈。为缓解此问题，滑动窗口（Sliding Window）策略被引入以限制缓存大小，但直接丢弃早期Token会破坏模型对长程上下文的整合能力，导致推理准确率显著下降。

当前领域共识认为，推理效率优化主要聚焦于Token数量压缩或潜空间表征重构，如LEASH通过奖励整形抑制冗余步骤，Coconut将推理转移至连续潜在空间。然而，这些方法多关注计算量或Token带宽，未直接解决RL训练过程中因长Rollout导致的显存峰值问题。现有方案在“保持长程依赖”与“限制内存占用”之间存在根本矛盾：直接截断损失信息，全缓存则内存溢出。本文切入点在于将内存约束内化为训练策略，通过参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）动态补偿被驱逐上下文的信息损失，从而在固定内存预算下维持推理完整性。

## 核心方法

### 方法参照系

标准RL训练流程中，模型在Rollout阶段生成完整CoT序列，KV缓存随序列长度线性增长。本文问题与该通用流程的关键差异在于：引入滑动窗口驱逐策略，要求模型在缓存饱和时丢弃早期Token，同时通过在线参数更新保持对丢弃信息的“记忆”，实现固定内存下的长程推理。

### 驱逐Token的动态编码机制

传统滑动窗口策略在缓存饱和时直接丢弃早期Token，导致模型无法访问长程上下文，进而削弱多步推理的连贯性。本文创新在于引入全局查询向量 $q_g$ 与上下文状态 $S_e$，将被驱逐Token的信息压缩并注入LoRA权重。具体而言，当缓存填满时，被驱逐的Key $K_e$ 与Value $V_e$ 通过投影矩阵映射至潜在空间，与全局查询 $q_g$ 交互生成上下文状态 $S_e$：

$$ S_e = \text{Normalize}(S_e + W_Q^a q_g (W_K^a K_e)^\top W_V^a V_e) $$

该公式的物理含义是：$q_g$ 作为可学习的摘要载体，聚合所有被驱逐Token的信息，$S_e$ 则累积这些信息的压缩表示。随后，$S_e$ 通过LoRA权重矩阵 $A, B$ 更新模型参数 $\Delta W$，使模型在后续解码中“记住”被驱逐的上下文。这一设计解决了直接丢弃Token导致的长程依赖断裂问题，使模型在固定缓存大小下仍能近似全缓存策略的推理能力。

### 缓存感知GRPO目标函数

标准GRPO（Grouped Reinforcement Policy Optimization）假设轨迹在完整缓存下生成，而本文需适应部分缓存策略 $D$。本文创新在于重新定义Rollout分布，将缓存驱逐策略 $D$ 纳入策略优化目标。缓存感知GRPO目标函数为：

$$ \mathcal{J}(\theta_g) = \mathbb{E}_{p \sim \mathcal{D}, y \sim \pi_{\theta_g}^{[D]}(\cdot|p)} \left[ r(y) - \beta D_{KL}(\pi_{\theta_g}^{[D]}(\cdot|p) \| \pi_{\theta_{ref}}(\cdot|p)) \right] $$

其中 $\pi_{\theta_g}^{[D]}$ 表示在驱逐策略 $D$ 下生成的策略，$\pi_{\theta_{ref}}$ 为全缓存参考策略。该公式的物理含义是：优化目标不再仅是最大化奖励，而是使部分缓存策略 $\pi_{\theta_g}^{[D]}$ 逼近全缓存策略 $\pi_{\theta_{ref}}$ 的行为分布。这一设计解决了标准GRPO在内存受限场景下失效的问题，确保模型在训练阶段即学会在有限缓存下保持推理一致性，而非仅在推理时被动适应。

## 实验评估

实验在Qwen2.5-3B/7B-Instruct与DeepSeek-R1-Distill-Llama-8B三个模型上，针对Math500、OlympiadBench、Minerva Math、AMC、AIME2024/2025六个基准进行评估。基线覆盖原始模型（Baseline）、全缓存LoRA、滑动窗口LoRA（LoRA_c），但缺失LEASH、Coconut等主流效率优化方法，限制了横向对比的完整性。

| 模型 | 方法 | Avg. Accuracy (%) | Peak GPU Mem. (%) | Max TFLOPs |
| :--- | :--- | :--- | :--- | :--- |
| Qwen2.5-3B-Instruct | LoRA | 28.2 | 82.8 | 4.2 |
| Qwen2.5-3B-Instruct | LoRA_c | 25.6 | 38.0 | 2.6 |
| Qwen2.5-3B-Instruct | Ours | 30.1 | 45.3 | 2.7 |
| Qwen2.5-7B-Instruct | LoRA | 38.1 | 85.8 | 5.7 |
| Qwen2.5-7B-Instruct | LoRA_c | 36.7 | 63.1 | 3.5 |
| Qwen2.5-7B-Instruct | Ours | 39.6 | 67.2 | 3.6 |
| DeepSeek-R1-Distill-Llama-8B | LoRA | 34.9 | 88.7 | 7.4 |
| DeepSeek-R1-Distill-Llama-8B | LoRA_c | 35.1 | 59.1 | 4.6 |
| DeepSeek-R1-Distill-Llama-8B | Ours | 45.6 | 59.8 | 4.6 |

在DeepSeek-R1-Distill-Llama-8B上，本文方法平均准确率45.6%，较LoRA提升10.7个百分点，峰值显存59.8%较LoRA的88.7%降低28.9个百分点，表明参数更新有效补偿了缓存驱逐的信息损失。

消融实验显示，全局Token数量对性能影响显著：#Global-32在768缓存长度下优于#Global-64，表明过多全局Token可能引入噪声。Token丢弃策略对比中，HeadKV在768缓存下准确率达50.7%，较滑动窗口的48.4%提升2.3个百分点，但训练时间增加37%，故本文保留滑动窗口以平衡效率。

评估边界方面，实验仅覆盖数学推理任务，未验证代码或常识推理场景；AIME采用pass@16指标，与其他基准的pass@1协议不一致，可能高估长轨迹优势；论文未提供代码仓库，超参数如LoRA秩固定为32，未探索不同秩对性能的影响，可复现性受限。

## 关联研究分析

从问题动机看，LEASH（Li et al., 2025）通过奖励整形抑制过度思考，优化Token数量，而本文聚焦内存约束，优化KV缓存占用。两者均基于RLVR框架，但LEASH假设全缓存可用，本文则针对内存受限场景。差异根源在于任务特性：LEASH适用于计算资源充足但需降低延迟的场景，本文适用于显存受限的部署环境。本文未探索LEASH的奖励整形机制是否可迁移至内存受限场景，若结合两者，可能在降低Token数的同时进一步压缩显存，但论文未给出回答。

从方法设计看，Coconut（Shan et al., 2025）将推理转移至连续潜在空间，实现全潜空间推理，而本文仅压缩被驱逐Token，保留显式文本生成。Coconut牺牲可解释性换取延迟降低，本文则通过LoRA更新保持文本可解释性。差异根源在于架构选择：Coconut需重构模型架构，本文兼容现有Transformer。本文未验证潜空间推理在内存受限下的表现，若Coconut的连续状态能更紧凑地表示长程依赖，其显存效率可能优于本文的LoRA编码，但论文未提供对比实验。

## 总结

本文核心矛盾是RL训练中长CoT导致的显存瓶颈与滑动窗口缓存导致的推理退化。现有方法如LEASH优化Token数，Coconut重构推理空间，均未直接解决内存约束下的长程依赖保持问题。本文通过将被驱逐Token信息编码进LoRA权重，在固定缓存下实现参数动态更新，证明了在DeepSeek-R1-Distill-Llama-8B上平均准确率45.6%、峰值显存59.8%的可行性。其边界在于仅验证数学任务，且依赖滑动窗口策略，未探索更复杂的驱逐机制。当缓存窗口进一步缩小至512 Token时，LoRA编码的信息压缩是否仍能有效维持多步推理的连贯性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16839)