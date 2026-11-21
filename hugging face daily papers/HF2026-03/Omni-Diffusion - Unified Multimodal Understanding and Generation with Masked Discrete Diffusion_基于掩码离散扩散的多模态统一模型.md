# HuggingFace最新推荐论文 ｜Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion ｜基于掩码离散扩散的多模态统一模型

研究机构：南京大学

作者：Lijiang Li、Zuwei Long、Yunhang Shen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.06577)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06577)

> 统一多模态模型旨在单一架构内融合理解与生成，但主流自回归架构受限于串行解码效率与顺序依赖，难以实现高效的多模态交互。现有方案多依赖级联解码器或混合训练，缺乏对非自回归概率建模的深入探索。本文提出 Omni-Diffusion，首次将基于掩码的离散扩散模型（Mask-based Discrete Diffusion Model, MDM）作为骨干，通过联合建模文本、图像与语音的离散 Token 分布，实现 Any-to-Any 多模态交互。该方法在语音与视觉任务上达到或超越自回归基线，但缺乏对高分辨率生成保真度与闭环协同效应的严格验证。

## 研究背景

当多模态大语言模型（MLLMs）处理长序列语音或高分辨率图像时，自回归架构的串行解码机制导致推理延迟随序列长度线性增长，且生成过程严格依赖前序 Token，限制了并行计算潜力。为突破此瓶颈，离散扩散模型（Discrete Diffusion Model）通过迭代去噪并行预测 Token，成为替代自回归架构的候选方案。然而，将离散扩散应用于多模态统一模型面临两大挑战：一是不同模态（文本、图像、语音）的 Token 分布差异巨大，直接联合训练易导致模态间干扰；二是离散 Token 化本身存在信息损失，需设计特定的训练与推理策略以维持生成质量。

统一多模态理解与生成领域的核心矛盾在于理解任务对语义抽象的偏好与生成任务对像素保真的偏好之间的表征冲突。主流路线如 Janus 采用解耦编码器，Transfusion 采用混合自回归-扩散目标，虽缓解了冲突，但架构复杂度增加且未根本解决推理效率问题。本文切入点在于彻底摒弃自回归骨干，利用 MDM 的并行解码特性与联合分布建模能力，在共享离散 Token 空间中实现多模态对齐，旨在验证非自回归架构在多模态统一任务中的可行性与效率优势。

## 核心方法

### 统一概率建模框架

本文方法参照系为基于 Transformer 的统一多模态模型，其标准流程是将各模态数据离散化为 Token，通过自回归预测下一 Token。本文的关键差异在于将骨干网络替换为 MDM，训练目标从预测下一 Token 变为预测被掩码的 Token。给定文本 $T$、语音 $S$、图像 $I$，模型将其编码为离散 Token 序列 $x_0$，并通过随机掩码比例 $r$ 生成噪声序列 $x_t$。模型学习预测干净序列 $\hat{x}_0 = p_\theta(x_0|x_t)$，损失函数为掩码位置的交叉熵：

$$ \mathcal{L} = -\sum_{i \in \mathcal{M}} \log p_\theta(x_{0,i} | x_t) $$

其中 $\mathcal{M}$ 为掩码位置集合。该设计消除了自回归的顺序依赖，允许并行解码，但需解决变长生成中的过拟合问题。

### 渐进式训练与掩码策略

针对多模态数据分布差异导致的训练不稳定，本文提出三阶段渐进式训练：第一阶段对齐视觉-语言模态，第二阶段引入语音-文本对齐，第三阶段在自构建的语音驱动视觉交互（SDVI）数据集上微调，强化跨模态协同。为解决变长生成中 Pad Token 过拟合问题，提出衰减尾部填充掩码（Attenuated Tail-Pad Masking）策略。在标准掩码策略中，Pad Token 与语义 Token 以相同比例被掩码，导致模型过度关注 Pad Token。本文引入缩放因子 $\gamma < 1$，专门降低 Pad Token 的掩码比例：

$$ r_{pad} = \gamma \cdot r_{semantic} $$

此设计确保梯度更新主要由语义 Token 驱动，抑制 Pad Token 的过度生成，从而提升变长响应的生成质量。

