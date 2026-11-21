# HuggingFace最新推荐论文 ｜DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models ｜扩散模型在线强化学习的稳定性与效率优化

研究机构：新加坡国立大学

作者：Zhenglin Wan、Jiayu Chen、Zhengfeiyang Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.12572)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.12572)

> 在线强化学习（Reinforcement Learning, RL）通过黑盒奖励优化扩散模型，但前向过程方法（如 DiffusionNFT）因隐含的前向-反向速度场不一致导致训练崩溃，需依赖指数移动平均（Exponential Moving Average, EMA）调参维持稳定。现有方法在效率与稳定性间存在根本张力：反向过程 RL 信用分配差，前向过程 RL 需逐任务调参。DiffusionART 提出聚合优先奖励倾斜（Aggregation-First Reward Tilting），将奖励信号聚合为共享方向直接作用于反向状态，并通过信任域掩码实现自适应恢复力，消除对 EMA 的依赖。该工作揭示了前向过程 RL 不稳定的几何根源，确立了无需调参的高效在线 RL 新范式，但在多目标奖励权重平衡上仍存疑。

## 研究背景

当扩散模型通过在线 RL 对齐人类偏好时，奖励信号仅在完整样本生成后获得，导致昂贵的输出级反馈难以有效分配至去噪轨迹的中间状态，这一现象称为信用分配问题。为解决此问题，前向过程 RL（如 DiffusionNFT）通过对生成样本进行前向加噪并回归速度，避免了似然计算，效率显著。然而，其正负分支隐含的“前向-反向一致性力”导致训练不稳定，迫使研究者引入 EMA 作为恢复力，但 EMA 的滞后系数需针对每个任务单独调优，限制了规模化应用。

在线 RL 对齐扩散模型的主流路线分为反向过程与前向过程两类。反向过程方法（如 Flow-GRPO）直接优化采样转移，但需将 ODE 转换为 SDE 以计算似然，且轨迹级优势难以精确分配至单步转移，效率受限。前向过程方法（如 DiffusionNFT）虽高效，但其稳定性依赖正负样本的相互抵消与 EMA 的恢复力。现有研究未能厘清前向过程 RL 崩溃的根本几何机制，导致调参成本高且泛化性差。本文通过诊断发现，前向过程 RL 的回归目标隐含了模型采样速度与理想前向速度之间的差异，这一差异产生的非奖励改进力是训练不稳定的根源，从而确立了无需调参的稳定性优化方向。

## 核心方法

### 前向过程 RL 的失效机制诊断

前向过程 RL 通常通过正负分支回归理想速度来优化策略。DiffusionNFT 构造正负目标 $v_{\theta,\pm} = v_{\text{old}} \pm \beta(v_\theta - v_{\text{old}})$，并最小化加权 MSE 损失。其理想引导方向由奖励与速度的协方差 $g$ 决定，正负分支理论上应指向同一改进方向。然而，实际反向采样场 $v_{\text{old}}^{\text{rvs}}$ 与由端点分布诱导的理想前向速度 $v_{\text{old}}^{\text{fwd}}$ 存在差异 $e = v_{\text{old}}^{\text{fwd}} - v_{\text{old}}^{\text{rvs}}$。

$$ F_{\text{NFT}}(s_t) = 2g + (2q - 1)e $$

该公式表明，NFT 的更新力包含奖励改进项 $2g$ 和一致性力 $(2q - 1)e$。正负分支仅在 $q=1/2$ 时完全抵消一致性力，但状态级奖励不平衡导致 $q$ 偏离 0.5，残留的一致性力干扰奖励优化。EMA 通过维持非零漂移 $d$ 提供恢复力 $\beta^2 \|d\|^2$，但其强度需逐任务调参。

### 聚合优先奖励倾斜

针对一致性力问题，DiffusionART 不再基于前向速度构建回归目标，而是将每个提示（prompt）的 $K$ 个端点样本与奖励聚合为共享的奖励改进方向 $G(c)$。该方向基于奖励与端点的协方差估计，并经过 RMS 归一化以消除奖励尺度差异。

$$ G(c) = \frac{\text{Cov}_{p_{\text{old}}}(R, x_0 | c)}{\text{RMS}(\text{Cov}_{p_{\text{old}}}(R, x_0 | c))} $$

该公式将轨迹级奖励信号转化为状态无关的共享引导向量。DiffusionART 将 $G(c)$ 直接应用于反向采样状态 $s_t$，构造目标 $v_{\text{tgt}}^{\text{ART}} = v_\theta^{(0)}(s_t) + G(c)$。由于目标不涉及前向速度 $v_{\text{old}}^{\text{fwd}}$，一致性力 $e$ 在构造上被消除，每个状态直接接收显式的奖励改进方向，避免了跨样本抵消导致的梯度稀释。

