# TVCG2026最新论文 ｜DreamLifting: A Plug-in Module Lifting MV Diffusion Models for 3D Asset Generation ｜轻量级高斯资产适配器

研究机构：南开大学、南京大学

作者：Ze-Xin Yin、Jiaxiong Qiu、Liu Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.07435)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07435)

> 导读 现代图形管线依赖具备物理基于渲染（PBR）材质的3D资产，但传统建模耗时且现有生成方法多仅输出顶点色，无法支持重光照。本文提出LGAA，通过复用预训练多视图扩散模型的特征，直接生成带PBR通道的高斯资产，规避了对大规模3D数据的依赖。该方法以69k实例实现数据高效微调，在PBR质量上优于联合生成基线，但其几何保真度是否足以支撑复杂拓扑场景仍存疑。

## 研究背景

PBR材质包含反照率、金属度与粗糙度，是资产可重光照的前提。然而，几何、材质与光照的联合恢复是病态问题，导致多数生成方法将纹理烘焙为顶点色，或依赖后处理扩散模型合成纹理，后者易产生UV对齐模糊。多视图（MV）扩散模型在生成多视图一致图像时，其内部特征已隐含几何与PBR先验，这为直接提取3D资产提供了可能。

主流路线分为优化式蒸馏与前馈式生成。优化式方法如DreamFusion依赖分数蒸馏采样，速度慢且存在多视图幻觉；前馈式方法如TRELLIS虽实现快速生成，但仅建模几何与顶点色，缺乏PBR通道。3DTopia-XL虽支持端到端PBR生成，但需16节点A100 GPU及256k高质量3D实例训练，数据与算力门槛极高。本文切入点在于：预训练MV扩散模型的特征是否可直接映射为显式3D表示，从而在低数据量下实现PBR资产生成。

## 核心方法

### 方法参照系

标准3D资产生成流程为：3D VAE压缩几何至潜空间，LDM在潜空间扩散，解码器重建网格。本文差异在于：不训练原生3D LDM，而是复用2D MV扩散模型的特征，通过适配器直接生成2D高斯泼溅（2DGS）资产，将3D生成转化为2D特征到3D表示的映射问题。

### LGAA Wrapper与Switcher

LGAA Wrapper克隆并冻结MV扩散模型的预训练层，注入零初始化卷积层（ZC）以适配3D任务。设计动机是保留预训练先验，避免从头训练导致的收敛困难与先验丢失。LGAA Switcher通过层间ZC层对齐几何分支与外观分支的特征，防止早期训练中的先验冲突。其对齐机制可表示为：

$$Y'_{align} = Y_{geo} + ZC(Y_{app})$$

其中$Y_{geo}$与$Y_{app}$分别为几何与外观分支特征，$ZC$为零初始化卷积。该设计使模型在训练初期保持分支独立性，随训练推进逐步建立双向信息交换。

### LGAA Decoder与延迟着色

LGAA Decoder将特征上采样并解码为像素对齐的2DGS，每个像素对应一个高斯基元，包含位置$\boldsymbol{\mu} \in \mathbb{R}^3$、旋转$\boldsymbol{q} \in \mathbb{R}^4$、缩放$\boldsymbol{s} \in \mathbb{R}^2$、不透明度$o \in \mathbb{R}$及PBR通道。设计动机是解决几何-材质歧义：引入基于图像的延迟着色损失，将G-buffer与RGB外观耦合。损失函数为：

$$\mathcal{L}_{deferred} = \| I_{shaded} - I_{gt} \|_2^2$$

其中$I_{shaded}$为通过G-buffer与恢复的环境图渲染的图像，$I_{gt}$为真实图像。该损失在训练阶段约束PBR通道与外观的一致性，提升材质真实感。

## 实验评估

实验基于G-Objaverse数据集，筛选69k实例训练，10k实例用于延迟着色微调。基线覆盖3DTopia-XL（PBR联合生成）、TRELLIS（原生3D几何）、LGM/LaRa（重建式）及两阶段管线（TRELLIS+TexGaussian）。缺失SOPHY、PhysGen等PBR专用方法的直接对比。

| 模块 | FID↓ | FID_mat↓ | CLIP score↑ |
| :--- | :--- | :--- | :--- |
| w/o LGAA-W | 54.52 | 74.31 | 32.76 |
| w/o LGAA-S | 38.33 | 47.48 | 33.60 |
| w/o LGAA-D | 37.39 | 42.37 | 33.73 |
| Full model | 36.38 | 41.47 | 33.70 |

消融显示，移除LGAA Wrapper导致FID从36.38升至54.52，证实预训练先验保留的关键性；移除Switcher使FID_mat从41.47升至47.48，表明分支对齐对PBR质量的影响大于几何质量。延迟着色损失对FID_mat的改善边际较小（43.52→41.47），但定性结果显示金属度与粗糙度通道视觉质量提升。

评估协议包含CD、F-Score、FID、CLIP Score及PBR专用指标（PSNR_albedo, MSE_metallic, MSE_roughness）。局限在于：未报告置信区间；几何指标（CD/F-Score）未与纯几何SOTA（如SPGen CD 0.85）直接对比，仅定性优于TRELLIS；后处理时间30秒未纳入效率评估。代码与权重已开源，训练仅需单节点8卡H20 GPU，可复现性较高。

## 关联研究分析

从问题动机看，LGAA与3DTopia-XL均追求端到端PBR生成，但前者复用2D先验，后者依赖大规模3D数据。差异根源在于数据效率：LGAA通过冻结预训练层保留2D知识，仅需69k实例微调，而3DTopia-XL需256k实例从头训练。这暗示2D先验在PBR生成中可能比3D数据更关键，但论文未评估稀有类别的泛化能力，69k数据是否覆盖长尾分布存疑。

从方法设计看，LGAA与TRELLIS同属前馈式生成，但TRELLIS仅输出几何+顶点色，LGAA补充PBR通道。差异在于表示选择：TRELLIS使用结构化潜变量（SLats），LGAA使用2DGS。2DGS的像素对齐特性使其更易利用2D网络，但非结构化表示可能限制复杂拓扑的精确建模。论文未对比2DGS与SLats在拓扑稳定性上的差异，这一盲区可能影响资产在仿真中的可用性。

## 总结

LGAA解决的核心矛盾是PBR资产生成对大规模3D数据的依赖与数据稀缺的冲突。其切入点在于预训练MV扩散模型特征隐含几何与PBR先验，通过LGAA Wrapper/Switcher/Decoder直接映射为2DGS，实现数据高效生成。实验证明，69k实例下FID_mat达41.47，优于3DTopia-XL，且训练算力仅为后者的1/16。边界在于：几何保真度未与纯几何SOTA定量对比，后处理30秒限制实时应用，且未评估复杂拓扑场景的稳定性。当资产需参与物理仿真时，2DGS表示的拓扑一致性是否足以支撑关节运动，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07435)