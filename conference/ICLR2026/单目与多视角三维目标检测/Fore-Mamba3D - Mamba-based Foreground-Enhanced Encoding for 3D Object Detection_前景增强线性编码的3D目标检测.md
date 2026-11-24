# ICLR2026最新论文 ｜Fore-Mamba3D: Mamba-based Foreground-Enhanced Encoding for 3D Object Detection ｜前景增强线性编码的3D目标检测

研究机构：上海交通大学

作者：Zhiwei Ning、Xuanang Gao、Jiaxi Cao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19536)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19536)

> 3D目标检测中，LiDAR体素序列包含大量无信息的背景噪声，导致线性编码器计算冗余且难以聚焦有效特征。现有Mamba方法对全序列进行双向扫描，既浪费算力又因长程依赖衰减导致跨实例信息丢失。本文通过预测前景分数筛选Top-k体素，结合区域到全局滑动窗口与语义几何融合模块，在保持线性复杂度的同时提升检测精度。该方法在nuScenes和KITTI上刷新了LiDAR-only检测的SOTA，但其前景采样策略对边界模糊物体的鲁棒性仍存疑。

## 研究背景

LiDAR点云经体素化后形成稀疏三维网格，其中约80%的体素为地面或天空等背景区域。直接对这些体素进行特征编码不仅消耗大量GPU内存，更关键的是，背景噪声会稀释前景物体的语义信号，使得线性自回归模型难以捕捉跨实例的长程依赖。状态空间模型（State Space Model, SSM）如Mamba以线性复杂度处理序列，成为替代Transformer的主流选择，但其因果性设计导致信息单向流动，在稀疏前景序列中易出现响应衰减。

LiDAR 3D检测的主流路线分为基于稀疏卷积（SpCNN）和基于Transformer两类。SpCNN受限于局部感受野，难以捕获全局上下文；Transformer虽具备全局交互能力，但二次方计算复杂度阻碍实时部署。近期Mamba-based方法（如LION, Voxel-Mamba）尝试用线性编码解决效率问题，但LION采用分组策略导致组间信息隔离，Voxel-Mamba虽采用无分组扁平化，却对全场景体素进行编码，未能区分前景与背景。本文切入点在于：仅编码前景体素可大幅降低序列长度，但直接应用标准Mamba会因前景体素的空间离散性导致长程依赖失效，需设计专门的机制缓解响应衰减并增强语义几何感知。

## 核心方法

### 方法参照系

本文基于Mamba架构的LiDAR 3D检测框架，核心差异在于将编码对象从“全场景非空体素”缩减为“预测的前景体素”，并引入区域-全局信息传播机制以弥补稀疏序列的上下文缺失。

### 前景体素采样与Hilbert曲线旋转

标准Mamba对输入序列进行单向扫描，若直接输入稀疏前景体素，空间上相邻的体素在序列中可能相距甚远，导致信息断裂。本文首先通过子流形卷积预测每个非空体素的前景分数 $F$，选取Top-$k$ 体素构成前景特征 $X_f$。为解决Hilbert曲线扁平化导致的“区域截断”问题（即3D空间邻近体素在1D序列中距离过远），本文对场景进行多次旋转。给定旋转角 $\theta$，坐标变换为：

$$ R(\theta, p) = (\lfloor x\cos\theta + y\sin\theta \rfloor, \lfloor y\cos\theta - x\sin\theta \rfloor, z)^T $$

通过 $\theta=0$ 和 $\theta=\pi/2$ 两次旋转并扁平化，确保被截断的邻近体素在至少一个序列中保持接近，最后将多视角特征求和并拼接背景特征，有效缓解了空间邻近性丢失问题。

### 区域到全局滑动窗口（RGSW）

前景体素在实例间分布稀疏，标准Mamba的因果性阻碍了跨实例的信息流动。RGSW将序列分为 $M$ 个Patch，在每个Patch末尾插入局部Token $T_i$ 以聚合区域信息。随后，通过滑动窗口机制，将当前Patch的后半部分与下一Patch的前半部分重叠，形成新的滑动Patch $x_s$，并再次送入SSM编码。该过程迭代 $t$ 次，实现信息从局部区域向全局序列的传播，解决了分组方法中组间交互缺失的问题，同时避免了双向编码的计算开销。

### 语义辅助与状态空间融合（SASFMamba）

