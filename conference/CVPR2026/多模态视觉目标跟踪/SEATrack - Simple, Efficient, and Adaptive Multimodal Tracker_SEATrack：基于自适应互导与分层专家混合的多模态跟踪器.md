# CVPR2026最新论文 ｜SEATrack: Simple, Efficient, and Adaptive Multimodal Tracker ｜SEATrack：基于自适应互导与分层专家混合的多模态跟踪器

研究机构：北京航空航天大学、上海交通大学

作者：Junbin Su、Ziteng Xue、Shihui Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12502)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12502)

> 多模态视觉目标跟踪旨在融合可见光、深度、热红外及事件等异构信号，以突破单一RGB模态在复杂场景下的感知瓶颈。现有参数高效微调（PEFT）方法虽降低了训练成本，但为逼近全参数微调性能，可训练参数量膨胀至先驱工作的16倍，违背了PEFT的效率初衷，且跨模态注意力图的不一致性阻碍了联合表征学习。SEATrack通过引入自适应互导低秩适应（AMG-LoRA）动态对齐跨模态注意力，并采用分层混合专家（HMoE）实现高效全局融合，在保持极低参数量的同时提升了跟踪精度。该方法在效率与性能的权衡上提供了新视角，但其精度上限仍受限于冻结骨干的容量，且在模态缺失场景下的鲁棒性机制尚需进一步验证。

## 研究背景

多模态跟踪的核心困境在于异构传感器数据间的分布差异与计算资源的有限性。当RGB图像因光照变化或遮挡失效时，深度或热红外模态提供互补信息，但直接拼接特征往往因模态间语义鸿沟导致融合效果不佳。为解决这一问题，参数高效微调（PEFT）范式通过冻结预训练RGB骨干网络，仅训练轻量级适配模块，从而避免灾难性遗忘并降低计算开销。然而，PEFT的有效性依赖于适配模块能否在极少参数下有效弥合模态分布差异，这一前提在现有方法中并未得到充分满足。

主流PEFT方法如ViPT（Zhu et al., 2023）和SDSTrack（Wang et al., 2023）通过提示学习或双流架构实现模态适配，但面临两个关键瓶颈：一是参数量随性能提升而急剧膨胀，例如OneTracker（Hong et al., 2024）的可训练参数达14.8M，远超ViPT的0.8M，使得“高效”名不副实；二是跨模态注意力图的不一致性，即不同模态对同一目标的匹配响应存在冲突，导致联合表征学习受阻。SEATrack的切入点在于重新审视PEFT的效率承诺，指出性能-效率权衡的失效源于跨模态对齐的缺失，而非参数量的不足。

## 核心方法

### 方法参照系

SEATrack基于OSTrack（Bertinetto et al., 2019）的ViT-Base骨干，采用双流架构分别处理RGB与X模态（深度、热红外或事件）输入。与单流方法将混合模态特征直接送入共享注意力层不同，双流设计保留了模态特异性，但需解决跨模态信息交互问题。本文的关键差异在于，不仅关注特征融合，更强调匹配注意力图的对齐，认为这是打破性能-效率困境的前提。

### AMG-LoRA：跨模态注意力对齐

现有双流PEFT方法中，冻结的注意力层因预训练于RGB域，对X模态的匹配响应存在域偏差，导致注意力图不一致。SEATrack提出AMG-LoRA，通过低秩适应（LoRA）更新注意力层的投影矩阵，实现域适应。具体而言，LoRA在$W_k$和$W_v$上引入低秩矩阵$A \in \mathbb{R}^{D \times r}$和$B \in \mathbb{R}^{r \times D}$，其中$r \ll D$，以最小参数代价调整注意力权重。

$$
\tilde{H}_{\text{attn}}^* = \text{Softmax}\left(\frac{(Q + A B Q) K^T}{\sqrt{D}} + A B V\right)
$$

该公式表明，LoRA通过低秩更新增强匹配注意力图，但静态更新无法适应场景动态变化。为此，SEATrack引入自适应互导（AMG），受无分类器引导（CFG）启发，将跨模态对齐重构为多分支权衡问题。AMG通过可学习缩放因子$w_X$和$w_{\text{rgb}}$，动态调整模态间的引导强度，实现双向互导。

$$
\tilde{H}_{\text{attn}}^{\text{aligned}} = w_X \tilde{H}_{\text{attn}}^X + w_{\text{rgb}} \tilde{H}_{\text{attn}}^{\text{rgb}}
$$

这一设计解决了静态LoRA在模态可靠性动态变化时的负迁移问题，使不可靠模态不再误导可靠模态，从而提升联合表征的鲁棒性。

### HMoE：高效全局关系建模

