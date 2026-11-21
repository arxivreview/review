# HuggingFace最新推荐论文 ｜Factorized Learning for Temporally Grounded Video-Language Models ｜解耦式视频语言模型

研究机构：新加坡国立大学

作者：Wenzheng Zeng、Difei Gao、Mike Zheng Shou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.24097)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24097)

> 视频时间理解旨在让多模态大语言模型（MLLMs）精准定位事件时空关系并生成对应文本。现有方法将时间定位与文本生成耦合在同一自回归序列中，导致学习目标混淆且缺乏视觉语义支撑。本文提出 D²VLM 框架，通过引入证据 Token 解耦定位与回答两阶段，并设计因子化偏好优化（FPO）算法。该设计在 3.8B 参数规模下显著优于 7B 基线，但其优势是否源于架构解耦而非优化算法的先进性，仍需与强化学习（RL）方法对比验证。

## 研究背景

视频理解中，时间定位（Temporal Grounding）与文本响应（Textual Response）存在强逻辑依赖：定位提供证据，响应基于证据生成。然而，现有视频 LLM 通常将二者耦合处理，特殊时间 Token 与文本 Token 混合生成，缺乏清晰的逻辑结构。这种耦合导致模型难以区分“定位错误”与“描述错误”，且时间 Token 仅表示时间戳，未捕获事件级视觉语义，使得后续文本生成缺乏视觉上下文支撑。

领域主流路线包括特征解耦（如 DIVID）与端到端联合建模（如 Qwen2.5-VL）。特征解耦在编码器层面分离时空特征，但可能损失联合推理能力；联合建模保留交互信息，但易陷入语言先验依赖。本文切入点在于生成序列层面的逻辑解耦：不切断特征交互，而是通过“先定位后回答”的范式，强制模型在回答前显式捕获视觉证据，从而在保留依赖关系的同时明确任务边界。

## 核心方法

### 方法参照系

本文问题属于视频时间理解中的生成范式优化。标准流程为：视觉编码器提取帧特征，LLM 自回归生成包含时间戳与文本的响应序列。关键差异在于，本文不修改编码器或回归头，而是在 LLM 生成序列中引入中间证据载体，将单一耦合目标分解为两个有序子目标。

### 证据 Token 与视觉语义捕获

现有方法中，时间 Token 仅作为离散符号表示时间戳，其生成过程与文本 Token 无逻辑关联。本文引入 `<evi>` Token，其设计动机是解决“时间定位缺乏视觉语义支撑”导致的幻觉问题。当 LLM 生成 `<evi>` Token 时，计算其与所有帧级视觉特征 $\tilde{F}_V \in \mathbb{R}^{T \times C}$ 的相似度，选取高相似度的显著帧，将其视觉语义平均池化后加至 `<evi>` Token 中：

$$ \text{evi}_k = \text{evi}_k + \frac{1}{|S_k|} \sum_{t \in S_k} \tilde{F}_V[t] $$

其中 $S_k$ 为第 $k$ 个 `<evi>` Token 对应的显著帧集合。该操作使 `<evi>` Token 不仅定位时间，还携带事件级视觉语义，为后续文本生成提供实质性上下文。

### 交错文本-证据生成与一致性约束

在纯定位阶段后，模型进入交错生成阶段，再次生成 `<evi>` Token 以引用先前定位的证据。为确保两阶段一致性，引入约束：第 $k$ 个 `<evi>` Token 在两阶段中必须对应同一时间区间。损失函数包含标准 SFT 损失与定位损失：

$$ \mathcal{L} = \mathcal{L}_{sft} + \lambda \sum_{k=1}^{K} \mathcal{L}_{gnd}(\text{evi}_k^{(1)}, \text{evi}_k^{(2)}) $$

其中 $\mathcal{L}_{gnd}$ 为二元交叉熵损失，基于 `<evi>` Token 与帧特征的相似度计算帧级前景/背景概率。该设计通过 teacher-forcing 范式，使文本生成条件于正确定位的证据，形成学习捷径，提升训练稳定性。

