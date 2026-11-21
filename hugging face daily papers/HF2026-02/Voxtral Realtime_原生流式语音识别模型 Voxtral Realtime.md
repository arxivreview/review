# HuggingFace最新推荐论文 ｜Voxtral Realtime ｜原生流式语音识别模型 Voxtral Realtime

作者：Mistral-AI、:、Alexander H. Liu 等 169 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.11298)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.11298)

> 实时语音交互要求系统在音频流式到达时即时输出文本，而离线模型依赖双向声学上下文，直接分块处理会导致训练与推理分布不匹配，在低延迟下精度显著退化。现有原生流式架构虽能缓解此问题，但在亚秒级延迟下难以达到离线精度，尤其在多语言场景。本文提出 Voxtral Realtime，通过因果音频编码器与自适应延迟条件化机制，使单一模型在 80ms 至 2400ms 任意延迟下运行，在 480ms 延迟下性能比肩 Whisper。该架构在流式 ASR 中实现了精度与延迟的平衡，但其绝对精度仍低于参数共享式流式模型，且未验证极低延迟下的泛化边界。

## 研究背景

语音流式识别的核心困境在于声学上下文的单向性。离线模型训练时假设完整音频可用，编码器采用双向注意力捕捉全局依赖；而流式系统必须在未来音频到达前输出 token，这种训练-推理不匹配随延迟降低而加剧。为弥合差距，主流方案分为两类：一是将离线模型分块处理，虽工程简单但低延迟下精度崩塌；二是原生流式架构，如 RNN-T 通过联合网络预测帧同步 token，或 Delayed Streams Modeling (DSM) 用解码器-only 模型处理对齐的音频-文本流。RNN-T 依赖显式对齐策略，解码逻辑复杂；DSM 虽简化了架构，但仅在较高延迟下接近离线精度，亚秒级延迟下的多语言鲁棒性仍是空白。

Voxtral Realtime 切入这一空白，继承 DSM 的流同步思想，但重构了编码器与延迟条件化机制。传统 DSM 使用双向编码器或简单正弦嵌入表示延迟，前者无法流式运行，后者在训练收敛上表现平庸。本文通过从头训练因果编码器，并引入 Ada RMS-Norm 将延迟作为连续变量注入解码器残差流，使模型在单一权重下支持任意 80ms 整数倍延迟，解决了此前方法需多模型部署或延迟固定导致的灵活性缺失问题。

## 核心方法

### 流同步解码参照系

DSM 框架将 ASR 重构为音频-文本流的同步预测：每 80ms 音频帧对应一个解码步骤，模型输出文本 token 或占位符。与 RNN-T 不同，DSM 不依赖外部对齐器，而是通过训练目标隐式学习对齐。本文沿用此范式，但关键差异在于编码器从双向改为因果，且延迟不再作为离散嵌入，而是通过归一化层动态条件化。

### 因果音频编码器

设计动机在于解决双向编码器无法流式运行的根本矛盾。Whisper 等离线模型使用 640M 参数的双向 Transformer，而 Voxtral Realtime 采用 970M 参数的因果编码器，输入为 128 维 log-Mel 谱（10ms 帧移），经 2x 下采样卷积茎后，以 50Hz 频率输出嵌入。编码器采用 RMSNorm、SwiGLU 激活与 RoPE 位置编码，注意力窗口限制为 750 帧（15 秒），通过滑动窗口机制实现无界流式处理。因果性确保输出仅依赖当前及过去输入，4 帧历史缓冲区精确复现卷积依赖，避免了分块处理中的边界误差。

### 自适应延迟条件化

设计动机在于克服正弦嵌入或特殊 token 在延迟泛化上的局限。DSM 将延迟嵌入与音频-文本嵌入相加，但收敛慢且精度低；特殊 token 需在滑动窗口边界重复，增加序列复杂度。本文提出 Ada RMS-Norm，将目标延迟 $\tau$ 编码为向量 $g(\tau)$，加性注入解码器每个 Transformer 块的前馈分支：

$$
\text{FFN}(x) = W_2 \cdot \text{GELU}(W_1 x + g(\tau))
$$

其中 $g(\tau)$ 由正弦嵌入经 32 维 MLP 投影得到，仅增加 5M 参数。该机制使延迟成为连续可调变量，训练时 $\tau$ 在 80ms 至 2400ms 间均匀采样，推理时通过同一模型切换延迟，无需重新训练或部署多模型。

## 实验评估

