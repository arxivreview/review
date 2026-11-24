# ACL2026最新论文 ｜Towards Mitigating Modality Bias in Vision-Language Models for Temporal Action Localization ｜时序动作定位中的模态偏差抑制

研究机构：英国华威大学、英国剑桥大学

作者：Jiaqi Li、Guangming Wang、Shuntian Zheng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21078)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21078)

> 时序动作定位（Temporal Action Localization, TAL）需在未修剪视频中精确定位动作起止边界，但现有视觉-语言模型（VLMs）常因语言先验偏差导致视觉证据被忽视，性能甚至不及纯视觉基线。本文切入点在于量化语言相对于视觉的增量收益，并据此动态调节模态权重。ActionVLM 通过交替 Epoch 训练估计语言优势（Language Advantage, LA），结合残差聚合策略，将语言作为视觉特征的修正信号而非主驱动。该方法在 THUMOS14 上取得 74.2% mAP，较纯视觉基线 AdaTAD 提升 0.5%，证明了去偏机制在密集预测任务中的有效性，但其对长视频时序稳定性的验证尚显不足。

## 研究背景

TAL 任务要求模型输出帧级分类序列 $\hat{\phi}_{cls} \in \mathbb{R}^{L \times C}$ 与边界定位序列 $\hat{\phi}_{loc} \in \mathbb{R}^{L \times 2}$。当动作视觉特征高度相似（如 Billiard 与 FrisbeeCatch）时，纯视觉模型因缺乏高层语义而失效。引入 VLMs 旨在利用语言描述中的意图与顺序线索，但 VLMs 的注意力机制存在“注意力汇”（Attention Sink）现象，即部分 Token 垄断注意力质量，导致关键视觉信号被抑制。同时，基于问答（QA）的任务范式鼓励模型在文本空间生成预测，进一步强化了对语言捷径的依赖，使得视觉证据在推理中被系统性低估。

现有 TAL 研究主要沿两条路线演进：一是纯视觉路线，通过 ActionFormer 等检测头优化时序建模，但受限于视觉冗余与因果依赖建模不足；二是 VLM 路线，如 VTimeLLM 和 Timemarker，通过大规模预训练对齐视频与文本，但固定模态权重导致语言先验偏差无法消除。这些方法在视觉模糊场景下表现不佳，且 QA 范式固有的文本生成特性引入了系统性错误与过度自信。本文针对这一瓶颈，提出将 TAL 重构为特征聚合（Feature Aggregation, FA）问题，通过显式估计语言优势并实施去偏聚合，解决 VLMs 在密集时序预测中视觉接地不足的问题。

## 核心方法

### 方法参照系

标准 VLM 处理 TAL 的流程为：视觉编码器提取帧特征 $F_{vis}$，语言模型基于指令 $T_{ins}$ 与描述 $T_{desc}$ 生成文本预测。该流程的关键差异在于，传统方法将语言视为预测的主驱动，而本文将其视为视觉特征的修正信号，核心改动发生在特征融合阶段，替代了原有的文本生成主导模式。

### 语言优势估计与交替 Epoch 训练

传统去偏方法（如 Cadene et al., 2019）需额外分支计算纯视觉损失，导致计算量翻倍。本文采用交替 Epoch 策略，在纯视觉 Epoch 中累积类别平均损失 $\bar{L}_v(c)$，在视觉-语言 Epoch 中将其作为纯视觉损失的代理。语言优势 $A_{lang}$ 定义为纯视觉损失与视觉-语言损失之差：

$$ A_{lang} = \bar{L}_v(c) - L_{vl} $$

该公式的物理含义是：当语言引入互补语义时，$L_{vl} < \bar{L}_v(c)$，$A_{lang} > 0$；当语言引入误导性先验时，$A_{lang} \le 0$。通过可学习的 [adv] Token 回归 $A_{lang}$，模型在推理时能动态判断语言是否有益，避免了额外视觉分支的计算开销，且该估计基于任务损失而非数据集统计，具备模型与数据集无关性。

