# CVPR2026最新论文 ｜DeltaQuant: 4-bit Video Diffusion Models with Spatiotemporal Delta Smoothing ｜时空差分平滑的视频扩散模型4位量化

研究机构：美国麻省理工学院、美国卡内基梅隆大学

作者：Xingyang Li、Samuel Tesfai、Zhekai Zhang 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c3dc3c6c475)

> 视频扩散模型在去噪过程中激活值异常值随时间步剧烈波动，导致静态校准的量化方法失效。现有方案如SVDQuant依赖离线固定的低秩分支，无法适应这种动态性。本文利用视频数据固有的时空冗余，将激活分解为高精度核心Token与低精度差分Token，以在线均值计算替代静态平滑。该方法在Wan2.2上实现了2.9倍模型压缩与2.3倍显存降低，但仅验证了特定分辨率下的性能，未探讨不同视频内容复杂度对时空相似性的影响。

## 研究背景

视频扩散模型（Video Diffusion Model, VDM）基于DiT架构处理长序列时空Token，其推理瓶颈已从注意力机制转移至线性层。量化技术通过降低权重与激活精度来加速线性层计算，但VDM中激活分布的非均匀性远超图像模型，传统均匀量化在4位精度下导致严重精度崩塌。

VDM的激活异常值具有显著的时间步依赖性。在去噪初期，某些通道幅值极大，而在后期则趋于平缓。这种动态变化使得基于单一时间步校准的静态平滑策略（如SmoothQuant）失效：为早期时间步优化的缩放因子会恶化后期时间步的量化误差。SVDQuant虽通过权重低秩分解吸收了部分异常值，但其激活平滑仍依赖离线静态校准，无法应对VDM中跨时间步的分布漂移。在线SVD虽理论上可行，但计算开销在推理阶段不可接受。

本文切入点在于利用视频数据的时空局部相似性。相邻帧及空间邻近Token的激活值高度相关，这一特性与视频编码中的帧间预测原理一致。通过在线计算局部时空立方体的均值作为核心Token，并将剩余差分量化为4位，可在不增加显著计算开销的前提下，动态消除异常值对量化步长的支配效应。

## 核心方法

### 方法参照系

本文问题属于后训练量化（Post-Training Quantization, PTQ）范畴，但针对VDM的动态激活特性进行了改造。标准PTQ流程假设激活分布静态，通过离线校准确定缩放因子。本文的关键差异在于引入在线时空分解，将静态的通道级平滑替换为动态的Token级差分量化，以适配VDM中随去噪步骤变化的激活分布。

### 时空立方体分解

针对静态平滑无法处理时间步动态异常值的问题，本文提出时空立方体分解。将激活张量$X \in \mathbb{R}^{N \times C_i}$重塑为$T \times H \times W \times C_i$，并划分为$K$个大小为$t \times h \times w$的非重叠立方体。对每个立方体$X^{(k)}$，计算其均值作为核心Token $\bar{X}^{(k)}$，并计算差分Token $\tilde{X}^{(k)}$：

$$
\bar{X}^{(k)} = \frac{1}{thw} \sum_{n=1}^{thw} X_n^{(k)}, \quad \tilde{X}^{(k)} = X^{(k)} - \bar{X}^{(k)}
$$

该公式的物理含义是提取局部时空平均趋势作为基准，剩余部分即为局部波动。由于视频帧间及空间邻近Token高度相似，差分Token的幅值与方差显著小于原始激活，从而降低了量化难度。

### 混合精度量化与内核融合

差分Token $\tilde{X}$量化为4位（FP4），核心Token $\bar{X}$量化为8位（FP8）。线性层计算分解为两部分：

$$
X^{(k)}W \approx Q_8(\bar{X}^{(k)})Q_4(W) + Q_4(\tilde{X}^{(k)})Q_4(W)
$$

第一项在FP8 Tensor Core上执行，作为动态Token偏置广播至立方体内所有Token；第二项在FP4 Tensor Core上执行。这种设计利用了硬件对不同精度Tensor Core的支持，将算法层面的混合精度转化为实际的速度提升。核心Token的FP8精度比BF16略低，但比FP4高，且FP8 Tensor Core吞吐量是FP4的4倍，实现了精度与速度的平衡。

