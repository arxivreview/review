# HuggingFace最新推荐论文 ｜Cheers: Decoupling Patch Details from Semantic Representations Enables Unified Multimodal Comprehension and Generation ｜解耦细节与语义的统一多模态模型

研究机构：清华大学、中国科学院大学

作者：Yichen Zhang、Da Peng、Zonghao Guo 等 22 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.12793)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12793)

> 统一多模态模型（UMM）旨在单一架构内融合视觉理解与图像生成，但理解任务偏好紧凑语义表征，生成任务偏好高频细节重建，两者在共享参数中产生梯度冲突。现有解耦架构分离编码器导致知识共享减弱，而融合架构又易引发表征干扰。CHEERS 通过统一视觉分词器解耦 Patch 细节与语义表征，并引入级联流匹配头注入高频残差，在 1.5B 参数规模下以 83M 训练样本实现了 GenEval 0.78 与 MMBench 75.7 的性能，验证了该解耦策略在数据效率上的优势，但其绝对性能仍低于大规模混合架构，且缺乏对推理延迟的量化评估。

## 研究背景

当多模态大语言模型（MLLMs）处理视觉理解任务时，其依赖的视觉编码器倾向于提取全局语义紧凑表征；而扩散模型进行图像生成时，则依赖保留高频细节的重建导向潜空间。这种表征偏好的根本差异导致在单一 Transformer 骨干中联合训练时，理解任务的梯度 $\nabla \mathcal{L}_{understand}$ 与生成任务的梯度 $\nabla \mathcal{L}_{generate}$ 在共享参数上发生显著冲突，即“伪统一”现象。

早期纯自回归统一模型（如 Chameleon, Emu3）通过离散视觉 Token 化实现 Any-to-Any 交互，但量化误差导致高频细节丢失，生成保真度远低于专用扩散模型。为缓解此问题，Janus 等采用解耦视觉编码器分离理解与生成路径，虽缓解了梯度冲突，但增加了参数冗余并削弱了模态间知识共享。Transfusion 等混合架构尝试在同一 Transformer 中结合自回归与扩散目标，但直接处理潜空间或融合异构特征时，仍难以同时满足语义稳定性与像素保真度的双重需求。CHEERS 的切入点在于：不分离编码器，而是在统一视觉分词器内部解耦 Patch 级细节与语义表征，并通过级联流匹配头在生成阶段动态注入细节，从而在单一架构内消解优化冲突。

## 核心方法

### 混合解码架构参照系

CHEERS 属于混合 AR-Diffusion 架构路线，其标准流程为：LLM 骨干处理文本自回归解码，扩散或流匹配头处理图像连续潜空间解码。与 Transfusion 等直接混合损失的方法不同，CHEERS 的关键差异在于视觉编码端的解耦设计与生成端的级联注入机制，旨在解决单一表征空间无法同时满足语义抽象与像素保真的问题。

### 统一视觉分词器与语义压缩

CHEERS 的统一视觉分词器由 VAE 解码器与 SigLIP2-ViT 语义编码器组成。给定输入图像 $\mathbf{X}$，首先经 VAE 编码器得到潜状态 $\mathbf{z}_1$，随后通过 VAE 解码器 $D(\cdot)$ 重建像素级图像，再由 SigLIP2 提取高维语义特征 $\mathbf{z}_{s(t)}$。这一设计动机在于：直接处理潜状态会丢弃细粒度特征，阻碍 OCR 等依赖局部细节的理解任务。为降低 LLM 计算开销，引入 Pixel-Unshuffle 模块将空间分辨率降低 2 倍并投影至 LLM 隐藏维度 $c$，实现 4 倍 Token 压缩：

$$ \mathbf{Z}_{s(t)} = \text{PixelUnshuffle}(\mathbf{z}_{s(t)}) \in \mathbb{R}^{h/2 \times w/2 \times c} $$

该公式表明，语义 Token 在送入 LLM 前已完成空间降采样与通道投影，既保留了语义完整性，又显著减少了序列长度，解决了高分辨率图像理解中的效率瓶颈。

### 级联流匹配头与高频注入

