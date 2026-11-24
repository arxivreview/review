# ICLR2026最新论文 ｜Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention ｜解耦协同细化注意力机制

研究机构：复旦大学、上海交通大学

作者：Xiaosong Jia、Yihang Sun、Junqi You 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.06478)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06478)

> 前馈式新视角合成（Novel View Synthesis, NVS）旨在从少量已知位姿图像直接回归目标视图，以突破逐场景优化的效率瓶颈。现有基于Transformer的模型如LVSM采用全自注意力机制，导致计算复杂度随输入视图数呈二次增长，且强制异构Token共享参数，阻碍了场景理解与视图渲染的专门化学习。本文提出Efficient-LVSM，通过双流架构解耦输入编码与目标生成，并引入层间协同细化机制。该设计在RealEstate10K基准上以50%的训练时间实现了比LVSM高0.2 dB的PSNR，但其在无扩散先验下的生成多样性边界尚存疑。

## 研究背景

前馈式NVS的核心在于利用大规模数据学习通用三维先验，替代传统的逐场景优化。该范式依赖Transformer架构处理图像与相机位姿信息，其中Plücker射线嵌入用于编码相机几何，图像块化（Patchification）用于提取视觉特征。然而，当输入视图数量增加时，全自注意力机制的计算开销呈二次方增长，且输入视图（富含语义与几何）与目标查询（仅含位姿）在信息密度上存在本质差异，这种异构性在全共享参数下难以被有效区分。

从NeRF到3D Gaussian Splatting（3DGS），再到大型重建模型（Large Reconstruction Models, LRMs），NVS领域经历了从隐式场优化到显式前馈回归的范式转移。LVSM作为近期代表，通过最小化手工归纳偏置直接合成视图，但在处理多视图输入时，其单体自注意力结构导致效率低下且泛化能力受限。具体而言，全自注意力迫使模型在理解场景结构（输入任务）与渲染新视图（目标任务）之间共享同一套参数，导致特征纠缠。本文切入点在于识别这一架构瓶颈，通过解耦输入与目标的处理流，实现计算效率与重建质量的双重提升。

## 核心方法

### 前馈式NVS架构参照系

LVSM采用端到端Transformer范式，将输入图像块与Plücker射线块拼接为输入Token，目标位姿编码为目标Token。所有Token进入统一的Transformer块进行全自注意力计算，最终通过线性层与Sigmoid函数输出RGB值。该流程的关键差异在于，LVSM未区分输入与目标Token的功能角色，导致计算复杂度为 $O(N^2M)$，其中 $N$ 为输入视图数，$M$ 为目标视图数。

### 双流解耦注意力机制

针对全自注意力中异构Token参数共享导致的特征纠缠问题，本文提出双流架构。输入编码器（Input Encoder）仅处理输入视图，采用视图内自注意力（Intra-view Self-Attention）独立构建每个视图的表示，避免跨视图的冗余计算。目标解码器（Target Decoder）通过交叉注意力（Cross-Attention）查询编码器特征。该设计将计算复杂度从 $O(N^2M)$ 降低至 $O(NM)$，并支持KV-Cache增量推理。

$$
\mathbf{S}_i^l = \mathbf{S}_i^{l-1} + \text{Self-Attn}_{input}(\mathbf{S}_i^{l-1})
$$

输入编码器在第 $l$ 层对第 $i$ 个输入视图的Token进行自注意力更新，确保每个视图的特征提取独立于其他视图，从而支持可变视图数的零样本泛化。

### 层间协同细化与REPA蒸馏

为解决仅使用编码器最后一层特征导致的信息损失，本文引入协同细化（Co-refinement）机制。解码器在每一层不仅查询编码器对应层的特征，还通过自注意力整合场景级信息。此外，引入REPA（Representation Alignment）蒸馏，利用预训练DINOv3特征对齐输入与目标Token，弥补纯几何先验在语义理解上的不足。

