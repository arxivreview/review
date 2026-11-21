# HuggingFace最新推荐论文 ｜Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization ｜探索性记忆增强混合策略优化

研究机构：微软研究院、韩国科学技术院

作者：Zeyuan Liu、Jeonghye Kim、Xufang Luo 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23008)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23008)

> 在线强化学习（RL）训练大语言模型（LLM）智能体时，模型常因过度依赖预训练先验而陷入局部最优，无法在需要发现新状态的环境中有效探索。现有方法要么仅更新参数导致探索停滞，要么仅使用外部记忆导致性能快速饱和。本文提出 EMPO²，通过联合更新参数化策略与非参数化记忆模块，并引入 On/Off-policy 混合优化机制，使智能体在探索中积累知识并内化至模型权重。该框架在 ScienceWorld 和 WebShop 上显著优于 GRPO 基线，但其对记忆检索机制的依赖及 Off-policy 蒸馏的泛化边界仍需进一步验证。

## 研究背景

LLM 智能体在交互决策中面临的核心困境是“探索-利用”失衡。当智能体执行动作时，策略 $\pi_\theta$ 基于当前状态 $s_t$ 生成动作 $a_t$，环境返回奖励 $r_t$ 与下一状态 $s_{t+1}$。若智能体仅利用预训练知识，其动作分布将局限于熟悉区域，导致在稀疏奖励环境中无法发现通往目标的新路径。为突破这一限制，引入外部记忆模块 $M$ 存储历史轨迹中的反思提示（Tips），通过检索相关 Tips 引导智能体尝试非常规动作，从而扩展探索空间。

当前主流路线存在明显瓶颈。纯参数化 RL 方法如 GRPO（Shao et al., 2024）通过组内相对优势估计优化策略，但缺乏跨轨迹的信息传递机制，导致智能体在失败后无法从错误中吸取教训，性能迅速收敛至次优解。纯非参数化方法如 Reflexion（Shinn et al., 2023）虽能通过记忆修正行为，但参数固定导致知识无法内化，性能随训练步数增加而饱和。本文切入点在于构建参数与非参数更新的闭环：记忆引导探索产生高质量轨迹，参数更新将探索收益固化，从而打破“探索停滞”与“知识饱和”的双重限制。

## 核心方法

### 方法参照系

EMPO² 基于在线 RL 的标准流程：Rollout 阶段生成轨迹，Update 阶段优化策略。与 GRPO 仅使用参数化更新不同，EMPO² 在 Rollout 阶段引入记忆增强提示，在 Update 阶段区分 On-policy 与 Off-policy 两种模式，形成混合优化机制。

### 记忆引导的探索机制

设计动机：解决 GRPO 中轨迹间缺乏连续性、智能体无法从失败中反思的问题。在 Rollout 阶段，智能体以概率 $p$ 启用记忆增强提示。对于任务 $u$ 和状态 $s_t$，检索算子 $\text{Retr}(o_t; M)$ 从记忆库 $M$ 中选取最相关的 Tips 集合 $\text{tips}_t$。策略据此生成动作：

$$ a_{t+1} \sim \pi_\theta(\cdot | s_t, u, \text{tips}_t) $$

该公式表明，动作生成不仅依赖当前状态，还受历史反思信息引导。Tips 由策略 $\pi_\theta$ 在轨迹结束时自主生成，例如“未找到绿色电线，需检查其他房间”，从而避免重复无效动作。

### 混合 On/Off-policy 优化

设计动机：解决记忆辅助知识无法内化至参数、导致测试时无记忆性能下降的问题。在 Update 阶段，记忆增强轨迹以概率 $q$ 采用 Off-policy 更新。此时，重要性采样比率 $\rho_\theta$ 的计算方式改变：

$$ \rho_\theta(a_{t}^{[i]}) = \frac{\pi_\theta(a_{t}^{[i]} | s_{t}^{[i]}, u)}{\pi_{\theta_{\text{old}}}(a_{t}^{[i]} | s_{t}^{[i]}, u, \text{tips}_t)} $$

该公式将记忆增强策略视为教师，无记忆策略视为学生，通过奖励信号引导学生模仿高奖励轨迹的行为。高优势轨迹被强化，低优势轨迹被抑制，实现选择性知识蒸馏。此外，引入低概率 Token 掩码机制，当 $\pi_\theta(a_t | s_t, u) < \delta$ 时，优势项被置零，防止 Off-policy 训练中的梯度爆炸。

## 实验评估

实验在 ScienceWorld 和 WebShop 上进行，基线模型为 Qwen2.5-7B-Instruct。对比方法包括 Reflexion、Retrospex、GRPO 和 GiGPO。EMPO² 在 ScienceWorld 平均成功率达 75.9%，较 GRPO 的 33.2% 提升 128.6%；在 WebShop 平均成功率达 88.3%，较 GRPO 的 79.3% 提升 11.3%。

| 基准 | 方法 | 平均成功率 (%) |
| :--- | :--- | :--- |
| ScienceWorld | GRPO | 33.2 |
| ScienceWorld | EMPO² | 75.9 |
| WebShop | GRPO | 79.3 |
| WebShop | EMPO² | 88.3 |

消融实验显示，移除 Off-policy 学习或 On-policy 记忆学习均导致性能下降。在 ScienceWorld 的 power-component 任务中，完整 EMPO² 达到 94.3%，而移除 Off-policy 学习后降至 89.5%，移除 On-policy 记忆学习后降至 82.7%。这表明两种更新模式具有互补性：On-policy 保证训练稳定性，Off-policy 实现知识内化。

评估边界方面，论文未报告计算效率指标，且记忆检索仅采用简单相似度搜索，未探索更复杂的检索机制。代码已开源，但超参数（如 $p, q, \delta$）的敏感性分析仅在附录中简要提及，缺乏系统性消融。

## 关联研究分析

从问题动机看，EMPO² 与 Reflexion 的核心差异在于知识内化路径。Reflexion 仅通过记忆修正行为，参数固定导致性能饱和；EMPO² 通过 Off-policy 蒸馏将记忆收益固化至参数，使测试时无记忆仍具备探索能力。这一差异源于任务特性：ScienceWorld 等环境要求智能体具备长期适应能力，而非仅短期修正。

从方法设计看，EMPO² 与 GiGPO 同属在线 RL 改进，但关注点不同。GiGPO 通过观察分组细化信用分配，解决长程任务中奖励稀疏问题；EMPO² 通过记忆引导探索，解决智能体无法发现新状态的问题。两者可视为互补：GiGPO 优化“如何分配奖励”，EMPO² 优化“如何发现奖励”。论文未探索将两者结合的可能性，这或许是未来方向。

## 总结

EMPO² 针对 LLM 智能体在稀疏奖励环境中探索停滞的问题，提出参数与非参数联合更新框架。通过记忆引导探索产生高质量轨迹，并通过 Off-policy 蒸馏将知识内化至参数，实现了 ScienceWorld 上 128.6% 的性能提升。然而，其依赖简单相似度检索的记忆机制，以及 Off-policy 蒸馏在分布外任务上的泛化能力，仍是未解之谜。当记忆库规模扩大至数千条 Tips 时，检索精度与计算开销的平衡如何维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23008)