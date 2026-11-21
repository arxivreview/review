# HuggingFace最新推荐论文 ｜Imagine Before You Predict: Interleaved Latent Visual Reasoning for Video Event Prediction ｜交错式潜在视觉推理用于视频事件预测

研究机构：中国科学技术大学、香港城市大学

作者：Tianxiang Jiang、Linquan Wu、Sheng Xia 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.05769)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05769)

> 视频事件预测（Video Event Prediction, VEP）要求模型从部分观测视频推断未发生的未来状态，现有多模态大语言模型（MLLMs）将中间推理文本化，导致细粒度运动与几何信息丢失，产生看似合理但视觉未接地的幻觉。FUTURE-L1 在自回归解码中交替生成文本 Token 与连续潜在视觉跨度，通过视觉增益筛选数据与潜在感知强化学习优化，在 FutureBench 上将 Qwen3-VL-8B 从 61.0 提升至 85.4。该方法验证了潜在通道对动态未来建模的有效性，但其可解释性低于文本推理，且未探索与视频生成模型的协同验证机制。

## 研究背景

当模型面对“接下来会发生什么”的预测任务时，若仅依赖文本思维链（Chain-of-Thought, CoT），视觉证据一旦转化为语言描述，细粒度的物体运动轨迹、相对位置及交互几何便发生不可逆的信息损耗。这种文本化接口迫使模型在语义空间而非视觉空间进行推理，导致预测结果虽符合语言逻辑却偏离真实视觉动态。为保留动态视觉结构，潜在推理（Latent Reasoning）将中间步骤映射至连续隐藏状态，但现有方法多将潜在状态锚定于静态辅助图像或单帧提示，缺乏对时间维度上动态演化的建模能力。

视频理解领域的主流路线已从静态特征匹配转向基于可验证奖励强化学习（RLVR）的后训练，旨在提升推理一致性。然而，回顾性任务（如视频问答）的答案可接地于可见帧，而 VEP 要求构建关于未观测状态的内部假设，现有 MLLM 在此类前瞻性任务上表现不佳：GPT-4o 在 FutureBench 上仅获 59.0，最强的文本推理模型 Video-CoE 在 3-Hop 子集上也仅 71.6。静态潜在推理方法如 Monet（47.9）和 LVR（21.0）因无法处理动态未来帧而失效。FUTURE-L1 的切入点在于将潜在推理从“静态视觉提示”扩展为“动态未来状态演化”，通过交错式潜在视觉跨度在自回归过程中持续更新想象的未来视觉结构。

## 核心方法

### 方法参照系

本文问题置于“强化学习后训练”与“时空证据接地推理”的交叉路线下。标准流程为：SFT 冷启动对齐视觉证据，RL 优化文本推理轨迹。关键差异在于：标准流程优化离散文本 Token 并接地于可见帧，本文优化连续潜在视觉跨度并接地于未来帧嵌入，且引入针对潜在轨迹的专用奖励机制。

### 交错式潜在视觉推理与视觉增益筛选

SFT 阶段需解决潜在跨度何时调用及如何对齐的问题。通常做法是随机插入潜在 Token 或依赖静态图像对齐，但 VEP 需要动态未来状态。FUTURE-L1 引入特殊 Token `<|latent_start|>`、`<|latent|>`、`<|latent_end|>`，在文本推理间插入长度自适应的潜在跨度。设计动机是避免文本化导致的语义漂移，同时防止潜在跨度退化为重复的静态噪声。数据筛选采用视觉增益（Visual-Gain）策略：对 TwiFF-2.7M 候选样本，分别计算纯文本输入（$p_t$）与含未来帧提示输入（$p_v$）的正确率，仅保留 $p_t \le 6$ 且 $p_v - p_t \ge 2$ 的样本，确保视觉提示具有边际效用。SFT 目标函数联合优化文本预测与潜在状态对齐：

$$ \mathcal{L}_{SFT} = \sum_{t \in T} \mathcal{L}_{CE}(y_t, \hat{y}_t) + \lambda \sum_{t \in S} \| \mathbf{h}_t - \mathbf{e}_t^* \|^2 $$

其中 $\mathbf{h}_t$ 为潜在位置隐藏状态，$\mathbf{e}_t^*$ 为对应未来帧的视觉嵌入，$\lambda$ 控制对齐强度。该公式将潜在跨度锚定至未来帧流形，同时保持文本通道的标准语言建模。

### LA-DAPO 潜在感知强化学习

SFT 仅提供教师强制初始化，未直接优化预测成功。LA-DAPO 在 DAPO 基础上增加两项潜在轨迹奖励。设计动机是解决 RL 阶段潜在跨度可能坍缩为重复视觉思考的问题，且无需中间帧标注。结果对比奖励 $R_{ctr}$ 利用组内正确/错误 rollout 的潜在轨迹相似度，采用最难正例 InfoNCE 形式：

$$ R_{ctr} = -\log \frac{\exp(s_{i, j^+} / \tau)}{\sum_{j \in P_i \cup N_i} \exp(s_{i, j} / \tau)} $$

