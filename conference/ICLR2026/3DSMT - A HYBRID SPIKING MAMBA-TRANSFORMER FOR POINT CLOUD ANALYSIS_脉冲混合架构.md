# ICLR2026最新论文 ｜3DSMT: A HYBRID SPIKING MAMBA-TRANSFORMER FOR POINT CLOUD ANALYSIS ｜脉冲混合架构

研究机构：安徽大学、天津大学

作者：zhiming Zhou、Yong He、Qiaoyun Wu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66519055)

> 导读 3D点云分析在边缘设备部署时面临计算能耗与精度的双重约束，传统人工神经网络（ANN）的浮点运算导致能耗过高，而现有脉冲神经网络（SNN）方案在精度上存在显著差距。本文切入点在于将Transformer的局部建模能力与Mamba的全局线性复杂度优势，共同嵌入到SNN的事件驱动框架中，以稀疏脉冲计算替代高能耗的浮点乘累加。具体做法是构建包含脉冲局部偏移注意力与脉冲Mamba块的混合架构。该方案在SNN类别中实现了精度与能效的平衡，但其精度上限仍低于顶级ANN模型，且未验证其在对抗攻击下的鲁棒性。

## 研究背景

点云数据的无序性导致标准序列模型难以直接应用，通常需通过最远点采样（FPS）与K近邻（KNN）构建局部Patch以引入几何结构。然而，这种离散化过程在人工神经网络（ANN）中依赖密集的浮点乘累加（MAC）操作，导致在无人机等边缘设备上能耗过高。为突破此瓶颈，脉冲神经网络（SNN）利用事件驱动的稀疏二进制脉冲通信，将计算转化为低能耗的加法与逻辑操作，其稀疏特性与点云分布天然契合。

Transformer架构凭借自注意力机制在点云全局依赖建模上表现优越，但其二次方计算复杂度限制了大规模点云的处理效率。状态空间模型（SSM）如Mamba以线性复杂度提供了替代方案，但现有SNN点云模型（如SPM、SPT）在精度上仍落后于ANN基线，且往往以牺牲过多精度换取低能耗。本文旨在解决SNN点云模型特征表示能力不足与训练机制不成熟的问题，通过混合架构平衡精度与能效。

## 核心方法

### 方法参照系

本文问题属于高效架构设计路线，但引入了SNN新范式。与标准Transformer/Mamba流程的关键差异在于：所有线性层与激活函数被替换为脉冲神经元层（SN），计算过程从连续浮点域转移至离散时空域，且引入了阈值与时间步作为关键超参数。

### 脉冲局部偏移注意力

局部几何特征提取通常依赖K-Norm与K-Pool进行特征传播与聚合，但传统注意力机制中的Softmax函数涉及高能耗的浮点运算。本文提出脉冲局部偏移注意力（SLOA），利用脉冲序列的非负性与稀疏性，通过逻辑与（AND）和累加（AC）操作直接计算注意力矩阵，避免了MAC操作。

$$ A = \text{AC}(\text{AND}(Q, K)) $$

该公式表明注意力权重通过脉冲信号的逻辑与运算和累加获得，物理含义是利用脉冲的稀疏性将高能耗的矩阵乘法转化为低能耗的逻辑运算，从而在保持局部几何细节捕获能力的同时大幅降低能耗。

### 脉冲Mamba块

全局特征融合通常采用双向扫描策略以缓解点云无序性，但标准Mamba仍依赖浮点运算。本文设计脉冲Mamba块（SMB），将输入特征转换为二进制脉冲序列，并通过双向扫描（L+SSM与C-SSM）捕获全局依赖。

$$ Z_3 = \text{SN}(\text{Lin}(Z_L \odot Z_G + Z_C \odot Z_G)) $$

其中 $\odot$ 表示Hadamard积，$Z_G$ 为稀疏脉冲门控矩阵。该设计通过门控机制选择性激活显著特征并抑制噪声，利用非因果Conv1D消除时间伪影，在实现线性复杂度全局建模的同时，通过脉冲稀疏化进一步降低特征空间冗余与能耗。

