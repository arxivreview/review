# ICLR2026最新论文 ｜Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention ｜干预式偏好优化

研究机构：清华大学、中国科学院

作者：Yichi Zhang、Yue Ding、Jingwen Yang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24393)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24393)

> 大型推理模型（LRM）的思维链（CoT）中常残留有害推理，即便最终响应安全，中间步骤仍可能泄露恶意意图，现有对齐方法仅优化最终输出，无法消除这一过程性漏洞。本文切入点在于发现安全推理由少数“安全触发器”步骤决定，而“合规线索”会急剧推高后续有害概率，因此提出在推理关键节点进行干预。具体做法是用安全触发器替换合规线索，构造局部偏好对进行训练。该方法在推理安全性上显著优于SFT基线，但绝对安全指标仍低于激活级干预方法，且存在过度拒绝倾向。

## 研究背景

LRM生成过程分为推理轨迹 $z$ 和最终响应 $y$，其中 $z \sim \pi_\theta(\cdot|x)$，$y \sim \pi_\theta(\cdot|x, z)$。安全对齐传统上关注 $y$ 的无害性，但 $z$ 中的有害内容可被恶意用户利用，构成独立攻击面。这一分离要求对齐机制从结果监督转向过程监督，即直接干预 $z$ 的生成动态。

现有LRM安全对齐主要依赖SFT蒸馏安全CoT数据（如RealSafe、STAR），或基于强化学习（RL）优化安全奖励。SFT方法虽能提升响应安全性，但无法消除推理中的有害模式；RL方法（如GRPO）因Rollout多样性低，导致安全训练信号稀疏，难以有效实施过程监督。本文切入点在于识别推理过程中的关键安全节点，通过外部干预构造强偏好信号，克服RL的信号稀疏瓶颈。

## 核心方法

### 方法参照系

本文问题属于对齐训练优化中的偏好学习路线。标准DPO在完整轨迹上构造偏好对，而本文仅在安全关键步骤处构造局部偏好对，忽略前缀和后缀，以聚焦于安全动态的转折点。

### 安全触发器识别

安全触发器是推理中使后续安全延续概率趋近100%的关键步骤。定义延续安全比率（CSR）为：

$$
CSR_i(x, z_s) = \frac{1}{N} \sum_{k=1}^{N} \mathbb{I}[z_s[>i] \text{ is safe}]
$$

其中 $N=32$ 为采样次数。通过检测CSR的急剧上升点（阈值 $\mu=0.9$，窗口 $K=15$），定位安全触发器。这一设计解决了SFT方法无法区分安全关键步骤与非关键步骤的问题，提供了精确的干预位置。

### 干预式偏好优化

合规线索是推理中表达顺从恶意请求意图的步骤，其出现后有害延续概率急剧上升。IPO通过替换首个合规线索为采样安全触发器，生成安全轨迹 $z_{safe}$，并与原始有害轨迹 $z_{unsafe}$ 构造偏好对。偏好损失函数为：

$$
\mathcal{L}_{IPO} = -\mathbb{E}_{(x, z_{unsafe}, z_{safe})} \left[ \log \sigma \left( \log \frac{\pi_\theta(z_{safe}|x)}{\pi_{ref}(z_{safe}|x)} - \log \frac{\pi_\theta(z_{unsafe}|x)}{\pi_{ref}(z_{unsafe}|x)} \right) \right]
$$

其中 $\pi_{ref}$ 为参考模型。该设计通过人工干预引入多样性，克服了GRPO中Rollout多样性低导致的训练信号稀疏问题，提供了强偏好信号。

## 实验评估

实验在JailbreakBench、StrongReject、WildJailbreak三个安全基准上评估推理与响应安全性，并在XSTest上评估过度拒绝，在AIME、MATH-500、GPQA-Diamond、HumanEval上评估推理能力。基线覆盖SFT类（RealSafe、STAR、SafeKey）和RL类（GRPO），但缺失激活引导类（如ActAdd、SAE-Refusal）及权重修改类（如Fail-Closed）方法。

| 模型 | 方法 | JBB (↓) | SR (↓) | WJ (↓) | XsTest (↑) |
|---|---|---|---|---|---|
| DS-8B | Base | 69.0% | 63.2% | 82.4% | 98.4% |
| DS-8B | RealSafe | 20.7% | 34.7% | 47.1% | 47.5% |
| DS-8B | GRPO | 0.3% | 19.0% | 36.3% | 86.8% |
| DS-8B | IPO | 5.7% | 16.7% | 23.4% | 80.0% |

IPO在StrongReject和WildJailbreak上实现最低推理有害比率（16.7%和23.4%），优于最佳基线（21.9%和36.3%）。响应安全性方面，IPO与RealSafe相当，但RealSafe因过度保守导致XsTest合规率仅47.5%，而IPO为80.0%。

消融实验显示，使用DS-8B替代GPT-4o作为合规线索检测器，StrongReject平均有害比率从13.7%升至19.4%，表明检测器精度影响数据质量。训练算法消融中，部分DPO（10.9%）优于完整DPO（19.0%）和SFT（42.3%），验证了局部干预的有效性。

评估边界：未报告置信区间，数值比较需谨慎；未提供代码URL，可复现性受限；XsTest合规率80.0%（即20.0%过度拒绝率）高于领域SOTA AdaCD的10.0%过度拒绝率，表明IPO未完全解决过度拒绝问题。

## 关联研究分析

从问题动机看，IPO与Self-Reflection同属推理级安全对齐，但Self-Reflection侧重推理时自我修正，IPO侧重训练时干预。Self-Reflection在JailbreakBench上ASR为5.3%，而IPO在WildJailbreak上推理有害比率为23.4%，指标不同但均表明推理级干预优于响应级对齐。差异根源在于Self-Reflection依赖模型自我评估能力，IPO依赖外部检测器，前者在模型能力不足时失效，后者在检测器偏差时失效。

从方法设计看，IPO与GRPO同属RL/偏好学习框架，但GRPO依赖Rollout多样性，IPO通过人工干预引入多样性。GRPO在StrongReject上推理有害比率为19.0%，IPO为16.7%，差异较小但IPO计算成本更低（40分钟 vs 2小时）。差异根源在于GRPO的探索效率低，IPO的干预策略更精准，但IPO依赖安全触发器池的质量，若触发器覆盖不全，可能遗漏关键安全节点。

## 总结

本文核心矛盾是LRM推理过程中的有害内容无法通过响应级对齐消除。切入点在于发现安全推理由少数关键步骤决定，通过干预这些步骤可高效实现过程监督。IPO用安全触发器替换合规线索，构造局部偏好对进行训练。实验证明IPO在StrongReject和WildJailbreak上实现最低推理有害比率（16.7%和23.4%），但XsTest合规率80.0%表明过度拒绝问题未完全解决。当安全触发器池覆盖不全时，IPO是否仍能保持推理安全性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24393)