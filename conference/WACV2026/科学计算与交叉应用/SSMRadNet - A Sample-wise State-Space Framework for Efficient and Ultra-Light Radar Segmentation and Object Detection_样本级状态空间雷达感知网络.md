# WACV2026最新论文 ｜SSMRadNet : A Sample-wise State-Space Framework for Efficient and Ultra-Light Radar Segmentation and Object Detection ｜样本级状态空间雷达感知网络

研究机构：美国佐治亚理工学院

作者：Anuvab Sen、Mir Sayeed Mohammad、Saibal Mukhopadhyay

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_751eb9b19147)

> 自动驾驶系统在恶劣天气下依赖FMCW雷达进行全天候感知，但高分辨率雷达产生的海量原始数据在边缘设备上处理时面临算力与延迟的双重瓶颈。传统CNN与Transformer架构因计算复杂度随数据维度非线性增长，难以实时处理原始ADC信号。SSMRadNet通过双尺度状态空间模型（SSM）对样本与chirp序列进行线性复杂度建模，在保持分割精度的同时大幅降低计算开销。该方法在效率-精度帕累托前沿上占据显著优势，但检测任务性能未达最优，且跨帧状态管理的鲁棒性尚存疑。

## 研究背景

FMCW雷达通过发射线性调频信号并接收回波，将目标距离、速度与角度信息编码在原始模拟-数字转换（ADC）样本中。传统流程需经多级快速傅里叶变换（FFT）生成距离-多普勒-角度（RAD）张量，再提取稀疏点云供卷积神经网络（CNN）处理。这一流程不仅引入计算延迟，更在FFT阶段丢失了相位与极化等细粒度物理信息，导致弱信号丢失与角分辨率受限。为保留完整信息，直接处理原始ADC立方体成为趋势，但ADC数据量随天线数、chirp数与采样率呈乘积增长，对计算资源提出极高要求。

现有直接处理ADC的路线面临效率与精度的权衡困境。CNN路线（如FFT-RadNet）虽避免了部分FFT，但3D卷积的计算量随ADC维度非线性增长；Transformer路线（如T-FFT-RadNet）通过自注意力建模长程依赖，但二次方复杂度使其在处理长序列时延迟激增；递归路线（如ChirpNet）采用GRU逐chirp处理，虽降低了计算量，但感知精度受限。SSMRadNet的切入点在于引入状态空间模型（SSM），其计算复杂度与序列长度呈线性关系，且能捕获长程依赖，从而在保留原始ADC信息的同时，突破边缘部署的算力瓶颈。

## 核心方法

### 方法参照系

本文问题属于从原始雷达信号到鸟瞰图（BEV）语义感知的端到端映射。通用流程通常包含信号预处理（FFT/CFAR）、特征提取（CNN/Transformer）与空间解码。本文的关键差异在于摒弃了FFT与3D卷积，将ADC样本视为时序令牌，通过序列建模直接提取时空特征，避免了中间张量生成的计算开销与信息损失。

### 样本级Mamba块（Chirp内建模）

在ChirpNet等递归方法中，chirp内样本通常被展平后通过线性投影处理，当样本数 $S$ 与接收通道数 $N_{Rx}$ 较大时，该投影矩阵参数量激增且难以捕捉样本间的时间相关性。SSMRadNet在chirp内引入Mamba块，将每个ADC样本 $\mathbf{X}(t)$ 嵌入为实虚部拼接的向量，并通过因果卷积与SSM递归更新状态。其核心状态更新公式为：

$$ \mathbf{h}_{s} = \mathbf{h}_{s-1} \odot \mathrm{decay}_{s} + \tilde{x}_{s} \odot (dt_{s} \odot B_{\mathrm{mod},s}) $$

该公式通过可学习的衰减系数 $\mathrm{decay}_{s}$ 控制历史信息的保留比例，使模型能自适应地聚焦于当前样本与关键历史样本，从而在低算力下精确建模距离域结构。

### Chirp级Mamba块（Chirp间建模）

Chirp内特征提取后，需进一步建模chirp间的动态变化以区分静态背景与移动目标。传统方法常使用GRU或自注意力处理chirp序列，但前者长程依赖能力弱，后者计算开销大。SSMRadNet将chirp内特征聚合为chirp令牌，并沿chirp轴应用第二个Mamba块。其输出公式为：

