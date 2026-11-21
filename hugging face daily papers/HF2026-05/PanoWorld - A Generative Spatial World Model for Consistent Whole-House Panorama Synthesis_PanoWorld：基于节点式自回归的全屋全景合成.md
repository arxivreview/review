# HuggingFace最新推荐论文 ｜PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis ｜PanoWorld：基于节点式自回归的全屋全景合成

作者：Jinrang Jia、Zhenjia Li、Yijiang Hu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17916)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17916)

> 全屋VR漫游生成需同时满足单帧视觉保真度与跨房间几何一致性，现有2D扩散模型缺乏持久空间记忆，而单体3D生成在房屋尺度下计算成本过高且纹理细节丢失。PanoWorld将任务重构为离散节点式自回归生成，利用Floorplan Shell提供全局几何约束，结合动态3DGS缓存维持局部外观记忆，通过解耦几何与纹理引导实现跨节点一致性。该方法在RealSee3D重建任务中PSNR达29.2361，显著优于基线，但其依赖Floorplan精度且未处理动态物体，节点式离散生成是否牺牲连续视角平滑性仍存疑。

## 研究背景

当相机在室内移动时，2D扩散模型虽能生成高保真全景，但同一门框或沙发在不同视角下可能呈现不同形状与材质，这种缺乏持久空间记忆的特性导致全屋漫游出现几何崩坏。为解决此问题，研究者引入3D高斯泼溅（3D Gaussian Splatting, 3DGS）作为可渲染空间记忆，但传统3DGS重建需处理全量历史视图，计算复杂度随路径长度线性增长，难以扩展至多房间场景。此外，标准自注意力机制在多房间视图中会导致纹理跨墙泄漏，产生鬼影几何，需引入拓扑感知机制抑制跨房间特征干扰。

全屋全景合成面临的核心矛盾是2D生成的高纹理保真度与3D重建的几何一致性之间的权衡。主流路线中，纯2D方法如DreamHome-Pano缺乏跨节点一致性模块，而单体3D生成方法如NeRF在房屋尺度下内存占用高且推理缓慢。PanoWorld的切入点在于借鉴商业VR漫游的节点式导航逻辑，将连续6-DoF生成转化为离散节点自回归过程，通过Floorplan Shell提供全局坐标框架，利用局部3DGS缓存增量更新，避免全历史重建的计算瓶颈。

## 核心方法

### 节点式自回归生成框架

PanoWorld将全屋合成建模为节点图上的自回归过程，输入为Floorplan $F$、风格条件 $s$ 及目标全景位姿集合 $V_{tar}$。与连续视频生成不同，该框架仅生成离散节点全景，节点间通过拓扑邻接关系连接。Floorplan被转换为粗粒度3D Shell $S$，渲染为几何代理 $G_i$ 提供低频结构约束，而3DGS缓存 $C$ 作为动态空间记忆，通过局部增量更新维持跨节点外观一致性。该设计将计算复杂度从全历史视图降至局部拓扑相关节点，使多房间场景下的重建成本保持近似常数。

### 房间感知全景LRM

针对多房间视图中纹理跨墙泄漏问题，PanoWorld设计房间感知全景大型重建模型（Room-Aware Panoramic LRM）。该模块采用前馈网络从多视角全景预测局部3DGS增量 $\Delta C_t$，核心创新在于房间感知分组注意力（Room-Aware Group Attention, RAGA）。对于节点 $i$ 和 $j$ 的token，注意力掩码 $M_{ij}$ 定义为：

$$
M_{ij} = \begin{cases}
0 & \text{if } i, j \in \text{same room or connected doorway} \\
-\infty & \text{otherwise}
\end{cases}
$$

该掩码允许同房间内密集交互，仅通过门洞节点限制跨房间通信，防止无关视图特征混合。此外，采用循环位置编码（Circular PRoPE, CPRoPE）将水平RoPE坐标映射为周期性整数谐波，确保全景接缝处注意力连续，解决等距圆柱投影（Equirectangular Projection, ERP）边界不连续问题。

### 拓扑感知渐进式3DGS缓存

