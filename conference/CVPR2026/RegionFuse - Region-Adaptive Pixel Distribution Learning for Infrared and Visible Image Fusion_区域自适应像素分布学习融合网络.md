# CVPR2026最新论文 ｜RegionFuse: Region-Adaptive Pixel Distribution Learning for Infrared and Visible Image Fusion ｜区域自适应像素分布学习融合网络

研究机构：北京理工大学

作者：Jianghan Xia、Hong Song、Jinfu Li 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70daa2c16984)

> 红外可见光图像融合（IVIF）旨在整合热辐射与纹理细节，但现有固定或样本级自适应范式无法应对图像内部非均匀光照导致的区域级模态可靠性差异。本文提出RegionFuse，通过区域自适应像素分布学习动态生成融合权重，解决过曝与欠曝区域的信息丢失问题。该方法引入区域混合注意力机制与特征压缩模块，在四个基准上取得SOTA结果。其区域级动态权重设计有效提升了非均匀光照下的融合质量，但跨区域依赖建模的缺失限制了其在复杂场景中的泛化能力。

## 研究背景

当可见光图像在夜间或强光环境下出现局部过曝或欠曝时，单一模态的纹理或热信息会失效，此时需依赖另一模态补充。这种图像内部像素分布的空间不一致性，使得全局统一的融合权重无法同时保留不同区域的有效信息，构成了区域自适应融合的核心挑战。解决此问题需先理解模态互补性（Modality Complementarity），即红外对热辐射敏感但缺乏纹理，可见光纹理丰富但受光照干扰，两者在物理感知上存在固有盲区。

IVIF的主流路线从像素级重建演进至特征级融合，CDDFuse等基于Transformer的方法通过全局注意力捕捉长距离依赖，但计算复杂度呈二次方增长且无法区分区域级光照差异。PIAFusion引入光照感知损失，MoE-Fusion采用混合专家（Mixture of Experts, MoE）实现样本级动态路由，但这些方法仍停留在图像全局层面，未能处理同一图像内不同区域模态可靠性的空间变化。RegionFuse的切入点在于将融合粒度从样本级细化至区域级，通过学习局部像素分布动态调整融合权重，使过曝区域侧重红外信息，正常光照区域保留可见光细节。

## 核心方法

### 方法参照系

RegionFuse遵循编码器-融合-解码器的标准IVIF架构，但关键差异在于融合阶段采用区域自适应动态权重而非固定或全局动态权重。其编码器基于X-Restormer块构建多粒度Transformer（Multi-Granular Transformer, MGT）编码器，提取区域级细粒度特征与全局粗粒度特征，为后续区域自适应融合提供基础。

### 区域混合注意力机制

MoRA机制将MoE的任务分解能力与注意力的特征交互能力结合，实现区域级动态融合。设计动机在于解决现有方法无法在图像内部空间维度上区分模态可靠性的问题。MoRA首先通过区域嵌入层将特征图划分为区域token，引入重叠分区机制缓解区域边界处的像素强度不连续性，最终区域大小 $R = (1 + \gamma)R_o$，其中 $R_o$ 为原始区域大小，$\gamma$ 为随深度增加的重叠比例。随后，区域像素分布感知路由器通过多层感知机（MLP）与Softmax函数预测每个区域的责任分数：

$$S = \text{Softmax}(\text{MLP}(\text{RSP}(X)))$$

该公式将输入特征 $X$ 重塑为区域表示后，计算每个区域属于不同像素分布类别的概率，实现区域级路由。每个专家内部执行掩码注意力，仅与相同像素分布的区域交互：

$$\text{ATTN}_e(Q, K, V) = \text{Softmax}(M_e \odot QK^T / \alpha)V$$

其中 $M_e$ 为注意力掩码，$\alpha$ 为可学习缩放参数。MoRA输出为各专家注意力的加权平均，权重由责任分数矩阵 $S^{(e)}$ 决定。这一设计使不同区域能根据局部像素分布选择最适合的融合策略，避免全局权重在过曝区域引入冗余红外噪声或在正常区域丢失可见光纹理。

### 区域特征压缩模块

RFCM模块置于每个MoRA块之后，解决高维区域特征注意力计算成本过高的问题。设计动机在于MoRA生成的区域特征包含大量冗余信息，直接用于后续融合会引入噪声并增加计算负担。RFCM首先将输入特征图重塑为区域补丁 $F_r \in \mathbb{R}^{\frac{H}{R} \times \frac{W}{R} \times C \times R \times R}$，然后通过通道注意力模块增强关键特征并抑制冗余特征：

$$F'_r = M_c(F_r) \odot F_r, \quad M_c(F_r) = \text{Sigmoid}(\text{Conv}(\text{GAP}(F_r)))$$