$$ y_{s} = \sum_{j=1}^{d_{\text{state}}} \mathbf{h}_{s}^{(j)} C_{\mathrm{mod},s}^{(j)} + D \tilde{x}_{s} $$

该公式通过状态向量与调制参数的加权求和，结合跳跃连接，将chirp序列压缩为紧凑的帧级特征图。这种双尺度设计使模型能同时捕获chirp内的距离细节与chirp间的速度动态，实现了静态背景与动态目标的有效分离。

## 实验评估

实验在RADIal与RaDICaL数据集上进行，前者包含192虚拟通道的77 GHz成像雷达数据，后者为4接收通道的77 GHz雷达数据。基线覆盖CNN（FFT-RadNet）、Transformer（T-FFT-RadNet）与递归（ChirpNet）路线，但未包含扩散模型类基线。在RADIal分割任务中，SSMRadNet以1.67 GMACs的算力实现了0.79的mIoU，与T-FFT-RadNet（99.38 GMACs, 0.79 mIoU）精度持平，但算力降低60倍，延迟从52.90 ms降至14.20 ms。

| 模型 | GMACs | Params (M) | mIoU | mAP | Latency (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T-FFT-RadNet | 99.38 | 10.29 | 0.79 | 0.88 | 52.90 |
| FFT-RadNet | 146.58 | 3.79 | 0.74 | 0.97 | 53.59 |
| ChirpNet | 24.70 | 57.72 | 0.64 | — | 27.33 |
| SSMRadNet | 1.67 | 0.31 | 0.79 | 0.83 | 14.20 |

消融实验揭示了特征聚合策略对性能的关键影响。仅使用chirp-SSM时mIoU为0.65，引入样本级SSM后提升至0.68，而采用AvgPool聚合样本特征后mIoU跃升至0.75，最终通过通道扩展达到0.79。这表明样本级时序建模与合理的特征聚合是精度提升的核心，而非单纯增加模型深度。

评估协议采用0.8-0.2训练验证划分，指标涵盖mIoU、mAP、Chamfer Distance与计算效率。局限在于：检测任务中SSMRadNet的mAP（0.83）低于FFT-RadNet（0.97），论文归因于解码器简化，但未提供消融验证；跨帧状态保持实验仅在10帧短序列上进行，未测试长序列下的状态漂移；代码未开源，超参数细节（如Mamba块内部维度）未完全披露，可复现性受限。

## 关联研究分析

从方法设计看，SSMRadNet与ChirpNet同属序列处理路线，但ChirpNet依赖GRU的固定状态转移，难以自适应调整历史权重，而SSMRadNet通过Mamba的可学习衰减机制，在低算力下实现了更灵活的时序建模。这一差异源于SSM的线性复杂度特性，使其能在边缘设备上处理更长的chirp序列，而ChirpNet受限于GRU的递归深度，长序列下信息衰减严重。

从问题动机看，SSMRadNet与T-FFT-RadNet均直接处理ADC数据，但T-FFT-RadNet追求精度上限，采用Transformer的二次方注意力，适合云端部署；SSMRadNet则针对边缘场景，以线性复杂度换取实时性，牺牲了部分检测精度。这种取舍反映了任务特性对架构选择的决定：当算力受限且实时性要求高时，SSM的线性复杂度优势凸显；当算力充足且精度优先时，Transformer的长程依赖建模能力更具价值。SSMRadNet在检测任务上的性能差距，是否源于SSM对局部细节的捕捉能力弱于自注意力，论文未给出明确回答。

## 总结

SSMRadNet旨在解决FMCW雷达原始ADC数据在边缘设备上的实时处理难题，其切入点在于利用SSM的线性复杂度特性，突破CNN与Transformer的算力瓶颈。通过双尺度Mamba块对样本与chirp序列进行建模，该方法在RADIal数据集上以1.67 GMACs的算力实现了0.79的mIoU，与Transformer基线精度持平但算力降低60倍。然而，检测任务中mAP（0.83）低于CNN基线（0.97），且跨帧状态保持仅在短序列上验证，暴露了SSM在长程动态场景下的鲁棒性局限。当chirp序列长度从256扩展至数千时，SSM的状态衰减机制是否仍能保持对早期关键样本的敏感度，论文未提供实验证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_751eb9b19147)