## 实验评估

| 方法 | 年份 | R@1(IoU=0.5) | R@1(IoU=0.7) |
| :--- | :--- | :--- | :--- |
| TimeChat-7B | CVPR’24 | 32.2 | 13.4 |
| VTG-LLM-7B | AAAI’25 | 33.8 | 15.7 |
| TRACE-7B | ICLR’25 | 40.3 | 19.4 |
| E.T.Chat-3.8B | NeurIPS’24 | 45.9 | 20.0 |
| D²VLM-3.8B | ICCV’25 | 50.3 | 26.0 |

实验在 Charades-STA 上评估，基线覆盖 SFT 类方法（TimeChat, VTG-LLM）与近期 SOTA（TRACE, E.T.Chat），但缺失 RL 方法（如 TempR1, TimeLens）。D²VLM 以 3.8B 参数在 R@1(IoU=0.5) 上达到 50.3，较同规模基线 E.T.Chat 提升 4.4 点，较 7B 方法 TRACE 提升 10 点。据领域综述，TempR1 在 Charades-STA 上 mIoU 为 59.8，虽指标不同，但表明 RL 方法在绝对精度上仍领先。

| 组件 | Grounding Avg_F1 | Dense Captioning Avg_F1 |
| :--- | :--- | :--- |
| w/o event-level modeling | 26.1 | 33.4 |
| w/o visual semantic capture | 37.1 | 16.2 |
| Full design | 39.5 | 35.0 |

消融显示，移除事件级建模导致 Grounding 性能下降 13.4 点，移除视觉语义捕获导致 Dense Captioning 性能下降 18.8 点。这表明视觉语义捕获对文本生成任务的影响远大于定位任务，验证了 `<evi>` Token 作为“证据载体”的核心价值。FPO 算法进一步将 Grounding Avg_F1 从 39.5 提升至 42.3，但提升幅度小于架构解耦本身。

评估边界方面，论文未报告置信区间，且仅在 E.T. Instruct 164K 数据集上微调，泛化性存疑。代码已开源（https://github.com/nusnlp/d2vlm），训练使用 4×H100 GPU 一天内完成，可复现性较高。

## 关联研究分析

从方法设计看，D²VLM 与 DIVID 同属解耦路线，但 DIVID 在特征提取层面分离时空，而 D²VLM 在生成序列层面解耦。这一差异源于任务特性：DIVID 侧重细粒度定位精度，需特征级解耦以避免时空干扰；D²VLM 侧重生成一致性，需保留特征交互以支持文本生成。D²VLM 的 `<evi>` Token 设计更接近 ViKey 的视觉提示注入，但 ViKey 仅注入帧编号，未捕获语义，而 D²VLM 通过相似度聚合实现语义捕获，这是其优于 ViKey 的关键。

从优化算法看，D²VLM 采用 FPO（偏好优化），而 TempR1 采用 GRPO（强化学习）。FPO 通过合成数据解决缺乏带时间标注的偏好数据问题，但仅生成负样本，正样本多样性不足。GRPO 通过组内相对优势估计，无需额外数据，但训练不稳定。D²VLM 未与 GRPO 对比，无法判断 FPO 在时间定位任务上的效率与效果是否优于 RL。这一缺失暗示，偏好优化在视频时间理解中的适用性尚未充分验证。

## 总结

本文核心矛盾是时间定位与文本生成的耦合导致学习目标混淆。切入点在于生成序列层面的逻辑解耦，通过 `<evi>` Token 捕获视觉语义，使定位成为回答的显式前提。方法上，D²VLM 将响应分解为纯定位与交错回答两阶段，FPO 算法将时间定位概率纳入偏好优化目标。实验证明，3.8B 模型在 Charades-STA 上 R@1(IoU=0.5) 达 50.3，较同规模基线提升 4.4 点。边界在于，FPO 仅生成负样本，且未与 RL 方法对比，无法确认架构解耦与优化算法的独立贡献。当支持集增大时，FPO 的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24097)