# ICLR2026最新论文 ｜THICKER AND QUICKER: A JUMBO TOKEN FOR FAST PLAIN VISION TRANSFORMERS ｜宽全局Token加速纯视觉Transformer

研究机构：加拿大不列颠哥伦比亚大学、加拿大向量研究所

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_2986316)

> 视觉Transformer（ViT）在保持通用性的同时面临推理速度瓶颈，现有高效架构多通过引入卷积或层级结构牺牲了纯ViT的生态兼容性。本文切入点在于识别出全局信息容量不足是纯ViT低速场景下的精度短板，而非计算量本身。通过引入一个宽度为Patch Token $J$ 倍的Jumbo Token并共享其FFN参数，在不改变纯ViT接口的前提下实现了速度-精度的帕累托前沿。该设计在保持自监督学习、多模态兼容性的同时提升了效率，但其对极端小模型（Nano级）的增益依赖特定训练协议，且未验证在动态Token剪枝场景下的稳定性。

## 研究背景

纯ViT的通用性源于其“仅注意力”且“非层级”的架构特性，这使其能无缝适配自监督学习（SSL）、多模态对齐及测试时自适应（TTA）等依赖标准Transformer接口的技术。然而，这种通用性以计算效率为代价：在Nano至Tiny规模下，纯ViT的吞吐量远低于MobileNetV4或SHViT等混合架构。传统ViT将全局信息聚合任务分配给单个CLS Token，其宽度与Patch Token相同（$D$），导致全局表示容量仅占模型总容量的 $1/(N+1)$，在高分辨率或大类别任务中成为瓶颈。

现有高效架构路线主要分为两类：一是引入卷积或池化的混合架构（如EfficientViT、SHViT），虽提升了速度但破坏了纯ViT接口，无法直接支持MAE等SSL算法或Flash Attention优化；二是通过缩减Token宽度（如ViT-Tiny）降低计算量，但这同时削弱了局部与全局特征的表达能力。Darcet et al. (2024) 提出的Registers机制通过增加等宽Token缓解全局容量不足，但未解决宽度受限导致的表达能力上限问题。本文针对“如何在保持纯ViT通用性前提下，突破小模型的全局容量瓶颈”这一矛盾，提出非对称宽度扩展策略。

## 核心方法

### 方法参照系

本文问题属于高效架构设计路线，但区别于常规的混合CNN-Transformer或线性注意力改造。标准流程旨在通过结构替换降低FLOPs，而本文保留纯ViT的注意力-only与非层级结构，仅修改Token宽度分布。关键差异在于：本文不减少序列长度或改变注意力机制，而是通过增加单一全局Token的宽度来补偿小模型中全局信息容量的缺失，同时利用参数共享控制内存开销。

### 非对称宽度扩展与Split-Merge机制

传统ViT中所有Token宽度均为 $D$，导致全局Token容量受限。本文引入Jumbo Token，其宽度为 $J \cdot D$，其中 $J$ 为扩展因子（Base模型取3，其他取6）。在自注意力层前，Jumbo Token被拆分为 $J$ 个宽度为 $D$ 的子Token，与Patch Token拼接后进入MHSA：

$$
\mathbf{x}_{\text{Jumbo}} \in \mathbb{R}^{J \cdot D} \xrightarrow{\text{split}} \mathbf{x}_{\text{Jumbo}}' \in \mathbb{R}^{J \times D}, \quad \mathbf{x} = \mathbf{x}_{\text{Jumbo}}' \parallel_0 \mathbf{x}_P \in \mathbb{R}^{(N+J) \times D}
$$

注意力计算后，Jumbo子Token被重新拼接为宽Token，并送入独立的Jumbo FFN。这一设计解决了小模型中全局Token因宽度不足而无法充分聚合长程依赖的问题，同时通过Split-Merge机制保持了与标准ViT相同的注意力接口，确保兼容Flash Attention等硬件优化。

### 跨层FFN共享与容量补偿

