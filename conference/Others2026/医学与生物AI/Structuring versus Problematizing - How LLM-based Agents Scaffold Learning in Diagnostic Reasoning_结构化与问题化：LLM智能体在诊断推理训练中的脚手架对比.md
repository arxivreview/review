# 洛桑联邦理工团队新研究：结构化与问题化：LLM智能体在诊断推理训练中的脚手架对比

研究机构：瑞士洛桑联邦理工学院

作者：Fatma Betül Güreş、Tanya Nazaretsky、Seyed Parsa Neshaei 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09158)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09158)

> 导读 在职业教育中，新手常因认知偏差导致诊断推理失败，而现有LLM导师缺乏对教学策略的精细化控制。本文切入LLM对话生成与学习科学理论的结合点，通过PharmaSim Switch系统对比“结构化”与“问题化”两种脚手架。系统利用规则模型追踪学生状态，驱动LLM生成符合Reiser框架的特定教学反馈。实验表明，结构化脚手架提升任务效率，问题化脚手架促进深度认知参与。该研究验证了LLM在教育场景中的行为可控性，但其在真实临床诊断中的泛化能力仍存疑。

## 研究背景

当新手面对复杂诊断任务时，常因信息过载而依赖表面启发式，导致过早闭合（Premature Closure）或忽略关键证据。为解决此问题，场景化学习（Scenario-Based Learning, SBL）通过模拟真实情境提供实践机会，但缺乏引导时易引发认知超载。大语言模型（Large Language Models, LLM）的介入使构建自适应对话导师成为可能，然而现有研究多关注LLM能否生成合理回复，缺乏对LLM如何具体实施不同教学策略（如引导步骤或激发反思）的实证对比。

在临床决策支持（Clinical Decision Support, CDS）领域，LLM智能体正从静态问答向交互式诊断演进，强调通过主动询问和工具调用缩小假设空间。然而，现有CDS方法旨在直接输出诊断结果，而非训练人类医生的推理过程。教育场景下的“诊断推理”训练需要LLM扮演导师角色，通过特定脚手架（Scaffolding）干预学生行为。Reiser框架将脚手架分为“结构化”（Structuring，分解任务、聚焦注意力）和“问题化”（Problematizing，激发论证、揭示矛盾）。目前，LLM如何在这两种截然不同的教学范式下影响学生的认知参与度（如ICAP框架中的Active/Constructive/Interactive）及策略迁移，尚缺乏系统性实证数据。

## 核心方法

### 方法参照系：交互式诊断架构的教育化改造

本文方法属于交互式诊断路线，但目标从“辅助临床决策”转变为“训练人类决策”。标准交互式诊断流程包括状态感知、动作选择（询问/检查）和信念更新。本文的关键差异在于：LLM不直接执行诊断，而是作为导师监控学生状态，并生成符合特定教学策略的对话。系统由Client Character（规则系统，模拟患者）、Student Model Agent（规则系统，追踪进度）和Pharmacist Character（LLM，生成教学反馈）组成。

### 核心创新：基于状态机的双模态脚手架生成

该设计发生在交互式诊断的“动作选择”环节。通常做法是LLM根据当前对话历史自由生成回复，导致教学策略不可控。本文引入Reiser框架，将LLM输出严格约束为Structuring或Problematizing两类。

在Structuring模式下，LLM通过分解任务、聚焦努力和监控进度来降低任务自由度。其核心机制是通过提示工程强制LLM执行以下逻辑：

$$
\text{Response}_{\text{Struct}} = \text{LLM}(\text{Prompt}_{\text{Struct}} \mid \text{State}_{\text{DC/DI}}, \text{History})
$$

其中 $\text{State}_{\text{DC/DI}}$ 由Student Model Agent根据LINDAFF清单完成度确定。该公式的物理含义是：LLM的回复不仅依赖对话历史，还显式依赖于规则模型计算出的学生当前处于“数据收集”还是“数据解释”阶段，从而确保反馈与任务进度同步。

