# CVPR2026最新论文 ｜DreamSR: Towards Ultra-High-Resolution Image Super-Resolution via a Receptive-Field Enhanced Diffusion Transformer ｜面向超高分辨率图像超分的感受野增强扩散Transformer

作者：Qingji Dong、Hang Dong、Mingqin Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15682)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15682)

> 超高分辨率（UHR）图像超分面临分块推理导致的局部语义缺失与全局提示冲突，引发过生成或细节丢失。现有基于文本到图像（T2I）扩散模型的方法在分块处理时无法有效对齐局部视觉特征与全局文本语义。DreamSR通过双分支MM-ControlNet融合局部与全局文本特征，并结合两阶段推理框架，解决了这一语义错位问题。该方法在高分辨率基准上实现了SOTA性能，但其对标准低分辨率基准的增益有限，且依赖特定骨干网络。

## 研究背景

当扩散模型处理4K及以上分辨率图像时，受显存限制必须采用分块推理策略。然而，单个图像块（patch）仅包含局部语义信息，而全局文本提示（global prompt）描述整幅图像内容，两者在分块推理中产生语义错位。这种错位导致模型在局部区域过度生成不存在的细节（over-generation），或因局部提示不足而无法激活预训练模型的完整生成能力（under-generation）。

传统基于卷积神经网络（CNN）或生成对抗网络（GAN）的超分方法受限于回归范式，难以恢复真实纹理。扩散模型凭借强大的生成先验提升了感知质量，但多步迭代推理效率低下。2024年后，研究重心转向利用预训练T2I模型（如Stable Diffusion、FLUX）作为骨干，通过ControlNet注入低分辨率（LR）条件。然而，现有方法（如SeeSR、SUPIR）通常仅注入视觉特征，忽视文本特征在分块推理中的对齐作用。DreamSR的切入点在于：在超高分辨率场景下，必须同时利用局部文本提示捕捉块内细节，并利用全局文本提示维持整体语义一致性，且需通过架构设计解决两者冲突。

## 核心方法

### 方法参照系

基于预训练T2I扩散模型的超分标准流程为：将LR图像编码为潜变量，通过ControlNet注入视觉条件，由冻结的DiT骨干执行多步去噪。该流程假设全局文本提示足以指导所有局部区域的重建。本文的关键差异在于：针对分块推理场景，引入局部文本提示，并设计双分支机制融合局部与全局文本特征，同时采用两阶段推理加速去退化过程。

### 双分支MM-ControlNet与上下文交叉注意力

在标准ControlNet仅注入视觉特征的基础上，DreamSR构建Patch Context aware MM-ControlNet，从FLUX DiT中复制部分多模态DiT（MM-DiT）块，形成独立分支。该分支接收局部图像块潜变量 $z_{lq}^{[i,j]}$ 和局部文本提示嵌入 $E_{ij}$，输出图像特征 $f_{c,img}^{[l]}$ 和文本特征 $f_{c,txt}^{[l]}$。图像特征通过零MLP直接注入主DiT，而文本特征通过上下文交叉注意力模块与全局文本特征融合。该模块定义为：

$$ \text{Attn}(Q_{txt}^{[l]}, K_{c,txt}^{[l]}, V_{c,txt}^{[l]}) = \text{softmax}\left(\frac{Q_{txt}^{[l]} (K_{c,txt}^{[l]})^T}{\sqrt{d}}\right) V_{c,txt}^{[l]} $$

其中 $Q_{txt}^{[l]} = P_Q(f_{txt}^{[l]})$ 为局部文本查询，$K_{c,txt}^{[l]} = P_K(f_{c,txt}^{[l]})$ 和 $V_{c,txt}^{[l]} = P_V(f_{c,txt}^{[l]})$ 为全局文本键值。该设计使每个局部块能动态关注全局提示中最相关的语义线索，抑制无关信号，从而解决分块推理中局部提示不足导致的细节缺失与全局提示冲突导致的过生成。

### 两阶段推理与恢复加速LoRA

针对多步去噪效率低下的问题，DreamSR将推理分为退化去除与纹理生成两阶段。第一阶段引入恢复加速LoRA（Restoration Acceleration LoRA），在单步内完成退化去除，输出潜变量 $z_{dr}$。第二阶段以 $z_{dr}$ 为中间状态，注入受控高斯噪声得到 $z_t$，执行多步去噪生成纹理。该设计动机在于：单步去退化可压缩早期冗余去噪步骤，使后续多步专注于高频纹理细化，避免从纯噪声开始导致的语义漂移。LoRA模块通过低秩适应技术修改DiT权重，在保持预训练先验的同时加速退化去除过程。

