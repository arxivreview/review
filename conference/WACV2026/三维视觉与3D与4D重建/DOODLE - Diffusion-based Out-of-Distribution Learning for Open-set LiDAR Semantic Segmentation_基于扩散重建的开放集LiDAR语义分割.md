# WACV2026最新论文 ｜DOODLE: Diffusion-based Out-of-Distribution Learning for Open-set LiDAR Semantic Segmentation ｜基于扩散重建的开放集LiDAR语义分割

研究机构：韩国科学技术院

作者：Changgyoon Oh、Hyeonseong Kim、Daehyun We 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45c5a6edb7aa)

> 开放集LiDAR语义分割旨在区分已知类别与未知类别，但现有方法依赖冗余分类器或合成异常样本，易受点云稀疏性影响导致高假阳性率。DOODLE利用潜扩散模型重建分布内语义特征，通过重建误差量化OOD分数，并引入密度感知后处理抑制噪声。该方法作为插件模块集成于现有骨干网络，在SemanticKITTI和nuScenes上刷新了SOTA。其有效性依赖于扩散模型对特征流形的精确建模，但在复杂城市场景下的泛化能力仍存疑。

## 研究背景

LiDAR点云具有无序、稀疏且语义信息贫乏的特性，直接应用2D领域的OOD检测算法往往失效，因为高维空间中的距离度量无法有效区分未知物体。为解决此问题，开放集识别框架引入了冗余分类器，专门学习未知类别的判别边界，而正常分类器处理已知类别。然而，这种判别式方法缺乏对数据分布内在结构的建模，导致在点云密度不均的真实驾驶场景中，孤立噪声点极易被误判为未知物体。

现有3D开放集分割的主流路线包括基于随机缩放模拟未知类的REAL，以及利用ShapeNet生成合成异常样本的LiON。REAL的缩放操作破坏了LiDAR的自然采样几何结构，而LiON依赖外部数据集生成的异常样本与真实LiDAR分布存在域差距。尽管这些方法能区分已知与未知，但假阳性率居高不下，限制了其在安全关键场景的部署。DOODLE的切入点在于利用生成式模型学习分布内（In-Distribution, ID）特征的流形结构，将OOD检测转化为特征重建误差的度量，从而摆脱对人工合成异常样本或几何畸变操作的依赖。

## 核心方法

### 方法参照系

DOODLE建立在预训练开放集分割模型之上，该模型包含特征提取器、正常分类器和冗余分类器。标准流程是提取点云特征后，由冗余分类器直接输出OOD分数。DOODLE的关键差异在于不直接信任冗余分类器的输出，而是引入潜扩散模型（Latent Diffusion Model, LDM）对特征进行重建，利用重建一致性作为OOD证据的补充信号。

### 特征空间扩散重建

传统方法在像素或点坐标空间进行生成，忽略了语义特征的内在结构。DOODLE将语义特征投影至Range-view表示，并通过向量量化变分自编码器（Vector-Quantized Variational Autoencoder, VQ-VAE）压缩至低维潜空间，以抑制高频噪声并降低计算成本。设计动机在于，扩散模型在语义嵌入空间训练比在原始数据空间训练更能捕捉类别间的语义边界。训练时，仅对ID区域进行重建，通过掩码机制$\mathcal{M}$排除OOD区域：

$$ \mathcal{F}_{\mathrm{range}}^{\mathrm{in}} = \mathcal{M} \odot \mathcal{F}_{\mathrm{range}} $$

其中$\mathcal{M}$为二值掩码，ID区域为1，OOD区域为0。扩散模型学习ID特征的去噪过程，推理时计算输入特征与重建特征的差异作为OOD分数。这一机制使得OOD分数不仅反映分类置信度，还反映特征在ID流形上的偏离程度，从而降低对孤立噪声点的敏感度。

### 密度感知后处理

