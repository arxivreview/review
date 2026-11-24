# ICLR2026最新论文 ｜A$^2$Search: Ambiguity-Aware Question Answering with Reinforcement Learning ｜歧义感知强化学习问答

研究机构：香港城市大学、阿里巴巴集团

作者：Fengji Zhang、Xinyao Niu、Chengyang Ying 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07958)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07958)

> 开放域问答（Open-Domain QA）的核心矛盾在于模型需同时具备精准推理与有效检索能力，但现有基准普遍假设单一金标答案，导致强化学习（RL）训练信号失真。主流RL智能体方法（如ReSearch）仅奖励匹配单一参考答案，系统性低估了模型在真实歧义场景下的能力。本文切入点在于将“歧义”从评测问题转化为训练信号问题，通过自动挖掘替代答案并设计多答案感知的奖励函数进行端到端优化。其价值在于证明了单轮推理即可超越多轮采样的基线，但替代答案挖掘的可靠性与泛化边界仍存疑。

## 研究背景

当模型面对“谁是伊斯兰哲学最具影响力人物的最大思想家之一”这类问题时，不同推理链可能合法地导向不同结论（如George Sarton或Oliver Leaman），但基准仅提供一个金标答案。这种单答案假设导致RL训练中的奖励信号偏差：模型若生成证据支持的替代答案，会被错误惩罚，从而抑制其探索多解的能力。这一困境在强化学习策略优化路线中尤为突出，因为RL依赖环境反馈塑造行为，错误的奖励信号会直接固化模型的单路径推理习惯。

现有RL智能体方法（如Search-R1, ReSearch）通过迭代检索与推理提升多跳问答性能，但其奖励机制仅基于最终答案与单一金标的匹配度。这种设计隐含假设“每个问题有且仅有一个正确答案”，忽略了标注噪声与真实世界歧义的普遍性。AmbigQA等基准虽尝试通过人工标注解决歧义，但成本高且局限于单跳问题，难以扩展至HotpotQA、MuSiQue等多跳数据集。本文的切入点在于：不依赖人工标注，而是利用现有RL模型的轨迹采样能力，自动识别并验证替代答案，将其纳入训练数据，从而在RL循环中直接优化模型对歧义的感知与多答案生成能力。

## 核心方法

### 方法参照系

本文问题属于RL智能体问答框架，标准流程为：模型通过工具调用迭代检索，生成轨迹，基于最终答案匹配度计算奖励并更新策略。关键差异在于：标准流程假设单答案，而本文需处理多答案场景，且替代答案需自动挖掘而非人工提供。

### 替代答案自动挖掘

设计动机：人工标注歧义答案成本高且不可扩展，需自动化管道从现有模型轨迹中提取可靠替代答案。本文采用四步流程：采样（Sampling）、过滤（Filtering）、验证（Verification）、分组（Grouping）。采样阶段使用5个RL搜索模型（ReSearch-7B/32B, Search-R1-7B/14B/32B）对49,938个问题各生成16条轨迹，共3.99M条轨迹。过滤阶段移除与金标语义等价、全错或重复的轨迹，保留208,829条。验证阶段使用4个LLM（Claude 3.5/3.7 Sonnet, OpenAI o3/o4-mini）对候选答案进行证据支持性判断，采用多数投票阈值$\eta=3$，保留19,529条轨迹（9.4%），人工一致率达96%。分组阶段合并语义等价答案，最终为19.0%的问题提供替代答案。该流程的核心在于将“证据支持”作为替代答案入库的硬性门槛，避免引入噪声。

### 多答案感知奖励函数

设计动机：标准RL奖励仅匹配单一金标，无法激励模型生成多个有效答案。本文采用Group Relative Policy Optimization (GRPO) 替代PPO，消除Critic网络，直接从组内采样轨迹估计基线。奖励函数$R(q, \hat{ans})$定义为：

$$
R(q, \hat{ans}) = \begin{cases}
0 & \text{if format invalid} \\
0.1 & \text{if format valid and hits} = 0 \\
1 - \alpha(1 - \text{AnsF1}) & \text{if format valid and hits} > 0
\end{cases}
$$

其中AnsF1基于精确匹配计算，$\alpha \in [0,1]$控制精度-召回平衡。AnsF1定义为：

$$
\text{AnsF1} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

