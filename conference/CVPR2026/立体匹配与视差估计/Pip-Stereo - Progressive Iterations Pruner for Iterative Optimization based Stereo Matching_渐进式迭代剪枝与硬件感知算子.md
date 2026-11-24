# CVPR2026最新论文 ｜Pip-Stereo: Progressive Iterations Pruner for Iterative Optimization based Stereo Matching ｜渐进式迭代剪枝与硬件感知算子

作者：Jintu Zheng、Qizhe Liu、HuangXin Xu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20496)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20496)

> 迭代优化立体匹配模型在边缘设备部署时面临严重的内存带宽瓶颈，传统实时方法通过移除循环结构换取速度，却牺牲了泛化能力。Pip-Stereo 指出迭代更新存在空间稀疏与时间冗余，通过渐进式迭代剪枝（PIP）将递归计算压缩至单次推理，并引入硬件感知的 FlashGRU 算子降低内存访问开销。该方法在保持 SOTA 精度的同时实现了边缘实时推理，但其对零初始化架构的适配性仍存疑。

## 研究背景

立体匹配的核心挑战在于病态区域（弱纹理、遮挡）的匹配歧义，而迭代优化范式通过 Gate Recurrent Unit (GRU) 在 2D 相关场上递归更新视差，已成为解决该问题的主流架构。然而，GRU 的递归特性导致静态计算图控制流复杂，阻碍算子融合，且对量化噪声敏感。更关键的是，高分辨率输入下，RNN 隐藏状态的全局内存读写引发巨大的数据移动开销，这一内存带宽瓶颈无法通过参数量或 FLOPs 等标量指标捕捉，成为边缘部署的主要障碍。

现有实时方法多通过移除 RNN 或简化代价体构建来规避迭代开销，如 LightStereo 和 HitNet。这些非迭代架构虽降低了延迟，但在跨域微调时表现出显著的精度下降与泛化能力不足。相比之下，迭代方法在同等延迟约束下展现出更强的鲁棒性，表明迭代细化不仅是后处理精修，更是学习过程中的核心归纳偏置。Pip-Stereo 的切入点在于：迭代更新并非均匀分布，而是高度稀疏且冗余的。通过量化 Middlebury 测试集上的更新标志命中率，发现 IGEV 在迭代 10 次后命中率超过 0.99，RAFT-Stereo 在 15 次后趋近 0.99，32 次迭代时更新像素占比不足 1%。这一发现揭示了迭代过程的“边际收益递减”特性，为在不牺牲精度的前提下压缩递归深度提供了理论依据。

## 核心方法

### 方法参照系

Pip-Stereo 基于 Selective-IGEV 架构，该架构采用正则化初始化策略，从粗视差引导迭代优化。与 MonSter 等依赖显式单目深度编码器不同，本文旨在消除 RNN 部署瓶颈，同时保留迭代优化的泛化优势，核心差异在于通过算法剪枝而非架构替换来加速推理。

### 单目深度先验迁移（MPT）

显式嵌入 Depth Anything V2 等基础模型作为独立编码器会引入巨大的计算负担，阻碍边缘部署。MPT 采用师生框架，将单目深度先验知识蒸馏至轻量级 RepViT 学生骨干。通过超网搜索确定各分辨率层的块配置，并利用均方误差损失对齐教师与学生的多尺度上下文特征及代价体嵌入。

$$ \mathcal{L}_{align} = \sum_{l} \| F_{teacher}^{(l)} - F_{student}^{(l)} \|^2 $$

该公式强制学生网络在特征层面复现教师的几何感知能力，从而在不增加推理时显式编码器开销的前提下，提升病态区域的匹配鲁棒性。

### 渐进式迭代剪枝（PIP）

直接截断迭代次数会导致精度急剧下降。PIP 采用两阶段学习策略，通过连续减半迭代次数并执行渐进式特征对齐，驱动递归计算图向单次迭代收敛。设 Mi-RNN 为原始迭代模型，Fi-RNN 为剪枝后模型，PIP 强制 Mi-RNN 在粗时间间隔上的累积输出与 Fi-RNN 的单步输出对齐。

$$ \mathcal{L}_{pip} = \sum_{s=1}^{T/r} \| \sum_{k=0}^{r-1} \Psi(\mathbf{z}_{Mi, sr+k}) - \Psi(\mathbf{z}_{Fi, s}) \|^2 + \lambda \| \mathbf{d}_{final} - \mathbf{d}_{gt} \|^2 $$

此损失函数确保剪枝后的模型不仅匹配瞬时预测，还保留原始迭代过程的演化趋势，有效抑制因迭代减少导致的精度损失。

### FlashGRU 硬件感知算子