## 实验评估

实验在RealSR、DRealSR、RealLQ250、RealLR200和RealDeg五个真实世界数据集上进行，对比基线包括GAN方法（BSRGAN、Real-ESRGAN）和扩散方法（StableSR、DiffBIR、SeeSR、SUPIR、OSEDiff、FaithDiff、DreamClear、DiT4SR）。基线覆盖主流扩散超分路线，但缺少最新流匹配方法（如OFTSR、FlowMapSR）的对比。

| 数据集 | 方法 | MUSIQ ↑ | MANIQA ↑ | CLIPIQA+ ↑ |
|---|---|---|---|---|
| RealSR | Ours | 70.5560 | 0.5731 | 0.7318 |
| RealSR | SUPIR | 69.2206 | 0.4847 | 0.7200 |
| DRealSR | Ours | 67.3315 | 0.5404 | 0.7028 |
| DRealSR | SUPIR | 65.2829 | 0.4765 | 0.7008 |
| RealDeg | Ours | 45.6234 | 0.4574 | 0.6647 |
| RealDeg | SUPIR | 47.5436 | 0.4437 | 0.6841 |

在RealSR和DRealSR上，DreamSR的MUSIQ分别达到70.5560和67.3315，优于SUPIR的69.2206和65.2829。但在RealDeg（高分辨率）上，DreamSR的MUSIQ为45.6234，低于SUPIR的47.5436，表明其在超高分辨率场景下的感知质量优势未完全体现。

| 消融设置 | MUSIQ ↑ | MANIQA ↑ | CLIPIQA+ ↑ |
|---|---|---|---|
| w/o i2i deg | 43.7706 | 0.3917 | 0.6355 |
| w/o RFE train | 43.5546 | 0.3868 | 0.5975 |
| Full setting | 45.6234 | 0.4574 | 0.6647 |

消融实验显示，移除图像到图像（i2i）退化策略或感受野增强（RFE）训练均导致MUSIQ下降约1.85-2.07，验证了训练策略对细节生成的关键作用。移除恢复加速LoRA后，即使增加推理步数，性能仍低于完整模型，证明两阶段框架的有效性。

评估指标包含参考型（PSNR、SSIM、LPIPS）和非参考型（MUSIQ、MANIQA、CLIPIQA+），但论文未报告置信区间。代码与模型已开源，训练使用16块H20 GPU，批大小64，学习率5e-6，超参数 $\lambda=2, \lambda_1=2, \lambda_2=0.5$。

## 关联研究分析

从问题动机看，DreamSR与SeeSR均基于预训练T2I模型，但SeeSR仅使用全局文本提示，而DreamSR引入局部文本提示以解决分块推理的语义错位。这一差异源于任务特性：SeeSR针对标准分辨率，全局提示足以指导重建；DreamSR针对超高分辨率，分块推理导致局部语义缺失，必须引入局部提示。然而，局部提示的生成依赖多模态大语言模型（LLaVA），其准确性可能影响最终重建质量，论文未评估LLaVA提示错误对性能的敏感性。

从方法设计看，DreamSR与OSEDiff均采用单步去退化加速，但OSEDiff将单步用于最终生成，而DreamSR将单步用于退化去除，保留多步纹理生成。这一设计选择旨在平衡效率与质量：单步去退化压缩早期冗余步骤，多步生成确保纹理细节。与DiT4SR相比，DreamSR同样基于DiT架构，但DiT4SR未专门解决分块推理的局部-全局对齐问题，其ControlNet仅注入视觉特征。DreamSR的双分支MM-ControlNet通过上下文交叉注意力融合文本特征，是其核心创新。

## 总结

DreamSR解决的核心矛盾是超高分辨率分块推理中局部语义缺失与全局提示冲突导致的过生成或细节丢失。现有方法仅注入视觉特征或仅使用全局提示，无法同时满足局部细节与全局一致性需求。DreamSR通过双分支MM-ControlNet融合局部与全局文本特征，并结合两阶段推理框架，实现了语义对齐与高效推理。实验表明，其在RealSR和DRealSR上的MUSIQ达到70.5560和67.3315，优于SUPIR，但在RealDeg上低于SUPIR的47.5436。论文边界在于：依赖FLUX骨干，未验证其他DiT架构的适用性；局部提示生成依赖LLaVA，未评估提示错误的影响；RealDeg上的性能劣势暗示分块边界伪影可能未被完全抑制。当分块大小进一步增大时，局部提示与全局提示的语义差异是否缩小，从而降低双分支机制的必要性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15682)