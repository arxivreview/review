# HuggingFace最新推荐论文 ｜OneStreamer: Unifying Perception, Memory, and Proactive Response in Streaming Video Interaction ｜流式视频交互中的统一感知、记忆与主动响应

研究机构：中国科学院、香港中文大学

作者：Xiangyu Zeng、Yuandong Yang、Zhiqiu Zhang 等 24 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.01762)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.01762)

> 流式视频理解的核心矛盾在于：模型必须在证据尚未被查询时保留其价值，同时在不牺牲实时感知的前提下决定何时响应。现有方法将记忆压缩与响应控制解耦，导致历史视觉 Token 竞争上下文容量或推理轨迹无法复用。OneStreamer 通过共享生成过程统一查询无关的证据记录与任务响应，利用 Proactive Hierarchical Caption Memory (PHCM) 将视觉证据转化为文本记忆，并采用 Proactive State Transition Learning (PSTL) 解决状态监督不平衡。该方案在 8 个基准上取得 SOTA，但文本记忆对细粒度视觉细节的潜在损失及数据合成对基础模型能力的依赖仍需审视。

## 研究背景

实时交互场景要求模型在因果约束下处理无限视频流，即时间 $t$ 仅能访问 $t$ 之前的观测。这一约束导致两个核心困境：一是视觉 Token 随时间线性增长，超出有限上下文窗口；二是模型需自主判断何时响应，而非被动等待查询。解决前者通常依赖滑动窗口或 KV Cache 压缩，但这往往丢弃长程依赖；解决后者则需引入状态控制机制，但密集的静默标签监督易导致模型过拟合于“等待”状态，削弱对稀疏响应决策的学习。

流式视频理解的主流路线分为内存管理与主动响应两类。内存管理路线（如 StreamingVLM, HERMES）聚焦于视觉 Token 的压缩与分层存储，但保留的历史视觉特征会与近期观测竞争有限的上下文容量，削弱实时感知能力。主动响应路线（如 VideoLLM-Online, VST）通过 EOS 或状态 Token 决定响应时机，但其推理轨迹或记忆机制往往与任务查询耦合，难以形成查询无关的可复用事实记录。OneStreamer 的切入点在于将“证据记录”视为一种查询无关的生成任务，与“任务响应”共享同一因果生成过程，从而在单次前向传播中同时解决记忆形成与时序决策问题。

## 核心方法

### 方法参照系

流式视频 LLM 的标准架构通常包含视觉编码器、投影层、LLM 及记忆模块。常规流程中，记忆模块独立于生成过程，通过检索或压缩历史视觉 Token 来扩展上下文；响应控制则通过额外的分类头或独立的 EOS 预测实现。OneStreamer 的关键差异在于：它不维护独立的视觉记忆库，而是将记忆写入（Caption Generation）与响应生成（QA Generation）统一在同一个自回归序列中，通过控制 Token 动态切换任务模式。

### Proactive Hierarchical Caption Memory (PHCM)

PHCM 解决了历史视觉 Token 与近期观测竞争上下文容量的问题。在 Recent-N FIFO 窗口保留最新 N 帧视觉 Token 的基础上，模型主动生成两类文本记录：`</Observe>` 引入局部细节描述，`</Summary>` 引入事件级语义摘要。这些文本记录在源帧离开视觉窗口后保留在文本历史中，作为长程事实上下文。其核心机制在于将视觉信息转化为紧凑的文本表示，避免了视觉 Token 的累积。

$$
M_t = \text{Concat}(V_{t-N:t}, C_{1:t})
$$

其中 $V_{t-N:t}$ 为 Recent-N 窗口内的视觉 Token，$C_{1:t}$ 为累积的文本记忆（包含 `</Observe>` 和 `</Summary>` 生成的内容）。该公式表明，模型在时间 $t$ 的上下文由近期视觉细节与长期文本记忆共同构成，实现了感知与记忆的异构融合。

### Proactive State Transition Learning (PSTL)

PSTL 解决了密集状态 Token 监督中静默标签主导损失函数的问题。传统方法对所有状态 Token 应用交叉熵损失，导致大量重复的 `</Silence>` 标签淹没稀疏的 `</Response>` 信号。PSTL 通过选择性监督，仅对输出锚点（Output Anchors）及代表性的状态变化/持续 Token 计算损失。具体而言，定义监督配额 $q$ 为最大输出锚点组的 Token 数量，并对其他组进行无放回均匀采样以匹配该配额。

$$
q = \max_{X} \max_{a \in A_\tau} n_{X \to a}
$$

$$
|I_{X \to Y}| = \min(n_{X \to Y}, q)
$$

