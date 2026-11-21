# HuggingFace最新推荐论文 ｜VideoLoom: A Video Large Language Model for Joint Spatial-Temporal Understanding ｜视频时空联合理解模型

研究机构：复旦大学、美国马里兰大学帕克分校

作者：Jiapeng Shi、Junke Wang、Zuyao You 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07290)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07290)

> 视频大语言模型（Video LLM）在处理细粒度视频理解时，长期面临空间定位与时间定位的割裂，导致无法在单一框架内完整解析复杂时空事件。现有方法或依赖单一维度标注数据，或在固定算力下难以平衡高分辨率空间需求与密集采样时间需求。本文通过构建时空一致数据集 LoomData-8.7k，并提出基于 SlowFast 视觉 Token 与 MLLM-SAM2 架构的 VideoLoom，实现了时空联合推理。该方法在联合基准上显著优于级联基线，但在单一维度 SOTA 上未超越专用模型，其性能上限是否受限于缺乏强化学习优化仍存疑。

## 研究背景

视频理解任务中，空间定位要求高分辨率输入以捕捉物体细节，而时间定位依赖密集帧采样以建模运动动态。这种输入粒度的内在冲突，使得在固定计算预算下，单一模型难以同时满足两类任务的需求。传统做法是将空间与时间任务分离训练，但标注格式与数据分布的不一致会导致训练不稳定，阻碍模型建立连贯的时空关联。

视频大语言模型（Video LLM）的发展推动了从粗粒度问答向细粒度定位的演进。时序模型如 TimeChat 和 TRACE 专注于时间戳感知指令微调，空间模型如 VRS-HQ 和 Sa2VA 聚焦于轨迹或掩码预测。然而，这些模型均局限于单一维度，无法处理需要同时回答“何时”与“何地”的复合查询。现有联合尝试多受限于特定任务或粗粒度感知，缺乏细粒度时空标注数据的支持。本文的切入点在于解决数据稀缺与算力冲突的双重瓶颈，通过自动标注流水线生成时空一致数据，并设计双粒度视觉 Token 机制，在统一框架内实现时空联合理解。

## 核心方法

### 方法参照系

本文问题属于视频大语言模型（Video LLM）的细粒度理解范畴。通用流程通常采用单一分辨率帧序列输入视觉编码器，生成视觉 Token 后与文本指令拼接，由大语言模型（LLM）生成文本响应。本文的关键差异在于，标准流程无法在固定算力下同时满足空间高分辨率与时间密集采样的需求，且缺乏从文本生成到像素级分割的统一输出接口。

### SlowFast 双粒度视觉 Token

针对空间与时间任务对输入粒度的不同需求，本文在视觉编码阶段引入双粒度 Token 机制。通常做法是均匀采样固定数量帧并生成单一密度 Token，导致空间细节丢失或时间覆盖不足。本文创新性地生成 Fast Token 与 Slow Token：Fast Token 从全视频均匀采样至多 128 帧，每帧仅分配 16 个 Token，提供低密度全局时序上下文；Slow Token 从 5 个关键帧提取，每帧分配 256 个 Token，保留高分辨率空间细节。两种 Token 与语言指令交错排列，形成输入序列。该设计解决了固定算力下无法平衡时间覆盖与空间精度的失效，使模型能同时感知长视频动态与局部细节。

$$
\text{Input Sequence} = \text{Interleave}(\text{Fast Tokens}_{128 \times 16}, \text{Slow Tokens}_{5 \times 256}, \text{Language Instructions})
$$

此公式表示输入序列由低密度时序 Token、高密度空间 Token 与文本指令交错构成，实现了时空信息的解耦与联合编码。

### MLLM-SAM2 统一架构

在模型架构层面，本文解决了文本生成与像素级分割输出不兼容的问题。通常做法是 LLM 仅输出文本，分割任务需独立模型处理。本文创新地将 InternVL3 作为 MLLM 主干，SAM2 作为分割模块，通过特殊 `[SEG]` Token 连接两者。LLM 处理 SlowFast Token 与文本查询，生成时间戳文本及 `[SEG]` Token 嵌入；SAM2 利用该嵌入生成关键帧掩码，并通过视觉记忆传播至全视频。该设计实现了从语义理解到像素定位的统一输出，消除了级联范式中的信息损失。

