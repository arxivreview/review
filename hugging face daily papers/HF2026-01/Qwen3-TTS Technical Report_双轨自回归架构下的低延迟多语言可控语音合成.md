# HuggingFace最新推荐论文 ｜Qwen3-TTS Technical Report ｜双轨自回归架构下的低延迟多语言可控语音合成

作者：Hangrui Hu、Xinfa Zhu、Ting He 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15621)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15621)

> 表达性文本转语音（Expressive and Controllable TTS）旨在解决“说什么”与“怎么说”的解耦难题，但现有自回归模型在长序列生成中易出现误差累积，且流匹配模型难以兼顾指令遵循与超低延迟。Qwen3-TTS 通过引入双轨自回归架构与两种不同频率的离散语音分词器，在保持自然语言指令控制能力的同时，将首包延迟降至 97 ms。该方案在零样本克隆与跨语言合成上刷新了基准记录，但其对大规模预训练数据的依赖使得架构本身的边际贡献难以剥离。

## 研究背景

当自回归语言模型（LLM）处理离散语音 Token 时，长序列中的量化误差会随时间步累积，导致韵律漂移或内容遗漏；而纯声学 Token 虽保真度高，却因包含过多低层细节而增加 LLM 建模难度。为平衡语义表达力与声学可建模性，研究需构建能同时捕获高层语义与低层声学特征的混合表示，这构成了离散语音 Tokenization 的核心挑战。

可控 TTS 的主流路线已从显式韵律特征转向自然语言指令驱动，但现有方法面临两难：基于流匹配的非自回归模型推理效率高，却难以捕捉复杂语义指令；基于 LLM 的自回归模型擅长指令遵循，但受限于自回归解码的串行特性，首包延迟高，无法满足实时交互需求。Qwen3-TTS 的切入点在于解耦“语义建模”与“声学解码”的延迟瓶颈，通过双轨架构让文本 Token 与声学 Token 并行处理，并设计专用分词器以最小化解码等待时间。

## 核心方法

### 双轨自回归架构

本文问题与标准自回归 TTS 的关键差异在于，标准流程中声学 Token 的生成严格依赖于前序声学 Token，导致首包延迟受限于 LM 生成速度。Qwen3-TTS 采用双轨表示，将文本 Token 与声学 Token 沿通道轴拼接。当 LM 接收到一个文本 Token 时，立即预测对应的声学 Token，而非等待完整的文本序列。这种设计将声学生成的起始点提前至文本流的早期阶段，实现了流式输入与流式输出的同步。

### 多码本语义-声学解耦分词器

针对单一码本在表达力与延迟间的权衡失效，本文设计了两种分词器。Qwen-TTS-Tokenizer-12Hz 采用 12.5 Hz 多码本方案，其第一层码本编码语义内容，后续 15 层残差向量量化（RVQ）层捕获声学细节。其核心公式为：

$$
\mathbf{c} = \text{RVQ}(\mathbf{z}_{\text{acoustic}}) \oplus \mathbf{c}_{\text{semantic}}
$$

其中 $\mathbf{c}_{\text{semantic}}$ 由 WavLM 教师模型引导生成，$\mathbf{z}_{\text{acoustic}}$ 为声学潜变量。该设计允许使用轻量级因果 ConvNet 直接重建波形，无需复杂的扩散模型或说话人向量提取。相比之下，25Hz 分词器采用单码本，依赖块状流匹配（Flow Matching）重建，虽支持流式但首包延迟较高。12Hz 分词器的因果设计使得每个 Token 生成后可立即解码，消除了对上下文前瞻的依赖。

### 多 Token 预测（MTP）模块

为解决多码本序列的串行预测延迟，本文引入 MTP 模块。在 12Hz 架构中，骨干网络预测第 0 层码本后，MTP 模块并行生成所有剩余码本。其预测过程可表示为：

$$
\mathbf{c}_{1:L} = \text{MTP}(\mathbf{c}_0, \mathbf{h}_{\text{text}})
$$

其中 $\mathbf{h}_{\text{text}}$ 为文本隐状态。这一机制将多码本解码从串行迭代转化为单次前向传播，显著降低了 Tokenizer 解码时间，是实现 97 ms 首包延迟的关键组件。

## 实验评估

