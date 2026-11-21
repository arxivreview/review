# HuggingFace最新推荐论文 ｜TimeChat-Captioner: Scripting Multi-Scene Videos with Time-Aware and Structural Audio-Visual Captions ｜全模态密集视频字幕生成

研究机构：北京大学、快手

作者：Linli Yao、Yuancheng Wei、Yaojie Zhang 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.08711)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08711)

> 密集视频字幕生成（Dense Video Captioning, DVC）旨在从长视频中定位事件并生成描述，但现有方法多局限于视觉模态或仅生成稀疏摘要，无法提供全模态、细粒度的时空监督信号。本文提出OmniDenseCaptioning任务，要求模型对视频进行连续场景分割，并生成覆盖六维结构（事件、背景、镜头、剪辑、对话、声学）的密集字幕。通过构建OmniDCBench基准、提出SodaM统一评估指标，以及训练TimeChat-Captioner-7B基线，本文验证了强化学习在时间-语义联合优化中的有效性。该工作填补了全模态密集字幕的空白，但基准规模与评估协议的泛化性仍存疑。

## 研究背景

当多模态大语言模型（MLLMs）处理长视频时，视觉与音频信号的时空对齐成为核心挑战。传统DVC任务（如Vid2Seq）将视频形式化为序列到序列问题，但仅关注视觉模态，忽略了音频中蕴含的丰富语义（如对话、环境音）。这种视觉主导的范式导致生成的字幕缺乏全模态覆盖，无法为MLLMs提供细粒度的跨模态对齐监督。

现有全模态字幕方法（如LongVALE）虽引入音频线索，但聚焦于显著事件识别与简短摘要，属于稀疏范式。这种设计遗漏了连续、细粒度的视听细节，难以捕捉深度全模态对齐所需的全面语义。同时，传统评估指标（如CIDEr）基于n-gram匹配，不适用于段落级、多维度的长描述，且无法处理场景边界模糊问题。本文切入点在于定义OmniDenseCaptioning任务，强制要求连续场景分割与六维结构化输出，并通过SodaM指标解决边界模糊与评估不匹配问题。

## 核心方法

### 任务定义与结构化输出

OmniDenseCaptioning任务要求模型将输入视频 $V$ 分割为连续场景，并为每个场景生成六维结构化字幕。设视频帧序列为 $F = \{f_1, ..., f_T\}$，音频信号为 $A = \{a_1, ..., a_T\}$，输出为场景级字幕序列 $C = \{(t_1, c_1), ..., (t_N, c_N)\}$，其中 $t_i$ 为时间戳，$c_i$ 包含事件、背景、镜头状态、剪辑风格、对话内容、声学线索六个维度。该设计动机在于解决现有方法仅生成稀疏事件摘要、缺乏全模态覆盖的问题，通过结构化schema确保字幕的“脚本式”完整性。

### SodaM统一评估指标

SodaM通过两阶段对齐策略联合评估时间戳精度与字幕质量。首先，利用IoU-based动态规划在 $(M, N)$ 场景网格中寻找最优对齐路径，其中 $M$ 和 $N$ 分别为预测与真值场景数。对齐公式为：

$$ \text{IoU}(t_{\hat{i}}, t_j) = \frac{|t_{\hat{i}} \cap t_j|}{|t_{\hat{i}} \cup t_j|} $$

该公式计算预测与真值时间戳的交并比，用于动态规划中的评分成本。当多个预测场景对齐到同一真值场景时，合并其字幕并扩展时间范围，形成单一合并预测。随后，对每个匹配对计算时间戳F1分数（阈值 $\{0.3, 0.5, 0.7, 0.9\}$）与CheckList字幕质量分数，最终SodaM为所有匹配对的F1分数平均。该设计解决了场景边界模糊导致的评估不匹配问题，将评估成本从 $O(MN)$ 降至 $O(K)$（$K \le N$）。

### TimeChat-Captioner训练框架