对于无法完全压缩至单次迭代的架构（如零初始化的 RAFT-Stereo），FlashGRU 提供加速方案。该算子利用结构化稀疏性和 I/O 感知设计，将 GRU 中的顺序卷积实现为时间融合内核，并通过静态多级双向索引映射表将稀疏像素打包至连续 GPU 缓冲区，减少内存碎片。

$$ \text{Speedup} = \frac{\text{Latency}_{native}}{\text{Latency}_{flash}} \propto \frac{1}{\text{Memory Access Ratio}} $$

FlashGRU 通过降低全局内存请求次数，在高分辨率下实现显著加速，弥补了 PIP 在零初始化架构上的精度损失。

## 实验评估

实验在 SceneFlow、KITTI 2015/2012、ETH3D 及 DrivingStereo 上进行，基线涵盖 MonSter、IGEV、RAFT-Stereo 等迭代 SOTA 及 LightStereo、HitNet 等实时方法。Pip-Stereo 在 KITTI 2015 上取得 0.35 EPE，优于 MonSter 的 0.44 EPE；在 ETH3D 上取得 0.52 EPE，优于 MonSter 的 0.70 EPE。在 DrivingStereo 零样本泛化测试中，Pip-Stereo 的 Avg EPE 为 4.35，略低于 RT-MonSter++ 的 4.18，但显著优于 FoundaStereo 的 4.93。

| 数据集 | 方法 | EPE (px) | 备注 |
| :--- | :--- | :--- | :--- |
| KITTI 2015 | Pip-Stereo | 0.35 | 最佳 |
| KITTI 2015 | MonSter | 0.44 | 迭代基线 |
| ETH3D | Pip-Stereo | 0.52 | 最佳 |
| ETH3D | MonSter | 0.70 | 迭代基线 |
| DrivingStereo | Pip-Stereo | 4.35 | Avg EPE |
| DrivingStereo | RT-MonSter++ | 4.18 | 实时基线 |

消融实验显示，MPT 带来 13.6% 的 EPE 降低，PIP 将 32 次迭代压缩至 1 次时，EPE 增加从 0.18 降至 0.07。FlashGRU 在 2K 分辨率下实现 7.28 倍加速，峰值内存降低 76.6%，全局内存访问减少 80.9%。值得注意的是，PIP 在零初始化的 RAFT-Stereo 上效果有限，EPE 仍高于 2，需结合 FlashGRU 保留少量迭代才能缓解精度下降。

评估边界方面，论文未报告置信区间，且部分基线结果引用自其他文献。代码已开源，但 FlashGRU 的 NPU 适配细节未完全披露。

## 关联研究分析

从问题动机看，Pip-Stereo 与 MonSter 均利用单目深度先验解决病态区域歧义，但 MonSter 将深度编码器作为独立模块嵌入推理流程，导致边缘设备延迟高达 7.6 秒/帧。Pip-Stereo 通过 MPT 将先验知识内化至轻量骨干，消除了显式编码器的计算开销。这一差异源于对部署约束的不同理解：MonSter 侧重精度上限，Pip-Stereo 侧重硬件兼容性。Pip-Stereo 的蒸馏策略是否在所有域变化下都能保持 MonSter 的泛化能力，论文未给出全面对比。

从方法设计看，Pip-Stereo 与 LightStereo 等实时方法均追求低延迟，但 LightStereo 通过移除 RNN 实现加速，而 Pip-Stereo 保留 RNN 结构并通过剪枝压缩。LightStereo 在跨域微调时泛化能力较弱，而 Pip-Stereo 在 DrivingStereo 上表现出更强的鲁棒性。这表明迭代细化作为归纳偏置的价值不可被简单架构替换所取代。然而，Pip-Stereo 对零初始化架构的依赖 FlashGRU 加速，暗示其 PIP 算法在缺乏正则化初始化的场景下存在局限性，这一盲区限制了其在更广泛迭代架构中的通用性。

## 总结

Pip-Stereo 针对迭代立体匹配在边缘部署中的内存带宽瓶颈，利用迭代更新的稀疏性与冗余性，通过渐进式迭代剪枝将递归计算压缩至单次推理，并辅以硬件感知的 FlashGRU 算子。该方法在 KITTI 2015 上实现 0.35 EPE，在 2K 分辨率下获得 7.28 倍加速，证明了精度与速度可兼得。然而，实验显示 PIP 在零初始化架构（如 RAFT-Stereo）上精度损失显著，需依赖 FlashGRU 保留少量迭代，暴露了算法对正则化初始化的依赖。当面对无粗视差引导的纯零初始化场景时，PIP 能否在不牺牲过多精度的前提下进一步压缩迭代次数，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20496)