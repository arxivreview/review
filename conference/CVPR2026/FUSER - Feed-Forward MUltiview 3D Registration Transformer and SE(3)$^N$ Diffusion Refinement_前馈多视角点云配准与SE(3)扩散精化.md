# CVPR2026最新论文 ｜FUSER: Feed-Forward MUltiview 3D Registration Transformer and SE(3)$^N$ Diffusion Refinement ｜前馈多视角点云配准与SE(3)扩散精化

研究机构：新加坡南洋理工大学、阿里巴巴集团

作者：Haobo Jiang、Jin Xie、Jian Yang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09373)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09373)

> 多视角点云配准旨在将无序、部分重叠的扫描序列对齐至统一坐标系，传统“两两配准+全局同步”范式因冗余计算与误差累积而效率低下。FUSER通过联合编码所有扫描并直接回归全局位姿，消除了显式匹配步骤。该方法结合绝对几何编码与2D注意力先验迁移，实现了从分钟级到秒级的推理加速。其核心贡献在于验证了前馈范式在精度与效率上的双重优势，但大规模场景下的可扩展性仍存疑。

## 研究背景

多视角配准需估计 $N$ 个扫描的全局刚体位姿 $\mathbf{T}_i \in SE(3)$。传统流程依赖两两相对位姿估计构建位姿图，再通过同步算法求解全局解。这一过程隐含假设两两估计的独立性，忽略了全局几何约束，导致低重叠场景下相对位姿歧义，且误差在同步阶段累积。

主流方法如LMVR、SGHR及MDGD均遵循“两两-全局”范式，通过优化图结构或引入鲁棒损失提升稳定性，但无法摆脱冗余两两计算的开销。随着扫描数量增加，两两匹配的计算复杂度呈二次增长，且对离群点敏感。FUSER的切入点在于打破这一范式，提出端到端的前馈Transformer，直接在全局潜空间中推理所有扫描的位姿，避免中间两两估计的误差传播与计算瓶颈。

## 核心方法

### 绝对几何编码与前馈架构

传统描述符如GeoTransformer采用相对坐标归一化以增强旋转不变性，但FUSER需回归绝对平移，相对编码会丢失全局位置线索。为此，FUSER采用基于MinkowskiEngine的稀疏3D CNN，将每个扫描编码为低分辨率超级点特征 $\mathbf{F}_i \in \mathbb{R}^{M'_i \times d}$，保留绝对空间线索。该编码器通过五层稀疏卷积（kernel size 3, stride 2）压缩点数，确保后续注意力机制的计算可行性。

### 几何交替注意力与2D先验迁移

为平衡局部细节与全局上下文，FUSER引入几何交替注意力（Geometric Alternating Attention），包含16层内扫描与16层跨扫描注意力块。其关键创新在于从2D基础模型 $\pi_3$ 迁移注意力权重，利用2D重建中学习的视图分组与对齐一致性先验增强3D几何推理。为保持排列等变性，移除了VGGT中的参考令牌，并采用正弦位置编码替代2D ROPE。

$$
\mathbf{F}^{(l+1)} = \text{AA}^{(l)}(\mathbf{F}^{(l)}; \mathbf{P}_\pi)
$$

该公式表示第 $l$ 层交替注意力更新特征，$\mathbf{P}_\pi$ 为排列算子，确保扫描顺序变化不改变特征表示。

### SE(3)_[N]_ 扩散精化

FUSER-DF将位姿精化建模为联合 $SE(3)_{[N]}$ 空间中的去噪过程。不同于从单位矩阵开始的两两扩散，FUSER-DF以FUSER预测的位姿 $\hat{\mathbf{T}}_{1:N}$ 为先验，通过前向扩散引入噪声，反向去噪逐步修正至最优位姿。

$$
\mathbf{T}^{(t)}_{1:N} = F(\sqrt{\bar{\alpha}_t}; \mathbf{T}^{(0)}_{1:N}, \hat{\mathbf{T}}_{1:N}) + \gamma \sqrt{1-\bar{\alpha}_t} \boldsymbol{\epsilon}
$$

该公式定义前向扩散过程，$F$ 为位姿插值函数，$\boldsymbol{\epsilon} \sim \mathcal{N}(0, \mathbf{I})$ 为高斯噪声，$\gamma$ 控制噪声强度。

## 实验评估

在ScanNet（30 scans）、3DMatch（60 scans）及ArKitScenes（200 scans）上，FUSER与FUSER-DF均显著优于LMVR、SGHR、MDGD等基线。基线覆盖了两两配准+同步的主流路线，但未包含纯生成式多视角基线。

| 数据集 | 方法 | RR (%) | RE (°) | TE (m) |
|---|---|---|---|---|
| 3DMatch (60 scans) | FUSER | 88.6 | 3.2 | 0.16 |
| 3DMatch (60 scans) | FUSER-DF | 90.5 | 2.9 | 0.15 |
| 3DMatch (60 scans) | Full+PARENet | 61.9 | 31.2 | 0.68 |
| ArKitScenes (200 scans) | FUSER | 84.1 | 6.6 | 0.20 |
| ArKitScenes (200 scans) | FUSER-DF | 90.3 | 6.2 | 0.17 |
| ArKitScenes (200 scans) | Full+GeoTrans | 24.7 | 92.5 | 1.36 |

FUSER-DF在3DMatch上RR达90.5%，较最强基线Full+PARENet提升28.6个百分点；在ArKitScenes上RR达90.3%，远超Full+GeoTrans的24.7%。

消融实验显示，2D注意力先验迁移对性能提升显著：移除该先验后，ScanNet上Mean RE从7.1°升至34.6°。训练数据规模扩展（从ScanNet到四数据集联合）使Mean RE从22.3°降至7.1°，表明数据多样性对泛化性至关重要。

评估边界方面，论文未报告置信区间，且最大扫描数限于200。代码已开源，训练使用8块NVIDIA L20 GPU，FUSER参数量约0.6B。

## 关联研究分析

从问题动机看，FUSER与Predator、GeoTransformer等两两配准方法存在根本差异。后者聚焦于两云间相对位姿的鲁棒估计，依赖显式特征匹配与RANSAC；FUSER则直接回归全局位姿，摒弃匹配步骤。这一差异源于任务定义：两两配准假设重叠区域显著，而多视角配准需处理全局一致性，显式匹配在低重叠下易失效。FUSER的绝对编码设计正是为了解决两两方法中相对坐标导致的平移歧义问题。

从方法设计看，FUSER与VGGT共享交替注意力架构，但VGGT用于2D图像重建，FUSER将其迁移至3D点云。关键差异在于位置编码：VGGT使用2D ROPE，FUSER改用正弦编码以适配3D空间。此外，FUSER-DF扩展了SE(3)扩散模型从两两到多视角，引入先验条件以加速收敛。这一设计是否牺牲了对极端离群点的鲁棒性，相比RANSAC缺乏理论保障，论文未提供对比实验。

## 总结

FUSER解决了多视角配准中两两范式导致的冗余计算与误差累积矛盾，通过前馈Transformer直接回归全局位姿，实现了精度与效率的双重突破。其核心创新在于绝对几何编码保留平移线索，2D注意力先验迁移增强3D推理，以及SE(3)_[N]_扩散精化提升最终精度。实验证明FUSER-DF在3DMatch上RR达90.5%，推理时间从分钟级降至秒级。然而，论文实验最大扫描数为200，未验证超大规模场景（>1000 scans）下的可扩展性。当扫描数量进一步增加时，交替注意力的计算复杂度是否仍保持线性增长，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09373)