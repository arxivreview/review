# HuggingFace最新推荐论文 ｜StreamVibe: Proactive Video Agents for Evolving User Intent ｜面向演化用户意图的流式主动视频代理

研究机构：美国斯坦福大学、美国加州大学圣塔芭芭拉分校

作者：Chengzhi Liu、Yuxiang Lai、Yuzhe Yang 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.34662)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.34662)

> 导读 流式视频理解正从被动问答向主动交互演进，核心挑战在于模型需在严格因果约束下，自主决定何时介入并生成何种响应。现有方法多依赖显式指令触发，难以处理隐式意图推断与动态状态跟踪，导致在长程交互中出现响应滞后或状态漂移。StreamVibe 提出 StreamVibe-Bench 基准与 StreamVibe-VL 模型，通过流式监督微调与局部轨迹强化学习联合优化响应时机与内容，并引入 StreamVibe-Harness 维护意图生命周期与分层记忆。该工作填补了隐式意图建模的空白，但其显式状态机架构在极端动态场景下的鲁棒性仍有待验证。

## 研究背景

当智能体面对无限视频流时，其决策不仅受限于“看到了什么”，更受制于“用户想要什么”以及“当前任务进展如何”。这一困境源于流式因果性（Streaming Causality）约束：模型在时间 $t$ 仅能访问 $t$ 之前的观测，无法利用未来帧进行全局优化。在此约束下，主动响应（Proactive Response）成为核心能力，要求模型在无需用户显式指令的情况下，基于上下文推断隐式意图并决定介入时机。然而，传统流式模型如 VideoLLM-Online 仅将“何时说话”形式化为二元决策，缺乏对意图语义的深层理解，导致在复杂交互中频繁出现误报或漏报。

随着交互深入，用户意图并非静态，而是随任务进展动态演化。现有方法如 VST 虽引入双记忆系统提升推理深度，但其记忆管理仍侧重于视觉与文本特征的压缩，未显式建模意图的生命周期。当用户中途修改需求或插入新任务时，模型难以区分哪些意图已失效、哪些仍活跃，导致响应与当前状态脱节。StreamVibe 指出，主动交互不仅是时序决策问题，更是意图感知与状态跟踪问题，亟需一种能同时处理隐式推断、动态更新与长程一致性的架构。

## 核心方法

### 方法参照系：因果流决策与状态解耦

StreamVibe 将主动辅助建模为因果流决策过程。智能体观察视频流 $V$，在时间 $t$ 访问因果上下文 $c_t = \langle V_{\le t}, I_{\le t}, H_{<t} \rangle$，其中 $I_{\le t}$ 为已表达意图，$H_{<t}$ 为历史交互。策略 $\pi$ 输出动作 $a_t \in \{\text{silence, response}\}$。该框架与 VideoLLM-Online 的 EOS 预测机制同属流式推理路线，但关键差异在于：StreamVibe 显式区分了“意图有效性”与“响应决策”，前者由 Harness 维护，后者由策略 $\pi$ 执行，从而解耦了状态跟踪与感知决策。

### StreamVibe-VL：流式策略与局部轨迹强化学习

针对隐式意图推断，StreamVibe-VL 采用两阶段训练。首先通过流式监督微调（SFT）学习基础响应模式，随后引入局部轨迹强化学习（RL）优化关键交互时刻。传统 RL 在全轨迹上优化易受稀疏奖励干扰，StreamVibe 聚焦于响应时机与内容质量的耦合点。其优化目标可形式化为：

$$
\mathcal{L}_{RL} = -\mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t \in \mathcal{T}_{crit}} \log \pi_\theta(a_t | c_t) \cdot R_t \right]
$$

其中 $\mathcal{T}_{crit}$ 为交互关键时刻集合，$R_t$ 为综合响应时机与内容质量的奖励。该设计动机在于：全轨迹优化计算开销大且梯度噪声高，而局部轨迹 RL 仅在决策边界处施加强监督，显著提升了模型在模糊意图下的响应准确性，避免了因过度拟合静态启发式规则导致的僵化。

### StreamVibe-Harness：意图生命周期与分层记忆

为解决动态意图下的状态漂移，StreamVibe-Harness 维护显式交互状态 $S_t = \langle A_t, P_t, R_t \rangle$，分别表示活跃意图集、任务进度与已交付响应。Harness 通过分层记忆 $M_{<t}$ 检索相关历史，生成增强上下文 $\tilde{c}_t$：

$$
\tilde{c}_t = \phi(c_t, S_t, m_t), \quad m_t = \text{Retrieve}(M_{<t}, A_t, P_t)
$$

