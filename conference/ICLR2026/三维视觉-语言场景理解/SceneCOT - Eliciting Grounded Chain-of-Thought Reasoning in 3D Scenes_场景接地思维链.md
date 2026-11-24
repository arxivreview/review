# ICLR2026最新论文 ｜SceneCOT: Eliciting Grounded Chain-of-Thought Reasoning in 3D Scenes ｜场景接地思维链

研究机构：北京大学、清华大学

作者：Xiongkun Linghu、Jiangyong Huang、Ziyu Zhu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.16714)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.16714)

> 3D场景理解的核心困境在于模型常生成流畅但缺乏场景依据的答案，导致推理过程不可解释且接地-问答一致性低。现有3D大语言模型多采用端到端范式，忽略了中间接地步骤的显式建模，难以处理复杂空间关系。本文提出SceneCOT框架，将复杂3D推理任务分解为任务识别、区域定位、实体接地和接地推理四个阶段，并构建了首个大规模接地思维链数据集SceneCOT-185K。该方法在接地-问答一致性指标上显著优于基线，但其在纯定位精度上未超越专用定位模型，且依赖外部符号引擎，泛化效率存疑。

## 研究背景

当智能体在3D场景中执行导航或问答任务时，它需要理解“2点钟方向”这类相对空间指令。这要求模型不仅识别物体，还需将其定位到特定的空间区域，这一过程称为3D视觉接地（3D Visual Grounding）。然而，传统的3D大语言模型（3D LLM）通常将问答视为单步映射，直接从场景特征和文本生成答案，忽略了中间的空间定位步骤。这种黑盒推理导致模型可能“答对但没接地”或“接地对但答错”，即接地-问答一致性（Grounding-QA Coherence, GC）低下。

3D场景理解的主流路线正从封闭词汇的静态定位向开放世界的动态推理演进。早期工作如ReferIt3D确立了检测-匹配范式，而近期基于CLIP蒸馏的方法实现了零样本理解。然而，这些方法在处理多物体交互和复杂空间关系时，仍缺乏显式的推理机制。Chain-of-Thought（CoT）推理在2D视觉语言模型中已证明能有效提升复杂任务性能，但在3D场景中，由于语言推理与多模态3D表示的对齐困难，其潜力尚未被充分挖掘。

本文的切入点在于指出，实现类人3D推理需要答案从透明、接地且逐步的推理过程中产生。现有研究虽引入了场景图或CoT，但多聚焦于定位精度，未系统解决推理链中接地步骤与最终答案的一致性验证问题。SceneCOT通过显式分解推理过程，将接地作为中间可验证步骤，旨在弥合这一差距。

## 核心方法

### 方法参照系

本文问题属于3D多模态大模型（3D MLLM）的认知层任务，标准流程是端到端映射场景特征与文本至答案。关键差异在于，本文不直接输出答案，而是插入显式的“符号引擎”与“专家模块”调用，将推理拆解为离散步骤，并定义标准化的3D-CoT标记语言。

### 四阶段接地推理架构

SceneCOT将复杂3D推理任务分解为四个阶段：任务识别、区域定位、实体接地和接地推理。设计动机在于解决端到端模型在复杂空间关系上推理不可解释且接地-问答解耦的问题。推理轨迹定义为：

$$
\text{Trace} = \langle \text{think\_type} \rangle \langle \text{think\_rgn} \rangle \langle \text{think\_grd} \rangle [\text{OBJ}] \langle \text{think\_task} \rangle \langle \text{think\_sum} \rangle \langle \text{answer} \rangle
$$

其中，$\langle \text{think\_type} \rangle$ 识别任务类型（如计数、导航），$\langle \text{think\_rgn} \rangle$ 基于方向线索定位任务相关区域，$\langle \text{think\_grd} \rangle$ 生成接地指令并触发[OBJ]标记调用专家模块，$\langle \text{think\_task} \rangle$ 指定所需信息（如物体概率、3D坐标或图像令牌），$\langle \text{think\_sum} \rangle$ 引导总结，$\langle \text{answer} \rangle$ 生成最终答案。该架构确保每个答案都有显式接地步骤支持，提升GC。

