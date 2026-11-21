# CVPR2026最新论文 ｜LiteSense: Lifting Lightweight ToF with RGB for High-Resolution Metric Depth Estimation ｜轻量ToF与RGB融合的高分辨率度量深度估计

研究机构：同济大学

作者：Yusheng Li、Lizhi Lou、Yan Tang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7813ec75cc73)

> 度量深度估计旨在从视觉观测中恢复具有绝对尺度的稠密深度图，是自动驾驶与机器人导航的底层感知能力。现有方案要么依赖参数量巨大的单目基础模型导致边缘部署困难，要么使用高分辨率主动传感器造成硬件成本过高，而轻量ToF传感器虽提供绝对尺度先验，但其8×8的低分辨率输出无法独立重建场景细节。LiteSense通过引入ToF传感器固件生成的紧凑归一化直方图（Compact Normalized Histogram, CNH）信号，设计了块状局部交叉注意力融合模块，在仅5.48M参数的约束下实现了接近SOTA的精度。该方法在资源受限场景下提供了替代大模型的可行路径，但其对ToF传感器有效量程的依赖及跨域泛化的边界仍需进一步验证。

## 研究背景

度量深度估计的核心困境在于单目视觉缺乏绝对尺度先验，而主动传感器虽能提供尺度信息却受限于分辨率或成本。单目深度估计（Monocular Depth Estimation, MDE）模型如Depth Anything通过大规模无标签数据学习相对几何，但缺乏显式度量监督，导致绝对尺度恢复不稳定。为弥补这一缺陷，研究者引入主动传感器作为辅助先验，其中轻量飞行时间（Time-of-Flight, ToF）传感器因成本低、体积小成为边缘设备的首选，但其输出仅为8×8的低分辨率深度网格，无法直接用于稠密重建。

主流辅助引导深度估计路线存在两条技术分支：一是利用稀疏LiDAR点云作为提示嵌入单目网络，二是融合轻量ToF的深度与方差图。DELTAR（Kim et al., 2024）首次将多区域ToF模块与RGB图像融合，但通过高斯分布采样离散深度值，丢弃了原始传感器输出的分布细节，且模型参数量较大，难以满足实时部署需求。LiteSense的切入点在于直接利用ToF传感器固件生成的CNH信号，该信号以18个离散深度bin的形式紧凑保留了区域内光子返回的完整分布信息，避免了高斯近似带来的信息损失，从而在极低参数量下实现更鲁棒的度量深度估计。

## 核心方法

### 方法参照系

LiteSense属于辅助引导度量深度估计（Auxiliary-Guided Metric Depth Estimation）路线，其标准流程为：提取RGB与辅助深度特征，通过注意力机制融合，解码为稠密深度图。与LiDAR稀疏点补全不同，ToF提供的是空间连续但分辨率极低的深度图，且伴随独立的直方图分布信号，这要求融合策略必须处理模态间的分辨率失配与分布信息的局部对齐。

### 混合特征提取与CNH编码

针对ToF深度图分辨率低（8×8）与RGB图像高分辨率（416×416）之间的巨大尺度差异，LiteSense采用MobileNetV4骨干网络提取RGB-D特征。ToF深度图经上采样后与RGB图像拼接形成4通道输入，提供全局尺度先验。对于CNH信号，每个ToF区域生成一个18-bin的归一化直方图，共64个独立分布。设计动机在于：DELTAR使用均值和方差拟合高斯分布并采样，丢弃了多峰分布的细节；而CNH直接保留了原始物理信号，通过MLP编码器（无下采样）将每个直方图映射为固定维度向量，确保分布形态信息完整传递至后续融合阶段。

### 块状CNH空间注入（PCSI）

全局交叉注意力会导致空间无关区域的CNH分布相互干扰，因为不同ToF区域的深度分布缺乏相关性。PCSI模块将RGB-D特征图 $F \in \mathbb{R}^{H \times W \times C_I}$ 和CNH嵌入 $H \in \mathbb{R}^{N^2 \times C_H}$ 均匀划分为 $N \times N$ 个非重叠块，每个块通过1×1卷积投影至统一维度。局部调制通过交叉注意力实现，其中RGB-D特征作为Query，对应块的CNH特征作为Key和Value：

$$
\tilde{F}_i = \phi(F_i, H_i) = \text{CrossAttention}(Q=F_i, K=H_i, V=H_i)
$$

