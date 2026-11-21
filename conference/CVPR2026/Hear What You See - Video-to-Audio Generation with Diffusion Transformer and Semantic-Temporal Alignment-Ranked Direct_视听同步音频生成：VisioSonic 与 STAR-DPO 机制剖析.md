# CVPR2026最新论文 ｜Hear What You See: Video-to-Audio Generation with Diffusion Transformer and Semantic-Temporal Alignment-Ranked Direct Preference Optimization ｜视听同步音频生成：VisioSonic 与 STAR-DPO 机制剖析

研究机构：加拿大多伦多大学、复旦大学

作者：Kai Wang、Tao Zhou、Jiayi Lei 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3776ce797275)

> 视频到音频（Video-to-Audio, V2A）生成的核心矛盾在于视觉动作与声学事件在毫秒级时序上的精确对齐，以及语义内容的一致性。现有方法多依赖粗粒度特征融合或人工标注的偏好数据，导致生成音频常出现语义漂移或时间错位。本文提出 VisioSonic 框架，通过协同注意力机制显式对齐音视频潜变量，并引入自动偏好优化（STAR-DPO）以无监督方式强化同步质量。该方案在最小参数量下实现了领先的同步指标，但其单数据集训练策略对跨域泛化能力的验证尚存疑。

## 研究背景

理解本文需先厘清流匹配（Flow Matching）与潜空间建模的耦合关系。传统扩散模型在波形域直接去噪面临高维计算瓶颈，而潜在扩散模型（Latent Diffusion Model, LDM）将生成任务移至低维潜空间，显著提升了训练稳定性。然而，LDM 的多步采样延迟难以满足实时需求，流匹配技术通过定义噪声与数据分布间的线性传输路径，预测速度场以实现少步生成，成为当前高效音频合成的主流范式。

V2A 任务要求生成的音频不仅语义正确，还需与视频动作严格同步。早期工作如 Diff-Foley 和 Frieren 尝试在对比潜空间或输入层面对齐音视频，但缺乏对细粒度时间动态的显式建模。MMAudio 虽引入多模态 Transformer 联合处理视频、文本与音频，但其自注意力机制未充分利用音视频固有的时序相关性，且依赖类别标签而非描述性文本，限制了语义引导的丰富度。本文切入点在于：通过显式的 Token 对齐器桥接音视频时间分辨率差异，并设计协同注意力机制强化跨模态交互，同时引入自动偏好优化解决人工标注稀缺问题。

## 核心方法

### 方法参照系

本文基于 Next-DiT 架构，采用 Rectified Flow Matching (RFM) 目标。与 MMAudio 使用 MMDiT 自注意力直接拼接三模态不同，VisioSonic 将视频与音频潜变量沿时间轴对齐后，再与文本进行协同注意力交互，旨在利用音视频内在同步性提升生成一致性。

### 多模态条件器与协同注意力 DiT

多模态条件器将视频编码为低帧率语义嵌入（CLIP）和高帧率时间嵌入（Synchformer），文本编码为语义嵌入。设计动机在于解决低帧率视频缺乏细粒度时间线索、导致生成音频与动作错位的问题。协同注意力 DiT 通过 Token Aligner 将视频嵌入插值至与音频潜变量相同的时间长度，随后通过 QKV 投影进行自注意力交互，并通过交叉注意力注入文本信息。

$$
L_{\text{RFM}} = \mathbb{E}_{t, p_0(a_0), p_1(a_1)} \left\| v_\theta(t, a_t, C) - (a_1 - a_0) \right\|_2^2
$$

该公式定义了流匹配训练目标，其中 $v_\theta$ 预测速度场，$C$ 包含视频与文本条件。通过最小化预测速度与真实速度差的平方，模型学习在潜空间中沿直线路径从噪声传输至数据分布，实现高效采样。

### STAR-DPO 偏好优化

STAR-DPO 是首个将直接偏好优化（DPO）扩展至 V2A 生成的框架。设计动机在于解决人工标注偏好数据成本高且难以覆盖细粒度同步需求的问题。该模块利用预训练的 ImageBind 和 Synchformer 作为奖励模型，自动评估生成音频的语义与时间对齐得分，构建偏好对进行微调。

$$
L_{\text{final}} = -\mathbb{E} \log \sigma \left( -\beta \left[ (L_w - L_w^{\text{ref}}) - (L_l - L_l^{\text{ref}}) \right] \right) + L_{\text{RFM}}
$$

