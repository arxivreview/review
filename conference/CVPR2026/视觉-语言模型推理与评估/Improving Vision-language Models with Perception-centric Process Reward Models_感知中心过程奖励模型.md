# CVPR2026最新论文 ｜Improving Vision-language Models with Perception-centric Process Reward Models ｜感知中心过程奖励模型

研究机构：中国人民大学、美国加州大学圣迭戈分校

作者：Yingqian Min、Kun Zhou、Yifan Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24583)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24583)

> 视觉-语言模型（VLM）在强化学习后训练中面临奖励稀疏导致的信用分配难题，序列级信号无法定位推理链中的感知错误。现有方法依赖最终答案正确性，忽视了中间步骤的视觉接地失效。Perceval 通过外部过程奖励模型提取图像相关声明并比对视觉证据，将序列级优势分解为 token 级惩罚，实现细粒度监督。该方法在感知密集任务上显著优于基线，但其泛化机制与计算开销的平衡仍存疑。

## 研究背景

VLM 推理的核心困境在于语言先验对视觉证据的压制。当模型生成思维链时，往往依赖文本统计规律而非图像内容，导致幻觉对象或空间关系错误。Reinforcement Learning with Verifiable Rewards (RLVR) 通过 Group Relative Policy Optimization (GRPO) 优化策略，但仅对最终答案赋予标量奖励。这种序列级信号对所有 token 一视同仁，无法区分感知错误与逻辑错误，形成硬信用分配问题。

RLVR 已成为 VLM 后训练主流范式，但稀疏奖励限制了其在复杂视觉推理上的增益。模型常在推理链中途偏离图像上下文，而最终奖励无法提供定位失败的反馈。Perceval 的切入点在于利用视觉推理中大量中间步骤为可验证的感知声明（如物体、属性、空间关系），通过外部模型自动检测图像-文本错位，将粗粒度结果监督转化为细粒度过程监督。

## 核心方法

### 方法参照系

标准 GRPO 流程中，策略模型采样多个响应，每个响应获得标量奖励 $R_i$，优势值 $\hat{A}_i$ 在组内归一化后对所有 token 恒定。本文问题与该通用流程的关键差异在于：GRPO 无法识别响应中哪些 token 对应感知幻觉，导致错误信号被均匀稀释。

### 感知中心过程奖励模型

Perceval 作为外部 critic，接收图像 $v$、查询 $q$ 和响应 $o$，生成结构化验证 $V$。其设计动机是解决 GRPO 中“哪些 token 出错”的不可知性。Perceval 采用 think-then-answer 范式，先在 $\texttt{<think>}$ 中逐条评估 $o$ 中声明与 $v$ 的一致性，再在 $\texttt{<answer>}$ 中输出错误 span 列表。训练数据通过四阶段流水线构建：从视觉搜索数据集选取查询，用 Qwen2.5-VL-7B 生成含幻觉的响应，由 Gemini-2.5-Pro 自动标注图像-文本错位，最后对 Perceval 骨干进行监督微调。

### Token 级优势重分配

Perceval 识别出幻觉 span 后，通过精确字符串匹配定位其在响应 $o_i$ 中的 token 区间 $[j_k, l_k]$，构建二元掩码 $M_i$。设计动机是将序列级优势分解为 token 级信号，使惩罚直接作用于错误位置。token 级优势计算如下：

$$
\hat{A}'_{i,t} = \hat{A}_i (1 - m_{i,t} \alpha)
$$

其中 $\alpha \in [0,1]$ 控制惩罚强度。当 $m_{i,t}=1$（幻觉 token）且 $\hat{A}_i > 0$ 时，$\hat{A}'_{i,t} = \hat{A}_i(1-\alpha) < \hat{A}_i$，降低正向奖励；当 $\hat{A}_i < 0$ 时，$\hat{A}'_{i,t} = \hat{A}_i(1+\alpha) < \hat{A}_i$，增强负向惩罚。该机制在保留序列级偏好的同时，对无接地内容施加直接纠正压力。

## 实验评估

实验在 V*、BLINK、MMStar、MathVista 等 8 个基准上进行，基线覆盖 VLM-R1、DeepEyes、PixelReasoner 等 12 种 RLVR 及工具增强方法，但缺失纯监督微调基线。主实验显示，Perceval 在感知密集任务上显著优于 GRPO 基线：3B 模型在 V* pos 子集从 86.95 提升至 90.43，7B 模型在 BLINK 从 62.30 提升至 63.80。

| 模型 | V* pos | BLINK | MathVision | ChartQA |
| :--- | :--- | :--- | :--- | :--- |
| Qwen2.5-VL 3B + GRPO | 86.95 | 60.73 | 23.36 | 83.32 |
| Qwen2.5-VL 3B + Ours | 90.43 | 62.30 | 26.32 | 85.04 |
| Qwen2.5-VL 7B + GRPO | 85.22 | 62.30 | 27.96 | 85.16 |
| Qwen2.5-VL 7B + Ours | 86.84 | 63.80 | 30.92 | 84.44 |

消融实验表明，惩罚强度 $\alpha=0.1$ 时性能最优，$\alpha=0.3$ 时出现负迁移（V* 从 83.25 降至 78.53），提示过强惩罚可能干扰正常推理。测试时扩展中，Truncate 策略在 k=16 时 V* 达到 94.78，优于多数投票的 92.17，但 Truncate-Thinking 策略因反思提示与训练分布不匹配，效果弱于直接 Truncate。

评估边界方面，论文未报告置信区间，且 Perceval 仅在感知数据上应用，数学任务回退 GRPO，这种条件策略限制了通用性验证。代码已开源，但 Perceval 训练依赖 Gemini-2.5-Pro 标注，复现成本较高。

## 关联研究分析

从问题动机看，Perceval 与 R1-VL 的 StepGRPO 均针对 RLVR 奖励稀疏问题，但 StepGRPO 依赖规则化步骤奖励，而 Perceval 使用外部模型检测感知错误。差异根源在于任务特性：数学推理步骤可规则化验证，而视觉感知错误需图像比对，规则难以覆盖。Perceval 的感知中心设计更适配 VLM 的视觉接地需求，但牺牲了规则方法的计算效率。

从方法设计看，Perceval 与 DeepEyes 同属 RLVR 框架，但 DeepEyes 依赖工具调用（如 zoom/crop）进行视觉接地，Perceval 则通过内在感知提升实现类似效果。7B 模型在 V* pos 上 86.84 接近 DeepEyes 的 87.43，表明内在感知增强可媲美工具增强。差异根源在于：工具调用引入额外计算开销与错误传播风险，而 Perceval 的 token 级惩罚直接优化模型内部表示，但依赖 Perceval 的标注质量。

## 总结

Perceval 解决的核心矛盾是 RLVR 中序列级奖励无法定位感知错误。其切入点在于利用视觉推理中可验证的感知声明，通过外部 PRM 实现 token 级惩罚。方法上，Perceval 将 GRPO 优势分解为 token 级信号，对幻觉 span 施加惩罚，并在推理阶段通过截断-重生成循环纠错。实验证明，3B 模型在 V* pos 上从 86.95 提升至 90.43，7B 模型在 MathVision 上从 27.96 提升至 30.92。边界在于：Perceval 仅在感知数据上应用，数学任务回退 GRPO，且 $\alpha=0.3$ 时出现负迁移。当支持集增大时，Perceval 标注的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24583)