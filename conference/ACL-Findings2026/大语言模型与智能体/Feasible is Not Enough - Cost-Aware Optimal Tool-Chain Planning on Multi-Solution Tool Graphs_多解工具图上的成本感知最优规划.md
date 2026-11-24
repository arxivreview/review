# ACL-Findings2026最新论文 ｜Feasible is Not Enough: Cost-Aware Optimal Tool-Chain Planning on Multi-Solution Tool Graphs ｜多解工具图上的成本感知最优规划

作者：Liangliang Liu、Yanming Li、Yigang Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d03aa10b9cd1)

> 工具增强大语言模型（Tool-Augmented LLMs）在大规模工具库中常面临候选路径爆炸与上下文窗口受限的双重压力，现有方法多将工具调用视为单解问题，忽略同一任务存在多条有效路径且成本差异巨大的现实。本文切入点在于将工具学习（Tool Learning, TL）重构为多解图上的最优路径选择问题，通过强化学习（Reinforcement Learning, RL）驱动的两阶段渐进式图扩展与推理框架，在构建紧凑任务相关子图的同时执行成本感知规划。该框架在自建基准上显著提升了任务成功率与解的最优性，但其泛化能力受限于特定领域API的静态结构，且未与最新RLVR基线进行同协议对比。

## 研究背景

当智能体面对包含数千个API的工具库时，直接提示所有工具会迅速耗尽大语言模型（LLM）的上下文窗口，而基于语义相似度的静态检索往往只能捕捉局部相关性，遗漏工具间复杂的资源依赖关系。这种依赖关系构成了工具图（Tool Graph, TG），其中工具节点与资源节点通过输入输出连接，形成有向图结构。在TG中，从源资源到目标资源可能存在多条路径，每条路径对应不同的工具调用序列，其执行成本（如API延迟、调用次数）各异。

主流工具编排方法如ToolChain*采用A*搜索或MCTS在预构建的TG上寻找路径，但这类方法假设工具集静态且任务单解，无法处理动态子图构建与多解择优。ReAct等框架虽支持交互，但依赖线性序列规划，难以并行探索或回溯。本文指出，现有基准多关注“能否找到一条有效路径”，而忽略了“如何找到成本最低的路径”这一工程核心。TOPT的切入点是将TL形式化为马尔可夫决策过程（Markov Decision Process, MDP），通过RL Agent动态决定图扩展时机与路径计算策略，从而在有限预算下实现最优解选择。

## 核心方法

### 方法参照系

本文问题属于工具编排与规划路线，但区别于静态检索+启发式搜索的标准流程。关键差异在于：标准流程假设TG预先构建且固定，而TOPT将TG视为动态环境，Agent需在线构建任务相关子图，并在多解中择优。

### 渐进式图扩展与终止决策

Stage I 解决子图构建中的过度扩展问题。传统启发式方法为避免遗漏关键节点，倾向于保守分支，导致子图膨胀、候选路径集爆炸。TOPT将Stage I 建模为带最优停止的约束子图构建问题，Agent通过调用图处理工具（如ExpandForward, JumpToNode）逐步构建子图 $G_k$，并决定何时终止。其优化目标 $J_E$ 平衡终端连通性、过程相关性与约束惩罚：

$$
J_E = \max_{\pi_E} \mathbb{E}_{\tau_E \sim \pi_E} \left[ \sum_{t=0}^{K} \gamma^t \Phi_{rel}(s_t, a_t) + \Phi_{conn}(G_K) - \lambda_f \sum_{t=0}^{K} \gamma^t C_f^t - \lambda_s \sum_{t=0}^{K} \gamma^t C_s^t \right]
$$

其中 $\Phi_{conn}(G_K)$ 确保终止子图包含至少一条源-目标路径，$C_f^t$ 惩罚无效工具调用，$C_s^t$ 惩罚超出阈值 $t_{GT}$ 的扩展步数。该设计使Agent学会在“可解性”与“紧凑性”间权衡，避免冗余节点干扰后续推理。

### 成本感知渐进式图推理

Stage II 在固定子图 $G_k$ 上执行最优路径选择。传统方法直接枚举所有路径并评分，但路径数随节点数指数增长。TOPT将Stage II 建模为约束多路径规划问题，Agent调用图操作原语（如ComputeAllPath, ComputePathCost）收集路径信息，并决定何时终止以输出最优路径 $p^*$。其目标函数 $J(p)$ 联合优化工具成本与路径长度：

$$
p^* = \arg \min_{p \in P_{G_k}(N_{src}, N_{tgt})} J(p), \quad J(p) = \alpha \cdot Cost(p) + \beta \cdot |p|
$$

