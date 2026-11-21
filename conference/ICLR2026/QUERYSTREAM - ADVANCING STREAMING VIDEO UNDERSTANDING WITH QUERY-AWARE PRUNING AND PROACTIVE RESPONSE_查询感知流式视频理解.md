# ICLR2026最新论文 ｜QUERYSTREAM: ADVANCING STREAMING VIDEO UNDERSTANDING WITH QUERY-AWARE PRUNING AND PROACTIVE RESPONSE ｜查询感知流式视频理解

研究机构：上海科技大学、中国科学院

作者：Kairui Zhang、Zhenyu Yang、Bing Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_67543100)

> 流式视频理解需在因果约束下处理无限视频流，核心矛盾在于实时响应延迟与长程语义记忆的完整性。现有主动响应方法多依赖训练式模块或“变化即重要”的启发式规则，导致计算冗余与响应时机错位。QueryStream 通过引入查询感知的差分剪枝与双门控响应机制，在无需额外训练的前提下实现了高效且精准的交互。该框架在中等剪枝率下达到了流式基准的领先性能，但其无训练逻辑门控在复杂多步推理场景下的泛化上限尚存疑。

## 研究背景

当视频流以 1 FPS 持续输入时，模型面临显存溢出与计算爆炸的双重压力。解决这一问题的常规手段是视觉 Token 压缩，但传统压缩策略往往忽略用户意图，将视觉动态等同于语义重要性。这种混淆导致模型在无关场景切换时误触发，或在关键事件发生时因视觉特征不显著而漏检。因此，流式理解的关键不仅在于“看到什么”，更在于“何时响应”以及“如何过滤噪声”。

流式视频理解的主流路线分为被动响应与主动响应两类。被动模型依赖用户提示触发，缺乏自主性；主动模型虽能自主决策，但多依赖重训练的 EOS 预测头或辅助分类器，增加了系统复杂度。TimeChat-Online 提出的“变化即重要”策略虽轻量，却将视觉动态与语义相关性混为一谈，导致在语义无关的视觉显著变化面前产生大量误报。QueryStream 的切入点在于将查询语义直接嵌入剪枝与响应决策的核心逻辑，通过逻辑门控替代学习式调度，解决了视觉显著性与查询特异性脱节的问题。

## 核心方法

### 方法参照系

流式视频理解的标准流程通常包含视觉编码、记忆管理与响应生成三个环节。本文问题与该通用流程的关键差异在于，传统流程中的记忆管理与响应生成是查询无关的（Query-agnostic），而 QueryStream 将查询语义作为前置条件，重构了 Token 过滤与响应触发的决策逻辑。

### 查询感知差分剪枝

传统差分剪枝仅基于帧间差异保留 Token，忽略了语义相关性。QueryStream 引入查询感知差分剪枝（Query-Aware Differential Pruning, QDP），通过语义相关性与时间新颖性的逻辑与运算决定 Token 保留。设计动机在于解决“视觉显著但语义无关”的 Token 占用计算资源的问题。QDP 首先计算每个 Patch 特征与查询嵌入的余弦相似度，并设定动态阈值；同时，利用动态平滑历史（Dynamically Smoothed History, DSH）计算时间新颖性。最终保留掩码 $M_{qdp}$ 定义为：

$$ M_{qdp}(t, i) = M_{sem}(t, i) \land M_{temp}(t, i) $$

其中 $M_{sem}$ 为语义相关掩码，$M_{temp}$ 为时间新颖掩码。该公式确保了仅当 Patch 既与查询相关又相对历史背景发生显著变化时，才被送入下游模型，从而实现了计算焦点的精准对齐。

### 相关性触发主动响应

QDP 解决了“处理什么”，但“何时响应”仍需独立机制。传统方法依赖学习式 EOS 预测，存在训练偏差。QueryStream 设计相关性触发主动响应（Relevance-Triggered Active Response, RTAR）机制，通过双门控逻辑决定响应时机。设计动机在于避免在视觉活跃但语义无关的片段中浪费推理资源。RTAR 监控两个信号：帧级语义相关性 $R_t$ 与信息密度 $D_t$（即 QDP 的 Token 保留率）。触发信号 $T_t$ 定义为：

