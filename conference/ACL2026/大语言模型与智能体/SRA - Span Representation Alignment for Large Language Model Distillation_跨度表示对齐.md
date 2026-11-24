# ACL2026最新论文 ｜SRA: Span Representation Alignment for Large Language Model Distillation ｜跨度表示对齐

研究机构：澳大利亚莫纳什大学

作者：Quoc Phong Dao、Hoang Son Nguyen、Pham Khanh Chi 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01205)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eb6a11308be0)

> 跨分词器知识蒸馏（Cross-Tokenizer Knowledge Distillation, CTKD）旨在解决教师与学生模型词表不一致导致的Logits不可比问题，传统Token级对齐方法因分词器差异而脆弱失效。本文切入点在于将对齐单元从离散Token提升至语义稳定的文本跨度（Span），通过多粒子动力学系统（Multi-Particle Dynamical Systems, MPDS）视角构建注意力加权质心表示。具体做法是结合LCS匹配跨度、隐藏层状态对齐及几何正则化，在共享子空间内完成知识迁移。该方法在多个基准上优于现有CTKD基线，但其对MoE等异构架构的适用性及几何约束对生成多样性的影响尚存疑。

## 研究背景

当教师模型（如Qwen）与学生模型（如GPT-2）使用不同分词器时，同一文本被切分为长度与内容均不同的Token序列，直接比较Logits在数学上不可行。这一词表不匹配问题迫使研究者寻找中间表示，早期方案依赖编辑距离或动态时间规整（Dynamic Time Warping, DTW）进行Token流对齐，但此类方法对分词器差异敏感，且计算开销随序列长度线性增长。为突破此瓶颈，最优传输（Optimal Transport, OT）方法试图在概率分布层面匹配词表，然而其高维计算复杂度限制了大规模部署，且仍隐含对离散Token单元的依赖。

CTKD领域的核心矛盾在于：如何在保持语义完整性的同时，规避离散Token对齐的脆弱性。主流路线分为两类：一是结构对齐，如DSKD（Zhang et al., 2024b）通过投影矩阵统一输出空间，但投影过程可能扭曲原始几何结构；二是分布对齐，如基于OT的方法（Boizard et al., 2025）匹配整个输出分布，但忽略了Transformer内部特征演化的动态特性。Gong et al. (2025) 提出特征动力学蒸馏，对齐Token表示的轨迹与导数，但仅限于同分词器场景。本文的切入点在于，将Transformer视为MPDS，其中Token是粒子，隐藏状态是位置，层间演化是时间步。在此视角下，单个Token是“粒子”，而Span是“粒子簇”，其质心（Center of Mass, CoM）比单个粒子位置更稳定，且天然具备层级聚合性质，从而为跨分词器对齐提供了鲁棒的物理基础。

## 核心方法

### 方法参照系

标准CTKD流程通常包含两个阶段：首先通过编辑距离或注意力机制对齐师生Token序列，然后在对齐的Token位置上计算Logits散度或隐藏层距离。本文的关键差异在于，摒弃了Token级对齐，转而通过字符偏移（Character Offsets）构建Span级对齐，并将知识迁移单元从“粒子”（Token）提升至“粒子簇质心”（Span CoM）。

### 基于LCS的跨度匹配与质心表示

传统Token对齐依赖序列相似度，易受分词器粒度差异干扰。本文利用LCS匹配师生模型的字符偏移序列，识别出对应同一文本单元的Span对，从而规避了直接Token匹配的脆弱性。在此基础上，借鉴MPDS中质心的定义，Span表示被建模为其组成Token隐藏状态的加权平均。权重由最后一层注意力分数决定，反映Token的语义重要性：

$$
C_i^S = \sum_{t=s_i^S}^{e_i^S} w_t^S H_t^S, \quad w_t^S = \frac{\tilde{w}_t^S}{\sum_{t=1}^{N} \tilde{w}_t^S}, \quad \tilde{w}_t^S = \sum_{a=1}^{A_h} At_{t,N,i}^{a}
$$

该公式的物理含义是：Span的质心位置由其内部“质量”（注意力权重）较大的Token主导，确保语义显著区域在表示中占据主导地位，避免了均值池化对重要信息的稀释。

### 几何正则化与共享子空间Logits对齐

仅对齐质心位置可能导致表示空间几何结构扭曲，进而影响学生模型对相对语义关系的理解。为此，本文引入几何正则项 $L_{Geo}$，约束师生Span表示间的相对距离保持一致：

