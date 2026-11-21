# ICLR2026最新论文 ｜DON T SETTLE TOO EARLY: SELF-REFLECTIVE RE MASKING FOR DIFFUSION LANGUAGE MODELS ｜自反思重掩码扩散语言模型

研究机构：浙江大学、西湖大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_39811228)

> 掩码扩散语言模型（Masked Diffusion Language Model, MDLM）在并行解码中面临已生成 token 无法修正的误差固化问题，导致早期预测错误贯穿整个生成过程。现有方法或依赖随机重掩码缺乏针对性，或修改扩散过程增加复杂度，均未能提供原则性的错误检测机制。RemeDi 引入双流架构与置信度评分，通过两阶段训练使模型学会识别并重掩码低质量 token。该机制在开源 DLM 中实现了多项基准的领先性能，但其对长序列计算开销及随机错误模拟与真实推理误差分布的匹配度仍存疑。

## 研究背景

掩码扩散语言模型（Masked Diffusion Language Model, MDLM）通过迭代去噪并行生成文本，其核心优势在于突破自回归（AR）模型串行解码的效率瓶颈。然而，标准 MDLM 假设一旦 token 被去掩码即视为正确，这一假设在早期步骤中尤为脆弱：由于上下文信息有限，模型可能生成错误 token，且这些错误在后续步骤中无法被修正，导致误差累积。这种“一次性承诺”机制使得 MDLM 在复杂推理任务上的表现受限，尤其是在需要全局一致性校验的场景中。

主流解决思路分为两类：一是预测-校正采样器，如在推理时随机重掩码部分 token（Wang et al., 2025a），但缺乏识别错误 token 的机制，需大量额外采样步骤；二是修改扩散过程，如结合均匀噪声或编辑扩散（von Rütte et al., 2025; Song et al., 2025），但增加了架构复杂度且未提供原则性的错误检测方式。RemeDi 的切入点在于将“错误检测”内化为模型能力，通过训练模型预测每个 token 的置信度分数，使其能够自主识别低质量 token 并重掩码，从而在后续步骤中利用更丰富的上下文进行修正。

## 核心方法

### 方法参照系

标准 MDLM 采用单流 Transformer 架构，仅预测掩码位置的 token 分布 $p_\theta$。其推理过程遵循单调去噪原则，即掩码数量随步骤线性减少，已去掩码 token 固定不变。本文的关键差异在于引入“重掩码”机制，允许已去掩码 token 在后续步骤中被重新掩码，这要求模型具备评估自身预测质量的能力，而标准 MDLM 缺乏此机制。

### 双流架构与置信度评分

RemeDi 将标准 Transformer 扩展为双流架构，包含 Token Prediction Stream (TPS) 和 Unmasking Policy Stream (UPS)。TPS 负责预测掩码位置的 token 分布，UPS 则输出每个位置的置信度分数 $h_\theta$。两流并行运行，UPS 接收 TPS 的隐藏状态作为输入，并通过双向特征共享增强表示。在最终层，两个独立的线性头分别产生 $p_\theta$ 和 $h_\theta$。这一设计解决了标准 MDLM 无法区分“正确预测”与“错误预测”的问题，使模型能够基于置信度动态决定哪些 token 应被去掩码或重掩码。

$$
h_\theta = \text{Linear}_{UPS}(f_{UPS}), \quad p_\theta = \text{Linear}_{TPS}(f_{TPS})
$$

该公式表明，置信度分数 $h_\theta$ 和 token 分布 $p_\theta$ 由两个独立的线性头从各自流的最终表示中生成，实现了预测与评估的解耦。

### 重掩码感知训练

Remask SFT 阶段通过模拟错误 token 训练模型识别错误。具体而言，在构建训练样本时，除随机掩码外，还以比例 $\rho_{t, incorrect}$ 将部分未掩码 token 替换为随机替代 token，模拟推理中的错误。训练目标包括扩散损失 $L_{diffusion}$ 和 UPS 的二元交叉熵损失 $L_{UPS}$，其中 $L_{UPS}$ 监督置信度分数 $h_\theta$ 与标签 $y$ 的一致性。标签 $y$ 根据 token 类型分配：干净 token 为 1，错误 token 为 0，掩码 token 为预测概率的停止梯度值。

$$
L(\theta) = L_{diffusion}(\theta) + \lambda_{UPS} L_{UPS}(\theta)
$$

该公式表明，总损失由扩散损失和置信度监督损失加权组成，$\lambda_{UPS}$ 平衡两者，确保模型同时学习预测 token 和评估其质量。

## 实验评估

实验在 GSM8K、MATH、HumanEval、MBPP、ARC-C、IFEval 和 AlpacaEval 等基准上进行，对比了 Dream、LLaDA、LLaDA 1.5 等 DLM 及 LLaMA、Deepseek 等 AR 模型。基线覆盖了主流 DLM 和 AR 模型，但缺少与最新 RL 对齐方法（如 SPG、DISPO）的直接对比。

| 方法 | GSM8K | MATH | HumanEval | MBPP |
| :--- | :--- | :--- | :--- | :--- |
| LLaDA | 82.1 | 49.6 | 59.6 | 45.7 |
| Dream | 82.1 | 30.6 | 59.8 | 45.7 |
| RemeDi (+ SFT) | 86.3 | 51.4 | 71.3 | 57.8 |
| RemeDi (+ RL) | 89.1 | 52.9 | 73.2 | 59.4 |

RemeDi 在 Remask SFT 后已超越 LLaDA 和 Dream，Remask RL 后进一步提升，GSM8K 准确率达 89.1%，HumanEval Pass@1 达 73.2%。

消融实验显示，Remask SFT 相比 Vanilla SFT 在 GSM8K 上提升 3.3 个点（83.6 vs 80.3），HumanEval 提升 8.5 个点（50.0 vs 41.5），表明重掩码机制对代码生成任务收益显著。Remask RL 相比 LLaDOU RL 在 50 步时准确率更高（80.00% vs 77.58%），收敛速度更快。

评估边界方面，论文未报告长文本生成中的计算开销，且随机错误模拟可能无法完全覆盖真实推理中的误差分布。代码已开源，但超参数细节（如 $\lambda_{UPS}$ 的具体值）未在正文中明确给出，可能影响复现性。

## 关联研究分析

从问题动机看，RemeDi 与 Seed Diffusion（Song et al., 2025）均旨在解决 token 无法修正的问题，但 Seed Diffusion 允许所有 token 在每步重采样，计算开销大且缺乏选择性；RemeDi 通过置信度筛选实现局部重掩码，效率更高。这一差异源于任务特性：Seed Diffusion 适用于短序列，而 RemeDi 通过选择性重掩码更适合长序列场景。

从方法设计看，RemeDi 与 SPG（Wang et al., 2025）同属 RL 对齐路线，但 SPG 优化策略梯度以提升推理能力，RemeDi 则将重掩码决策纳入策略空间，优化整个生成轨迹。这一差异暗示，RemeDi 的 RL 阶段不仅优化最终输出，还优化中间步骤的错误修正行为，可能更适用于需要多步推理的任务。

## 总结

RemeDi 针对 MDLM 中已生成 token 无法修正的误差固化问题，通过双流架构与置信度评分实现自反思重掩码。其两阶段训练使模型学会识别错误 token 并在后续步骤中修正，GSM8K 准确率达 89.1%，HumanEval Pass@1 达 73.2%。然而，论文未探讨长序列下重掩码的计算开销，且随机错误模拟与真实推理误差分布的匹配度未经验证。当序列长度增加时，置信度评分的可靠性是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_39811228)