# ICLR2026最新论文 ｜Stop Wasting Your Tokens: Towards Efficient Runtime Multi-Agent Systems ｜监督智能体框架

研究机构：浙江大学、西湖大学

作者：Fulin Lin、Shaowen Chen、Ruishan Fang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26585)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26585)

> 多智能体系统（MAS）在复杂任务中常因错误传播与低效循环导致 Token 消耗激增且鲁棒性下降。现有事后归因方法无法在故障发生前阻断风险，而静态架构优化难以应对动态执行中的上下文噪声。本文提出 SUPERVISORAGENT，一种基于 LLM-free 自适应过滤器的运行时元智能体，通过实时干预纠正错误、引导低效行为并净化观察。该框架在不改变基座智能体架构的前提下实现了效率与鲁棒性的帕累托改进，但其启发式过滤机制在极端对抗场景下的边界尚待验证。

## 研究背景

当 LLM 驱动的 MAS 执行长链任务时，单个智能体的幻觉或工具返回的冗余信息会迅速污染下游推理，形成错误传播。这种传播不仅导致任务失败，更引发智能体陷入重复动作循环或处理超长上下文，造成计算资源浪费。解决这一问题的关键在于识别高风险交互位点，即在 Agent-Agent、Agent-Tool 和 Agent-Memory 之间建立实时监控机制，以在错误固化前进行干预。

MAS 的可靠性是集体属性，错误会在智能体间传播并放大，因此需要专门的错误传播阻断机制。主流研究路线分为事后故障归因与静态架构优化两类。Aegis 和 AgenTracer 等方法专注于任务失败后的根因追溯，属于被动响应；AgentDropout 和 SafeSieve 等则通过剪枝智能体或通信链路在部署前优化效率，属于静态设计。这两类方法均无法捕捉运行时动态产生的低效行为与突发错误。SUPERVISORAGENT 的切入点在于引入运行时过程控制，通过轻量级元智能体在执行过程中实时介入，填补了静态优化与事后归因之间的空白。

## 核心方法

### 监督多智能体系统形式化

本文定义监督多智能体系统（SMAS），即在标准 MAS 中增加一个元层级控制智能体（Supervisor）。监督的基本单元是交互，分为 Agent-Agent、Agent-Tool 和 Agent-Memory 三类。Supervisor 的目标是实时监控这些交互，在不改变核心智能体逻辑的前提下检测并缓解运营风险。这一形式化将监控对象从静态拓扑结构转向动态交互流，明确了监督的介入边界。

### 自适应过滤与上下文窗口

为避免监控所有交互带来的高昂计算开销，SUPERVISORAGENT 引入 LLM-free 自适应过滤器。该过滤器基于启发式规则触发监督，仅当检测到显式错误、低效行为模式或观察长度超标时激活。触发后，Supervisor 访问扩展上下文窗口 $W_{ext}$，其定义为：

$$ W_{ext} = (N, Q_g, Q_l, T_l, S, T_g) $$

其中 $N$ 为被审查智能体名称，$Q_g, Q_l$ 为全局与局部任务，$T_l$ 为局部动作轨迹，$S$ 为最新交互摘要，$T_g$ 为全局交互轨迹。引入 $T_g$ 使 Supervisor 具备超越单个智能体视角的全局视野，从而能识别跨智能体的系统性低效。

### 多级干预动作空间

Supervisor 根据干预上下文 $c \in \{c_{error}, c_{inefficient}, c_{excessive}\}$ 从动作空间 $A$ 中选择特定子集 $A(c)$ 执行干预：

$$ A(c) = \begin{cases} \{correct\_observation, provide\_guidance, run\_verification\} & \text{if } c = c_{error} \\ \{approve, provide\_guidance\} & \text{if } c = c_{inefficient} \\ \{correct\_observation\} & \text{if } c = c_{excessive} \end{cases} $$

该设计动机在于解决此前方法中“一刀切”干预导致的过度修正或干预不足问题。通过区分错误、低效与冗余三种情境，Supervisor 能执行从最小化提示（approve）到深度验证（run_verification）的梯度化干预。例如，在 $c_{excessive}$ 情境下，仅执行观察净化以去除噪声；而在 $c_{error}$ 情境下，可调用子智能体进行外部事实核查。这种分级机制确保了干预强度与问题严重性匹配，避免了因过度干预破坏智能体自主性或因干预不足导致错误扩散。

