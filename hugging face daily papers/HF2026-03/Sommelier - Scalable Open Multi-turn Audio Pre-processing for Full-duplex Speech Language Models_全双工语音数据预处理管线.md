# HuggingFace最新推荐论文 ｜Sommelier: Scalable Open Multi-turn Audio Pre-processing for Full-duplex Speech Language Models ｜全双工语音数据预处理管线

研究机构：韩国科学技术院

作者：Kyudan Jung、Jihwan Kim、Soyoon Kim 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25750)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25750)

> 全双工语音对话模型（Full-Duplex Speech Language Models, SLMs）的训练受限于高质量多说话人对话数据的稀缺，现有大规模语料多为单流录音，无法提供重叠语音与回授行为的监督信号。本文切入点在于构建一条可扩展的开源数据预处理管线，将野外录音转化为保留对话动态的双通道训练语料。该管线通过集成说话人分离、重叠语音解混与多模型ASR投票，解决了传统级联处理中分离错误与转录幻觉累积的问题。其价值在于验证了83小时处理后数据即可提升Moshi模型的交互指标，但数据规模对模型泛化能力的长期影响仍存疑。

## 研究背景

全双工交互要求模型在生成响应的同时持续监听用户输入，这要求训练数据必须包含真实的说话重叠（Overlap）与回授（Backchanneling）动态。然而，现有大规模语音数据集如LibriSpeech或GigaSpeech主要面向单说话人识别，缺乏说话人分离标注，直接用于全双工训练会导致模型无法学习轮替边界与中断处理逻辑。为解决此问题，研究界尝试从播客或广播录音中挖掘多说话人片段，但原始音频中的背景噪声、音乐及非对话区域会严重干扰下游模型的语义理解。

传统数据构建流程依赖自动语音识别（ASR）与说话人日志（Speaker Diarization）的级联，但这一路径存在两个核心瓶颈：一是标准日志模型（如Pyannote）对短促回授与快速轮替的边界检测精度不足，导致重叠区域被错误截断或归属；二是单一ASR模型在静音或噪声片段中易产生重复性幻觉（Hallucination），将错误文本标签注入训练集，使下游模型模仿这些病态行为。Sommelier管线针对这两个失效点，通过引入更鲁棒的日志模型与多模型集成策略，在保留对话原始动态的前提下提升了数据质量。

## 核心方法

### 方法参照系

标准语音数据预处理流程通常包含音频标准化、静音切分、说话人日志、ASR转录四个阶段。本文的关键差异在于不剥离重叠语音，而是将其作为全双工训练的核心信号保留，并针对重叠区域引入双说话人分离与身份匹配模块，以解决级联误差在重叠场景下的放大效应。

### 重叠语音分离与身份匹配

传统日志模型将重叠区域视为噪声或错误归属，导致训练数据丢失关键交互信息。Sommelier采用Sortformer替代Pyannote 3.1，因其对短促语音与快速轮替的边界检测更鲁棒。对于重叠区间，管线提取非重叠部分生成说话人嵌入参考向量，并将重叠音频输入SepReformer分离模型，通过余弦相似度匹配候选语音与参考向量，实现身份归属：

$$
S_i = \cos\left(\text{Emb}(a_{\text{cand},i}), \text{Emb}(a_{\text{ref},i})\right)
$$

该公式计算分离候选语音与参考嵌入的相似度，确保重叠语音被正确分配至对应说话人通道。这一设计解决了传统方法中重叠区域被单侧归属导致的ASR混淆问题，使模型能同时学习两个说话人的并行语音流。

### 集成ASR与幻觉过滤

单一ASR模型在低信噪比片段中易产生重复性幻觉，污染训练标签。Sommelier采用Recognizer Output Voting Error Reduction (ROVER) 策略，集成Whisper、Canary与Parakeet三个模型，通过词级对齐与多数投票生成最终转录：

$$
\text{Word}_{\text{final}} = \begin{cases} \text{Word}_{\text{majority}} & \text{if } \text{count}(\text{Word}) \geq 2 \\ \text{Word}_{\text{Whisper}} & \text{otherwise} \end{cases}
$$

该机制通过模型多样性抑制单模型幻觉，辅以n-gram重复过滤器（n=15, count≥5）剔除病态样本。这一设计解决了单一ASR在噪声环境下的转录不稳定问题，确保训练标签的语义一致性。

## 实验评估

实验在VoxConverse、LibriSpeech与TEDLIUM3上评估组件性能，并在Full-Duplex-Bench 1.0上验证数据效用。基线覆盖Pyannote 3.1、Whisper-large-v3与Moshi，但缺乏与其他全双工数据管线（如DuplexChat-Pipe）的直接对比。

| 指标 | Pyannote 3.1 | Sortformer |
| :--- | :--- | :--- |
| DER (%) | 8.40 | 7.16 |
| JER (%) | 17.68 | 14.69 |
| RTF | 0.051 | 0.006 |

| 数据集 | Whisper WER (%) | MoE WER (%) |
| :--- | :--- | :--- |
| LibriSpeech Test Other | 6.26 | 3.92 |
| TEDLIUM3 Test | 12.19 | 10.66 |

Sortformer在DER与JER上均优于Pyannote，尤其在短语音与轮替区域表现更鲁棒。集成ASR在LibriSpeech Test Other上将WER从6.26%降至3.92%，降幅约37%，验证了多模型投票对噪声鲁棒性的提升。

在Full-Duplex-Bench 1.0上，使用Sommelier处理83小时数据微调Moshi后，Backchanneling指标从0.985提升至1.000，Smooth Turn-Taking从1.000保持至1.000，User Interruption从0.941提升至1.000。Pause Handling指标无显著变化，作者归因于Moshi架构限制或缺乏提示音频。延迟指标从0.257增至1.065，作者解释为模型从“持续说话”转变为“主动处理用户输入”的正向信号。

评估边界方面，实验未报告置信区间，且83小时数据规模是否足以代表大规模数据效用未明确验证。管线在A100上RTF为0.1746，处理10,000小时音频需约55小时，计算可行性已验证，但代码与超参数细节仅在附录中提供，可复现性依赖开源仓库完整性。

## 关联研究分析

从问题动机看，Sommelier与DuplexChat-Pipe均针对全双工数据稀缺问题，但前者聚焦于野外录音的清洗与分离，后者侧重合成数据生成。Sommelier保留真实对话的动态噪声与交互模式，而合成数据虽规模占优但分布偏差难以消除。这一差异源于任务特性：真实录音中的重叠与回授具有不可预测性，合成数据难以完全模拟，但真实数据的隐私成本与处理复杂度更高。

从方法设计看，Sommelier采用Sortformer与ROVER集成，而Moshi等模型依赖大规模无监督预训练。Sommelier的模块化设计允许研究者调整数据纯度与对话真实性的权衡，而端到端模型将数据质量内化于训练过程。这一差异暗示数据预处理与模型架构的耦合程度：Sommelier作为前置管线，其输出质量直接决定下游模型的上限，而端到端模型可通过架构创新部分弥补数据缺陷。

## 总结

Sommelier解决的核心矛盾是全双工训练数据中重叠语音的保留与转录质量的平衡。其切入点在于通过模块化管线分离数据清洗与模型训练，利用Sortformer与ROVER集成解决级联误差累积问题。实验证明83小时处理后数据即可提升Moshi的Backchanneling与Interruption指标至1.000，但Pause Handling无改善，暴露了数据管线对模型架构限制的依赖。当数据规模从83小时扩展至万小时级时，管线中ASR集成与分离模块的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25750)