### 推理优化策略

推理阶段采用基于熵的解码策略，结合重复惩罚与分类器自由引导。针对图像生成，引入位置惩罚（Position Penalty）约束生成顺序，提升视觉质量；针对语音生成，提出特殊 Token 预填充（Special Token Pre-infilling）策略，允许模型在生成语音时融入文本语义。此外，应用自适应 Token 长度初始化策略，根据任务特性动态调整初始掩码序列长度，进一步优化语音理解与生成的性能。

## 实验评估

实验在 LibriSpeech、LibriTTS、POPE、MME-Perception、Seed-2-Plus 及 MSCOCO 上进行，对比基线包括 AnyGPT、NExT-GPT、GLM-4-Voice 及专用视觉 LLM（如 LLaVA、Emu）。基线覆盖自回归 Any-to-Any 模型与专用模态模型，但缺失 BAGEL、Transfusion 等主流混合架构基线，限制了与当前 SOTA 混合模型的直接对比。

| 任务 | 方法 | 指标 | 数值 |
|---|---|---|---|
| ASR | Omni-Diffusion | WER ↓ | 7.05 |
| ASR | AnyGPT | WER ↓ | 8.50 |
| TTS | Omni-Diffusion | WER ↓ | 3.07 |
| TTS | GLM-4-Voice | WER ↓ | 2.82 |
| VQA | Omni-Diffusion | POPE ↑ | 76.6 |
| VQA | AnyGPT | POPE ↑ | 67.7 |
| T2I | Omni-Diffusion | CLIP-T ↑ | 0.235 |
| T2I | Emu | CLIP-T ↑ | 0.286 |
| T2I | Omni-Diffusion | CLIP-I ↑ | 0.667 |
| T2I | Emu | CLIP-I ↑ | 0.656 |

Omni-Diffusion 在 ASR 与 VQA 任务上优于 AnyGPT，TTS 性能接近专用模型 GLM-4-Voice（3.07 vs 2.82）。在文本到图像生成中，CLIP-I 得分（0.667）略高于 Emu（0.656），但 CLIP-T 得分（0.235）显著低于 Emu（0.286），表明文本-图像对齐能力较弱。消融实验未提供详细数值，但论文指出衰减尾部填充掩码策略有效缓解了 Pad Token 过拟合，位置惩罚提升了图像生成质量。

评估边界方面，本文未使用 GenEval、MMBench 等标准组合生成与理解基准，缺乏对复杂指令遵循与高阶推理能力的验证。代码未公开，超参数细节有限，可复现性受限。指标完备性不足，未报告置信区间，数值比较需谨慎。

## 关联研究分析

从问题动机看，本文与 NExT-GPT 同属 Any-to-Any 框架，但 NExT-GPT 依赖外部扩散解码器，本文端到端建模离散 Token 分布。差异根源在于架构选择：NExT-GPT 保留自回归骨干，本文采用 MDM。本文未探索 MDM 在长序列语音生成中是否真正优于自回归的并行解码效率，仅展示性能持平。

从方法设计看，本文与 Transfusion 均涉及扩散机制，但 Transfusion 采用混合自回归-扩散目标，本文纯离散扩散。Transfusion 通过混合目标缓解表征冲突，本文通过联合分布建模实现模态对齐。本文未验证纯离散扩散在高分辨率生成上是否必然低于连续潜空间方法，CLIP-T 低于 Emu 的结果暗示离散 Token 化在细节保真度上的局限。

## 总结

Omni-Diffusion 旨在解决自回归架构在多模态统一模型中的推理效率瓶颈与顺序依赖问题。通过采用 MDM 骨干与联合离散 Token 建模，本文实现了 Any-to-Any 多模态交互，在 ASR 与 VQA 任务上优于 AnyGPT，TTS 性能接近专用模型。然而，实验未覆盖 GenEval 等标准基准，CLIP-T 低于 Emu 表明文本-图像对齐能力不足，且缺乏闭环评估验证理解与生成的协同效应。当序列长度进一步增加时，MDM 的并行解码效率是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06577)