$$ T_t = \mathbb{I}(R_t > \tau_{rel}) \land \mathbb{I}(D_t > \tau_{den}) $$

其中 $\tau_{rel}$ 和 $\tau_{den}$ 为预设阈值。该机制要求当前帧既高度契合查询语义，又包含大量新的查询相关信息，才触发 Video-LLM 生成响应，从而实现了上下文感知的精准交互。

## 实验评估

实验在 StreamingBench 和 OVO-Bench 上进行，基线包括 TimeChat-Online、Flash-VStream 及 Qwen2.5-VL-7B。QueryStream 在 StreamingBench 上以 57.2% 的保留率取得 75.32 分，高于 TimeChat-Online 的 74.32 分；在 OVO-Bench 上以 52.9% 的保留率取得 49.4 分，显著优于 TimeChat-Online 的 46.7 分。

| 基准 | 模型 | 保留率 (%) | Overall Score |
| :--- | :--- | :--- | :--- |
| StreamingBench | QueryStream-7B | 57.2 | 75.32 |
| StreamingBench | TimeChat-Online-7B | 55.8 | 74.32 |
| OVO-Bench | QueryStream-7B | 52.9 | 49.4 |
| OVO-Bench | TimeChat-Online-7B | 100 | 46.7 |

消融实验显示，QDP 中语义剪枝与视觉剪枝的协同效应显著。仅使用视觉剪枝（63.4% 保留率）得分为 74.76，仅使用语义剪枝（61.7% 保留率）得分为 74.52，而完整 QDP（57.2% 保留率）达到 75.32。这表明单一维度的过滤不足以应对流式视频的复杂性，双准则的交集过滤在降低计算量的同时提升了精度。RTAR 的消融表明，仅基于密度的触发（TimeChat-Online 基线）在 OVO-Bench 的 Forward Active Responding 任务上准确率为 36.8，而完整 RTAR 提升至 40.2，验证了语义门控对响应时机的修正作用。

评估边界方面，论文未报告 TTFT（Time To First Token）或 MaxFPS 等系统级延迟指标，仅以 Token 保留率作为效率代理。超参数 $\alpha=0.1$ 及阈值在验证集上确定，但未提供不同场景下的敏感性分析。代码已开源，实验在单张 A800 GPU 上完成，具备可复现性。

## 关联研究分析

从问题动机看，QueryStream 与 VST 均关注流式视频中的主动响应，但路径截然不同。VST 采用训练式的双记忆系统，利用查询前的间隔进行自回归推理，依赖模型内部状态更新；而 QueryStream 采用无训练的逻辑门控，依赖外部特征匹配。这种差异源于对“推理深度”与“计算效率”的不同取舍：VST 追求复杂场景下的深度理解，代价是额外的生成开销；QueryStream 追求轻量部署，但可能牺牲多步推理能力。

从方法设计看，QueryStream 与 TimeChat-Online 共享差分剪枝的框架，但核心差异在于查询感知的引入。TimeChat-Online 的 DTD 机制是查询无关的，其“变化即重要”假设在语义无关的视觉变化面前失效；QueryStream 通过引入查询嵌入作为过滤条件，将剪枝从“去噪”升级为“意图对齐”。这一改进并非简单的模块替换，而是改变了信息过滤的底层逻辑，使得计算资源分配与用户意图直接挂钩。

## 总结

QueryStream 旨在解决流式视频理解中视觉动态与语义相关性混淆导致的计算冗余与响应错位问题。其切入点在于将查询语义嵌入剪枝与响应决策的核心逻辑，通过无训练的逻辑门控替代重训练的调度模块。方法上，QDP 与 RTAR 协同工作，实现了意图驱动的 Token 过滤与精准响应。实验证明，在 57.2% 的 Token 保留率下，QueryStream 在 StreamingBench 上达到 75.32 分，优于基线。然而，其无训练框架的性能上限受限于骨干模型的能力，且在 OVO-Bench 上仍低于 2026 年最新的训练式 SOTA 方法。当视频流包含复杂的多步因果推理任务时，仅依赖特征匹配的逻辑门控是否足以捕捉深层语义依赖，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_67543100)