# HuggingFace最新推荐论文 ｜SIMART: Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM ｜SIMART：基于稀疏3D VQ-VAE的多模态大语言模型铰接资产生成

研究机构：新加坡南洋理工大学

作者：Chuanrui Zhang、Minghan Qin、Yuang Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.23386)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23386)

> 导读 铰接物体重建旨在从视觉观测中同时恢复几何外观与运动学结构，其核心价值在于为机器人操作提供可交互的数字孪生。现有方法多采用多阶段流水线，部件分割与关节估计解耦导致误差累积，且直接回归URDF常牺牲几何保真度。SIMART提出统一的多模态大语言模型（MLLM）框架，通过稀疏3D VQ-VAE将静态网格转化为Sim-ready资产，在保留输入几何的同时生成部件分割与运动学参数。该方法在PartNet-Mobility及AIGC数据上超越了基于2D输入的MLLM基线，但其对高质量静态网格输入的依赖及复杂运动链处理能力仍存疑。

## 研究背景

铰接物体由通过关节连接的刚性部件组成，其建模需同时恢复几何与运动学结构。URDF（Unified Robot Description Format）是描述机器人运动学链与物理属性的标准格式，包含关节类型、轴、枢轴点及限位。将静态3D网格转化为URDF资产，需解决部件边界识别与运动参数推断的耦合问题。传统方法依赖专家手动建模，成本高且难以规模化，而自动化方法需在几何保真度与运动学准确性间取得平衡。

主流路线分为优化式重建与前馈/生成式建模。优化式方法（如PARIS、ArtGS）基于多视图或多状态观测，通过可微渲染迭代优化，精度高但速度慢且泛化能力受限。前馈式方法（如URDFormer、Particulate）从单图或网格直接预测URDF，效率高但几何细节粗糙。生成式方法（如SINGAPO、SPARK）利用扩散模型或VLM先验合成资产，多样性强但物理可行性不足。现有MLLM驱动方法（如Articulate-Anything、PhysX-Anything）尝试利用语义推理消解运动歧义，但受限于2D输入缺乏3D空间定位，或密集体素编码导致内存溢出。SIMART的切入点在于：利用稀疏3D表示解决MLLM处理复杂几何的计算瓶颈，统一部件分割与运动学预测，实现从静态网格到Sim-ready资产的端到端转换。

## 核心方法

### 方法参照系

本文问题属于“从静态资产到动态资产的转换”，即自动化为静态网格添加铰接结构。与通用3D生成不同，本文以输入网格为条件，要求输出严格保持输入几何保真度，同时生成语义一致的部件分割与URDF参数。关键差异在于：传统生成方法合成新几何，而本文需对已有几何进行“功能化”分解与运动学标注。

### 稀疏3D VQ-VAE表示

密集体素编码将$O(N^3)$空间全部映射为token，大量token用于空空间，导致MLLM上下文长度爆炸。SIMART引入稀疏3D VQ-VAE，仅编码占据表面体素。对于每个潜在特征$z_i$，量化表示$\hat{z}_i$定义为：

$$
\hat{z}_i = \begin{cases}
\mathbf{e}_{zero} & \text{if } z_i \text{ is unoccupied} \\
\arg\min_{k} \| z_i - \mathbf{c}_k \|_2 & \text{if } z_i \text{ is occupied}
\end{cases}
$$

其中$\mathbf{e}_{zero}$为保留的零token，$\mathbf{c}_k$为码本向量。该设计跳过空空间，减少约70%的token数量，使MLLM能处理复杂多部件物体而不发生内存溢出。每个占据体素序列化为$\langle \text{voxel} \rangle [xyz] [K]$三元组，其中$xyz$通过线性映射$64x + 8y + z$编码空间位置，确保MLLM能进行细粒度几何推理。

### 统一MLLM推理与资产合成

MLLM骨干（Qwen3-VL-8B）接收视觉、几何与文本token的拼接序列，联合执行部件定位与URDF生成。输出包含部件级网格token与结构化URDF描述。为将离散的部件种子映射回高保真网格，SIMART采用图平滑算法：初始化顶点概率分布，通过高斯核计算顶点$v$属于部件$p$的初始概率：

$$
P(v \in p) \propto \exp\left(-\frac{d(v, S_p)^2}{2\sigma^2}\right)
$$

其中$d(v, S_p)$为顶点到部件$p$最近种子的距离，$\sigma$为尺度超参数。随后在网格邻接矩阵上迭代平滑，通过多数投票确定最终面标签。该设计解决了MLLM生成的离散token与连续网格表面之间的对齐问题，确保部件边界与输入几何严格一致，避免了生成式方法中常见的几何扭曲。

## 实验评估

