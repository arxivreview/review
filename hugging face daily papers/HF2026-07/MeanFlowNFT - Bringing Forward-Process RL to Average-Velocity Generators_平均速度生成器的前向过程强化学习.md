# HuggingFace最新推荐论文 ｜MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators ｜平均速度生成器的前向过程强化学习

研究机构：香港科技大学、Hugging Face

作者：Yushi Huang、Xiangxin Zhou、Jun Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.15273)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.15273)

> 现有扩散与流模型依赖多步瞬时速度积分，导致推理延迟高企，而主流强化学习（RL）对齐方法均基于瞬时速度场优化，无法直接适配以区间平均速度为参数的 MeanFlow 生成器。本文通过 MeanFlow 恒等式构造诱导瞬时速度预测器，将 DiffusionNFT 的前向过程 RL 目标迁移至平均速度网络，在保持少步采样效率的同时实现偏好对齐。该方法在图像与视频生成中均显著超越多步 RL 基线，但其理论保证仅在理想化设定下成立，实际有限差分近似引入的偏差尚未被量化。

## 研究背景

流匹配（Flow Matching, FM）通过回归确定性常微分方程（ODE）的速度场实现从噪声到数据的传输，其训练目标为最小化预测速度与条件速度之间的均方误差。在整流流（Rectified Flow）设定下，条件速度 $v_t = \epsilon - x_0$ 为线性插值，最优预测器为后验均值。然而，标准 FM 采样需沿 ODE 轨迹进行数百次网络评估，推理效率受限。MeanFlow 通过预测时间区间 $[s, t]$ 上的平均速度 $u$ 替代瞬时速度 $v$，利用位移恒等式 $x_s = x_t - (t-s)u$ 实现单步或少步跳跃采样，从根本上解耦了采样步数与网络评估次数。

当前 RL 对齐的主流路线存在两条技术路径：一是基于反向过程离散化的策略梯度方法（如 GRPO），需估计每步似然并展开去噪轨迹，计算开销大且依赖随机性；二是前向过程 RL（如 DiffusionNFT），直接在加噪过程上对比正负样本构建隐式策略改进方向，无需似然估计且求解器无关。然而，DiffusionNFT 的目标函数显式作用于瞬时速度预测器 $v_\theta$，而 MeanFlow 网络输出的是平均速度 $u_\theta$，二者参数化空间不匹配。这一不匹配导致现有前向过程 RL 方法无法直接微调 MeanFlow 模型，使得高效少步生成器缺乏有效的偏好对齐机制，成为部署场景中的关键瓶颈。

## 核心方法

### 前向过程 RL 参照系

DiffusionNFT 在瞬时速度空间定义 RL 目标：冻结参考策略 $v_{old}$，通过奖励 $r$ 划分正负后验，构建隐式正负预测器 $v_{\theta \pm}$，并优化奖励加权的流匹配损失。该框架的核心假设是网络输出为瞬时速度，且最优解 $v_{\theta^*} = v_{old} + \frac{\beta}{2}\Delta$ 对应改进策略的边际速度。本文问题与该通用流程的关键差异在于：MeanFlow 网络输出为区间平均速度 $u_\theta$，无法直接代入上述目标函数，需建立平均速度与瞬时速度之间的可优化桥梁。

### 诱导瞬时速度预测器构造

MeanFlow 恒等式揭示了平均速度与瞬时速度的微分联系：对位移形式 $(t-s)u = \int_s^t v d\tau$ 关于 $t$ 求导，得 $\frac{d}{dt}u = \partial_t u + (\partial_x u)v$。本文利用该恒等式，从平均速度网络 $u_\theta$ 构造诱导瞬时速度预测器 $V_\theta(x_t, s, t) = u_\theta(x_t, s, t) + (t-s)\left(\partial_t u_\theta + (\partial_x u_\theta)\dot{v}_\theta\right)$，其中 $\dot{v}_\theta = u_\theta(x_t, t, t)$ 为网络在 $s=t$ 时的瞬时速度输出。该构造的设计动机在于：直接优化 $u_\theta$ 会破坏 MeanFlow 的少步采样结构，而优化 $V_\theta$ 可在瞬时速度空间执行 RL 目标，同时通过恒等式将梯度传递至 $u_\theta$，保持采样器不变。在理想化设定下，$V_\theta$ 对所有 $s \le t$ 退化为 $v_\theta$，确保优化目标与 DiffusionNFT 一致。

### 有限差分近似与策略改进传递

实际计算中，总导数项 $\frac{d}{dt}u_\theta$ 涉及 Jacobian-Vector Product（JVP），前向模式自动微分在 Fully Sharded Data Parallel（FSDP）训练中开销过大且兼容性差。本文采用中心有限差分近似：$\frac{d}{dt}u_\theta \approx \frac{u_\theta(x_{t+\Delta t}, s, t+\Delta t) - u_\theta(x_{t-\Delta t}, s, t-\Delta t)}{2\Delta t}$，其中 $x_{t \pm \Delta t} = x_t \pm \Delta t v_t$ 沿条件速度方向位移。该近似的设计动机在于降低计算成本并提升训练稳定性，且可训练与参考预测器共享同一有限差分估计，避免梯度不一致。理论证明表明，当诱导最优解 $V_{\theta^*}(x_t, s, t) = v_+(x_t, t)$ 对所有区间成立时，$u_{\theta^*}$ 满足 MeanFlow 一致性条件，即为改进策略 $v_+$ 诱导 ODE 的精确平均速度，从而策略改进从瞬时速度空间传递至平均速度网络。