其中 $A_\tau$ 为任务 $\tau$ 的输出锚点集合，$n_{X \to Y}$ 为状态转移 $X \to Y$ 的出现次数。该机制确保所有输出起始 Token 均被监督，同时限制高频静默状态的影响，使模型更关注“何时响应”的决策边界。

## 实验评估

OneStreamer-4B 在 8 个流式视频理解与主动响应基准上取得最佳结果。基线覆盖包括 Qwen3-VL-4B、MOSS-VL-Realtime-11B 等主流模型，但缺失 HERMES、VST 等 2026 年最新记忆管理方法的直接对比。在 OVO-Bench Overall 上，OneStreamer 取得 72.1，较 Qwen3-VL-4B 的 70.2 提升 1.9 点，较 MOSS-VL-Realtime-11B 的 70.8 提升 1.3 点。在 StreamingBench Realtime 上，OneStreamer 取得 86.9，显著高于 Qwen3-VL-4B 的 82.7 和 MOSS-VL-Realtime-11B 的 83.2。

| 方法 | OVOBench (Overall) | StreamingBench (Realtime) | ProactiveVideoQA (Avg) | OmniMMI (Avg) |
| :--- | :--- | :--- | :--- | :--- |
| OneStreamer (4B) | 72.1 | 86.9 | 48.7 | 36.6 |
| Qwen3-VL (4B) | 70.2 | 82.7 | 47.2 | 38.5 |
| MOSS-VL-Realtime (11B) | 70.8 | 83.2 | 29.4 | 24.6 |

消融实验验证了 PHCM 与 PSTL 的有效性。在 OVOBench Backward 任务中，保留 PHCM 生成的 Caption 记录使 ASI 从 63.5 提升至 71.6，证明文本记忆在源帧离开窗口后仍具价值。PSTL 在仅监督 27.5% 状态 Token 的情况下，在 ProactiveVQA、OmniMMI 和 OVO-Timing 上均优于密集监督（100%）和随机稀疏监督（27.5%），表明选择性监督优于单纯的稀疏化。

| 策略 | OVOBench Backward (ASI) | OVOBench Backward (EPM) | ProactiveVQA (Avg) | OmniMMI (Avg) |
| :--- | :--- | :--- | :--- | :--- |
| FIFO (Recent-16) | 63.5 | 62.0 | 26.1 | 30.8 |
| PHCM (Ours) | 71.6 | 62.6 | 48.7 | 36.6 |
| PSTL (Ours) | - | - | 48.7 | 36.6 |
| All state tokens (CE) | - | - | 26.1 | 30.8 |

评估边界方面，论文未报告 TTFT 之外的系统级延迟指标，且数据合成依赖 Gemini 和 Seed 等外部 VLM，其性能提升可能部分归因于基础模型的视觉理解能力而非流式适配策略本身。代码已开源，但训练数据 OneStreamer-1M 的构建细节需结合附录进一步验证。

## 关联研究分析

从记忆机制看，OneStreamer 与 HERMES 和 VST 存在显著差异。HERMES 基于 KV Cache 分层，保留视觉特征以支持细粒度检索；VST 利用自回归推理生成思维链作为记忆。OneStreamer 则完全放弃历史视觉 Token，转而生成文本 Caption。这一选择的根源在于任务特性：对于需要长程事实记忆而非细粒度视觉匹配的任务，文本记忆更紧凑且不易受上下文竞争影响。然而，文本记忆是否丢失了视觉细节，导致在动态场景下的细粒度感知任务性能受损，论文未给出直接回答。

从响应控制看，OneStreamer 的 PSTL 与 VideoLLM-Online 的 EOS 预测不同。VideoLLM-Online 采用二元静默/响应决策，而 OneStreamer 引入多状态转移（`</Silence>`, `</Standby>`, `</Response>`）并采用选择性监督。PSTL 的优势在于解决了静默标签过拟合问题，但其有效性依赖于输出锚点的准确定义。若任务中输出锚点分布不均或定义模糊，PSTL 的配额机制可能失效。此外，OneStreamer 将记忆写入与响应生成统一，而 VST 将推理与响应分离，这种统一架构在计算效率上更具优势，但在复杂多步推理场景下的深度可能受限。

## 总结

OneStreamer 解决了流式视频理解中记忆形成与响应决策解耦导致的上下文竞争与监督不平衡问题。其核心创新在于通过共享生成过程统一查询无关的证据记录与任务响应，利用 PHCM 将视觉证据转化为文本记忆，并通过 PSTL 优化状态监督。实验表明，该方案在 8 个基准上取得 SOTA，其中 OVO-Bench Overall 达 72.1，ProactiveVQA 达 48.7。然而，文本记忆对细粒度视觉细节的潜在损失及数据合成对基础模型能力的依赖仍是其边界。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.01762)