# CVPR2026最新论文 ｜OccuFly: A 3D Vision Benchmark for Semantic Scene Completion from the Aerial Perspective ｜基于纯视觉重建的低空语义场景补全基准

研究机构：美国加州大学洛杉矶分校、德国慕尼黑工业大学

作者：Markus Gross、Sai B. Matha、Aya Fahmy 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.20770)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20770)

> 无人机低空3D感知长期受限于LiDAR硬件的重量功耗约束及高空视角下的点云稀疏性，导致语义场景补全（Semantic Scene Completion, SSC）任务在航空域缺乏真实世界基准。现有地面SSC数据集依赖LiDAR融合生成真值，无法直接迁移至UAV场景，而纯视觉重建的几何精度与语义标注效率尚未得到系统性验证。本文提出OccuFly，首个基于相机模态的低空SSC基准，通过SfM+MVS重建点云并利用<10%图像标注覆盖99%点云，实现了LiDAR-free的大规模数据生成。该基准揭示了现有SSC与深度估计模型在航空域的严重泛化失效，但当前模型在OccuFly上mIoU仅2.04%，表明该任务仍处于早期探索阶段。

## 研究背景

无人机自主飞行需要构建完整的3D场景理解，语义场景补全（SSC）通过从稀疏观测推断完整几何结构并分配语义标签，是导航与监控的核心基础。然而，SSC真值生成传统上依赖多帧LiDAR扫描融合，这一流程在地面自动驾驶中成熟，但在UAV场景中面临双重困境：一是UAV平台受严格飞行法规与SWaP（尺寸、重量与功耗）约束，LiDAR的重量与能耗远超相机，难以普及；二是高空视角导致LiDAR点云稀疏性加剧，大量区域未被观测，生成的体素真值存在严重缺失与噪声。

地面SSC数据集如SemanticKITTI、nuScenes均基于LiDAR模态，其数据生成流程假设传感器外参精确且点云密度足够，这在低空航拍中不成立。现有研究虽尝试通过多视角融合或伪标签缓解LiDAR稀疏性，但仍未摆脱对LiDAR硬件的依赖，且3D点云标注成本高昂。本文切入点在于彻底摒弃LiDAR，利用UAV普遍搭载的相机模态，通过经典3D重建技术生成度量点云，并将2D语义标注高效提升为3D体素真值，从而构建首个真实世界低空SSC基准。

## 核心方法

### 基于SfM+MVS的度量重建与2D-3D对应

标准SSC数据生成流程依赖LiDAR点云融合与3D标注，本文将其替换为基于地理参考图像的SfM+MVS重建。给定N张标定RGB图像及其位姿，通过SfM+MVS生成度量点云P与逐帧度量深度图D，并建立2D-3D对应关系A，将图像像素与3D点关联。这一设计动机在于规避LiDAR硬件限制，同时利用相机的高分辨率与低成本特性，为后续语义标注提供几何基础。重建过程确保几何保真度，平均重投影误差为1.24像素，验证了2D-3D对齐的精度。

### 分层采样标注与多视角语义提升

为降低3D标注成本，本文采用空间分层采样策略，仅标注每场景<10%的图像子集J。通过2D-3D对应关系，将2D语义掩码反投影至点云，并利用多视角证据融合（无权重多数投票）分配鲁棒的逐点标签。对于未标注点，应用k近邻（kNN）逆距离加权进行标签传播，并通过二次kNN去噪。该机制解决了LiDAR-free场景下3D标注不可行的问题，实证表明标注<10%图像可覆盖>99%的3D点，显著提升了标注效率。

$$
\rho(J) = \frac{|\bigcup_{n \in J} \mathcal{P}_n|}{|\mathcal{P}|} > 0.99, \quad \frac{|J|}{N} < 0.1
$$

该公式量化了标注子集J对全局点云P的覆盖率，表明少量图像标注即可实现近乎完整的3D语义覆盖。

### 类别感知稠密化与体素化

语义点云按类别分为实例类（如车辆）、地面类（如道路）与其他类（如建筑）。实例类通过DBSCAN聚类分离，利用24个虚拟相机的剪影提取与多视角雕刻生成视觉外壳（Visual Hull），填充内部体素；地面类通过Poisson表面重建生成水密网格并体素化；其他类直接体素化。最终通过固定优先级（实例>其他>地面）解决标签冲突，生成场景级语义体素网格。该设计动机在于不同类别的几何特性差异巨大，统一处理会导致边界模糊或空洞，分类别稠密化确保了体素真值的几何完整性与语义准确性。