扩散重建产生的OOD分数仍受LiDAR点云随距离稀疏化的物理特性影响，远端点云稀疏导致重建误差增大，易产生假阳性。DOODLE引入密度感知后处理（Density-Aware Post-processing, DAP）模块，利用HDBSCAN聚类识别潜在OOD区域，并基于深度校正密度。设计动机在于，真实物体在LiDAR扫描中通常形成连贯的簇，而噪声点往往孤立存在。DAP计算每个簇的密度$\rho_j$，并应用深度校正因子，对远端稀疏簇进行密度放大，对近端密集簇进行抑制。校正后密度低于阈值$\tau_{density}$的簇被视为假阳性，其分数被衰减。这一模块显式建模了传感器物理特性，弥补了纯数据驱动方法在空间分布上的盲区。

## 实验评估

实验在SemanticKITTI和nuScenes验证集上进行，基线包括REAL、LiON及APF。DOODLE作为插件模块集成于LiON和REAL之上。在SemanticKITTI上，LiON+DOODLE的AUPR从44.68%提升至46.53%，AUROC从92.69%提升至93.98%；在nuScenes上，AUPR从31.58%提升至33.95%，AUROC从95.24%微增至95.26%。

| 方法 | SemanticKITTI AUPR | SemanticKITTI AUROC | nuScenes AUPR | nuScenes AUROC |
| :--- | :--- | :--- | :--- | :--- |
| LiON | 44.68 | 92.69 | 31.58 | 95.24 |
| LiON + DOODLE | 46.53 | 93.98 | 33.95 | 95.26 |
| REAL | 20.08 | 84.90 | 21.20 | 84.50 |
| REAL + DOODLE | 22.17 | 85.72 | 22.53 | 84.76 |

消融实验显示，扩散重建与DAP模块具有互补性。单独使用扩散重建（无DAP）在SemanticKITTI上AUPR为45.20%，加入DAP后提升至46.53%。深度校正密度模块贡献了+0.32%p的AUPR增益。扩散噪声集成次数从1次增至5次，AUPR和AUROC均单调提升，表明集成平均有效缓解了扩散采样的随机性。

评估边界方面，论文未报告计算效率指标，5次集成平均显著增加了推理延迟。代码已开源，超参数如$\tau_{score}$、$\tau_{density}$等已公开，但缺乏跨传感器配置的泛化性测试。nuScenes上AUROC几乎无提升，暗示扩散模型在复杂城市场景的OOD区分力可能受限于训练数据分布的覆盖度。

## 关联研究分析

从问题动机看，DOODLE与Neural Distribution Prior (NDP) 形成机制对比。NDP通过学习点级分布先验来检测OOD，属于判别式方法，计算高效但难以捕捉复杂的几何-语义耦合关系。DOODLE采用生成式重建，通过显式建模ID流形来识别偏离，虽然计算成本高，但在SemanticKITTI上AUROC达到0.92，优于NDP的0.90。这一差异源于LiDAR点云的非欧结构，生成式模型在Range-view投影后能更好地利用2D卷积归纳偏置，而NDP的分布建模可能忽略了空间局部性。

从方法设计看，DOODLE与LiDiff在扩散模型应用上存在根本差异。LiDiff将扩散模型用于场景补全，在点云坐标空间去噪，目标是恢复几何结构。DOODLE将扩散模型用于特征空间重建，目标是学习语义流形。这种差异导致DOODLE对语义混淆的鲁棒性更强，但对几何细节的恢复能力较弱。LiDiff在SemanticKITTI场景补全任务中Chamfer Distance为0.12 m²，而DOODLE不涉及几何重建，因此无法直接对比。DOODLE的设计表明，扩散模型在感知任务中的应用已从数据生成转向特征表征学习，这一转变是否适用于其他3D任务，如目标检测，尚需验证。

## 总结

DOODLE解决了开放集LiDAR分割中假阳性率高的核心矛盾，切入点在于利用扩散模型学习ID特征流形，将OOD检测从判别式分类转化为生成式重建误差度量。该方法通过VQ-VAE压缩特征并引入密度感知后处理，在SemanticKITTI上将LiON的AUPR从44.68%提升至46.53%。其边界在于nuScenes上AUROC几乎无提升，且5次集成平均带来的计算开销限制了实时性。当训练数据分布覆盖度不足时，扩散模型的重建误差是否仍能准确反映OOD程度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_45c5a6edb7aa)