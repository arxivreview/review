# CVPR2026最新论文 ｜Abstract 3D Perception for Spatial Intelligence in Vision-Language Models ｜抽象感知驱动的空间智能增强

研究机构：清华大学、美国哈佛大学

作者：Yifan Liu、Fangneng Zhan、Kaichen Zhou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.10946)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10946)

> 视觉语言模型（Vision-Language Model, VLM）在3D空间推理任务中受限于2D训练数据的模态鸿沟，导致其难以从平面图像恢复度量空间结构。现有训练式方法依赖昂贵的3D监督数据且无法适配闭源大模型，而纯2D推理又缺乏几何约束。SandboxVLM提出“抽象感知”范式，通过视频扩散生成多视图先验，并利用代理点提升与多视图投票聚类构建符号化3D边界框，以零样本方式注入VLM。该框架在SAT-Real基准上较基线提升8.3%，验证了粗粒度结构表示的有效性，但其对深度估计精度的依赖及计算开销仍是潜在瓶颈。

## 研究背景

VLM处理3D场景时面临的核心困境是输入模态与任务需求的错位。模型预训练基于2D图像与1D文本，缺乏对深度、体积和空间关系的内在表征，导致在视角变换、相对位置估计等任务中表现不佳。这种2D语义与3D几何的模态鸿沟，使得模型难以从单视图图像中准确推断立体结构，成为制约具身智能应用的关键障碍。

早期3D-LLM（Chen et al., 2025）等工作通过Q-Former对齐点云特征与LLM，确立了多模态编码基线，但依赖密集3D监督与专用架构，难以扩展至通用VLM。SpatialVLM（Guo et al., 2025）转向数据驱动，利用合成数据微调，但牺牲了可解释性且无法利用闭源模型。SandboxVLM的切入点在于借鉴人类“抽象感知”机制，即通过粗粒度结构线索而非精确几何重建进行空间推理，从而在免训练条件下弥合模态鸿沟。

## 核心方法

### 方法参照系

本文问题属于测试时扩展（Test-time Scaling）范畴，旨在不修改模型参数的前提下增强VLM的3D推理能力。与MindJourney等依赖视频序列隐式先验的方法不同，SandboxVLM将多视图信息显式结构化为3D符号表示，以解决隐式表示可解释性差的问题。

### 多视图先验生成与抽象控制

设计动机在于解决单视图图像3D信息不足导致的歧义。传统方法直接输入原始图像，缺乏跨视角对应关系。SandboxVLM引入视频扩散模型 $G_\theta$ 生成多视图序列，并通过抽象控制机制引导视角生成。给定查询 $q$ 和图像 $I_v$，VLM从预定义动作集 $\mathcal{T}$ 中选择最相关方向 $c^*$，实例化为 $M$ 条相机轨迹 $\{\hat{\mathbf{T}}_{v[m],t}\}$。条件生成公式为：

$$ X_{v[m],t} = G_\theta(I_v, \hat{\mathbf{T}}_{v[m],t}) $$

该机制确保计算资源聚焦于任务相关视角，避免无关视角引入噪声，提升了后续3D重建的信息密度。

### 代理点提升与多视图投票聚类

设计动机在于解决密集点云重建计算冗余及噪声敏感问题。常规方法直接反投影所有像素，易受深度估计误差影响。SandboxVLM提出代理点（Proxy Points）稀疏化策略。首先，VLM识别任务相关物体并定位中心点，分割模型生成掩码 $\mathbf{M}_{v,i}$。经形态学侵蚀后，采用最远点采样（FPS）选取固定数量像素作为2D代理 $S_{v,i}$。利用深度图 $D_v$ 和相机参数 $\mathbf{K}, Rt$ 反投影至3D空间：

$$ \mathbf{p} = \mathbf{K}^{-1} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} \cdot D_v(x,y) $$

