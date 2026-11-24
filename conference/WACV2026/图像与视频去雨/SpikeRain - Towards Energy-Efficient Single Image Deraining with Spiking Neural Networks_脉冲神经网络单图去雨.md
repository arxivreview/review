# WACV2026最新论文 ｜SpikeRain: Towards Energy-Efficient Single Image Deraining with Spiking Neural Networks ｜脉冲神经网络单图去雨

研究机构：韩国成均馆大学

作者：Md Tanvir Islam、Inzamamul Alam、Sambit Bakshi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4e8c48c32975)

> 单图去雨旨在从受雨丝遮挡的图像中恢复清晰场景，其核心价值在于支撑自动驾驶等关键视觉任务。现有基于CNN与Transformer的方法虽提升了精度，但计算复杂度高且能耗大，难以在资源受限的边缘设备实时部署。本文提出SpikeRain，一种基于脉冲神经网络（Spiking Neural Networks, SNN）的编码器-解码器架构，利用事件驱动的稀疏激活机制实现极致的能效优化。该架构在保持竞争性恢复精度的同时，将计算量降低近89%，为低功耗神经形态硬件上的图像恢复提供了新路径，但其脉冲离散化对高频细节的保留极限尚存疑。

## 研究背景

单图去雨的核心挑战在于从雨纹退化图像中恢复清晰内容，雨纹主要影响中高频分量，且常与背景纹理重叠。传统方法依赖手工先验，泛化能力差；深度学习方法将其建模为监督图像到图像回归问题，但主流CNN受限于局部感受野，难以捕捉长程依赖，而Transformer虽能实现全局建模，却因二次方计算复杂度导致内存与能耗激增。在边缘部署场景下，计算量（FLOPs）与能耗（Energy）成为比单纯精度更关键的约束指标。

去雨领域的主流路线已从局部卷积演进至全局高效建模。2020-2022年，Restormer等Transformer架构确立了全局建模范式，但难以在移动设备实时运行；2024-2025年，Mamba等状态空间模型（State Space Models, SSM）以线性复杂度崛起，平衡了精度与效率。然而，这些方法仍基于人工神经网络（Artificial Neural Networks, ANN）的密集激活机制，未充分利用生物神经系统的稀疏事件驱动特性。SpikeRain的切入点在于：不追求在ANN框架内极致压缩FLOPs，而是转向SNN范式，通过时间步上的稀疏脉冲累积替代空间上的密集注意力，从底层计算机制上解决能效瓶颈。

## 核心方法

### 方法参照系

本文遵循图像恢复的编码器-解码器通用范式，但关键差异在于将连续激活的ANN替换为离散脉冲的SNN。标准流程中，输入图像经卷积提取特征，通过注意力机制建模依赖，最后解码重建。SpikeRain将输入图像在时间维度上复制为T个时间步的序列，利用LIF神经元将空间特征转化为时间上的二进制脉冲流，通过时间累积实现上下文建模，而非空间自注意力。

### 密集脉冲残差块（DSRB）

DSRB是SpikeRain的核心特征提取单元，旨在解决SNN中稀疏脉冲导致的激活不稳定与梯度爆炸问题。在标准SCU（Spiking Control Unit）中，LIF神经元根据膜电位阈值产生脉冲，但单一脉冲流难以捕捉复杂雨纹。DSRB引入密集连接，将前序SCU的输出与当前SCU的输出进行通道拼接，再通过1×1卷积（LFF）压缩维度并添加残差连接。其核心公式为：

$$ \mathbf{X}^{t,n} = \text{LFF} \left( \left[ \mathbf{X}_{\text{MDSA}}^{t}, \mathbf{X}_{\text{SCU}}^{t,1}, \dots, \mathbf{X}_{\text{SCU}}^{t,n} \right] \right) + \mathbf{X}^{t,n-1} $$

该公式表明，当前层的输出是密集拼接特征经线性投影后的结果加上前一层的残差。设计动机在于，密集连接允许脉冲信号在多个卷积层间复用，增强了网络对雨纹局部强度波动的建模能力，同时残差连接稳定了训练过程，保留了输入图像的高频线索。

### 多维脉冲注意力（MDSA）

MDSA模块嵌入DSRB中，用于动态重校准脉冲响应，解决单一维度注意力无法同时捕捉雨纹时空结构的问题。它并行计算时间、通道和空间三个维度的注意力权重，并通过逐元素乘法调制脉冲特征。其核心公式为：

$$ \mathbf{X}_{\text{MDSA}} = \mathbf{X} \odot \mathbf{A}_{\text{T}} \odot \mathbf{A}_{\text{C}} \odot \mathbf{A}_{\text{S}} $$

