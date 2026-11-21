# HuggingFace最新推荐论文 ｜Root-Cause Attribution Is a Search Problem: Continual Search for Long-Horizon Agent Failures ｜长程智能体故障归因的持续搜索机制

作者：Harsh Raj、David Lee、Anas Mahmoud 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.13463)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.13463)

> 长程AI智能体执行日志的根因分析（Root Cause Analysis, RCA）面临证据稀疏且分布不均的挑战，导致传统单次LLM判断易陷入过早承诺。现有方法依赖一次性推理或独立重采样，无法在海量未读证据中有效定位故障源头。本文提出Continual Search，通过多轮迭代提示强制裁判模型探索未读证据，将RCA重构为主动搜索问题。该方法在长日志基准上显著提升了归因准确率，但其在短轨迹场景下的负迁移效应及模型规模与搜索策略的权衡关系仍需进一步厘清。

## 研究背景

当AI智能体执行长程任务时，其产生的执行日志（Execution Logs）往往包含数十万甚至数百万Token，故障线索可能隐藏在早期步骤或分散的工具调用中。这种证据的稀疏性与分布性使得简单的序列匹配失效，要求系统具备在巨大证据空间中排除干扰、定位初始分歧点的能力。这一过程本质上是搜索问题，而非单纯的分类任务。

当前主流RCA方法主要依赖LLM裁判（LLM Judge）对执行轨迹进行单次评估，或通过Self-Consistency等策略进行独立重采样。然而，这些方法假设关键证据能在单次上下文窗口内被充分处理，忽略了长程日志中“未读证据”的存在。随着日志规模扩大，LLM倾向于在早期锁定一个看似合理的故障解释，而忽略后续出现的矛盾证据，导致归因错误。本文的切入点在于识别这一“搜索受限”（Search-limited）特性，即性能瓶颈不在于模型的推理能力，而在于证据获取的广度。

## 核心方法

### 方法参照系

本文基于Agent-as-a-Judge框架，该框架允许LLM通过工具调用检查中间执行状态。标准流程是裁判模型接收完整轨迹或摘要，生成一次性的归因标签。本文的关键差异在于将单次静态判断扩展为多轮动态交互，引入“未读证据”作为核心驱动变量，而非依赖模型内部注意力的自发分配。

### 持续搜索迭代机制

针对LLM过早承诺（Premature Commitment）的问题，Continual Search在每轮迭代中强制裁判挑战当前结论。其核心逻辑可形式化为证据集 $E_t$ 的扩展过程：在第 $t$ 轮，裁判被提示寻找 $E_{t-1}$ 中未覆盖的证据片段 $E_{new}$，并基于 $E_t = E_{t-1} \cup E_{new}$ 重新评估归因。

$$
\text{Prompt}_t = \text{Challenge}(\text{Current\_Hypothesis}, \text{Unread\_Evidence}(E_{t-1}))
$$

该公式的物理含义是：归因结果不再由初始上下文决定，而是由累积的、去重后的证据集决定。通过显式提示“寻找未读工具输出”或“探索未探索分支”，该机制打破了单次推理的局部最优陷阱，迫使模型在后续轮次中主动检索新信息，从而缓解因上下文饱和导致的证据遗漏。

### 被动延续对照设计

为隔离“搜索”与“压力”的影响，本文设计了Passive Continuation作为对照。该机制仅要求裁判重新确认当前结论，不强制探索新证据。其形式化表达为：

$$
\text{Prompt}_t^{passive} = \text{Reconfirm}(\text{Current\_Hypothesis})
$$

这一设计动机在于验证性能提升是否源于“认知压力”导致的标签翻转，还是源于“新证据”的引入。实验表明，Passive Continuation在长日志中表现有限，而在短日志中甚至导致性能下降，证实了Continual Search的有效性依赖于新证据的可用性，而非单纯的重复提示。

## 实验评估

