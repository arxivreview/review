# HuggingFace最新推荐论文 ｜Unified Audio Intelligence Without Regressing on Text Intelligence ｜统一音频智能与文本推理保持

作者：Zhifeng Kong、Sang-gil Lee、Jaehyeon Kim 等 20 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.05196)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.05196)

> 音频语言模型（Audio-Language Model, ALM）在获得多模态生成能力后，常伴随文本推理能力的显著退化，这限制了其作为通用智能体的潜力。现有统一架构如 Qwen3-Omni 在引入语音生成后，数学与代码基准成绩大幅下滑，暴露了多模态训练对文本先验的干扰。本文提出 Audex，通过单一 MoE Transformer 解码器统一处理文本与量化音频 token，并在训练后期引入纯文本强化学习以恢复推理能力。该方案在保持文本智能无损的前提下，实现了公开数据上的 SOTA 音频生成与理解，但其对音频生成多样性的潜在影响及长音频时序推理的边界仍存疑。

## 研究背景

当模型需要同时处理语音转录与环境音生成时，传统级联系统（ASR+LLM+TTS）因模块间信息丢失导致端到端延迟高且语义一致性差。为解决此问题，研究者转向大型音频语言模型（LALM），将音频任务统一为文本生成任务。然而，LALM 在引入多模态输出（特别是音频生成）时，往往牺牲文本推理能力，因为音频 token 的预测分布与文本 token 存在显著差异，导致共享参数空间中的梯度冲突。

早期 LALM 如 Audio Flamingo 系列聚焦于音频理解，通过对比学习对齐音频与文本嵌入，但缺乏生成能力。随着 Qwen-Omni 等模型尝试统一理解与生成，发现多模态输出会导致文本基准（如 AIME、LiveCodeBench）性能下降 10-20 个点。这一“文本-音频智能权衡”成为阻碍 ALM 成为通用智能体的核心瓶颈。本文切入点在于：如何在单一模型架构中，通过架构设计与训练策略的解耦，实现音频生成能力的最大化，同时确保文本推理能力不出现可测量的退化。

## 核心方法

### 统一离散 Token 架构

LALM 的标准流程是音频编码器提取连续特征，经投影层映射至文本嵌入空间，再由 LLM 自回归生成文本。本文的关键差异在于：不仅输入侧统一，输出侧也将音频量化为离散 token，与文本 token 共享同一词表和解码头。这种设计消除了独立生成头（如扩散模型或 VAE）带来的架构复杂性，使音频生成与文本生成在同一个自回归过程中完成。

### 混合 MoE 骨干与音频 Codec 集成

设计动机：解决多模态任务间梯度冲突导致的文本推理退化。本文采用 Nemotron-Cascade-2-30B-A3B 作为骨干，这是一个 Mamba2-Transformer 混合 MoE 架构，拥有 128 个可路由专家，每次激活 6 个。音频输入通过 AF-Whisper 编码器提取 25Hz 特征，经 2 层 MLP 投影至 LLM 维度。音频输出使用两种 Codec：语音使用 X-Codec2（50Hz, FSQ, 65536 词表），非语音使用 X-Codec（50Hz, 4 层 RVQ, 4096 词表）。音频 token 直接扩展至词表，总词表大小从 131,072 扩展至 205,312。

$$
V_{total} = V_{text} + V_{speech} + V_{audio} + V_{special} = 131072 + 65536 + 8192 + 5 = 204805
$$

该公式表明，音频 token 被赋予独立的词汇空间，通过随机初始化（均值 0，标准差 0.02）嵌入，避免了与文本 token 的初始冲突。

### 多阶段 SFT 与文本 RL 恢复

设计动机：解决音频 SFT 对文本推理能力的负迁移。训练分为多阶段：先进行音频预热（Audio Warmup），再进行音频生成与理解联合训练，最后进行纯文本 SFT 和文本 RL。关键创新在于引入 Cascade RL 和多域在线蒸馏，专门针对文本推理任务优化，以抵消音频训练带来的性能损失。

$$
\mathcal{L}_{total} = \mathcal{L}_{SFT}^{audio} + \lambda \mathcal{L}_{SFT}^{text} + \mathcal{L}_{RL}^{text}
$$