CHEERS 的核心创新在于级联流匹配（CFM）头，它将图像生成解耦为低分辨率语义合成与高分辨率细节注入两个阶段。第一阶段由 7 个 DiT 块处理 LLM 输出的上下文隐藏状态 $\mathbf{Z}_{s(t)}$，生成低分辨率语义特征，随后经 PixelShuffle 上采样至全分辨率 $\mathbf{Z}'_{s(t)}$。第二阶段引入门控网络 $G(\cdot)$，将视觉分词器提取的高频 Patch 细节 $S(D(\mathbf{z}_t))$ 注入 $\mathbf{Z}'_{s(t)}$：

$$ \mathbf{Z}''_{s(t)} = \mathbf{Z}'_{s(t)} + G(\mathbf{Z}'_{s(t)}) \odot S(D(\mathbf{z}_t)) $$

其中 $G(\cdot)$ 输出标量门控值，动态控制细节注入强度。由于 $\mathbf{Z}'_{s(t)}$ 受时间步 $t$ 调制，高频注入强度随生成轨迹自然增强，无需显式监督即可实现从全局布局到局部细节的渐进式生成，有效缓解了生成任务对理解表征的破坏。

## 实验评估

CHEERS 在 GenEval、MMBench、DPG-Bench 等标准基准上评估，对比了 Janus-Pro、Show-o2、Tar 等 1.5B 参数规模的 UMM 基线，但缺失 BAGEL 等大规模混合架构的直接对比。在 GenEval 上，CHEERS 以 0.78 的 Overall Score 超越 Tar（0.76）和 Show-o2（0.76），但在 DPG-Bench 上以 83.48 低于 Show-o2 的 85.02，表明其在复杂提示遵循上仍有差距。

| 模型 | #Params. | #Data | GenEval Overall | MMBench | DPG-Bench Overall |
|---|---|---|---|---|---|
| Janus-Pro | 1.5B | 162M | 0.76 | 68.3 | 82.63 |
| Show-o2 | 1.5B | 177M | 0.76 | 65.6 | 85.02 |
| Tar | 1.5B | 403M | 0.76 | 70.4 | 82.96 |
| CHEERS | 1.5B | 83M | 0.78 | 75.7 | 83.48 |

消融实验显示，移除高频注入（HFI）后，GenEval 从 0.30 降至 0.17，DPG-Bench 从 51.63 降至 39.11，证实 HFI 对生成保真度的关键作用。仅使用理解数据微调时，MMBench 达 70.0，但 GenEval 为 0，表明理解与生成能力在预训练阶段已建立基础，后训练主要起对齐作用。

评估边界方面，论文未报告推理延迟与吞吐量，尽管 4 倍 Token 压缩旨在提升效率，但缺乏量化验证。训练使用 128 张 A100 GPU，超参数完整公开，代码与数据已开源，可复现性良好。

## 关联研究分析

从方法设计看，CHEERS 与 Janus 同属解耦思路，但 Janus 物理分离编码器，导致理解与生成模块间知识共享减弱；CHEERS 通过统一分词器内的特征解耦，在保持参数共享的同时缓解冲突，其 4 倍 Token 压缩是 Janus 未探索的效率优化方向。与 Transfusion 相比，Transfusion 直接混合 AR 与 Diffusion 损失，易导致优化不稳定；CHEERS 通过级联头将生成过程解耦为语义与细节两阶段，使高频注入强度随时间步动态调整，避免了直接混合损失带来的梯度干扰。

从问题动机看，CHEERS 聚焦于表征冲突的解耦，而 Show-o2 等融合架构试图通过单一 Token 接口整合异构特征，但论文指出融合易导致语义与细节相互干扰。CHEERS 的实验表明，在 1.5B 规模下，解耦策略在 MMBench 上显著优于融合策略（75.7 vs 65.6），但在 DPG-Bench 上未超越 Show-o2，暗示解耦策略在复杂组合生成上可能受限于细节注入的粒度。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

CHEERS 旨在解决统一多模态模型中理解与生成任务的表征冲突，其切入点在于不分离编码器，而是在统一视觉分词器内解耦 Patch 细节与语义表征，并通过级联流匹配头动态注入高频残差。该方法在 1.5B 参数规模下，以 83M 训练样本实现了 GenEval 0.78 与 MMBench 75.7 的性能，超越了同规模基线 Tar 和 Show-o2，验证了解耦策略在数据效率上的优势。然而，CHEERS 在 DPG-Bench 上未超越 Show-o2，且缺乏对推理延迟的量化评估，表明其解耦策略在复杂组合生成与效率验证上仍有局限。当训练数据规模扩大至 400M 以上时，解耦策略相对于融合架构的性能优势是否持续存在，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12793)