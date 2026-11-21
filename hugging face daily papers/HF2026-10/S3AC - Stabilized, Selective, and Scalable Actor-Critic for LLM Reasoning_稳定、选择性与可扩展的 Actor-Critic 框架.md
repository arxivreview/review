# HuggingFace最新推荐论文 ｜S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning ｜稳定、选择性与可扩展的 Actor-Critic 框架

作者：Shuo Shen、Guangran Cheng、Chengqi Lyu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.35518)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.35518)

> 导读 长思维链推理中的强化学习面临稀疏奖励导致的信用分配模糊与探索效率低下问题。现有无 Critic 方法如 GRPO 依赖组内统计估计基线，缺乏 Token 级细粒度信号，且在单 Rollout 场景下性能崩塌。S3AC 引入经过多策略预训练与稳定化优化的 Critic，提供难度感知的基线与 Token 级优势，并基于 Critic 初始值实现生成前的难度感知提示采样。该框架在 1.5B 至 397B 参数模型上验证了 Actor-Critic 在长 CoT RLVR 中的有效性，但 Critic 预训练数据分布对分布外任务的泛化影响仍存疑。

## 研究背景

当大语言模型在数学或代码等可验证任务中进行长思维链推理时，最终答案的二元奖励信号过于稀疏，无法区分长序列中关键推理步骤与无关 Token 的贡献。这种稀疏性导致信用分配困难，模型难以从失败轨迹中定位错误。为缓解此问题，组相对策略优化（Group Relative Policy Optimization, GRPO）通过同一提示词下多个响应的奖励均值作为基线，消除了对独立价值网络（Critic）的需求，大幅降低了内存开销。然而，GRPO 的基线估计依赖组内所有响应生成完毕，且优势函数在序列内均匀广播，无法反映推理过程中状态价值的动态变化。

在单 Rollout 场景下，GRPO 退化为使用批次统计量，完全丧失了对提示词难度的感知能力，导致模型在简单与困难问题上获得相同的更新信号。虽然过程奖励模型（Process Reward Models, PRM）可提供密集反馈，但其标注成本高且易受奖励黑客攻击。近期研究如 Token Hidden Reward 试图从策略梯度中挖掘隐藏信号，但仍受限于无 Critic 架构的固有缺陷。S3AC 指出，学习一个可靠的 Critic 是同时解决提示词难度感知与 Token 级信用分配的关键，但长序列 Critic 训练面临轨迹覆盖不足与初始梯度主导两大障碍。

## 核心方法

### 方法参照系：Actor-Critic 在长 CoT 中的失效模式

标准 Actor-Critic 框架中，Critic 估计状态价值 $V_\phi(s_t)$，Actor 利用广义优势估计（Generalized Advantage Estimation, GAE）计算优势函数。在长 CoT RLVR 中，直接应用该框架面临两个具体失效：一是初始策略生成的轨迹多为短且错误的响应，导致 Critic 对长且正确的轨迹缺乏监督信号，价值估计偏差大；二是新初始化的价值头（Value Head）梯度范数远大于骨干网络，早期训练被价值头梯度主导，导致骨干网络更新被过度缩放，训练不稳定。S3AC 针对这两个失效模式设计了预训练与优化策略。

### 稳定化 Critic 训练：多策略预训练与梯度控制

为解决轨迹覆盖不足，S3AC 采用多策略混合预训练。不同于 VC-PPO 使用固定初始策略，S3AC 从不同强度的策略中收集轨迹，覆盖从短错误到长正确的响应分布。预训练阶段冻结注意力层与 MoE 路由器，仅训练价值头，使用截断平方误差损失回归蒙特卡洛回报。

针对梯度主导问题，S3AC 实施两项关键优化。首先，价值头初始化标准差设为 $1/(H+1)$，其中 $H$ 为隐藏层大小，以控制初始预测幅度。其次，将 Critic 的梯度裁剪阈值从常见的 1 提升至 10。这一设计动机在于，价值头梯度直接依赖隐藏状态，而进入骨干网络的梯度被小权重缩放；若使用统一的小阈值裁剪，会过度压缩骨干网络的有效更新。在线训练阶段，Critic 学习率设为 Actor 的 5 倍，且每批次执行 2 个 Critic 轮次，以加速价值估计收敛。

### 难度感知提示采样（DAPS）：生成前的动态筛选

Critic 的初始状态价值 $V_\phi(s_0)$ 提供了生成前的提示词难度估计。S3AC 提出难度感知提示采样（Difficulty-Aware Prompt Sampling, DAPS），替代 DAPO 的事后过滤机制。DAPS 将 Critic 估计值与历史观测结果结合，计算成功概率估计 $\hat{p}$：

$$
\hat{p} = \frac{S + n_c p_c}{N + n_c}, \quad p_c = \text{clip}\left(\frac{V_\phi(s_0)+1}{2}, 0, 1\right)
$$

其中 $S$ 和 $N$ 为历史成功与总尝试次数，$n_c$ 控制 Critic 权重。对于新提示词，估计值直接由 Critic 初始化，无需离线 Rollout。

