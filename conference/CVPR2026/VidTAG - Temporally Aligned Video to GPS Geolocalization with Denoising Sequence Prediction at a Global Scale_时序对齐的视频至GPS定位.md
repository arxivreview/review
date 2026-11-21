# CVPR2026最新论文 ｜VidTAG: Temporally Aligned Video to GPS Geolocalization with Denoising Sequence Prediction at a Global Scale ｜时序对齐的视频至GPS定位

作者：Parth Parag Kulkarni、Rohit Gupta、Prakash Chandra Chhipa 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12159)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12159)

> 视频地理定位旨在从视频帧序列中推断每一帧的精确GPS坐标并重建轨迹。现有分类方法粒度粗且无法捕捉细粒度细节，而图像检索方法在全球尺度下因需构建海量图像库而不可行。本文提出帧至GPS检索范式，利用双编码器提取特征，并通过时序对齐与去噪模块解决单帧预测导致的轨迹抖动。该方法在全球视频定位任务上显著优于基线，但其缺乏3D几何先验的设计在复杂城市环境下的亚米级精度潜力存疑。

## 研究背景

当视频帧被独立处理时，每帧的预测位置受光照、遮挡或视角微小变化影响，导致轨迹出现高频抖动甚至跨大陆跳跃。这种单帧预测的独立性破坏了视频固有的时序连贯性，即相邻帧在物理空间中应呈现平滑过渡。为恢复这种连贯性，模型需显式建模帧间的长程依赖关系，而非仅依赖局部平滑或后处理滤波。

全球视频地理定位面临两大瓶颈：分类范式将地球划分为离散区域，虽支持单次推理但精度受限于区域粒度，且增加粒度会引发类别混淆与计算成本激增；检索范式虽精度高，但传统图像库检索在全球尺度下需覆盖所有地理区域的密集图像，构建与维护成本不可接受。GeoCLIP通过嵌入图像与GPS坐标至共享空间，实现了无需图像库的直接GPS检索，但仅针对单帧图像，未解决视频时序一致性问题。VidTAG的切入点在于将GeoCLIP的帧-GPS检索扩展至视频域，并引入时序对齐机制以生成连贯轨迹。

## 核心方法

### 方法参照系

本文基于GeoCLIP的对比学习框架，将视频定位建模为帧-GPS检索问题。与单帧图像定位不同，视频任务要求输出序列在时间轴上保持一致，这要求特征提取与检索过程必须显式编码帧序信息，而非独立处理每帧。

### 双编码器与TempGeo时序对齐

设计动机在于解决单帧预测中因上下文缺失导致的轨迹漂移。通常做法是独立编码每帧后直接检索，VidTAG采用CLIP与DINOv2双编码器融合语义与视觉特征，并通过TempGeo模块进行全自注意力对齐。TempGeo将帧嵌入 $\mathbf{z}_t$ 添加时序位置编码后，通过多头自注意力机制生成对齐嵌入 $\mathbf{z}_t^*$：

$$ \mathbf{z}_t^* = \text{SelfAttn}(\mathbf{z}_t + \mathbf{p}_t) $$

该公式允许每帧关注序列中所有其他帧，使模糊帧能从远处帧借用上下文，将孤立离群点拉向特征空间共识，从而在检索前实现端到端时序对齐。

### GeoRefiner去噪序列预测

设计动机在于修正Phase I对比学习中产生的GPS序列噪声，如整体偏移或坍塌。通常做法是直接输出检索结果，VidTAG引入GeoRefiner编码器-解码器架构，将GPS预测建模为去噪过程。训练时，对真实GPS坐标添加模拟噪声（偏移、坍塌、抖动）生成噪声嵌入 $\mathbf{g}_t^{noisy}$，解码器以 $\mathbf{g}_t^{noisy}$ 为查询，以对齐帧嵌入 $\mathbf{z}_t^*$ 为上下文，通过交叉注意力输出精化嵌入 $\mathbf{g}_t'$。损失函数采用加权Hinge损失，同时优化帧级与视频级对齐：