## 实验评估

实验在 GAIA 验证集及 AIME、GSM8K-Hard、HumanEval、MBPP、DROP 五个基准上进行，基线涵盖 Smolagent、OAgents、MetaAgent、OWL 等主流 MAS 框架。主实验结果显示，SUPERVISORAGENT 在 Smolagent 上实现了显著的 Token 效率提升。

| 方法 | Avg. Acc. | Avg. Tokens (K) | L2 Tokens (K) | L3 Tokens (K) |
| :--- | :--- | :--- | :--- | :--- |
| Smolagent | 50.91 | 527.76 | 619.59 | 691.33 |
| + SMAS (ours) | 50.91 | 371.12 | 404.96 | 489.22 |

在 pass@1 设置下，SMAS 保持准确率不变，平均 Token 消耗降低 29.68%。在更难的 Level 2 和 Level 3 任务上，Token 节省幅度分别达到 34.64% 和 29.23%。跨基准测试中，AIME 解决率提升 6.67% 同时 Token 成本降低 18.92%，HumanEval Token 使用量减少 23.74%。

| 方法 | Avg. Acc. | Avg. Token | L1 Avg. Token | L2 Avg. Token | L3 Avg. Token |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Smolagent | 50.91 | 527,759 | 298,506 | 619,591 | 691,331 |
| + SMAS (w/o Purification) | 49.70 | 443,520 | 270,058 | 502,937 | 600,582 |
| + SMAS (w/o Correction) | 47.88 | 354,226 | 221,515 | 363,871 | 592,852 |
| + SMAS | 50.91 | 371,119 | 258,279 | 404,955 | 489,222 |

消融实验揭示了各模块的协同作用：移除观察净化（Purification）导致 Token 节省从 29.68% 降至 15.96%，表明其是效率提升的主要驱动力；移除错误纠正（Correction）或低效引导（Guidance）则导致准确率显著下降，证实了其对鲁棒性的必要性。这种分工表明，净化模块负责成本最小化，而纠正与引导模块负责任务成功保障。

评估边界方面，论文未报告置信区间，且主要基于 Smolagent 框架验证，虽在 GPT-4.1、Gemini-2.5-pro 和 Qwen3-235B 上验证了模型无关性，但未提供代码开源链接。评估协议聚焦于 Token 消耗与准确率，未涵盖延迟或实时性指标，限制了其在高吞吐场景下的适用性评估。

## 关联研究分析

从问题动机看，SUPERVISORAGENT 与 ProMAS 同属主动监控路线，但两者关注点存在根本差异。ProMAS 侧重通过因果流形学习预测潜在故障，属于风险预测；而 SUPERVISORAGENT 侧重实时纠正已发生的低效行为与错误，属于过程控制。这种差异源于任务特性的不同：ProMAS 假设故障具有可预测的前兆，而 SUPERVISORAGENT 假设低效行为与错误是动态涌现的，需即时响应。SUPERVISORAGENT 的启发式过滤器在动态对抗场景下的鲁棒性是否足以替代形式化验证，论文未给出回答。

从方法设计看，SUPERVISORAGENT 与 SentinelAgent 同属运行时治理，但干预机制截然不同。SentinelAgent 依赖形式化委托链演算进行意图验证，提供强正确性保证但计算开销大；SUPERVISORAGENT 采用 LLM 推理结合启发式过滤，牺牲了强正确性保证以换取低延迟与低开销。这种取舍反映了效率与保证之间的权衡：在资源受限的生产环境中，SUPERVISORAGENT 的轻量级设计更具部署可行性，但在安全关键场景中，其缺乏形式化保证可能成为隐患。

## 总结

本文旨在解决 MAS 中错误传播与低效循环导致的鲁棒性下降及 Token 成本激增问题。现有事后归因与静态优化方法无法应对运行时动态风险，SUPERVISORAGENT 通过 LLM-free 自适应过滤器与多级干预动作空间，实现了实时过程控制。实验证明其在 GAIA 上降低 29.68% Token 消耗且保持准确率，在 AIME 上提升 6.67% 解决率。然而，其启发式过滤器依赖预定义规则，面对未知类型的低效行为或复杂对抗攻击时可能失效。当智能体交互模式发生结构性变化时，该过滤器的触发准确率是否会显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26585)