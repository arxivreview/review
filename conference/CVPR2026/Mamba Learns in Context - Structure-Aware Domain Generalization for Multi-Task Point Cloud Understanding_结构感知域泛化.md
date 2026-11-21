# CVPR2026最新论文 ｜Mamba Learns in Context: Structure-Aware Domain Generalization for Multi-Task Point Cloud Understanding ｜结构感知域泛化

研究机构：吉林大学、澳大利亚西澳大学

作者：Jincen Jiang、Qianyu Zhou、Yuhang Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20739)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20739)

> 多任务点云域泛化（Domain Generalization, DG）旨在让单一模型在未见过的传感器域与几何任务间保持性能，但现有Transformer架构因二次方复杂度与无序性难以兼顾效率与结构一致性，而Mamba虽具线性复杂度却依赖坐标序列化，在视角偏移与缺失区域下易导致结构漂移。本文提出SADG，通过质心距离谱与测地曲率谱构建变换不变的序列化序列，结合层次域感知建模与测试时谱图对齐，在重建、去噪与配准任务上实现了跨域结构保持。该框架在效率与泛化性上优于基线，但其对极端缺失场景下的拓扑稳定性及语义级泛化能力的验证仍显不足。

## 研究背景

点云数据的无序性使得标准序列模型难以直接应用，而状态空间模型（State-Space Model, SSM）如Mamba虽以线性复杂度处理长序列，但其递归状态传播高度依赖输入顺序。当采用坐标驱动序列化（如轴扫描或Hilbert曲线）时，视角旋转或表面缺失会破坏局部邻域连续性，导致SSM在跨域推理中出现状态不稳定。这一矛盾在多任务DG中尤为突出，因为重建、去噪与配准均依赖全局拓扑与局部几何连续性的协同保持，而坐标序列化在域偏移下无法保证这种结构一致性。

现有Transformer-based ICL框架（如DG-PIC）虽能统一多任务，但受限于二次方注意力成本且缺乏显式结构排序，导致特征在域间对齐时丢失几何细节。SSM-based方法虽提升了效率，但普遍依赖坐标序列化，在真实扫描数据（如MP3DObject）中因视角与缺失变化而性能骤降。本文切入点在于识别“结构漂移”这一被忽略的失效模式：坐标序列化在域偏移下扭曲序列局部邻域，破坏Mamba递归所需的拓扑与几何连续性，从而阻碍跨域泛化。

## 核心方法

### 方法参照系

本文问题置于多任务ICL框架下，参照DG-PIC的Prompt-Query机制，但关键差异在于骨干网络从Transformer替换为Mamba，并引入结构感知序列化以解决SSM的顺序敏感性与坐标序列化的域偏移脆弱性。

### 结构感知序列化（SAS）

针对坐标序列化在域偏移下破坏局部连续性的问题，SAS基于两个内在谱构建变换不变序列。质心距离谱（Centroid Distance Spectrum, CDS）通过BFS遍历质心距离图保持全局拓扑，其亲和度定义为：

$$ w_{CDS}(i,j) = \exp\left(-\frac{\|u_i - u_j\|^2}{2\sigma^2}\right) $$

该公式软连接邻近token，抑制远距干扰，确保遍历的局部平滑性。测地曲率谱（Geodesic Curvature Spectrum, GCS）通过Laplace-Beltrami算子的热扩散隐式编码曲率，其热核为：

$$ K_\tau(i,j) = \sum_{k=0}^{\infty} e^{-\lambda_k \tau} \phi_k(u_i)\phi_k(u_j) $$

此扩散过程在曲率高处快速耗散，平坦处保留，从而在噪声与缺失下提供稳定的几何线索。SAS将CDS与GCS双向遍历序列拼接，为Mamba提供拓扑-几何一致的输入，解决了坐标序列化在视角变化下的结构断裂问题。

### 层次域感知建模（HDM）