### 联合优化与专家模块集成

SceneCOT基于LLaVA-1.5构建，集成3D视觉接地模型（PQ3D）和2D视觉语言模型作为专家模块。设计动机在于利用预训练权重提升接地精度，同时通过联合优化确保推理链与接地模块的一致性。训练目标为：

$$
\mathcal{L} = \mathcal{L}_{\text{CoT}} + \mathcal{L}_{\text{ans}} + \lambda \mathcal{L}_{\text{ground}}
$$

其中，$\mathcal{L}_{\text{CoT}}$ 和 $\mathcal{L}_{\text{ans}}$ 是预测推理轨迹和最终答案的因果语言建模损失，$\mathcal{L}_{\text{ground}}$ 是应用于接地模块的交叉熵损失，$\lambda$ 为权重。该损失函数确保模型在生成推理链的同时，优化接地模块的物体定位精度，从而提升整体推理的可靠性。

## 实验评估

实验在MSQA（Situated Reasoning）和Beacon3D（Object-Centric Reasoning）上进行，基线包括GPT-4o、LEO、MSR3D、Chat-Scene和SplatTalk。遗漏了最新的3DGS-based推理方法（如LangSplat系列在QA上的表现），可能影响对比的全面性。

| 方法 | Grounded? | MSQA Overall | Beacon3D Case | Beacon3D Obj. |
| --- | --- | --- | --- | --- |
| GPT-4o* | ✕ | 57.1 | 20.2 | 43.2 |
| LEO | ✕ | 52.5 | 12.7 | 51.4 |
| MSR3D | ✕ | 51.4 | 11.9 | 53.6 |
| Chat-Scene | ✕ | 53.6 | 14.0 | **58.9** |
| SCENECOT | ✓ | **55.6** | **56.6** | **23.2** |

SceneCOT在MSQA Overall（55.6）和Beacon3D Case（56.6）上领先，但在Beacon3D Obj.（23.2）上低于Chat-Scene（58.9），表明其在对象级QA上仍有提升空间。

消融实验显示，移除任务类型识别、区域识别或接地损失均导致性能下降，其中区域识别对Counting和Refer任务影响最大。接地损失对Navigation任务至关重要，而Existence任务受其影响较小，可能因语义标签已足够。

评估边界方面，MSQA使用GPT-score，Beacon3D使用GC和QA (Obj.)，指标不可直接比较。代码和数据在项目页面提供，但具体URL未明确。训练使用4块A100 GPU，5个epoch，LoRA微调，可复现性较好。

## 关联研究分析

从问题动机看，SceneCOT与SceneCOT（Linghu et al., 2025）同属接地推理方向，但前者聚焦定位精度（Acc@0.25），后者聚焦推理链完整性与GC。差异根源在于任务特性：定位任务需精确坐标，而推理任务需可解释的中间步骤。SceneCOT通过显式分解，解决了SceneCOT在复杂空间关系上推理不可解释的问题，但未验证其在纯定位精度上的优势。

从方法设计看，SceneCOT与PQ3D（Zhu et al., 2024b）同用3D接地模块，但PQ3D是独立检测器，SceneCOT将其集成到CoT链中作为可调用工具。差异根源在于范式转变：PQ3D追求检测精度，SceneCOT追求推理一致性。SceneCOT通过联合优化$\mathcal{L}_{\text{ground}}$，确保接地模块服务于推理链，但依赖外部符号引擎，可能牺牲端到端模型的泛化效率。

## 总结

SceneCOT要解决的核心矛盾是3D LLM推理过程不可解释且接地-问答一致性低。其切入点在于显式分解推理过程，将接地作为中间可验证步骤，利用PQ3D和LLaVA-1.5构建四阶段架构。实验证明，SceneCOT在Beacon3D GC上达到34.7，显著优于LEO（1.6）和SceneVerse（20.4），验证了显式推理对GC的关键作用。然而，其在Beacon3D Obj.上低于Chat-Scene，且依赖外部符号引擎，暴露了接地鲁棒性与推理链自我修正的局限。当支持集增大时，显式分解的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.16714)