TimeChat-Captioner基于Qwen2.5-Omni骨干，采用两阶段训练：SFT与GRPO。SFT阶段使用40K合成样本学习任务格式，GRPO阶段使用2K样本优化时间-语义对齐。GRPO奖励函数包含格式、长度、时间戳精度与字幕质量四项，权重分别为0.5、0.5、1.0、1.0。时间戳奖励 $R_T$ 定义为预测与真值时间戳在最优对齐路径上的平均F1分数：

$$ R_T = \frac{1}{K} \sum_{k=1}^{K} \text{F1}(t_{\hat{k}}, t_{g_k}) $$

该公式直接优化时间边界准确性，解决SFT阶段时间戳token占比低（0.7%）导致梯度信号不足的问题。字幕质量奖励采用SodaM中的CheckList分数，由Gemini-2.5-Flash作为裁判模型评估预测字幕对真值原子元素的覆盖度。

## 实验评估

实验在OmniDCBench（1,122个人工标注样本）上进行，基线包括闭源模型（Gemini-2.5-Pro/Flash）与开源模型（Qwen2.5-Omni, MiniCPM-o-2.6, LongVALE等）。TimeChat-Captioner-7B-GRPO在SodaM指标上达到35.0，超越Gemini-2.5-Pro的30.0，且在多场景分割F1（61.2）与mIoU（69.6）上仅次于Gemini-2.5-Pro（68.5/74.9）。在下游任务Daily-Omni与WorldSense上，该模型分别达到52.8与22.6，显著优于开源基线。在Charades-STA时间接地任务上，R1@0.3达到79.8，高于Qwen2.5-Omni的78.3。

| 模型 | 多场景分割 F1 | 多场景分割 mIoU | SodaM (Avg.) |
|---|---|---|---|
| Gemini-2.5-Pro | 68.5 | 74.9 | 30.0 |
| TimeChat-Captioner-7B-SFT | 62.4 | 70.8 | 32.6 |
| TimeChat-Captioner-7B-GRPO | 61.2 | 69.6 | 35.0 |

消融实验显示，SFT数据量从20K增至40K时，SodaM从31.3提升至32.6；GRPO阶段引入时间戳奖励 $R_T$ 后，SodaM从32.5提升至35.0，表明时间-语义联合优化对性能提升贡献显著。

评估边界方面，OmniDCBench仅1,122样本，统计显著性有限；SodaM依赖Gemini-2.5-Flash作为裁判模型，存在评估偏差风险；代码与数据已开源，但GPU配置（32×80G）限制了复现性。

## 关联研究分析

从问题动机看，本文与LongVALE同属全模态字幕生成，但LongVALE聚焦显著事件识别与简短摘要，属于稀疏范式；本文要求连续场景分割与六维结构化输出，属于密集范式。这一差异源于任务目标不同：LongVALE旨在快速定位关键事件，而本文旨在提供全模态、细粒度的监督信号。从方法设计看，本文与Vid2Seq同属序列到序列形式化，但Vid2Seq仅处理视觉模态，本文扩展至音频-视觉联合输入。本文未采用检索增强生成（RAG），而是通过GRPO强化学习内化知识，这与领域共识中RAG提升事实一致性的做法形成对比。无RAG情况下，长视频事实一致性如何保证，论文未给出明确回答。

## 总结

本文要解决的核心矛盾是全模态密集字幕生成中时间边界模糊与评估指标不匹配的问题。现有方法要么局限于视觉模态，要么生成稀疏摘要，无法提供全模态、细粒度的时空监督信号。本文通过定义OmniDenseCaptioning任务、构建OmniDCBench基准、提出SodaM指标，以及训练TimeChat-Captioner-7B基线，验证了强化学习在时间-语义联合优化中的有效性。实验表明，TimeChat-Captioner-7B-GRPO在SodaM指标上达到35.0，超越Gemini-2.5-Pro的30.0，且在下游任务上表现优异。本文的边界在于OmniDCBench规模有限（1,122样本），SodaM依赖外部裁判模型，且未探索RAG与RL的协同作用。当支持集增大到更大规模时，SodaM的评估稳定性与GRPO奖励的泛化性是否保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08711)