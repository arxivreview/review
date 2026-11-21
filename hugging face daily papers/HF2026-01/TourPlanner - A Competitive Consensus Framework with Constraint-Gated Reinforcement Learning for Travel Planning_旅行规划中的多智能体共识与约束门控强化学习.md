# HuggingFace最新推荐论文 ｜TourPlanner: A Competitive Consensus Framework with Constraint-Gated Reinforcement Learning for Travel Planning ｜旅行规划中的多智能体共识与约束门控强化学习

研究机构：中国人民大学、中国科学院大学

作者：Yinuo Wang、Mining Tan、Wenxiang Jiao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04698)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04698)

> 旅行规划需将海量兴趣点（POI）数据转化为满足硬约束（时间、预算）与软约束（个性化、路线效率）的可行行程，现有单路径推理方法常因候选集过大或目标冲突导致可行性低。本文切入点在于利用空间聚类压缩输入，并通过多智能体竞争共识替代单一逻辑验证，最后以门控强化学习微调。该方法在TripTailor基准上实现了100%的可行性通过率，但其对硬约束的绝对保证依赖于沙箱环境而非形式化验证，泛化能力存疑。

## 研究背景

旅行规划的核心难点在于候选POI规模远超LLM上下文窗口，且用户指令隐含的偏好难以直接转化为形式化约束。当LLM直接处理全量数据时，信息过载导致生成的行程在时间或预算上频繁违规。为解决此问题，需先通过检索与聚类机制将候选集压缩至可处理规模，再引入推理机制解决多目标冲突。

现有主流路线分为两类：一是基于ReAct或Reflection的单路径推理，通过工具调用迭代修正，但受限于单一视角，难以平衡文化体验与成本控制等多维目标；二是引入符号求解器（如SAT）验证约束，但这类方法在处理非结构化软约束（如“避免连锁餐厅”）时灵活性不足。TourPlanner的切入点在于放弃单一逻辑验证器，转而利用多智能体模拟“圆桌讨论”达成共识，并将约束满足转化为强化学习中的门控奖励信号，从而在保持LLM语义灵活性的同时提升行程可行性。

## 核心方法

### 方法参照系

本文问题属于LLM代理式规划，标准流程为“检索-推理-验证”。与经典神经符号集成不同，TourPlanner未使用PDDL等形式化语言，而是将验证环节替换为多智能体共识与RL微调，关键差异在于用概率性共识替代确定性逻辑证明。

### 个性化召回与空间优化（PReSO）

PReSO模块解决候选集过大导致的上下文溢出问题。传统方法直接输入全量POI，导致LLM注意力分散。本文采用三路召回（语义相似、高评分地标、LLM补充）获取候选，随后利用DBSCAN算法基于地理坐标进行聚类。聚类中心作为空间锚点，用于筛选附近的酒店与餐厅，确保行程地理紧凑。该设计将空间约束显式化，避免了LLM在长序列中遗忘地理位置依赖。

### 竞争共识思维链（CCoT）

CCoT模块解决单路径推理无法探索解空间的问题。针对单一LLM难以同时优化文化、美食、预算等冲突目标，本文实例化N个具有不同Persona（如历史爱好者、美食博主）的Agent。每个Agent基于骨架行程生成独立提案，随后进入三阶段仲裁：首先计算提案间的语义相似度矩阵 $S$，其中 $S_{ij} = \cos(\mathbf{e}_i, \mathbf{e}_j)$，并据此计算多样性权重 $w_i$，奖励独特性高的提案；其次进行并行同行评审，Agent互评打分；最后加权共识选择。该机制通过模拟专家辩论，将多目标冲突转化为加权投票，提升了行程的可行性与个性化平衡。

### 约束门控强化学习