该公式结合了 DPO 损失与流匹配正则项。$L_w$ 和 $L_l$ 分别为获胜与落败样本的流匹配损失，$\beta$ 控制偏好强度，$L_{\text{RFM}}$ 防止过优化。通过最大化获胜样本与落败样本的对数似然比，模型被引导生成更高对齐质量的音频。

## 实验评估

实验在 VGGSound 测试集上进行，对比了 Seeing&Hearing、MMAudio、Frieren 等 9 种 SOTA 方法。基线覆盖了从自回归到扩散、从单模态到多模态的主流路线，但缺失基于最新连续自回归架构的对比。

| 方法 | 参数量 | FD_PaSST↓ | KL_PANNs↓ | IB-score↑ | DeSync↓ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MMAudio-L | 1.03B | 60.60 | 0.97 | 17.40 | 0.442 |
| Frieren | 159M | 106.10 | 1.34 | 12.25 | 0.851 |
| VisioSonic Base | 151M | 58.27 | 1.18 | 18.12 | 0.45 |
| VisioSonic w/ STAR-DPO | 151M | 55.48 | 0.99 | 18.41 | 0.41 |

VisioSonic w/ STAR-DPO 在 FD_PaSST 和 DeSync 上均取得最优，较 MMAudio-L 的 FD 降低 5.12，DeSync 降低 0.032，且参数量仅为后者的 14.7%。

消融实验验证了协同注意力与奖励模型的有效性。

| 变体 | FD_PaSST↓ | IB-score↑ | DeSync↓ |
| :--- | :--- | :--- | :--- |
| T+V+A (Co-attn) | 59.71 | 15.70 | 0.47 |
| T+AV (Flux-like) | 66.76 | 16.04 | 0.46 |
| T+AV (Co-attn) | 58.27 | 18.12 | 0.45 |
| IB-AV + DeSync | 55.48 | 33.1 | 0.41 |

完全分离模态的 T+V+A 变体语义对齐最弱，表明跨模态交互必要性。组合使用 IB-AV 和 DeSync 奖励模型在 IB-score 上达到 33.1，显著优于单一奖励模型，证实了语义与时间奖励的互补性。

评估指标涵盖分布匹配、感知质量、语义与时间对齐，但未报告实时因子（RTF）或 FLOPs，计算效率维度缺失。代码已开源，但偏好优化迭代次数对最终性能的影响未在正文详细展开，仅指出第 2 轮迭代效果最佳。

## 关联研究分析

从方法设计看，VisioSonic 与 MMAudio 的核心差异在于模态融合策略。MMAudio 采用 MMDiT 自注意力，将视频、文本、音频视为平等序列，忽略了音视频在时间轴上的天然对应关系。VisioSonic 引入 Token Aligner 显式对齐时间维度，并通过协同注意力区分自交互（音视频）与交叉交互（文本），这种结构先验更契合 V2A 任务的物理特性。然而，Token Aligner 采用线性插值，对于非匀速运动场景（如突然加速）的时间对齐精度是否足够，论文未提供针对性实验。

从偏好优化路线看，VisioSonic 的 STAR-DPO 与 TangoFlux 的 CLAP 偏好优化形成对比。TangoFlux 针对 T2A 任务使用 CLAP 评估文本-音频对齐，而 STAR-DPO 针对 V2A 任务使用 ImageBind（语义）和 Synchformer（时间）双奖励模型。这种奖励模型的适配性源于任务特性：V2A 需要同时满足语义与时间约束，单一模态奖励无法覆盖。但 STAR-DPO 依赖预训练奖励模型的准确性，若 ImageBind 或 Synchformer 在特定域（如音乐）存在偏差，偏好数据质量将受影响，这一风险在跨域泛化实验中未充分暴露。

## 总结

VisioSonic 旨在解决 V2A 生成中语义与时间同步的双重挑战，其切入点在于显式利用音视频时间相关性并引入自动偏好优化。通过协同注意力 DiT 与 STAR-DPO，模型在 151M 参数量下实现了 FD_PaSST 55.48 与 DeSync 0.41 的领先性能。然而，实验仅基于 VGGSound 单数据集，且偏好优化迭代次数对泛化性的影响未深入探讨。当训练数据扩展至多源混合数据集时，自动偏好优化能否维持同步优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_3776ce797275)