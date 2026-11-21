# HuggingFace最新推荐论文 ｜Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis ｜数据科学智能体的过程级奖励建模

研究机构：浙江大学

作者：Zhisong Qiu、Shuofei Qiao、Kewei Xu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24198)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24198)

> 数据科学智能体在长链推理中常因缺乏中间步骤验证而传播逻辑错误，现有结果导向监督无法捕捉执行成功但语义错误的“静默失败”。通用过程奖励模型（Process Reward Model, PRM）在静态数学域有效，但在动态数据环境中因无法交互验证而失效。本文提出DataPRM，通过环境交互探针与三元奖励策略实现步骤级监督。该方法在4B参数下超越235B基线，但三元奖励的阈值泛化性仍存疑。

## 研究背景

数据科学智能体（Data Science Agent, DSA）通常被形式化为部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP），其中智能体通过代码生成执行动作，并依赖解释器反馈更新状态。然而，LLM无法直接感知DataFrame等内存对象的完整状态，导致基于错误假设继续执行。这种状态不可见性催生了“静默失败”现象：代码执行无异常，但输出结果逻辑错误。传统结果监督仅关注最终答案，无法拦截中间步骤的逻辑断裂，使得幻觉逻辑沿任务链向下游扩散。

当前主流方案分为两类：一是依赖执行反馈的单体智能体，如Data Interpreter，其瓶颈在于执行成功即被视为正确，无法检测静默错误；二是通用PRM，如Math-Shepherd，其设计基于静态文本推理，缺乏与动态环境交互的能力。通用PRM在数据分析任务中面临双重失效：既无法通过静态阅读验证执行结果的语义正确性，又常将必要的试错探索误判为不可恢复的失败，导致对探索行为的过度惩罚。本文切入点在于将PRM从静态文本验证转变为动态环境交互验证，并引入区分探索与错误的奖励机制。

## 核心方法

### 方法参照系

标准PRM流程基于轨迹历史 $h_t$ 和当前步骤 $\tau_t$，通过评分函数 $R_\theta$ 输出二元奖励 $r_t \in \{0, 1\}$。本文问题与该通用流程的关键差异在于：数据分析步骤的正确性依赖于运行时环境状态，而非仅由代码文本决定，且探索性步骤不应被简单标记为错误。

### 环境交互验证机制

通用PRM仅读取代码文本，无法感知执行后的实际数据状态。DataPRM在验证阶段引入主动环境交互，允许模型执行探针代码以检查中间状态。这一设计解决了静态PRM无法检测“静默错误”的失效问题。验证过程定义为：

$$
r_t = R_\theta(\cdot | h_t, \tau_t, \mathcal{E}(\tau_t))
$$

其中 $\mathcal{E}(\tau_t)$ 表示PRM对当前步骤执行的环境探针交互。通过多轮代码执行，PRM能够确认可视化结果是否真正生成，从而避免被“执行成功”的表象欺骗。

### 三元奖励策略

二元奖励无法区分“致命错误”与“可恢复的探索性接地错误”。DataPRM将奖励空间扩展为三元集 $\mathcal{R} = \{0, 0.5, 1\}$，其中0.5代表中性探索步骤。该策略解决了通用PRM因误判探索行为而抑制智能体环境适应能力的失效。奖励聚合公式为：

$$
r_{traj} = \sum_{t=1}^{T} \lambda_t r_t, \quad r_t \in \{0, 0.5, 1\}
$$

通过赋予探索步骤中间分值，DataPRM在强化学习中保留了必要的试错空间，防止策略过早收敛于保守路径。

## 实验评估

实验在ScienceAgentBench、DABStep（TTS设置）及DABench、TableBench（RL设置）上进行。基线覆盖通用PRM（Qwen2.5-Math-PRM-72B, GenPRM-32B）、Self-Rewarding（Qwen3-235B）及Majority Voting。缺失多智能体协作类基线（如VDSAgents），限制了与架构级优化方案的直接对比。

| 设置 | 方法 | 指标 | 数值 |
| :--- | :--- | :--- | :--- |
| TTS | DataPRM (4B) | ScienceAgentBench提升 | 7.21% |
| TTS | DataPRM (4B) | DABStep提升 | 11.28% |
| RL | DataPRM | DABench Accuracy | 78.73% |
| RL | DataPRM | TableBench Accuracy | 64.84% |

DataPRM在4B参数下超越Qwen3-235B Self-Rewarding基线，参数效率达58倍。在Best-of-N设置中，随着N从8增至16，Qwen2.5-Math-PRM-72B性能从33.33%降至31.33%，而DataPRM保持持续上升，表明其具备区分有效推理与幻觉的能力。

消融实验显示，引入环境交互（Env）和多轮交互（Multi）对Hard子集提升最显著。CoT基线在N=16时Hard子集准确率为35.71%，加入环境交互后升至36.77%，DataPRM进一步达到37.57%。三元奖励（Refl）在Easy子集上贡献有限，但在Hard子集上避免了探索抑制，验证了奖励空间扩展的必要性。

评估边界方面，TTS实验使用Qwen3-VL-235B作为Judge，RL实验使用Qwen3-30B作为Judge，Judge模型的能力可能影响最终分数。代码已开源，训练使用8×H20 GPU，学习率1e-5，batch size 32。未报告置信区间，且未控制骨干网络差异对结果的贡献。

## 关联研究分析

从问题动机看，Tree-Notebook同样关注静默失败检测，但其通过树搜索和熵感知数据影子在导航层面解决状态重建，而DataPRM在奖励层面解决步骤验证。Tree-Notebook侧重于“如何找到正确路径”，DataPRM侧重于“如何评估路径质量”。二者差异源于任务特性：Tree-Notebook处理交互式探索，需实时状态更新；DataPRM处理离线轨迹评估，需全局一致性判断。DataPRM未探索树搜索结构，其线性轨迹假设在高度分支的探索任务中可能受限。

从方法设计看，VDSAgents通过多智能体分工缓解长上下文注意力稀释，而DataPRM通过外部PRM提供细粒度反馈。VDSAgents依赖角色间通信传递状态，DataPRM依赖环境交互获取状态。VDSAgents的瓶颈在于角色间信息不一致，DataPRM的瓶颈在于环境交互的计算开销。DataPRM未采用多智能体架构，其单PRM设计在复杂多步任务中可能面临上下文窗口限制，而VDSAgents的分治策略在此场景下更具扩展性。

## 总结

本文核心矛盾在于通用PRM无法区分数据科学中的静默错误与探索性接地错误。DataPRM通过环境交互探针和三元奖励策略，将静态文本验证转变为动态状态检查，解决了通用PRM在动态域判别力不足的问题。实验证明4B参数的DataPRM在TTS和RL设置中均优于大规模基线，DABench准确率达78.73%。其边界在于三元奖励中0.5阈值的确定依赖专家标注，缺乏自适应机制，且在高度分支的探索任务中未验证树搜索结构的适用性。当探索空间极大时，固定阈值的三元奖励是否会导致策略收敛于局部最优，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24198)