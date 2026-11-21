# WACV2026最新论文 ｜Hymavi : A Hybrid Mamba-Attention Network in Multi-View Framework for Volumetric Medical Image Segmentation ｜并行混合架构与多视角融合

作者：Sy Dat Tran、Jin Kyu Gahm

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ab069a11172b)

> 3D医学图像分割需同时捕获跨切片的长程依赖与局部解剖细节，但Transformer的二次复杂度阻碍高分辨率体积数据处理，而纯Mamba模型缺乏空间自适应交互能力。Hymavi通过并行融合Mamba与Attention机制，并引入轴状、矢状、冠状三视角交互框架，解决了串行堆叠导致的信息覆盖问题。该方法在BraTS2023、ACDC和AMOS22数据集上均取得领先性能，但其多视角平均聚合策略是否最优，以及并行架构在极端各向异性数据上的泛化边界，仍需进一步验证。

## 研究背景

3D医学影像分割面临的核心矛盾是全局上下文建模与局部细节保留的平衡。状态空间模型（State Space Model, SSM）如Mamba以线性复杂度实现了高效的全局依赖捕获，但其线性且位置不变的建模特性难以处理不规则边界；自注意力机制虽能进行空间自适应交互，却受限于二次计算复杂度。这一矛盾在高分辨率CT/MRI体积数据中尤为突出，导致现有方法要么牺牲精度换取效率，要么因内存爆炸无法部署。

主流混合架构如SegMamba、HMT-UNet多采用串行堆叠策略，即先执行Mamba再执行Attention，或反之。这种设计存在信息流瓶颈：前一模块捕获的依赖关系可能被后续模块稀释或覆盖，且多数现有工作仅针对2D任务优化，未能充分利用3D体积数据的空间连续性。此外，传统方法仅处理轴状视图，忽略了冠状和矢状视图中蕴含的细长结构（如胰腺、血管）的空间线索。Hymavi的切入点在于：通过并行分支保留两种机制的独立贡献，并将多视角交互作为核心框架而非辅助组件，以解决串行融合的信息损失与单视角的空间信息缺失问题。

## 核心方法

### 方法参照系

本文基于U-Net编码器-解码器骨架，标准流程为CNN提取局部特征后串联Transformer或Mamba模块进行全局建模。关键差异在于：本文摒弃串行堆叠，采用Mamba与Attention并行处理同一输入特征，并引入多视角（轴状、矢状、冠状）联合处理框架，而非仅依赖轴状视图。

### 并行混合Mamba-Attention块（HYMA）

串行融合中，Mamba输出的全局上下文可能被Attention层覆盖，导致局部细节与全局语义无法同时保留。HYMA块将输入特征 $x_h \in \mathbb{R}^{L \times d}$ 经RMS归一化和线性投影后，同时送入Attention流和Mamba流。Attention流执行标准缩放点积注意力，捕获空间自适应的token间交互；Mamba流通过双向扫描机制，利用离散化状态空间方程建模长程依赖。两路输出直接相加融合，避免了串行结构中的信息瓶颈。

$$
f_x = \text{Att}(Q, K, V) + \text{SSM}(X)
$$

该公式的物理含义是：Attention项提供内容自适应的局部-全局交互权重，SSM项提供结构化记忆的全局上下文摘要，二者并行计算后线性叠加，确保局部细节与全局语义在特征空间中独立贡献而非相互干扰。

### 多视角交互增强框架

单视角处理无法充分表达各向异性解剖结构的空间连续性。Hymavi引入Intra-view Enhancement (ITA) 和 Inter-view Enhancement (ITE) 模块。ITA模块在每个视图内应用HYMA块，通过3D ResBlock提取空间特征后，将特征转换为视图特定序列 $f_v' \in \mathbb{R}^{C' \times L}$，其中 $L$ 对应轴状、矢状或冠状视图的序列长度。ITE模块通过跨视图注意力实现视图间信息交换，利用轴状特征作为查询，矢状和冠状特征作为键值，生成跨视图增强特征。

$$
f_{sa} = \sigma(W_{sa} f_a f_s^\top / \sqrt{d}) f_s, \quad f_{ca} = \sigma(W_{ca} f_a f_c^\top / \sqrt{d}) f_c
$$

该公式表明：ITE模块通过可学习权重矩阵 $W_{sa}, W_{ca}$ 计算轴状视图与矢状/冠状视图的注意力权重，实现跨视角上下文动态交换。最终多视角表示通过三视图特征平均聚合，确保各视角的互补信息被均匀整合，避免单一视角主导分割结果。

## 实验评估

实验在BraTS2023、ACDC和AMOS22三个基准数据集上进行，对比基线涵盖Transformer路线（UNETR, SwinUNETR-V2, nnFormer）、Mamba路线（SegMamba, EM-Net, LKM-UNet）及经典U-Net变体。基线覆盖较全面，但缺失近期SOTA如BiSegMamba、HybridMamba，可能高估本文方法的相对优势。