## 实验评估

实验在Wan2.2（27B参数）和LTX-Video（13B参数）上进行，评估指标包括LPIPS、PSNR、SSIM及VBench子项。基线覆盖SmoothQuant、SVDQuant、S2Q-VDiT、Q-VDiT及GGUF 4位权重量化。

| 模型 | 方法 | LPIPS (↓) | PSNR (↑) | Vision Reward (↑) |
| :--- | :--- | :--- | :--- | :--- |
| Wan2.2 I2V | SVDQuant | 0.165 | 21.9 | 0.134 |
| Wan2.2 I2V | GGUF W4A16 | 0.137 | 23.2 | 0.141 |
| Wan2.2 I2V | DeltaQuant | 0.128 | 23.2 | 0.146 |
| Wan2.2 T2V | SVDQuant | 0.354 | 17.5 | 0.083 |
| Wan2.2 T2V | DeltaQuant | 0.338 | 17.7 | 0.083 |

DeltaQuant在Wan2.2 I2V任务上LPIPS为0.128，优于SVDQuant的0.165，且Vision Reward达到0.146，超过GGUF W4A16的0.141。在T2V任务上，DeltaQuant的LPIPS为0.338，略优于SVDQuant的0.354。这表明时空差分分解在保持生成质量方面优于静态平滑方法。

消融实验显示，立方体大小对性能影响显著。增大立方体尺寸会降低时空相似性捕获能力，导致性能下降。自适应立方体大小策略（前30%时间步用16，后70%用64）比统一大小32提升PSNR 0.5。核心Token精度方面，FP8量化比BF16 PSNR更高，而FP4量化导致PSNR下降1.3，验证了FP8作为核心Token精度的合理性。

评估边界方面，实验仅在720p和480p分辨率下进行，未测试更低分辨率或更长视频时长。代码未公开，超参数如立方体尺寸$t, h, w$的选取依赖经验。GPU环境限定为NVIDIA RTX 5090，其他硬件平台的兼容性未验证。

## 关联研究分析

从问题动机看，DeltaQuant与SVDQuant均旨在解决激活异常值导致的量化精度崩塌，但SVDQuant依赖离线静态校准，适用于激活分布相对稳定的图像扩散模型。DeltaQuant针对VDM中激活分布随时间步剧烈变化的特性，引入在线时空分解。这一差异源于VDM的时序生成机制，使得静态校准无法覆盖所有去噪步骤的分布变化。SVDQuant的权重低秩分解在DeltaQuant中被保留，但激活处理从静态平滑转为动态差分，体现了任务特性对方法设计的决定性影响。

从方法设计看，DeltaQuant与SmoothQuant同属平滑类方法，但SmoothQuant通过离线通道缩放迁移量化难度，而DeltaQuant通过在线Token均值分解降低差分幅值。SmoothQuant的静态缩放因子在VDM中会导致某些时间步的异常值被放大，而DeltaQuant的在线计算能实时适应当前时间步的分布。此外，DeltaQuant与硬件协同设计紧密结合，利用FP8/FP4 Tensor Core实现混合精度计算，而SmoothQuant通常依赖通用INT8/INT4内核，未充分利用新兴浮点格式的硬件优势。

## 总结

DeltaQuant解决了视频扩散模型中激活异常值的时间步动态性导致的静态量化失效问题。其切入点在于利用视频数据的时空局部相似性，通过在线计算局部均值作为核心Token，将量化难度从原始激活转移至幅值更小的差分Token。该方法在Wan2.2上实现了2.9倍模型压缩与2.3倍显存降低，且LPIPS优于SVDQuant。然而，实验仅在特定分辨率和硬件平台上进行，未探讨不同视频内容复杂度（如高动态场景 vs 静态场景）对时空相似性的影响。当视频内容包含剧烈运动或快速场景切换时，时空立方体内的Token相似性是否仍足以支持4位差分量化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_5c3dc3c6c475)