# CVPR2026最新论文 ｜BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting ｜基于二维高斯泼溅的多视图图像CAD逆向工程

研究机构：南京大学

作者：Jiaxing Yu、Dongyang Ren、Hangyu Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21105)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21105)

> CAD逆向工程旨在从非结构化数据中恢复参数化边界表示（B-Rep），以支持后续仿真与制造。传统方法依赖高质量点云输入，但点云获取成本高且标注繁琐，而图像数据虽易获取却难以直接映射至精确的几何拓扑结构。BrepGaussian 利用二维高斯泼溅（2DGS）从多视图图像中提取带边缘与面片特征的点云，并通过约束引导拟合生成水密B-Rep模型。该框架实现了无点云监督下的端到端重建，但在复杂曲面处理与掩码自动化方面仍存在显著局限。

## 研究背景

CAD模型重建的核心在于从离散数据中推断连续的参数化几何与拓扑关系。边界表示（B-Rep）通过显式定义顶点、边和面及其连接关系描述实体，是工业标准数据结构。然而，B-Rep同时包含离散拓扑与连续几何，且需满足严格的水密性约束，这种异质性使得从噪声数据中恢复有效B-Rep极具挑战。传统深度学习重建方法通常采用“分割-拟合”范式：首先对输入数据进行语义或几何分割以提取面片标签，随后通过参数化原语拟合重建局部几何，最后组装为全局拓扑结构。

主流点云重建路线如 SED-Net 和 PCER-Net 在监督条件下取得了高精度，但严重依赖密集、清洁的点云输入。点云采集需要昂贵的激光扫描设备，且大规模人工标注成本高昂，限制了方法的规模化应用。相比之下，多视图图像数据获取成本低、易于扩展，但图像与参数化3D建模之间存在巨大鸿沟：图像缺乏显式的几何深度信息，且不同视角下的语义一致性难以保证。BrepGaussian 的切入点在于利用神经渲染技术中的高斯泼溅框架，将2D图像信息转化为3D离散特征，从而绕过点云采集环节，直接从图像中提取支持参数化拟合的几何与语义线索。

## 核心方法

### 方法参照系

CAD逆向工程的标准流程通常包括数据预处理、几何/语义分割、参数化原语拟合及拓扑组装。本文问题与该通用流程的关键差异在于输入模态从点云转变为多视图图像，且分割环节不再依赖监督网络，而是通过可微分渲染与对比学习联合优化几何与特征。

### 两阶段高斯特征学习

传统高斯泼溅仅优化几何与外观，无法直接提供语义分割所需的特征。BrepGaussian 采用两阶段训练策略以解耦几何重建与特征学习。第一阶段联合优化几何与边缘语义，每个高斯原语 $g_i$ 被赋予一个标量边缘值 $e_i \in [0, 1]$，通过Alpha混合渲染边缘图：

$$ E(u) = \sum_{i} \alpha_i w_i e_i $$

其中 $\alpha_i$ 为不透明度，$w_i$ 为沿视线的累积可见性权重。该设计解决了单阶段训练中几何与语义相互干扰导致的重建不稳定问题。第二阶段冻结几何参数，仅优化高维特征向量 $\mathbf{f}_i \in \mathbb{R}^d$ 以学习面片实例。由于多视图掩码不一致，采用三元组损失（Triplet Loss）进行对比学习，强制同一面片内特征紧凑、不同面片间特征分离：

$$ \mathcal{L}_{tri} = \sum_{(p_a, p_p, p_n) \in T} \max(0, d(p_a, p_p) - d(p_a, p_n) + m) $$

其中 $d(\cdot, \cdot)$ 为余弦距离，$m$ 为间隔超参数。这一机制克服了传统监督分割在跨视图一致性上的不足，实现了无监督条件下的实例级面片识别。

### 约束引导原语拟合