| 数据集 | 方法 | Avg DSC (%) | HD95 (mm) |
| :--- | :--- | :--- | :--- |
| BraTS2023 | Hymavi | 91.92 | 3.54 |
| BraTS2023 | SegMamba | 91.32 | 3.56 |
| BraTS2023 | SwinUNETR-V2 | 89.39 | 4.51 |
| ACDC | Hymavi | 92.67 | - |
| ACDC | SegMamba | 92.27 | - |
| ACDC | nnFormer | 92.06 | - |
| AMOS22 | Hymavi | 87.33 | - |
| AMOS22 | SegMamba | 86.46 | - |
| AMOS22 | nnFormer | 86.45 | - |

Hymavi在三个数据集上均超越SegMamba和SwinUNETR-V2，BraTS2023上较SegMamba提升0.60% DSC，ACDC上提升0.40% DSC，AMOS22上提升0.87% DSC。配对t检验显示改善具有统计显著性（BraTS2023 TC: p=0.01, ET: p=0.007；ACDC RV: p=0.03, Myo: p=0.04, LV: p=0.02）。

| 消融配置 | Avg DSC (%) | 参数 (M) | 推理速度 (case/s) |
| :--- | :--- | :--- | :--- |
| 完整模型（多视角+并行） | 92.67 | 9.45 | 8.75 |
| 移除Mamba | 90.97 | 13.28 | - |
| 移除Attention | 91.44 | 11.35 | - |
| 移除多视角 | 92.28 | 17.20 | - |
| 串行SSM→Att | 90.72 | - | - |
| 串行Att→SSM | 91.22 | - | - |

消融实验表明：Mamba移除导致DSC下降1.70%，Attention移除下降1.23%，多视角移除下降0.39%，证实Mamba对长程依赖捕获贡献最大。并行融合较串行SSM→Att提升1.95% DSC，较Att→SSM提升1.45% DSC，直接验证了并行策略优于串行堆叠。Hymavi参数量9.45M低于完整多视角模型17.20M，推理速度8.75 case/s，内存占用约7.4GB，显著低于SegMamba的25GB，得益于Stem层降采样和切片级处理策略。

评估指标包含DSC和HD95，覆盖重叠度与边界精度。实验协议采用70/10/20训练/验证/测试划分，训练约850 epochs，使用SGD优化器。代码已开源，超参数（学习率、权重衰减、动量）明确记录，可复现性良好。局限在于：未报告置信区间，跨数据集比较需谨慎；多视角平均聚合策略未探索动态加权，可能忽略视图重要性差异。

## 关联研究分析

从问题动机看，Hymavi与SegMamba均聚焦3D体积分割中的全局-局部建模，但SegMamba采用纯SSM串行设计，依赖结构化状态空间动态建模空间依赖，而Hymavi引入并行Attention以弥补SSM在空间自适应交互上的不足。这一差异源于任务特性：BraTS2023等数据集包含不规则肿瘤边界，纯线性建模难以捕获细微形态变化，而Attention的空间自适应权重能动态聚焦关键区域。Hymavi在BraTS2023上较SegMamba提升0.60% DSC，证实了并行架构对复杂边界的优势。

从方法设计看，Hymavi与SwinUNETR-V2同属混合架构，但SwinUNETR-V2采用移位窗口注意力替代全局自注意力以降低复杂度，而Hymavi通过Mamba实现线性复杂度全局建模，并引入多视角交互。SwinUNETR-V2在BraTS2023上DSC为89.39%，低于Hymavi的91.92%，表明Mamba的全局摘要能力优于窗口注意力。然而，Hymavi的多视角框架增加了计算开销，其平均聚合策略是否优于动态加权视图重要性，论文未给出回答。此外，Hymavi未对比BiSegMamba等最新SOTA，其优势是否源于多视角而非并行架构，仍需进一步验证。

## 总结

Hymavi旨在解决3D医学分割中全局上下文建模与局部细节保留的矛盾，以及单视角处理的空间信息缺失问题。现有串行混合架构存在信息覆盖瓶颈，纯SSM模型缺乏空间自适应能力，而Hymavi通过并行Mamba-Attention融合和多视角交互框架，同时保留两种机制的独立贡献并整合跨视角线索。该方法在BraTS2023、ACDC和AMOS22上均超越SegMamba和SwinUNETR-V2，BraTS2023 Avg DSC达91.92%，ACDC达92.67%。其边界在于：多视角采用平均聚合，未探索动态视图加权；并行架构在极端各向异性数据上的泛化能力未充分验证。当支持集增大或数据分布发生显著漂移时，并行融合与多视角交互的相对贡献是否会发生逆转，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ab069a11172b)