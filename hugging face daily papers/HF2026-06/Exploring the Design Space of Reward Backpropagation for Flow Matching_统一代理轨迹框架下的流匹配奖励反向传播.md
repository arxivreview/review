# HuggingFace最新推荐论文 ｜Exploring the Design Space of Reward Backpropagation for Flow Matching ｜统一代理轨迹框架下的流匹配奖励反向传播

研究机构：西湖大学、澳大利亚悉尼大学

作者：Ruoyu Wang、Boye Niu、Xiangxin Zhou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.11075)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.11075)

> 预训练流匹配模型虽能生成高质量图像，但缺乏与人类偏好对齐的能力。现有直接奖励反向传播方法受限于全轨迹激活存储的内存瓶颈与跨步雅可比链导致的梯度爆炸，而策略梯度法虽规避了此问题却引入了高方差。本文提出 FlowBP，将反向传播轨迹本身作为设计对象，通过构建轻量级代理轨迹解耦采样与优化过程。该框架统一了 ReFL、DRaFT-LV 等既有方法，并衍生出三种变体，在多个骨干模型上实现了偏好对齐与组合生成能力的同步提升，但其对连接器残差的依赖仍限制了其在长区间跳跃下的稳定性。

## 研究背景

整流流（Rectified Flow, RF）通过回归确定性常微分方程（ODE）的速度场，将生成过程建模为从噪声到数据的直线传输。这种确定性轨迹具备端到端可微性，理论上允许直接对奖励函数求导以更新模型参数，从而避免策略梯度方法（如 GRPO）中随机采样带来的高方差。然而，直接对 $N$ 步 ODE 积分轨迹进行反向传播时，需存储所有中间激活值，这在现代大模型规模下内存不可行；同时，跨步雅可比乘积会导致奖励梯度在回传至早期时间步时发生指数级放大，引发训练不稳定。

直接奖励反向传播路线旨在利用 ODE 的可微性实现样本高效对齐，但面临上述两大病理。ReFL 仅保留单步可微并评估后验均值，DRaFT-LV 固定末步并平均噪声梯度，DRTune 采用稀疏时间步并切断中间梯度，LeapAlign 则引入直通连接器以双段跳跃替代全轨迹。这些方法各自解决了部分问题，但设计孤立，未形成统一视角，导致在长区间跳跃时连接器残差大、梯度质量不稳定。FlowBP 的切入点在于将反向轨迹视为设计对象，通过代理轨迹构建，将内存占用从 $O(N)$ 降至 $O(K)$（$K$ 为活跃集大小），并将梯度放大限制在单步雅可比因子内，从而系统性地探索了奖励输入、活跃集、积分权重与桥接耦合四个设计轴。

## 核心方法

### 方法参照系

直接奖励反向传播的标准流程是对完整 ODE 积分轨迹进行反向模式自动微分。本文的关键差异在于不直接反传全轨迹，而是构建一个“代理轨迹”（Surrogate Trajectory）：前向使用缓存的无梯度 rollout 状态，反向仅对稀疏的活跃速度场重前向计算梯度，其余状态视为常数。

### 代理轨迹构建与统一梯度

设计动机：解决全轨迹反传的内存爆炸与梯度链式放大问题。FlowBP 首先执行无梯度的 Euler 积分，缓存状态 $\{x_i\}$ 与速度 $\{v_i\}$。随后构建代理轨迹，仅对活跃集 $A$ 中的速度进行重前向，其余速度使用缓存值。代理轨迹的端点通过 Euler 重构或连接器固定。统一梯度公式为：

$$ \nabla_\theta r(x_0) = \sum_{i \in A} w_i \frac{\partial v_\theta(x_i)}{\partial \theta} + \alpha \frac{\partial v_\theta(x_j)}{\partial \theta} \frac{\partial x_j}{\partial x_k} $$

其中第一项为直接项，第二项为嵌套项，$\alpha$ 控制桥接耦合强度。该公式表明，梯度仅由活跃集大小 $K=|A|$ 决定，内存与计算复杂度与 rollout 长度 $N$ 解耦，且嵌套项深度仅为 1，避免了多步雅可比乘积。

### 三种变体：稀疏重构、桥接耦合与高阶求积

设计动机：探索设计空间中未被覆盖的配置，以平衡梯度稳定性与信号传播。FlowBP-Sparse 采用稀疏 Euler 重构，$j=0$，无桥接，梯度完全解耦，确保奖励输入为真实样本 $x_0$ 而非后验均值。FlowBP-Bridge 引入桥接耦合，将活跃集分为前后两段，通过 $\alpha$ 控制跨段梯度传递，实现受控的信用分配。FlowBP-Lagrange 保留 LeapAlign 的双段连接器拓扑，但将单速度跳跃替换为高阶 Lagrange 求积规则，通过增加支持点与积分精度降低连接器残差 $d_0 = \|x_0 - \hat{x}_0\|_2$，从而缓解因残差尖峰导致的奖励崩塌。

