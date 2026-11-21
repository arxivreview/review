# HuggingFace最新推荐论文 ｜Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR ｜策略引导的探索优化

研究机构：韩国科学技术院

作者：Chanuk Lee、Sangwoo Park、Minki Kang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15726)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15726)

> 基于可验证奖励的强化学习（Reinforcement Learning from Verifiable Rewards, RLVR）旨在通过客观二元奖励提升大语言模型（LLM）的长思维链推理能力，但标准算法常因采样陷入主导模式而导致策略分布锐化与解多样性坍缩。现有方法或依赖暴力增加采样量，或修改优化目标，均难以精确控制探索的语义方向。本文提出 NudgeRL，通过在采样阶段引入轻量级策略上下文强制模型遍历不同推理模式，并配合跨组优势估计与蒸馏机制实现高效探索。该方法在有限预算下超越了更大预算的基线，但上下文生成的独立性与模型训练脱节，限制了其在开放域任务中的泛化潜力。

## 研究背景

当 LLM 在数学推理任务中生成思维链时，策略梯度更新往往强化高概率路径，导致模型反复采样相似的推理模式。这种分布锐化现象称为熵坍缩，它使得模型难以发现稀有但正确的长尾推理策略。为缓解此问题，组相对策略优化（Group-Relative Policy Optimization, GRPO）通过组内奖励归一化估计优势函数，避免了独立价值网络的训练，成为 RLVR 的标准算法。然而，GRPO 的探索能力受限于采样分布本身：若初始策略未覆盖某类推理路径，增加采样量也无法有效发现该路径，因为低概率轨迹的期望采样次数随概率指数增长。

RLVR 领域的核心矛盾在于探索效率与计算成本的权衡。主流路线包括暴力扩展 rollout 数量以覆盖长尾分布，或引入熵正则化、解耦裁剪等目标函数修改以维持分布宽度。前者计算成本高昂且收益递减，后者仅控制分布的统计特性，无法确保覆盖语义上不同的推理策略。另一路线利用 oracle 解或中间步骤等特权信息引导探索，虽能提升正确轨迹的可行性，但依赖昂贵的外部监督，且将策略限制在预定义的狭窄路径上，抑制了替代策略的发现。NudgeRL 的切入点在于结构化探索：不依赖外部解，而是通过轻量级策略上下文主动塑造采样分布，使模型在有限预算内高效覆盖多样化的推理模式。

## 核心方法

### 方法参照系

NudgeRL 基于 GRPO 框架，但修改了采样过程与优势估计机制。标准 GRPO 从单一提示 $x_0$ 采样 $N$ 个 rollout，组内奖励均值作为基线计算优势。NudgeRL 的关键差异在于：采样前为每个 rollout 分配不同的策略上下文 $z_i$，形成上下文条件化提示 $x_1 = (x_0, z_i)$，从而在输入层面诱导多样性。

### 策略引导与上下文 Dropout

设计动机：标准采样反复命中高概率主导模式，导致长尾策略发现成本过高。NudgeRL 通过上下文条件化改变采样分布，使稀有策略的概率 $\pi(y|x, c)$ 显著高于 $\pi(y|x)$，从而降低发现成本。具体实现中，为每个提示 $x_0$ 构建策略上下文池 $C(x_0) = \{c_1, ..., c_M\}$，每个 rollout 独立采样一个上下文 $c_{(i)} \sim \text{Uniform}(C(x_0))$。为避免策略过拟合于上下文格式，引入上下文 Dropout 机制：以概率 $p_{\text{drop}}$ 将上下文置空，即 $z_{(i)} = c_{(i)}$ 以概率 $1-p_{\text{drop}}$，否则 $z_{(i)} = \emptyset$。最终提示为 $x_{1(i)} = (x_0, z_{(i)})$，rollout 采样自 $\pi_\theta(\cdot | x_{1(i)})$。

$$
z_{(i)} = \begin{cases}
c_{(i)} & \text{with probability } 1 - p_{\text{drop}} \\
\emptyset & \text{with probability } p_{\text{drop}}
\end{cases}
$$

该机制在输入层面强制多样性，而非依赖采样随机性，使同一预算下覆盖更多推理模式。

### 跨组优势估计与蒸馏目标

设计动机：上下文条件化导致 rollout 自然划分为多个组，组内奖励方差混杂了轨迹质量与上下文偏差，标准组内优势估计失真。NudgeRL 提出 Inter-Intra Group Advantage，分离组内信号（同一上下文下的轨迹质量）与组间信号（上下文本身的可靠性）。设上下文组 $g$ 的奖励均值为 $\bar{r}_g$，全局均值为 $\bar{r}$，则优势函数定义为：

$$
A_i = \frac{r_i - \bar{r}_g}{\sigma_g} + \lambda \frac{\bar{r}_g - \bar{r}}{\sigma_{\text{global}}}
$$

