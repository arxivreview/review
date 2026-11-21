# ACL2026最新论文 ｜TagSpeech: End-to-End Multi-Speaker ASR and Diarization with Fine-Grained Temporal Grounding ｜TagSpeech：基于交错时间锚点的端到端多说话人ASR与分离

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国约翰斯·霍普金斯大学

作者：Mingyue Huo、Yiwen Shao、Yuheng Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2601.06896)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06896)

> 多说话人语音处理的核心挑战在于同时解决“谁在何时说了什么”，即语义转录、说话人归属与细粒度时间定位的联合解耦。现有LLM-based方法虽能生成带说话人标签的文本，但普遍缺乏显式时间戳预测能力，导致无法通过标准分离误差率（DER）评估，且在重叠语音下存在时间线性化偏差。TagSpeech通过引入交错数值时间锚点机制与双编码器解耦架构，在冻结LLM骨干的前提下实现了显式时间接地。该方法在AMI和AliMeeting上显著降低了DER，但cpWER仍高于分离条件化ASR基线，其时间锚点机制对语义连贯性的潜在干扰尚需进一步验证。

## 研究背景

多说话人语音处理要求模型在复杂声学干扰下同时输出转录文本、说话人身份及精确时间边界。传统级联流水线将语音活动检测、分离、识别与聚类解耦，但误差累积导致重叠语音处理失效。端到端神经说话人分离（EEND）将分离建模为帧级多标签分类，解决了固定说话人数量限制，但无法处理长音频中的身份漂移。EEND-VC框架结合局部EEND与全局向量聚类，成为处理任意说话人数量与长音频一致性的主流基线。随着大型音频语言模型（Large-Audio Language Models, LALMs）的兴起，研究重心转向利用语义推理能力实现联合ASR与分离，但现有LLM方法多聚焦于“谁说了什么”，忽略了“何时说”的显式时间定位，导致无法进行精确的时序对齐评估。

本文切入点在于解决LLM在连续语音信号与离散语义token之间的粒度失配问题。现有LALM缺乏将毫秒级语音帧映射到绝对时间戳的内在机制，导致在重叠区域产生时间线性化偏差，即强制序列化同时发生的事件。TagSpeech通过引入显式时间锚点与双编码器解耦，弥补了这一缺陷，实现了语义、说话人与时间的统一建模。

## 核心方法

### 方法参照系

本文问题属于LLM-based端到端联合识别路线，与DiCoW等分离条件化ASR方法的关键差异在于：后者利用外部分离掩码调制声学编码器，而本文直接在LLM解码过程中显式预测时间戳，无需外部分离模块。

### 双编码器解耦与SOT微调