$$
\mathcal{L}_{REPA} = - \sum_{k} \log \frac{\exp(\text{sim}(h_\phi(\mathbf{X}_k), f(\mathbf{I})) / \tau)}{\sum_{k'} \exp(\text{sim}(h_\phi(\mathbf{X}_{k'}), f(\mathbf{I})) / \tau)}
$$

该损失函数通过最大化投影后的隐藏特征与DINOv3编码图像之间的相似度，将视觉语义信息注入模型，其中 $h_\phi$ 为可训练投影器，$f$ 为预训练编码器。

## 实验评估

| 方法 | PSNR (dB) | SSIM | LPIPS |
| :--- | :--- | :--- | :--- |
| LVSM Dec-Only (Res-256) | 29.67 | 0.906 | 0.098 |
| **Efficient-LVSM (Res-256)** | **29.86** | **0.905** | **0.147** |
| GS-LRM (Res-256) | 28.98 | 0.926 | 0.074 |
| MVSplat | 26.39 | 0.869 | 0.128 |

在RealEstate10K场景级基准上，Efficient-LVSM以29.86 dB的PSNR超越LVSM Dec-Only的29.67 dB，同时训练时间减半。基线覆盖包括pixelSplat、MVSplat等前馈方法及GS-LRM等重建模型，但未对比最新视频扩散类方法如ViewCrafter的增强版本。消融实验显示，协同细化机制带来1.28 dB的PSNR增益，而REPA蒸馏在Efficient-LVSM上带来0.8 dB增益，远高于在LVSM上的0.16 dB，表明解耦架构更利于语义特征注入。

评估协议遵循LVSM设置，使用2输入视图和3目标视图。指标包含PSNR、SSIM、LPIPS，但未报告推理延迟的具体数值分布（仅提及4.4倍加速）。代码未明确开源，但提供了项目主页。实验未覆盖动态场景或极端稀疏视图（如单视图）下的鲁棒性测试，限制了结论的泛化范围。

## 关联研究分析

从方法设计看，Efficient-LVSM与MM-DiT在处理异构Token上存在根本差异。MM-DiT采用统一的全自注意力块，仅通过不同的投影层区分输入与目标，而本文采用完全解耦的双流架构，输入编码器独立处理视图，目标解码器通过交叉注意力查询。这一差异源于任务特性：NVS中输入视图需独立保持几何一致性，而MM-DiT处理的文本-图像生成中，文本与图像特征需更紧密的交互。本文的解耦设计牺牲了部分跨视图全局交互能力，换取了计算效率与可变视图数的泛化性，这在稀疏视图NVS中是合理的取舍，但在密集视图下是否最优，论文未给出回答。

从问题动机看，本文聚焦于前馈模型的效率瓶颈，而领域内另一条路线如ViewCrafter利用视频扩散模型生成伪视图以增强3DGS训练。ViewCrafter依赖生成先验填补未观测区域，解决的是几何歧义问题；而Efficient-LVSM依赖Transformer回归，解决的是计算复杂度问题。两者在“几何引导的生成”这一大框架下，分别侧重生成多样性与计算效率。本文未使用扩散模型，因此在处理大视角变化时的外观多样性可能受限，这与其在RealEstate10K上仅使用2输入视图的设置有关，更极端的视角变化下，纯回归方法的表现尚不明确。

## 总结

Efficient-LVSM旨在解决前馈式NVS中全自注意力导致的二次计算复杂度与异构Token参数共享问题。通过解耦输入编码与目标生成，并引入层间协同细化，该架构在保持高质量重建的同时实现了显著的效率提升。实验证明，在RealEstate10K上，该方法以50%的训练时间实现了比LVSM高0.2 dB的PSNR，推理速度提升4.4倍。然而，其边界在于未使用扩散先验，且在极端稀疏视图或动态场景下的鲁棒性未经验证。当输入视图数进一步减少至单视图时，解耦架构中目标解码器对输入特征的依赖是否会加剧几何歧义，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06478)