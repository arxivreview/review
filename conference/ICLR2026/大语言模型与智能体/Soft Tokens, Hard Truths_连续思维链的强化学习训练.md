# ICLR2026最新论文 ｜Soft Tokens, Hard Truths ｜连续思维链的强化学习训练

研究机构：荷兰阿姆斯特丹大学、美国纽约大学

作者：Natasha Butt、Ariel Kwiatkowski、Ismail Labiad 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.19170)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.19170)

> 连续思维链（Continuous Chain-of-Thought, C-CoT）旨在突破离散Token自回归解码的表达瓶颈，但现有方法受限于推理时干预或依赖Ground-truth蒸馏，无法进行可扩展的强化学习（Reinforcement Learning, RL）训练。本文切入点在于通过向概率加权嵌入注入高斯噪声，为连续空间提供RL所需的探索信号，从而无需参考离散轨迹即可微调模型。该方法在Pass@1上与离散CoT持平，在Pass@32上显著超越，验证了连续表示在多样性上的优势，但其对基础模型分布外性能的保留机制仍存疑。

## 研究背景

思维链推理通过生成中间步骤提升大语言模型在复杂任务上的表现，但自回归机制强制模型逐Token解码，导致计算复杂度随链长线性增长，且离散符号难以并行表达抽象概念。这种离散性限制了模型探索多样化推理路径的能力，与人类认知中基于流体概念的抽象推理形成鲜明对比。

为突破这一局限，研究界转向连续潜在空间推理。Coconut（Hao et al., 2024）通过蒸馏Ground-truth CoT实现连续推理，但受限于反向传播通过时间（Backpropagation Through Time, BPTT）的计算开销，仅支持6步连续Token；Soft Thinking（Zhang et al., 2025）提出在推理时使用概率加权嵌入混合，但Wu et al. (2025)指出其常退化为贪心解码，且缺乏训练机制。现有方案要么局限于推理时技巧，要么依赖昂贵的蒸馏过程，导致连续推理模型难以通过RL进行大规模后训练，制约了其在复杂数学任务上的泛化能力。

## 核心方法

### 连续CoT训练参照系

标准离散CoT训练通过采样离散Token并计算对数似然进行优化。本文问题与该通用流程的关键差异在于：连续Token是概率分布的线性组合，缺乏离散采样的随机性，导致标准Reinforce算法无法直接应用，且BPTT计算成本随链长指数增长。

### 噪声注入的连续Token生成

在Soft Thinking框架中，CoT阶段的输入嵌入 $h_t^{[0]}$ 由前一步概率向量 $p_{t-1}$ 与嵌入矩阵 $E$ 的乘积决定：

$$ h_t^{[0]} = p_{t-1} E $$

该设计保留了完整的分布信息，但导致CoT生成过程成为提示的确定性函数，无法进行RL探索。本文在输入嵌入层注入高斯噪声 $\epsilon_t \sim \mathcal{N}(0, I\sigma)$，得到带噪嵌入：

$$ \tilde{h}_t^{[0]} = h_t^{[0]} + \epsilon_t $$

这一改动解决了连续空间缺乏随机性的问题，使得模型能够通过噪声探索不同的推理路径，从而适配RL训练。噪声标准差 $\sigma$ 设为Token嵌入均方根范数的0.33倍，确保噪声幅度与嵌入相当但略小，避免破坏语义结构。

### 基于RLOO的连续CoT强化学习

引入噪声后，连续CoT的采样过程由噪声分布定义，可应用Reinforce类算法。本文采用RLOO（Reinforce with Leave-One-Out）基线优化，目标是最小化以下损失：

$$ \mathcal{L} = -\mathbb{E}_{\tilde{h}^{[0]}, a} \left[ R(a) \left( \log \pi(a|\tilde{h}^{[0]}) + \sum_{t=1}^T \log \pi(\tilde{h}_t^{[0]} | \tilde{h}_{<t}^{[0]}) \right) \right] $$

其中 $\log \pi(\tilde{h}_t^{[0]} | \tilde{h}_{<t}^{[0]})$ 可通过高斯分布的对数似然计算，因为 $\tilde{h}_t^{[0]}$ 是前序连续Token的可微函数。该设计避免了BPTT的计算瓶颈，仅需存储概率向量并注入噪声，计算开销与离散CoT相当，实现了可扩展的连续CoT训练。

## 实验评估