$$
\mathcal{L} = \lambda_{\text{text}} \mathcal{L}_{\text{text}} + \lambda_{\text{mask}} \mathcal{L}_{\text{mask}}
$$

此公式表示端到端训练目标，其中 $\mathcal{L}_{\text{text}}$ 为文本生成的交叉熵损失，$\mathcal{L}_{\text{mask}}$ 为分割损失（BCE 与 DICE 之和），$\lambda$ 为平衡超参数，确保时空联合优化。

## 实验评估

实验在 Charades-STA、YouCook2、QVHighlights 等时序基准及 MeVIS、ReVOS 等空间基准上进行。基线覆盖 TimeChat、TRACE、TimeSuite 等时序模型及 VRS-HQ、Sa2VA 等空间模型，但缺失 TempR1 等基于强化学习（RL）的时序定位 SOTA 直接对比。

| 基准 | 指标 | VideoLoom-8B | TimeSuite-7B | VRS-HQ-7B |
| :--- | :--- | :--- | :--- | :--- |
| Charades-STA | R1@0.7 | 48.3 | 43.0 | - |
| QVHighlights | HIT@1 | 63.3 | 55.3 | - |
| MeVIS | J&F | 51.7 | - | 50.6 |
| ReVOS | J&F | 63.1 | - | 59.1 |

VideoLoom 在时序与空间基准上均取得 SOTA 或竞争性结果，Charades-STA R1@0.7 达 48.3，MeVIS J&F 达 51.7，优于 TimeSuite 与 VRS-HQ。

在 LoomBench 联合基准上，VideoLoom 在 Combined 问题上 tIoU 达 41.6，J&F_bi-fore 达 49.1，显著优于 TimeSuite+Sa2VA 级联基线（25.4 tIoU，33.7 J&F_bi-fore）。这一差距验证了端到端联合建模优于“先定位后分割”的级联范式，表明时空联合理解需在同一框架内完成，而非任务串联。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码与超参数已公开，使用 8 张 NVIDIA H20 GPU 训练，可复现性良好。但 LoomBench 的 Combined 问题仅 456 个，样本量较小，可能影响统计显著性。

## 关联研究分析

从问题动机看，VideoLoom 与 TimeSuite 的核心差异在于处理时空耦合的方式。TimeSuite 采用级联策略，先定位时间片段再分割空间区域，导致时间定位误差传递至空间分割，且无法处理时空交织的复合查询。VideoLoom 通过 SlowFast Token 与 MLLM-SAM2 架构实现端到端联合，避免了级联误差累积。这一差异源于任务特性：复合查询要求时空信息同时参与推理，级联范式在信息融合阶段存在瓶颈，而联合架构在特征层面实现了时空交互。

从方法设计看，VideoLoom 与 TempR1 的差异在于优化范式。TempR1 采用强化学习（RL）提升时序推理精度，通过过程奖励增强模型对时间动态的敏感性；VideoLoom 采用监督微调（SFT），依赖高质量数据 LoomData-8.7k 提升性能。这一差异暗示，SFT 在数据充足时可能达到较高性能，但 RL 在数据稀缺或复杂推理场景中可能更具优势。VideoLoom 未使用 RL，是否导致其在时序定位上落后于 TempR1，论文未给出直接对比，但 Charades-STA 上 48.3 R1@0.7 与 TempR1 59.8 mIoU 的差距（协议不同）提示 RL 可能提升时序精度上限。

## 总结

VideoLoom 旨在解决视频大语言模型中空间与时间定位割裂、无法在单一框架内处理复合时空查询的核心矛盾。其切入点在于构建时空一致数据集 LoomData-8.7k，并提出 SlowFast 双粒度 Token 与 MLLM-SAM2 架构，在固定算力下平衡时间覆盖与空间精度，实现端到端联合输出。实验证明，VideoLoom 在 LoomBench Combined 问题上 tIoU 达 41.6，显著优于级联基线，验证了联合建模的有效性。然而，论文未与 TempR1 等 RL 方法直接对比，且 LoomBench 样本量较小，限制了结论的普适性。当支持集增大或引入 RL 优化时，SlowFast 机制的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07290)