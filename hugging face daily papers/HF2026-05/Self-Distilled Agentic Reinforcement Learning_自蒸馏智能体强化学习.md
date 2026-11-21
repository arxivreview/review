# HuggingFace最新推荐论文 ｜Self-Distilled Agentic Reinforcement Learning ｜自蒸馏智能体强化学习

研究机构：浙江大学、美团

作者：Zhengxi Lu、Zhiyuan Yao、Zhuowen Han 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15155)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15155)

> 多轮智能体强化学习（Agentic RL）面临轨迹级奖励稀疏导致的信用分配难题，而在线自蒸馏（On-Policy Self-Distillation, OPSD）虽能提供密集的Token级指导，但在多轮交互中因教师-学生分布漂移引发训练崩溃。现有混合方法如RLSD直接重加权优势函数，在训练初期因巨大的教师-学生差距导致梯度爆炸。SDAR将OPSD重构为受控辅助目标，通过Token级Sigmoid门控机制动态调节蒸馏强度，仅信任教师正向背书并软衰减负向拒绝。该方法在ALFWorld等基准上显著优于GRPO及混合基线，但其性能增益对检索质量的依赖性及小模型上的泛化边界仍需进一步厘清。

## 研究背景

多轮智能体在长程任务中需维持状态一致性，其决策过程可建模为部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP）。在此框架下，策略优化依赖环境反馈的稀疏奖励，导致梯度信号噪声大。为缓解此问题，引入特权上下文（如检索技能）增强教师分支，通过在线自蒸馏（OPSD）提供Token级密集监督。然而，教师分支并非独立强模型，而是同一策略叠加训练期特权信息，这种非对称性使得教师信号在负向差距时可能源于检索噪声而非策略错误。

Agentic RL的主流路线以GRPO（Group Relative Policy Optimization）为骨干，通过组内相对优势估计替代价值函数，降低计算开销。然而，单纯RL在长程任务中信用分配粗糙，而直接叠加OPSD会导致多轮KL散度激增与性能崩塌。现有混合方法如Skill-SD采用刚性时间调度，RLSD直接利用自散度重加权优势，二者均未能区分教师信号的可靠性来源。SDAR的切入点在于识别“非对称信任”问题：正向教师背书应被强化，而负向拒绝需保守处理，以避免将检索噪声误判为策略缺陷。

## 核心方法

### 方法参照系

SDAR置于RL-OPSD混合训练范式下，其关键差异在于不修改RL主损失，而是将OPSD作为独立辅助目标，并通过Token级门控实现非对称信任。标准流程中OPSD损失均匀施加于所有Token，而SDAR引入动态门控机制，使每个Token自主决定蒸馏强度，从而隔离RL信号的无偏性。

### 非对称信任门控机制

传统OPSD在教师概率低于学生时仍施加蒸馏损失，导致负向信号被错误强化。SDAR引入Token级门控 $g_t \in [0, 1]$，基于教师-学生对数概率差距 $\Delta_t$ 和Student熵 $h_t$ 计算。门控函数采用Sigmoid形式：

$$ g_t = \sigma(\beta \Delta_t) $$

其中 $\beta$ 控制过渡锐度。该设计动机在于：当 $\Delta_t > 0$（教师背书）时，$g_t$ 趋近1，强化蒸馏；当 $\Delta_t < 0$（教师拒绝）时，$g_t$ 趋近0，软衰减信号。这解决了RLSD在训练初期因巨大负向差距导致梯度放大的失效问题。

### 辅助损失解耦

SDAR将OPSD损失定义为独立优化目标，与GRPO损失相加：

$$ \mathcal{L}_{total} = \mathcal{L}_{GRPO} + \lambda \mathcal{L}_{SDAR} $$