## 实验评估

实验在ModelNet40、ScanObjectNN、ShapeNetPart、S3DIS及SemanticKITTI上进行，基线覆盖ANN（PTv2/3, PointMamba, PCM）与SNN（SPM, SPT, E-3DSNN）。缺失最新轻量化Transformer（如LitePT）及纯SSM基线（如RWKV）的对比。

| 方法 | 类型 | ModelNet40 OA (%) | Energy (mJ) | ScanObjectNN PB-T50-RS OA (%) |
|---|---|---|---|---|
| PTv2 | ANN | 93.7 | 78.7 | 88.1 |
| PCM | ANN | 93.4 | 207.0 | 87.3 |
| SPM | SNN | 92.3 | 5.4 | 84.2 |
| 3DSMT (w/ vot.) | SNN | 95.2 | 4.3 | 92.0 |

3DSMT在ModelNet40上以95.2%的OA领先，能耗仅为4.3 mJ，较PCM降低48倍，较PTv2降低18倍。在ScanObjectNN最难的PB-T50-RS子集上，3DSMT以92.0%的OA超越SPM 7.8个百分点，且FLOPs更低（1.3G）。

| 配置 | ModelNet40 OA (%) | Energy (mJ) |
|---|---|---|
| No-MT (Baseline) | 92.1 | 3.3 |
| Only-MB (Bi-SSM) | 94.0 | 4.0 |
| Full-MBT (Hybrid) | 94.7 | 4.3 |

消融实验显示，混合架构（Full-MBT）较仅使用双向SSM（Only-MB）提升0.7个百分点OA，能耗仅增加0.3 mJ。双向SSM较单向SSM提升0.2个百分点OA且无额外能耗，表明双向扫描在无序点云处理中至关重要。阈值1.0与时间步3为最优组合，时间步超过3会导致性能下降。

评估指标包含OA、mIoU、能耗与FLOPs，但缺乏对抗鲁棒性测试。代码基于PyTorch与SpikingJelly实现，使用NVIDIA RTX 3090 GPU。投票策略（Voting）对最终精度有显著贡献，去除投票后ModelNet40 OA降至94.7%，ScanObjectNN PB-T50-RS降至90.4%。

## 关联研究分析

从问题动机看，3DSMT与LitePT均针对Transformer效率瓶颈，但LitePT通过解耦卷积与注意力降低参数量，仍依赖浮点运算；3DSMT则从计算范式层面引入SNN，以稀疏脉冲替代浮点MAC。差异根源在于任务场景：LitePT面向通用高性能骨干，3DSMT面向边缘设备低能耗部署，后者牺牲了部分精度上限（95.2% vs LitePT的82.5% mIoU在ScanNet，但基准不同）以换取数量级的能耗降低。

从方法设计看，3DSMT与Mamba3D同属SSM路线，但Mamba3D使用浮点双向扫描，3DSMT将其脉冲化。3DSMT引入SLOA模块弥补Mamba在局部几何细节上的不足，而Mamba3D依赖K-Norm/K-Pool。这种混合设计解决了单一SSM在无序点云局部结构感知上的弱点，但SNN的离散化是否导致几何细节丢失，论文未通过定量指标（如Chamfer Distance）深入验证，仅在分类任务中体现为精度差距。

## 总结

3DSMT旨在解决点云分析在边缘设备上的能耗与精度矛盾，通过SNN框架融合Transformer局部建模与Mamba全局线性复杂度优势。该架构在ModelNet40上取得95.2% OA与4.3 mJ能耗，在ScanObjectNN PB-T50-RS上达到92.0% OA，证明了SNN混合架构在能效-精度平衡上的有效性。其边界在于精度仍低于顶级ANN（如PTv3的73.6% mIoU在S3DIS），且未评估对抗攻击下的鲁棒性。当支持集增大或面对未知攻击时，SNN的离散脉冲机制是否具备内在鲁棒性，还是需额外正则化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66519055)