其中 $\alpha=0.75, \beta=0.25$ 为预设权重，反映对成本优先于长度的工程偏好。Agent通过PPO-clip算法联合优化Stage I 与Stage II 策略，奖励函数包含终端效用 $\Phi_{opt}(p; G_k)$，鼓励输出 $J(p)$ 最小的路径。该设计将经典图算法封装为Agent可调用的工具，使策略学习聚焦于“何时调用何种图操作”，而非重复实现确定性计算。

## 实验评估

实验在自建MultiSoTLBench上进行，该基准基于TMDB与Spotify API，包含约20K样本，按工具调用数分为EASY（1-2）、MEDIUM（3-5）、HARD（>5）三级。基线覆盖CoT、ReAct、ToolLLaMA、RestGPT等主流方法，但缺失Tool-R1、Tool Zero等最新RLVR基线，限制了与当前SOTA的直接对比。

| 方法 | 难度 | CP%↑ | OP%↑ | Time Cost↓ (s) | Token↓ (k) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TOPT (Ours) | EASY | 2.13 | 8.29 | 1.71 | 8.30 |
| TOPT (Ours) | MEDIUM | 33.33 | 16.67 | 1.76 | 8.26 |
| TOPT (Ours) | HARD | 2.5 | 2.5 | 2.19 | 11.29 |
| ReAct (GPT-4.1) | EASY | 29.57 | 24.10 | 29.68 | 10.61 |
| ReAct (GPT-4.1) | MEDIUM | 33.33 | 16.67 | 37.56 | 30.43 |
| ReAct (GPT-4.1) | HARD | 26.29 | 25.46 | 35.52 | 14.22 |

TOPT在MEDIUM难度下CP%与ReAct持平（33.33%），但OP%（最优路径率）显著更高，且时间成本从37.56s降至1.76s，Token消耗从30.43k降至8.26k。在HARD难度下，TOPT的CP%（2.5%）低于ReAct（26.29%），但OP%（2.5%）与ReAct（25.46%）差距缩小，表明复杂任务中TOPT更倾向于输出低成本路径，但可能牺牲部分可行性。

消融实验未单独报告，但Stage I 与Stage II 的联合优化设计暗示：若仅使用启发式扩展（如BFS），子图可能包含大量无关节点，导致Stage II 搜索空间膨胀；若仅使用静态检索，则无法适应未见工具组合。TOPT的RL策略通过动态终止决策，在EASY任务中仅用1.71s完成规划，而ReAct需29.68s，效率提升约17倍。

评估边界受限于自建基准的领域特异性（TMDB/Spotify），未验证在BFCL、ToolBench等通用基准上的表现。代码已开源，但超参数（如 $\alpha, \beta, \lambda_f, \lambda_s$）的敏感性分析缺失，且未报告GPU训练成本，可复现性受限。

## 关联研究分析

从问题动机看，TOPT与ToolChain*同属图结构工具编排，但ToolChain*假设TG静态且任务单解，其A*搜索旨在找到任意有效路径；TOPT则针对多解场景，引入成本感知目标 $J(p)$，将“最优性”作为核心指标。这一差异源于任务特性：ToolChain*面向短链、低复杂度任务，而TOPT面向长链、高成本敏感任务。TOPT未探索动态TG（如API版本更新）下的在线重规划，其子图构建策略在工具集变化时可能失效。

从方法设计看，TOPT与Tool-R1同属RLVR路线，但Tool-R1关注通用工具调用的泛化性，通过损失掩码区分模型生成与工具返回token；TOPT则聚焦图结构下的最优路径选择，其奖励函数针对图连通性与路径成本定制。TOPT的RL Agent动作空间限制为图操作原语，而Tool-R1的动作空间为自然语言指令。这种设计使TOPT在结构化任务中更高效，但牺牲了灵活性：若工具依赖关系无法用资源节点准确建模（如时序依赖），TOPT的图扩展策略可能失效。

## 总结

TOPT解决的核心矛盾是大规模工具库中多解路径的选择与上下文预算的冲突。其切入点在于将TL重构为MDP，通过RL Agent动态构建紧凑子图并执行成本感知规划，从而在有限预算下实现最优解选择。实验证明，TOPT在MEDIUM难度下将时间成本从37.56s降至1.76s，OP%显著提升。其边界在于：基准局限于TMDB/Spotify静态API，未验证动态工具集下的鲁棒性；且未与最新RLVR基线同协议对比，泛化能力存疑。当工具依赖关系超出资源节点建模范围（如时序、环境依赖）时，TOPT的图扩展策略是否仍能保持最优性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_d03aa10b9cd1)