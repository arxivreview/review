# ACL2026最新论文 ｜Android Coach: Improve Online Agentic Training Efficiency with Single State Multiple Actions ｜Android Coach：单状态多动作在线强化学习框架

研究机构：浙江大学

作者：Guo Gan、Yuxuan Ding、Cong Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07277)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07277)

> 在线强化学习（RL）旨在通过环境交互提升图形用户界面（GUI）智能体的决策能力，但模拟器的高延迟与单步单动作（SSSA）范式导致样本效率低下，限制了模型在动态环境中的适应速度。现有方法如PPO和GRPO受限于每次交互仅能获取一个状态-动作对，无法充分探索高成本状态。本文提出Android Coach，采用单状态多动作（SSMA）范式，通过在线训练的Critic评估多个采样动作的价值，在不增加模拟器开销的前提下提升训练效率。该方法在AndroidWorld上较基线提升8.3%成功率，训练效率提升1.4倍，但其绝对性能仍低于领域SOTA，且Critic对未执行动作的价值估计可靠性未充分验证。

## 研究背景

GUI智能体通过像素级截图理解并操作数字设备，其核心价值在于摆脱对HTML或Accessibility Tree等结构化数据的依赖，实现跨平台通用交互。当智能体执行多步任务时，早期微小错误会导致后续轨迹偏离，即错误累积问题。解决此问题需要智能体具备自主纠错能力，而强化学习（RL）通过试错机制提供这种能力。然而，在线RL依赖模拟器交互，每次交互包含初始化、恢复和反应等高延迟环节，总耗时是模型加载与推理时间的1.7倍，导致状态收集成本高昂。

主流在线RL方法采用单状态单动作（SSSA）范式，如UI-TARS-2中的PPO和MobileRL中的GRPO。该范式下，智能体在每个状态仅采样一个动作，执行后环境立即转移至下一状态，无法尝试其他动作。这导致两个问题：一是状态探索不充分，智能体难以发现更优动作；二是样本效率低，相同训练时间内获取的有效样本有限。离线方法虽避免交互延迟，但受限于数据质量且无法适应应用更新。本文切入点在于解耦动作评估与环境交互：通过在线训练的Critic估计多个动作的价值，使智能体能在同一状态下探索多个动作，从而提升样本效率。

## 核心方法

### 方法参照系

在线Actor-Critic框架中，策略网络（Actor）与环境交互收集轨迹，价值网络（Critic）估计状态-动作价值以指导策略更新。标准流程中，Critic仅基于已执行动作的回报进行训练，策略更新依赖单状态单动作（SSSA）范式。本文的关键差异在于：Critic不仅评估已执行动作，还评估同一状态下未执行的其他动作，实现单状态多动作（SSMA）探索。

### 过程奖励模型引导的Critic训练

传统Critic训练仅使用轨迹级结果奖励，导致失败轨迹中的正确步骤无法获得正向信号，中间步骤监督不足。本文引入预训练的过程奖励模型（PRM），为每个中间动作提供步级奖励。PRM作为推理模型，先生成分析再生成判断，其训练数据由离线轨迹和初步滚动数据构建，共20k样本，每个样本结构为$(I, s_t, a_t, label)$，其中$I$为指令，$s_t$为状态，$a_t$为动作，$label$为二值标签。Critic的目标回报$R_t$通过加权蒙特卡洛估计计算：

$$R_t = \omega_p \sum_{\tau=t}^{T} \gamma^{T-\tau} r_p^\tau + \omega_o r_o$$

其中$r_p^\tau$为PRM提供的步级过程奖励，$r_o$为结果验证器提供的结果奖励，$\gamma$为折扣因子，$\omega_p, \omega_o$为权重参数。该设计使Critic能区分失败轨迹中的正确步骤，提供更细粒度的监督信号，解决传统方法中中间步骤奖励稀疏的问题。

### 单状态多动作与ACLOO优势估计

