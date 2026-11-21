# CVPR2026最新论文 ｜ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction ｜ClipGStream：面向任意长度与运动的Clip-Stream高斯泼溅多视角动态重建

研究机构：北京大学

作者：Jie Liang、Jiahao Wu、Chao Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13746)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13746)

> 多视角动态场景重建旨在从同步相机序列恢复时空一致的三维表示，以支撑VR/XR沉浸式内容生产。现有Frame-Stream方法虽可扩展至长序列，但帧间抖动与累积误差严重；Clip方法虽保证局部一致性，却受限于内存开销且无法处理超长视频。ClipGStream通过Clip级流式优化，结合Reference Clip继承与Source Clip残差补偿，在1,400帧长序列上实现了24.54 PSNR的SOTA性能，但其对COLMAP位姿的强依赖及冻结继承机制对光照变化的适应性尚存疑。

## 研究背景

多视角动态重建的核心难点在于平衡时间一致性与空间覆盖度。3D Gaussian Splatting (3DGS) 作为显式渲染基元，通过各向异性高斯与光栅化实现实时合成，但其独立优化特性导致高斯冗余且难以捕捉长时运动。ScaffoldGS 引入Anchor机制，将高斯参数解码为Anchor特征的函数，提升了表示紧凑性，却未解决跨时间步的运动建模问题。

动态重建领域长期存在Frame-Stream与Clip两种范式的对立。Frame-Stream方法如3DGStream逐帧优化，虽能处理超长序列，但缺乏全局时间约束，导致帧间抖动与误差累积；Clip方法如SpaceTimeGS联合优化固定长度片段（约300帧），虽保证局部一致性，但内存占用随帧数线性增长，无法扩展至数千帧的长视频。更关键的是，两类方法在面对大幅度快速运动时均表现不佳：Frame-Stream因帧间依赖断裂而丢失运动轨迹，Clip方法则因优化范围受限而难以捕捉大位移结构。ClipGStream的切入点在于将优化粒度从“帧”或“全片段”调整为“Clip级流式”，通过冻结共享组件与动态补偿残差，同时解决长序列扩展性与大运动建模难题。

## 核心方法

### 方法参照系

本文基于ScaffoldGS的Anchor-Field架构，将动态场景表示为静态特征与动态特征的解码组合。与标准Clip方法联合优化所有帧不同，ClipGStream将视频切分为Reference Clip与Source Clips，采用“继承+补偿”的流式训练策略，核心差异在于跨Clip的组件冻结与残差Anchor的动态生成机制。

### Intra-clip训练与残差Anchor补偿

针对Source Clip中大位移结构无法被Reference Clip Anchor准确覆盖的问题，本文引入几何感知的残差Anchor补偿模块。首先，将Reference Clip的Anchor $A_0$ 转化为球面覆盖场，每个Anchor $p$ 对应一个半径为 $r$ 的球体，其中 $r$ 定义为 $p$ 到其三个最近邻的平均欧氏距离：

$$ r = \frac{1}{3} \sum_{i=1}^{3} \| p - p_i \|_2 $$

该公式构建了Reference Clip的空间覆盖边界。对于Source Clip的候选Anchor $q$，计算其到覆盖场的有符号距离 $SDF(q)$；若 $SDF(q) > 0$，则 $q$ 被保留为残差Anchor $A_n^r$，否则丢弃。这一设计确保了仅新增或显著位移的结构被引入，避免了Anchor数量的冗余增长。随后，Source Clip的Anchor集合 $A_n$ 由继承的 $A_0$ 与残差 $A_n^r$ 合并而成，并训练独立的时空场 $STF_n$ 以建模局部运动。独立STF的引入解决了单一变形场在长序列中运动表示不一致的问题，使每个Clip能自适应其局部动态。

### Inter-clip继承与时间一致性

为防止Source Clip独立优化导致的静态区域闪烁，本文提出静态继承策略。Reference Clip训练得到的Anchor $A_0$、静态特征 $f_{s,0}$ 及解码器 $d(\cdot)$ 在所有Source Clip中保持冻结。Source Clip仅优化其残差Anchor的静态特征 $f_{s,n}^r$ 与独立STF $STF_n$。解码后的Temporal Gaussians由冻结解码器生成：