实验在 Seed-TTS、InstructTTSEval 及内部长文本数据集上进行，基线覆盖 CosyVoice、MiniMax、ElevenLabs 及 VibeVoice 等。在零样本克隆任务中，Qwen3-TTS-12Hz-1.7B 在 Seed-TTS test-en 上取得 1.24% 的 WER，优于 CosyVoice 3 的 1.45% 和 Seed-TTS 基线的 2.25%。

| 模型 | Seed-TTS test-en WER (%) | Seed-TTS test-zh WER (%) |
| :--- | :--- | :--- |
| Qwen3-TTS-12Hz-1.7B-Base | 1.24 | 0.77 |
| CosyVoice 3 | 1.45 | 0.71 |
| F5-TTS | 1.83 | 1.56 |
| MaskGCT | 2.62 | 2.27 |

在跨语言合成中，Qwen3-TTS 在中文到韩语（zh-to-ko）任务上表现突出，错误率从 CosyVoice3 的 14.4 降至 4.82。在指令遵循任务中，Qwen3-TTS-12Hz-1.7B-VD 在 InstructTTSEval-ZH 的 DSD 指标上达到 81.1，优于 GPT-4o-mini-tts 的 52.3。

| 任务 | 模型 | 指标 | 数值 |
| :--- | :--- | :--- | :--- |
| Cross-Lingual (zh-to-ko) | Qwen3-TTS-12Hz-1.7B | CER | 4.82 |
| Cross-Lingual (zh-to-ko) | CosyVoice3 | CER | 14.4 |
| InstructTTSEval-ZH (Voice Design) | Qwen3-TTS-12Hz-1.7B-VD | DSD | 81.1 |
| InstructTTSEval-ZH (Voice Design) | GPT-4o-mini-tts | DSD | 52.3 |

消融实验显示，12Hz 分词器在内容准确性上优于 25Hz，表明更粗的时间分辨率有助于 LLM 建模长程依赖。然而，在长文本生成任务中，25Hz 变体（WER 1.517）优于 12Hz 变体（WER 2.356），暗示语义 Token 在超长序列稳定性上更具优势。

评估边界方面，论文未报告置信区间，且部分主观指标（如 MOS）缺失。代码与模型已开源，但 500 万小时预训练数据的具体构成未完全披露，限制了复现的精确性。

## 关联研究分析

从方法设计看，Qwen3-TTS 与 FLEXIVOICE 均致力于指令遵循，但 FLEXIVOICE 依赖强化学习（RL）对齐偏好，而 Qwen3-TTS 通过架构层面的双轨并行与 MTP 模块解决延迟问题。FLEXIVOICE 在 Seed-TTS test-en 上 WER 为 2.17%，虽高于 Qwen3-TTS 的 1.24%，但其 RL 训练流程复杂且依赖偏好数据。Qwen3-TTS 的优势在于将控制信号直接嵌入语言建模任务，无需额外的 RL 阶段，这是否意味着在数据充足时，架构优化比后训练对齐更具效率，论文未给出直接对比。

从问题动机看，VIBEVOICE 采用 Next-Token Diffusion 解决长文本韵律漂移，而 Qwen3-TTS 坚持自回归路线。VIBEVOICE 在长文本 MOS 上为 3.71，Qwen3-TTS 在内部长文本测试中 WER 为 1.517。两者在长序列稳定性上的差异源于表示形式：VIBEVOICE 使用连续特征，Qwen3-TTS 使用离散 Token。离散 Token 的量化损失是否在长文本中导致韵律单调性，还是被 MTP 模块的并行解码所补偿，这一机制差异在现有基准中缺乏细粒度诊断。

## 总结

Qwen3-TTS 旨在解决自回归 TTS 中指令遵循精度与实时性延迟的矛盾。其切入点在于解耦语义建模与声学解码，通过双轨架构与多码本分词器，使声学生成不再严格依赖前序声学 Token 的完整序列。该方法在 Seed-TTS test-en 上实现 1.24% WER，并在 zh-to-ko 跨语言任务中将错误率降低约 66%。然而，实验显示 12Hz 分词器在长文本生成中 WER 升至 2.356，高于 25Hz 变体的 1.517，暴露了多码本低延迟设计在超长序列稳定性上的局限。当序列长度超过 10 分钟时，MTP 模块的并行解码是否足以抑制量化误差的累积，从而维持韵律的自然度，论文未提供进一步的消融证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15621)