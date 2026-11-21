# HuggingFace最新推荐论文 ｜EasyPPO: Stabilizing the Critic Is Key ｜稳定PPO Critic以解决LLM长程推理训练崩溃

研究机构：美国加州大学伯克利分校、美国普林斯顿大学

作者：Xuanyi Zhou、Qiuyang Mang、Huanzhi Mao 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.36802)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.36802)

> 强化学习后训练中，长序列任务常因奖励稀疏与截断噪声导致策略更新不稳定，现有GRPO等无Critic算法虽简化了流程，但牺牲了细粒度信用分配能力，而PPO的Critic模块在LLM场景下常被忽视其自身的失效模式。本文指出PPO中Critic学习存在“目标偏移”与“噪声主导”两大失效，导致训练后期性能崩溃。通过仅对Actor过滤截断样本、对Critic损失进行噪声归一化及调整Mini-batch大小，EasyPPO在连续奖励编码、二元奖励数学推理及多轮搜索任务上实现了全程稳定训练，验证了稳定Critic是PPO在LLM长程推理中可靠性的关键，但其性能增益是否足以抵消Critic带来的额外计算开销仍存疑。

## 研究背景

当大语言模型（LLM）在数学证明或代码生成等长程任务中进行强化学习时，策略网络（Actor）需要基于历史轨迹估计每个Token的期望回报以计算优势函数，这一过程依赖价值网络（Critic）提供低方差的基线。然而，Critic的预测精度直接决定了策略梯度的质量，若Critic学习不稳定，其产生的噪声优势函数会误导Actor更新，导致策略分布锐化或性能崩溃。在可验证奖励（RLVR）范式下，奖励信号虽客观但稀疏，且长序列中截断样本（Truncated Rollouts）的奖励反映的是不完整响应，进一步加剧了Critic学习的难度。

主流RLVR算法如GRPO通过组内相对优势估计消除了对独立Critic的依赖，降低了内存开销，成为当前标准基线。然而，GRPO将单一轨迹优势广播至所有Token，无法区分关键决策点与无关Token，在长程任务中面临信用稀释问题。PPO通过Actor-Critic架构保留了Token级回报估计能力，理论上更适合长程推理，但其在LLM场景下的Critic稳定性未被充分研究。现有工作如DAPO和VAPO主要关注Actor侧的裁剪机制或价值学习目标改进，却忽视了Critic训练过程中因截断样本过滤和异质回报噪声导致的系统性偏差。本文切入点在于揭示PPO中Critic失效的具体机制，并通过针对性修改稳定Critic学习，从而恢复PPO在长程任务中的细粒度信用分配优势。

## 核心方法

### 方法参照系

PPO在LLM RLVR中的标准流程包含Actor策略更新与Critic价值回归两个并行过程。通常做法是对截断样本进行统一过滤，以减少奖励噪声对策略更新的影响。本文问题与该通用流程的关键差异在于：统一过滤改变了Critic的学习目标，使其从预测全量回报均值偏移至预测条件完成回报均值，导致策略目标发生隐性偏移，且异质回报噪声在有限批次中主导Critic梯度更新。

### Actor-only Overlong Filtering

在标准PPO中，截断样本通常从Actor和Critic更新中同时剔除，以避免不完整响应的噪声奖励干扰策略优化。本文指出，这种联合过滤使Critic学习目标从 $E[R|s]$ 变为 $E[R|s, C]$，其中 $C$ 为未截断事件。根据对数导数恒等式，联合过滤下的策略梯度等价于优化条件完成奖励，而非鼓励策略避免截断：

$$
\nabla_\theta E[R|s, C] = E_{\tau \in C} \left[ (R - V_\phi(s)) \nabla_\theta \log \pi_\theta(\tau|s) \right]
$$

该公式表明，联合过滤仅优化已完成响应的奖励，而忽略了截断概率本身，导致截断率随训练增加而整体奖励停滞。本文创新在于仅对Actor更新应用截断过滤，保留所有样本用于Critic训练，使Critic目标恢复为 $E[R|s]$。这一设计动机在于，Critic需要准确估计全量回报均值以提供无偏基线，而Actor可通过过滤避免被噪声奖励误导。保留截断样本使Critic能感知截断风险，从而在优势函数中隐含鼓励完成的信号，解决了联合过滤导致的策略目标偏移问题。

### Noise-Normalized Critic Regression

保留截断样本后，Critic面临异质回报噪声挑战：不同提示词（Prompt）的回报方差差异巨大，高方差提示词在有限批次中主导Critic梯度更新。Critic的MSE损失梯度二阶矩分解为预测误差与回报噪声两项：

