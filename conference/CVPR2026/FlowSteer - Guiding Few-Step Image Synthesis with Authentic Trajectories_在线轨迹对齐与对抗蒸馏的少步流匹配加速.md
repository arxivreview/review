# CVPR2026最新论文 ｜FlowSteer: Guiding Few-Step Image Synthesis with Authentic Trajectories ｜在线轨迹对齐与对抗蒸馏的少步流匹配加速

研究机构：清华大学、香港科技大学

作者：Lei Ke、Hubery Yin、Gongye Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18834)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18834)

> 流匹配模型在少步推理中因轨迹弯曲导致数值误差累积，现有分段整流流方法虽理论一致但实际性能受限。本文指出分段整流流存在训练-推理分布不匹配的根本缺陷，即教师模型在离线插值起点上训练导致轨迹偏离，学生模型在阶段边界处遭遇分布断裂。通过在线轨迹对齐（Online Trajectory Alignment, OTA）强制教师沿真实轨迹生成训练数据，并结合轨迹级对抗蒸馏，FlowSteer 在 4 步推理下显著提升了生成质量。该方法有效修复了调度器缺陷并提升了少步生成保真度，但其训练开销与多样性保持能力仍存疑。

## 研究背景

流匹配（Flow Matching, FM）通过回归确定性常微分方程（ODE）的速度场实现从噪声到数据的传输，其核心优势在于训练无需模拟随机轨迹。然而，由于噪声-数据对的非结构化耦合，学习到的速度场轨迹通常呈弯曲状，导致大步长数值积分时误差显著。为压缩推理步数，整流流（Rectified Flow, RF）通过迭代重参数化直线化轨迹，而分段整流流（Piecewise Rectified Flow, PeRFlow）进一步将全轨迹划分为多个短阶段，分别进行局部直线化，旨在以分治策略提升少步生成的可行性。

尽管 PeRFlow 在理论上与流匹配一致，但其在实际应用中性能不及一致性蒸馏（Consistency Distillation, CD）与分布匹配蒸馏（Distribution Matching Distillation, DMD）方法，导致该路线被社区忽视。主流加速方案如 PCM 和 Hyper-SD 依赖一致性损失或分数匹配，虽能实现少步生成，但往往需要额外的分类器自由引导（Classifier-Free Guidance, CFG）前向传播，增加了推理延迟。本文切入点在于诊断 PeRFlow 性能落后的根本原因：其训练协议中使用的静态线性插值起点与推理时的动态状态分布存在本质差异，导致教师模型提供次优指导，学生模型误差累积。

## 核心方法

### 分段整流流参照系

PeRFlow 的标准流程将时间区间 $[1, 0]$ 划分为 $K$ 个阶段，每个阶段 $[t_k, t_{k-1}]$ 内，训练对 $(z_{t_k}, z_{t_{k-1}})$ 的起点 $z_{t_k}$ 由真实图像 $z_0$ 与噪声 $\epsilon$ 线性插值得到，终点 $z_{t_{k-1}}$ 由教师 ODE 求解器演化获得。学生模型学习匹配该阶段内的恒定速度 $v^* = (z_{t_{k-1}} - z_{t_k}) / (t_{k-1} - t_k)$。该流程的关键差异在于，训练时的起点 $z_{t_k}$ 是静态构造的，而推理时起点是前一阶段的输出，两者分布不一致。

### 在线轨迹对齐（OTA）

PeRFlow 的静态插值起点导致教师轨迹偏离其真实推理路径，即“教师轨迹不匹配”，同时造成阶段间分布断裂，即“阶段间分布不匹配”。OTA 通过在线求解教师 ODE 生成起点，确保训练分布与推理分布一致。具体而言，对于阶段 $k$，起点 $z_{t_k}$ 不再由插值获得，而是通过求解教师速度场 $v_T$ 从初始噪声 $\epsilon$ 演化至 $t_k$ 得到：

$$ z_{t_k} = \text{ODESolve}(v_T, \epsilon, 1, t_k) $$

随后，终点 $z_{t_{k-1}}$ 由 $z_{t_k}$ 演化至 $t_{k-1}$，目标速度仍为 $v^* = (z_{t_{k-1}} - z_{t_k}) / (t_{k-1} - t_k)$。这一设计消除了教师轨迹偏离，使学生从教师的真实动力学中学习，同时闭合了阶段间分布差异，避免了误差累积。

### 轨迹级对抗蒸馏

在 OTA 基础上，FlowSteer 引入对抗蒸馏以进一步提升少步生成的感知质量。传统对抗蒸馏作用于最终图像，而本文将其应用于 ODE 轨迹空间。判别器 $D$ 基于预训练扩散模型骨干，学生模型 $v_S$ 生成 4 步轨迹，判别器区分教师轨迹状态 $z_t^{[T]}$ 与学生轨迹状态 $z_t^{[S]}$。学生目标函数包含蒸馏损失、对抗损失及特征匹配损失：

