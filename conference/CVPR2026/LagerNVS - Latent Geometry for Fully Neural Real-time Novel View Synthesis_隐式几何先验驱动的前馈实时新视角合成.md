# CVPR2026最新论文 ｜LagerNVS: Latent Geometry for Fully Neural Real-time Novel View Synthesis ｜隐式几何先验驱动的前馈实时新视角合成

研究机构：英国牛津大学、Meta AI

作者：Stanislaw Szymanowicz、Minghao Chen、Jianyuan Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20176)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20176)

> 神经视图合成（NVS）旨在从有限视角重建并渲染新视角，其核心价值在于满足增强现实、自动驾驶仿真及3D内容生成对实时、高保真三维表示的迫切需求。现有前馈方法虽摆脱了逐场景优化的速度瓶颈，但通用视觉特征缺乏3D几何约束，导致稀疏视角下重建质量受限。LagerNVS通过引入3D感知预训练特征与高速路编码器-解码器架构，在无需显式3D重建的前提下实现了实时渲染。该工作确立了确定性前馈NVS的新标准，但其对遮挡区域的平均化伪影处理仍依赖后续生成式模块，泛化边界尚待检验。

## 研究背景

当相机从稀疏视角观察场景时，单目深度估计在透明、反射表面及遮挡区域存在固有歧义，导致重建几何失真。这种几何歧义使得传统逐场景优化方法（如NeRF）在少量输入下易过拟合，而前馈方法虽能利用网络先验加速推理，但通用视觉特征（如DINOv2）未显式编码3D结构，难以在实时约束下保持几何一致性。解决这一矛盾的关键在于将3D归纳偏置注入前馈架构，同时避免显式重建带来的计算开销。

NVS领域长期面临实时性与高保真度的权衡：显式3D表示（如3DGS）渲染速度快但依赖密集数据，隐式表示平滑但优化耗时。2023年后，前馈式架构成为主流，LVSM等方法通过瓶颈编码器-解码器实现无优化NVS，但信息流受限导致质量瓶颈。LagerNVS的切入点在于证明：即使绕过显式3D重建，利用3D重建网络预训练的隐式特征仍能显著提升性能，且高速路架构比瓶颈设计更优。

## 核心方法

### 方法参照系

前馈NVS的标准流程是将源图像编码为中间表示，再解码为目标视角图像。本文问题与该通用流程的关键差异在于：编码器不输出显式3D坐标，而是利用3D预训练权重提取“3D感知”特征，解码器直接渲染而非重建几何。

### 3D感知编码器初始化

编码器通常采用通用视觉骨干，但缺乏3D结构约束。LagerNVS改用VGGT（Wang et al., 2024）预训练权重初始化编码器，提取其最后一层局部与全局注意力层的token，移除相机token后拼接投影至维度$C$。这一设计动机在于：VGGT特征虽非显式3D，但经3D监督预训练，隐含了几何先验，能缓解通用特征在稀疏视角下的歧义。

$$
\mathbf{z}_i = \text{LayerNorm}\left( W \cdot \left[ \mathbf{z}_i^{\text{local}} \parallel \mathbf{z}_i^{\text{global}} \right] \right)
$$

该公式表示将VGGT的局部与全局token拼接后线性投影并归一化，得到3D感知特征$\mathbf{z}_i$，为解码器提供几何约束。

### 高速路解码器架构

瓶颈解码器将特征压缩至固定维度，信息流受限。LagerNVS采用高速路架构，解码器直接访问所有源图像特征$\mathbf{z}_1, \dots, \mathbf{z}_V$，目标相机以Plücker射线图输入。解码器使用ViT-B，支持全注意力（$O(V^2)$）或交叉注意力（$O(V)$）两种变体。这一设计动机在于：高速路结构保留更多信息流，在固定解码预算下提升质量，同时交叉注意力变体支持9张源图的实时渲染。

$$
\mathbf{I} = h(\mathbf{g}; \mathbf{z}_1, \dots, \mathbf{z}_V)
$$

该公式表示解码器以目标相机$\mathbf{g}$和源特征$\mathbf{z}$为输入，直接输出目标图像$\mathbf{I}$，无需显式3D重建。

## 实验评估

实验在RealEstate10k、DL3DV、CO3D上进行，基线包括LVSM（隐式SOTA）与DepthSplat/AnySplat（显式3DGS）。遗漏生成式方法（如Kaleido）的直接对比，但覆盖了主要前馈路线。

| 方法 | 架构 | Batch | PSNR↑ | SSIM↑ | LPIPS↓ |
|---|---|---|---|---|---|
| LVSM | Bottleneck | 64 | 28.32 | 0.888 | 0.117 |
| LVSM | Decoder-only | 64 | 28.89 | 0.894 | 0.108 |
| Ours | Highway-x-attn | 64 | 30.11 | 0.912 | 0.089 |
| Ours | Highway-full | 64 | 30.48 | 0.918 | 0.086 |
| LVSM | Bottleneck | 512 | 28.58 | 0.893 | 0.114 |
| LVSM | Decoder-only | 512 | 29.67 | 0.906 | 0.098 |
| Ours | Highway-x-attn | 512 | 31.06 | 0.924 | 0.080 |
| Ours | Highway-full | 512 | 31.39 | 0.928 | 0.078 |

LagerNVS在RealEstate10k上PSNR 31.39，较LVSM（28.58）提升2.81dB，验证了3D预训练特征与高速路架构的有效性。

消融显示，端到端微调（E2E）比冻结VGGT权重提升显著，证明3D特征需适配NVS任务。交叉注意力变体在9张源图时仍达30FPS+，全注意力变体仅支持6张，复杂度从$O(V)$升至$O(V^2)$。

评估边界：未报告置信区间，速度对比未量化（仅称30FPS+），且未测试Tanks and Temples等复杂几何场景。代码开源，但超参数依赖数据集混合，可复现性受训练数据规模影响。

## 关联研究分析

从方法设计看，LagerNVS与SHARP（Mescheder et al., 2025）同属前馈路线，但SHARP显式回归3D高斯，LagerNVS隐式渲染。差异根源在于任务特性：SHARP侧重单图几何精度，LagerNVS侧重多视角实时性。LagerNVS在RealEstate10k上超越显式3DGS方法（如AnySplat），暗示隐式表示在通用场景下可能更优，但复杂几何场景下的优势未验证。

从问题动机看，LagerNVS与Kaleido（Liu et al., 2025）均处理遮挡区域，但Kaleido用生成式采样，LagerNVS用确定性回归。LagerNVS的回归损失在遮挡区易平均化，需扩散解码器补充，而Kaleido直接生成合理内容但推理慢。这一差异反映实时性与生成多样性的权衡，LagerNVS的扩散实验仅为初步，未解决在线部署效率问题。

## 总结

LagerNVS要解决的核心矛盾是前馈NVS中通用特征缺乏3D约束导致的几何歧义。其切入点在于证明3D预训练特征可替代显式重建，凭借VGGT权重与高速路架构实现实时渲染。方法上，它通过3D感知编码器与直接渲染解码器，在RealEstate10k上PSNR 31.39，较LVSM提升2.81dB。边界在于：回归损失在遮挡区产生平均化伪影，扩散解码器仅为初步探索，且未测试复杂几何场景。当源视图数量增至10张以上时，高速路架构的解码延迟是否仍满足实时要求，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20176)