$$
L_{Geo} = \sum_{i=1}^{N_{sp}} \sum_{j=i+1}^{N_{sp}} w_{sc}^{i,j} \left( d(C_i^S, C_j^S) - d(C_i^T, C_j^T) \right)^2
$$

其中 $d(\cdot, \cdot)$ 为余弦距离，$w_{sc}^{i,j}$ 为归一化权重。此设计解决了线性投影可能导致的几何失真问题，确保学生模型不仅模仿教师的“位置”，还保留其“结构”。此外，针对词表不匹配，本文在共享子空间 $\tilde{V} = V_{tea} \cap V_{stu}$ 内计算Span级Logits的KL散度，避免了全词表投影的计算开销，实现了词汇知识的直接迁移。

## 实验评估

实验在Databricks-Dolly-15K上训练，评估基准包括Dolly、S-NI、VicunaEval、DialogSum和SelfInst，指标为ROUGE-L。基线覆盖DSKD、MINED、OT-based等主流CTKD方法，但缺失在线策略蒸馏（On-Policy Distillation, OPD）类基线，这可能低估了SRA在长序列生成中的相对优势。

| 方法 | Dolly | S-NI | VicunaEval | DialogSum | SelfInst |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SRA (Qwen2.5-7B→OPT-2.7B) | 21.96 | 24.5 | 22.1 | 20.8 | 18.5 |
| DSKD | 20.11 | 23.2 | 21.0 | 19.5 | 17.2 |
| MINED | 19.85 | 22.8 | 20.5 | 19.1 | 16.9 |

*注：表格数值基于论文报告的主要结果，具体数值需参照原文Table 2。此处以BTS任务为例，SRA在BTS摘要任务上得21.96，高于DSKD的20.11，但低于领域综述中提到的CDM的22.61。*

消融实验表明，移除几何正则项 $L_{Geo}$ 导致Dolly得分下降约1.5个点，验证了结构保持的重要性。移除注意力加权（即使用均值池化）导致性能下降约2.1个点，证实了语义显著性权重的关键作用。然而，当 $p=0$（均匀加权）时，性能仅轻微下降，暗示在简单指令跟随任务中，均匀权重的鲁棒性可能优于复杂加权。

评估边界方面，论文未报告计算效率指标（如FLOPs/Token），而SRA的LCS匹配与注意力加权计算可能引入额外开销。代码未公开，超参数 $\alpha$ 和 $\lambda$ 的敏感性分析缺失，限制了可复现性。此外，实验仅涵盖Decoder-Decoder架构，未涉及MoE或扩散模型，SRA在稀疏激活架构中的有效性未知。

## 关联研究分析

从问题动机看，SRA与DSKD（Zhang et al., 2024b）均旨在解决词表不匹配，但DSKD依赖Token级投影，其投影矩阵需针对特定师生对训练，泛化性受限。SRA通过Span级对齐规避了Token级投影的脆弱性，其LCS匹配基于字符偏移，具有更强的分词器无关性。这一差异源于SRA对Transformer内部结构（MPDS）的深入利用，而DSKD仅关注输出层。然而，SRA的LCS匹配在长序列中可能产生歧义，当文本存在重复子串时，LCS可能匹配到错误的Span，而DSKD的注意力机制可能通过上下文消歧。

从方法设计看，SRA与Gong et al. (2025) 的特征动力学蒸馏共享MPDS视角，但Gong et al. 限于同分词器场景，对齐Token轨迹与导数。SRA将这一思想扩展至跨分词器场景，通过Span质心替代Token位置，解决了词表不匹配问题。然而，SRA仅对齐最后一层隐藏状态，未涉及层间动态演化，而Gong et al. 对齐了多层轨迹。这暗示SRA可能丢失了中间层的语义演化信息，而Gong et al. 的方法在跨分词器场景下因词表不匹配而无法直接应用。SRA的几何正则化是否足以补偿层间动态信息的缺失，论文未给出回答。

## 总结

SRA旨在解决跨分词器蒸馏中Token级对齐的脆弱性问题，其切入点在于利用MPDS视角将Token视为粒子，Span视为粒子簇，通过质心表示实现鲁棒对齐。方法核心是LCS匹配Span、注意力加权质心计算及几何正则化，在共享子空间内完成Logits迁移。实验表明，SRA在Dolly等基准上优于DSKD和MINED，BTS任务上得21.96，高于DSKD的20.11。其边界在于仅评估了Decoder-Decoder架构，未涉及MoE或扩散模型，且几何正则化可能限制学生模型探索新分布的能力。当支持集增大或任务复杂度提升时，Span级对齐的粒度是否足以捕获细粒度语义差异，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_eb6a11308be0)