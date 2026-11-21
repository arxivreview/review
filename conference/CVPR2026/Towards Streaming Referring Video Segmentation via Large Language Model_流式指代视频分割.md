# CVPR2026最新论文 ｜Towards Streaming Referring Video Segmentation via Large Language Model ｜流式指代视频分割

研究机构：东南大学、阿里巴巴集团

作者：Wenkang Zhang、Kaicheng Yang、Xiang An 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e887efcd7ca3)

> 指代视频分割（Referring Video Object Segmentation, RVOS）要求模型根据自然语言描述在视频流中实时定位目标像素，传统离线方法依赖关键帧采样与掩码传播，无法处理无限视频流的因果约束。现有 MLLM 分割框架因逐帧独立处理导致语义断裂，或因全量输入导致显存溢出，难以兼顾实时性与时间一致性。本文提出 StreamingRVOS，通过语义嵌入回收（Semantic Embedding Recycling, SER）与在线掩码一致性感知（Online Mask Consistency Perception, OMCP）实现流式逐帧分割。该方法在 MeViS 数据集上较基线提升 19.2%，但 FIFO 队列的语义污染机制限制了长程依赖的捕捉能力。

## 研究背景

指代视频分割任务中，模型需根据语言描述 $R$ 对视频帧序列 $I_{1:T}$ 生成目标掩码 $M_{1:T}$。多模态大语言模型（MLLMs）通过引入特殊分割令牌 [SEG] 连接语言理解与像素预测，但视频场景下帧间语义的连续性与计算效率构成核心矛盾。若逐帧独立调用 MLLM，冗余计算导致推理延迟激增；若丢弃历史帧信息，则产生时间遗忘，表现为掩码的突变与不一致。

当前 MLLM-based RVOS 主流路线采用“采样-分割-传播”范式：先提取稀疏关键帧进行图像级分割，再利用分割助手（如 SAM2）将掩码传播至全视频。该范式存在预处理约束与优化割裂，且依赖完整视频访问，无法适配流式场景。VRS-HQ 等改进方法虽引入时序动态聚合，仍受限于离线采样策略。StreamingRVOS 的切入点在于消除采样环节，将视频作为逐帧图像序列直接输入 MLLM，通过轻量级语义压缩机制替代全量上下文，实现无预处理的流式分割。

## 核心方法

### 方法参照系

本文问题属于 MLLM 指代分割的视频扩展。标准流程为：MLLM 处理图像与描述生成 [SEG] 令牌，分割助手（SA）解码掩码。关键差异在于：本文摒弃关键帧采样，要求模型在严格因果约束下逐帧处理无限视频流，且需动态决定何时重新调用 MLLM 以更新语义状态。

### 语义嵌入回收（SER）

SER 机制解决逐帧独立处理导致的上下文碎片化问题。传统方法中，[SEG] 令牌仅编码当前帧前景信息，帧间语义断裂。SER 将前帧生成的 [SEG] 令牌作为 [INFO] 令牌，封装在 [context] 与 [/context] 标记中，作为当前帧 MLLM 输入的组成部分。

$$
\text{Input}_i = \begin{cases} I_i + R, & \text{if } i = 1 \\ I_i + R + [\text{INFO}], & \text{otherwise} \end{cases}
$$

该公式表明，从第二帧起，MLLM 输入包含当前帧图像 $I_i$、描述 $R$ 及前帧语义嵌入 [INFO]。[INFO] 作为前帧前景信息的浓缩表示，使 MLLM 在感知当前帧时能利用历史语义，维持掩码的时间连贯性。SER 采用 FIFO 队列存储 [INFO] 嵌入，避免显存线性增长，但队列长度固定（实验中 $n=1$ 至 $3$），长程依赖信息可能被新帧覆盖。

### 在线掩码一致性感知（OMCP）

OMCP 策略解决逐帧调用 MLLM 的计算冗余问题。传统流式方法要么每帧都调用 MLLM（高延迟），要么固定间隔调用（可能错过语义突变）。OMCP 通过评估当前掩码质量与连续性，自适应决定是否重新调用 MLLM。

$$
\text{OMCP} = (P_i > \tau_1) \land (P_c > \tau_2)
$$

其中 $P_i$ 为当前帧掩码预测置信度（复用 SA 的预测 IoU），$P_c$ 为当前帧与前一帧掩码的一致性：

$$
P_c = \frac{|M_i \cap M_{i-1}|}{|M_i \cup M_{i-1}|}
$$

当 $P_i$ 或 $P_c$ 低于阈值 $\tau_1, \tau_2$ 时，触发 MLLM 重新调用，并附加指令引导其关注上下文信息以更新 [SEG] 令牌。该机制将“何时计算”形式化为基于掩码状态的决策问题，在语义稳定时跳过 MLLM 调用以降低延迟，在语义突变时及时修正以维持准确性。

## 实验评估