其中 $s_{i,j}$ 为轨迹余弦相似度，$P_i, N_i$ 分别为正确/错误 rollout 集合。时间多样性奖励 $R_{div}$ 惩罚相邻潜在跨度的相似性：

$$ R_{div} = -\sum_{m=1}^{M-1} \mathbf{b}_m \cdot \mathbf{b}_{m+1} $$

其中 $\mathbf{b}_m$ 为第 $m$ 个跨度的均值池化向量。两项奖励分别约束跨 rollout 的结果对齐与单 rollout 内的时间演化，总奖励为 $R = R_{ans} + \lambda_c R_{ctr} + \lambda_d R_{div}$。

## 实验评估

实验在 FutureBench（多选 VEP）与 TwiFF-Bench（开放未来推理）上进行，基线覆盖通用 MLLM（GPT-4o）、视频推理模型（Video-R1, Video-CoE）及静态潜在推理模型（Monet, LVR），缺失基于视频生成模型的预测基线。

| 模型 | 方法 | FutureBench AVG (%) | TwiFF-Bench Avg. |
|---|---|---|---|
| Qwen3-VL-8B | Zero-Shot | 61.0 | 2.44 |
| Video-CoE | SFT+RL | 75.0 | — |
| Monet | SFT+RL | 47.9 | — |
| FUTURE-L1 | SFT | 73.2 | 2.52 |
| FUTURE-L1 | SFT+RL | 85.4 | 3.04 |

FUTURE-L1-RL 在 FutureBench 上达 85.4，较骨干提升 24.4 点，较最强文本基线 Video-CoE（75.0）提升 10.4 点；在 TwiFF-Bench 上达 3.04，超越 TwiFF-2.7M（2.79）。

| 消融设置 | FutureBench AVG (%) |
|---|---|
| Text-Only SFT | 65.0 |
| FUTURE-L1-SFT ($\lambda=0.1, L_{max}=4$) | 73.2 |
| FUTURE-L1-SFT + DAPO | 83.8 |
| FUTURE-L1-SFT + DAPO + $R_{ctr}$ | 84.5 |
| FUTURE-L1-SFT + DAPO + $R_{div}$ | 84.8 |
| FUTURE-L1-RL ($\lambda_c=0.2, \lambda_d=0.1$) | 85.4 |

消融显示，潜在 SFT 较纯文本 SFT 提升 8.2 点，证明增益源于模态匹配而非数据量。$L_{max}=4$ 时性能最优（73.2），$L_{max}=64$ 时降至 67.4，表明过长潜在跨度稀释信号。$R_{ctr}$ 与 $R_{div}$ 单独使用分别提升 0.7 和 1.0 点，联合使用达 85.4，$\lambda_d=1.0$ 时性能降至 81.6，显示过度多样性压力会将潜在状态推离流形。

评估边界方面，FutureBench 未报告置信区间，TwiFF-Bench 依赖 LLM-as-judge 评分，存在主观性。代码与超参数已开源，实验在 8×NVIDIA H200 上完成，可复现性较好。

## 关联研究分析

从问题动机看，FUTURE-L1 与 Video-CoE 同属 VEP 任务，但 Video-CoE 将推理轨迹结构化为长文本链，依赖语言先验组织历史事件，而 FUTURE-L1 主张动态视觉结构应在潜在空间保持连续性。差异根源在于任务特性：VEP 的正确答案常依赖细微的未来动态（如物体运动轨迹），文本化接口无法保留这些细粒度信息，而潜在通道可直接编码视觉几何。Video-CoE 在 3-Hop 子集上仅 71.6，而 FUTURE-L1 达 86.6，印证了文本化在长程预测上的瓶颈。

从方法设计看，FUTURE-L1 与 Monet 同属潜在推理路线，但 Monet 将潜在状态锚定于静态辅助图像（如草图或场景），而 FUTURE-L1 对齐至未来帧嵌入。Monet 在 FutureBench 上仅 47.9，因其静态潜在状态无法建模动态演化；FUTURE-L1 通过时间多样性奖励 $R_{div}$ 强制相邻跨度表示不同未来更新，解决了静态潜在推理在动态任务上的失效。这一设计是否适用于非预测性动态任务（如实时视频理解），论文未给出回答。

## 总结

FUTURE-L1 解决的核心矛盾是文本化推理在动态未来预测中的信息损耗。现有方法将中间推理文本化或锚定于静态图像，无法保留细粒度运动与几何信息，而 FUTURE-L1 通过交错式潜在视觉跨度在自回归解码中持续更新动态未来状态，并利用视觉增益筛选与 LA-DAPO 优化潜在轨迹。实验证明该方法在 FutureBench 上达 85.4，较最强文本基线提升 10.4 点，在 TwiFF-Bench 上达 3.04。其边界在于潜在推理的可解释性低于文本 CoT，且 $L_{max}=4$ 的限制可能约束长程依赖建模。当潜在跨度长度增加时，性能为何下降而非提升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05769)