# CVPR2026最新论文 ｜A More Word-like Image Tokenization for MLLMs ｜解耦视觉Token化

研究机构：韩国首尔大学

作者：Hyun Lee、Hyemin Jeong、Yejin Kim 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17954)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17954)

> 多模态大语言模型（MLLMs）中，视觉编码器输出的Patch特征因自注意力机制产生高度语义纠缠，导致投影后的视觉Token与LLM所需的离散、独立文本Token存在结构性失配。现有剪枝或压缩方法仅减少Token数量，未解决Token内部语义混杂的根本问题，且在固定预算下难以适应不同复杂度的图像。本文提出解耦视觉Token化（Disentangled Visual Tokenization, DiVT），通过基于语义相似度的自适应聚类重构视觉Token，使每个Token对应单一视觉概念，并动态调整Token数量以匹配图像复杂度。该方法在极低Token预算下显著优于传统剪枝基线，但其性能增益依赖于特定的聚类阈值调优，且未验证在极端细粒度任务上的鲁棒性。

## 研究背景

多模态大语言模型（MLLMs）通过视觉编码器将图像映射为嵌入序列，再经投影层对齐至语言模型（LLM）的嵌入空间。然而，视觉Transformer（ViT）中的自注意力机制在深层逐渐同质化Patch嵌入，导致同一图像内的视觉特征高度相似。这种语义纠缠使得线性投影后的视觉Token在LLM中表现为冗余且难以区分的连续向量，与基于字节对编码（Byte Pair Encoding, BPE）生成的离散、独立文本Token在结构上存在根本差异。

当前主流方案分为两类：一是固定网格聚合或空间下采样，如TokenPacker，虽降低Token数量但保留空间邻近性导致的语义混杂；二是基于注意力分数或显著性的剪枝，如FastV和VisionZip，虽能动态移除低贡献Token，但依赖LLM内部信号或视觉显著性，未能从源头解决Patch特征的纠缠问题。这些方法均假设视觉Token是独立的信息单元，忽略了其在编码器内部已形成的强相关性。本文切入点在于重构Token生成逻辑，而非仅筛选或合并已有Token，旨在从投影阶段即实现语义解耦。

## 核心方法

### 方法参照系

现有视觉投影器通常采用线性层或简单聚合策略，将ViT输出的固定数量Patch特征映射为LLM输入。其核心假设是Patch特征已包含足够语义信息，仅需维度对齐或数量压缩。本文问题与该通用流程的关键差异在于：Patch特征在编码器深层已高度纠缠，直接映射会传播冗余，且固定预算无法适应图像语义复杂度的变化。

### 自适应语义聚类

传统聚类算法如K-means需预设簇数，导致所有图像使用相同Token预算，无法反映内容复杂度差异。本文提出基于余弦相似度的自适应质心选择算法，根据Patch特征分布动态确定簇数。具体而言，计算Patch两两余弦相似度矩阵 $\mathbf{S}$，定义阈值 $\theta$ 下的邻接关系，贪心选择度数最大的节点作为质心，直至所有节点被分配。该设计解决了固定预算在简单图像上冗余、在复杂图像上信息不足的问题，使Token数量自然随语义复杂度缩放。

$$
\mathbf{S}_{i,j} = \cos(\mathbf{x}_i, \mathbf{x}_j), \quad \text{neighbors}(i) = \{j \mid \mathbf{S}_{i,j} > \theta\}
$$

该公式通过阈值 $\theta$ 控制聚类粒度：高 $\theta$ 产生更多细粒度Token，低 $\theta$ 产生更少粗粒度Token，实现精度-效率的显式权衡。

### 簇内交叉注意力聚合

初始聚类基于贪心策略，可能导致Patch被分配至非最优簇。本文引入簇内交叉注意力机制，以质心为查询（Query），簇内Patch为键（Key）和值（Value），通过可学习参数 $\mathbf{W}_{Q,K,V}$ 和位置嵌入 $\mathbf{P}_i$ 聚合信息。位置嵌入仅注入Value分支，以避免扰动注意力分数。该设计解决了贪心聚类中Patch可能属于多个簇的歧义问题，确保每个Token封装单一语义单元，同时保留所有Patch信息，防止细粒度细节丢失。

$$
\mathbf{t}_k = \text{CrossAttn}(\mathbf{W}_Q \mathbf{x}_{c_k}, \mathbf{W}_K \mathbf{X}_k, \mathbf{W}_V (\mathbf{X}_k + \mathbf{P}_k))
$$