该公式表明，Harness 并非简单拼接历史，而是基于当前活跃意图 $A_t$ 和任务状态 $P_t$ 动态检索记忆。其设计动机在于：传统 KV Cache 压缩策略（如 StreamingVLM）虽节省显存，但丢失了意图语义的细粒度关联。StreamVibe-Harness 通过意图生命周期管理，确保仅保留与当前任务相关的证据，解决了长程交互中因上下文膨胀导致的注意力分散问题，使模型能准确区分已满足的一次性意图与持续监控的持久意图。

## 实验评估

StreamVibe-Bench 包含 4.1K 评估样本，覆盖显式、隐式与动态意图，支持 Pointwise 与 Trajectory 两种协议。基线对比涵盖专有模型（Gemini, GPT）、开源离线模型（Qwen）及流式模型（VideoLLM-Online, LiveStar）。

| 模型 | Explicit F1 | Implicit F1 | Dynamic F1 | Overall F1 |
| :--- | :--- | :--- | :--- | :--- |
| VideoLLM-Online | 9.32 | 7.15 | 16.16 | 10.88 |
| LiveStar | 10.74 | 17.10 | 9.32 | 12.39 |
| StreamVibe-VL (SFT) | 71.91 | 61.98 | 66.84 | 66.91 |
| StreamVibe-VL (RL) | 72.01 | 59.06 | 66.34 | 65.80 |

*注：数据取自 Pointwise 评估（±2s 容差），Overall F1 为三类意图 F1 均值。*

StreamVibe-VL 在隐式与动态意图上显著优于基线，VideoLLM-Online 在隐式意图上 F1 仅 7.15，表明显式触发机制在缺乏明确指令时几乎失效。RL 版本在 Explicit 上略优，但在 Implicit 上略低于 SFT，暗示强化学习在高度模糊场景下可能因奖励稀疏而收敛至保守策略。

| 模型 | Trajectory Timing F1 | Trajectory Content F1 |
| :--- | :--- | :--- |
| StreamVibe-VL (SFT) | 10.08 | 5.32 |
| StreamVibe-VL (RL) | 11.46 | 6.49 |
| + Harness (RL) | 19.53 | 14.22 |

*注：数据取自 Trajectory 评估（±2s 容差），Explicit 意图类别。*

引入 Harness 后，Trajectory 性能大幅提升，Timing F1 从 11.46 增至 19.53，Content F1 从 6.49 增至 14.22。这一增益验证了显式状态跟踪对长程一致性的关键作用：端到端模型在持续交互中易因历史累积产生误差传播，而 Harness 通过重置与检索机制切断了错误链。然而，Trajectory 绝对分数仍低，表明当前模型在复杂动态场景下的鲁棒性仍有巨大提升空间。

评估协议上，StreamVibe-Bench 引入了 Trajectory 评估，弥补了现有基准仅关注 Pointwise 的缺陷。但实验未报告极端延迟尖峰下的性能，且 Harness 的计算开销未量化，可能影响实时部署可行性。

## 关联研究分析

从问题动机看，StreamVibe 与 VideoLLM-Online 均致力于主动响应，但后者将意图视为外部给定条件，仅优化触发时机；StreamVibe 则将意图推断内化为模型能力，要求从视觉流中反推用户目标。这一差异源于任务特性：VideoLLM-Online 面向监控预警，意图明确；StreamVibe 面向助手交互，意图隐含。StreamVibe 的隐式意图建模是否过度依赖训练数据中的意图分布，在分布外场景下是否泛化，论文未给出回答。

从方法设计看，StreamVibe-Harness 与 HERMES 均利用分层记忆，但 HERMES 侧重视觉 Token 的语义压缩以节省显存，StreamVibe-Harness 侧重意图状态的逻辑维护以保障一致性。StreamVibe 显式维护意图生命周期，而 HERMES 通过注意力机制隐式聚合信息。在长程依赖任务中，显式状态机是否比隐式注意力更具鲁棒性，取决于意图结构的复杂度。若意图高度非线性且相互耦合，显式状态机的状态空间爆炸可能抵消其逻辑清晰的优势，这一权衡在论文中未深入探讨。

## 总结

StreamVibe 针对流式视频理解中隐式意图推断与动态状态跟踪的缺失，提出 StreamVibe-Bench 基准与 StreamVibe-VL 模型，通过流式 SFT 与局部轨迹 RL 优化响应策略，并引入 StreamVibe-Harness 维护意图生命周期。实验表明，StreamVibe-VL 在隐式意图上的 F1 达 61.98，显著优于 VideoLLM-Online 的 7.15；引入 Harness 后，Trajectory 评估的 Timing F1 提升 8.07 个百分点，验证了显式状态跟踪对长程一致性的增益。然而，Trajectory 绝对性能仍低，且 Harness 的计算开销未量化，限制了其在资源受限场景的部署。当意图动态演化频率超过 Harness 状态更新速率时，显式状态机是否会因同步延迟导致决策失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.34662)