$$ \mathcal{L} = \mathcal{L}_{\text{distill}} + \lambda_{\text{adv}} \mathcal{L}_{\text{adv}} + \lambda_{\text{fm}} \mathcal{L}_{\text{fm}} $$

其中，$\mathcal{L}_{\text{adv}}$ 最大化判别器对学生状态的真实度预测，$\mathcal{L}_{\text{fm}}$ 最小化判别器中间层特征的学生-教师 L2 距离。该设计促使学生不仅匹配终点，更忠实模仿教师的中间轨迹，从而在少步条件下保持高保真度。

## 实验评估

实验基于 Stable Diffusion 3 Medium (SD3-M) 和 SD3.5 Large 骨干，使用 FluxReason-6M 提示集进行 LoRA 微调，评估指标为 PickScore、HPSv2 和 CLIP Score。基线覆盖 CD（PCM, Hyper-SD）、DMD（Flash Diffusion）及 RF（PeRFlow），但缺失 SoFlow、MeanFlow 等最新单步生成 SOTA 方法，限制了横向对比的全面性。

| 方法 | NFE | PickScore | HPSv2 | CLIP Score |
| :--- | :--- | :--- | :--- | :--- |
| SD3-Medium (Pre-trained) | 20×2 | 22.41 | 28.02 | 32.78 |
| PCM (Shift=1) | 4×2 | 22.12 | 27.81 | 32.32 |
| Flash Diffusion | 4×1 | 22.28 | 28.04 | 32.31 |
| PeRFlow | 4×1 | 22.19 | 26.36 | 32.55 |
| **Ours** | **4×1** | **22.39** | **28.60** | **32.81** |

在 SD3-M 4 步推理下，FlowSteer 的 PickScore 22.39 和 HPSv2 28.60 均优于 PeRFlow 的 22.19 和 26.36，且超越 Flash Diffusion 的 22.28 和 28.04。消融实验显示，调度器修复贡献最大，PickScore 从基线 22.19 提升至 22.50；OTA 和对抗蒸馏分别带来 0.04 和 0.01 的 PickScore 增益，但 HPSv2 增益分别为 0.43 和 1.37，表明对抗蒸馏对感知质量提升更显著。

| 配置 | PickScore | HPSv2 |
| :--- | :--- | :--- |
| Baseline | 22.19 | 26.36 |
| Baseline + OTA | 22.23 | 26.79 |
| Baseline + Adv. Distillation | 22.18 | 27.73 |
| Baseline + Scheduler | 22.50 | 27.75 |
| **Ours (Full)** | **22.39** | **28.60** |

评估边界方面，论文未报告 FID 指标，仅使用偏好类指标，难以与 ImageNet 类条件生成 SOTA 直接对比。代码未公开，LoRA 超参数与 GPU 配置未详述，可复现性受限。调度器修复虽简单，但仅验证于 SD3 系列，对其他架构的普适性未验证。

## 关联研究分析

从问题动机看，FlowSteer 与一致性蒸馏（CD）路线存在根本差异。CD 方法如 PCM 强制学生映射任意轨迹点到同一终点，依赖点级一致性，而 FlowSteer 通过 OTA 确保学生沿教师真实轨迹学习，强调轨迹级一致性。CD 的瓶颈在于静态一致性损失无法捕捉轨迹动态，导致少步生成时细节丢失；FlowSteer 的 OTA 通过在线 ODE 求解解决此问题，但引入了额外训练开销。CD 在 4 步下需双前向传播（CFG），而 FlowSteer 单前向传播，推理效率更高，但训练成本更高。

从方法设计看，FlowSteer 与分布匹配蒸馏（DMD）如 Flash Diffusion 形成对比。DMD 通过分数函数匹配学生输出分布与真实分布，不依赖教师轨迹，而 FlowSteer 依赖教师轨迹作为指导。DMD 的优势在于无需教师 ODE 求解，训练更稳定；FlowSteer 的优势在于轨迹级反馈更精细，感知质量更高。Flash Diffusion 在 1 步 NFE 下表现优异，但 FlowSteer 在 4 步下超越其 1 步版本，表明轨迹对齐在少步（非单步）场景下更具优势。DMD 未解决轨迹弯曲问题，而 FlowSteer 通过 OTA 隐含优化了轨迹几何，但两者在多样性保持上的权衡未充分探讨。

## 总结

FlowSteer 旨在解决分段整流流在少步生成中因训练-推理分布不匹配导致的性能瓶颈。其切入点在于识别静态插值起点与动态推理状态的分布差异，并通过在线轨迹对齐（OTA）强制教师沿真实轨迹生成训练数据，结合轨迹级对抗蒸馏提升感知质量。实验证明，在 SD3-M 4 步推理下，FlowSteer 的 PickScore 22.39 和 HPSv2 28.60 显著优于 PeRFlow 和 Flash Diffusion。然而，论文未报告 FID 指标，且 OTA 的在线 ODE 求解增加了训练开销，其推理加速收益是否被训练成本抵消，以及该方法在多样性保持上的表现，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18834)