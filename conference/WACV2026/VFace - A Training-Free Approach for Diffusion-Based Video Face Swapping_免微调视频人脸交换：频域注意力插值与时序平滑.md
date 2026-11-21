# WACV2026最新论文 ｜VFace: A Training-Free Approach for Diffusion-Based Video Face Swapping ｜免微调视频人脸交换：频域注意力插值与时序平滑

研究机构：美国密歇根州立大学、韩国成均馆大学

作者：Sanoojan Baliah、Yohan Abeysinghe、Rusiru Thushara 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07835)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07835)

> 视频人脸交换旨在将单张源图像的身份特征迁移至目标视频序列，同时保留目标的姿态、表情与背景，核心难点在于扩散模型逐帧推理引发的时序闪烁与身份漂移。现有图像交换方法直接扩展至视频时缺乏时序建模，而视频生成方法又依赖完整源视频或额外训练，导致灵活性受限。VFace 通过双分支注意力注入、频域特征插值及光流引导的注意力平滑，实现了免训练的视频交换。该方法在 UNet 架构下验证了有效性，但其对 DiT 骨干的适配性及长视频累积漂移问题仍存疑。

## 研究背景

视频人脸交换面临的核心困境是扩散模型的随机性与时序一致性需求的冲突。当基于去噪扩散概率模型（DDPM）或去噪扩散隐式模型（DDIM）的图像交换方法逐帧处理视频时，每帧独立的去噪过程导致相邻帧间出现细微差异，表现为视觉上的闪烁（Flickering）。为缓解此问题，传统方法引入光流或时空注意力层，但前者依赖像素级对齐易受遮挡干扰，后者需大规模视频数据训练，限制了部署效率。

主流路线分为两类：一类是 GAN 架构（如 SimSwap、HifiFace），虽推理快但泛化性差，难以处理极端姿态；另一类是视频扩散模型（如 AnyV2V、Go-with-the-Flow），虽具备时序建模能力，但 AnyV2V 需 500 步 DDIM 反转导致推理缓慢，Go-with-the-Flow 需在噪声层进行光流扭曲且依赖少量视频微调。VFace 的切入点在于利用 DDIM 反转的确定性特性，在注意力层而非像素层或噪声层进行结构引导与身份注入，从而在保持图像交换模型免训练优势的同时，以极低计算成本实现时序平滑。

## 核心方法

### 双分支注意力注入参照系

VFace 基于 REFace 构建，采用双分支架构：重建分支（Reconstruction Pipeline）通过 DDIM 反转获取目标视频帧的潜变量 $\mathbf{I}^{tar}_i$，并去噪以提取结构信息；生成分支（Generation Pipeline）以源图像身份为条件进行生成。两分支共享去噪网络权重，差异在于条件输入。该架构的关键差异在于，VFace 不修改网络参数，而是通过动态替换生成分支中的注意力张量，将目标结构“嫁接”到身份生成过程中。

### 目标结构引导（TSG）

TSG 解决的是生成分支中目标姿态与表情丢失的问题。通常做法是将目标图像作为条件输入，但 VFace 选择直接替换生成分支在去噪步 $t$ 的查询（Query）和键（Key）张量。具体而言，生成分支的 $\mathbf{q}^{gen}_{i,t}$ 和 $\mathbf{k}^{gen}_{i,t}$ 被重建分支对应的 $\mathbf{q}^{rec}_{i,t}$ 和 $\mathbf{k}^{rec}_{i,t}$ 替换：

$$ \mathbf{q}^{gen}_{i,t} \leftarrow \mathbf{q}^{rec}_{i,t}, \quad \mathbf{k}^{gen}_{i,t} \leftarrow \mathbf{k}^{rec}_{i,t} $$

这一操作强制生成分支在空间布局上严格遵循目标视频的结构，确保了姿态和表情的精确对齐，避免了传统条件输入中可能出现的结构模糊。

### 频域注意力插值（FSAI）

TSG 的完全替换会导致源身份特征被目标结构淹没，造成身份保真度下降。FSAI 通过频域分解解耦身份与结构。假设 $\mathbf{a}^{src}$ 为源身份引导的注意力特征，$\mathbf{a}^{tar}_i$ 为目标结构引导的特征，VFace 对两者进行一维快速傅里叶变换（FFT），并按比例 $\rho$（实验设为 0.8）混合低频与高频分量：

$$ \mathbf{a}^{out} = \text{IFFT}(\text{Low}(\mathbf{a}^{src}) \cdot \rho + \text{High}(\mathbf{a}^{tar}_i) \cdot (1-\rho)) $$

低频分量承载粗粒度语义（如身份），高频分量承载细粒度结构（如纹理、边缘）。此设计保留了源图像的身份特征，同时从目标帧获取结构细节，解决了 TSG 中身份丢失的失效模式。

### 光流引导注意力时序平滑（FATS）