SAS输出的序列虽结构一致，但直接拼接不同域token会破坏Mamba的递归动态。HDM通过两阶段级联稳定跨域推理：首先，域内结构建模（ISM）独立处理Prompt与Query域的Mamba分支，确保各域内部拓扑与几何模式聚合；其次，域间关系融合（IRF）按共享结构顺序 $\pi$ 交错排列两域token，由共享Mamba处理：

$$ Z_{IRF} = \text{Mamba}([z_{p,1}, z_{q,1}, z_{p,2}, z_{q,2}, ..., z_{p,N}, z_{q,N}]) $$

该交错机制通过递归传播隐式交换域间特征，避免了Transformer注意力匹配的计算开销，同时保持了线性效率与结构对齐，解决了简单拼接导致的跨域状态不稳定问题。

## 实验评估

实验在五个域（ModelNet40, ShapeNet, ScanNet, ScanObjectNN, MP3DObject）上进行，采用留一域协议，指标为Chamfer Distance (CD)。基线覆盖通用点云（PointNet, PointMamba）、DG方法（PointMixup）及ICL框架（DG-PIC），但缺失最新轻量化Transformer（如LitePT）及纯SSM分类SOTA（如3DSMT）。

| 方法 | ModelNet (Rec/Den/Reg) | ScanNet (Rec/Den/Reg) | MP3DObject (Rec/Den/Reg) |
|---|---|---|---|
| PointMamba | 20.16/27.08/17.40 | 15.61/22.43/14.30 | 20.16/27.08/17.40 |
| DG-PIC | 6.84/9.40/5.01 | 5.21/9.71/5.10 | 5.91/10.40/5.64 |
| Vanilla Mamba ICL | 7.69/10.81/6.22 | 5.45/10.75/5.56 | 8.28/14.19/8.44 |
| **SADG** | **5.99/7.98/3.81** | **2.97/7.67/3.63** | **3.55/6.61/2.84** |

SADG在ScanNet重建任务上CD为2.97，较DG-PIC的5.21降低42.8%，在MP3DObject配准任务上CD为2.84，较Vanilla Mamba ICL的8.44降低66.3%，验证了SAS与HDM在真实扫描数据上的结构保持优势。

消融实验显示，移除CDS导致重建CD从3.55升至4.75，移除GCS导致去噪CD从6.61升至8.92，表明CDS对全局拓扑、GCS对局部几何的独立贡献。HDM中移除ISM导致重建CD升至5.41，移除IRF导致配准CD升至7.57，证实两阶段级联对跨域稳定性的必要性。

评估边界方面，CD指标仅反映几何一致性，未涵盖语义级泛化能力；实验仅使用TITAN RTX GPU，未报告多卡扩展性；代码已开源，但MP3DObject数据集的构建细节（如缺失样本过滤阈值）未在正文中详述，可能影响复现性。

## 关联研究分析

从问题动机看，SADG与PointMamba同属SSM路线，但PointMamba聚焦单任务分类，依赖坐标序列化，在域偏移下性能骤降（如MP3DObject CD 20.16）；SADG则针对多任务DG，通过SAS解决坐标序列化的结构漂移问题，其差异根源在于任务特性：多任务DG需同时保持拓扑与几何连续性，而单任务分类仅需局部特征聚合。从方法设计看，SADG与DG-PIC同属ICL框架，但DG-PIC使用Transformer骨干，缺乏显式结构排序，导致在真实扫描数据上CD高达5.91；SADG替换为Mamba并引入SAS，其差异根源在于骨干网络的顺序敏感性：Mamba需稳定序列以维持递归状态，而Transformer的无序注意力虽灵活但计算成本高且结构一致性弱。

## 总结

SADG解决的核心矛盾是SSM在跨域多任务中因坐标序列化导致的结构漂移与递归不稳定。其切入点在于识别坐标序列化在域偏移下破坏局部连续性的失效模式，并通过SAS构建变换不变的拓扑-几何序列，结合HDM与SGA实现跨域结构保持。实验证明SADG在ScanNet重建CD为2.97，MP3DObject配准CD为2.84，显著优于基线。其边界在于CD指标未涵盖语义泛化，且对极端缺失场景下的拓扑稳定性验证不足。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20739)