Precision = hits/preds，Recall = hits/refs。该设计通过$\alpha$参数调节：$\alpha=0.8$时奖励紧密耦合AnsF1，抑制过度生成；$\alpha=0.2$时奖励下限0.8，激励多答案覆盖。本文采用$\alpha=0.4$，在验证集上实现精度-召回稳定平衡。

## 实验评估

实验在8个开放域QA基准上进行，包括4个多跳（MuSiQue, HotpotQA, 2Wiki, Bamboogle）和4个通用（NQ, TriviaQA, PopQA, AmbigQA）。基线覆盖Prompt-based（DirectGen, Naive-RAG, Iter-RetGen, IRCoT）、RL-trained（Search-R1, ReSearch, AFM-MHQ）、单答案RL（SinSearch）及歧义专用（AbgSearch）。遗漏图结构方法（如HippoRAG）和效率优化方法（如CompactRAG）。

| 模型 | MuSiQue AnsF1@1 | HotpotQA AnsF1@1 | 2Wiki AnsF1@1 | Bamboogle AnsF1@1 | Macro-Avg AnsF1@1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ReSearch-32B | 46.2 | 45.6 | 25.4 | 22.6 | 46.2 |
| A2SEARCH-7B | 48.4 | 49.5 | 30.1 | 22.6 | 48.4 |
| A2SEARCH-3B | 43.1 | 42.8 | 24.2 | 15.1 | 43.1 |

A2SEARCH-7B在单轮贪心解码下，MuSiQue AnsF1@1达48.4%，超越ReSearch-32B的46.2%；Macro-Avg AnsF1@1为48.4%，较ReSearch-32B提升2.2个点。A2SEARCH-3B达43.1%，仍优于ReSearch-7B的39.3%。

消融实验显示，$\alpha$参数对答案数量影响显著：$\alpha=0.8$时模型收敛至单答案，$\alpha=0.2$时答案数快速增加，$\alpha=0.4$实现稳定平衡。采样温度消融表明，$T=0.6$在召回与F1间取得最佳权衡，ReSearch-7B在$T=0.6$时Recall@3达31.1%。

评估边界：指标限于Exact Match与LMJudge，未报告计算效率（如LLM调用次数、延迟）；替代答案挖掘依赖4个专有LLM验证，可复现性受限于API访问；未在全局聚合任务（计数/极值）上验证多答案奖励的有效性。

## 关联研究分析

从问题动机看，本文与ARCHIVE（Lee et al., 2026）均关注歧义，但ARCHIVE聚焦于歧义检测（区分表面缺陷与知识歧义），而本文聚焦于歧义处理（生成多答案）。差异根源在于任务定位：ARCHIVE旨在提升检测准确性，本文旨在提升生成完整性。本文未探索检测与生成的联合优化，若检测模块能提供更细粒度的歧义类型信息，是否有助于奖励函数的自适应调整，论文未给出回答。

从方法设计看，本文与GTA-RAG（Chen et al., 2026）同属RL策略优化路线，但GTA-RAG采用轨迹级奖励监督中间检索行为，本文采用结果级AnsF1奖励优化最终答案覆盖。差异根源在于奖励粒度：GTA-RAG关注过程忠实性，本文关注结果多样性。本文未分析AnsF1奖励对中间检索策略的影响，若模型为追求多答案覆盖而引入低质量检索路径，是否会导致推理链不稳定，论文未给出回答。

## 总结

本文要解决的核心矛盾是RL训练中单答案假设导致的奖励信号失真，现有方法因依赖人工标注或单金标奖励而无法处理真实歧义。本文抓住的切入点是利用现有RL模型的轨迹采样能力自动挖掘替代答案，并通过AnsF1奖励直接优化多答案生成能力。本文做了什么：构建了四步自动挖掘管道，设计了多答案感知奖励函数，在8个基准上验证了单轮推理超越多轮采样的基线。证明了什么：A2SEARCH-7B在MuSiQue上AnsF1@1达48.4%，超越ReSearch-32B的46.2%；在AmbigQA上超越直接在该数据集训练的AbgSearch。本文的边界在于替代答案挖掘依赖专有LLM验证，且未在全局聚合任务上验证多答案奖励的有效性。当替代答案的验证阈值$\eta$进一步收紧时，训练数据覆盖率与奖励信号可靠性之间的平衡点是否会发生偏移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07958)