在SSMA范式中，智能体对每个在线状态$s_t$采样$k$个候选动作$\{a_t^1, ..., a_t^k\}$，Critic评估这些动作的价值$Q_\phi(s_t, a_t^i)$。为避免训练额外的状态价值模型，本文提出Actor-Critic Leave-One-Out（ACLOO）优势估计方法。对于动作$a_t^i$，其优势估计为：

$$A(s_t, a_t^i) = Q_\phi(s_t, a_t^i) - \frac{1}{k-1} \sum_{j \neq i} Q_\phi(s_t, a_t^j)$$

该公式以组内其他动作的平均Q值作为基线，无需额外状态价值网络即可降低估计方差。ACLOO机制捕捉候选动作间的相对质量，引导策略学习优于平均水平的动作。相比RLOO基于奖励的优势估计，ACLOO使用长期价值，更适合GUI任务的长程依赖特性。策略更新采用PPO裁剪代理损失，利用ACLOO优势进行梯度优化。

## 实验评估

实验在AndroidLab（138个任务）和AndroidWorld（116个任务）上进行，基线包括UI-TARS-1.5-7B（Base/GRPO/PPO）及专有模型。Android Coach在UI-TARS-1.5-7B骨干上，将AndroidLab成功率从31.9%提升至39.4%，AndroidWorld从32.8%提升至41.1%。

| 模型 | AndroidLab SR (%) | AndroidWorld SR (%) |
| :--- | :--- | :--- |
| UI-TARS-1.5-7B (Base) | 31.9±0.7 | 32.8±2.3 |
| w/ GRPO | 34.8±1.4 | 38.2±2.2 |
| w/ PPO | 35.0±1.1 | 37.4±1.8 |
| w/ Android Coach | 39.4±0.8 | 41.1±1.8 |

消融实验显示，动作采样数$N$从1增至4时，AndroidLab成功率从34.8%提升至37.0%，训练时间仅增加1.62倍；$N$增至8时性能增益边际化，训练时间增至2.18倍，呈现次线性增长。PRM的引入使AndroidLab成功率从37.0%提升至39.4%，合理操作比率（ROR）提升6.6%。ACLOO优势估计使AndroidLab成功率从36.0%提升至39.4%，训练奖励曲线更平稳。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码已开源，但Critic对未执行动作的价值估计可靠性未充分验证，SSMA范式在极端分布外场景下的表现未知。

## 关联研究分析

从问题动机看，Android Coach与MobileRL同属在线RL路线，但MobileRL采用GRPO/SSSA范式，依赖完整轨迹获取结果奖励，而Android Coach通过Critic解耦动作评估与环境交互，实现SSMA探索。这一差异源于对样本效率的不同权衡：MobileRL追求轨迹级监督的完整性，Android Coach追求状态级探索的充分性。在相同训练时间预算下，Android Coach比PPO高5.2%成功率，比GRPO/PPO高1.4倍效率，表明SSMA范式在有限交互成本下更具优势。

从方法设计看，Android Coach与DigiRL同属混合RL框架，但DigiRL依赖离线演示数据初始化策略，受限于数据质量且无法适应应用更新，而Android Coach完全在线训练，通过PRM提供步级监督，避免离线数据的分布偏移问题。DigiRL的Critic训练仅使用结果奖励，而Android Coach引入PRM，使Critic能区分失败轨迹中的正确步骤，提供更细粒度的监督。这一设计差异源于对中间步骤监督重要性的不同认识：DigiRL关注轨迹级优化，Android Coach关注步骤级纠错。

## 总结

Android Coach解决的核心矛盾是在线RL中模拟器高延迟与样本效率低下的冲突。现有SSSA方法受限于每次交互仅获取一个状态-动作对，无法充分探索高成本状态，而Android Coach通过Critic解耦动作评估与环境交互，实现SSMA范式，在不增加模拟器开销的前提下提升探索充分性。该方法在AndroidWorld上较基线提升8.3%成功率，训练效率提升1.4倍，验证了SSMA范式的有效性。然而，其绝对性能（41.1%）仍低于领域SOTA（70.0%），且Critic对未执行动作的价值估计可靠性未充分验证。当训练分布外的新应用出现时，Critic的价值估计是否仍能保持可靠，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07277)