### 信任域掩码与自适应恢复

为替代需调参的 EMA，DiffusionART 采用双更新策略：将每个 rollout 批次分为两个不相交的小批次，分别执行 MSE 更新。第二次更新时，模型已产生漂移 $d(s_t) = v_\theta(s_t) - v_\theta^{(0)}(s_t)$，损失函数自动包含恢复项 $-d(s_t)$，其强度随状态漂移自适应增长。

$$ D_{\text{KL}}(q_\theta \| q_{\text{old}}) = \frac{\|\mu(s_t, v_\theta(s_t)) - \mu(s_t, v_\theta^{(0)}(s_t))\|^2}{2D\sigma_{\text{ref}}^2(t)} $$

为防止单次更新过度偏离，引入基于 ODE-to-SDE 转换的 KL 代理作为信任域掩码。该公式利用参考 SDE 步的均值差异量化策略漂移，当漂移超过阈值时屏蔽更新，从而在无需 EMA 调参的情况下实现稳定训练。

## 实验评估

实验在 HunyuanVideo-13B（视频）和 SD3.5-M（图像）上进行，对比 DiffusionNFT（前向 RL）和 Flow-GRPO-Fast（反向 RL）。基线覆盖了两类主流在线 RL 范式，但未包含 TreeGRPO 等树搜索方法。在 HunyuanVideo-13B 上，视觉质量（VQ）与运动质量（MQ）奖励权重设为 1:1。

| 方法 | 相对 GPU 小时数 | 相对平均训练奖励 |
| :--- | :--- | :--- |
| DiffusionNFT | 1.00× | 1.00× |
| Flow-GRPO-Fast | 1.00× | 1.00× |
| DiffusionART | 1/12.02× | 1.288× |
| DiffusionART | 1/11.72× | 1.530× |

DiffusionART 达到 DiffusionNFT 和 Flow-GRPO-Fast 的后期平均奖励水平，但 GPU 小时数分别减少 12.02 倍和 11.72 倍，且平均训练奖励分别高 28.8% 和 53.0%。在图像到视频生成任务中，DiffusionART 达到 MQ 6 所需 GPU 小时数比 Flow-GRPO-Fast 少 4.8 倍。

消融实验显示，NFT 中恢复力的输出力 RMS 比引导力小 9.4 倍，但聚合后的参数梯度范数大 4.9 倍，表明异质引导在状态间相互抵消，而恢复力主导更新并拖慢训练。DiffusionART 通过共享 $G(c)$ 减少抵消，使引导力保持主导。评估边界方面，实验未报告置信区间，且多目标奖励（VQ:MQ）的权重敏感性分析缺失，可能影响效率优势的普适性。

## 关联研究分析

从信用分配机制看，Flow-GRPO 通过 ODE-to-SDE 转换计算似然，将轨迹级优势分配至单步转移，但受限于似然计算开销与噪声注入的随机性。DiffusionART 摒弃似然计算，直接利用端点奖励协方差构造状态无关的共享方向 $G(c)$，将信用分配从“转移级”提升至“提示级”，避免了反向过程 RL 的似然瓶颈。然而，这种聚合是否丢失了状态级的细粒度偏好信息，论文未给出回答。

从稳定性机制看，DiffusionNFT 依赖 EMA 的滞后参考提供恢复力，但 EMA 系数需逐任务调优。DiffusionART 通过双更新与信任域掩码实现自适应恢复，消除了调参需求。与 TreeGRPO 相比，后者通过树结构复用前缀提升样本效率，而 DiffusionART 通过聚合减少梯度抵消提升效率，两者在样本效率优化路径上存在竞争，但 DiffusionART 未与 TreeGRPO 直接对比，无法判断在复杂约束任务上的相对优劣。

## 总结

本文针对在线 RL 中前向过程方法训练不稳定且需逐任务调参的矛盾，诊断出前向-反向速度场不一致产生的隐性一致性力是崩溃根源。通过聚合优先奖励倾斜消除一致性力，并引入信任域掩码实现自适应恢复，DiffusionART 在 HunyuanVideo-13B 上以 12.02 倍的计算效率提升达到 SOTA 奖励水平。该工作确立了无需调参的高效在线 RL 范式，但其实验仅验证了 VQ:MQ=1:1 的权重设置，当多目标奖励权重发生显著偏移时，聚合方向 $G(c)$ 的归一化是否仍能保持引导与恢复力的平衡，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.12572)