为避免全历史重建，PanoWorld引入拓扑感知渐进式缓存策略。对于新节点 $v_t$，仅使用同房间历史节点 $N_{same}$ 和门洞边界节点 $N_{door}$ 构建局部上下文，预测局部3DGS增量 $\Delta C_t$。合并时，仅当新高斯与现有高斯属于同房间、中心距离 $\|\mu_a - \mu_b\|_2 < \tau_\mu \min(\bar{\sigma}_a, \bar{\sigma}_b)$ 且视角余弦相似度大于 $\tau_v$ 时才进行融合。外观属性采用置信度加权策略：零阶球谐系数（SH）平滑混合，高阶SH严格继承主导高斯，避免数值平均破坏高频视角依赖特征。该机制使缓存随漫游路径增长，同时保持每节点重建成本恒定。

## 实验评估

实验在自建Floorplan基准（7场景，126全景）和RealSee3D held-out（50场景）上进行，基线覆盖DreamHome-Pano、OmniRoam、Nano Banana 2等2D生成与长时程视频方法，但缺少CubeComposer等Cubemap表示基线。全景合成任务中，PanoWorld的跨节点一致性指标PSNRov达22.1365，显著优于OmniRoam的16.3862和DreamHome-Pano的15.4022，但美学质量HPSv3为7.9564，低于Nano Banana 2的9.5483，表明该方法优先保证几何一致性而非单帧美学。

| 方法 | HPSv3 ↑ | CLIP-I Style ↑ | PSNRov ↑ |
|---|---|---|---|
| DreamHome-Pano | 8.5711 | 0.7785 | 15.4022 |
| OmniRoam | 6.1492 | 0.7201 | 16.3862 |
| Nano Banana 2 | 9.5483 | 0.7940 | 14.7476 |
| PanoWorld | 7.9564 | 0.7577 | 22.1365 |

消融实验显示，移除RAGA导致PSNR从29.2361降至21.7084，降幅最大，证实拓扑感知注意力对多房间重建的关键作用。移除CPRoPE使PSNRov从22.1365降至20.6109，但HPSv3仅微降，表明CPRoPE主要贡献于边界连续性而非单帧美学。移除视觉记忆（VM）和邻近视图条件（NV）均导致PSNRov下降约3.3，验证了解耦几何与外观引导的必要性。

| 变体 | PSNR ↑ | SSIM ↑ | LPIPS ↓ |
|---|---|---|---|
| Full panoramic LRM | 29.2361 | 0.8880 | 0.2225 |
| w/o CPRoPE | 28.1739 | 0.8622 | 0.2409 |
| w/o RAGA | 21.7084 | 0.8216 | 0.2916 |

评估指标PSNRov依赖Floorplan Shell投影，若Shell本身存在误差，该指标可能高估一致性。代码未开源，仅提供项目链接，可复现性受限。训练使用64块H200 GPU训练LRM七天，8块H200训练2D生成器四天，计算成本较高。

## 关联研究分析

从问题动机看，PanoWorld与OmniRoam均针对长时程全景生成，但OmniRoam侧重连续视频中的时间漂移抑制，采用自回归世界模型处理累积误差，而PanoWorld将任务重构为离散节点漫游，通过拓扑感知缓存避免全历史重建。这一差异源于任务特性：商业VR漫游多为节点式导航，用户视角跳跃而非连续移动，节点式生成更贴合实际应用，但牺牲了连续6-DoF视角的平滑性，论文未评估节点间插值质量。

从方法设计看，PanoWorld与CubeComposer同属3D感知路线，但CubeComposer采用Cubemap表示消除ERP极点失真，通过时空自回归实现4K生成，而PanoWorld坚持ERP表示，通过CPRoPE和RAGA解决边界与跨房间问题。这一选择可能源于ERP数据生态更成熟，且节点式生成对单帧分辨率要求低于连续视频，但论文未对比Cubemap在节点式任务中的表现，ERP在高分辨率下的极点失真是否影响全屋一致性，论文未给出回答。

## 总结

PanoWorld解决的核心矛盾是2D生成的高纹理保真度与3D重建的几何一致性之间的权衡，其切入点在于将连续视频生成转化为离散节点自回归，利用Floorplan Shell提供全局几何约束，结合局部3DGS缓存增量更新，避免全历史重建的计算瓶颈。该方法在RealSee3D重建任务中PSNR达29.2361，跨节点一致性PSNRov达22.1365，显著优于基线，但依赖Floorplan精度且未处理动态物体与镜面反射。当Floorplan存在门洞拓扑缺失或节点间距过大时，缓存引导效果减弱，节点式离散生成在学术上是否被视为对“视频生成”定义的偏离，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17916)