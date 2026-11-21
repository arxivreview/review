# HuggingFace最新推荐论文 ｜Discovering Multiagent Learning Algorithms with Large Language Models ｜基于大语言模型进化的多智能体博弈算法自动发现

研究机构：谷歌DeepMind

作者：Zun Li、John Schultz、Daniel Hennes 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16928)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16928)

> 多智能体博弈求解长期依赖人工迭代优化算法变体，如反事实遗憾最小化（Counterfactual Regret Minimization, CFR）的折扣策略与策略空间响应预言机（Policy Space Response Oracles, PSRO）的元求解器，这些设计往往受限于数学可处理性而非最优性。本文利用AlphaEvolve框架，将算法源代码作为基因组，通过大语言模型（Large Language Models, LLMs）进行语义变异，自动发现优于现有基线的新算法变体。该方法在不完全信息博弈基准上验证了自动发现机制的有效性，但进化出的非直觉参数缺乏理论收敛性证明，其泛化边界尚存疑。

## 研究背景

不完全信息博弈中，智能体需在隐藏信息下推断对手策略，核心挑战在于计算纳什均衡（Nash Equilibrium, NE）的可利用性（Exploitability）。可利用性衡量策略偏离NE的程度，是评估算法性能的关键指标。CFR通过递归分解全局遗憾为局部信息集上的独立问题，利用遗憾匹配（Regret Matching, RM）推导当前策略，但标准线性累积与固定折扣机制在复杂博弈中收敛缓慢。PSRO通过迭代生成最佳响应并求解元博弈，但静态元求解器无法适应训练过程中经验博弈拓扑的动态变化，导致探索与利用的权衡失衡。

现有CFR变体如折扣CFR（DCFR）与预测CFR+（PCFR+）依赖人工直觉设计权重方案，PSRO则使用均匀分布或纳什均衡作为固定元求解器。这些手动启发式方法在组合空间中的搜索效率低下，且往往默认采用数学上易处理的线性平均或固定折扣，忽略了动态调整的可能性。本文切入点在于将算法设计视为代码级进化问题，利用LLM的代码生成能力突破人类直觉的局限，自动发现非直觉的更新规则与调度机制。

## 核心方法

### 方法参照系

本文问题属于不完全信息博弈求解，标准流程为CFR迭代更新遗憾与策略，或PSRO迭代生成最佳响应并求解元策略。关键差异在于，传统方法固定算法逻辑，仅调整超参数，而本文将算法源代码本身作为可进化对象，允许LLM重写控制流与符号操作。

### AlphaEvolve进化框架

设计动机在于解决人工调参在组合空间中搜索效率低下的问题。AlphaEvolve初始化包含基线算法（如标准CFR或Uniform PSRO）的种群，每代基于适应度（负可利用性）选择父代，LLM接收代码并生成语义变异候选。候选在代理游戏（如Kuhn Poker）上执行，计算最终可利用性作为适应度分数，有效候选加入种群。该过程实现了从参数调优到符号逻辑重写的跨越，允许发现全新机制。

### VAD-CFR与SHOR-PSRO机制

VAD-CFR在遗憾累积环节引入波动率自适应折扣。设计动机在于解决固定折扣无法适应遗憾更新动态变化的问题。其核心公式为：

$$ \alpha = \max(0.1, 1.5 - 0.5 \cdot \text{volatility}), \quad \beta = \min(\alpha, -0.1 - 0.5 \cdot \text{volatility}) $$

其中波动率由瞬时遗憾幅度的指数加权移动平均计算。该机制动态调整正负遗憾的折扣率，并在瞬时更新中引入非对称提升（正遗憾乘以1.1）。策略累积环节采用硬热身（Hard Warm-Start），延迟至第500次迭代开始平均，并使用遗憾幅度加权而非线性加权，过滤早期噪声。SHOR-PSRO在元求解器环节引入混合机制，线性混合乐观遗憾匹配（Optimistic Regret Matching, ORM）与平滑最佳纯策略分布，通过退火调度动态调整混合因子、多样性奖励与温度，实现从探索到利用的自动过渡。

