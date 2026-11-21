# CVPR2026最新论文 ｜Deformation-based In-Context Learning for Point Cloud Understanding ｜基于变形的点云上下文学习

研究机构：美国普林斯顿高等研究院、四川大学

作者：Chengxing Lin、Jinhong Deng、Yinjie Lei 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02845)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02845)

> 3D点云上下文学习（In-Context Learning, ICL）旨在通过少量示例实现多任务泛化，但现有掩码点建模（Masked Point Modeling, MPM）方法因缺乏几何先验导致重建失真，且训练与推理目标存在根本性错位。DeformPIC 将 ICL 重构为几何变形过程，通过解耦任务提取与变形转移，显式建模查询点云向目标形状的映射。该方法在 ShapeNet In-Context 基准上显著降低了 Chamfer Distance，但在跨域泛化中仍受限于变形场的局部性假设。其价值在于确立了点云 ICL 的几何一致性范式，但变形机制对非刚性大位移任务的适用性尚存疑。

## 研究背景

点云数据的无序性使得标准序列模型难以直接应用，而 ICL 范式要求模型在不更新参数的前提下，仅凭上下文示例推断任务语义并执行对应操作。这一过程依赖于模型对输入-目标对之间几何变换关系的隐式学习，若缺乏显式的空间结构约束，模型极易陷入仅依赖 token 级相关性的捷径学习，导致生成的目标点云出现几何伪影。

主流点云 ICL 方法如 PIC 采用 MPM 框架，通过随机掩码目标点云并训练模型从可见部分重建缺失区域。然而，这种设计存在两个核心缺陷：一是掩码 token 作为抽象占位符，不包含任何空间或结构先验，模型必须纯粹依靠 Transformer 的自注意力机制推断全局几何，这在复杂形状上往往失效；二是训练时目标点云部分可见，而推理时目标完全被掩码，这种训练-推理目标不匹配鼓励模型依赖训练时观察到的目标侧线索，而非真正利用 prompt 作为几何引导。DeformPIC 的切入点在于摒弃“从空白重建”的逻辑，转而采用“从查询变形”的策略，将 ICL 视为一个由 prompt 条件化的几何变换过程。

## 核心方法

### 方法参照系

点云 ICL 的标准流程通常遵循 MPM 范式：将 prompt 对与 query 对拼接，通过联合采样获取对齐的中心点，利用 K-Nearest Neighbors (KNN) 提取局部 patch，随后将目标 patch 替换为可学习的掩码 token，并训练 Transformer 从可见 token 重建被掩码内容。本文的关键差异在于，不再将目标视为需要从零生成的独立实体，而是视为查询点云在特定任务条件下的变形结果，从而将重建问题转化为变形场估计问题。

### 变形提取网络

设计动机在于解决 MPM 中任务语义与几何重建在共享潜空间中的耦合干扰。Deformation Extraction Network (DEN) 负责从 prompt 对中解耦出任务特定的变形信息。首先，使用 mini-PointNet 将 prompt 输入 $P_i$ 和目标 $P_t$ 的 patch 编码为点 token，随后与一个可学习的任务 token $T_{task}$ 拼接。通过堆叠的 Transformer 块 $E(\cdot)$ 提取任务相关特征，输出聚合后的任务 token $\hat{T}_{task}$：

$$ \hat{T}_{task} = E([T_{task} \| E_{pt}(P_i) \| E_{pt}(P_t)]) $$

该公式表明，任务 token 不仅编码了“做什么”（如去噪、配准），还隐含了“怎么做”（如旋转角度、噪声分布），为后续的变形过程提供了条件化参数。

### 变形转移网络

设计动机在于确保训练与推理目标的一致性，并引入显式几何先验。Deformation Transfer Network (DTN) 接收查询输入 $Q_i$ 和 DEN 输出的任务 token，执行具体的几何变形。查询 patch 首先被编码为 token $T_{Qi}$，随后通过堆叠 Transformer 块 $T(\cdot)$ 进行处理。为了将任务条件注入变形过程，采用 AdaLN-Zero 调制机制，将任务 token 映射为缩放和偏移参数，调制每一层的 Layer Normalization：

$$ h_{[l+1]} = h_{[l]} + A(\text{LN}(h_{[l]}) \odot (1 + \alpha_{[l]}) + \beta_{[l]}) $$

其中 $\alpha_{[l]}, \beta_{[l]}$ 由任务 token 生成。最终通过投影头 $H(\cdot)$ 预测变形后的点云坐标 $\hat{Q}_t$。整个网络以 Chamfer Distance 的 $L_2$ 变体作为损失函数进行端到端优化，确保变形后的点云与真实目标在几何距离上最小化。

## 实验评估

实验在 ShapeNet In-Context 数据集上进行，该数据集包含 174,404 个训练样本和 43,050 个测试样本，覆盖重建、去噪、配准和部件分割四个任务。基线方法涵盖了任务特定模型（PointNet, DGCNN, PCT, ACT）、多任务模型（Point-MAE, ACT, I2P-MAE, ReCon, PCP-MAE, UniPre3D）以及 ICL 模型（PIC-Cat, PIC-Sep, PIC-S-Cat, PIC-S-Sep）。

