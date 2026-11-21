# ACL-Findings2026最新论文 ｜Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs ｜正注意力动态增强

研究机构：西安电子科技大学

作者：Guangtao Lyu、Qi Liu、Chenghao Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15556)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15556)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉。现有推理时干预方法要么依赖多前向传播引入扰动偏差，要么依赖静态注意力信号易受注意力汇聚（Attention Sink）干扰。本文发现层间正注意力动态（Positive Attention Dynamics, PAD）能更可靠地揭示语义核心视觉区域，据此提出PADE，通过单次前向传播在注意力Logits层注入动态信号以抑制幻觉。该方法在保持通用多模态理解能力方面表现优异，但在幻觉抑制的绝对指标上仍落后于最新解耦解码策略，其动态信号在不同架构下的鲁棒性尚存疑。

## 研究背景

当LVLMs处理模糊视觉输入时，模型倾向于依赖预训练中习得的文本共现关系而非视觉证据，导致生成图像中不存在的物体，这一现象称为对象幻觉。幻觉的根源并非单纯的视觉编码器缺陷，而是语言先验与视觉证据的冲突。为缓解此问题，研究范式从训练时对齐转向推理时动态平衡，核心目标是在不牺牲通用生成能力的前提下，重构视觉接地（Visual Grounding）权重。

推理时干预的主流路线包括对比解码、辅助专家模型与内部静态信号增强。对比解码（如VCD）通过对比原始与扰动输入的Logits分布抑制幻觉，但需额外前向传播且引入扰动偏差；辅助模型依赖外部检测器，存在语义不对齐风险；静态信号方法（如OPERA, VAF）基于Top-K选择或阈值筛选视觉相关头或层，但极易被注意力汇聚现象误导，即无关Token持续吸收高注意力权重，导致干预偏向虚假结构。PADE的切入点在于利用模型内部层间注意力的动态变化，而非静态分布，以规避Sink干扰并实现单次前向传播的低开销干预。

## 核心方法

### 方法参照系

PADE属于注意力机制调控路线，标准流程通常是在特定层对视觉相关注意力头进行静态重加权或Top-K放大。本文的关键差异在于摒弃静态阈值选择，转而利用层间注意力增量（Inter-layer Attention Deltas）作为动态信号源，并在注入阶段引入补偿机制以保护指令注意力。

### 正注意力动态提取

静态注意力图常被注意力汇聚主导，导致语义核心区域被抑制。PADE通过计算相邻层视觉注意力图的差值并保留正值，构建PAD图以识别语义核心区域。设 $A_l$ 为第 $l$ 层平均视觉注意力图，正增量定义为：

$$ \Delta A_l = \max(A_l - A_{l-1}, 0) $$

PAD图通过聚合多层正增量获得：

$$ PAD = \sum_{l=2}^{L} \Delta A_l $$

该公式的物理含义是：语义核心区域在模型理解过程中会经历多次显著的注意力增加，而无关区域保持低注意力，Sink Token则表现为不规则波动。仅保留正增量自然抑制了噪声与Sink影响，使PAD成为比静态图更可靠的核心区域指示器。

### MAD缩放与系统Token补偿

PAD注入注意力Logits而非Softmax后概率，以避免额外计算开销。然而Logits中存在由Sink引起的极端离群值，导致固定干预系数 $\lambda$ 产生不一致的扰动幅度。PADE采用中位数绝对偏差（MAD）进行每头自适应缩放，设 $Z_{l,h}^{[v]}$ 为第 $l$ 层第 $h$ 头视觉Logits，MAD计算为：