## 实验评估

实验在OpenSpiel框架上进行，训练集包含3玩家Kuhn Poker、2玩家Leduc Poker、4牌Goofspiel、5面Liars Dice，测试集为4玩家Kuhn Poker、3玩家Leduc Poker、5牌Goofspiel、6面Liars Dice。基线覆盖CFR、CFR+、LCFR、DCFR、PCFR+、DPCFR+、HS-PCFR+（CFR路线）及Uniform、Nash、AlphaRank、PRD、RM（PSRO路线），但未包含基于深度学习的MARL基线（如MADDPG）。

| 算法变体 | 测试游戏 | 可利用性趋势 |
| :--- | :--- | :--- |
| VAD-CFR | 4-player Kuhn Poker | 低于PCFR+和DPCFR+ |
| VAD-CFR | 3-player Leduc Poker | 低于PCFR+和DPCFR+ |
| SHOR-PSRO | 4-player Kuhn Poker | 低于Uniform, Nash, AlphaRank, PRD, RM |
| SHOR-PSRO | 3-player Leduc Poker | 低于Uniform, Nash, AlphaRank, PRD, RM |

VAD-CFR在1000次迭代内，可利用性曲线在所有测试游戏中均低于最强基线PCFR+和DPCFR+，表明其波动率自适应机制加速了收敛。SHOR-PSRO在100次PSRO迭代后，可利用性优于所有静态元求解器基线，验证了动态退火调度在平衡探索与利用上的有效性。

消融分析显示，VAD-CFR的硬热身机制（延迟至500次迭代）与遗憾幅度加权是性能提升的关键，早期线性平均会引入噪声污染最终策略。SHOR-PSRO的退火调度中，混合因子从0.30降至0.05，温度从0.50降至0.01，这一动态过程比固定参数更有效地引导种群从多样性探索转向均衡精化。

评估边界方面，实验仅在11个中小规模不完全信息博弈上进行，未测试大规模游戏（如No-Limit Hold'em）或连续动作空间任务。代码未公开，超参数（如LLM提示词、进化代数）未详细披露，可复现性受限。指标仅使用可利用性，未报告计算时间或内存开销，无法评估进化算法的实际部署成本。

## 关联研究分析

从问题动机看，本文与VAD-CFR的前置基线DCFR和PCFR+存在根本差异。DCFR和PCFR+依赖人工设计的固定折扣或预测目标，而VAD-CFR通过LLM进化发现波动率自适应机制，其非对称瞬时提升与硬热身策略是人工设计难以预见的。这一差异源于任务特性：不完全信息博弈的遗憾动态具有高度非线性，固定参数无法适应，而LLM进化能在代码级捕捉这种动态。

从方法设计看，本文与PSRO标准流程中的Nash元求解器形成对比。Nash求解器在每步计算精确纳什均衡，计算开销大且无法适应训练初期的探索需求。SHOR-PSRO通过混合ORM与平滑最佳纯策略，并动态退火，实现了计算效率与探索能力的平衡。这一差异揭示了静态元求解器在动态经验博弈中的局限性，而LLM进化通过代码重写解决了这一盲区。

## 总结

本文核心矛盾在于多智能体博弈算法设计依赖人工启发式，导致在组合空间中搜索效率低下且易陷入局部最优。本文利用AlphaEvolve框架，将算法源代码作为基因组，通过LLM语义变异自动发现VAD-CFR与SHOR-PSRO，突破了手动调参的瓶颈。实验证明VAD-CFR在1000次迭代内可利用性低于PCFR+，SHOR-PSRO在100次迭代内优于所有静态元求解器。然而，进化出的非直觉参数（如波动率阈值、退火调度）缺乏理论收敛性证明，且仅在中小规模离散博弈上验证。当博弈规模扩大至No-Limit Hold'em或引入连续动作空间时，LLM进化发现的机制是否仍具优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16928)