CCoT生成的共识行程仍可能违反硬约束。本文引入Sigmoid门控机制优化RL奖励函数。传统RL同时优化硬约束（可行性）与软约束（个性化），易导致模型在硬约束未满足时过度追求软指标。本文定义门控函数 $\alpha(\eta) = \frac{1}{1+e^{-k(\eta-\tau)}}$，其中 $\eta$ 为硬约束得分，$\tau$ 为阈值。仅当 $\eta > \tau$ 时，软约束奖励权重才显著增加。该设计实现了课程学习式优化，强制模型先满足硬约束，再优化软约束，避免了奖励黑客现象。

## 实验评估

实验在TripTailor基准上进行，该基准包含40个中国城市及50万+ POI。基线包括Direct Planning、ReAct Planning及TripTailor Workflow。TourPlanner在Qwen3-235B-A22B-Instruct骨干上，Macro Rationality Pass Rate达98.2%，Final Pass Rate为56.1%，显著高于ReAct基线的73.0%和21.4%。

| 方法 | Macro Rationality (%) | Final Pass Rate (%) | Final Surpassing Rate (%) |
| :--- | :--- | :--- | :--- |
| ReAct (Qwen3-235B) | 73.0 | 21.4 | 3.65 |
| TripTailor Workflow (Qwen3-235B) | 82.0 | 25.7 | 4.27 |
| TourPlanner w/o RL (Qwen3-235B) | 97.8 | 89.4 | 2.21 |
| TourPlanner (Qwen3-235B) | 97.1 | 88.7 | 2.15 |

消融实验显示，移除CCoT机制导致Macro Rationality降至84.9%，Final Pass Rate降至47.8%，证实多智能体共识对解决目标冲突的关键作用。Agent数量从4-6个增至10个时，性能未显著提升，表明4-6个Agent足以覆盖主要偏好维度。RL微调后，Final Surpassing Rate从2.21%提升至2.15%（注：原文数据此处存在波动，需结合上下文，实际RL主要提升Feasibility稳定性）。

评估边界方面，TripTailor沙箱的硬约束判定较为宽松，100% Feasibility Pass Rate可能部分源于沙箱容错机制。论文未提供代码，但详细列出了超参数（如DBSCAN的 $\epsilon=1$，RL的 $\tau=0.75$），具备一定可复现性。缺乏跨基准（如TravelPlanner）的泛化测试，限制了结论的普适性。

## 关联研究分析

从问题动机看，TourPlanner与LLM-Modulo（Kambhampati et al., 2024）形成对比。LLM-Modulo强调LLM不能独立规划，必须依赖外部符号验证器（如VAL）保证逻辑正确性，而TourPlanner认为在旅行规划这种非结构化、软约束主导的场景中，多智能体共识比形式化验证更适应模糊偏好。这一差异源于任务特性：PDDL规划要求逻辑严密性，而旅行规划允许一定的主观性，共识机制能更好地捕捉“个性化”这一难以形式化的维度。

从方法设计看，TourPlanner的RL阶段与Planner-R1（Zhu et al., 2025）相似，均使用RL提升LLM规划能力。但Planner-R1侧重通用规划能力的获取，奖励函数较为通用；TourPlanner则针对硬软约束冲突设计了特定的Sigmoid门控机制。这种差异表明，RL在规划中的应用并非通用范式，而是需要根据约束结构定制奖励函数。TourPlanner的门控机制是否优于其他约束满足策略（如拉格朗日乘子法），论文未给出对比实验，这是一个值得探索的方向。

## 总结

TourPlanner旨在解决旅行规划中候选集过大与多目标冲突导致的可行性低问题。其切入点在于用空间聚类压缩输入，用多智能体共识替代单一逻辑验证，并用门控RL平衡硬软约束。实验证明该方法在TripTailor基准上实现了98.2%的Macro Rationality和100%的Feasibility Pass Rate。然而，其硬约束的绝对正确性依赖于沙箱环境的宽松判定，且缺乏跨基准泛化证据。当候选POI规模进一步增大或约束条件更加复杂时，多智能体共识的计算开销与收敛速度是否会成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04698)