| 模型 | 部件分割 mIoU (%) | 重建 CD (Avg) | 去噪 CD (Avg) | 配准 CD (Avg) |
| :--- | :--- | :--- | :--- | :--- |
| PIC-Cat | 79.0 | 4.3 | 5.3 | 14.1 |
| PIC-S-Sep | 83.7 | 5.1 | 6.5 | 6.7 |
| Point-MAE | 5.4 | 6.0 | 5.6 | 14.5 |
| **DeformPIC** | **83.9** | **2.7** | **3.5** | **2.0** |

DeformPIC 在配准任务上表现尤为突出，平均 Chamfer Distance 为 2.0，显著优于 PIC-S-Sep 的 6.7 和 Point-MAE 的 14.5。在重建和去噪任务上，分别比 PIC-Cat 降低 1.6 和 1.8 个 CD 点。

消融实验验证了各组件的贡献。仅对齐训练-推理目标（完全掩码查询目标）即可在配准任务上带来显著改善，从 14.1 降至 3.5 CD。引入 DTN 后，重建和去噪性能进一步提升，表明显式几何线索的价值。最后引入 DEN 解耦变形提取，在所有任务上均带来额外增益，最终达到 2.7 (重建), 3.5 (去噪), 2.0 (配准) 的 CD 值。

| 模型变体 | 一致性目标 | DTN | DEN | 重建 CD | 去噪 CD | 配准 CD |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| PIC-Cat | ✗ | ✗ | ✗ | 4.3 | 5.3 | 14.1 |
| + 一致性目标 | ✓ | ✗ | ✗ | 3.2 | 4.0 | 3.5 |
| + DTN | ✓ | ✓ | ✗ | 3.1 | 3.8 | 2.9 |
| **DeformPIC** | ✓ | ✓ | ✓ | **2.7** | **3.5** | **2.0** |

评估边界方面，实验仅在 ShapeNet 合成数据上验证域内性能，虽构建了 ModelNet40 和 ScanObjectNN 的 In-Context 数据集用于泛化测试，但未报告具体的跨域数值对比细节。代码已开源，实验在单张 NVIDIA TITAN RTX 24GB GPU 上完成，训练 300 个 epoch，超参数设置（如学习率 1e-4，权重衰减 0.05）已公开，具备较高的可复现性。

## 关联研究分析

从问题动机看，DeformPIC 与 PIC 系列方法的核心分歧在于对“上下文”的理解。PIC 将 prompt 视为提供统计相关性的上下文，依赖 Transformer 的隐式注意力机制捕捉输入-目标映射；而 DeformPIC 将 prompt 视为提供几何变换参数的条件，显式解耦任务语义与几何执行。这种差异源于 MPM 范式在 3D 几何上的固有缺陷：2D 图像中的像素重建可通过纹理统计推断，但 3D 点云的结构完整性依赖于全局拓扑，缺乏空间先验的 token 重建难以保证几何一致性。

从方法设计看，DeformPIC 借鉴了神经变形（Neural Deformation）领域的思想，如 FlowNet3D 和 Pixel2Mesh，但将其从单对形状匹配迁移至多任务 ICL 场景。与 Point-MAE 等自监督预训练方法相比，DeformPIC 不依赖大规模无标签数据的预训练，而是通过 ICL 范式在推理时动态适应任务。然而，Point-MAE 在重建任务上的 CD 为 6.0，虽低于 DeformPIC 的 2.7，但其优势在于无需 prompt 对，适用于无示例场景。DeformPIC 的变形机制假设查询与目标之间存在平滑的局部变形场，这一假设在配准和去噪任务中成立，但在涉及剧烈拓扑变化的任务（如部件分割中的大幅裁剪）中，变形场的表达能力可能受限，论文未对此类极端变形进行单独分析。

## 总结

DeformPIC 旨在解决点云 ICL 中 MPM 范式导致的几何先验缺失与训练-推理目标不匹配矛盾。现有方法因依赖无空间信息的掩码 token 重建，难以保证几何一致性，而 DeformPIC 通过引入变形提取与转移网络，将 ICL 重构为条件化几何变形过程，显式建模查询点云向目标的映射。实验表明，该方法在 ShapeNet In-Context 基准上，配准任务 CD 降至 2.0，重建任务 CD 降至 2.7，显著优于 PIC 系列基线。然而，其变形机制依赖于查询与目标间的局部平滑性假设，在跨域泛化实验中虽构建了 ModelNet40 和 ScanObjectNN 数据集，但未深入探讨变形场在真实世界噪声和遮挡下的鲁棒性。当查询点云与目标存在非刚性大位移或拓扑结构剧变时，基于局部变形的 DTN 是否仍能保持几何完整性，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02845)