其中 $\mathcal{L}_{SDAR} = \text{Agg}(g_t \cdot (\log \pi_{\theta^+}(y_t|s_t^+) - \log \pi_{\theta}(y_t|s_t)))$。门控 $g_t$ 通过停止梯度（sg）操作，确保梯度仅流经Student对数概率，严格保留RL优势的无偏性。此设计避免了GRPO+OPSD中蒸馏梯度污染RL信号导致的性能退化，尤其在Qwen3-1.7B等小模型上表现稳定。

## 实验评估

实验在ALFWorld、WebShop和Search-QA三个基准上进行，使用Qwen2.5-3B/7B和Qwen3-1.7B模型，训练150步于8块H800 GPU。基线覆盖Training-free（Skill-Prompt）、Post-training（GRPO, OPSD, Skill-GRPO）及Hybrid（GRPO+OPSD, Skill-SD, RLSD）三类方法。缺失Tree-GRPO等系统级方法对比，但覆盖了RL-OPSD混合范式的主要变体。

| 方法 | ALFWorld (Qwen2.5-3B) | WebShop-Acc (Qwen2.5-3B) | Search-QA Avg (Qwen2.5-3B) |
| :--- | :--- | :--- | :--- |
| GRPO | 75.0 | 63.3 | 44.4 |
| GRPO+OPSD | 82.4 | 66.4 | 44.0 |
| RLSD | 79.7 | 66.4 | 44.3 |
| SDAR | 84.4 | 68.0 | 45.2 |

SDAR在ALFWorld上较GRPO提升+9.4%，在WebShop-Acc上提升+4.7%，在Search-QA上提升+7.0%。GRPO+OPSD在Qwen3-1.7B上性能退化至32.0（vs GRPO 46.1），而SDAR保持53.9，验证了门控机制对不稳定性的抑制作用。

消融实验显示，Teacher-Student Gap门控优于熵门控和Soft-OR门控，渐近成功率达0.84。$\beta=5.0$ 时性能最佳，$\lambda=0.01$ 平衡了蒸馏强度与RL稳定性。检索质量鲁棒性测试表明，即使Random Retrieval也较纯GRPO提升+1.9%（ALFWorld），证明门控机制能过滤低质量技能噪声。

评估边界方面，论文未报告置信区间，且Search-QA中NQ/HotpotQA为In-domain，其余为Out-of-domain，泛化性评估受限。代码已开源，超参数 $\lambda=0.01, \beta=5.0$ 固定，可复现性较高。

## 关联研究分析

从问题动机看，SDAR与RLSD均针对RL-OPSD混合训练的不稳定性，但根源认知不同。RLSD将教师-学生差距视为优势重加权信号，直接修改RL梯度，导致训练初期更新幅度失控。SDAR则识别出差距的非对称性：负向差距可能源于检索噪声而非策略错误，因此选择隔离蒸馏损失而非修改RL信号。这一差异源于对特权上下文可靠性的不同假设：RLSD假设教师信号始终有效，SDAR假设教师信号需经验证。

从方法设计看，SDAR与Skill-SD同属混合范式，但调度机制迥异。Skill-SD采用刚性时间或轨迹深度阈值，属于手工设计的课程学习，缺乏对Token级信号的响应能力。SDAR的Sigmoid门控基于实时Token级熵和差距，实现自调节课程，粒度更细。这种差异导致SDAR在Qwen3-1.7B等小模型上泛化性更强，因为小模型对刚性调度的适应性较差，而动态门控能自动抑制无效信号。

## 总结

SDAR解决的核心矛盾是OPSD密集指导与多轮RL稳定性之间的冲突，其切入点在于识别教师信号的非对称信任问题，通过Token级门控实现选择性蒸馏。方法上，SDAR将OPSD重构为受控辅助目标，保留RL主损失的无偏性，并在ALFWorld上实现+9.4%的性能提升，同时避免GRPO+OPSD的崩溃。其边界在于性能增益仍依赖检索质量，Random Retrieval下增益仅+1.9%，且小模型上的泛化优势可能源于门控的保守性而非知识内化。当检索质量降至随机水平时，门控机制是否仍能区分有效信号与噪声，论文未给出进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15155)