## 实验评估

实验在 SD3.5-M、FLUX.1-dev 和 FLUX.2-Klein-base 三个骨干模型上进行，使用 HPSv2.1、PickScore、ImageReward、UR-Align 和 UR-IQ 评估偏好与质量，GenEval 评估组合生成。基线覆盖 ReFL、DRaFT-LV、DRTune 和 LeapAlign，但未对比基于 DPO 的偏好优化方法，这可能限制了与主流对齐范式的横向比较。

| Method | HPSv2.1 (FLUX.1-dev) | PickScore (FLUX.1-dev) | GenEval Overall (FLUX.1-dev) |
| :--- | :--- | :--- | :--- |
| LeapAlign | 0.4063 | 23.6704 | 67.44 |
| FlowBP-Sparse | 0.4081 | 23.7458 | 68.19 |
| FlowBP-Bridge | 0.4119 | 23.7952 | 68.75 |
| FlowBP-Lagrange | 0.4134 | 23.7796 | 69.88 |

FlowBP-Lagrange 在 FLUX.1-dev 上取得最高 HPSv2.1 分数 0.4134 和 GenEval 总分 69.88，优于 LeapAlign 的 0.4063 和 67.44。在 SD3.5-M 上，FlowBP-Lagrange 在 HPSv2.1、PickScore、ImageReward 和 UR-Align 上领先，而 FlowBP-Sparse 在 UR-IQ 上最优，表明不同变体捕捉了奖励景观的不同方面。

消融实验显示，端点重构（Endpoint Reconstruction）对 ReFL 和 DRTune 均有显著提升，例如 ReFL 的 HPSv2.1 从 0.3930 提升至 0.3993，证明奖励输入应为真实样本而非后验均值。FlowBP-Lagrange 的 Lagrange 求积阶数与梯度支持尺度需平衡：阶数过高或支持尺度过大均会导致训练不稳定，而中等支持尺度下连接器残差 $d_0$ 显著低于 Euler 和 Uniform 连接器，直接解释了其更高的奖励稳定性。FlowBP-Bridge 的嵌套梯度尺度 $\alpha$ 在中间值（如 0.5）时奖励峰值最高，过强耦合会重新引入雅可比放大。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码未公开，但提供了详细的超参数（如学习率 $1 \times 10^{-5}$，batch size 64）。GenEval 评估仅针对 FLUX.1-dev，其他骨干模型的组合生成能力未充分验证。

## 关联研究分析

从问题动机看，FlowBP 与 LeapAlign 同属直接奖励反向传播路线，但 LeapAlign 依赖单速度跳跃的连接器，在长区间跳跃时残差大，导致梯度质量不稳定；FlowBP-Lagrange 通过高阶求积降低残差，解决了这一具体失效。然而，FlowBP 未对比 DPO 等基于偏好对的方法，而 DPO 在大规模对齐中已被广泛验证，FlowBP 在样本效率上的优势是否足以抵消其缺乏偏好对数据的局限性，论文未给出回答。

从方法设计看，FlowBP 与 DRTune 均使用稀疏活跃集，但 DRTune 切断中间梯度，奖励输入为后验均值，存在分布偏移；FlowBP-Sparse 通过 Euler 重构确保奖励输入为真实样本，消除了这一偏差。此外，FlowBP 的桥接耦合轴允许跨段梯度传递，而 DRTune 和 ReFL 完全解耦，FlowBP-Bridge 在受控耦合下实现了更好的信用分配，但 $\alpha$ 的最优值依赖具体任务，缺乏理论最优解，仅靠经验调参。

## 总结

FlowBP 旨在解决直接奖励反向传播中的内存爆炸与梯度放大矛盾，通过代理轨迹框架将反向传播限制在稀疏活跃集内，实现了内存与梯度的双重约束。该框架统一了既有方法，并衍生出三种变体，在 FLUX.1-dev 上取得 0.4134 的 HPSv2.1 分数和 69.88 的 GenEval 总分，优于 LeapAlign。其边界在于连接器残差对长区间跳跃的敏感性，以及 $\alpha$ 参数的经验依赖性。当 rollout 步数 $N$ 进一步增加时，高阶 Lagrange 求积的计算开销是否成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.11075)