# ICLR2026最新论文 ｜STaMP: Sequence Transformation and Mixed Precision for Low-Precision Activation Quantization ｜序列变换与混合精度量化

作者：Marco Federici、Riccardo Del Chiaro、Boris van Breugel 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26771)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26771)

> 低比特Transformer量化长期受困于激活值异常值对量化步长的支配，导致W4A4精度崩塌。现有特征维度变换（如Hadamard旋转）忽略了序列维度中相邻Token的强局部相关性，无法实现能量的高效集中。STaMP通过引入序列维度的离散小波变换（DWT）将激活能量压缩至前64个Token，并采用8/4-bit双精度分配策略，在无需重训练的前提下显著提升了LLM与LVM的量化保真度。该方法验证了序列维度治理的必要性，但其离散能量层级对比特分配细粒度的限制尚待进一步探索。

## 研究背景

当Transformer模型在边缘设备部署时，线性层的大矩阵乘法主导功耗，而激活值中少数极端幅值（Outliers）迫使量化器使用粗粒度步长，导致大部分正常值精度丢失。这一现象源于激活分布的非均匀性，传统Min-Max量化假设分布近似高斯，但在ViT和LLM中，异常值导致量化误差$\|WX - \hat{W}\hat{X}\|$急剧增大。为缓解此问题，SmoothQuant通过通道缩放将量化难度从激活迁移至权重，QuaRot等利用Hadamard矩阵在特征维度分散异常值能量。然而，这些方法仅作用于特征维度，忽略了序列维度中相邻像素或Token间的强自相关性，导致能量分布未达最优，W4A4下精度仍显著低于全精度基线。

现有方案在特征维度变换上已趋于饱和，但序列维度的局部结构未被利用。视觉与文本数据在中间激活层呈现块状Toeplitz自相关结构，相邻Token高度相关，远端Token弱相关。这一结构特性意味着，通过序列维度的线性变换可进一步集中能量，为混合精度分配提供物理基础。STaMP正是基于此切入点，将传统媒体压缩（如JPEG、HEVC）中的频率域能量集中原理迁移至Transformer激活空间，填补了序列维度量化治理的空白。

## 核心方法

### 特征变换参照系

现有PTQ方法通过右可逆矩阵$\mathbf{R}$对激活$\mathbf{X}$进行特征变换，即$\mathbf{X}' = \mathbf{X}\mathbf{R}$，以分散异常值。该流程假设激活在特征维度独立，忽略序列维度$\mathbf{X} \in \mathbb{R}^{s \times d}$中$s$维度的相关性。STaMP的关键差异在于引入左可逆矩阵$\mathbf{L}$作用于序列维度，形成$\mathbf{X}' = \mathbf{L}\mathbf{X}$，且$\mathbf{L}$与权重$\mathbf{W}$正交，不改变权重数值，仅重参数化激活。

### 序列变换与能量集中

STaMP定义序列变换为$\mathbf{L}\mathbf{X}$，其中$\mathbf{L}$为左可逆矩阵。设计动机在于利用激活自相关矩阵$\mathbf{S} = \mathbb{E}[\mathbf{X}\mathbf{X}^T]$的Toeplitz结构，通过变换将能量集中至前几个Token。理论上，最优变换为Karhunen-Loève Transform (KLT)，但KLT需全秩矩阵乘法，计算复杂度$O(s^2d)$不可接受。STaMP采用离散小波变换（DWT），其复杂度降至$O(ds)$，且DWT的离散能量层级特性天然适配硬件支持的有限比特宽度。DWT通过$\log s$级分解，将能量逐步推至序列前半部分，实现高效能量集中。

$$
\mathbf{X}' = \mathbf{L}_{\text{DWT}} \mathbf{X}
$$

该公式表示对激活矩阵$\mathbf{X}$应用DWT变换，将序列维度的局部相关性转化为能量集中，为后续混合精度分配提供基础。

### 混合精度比特分配

