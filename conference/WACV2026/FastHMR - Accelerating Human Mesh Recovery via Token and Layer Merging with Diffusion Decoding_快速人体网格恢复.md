# WACV2026最新论文 ｜FastHMR: Accelerating Human Mesh Recovery via Token and Layer Merging with Diffusion Decoding ｜快速人体网格恢复

研究机构：加拿大多伦多大学、加拿大向量研究所

作者：Soroush Mehraban、Andrea Iaboni、Babak Taati

论文原文见 [arXiv](https://arxiv.org/abs/2510.10868)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10868)

> 3D人体网格恢复（Human Mesh Recovery, HMR）旨在从单目图像重建人体姿态与形状，但基于Transformer的SOTA模型因自注意力机制的二次复杂度，难以在VR/AR等实时场景中部署。现有轻量化方法多依赖硬件定制或牺牲精度，缺乏通用且保精度的加速方案。本文通过层合并、掩码引导的Token合并与单步扩散解码器，在保持精度的同时实现2.3倍加速。该框架验证了“压缩-恢复”策略的有效性，但其对分割掩码的依赖与背景线索丢失问题，限制了在复杂场景下的鲁棒性。

## 研究背景

Transformer骨干网络通过全局自注意力机制显著提升了HMR的单帧精度，成为当前主流架构。然而，自注意力的计算量随序列长度呈二次方增长，导致显存占用与推理延迟激增，阻碍了其在资源受限设备上的应用。这种计算瓶颈源于模型内部存在的两类冗余：层间冗余与空间冗余。层间冗余表现为相邻Transformer层学习高度相关的特征表示，执行全部层造成计算浪费；空间冗余则源于大量Token对应背景区域，对最终姿态与形状估计贡献甚微。

HMR领域长期面临实时性与精度的权衡困境。确定性回归方法（如HMR2.0）虽推理速度快，但缺乏时序建模，导致视频序列中帧间抖动严重；概率生成方法（如ScoreHMR）通过多步去噪建模不确定性，但需多次采样，推理速度降至2.2–25.9 fps，远低于实时阈值。现有高效HMR方法如POTTER虽达83.3 fps，但精度落后于SOTA；VITA等硬件协同设计则依赖专用芯片，通用性差。FastHMR的切入点在于：不改变骨干网络架构，而是通过事后（post-hoc）合并层与Token降低计算量，并引入轻量级扩散解码器恢复精度与平滑性，从而在标准GPU上实现高效部署。

## 核心方法

### 方法参照系

标准Transformer HMR流程为：图像Token化→多层自注意力编码→线性解码器输出SMPL参数。本文问题与该通用流程的关键差异在于：需在保持精度前提下大幅降低计算量，且需解决逐帧独立估计导致的时序抖动。

### 误差约束层合并（ECLM）

层间冗余的消除通常依赖剪枝或蒸馏，但本文采用基于误差阈值的合并策略。ECLM从最后一层向前迭代，合并连续层直至MPJPE增量超过阈值$\tau$。合并操作遵循SLM方法，将层$L_i, \dots, L_j$的参数$\theta_i, \dots, \theta_j$合并为：

$$\theta_{merged} = \frac{1}{j-i+1} \sum_{k=i}^{j} \theta_k$$

该公式的物理含义是：若相邻层输出差异小于阈值，则其功能可被平均参数替代，从而减少模型深度。设计动机在于解决全层执行导致的计算浪费，同时通过误差约束确保精度损失可控。

### 掩码引导Token合并（Mask-ToMe）

空间冗余的消除通常依赖注意力权重稀疏化，但本文利用分割掩码直接排除人体Token。Mask-ToMe将Token分为集合$A$（偶数索引）与$B$（奇数索引），计算相似度并合并最相似的背景Token对。人体Token的相似度被设为$-\infty$，确保不被合并。合并后保留$M'$个Token，约束公式为：

$$M' = M_{person} + M_{background\_merged}$$

其中$M_{person}$为人体Token数，$M_{background\_merged}$为合并后的背景Token数。该设计解决了背景Token对姿态估计贡献低但占用大量计算资源的问题，通过掩码引导实现精准压缩。

### 单步扩散解码器

层与Token合并导致精度下降，传统线性解码器无法恢复时序平滑性。本文引入基于VAE潜空间的单步扩散解码器，替代姿态线性解码器。解码器在VAE潜空间中执行单步去噪，条件为视频帧序列特征$X_{1:F}$。去噪过程采用v-prediction目标，公式为：

$$\mathcal{L} = \| \epsilon_\theta(Z_t, t, X_{1:F}) - v_t \|^2$$

其中$v_t$为速度预测，$Z_t$为噪声潜变量。该设计动机在于：单步去噪规避了多步采样的实时性劣势，而VAE潜空间约束确保输出姿态符合人体运动学先验，同时时序条件抑制帧间抖动。

## 实验评估

实验在3DPW与EMDB基准上进行，对比确定性（HMR2.0, CameraHMR, WHAM）与概率（ScoreHMR, HMDiff）基线。遗漏了最新SOTA如SAM 3D Body与OnlineHMR，但覆盖了主要技术路线。

| 方法 | 3DPW PA-MPJPE (mm) | 3DPW MPJPE (mm) | 3DPW PVE (mm) | 吞吐量 (fps) |
|---|---|---|---|---|
| HMR2.0 | 50.6 | 75.0 | 96.4 | 65.2 |
| CameraHMR | 44.4 | 69.8 | 82.2 | 54.5 |
| FastHMR-HMR2.0 | 41.2 | 65.8 | 78.9 | 150.0 |
| FastHMR-CameraHMR | 39.1 | 62.2 | 73.9 | 103.4 |

FastHMR-HMR2.0在3DPW上PA-MPJPE为41.2 mm，优于HMR2.0基线的50.6 mm，吞吐量达150.0 fps，为基线的2.3倍。

| 消融项 | PA-MPJPE (mm) | MPJPE (mm) | 层数 |
|---|---|---|---|
| 基线 (CameraHMR) | – | 73.3 | 32 |
| ECLM ($\tau=0.1$) | – | 73.1 | 26 |
| Mask-ToMe | – | 84.0 | – |
| 扩散解码器 | 39.1 | 62.2 | – |

ECLM在$\tau=0.1$ mm时MPJPE略优于基线，表明严格阈值可提升精度。Mask-ToMe单独使用导致MPJPE升至84.0 mm，但扩散解码器将其恢复至62.2 mm，验证了“压缩-恢复”策略的有效性。

评估指标涵盖MPJPE、PA-MPJPE与PVE，但未报告置信区间。代码与超参数已公开，训练使用2块NVIDIA RTX 6000 GPU，推理使用单块RTX 3090。

## 关联研究分析

从问题动机看，FastHMR与POTTER同属高效HMR路线，但POTTER依赖池化注意力与高分辨率分支，参数缩减至METRO的7%，而FastHMR采用事后合并策略，无需修改骨干架构。这一差异源于任务特性：POTTER针对特定骨干优化，FastHMR追求通用性。FastHMR对分割掩码的依赖是其与POTTER的关键区别，掩码错误会导致背景线索丢失，而POTTER的注意力机制可自适应处理背景。

从方法设计看，FastHMR与ScoreHMR同属概率生成框架，但ScoreHMR采用多步去噪与多假设排序，推理速度仅2.2–18.3 fps；FastHMR采用单步v-prediction，速度达103.4–150.0 fps。这一差异源于实时性需求：ScoreHMR侧重离线高精度，FastHMR侧重在线部署。FastHMR的单步去噪是否足以替代多步采样的时序平滑效果，论文未给出极端遮挡下的消融证据。

## 总结

FastHMR要解决的核心矛盾是Transformer HMR的计算瓶颈与实时性需求。其切入点在于利用层间与空间冗余，通过ECLM与Mask-ToMe压缩计算量，并用单步扩散解码器恢复精度。该框架在3DPW上实现150.0 fps吞吐量与41.2 mm PA-MPJPE，验证了压缩-恢复策略的有效性。然而，实验暴露了分割掩码依赖与背景线索丢失的局限：当掩码错误时，模型无法重建合理姿态；在低光或拥挤场景中，Token合并导致精度下降。当分割掩码不可靠或背景线索主导时，自适应合并策略与联合分割训练是否能在不增加计算量的前提下恢复鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10868)