# ICLR2026最新论文 ｜FlowRL: Matching Reward Distributions for LLM Reasoning ｜奖励分布匹配策略优化

研究机构：上海交通大学、微软研究院

作者：Xuekai Zhu、Daixuan Cheng、Dinghuai Zhang 等 23 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15207)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15207)

> 现有强化学习后训练范式聚焦于最大化期望奖励，导致策略收敛至单一主导解法模式，抑制了推理路径的多样性与泛化能力。本文指出，这种模式坍缩源于对奖励分布中低频有效模式的忽略，而非单纯的探索不足。FlowRL 通过引入可学习配分函数将标量奖励转化为目标分布，并最小化策略与该分布间的反向 KL 散度，实现了从“奖励最大化”到“奖励分布匹配”的范式转移。该方法在数学与代码推理任务上显著优于 PPO 和 GRPO，但其绝对性能低于当前领域 SOTA，且未验证细粒度信用分配下的有效性。

## 研究背景

当大语言模型在长思维链（Chain-of-Thought, CoT）任务中进行强化学习时，策略往往倾向于重复使用高概率的解题路径，导致生成结果高度同质化。这一现象被称为模式坍缩，其根源在于传统算法如近端策略优化（Proximal Policy Optimization, PPO）和组相对策略优化（Group Relative Policy Optimization, GRPO）仅优化期望奖励，忽略了奖励分布中其他有效但低频的模式。为理解本文方法，需掌握生成流网络（Generative Flow Networks, GFlowNets）的核心机制：通过平衡前向与反向概率流，使采样概率与奖励成正比，从而自然覆盖多模态解空间。

主流后训练算法如 GRPO 通过消除 Critic 网络降低了计算开销，但其序列级优势估计仍受限于奖励最大化目标，导致策略分布熵值急剧下降，模型陷入局部最优。尽管 DAPO 等后续工作通过解耦裁剪和动态采样缓解了部分训练不稳定问题，但未能从根本上解决模式覆盖不足导致的泛化瓶颈。本文切入点在于，将策略优化目标从最大化期望奖励转变为匹配完整的奖励分布，利用 GFlowNets 的轨迹平衡机制作为理论桥梁，实现多模态解法的系统性探索。

## 核心方法

### 方法参照系

标准 RLVR 流程中，策略通过最大化裁剪后的策略梯度更新，优势函数由组内奖励标准化得出。本文问题与该通用流程的关键差异在于：不再将奖励视为标量信号进行最大化，而是将其视为分布源，通过配分函数归一化后作为策略匹配的目标。

### 分布匹配目标构建

设计动机在于解决奖励最大化导致的低频模式忽略问题。传统方法中，优势函数 $A_i = \frac{r_i - \text{mean}(\mathbf{r})}{\text{std}(\mathbf{r})}$ 仅反映相对优劣，无法引导策略覆盖所有有效解法。FlowRL 引入可学习配分函数 $Z_\phi(\mathbf{x})$，将标量奖励 $r(\mathbf{x}, \mathbf{y})$ 转化为目标分布 $\tilde{\pi}(\mathbf{y}|\mathbf{x}) = \frac{\exp(\beta r(\mathbf{x}, \mathbf{y}))}{Z_\phi(\mathbf{x})}$。策略优化目标变为最小化反向 KL 散度：

$$
\mathcal{L}_{KL} = \mathbb{E}_{\mathbf{y} \sim \pi_\theta} \left[ \log \pi_\theta(\mathbf{y}|\mathbf{x}) - \log \tilde{\pi}(\mathbf{y}|\mathbf{x}) \right]
$$

该公式的物理含义是：策略 $\pi_\theta$ 的采样概率应与奖励诱导的分布 $\tilde{\pi}$ 成比例，从而在优化高奖励路径的同时，保留对低奖励但有效路径的探索能力。

### 轨迹平衡与长序列适配

设计动机在于解决长 CoT 训练中的梯度爆炸与采样不匹配问题。直接优化 KL 目标在 8K token 序列上会导致梯度范数随序列长度线性增长。FlowRL 基于命题 1，将 KL 最小化等价于 GFlowNets 的轨迹平衡损失，并引入两项关键修正。首先，长度归一化将 $\log \pi_\theta(\mathbf{y}|\mathbf{x})$ 重写为 $\frac{1}{|\mathbf{y}|} \sum_{t=1}^{|\mathbf{y}|} \log \pi_\theta(y_t|y_{<t}, \mathbf{x})$，平衡长短序列的贡献。其次，重要性采样修正离策略数据偏差，定义裁剪权重 $w = \text{clip}\left(\frac{\pi_\theta(\mathbf{y}|\mathbf{x})}{\pi_{\text{old}}(\mathbf{y}|\mathbf{x})}, 1-\epsilon, 1+\epsilon\right)$，并 detach 当前策略梯度以防止过度漂移。最终目标为：

