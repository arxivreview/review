# HuggingFace最新推荐论文 ｜Chain-of-Thought Degrades Visual Spatial Reasoning Capabilities of Multimodal LLMs ｜多模态推理模型的空间推理退化分析

研究机构：印度理工学院、微软研究院

作者：Sai Srinivas Kancheti、Aditya Sanjiv Kanade、Vineeth N. Balasubramanian 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16060)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16060)

> 视觉-语言模型（Vision-Language Models, VLMs）在数学与逻辑领域通过思维链（Chain-of-Thought, CoT）实现了推理能力的跃升，但在空间几何任务中，这种文本中心范式是否有效尚存疑。现有研究多关注如何提升空间性能，却忽视了推理机制本身对视觉感知的干扰，本文切入点在于验证 CoT 在空间任务中的负面效应及其背后的捷径学习机制。通过统一评估协议与 No-Image++ 消融实验，量化了 17 个模型在 13 个基准上的表现差异。该工作提供了关键的诊断证据，但缺乏对视觉中心训练范式的具体构建方案。

## 研究背景

当模型面对“洞穴位于树木下方”这类空间关系时，若仅凭文本先验而非视觉证据作答，即发生空间幻觉。这种幻觉源于语言骨干对统计规律的过度依赖，而视觉编码器中分布式的空间信号被忽略。为量化这一现象，需引入多模态推理模型（Multimodal Reasoning Models, MRMs），即经监督微调（SFT）和强化学习（RL）后训练以生成逐步推理的模型，其核心假设是长 CoT 能提升复杂推理能力。

空间推理要求几何直觉与精确定位，这与文本推理的线性逻辑存在结构性冲突。主流路线如 GeoWeaver 和 SpatialLadder 试图通过注入几何先验或渐进训练提升性能，但均未系统评估 CoT 机制本身的影响。现有基准如 VSI-Bench 和 MindCube 侧重于性能排名，缺乏对推理过程与视觉接地之间关系的诊断。本文切入点在于：若 CoT 在空间任务中不仅无效甚至有害，则当前 MRMs 的架构假设需重新审视。

## 核心方法

### 方法参照系

本文属于机制可解释性路线，但采用纯评估范式。与 The Dual Mechanisms 等研究不同，本文不提出新架构，而是通过统一评估协议隔离 CoT 的影响。关键差异在于：标准流程关注“如何提升性能”，本文关注“为何文本推理在空间任务中失效”。

### 统一评估协议

设计动机：消除不同模型因提示词差异导致的性能波动，确保 CoT 与非 CoT 的公平比较。通常做法是各模型使用其原生提示词，本文采用 VLMEvalKit 统一系统提示，并定义两种模式：基础提示（Non-CoT）与 CoT 提示（要求输出思考过程）。

$$
\text{Accuracy}_{\text{CoT}} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}(\hat{y}_i^{\text{CoT}} = y_i)
$$

该公式计算 CoT 模式下的平均准确率，其中 $\mathbb{I}$ 为指示函数。通过对比 $\text{Accuracy}_{\text{CoT}}$ 与 $\text{Accuracy}_{\text{Non-CoT}}$，量化 CoT 的净效应。

### No-Image++ 消融实验

设计动机：验证模型是否依赖视觉证据，还是利用文本捷径。通常做法是移除图像，但模型可能因选项分布偏置而猜测。本文引入“无法确定”选项，强制模型承认视觉缺失。

$$
P(\text{Hallucination}) = \frac{\sum_{i=1}^{N} \mathbb{I}(\hat{y}_i \neq \text{"Cannot determine"} \land y_i = \text{"Cannot determine"})}{N}
$$

该公式计算幻觉率，即模型在图像缺失时仍选择具体答案的比例。高幻觉率表明模型依赖文本先验而非视觉感知。

## 实验评估

实验覆盖 13 个数据集，包括静态 2D（如 BLINK）和 3D/动态（如 MindCube）。基线审计显示，本文评估了 8 个开源 MRM（如 GThinker, ViGoRL）和 5 个专有模型（GPT 系列），但缺失 GeoWeaver 等几何接地方法，导致无法直接对比“几何驱动”与“文本推理”的差异。

| 模型 | CoT 准确率 (%) | Non-CoT 准确率 (%) | 差异 (%) |
| :--- | :--- | :--- | :--- |
| GThinker-7B | 62.52 | 39.38 | -23.14 |
| ViGoRL-7B-Spatial | 60.68 | 62.52 | +1.84 |
| Vision-G1-7B | 63.26 | 62.85 | -0.41 |
| Qwen2.5-VL-7B | 59.68 | 62.68 | +3.00 |

GThinker 在 Non-CoT 模式下性能骤降 23.14%，表明其对提示格式敏感；而 ViGoRL 在 CoT 模式下略优，但 No-Image++ 实验显示其幻觉率高达 43.18%，证实性能提升源于文本捷径而非视觉接地。

No-Image++ 消融中，Qwen2.5-VL-7B 的幻觉率为 38.59%，而 GThinker 为 28.10%。专有模型 GPT-5 的 CoT 退化幅度为 +0.65%，远小于开源模型，且其推理链长度仅约 350 字符，而 Qwen3-VL-8B-Thinking 为 3600 字符。这表明推理链的简洁性可能缓解幻觉，但训练细节不透明，限制了因果推断。

评估边界：指标仅包含 pass@1 准确率，未报告置信区间；评估协议依赖 LLM-as-a-judge（Qwen3-30B），虽 Cohen’s kappa > 0.99，但存在潜在偏置。可复现性方面，论文未提供代码 URL，但使用 vLLM 0.10.0 和 4 块 A100 GPU，超参数（batch size 16, max tokens 32768）已公开。

## 关联研究分析

从问题动机看，本文与 The Dual Mechanisms 形成互补。The Dual Mechanisms 通过线性探针揭示视觉编码器主导空间信号，但未评估 CoT 对这一机制的干扰。本文通过 No-Image++ 实验证实，CoT 加剧了语言骨干对视觉信号的忽略，导致空间幻觉。差异根源在于：The Dual Mechanisms 关注“空间信号在哪里”，本文关注“推理过程如何破坏信号利用”。

从方法设计看，本文与 GeoWeaver 构成对比。GeoWeaver 通过显式几何令牌提升 VSI-Bench 性能至 57.9%，而本文发现 MRMs 在相同基准上普遍劣于骨干。差异根源在于：GeoWeaver 注入硬几何约束，抑制文本先验；本文的 MRMs 依赖软文本推理，缺乏几何接地。GeoWeaver 未在本文评估中作为基线，导致无法量化“几何接地”与“文本推理”的性能差距，这一盲区限制了结论的普适性。

## 总结

本文要解决的核心矛盾是 CoT 在空间任务中的有效性假设与视觉接地需求之间的冲突。切入点在于：现有 MRMs 的失败源于文本捷径而非视觉缺失，本文通过 No-Image++ 消融证实了这一机制。方法上，统一评估协议与对抗性测试隔离了 CoT 的净效应。证明了 7/8 MRM 劣于骨干，且 CoT 平均降低准确率 3%。边界在于：未评估几何接地方法，且专有模型训练细节不透明。当推理链长度从 3600 字符压缩至 350 字符时，幻觉率是否线性下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16060)