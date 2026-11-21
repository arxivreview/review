# ICLR2026最新论文 ｜DRVOICE: PARALLEL SPEECH-TEXT VOICE CON VERSATION MODEL VIA DUAL-RESOLUTION SPEECH REPRESENTATIONS ｜双分辨率语音表示的并行语音-文本对话模型

研究机构：阿里巴巴集团

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66180065)

> 端到端语音生成模型面临语音令牌高频（25Hz）与文本令牌低频（~3Hz）的时序失配，导致语义稀释与计算冗余。现有并行架构如Moshi虽实现模态交互，但高频输入阻碍了大语言模型核心能力的充分利用。DRVOICE通过双分辨率机制将LLM输入压缩至5Hz，并引入语音精化头恢复细粒度声学细节，在保持SOTA性能的同时降低近50%训练算力。该方案在通用基准上表现优异，但缺乏对全双工动态交互能力的验证。

## 研究背景

离散语音令牌是连接音频信号与大语言模型（LLM）的关键接口。语义令牌（Semantic Tokens）相比声学令牌更利于对齐文本语义，但其采样率通常远高于文本令牌。这种频率差异导致LLM在处理语音序列时，大量计算资源被用于处理高频冗余信息，而非语义推理。

当前端到端语音模型主要分为文本驱动与联合语音-文本两类。文本驱动模型如Qwen2.5-Omni采用Thinker-Talker架构，文本生成先于语音合成，导致LLM无法感知语音生成状态，限制了副语言信息的表达。联合模型如Moshi和Kimi-Audio通过并行或交错解码实现模态交互，但Kimi-Audio使用12.5Hz音频表示，仍远高于文本的~3Hz频率。这种频率失配不仅增加了计算成本，还稀释了语义信息，阻碍了LLM核心能力的发挥。DRVOICE针对这一瓶颈，提出双分辨率语音表示（Dual-Resolution Speech Representations, DRSR），在理解阶段将25Hz语音令牌分组为5Hz表示，在生成阶段通过专用头部恢复原始分辨率，从而在效率与质量间取得平衡。

## 核心方法

### 并行联合语音-文本建模参照系

DRVOICE基于Moshi的并行架构，但核心差异在于模态对齐策略。Moshi直接处理高频语音令牌，而DRVOICE在LLM输入端引入分组机制，将语音与文本在时间分辨率上对齐。这种设计保留了自回归生成的统一框架，同时解决了频率失配问题。

### 双分辨率语音表示机制

设计动机在于解决25Hz语音令牌与~3Hz文本令牌之间的时序失配，避免高频语音令牌稀释LLM的语义处理能力。DRVOICE在理解阶段采用分组机制，将$k$个连续语音令牌拼接为一个组表示：

$$ \mathbf{g}_j = \mathbf{s}_{jk} \parallel \mathbf{s}_{jk+1} \parallel \cdots \parallel \mathbf{s}_{jk+k-1} $$

其中$\parallel$表示特征拼接，$k$为分组因子（本工作中$k=5$，将25Hz降至5Hz）。该组表示作为LLM的输入嵌入，与文本嵌入相加形成混合输入：

$$ \mathbf{c}_t = E_{\text{speech}}(\mathbf{g}_t) + E_{\text{text}}(\mathbf{t}_t) $$

这一设计将LLM处理的语音序列长度压缩为原来的$1/k$，显著降低了计算开销，同时使语音与文本在时间尺度上对齐，便于LLM捕捉跨模态语义关联。

### 语音精化头与解分组生成

设计动机在于分组过程不可避免地丢失细粒度声学细节，直接预测组内多个令牌会导致语音质量下降。DRVOICE引入语音精化头（Speech Refined Head, SRH），利用共享LLM层的隐藏状态$\mathbf{h}$进行解分组。首先将$\mathbf{h}$线性投影并时间分割为$k$个子向量：

$$ \mathbf{H} = [\mathbf{h}_{ug[1]}, \mathbf{h}_{ug[2]}, \ldots, \mathbf{h}_{ug[k]}] $$