该公式的物理含义是：每个空间块的深度结构估计仅受其对应ToF区域直方图分布的引导，实现了区域级的局部融合。消融实验表明，移除PCSI改用全局注意力后，RMSE从0.197m上升至0.352m，证明局部约束对抑制跨区域干扰至关重要。PCSI仅在1/2和1/4分辨率的高层特征上操作，避免低层特征因块状分割产生边界伪影，同时保证每个块包含足够的空间样本以与CNH分布有效交互。

## 实验评估

LiteSense在NYUv2和SUN RGB-D上进行了域内与零样本评估，基线覆盖单目度量深度估计（MMDE）方法（AdaBins, ZoeDepth, Metric3D-V2-L, DA-V2-S, HybridDepth）和辅助引导方法（DELTAR, PriorDA-S）。在NYUv2域内测试中，LiteSense以5.48M参数和33.87G FLOPs的最低计算成本，取得了0.197m RMSE和0.029 AbsRel，优于DELTAR（0.311m RMSE, 0.064 AbsRel）和PriorDA-S（0.697m RMSE, 0.134 AbsRel），但略逊于HybridDepth（0.183m RMSE, 0.047 AbsRel）。

| 方法 | 参数量 (M) | FLOPs (G) | δ1 ↑ | RMSE ↓ (m) | AbsRel ↓ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HybridDepth | 59.15 | 377.82 | 0.989 | 0.183 | 0.047 |
| DELTAR | 18.55 | 79.98 | 0.952 | 0.311 | 0.064 |
| LiteSense | 5.48 | 33.87 | 0.982 | 0.197 | 0.029 |

消融实验揭示了CNH信号的关键作用：仅使用ToF深度通道（Chan.）时RMSE为0.453m，加入CNH特征（Feat.）后降至0.359m，同时启用PCSI模块后进一步降至0.197m。这表明CNH分布信息比单一深度值提供了更丰富的结构约束，而PCSI的局部融合策略是释放这一信息潜力的必要条件。在SUN RGB-D零样本测试中，LiteSense取得0.228m RMSE，显著优于DELTAR的0.367m，验证了其在未见室内场景下的泛化能力。

评估边界方面，LiteSense在THDR3K真实传感器数据集上表现稳健，但论文未报告KITTI等室外基准结果，且ToF传感器有效量程约4.0m，超过3.5m后精度下降。代码与数据集已开源，训练使用单张RTX 3090 GPU，50 epochs，batch size 32，超参数公开，可复现性良好。

## 关联研究分析

从问题动机看，LiteSense与DELTAR同属RGB-ToF融合路线，但二者对辅助信息利用方式存在根本差异。DELTAR将ToF深度建模为高斯分布并采样离散值，本质上是压缩分布信息以适配网络输入；LiteSense则直接保留CNH原始直方图，通过PCSI模块在特征空间进行局部对齐。这一差异源于对传感器信号物理特性的理解：CNH是固件生成的紧凑表示，保留了多峰分布细节，而高斯近似在复杂场景下会丢失次要峰值信息。LiteSense在NYUv2上AbsRel从0.064降至0.029，证明分布细节对尺度精度的贡献超过了单一深度值。

从方法设计看，LiteSense与EfficientPENet同属高效网络架构路线，但融合机制截然不同。EfficientPENet针对LiDAR稀疏点设计传播机制，依赖空间邻域关系；LiteSense针对ToF连续低分辨率网格设计块状局部注意力，依赖区域级分布对齐。这种差异由传感器特性决定：LiDAR点云稀疏且不规则，需全局传播；ToF网格规则且连续，块状对齐即可保证空间对应。LiteSense未探索LiDAR与ToF的联合融合，也未评估动态场景下ToF失效时的鲁棒性，其方法边界局限于静态室内场景。

## 总结

LiteSense解决的核心矛盾是轻量ToF传感器低分辨率输出与高分辨率深度重建需求之间的冲突，以及单目模型缺乏绝对尺度先验的问题。其切入点在于利用ToF固件生成的CNH信号，通过PCSI模块实现区域级分布对齐，避免了高斯近似的信息损失。该方法在5.48M参数约束下实现了0.197m RMSE（NYUv2）和0.228m RMSE（SUN RGB-D零样本），证明了轻量级专用网络在特定硬件约束下可替代大模型。其边界在于ToF传感器4.0m有效量程的限制，以及未评估室外场景与动态环境的鲁棒性。当ToF传感器在远距离或动态场景下失效时，CNH分布信号的可靠性如何变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7813ec75cc73)