## 实验评估

实验在 Stable Diffusion 3.5-Medium（SD3.5-M，512×512 训练/1024×1024 评估）与 Wan2.1 1.3B（480p，81 帧）上进行，MeanFlow 权重由 AnyFlow 蒸馏获得，全程无分类器自由引导（CFG-free）。基线覆盖少步蒸馏（DMD、CDM、AnyFlow）与少步 RL（RTDMD、R_dm），但缺失 GRPO 类方法在同等少步条件下的直接对比，仅对比了 40-50 步的多步 RL 基线。

| 方法 | 步数 | ImageReward↑ | CLIPScore↑ | PickScore↑ | HPSv2↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SD3.5-M + DiffusionNFT | 40 | 1.4066 | 0.2889 | 23.6440 | 0.3236 |
| AnyFlow | 4 | 1.1125 | 0.2886 | 22.4789 | 0.2969 |
| RTDMD | 4 | 1.2315 | 0.2775 | 23.2825 | 0.3265 |
| MeanFlowNFT | 4 | 1.4504 | 0.2967 | 23.5019 | 0.3269 |

MeanFlowNFT 在 4 步内于 8 项指标中的 6 项取得最优，ImageReward 1.4504 与 CLIPScore 0.2967 均超越 40 步 DiffusionNFT（1.4066/0.2889），验证了前向过程 RL 在少步场景下的效率优势。视频生成中，4 步 MeanFlowNFT 的 VBench 总分 84.33 优于 50 步 LongCat-Video RL 的 82.57，HPSv3-G 0.7930 与 MQ 0.9535 亦领先，表明该方法在时序任务中同样有效。

消融实验未单独报告，但有限差分近似与共享总导数设计是核心决策。论文指出，若仅优化 $s=t$ 的瞬时速度 $v_\theta$，将退化为标准流匹配，丧失 MeanFlow 的少步采样能力；而有限差分近似虽降低 JVP 计算成本，但其引入的截断误差对最终生成质量的影响未量化，尤其在低噪声区域可能放大数值不稳定。

评估协议存在局限：图像生成未报告 FID 或 IS 等传统质量指标，仅依赖奖励分数，可能掩盖生成多样性或保真度的退化；视频生成使用 VBench 与 VideoAlign 指标，但 256 个提示集的规模较小，统计显著性未检验。代码与超参数已开源，但有限差分步长 $\Delta t$ 的选择对性能的影响未提供敏感性分析，可复现性依赖特定实现细节。

## 关联研究分析

从问题动机看，本文与 Flow-GRPO 形成路线对立。Flow-GRPO 基于反向过程离散化，需展开去噪轨迹并估计每步似然，其信用分配依赖随机探索，在确定性 ODE 中易陷入局部最优；本文采用前向过程 RL，直接在加噪过程上优化，无需似然估计且求解器无关，但牺牲了反向过程的显式探索机制。这一差异的根源在于任务特性：MeanFlow 的少步采样要求推理效率优先，而 GRPO 的多步设定允许更充分的探索。本文未讨论前向过程 RL 在缺乏随机性时如何避免模式坍塌，这是否构成少步生成中多样性的根本限制，论文未给出回答。

从方法设计看，本文与 DiffusionNFT 共享隐式正负预测器框架，但关键差异在于速度空间的转换。DiffusionNFT 直接优化瞬时速度 $v_\theta$，其理论保证基于后验均值的线性分解；本文通过 MeanFlow 恒等式构造 $V_\theta$，将优化目标从瞬时速度空间映射至平均速度空间，这一转换引入了总导数项的近似误差。该设计解决了 MeanFlow 参数化与 RL 目标的不匹配问题，但有限差分近似是否在所有时间步上保持精度，尤其在 $s$ 远离 $t$ 的长区间上，论文未提供误差界分析。

## 总结

本文解决的核心矛盾是 MeanFlow 少步采样效率与 RL 偏好对齐之间的参数化不匹配。现有前向过程 RL 方法均基于瞬时速度场，无法直接适配平均速度网络，而本文通过 MeanFlow 恒等式构造诱导瞬时速度预测器，将 DiffusionNFT 目标迁移至平均速度空间，在保持少步采样器不变的前提下实现策略改进。实验表明，4 步 MeanFlowNFT 在 SD3.5-M 上 ImageReward 达 1.4504，超越 40 步 DiffusionNFT 的 1.4066；在 Wan2.1 上 VBench 84.33 优于 50 步 LongCat-Video RL 的 82.57。本文的边界在于理论保证仅在理想化设定下成立，有限差分近似引入的截断误差未量化，且评估协议未包含传统质量指标，可能掩盖多样性退化。当有限差分步长 $\Delta t$ 在低噪声区域增大时，诱导预测器 $V_\theta$ 与真实瞬时速度的偏差是否导致策略改进失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.15273)