$$
\mathbf{Y}(\mathbf{v}) = \begin{cases}
c_{\text{inst}} & \text{if } \mathbf{v} \in O_{\text{inst}} \\
c_{\text{oth}} & \text{if } \mathbf{v} \in O_{\text{oth}} \text{ and } \mathbf{v} \notin O_{\text{inst}} \\
c_{\text{gnd}} & \text{if } \mathbf{v} \in O_{\text{gnd}} \text{ and } \mathbf{v} \notin (O_{\text{inst}} \cup O_{\text{oth}}) \\
0 & \text{otherwise}
\end{cases}
$$

该公式定义了体素网格Y的标签分配规则，通过优先级顺序解决多类别重叠区域的语义冲突。

## 实验评估

实验在OccuFly测试集上进行，对比SSC方法Symphonies与DISC，以及深度估计模型MapAnything、Metric3Dv2、DepthAnything2/3。基线覆盖地面SSCSOTA与3D基础模型，但缺乏UAV专用3D方法，因该领域此前无先例。SSC结果显示，DISC在50m高度mIoU为2.20%，30m高度为2.23%，Symphonies均低于1%，表明现有模型在航空域几乎失效。深度估计方面，零样本DepthAnything2的$\delta_1$为0.003，微调后提升至0.834，但SILog指标从0.043微升至0.112，显示度量精度与相对一致性存在权衡。

| 方法 | 高度 [m] | IoU [%] | mIoU [%] |
| --- | --- | --- | --- |
| Symphonies | 50 | 15.88 | 0.58 |
| DISC | 50 | 31.10 | 2.20 |
| Symphonies | 30 | 13.22 | 0.76 |
| DISC | 30 | 26.88 | 2.23 |

| 方法 | $\delta_1$ | $\delta_2$ | $\delta_3$ | AbsRel | RMSE | MAE | SILog |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DepthAnything2 | 0.003 | 0.069 | 0.471 | 19.578 | 18.409 | 0.156 | 0.192 |
| DepthAnything2-OccuFly | 0.834 | 0.976 | 0.999 | 4.844 | 4.193 | 0.112 | 0.043 |

消融分析显示，高度增加导致深度估计性能持续下降，30m高度比50m高度更具挑战性。微调DepthAnything2后，绝对误差显著降低，但SILog轻微恶化，表明模型在适配度量尺度时牺牲了部分相对一致性。评估边界方面，OccuFly仅包含静态场景，动态物体被抑制；跨高度采集可能存在时间不一致性；2D伪标签在航空域mIoU仅17.58%，验证了人工标注的必要性。代码已开源，但超参数与GPU配置未在正文中详细披露。

## 关联研究分析

从问题动机看，OccuFly与SemanticKITTI均旨在解决SSC真值生成问题，但SemanticKITTI依赖LiDAR融合，而OccuFly采用纯视觉重建。这一差异源于UAV的SWaP约束，LiDAR在航空域不可行，迫使研究转向相机模态。然而，纯视觉重建的几何噪声可能影响SSC精度上限，论文未量化SfM+MVS误差对最终mIoU的贡献，仅报告了重投影误差。从方法设计看，OccuFly的2D-3D标注提升机制与PointSSC类似，但PointSSC基于LiDAR点云，而OccuFly基于SfM重建点云，后者在稀疏区域可能引入更多几何不确定性。此外，OccuFly未探索Transformer骨干在SSC中的优势，仅使用现有SOTA模型，未针对航空域设计专用架构，这可能限制了性能上限。

## 总结

OccuFly解决了UAV低空SSC缺乏真实世界基准的核心矛盾，切入点是摒弃LiDAR依赖，利用相机模态与SfM+MVS重建实现LiDAR-free数据生成。该方法通过<10%图像标注覆盖99%点云，大幅降低标注成本，并构建了包含20,000+样本、21类语义的基准。实验证明现有SSC模型在航空域mIoU仅2.04%，深度估计微调后$\delta_1$达0.834，揭示了显著的域差距。本文边界在于静态场景假设与纯视觉重建的几何噪声未量化，且未提出UAV专用SSC算法。当SfM+MVS重建误差在稀疏区域累积时，其对体素真值精度的具体影响程度，论文未给出定量分析。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20770)