Jumbo FFN的参数在所有ViT层间共享，而非每层独立。这一设计动机在于：Jumbo Token仅处理单一全局表示，其计算量远小于Patch Token序列，独立FFN会导致内存冗余。共享FFN不仅将Jumbo部分的参数量降至最低，还起到正则化作用。实验表明，共享FFN在保持甚至提升精度的同时，显著降低了内存占用（ViT-Base+Jumbo内存3.9GB vs 非共享4.1GB）。该机制使得Jumbo Token能以极低的额外成本提供比Registers更强大的全局处理能力，因为宽FFN能执行更复杂的非线性变换，而Registers仅通过注意力交互。

## 实验评估

| 架构 | 速度 (K imgs/s) | 参数量 (M) | 内存 (GB) | FLOPs (G) | Top-1 Acc. (%) |
|---|---|---|---|---|---|
| ViT-Base | 3.1 | 86.6 | 3.3 | 16.5 | 68.1 |
| ViT-Base+Jumbo | 3.1 | 130.7 | 3.9 | 16.9 | 73.0 |
| ViT-Large | 1.0 | 304.4 | 5.0 | 59.7 | 73.0 |
| ViT-Large+Jumbo | 1.0 | 382.2 | 5.2 | 59.9 | 74.0 |

实验在ImageNet-1K上训练，基线包括ViT+Registers、SHViT、EfficientViT及MobileNetV4。ViT-Base+Jumbo在保持3.1 K imgs/s吞吐量的同时，Top-1准确率从68.1%提升至73.0%，与ViT-Large持平但参数量仅为后者的43%。在ImageNet-21K上，Jumbo的增益随类别数增加而扩大（Small模型增益从0.8%升至3.1%），验证了全局容量对高维输出任务的敏感性。

消融实验显示，移除Jumbo FFN导致准确率下降1.36%（44.61% vs 43.64%），证明独立FFN对全局信息处理的必要性。Jumbo Token数量从6增至10时，准确率进一步提升至45.62%，但速度降至6.9 K imgs/s，表明存在速度-精度的边际收益递减点。在ImageNet-C鲁棒性测试中，Jumbo+SAR较Registers+SAR平均提升5.2%，说明宽全局Token增强了模型对分布偏移的适应能力。

评估边界方面，论文未报告置信区间，且所有吞吐量数据基于RTX 4090 GPU与PyTorch 2.6.0，缺乏跨硬件平台的能效对比。代码已开源，但超参数搜索范围有限（仅学习率与Dropout），未探索Jumbo Token与动态Token剪枝（如ToMe）的结合效果。

## 关联研究分析

从方法设计看，Jumbo Token与Registers机制（Darcet et al., 2024）均旨在增强全局信息容量，但Registers通过增加等宽Token数量实现，而Jumbo通过增加单Token宽度实现。Registers的增益主要来自注意力图的噪声减少，而Jumbo的增益源于FFN的非线性处理能力。这一差异暗示，当模型规模缩小至Nano级时，宽度扩展比数量扩展更能突破表达能力上限，因为小模型的注意力头数有限，等宽Token的交互效率较低。

从问题动机看，本文与SHViT（Yun & Ro, 2024）等混合架构形成鲜明对比。SHViT通过引入卷积层降低计算量，但牺牲了纯ViT接口，导致无法直接支持MAE等SSL算法。Jumbo则证明，通过非对称宽度扩展而非结构替换，可以在保持纯ViT通用性的同时达到甚至超越混合架构的效率。这一发现挑战了“高效ViT必须引入卷积”的假设，表明全局容量不足是小模型效率瓶颈的关键因素，而非局部特征提取的计算开销。

## 总结

本文要解决的核心矛盾是纯ViT在小模型规模下全局信息容量不足导致的精度-速度权衡失衡。现有混合架构通过牺牲通用性换取速度，而本文抓住“全局Token宽度受限”这一被忽略的瓶颈，通过引入宽Jumbo Token并共享FFN参数，在保持纯ViT接口的前提下实现了效率突破。实验证明，ViT-Base+Jumbo在3.1 K imgs/s吞吐量下达到73.0% Top-1准确率，与ViT-Large持平但参数量减少57%。本文的边界在于，其增益依赖于静态Token结构，未验证在动态Token剪枝或极端低比特量化场景下的稳定性。当Jumbo Token与动态Token剪枝方法结合时，宽全局Token是否仍能保持其容量优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_2986316)