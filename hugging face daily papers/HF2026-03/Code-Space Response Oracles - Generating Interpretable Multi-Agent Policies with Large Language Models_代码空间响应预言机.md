# HuggingFace最新推荐论文 ｜Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models ｜代码空间响应预言机

研究机构：谷歌DeepMind

作者：Daniel Hennes、Zun Li、John Schultz 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10098)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10098)

> 多智能体博弈中的策略计算长期依赖深度强化学习（Deep RL）训练的黑盒神经网络，导致策略无法被人类审计或调试，阻碍了其在高风险场景的部署。现有Policy-Space Response Oracles (PSRO) 框架虽能逼近纳什均衡，但其Oracle环节产生的不透明参数使得策略验证成为不可能。本文提出Code-Space Response Oracles (CSRO)，将最佳响应计算重构为大语言模型（LLM）的代码生成任务，通过生成可执行源码替代神经网络权重，实现了策略的完全可解释性。该方法在标准博弈基准上达到了与成熟求解器相当的均衡质量，但其性能高度依赖进化搜索机制，且未验证在连续动作空间或复杂谈判场景中的泛化能力。

## 研究背景

多智能体博弈的核心挑战在于计算鲁棒策略。Policy-Space Response Oracles (PSRO) 通过迭代构建策略集并求解元博弈均衡，成为处理复杂不完全信息博弈的主流框架。然而，标准PSRO依赖深度强化学习Oracle，其输出为黑盒神经网络，不仅缺乏可解释性，且训练过程需数百万次模拟，样本效率极低。这种不透明性使得策略无法被验证，构成了在网络安全、经济建模等高风险领域部署的主要障碍。

该领域的研究脉络从追求数值最优转向兼顾可解释性。早期工作如Barrage Stratego和StarCraft中的PSRO变体证明了迭代方法的有效性，但始终未解决策略黑盒问题。Bachrach et al. (2025) 提出的LLM-PSRO尝试利用LLM生成策略，但仅采用开环“best-of-N”采样，缺乏闭环优化机制，且无法处理上下文窗口限制。CSRO的切入点在于将LLM视为程序合成器，通过引入迭代精炼与上下文抽象，解决LLM-PSRO在可扩展性与策略质量上的瓶颈，从而在保持博弈论最优性的同时实现策略透明化。

## 核心方法

### 方法参照系

CSRO基于标准PSRO迭代框架，但将Oracle从深度强化学习替换为LLM代码生成。与通用PSRO流程的关键差异在于，策略表示从神经网络权重变为可执行代码，最佳响应计算从数值优化变为程序合成任务，使得策略逻辑显式化且可审计。

### 代码策略生成与上下文抽象

标准PSRO中Oracle通过大量交互训练神经网络逼近最佳响应，而CSRO利用LLM预训练中的逻辑与规划知识，直接生成Python函数作为策略。设计动机是消除黑盒参数，使策略逻辑可被人类阅读与验证。LLM接收游戏规则、API规范及对手策略描述，生成映射观测到动作的代码策略。为应对上下文限制，CSRO引入上下文抽象机制，通过LLM摘要或过滤Top-k对手代码，将原始源码转化为高层行为描述，避免输入超出窗口限制。该机制使得CSRO能扩展至复杂博弈，其中完整源码会溢出上下文窗口。

$$
\pi' \leftarrow \text{LLM}_{\text{oracle}}(\text{prompt}(G, \sigma, P))
$$

该公式表示LLM基于游戏规则$G$、元博弈均衡$\sigma$及当前策略集$P$生成候选策略$\pi'$，将最佳响应计算转化为条件代码生成任务。

### 迭代精炼与进化搜索

零样本生成的策略质量不稳定，CSRO引入两种精炼机制以闭环优化策略。设计动机是解决LLM单次生成缺乏反馈修正的问题，确保策略对当前元博弈$\sigma$具有鲁棒性。LinearRefinement采用单线程线性反馈，若策略效用$u < 0$，则触发重新生成直至效用非负或达到预算$M$。AlphaEvolve则采用分布式进化搜索，通过多线程变异程序并利用效用作为评分函数，引导进化过程向高得分变体收敛。AlphaEvolve通过聚类子种群保持多样性，持续采样历史程序并提示LLM生成修改，显著提升了策略的探索效率与最终质量。