其中 $\lambda \in [0, 2]$ 控制组间信号权重。$\lambda < 1$ 鼓励探索低奖励上下文，$\lambda > 1$ 强调高可靠性上下文。此外，为解决训练-推理分布不匹配（训练时有上下文，推理时无），引入优势加权蒸馏目标：

$$
\mathcal{L}_{\text{distill}} = -\mathbb{E}_{x_0, y \sim \pi_\theta(\cdot|x_1)} \left[ A_i \log \pi_\theta(y|x_0) \right]
$$

该目标将上下文条件下发现的高优势轨迹蒸馏回基础策略 $\pi_\theta(\cdot|x_0)$，使模型在无上下文时也能复现有效推理模式。

## 实验评估

实验在 AIME24/25、AMC23、MATH500（Level 5）和 Apex Shortlist 上进行，使用 Qwen3-4B-Instruct-2507 和 Olmo-3-7B-Instruct-SFT 模型，训练集为 DAPO-17k-Processed。基线包括基础模型、GRPO（$N \in \{8, 16, 32, 64\}$）和 POPE（oracle 前缀引导）。NudgeRL 使用 8 个 rollout，上下文由 gpt-4o-mini 生成，每问题 2 个策略级上下文。

| 模型 | 方法 | Rollouts (N) | AIME24 | AIME25 | AMC23 | MATH500 | APEX | Average |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen3-4B-Instruct | Base model | – | 0.374 | 0.352 | 0.653 | 0.592 | 0.036 | 0.402 |
| Qwen3-4B-Instruct | GRPO | 8 | 0.444 | 0.367 | 0.749 | 0.668 | 0.040 | 0.454 |
| Qwen3-4B-Instruct | GRPO | 32 | 0.451 | 0.370 | 0.881 | 0.674 | 0.058 | 0.487 |
| Qwen3-4B-Instruct | GRPO | 64 | 0.415 | 0.324 | 0.848 | 0.641 | 0.027 | 0.451 |
| Qwen3-4B-Instruct | NudgeRL | 8 | 0.482 | 0.393 | 0.857 | 0.660 | 0.053 | 0.489 |
| Olmo3-7B-Instruct-SFT | Base model | – | 0.134 | 0.118 | 0.467 | 0.384 | 0.021 | 0.225 |
| Olmo3-7B-Instruct-SFT | GRPO | 32 | 0.195 | 0.176 | 0.553 | 0.459 | 0.024 | 0.281 |
| Olmo3-7B-Instruct-SFT | NudgeRL | 8 | 0.190 | 0.179 | 0.563 | 0.468 | 0.025 | 0.285 |

NudgeRL 在 8 个 rollout 下达到 0.489 平均 pass@1（Qwen3-4B），超越 GRPO-32 的 0.487 和 GRPO-64 的 0.451，表明结构化探索比暴力扩展更高效。GRPO 在 $N=64$ 时性能下降，显示暴力扩展的不稳定性。消融实验显示，$p_{\text{drop}}$ 从 0.00 增至 0.75 时，训练奖励先升后降，最优值在 0.25-0.50 区间；采样策略中，Top-ranked 上下文优于 Random，验证了策略引导的有效性。

评估边界：指标仅报告 pass@1，未提供置信区间；上下文生成依赖 gpt-4o-mini，未验证上下文质量对性能的影响；代码已开源，但超参数（如 $\lambda$、$p_{\text{drop}}$）的敏感性分析不足。

## 关联研究分析

从问题动机看，NudgeRL 与 DAPO 均针对熵坍缩，但机制不同：DAPO 通过动态采样和解耦裁剪修改优化目标，维持分布宽度；NudgeRL 通过上下文条件化修改采样分布，直接控制探索的语义方向。DAPO 的改进是统计层面的，无法确保覆盖特定推理策略；NudgeRL 的改进是结构层面的，但依赖上下文池的质量。两者未直接对比，DAPO 在长序列训练中的稳定性优势未在 NudgeRL 实验中体现。

从方法设计看，NudgeRL 与 POPE 同属“引导探索”路线，但引导信号不同：POPE 使用 oracle 解前缀，提供强监督但限制策略多样性；NudgeRL 使用策略级上下文，提供弱监督但鼓励多样化探索。NudgeRL 在平均性能上超越 POPE，表明结构化多样性优于窄幅可行性引导。然而，NudgeRL 的上下文生成独立于模型训练，未考虑模型当前能力边界，可能导致上下文与模型能力不匹配。

## 总结

NudgeRL 解决的核心矛盾是 RLVR 中探索效率与计算成本的权衡，其切入点在于通过策略上下文主动塑造采样分布，而非被动增加采样量或修改优化目标。方法通过 Inter-Intra Group Advantage 解决跨组信用分配失真，通过蒸馏目标解决训练-推理分布不匹配。实验证明，在 8 个 rollout 下，NudgeRL 超越 GRPO-64 的性能，验证了结构化探索的效率优势。但上下文生成独立于模型训练，且仅验证于数学任务，其在开放域任务中的泛化性未探索。当上下文池与模型能力边界不匹配时，策略引导是否仍能有效提升探索效率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15726)