实验在Llama-3.2-3B-Instruct、Llama-3.1-8B-Instruct和Qwen-2.5-3B-Instruct上，使用GSM8K、MATH和DeepScaleR数据集进行训练，并在多个数学及分布外基准上评估。基线覆盖离散Hard Token CoT，但缺失与UCoT、SLAT等显式压缩方法的直接对比，限制了跨路线的性能比较。

| 模型 | 训练集 | 推理方式 | Pass@1 (%) | Pass@32 (%) |
|---|---|---|---|---|
| Llama 3B Instruct | GSM8K | Hard Sample | 75.9±1.3 | 94.1±0.3 |
| Llama 3B Instruct | GSM8K | Soft Sample | 77.2±0.9 | 97.9±0.3 |
| Llama 3B Instruct | MATH | Hard Sample | 80.0±0.5 | 97.6±0.3 |
| Llama 3B Instruct | MATH | Soft Sample | 79.6±1.4 | 97.8±0.3 |
| Llama 8B Instruct | GSM8K | Fuzzy Sample | 83.7±1.3 | 98.2±0.2 |
| Llama 8B Instruct | GSM8K | Soft Sample | 82.6±1.6 | 98.3±0.2 |

在GSM8K上，Llama-3B Soft Token Pass@1为77.2%，高于Hard Token的75.9%；Pass@32从94.1%提升至97.9%，表明连续训练增强了推理多样性。在MATH上，Soft Token Pass@1与Hard Token持平（79.6% vs 80.0%），但Pass@32略高（97.8% vs 97.6%）。Llama-8B在GSM8K上，Fuzzy Token Pass@1达到83.7%，Soft Token为82.6%，均显著高于Hard Token的81.2%，且Pass@32均超过98%。

消融实验显示，噪声强度 $\sigma$ 对性能影响较小，算法在 $\sigma \leq 1.0$ 倍均方根范数范围内鲁棒。温度 $\tau$ 在 $[0.0001, 0.1]$ 范围内均有效，其中Fuzzy Token（$\tau=0.0001$）在Llama-8B上表现最佳，Soft Token（$\tau=0.5$）在Llama-3B上表现最佳，表明不同模型规模对温度敏感度不同。

评估边界方面，论文未报告计算效率指标（如延迟、显存占用），且未提供代码开源链接，可复现性受限。评估协议仅关注数学任务，未覆盖代码生成（HumanEval）或抽象推理（ARC-AGI）等非数学领域，限制了泛化能力的验证。

## 关联研究分析

从问题动机看，本文与Coconut（Hao et al., 2024）的核心差异在于训练范式。Coconut依赖Ground-truth CoT蒸馏，通过BPTT优化连续Token，导致链长受限且计算成本高；本文通过噪声注入实现无监督RL训练，摆脱了对参考轨迹的依赖，支持数百Token的连续CoT。这一差异源于对“连续推理如何学习”的不同理解：Coconut视连续Token为离散轨迹的压缩表示，本文视其为独立的探索空间。

从方法设计看，本文与Soft Thinking（Zhang et al., 2025）的关键区别在于噪声的作用。Soft Thinking在推理时使用概率混合，但Wu et al. (2025)指出其常退化为贪心解码，缺乏训练机制；本文在训练时注入噪声，为RL提供探索信号，并在推理时切换为离散Token。这一设计解决了Soft Thinking“推理时有效但训练时失效”的问题，但论文未探讨噪声强度 $\sigma$ 与RL探索效率的理论关系，也未验证连续Token在代码生成等非数学任务上的泛化能力。

## 总结

本文要解决的核心矛盾是连续CoT训练缺乏探索信号与计算效率的平衡。现有方法如Coconut依赖蒸馏且链长受限，Soft Thinking仅适用于推理时，均无法进行可扩展的RL训练。本文通过向概率加权嵌入注入高斯噪声，为连续空间提供RL探索信号，实现了无需Ground-truth CoT的可扩展训练。实验证明，该方法在GSM8K和MATH上Pass@1与离散CoT持平，Pass@32显著超越（如Llama-3B GSM8K Pass@32从94.1%提升至97.9%），验证了连续表示在多样性上的优势。本文的边界在于仅验证了数学任务，且未报告计算效率指标，噪声强度 $\sigma$ 的最优值依赖模型规模（Llama-3B偏好Soft Token，Llama-8B偏好Fuzzy Token），这一现象的内在机制尚未阐明。当模型规模进一步扩大时，噪声强度 $\sigma$ 与温度 $\tau$ 的最优组合是否遵循可预测的规律，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.19170)