### 残差聚合与去偏融合

基于估计的语言优势，本文计算可靠性权重 $\lambda_{lang}$，并通过 Sigmoid 映射至 $[0, 1)$ 区间，确保负优势不贡献正权重。最终特征通过残差连接获得：

$$ F_{cls} = F_{vis} + \lambda_{lang} \cdot F_{lang, cls} $$

$$ F_{loc} = F_{vis} + \lambda_{lang} \cdot F_{lang, loc} $$

这一设计动机在于解决 QA 范式中语言主导导致的视觉信号丢失。通过保留 $F_{vis}$ 为主干，语言仅作为有界残差修正，模型在视觉证据充分时（$A_{lang} \approx 0$）自动抑制语言贡献，在视觉模糊时（$A_{lang} > 0$）激活语言补充，从而在密集预测任务中实现视觉接地的鲁棒性。

## 实验评估

实验在 THUMOS14 和 ActivityNet-1.3 上进行，基线覆盖纯视觉（ViT-TAD, AdaTAD）与 VLM（VTimeLLM, Timemarker）两类。ActionVLM-B-3B 在 THUMOS14 上取得 74.2% mAP，在 ActivityNet-1.3 上取得 39.7% mAP，分别超越同骨干纯视觉基线 AdaTAD 0.5% 和 0.3%。

| 模型 | THUMOS14 Avg. mAP (%) | ActivityNet-1.3 Avg. mAP (%) |
| :--- | :--- | :--- |
| AdaTAD (Baseline) | 73.7 | 39.4 |
| ActionVLM-S-3B | 72.0 | 39.2 |
| ActionVLM-B-3B | 74.2 | 39.7 |

消融实验表明，移除语言优势损失 $L_{adv}$ 后，模型在简单动作上分配非零语言权重（mLA=0.16），导致性能下降 6.6% mAP；完整模型将简单动作的 mLA 降至 0.08，而在困难动作上提升至 0.36，验证了 LA 机制对模态偏差的精准抑制。固定 $\lambda_{lang}$ 的变体性能低于自适应版本，证实了样本级动态权重的必要性。

评估协议采用标准 mAP@tIoU，但未报告置信区间，且未对比 ClusterSTM 等预训练优化类基线，因任务侧重不同。代码已开源，超参数（如 $\lambda_{adv}=0.1$）明确，但 GPU 资源（Nvidia L40）与训练时长（120 Epochs）限制了复现的便捷性。

## 关联研究分析

从问题动机看，VidGround 同样针对语言先验偏差，但采用 RL 后训练显式纠偏，而本文采用基于损失差值的 LA 估计。VidGround 的 RL 训练成本高且不稳定，本文的 LA 机制通过交替 Epoch 实现低成本估计，更适合 TAL 的密集预测特性。然而，LA 估计依赖纯视觉损失的稳定性，在长视频序列中，视觉损失的时序波动可能影响 LA 的准确性，论文未对此进行充分验证。

从方法设计看，VTimeLLM 代表 QA 范式，通过文本生成预测边界，本文通过 FA 范式证明其局限性。VTimeLLM 的文本生成特性导致“固定输出”与“无限列举”等幻觉模式，本文的 FA 范式从根本上消除了这些结构源。但本文的 FA 范式依赖 GPT-4o 生成的动作描述，若描述质量下降或存在偏差，语言特征的可靠性将受损，论文未探讨描述生成质量对最终性能的影响。

## 总结

本文核心矛盾是 VLMs 在 TAL 中因语言先验偏差导致视觉接地不足。切入点在于量化语言相对于视觉的增量收益，通过交替 Epoch 训练低成本估计语言优势，并实施残差聚合。ActionVLM 在 THUMOS14 上取得 74.2% mAP，较纯视觉基线提升 0.5%，证明了去偏机制的有效性。边界在于 LA 估计对长视频时序稳定性的依赖，以及动作描述生成质量的影响。当视频长度增加至数百帧时，纯视觉损失的时序波动是否会导致 LA 估计失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21078)