实验在 Ref-DAVIS、Ref-YouTube-VOS、MeViS、ReVOS 四个 RVOS 基准及 RefCOCO 系列 RES 基准上进行。基线覆盖 MLLM-based（VRS-HQ, GLUS, Sa2VA）与 SAM-based（SAMWISE, AL-Ref-SAM2）路线，但缺乏最新流式专用分割基线的对比。

| 方法 | Ref-DAVIS J&F | Ref-YouTube-VOS J&F | MeViS J&F | ReVOS J&F |
| :--- | :--- | :--- | :--- | :--- |
| VRS-HQ-7B | 76.0 | 70.4 | 50.6 | 62.1 |
| Sa2VA-4B | 73.8 | 70.0 | 46.2 | 59.8 |
| StreamingRVOS-1B | 76.4 | 69.1 | 49.7 | 59.7 |
| StreamingRVOS-4B | 76.6 | 70.5 | 50.9 | 63.0 |

StreamingRVOS-4B 在 Ref-DAVIS 上以 76.6 的 J&F 超越 VRS-HQ-7B 的 76.0，在 MeViS 上以 50.9 超越 VRS-HQ-7B 的 50.6，验证了流式范式在精度上的竞争力。1B 模型在 MeViS 上较 Sa2VA-1B 提升 19.2%（49.7 vs 41.7），表明 SER 机制对小模型增益显著。

| 策略 | Ref-DAVIS J&F | MeViS J&F | ReVOS J&F | FPS |
| :--- | :--- | :--- | :--- | :--- |
| First frame | 70.8 | 54.4 | 56.5 | 8.9 |
| Every 1 frame | 75.4 | 59.2 | 58.9 | 3.4 |
| Every 5 frames | 75.2 | 59.0 | 59.3 | 6.7 |
| OMCP | 76.4 | 59.5 | 59.7 | 6.7 |

消融实验显示，OMCP 策略在 Ref-DAVIS 上较固定间隔（Every 5 frames）提升 1.2 点 J&F，且 FPS 与固定间隔持平（6.7），优于逐帧调用（3.4 FPS）。[INFO] 令牌数量 $n$ 从 1 增至 3 时，MeViS J&F 从 58.5 微降至 58.2，ReVOS 从 58.9 降至 60.1 后回升，表明 FIFO 队列中语义令牌存在污染效应，增加令牌数未带来显著增益。

评估指标涵盖 J、F、J&F 及 FPS，但缺乏对极端动态场景下延迟尖峰的细粒度分析。代码已开源，超参数（$\lambda_{bce}, \lambda_{dice}, \lambda_{txt}, \lambda_{mask}$）均设为 1，训练使用 1×A800 GPU。

## 关联研究分析

从问题动机看，StreamingRVOS 与知识库中“内存管理与压缩”路线的 StreamingVLM 存在本质差异。StreamingVLM 采用注意力沉没（Attention Sink）与连续 RoPE 处理无限文本流，其记忆载体为全量 KV 缓存；而本文用 [INFO] FIFO 队列替代 KV 缓存，将视觉语义压缩为单一令牌。这一差异源于任务特性：文本流需保留细粒度 token 以支持长程推理，而分割任务仅需前景语义的连贯性，[INFO] 的语义压缩足以维持掩码一致性。然而，FIFO 队列的固定长度可能丢失长程依赖，当目标在视频中长时间消失后重现时，[INFO] 是否仍能准确召回历史语义，论文未提供证据。

从方法设计看，OMCP 的自适应触发机制与知识库中“主动响应”路线的 VST 形成对比。VST 利用查询前的流式间隔进行自回归文本推理，其决策依据为文本语义的完整性；而 OMCP 的决策依据为掩码的 IoU 与一致性，属于像素级反馈。这种差异导致 OMCP 对语义歧义（如目标被遮挡但掩码仍连续）的鲁棒性可能不足，因为掩码一致性无法捕捉语义层面的变化。VST 的双记忆系统（短期视觉+长期文本）在长程推理上更具优势，但引入了额外的自回归计算开销，而 OMCP 通过复用 SA 的预测 IoU 避免了额外模块，计算效率更高。

## 总结

StreamingRVOS 解决的核心矛盾是流式分割中语义连贯性与计算效率的冲突。现有离线采样方法无法处理无限视频流，而逐帧独立调用 MLLM 导致延迟激增。本文通过 SER 将前帧 [SEG] 令牌作为 [INFO] 输入，维持语义连贯；通过 OMCP 基于掩码一致性自适应触发 MLLM 调用，平衡精度与延迟。实验证明，4B 模型在 Ref-DAVIS 上以 76.6 J&F 超越 VRS-HQ-7B，1B 模型在 MeViS 上较 Sa2VA 提升 19.2%。然而，FIFO 队列的语义污染效应限制了长程依赖的捕捉，[INFO] 令牌数量增加未带来性能提升。当目标在视频中经历长时间遮挡或场景剧烈变化后，[INFO] 队列中的语义嵌入是否仍能准确引导分割，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e887efcd7ca3)