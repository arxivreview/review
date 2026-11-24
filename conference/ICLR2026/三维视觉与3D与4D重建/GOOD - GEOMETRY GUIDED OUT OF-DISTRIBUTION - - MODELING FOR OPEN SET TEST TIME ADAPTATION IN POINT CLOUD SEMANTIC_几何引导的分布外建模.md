# ICLR2026最新论文 ｜GOOD: GEOMETRY GUIDED OUT OF-DISTRIBUTION - - MODELING FOR OPEN SET TEST TIME ADAPTATION IN POINT CLOUD SEMANTIC SEGMENTATION ｜几何引导的分布外建模

研究机构：同济大学

作者：Tianpei Zou、Guo Yu、Ya Wu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_78404819)

> 3D点云语义分割在部署时面临目标域出现训练集未见类别的语义偏移，传统测试时适应（Test-time Adaptation, TTA）方法仅处理已知类别的协变量偏移，导致模型对未知物体产生高置信度误判。现有2D开放集TTA方法直接迁移至3D点云时，因ID/OOD点数量极度失衡而失效，将大量已知点误判为未知。本文提出GOOD框架，通过超点聚类缓解失衡，结合超点置信度与ID原型实现开放集在线适应。该方法在Synth4D到SemanticKITTI任务上mIoU提升4.83%，AUROC达73.39%，但在OOD完全缺失场景下的鲁棒性边界尚待进一步验证。

## 研究背景

自动驾驶场景中的LiDAR点云在部署时可能遭遇训练域未覆盖的物体类别，这种语义偏移导致模型将未知物体错误分类为已知类别，例如将自行车误判为植被。测试时适应（TTA）通过利用无标签目标域数据在线更新模型参数来应对分布偏移，但现有TTA-3DSeg方法如GIPSO和HGL仅关注已知类别的协变量偏移，缺乏对未知类别的显式识别机制。开放集测试时适应（OSTTA）旨在同时解决在线优化与开放集检测，但2D图像领域的OSTTA方法依赖实例级处理，直接应用于3D点云时因ID/OOD点数量失衡而失效。

3D点云数据中已知（ID）点占绝对主导，未知（OOD）点稀疏甚至缺失，这种极端失衡导致基于单点置信度的OOD检测方法将大量ID点误判为OOD，破坏分割性能。现有方法假设OOD样本充足以辅助ID/OOD区分，但户外LiDAR场景中该假设不成立。本文切入点在于利用点云的几何结构特性，将识别任务从点级提升至超点级，通过空间聚合缓解数量失衡，并引入原型机制校正高斯混合模型（GMM）在OOD稀疏时的误判。

## 核心方法

### 方法参照系

本文问题属于开放集测试时适应（OSTTA-3DSeg），即在无源域数据访问条件下，在线适应目标域同时识别ID/OOD点。与标准TTA的关键差异在于目标域包含训练集未见类别，要求模型在优化ID分割性能的同时拒绝OOD点。通用OSTTA流程包含伪标签生成、ID/OOD判别与在线优化三个环节，本文在ID/OOD判别环节引入几何先验。

### 超点表示分支

标准OSTTA方法基于单点置信度进行ID/OOD判别，在ID/OOD极度失衡时失效。本文通过超点聚类将离散点聚合为空间连贯的超点，利用超点纯度与熵构建置信度指标。超点纯度 $C_k^{pur}$ 衡量超点内预测标签的一致性：

$$C_k^{pur} = \frac{1}{N_k} \sum_{j \in S_k} \mathbb{1}_c(\arg\max \hat{p}_{j,c})$$

其中 $N_k$ 为超点 $S_k$ 的点数，$\mathbb{1}_c$ 为指示函数。超点熵 $C_k^{ent}$ 采用softmax概率替代硬标签以捕捉分布不确定性，最终置信度 $C_k^{sup} = C_k^{ent} \cdot C_k^{pur}$。该设计解决了单点置信度在ID主导场景下区分度不足的问题，通过空间聚合提升OOD检测的稳定性。

### 超点ID原型与时间伪标签

GMM基于超点置信度进行ID/OOD分割，但在OOD样本稀疏或缺失时强制分割出OOD簇，导致ID超点误判。本文引入超点ID原型 $\rho_c^t$ 校正GMM误判：

