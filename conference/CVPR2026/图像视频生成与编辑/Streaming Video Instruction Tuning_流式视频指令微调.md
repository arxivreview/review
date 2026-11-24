# CVPR2026最新论文 ｜Streaming Video Instruction Tuning ｜流式视频指令微调

研究机构：香港浸会大学

作者：Jiaer Xia、Peixian Chen、Mengdan Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21334)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21334)

> 流式视频理解要求模型在因果约束下处理无限视频流，核心矛盾在于实时响应延迟与长程语义记忆的完整性。现有方法多依赖外部决策模块或二元 EOS 机制，导致感知与响应解耦，难以适应动态交互。Streamo 提出端到端三态决策头与大规模多任务指令数据集，将离线模型转化为实时助手。该方案在主动响应任务上表现优异，但缺乏显式记忆管理，其长程推理能力存疑。

## 研究背景

实时交互场景要求模型在帧序到达时即时决策，这引入了流式因果性（Streaming Causality）约束：模型在时间 $t$ 仅能访问 $t$ 之前的观测数据。这一约束使得离线视频模型的全局优化策略失效，因为模型无法利用未来帧信息进行全局对齐。在此约束下，模型不仅需理解视觉内容，更需判断“何时响应”，即主动响应（Proactive Response）时机决策。

现有主流路线存在显著瓶颈。一类方法如 Dispider 和 StreamBridge 采用辅助模型分割视频流，再调用离线模型生成内容，这种解耦架构导致感知与响应无法紧密耦合，且引入额外计算开销。另一类方法如 VideoLLM-Online 和 StreamingVLM 使用特殊 EOS 令牌预测响应时机，但二元状态（静默/响应）难以平衡复杂指令下的细粒度时序需求，且易产生语义冲突。Streamo 的切入点在于将决策与生成统一于端到端框架，通过引入中间状态提升时序决策的精细度。

## 核心方法

### 方法参照系

本文问题属于流式推理与决策路线，其通用流程为：接收视频流 $\rightarrow$ 维护内部状态 $\rightarrow$ 预测响应时机 $\rightarrow$ 生成内容。与通用流程的关键差异在于，Streamo 摒弃了外部控制器或单一 EOS 令牌，将帧级响应状态预测直接嵌入语言模型（LLM）的自回归生成过程中，实现感知与生成的端到端耦合。

### 三态响应状态机

传统方法使用二元 EOS 令牌，无法区分“正在观察”与“准备响应”的中间状态，导致在复杂任务中响应时机模糊。Streamo 引入三个离散状态头：`<Silence>`（继续处理）、`<Standby>`（检测到相关输入，等待完整信息）、`<Response>`（信息充分，生成响应）。这一设计将时序决策从二元分类扩展为三态状态机，使模型能更精细地监控输入流。状态预测直接整合到标准下一令牌预测框架中，无需额外模块。

$$
\mathcal{L}_{total} = \frac{1}{|M|} \sum_{i \in M} \sum_{j=1}^{|V|} \mathbb{1}[j=c_i] \left( -\log \frac{e^{z_{i,j}}}{\sum_{k=1}^{|V|} e^{z_{i,k}}} \right)
$$

该公式表示标准交叉熵损失，其中 $M$ 为有效位置掩码，$c_i$ 为真实令牌，$z_{i,j}$ 为令牌 $j$ 的对数几率。三态头作为特殊令牌参与此损失计算，确保模型在预测状态时与内容生成共享同一优化目标。

### 焦点加权损失函数

流式数据中 `<Silence>` 令牌占比超过 80%，导致严重的类别不平衡，模型倾向于保持静默而忽略响应时机。为缓解此问题，Streamo 引入焦点加权（Focal Weighting）与频率平衡（Frequency Balancing）机制。焦点权重强调难样本，频率权重提升稀有状态（如 `<Response>`）的损失贡献。

$$
w_i = (1 - p_{c_i})^\gamma \cdot \alpha_{c_i}
$$

其中 $p_{c_i}$ 为真实类别预测概率，$\gamma$ 为聚焦参数（设为 2），$\alpha_{c_i}$ 为基于批次内频率计算的权重。该公式通过降低易样本权重、提升稀有状态权重，使模型在训练过程中更关注响应时机的学习，从而解决类别不平衡导致的时序决策偏差。

## 实验评估

Streamo 在 OVO-Bench、VideoMME 等基准上评估，基线覆盖 Flash-VStream、VideoLLM-Online、Dispider 等主流方法，但缺失 2026 年 VST、EvoStreaming 等最新工作。Streamo-7B 在 OVO-Bench 整体准确率上达到 55.61%，低于 ThinkStream-3B 的 59.66%（据领域综述），但在 Forward Active Responding (FAR) 任务上取得 54.77%，显著优于 StreamPro-GRPO-4B 的 20.6%（据领域综述）。

| 模型 | OVO-Bench Overall (%) | OVO-Bench FAR (%) | VideoMME (%) |
| :--- | :--- | :--- | :--- |
| Streamo-7B | 55.61 | 54.77 | 67.9 |
| Dispider-7B | 41.78 | 34.72 | 57.2 |
| StreamingVLM-7B | 54.25 | - | 65.1 |

消融实验显示，焦点损失（Focal Loss）相比交叉熵（CrossEntropy）在 FAR 任务上将 CRR 指标从 41.67 提升至 82.5，表明损失函数设计对时序决策至关重要。然而，Streamo 未报告计算延迟或显存占用，且未评估超长视频下的记忆一致性，其性能优势可能部分源于数据规模而非架构创新。

## 关联研究分析

从问题动机看，Streamo 与 VideoLLM-Online 均聚焦主动响应，但前者通过三态头解决后者二元 EOS 的语义冲突问题。VideoLLM-Online 的 EOS 决策与内容生成耦合，导致在复杂指令下难以区分“观察”与“响应”状态，而 Streamo 的 `<Standby>` 状态提供了中间缓冲，使模型能更准确地判断信息充分性。这一差异源于任务复杂度：Streamo 处理多任务指令，需要更细粒度的时序控制。

从方法设计看，Streamo 与 StreamingVLM 在架构选择上存在分歧。StreamingVLM 采用注意力沉没（Attention Sink）与连续 RoPE 解决长程记忆断裂，而 Streamo 依赖骨干 Qwen2.5-VL 的隐式 KV Cache 机制，未引入显式记忆管理。这种差异暗示 Streamo 可能在超长视频上面临记忆瓶颈，但其端到端训练范式在短中视频流中提供了更紧密的感知-响应耦合。

## 总结

Streamo 旨在解决流式视频理解中主动响应时机决策与多任务指令跟随的矛盾，通过端到端三态决策头与大规模多任务指令数据集，将离线模型转化为实时助手。实验表明，Streamo-7B 在 OVO-Bench FAR 任务上取得 54.77% 的准确率，显著优于现有方法，但在整体准确率上略低于最新 SOTA。其边界在于缺乏显式记忆管理，依赖骨干隐式记忆，可能在超长视频上面临长程推理挑战。当视频时长超过 10 分钟时，三态决策头的时序精度是否因记忆丢失而下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21334)