# HuggingFace最新推荐论文 ｜MPDiT: Multi-Patch Global-to-Local Transformer Architecture For Efficient Flow Matching and Diffusion Model ｜多补丁全局-局部扩散Transformer

研究机构：美国罗格斯大学

作者：Quan Dao、Dimitris Metaxas

论文原文见 [arXiv](https://arxiv.org/abs/2603.26357)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26357)

> 导读 扩散Transformer（DiT）的等向性设计导致每个块处理相同数量的Token，造成训练与推理过程中的计算冗余。现有线性注意力或状态空间架构因长程依赖捕获能力不足或Token序列长度限制，难以在保持生成质量的同时显著降低计算成本。本文提出MPDiT，通过层级化多补丁架构将早期块的大补丁Token与后期块的小补丁Token解耦，并引入傅里叶神经算子时间嵌入与多Token类别嵌入。该架构在ImageNet 256x256上实现了50%的GFLOPs削减，但其在高分辨率视频生成中的扩展性仍存疑。

## 研究背景

扩散模型训练的核心瓶颈在于潜在空间中的Token数量与注意力计算的二次方复杂度。当VAE将图像压缩为潜在表示后，标准DiT对每个Transformer块应用相同的补丁嵌入，导致所有块处理相同数量的Token。这种等向性设计使得早期块在捕获全局结构时，被迫计算大量与局部细节无关的注意力交互，造成计算资源的浪费。

DiT架构确立了Transformer在视觉生成中的主导地位，但其$O(N^2)$的注意力复杂度成为主要延迟来源。主流加速路线包括线性注意力（如SANA、LIT）和状态空间模型（如Mamba），但前者在长程依赖捕获上存在性能损失，后者仅在Token序列超过1k时才有显著优势，而大多数潜在扩散模型涉及少于1k的Token。卷积架构（如DiCo、DiC）虽降低了GFLOPs，但未能充分利用Transformer的扩展性。本文切入点在于架构层级而非注意力层级，通过多补丁设计在保留全注意力优势的同时，从源头减少参与计算的Token数量。

## 核心方法

### 方法参照系

标准DiT架构采用等向性设计，所有N个Transformer块处理相同数量的Token。本文问题与该通用流程的关键差异在于：早期块处理的全局信息与后期块处理的局部细节具有不同的Token密度需求，等向性设计忽视了这种层级化的信息结构。

### 多补丁层级化架构

标准DiT中，补丁嵌入模块将潜在表示$z \in \mathbb{R}^{h \times w \times d}$转换为固定数量的Token序列。MPDiT将这一过程解耦为两个阶段：前$N-k$个块使用大补丁$p=4$，将Token数量从256减少至64；随后通过上采样模块将64个Token扩展回256个，最后$k$个块处理这些细粒度Token。

$$
\text{Tokens}_{early} = \frac{h \times w}{p_{large}^2}, \quad \text{Tokens}_{late} = \frac{h \times w}{p_{small}^2}
$$

其中$p_{large}=4$，$p_{small}=2$。这一设计动机在于：早期块仅需捕获全局上下文，64个Token足以建模整体结构；后期块需细化局部细节，256个Token提供更精细的空间分辨率。通过这种层级化设计，MPDiT在保持全注意力机制的同时，将早期块的注意力计算量降低至标准DiT的25%，实现了50%的GFLOPs削减。

### 傅里叶神经算子时间嵌入

标准DiT使用线性层对正弦时间嵌入进行投影，这种设计难以捕获时间步之间的平滑过渡。MPDiT引入傅里叶神经算子（FNO）时间嵌入，将时间特征映射到频域进行处理。

$$
\mathbf{e}_t = \text{FNO}(\sin(2\pi t \mathbf{w}))
$$

其中$\mathbf{w}$为可学习的频率参数。FNO层通过谱卷积捕获时间步之间的全局依赖关系，相比线性嵌入，能更有效地建模扩散过程中的ODE动态。这一设计动机在于：线性嵌入将时间视为离散点，而FNO将其视为连续函数，更好地匹配流匹配的训练目标。

### 多Token类别嵌入

标准DiT使用单个类别Token通过AdaIN调制注入条件信息。MPDiT采用多Token策略，将类别索引编码为$m$个Token序列，前置到输入Token序列中。

$$
\mathbf{c} = [\mathbf{c}_1, \mathbf{c}_2, \dots, \mathbf{c}_m] \in \mathbb{R}^{m \times d}
$$

其中$m=16$。这一设计动机在于：单个Token难以充分编码类别语义，多Token提供了更丰富的表示空间，增强了类别信息与空间图像Token之间的交互。

## 实验评估

实验在ImageNet 256x256上进行，使用50K样本评估FID、IS、Precision和Recall。基线覆盖DiT、SiT、DiG、DiC、DiCo等架构，但缺失推理加速类基线（如TeaCache、SpargeAttention）。

| 模型 | Epochs | GFLOPs↓ | FID↓ | sFID↓ | IS↑ |
|---|---|---|---|---|---|
| SiT-XL/2 | 1400 | 118.66 | 9.35 | 6.38 | 126.06 |
| DiT-XL/2 | 1400 | 118.66 | 9.62 | 6.85 | 121.50 |
| MPDiT-XL | 240 | 59.30 | 7.36 | 5.09 | 127.57 |
| SiT-XL/2-G | 1400 | 118.66 | 2.15 | 4.60 | 258.09 |
| DiT-XL/2-G | 1400 | 118.66 | 2.27 | 4.60 | 278.24 |
| MPDiT-XL-G | 240 | 59.30 | 2.05 | 4.51 | 278.73 |

MPDiT-XL在240 epochs内达到FID 7.36，而SiT-XL/2需1400 epochs达到FID 9.35，表明MPDiT在训练效率上具有显著优势。在CFG设置下，MPDiT-XL-G的FID 2.05优于DiT-XL/2-G的2.27，同时GFLOPs降低50%。

| 方法 | Params(M) | GFLOPs↓ | FID↓ |
|---|---|---|---|
| DiT-B/2† | 101.2 | 24.3 | 24.52 |
| MPDiT_k=4 | 104.8 | 13.9 | 26.94 |
| MPDiT_k=6 | 104.8 | 16.6 | 24.74 |
| MPDiT_k=8 | 104.8 | 19.3 | 24.62 |
| 2×Linear | 105.5 | 16.6 | 27.92 |
| 3×MixedFNO | 104.8 | 16.6 | 24.74 |
| m=1 | 93.3 | 15.3 | 32.31 |
| m=16 | 104.8 | 16.6 | 24.74 |

消融实验显示，$k=6$时FID下降小于1点，而GFLOPs显著降低；FNO时间嵌入相比线性嵌入提升约4点FID；多Token类别嵌入（$m=16$）相比单Token提升约7点FID。这些结果表明，架构层级化、时间嵌入改进和类别嵌入增强是性能提升的主要来源。

评估协议使用Euler求解器250步，指标完备但缺乏推理延迟的直接测量。代码已开源，超参数完整，可在8×A100 GPU上复现。

## 关联研究分析

从问题动机看，MPDiT与稀疏注意力方法（如SpargeAttention）都旨在降低注意力计算成本，但前者通过架构设计减少Token数量，后者通过动态稀疏化跳过冗余计算。MPDiT的优势在于无需训练额外的稀疏化模块，但劣势在于Token数量固定，无法根据输入内容动态调整。这种差异源于任务特性：图像生成的Token数量相对固定，而视频生成的Token数量随帧数变化，稀疏注意力在视频任务中可能更具优势。

从方法设计看，MPDiT与REPA等训练加速方法都关注收敛速度，但前者通过架构优化降低计算量，后者通过表示对齐增强语义监督。MPDiT的FNO时间嵌入与REPA的DINO对齐在功能上相似，都旨在提供更丰富的表示，但前者作用于时间维度，后者作用于空间维度。这种差异暗示，时间维度和空间维度的表示学习可能存在不同的优化路径，MPDiT未探索将FNO与表示对齐结合的可能性。

## 总结

MPDiT要解决的核心矛盾是DiT等向性设计导致的计算冗余与生成质量之间的权衡。现有线性注意力或状态空间架构因长程依赖捕获能力不足或Token序列长度限制，难以在保持质量的同时显著降低计算成本。MPDiT通过多补丁层级化架构，将早期块的大补丁Token与后期块的小补丁Token解耦，并引入FNO时间嵌入与多Token类别嵌入，实现了50%的GFLOPs削减。实验证明，MPDiT-XL在240 epochs内达到FID 7.36，优于SiT-XL/2在1400 epochs的FID 9.35。本文的边界在于仅在ImageNet 256x256上验证，未探索高分辨率或视频生成场景。当Token序列长度超过1k时，多补丁架构的计算优势是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26357)