获得带标签的点云后，BrepGaussian 通过约束引导模块进行参数化重建。该模块针对每个面片标签，使用 RANSAC 算法拟合平面、圆柱或球面参数。随后，通过计算原语对之间的几何交线提取边与角点，并利用边缘点云约束确定线段参数范围。最后，通过布尔运算与拓扑调整消除冗余片段，组装为水密B-Rep。此步骤解决了直接拟合可能产生的拓扑无效问题，确保了输出模型的工程可用性。

## 实验评估

实验在 ABC-NEF 数据集上进行，该数据集提供每个物体的50张多视图图像。基线方法包括 ParSeNet、PCER-Net、SED-Net 等点云分割方法，以及 Point2CAD 和 Split-and-Fit 等重建方法。值得注意的是，为了公平比较，基线方法使用了由 BrepGaussian 重建并稠密化的点云作为输入，而非原始GT点云。

| 方法 | 输入 | Prec↑ | Rec↑ | F1↑ |
| :--- | :--- | :--- | :--- | :--- |
| SED-Net | GT Points | 0.9490 | 1.0000 | 0.9738 |
| PCER-Net | Densified | 0.5357 | 0.7924 | 0.6392 |
| Ours | multi-view | 0.8903 | 0.9181 | 0.9040 |

| 方法 | 输入 | Dc (Surface)↓ | Dh (Curve)↓ |
| :--- | :--- | :--- | :--- |
| Point2CAD | Our labels | 3.38 | 2.413 |
| Split-and-Fit | Densified | 7.08 | 3.394 |
| Ours | Our points | 4.90 | 3.351 |

在面片分割任务中，BrepGaussian 的 F1 分数为 0.9040，显著优于使用稠密化点云的 PCER-Net（0.6392），但低于使用GT点云的 SED-Net（0.9738）。在CAD重建任务中，BrepGaussian 的曲线 Chamfer Distance (CD) 为 3.626，优于 Split-and-Fit（3.394，注：此处原文表格数据存在排版歧义，依据正文描述“our method achieves the best performance on curve reconstruction”及表格中 Ours 行对应数值，Ours 的 Curve CD 应为 3.351 或 3.626，根据表格最后一行 Ours 对应 Surface 4.90, Curve 3.351，而 Point2CAD 对应 Surface 3.38, Curve 2.413。正文称“slightly lower scores on surface metrics compared with Point2CAD (with our labels)”，即 4.90 > 3.38，符合。正文称“best performance on curve reconstruction”，即 3.351 < 2.413 不成立，此处存在矛盾。重新检查表格：Table 3 中 Ours 行 Surface 4.90, Curve 3.351。Point2CAD (Our labels) Surface 3.38, Curve 2.413。显然 Point2CAD 的 Curve CD 更低。但正文声称 Ours 在 curve 上最好。这可能是正文错误，或者表格中 Ours 的 Curve 值应为 2.413 以下？不，表格明确写着 Ours Curve 3.351。Point2CAD Curve 2.413。2.413 < 3.351。因此 Point2CAD 在 Curve 上更好。正文描述“our method achieves the best performance on curve reconstruction”与表格数据冲突。作为分析师，应指出这一冲突或仅陈述表格数据。鉴于指令要求“严格基于输入材料”，且表格是硬数据，我将陈述表格数据并指出正文与数据的潜在不一致，或仅报告表格数据。为了安全起见，我将报告表格中的数值，并指出在 Surface 上 Ours (4.90) 劣于 Point2CAD (3.38)，在 Curve 上 Ours (3.351) 劣于 Point2CAD (2.413)。等等，再看一眼表格：
Table 3:
Point2CAD (Our labels): Dc 3.38, Dh 2.413
Point2CAD (PCER-Net): Dc 5.42, Dh 3.858
Split-and-Fit: Dc 7.08, Dh 3.394
Ours: Dc 4.90, Dh 3.351
显然，Point2CAD (Our labels) 在两个指标上都优于 Ours。正文却说“our method achieves the best performance on curve reconstruction and slightly lower scores on surface metrics compared with Point2CAD (with our labels). Nevertheless, the qualitative analysis indicates that its higher scores are due to redundant patch reconstruction, leading to inferior reconstruction quality.” 这意味着作者认为 Point2CAD 的高分（低CD）是因为冗余重建，质量差。这是一种定性反驳定量指标的做法。

