# CVPR2026最新论文 ｜GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator ｜几何感知视频生成修复 3DGS 伪影

研究机构：美国斯坦福大学

作者：Liyuan Zhu、Manjunath Narayana、Michal Stary 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25053)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25053)

> 3DGS 重建在稀疏视图或噪声输入下常产生浮点、闪烁与模糊伪影，现有基于 RGB 的生成式修复方法因缺乏几何约束而难以处理严重几何错误，且无法跨优化式与前馈式重建范式泛化。GaussFusion 提出一种几何感知的视频到视频生成框架，通过编码高斯基元的深度、法线、不透明度与协方差信息，实现跨范式伪影修复。该方法在 DL3DV 和 RE10K 上显著优于基线，蒸馏变体达到 15.11 FPS 实时性能。其价值在于打破了修复模型对特定重建管线的依赖，但未提供几何精度指标以验证生成内容是否引入幻觉。

## 研究背景

3DGS 将场景表示为各向异性高斯集合，通过可微光栅化实现实时渲染。然而，当输入视图稀疏或相机位姿存在误差时，优化过程易陷入局部极小值，导致高斯分布出现浮点伪影或几何塌陷。前馈式重建虽消除了逐场景优化，但其预测的高斯参数在极端稀疏视图下同样存在几何不一致性。这两种范式产生的退化模式截然不同，优化式管线倾向于产生模糊与重影，而前馈式管线则易出现半透明高斯与尖刺几何。

现有生成式修复方法如 Difix3D+ 和 ExploreGS 仅以 RGB 渲染图为条件，缺乏对底层几何结构的感知，导致在处理大面积缺失或严重几何错误时产生歧义。更关键的是，这些模型通常针对单一重建范式训练，无法泛化至其他管线。GaussFusion 的切入点在于：利用 3DGS 本身携带的丰富几何属性作为生成条件，并通过混合多种退化模式的训练数据，构建一个对重建范式无关的通用修复器。

## 核心方法

### 方法参照系

本文问题属于生成式先验辅助的 3D 重建后处理。标准流程是：获取初始 3DGS 重建 → 渲染新视角图像 → 使用扩散模型修复伪影 → 可选地用修复图像更新 3DGS。关键差异在于，本文不再仅使用 RGB 图像作为条件，而是引入包含几何信息的 GP-Buffer，并采用视频生成框架保证时序一致性。

### GP-Buffer 几何条件编码

传统方法仅将 RGB 渲染图输入生成器，导致模型无法区分“模糊是因为纹理缺失”还是“模糊是因为高斯分布错误”。GaussFusion 引入 Gaussian Primitives Buffer (GP-Buffer)，将 3DGS 的高斯属性投影至像素空间。GP-Buffer 包含颜色 $\mathbf{C}$、不透明度 $A$、深度 $D$、法线 $\mathbf{N}$ 和逆协方差 $\mathbf{U}$，其中逆协方差 $\mathbf{U}$ 编码了局部几何不确定性：

$$
\mathbf{G} = [\mathbf{C}, A, D, \mathbf{N}, \mathbf{U}] \in \mathbb{R}^{W \times H \times 10 \times T}
$$

该公式将多模态几何线索对齐至像素网格，使生成器能“看穿”浮点伪影，识别哪些区域是真实表面，哪些是噪声高斯。法线通过相机空间位置图的有限差分计算，仅在 $A(\mathbf{u}) > \tau$ 的像素处评估，避免前景背景混合。

### Geometry Adapter 与跨范式泛化

GP-Buffer 需注入视频生成骨干网络。GaussFusion 设计 Geometry Adapter (GA) 模块，作为并行侧网络与 DiT 块交错。GA 将编码后的 GP-Buffer 潜变量 $\mathbf{z}_G$ 通过 3D 卷积投影，并通过自注意力与交叉注意力融合几何与文本特征：

$$
\mathbf{x}_g = \text{GA}(\mathbf{z}_G, \mathbf{x}_{\text{text}}), \quad \mathbf{x} \leftarrow \mathbf{x} + \text{Modulate}(\mathbf{x}, \mathbf{x}_g)
$$

此设计解决了直接拼接条件潜变量导致的几何对齐弱问题。为提升效率，采用分布匹配蒸馏 (DMD) 将多步生成器压缩为 4 步，仅微调 GA 层。训练数据通过模拟稀疏视图、随机初始化及前馈模型退化构建，确保模型同时见过优化式与前馈式伪影，从而实现跨范式泛化。