标准ASR编码器如Whisper缺乏建模重叠语音动态的能力，导致语义与说话人信息在单一表示空间中纠缠。本文采用双Zipformer编码器架构，将Melspectrogram特征$M \in \mathbb{R}^{[T] \times [80]}$分别输入语义编码器与说话人编码器，生成解耦表示$H_{sem}, H_{spk} \in \mathbb{R}^{[T'] \times [D_{enc}]}$。语义编码器通过序列化输出训练（Serialized Output Training, SOT）微调，将参考转录重组为以说话人变化token $\langle sc \rangle$ 分隔的时序序列，使编码器捕捉轮替动态。这一设计解决了单一编码器在共享表示空间中语义与说话人信息相互干扰的问题，显著降低了下游LLM对重叠语音的理解负担。

### 交错数值时间锚点机制

LLM解码器缺乏对连续语音帧的绝对时间感知，导致时间定位依赖隐式推理，在重叠区域失效。本文引入交错数值时间锚点机制，定义函数$F_{anc}(\cdot; m)$将离散数值token集合$A \subset V_{LLM}$以固定间隔$m$帧注入特征序列，生成时间接地表示$Z_{sem}, Z_{spk} \in \mathbb{R}^{[L'] \times [D_{LLM}]}$，其中$L' = L + \lfloor L/m \rfloor + 1$。该机制利用LLM固有的数值推理能力，无需扩展词表或修改架构，同时作为语义流与说话人流的同步信号。相比文本锚点（如`<time=0.16s>`），数值锚点仅需1-2个预缓存整数token，计算成本更低，且能自然扩展至长音频。

## 实验评估

实验在AMI（英语）与AliMeeting（中文）远场子集上进行，基线覆盖Gemini-2.0、Qwen-2.5-Omni-7B、Qwen-3.0-Omni-30B等LLM端到端系统及Pyannote 3.1 + Whisper-large-v3级联系统。缺失DiCoW等分离条件化ASR基线，限制了与声学条件化路线的直接对比。

| 模型 | AMI-SDM Fail Rate↓ | AMI-SDM DER↓ | AMI-SDM cpWER↓ | AliMeeting-Far Fail Rate↓ | AliMeeting-Far DER↓ | AliMeeting-Far cpCER↓ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Gemini-2.0-flash | 2.11 | 45.16 | 36.24 | 31.90 | 50.35 | 59.02 |
| Qwen2.5-Omni-7B | 4.07 | 34.71 | 49.86 | 6.40 | 37.42 | 41.23 |
| Qwen3.0-Omni-30B | 2.15 | 39.06 | 38.83 | 0.39 | 34.60 | 33.69 |
| Pyannote 3.1 + Whisper | 4.60 | 23.05 | 43.57 | 2.52 | 26.13 | 46.56 |
| TagSpeech (Ours) | 1.27 | 24.84 | 42.55 | 3.04 | 22.13 | 33.84 |

TagSpeech在AMI上DER为24.84%，优于所有LLM基线，但略高于Pyannote级联系统的23.05%；在AliMeeting上DER为22.13%，优于Pyannote的26.13%。cpWER方面，TagSpeech在AMI上为42.55%，低于Pyannote的43.57%，但显著高于据领域综述中SA-DiCoW的18.6%。

消融实验显示，单编码器架构（如WavLM-Large）导致Fail Rate高达21.94%，而双编码器SOT-FT架构将Fail Rate降至1.27%，DER从30.94%降至24.84%。时间锚点粒度分析表明，间隔8帧时DER与cpWER达到平衡，间隔过密（1-4帧）导致语义连贯性下降，间隔过疏（≥16帧）导致DER上升。

评估协议采用0ms collar的DER，严格捕捉时间戳精度，但缺乏置信区间报告。代码已开源，但训练数据规模较小（AMI 65小时，AliMeeting 103小时），限制了泛化性评估。推理延迟受自回归生成限制，虽支持分块推理，但仍落后于优化后的级联系统。

## 关联研究分析

从问题动机看，TagSpeech与DiCoW代表了多说话人ASR的两条不同路线：DiCoW利用外部分离掩码调制声学编码器，依赖分离模块的精度，误差传递风险高；TagSpeech通过时间锚点直接接地时间，无需外部分离，但cpWER较高。这一差异源于任务特性：DiCoW聚焦于重叠语音下的识别鲁棒性，而TagSpeech强调显式时间定位，两者在计算效率与时间精度间做出了不同取舍。

从方法设计看，TagSpeech与Sortformer均试图解决时间对齐，但机制不同：Sortformer基于到达时间排序，属于隐式时间建模；TagSpeech通过显式数值锚点，利用LLM数值推理能力，避免了词表扩展。与SpeakerLM等LLM方法相比，TagSpeech显式预测时间戳，而后者仅输出说话人归属文本，无法进行DER评估。这种差异暗示，显式时间锚点可能是LLM实现细粒度时间定位的必要条件，而非可选优化。

## 总结

TagSpeech解决的核心矛盾是LLM在连续语音信号与离散语义token之间的粒度失配，导致时间定位失效。其切入点在于利用LLM固有的数值推理能力，通过交错数值时间锚点实现显式时间接地，同时通过双编码器解耦避免语义与说话人信息纠缠。实验证明，该方法在AMI上DER为24.84%，在AliMeeting上为22.13%，显著优于Gemini-2.0与Qwen-Omni等LLM基线。然而，其cpWER（AMI 42.55%）仍高于分离条件化ASR基线，且训练数据规模较小，泛化性未充分验证。当时间锚点间隔进一步缩小至4帧以下时，语义连贯性下降是否可通过更复杂的锚点编码策略缓解，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06896)