# CVPR2026最新论文 ｜RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cue for 3D Object Detection ｜雷达-相机融合3D检测中的高斯动态聚合

研究机构：浙江大学、同济大学

作者：Xiaokai Bai、Chenxu Zhou、Lianqing Zheng 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7498eb3c6f2b)

> 4D毫米波雷达与单目相机融合3D检测面临的核心矛盾是：雷达点云极度稀疏且含噪，而相机提供密集语义但缺乏深度几何。现有BEV网格方法因固定分辨率导致背景冗余计算，实例级方法则缺乏全局场景理解。RaGS提出将场景建模为连续3D高斯场，通过迭代聚合动态聚焦前景目标，在View-of-Delft和TJ4DRadSet上取得SOTA性能，但其对LiDAR深度监督的依赖及环视扩展的局限性尚待验证。

## 研究背景

4D毫米波雷达提供距离、方位角、俯仰角和多普勒速度四维信息，但点云密度远低于LiDAR（如VoD数据集中雷达约210点 vs LiDAR 24000点），直接套用LiDAR的体素或柱状编码器时特征图空洞，难以捕捉精细几何结构。相机图像提供高分辨率语义信息，但单目深度估计存在歧义，且受光照影响。这种模态间的稀疏-密集、几何-语义错位，构成了雷达-相机融合3D检测的核心挑战。

主流融合范式分为实例级与BEV级两类。实例级方法（如CenterFusion、CRAFT）依赖2D检测器生成提案，再通过雷达特征精化，但受限于级联网络设计，缺乏全局场景理解；BEV级方法（如BEVFusion、LXL）将多模态特征投影至固定顶视空间，实现全局推理，但固定体素化导致锚点采样僵化，且对背景区域进行过度聚合，计算效率低下。RaGS的切入点在于：3D高斯泼溅（3D Gaussian Splatting, 3DGS）作为连续、可微分的场景表示，能动态分配计算资源至前景目标，同时保持全局感知能力，恰好匹配3D检测任务的稀疏本质。

## 核心方法

### 方法参照系

RaGS属于雷达-相机中间融合范式，但摒弃了传统BEV网格的固定采样机制。其核心差异在于：用可学习的高斯中心迭代优化替代固定体素投影，用3D可变形交叉注意力（3D-DCA）替代2D图像特征采样，实现几何与语义在3D空间的一致性交互。

### 视锥定位初始化（FLI）

FLI解决高斯初始化的前景聚焦问题。传统BEV方法对全场景均匀采样，导致大量计算浪费于背景。RaGS从分割日志与度量深度中选取Top-K前景像素，反投影至3D空间：

$$ \mathbf{P}_{\text{unproj}} = d \cdot \mathbf{K}^{-1} (u, v, 1)^T $$

其中 $d$ 为像素深度，$\mathbf{K}$ 为相机内参矩阵。同时融合4D雷达点云与视锥内随机采样点，确保所有高斯位于视场内，形成粗粒度但结构化的初始定位。这一设计避免了BEV网格对全场景的盲目覆盖，将计算资源集中于潜在目标区域。

### 迭代多模态聚合（IMA）

IMA解决高斯位置精化与多模态特征融合问题。固定网格方法无法适应目标尺度变化，导致小目标检测失效。RaGS通过3D-DCA在深度感知3D图像特征空间中聚合语义：

$$ \mathbf{F}^{\text{I}} = \sum_{n=1}^{T} \mathbf{A}_n \mathbf{W} \cdot \phi (\mathbf{F}^{\text{2D}} \otimes \mathbf{D}^{\text{prob.}}, \mathcal{P}(\mathbf{P}) + \Delta \mathbf{q}) $$

其中 $\mathbf{F}^{\text{2D}} \otimes \mathbf{D}^{\text{prob.}}$ 构建深度感知3D特征空间，$\Delta \mathbf{q}$ 为可学习偏移。随后，高斯点云与雷达稀疏柱状特征在统一体素空间中通过稀疏卷积交互，雷达速度作为隐式运动线索引导高斯向动态目标收敛。最后，MLP预测残差偏移 $\Delta \mathbf{p}$ 更新高斯位置，实现迭代精化。这一过程使高斯动态聚焦于前景目标，规避了固定网格的背景冗余。

### 多层高斯融合（MGF）