该公式通过全局平均池化（GAP）提取区域级通道统计信息，经卷积与Sigmoid生成通道注意力图，实现区域级特征选择。随后通过 $1 \times 1$ 卷积与LeakyReLU激活降低特征维度，输出压缩后的区域特征 $F'_{r,\text{out}} \in \mathbb{R}^{\frac{H}{R} \times \frac{W}{R} \times C' \times R \times R}$，最终合并为压缩输出特征图 $F_{r,\text{out}} \in \mathbb{R}^{C' \times H \times W}$。RFCM通过区域级特征压缩，在保留关键区域信息的同时降低计算复杂度，使RegionFuse能在高分辨率图像上保持可接受的推理速度。

## 实验评估

RegionFuse在MSRS、RoadScene、M3FD、TNO四个数据集上评估，使用SF、AG、VIF、Qabf、Qcb五项指标。基线覆盖CDDFuse、DDFM、SHIP、DCE、SAGE、A2R、PIAFusion等主流方法，但缺失FusionFM等生成式模型与MagicFuse等最新SOTA。在MSRS数据集上，RegionFuse的VIF达到1.063，显著超越CDDFuse的0.85与DCE的1.10（据领域综述，DCEvo在M3FD上VIF为0.87，本文MSRS结果因数据集差异不可直接比较）。M3FD检测任务中，RegionFuse的mAP@0.5为86.50%，在Lamp与Motorcycle类别上取得最佳AP，但Car与Truck类别为次优，表明区域自适应权重对纹理保留敏感的目标类别提升更显著。

消融实验显示，移除MoRA导致VIF从1.063降至1.060，移除RFCM导致VIF降至1.018，表明RFCM对特征质量的影响大于MoRA。移除负载平衡损失（Lload）后VIF降至1.036，说明路由器训练稳定性对最终性能有显著影响。将区域自适应退化为样本自适应（Region→Sample）后，VIF降至1.039，验证了区域级粒度优于样本级粒度的假设。在极端光照条件下（k从1.5到5.0），RegionFuse在SF、AG、VIF、Qabf四项指标上均优于所有对比方法，且随k值增加优势更明显，证明其对非均匀光照的鲁棒性。

评估协议存在局限：VIF指标在MSRS上超过1.0，可能因计算方式差异导致虚高，需与领域标准协议对齐验证。代码已开源，训练使用NVIDIA RTX 4090 GPU，Adam优化器，80 epochs，初始学习率 $10^{-4}$，batch size 8。检测任务使用YOLOv5s预训练模型，M3FD数据集按8:1:1划分。论文未报告置信区间与计算效率指标（FLOPs、推理速度），限制了与实时性要求高的应用场景的对比。

## 关联研究分析

从问题动机看，RegionFuse与MoE-Fusion同属动态融合路线，但MoE-Fusion在样本级路由不同图像至不同专家，而RegionFuse在区域级路由同一图像的不同区域至不同专家。这一差异源于任务特性：MoE-Fusion假设不同图像属于不同子任务，而RegionFuse假设同一图像内部存在空间变化的子任务。MoE-Fusion未探索图像内部非均匀光照问题，RegionFuse的区域级路由是其直接演进，但MoE-Fusion的样本级路由在光照均匀场景中可能更高效，论文未给出两者在不同光照均匀度下的性能对比。

从方法设计看，RegionFuse与PIAFusion均关注光照感知，但PIAFusion通过全局光照估计生成融合权重，RegionFuse通过区域梯度加权生成局部权重。PIAFusion的光照感知损失是全局约束，RegionFuse的增强强度损失利用局部区域平均梯度 $G_v(i,j)$ 与 $G_r(i,j)$ 计算掩码 $M$，实现区域级光照自适应。这一设计差异源于对光照变化粒度的理解：PIAFusion假设光照变化是图像全局属性，RegionFuse假设光照变化是空间局部属性。PIAFusion未处理图像内部非均匀光照，RegionFuse的区域级设计是其关键改进，但区域划分粒度 $R$ 对性能的影响未充分消融，小目标检测中区域过大可能导致目标信息被稀释。

## 总结

RegionFuse解决的核心矛盾是固定融合范式无法应对图像内部非均匀光照导致的区域级模态可靠性差异。现有方法如MoE-Fusion与PIAFusion仅在样本级或全局层面动态调整权重，无法区分同一图像内不同区域的像素分布差异，导致过曝区域引入冗余红外噪声或正常区域丢失可见光纹理。RegionFuse通过MoRA机制实现区域级动态路由，结合RFCM压缩区域特征，在MSRS上VIF达1.063，M3FD检测mAP@0.5达86.50%，验证了区域自适应权重的有效性。其边界在于MoRA仅实现区域内交互，未建模跨区域依赖，当目标跨越多个区域时，区域级路由可能无法捕捉全局上下文。当区域划分粒度 $R$ 增大时，MoRA对跨区域目标的融合质量是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_70daa2c16984)