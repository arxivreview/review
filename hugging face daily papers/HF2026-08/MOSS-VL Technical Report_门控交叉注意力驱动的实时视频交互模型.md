# HuggingFace最新推荐论文 ｜MOSS-VL Technical Report ｜门控交叉注意力驱动的实时视频交互模型

作者：Pengyu Wang、Chenkun Tan、Shaojun Zhou 等 32 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.15045)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.15045)

> 实时视频交互要求模型在生成回复的同时持续感知新帧，以修正或中断输出，但现有流式模型在回复期间处于“盲视”状态，无法响应场景变化。MOSS-VL 通过架构、数据与训练策略的协同设计，将视觉 Token 隔离于解码序列之外，使新帧仅追加至交叉注意力缓存，从而在生成过程中保持感知能力。该方案在四个流式基准的主动响应子任务上取得领先，但 L5 级“生成时感知”行为缺乏量化基准验证，其长期稳定性与细粒度感知代价尚存疑。

## 研究背景

实时视频理解的底层约束是流式因果性，即模型在时间 $t$ 仅能访问 $t$ 之前的观测。这一约束将问题从静态识别转化为动态时序决策，核心矛盾在于无限视频流与有限上下文窗口的冲突：帧持续累积导致显存溢出，而滑动窗口或暴力压缩往往丢失长程依赖。更深层的瓶颈在于响应时机：模型需自主判断“何时说话”，过早产生噪音，过晚失去实时意义，现有方法多依赖启发式规则或简单的 EOS 预测，缺乏对事件显著性的深层理解。

2024 年至 2025 年，领域重心从“能否看懂”转向“何时响应”，VideoLLM-Online 确立了静默/响应的二元范式，StreamingVLM 通过注意力沉没解决了无限流架构标准。然而，这些方法在生成回复期间仍无法感知新帧，导致回复一旦发出便无法修正，这在场景快速变化的实时交互中是致命缺陷。MOSS-VL 的切入点在于突破“回复期间盲视”的限制，将实时交互定义为一级能力，通过架构层面的视觉-语言解耦，使模型在生成过程中自然接收新帧，从而支持回复的动态修正与中断。

## 核心方法

### 门控交叉注意力架构

主流视频语言模型通常将视觉 Token 与文本 Token 交错输入自注意力层，导致视觉信息直接参与解码序列，新帧到达时需重新计算注意力，阻碍了生成过程中的实时感知。MOSS-VL 采用门控交叉注意力（Gated Cross-Attention），视觉 Token 仅作为键（Key）和值（Value）进入交叉注意力层，查询（Query）来自文本隐藏状态，视觉 Token 不进入解码序列。其核心公式为：

$$
\text{Attn}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V
$$

其中 $Q$ 为文本查询，$K, V$ 为视觉键值。该设计使新帧仅需追加至缓存，解码状态保持不变，下一个生成 Token 即可通过门控层关注更新后的视觉信息，实现了“生成时感知”的架构基础。

### XRoPE 与绝对时间戳

位置编码通常仅反映序列顺序，无法区分不同帧率下的实际时间间隔，导致模型难以精确建模时间依赖。MOSS-VL 引入 XRoPE（Cross-attention Rotary Position Embedding），将文本与视觉置于共享的三维坐标空间 $(t, h, w)$，其中 $t$ 为时间轴，$h, w$ 为空间轴。视觉块的位置定义为：

$$
p_{a,b} = (t, t+a, t+b), \quad 0 \le a < h', 0 \le b < w'
$$

其中 $t$ 为帧的时间锚点，$a, b$ 为空间偏移。同时，每帧前插入绝对时间戳 Token，使模型直接从 Token 读取真实时间，而非从位置推断。这一设计解决了变帧率下时间语义模糊的问题，使模型能精确判断事件发生的时刻，支撑主动响应时机的决策。

## 实验评估

