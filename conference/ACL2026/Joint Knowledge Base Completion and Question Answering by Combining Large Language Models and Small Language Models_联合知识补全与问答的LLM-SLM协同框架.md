# ACL2026最新论文 ｜Joint Knowledge Base Completion and Question Answering by Combining Large Language Models and Small Language Models ｜联合知识补全与问答的LLM-SLM协同框架

研究机构：美国东北大学

作者：Yinan Liu、Dongying Lin、Sigang Luo 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05875)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05875)

> 知识库问答（KBQA）长期受制于知识图谱（KG）的不完整性，而知识补全（KBC）与KBQA在逻辑上互为因果却常被孤立求解。现有联合方案依赖小语言模型（SLM）导致推理能力受限，或依赖大语言模型（LLM）引发高昂成本与幻觉。JCQL通过双向知识转化机制，将SLM训练的KBC模型嵌入LLM智能体作为动作，同时利用LLM生成的推理路径增量微调SLM。该框架在联合任务设定下显著优于基线，但其KBQA绝对性能低于纯KBQA最优方法，且未验证联合训练是否优于独立训练。

## 研究背景

KBQA旨在利用结构化知识回答自然语言问题，其核心挑战在于KG往往存在大量缺失三元组，导致基于路径检索的推理链断裂。KBC旨在推断KG中缺失的三元组，二者在数据依赖上形成闭环：KBC补全的三元组可修复KBQA的推理路径，而KBQA推理过程中发现的新事实又可作为KBC的训练数据。理解这一闭环需把握两个关键概念：一是LLM的参数化知识虽具备强推理能力，但缺乏对KG schema的严格约束，易产生事实幻觉；二是SLM虽计算成本低且可通过微调吸收结构化知识，但缺乏长程推理与复杂逻辑组合能力。

传统联合KBC与KBQA的研究主要依赖SLM，如BiNet通过共享嵌入空间实现特征交换，但需人工标注推理路径；KGT5将任务建模为序列到序列生成，但忽略了KBQA对KBC的反向增强。随着LLM兴起，直接利用LLM进行迭代推理成为主流，如ToG通过Beam Search探索KG，但面临LLM调用成本高与幻觉问题。JCQL的切入点在于识别LLM与SLM的互补性：LLM能替代人工标注生成高质量推理路径，SLM能缓解LLM的计算开销与幻觉，从而构建双向增强的联合训练框架。

## 核心方法

### 智能体-模型协同架构

JCQL继承ToG的智能体范式，将LLM作为推理主体，通过Thought-Action-Observation循环探索KG。与ToG仅依赖LLM参数化知识不同，JCQL在动作空间中引入SLM训练的KBC模型作为`complete(entity, relation)`动作。该设计解决了LLM在KG缺失区域生成不可靠三元组的问题，通过结构化知识约束LLM的生成边界。

### 双向知识转化机制

KBC→KBQA方向，JCQL将SLM KBC模型嵌入LLM智能体。当LLM执行`complete`动作时，输入头实体与关系，SLM预测尾实体。该过程将KG的显式结构化知识转化为LLM的隐式参数化知识，公式化为：

$$ \hat{t} = \text{SLM}_{\theta}(\text{Enc}(h, r, D_h, T)) $$

其中$D_h$为实体描述，$T$为基于共现分数$S(r, \hat{r})$筛选的上下文三元组。这一机制在LLM推理路径中注入精确的实体预测，直接降低幻觉率。

KBQA→KBC方向，JCQL利用LLM生成的推理路径增量微调SLM。具体而言，以黄金答案为监督，引导LLM生成多路径推理轨迹$C_q$，提取其中正确三元组构建推理子图$G_q$，通过BFS搜索从主题实体到答案实体的路径，最终由LLM筛选最相关三元组$P_q$作为SLM的补充训练数据。该过程将LLM的隐式参数化知识转化为SLM的显式结构化知识，公式化为：

$$ \theta_{new} = \text{IncrFinetune}(\theta_{old}, \{P_q\}) $$

其中$\text{IncrFinetune}$采用增量学习技术避免灾难性遗忘。双向机制形成迭代闭环：SLM增强LLM推理质量，LLM路径反哺SLM补全能力。

## 实验评估

实验在WebQSP与CWQ上进行，KB限制为Wikidata子集，设置30%与50% KB缺失率。基线覆盖ToG、PoG、GoG等智能体方法及KGT5、BiNet等联合方法，但缺失GraphRAG类检索增强基线。JCQL在KBQA任务中，GPT-4o-mini版本在WebQSP 50% KB下Hits@1达0.738，CWQ 50% KB下达0.508，均优于ToG（0.706/0.328）与GoG（0.693/0.477）。

| 方法 | WebQSP (50% KB) | CWQ (50% KB) |
| :--- | :--- | :--- |
| ToG | 0.706 | 0.328 |
| GoG | 0.693 | 0.477 |
| JCQL (GPT-4o-mini) | 0.738 | 0.508 |

消融实验显示，移除`generate`动作后WebQSP Hits@1降至0.722，移除`complete`动作后降至0.696，表明SLM KBC模型对缓解幻觉贡献显著。KBC任务中，JCQL (T5-small)在WebQSP 50% KB下MRR达0.630，优于KGT5（0.543）与BiNet（0.166）。

| 方法 | WebQSP (50% KB) MRR | CWQ (50% KB) MRR |
| :--- | :--- | :--- |
| KGT5 | 0.543 | 0.536 |
| BiNet | 0.166 | 0.178 |
| JCQL (T5-small) | 0.630 | 0.614 |

评估边界方面，论文未报告置信区间，且KBQA性能低于纯KBQA SOTA（如RPO-RAG 89.9），可能因联合任务设定或KB子集限制。代码已开源，超参数统一设置，但SLM增量学习的灾难性遗忘问题未深入探讨。

## 关联研究分析

从问题动机看，JCQL与ToG同属智能体推理框架，但ToG聚焦单次查询的准确性，依赖LLM参数化知识探索KG，而JCQL聚焦KBC与KBQA的联合优化，通过SLM嵌入解决KG缺失导致的推理链断裂。这一差异源于任务特性：ToG假设KG相对完整，而JCQL直面KG不完整问题，SLM作为KBC动作是任务特性迫使的必然选择，而非通用改进。

从方法设计看，JCQL与KGT5同属联合训练范式，但KGT5仅通过共享参数实现KBC到KBQA的知识迁移，忽略反向增强；JCQL通过增量微调实现双向知识转化。这一差异揭示了KGT5的设计盲区：单向迁移无法充分利用KBQA推理过程中发现的新事实。JCQL的增量学习机制虽解决了反向增强，但未验证联合训练是否优于独立训练KBC与KBQA，这一缺失限制了其相对于独立方法的优越性论证。

## 总结

JCQL要解决的核心矛盾是LLM推理成本高与SLM泛化弱在联合KBC与KBQA任务中的不可调和性。其切入点在于识别二者互补性，通过双向知识转化机制实现协同增强。方法上，将SLM KBC模型嵌入LLM智能体作为动作，同时利用LLM推理路径增量微调SLM。实验证明，JCQL在WebQSP 50% KB下KBQA Hits@1达0.738，KBC MRR达0.630，均优于基线。但论文边界在于KBQA绝对性能低于纯KBQA SOTA，且未验证联合训练相对于独立训练的增益。当支持集增大或KB缺失率降低时，SLM嵌入的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05875)