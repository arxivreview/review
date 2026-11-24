# WACV2026最新论文 ｜FARF-Net: Frequency-guided Adaptive Receptive Field Network for Edge-enhanced Polyp Segmentation ｜频率引导自适应感受野网络

作者：Xue Li、Aiwen Jiang、Hongqian Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_31d5193cdf20)

> 息肉分割的核心难点在于病变边界与周围黏膜在纹理和颜色上的高度相似性，导致现有模型在复杂成像条件下边界定位模糊。主流方法依赖固定膨胀率的卷积核，无法适应息肉内部与边缘区域截然不同的频率特性，且缺乏显式的边界建模机制，致使高频背景噪声易被误判为前景。本文切入点在于利用频域能量驱动卷积感受野的动态调整，并结合Kolmogorov-Arnold Networks（KAN）进行通道级非线性增强。通过构建频率引导的自适应感受野模块与双监督解码器，FARF-Net在五个基准数据集上实现了SOTA性能，但其33.71M参数量与11.91G FLOPs的计算开销是否满足临床实时部署需求，仍存疑。

## 研究背景

息肉分割任务要求模型在低对比度与高噪声环境下精确勾勒病变轮廓。这一过程受限于卷积神经网络（CNN）的局部感受野特性，固定膨胀率的卷积核难以同时捕捉边缘的高频细节与内部的低频语义。为解决此矛盾，研究者引入Transformer架构以增强全局上下文建模，但二次方计算复杂度阻碍了实时应用。与此同时，Kolmogorov-Arnold Networks（KAN）凭借其在通道维度的非线性拟合能力，为医学图像分割提供了替代MLP的新路径，但其直接应用往往带来高昂的计算与内存开销。

现有静态分割架构虽在精度上取得进展，但普遍存在两个瓶颈：一是空间域感受野的刚性，无法根据局部频率响应自适应调整；二是边界建模的缺失，多数方法依赖浅层边缘线索或辅助分支，缺乏跨多尺度语义空间的显式边界机制。这导致在小型息肉或边界模糊场景中，分割结果常出现锯齿状伪影或区域遗漏。FARF-Net针对这一痛点，将频域分析与KAN架构结合，旨在通过频率驱动的动态卷积与通道级非线性增强，解决固定感受野与边界模糊的双重失效问题。

## 核心方法

### 方法参照系

FARF-Net基于编码器-解码器范式，采用Pyramid Vision Transformer v2（PVTv2）作为骨干网络提取多尺度特征。与标准U-Net变体不同，本文在特征增强阶段引入频率驱动的自适应机制，并在解码阶段增加高频噪声抑制门控，以解决固定感受野无法适应异质频率分布的问题。

### EdgeKAN模块

EdgeKAN模块旨在补偿PVTv2在局部边界感知上的不足，通过KAN实现通道级非线性建模。针对直接采用通用KAN层导致的计算开销过大问题，本文设计了LiteDWSKAN与Token-KAN两种变体。LiteDWSKAN作用于中层特征，通过1×1卷积嵌入特征后，利用可学习样条激活函数进行通道级非线性映射：

$$ \tilde{x}_i(b, h, w) = \sum_{j=1}^{d} w_j \cdot \phi_j(x_{embed}^i[b, :, h, w]) $$

其中 $\phi_j(\cdot)$ 为分段线性B样条函数，$w_j$ 为通道权重。该设计避免了Token化，适合高分辨率中间特征。Token-KAN则作用于深层低分辨率特征，通过三次B样条函数构建分层非线性映射，捕捉长程轮廓一致性。这种分层策略解决了传统CNN在复杂边界区域特征表达不足的问题，提升了模型对模糊边缘的感知能力。

### ARF与FGDS解码器

ARF模块基于EdgeKAN输出，利用Haar小波变换提取局部频率能量 $E_i(h, w)$，并据此动态调整卷积膨胀率 $d_i(h, w)$：

$$ d_i(h, w) = \begin{cases} 1, & \text{if } \bar{E}_i(h, w) > \tau_{high} \\ 3, & \text{if } \tau_{low} < \bar{E}_i(h, w) \le \tau_{high} \\ 5, & \text{if } \bar{E}_i(h, w) \le \tau_{low} \end{cases} $$