$$
\pi^* = \arg\max_{\pi' \in \Pi} \mathbb{E}_{\pi' \sim \sigma}[u(\pi, \pi')]
$$

该公式定义了最佳响应的目标，即最大化对元博弈策略$\sigma$的期望效用，CSRO通过进化搜索在代码空间中逼近该最优解。

## 实验评估

实验在Repeated Rock-Paper-Scissors (RRPS) 与Repeated Leduc hold’em poker上进行，基线包括PSRO-IMPALA、CFR+及LLM Agent。CSRO-AlphaEvolve在RRPS中PopExpl为25.2±20.3，显著优于PSRO-IMPALA的423.2±28.0，表明进化搜索有效降低了可剥削性。在Leduc Poker中，CSRO-AlphaEvolve对AlwaysCall策略的平均收益达110.3±9.7，高于CFR+的62.1±0.8，展示了代码策略在利用对手可预测性方面的优势。

| Method | PopReturn↑ | PopExpl↓ | AggScore↑ |
| :--- | :--- | :--- | :--- |
| CSRO-AlphaEvolve | 50.5±1.9 | 25.2±20.3 | 25.4±21.6 |
| CSRO-LinearRef. (code) | 159.8±7.7 | 37.7±10.6 | 122.1±9.8 |
| PSRO-IMPALA | -108.9±17.6 | 423.2±28.0 | -532.1±41.5 |
| LLM Agent (27B) | 193.2 | 67.2 | 126.0 |

消融实验显示，Oracle强度直接决定策略质量，AlphaEvolve优于LinearRefinement，后者优于ZeroShot。LinearRefinement (code) 在RRPS中AggScore达122.1±9.8，接近27B LLM Agent的126.0，但可剥削性更低。在Leduc Poker中，LinearRefinement对AlwaysFold的收益57.3±8.8高于AlphaEvolve的42.0±3.2，表明不同精炼机制发现非支配策略集，进化搜索侧重鲁棒性，线性精炼侧重特定对手利用。

评估边界受限于离散动作空间博弈，未验证连续动作或复杂谈判场景。代码未公开，但提供了OpenSpiel环境实现。超参数$K=20, M=10$固定，未探索不同预算下的性能权衡。

## 关联研究分析

从问题动机看，CSRO与Verifiable RL Pipeline (RLVR) 形成鲜明对比。RLVR通过可验证奖励强化学习优化LLM谈判智能体的经济理性，聚焦于修正亲社会偏差以提升剩余提取能力；而CSRO聚焦于博弈论均衡计算的可解释性，不涉及谈判场景特有的对齐偏差修正。两者均利用LLM的策略推理能力，但RLVR将LLM作为被优化的智能体，CSRO将LLM作为策略生成器。这种差异源于任务特性：谈判需处理不完全信息与情感策略，而标准博弈需计算精确均衡。CSRO未探索RLVR奖励信号能否引导代码策略的经济理性优化，这或许是两者结合的关键盲区。

从方法设计看，CSRO与Mechanistic Evidence of NE Suppression 在可解释性路径上互补。后者通过探针实验分析LLM内部亲社会覆盖机制，解释为何偏离纳什均衡；CSRO则通过生成代码显式化策略逻辑，提供可审计的中间层。CSRO的上下文抽象机制本质上是一种基于代码摘要的对手建模，而非直接模拟对手行为。与Opponent Simulation for Online Adaptation 相比，CSRO不模拟对手动态，而是静态分析当前元博弈策略集。这种静态分析在动态谈判中可能失效，因为对手策略会随交互演化，而CSRO的元博弈均衡假设策略集固定。

## 总结

CSRO旨在解决多智能体博弈中策略黑盒化导致的不可审计问题，抓住LLM代码生成能力与PSRO迭代框架的结合点，将最佳响应计算重构为程序合成任务。通过引入AlphaEvolve进化搜索与上下文抽象，CSRO在RRPS与Leduc Poker中实现了与CFR+相当的均衡质量，其中AlphaEvolve在RRPS中PopExpl降至25.2，在Leduc中对AlwaysCall收益达110.3。然而，实验局限于离散动作空间的标准博弈，未验证在连续动作或复杂谈判场景中的适用性。当对手策略动态演化时，基于静态元博弈均衡的代码生成策略是否仍能保持鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10098)