实验覆盖英语短/长音频、FLEURS 13 语言及 Mozilla Common Voice (MCV)，基线包括离线模型 Whisper、Voxtral Mini Transcribe V2，实时 API GPT-4o mini Transcribe、Scribe v2 Realtime，及开源流式模型 DSM 1B/2.6B、Nemotron Streaming。缺失 MCR-RNNT 等参数共享式流式基线，限制了与当前 SOTA 的直接对比。

| 模型 | 延迟 (ms) | En-Short | En-Long | FLEURS | MCV |
|---|---|---|---|---|---|
| Whisper | — | 8.39 | 7.97 | 8.23 | 14.25 |
| Voxtral Mini Transcribe V2 | — | 7.27 | 7.11 | 5.90 | 8.07 |
| Scribe v2 Realtime | — | 7.93 | 7.97 | 7.95 | 12.85 |
| DSM 1B En-Fr | 500 | 8.11 | 7.72 | — | — |
| Voxtral Realtime | 480 | 9.59 | 14.29 | — | — |
| Voxtral Realtime | 960 | 9.41 | 13.02 | — | — |
| Voxtral Realtime | 2400 | 9.95 | 9.29 | 10.80 | 19.22 |

在 480ms 延迟下，Voxtral Realtime 的 FLEURS WER 未直接列出，但据正文描述其性能比肩 Scribe v2 Realtime 与 Whisper；960ms 时超越两者，2400ms 时接近 Voxtral Mini Transcribe V2 的 5.90。

| 延迟条件化方法 | 收敛速度 | 最终 WER (En) |
|---|---|---|
| Sum (正弦嵌入) | 慢 | 0.0650 |
| Special Tokens | 慢 | 0.0625 |
| Ada RMS-Norm | 快 | 0.0500 |

消融显示 Ada RMS-Norm 在英语、法语、德语上均实现更快收敛与更低 WER，验证了加性条件化优于嵌入相加。词分组策略中，每词插入 `[W]` token 导致 WER 0.35，而每组插入仅 0.05，表明保留预训练语言模型的子词分布至关重要。左填充从 0 增至 32 帧，En-Short WER 从 9.10 降至 8.47，但 MCV 从 16.03 升至 15.24 后微升，提示填充对多语言鲁棒性影响有限。

评估边界方面，论文未报告置信区间，FLEURS 结果仅给出宏平均，缺乏逐语言方差分析。代码与权重已开源（Apache 2.0），vLLM 集成支持实时服务，但训练数据规模（13 语言）未详细披露，限制了复现性。

## 关联研究分析

从方法设计看，Voxtral Realtime 与 MCR-RNNT 代表流式 ASR 的两条路径：前者采用原生因果编码器，后者通过参数共享统一离线-流式模式。MCR-RNNT 在 LibriSpeech Streaming 上 WER 7.33，低于 Voxtral Realtime 在类似协议下的表现（据领域综述），但 MCR-RNNT 依赖一致性损失缩小表示差距，训练复杂度更高。Voxtral Realtime 的因果架构部署更简单，但绝对精度较低，根源可能在于因果编码器丢失了双向上下文，而参数共享模型通过离线训练阶段保留了部分全局信息。

从框架继承看，Voxtral Realtime 与 DSM 共享流同步解码思想，但 DSM 使用双向编码器或固定延迟，而本文引入因果编码器与 Ada RMS-Norm。DSM 在 500ms 延迟下 FLEURS WER 未直接对比，但 Voxtral Realtime 在 480ms 下性能比肩 Scribe v2 Realtime，表明延迟条件化机制有效弥补了因果编码器的上下文损失。然而，DSM 未探索多延迟统一，本文的 Ada RMS-Norm 是否在其他多模态任务（如语音翻译）中同样有效，论文未给出回答。

## 总结

Voxtral Realtime 解决的核心矛盾是流式 ASR 中因果上下文限制与离线精度之间的张力。现有分块方法在低延迟下精度崩塌，RNN-T 解码复杂，DSM 延迟固定，均无法在亚秒级延迟下实现多语言鲁棒识别。本文通过因果编码器与 Ada RMS-Norm 延迟条件化，使单一模型支持 80ms 至 2400ms 任意延迟，在 480ms 下 FLEURS 性能比肩 Whisper，960ms 下超越 Scribe v2 Realtime。其边界在于绝对精度仍低于参数共享式流式模型（如 MCR-RNNT），且未验证极低延迟（<100ms）下的泛化性。当延迟降至 80ms 时，Ada RMS-Norm 的条件化信号是否仍能有效引导解码器，论文未提供实验数据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.11298)