| 基准 | 指标 | Single-turn (GPT-5.5) | Passive (GPT-5.5) | Continual Search (GPT-5.5) |
| :--- | :--- | :--- | :--- | :--- |
| MegaRCA-Mix | F1 | 0.349 | 0.401 | 0.498 |
| TRAIL | Weighted F1 | 0.426 | 0.451 | 0.500 |
| TRAIL | Joint Acc. | 0.156 | 0.189 | 0.257 |
| TELBench | Span Acc. | 0.121 | 0.152 | 0.212 |

实验在MegaRCA-Mix、TRAIL、TELBench、AgentRx和Who&When五个基准上进行，涵盖从2.4K到286K Token的日志规模。基线包括Single-turn、Passive Continuation、Self-Consistency和Heterogeneous Judge Panel。在长日志基准（MegaRCA-Mix, TRAIL, TELBench）上，Continual Search显著优于所有基线，例如在MegaRCA-Mix上，GPT-5.5的F1从0.349提升至0.498。相比之下，Self-Consistency在TRAIL上甚至低于Single-turn（0.135 vs 0.156），证明独立重采样无法解决证据缺失问题。

消融实验揭示了模型规模与搜索策略的交互作用。在TRAIL基准上，GLM-4.7通过Continual Search将Weighted F1从0.268提升至0.473，接近Sonnet-5和Fable-5的水平。Sonnet-5在Turn 4达到0.518，仅消耗约76%的Fable-5计算预算。此外，推理努力（Reasoning Effort）的消融显示，低努力配置在Turn 3即可达到高努力配置的性能，表明长程RCA主要受限于搜索广度而非单轮推理深度。

在短轨迹基准（AgentRx, Who&When）上，Continual Search出现负迁移。GPT-5.5在AgentRx上的F1从0.345降至0.241，Who&When从0.548降至0.452。这是因为短日志中初始判断已覆盖大部分证据，额外轮次仅施加认知压力，导致模型偏离正确标签。评估边界方面，论文未提供代码开源链接，且MegaRCA-Mix仅包含50个样本，统计显著性有限。此外，所有实验均基于特定LLM家族（GPT, Claude, GLM），未验证跨架构泛化性。

## 关联研究分析

从问题动机看，本文与云系统RCA中的StableRCA存在本质差异。StableRCA通过局部马尔可夫毯估计处理静态拓扑下的混淆变量，强调数学上的因果充分性；而Continual Search针对的是动态、非结构化的Agent日志，其核心假设是“证据稀疏性”而非“拓扑不确定性”。StableRCA无法处理文本日志中的语义依赖，而Continual Search不依赖预定义的因果图，这反映了任务特性从结构化指标向非结构化轨迹的迁移。

从方法设计看，本文与Self-Consistency（Wang et al., 2022）形成鲜明对比。Self-Consistency通过多次独立采样投票来降低随机性，假设错误是独立同分布的；Continual Search则通过迭代依赖前一轮结果来扩展证据集，假设错误源于信息缺失。实验证明，在长日志场景下，增加采样次数（Self-Consistency）不如增加证据覆盖（Continual Search）有效，这挑战了“更多计算=更好推理”的常规认知，指出在搜索受限任务中，计算应分配给数据获取而非模型内部推理。

## 总结

本文核心矛盾在于长程Agent日志中证据的稀疏性与LLM单次推理的有限上下文窗口之间的冲突。现有方法因无法主动探索未读证据而失效，本文通过Continual Search机制，将RCA转化为多轮主动搜索过程，强制模型在每轮迭代中获取新证据。实验证明，该机制在MegaRCA-Mix上将GPT-5.5的F1从0.349提升至0.498，且低阶模型配合搜索策略可超越高阶模型。然而，该方法的边界在于其有效性严格依赖于“未读证据”的存在：在短轨迹场景中，由于证据已充分覆盖，迭代搜索反而因认知压力导致性能下降。当执行日志规模进一步缩小至初始上下文窗口可完全容纳的范围时，Continual Search的边际收益是否归零，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.13463)