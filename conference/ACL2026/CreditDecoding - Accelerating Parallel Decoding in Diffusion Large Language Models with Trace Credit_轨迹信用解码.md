# ACL2026最新论文 ｜CreditDecoding: Accelerating Parallel Decoding in Diffusion Large Language Models with Trace Credit ｜轨迹信用解码

研究机构：上海交通大学、西湖大学

作者：Kangyu Wang、Zhiyun Jiang、Haibo Feng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06133)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06133)

> 扩散语言模型（dLLMs）在并行解码中面临“计算冗余”与“历史无关”的双重瓶颈，导致正确令牌因瞬时置信度不足被反复重掩码。现有阈值解码策略仅依赖当前步Logits，忽略了去噪过程中置信度的时间一致性，造成大量无效迭代。本文提出CreditDecoding，通过累积历史Logits构建轨迹信用（Trace Credit）作为先验，融合至当前Logits以提升置信度。该方法免训练，在LLaDA-8B-Instruct上实现5.48倍加速并提升0.48分准确率，但其在长上下文下的稳定性及与KV缓存优化的协同效应仍需进一步验证。

## 研究背景

扩散语言模型（dLLMs）通过迭代去噪和双向注意力打破自回归模型的左到右顺序依赖，支持任意顺序的并行令牌更新。然而，这种并行性引入了新的效率瓶颈：由于缺乏无损KV缓存，模型需在多步去噪中反复预测所有掩码位置。标准并行解码策略在每个去噪步仅解码置信度超过阈值 $\tau$ 的令牌，其余位置重新掩码以待后续步骤。这一机制导致两个关键问题：一是“计算冗余”，即正确令牌往往在早期步骤已被预测，但因瞬时置信度波动未达阈值而被反复重掩码；二是“历史无关解码”，即当前步的解码决策完全独立于历史预测，无法利用令牌置信度随去噪进程单调递增的时间一致性特征，导致错误累积与收敛缓慢。

现有加速方案如Fast-dLLM主要聚焦于块级并行与置信度阈值优化，但未解决瞬时置信度滞后于真实预测能力的问题。本文切入点在于发现去噪轨迹中存在的“时间一致性”：目标令牌的置信度在接近解码时快速趋近1，且该趋势对去噪总步长不敏感。基于此，本文提出利用历史Logits累积构建“轨迹信用”，将其作为先验条件融合至当前Logits，从而在保持免训练特性的前提下，提前触发正确令牌的解码，同时抑制错误令牌的置信度尖峰。

## 核心方法

### 标准并行解码参照系

标准dLLM并行解码流程为：在去噪步 $t$，模型预测所有掩码位置 $i \in M_t$ 的令牌分布 $p_\theta(\cdot|x_t)$，选取置信度 $s_i^t = \max_v p_\theta(v|x_t) \ge \tau$ 的令牌并行解码，其余位置重掩码。该流程的核心局限在于 $s_i^t$ 仅反映当前步的瞬时状态，忽略了历史步中该令牌已多次被正确预测的证据，导致解码边界（Decoding Boundary）滞后于实际预测能力。

### 轨迹信用累积机制

为克服瞬时置信度的不稳定性，本文引入轨迹信用 $C_{t}^{[i,v]}$，通过指数移动平均（EMA）规则累积历史Logits证据。对于每个掩码位置 $i$ 和令牌 $v$，信用更新公式为：

$$ C_{t}^{[i,v]} = \beta C_{t-1}^{[i,v]} + (1-\beta) \gamma (s_i^{t-1})^{\gamma} \cdot \mathbb{I}(\tilde{x}_i^{t-1} = v) $$

其中 $\beta \in (0,1)$ 控制全局衰减，$\gamma \in (0,1)$ 为凹变换参数，用于放大低置信度值的贡献，$\mathbb{I}(\cdot)$ 为指示函数，仅当上一步预测令牌为 $v$ 时更新信用。该设计动机在于：通过 $\beta$ 遗忘陈旧证据以抑制早期噪声，同时通过聚焦增强（Focused Enhancement）仅累积当前预测令牌的信用，确保信用主要赋予那些在去噪轨迹中持续排名Top-1的令牌，而非瞬时尖峰。

### 信用融合与解码加速

轨迹信用作为先验条件，通过Logit空间融合提升目标令牌的置信度。融合后的Logit $\hat{l}_t^{[i,v]}$ 计算为：

