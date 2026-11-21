# ACL-Findings2026最新论文 ｜MCLE-Mol: Empowering LLM with Molecular Comprehension and Low-Cost Continual Evolution for Interpretable Property Prediction ｜分子性质预测中的语义鸿沟与可解释性：MCLE-Mol 框架

作者：Zhili Pu、Lantian Zhang、Hao Duan 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4f0ce91506f)

> 导读 分子性质预测（Molecular Property Prediction, MPP）旨在从分子结构推断生物活性或毒性，是AI辅助药物发现的核心环节。图神经网络（Graph Neural Networks, GNNs）虽精度高但缺乏可解释性，而大语言模型（Large Language Models, LLMs）虽能生成解释却常因语义鸿沟导致幻觉与性能下降。MCLE-Mol通过注入机器学习（Machine Learning, ML）模型产生的子结构归因值，并引入上下文校准子结构归因规则（Context-Calibrated Substructure Attribution Rules, CCSAR）动态修正统计偏差，实现了性能与可解释性的平衡。该框架在BACE和BBBP上超越了部分专用GNN模型，但在HIV等大规模数据集上仍落后于全量训练的专家模型，其规则库的长期演化稳定性尚待验证。

## 研究背景

MPP任务要求模型捕捉结构-活性关系（Structure-Activity Relationships, SAR），即局部子结构对宏观性质的贡献。传统GNN通过消息传递机制聚合原子与键信息，虽在MoleculeNet基准上表现优异，但其黑盒特性导致预测结果无法被化学家追溯至具体结构单元。LLM提供了生成自然语言解释的路径，但自然语言与分子拓扑图之间存在显著的语义鸿沟，导致LLM难以准确捕捉SAR，常将统计共现误读为化学原理，产生幻觉推理。

当前主流LLM-MPP路线分为两类：一是多模态对齐，将图特征直接注入LLM嵌入空间（如InstructMol）；二是检索增强生成（Retrieval-Augmented Generation, RAG），通过检索相似分子案例辅助推理（如MolRAG）。然而，这两类方法均依赖数据中的统计规律，忽略了目标分子的具体化学上下文。例如，硝基基团在多数情况下增加毒性，但在特定电子环境或空间位阻下其影响可能反转。这种“统计关联≠化学原理”的偏差限制了LLM的预测可靠性与解释可信度。MCLE-Mol的切入点在于引入外部ML模型的归因信号作为“物理锚点”，并通过规则库动态校准，使LLM在特定化学上下文中进行机制驱动的推理，而非依赖全局统计模式。

## 核心方法

### 方法参照系

标准LLM-MPP流程通常将分子SMILES或图特征直接输入LLM进行端到端预测或RAG检索。本文的关键差异在于引入了一个独立的ML模型（RGCN）作为归因信号源，并构建了外部规则库（CCSAR）作为推理时的动态校准器，而非将结构信息静态嵌入LLM参数或检索库。

### 子结构归因与多模态描述生成

设计动机：LLM缺乏对局部子结构贡献的量化感知，直接输入SMILES无法显式区分哪些原子团对性质影响最大。本文首先利用RGCN模型计算子结构归因值，通过掩码原子特征测量预测变化来量化贡献：

$$ Attr(S) = f(G) - f(G \setminus S) $$

其中 $G \setminus S$ 表示将子结构 $S$ 中所有原子特征置零后的分子图。该值作为“启发式线索”注入提示词，引导教师模型（GPT-4o）聚焦关键药效团。同时，利用RDKit计算LogP、TPSA等物理化学属性作为“物理锚点”，生成1D SMILES、2D图拓扑、3D空间构象的文本描述，确保生成内容严格基于物理事实，从源头抑制幻觉。

### 上下文校准子结构归因规则（CCSAR）

设计动机：ML归因值本身包含统计偏差，直接用于推理可能导致错误校准。CCSAR通过“3W”机制（Who: 子结构本身, Where: 拓扑位置, With Whom: 周围环境）动态校准归因值。规则提取采用“知识冲突”策略，故意绕过预测有效性验证，以对抗LLM的参数记忆偏差。检索机制借鉴HyDE，将分子关键子结构转化为自然语言查询，与规则库中的触发条件计算语义相似度，获取Top-k规则。最终，LLM在CCSAR指导下生成校准后的推理轨迹（CCRT），实现从“统计关联”到“机制推理”的转变。