MGF解决多尺度特征整合问题。单一层级的高斯表示难以兼顾细节与全局上下文。RaGS将M层精化后的高斯场分别渲染至BEV空间，通过可微分光栅化器计算加权累积：

$$ \mathbf{F}^{(l)}_{\text{bev}} = \text{Rasterize}(\mathbf{G}_{M-L+l}), \quad l = 1, \ldots, L $$

其中 $\mathbf{G}_{M-L+l}$ 为第 $l$ 层高斯集合。多层BEV特征经卷积融合后，与雷达稀疏柱状特征通过跨模态融合器整合，生成最终检测特征。这一设计补偿了高斯表示的稀疏性，提供了多尺度语义-几何抽象。

## 实验评估

RaGS在View-of-Delft（VoD）、TJ4DRadSet和OmniHD-Scenes三个基准上评估。基线覆盖BEV级（LXL、BEVFusion）、实例级（FUTR3D）及高斯类（SGDet3D），但遗漏了最新SOTA RPGFusion。在VoD验证集上，RaGS取得61.86 mAP（EAA）和81.63 mAP（DC），超越LXL的56.31和58.30；在TJ4DRadSet测试集上，RaGS取得41.95 AP3D和51.04 APBEV，显著优于SGDet3D的41.82和47.16。

| 数据集 | 方法 | mAP/AP3D | mAPDC/APBEV | FPS |
| :--- | :--- | :--- | :--- | :--- |
| VoD (Val) | LXL | 56.31 | 58.30 | 6.1 |
| VoD (Val) | SGDet3D | 59.75 | 77.42 | 9.2 |
| VoD (Val) | RaGS | 61.86 | 81.63 | 10.5 |
| TJ4DRadSet (Test) | SGDet3D | 41.82 | 47.16 | - |
| TJ4DRadSet (Test) | RaGS | 41.95 | 51.04 | - |

消融实验显示，FLI、IMA、MGF各模块均贡献正向增益：仅FLI提升mAP至57.40，加入IMA后达59.45，MGF进一步提升至59.45（EAA）和76.98（DC）。高斯锚点数N从52.24增至12800时，mAP从54.77提升至59.45，但FLOPS从599.39增至639.82，表明性能与计算成本存在权衡。

评估边界方面，RaGS依赖LiDAR深度监督进行预训练，无LiDAR场景下的鲁棒性未验证；OmniHD-Scenes环视扩展仅初步探索，未提供详细消融；代码已开源，但训练细节（如λ=0.1的超参数选择）缺乏敏感性分析。

## 关联研究分析

从方法设计看，RaGS与SGDet3D同属高斯表示路线，但SGDet3D采用静态高斯属性预测，而RaGS引入迭代位置更新机制。这一差异源于任务特性：SGDet3D侧重单帧几何精化，RaGS需处理雷达稀疏性导致的定位不确定性，迭代聚合通过多轮特征交互逐步收敛至目标区域。然而，RaGS对LiDAR深度监督的依赖是否限制了其在无LiDAR场景的泛化能力，论文未给出回答。

从问题动机看，RaGS与BEVFusion均解决雷达-相机语义-几何错位，但BEVFusion采用固定BEV网格投影，RaGS采用动态高斯聚合。BEVFusion的全局上下文优势在标准场景（如VoD）中体现为稳定性能，而RaGS的动态聚焦在复杂场景（如TJ4DRadSet的夜间、桥下）中展现更高精度。这种差异暗示：固定网格适合结构化场景，动态高斯适合非结构化稀疏场景，但两者的计算-精度权衡缺乏统一基准。

## 总结

RaGS针对4D雷达-相机融合中固定BEV网格的背景冗余与实例级方法的全局感知缺失，提出3D高斯动态聚合框架。通过FLI前景初始化、IMA迭代多模态聚合、MGF多层融合，RaGS在VoD上取得61.86 mAP，在TJ4DRadSet上取得41.95 AP3D，验证了连续高斯表示在稀疏场景下的有效性。其边界在于：依赖LiDAR深度监督、环视扩展未充分验证、计算效率（10.5 FPS）虽优于LXL但低于SGDet3D（9.2 FPS）的对比存在矛盾。当雷达点云密度进一步降低或场景复杂度增加时，高斯迭代收敛的稳定性与计算开销是否仍具优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7498eb3c6f2b)