为增强前景编码的语义与几何感知，SASFMamba包含两个模块。语义辅助融合（SAF）根据预测的语义类别 $S$ 对状态变量 $h$ 进行重排，使语义相似的体素在序列中相邻，再通过1D卷积聚合语义上下文。其理论依据在于，重排后状态变量 $h'_i$ 可表示为语义邻居的加权和：

$$ h'_i = \sum_{k \in K} \alpha_k h_{N_k(i)} $$

其中 $N_k(i)$ 为语义域中 $i$ 的邻居索引。该机制使当前状态能捕获远距离但语义相似的输入信息，克服线性编码器的局部偏置。状态空间融合（SSF）则将状态变量映射回3D空间，通过维度卷积（DwConv）增强几何结构感知，最后映射回序列空间，实现非因果的几何相关编码。

## 实验评估

实验在nuScenes、KITTI和Waymo数据集上进行，基线涵盖SpCNN（SECOND）、Transformer（DSVT, TransFusion）及Mamba（LION, Voxel-Mamba）路线。在nuScenes验证集上，Fore-Mamba3D取得68.4 mAP和72.3 NDS，超越LION（68.0 mAP）和Voxel-Mamba（67.5 mAP）。KITTI验证集上，Car Hard AP达90.3，较Voxel-Mamba提升1.2个点。Waymo数据集（20%训练数据）上，L2级别mAP达71.9%，比CenterPoint高7.4%。

| 数据集 | 方法 | mAP | NDS | Car Hard (KITTI) |
| :--- | :--- | :--- | :--- | :--- |
| nuScenes | LION | 68.0 | 72.1 | - |
| nuScenes | Voxel-Mamba | 67.5 | 71.9 | - |
| nuScenes | **Fore-Mamba3D** | **68.4** | **72.3** | - |
| KITTI | Voxel-Mamba | - | - | 89.1 |
| KITTI | **Fore-Mamba3D** | - | - | **90.3** |

消融实验显示，前景采样比例 $\alpha=0.2$ 时性能最佳，FLOPs较LION降低43.7%，FPS提升23.9%。RGSW迭代次数 $t=2$ 时mAP最高（71.3），$t=4$ 时性能下降，表明过度滑动导致信息冗余。SAF模块中，卷积核大小 $K=7$ 时mAP达68.4，相似度得分0.64，优于 $K=3$ 和 $K=15$，说明中等感受野在语义聚合与计算成本间取得平衡。

评估边界方面，论文未报告置信区间，nuScenes上0.4 mAP的提升幅度在统计显著性上存疑。代码已开源，但Hilbert曲线模板需离线生成，增加了部署复杂度。Waymo实验仅使用20%训练数据，与全量训练SOTA的可比性受限。

## 关联研究分析

从问题动机看，本文与视觉领域的BEV稀疏化策略（如Sparse4D）共享“降低计算冗余”的目标，但LiDAR体素的稀疏性是固有的，而视觉BEV的稀疏化是人为选择的。本文的前景采样依赖于预测分数，若预测错误会导致关键结构丢失，这在视觉领域通过多视角互补缓解，但在单模态LiDAR中缺乏冗余信息，使得采样精度成为性能上限的决定因素。

从方法设计看，本文的RGSW机制与Transformer的局部-全局注意力（如Swin Transformer）在逻辑上相似，均旨在解决局部编码的全局交互问题。但RGSW基于SSM的线性特性，通过滑动窗口实现信息传播，避免了二次方复杂度。然而，RGSW的迭代次数 $t$ 对性能敏感，且其信息传播路径受Hilbert曲线顺序限制，不如Transformer的自注意力灵活。与Voxel-Mamba相比，本文引入了语义重排（SAF），而Voxel-Mamba仅依赖空间邻近性，这解释了本文在长尾类别上的潜在优势，但论文未提供细粒度类别分析以验证此点。

## 总结

Fore-Mamba3D旨在解决LiDAR 3D检测中背景噪声导致的计算冗余与前景稀疏导致的长程依赖失效矛盾。通过前景分数筛选、Hilbert旋转、RGSW滑动窗口及SASFMamba语义几何融合，该方法在nuScenes上以68.4 mAP超越LION，并在KITTI上取得90.3 Car Hard AP。其边界在于前景采样对预测精度的依赖，以及RGSW迭代次数的敏感性。当前景体素极度稀疏（如远距离小目标）时，Top-k采样是否仍能保留足够的结构信息以支撑准确的边界框回归，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19536)