实验在 OVO-Bench、OmniMMI、StreamingBench 和 ProactiveVideoQA 四个流式基准上进行，对比 AURA、VideoChat3-4B、ViSpeak-7B 等开源流式模型。MOSS-VL-Realtime 在三个基准的平均分上领先，在 StreamingBench 视觉平均分上排名第二。

| 基准 | MOSS-VL-Realtime | AURA | VideoChat3-4B | ViSpeak-7B |
| :--- | :--- | :--- | :--- | :--- |
| OVO-Bench Avg | 70.2 | 65.3 | 57.8 | 59.3 |
| OmniMMI Avg | 32.7 | 25.4 | – | – |
| StreamingBench Avg (visual) | 69.7 | 71.1 | – | 57.2 |
| ProactiveVideoQA Avg | 47.2 | – | 31.6 | – |

在主动响应子任务上，MOSS-VL 表现突出：OmniMMI 的 Proactive Alerting 得分 66.0，远超 AURA 的 37.5；OVO-Bench 的 Forward Active Responding 得分 62.1，优于 AURA 的 55.8。这一优势直接源于 Realtime-SFT 阶段对“何时说话”的显式监督，而非架构本身的感知能力。

消融实验未单独列出，但训练策略显示 Realtime-SFT 仅占总训练 Token 的 3% 以下，却带来了显著的主动响应提升。这表明实时交互能力可通过轻量级微调注入，而非依赖大规模重训练。然而，MOSS-VL 在 StreamingBench 的 Contextual Understanding 子任务上得分 56.4，低于 AURA 的 59.0，暗示视觉 Token 分离可能在长程上下文依赖任务中引入信息损失。

评估边界方面，论文未报告置信区间，且 L5 级“生成时感知”行为仅通过定性演示验证，缺乏量化基准。代码与模型已开源，但实时推理代码的延迟指标未在正文中详细列出，仅提及与 Qwen3-VL-8B 相比，首 Token 延迟优势随视觉上下文增长从 2.8 倍扩大至 5.1 倍。

## 关联研究分析

从问题动机看，MOSS-VL 与 VST 均关注主动响应，但 VST 依赖自回归推理在观察间隙进行深度思考，而 MOSS-VL 通过架构解耦在生成过程中持续感知。VST 的推理时机是离散的，MOSS-VL 的感知是连续的，这使后者能支持回复的中断与修正，但前者可能在复杂多步推理上更具优势。MOSS-VL 未与 VST 直接对比，可能因两者评估协议不兼容，或 VST 的自回归开销在实时场景中不可接受。

从方法设计看，MOSS-VL 与 StreamingVLM 均解决无限流问题，但 StreamingVLM 采用注意力沉没与连续 RoPE，视觉 Token 仍参与自注意力，而 MOSS-VL 采用门控交叉注意力，视觉 Token 完全隔离。这一差异导致 MOSS-VL 在细粒度感知任务上可能受损，但在实时性上更具优势。MOSS-VL 的视觉 Token 分离挑战了“视觉 Token 压缩是必要手段”的共识，暗示在实时交互场景中，感知与生成的解耦比压缩更重要。

## 总结

MOSS-VL 要解决的核心矛盾是实时交互中“生成时盲视”导致的回复不可修正问题。现有流式模型在回复期间无法感知新帧，而 MOSS-VL 通过门控交叉注意力将视觉 Token 隔离于解码序列，使新帧仅追加至缓存，从而在生成过程中保持感知能力。该方案在 OVO-Bench 的 Forward Active Responding 任务上取得 62.1 分，OmniMMI 的 Proactive Alerting 任务上取得 66.0 分，显著优于开源基线。然而，论文未提供 L5 级行为的量化基准，且 StreamingBench 的 Contextual Understanding 子任务得分低于 AURA，暗示视觉 Token 分离可能在长程上下文任务中引入信息损失。当视频流时长超过 12.8 分钟时，门控交叉注意力的缓存增长是否会导致显存溢出或延迟尖峰，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.15045)