其中 $\mathbf{A}_{\text{T}}$ 通过3D平均池化和Sigmoid门控获取，捕捉时间步上的显著性；$\mathbf{A}_{\text{C}}$ 和 $\mathbf{A}_{\text{S}}$ 分别通过通道和空间维度的降维-升维卷积获取。这一设计使得网络能够自适应地聚焦于雨纹密集区域和关键通道，抑制无关背景噪声，从而在稀疏脉冲表示下实现更精准的雨纹抑制。

## 实验评估

实验在Rain12、Rain200L、Rain200H、Rain1200四个合成基准及RW-Data真实基准上进行。基线覆盖CNN（NAFNet）、Transformer（NeRD-Rain）、SSM（DFSSM）及前作SNN（ESDNet），但缺失Mamba类最新SOTA（如PRISM、DeRainMamba）的直接对比。

| 方法 | 类型 | Rain200L PSNR (dB) | Rain200H PSNR (dB) | FLOPs (G) | Energy (µJ) |
|---|---|---|---|---|---|
| NeRD-Rain | ViT | 41.71 | 32.40 | 156.3 | 1.953 × 10^6 |
| DFSSM | SSM | 41.81 | 32.99 | 212.4 | 2.655 × 10^6 |
| ESDNet | SNN | 39.85 | 30.01 | 7.320 | 9.150 × 10^4 |
| SpikeRain | SNN | 40.01 | 31.17 | 0.808 | 1.01 × 10^4 |

SpikeRain在Rain200L上以40.01 dB的PSNR略高于ESDNet的39.85 dB，但低于NeRD-Rain的41.71 dB；在Rain200H上以31.17 dB显著高于ESDNet的30.01 dB。其核心优势在于能效：0.808 GFLOPs和1.01×10^4 µJ的能耗比NeRD-Rain低约193倍和193倍，比ESDNet低约9倍和9倍。

| 配置 | Rain200H PSNR (dB) | FLOPs (G) | Energy (µJ) |
|---|---|---|---|
| T=1 | 28.81 | 0.047 | 0.587 × 10^4 |
| T=2 | 30.19 | 0.065 | 0.812 × 10^4 |
| T=4 (Baseline) | 31.17 | 0.808 | 1.01 × 10^4 |
| + MDSA | 30.91 | - | - |
| + MDSA + ARFE | 31.05 | - | - |
| + MDSA + ARFE + TF | 31.17 | - | - |

消融实验显示，时间步T从1增至4，PSNR从28.81 dB提升至31.17 dB，验证了时间累积对特征提取的贡献。MDSA模块带来0.72 dB的提升，ARFE带来0.14 dB，TF带来0.12 dB，表明多维注意力是性能增益的主要来源，而时间融合模块的边际收益较小。

评估指标包含PSNR、SSIM及无参考指标PIQE、MetaIQA，但缺乏置信区间报告。代码已开源，训练使用2块NVIDIA RTX 3080Ti GPU，超参数（如T=4, αs=4.0）已公开，可复现性良好。

## 关联研究分析

从问题动机看，SpikeRain与PRISM（Mamba路线）均旨在解决高效全局建模问题，但技术路径截然不同。PRISM通过状态空间模型在空间序列上实现线性复杂度，而SpikeRain通过时间步上的脉冲累积实现能效优化。SpikeRain未使用显式频域模块，仅靠空间脉冲响应取得竞争性精度，这暗示在SNN架构下，频域先验可能并非必要，或LIF神经元的膜电位动态已隐式学习了雨纹的频域特性。

从方法设计看，SpikeRain与ESDNet（前作SNN）同属SNN去雨路线，但SpikeRain引入了MDSA和ARFE模块。ESDNet依赖简单的残差连接，而SpikeRain通过多维注意力动态重校准脉冲响应，解决了ESDNet在复杂雨纹下细节恢复不足的问题。SpikeRain的参数比ESDNet减少约40%，FLOPs减少约89%，表明其架构在保持精度的同时实现了更极致的压缩。

## 总结

SpikeRain要解决的核心矛盾是图像去雨的高精度需求与边缘设备低功耗约束之间的冲突。现有ANN方法受限于密集激活机制，难以在能效上实现数量级突破，而SpikeRain凭借SNN的事件驱动稀疏特性，通过时间步累积替代空间注意力，实现了0.808 GFLOPs和1.01×10^4 µJ的极致能效。实验证明其在Rain200L上达到40.01 dB PSNR，虽低于NeRD-Rain的41.71 dB，但能效优势显著。其边界在于脉冲离散化可能损失部分高频细节，且在Rain200H上仍低于DeRainMamba的32.45 dB。当时间步T进一步增加时，脉冲离散化对高频细节的恢复能力是否会出现饱和或退化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_4e8c48c32975)