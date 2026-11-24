# ACL-Findings2026最新论文 ｜ProCeedRL: Process Critic with Explorative Demonstration Reinforcement Learning for LLM Agentic Reasoning ｜过程级批评与探索性演示强化学习

研究机构：清华大学

作者：Jingyue Gao、Yanjiang Guo、Chen Xiaoshuai 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_655b3177927a)

> 多轮智能体任务中，次优动作引发的噪声反馈会累积并破坏后续推理，导致标准强化学习（RL）探索效率低下且受限于基座模型能力。现有方法依赖独立重复采样或事后惩罚，无法在错误扩散前进行干预。本文提出 ProCeedRL，通过实时过程级批评者（Critic）检测并回溯修正低质量步骤，将探索从被动选择转为主动干预。该方法在深度搜索与具身任务上突破了标准 RL 的性能上限，但其效果高度依赖 Critic 的准确性，且缺乏理论保证。

## 研究背景

多轮智能体交互可建模为部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP），其中智能体根据历史观察 $o_{1:t}$ 生成动作 $a_t$，环境返回下一状态 $s_{t+1}$ 及稀疏奖励 $r_t$。与单轮生成不同，多轮场景下动作空间扩展至工具调用，状态空间受限于上下文窗口，且奖励信号通常仅在任务结束时给出。这种稀疏性与延迟性使得传统基于结果奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）难以区分轨迹中关键步骤与无关步骤的贡献，导致梯度信号噪声大，信用分配困难。

当前主流 RLVR 方法如 GRPO 和 DAPO 通过组内相对优势估计替代价值函数，降低了计算开销并提升了训练稳定性。然而，这些方法依赖独立重复采样进行探索，其性能上限受限于基座模型的推理能力与环境随机性。当智能体生成次优动作时，环境返回的噪声观察会污染上下文，进而削弱后续决策质量，形成“次优动作-噪声反馈”的正反馈恶性循环。这一机制使得标准探索策略在长程任务中失效，模型难以从错误中恢复，探索效率显著降低。

ProCeedRL 针对这一恶性循环，提出在 Rollout 阶段引入实时过程级 Critic，对每个中间步骤进行评分。当检测到低质量步骤时，系统回溯至该步骤，利用 Critic 反馈生成修正后的演示动作，替换原始动作后继续交互。这一机制将过程监督嵌入训练流程，而非依赖测试时的额外管道或独立的过程奖励模型（Process Reward Model, PRM），从而在提升探索效率的同时，将纠错知识内化至模型参数中。

## 核心方法

### 方法参照系

ProCeedRL 基于 DAPO 算法框架，其标准流程为“采样-评估-更新”。与标准流程的关键差异在于，ProCeedRL 在采样阶段插入了“Critic 检测-回溯-重生成”环节，将离散的终端奖励转化为步骤级信号，并在错误扩散前进行主动干预。

### 过程级 Critic 与回溯机制

标准 RLVR 在轨迹完成后才评估整体质量，无法拦截中间步骤的错误。ProCeedRL 引入 Critic $\phi$，在每步 $t$ 基于历史 $\tau_t$、动作 $a_t$ 及下一状态 $s_{t+1}$ 输出整数评分 $l_t$ 和文本批评 $c_t$：

$$ l_t, c_t = \phi(\tau_t, a_t, s_{t+1}) $$

当 $l_t \le l_{th}$ 时，触发回溯机制。该设计解决了标准方法中错误累积导致探索效率低下的问题，通过实时干预防止噪声上下文污染后续推理。

### 演示融合与策略优化

回溯生成的修正动作 $a'_t$ 与当前策略分布存在偏移，直接训练会导致不稳定。ProCeedRL 采用 chord-$\phi$ 方法，对演示数据加权，抑制高概率与低概率演示的影响：

$$ \sigma(d_{j,t}) = \pi_\theta(d_{j,t}|x, d_{j,<t}) \cdot (1 - \pi_\theta(d_{j,t}|x, d_{j,<t})) $$