$$ G_t = d([f_{s,n}; f_{d,n}]) $$

其中 $f_{d,n}$ 为 $STF_n$ 输出的动态特征。冻结机制确保了静态几何与外观属性在时间轴上的严格对齐，而残差补偿则保留了动态区域的表达能力。这种“冻结共享+动态补偿”的设计，使得长序列重建既具备Clip方法的时间稳定性，又拥有Frame-Stream方法的扩展性。

## 实验评估

实验在Long 360（1,400帧，36相机）、N3DV（5个300帧场景）及VRU（250帧）上进行，基线覆盖Frame-Stream（3DGStream, iFVC）与Clip（4DGaussian, SpaceTimeGS, LocalDyGS）两类方法。在Long 360上，ClipGStream取得24.54 PSNR，显著优于Frame-Stream最优的iFVC（22.35 PSNR）与Clip最优的LocalDyGS（23.11 PSNR），验证了Clip-Stream框架在大运动长序列上的优势。

| Method | PSNR ↑ | DSSIM1 ↓ | DSSIM2 ↓ | LPIPS ↓ |
| :--- | :--- | :--- | :--- | :--- |
| iFVC [44] | 22.35 | 0.101 | 0.050 | 0.192 |
| LocalDyGS [31] | 23.11 | 0.093 | 0.046 | 0.178 |
| **ClipGStream** | **24.54** | **0.079** | **0.036** | **0.146** |

消融实验显示，移除残差Anchor补偿（RAC）导致PSNR下降0.92 dB（24.54→23.62），移除解码器继承（DI）下降0.20 dB（24.54→24.34），表明RAC对大运动建模的贡献大于DI。此外，对比独立训练（21.85 PSNR）与共享STF（23.11 PSNR），Clip-Stream策略（24.54 PSNR）的优势显著，证实了Clip级独立STF与继承机制的协同效应。

评估指标仅包含PSNR、DSSIM、LPIPS，缺乏几何精度（如Chamfer Distance）与物理一致性指标，无法验证重建表面的几何质量。论文未提供代码与超参数细节，且依赖COLMAP位姿估计，在低重叠或无纹理场景下的鲁棒性未做测试，限制了其在真实复杂环境中的可复现性。

## 关联研究分析

从问题动机看，ClipGStream与LocalDyGS同属Anchor-Field架构，但LocalDyGS聚焦于短序列（300帧）内的局部动态建模，而ClipGStream针对长序列（1,400帧）的跨Clip一致性。两者的核心差异在于时间建模粒度：LocalDyGS依赖单一STF覆盖全片段，而ClipGStream采用Clip级独立STF与冻结继承。这一差异源于任务特性：长序列中单一变形场易产生漂移，Clip级独立建模虽增加计算开销，但通过冻结继承避免了误差累积。然而，冻结继承机制是否限制了Source Clip对全局光照变化的适应能力，论文未给出回答。

从方法设计看，ClipGStream与3DGStream同属流式框架，但3DGStream采用帧级Neural Transformation Cache (NTC) 维持时间连续性，而ClipGStream采用Clip级残差Anchor补偿。3DGStream的帧级依赖导致误差随帧数线性累积，而ClipGStream的Clip级优化将误差控制单元扩大，结合冻结继承实现了更稳定的长序列重建。这一设计选择反映了从“帧间连续”到“Clip间一致”的范式转变，但残差Anchor的几何感知去重策略在极端稀疏视角下的有效性尚待验证。

## 总结

ClipGStream旨在解决长序列多视角动态重建中精度与扩展性的矛盾，其切入点在于将优化粒度从帧或全片段调整为Clip级流式，通过冻结Reference Clip组件与动态补偿Source Clip残差，同时保证时间一致性与大运动建模能力。该方法在Long 360上取得24.54 PSNR，优于现有SOTA。然而，其依赖COLMAP位姿估计，且在冻结继承机制下对全局光照变化的适应性未做测试。当场景中存在显著光照变化时，冻结的静态特征与解码器是否会导致Source Clip渲染失真，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13746)