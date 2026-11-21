# HuggingFace最新推荐论文 ｜StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction ｜策略轨迹抽象

研究机构：香港中文大学、美国佐治亚大学

作者：Xiangyuan Xue、Yifan Zhou、Zidong Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.06642)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06642)

> 长程智能体任务中，稀疏奖励与多步依赖导致传统反应式强化学习（RL）难以区分关键决策步骤的贡献，且探索易陷入局部最优。现有基于组相对策略优化（GRPO）的方法仅在同一任务下比较轨迹，缺乏对全局行动路径的显式约束，导致策略短视与行为不一致。StraTA 通过在 episode 起始生成固定自然语言策略并条件化后续动作，结合层级化 GRPO 训练、最远点采样（FPS）策略多样性及关键自我判断步级惩罚，将规划与执行解耦。该方法在 ALFWorld 与 WebShop 上显著优于单智能体基线，但其策略固定机制在动态环境中的适应性存疑。

## 研究背景

长程智能体任务要求模型在部分可观测马尔可夫决策过程（POMDP）中维持状态一致性并处理延迟奖励。当智能体仅依据当前状态生成动作时，策略必须同时推断长期行动路径与即时步骤，这种耦合导致探索短视与回溯冗余。为缓解此问题，组相对策略优化（GRPO）移除 Critic 网络，通过组内相对奖励比较计算优势，降低了计算开销，但其组内比较仅限于同一任务下的多条轨迹，无法区分不同全局策略的质量差异。

Agentic RL 的核心挑战在于稀疏奖励下的信用分配与探索效率。主流路线如 GiGPO 引入锚点状态细化优势估计，但仍属于反应式范式，未解决“先规划后执行”的认知结构缺失。StraTA 的切入点在于引入显式轨迹级策略抽象，将决策分解为策略生成与动作执行两个子目标，从而在 GRPO 框架内实现策略级与动作级的双重优化。

## 核心方法

### 层级化组构建

标准 GRPO 对同一任务采样 $G$ 条轨迹，计算组内归一化优势 $\hat{A}_i = \frac{r_i - \text{mean}(r)}{\text{std}(r)}$。StraTA 将采样结构扩展为两级：对每个任务采样 $N$ 个策略 $\{z_i\}$，每个策略下执行 $M$ 次 rollout $\{\tau_{i,j}\}$。策略级组比较不同策略 $z_i$ 的质量，动作级组比较同一策略下不同轨迹 $\tau_{i,j}$ 的执行效果。策略奖励采用 top-$\delta$ 均值而非全量均值，以抑制早期动作噪声对策略质量评估的干扰：

$$ R(z_i) = \frac{1}{\lceil \delta M \rceil} \sum_{j \in \text{top-}\delta} R(\tau_{i,j}) $$

该设计使策略优势反映其最佳潜在性能，而非执行瑕疵。

### 多样化策略采样与步级惩罚

为解决高温度采样下策略语义趋同问题，StraTA 引入最远点采样（FPS）。首先过采样 $\sigma N$ 个候选策略，利用预训练嵌入模型 $\phi(\cdot)$ 计算余弦相似度，贪心选择与已选集合最大相似度最小的策略，确保策略空间覆盖度。针对动作执行中偏离策略且未推进任务的行为，引入关键自我判断（Critical Self-judgment）步级辅助奖励：

$$ r_{\text{step}} = \kappa \cdot \mathbb{I}(\text{not follow } z \land \text{no progress}) $$

其中 $\kappa$ 为惩罚权重。该机制在轨迹级结果奖励之外提供细粒度梯度信号，直接抑制无效动作重复，缓解熵坍缩。

## 实验评估

实验在 ALFWorld、WebShop 与 SciWorld 上进行，基线涵盖 PPO、GRPO、GiGPO 及 GPT-5.1 等闭源模型。StraTA 在单智能体框架内表现突出，但缺失与 Tree-GRPO 等细粒度信用分配方法的直接对比。

| 方法 | ALFWorld (7B) | WebShop (7B) | SciWorld (7B) |
| :--- | :--- | :--- | :--- |
| GiGPO | 90.8 | 72.8 | - |
| StraTA | 93.1 | 84.2 | 63.5 |
| Claude-4-Sonnet | 72.9 | 22.2 | 57.4 |

StraTA 在 ALFWorld 上较 GiGPO 提升 2.3 个点，在 WebShop 上提升 11.4 个点，SciWorld 总分超越最强闭源模型 Claude-4-Sonnet 6.1 个点。消融实验显示，移除 FPS 导致 ALFWorld 成功率从 93.1% 降至 87.9%，移除自我判断则降至 81.9%，表明策略多样性与步级惩罚对性能贡献显著。

评估协议采用 AgentGym 统一框架，报告 3 个随机种子的均值。代码与模型已开源，超参数包括 4 策略、8 rollout、$\sigma=8$、$\delta=0.5$。局限在于未报告计算效率指标，且 SciWorld 中 Lifespan 子集达到 100% 可能反映任务特定过拟合。

## 关联研究分析

从问题动机看，StraTA 与 Tree-GRPO 均致力于解决长程信用分配，但路径不同。Tree-GRPO 通过树搜索扩展轨迹采样空间，基于树结构进行细粒度优势估计，属于“结构化采样”路线；StraTA 则通过显式策略抽象将问题分解为规划与执行，属于“认知结构解耦”路线。前者依赖计算密集型搜索，后者依赖语义空间多样性，StraTA 在计算效率上更具优势，但策略固定机制可能限制其在动态环境中的适应性。

从方法设计看，StraTA 与 GiGPO 同属 GRPO 变体，但 GiGPO 使用状态锚点细化优势，StraTA 使用策略锚点。GiGPO 的锚点状态是隐式的，而 StraTA 的策略是显式自然语言，这使得策略质量可被直接评估与优化。然而，StraTA 未探索策略的动态重规划，当环境状态发生显著变化时，固定策略可能导致执行偏差，这是其相对于反应式方法在灵活性上的潜在短板。

## 总结

StraTA 针对长程 Agentic RL 中反应式决策导致的短视探索与信用分配模糊问题，通过引入显式轨迹级策略抽象，将规划与执行解耦。该方法在层级化 GRPO 框架下，结合 FPS 策略多样性与步级自我判断惩罚，在 ALFWorld 与 WebShop 上分别达到 93.1% 与 84.2% 的成功率，SciWorld 总分 63.5% 超越闭源模型。其边界在于策略一旦生成即固定，未涉及在线修正机制，且在多智能体协作主导的 SOTA 坐标系中（如 Stronger-MAS 的 99.5%）仍有差距。当环境状态在 episode 中途发生不可预测变化时，固定策略的执行偏差是否可通过步级惩罚完全补偿，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06642)