$$
\mathcal{L}_{\text{FlowRL}} = \mathbb{E}_{\mathbf{y} \sim \pi_{\text{old}}} \left[ w \cdot \left( \frac{1}{|\mathbf{y}|} \log \pi_\theta(\mathbf{y}|\mathbf{x}) - \log Z_\phi(\mathbf{x}) + \beta \hat{r}(\mathbf{x}, \mathbf{y}) \right)^2 \right]
$$

该公式通过平方损失形式稳定优化过程，同时利用参考模型 $\pi_{\text{ref}}$ 约束奖励分布，确保探索不偏离预训练语义空间。

## 实验评估

实验在数学与代码领域进行，数学任务使用 Qwen2.5-7B/32B 基座，代码任务使用 DeepSeek-R1-Distill-Qwen-7B，评估协议为 Avg@16。基线覆盖 REINFORCE++、PPO 和 GRPO，但缺失 DAPO、SSVPO 等 2025-2026 年 SOTA 方法，构成性能参照缺口。

| 模型 | AIME24 | AIME25 | AMC23 | MATH500 | Minerva | Olympiad | Avg |
|---|---|---|---|---|---|---|---|
| Qwen2.5-32B-Base GRPO | 28.59 | 21.37 | 52.48 | 76.40 | 28.79 | 37.90 | 43.25 |
| Qwen2.5-32B-Base FlowRL | 23.95 | 21.87 | 73.75 | 80.75 | 38.21 | 51.83 | 48.39 |
| Qwen2.5-7B-Base GRPO | 30.78 | 24.03 | 54.47 | 64.53 | 23.06 | 26.88 | 31.98 |
| Qwen2.5-7B-Base FlowRL | 15.41 | 10.83 | 54.53 | 66.96 | 31.41 | 34.61 | 35.63 |

FlowRL 在 32B 模型上平均准确率 48.39%，较 GRPO 的 43.25% 提升 5.14 个点；在 7B 模型上提升 3.65 个点。代码任务中，FlowRL 在 LiveCodeBench 达 37.43%，CodeForces 评分 1549.47，均优于所有基线。

消融实验显示，移除重要性采样（IS）导致 7B 模型平均准确率从 35.63% 降至 26.71%，降幅达 8.92 个点，表明离策略修正在长序列训练中至关重要。长度归一化虽未单独消融，但论文指出其解决了 8K token 序列的梯度爆炸问题，是训练稳定性的前提。

评估协议采用 Avg@16 而非领域主流的 Pass@1，且未报告置信区间，限制了与 SSVPO（AIME24 80.0%）等 SOTA 的直接比较。代码开源情况未明确，但基于 veRL 框架实现，超参数 $\beta=15$、学习率 1e-6 已披露，可复现性中等。

## 关联研究分析

从问题动机看，FlowRL 与 UCAS 均针对熵坍缩，但机制截然不同。UCAS 通过不确定性感知优势整形在响应级和 Token 级重塑学习信号，属于被动适应策略，旨在维持策略分布的熵值；FlowRL 则通过分布匹配主动覆盖奖励分布的所有模式，属于主动干预策略。UCAS 的局限在于其依赖熵信号作为代理指标，可能无法区分“高熵但无效”与“高熵且有效”的路径；FlowRL 的局限在于其配分函数 $Z_\phi$ 的输入仅为问题嵌入，未考虑推理过程中的中间状态，可能无法捕捉步骤级的模式差异。

从方法设计看，FlowRL 与 SSVPO 在信用分配粒度上存在根本分歧。SSVPO 通过步骤级信用分配将最终奖励分解至每个推理步骤，解决序列级奖励稀疏导致的中间步骤贡献不均问题；FlowRL 则完全放弃细粒度分配，仅做序列级分布匹配。SSVPO 在 AIME25 达 82.0% 的 Pass@1，远高于 FlowRL 的 21.87% Avg@16，但两者协议不同且骨干不同，无法直接比较。FlowRL 未验证细粒度信用分配下的有效性，其分布匹配机制在长推理链中是否仍能保持步骤级信号的精准度，论文未给出回答。

## 总结

FlowRL 要解决的核心矛盾是奖励最大化导致的模式坍缩与泛化能力受限。其切入点在于，现有方法仅优化期望奖励，忽略了奖励分布中低频有效模式，而 GFlowNets 的轨迹平衡机制提供了匹配完整分布的理论工具。FlowRL 通过引入可学习配分函数和长度归一化，实现了从奖励最大化到分布匹配的范式转移，在 32B 模型上较 GRPO 提升 5.14 个点的平均准确率。其边界在于，实验未覆盖 DAPO 等 SOTA 基线，且未验证细粒度信用分配下的有效性。当推理链长度超过 8K token 时，长度归一化是否仍能有效抑制梯度爆炸，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15207)