该公式通过簇限制注意力掩码确保聚合仅在语义相关Patch内进行，使每个视觉Token对应一个解耦的视觉概念，如物体或显著区域，而非空间网格单元。

## 实验评估

实验基于LLaVA-1.5 7B骨干，在MMBench、VQAv2、GQA、MME、MM-Vet、TextVQA、SQA-IMG、POPE八个基准上评估。基线覆盖Training-free剪枝方法（ToME, FastV, VisionZip, VisPruner, ATP-LLaVA）和Training-based投影器（TokenPacker），但缺失2025-2026年最新SOTA方法如GRIP-VLM和SparseVLM，限制了与当前前沿的直接对比。

| 方法 | # Tokens | MMBench | VQAv2 | GQA | MM-Vet | POPE |
|---|---|---|---|---|---|---|
| MLP (full) | 576 | 64.3 | 78.5 | 62.0 | 31.1 | 85.9 |
| TokenPacker | 64 | 64.1 | 77.2 | 61.1 | 30.6 | 86.2 |
| DiVT ($\theta=0.62$) | 63.7 | 64.3 | 77.7 | 61.4 | 32.1 | 85.8 |
| DiVT ($\theta=0.75$) | 136.5 | 66.7 | 78.2 | 62.0 | 33.7 | 84.2 |

DiVT在136.5 Token下MMBench得分66.7，超越全量MLP的64.3；在63.7 Token下VQAv2得分77.7，优于TokenPacker的77.2。性能增益在低Token预算下更显著，表明语义解耦在信息受限条件下更具鲁棒性。

消融实验显示，推理时调整阈值 $\theta$ 可实现Training-free的粒度控制。训练于 $\theta=0.65$ 的模型在推理时使用 $\theta=0.5$ 时，Token数从74.1降至58.3，MMBench得分从65.5降至64.3，性能损失轻微。反之，提高 $\theta$ 未带来性能提升，因Token无法获得训练时未学习的细粒度信息。该结果验证了阈值作为精度-效率权衡旋钮的有效性，但也暴露了训练-推理一致性限制。

评估边界方面，论文未报告计算延迟或内存占用的具体数值，仅定性声称降低推理成本。代码已开源，但超参数 $\theta$ 的调优依赖交叉验证，未提供自动化选择策略。实验仅在LLaVA-1.5 7B和13B骨干上验证，未测试其他视觉编码器（如DINOv2）或更大规模LLM，泛化性存疑。

## 关联研究分析

从问题动机看，DiVT与FastV、VisionZip等剪枝方法的核心差异在于解决层次。FastV依赖LLM浅层注意力分数移除低贡献Token，假设注意力信号能准确反映任务相关性；VisionZip结合视觉显著性与上下文合并，侧重空间冗余消除。两者均在Token生成后进行操作，未触及Patch特征纠缠的根源。DiVT在投影阶段重构Token生成逻辑，通过语义聚类实现解耦，其优势源于对编码器内部表示结构的利用，而非外部信号。这种差异暗示，当LLM注意力信号受位置偏差或噪声影响时，基于编码器特征的解耦可能更稳定，但论文未提供在对抗攻击或分布外数据上的鲁棒性对比。

从方法设计看，DiVT与Resampler共享查询聚合思想，但Resampler使用固定数量的全局查询，导致所有图像使用相同Token预算；DiVT采用自适应数量的局部簇质心查询，实现动态预算。这一改进解决了固定预算在复杂图像上信息不足的问题，但引入了聚类阈值 $\theta$ 的调优依赖。与ToMe的空间邻近合并不同，DiVT的语义聚类可能破坏空间连续性，影响定位任务。论文未提供在OCR或细粒度定位任务上的专项评估，仅通过TextVQA间接验证，其空间信息保留能力存疑。

## 总结

DiVT旨在解决视觉Token与文本Token的结构性失配，通过语义聚类重构Token生成逻辑，实现解耦与动态预算。其核心贡献在于证明基于编码器特征的语义解耦在低Token预算下优于传统剪枝方法，如136.5 Token下MMBench得分66.7超越全量模型的64.3。然而，论文边界在于未验证在极端细粒度任务（如OCR）上的鲁棒性，且阈值 $\theta$ 的调优依赖交叉验证，缺乏自动化策略。当图像包含大量细粒度文本或密集物体时，语义聚类是否会导致空间细节丢失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17954)