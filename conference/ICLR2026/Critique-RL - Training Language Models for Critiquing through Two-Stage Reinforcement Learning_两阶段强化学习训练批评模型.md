# ICLR2026最新论文 ｜Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning ｜两阶段强化学习训练批评模型

研究机构：复旦大学

作者：Zhiheng Xi、Jixuan Huang、Xin Guo 等 18 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24320)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24320)

> 可规模监督（Scalable Oversight）旨在解决复杂推理任务中人类难以直接提供可靠标注的问题，核心在于训练能评估并反馈模型输出的批评模型。现有方法依赖强监督标注或测试时外部验证器，导致成本高昂或无法独立判别响应质量。本文提出 Critique-RL，通过两阶段强化学习解耦批评模型的判别性与有用性，无需强监督即可在线优化。该方法在数学推理任务上显著提升了 Actor 的修正准确率，但依赖训练时的 Oracle 验证器，限制了其在无验证器开放域任务中的直接适用性。

## 研究背景

当大语言模型（Large Language Models, LLMs）处理复杂推理任务时，其输出往往包含细微的逻辑错误，而人类专家难以对所有中间步骤进行精确标注。这种监督信号的稀缺性构成了可规模监督的核心困境。为缓解此问题，研究者引入批评模型（Critique Model），其职责是评估 Actor 生成的响应质量（判别性）并提供自然语言反馈（有用性），促使 Actor 进行自我修正。然而，批评模型自身的训练面临两难：若依赖强模型（如 GPT-4o）标注批评数据，成本极高且分布偏移严重；若仅利用 Actor 修正后的正确率作为间接奖励信号，则无法有效区分“原本正确”与“原本错误”的响应，导致判别能力退化。

主流训练路线分为提示工程与微调两类。提示工程方法（如 Reflexion）假设测试时存在外部验证器，使批评模型仅需关注反馈生成，回避了判别难题，但在无验证器场景下性能瓶颈明显。微调方法（如 Retroformer, CTRL）尝试通过强化学习优化批评模型，但仅使用间接奖励信号（如修正正确率或正确率差值）。本文发现，这种单一间接奖励会导致优化崩溃：模型要么变得过于保守（不敢指出错误），要么过于激进（将正确响应改为错误），且判别性（Acc@Dis）在训练过程中无法稳定提升。Critique-RL 的切入点在于揭示判别性与有用性在单一奖励下的冲突，并通过两阶段解耦优化策略，先建立判别基准，再优化反馈质量，从而在无强监督标注下实现稳定的批评模型训练。

## 核心方法

### 方法参照系

本文问题归属于基于人类反馈的强化学习（Reinforcement Learning from Human Feedback, RLHF）中的过程奖励建模变体，但关键差异在于：标准过程奖励模型（Process Reward Model, PRM）依赖人工或强模型标注的步骤级标签，而本文采用在线强化学习，以 Actor 的两次响应（原始与修正）的正确性作为奖励来源，且 Actor 在训练过程中保持固定，仅优化批评模型。

### 判别性优先的直接奖励优化

传统间接奖励方法（如 $r_{refine}$ 或 $r_{\Delta}$）仅关注 Actor 修正后的结果，忽略了批评模型对原始响应正确性的判断能力。本文在 Stage I 引入直接规则奖励，强制批评模型准确判断原始响应的正确性。该阶段的目标函数为：

$$ \max_{\pi_{\phi}^{Stage-I}} \mathbb{E}_{c \sim \pi_{\phi}^{Stage-I}(\cdot|x,y)} [r_{dis}(x, y, c) - \beta_{KL} KL(\pi_{\phi}^{SFT}(c|x,y) || \pi_{\phi}^{Stage-I}(c|x,y))] $$

其中 $r_{dis}(x, y, c) = \mathbb{1}[f(x, y, c) = r_{oracle}(x, y)]$，$f$ 为从批评文本中提取的正确性判断，$r_{oracle}$ 为 Oracle 验证器提供的真实标签。此设计动机在于：通过直接奖励锚定判别能力，防止后续优化中因追求有用性而牺牲对错误响应的识别精度，解决间接奖励导致的“保守”或“激进”行为失衡问题。

### 有用性优化与判别性正则化

Stage I 建立的判别基准可能缺乏反馈的构建性。Stage II 引入基于 Actor 修正正确率的间接奖励 $r_{refine}$，同时保留 Stage I 的判别奖励 $r_{dis}$ 并增加对 Stage I 模型的 KL 散度正则化。目标函数为：