优化目标中，演示步骤的损失乘以 $\sigma(d_{j,t})$，而 On-policy 步骤权重为 1。这一机制缓解了 Off-policy 演示与 On-policy 样本间的分布偏移，确保训练稳定性，同时将纠错知识内化至模型参数，消除测试时的额外开销。

## 实验评估

实验在深度搜索（MuSiQue, WebWalkerQA, GAIA, Frames, Bamboogle）与具身任务（ALFWorld）上进行，基线包括 ReAct、RFT、DAPO/Search-R1、GiGPO 等。ProCeedRL 在深度搜索任务上平均提升 3.72%，在 ALFWorld 上结合 SFT 后提升超过 10%。

| 方法 | MuSiQue | WebWalkerQA | GAIA | Frames | Bamboogle |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ReAct Prompting | 50.93% | 18.64% | 31.92% | 9.69% | 18.62% |
| +DAPO/Search-R1 | 70.83% | 23.60% | 43.59% | 10.10% | 19.51% |
| +ProCeedRL | 73.87% | 29.52% | 46.42% | 13.79% | 23.01% |

消融实验显示，回溯阈值 $l_{th}$ 对性能影响显著：增加回溯步骤可提升性能，但过度回溯会导致性能下降，因替换了部分合理动作。Critic 类型方面，Self-Critic 在 ALFWorld 上达到 69.21%，优于外部 Critic 的 64.55%，表明方法不依赖强外部模型。计算开销上，ProCeedRL 每条轨迹计算量约为标准方法的 2 倍，但所需轨迹数量仅为标准方法的 1/4，总体计算量减半。

评估边界方面，论文未报告置信区间，数值比较需谨慎。ALFWorld 上 ProCeedRL 的 69.21% 低于多智能体 SOTA（Stronger-MAS 99.5%），但高于单智能体基线（SLEA-RL 60.3%），表明单智能体架构可能存在性能上限。代码已开源，超参数详见附录，但 Critic 的推理开销在异构环境下的可扩展性未充分验证。

## 关联研究分析

从问题动机看，ProCeedRL 与 Tree-GRPO 均关注细粒度信用分配，但 Tree-GRPO 依赖树搜索扩展采样空间，通过分支探索增强策略多样性，而 ProCeedRL 依赖实时 Critic 回溯，通过主动干预防止错误累积。Tree-GRPO 的增益源于采样空间的扩展，ProCeedRL 的增益源于探索效率的提升。两者在长程任务上的表现差异，可能源于任务特性：Tree-GRPO 更适合分支结构明显的任务，ProCeedRL 更适合线性交互且错误累积显著的任务。

从方法设计看，ProCeedRL 与 SLEA-RL 同为单智能体增强方法，但 SLEA-RL 侧重经验增强，通过记忆库存储成功轨迹，而 ProCeedRL 侧重实时纠错，通过 Critic 检测并修正低质量步骤。SLEA-RL 的增益源于经验复用，ProCeedRL 的增益源于错误拦截。两者在 ALFWorld 上的性能差距（60.3% vs 69.21%），可能源于实时纠错在长程任务中更有效地防止了错误累积，而经验复用仅能复用已验证的成功路径，无法应对新出现的错误模式。

## 总结

ProCeedRL 针对多轮智能体任务中“次优动作-噪声反馈”恶性循环导致的探索效率低下问题，提出实时过程级 Critic 回溯机制，将探索从被动选择转为主动干预。该方法在深度搜索任务上平均提升 3.72%，在 ALFWorld 上结合 SFT 后提升超过 10%，突破了标准 RLVR 的性能上限。然而，其效果高度依赖 Critic 的准确性，且缺乏理论保证，过度回溯可能导致性能下降。当 Critic 评分分布高度偏斜时，回溯阈值的动态校准是否仍能保持探索效率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_655b3177927a)