## 实验评估

实验在 DL3DV 和 RE10K 数据集上进行，对比基线包括 Splatfacto、GenFusion、Difix3D+ 和 ExploreGS。基线覆盖了图像扩散与视频扩散两种路线，但缺失非生成式的几何正则化方法（如 LGDWT-GS）作为对照，可能高估生成式方法的相对优势。

| 方法 | DL3DV PSNR | DL3DV SSIM | RE10K PSNR | RE10K SSIM |
| :--- | :--- | :--- | :--- | :--- |
| Splatfacto | 17.417 | 0.605 | 19.234 | 0.708 |
| Difix3D+ | 18.87 | 0.626 | 21.98 | 0.767 |
| ExploreGS | 18.71 | 0.611 | 22.06 | 0.742 |
| GaussFusion (Full) | 20.689 | 0.760 | 24.025 | 0.874 |
| GaussFusion (Few-step) | 22.494 | 0.842 | 28.254 | 0.952 |

GaussFusion (Full) 在 DL3DV 上 PSNR 达 20.689，较 Difix3D+ 提升 1.819 dB；在 RE10K 上 PSNR 达 24.025，较 ExploreGS 提升 1.965 dB。Few-step 变体在 RE10K 上 PSNR 达 28.254，显著高于 Full 版本，表明蒸馏过程可能引入了额外的正则化效应或数据分布偏差，这一反直觉现象需进一步探究。

消融实验显示，仅使用 RGB 条件时 PSNR 为 19.148，加入全部几何模态后提升至 20.753，证明几何线索对伪影消除的关键作用。移除 Geometry Adapter 后 PSNR 从 22.548 降至 20.904，LPIPS 从 0.278 升至 0.308，验证了 GA 模块在几何对齐上的必要性。

评估仅使用 PSNR、SSIM、LPIPS 和 FID，未报告 Chamfer Distance (CD) 或 F-score 等几何精度指标。这意味着无法判断生成式修复是否在提升视觉质量的同时引入了几何幻觉。代码未公开，但提供了训练细节：8 张 H200 GPU，100K 步，batch size 8，分辨率 480×832。

## 关联研究分析

从问题动机看，GaussFusion 与 MVSplat360 均旨在修复前馈式 3DGS 伪影，但 MVSplat360 紧密耦合于 MVSplat 特定模型，无法泛化至优化式管线。GaussFusion 通过混合退化数据训练，证明了单一模型可处理两种范式的不同退化模式。这一差异源于任务特性：前馈式伪影具有特定的半透明与尖刺特征，而优化式伪影多为模糊与重影，混合训练迫使模型学习更鲁棒的几何先验，而非过拟合特定管线。

从方法设计看，GaussFusion 与 ExploreGS 同属视频扩散修复框架，但 ExploreGS 仅以 RGB 为条件，而 GaussFusion 引入 GP-Buffer。这一差异并非单纯的技术升级，而是对“生成式先验应如何感知 3D 结构”的不同回答。ExploreGS 依赖时序一致性隐含几何约束，而 GaussFusion 显式注入几何属性。在 DL3DV 上，GaussFusion 的 SSIM (0.760) 显著高于 ExploreGS (0.611)，表明显式几何条件比隐式时序约束更能保持结构一致性。然而，GaussFusion 的 FID (6.269) 高于 ExploreGS (4.217)，暗示显式几何条件可能在某些场景下限制了生成多样性。

## 总结

GaussFusion 解决的核心矛盾是生成式修复模型对重建范式的依赖性与几何条件缺失问题。现有方法如 Difix3D+ 仅以 RGB 为条件，无法处理严重几何错误；MVSplat360 虽针对前馈式优化，但无法泛化至优化式管线。GaussFusion 通过引入 GP-Buffer 显式编码深度、法线与协方差，并采用混合退化数据训练，实现了跨范式泛化。实验证明其在 DL3DV 上 PSNR 达 20.689，较基线提升约 1.8 dB，蒸馏变体达到 15.11 FPS 实时性能。其边界在于未提供几何精度指标，无法验证生成内容是否引入幻觉；且 Few-step 变体在 RE10K 上 PSNR 异常高于 Full 版本，暗示蒸馏过程可能存在数据分布偏差。当输入视图极度稀疏（如 2-3 张）时，GP-Buffer 中的几何信息本身已严重退化，此时生成式修复是否仍能保持几何一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25053)