$$
\mathbb{E} \left[ \|\nabla_W L_V(\phi)\|^2 \right] = \left( V_\phi(s) - E[R|s] \right)^2 + \text{Var}(R|s)
$$

随着Critic预测精度提升，预测误差项减小，回报噪声项 $\text{Var}(R|s)$ 成为主导，导致高方差提示词贡献不成比例的梯度。本文创新在于对Critic损失进行噪声归一化，权重 $w(s)$ 设为提示词回报标准差的倒数：

$$
w(s) = \frac{|B| / \max\{\hat{\sigma}(s), \epsilon\}}{\sum_{s' \in B} 1 / \max\{\hat{\sigma}(s'), \epsilon\}}
$$

该公式将每个提示词的梯度贡献归一化，消除回报方差差异对有限批次更新的影响。设计动机在于，异质噪声导致Critic学习偏向高方差提示词，忽略低方差但关键的提示词，归一化确保Critic均匀学习所有提示词的回报均值，解决了噪声主导导致的Critic预测偏差问题。

### Critic Mini-Batch Clipping

噪声归一化后，离群值仍可能影响Critic更新。本文发现，较小的Critic Mini-batch在梯度裁剪下能更有效地限制离群值影响。设Mini-batch大小为 $m$，单个离群值对平均裁剪梯度的影响为 $O(m)$，而梯度方差为 $O(1/m)$。本文选择 $B/m = 4$ 的中等Mini-batch大小，平衡噪声平均与离群值限制。这一设计动机在于，较大Mini-batch虽能平均噪声，但离群值影响范围更广；较小Mini-batch通过裁剪将离群值影响限制在少数样本内，解决了离群值导致的Critic更新不稳定问题。

## 实验评估

实验在FrontierCS（连续奖励编码）、AIME24（二元奖励数学推理）和Search-R1（多轮搜索）三个任务上进行，基线包括PPO、PPO+Actor-only Filtering、VAPO和HL-Gauss PPO。本文未对比GRPO等主流无Critic算法，基线覆盖局限于PPO变体，可能高估PPO框架内的相对优势。

| 任务 | 方法 | 最佳验证分数（相对PPO增益） |
| :--- | :--- | :--- |
| FrontierCS | EasyPPO | +14.89% |
| AIME24 | EasyPPO | +2.28% |
| Search-R1 | EasyPPO | +9.47% |

EasyPPO在三个任务上均取得最佳验证分数，且是唯一全程稳定的方法。消融实验显示，噪声归一化在4 Mini-batch配置下对稳定性贡献最大，无归一化时性能崩溃不可恢复；Mini-batch大小与噪声归一化存在交互作用，较小Mini-batch需归一化才能稳定。

评估边界方面，论文未报告置信区间，数值比较需谨慎；FrontierCS和Search-R1为本文特有基准，缺乏与领域SOTA（如TEMPO在AMC23的92.5%）的直接对比；代码已开源，但Critic学习率等超参数调整细节需参考附录。

## 关联研究分析

从问题动机看，本文与DAPO均处理截断样本问题，但DAPO在GRPO中统一过滤，本文在PPO中仅过滤Actor。这一差异源于GRPO无Critic，过滤不影响价值估计；而PPO的Critic依赖全量数据学习回报均值，过滤导致目标偏移。根源在于算法架构差异：GRPO的组内相对优势估计对截断样本不敏感，而PPO的Critic回归对样本分布敏感。

从方法设计看，本文与VAPO同属PPO框架，但VAPO改进价值学习目标与优势估计，本文改进Critic训练稳定性。VAPO未考虑异质回报噪声对Critic梯度的影响，而本文通过噪声归一化解决这一问题。差异根源在于VAPO假设Critic学习稳定，而本文揭示Critic学习本身是LLM RLVR中的主要不稳定源。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文要解决的核心矛盾是PPO在LLM长程推理中Critic学习不稳定导致的训练崩溃。现有方法如GRPO通过消除Critic规避此问题，但牺牲了细粒度信用分配能力；本文抓住Critic失效的具体机制，通过Actor-only过滤、噪声归一化及Mini-batch裁剪稳定Critic学习。实验证明EasyPPO在三个任务上实现全程稳定训练，相对PPO增益最高达14.89%。本文边界在于未对比GRPO等无Critic算法，无法量化Critic带来的性能增益是否抵消其计算开销；当序列长度进一步增加时，Critic的内存开销是否成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.36802)