其中 $\mathcal{L}_{RL}^{text}$ 仅在文本任务上计算，确保推理能力在音频训练后得到恢复。

## 实验评估

实验在 MMAU、MMAR、MMSU、AudioCaps、LibriSpeech 等基准上进行，对比基线包括 Qwen3-Omni、Step-Audio-R1.1、Kimi-Audio 等。基线覆盖主流 LALM 路线，但缺少纯检索基线（如 CLAP），因任务类型不同。

| 基准 | Audex 30B-A3B | Qwen3-Omni 30B-A3B | Step-Audio R1.1 33B |
| :--- | :--- | :--- | :--- |
| MMAU | 75.6 | 75.4 | 73.6 |
| MMAR | 63.2 | 66.4 | 69.8 |
| MMSU | 63.4 | 70.2 | 74.1 |
| AudioCaps (FD↓) | 60.9 | N/S | N/S |
| LibriSpeech (WER↓) | 1.34 | 1.11 | 1.66 |

Audex 在 MMAU 上与 Qwen3-Omni 持平，但在 MMAR 和 MMSU 上落后，表明其在复杂推理和音乐理解上仍有差距。在音频生成（AudioCaps FD）上，Audex 达到 60.9，优于 UALM 的 65.9，且为公开数据 SOTA。在 ASR 任务上，Audex 的 WER 为 1.34，优于 Step-Audio 的 1.66，但略高于 Qwen3-Omni 的 1.11。

消融实验显示，多阶段 SFT 相比单阶段 SFT，在 AIME 2025 上提升 4.6 个点（91.7 vs 87.1），在 MMAU 上提升 2.8 个点（75.5 vs 72.7）。这表明分阶段训练对文本推理和音频理解的协同优化至关重要。文本 RL 阶段对 AIME 2026 的提升尤为显著（96.6 vs 91.4），验证了 RL 在恢复复杂推理能力上的有效性。

评估边界方面，论文未报告置信区间，且部分基线（如 Qwen3.5-Omni-Flash）为专有模型，无法复现。代码未公开，但提供了模型检查点。音频生成质量使用 FDopenl3 指标，该指标对分布距离敏感，但可能无法完全反映感知质量。

## 关联研究分析

从问题动机看，Audex 与 Qwen3-Omni 均旨在统一音频理解与生成，但 Qwen3-Omni 采用 thinker-talker 架构，将推理与生成解耦，导致文本推理能力在生成模式下显著下降。Audex 通过单一解码器和文本 RL 恢复，证明了在统一架构下，通过训练策略而非架构解耦，可以保持文本智能。这一差异源于任务特性：Qwen3-Omni 更侧重实时交互，而 Audex 更侧重离线高质量生成与推理。

从方法设计看，Audex 与 UALM 同属 LLM-based 音频生成路线，但 UALM 使用 7B 模型且未引入文本 RL，导致文本推理能力有限。Audex 扩展至 30B MoE 并引入 Cascade RL，显著提升了文本推理能力。这一改进源于规模效应与训练策略的结合：MoE 架构提供了足够的参数容量以容纳多模态知识，而文本 RL 则专门优化了推理路径。与扩散模型（如 AudioLDM2）相比，Audex 的离散 token 生成在推理速度上更具优势，但可能在音频细节丰富度上存在差距，论文未对此进行定量对比。

## 总结

本文核心矛盾在于多模态生成与文本推理能力的权衡。Audex 抓住的切入点是：通过单一 MoE 解码器统一处理文本与量化音频 token，并在训练后期引入纯文本 RL 以恢复推理能力。该方法在 MMAU 上达到 75.6，在 AudioCaps 生成上达到 60.9 FD，证明了统一架构的可行性。其边界在于：在 MMAR 和 MMSU 上仍落后于 Qwen3-Omni，表明复杂推理和音乐理解能力尚未完全对齐；且未报告音频生成的感知质量对比，离散 token 生成在细节丰富度上的表现存疑。当音频输入长度超过 900 秒时，模型在长时序推理上的性能衰减程度如何，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.05196)