实验在SIMART-Bench上进行，该基准整合了PartNet-Mobility（ID）与AIGC生成物体（OOD）。基线包括URDFormer（前馈回归）、Articulate-Anything/PhysX-Anything（2D/密集体素MLLM）及Particulate（点分割）。缺失优化式重建（如ArtGS）及纯扩散生成（如SINGAPO）的直接对比，因输入模态不同（网格vs图像/视频）。

| 方法 | ID Type $\uparrow$ | ID Axis $\downarrow$ | ID IoU $\uparrow$ | OOD Type $\uparrow$ | OOD Axis $\downarrow$ | OOD IoU $\uparrow$ |
|---|---|---|---|---|---|---|
| URDFormer | 0.496 | 0.585 | 0.002 | 0.544 | 0.557 | 0.016 |
| Articulate-Anything | 0.891 | 0.315 | 0.202 | 0.765 | 0.243 | 0.069 |
| PhysX-Anything | 0.686 | 0.312 | 0.128 | 0.658 | 0.481 | 0.100 |
| Particulate | 0.822 | 0.208 | 0.643 | 0.817 | 0.166 | 0.618 |
| **SIMART** | **0.928** | **0.080** | **0.690** | **0.831** | **0.136** | **0.777** |

SIMART在ID与OOD数据上均取得SOTA性能。ID数据上Axis Error 0.080，显著低于Articulate-Anything的0.315；OOD数据上IoU 0.777，远超Particulate的0.618，表明稀疏3D表示在泛化新拓扑结构时具有优势。

消融实验验证了稀疏机制与视觉特征的作用。

| 配置 | Type $\uparrow$ | Center $\downarrow$ | IoU $\uparrow$ | CD $\downarrow$ | Token Num $\downarrow$ |
|---|---|---|---|---|---|
| Dense Token | OOM | - | - | - | 4138 |
| Force Sparse | 0.661 | 0.157 | 0.678 | 0.100 | 862 |
| Zero Sparse | 0.794 | 0.108 | 0.745 | 0.074 | 516 |
| Vision (Ours) | **0.937** | **0.074** | **0.832** | **0.055** | **516** |

Dense Token导致OOM，Force Sparse虽降低token数但精度下降，Zero Sparse通过零token机制进一步减少冗余并提升精度。加入视觉特征后，Type Accuracy从0.794提升至0.937，表明视觉信息在消解几何歧义（如相似形态不同铰接结构）中起关键作用。

评估边界方面，论文未报告置信区间，且ID数据可能受训练分布影响。代码未开源，超参数（如$\sigma$）细节有限。指标覆盖运动学（Type, Axis, Origin）与几何（IoU, CD），但缺乏物理仿真稳定性（如碰撞率）的量化评估。

## 关联研究分析

从问题动机看，SIMART与Articulate-Anything同属MLLM驱动路线，但后者仅依赖2D图像输入，缺乏3D空间定位能力，导致关节轴估计易受视角影响。SIMART通过稀疏3D VQ-VAE提供显式空间坐标token，使MLLM能直接推理3D几何关系，从而在Axis Error上取得显著优势。这一差异源于任务特性：2D输入无法唯一确定3D关节轴，而3D原生表示消除了视角歧义。

从方法设计看，SIMART与PhysX-Anything均使用MLLM生成3D资产，但PhysX-Anything采用密集体素编码，导致内存开销大且需下采样，牺牲几何细节。SIMART的稀疏机制不仅解决效率问题，还通过保留占据表面细节提升了IoU。然而，SIMART依赖高质量静态网格输入，而PhysX-Anything可从文本或图像生成新几何。当输入网格本身存在拓扑错误或缺失时，SIMART的“保真”策略可能放大输入缺陷，而生成式方法可能通过先验补全。这种对输入质量的依赖是SIMART与生成式方法的根本分歧，也是其在野外场景应用的主要限制。

## 总结

SIMART旨在解决静态3D网格向Sim-ready铰接资产自动化转换中的几何保真度与运动学准确性矛盾。现有方法或因解耦流水线导致误差累积，或因密集体素编码受限于计算资源。SIMART通过稀疏3D VQ-VAE减少70% token冗余，结合Qwen3-VL-8B统一执行部件分割与URDF生成，在PartNet-Mobility ID数据上实现0.080的Axis Error，OOD数据上实现0.777的IoU。其边界在于：方法假设输入网格拓扑正确且完整，对缺失内部结构或复杂闭环运动链的处理能力未经验证；且评估主要基于几何与运动学指标，缺乏物理仿真中碰撞检测与动力学稳定性的量化证明。当输入网格包含非流形结构或高自由度串联关节时，稀疏VQ-VAE的量化误差是否会累积导致运动学失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23386)