$$\rho_c^t = \alpha \hat{\rho}_c^{t-1} + (1-\alpha) \frac{1}{N_c} \sum_{k \in N_c} z_k^t$$

其中 $z_k^t$ 为超点嵌入特征均值，$\alpha=0.99$ 为EMA系数。通过计算OOD超点与ID原型的余弦相似度，将相似度超过阈值 $\tau=0.85$ 的超点重新标记为ID。时间伪标签分支利用K-NN在连续帧间建立时空邻域，仅当当前帧与历史帧预测一致时生成ID伪标签，提升在线优化的稳定性。该设计解决了GMM在OOD缺失场景下的过分割问题，同时利用时序一致性抑制伪标签噪声。

## 实验评估

实验在Synth4D到SemanticKITTI、Synth4D到nuScenes、SynLiDAR到SemanticKITTI三个基准上进行，骨干网络为MinkowskiUNet-18，体素大小0.05。基线覆盖GIPSO、HGL等TTA-3DSeg方法及UniEnt、WCEM等2D OSTTA方法，但未对比最新Mamba骨干或纯无监督分割方法。

| 方法 | mIoU (%) | AUROC (%) | FPR95 (%) |
| :--- | :--- | :--- | :--- |
| Source | 40.26 | 65.80 | 78.39 |
| HGL | +2.90 | 64.40 | 79.82 |
| GOOD | +4.83 | 73.39 | 71.91 |

在Synth4D到SemanticKITTI任务中，GOOD相比HGL在mIoU、AUROC、FPR95上分别提升1.93%、8.99%、7.91%。消融实验显示，超点置信度（SC）引入后AUROC从66.66%提升至71.47%，但mIoU微降0.07%；超点ID原型（SIDP）进一步将AUROC提升至73.39%，mIoU恢复至+4.83%。SIDP对OOD稀疏场景的校正效果显著，验证了原型机制在缓解GMM误判中的关键作用。

评估指标包含mIoU、AUROC、FPR95，覆盖封闭集与开放集性能。评估协议假设可靠自定位（pose）用于时间对齐，未测试pose噪声下的鲁棒性。论文未提供代码URL，超参数 $\lambda=0.1$、$w=3$、$\tau=0.85$ 已公开，但DBSCAN聚类参数细节仅在附录中提及。

## 关联研究分析

从问题动机看，GOOD与HGL同属TTA-3DSeg路线，但HGL仅处理协变量偏移，GOOD扩展至语义偏移。HGL的局部-全局伪标签策略在封闭集下有效，但缺乏OOD识别机制，导致在开放集场景下对未知物体产生高置信度误判。GOOD通过超点几何先验引入OOD检测能力，解决了HGL在语义偏移下的失效问题。这一差异源于任务定义的不同：HGL假设目标域类别集与源域一致，GOOD则显式处理类别集扩展。

从方法设计看，GOOD与2D OSTTA方法UniEnt在ID/OOD判别机制上存在根本差异。UniEnt基于实例级熵最大化进行OOD检测，直接迁移至3D点云时因ID/OOD点数量失衡导致大量ID点被误判为OOD，mIoU反而下降。GOOD通过超点聚合将判别单元从点提升至超点，利用空间连贯性缓解数量失衡，同时引入ID原型校正GMM误判。这一设计选择源于3D点云的几何结构特性，2D图像缺乏类似的空间聚合先验，因此无法直接复用UniEnt的实例级判别机制。

## 总结

本文核心矛盾在于3D点云开放集TTA中ID/OOD点数量极度失衡导致现有方法失效。GOOD通过超点聚类缓解失衡，结合超点置信度与ID原型实现鲁棒的ID/OOD判别，在Synth4D到SemanticKITTI任务上mIoU提升4.83%，AUROC达73.39%。方法边界在于依赖可靠自定位进行时间对齐，未测试pose噪声下的性能退化；超点聚类引入约0.7秒延迟，可能限制实时性要求极高的自动驾驶场景。当OOD样本完全缺失时，GMM是否仍会强制分割出OOD簇，SIDP的校正能力是否足以应对极端稀疏场景，论文未给出系统性验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_78404819)