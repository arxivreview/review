# ICLR2026最新论文 ｜SoftCFG: Uncertainty-guided Stable Guidance for Visual Autoregressive Model ｜软分类器自由引导

研究机构：比利时鲁汶大学

作者：Dongli Xu、Aleksei Tiulpin、Matthew B. Blaschko

论文原文见 [arXiv](https://arxiv.org/abs/2510.00996)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00996)

> 自回归视觉生成模型在推理阶段面临引导信号随解码步数增加而衰减，以及强引导导致视觉结构畸变的双重困境。标准分类器自由引导（Classifier-Free Guidance, CFG）仅扰动序列起始的条件Token，无法解决长序列中条件信息远离局部上下文的问题。本文提出SoftCFG，通过置信度加权扰动所有历史Token的Value Cache，并引入步归一化机制稳定长序列生成。该方法无需重训练即可将Alitok-XL在ImageNet 256x256上的FID从1.37降至1.27，但其效果是否依赖于特定骨干网络架构，以及能否泛化至Next-Scale生成范式，仍存疑。

## 研究背景

自回归视觉生成将图像建模为离散Token序列，通过解码器Transformer预测下一个Token。这一范式依赖向量量化自编码器（Vector-Quantized Autoencoder, VQ-VAE）将连续像素映射为离散码本索引，使语言模型架构可直接迁移至视觉领域。在条件生成任务中，模型需同时处理外部条件（如类别标签）与已生成内容的上下文依赖，而引导机制是平衡条件对齐与生成多样性的关键。

当前主流方案采用CFG，通过插值条件与无条件分支的预测差异来增强条件对齐。然而，在自回归序列中，条件Token位于序列起始，随着解码推进，其距离局部注意力窗口越来越远，导致条件-无条件差异迅速消失，即“引导衰减”。同时，过强的引导尺度会过度强调语义标签，引发肢体重复、物体部件冗余等视觉连贯性破坏，即“过度引导”。现有方法如AdaLN虽将条件嵌入注入预测头，但仍依赖外部信号，无法利用已生成内容本身作为引导源，难以同时解决信号衰减与语义-视觉冲突。

## 核心方法

### 方法参照系

标准CFG在每步解码时，通过替换第一个条件Token为空Token生成无条件分支，计算条件与无条件Logits的差值$\Delta_t$，并以固定尺度$\gamma$放大该差值。其核心假设是引导信号仅由外部条件决定，且对所有历史Token的影响是均质的。本文的关键差异在于：将引导信号从“仅依赖外部条件”扩展为“依赖外部条件与已生成内容的置信度”，并作用于所有历史Token的Value Cache而非仅第一个Token。

### 不确定性加权扰动

标准CFG的失效源于其无法区分已生成Token的可靠性。SoftCFG在解码步$t$时，对每个历史Token $i < t$ 计算其最大预测概率$p_{max}(x_i)$作为置信度，并定义扰动权重$w_i = 1 - p_{max}(x_i)$。高置信度Token（$w_i$小）被视为语义可靠，其Value Cache被更强地缩放，从而放大其对后续预测的影响。具体而言，无条件分支的Value向量被更新为：

$$\tilde{\mathbf{v}}_i^{[uncond]} = w_i \cdot \mathbf{v}_i^{[uncond]}$$

随后，基于扰动后的Value Cache计算无条件Logits $\tilde{\mathbf{z}}_t^{[uncond, pertcontext]}$，并与条件Logits组合：

$$\mathbf{z}_t^{[SoftCFG]} = (1 + \gamma)\mathbf{z}_t^{[cond]} - \gamma \tilde{\mathbf{z}}_t^{[uncond, pertcontext]}$$

这一设计使引导信号嵌入模型的记忆中，通过高置信度Token的持续影响，解决了标准CFG中引导信号随步数衰减的问题，同时通过置信度加权自然正则化了语义对齐与视觉连贯性的冲突。

### 步归一化机制

SoftCFG的累积扰动可能导致无条件分支退化。当多个高置信度Token的$w_i$趋近于0时，无条件Value Cache的贡献被过度抑制，导致$\tilde{\mathbf{z}}_t^{[uncond, pertcontext]}$趋近于0，引发长序列生成不稳定。为解决此问题，SoftCFG引入步归一化（Step Normalization），在每步解码前对扰动权重进行归一化：

$$\hat{w}_i = \frac{1 - w_i}{\sum_{j=1}^{t-1} (1 - w_j) + \epsilon}$$

归一化后，所有扰动权重之和恒为1，确保每步的扰动预算固定。这一机制将累积扰动限制在单个Token的贡献范围内，避免了无条件分支的退化，保证了长序列生成的稳定性。

## 实验评估

实验在ImageNet-1K 256x256类别条件生成基准上进行，生成50k样本评估FID、IS、sFID、Precision和Recall。基线覆盖扩散模型（DiT, REPA）、掩码模型（MaskGIT）及自回归模型（LlamaGen, Alitok），但缺失VAR架构的直接对比，而VAR是当前自回归生成中Next-Scale范式的代表。

| 方法 | 参数量 | FID↓ | IS↑ | sFID↓ | Pre.↑ | Rec.↑ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Alitok-XL (Wu et al., 2025b) | 662M | 1.37 | 321.4 | 7.29 | 0.79 | 0.64 |
| Alitok-XL*+SoftCFG (ours) | 662M | 1.27 | 302.4 | 6.76 | 0.78 | 0.65 |
| REPA-E (Leng et al., 2025) | 675M | 1.26 | 314.9 | 4.11 | 0.79 | 0.66 |

SoftCFG将Alitok-XL的FID从1.37降至1.27，IS从321.4降至302.4，sFID从7.29降至6.76。FID的改善表明生成质量提升，但IS的下降暗示样本多样性可能略有牺牲。与扩散模型REPA-E的FID 1.26相比，SoftCFG后的自回归模型在FID上已接近扩散模型水平，但sFID（6.76 vs 4.11）仍有差距，表明在细粒度结构一致性上自回归模型仍落后于扩散模型。

消融实验显示，SoftCFG相比标准CFG将FID从1.37降至1.32，步归一化进一步将sFID从7.62降至7.16，IS从288.1提升至302.0。这表明步归一化主要改善了生成稳定性与多样性，而非FID。联合调优$\gamma$和$k$后，FID进一步降至1.27，sFID降至6.70，说明超参数对最终性能有显著影响，但边际收益递减。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码未公开，但Alitok和VAR均有开源实现，可复现基线。超参数$\gamma=13, k=1.4$在Alitok-XL上最优，但未提供其他模型的调优细节。

## 关联研究分析

从问题动机看，SoftCFG与VAR的Next-Scale范式存在根本差异。VAR通过从粗到细的层级生成解决空间结构错位，其引导信号可能随尺度切换而重新注入，而SoftCFG基于Next-Token范式，引导信号依赖序列内的Token置信度。SoftCFG在Alitok（Next-Token）上有效，但未验证在VAR（Next-Scale）上的效果。若VAR的层级生成已部分缓解了引导衰减，SoftCFG的增益可能有限；反之，若Next-Scale范式加剧了跨尺度误差累积，SoftCFG的置信度加权可能更具价值。这一差异源于生成顺序对上下文依赖的影响，而非引导机制本身。

从方法设计看，SoftCFG与StepVAR等加速方法同属推理优化路线，但目标不同。StepVAR通过剪枝降低计算量，SoftCFG通过扰动Value Cache提升引导稳定性。两者均不改变模型架构，但SoftCFG的扰动操作可能影响KV Cache的复用效率。论文声称计算开销可忽略，但未提供具体的延迟数据。若Value Cache的频繁缩放导致内存带宽瓶颈，SoftCFG在高分辨率生成中的实际加速比可能低于预期。这一盲区源于论文仅关注生成质量，未深入分析推理效率的微观影响。

## 总结

SoftCFG旨在解决自回归生成中CFG引导信号衰减与过度引导的矛盾，其切入点在于利用已生成Token的置信度作为内部引导源，替代标准CFG仅依赖外部条件的做法。通过置信度加权扰动Value Cache与步归一化，SoftCFG在Alitok-XL上将FID从1.37降至1.27，sFID从7.29降至6.76，证明了内部引导的有效性。然而，实验仅基于Next-Token范式的Alitok，未验证在Next-Scale范式（如VAR）下的泛化性，且IS的下降暗示多样性可能受损。当生成范式从Next-Token转向Next-Scale时，置信度加权是否仍能稳定跨尺度引导信号，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00996)