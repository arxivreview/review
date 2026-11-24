# ICLR2026最新论文 ｜REVOLUTIONIZING REINFORCEMENT LEARNING FRAMEWORK FOR DIFFUSION LARGE LANGUAGE MODELS ｜轨迹感知强化学习框架

研究机构：美国普林斯顿大学、美国芝加哥大学

作者：Yinjie Wang、Ling Yang、Bowen Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_42745241)

> 扩散语言模型（Diffusion Language Models, DLMs）在并行解码中面临训练目标与推理轨迹的结构性错位，导致强化学习（Reinforcement Learning, RL）对齐效率低下。现有方法多采用随机掩码优化，忽略了语言生成的顺序逻辑性，造成策略梯度估计偏差。本文提出TraceRL，通过聚合推理轨迹并引入扩散价值模型，实现全注意力与块注意力架构的统一RL优化。该方法在数学与代码推理任务上显著提升了模型性能，但其对长序列误差累积的抑制机制尚需进一步理论验证。

## 研究背景

扩散语言模型通过迭代去噪并行生成文本，其核心优势在于利用双向上下文进行全局推理。然而，自然语言具有严格的顺序依赖逻辑，而标准掩码扩散训练目标假设噪声分布是随机的，这导致模型在推理时采用的置信度解码策略与训练时的随机掩码分布产生系统性偏差。这种训练-推理不一致性使得基于随机掩码的RL优化难以有效捕捉中间步骤的信用分配，限制了模型在复杂推理任务上的表现。

早期DLM的RL方法如MMaDA（Yang et al., 2025b）和Gong et al. (2025)主要聚焦于全注意力架构，通过随机掩码或互补掩码减少方差，但未能解决轨迹对齐问题。块注意力扩散模型（Block Diffusion）虽支持KV缓存复用，但缺乏统一的RL框架。本文切入点在于揭示推理轨迹与训练目标的错位，并提出一种轨迹感知机制，将RL优化目标与模型实际生成的解码路径对齐，从而在保持并行解码效率的同时提升推理能力。

## 核心方法

### 方法参照系

标准DLM的RL训练基于PPO框架，使用随机掩码目标 $J_{full}$ 优化策略。本文的关键差异在于：不再对随机噪声状态进行优化，而是对模型实际生成的推理轨迹 $\tau$ 进行轨迹感知优化，并引入价值模型处理多步决策的信用分配。

### 轨迹感知策略优化

传统方法在每一步独立优化随机掩码状态，忽略了token解码的顺序逻辑。TraceRL将生成的响应表示为轨迹 $\tau = \tau^{(1)} \cup \dots \cup \tau^{(|\tau|)}$，其中 $\tau^{(t)}$ 为第 $t$ 步解码的token集合。为降低计算复杂度，引入收缩参数 $s$ 聚合连续步骤，定义压缩轨迹 $\tau_i^{[s]}$。策略优化目标为：

$$ J_{policy}(\theta_p) = \mathbb{E}_{\tau \sim \pi_{old}} \left[ \frac{1}{|\tau_i^{[s]}|} \sum_{t=1}^{|\tau_i^{[s]}|} \min \left( r_t A_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon) A_t \right) - \beta D_{KL}(\pi_\theta || \pi_{old}) \right] $$

该公式通过聚合步骤减少前向传播次数，同时保留轨迹中的顺序信息，解决了随机掩码导致的训练-推理偏差。

### 扩散价值模型与信用分配

为解决多步去噪中终端奖励难以分配至中间步骤的问题，本文引入基于扩散的价值模型。对于轨迹 $\tau$，价值网络 $V_{\theta_v}$ 预测每个token的价值 $V_j$，并计算步级价值 $V_t^\star = \frac{1}{|\tau^{(t)}|} \sum_{j \in \tau^{(t)}} V_j$。优势函数通过广义优势估计（GAE）计算：

$$ A_t^\star = \delta_t^\star + \gamma \lambda A_{t+1}^\star, \quad \delta_t^\star = r_t^\star - V_t^\star + \gamma V_{t+1}^\star $$

该机制将终端奖励分解至中间步骤，提供了方差减少的基线，显著提升了训练稳定性。价值模型还自然兼容过程奖励，通过中间步骤的细粒度监督增强推理能力。

## 实验评估

实验在MATH500、GSM8K、LiveCodeBench-V2等基准上进行，基线包括LLaDA、Dream、SDAR及AR模型（Qwen2.5、Llama3.1）。TraceRL在数学推理任务上表现突出，TraDo-4B-Instruct在MATH500上达到75.6%，超越Qwen2.5-7B-Instruct的74.0%；TraDo-8B-Instruct在LiveCodeBench-V2上达到25.9%，领先Llama3.1-8B-Instruct的20.0%。

| 模型 | MATH500 | GSM8K | LiveCodeBench-V2 |
| :--- | :--- | :--- | :--- |
| Qwen2.5-7B-Instruct | 74.0 | 89.9 | 26.9 |
| Llama3.1-8B-Instruct | 51.9 | 84.5 | 20.0 |
| SDAR-4B-Chat | 70.2 | 90.2 | 15.6 |
| TraDo-4B-Instruct | 75.6 | 91.2 | 18.7 |
| TraDo-8B-Instruct | 78.5 | 92.3 | 25.9 |

消融实验显示，收缩参数 $s$ 对性能影响显著：$s=1$ 时MBPP准确率为33.2%，$s=2$ 时提升至37.0%，但 $s=4$ 时降至35.6%，表明过大的聚合会损失轨迹细节。价值模型将奖励方差从 $6.6 \times 10^{-4}$ 降至 $3.6 \times 10^{-4}$，降幅约45.5%，验证了其稳定性贡献。

评估边界方面，论文未报告置信区间，且部分基线（如SPG、DISPO）未直接对比。代码已开源，但长CoT模型TraDo-8B-Thinking的SFT数据规模（75K）可能影响结果可复现性。

## 关联研究分析

从问题动机看，TraceRL与SPG（Wang et al., 2025）均解决DLM的RL优化难题，但SPG聚焦于掩码感知策略梯度，而TraceRL强调轨迹对齐。SPG在Sudoku上达到62.9%，但TraceRL在MATH500上表现更优，这可能源于轨迹感知对长序列推理的适应性。从方法设计看，TraceRL与Gong et al. (2025)的互补掩码策略不同，后者通过数据增强减少方差，而TraceRL通过价值模型实现细粒度信用分配。这种差异反映了任务特性：数学推理需要中间步骤的精确监督，而代码生成更依赖整体结构一致性。

## 总结

TraceRL解决了DLM中训练目标与推理轨迹的错位问题，通过轨迹感知优化与扩散价值模型，实现了全/块注意力架构的统一RL框架。实验证明其在数学与代码推理上超越同级AR模型，如TraDo-4B-Instruct在MATH500上比Qwen2.5-7B-Instruct高1.6%。然而，收缩参数 $s$ 的最优值依赖于任务复杂度，且长CoT模型的SFT数据规模可能引入偏差。当序列长度超过1024时，轨迹聚合的误差累积是否会被价值模型有效抑制，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_42745241)