## 实验评估

实验基于MoleculeNet的BACE、BBBP、HIV、Tox21四个基准，使用Qwen3-8B作为骨干，LoRA微调。基线涵盖GNN专家模型（Graphormer-p, DMP, GEM等）和LLM通用模型（InstructMol, MolRAG, M2LLM等）。

| 模型 | BACE | BBBP | HIV | Tox21 | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DMP (TF+GNN) | 0.8940 | 0.7780 | 0.8140 | 0.7910 | 0.8192 |
| Graphormer-p | 0.8575 | 0.7163 | 0.7788 | 0.7729 | 0.7813 |
| InstructMol-GS | 0.8210 | 0.7240 | 0.6890 | - | 0.7446 |
| MolRAG | 0.7225 | 0.5411 | 0.6436 | 0.6393 | 0.6366 |
| **MCLE-Mol** | **0.9178** | **0.8581** | 0.7668 | 0.7596 | **0.8255** |

MCLE-Mol在BACE和BBBP上显著超越所有基线，平均AUROC达0.8255，超过DMP的0.8192。但在HIV（0.7668 vs 0.8140）和Tox21（0.7596 vs 0.7910）上低于DMP，主要因本文仅使用少于1000个样本进行微调，而基线使用全量数据。

| 变体 | BACE | BBBP | HIV | Tox21 |
| :--- | :--- | :--- | :--- | :--- |
| Full | 0.9178 | 0.8581 | 0.7668 | 0.7596 |
| w/o Iterative Evolution | 0.8816 | 0.8081 | 0.7014 | 0.7506 |
| w/o CCSAR | 0.7074 | 0.7729 | 0.6217 | 0.7171 |
| w/o ML Attribution | 0.5134 | 0.5827 | 0.5261 | 0.5968 |

消融实验显示，移除ML归因导致性能崩溃（BACE降至0.5134），证明归因信号是核心；移除CCSAR导致BACE下降0.2104，证实上下文校准对消除统计偏差至关重要。迭代进化机制带来约0.03-0.06的增益，表明规则库的持续更新有效。检索参数k=5时性能最佳，k>5时因冗余信息干扰导致性能下降。

评估边界方面，本文未报告置信区间，且HIV/Tox21的小样本设置限制了与全量基线的公平比较。代码已开源，超参数（lr=1e-4, epochs=10, k=5）明确，但CCSAR规则库的初始规模与更新频率未详细披露，可能影响可复现性。

## 关联研究分析

从问题动机看，MCLE-Mol与MolRAG（Xian et al., 2025）均旨在通过外部知识增强LLM的分子理解，但MolRAG依赖静态检索相似分子案例，易受数据分布偏差影响；MCLE-Mol则通过ML归因值提供动态、量化的结构线索，并引入CCSAR进行上下文校准，解决了“统计关联误读为化学原理”的核心问题。这一差异源于任务特性：MPP需要精确的局部结构贡献量化，而非全局相似性匹配。

从方法设计看，MCLE-Mol与InstructMol（Cao et al., 2025）同属LLM-MPP框架，但InstructMol通过多模态对齐将图特征直接注入LLM，依赖端到端学习捕捉SAR；MCLE-Mol则采用“ML-LLM-Rule”协作范式，将结构感知任务解耦给ML模型，LLM专注推理与解释。这种解耦设计降低了LLM的学习难度，但引入了ML模型归因值的准确性依赖。若RGCN归因值本身存在系统性偏差，CCSAR的校准能力是否足以完全纠正，论文未给出量化分析。

## 总结

MCLE-Mol旨在解决MPP中性能与可解释性的权衡矛盾，通过引入ML归因值作为物理锚点，并利用CCSAR动态校准统计偏差，使LLM在特定化学上下文中进行机制推理。实验证明其在BACE（0.9178）和BBBP（0.8581）上超越专用GNN模型，且仅需少于1000个样本即可达到竞争力。然而，其在HIV和Tox21上的性能落后于全量训练的DMP，暴露了小样本微调与规则库泛化能力的局限。当化学空间持续演化时，CCSAR规则库的规模上限与检索效率如何平衡，以及规则库污染对长期预测稳定性的影响，仍是亟待验证的关键问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_f4f0ce91506f)