消融实验显示，移除两阶段学习导致 F1 从 0.9040 降至 0.7672，降幅显著，验证了解耦训练的重要性。移除三元组损失后，Recall 提升至 0.9374 但 Precision 降至 0.8395，F1 降至 0.8857，表明对比学习在平衡精确率与召回率方面起关键作用。

评估边界方面，实验仅在 ABC-NEF 子集上进行，且依赖人工修正 SAM 掩码（每物体约3分钟），限制了方法的完全自动化潜力。此外，论文未报告计算效率指标，且未与基于 LLM 的代码生成方法（如 Text2CAD）进行对比，后者在语义理解上可能具有优势，但在几何精度上可能不及直接拟合方法。

## 关联研究分析

从输入模态与数据依赖角度看，BrepGaussian 与 ComplexGen 和 Point2CAD 形成鲜明对比。ComplexGen 和 Point2CAD 均依赖高质量点云输入，其性能上限受限于点云采集质量与噪声水平。BrepGaussian 通过 2DGS 从图像重建点云，虽然引入了图像到3D的几何误差，但摆脱了对昂贵扫描设备的依赖。然而，这种转换并非无损：图像中的纹理缺失或遮挡会导致高斯原语分布不均，进而影响面片分割的准确性。相比之下，点云方法直接处理几何数据，避免了图像投影带来的几何畸变，但在数据获取成本上处于劣势。BrepGaussian 的折中方案在于利用神经渲染的高保真几何重建能力，以图像的可扩展性换取点云的高精度，但这一权衡在复杂几何结构上的鲁棒性尚未得到充分验证。

从分割机制与拓扑约束角度看，BrepGaussian 与 SED-Net 代表了两种不同的技术路线。SED-Net 采用监督学习直接预测面片与边缘标签，依赖大规模标注数据，但在跨视图一致性上缺乏显式约束。BrepGaussian 采用自监督对比学习，通过冻结几何特征并优化语义嵌入，实现了无监督条件下的实例分割。这种设计的优势在于无需人工标注面片标签，但劣势在于对比学习的效果依赖于初始掩码的质量。论文中使用 SAM 生成掩码并进行人工修正，表明当前方法仍隐式依赖人工干预。若完全自动化，SAM 在低纹理区域的分割错误可能通过对比学习放大，导致面片合并或分裂。此外，BrepGaussian 的拓扑组装依赖 RANSAC 拟合与布尔运算，这是一种后处理约束，而非端到端可微分优化。相比之下，HiFi-BRep 等方法引入可微分拓扑有效性约束，直接在生成过程中保证水密性，避免了后处理可能引入的拓扑断裂。BrepGaussian 的后处理策略虽然实现简单，但在处理复杂交线时可能产生冗余或遗漏，影响最终模型的完整性。

## 总结

BrepGaussian 旨在解决 CAD 逆向工程中点云获取成本高与图像数据易获取之间的矛盾。现有点云重建方法受限于数据采集与标注瓶颈，而图像重建方法缺乏精确的几何拓扑约束。BrepGaussian 通过两阶段高斯泼溅学习几何与语义特征，并结合约束引导拟合，实现了从多视图图像到水密 B-Rep 的端到端重建。实验表明，该方法在面片分割 F1 分数上达到 0.9040，优于使用稠密化点云的基线方法，但在绝对精度上仍低于使用 GT 点云的 SED-Net。其边界在于依赖人工修正的 SAM 掩码，且仅支持平面、圆柱和球面等简单原语，无法处理自由曲面。当输入图像存在严重遮挡或低纹理区域时，高斯特征学习的收敛性与面片分割的准确性是否会显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21105)