跨模态融合的传统方法或采用局部融合（表达力有限），或采用注意力机制（计算复杂度二次方增长）。SEATrack提出分层混合专家（HMoE），作为高效的全局关系建模器。HMoE通过分层软路由，从子token到token级别实现细粒度交互。输入token序列$\mathbf{X}_{\text{in}} \in \mathbb{R}^{N \times D}$被拆分为$h$个子token，形成$\mathbf{X}_{\text{split}} \in \mathbb{R}^{(N \cdot h) \times (D/h)}$。

$$
\mathbf{Y}_{\text{head}} = \text{Concat}\left(\{f_i(\mathbf{X}_{\text{split}} \Phi_i)\}_{i=1}^e\right)
$$

其中$\Phi \in \mathbb{R}^{D_h \times (e \cdot h)}$为可学习门控矩阵，$f_i$为低秩线性专家函数。HMoE通过子token融合与token融合两级操作，实现跨模态目标线索的丰富。与注意力机制相比，HMoE在保持可比性能的同时，推理速度提升约35%，解决了全局融合的效率瓶颈。

## 实验评估

SEATrack在LasHeR、RGBT234、DepthTrack、VOT-RGBD2022和VisEvent五个基准上评估，对比了FFT（如IIMF、DeT）和PEFT（如ViPT、SDSTrack、XTrack）方法。基线覆盖全面，但缺少最新SSM-based方法如UBATrack的对比。

| 方法 | 类型 | LasHeR PR | DepthTrack F-score | VisEvent PR | 可训练参数 | FPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SEATrack | PEFT | 71.6 | 63.2 | 77.1 | 0.6M | 63.5 |
| IIMF | FFT | 65.7 | 59.8 | 76.3 | 182M | - |
| SDSTrack | PEFT | 70.2 | 61.0 | 76.7 | 2.1M | 20.8 |
| XTrack | PEFT | 65.8 | 61.5 | 77.5 | 5.4M | 10.3 |

SEATrack在LasHeR上PR达71.6，较SDSTrack高1.4，且参数量仅为SDSTrack的28.6%。在VisEvent上，SEATrack PR 77.1，与XTrack的77.5接近，但FPS高达63.5，远超XTrack的10.3，验证了HMoE的效率优势。

消融实验显示，AMG-LoRA单独使用即可在LasHeR上带来18.3%的PR提升，仅增加0.14M参数。缩放因子$w_X$和$w_{\text{rgb}}$初始化为1时性能最优，表明RGB分支的强先验对X模态学习至关重要。HMoE中，每专家2个头时性能最佳，4个头时参数量增加但性能未提升，存在边际收益递减。

评估边界方面，论文未报告置信区间，且未对比SSM-based方法。代码已开源，但超参数细节（如学习率调度）未完全披露。可复现性受限于GPU型号（RTX 4090），不同硬件上FPS可能波动。

## 关联研究分析

从问题动机看，SEATrack与SDSTrack均针对双流PEFT的跨模态交互，但SDSTrack复用冻结注意力层进行全局交互，而SEATrack指出注意力图不一致是性能瓶颈，提出AMG-LoRA进行动态对齐。这一差异源于对“对齐”定义的深化：SDSTrack关注特征空间的对齐，SEATrack则聚焦匹配响应（注意力图）的对齐，认为后者是联合表征学习的前提。

从方法设计看，SEATrack的HMoE与XTrack的MoE均用于跨模态融合，但XTrack的MoE侧重特征增强，通过top-k路由选择专家，而SEATrack的HMoE侧重全局关系建模，通过分层软路由实现子token到token的细粒度交互。这一差异反映了任务特性的不同：XTrack处理模态特异性信息提取，SEATrack则需解决全局上下文依赖。HMoE的效率优势（35% FPS提升）是否源于软路由的稀疏性，还是低秩专家的压缩效果，论文未给出明确归因。

## 总结

SEATrack要解决的核心矛盾是PEFT方法中性能提升伴随的参数膨胀，以及跨模态注意力不一致导致的联合表征学习受阻。其切入点在于指出对齐缺失是效率承诺失效的根源，通过AMG-LoRA动态对齐注意力图，以0.14M参数实现18.3%的PR提升。方法上，SEATrack结合LoRA域适应与AMG动态引导，并引入HMoE实现高效全局融合，在LasHeR上以0.6M参数达到71.6 PR，FPS 63.5。其边界在于精度仍低于最新SOTA（如SCDT的77.4 PR），且模态缺失场景下的鲁棒性依赖AMG的动态调整，但缺乏对极端缺失（如单模态完全失效）的系统评估。当模态可靠性差异超过AMG可学习缩放因子的调节范围时，对齐机制是否仍能避免负迁移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12502)