随后，通过多视图投票过滤噪声点。定义“Agree to”关系，若3D点 $\mathbf{p}$ 在 $N$ 个视图中均满足距离阈值 $\delta$，则视为可靠点。最终，利用DBSCAN聚类剩余点，并通过PCA拟合有向3D边界框（OBB），形成紧凑的“3D Sandbox”表示。

## 实验评估

实验在SAT、BLINK、EmbSpatial及PhysBench基准上进行，基线涵盖GPT-4o、Qwen2.5-VL等通用VLM，以及RoboBrain2.0等训练式模型和MindJourney等测试时扩展方法。缺失SR-3D、SpatialStack等专用3D架构基线，限制了与训练式SOTA的直接对比。

| 方法 | Spatial-Avg | BLINK-Spatial | BLINK-Depth | SAT-Real | PhysBench |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-5-mini | 78.3 | 82.3 | 79.0 | 75.4 | 58.7 |
| MindJourney | 79.1 | 83.1 | 74.7 | 78.7 | 54.9 |
| SandboxVLM | 81.4 | 83.7 | 82.3 | 84.1 | 58.3 |

SandboxVLM在Spatial-Avg上达81.4%，较GPT-5-mini提升2.9%，在SAT-Real上较MindJourney提升5.4%。消融实验显示，多视图先验贡献3.3%增益，而3D坐标文本提示（80.8%）优于渲染代理点（77.0%），表明当前VLM仍具语言中心特性，视觉模态未完全利用。

| 消融设置 | Average | EgoM | ObjectM | GoalAim | ActCons | Perspect |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Vanilla VLM | 75.4 | 82.6 | 73.9 | 76.5 | 81.1 | 63.6 |
| Multi-View Images Only | 78.7 | 87.0 | 73.9 | 85.3 | 81.1 | 66.7 |
| 3D Coordinate Text | 80.8 | 95.6 | 85.7 | 85.3 | 81.1 | 66.7 |
| Full SandboxVLM | 84.1 | 100.0 | 82.6 | 92.9 | 79.4 | 70.0 |

评估边界方面，论文未报告置信区间，且SAT-Synth子集因API限制仅报告部分结果。代码未开源，超参数如 $M, T, N, \delta$ 仅在补充材料中提及，复现依赖VGGT与SEVA等外部组件的精确配置。

## 关联研究分析

从问题动机看，SandboxVLM与Map2Thought（Gao et al., 2026）均追求显式几何表示，但Map2Thought构建度量认知地图以支持长程记忆，而SandboxVLM聚焦单查询下的即时空间推理。差异根源在于任务特性：Map2Thought面向动态场景的全局理解，需持久化存储；SandboxVLM面向静态场景的定性关系判断，无需维护全局状态。这种取舍使得SandboxVLM在零样本场景下更轻量，但牺牲了跨帧一致性。

从方法设计看，SandboxVLM与SR-3D（Cheng et al., 2025）均利用多视图信息，但SR-3D通过共享视觉令牌空间进行训练式对齐，而SandboxVLM通过视频扩散生成伪多视图进行推理时增强。SR-3D依赖3D训练数据，性能受数据规模制约；SandboxVLM依赖生成模型先验，性能受生成质量制约。当视频扩散模型生成的视角存在物理不一致性时，SandboxVLM的投票机制能否有效过滤此类系统性误差，论文未给出回答。

## 总结

SandboxVLM旨在解决VLM在零样本3D空间推理中因2D训练导致的模态鸿沟。现有训练式方法依赖昂贵3D数据且无法适配闭源模型，而纯2D推理缺乏几何约束。本文通过抽象感知范式，利用视频扩散生成多视图先验，并经代理点提升与多视图投票聚类构建符号化3D边界框，以免训练方式注入VLM。实验表明，该方法在SAT-Real上较基线提升8.3%，在BLINK-Spatial上达83.7%，验证了粗粒度结构表示的有效性。然而，消融显示3D坐标文本提示优于视觉渲染，暗示当前VLM对视觉几何信息的利用仍不充分。当输入场景包含复杂遮挡或动态物体时，基于静态边界框的抽象表示能否维持推理稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10946)