基于 $\hat{p}$，DAPS 采用如下接受概率 $a$ 筛选提示词：

$$
a = a_{\min} + (1 - a_{\min}) 4\hat{p}(1 - \hat{p})
$$

该概率在 $\hat{p}=0.5$ 时达到峰值，优先选择中等难度提示词。$a_{\min}$ 作为接受下限，确保极难或极易提示词仍有被选中的机会，类似 $\epsilon$-greedy 探索。这一机制在生成前即排除低信息量提示词，减少了组内全对或全错导致的零优势计算浪费。

## 实验评估

实验在 Qwen2.5-Math-1.5B、R1-Distill-1.5B、Intern-S2-Preview-35B 及 Intern-S2-397B 四个模型上进行，涵盖数学、科学推理及多模态基准。基线包括 GRPO-X（组 Rollout）、REINFORCE++ 与 FlashREINFORCE（单 Rollout）。

| 模型 | 方法 | 设置 | MATH500 | AMC23 | AIME25 | Olympiad | Minerva | Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen2.5-Math-1.5B | GRPO-X | Group | 72.3 | 57.3 | 9.0 | 35.3 | 39.8 | 42.7 |
| Qwen2.5-Math-1.5B | S3AC | Group | 71.7 | 56.7 | 11.2 | 35.4 | 41.3 | 43.3 |
| Qwen2.5-Math-1.5B | REINFORCE++ | Single | 69.3 | 56.6 | 8.1 | 32.1 | 36.1 | 40.4 |
| Qwen2.5-Math-1.5B | S3AC | Single | 71.4 | 57.3 | 10.2 | 35.4 | 40.7 | 43.0 |

在 1.5B 模型上，S3AC 在组 Rollout 设置下平均性能略高于 GRPO-X（43.3 vs 42.7），在单 Rollout 设置下显著优于 REINFORCE++（43.0 vs 40.4）。在 35B 模型上，S3AC 组 Rollout 平均分为 80.5，较 GRPO-X 的 76.4 提升 4.1 分；单 Rollout 平均分为 80.9，较 REINFORCE++ 的 70.4 提升 10.5 分。397B 模型上，S3AC 组 Rollout 平均分为 87.3，较 GRPO-X 的 85.1 提升 2.2 分。

训练动态显示，单 Rollout 基线在初期提升后性能下降，而 S3AC 在 1600 步内保持性能稳定。REINFORCE++ 出现熵与响应长度快速膨胀，FlashREINFORCE 则趋向短响应，S3AC 通过 Critic 提供的稳定基线避免了这些退化。DAPS 进一步提升了样本效率，减少了动态采样丢弃的轨迹数量。

评估边界方面，论文未提供代码开源链接，超参数细节部分依赖附录。未对比 SC-GRPO 或 Token Hidden Reward 等纯 Critic-free 细粒度方法，无法直接量化 Critic 相对于隐藏信号挖掘的增益。397B 上的提升幅度较小，可能受限于模型规模带来的基线饱和效应。

## 关联研究分析

从信用分配机制看，S3AC 与 Token Hidden Reward 均旨在解决序列级优势广播的模糊性。Token Hidden Reward 通过正负样本对比挖掘 Token 级隐藏信号，无需外部 Critic，计算开销低但依赖样本对比的统计显著性。S3AC 通过显式 Critic 提供连续的价值估计，能更平滑地反映推理过程中的状态变化，但引入了 Critic 训练的不稳定性风险。S3AC 的 GAE 优势计算依赖于 Critic 的准确性，若 Critic 预训练覆盖不足，其 Token 级信号可能引入偏差，而 Token Hidden Reward 直接基于策略梯度更新，避免了这一依赖。

从探索机制看，S3AC 的 DAPS 与 DAPO 的动态采样均关注中等难度样本。DAPO 在生成后丢弃全对或全错组，计算浪费大；DAPS 利用 Critic 初始值在生成前筛选，效率更高。然而，DAPS 依赖 Critic 对难度的准确估计，若 Critic 对分布外提示词估计偏差大，可能导致采样偏差。相比之下，基于不确定性或信息增益的探索方法不依赖价值估计，但计算成本更高。S3AC 复用 Critic 实现采样，体现了架构设计的经济性，但其鲁棒性受限于 Critic 的泛化能力。

## 总结

S3AC 针对长 CoT RLVR 中 Critic 训练不稳定与探索效率低下的矛盾，通过多策略预训练与梯度控制稳定 Critic，并复用 Critic 初始值实现生成前难度感知采样。在 35B 模型上，S3AC 单 Rollout 性能较 REINFORCE++ 提升 10.5 分，验证了 Critic 在缺乏组内基线时的关键作用。其边界在于 Critic 预训练数据分布对分布外任务的泛化能力未充分验证，且 397B 上的增益幅度随规模增大而缩小。当模型规模进一步扩大至万亿参数时，Critic 的预训练成本与在线更新开销是否会抵消其带来的信用分配增益，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.35518)