SRH以$\mathbf{H}$和先前语音令牌为条件，自回归地生成单个语音令牌：

$$ P(\mathbf{s}_i | \mathbf{s}_{<i}, \mathbf{H}) = \text{Softmax}(W_{\text{SRH}} \mathbf{h}_{\text{SRH}}) $$

其中$\mathbf{h}_{\text{SRH}}$聚合了上下文信息。这种“先粗后细”的两阶段生成策略，既利用了LLM的语义理解能力，又通过SRH恢复了声学细节，避免了传统分组方法在生成任务中的性能损失。

## 实验评估

DRVOICE在OpenAudioBench、VoiceBench、UltraEval-Audio和Big Bench Audio四个基准上均取得SOTA。基线覆盖文本驱动（MiniCPM-o 2.6, Qwen2.5-Omni）与联合模型（GLM-4-Voice, Kimi-Audio, Baichuan-Omni-1.5, Step-Audio2-Mini），但未包含全双工专用模型如Moshi的完整对比。

| 基准 | 指标 | DRVOICE | Kimi-Audio | Qwen2.5-Omni |
| :--- | :--- | :--- | :--- | :--- |
| OpenAudioBench | Overall | **72.04** | 69.08 | 66.34 |
| VoiceBench | Overall | **80.17** | 76.93 | 72.83 |
| UltraEval-Audio | Overall | **56.66** | 42.79 | 50.46 |
| Big Bench Audio | Overall | **74.0** | 55.2 | 53.9 |

DRVOICE在语音理解与生成任务上全面领先，尤其在推理类任务（VoiceBench IFEval 71.39）上优势明显，表明双分辨率机制有效保留了LLM的推理能力。

消融实验显示，移除SRH导致S2M任务性能从68.67降至21.67，证明SRH对语音生成质量至关重要。移除CoM-Mixing训练策略后，S2T性能从72.33降至58.00，表明链式模态推理对文本-语音对齐有显著贡献。SRH预训练缺失导致S2M性能降至38.33，说明专用预训练对语音生成稳定性不可或缺。

评估边界方面，DRVOICE未在Full-Duplex-Bench或τ-Voice等全双工基准上测试，无法验证其在轮替、中断处理等动态交互场景中的表现。代码与模型权重已开源，但5Hz输入频率是否足以捕捉毫秒级全双工动态，论文未提供证据。

## 关联研究分析

从方法设计看，DRVOICE与Moshi同属并行联合建模，但Moshi直接处理12.5Hz语音令牌，而DRVOICE通过分组降至5Hz。这一差异源于任务目标的不同：Moshi侧重实时流式对话，需保留高频细节以支持低延迟；DRVOICE侧重通用语音理解与生成，优先优化LLM语义能力。DRVOICE的SRH通过解分组恢复细节，弥补了频率降低带来的质量损失，但这一机制是否适用于需要严格时序同步的全双工场景，尚不明确。

从问题动机看，DRVOICE与Kimi-Audio均针对频率失配问题，但Kimi-Audio采用双令牌器（离散+连续）保留声学信息，而DRVOICE采用单一语义令牌加SRH。Kimi-Audio的方案在声学保真度上可能更优，但计算成本更高；DRVOICE通过分组与解分组实现效率与质量的平衡，但依赖SRH的自回归生成，可能增加推理延迟。两种方案在效率与质量间的取舍，反映了不同应用场景下的设计偏好。

## 总结

DRVOICE旨在解决端到端语音模型中语音与文本令牌的频率失配问题，通过双分辨率机制将LLM输入降至5Hz，并利用SRH恢复声学细节。该方法在OpenAudioBench（72.04）和VoiceBench（80.17）上取得SOTA，证明其在通用语音任务上的有效性。然而，论文未评估全双工动态交互能力，5Hz输入频率是否足以支持毫秒级轮替与中断处理，缺乏实验验证。当应用于实时全双工对话时，DRVOICE的分组机制是否会引入不可接受的延迟，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66180065)