$$ \hat{l}_t^{[i,v]} = l_t^{[i,v]} + \alpha C_{t}^{[i,v]} $$

其中 $\alpha > 0$ 控制信用强度。该公式在概率域中等价于对 $p_\theta(v|x_t)$ 施加乘法增益，使得持续被预测的令牌置信度单调递增，从而更早跨越阈值 $\tau$ 被解码。这一机制将解码决策从“瞬时判断”转变为“历史加权判断”，不仅减少了冗余重掩码步骤，还通过早期解码正确令牌改善了后续步骤的上下文质量，形成正向反馈循环，提升了整体解码鲁棒性。

## 实验评估

实验在NVIDIA H20-3e 140 GB GPU上进行，生成长度设为256，块大小64，启用Early Stop。基线包括LLaDA-8B-Instruct（Baseline）和SOTA方法Fast-dLLM。评估覆盖MMLU、SQuAD2.0、DROP、KorBench、HumanEval、LCB、GSM8K、MATH八个基准。

| 基准 | 模型 | 方法 | Score | TPF (Speedup) |
| :--- | :--- | :--- | :--- | :--- |
| MMLU | LLaDA-8B-Ins | CreditDecoding | 63.78 | 4.57 |
| GSM8K | LLaDA-8B-Ins | CreditDecoding | 77.18 | 3.87 |
| HumanEval | LLaDA-8B-Ins | CreditDecoding | 36.59 | 4.69 |
| SQuAD2.0 | LLaDA-8B-Ins | CreditDecoding | 91.71 | 16.84 |

在LLaDA-8B-Instruct上，CreditDecoding平均TPF达5.48倍，平均Score提升0.48分，显著优于Fast-dLLM（TPF 4.31，Score 53.45）。在LLaDA-MoE-Instruct上，TPF达4.10倍，Score提升0.15分。消融实验显示，$\alpha$ 和 $\beta$ 在[0.2, 0.65]和[0.5, 0.7]范围内性能稳定，$\gamma$ 固定为0.2时加速效果最佳。

评估边界方面，论文未报告置信区间，且TPF指标受Early Stop影响较大，不同生成长度下的泛化性仅在附录中简要提及。代码未公开，超参数 $\alpha=0.65, \beta=0.7, \gamma=0.2$ 仅在LLaDA-8B-Instruct上调优，跨模型迁移性依赖Tuning-Free变体，但其性能损失未在主表中量化。

## 关联研究分析

从问题动机看，CreditDecoding与Speculative Decoding（SD）存在本质差异。SD依赖独立草稿模型生成候选序列，通过目标模型验证实现无损加速，其瓶颈在于草稿-目标模型分布不匹配导致的接受率低。而CreditDecoding无需额外模型，利用dLLM自身去噪轨迹中的时间一致性作为“内部草稿”，通过信用累积实现“自推测”。这种差异源于dLLM的迭代去噪特性：每一步预测都是对前一步的修正，历史Logits天然包含关于目标令牌的累积证据，而AR模型中历史令牌是固定前缀，无法提供类似的动态先验。

从方法设计看，CreditDecoding与Hierarchy Decoding同属dLLM免训练加速路线，但优化维度不同。Hierarchy Decoding通过分治原理动态调整并行度，侧重空间维度的令牌分组；CreditDecoding则侧重时间维度的置信度累积，通过EMA平滑瞬时波动。两者可互补：Hierarchy Decoding可能因并行度过高引入错误累积，而CreditDecoding的信用机制可稳定这些并行解码的令牌。然而，论文未探索两者结合的效果，且CreditDecoding在长上下文（>256 tokens）下的信用累积是否会导致早期错误预测被过度强化，缺乏实验验证。

## 总结

本文核心矛盾在于dLLM并行解码中瞬时置信度滞后于真实预测能力导致的计算冗余。CreditDecoding抓住去噪轨迹的时间一致性特征，通过EMA累积历史Logits构建轨迹信用，融合至当前Logits以提前触发解码。实验证明其在LLaDA-8B-Instruct上实现5.48倍加速并提升0.48分准确率，验证了免训练策略的有效性。然而，其边界在于超参数对模型规模的敏感性：在LLaDA-MoE-Instruct上加速比降至4.10倍，且Tuning-Free变体的性能损失未量化。当去噪步数增加至512时，轨迹信用的累积是否会导致早期噪声被过度放大，从而抵消加速收益，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06133)