该机制使模型在高频边缘区域使用小膨胀率保留细节，在低频内部区域使用大膨胀率增强上下文。FGDS解码器进一步引入边界高频保持与背景高频抑制（BPBS）块，通过可学习门控 $G_i$ 抑制伪边缘噪声：

$$ G_i = \sigma(W_g * H F_i + b_g) $$

其中 $H F_i$ 为高频分量，$\sigma$ 为Sigmoid函数。这一设计解决了高频背景噪声（如肠褶、高光）被误判为前景的问题，实现了边界与区域的联合优化。

## 实验评估

实验在Kvasir-SEG、CVC-ClinicDB、CVC-300、CVC-ColonDB及ETIS五个数据集上进行，训练集包含Kvasir-SEG 900张与CVC-ClinicDB 550张图像，测试集共798张。基线覆盖KAN类（UKAN, KMUNet）与经典CNN/Transformer类（MEGANet, PraNetv2），但缺失Mamba类（如STDDNet）及基础模型蒸馏类（如LiteBounD）强基线。

| 方法 | Kvasir-SEG mDice | CVC-ClinicDB mDice | ETIS mDice |
|---|---|---|---|
| MEGANet | 0.913 | 0.938 | 0.739 |
| UKAN | 0.856 | 0.886 | 0.569 |
| FARF-Net | 0.932 | 0.945 | 0.815 |

FARF-Net在Kvasir-SEG上以0.932 mDice超越MEGANet的0.913，在ETIS上以0.815 mDice显著优于UKAN的0.569，验证了频域自适应机制在复杂边界场景下的有效性。

消融实验显示，EdgeKAN模块在ETIS数据集上带来0.026 mDice提升（0.764至0.794），其中LiteDWSKAN贡献0.016，Token-KAN贡献0.007，表明中层特征增强对小型息肉分割更为关键。ARF模块进一步将mDice提升至0.806，FGDS解码器最终达到0.815。计算复杂度方面，FARF-Net参数量33.71M，FLOPs 11.91G，FPS 6.9，高于UKAN（6.35M, 14.02G）但低于KUNet（33.52M, 145.53G），显示其在精度与效率间的权衡。

评估边界方面，论文未报告置信区间，且未提供代码开源链接。实验仅在NVIDIA RTX 3090 GPU上进行，未验证CPU实时推理能力。33.71M参数量与11.91G FLOPs的计算开销，在资源受限的边缘设备上是否满足临床实时性要求，论文未给出明确回答。

## 关联研究分析

从方法设计看，FARF-Net与ASGNet同属频域引导路线，但ASGNet侧重全局频谱特征增强，而FARF-Net聚焦局部频率能量驱动的自适应卷积。这一差异源于任务特性：全局频谱增强适合处理整体光照不均，而局部自适应卷积更适合应对息肉内部与边缘的频率异质性。FARF-Net通过Haar小波分解实现空间-频率联合建模，解决了固定感受野无法适应局部频率变化的问题，但离散化膨胀率（1/3/5）是否限制了细粒度频率响应的连续性，论文未深入探讨。

从问题动机看，FARF-Net与LiteBounD代表不同技术路线。LiteBounD通过基础模型蒸馏提升跨域泛化，在CVC-ClinicDB上达到0.948 mDice，略高于FARF-Net的0.945。这一微小差距暗示，专用网络在干净基准上的精度优势可能无法完全抵消基础模型预训练先验在跨域场景下的泛化能力。FARF-Net未采用基础模型蒸馏，其泛化能力主要依赖数据增强与架构设计，这在多中心数据验证中可能面临挑战。

## 总结

FARF-Net旨在解决息肉分割中固定感受野与边界模糊的双重失效问题，通过频率驱动的自适应卷积与KAN通道级非线性增强，实现了SOTA性能。在Kvasir-SEG上，其0.932 mDice超越MEGANet的0.913，在ETIS上0.815 mDice显著优于UKAN的0.569，验证了频域自适应机制的有效性。然而，33.71M参数量与11.91G FLOPs的计算开销，以及离散化膨胀率的粒度限制，暴露了其在实时部署与细粒度频率响应上的边界。当支持集增大或成像条件进一步复杂化时，频率自适应机制的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_31d5193cdf20)