$$ MAD_{l,h} = \text{median}(|Z_{l,h}^{[v]} - \text{median}(Z_{l,h}^{[v]}|) $$

缩放后的PAD为 $PAD_{scaled} = PAD \times MAD_{l,h}$。直接增强视觉注意力会挤占指令与历史输出的注意力，损害长文本生成连贯性。PADE引入系统Token补偿（STC），利用高注意力但语义无关的系统Token作为补偿源，调整系统Token Logits：

$$ Z_{[s]}' = Z_{[s]} - \lambda \cdot PAD_{scaled} $$

最终注意力权重由调整后的Logits计算，从而在增强视觉接地的同时，保持对复杂指令与历史输出的注意力分配。

## 实验评估

实验在POPE、CHAIR、HallusionBench、AMBER及MME等基准上评估LLaVA-1.5、InstructBLIP、Qwen-VL等模型。基线覆盖对比解码（VCD, PAI）、辅助模型（HALC, AGLA）及静态信号（OPERA, VAF, VAR），但缺失表征空间编辑类强基线（如HulluEdit, Nullu）。

| 模型 | 方法 | POPE Random Acc (%) | CHAIRs | MME Perception |
| :--- | :--- | :--- | :--- | :--- |
| LLaVA-1.5 | Vanilla | 84.63 | 55.1 | 1508.97 |
| LLaVA-1.5 | VCD | 84.99 | 54.4 | 1515.01 |
| LLaVA-1.5 | PADE | 86.96 | 48.6 | 1520.68 |
| LLaVA-Next | PADE | 86.24 | 27.8 | - |

PADE在LLaVA-1.5上POPE Random准确率达86.96%，较VCD提升1.97个点；CHAIRs降至48.6，较VCD的54.4降低5.8个点。在MME Perception上，PADE得分1520.68，高于VCD的1515.01，表明其在抑制幻觉的同时未损害通用感知能力。

消融实验显示，移除MAD缩放导致CHAIRs从48.6升至54.9，移除STC导致CHAIRs升至49.2，证明MAD对极端值的鲁棒性校准与STC对指令注意力的保护均不可或缺。在LLaVA-1.5-13B上，PADE的CHAIRs为47.3，较7B版本略有改善，但提升幅度有限。

评估边界方面，论文未报告置信区间，且CHAIRs指标（48.6）显著高于领域综述中提到的最新SOTA（如HTDC的11.6），这可能源于骨干模型差异或解码策略不同。代码未开源，超参数 $\lambda=0.1$ 为固定值，缺乏自动化搜索机制。

## 关联研究分析

从方法设计看，PADE与VCD的核心差异在于信号来源与计算开销。VCD依赖外部扰动输入构建负样本，引入多前向传播开销及扰动偏差；PADE利用内部层间动态，实现单次前向传播。然而，PADE的PAD信号依赖于层间注意力的正增量，这在视觉信息模糊或Sink严重干扰时是否仍能准确定位核心区域，论文未提供定量分析。与静态方法OPERA相比，PADE通过动态增量规避了Top-K选择对Sink的敏感性，但MAD缩放引入了额外的中位数计算，虽开销小，但在实时性要求极高的场景下是否优于简单的阈值截断，尚需对比。

从问题动机看，PADE与HulluEdit均追求细粒度干预，但路线不同。HulluEdit在激活空间进行子空间编辑，依赖对幻觉子空间的准确定位；PADE在注意力Logits层注入动态信号，更易于解释但干预精度可能受限。PADE未对比HulluEdit等表征编辑方法，无法直接判断注意力动态增强与激活子空间编辑在细粒度幻觉（如属性、关系）上的优劣。此外，PADE的STC模块假设系统Token语义无关，但在某些复杂指令场景下，系统Token是否可能携带关键上下文信息，论文未探讨。

## 总结

PADE旨在解决推理时干预中静态注意力信号受Sink干扰及对比解码高开销的矛盾。其切入点在于发现层间正注意力动态能更可靠地揭示语义核心区域，从而在单次前向传播中实现精准增强。方法通过PAD提取、MAD缩放与STC补偿，在LLaVA-1.5上实现POPE Random 86.96%与CHAIRs 48.6，同时保持MME Perception 1520.68的通用能力。然而，其CHAIRs指标仍显著高于最新解耦解码策略，且缺乏对表征编辑类方法的对比。当视觉输入极度模糊或Sink干扰严重时，PAD信号是否仍能稳定定位核心区域，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15556)