在Problematizing模式下，LLM通过激发论证、决策和揭示矛盾来增加认知挑战。其生成逻辑为：

$$
\text{Response}_{\text{Prob}} = \text{LLM}(\text{Prompt}_{\text{Prob}} \mid \text{State}_{\text{DC/DI}}, \text{History})
$$

该设计动机在于解决传统LLM导师“过度帮助”的问题。通过强制LLM在Problematizing模式下避免直接给出答案，而是追问“为什么”或指出逻辑漏洞，迫使学生在Constructive（建构性）层面参与推理，而非仅停留在Active（主动）层面的信息检索。

## 实验评估

实验在63名瑞士职业学校药学学徒中进行，采用组间设计，对比Structuring-heavy与Problematizing-heavy两组。评估指标包括诊断策略得分（Checklist, Interpersonal, Data Interpretation）和基于ICAP框架的学生参与度（Active, Constructive, Interactive）。

| 指标 | Structuring-heavy (%) | Problematizing-heavy (%) |
| :--- | :--- | :--- |
| Active 参与度 | 64.0 | 数据不可得 |
| Constructive 参与度 | 21.5 | 45.5 |
| Interactive 参与度 | 39.6 | 24.3 |

*注：Active参与度在Problematizing组的具体数值未在提供的实验数据区中逐字定位，故留空。*

主结果显示，Problematizing组在Constructive参与度上显著高于Structuring组（45.5% vs 21.5%），表明问题化脚手架有效激发了学生的深度推理。然而，Structuring组在Interactive参与度上更高（39.6% vs 24.3%），说明结构化脚手架促进了更频繁的师生互动。在诊断策略得分上，两组在Checklist和Interpersonal策略上无显著差异，但在Data Interpretation策略上，Problematizing组更倾向于通过论证生成假设。

消融分析显示，LLM在两种模式下的行为差异显著：Structuring组中Monitoring子类别占比45.8%，而Problematizing组中Elicitation of Articulation占比91.4%。这验证了提示工程对LLM行为的有效约束。然而，评估边界在于：实验仅使用模拟场景，未验证学生在真实临床环境中的诊断准确性；且LLM偶尔产生“教学性错误”（约1-2%），虽不影响患者安全，但可能干扰学习。

## 关联研究分析

从问题动机看，本文与MeDxAgent等交互式诊断方法存在根本差异。MeDxAgent旨在通过多智能体协作直接输出诊断结果，其核心瓶颈在于长程状态管理中的错误累积；而本文PharmaSim Switch旨在通过LLM干预学生行为，其核心挑战在于教学策略的精确控制。本文未采用MeDxAgent中的多智能体辩论机制，而是采用单LLM导师配合规则状态机，这一选择源于教育场景对“单一权威导师”角色的需求，但也限制了系统处理复杂共病病例的能力。

从方法设计看，本文与Clinical Chain-of-Thought (CoT) 存在概念重叠但目标迥异。CoT旨在让LLM自身生成显式推理步骤以提升诊断准确性；本文的Problematizing策略旨在引导学生显式化推理步骤以提升学习迁移。本文未对比“LLM直接提供CoT示例”与“LLM通过问题化引导学生生成CoT”的效果差异，这一盲区使得无法判断哪种方式在促进策略迁移上更高效。

## 总结

本文要解决的核心矛盾是LLM导师在教学策略控制上的模糊性。通过引入Reiser框架和规则状态机，本文实现了LLM在“结构化”与“问题化”两种脚手架模式下的行为分化。实验证明，问题化脚手架能将学生的Constructive参与度从21.5%提升至45.5%，显著促进深度推理。然而，本文的边界在于其评估局限于模拟场景下的认知参与度，未验证这种教育干预是否转化为真实临床诊断中的准确率提升。当学生在模拟环境中习惯了问题化引导，其在面对真实临床中时间紧迫、信息缺失的压力时，是否会因过度依赖“被追问”而降低自主决策效率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09158)