FATS 针对扩散过程固有的随机性导致的帧间闪烁。不同于 Go-with-the-Flow 在噪声层操作，FATS 在注意力层利用光流 $\mathbf{f}_i$ 对前一帧特征 $\mathbf{x}_{prev,i}$ 进行扭曲，并与当前帧特征 $\mathbf{x}_{i+1}$ 混合：

$$ \mathbf{x}^{smooth}_{i+1} = \alpha \cdot \text{Warp}(\mathbf{x}_{prev,i}, \mathbf{f}_i) + (1-\alpha) \cdot \mathbf{x}_{i+1} $$

其中 $\alpha=0.8$。该操作仅在前 $T_1=10$ 个 DDIM 步执行，此时注意力图分辨率较低（64×64），计算开销小。通过软混合而非硬替换，FATS 对光流估计误差具有鲁棒性，有效抑制了早期去噪步骤中的时序不一致。

## 实验评估

VFace 在 FFHQ、CelebA、VFHQ 和 CelebV-HQ 数据集上进行了评估，基线包括 MegaFS、SimSwap、DiffSwap、REFace、AnyV2V 和 Go-with-the-Flow。在图像交换任务中，VFace 在 FFHQ 上取得 FID 4.29，优于 REFace 的 5.53；在 CelebA 上 FID 为 5.42，同样领先。在视频交换任务中，VFace 在 CelebV-HQ 上的 CD-FVD 为 163.82，FVD 为 96.54，显著优于 REFace+AnyV2V（CD-FVD 281.05）和 REFace+Go-with-the-Flow（CD-FVD 302.10）。

| 数据集 | 方法 | FID ↓ | ID Retrieval Top-1 ↑ | CD-FVD ↓ | FVD ↓ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FFHQ | REFace | 5.53 | 95.40% | - | - |
| FFHQ | VFace | 4.29 | 96.20% | - | - |
| CelebA | REFace | 6.09 | 98.80% | - | - |
| CelebA | VFace | 5.42 | 96.20% | - | - |
| CelebV-HQ | REFace+AnyV2V | - | - | 281.05 | 78.35 |
| CelebV-HQ | REFace+VFace | - | - | 163.82 | 96.54 |
| VFHQ | REFace+VFace | - | - | 170.90 | 230.31 |

消融实验显示，TSG 单独使用时 Pose 误差降至 2.61，但 ID Sim 降至 0.53；加入 FSAI 后 ID Sim 回升至 0.57，Pose 保持 2.77；加入 FATS 后 CD-FVD 从 232.20 降至 170.90。这表明 FSAI 对身份保真度至关重要，而 FATS 主要贡献于时序一致性。推理时间方面，VFace 每帧耗时 10.1 秒，高于 REFace 的 4.8 秒，但远低于 AnyV2V 的 15.8 秒和 Go-with-the-Flow 的 16.7 秒。

评估边界方面，VFace 使用 ArcFace 进行身份检索，但未报告置信区间。实验仅在 512×512 分辨率下进行，未测试更高分辨率下的性能。代码已开源，但超参数（如 $\rho$ 和 $\alpha$）的敏感性分析未在正文中详细展开，仅在附录提及。

## 关联研究分析

从问题动机看，VFace 与 InstantID 和 PuLID 同属免微调范式，但任务设定不同。InstantID 和 PuLID 依赖文本提示控制生成内容，而 VFace 依赖目标视频结构。VFace 的 FSAI 机制在频域解耦身份与结构，这与 DVI 的正交解耦思想相似，但 DVI 在 DiT 骨干上操作，VFace 在 UNet 上操作。VFace 未使用 ArcFace 嵌入直接注入，而是通过 DDIM 反转和注意力替换实现，这可能限制了其在极端姿态下的鲁棒性，因为 DDIM 反转对初始噪声敏感。

从方法设计看，VFace 与 Go-with-the-Flow 均利用光流，但作用层级不同。Go-with-the-Flow 在噪声层扭曲，VFace 在注意力层扭曲。注意力层操作更稳定，因为注意力图已包含语义信息，而噪声层仅包含随机信号。然而，VFace 的光流计算在 64×64 分辨率下进行，可能丢失细粒度运动信息。与 AnyV2V 相比，VFace 使用 50 步 DDIM 反转，而 AnyV2V 使用 500 步，VFace 的推理速度优势明显，但 50 步反转是否足以捕捉复杂结构，论文未提供对比实验。

## 总结

VFace 解决了图像交换模型扩展至视频时的时序闪烁问题，通过频域注意力插值平衡身份保真与结构对齐，利用光流在注意力层实现时序平滑。实验表明，VFace 在 CD-FVD 上比 REFace+AnyV2V 降低 41.6%，在 FFHQ 上 FID 比 REFace 降低 22.4%。其边界在于依赖 UNet 架构，未验证在 DiT 骨干上的有效性，且仅处理 3-20 秒短视频，长视频累积漂移问题未解决。当目标视频包含快速运动或复杂遮挡时，64×64 分辨率的光流估计是否足以维持时序一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07835)