基于DWT能量集中特性，STaMP设计双比特分配策略：前64个Token保留8-bit精度，其余Token使用4-bit。设计动机在于量化误差与比特宽度$b_i$呈指数关系，将额外比特分配给高能量Token可不成比例地降低总误差。具体分配方案为：

$$
b_i^* = \begin{cases} 8 & \text{if } i \leq 64 \\ 4 & \text{if } i > 64 \end{cases}
$$

该策略在PixArt-Σ上仅增加0.0625的平均比特宽度（4.0625 vs 4.0），却显著提升了SQNR。DWT的离散能量层级使得双比特分配成为近似最优解，避免了连续比特宽度在硬件上的不可实现性。

## 实验评估

实验在PixArt-Σ、SANA（LVM）和Llama 3 8B、Llama 3.2 1B/3B、Qwen 2.5 3B（LLM）上进行，采用W4A4 per-block量化（block size 64），基线包括SmoothQuant、QuaRot、FlatQuant、SVDQuant、ViDiT-Q。STaMP与上述方法组合，验证其正交性。

| 模型 | 基线 | STaMP | 指标 |
| :--- | :--- | :--- | :--- |
| PixArt-Σ | SVDQuant | SVDQuant+STaMP | SQNR: 8.78 → 9.72 |
| SANA | SVDQuant | SVDQuant+STaMP | SQNR: 9.99 → 10.69 |
| Llama 3 8B | FlatQuant | FlatQuant+STaMP | PPL: 9.29 → 6.77 |
| Llama 3.2 1B it | FlatQuant | FlatQuant+STaMP | PPL: 15.72 → 15.16 |

STaMP在所有基线上均带来一致提升，尤其在Llama 3.2 1B/3B等小模型上，PPL降幅显著，表明序列变换对量化困难模型的鲁棒性。

消融实验显示，高精度Token数量对SQNR影响显著：引入少量8-bit Token即可大幅提升SQNR，且在5-bit平均比特宽度下，STaMP优于均匀量化。DWT相比KLT和DCT，能量集中效率略低，但其离散层级特性更适配硬件，计算开销低于5%总运行时。

评估边界方面，论文未报告置信区间，且LVM实验未量化cross-attention的key/value（占比<5%运行时）。代码未公开，DWT CUDA kernel细节仅在附录提及，可复现性受限。LLM PPL在W4A4下仍高于ButterflyQuant（5.45 vs 6.77），表明序列变换在文本序列上的能量集中效率可能低于特征维度可学习变换。

## 关联研究分析

从问题动机看，STaMP与ButterflyQuant同属正交变换路线，但作用维度不同。ButterflyQuant在特征维度应用可学习蝴蝶变换，直接抑制异常值；STaMP在序列维度应用固定DWT，利用局部相关性。差异根源在于任务特性：视觉数据（PixArt-Σ）的块状结构使序列维度相关性更强，而文本数据（Llama）的序列相关性较弱，导致STaMP在LLM上的增益小于LVM。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，STaMP与SVDQuant形成互补。SVDQuant通过低秩分解吸收异常值，作用于权重；STaMP通过序列变换集中能量，作用于激活。两者正交性使得组合使用可叠加提升精度，如PixArt-Σ上SVDQuant+STaMP的SQNR达9.72，显著高于单独SVDQuant的8.78。这种组合策略突破了单一维度变换的精度上限，但依赖硬件对双比特精度的支持，部署兼容性存疑。

## 总结

STaMP针对低比特量化中激活异常值导致的精度崩塌，抓住序列维度局部相关性这一被忽略的结构特性，通过DWT能量集中与双比特混合精度分配，在无需重训练的前提下提升了LLM与LVM的量化保真度。实验证明，STaMP与特征变换正交，组合后PixArt-Σ SQNR从8.78提升至9.72，Llama 3 8B PPL从9.29降至6.77。其边界在于DWT离散能量层级限制了比特分配细粒度，且LLM PPL仍高于ButterflyQuant。当序列长度增加时，DWT的$\log s$级分解是否仍能保持能量集中效率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26771)