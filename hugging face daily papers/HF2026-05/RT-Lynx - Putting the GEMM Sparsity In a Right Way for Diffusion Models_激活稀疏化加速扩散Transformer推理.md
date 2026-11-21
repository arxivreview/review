# HuggingFace最新推荐论文 ｜RT-Lynx: Putting the GEMM Sparsity In a Right Way for Diffusion Models ｜激活稀疏化加速扩散Transformer推理

研究机构：阿里巴巴集团

作者：Xing Cong、Hanlin Tang、Kan Liu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.26632)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.26632)

> 扩散Transformer（DiT）推理延迟高企，传统权重剪枝因破坏模型容量导致生成质量严重退化。现有方案卡在权重分布缺乏内在稀疏性，无法有效利用硬件加速。本文切入点在于发现DiT激活值具有天然稀疏性，提出RT-Lynx框架，通过在线激活稀疏化结合范数补偿与LoRA微调实现无损加速。该方法在保持生成质量的同时实现了线性层1.55倍加速，但LoRA微调开销与单流架构性能缺口仍存疑。

## 研究背景

扩散模型推理需执行数十步迭代去噪，每步涉及大规模矩阵乘法，导致延迟与能耗激增。N:M半结构化稀疏（如2:4模式）能近乎减半浮点运算量（FLOPs），且被NVIDIA Sparse Tensor Core原生支持，理论加速上限为2倍。然而，稀疏化必须匹配硬件解码逻辑，要求非零元素呈固定局部模式，这对数据分布有严格要求。

DiT架构取代U-Net成为主流，但其线性层计算占比极高。主流加速路线聚焦权重剪枝，如Wanda、RIA等方法基于校准集统计量确定稀疏掩码。但这些方法在DiT上失效：权重值呈准高斯分布，缺乏2:4稀疏所需的内在结构，强行剪枝50%权重导致ImageReward下降超过3%。本文切入点在于观察到激活值分布截然不同——每个Token仅5%~10%神经元显著激活，这种由叠加机制导致的稀疏性更契合N:M约束，为范式转移提供基础。

## 核心方法

### 方法参照系

标准N:M稀疏化流程对权重矩阵$W \in \mathbb{R}^{D_{out} \times D_{in}}$执行静态剪枝，生成固定稀疏矩阵$W_s$，推理时直接调用稀疏内核。本文关键差异在于将稀疏操作从静态权重移至动态激活$X \in \mathbb{R}^{N \times D_{in}}$，需在线执行Top-K选择并融合补偿机制，以应对激活分布随输入变化的特性。

### 范数补偿稀疏化

直接对激活执行Top-K选择会削减其L2范数，导致信号幅度衰减。本文在稀疏化后引入缩放因子，恢复稀疏激活的原始幅度。对于激活向量$X \in \mathbb{R}^{1 \times 4}$，Top-2算子保留最大两个元素生成稀疏向量$\tilde{X}$，最终稀疏激活定义为：

$$X_{sparse} = \tilde{X} \cdot \frac{\|X\|_2}{\|\tilde{X}\|_2 + \epsilon}$$

其中$\epsilon = 1e-8$确保数值稳定。该设计解决了朴素剪枝导致的范数衰减问题，仅增加可忽略的计算开销，使稀疏输出幅度与稠密输出对齐。

### LoRA残差补偿与层跳过

低幅值激活虽接近零，但编码了头发、边缘等高频细节，直接移除会导致图像模糊。本文引入低秩LoRA分支补偿残差，最终输出计算为：

$$Y = S(X)W^\top + X(L_A L_B)^\top$$

其中$S(X)$为范数补偿后的稀疏激活，$L_A \in \mathbb{R}^{D_{out} \times R}$和$L_B \in \mathbb{R}^{R \times D_{in}}$为LoRA矩阵，秩$R=64$。训练目标是最小化稠密输出与稀疏+残差输出的L2距离，2k步内收敛。针对单流DiT（如Z-Image、FLUX），LoRA无法完全弥合性能缺口，故额外跳过特定线性层（如attn.o_proj、mlp.up/down），进一步降低计算量。

## 实验评估

实验在Qwen-Image（20B参数）、FLUX.1-dev（12B参数）、Z-Image（6B参数）上进行，分辨率1024×1024，随机种子42。基线覆盖Wanda、RIA、BaWA、SLiM等权重剪枝方法，但缺失TeaCache、SpargeAttention等缓存与稀疏注意力方法的直接对比，仅报告了组合实验。

| 模型 | 方法 | ImageReward | 加速比 |
|---|---|---|---|
| Qwen-Image | Full | 1.910 | 1.00x |
| Qwen-Image | Sparse Weight | 1.845 | - |
| Qwen-Image | Sparse Activation | 1.867 | - |
| Qwen-Image | RT-Lynx | 1.925 | 1.55x |

RT-Lynx的ImageReward（1.925）超过稠密基线（1.910），而所有权重稀疏方法均低于基线。在FLUX.1-dev上，RT-Lynx与TeaCache组合实现3.13倍加速，优于单独使用TeaCache的2.64倍。

消融显示，LoRA秩$R=64$为最优平衡点，参数量占比0.7306%。CUDA内核优化将在线稀疏开销从40%降至4.38%，Sparse GEMM加速达1.88倍。单流架构中，层跳过策略对Z-Image和FLUX的性能恢复至关重要，仅LoRA补偿存在明显质量差距。

评估边界：未报告ImageNet FID，仅使用模型特定指标（ImageReward、CLIP Score）；LoRA微调需2k步训练，非完全训练-free；代码未开源，超参数（如$\epsilon$、$R$）细节有限。

## 关联研究分析

从问题动机看，RT-Lynx与SpargeAttention均针对DiT计算瓶颈，但优化维度不同。SpargeAttention通过在线估计块重要性跳过冗余注意力计算，解决空间冗余；RT-Lynx通过激活稀疏化解决线性层计算冗余。二者可协同：RT-Lynx与SpargeAttention组合在Qwen-Image-2512上实现1.36倍加速，优于单独使用的1.11倍。差异根源在于任务特性：注意力稀疏依赖内容感知的动态调度，激活稀疏依赖数据分布的内在稀疏性，前者需额外计算开销估计重要性，后者仅需Top-K选择。

从方法设计看，RT-Lynx与TeaCache代表不同加速路线。TeaCache基于时间步敏感度动态缓存特征，消除时间冗余；RT-Lynx通过激活稀疏消除空间冗余。TeaCache无需训练，部署灵活；RT-Lynx需LoRA微调，但能更精细地恢复高频细节。组合实验显示二者互补：RT-Lynx+TeaCache在FLUX.1-dev上实现3.13倍加速，表明缓存与稀疏化可叠加。差异根源在于误差特性：缓存误差随迭代累积，需动态阈值控制；稀疏化误差源于信息丢失，需残差补偿恢复。

## 总结

本文核心矛盾是DiT推理延迟高与权重剪枝质量退化的冲突。现有权重剪枝方法因权重分布缺乏内在稀疏性而失效，本文凭借激活值天然稀疏性（5%~10%神经元激活）实现范式转移。RT-Lynx通过在线激活稀疏化、范数补偿、LoRA残差补偿与层跳过，在Qwen-Image上实现1.55倍线性层加速且ImageReward超过稠密基线。边界在于LoRA微调引入额外训练开销，单流架构需层跳过才能弥合性能缺口，且未报告标准基准FID。当激活稀疏化应用于视频DiT时，时空Token序列长度激增，在线Top-K选择的计算开销是否会被内核优化完全抵消，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.26632)