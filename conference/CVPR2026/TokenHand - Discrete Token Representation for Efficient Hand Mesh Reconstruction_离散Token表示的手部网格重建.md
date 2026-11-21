# CVPR2026最新论文 ｜TokenHand: Discrete Token Representation for Efficient Hand Mesh Reconstruction ｜离散Token表示的手部网格重建

研究机构：德国慕尼黑工业大学

作者：Xinguo He、Yixin Shen、Rahul Chaudhari

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8af062843c87)

> 单目3D手姿估计需在精度、鲁棒性与实时性间取得平衡，但现有方法难以同时满足这三者，尤其在遮挡场景下。主流参数化回归方法受限于MANO运动链的误差累积，而直接顶点回归方法则缺乏几何先验导致结构失真。TokenHand通过将手部网格映射为离散Token分类问题，结合轻量级解码器，在保持高精度的同时实现了实时推理。该方法在效率与精度的权衡上表现优异，但其对严重遮挡场景的鲁棒性及野外泛化能力尚未得到充分验证。

## 研究背景

单目图像缺乏深度信息，导致手部在3D空间中的尺度与位置存在歧义。为消解这一歧义，领域内确立了基于MANO参数化手模型的主流范式，通过回归低维形状与姿态参数来保证解剖学合理性。然而，MANO模型具有运动链结构，手腕处的微小误差会沿链条层级累积，导致指尖出现显著位移，使得重建结果对局部误差高度敏感。

现有方法主要分为两类：一类利用MANO作为强先验，但受限于上述误差累积问题；另一类直接回归3D顶点坐标，虽避免了关节依赖，但缺乏参数化先验，常产生手指融合或表面不连续等伪影。这两类方法在精度与效率之间难以兼得，特别是当模型规模增大以提升精度时，推理速度往往无法满足实时应用需求。TokenHand的切入点在于引入离散表示，将连续的空间回归问题转化为离散的分类问题，从而在保留结构先验的同时，大幅降低解码器的计算复杂度。

## 核心方法

### 方法参照系

本文问题属于单目3D手姿估计中的确定性回归路线，但与传统回归连续MANO参数或顶点坐标不同，TokenHand将重建任务重构为对离散Codebook索引的分类。其关键差异在于，通过量化编码阶段将几何先验嵌入离散空间，使得解码器无需处理复杂的连续值回归，从而实现了轻量化。

### 离散Token化表示

传统方法直接回归连续坐标，导致解码器参数庞大且易产生非物理结构。TokenHand借鉴VQ-VAE思想，引入共享Codebook $C \in \mathbb{R}^{K \times D}$，将3D手部点云 $H$ 映射为 $M$ 个离散Token。每个Token $t_i$ 通过最近邻查找量化为Codebook索引 $k$，公式为：

$$ q(t_i) = \arg \min_j \| t_i - c_j \|_2 $$

这一设计将手部几何分解为独立的子结构，每个Token对应特定的局部区域。由于Token间存在冗余，该表示增强了空间覆盖能力，同时避免了MANO运动链的误差累积，使得局部重建错误不会传播至全局。

### 分类式重建与轻量解码

在重建阶段，TokenHand将图像特征 $X_b$ 通过关键点引导采样生成Token特征 $X_m$，并预测其分类Logits $\hat{L}$。为了解决量化过程中的梯度断裂问题，采用软推理方案 $S = \hat{L} \times C$ 进行线性插值，再送入冻结的解码器 $f_d$ 重建网格。损失函数包含交叉熵损失 $\ell_{cls}$ 与重建损失 $\ell_{rec}$：

$$ \ell_{all} = \ell_{cls} + \ell_{rec} $$

其中 $\ell_{rec}$ 监督顶点、3D关节与2D关节的L1误差。这种分类式重建使得解码器仅需处理离散索引，参数量降至3.0M，相比传统Transformer方法减少约90%，从而在NVIDIA 2080 Ti上实现65 FPS的实时推理。

## 实验评估

| 方法 | Backbone | PA-MPJPE (mm) | PA-MPVPE (mm) | FPS |
| :--- | :--- | :--- | :--- | :--- |
| MeshGraphormer | HRNet | 6.3 | 6.5 | - |
| FastMETRO | HRNet | 6.5 | 7.1 | - |
| Zhou et al. | HRNet | 5.8 | 6.1 | - |
| TokenHand | FastViT-MA36 | 5.7 | 5.9 | 65 |

在FreiHAND数据集上，TokenHand取得了5.7 mm的PA-MPJPE，优于MeshGraphormer的6.3 mm和FastMETRO的6.5 mm，且推理速度达到65 FPS。基线覆盖了METRO、MeshGraphormer等经典Transformer方法，但缺失HaMeR、WiLoR等大规模预训练基线，这可能限制了其在野外场景泛化能力上的对比。

| 配置 | PA-MPJPE (mm) | PA-MPVPE (mm) |
| :--- | :--- | :--- |
| Codebook 384×512 | 4.9 | 5.2 |
| Regressor [48, 97, 194, 389] | 5.7 | 5.9 |
| Regressor [48, 128, 256, 512] | 5.9 | 6.1 |

消融实验显示，Codebook大小在384×512至640×512范围内对精度影响较小，表明所选尺寸已足够表达手部几何多样性。解码器结构方面，采用[48, 97, 194, 389]的渐进式Token扩展策略优于[48, 128, 256, 512]的均匀扩展，PA-MPJPE降低0.2 mm，验证了层级化特征聚合的有效性。

评估指标包含PA-MPJPE、PA-MPVPE及FPS，但未报告置信区间。实验仅在FreiHAND和DexYCB上进行，缺乏对严重遮挡场景的专门测试。代码未公开，但超参数（如损失权重 $w_{rec}=10, \beta=5$）已详细列出，复现性中等。

## 关联研究分析

从问题动机看，TokenHand与FastMETRO均致力于解决Transformer解码器的计算瓶颈，但FastMETRO通过编码器-解码器分离减少参数，而TokenHand通过离散化改变任务本质。FastMETRO仍回归连续坐标，受限于解码器复杂度；TokenHand的分类范式使得解码器可冻结，从而在保持精度的同时大幅降低延迟。这一差异源于对“几何先验”的不同利用方式：FastMETRO依赖数据驱动学习，TokenHand依赖离散空间的结构约束。

从方法设计看，TokenHand与HaMeR代表了效率与精度的不同取舍。HaMeR通过ViT-Huge骨干和大规模预训练提升野外鲁棒性，但推理速度慢；TokenHand采用轻量级FastViT-MA36，牺牲了大规模预训练带来的泛化能力，换取实时性。在DexYCB上，TokenHand的MPJPE为12.3 mm，显著高于UniHand的3.48 mm，这可能源于训练数据规模与预训练策略的差异。TokenHand未验证其在复杂野外场景下的表现，其离散表示对细微姿态变化的捕捉能力是否足以应对真实世界的多样性，尚存疑问。

## 总结

TokenHand旨在解决单目手姿估计中精度与实时性的矛盾，通过离散Token分类重构重建任务，规避了MANO运动链误差累积与连续回归的计算开销。该方法在FreiHAND上实现5.7 mm PA-MPJPE与65 FPS，证明了离散表示在效率-精度权衡上的优势。然而，实验仅覆盖受控数据集，缺乏对严重遮挡与野外场景的验证，且未与大规模预训练基线对比。当输入图像存在严重遮挡或背景杂乱时，离散Token分类的鲁棒性是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_8af062843c87)