$$ \max_{\pi_{\phi}^{Stage-II}} \mathbb{E}_{c \sim \pi_{\phi}^{Stage-II}(\cdot|x,y), y' \sim \pi_{\theta}(\cdot|x,y,c)} [r_{refine} + \beta_1 r_{dis}(x, y, c) - \beta_2 KL(\pi_{\phi}^{Stage-I}(c|x,y) || \pi_{\phi}^{Stage-II}(c|x,y))] $$

该公式的物理含义是：在提升反馈有用性（$r_{refine}$）的同时，通过 $\beta_1 r_{dis}$ 维持判别准确性，并通过 KL 项约束模型偏离 Stage I 判别基准的程度。这一设计解决了单一间接奖励无法同时优化判别性与有用性的冲突，确保批评模型在提供建设性反馈时，不会将原本正确的响应误判为错误，从而稳定提升 Actor 的最终修正准确率。

## 实验评估

实验在 MATH、GSM8K、AQUA（域内）及 SVAMP、TheoremQA（域外）上进行，基线包括 SFT、STaR、Retroformer 和 CTRL。Retroformer 和 CTRL 代表了仅使用间接奖励的强化学习路线，SFT 和 STaR 代表微调路线。本文方法在 Qwen2.5-7B 上域内任务平均提升 9.02%，域外任务提升 5.70%。在 Qwen2.5-3B 的 MATH 任务上，Critique-RL 的 Acc@Refine 达到 69.3%，显著高于 Retroformer 的 65.1% 和 CTRL 的 67.0%；判别性（Acc@Dis）方面，Critique-RL 在 GSM8K 上比 CTRL 高 5.31 点（3B）和 6.36 点（7B）。

| 模型 | 方法 | MATH Acc@Refine (%) | GSM8K Acc@Dis (%) | AQUA Acc@Refine (%) |
| :--- | :--- | :--- | :--- | :--- |
| Qwen2.5-3B | Retroformer | 65.1 | - | - |
| Qwen2.5-3B | CTRL | 67.0 | - | - |
| Qwen2.5-3B | Critique-RL | 69.3 | - | - |

*注：表格数值仅取自论文 Figure 1 及正文描述，部分单元格因原文未提供具体数值而留空。*

消融实验表明，移除 Stage I 或 Stage II 均导致性能下降。在 Stage II 中，若移除 $r_{dis}$ 和 KL 正则化，判别性显著恶化，验证了正则化对维持判别能力的关键作用。使用 $r_{\Delta}$ 或 $r_{correction}$ 替代 $r_{refine}$ 的效果均不如 $r_{refine}$，说明基于修正正确率的奖励在平衡保守与激进行为上更具优势。

评估边界方面，本文依赖 Oracle 验证器（如答案匹配）提供训练奖励，这限制了其在无明确正确答案的开放域任务（如创意写作）中的直接应用。代码已开源，但论文未报告不同 $\beta_1, \beta_2$ 超参数对性能的敏感性分析，也未提供 GPU 训练成本对比。

## 关联研究分析

从问题动机看，本文与过程奖励模型（PRM）路线存在本质差异。PRM（如 R-PRM）依赖人工或强模型标注的步骤级标签，旨在解决结果奖励信号稀疏问题，但标注成本高且噪声大。Critique-RL 则通过在线强化学习，利用 Actor 自身的修正行为生成奖励信号，避免了外部标注依赖。然而，PRM 的标签是静态的，而 Critique-RL 的奖励是动态的，取决于 Actor 的当前能力。这种动态性使得 Critique-RL 能自适应 Actor 的分布，但也引入了对 Actor 固定性的依赖——若 Actor 在训练中更新，奖励信号分布将发生漂移，论文未探讨此场景下的稳定性。

从方法设计看，Critique-RL 与直接偏好优化（Direct Preference Optimization, DPO）形成对比。DPO 绕过显式奖励模型，直接从偏好数据优化策略，适用于离线场景。而 Critique-RL 采用在线策略梯度，需要实时生成批评与修正响应，计算成本更高，但能捕捉更细粒度的过程反馈。DPO 的离线范式无法提供步骤级反馈，而 Critique-RL 的在线交互使其适用于需要迭代修正的推理任务。两者的核心差异在于：DPO 优化的是策略对偏好的拟合，而 Critique-RL 优化的是批评模型对响应质量的判别与反馈能力，前者是端到端对齐，后者是模块化监督。

## 总结

Critique-RL 旨在解决批评模型训练中判别性与有用性冲突导致的优化崩溃问题。现有间接奖励方法无法同时优化两者，而本文通过两阶段解耦策略，先以直接奖励建立判别基准，再以间接奖励优化有用性并正则化判别能力。实验证明，该方法在 Qwen2.5-7B 上域内任务提升 9.02%，域外任务提升 5.70%，显著优于 Retroformer 和 CTRL。其边界在于依赖训练时的 Oracle 验证器，且 Actor 固定，限制了其在无验证器任务及动态 Actor 场景中的适用性。当 Oracle 验证器不可用时，如何设计替代奖励信号以维持判别性优化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24320)