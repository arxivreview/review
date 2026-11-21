# HuggingFace最新推荐论文 ｜VoXtream2: Full-stream TTS with dynamic speaking rate control ｜全流式零样本TTS中的动态语速控制

研究机构：瑞典皇家理工学院

作者：Nikita Torgashov、Gustav Eje Henter、Gabriel Skantze

论文原文见 [arXiv](https://arxiv.org/abs/2603.13518)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13518)

> 实时语音交互要求系统在文本逐词到达时即刻发声，同时保持语速随语义状态动态调整的能力。现有流式TTS架构要么牺牲低延迟换取离线精度，要么在流式模式下仅支持全局静态语速，无法响应句内认知负荷变化。VoXtream2通过分布匹配机制在帧级实时调整时长状态，结合无分类器引导增强音色克隆，在消费级GPU上实现74毫秒首包延迟与4倍实时速率。该方案验证了低延迟与细粒度时序控制的兼容性，但动态语速在极端速率下的可懂度衰减及离散Token表示对音色相似度的潜在限制仍存疑。

## 研究背景

实时对话代理依赖大语言模型（LLM）增量生成文本，文本转语音（TTS）系统必须在严格延迟约束下将流式文本转换为短波形块。这一场景要求TTS具备全流式（Full-Stream）能力，即在完整文本可用前开始生成语音，以最小化首包延迟（First-Packet Latency, FPL）。然而，自然人类语音的语速并非恒定，而是随思维组织、停顿插入及信息密度在句内动态波动。当前多数TTS系统隐含假设语速在整句内静态，仅支持粗粒度全局控制，导致合成语音缺乏自发交流的真实感。

全流式TTS与动态语速控制在实践中紧密耦合。实时交互不仅需要低延迟，还需要自适应韵律以反映对话状态的演变。随着文本逐Token展开，合适的语速可能动态变化，以镜像底层LLM传达的不确定性、强调或紧迫性。现有流式架构如CosyVoice2和Kyutai-TTS虽支持流式生成，但语速控制要么缺失，要么仅在话语级别保持恒定。这种静态建模与流式生成的双重局限，阻碍了合成语音向真正类人交互的演进。

VoXtream2针对这一缺口，提出一种全流式零样本TTS模型，支持在生成过程中实时修改语速。该模型利用分布匹配和分类器自由引导（Classifier-Free Guidance, CFG）实现帧级细粒度语速控制，同时通过提示文本掩码减少对声学提示转录的依赖。在标准零样本基准和专用语速测试集上，VoXtream2以更小的模型规模和更少的训练数据，取得了与最先进系统相当的客观和主观结果，并在消费级GPU上实现4倍实时速率与74毫秒FPL。

## 核心方法

### 全流式自回归架构参照系

VoXtream2基于VoXtream架构，采用自回归时间Transformer（Temporal Transformer, TT）预测语义和时长Token，深度Transformer（Depth Transformer, DT）预测声学Token。TT以音素Transformer（Phoneme Transformer, PT）输出和Mimi编解码器提取的12.5 Hz音频Token为条件，通过单调对齐将音素嵌入分配至对应音频帧。DT以TT输出嵌入、说话人嵌入和语义Token为条件，预测16个码本的声学Token。该架构的关键差异在于：TT联合建模语义与时长Token，DT冻结权重以复用预训练对话语音知识，且引入IPA字典支持多语言生成。

### 分布匹配动态语速控制

动态语速控制的核心在于实时调整时长Token的采样分布。TT输出为$N \times D$矩阵，其中$N$为Mimi词汇表大小，$D=6$为时长Token数。通过边缘化计算当前时长分布$P_{current}$，并与滑动窗口（过去3秒）内累积分布$P_{acc}$及目标分布$P_{target}$对比，更新当前步的时长分布：

$$P_{updated}(d) \propto P_{current}(d) \cdot \left( \frac{P_{target}(d)}{P_{acc}(d)} \right)^\beta$$

其中$\beta$控制控制强度，设为5以平衡质量与可懂度。该机制允许在生成过程中动态修改目标语速，实现句内平滑过渡。设计动机在于解决现有流式模型仅支持全局静态语速的局限，通过帧级分布匹配实现实时自适应，避免多轮推理或复杂重采样带来的延迟与可懂度损失。

### 提示文本掩码与CFG增强

提示文本掩码通过替换提示文本为<UNK> Token，强制模型仅依赖音频信号进行音色克隆，消除对外部音素对齐器的依赖。训练时随机掩码前3-10秒音频对应的文本Token，生成时每个声学帧分配单个<UNK> Token。CFG应用于文本、音频和说话人嵌入条件，其中TT使用$\gamma_{temp}=1.5$以允许韵律变化，DT使用$\gamma_{depth}=3.0$以精确控制音色。说话人嵌入权重增加50%以增强克隆效果。设计动机在于解决声学提示转录错误导致的初始状态偏差，以及CFG增强音色相似度时信号质量下降的问题。通过掩码减少提示内容敏感性，通过声学提示增强（Sidon模型）缓解噪声传播，实现无文本提示的鲁棒零样本克隆。

## 实验评估

实验在LibriSpeech-PC test-clean、SEED-TTS test-en和Emilia speaking-rate三个测试集上进行，基线包括CosyVoice2、VoiceStar、MaskGCT、Spark-TTS、Kyutai-TTS和F5-TTS。基线覆盖自回归与非自回归路线，但缺失WeSCon等情感控制基线，且限制在1B参数以内和200k小时训练数据以内，以确保公平比较。VoXtream2在SEED-TTS test-en上WER 1.32%、SPK-SIM 0.656、UTMOS 4.05，优于CosyVoice2的WER 2.27%和Kyutai-TTS的WER 1.34%，但SPK-SIM低于MaskGCT的0.691。在LibriSpeech-PC test-clean上，VoXtream2自然度68.8±2.3，显著高于其他模型，WER 2.12%与Kyutai-TTS的2.05%接近。

| 模型 | SEED-TTS WER (%) | SEED-TTS SPK-SIM | SEED-TTS UTMOS | LibriSpeech-PC Naturalness |
| :--- | :--- | :--- | :--- | :--- |
| VoXtream2 | 1.32 | 0.656 | 4.05 | 68.8±2.3 |
| CosyVoice2 | 2.27 | 0.658 | 4.16 | 66.2±2.5 |
| Kyutai-TTS | 1.34 | 0.670 | 3.69 | 65.6±2.4 |
| MaskGCT | 2.03 | 0.605 | 3.92 | 57.6±2.6 |

消融实验显示，CFG文本条件将WER从2.29%降至1.37%，CFG音频条件将SPK-SIM从0.578提升至0.661，但UTMOS从3.91降至3.65。增加说话人嵌入权重进一步提升SPK-SIM至0.679，但UTMOS降至3.56。最终加入声学提示增强后，UTMOS恢复至4.05，WER降至1.32%，SPK-SIM略降至0.656。动态语速控制实验中，S→N→F过渡的Pearson相关系数为0.701，WER 4.73%；F→N→S相关系数0.826，WER 11.25%，表明快速到慢速过渡的可懂度损失更大。

| 模型 | WER (%) | SPK-SIM | UTMOS |
| :--- | :--- | :--- | :--- |
| VoXtream | 3.16 | 0.529 | 3.88 |
| + CFG text | 1.37 | 0.578 | 3.91 |
| + CFG audio | 1.62 | 0.661 | 3.65 |
| + Prompt enhance. | 1.32 | 0.656 | 4.05 |

评估边界方面，指标涵盖WER、SPK-SIM、UTMOS和MUSHRA自然度，但缺乏韵律多样性或情感相似度指标。评估协议使用Whisper-largev3和HuBERT-based ASR，未报告置信区间。代码、预训练模型和音频示例公开，训练使用2×NVIDIA H200 GPU，28小时，10个epoch，超参数固定以确保可复现性。

## 关联研究分析

从问题动机看，VoXtream2聚焦流式场景下的动态语速控制，而WeSCon（Wang et al., 2025）实现词级情感控制但依赖两阶段自训练和教师模型，且未解决流式低延迟问题。WeSCon的细粒度控制通过动态语速与过渡平滑机制实现，但训练流程长且依赖外部对齐，而VoXtream2通过分布匹配在单阶段生成中实现帧级控制，无需额外训练阶段。这一差异源于任务特性：情感控制需语义-声学对齐，而语速控制仅需时长分布调整，后者在流式架构中更易集成。

从方法设计看，VoXtream2采用离散Token自回归架构，而F5-TTS（Zheng and Maleki, 2025）基于流匹配的非自回归架构，通过文本填充简化对齐，WER 0.020%显著优于VoXtream2的1.32%。F5-TTS的高WER优势源于连续特征生成无量化损失，但缺乏流式能力，无法支持实时交互。VoXtream2的离散Token在流式场景下因单调对齐和有限前瞻（25音素）导致WER劣势，但实现了74毫秒FPL，这是F5-TTS无法提供的。离散Token在流式场景下是否因量化损失导致SPK-SIM劣势，论文未给出定量分析。

## 总结

VoXtream2解决的核心矛盾是实时流式TTS中低延迟与动态语速控制的兼容性。现有流式架构如CosyVoice2和Kyutai-TTS仅支持全局静态语速，无法响应句内认知负荷变化，而离线模型虽支持细粒度控制但延迟过高。VoXtream2通过分布匹配机制在帧级实时调整时长状态，结合提示文本掩码和CFG增强音色克隆，在消费级GPU上实现74毫秒FPL与4倍实时速率。实验证明其在SEED-TTS test-en上WER 1.32%、SPK-SIM 0.656，动态语速控制相关系数达0.826，验证了低延迟与细粒度时序控制的兼容性。然而，动态语速在快速到慢速过渡时WER升至11.25%，表明极端速率下的可懂度衰减仍是瓶颈。当输入文本速率降至10 TPS且前瞻仅3音素时，WER升至5.11%，流式架构的上下文限制是否可通过更大前瞻或更复杂对齐机制缓解，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13518)