$$ \mathcal{L} = \alpha \cdot \text{Mean}(\mathbf{M}_f[\text{trU} \cup \text{trL}]) + \beta \cdot \text{Mean}(\mathbf{M}_f[\text{dia}]) + \gamma \cdot \text{Mean}(\mathbf{M}_v[\text{trU} \cup \text{trL}]) $$

该公式通过惩罚负样本相似度并拉近正样本，确保精化后的GPS序列在帧级与视频级均与真实轨迹对齐，有效消除Phase I的序列级错误。

## 实验评估

实验在MSLS、GAMa和CityGuessr68k数据集上进行，基线覆盖分类（PlaNet, ISNs, GeoDecoder）、检索（GeoCLIP）及视频分类（CityGuessr）路线，但未包含跨视角专用基线（如Loc2），因任务定义不同。在MSLS数据集上，VidTAG在1km阈值下达到41.0%准确率，较GeoCLIP-FineTuned的22.5%提升18.5个百分点；在CityGuessr68k城市级预测中，VidTAG达到94.9%，较CityGuessr的69.6%提升25.3个百分点。

| 数据集 | 方法 | 1km准确率 (%) | 5km准确率 (%) | 25km准确率 (%) |
| :--- | :--- | :--- | :--- | :--- |
| MSLS | GeoCLIP-FineTuned | 22.5 | 63.0 | 93.9 |
| MSLS | VidTAG | 41.0 | 76.7 | 97.9 |
| GAMa | GeoCLIP-FineTuned | 28.3 | 57.8 | 89.1 |
| GAMa | VidTAG | 53.1 | 77.8 | 94.4 |

消融实验显示，TempGeo模块对1km准确率贡献最大，移除后从41.0%降至22.5%；GeoRefiner主要改善轨迹质量，DFD从3.87降至3.01，MRD从1.07降至0.41。Gallery分辨率从1km降至0.1km时，1km准确率从38.6%提升至41.0%，但边际收益递减，0.1km分辨率下计算成本显著增加。

评估指标包含帧级准确率、中位距离误差、DFD与MRD，但未报告置信区间。代码未公开，超参数与GPU配置仅在补充材料中简述，可复现性受限。MSLS数据集主要面向同视角检索，其全球覆盖度与地理多样性可能高估模型在真实全球场景下的泛化能力。

## 关联研究分析

从问题动机看，VidTAG与CityGuessr均针对全球视频定位，但CityGuessr采用整视频级分类，忽略帧级时序一致性，导致轨迹无法重建；VidTAG通过帧级检索与TempGeo对齐，实现了轨迹级输出。这一差异源于任务定义：CityGuessr关注城市识别，VidTAG关注轨迹重建。VidTAG未探索整视频级特征聚合，可能在长视频场景中因序列长度限制而性能下降。

从方法设计看，VidTAG与GeoCLIP共享Location Encoder与对比学习框架，但GeoCLIP仅处理单帧，VidTAG引入TempGeo与GeoRefiner解决时序问题。与跨视角定位方法（如Loc2）相比，VidTAG未引入3D几何先验（如点云、BEV），仅依赖2D特征与GPS坐标。这一设计选择源于全球尺度下3D重建的计算不可行性，但可能限制其在复杂城市环境下的细粒度精度。VidTAG未验证3D几何先验的引入是否能在保持实时性的同时提升亚米级精度。

## 总结

VidTAG解决的核心矛盾是全球尺度视频定位中精度与时序一致性的平衡。现有分类方法粒度粗，图像检索方法全球尺度不可行，VidTAG通过帧-GPS检索范式与TempGeo/GeoRefiner模块，实现了高精度且连贯的轨迹输出。在MSLS 1km阈值下，VidTAG达到41.0%准确率，较GeoCLIP提升18.5个百分点；在CityGuessr68k城市级预测中达到94.9%。其边界在于缺乏3D几何先验，仅依赖2D特征与GPS坐标，可能在复杂城市环境下的亚米级精度受限。当支持集增大到长视频序列时，TempGeo的全自注意力计算成本是否线性增长，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12159)