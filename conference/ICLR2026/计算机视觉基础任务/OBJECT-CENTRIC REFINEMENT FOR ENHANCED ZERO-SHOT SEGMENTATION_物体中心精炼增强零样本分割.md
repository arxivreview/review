# ICLR2026最新论文 ｜OBJECT-CENTRIC REFINEMENT FOR ENHANCED ZERO-SHOT SEGMENTATION ｜物体中心精炼增强零样本分割

作者：Srinivasa Rao Nandam、Sara Atito、Zhenhua Feng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_38118991)

> 零样本语义分割（Zero-Shot Semantic Segmentation, ZSS）旨在利用视觉-语言模型识别训练阶段未见的类别，但CLIP的Patch特征缺乏物体中心结构，导致密集预测时空间定位模糊。现有方法多聚焦于解码器侧的注意力优化，忽视了编码器内部特征表示的缺陷。OC-ZSS通过引入自监督引导的物体提示与双阶段物体精炼注意力模块，在冻结CLIP骨干的前提下重构Patch表示。该方法在标准基准上刷新了SOTA，但其依赖外部DINO模型生成掩码的机制，在物体重叠或模糊场景下的鲁棒性仍存疑。

## 研究背景

当CLIP将图像编码为全局嵌入时，其Patch级特征仅捕捉局部纹理，缺乏将像素自然分组为语义连贯区域的内在能力。这种“物体中心结构”的缺失，使得直接基于Patch-文本对齐的分割方法在未见类别上表现不佳，因为模型无法区分物体边界与背景噪声。为弥补这一缺陷，研究者通常引入外部结构先验或修改解码器逻辑，但这类方法往往增加了计算开销，或未能从根本上改善视觉特征的空间一致性。

零样本分割的主流路线分为两阶段范式与单阶段参数高效范式。两阶段方法如ZegFormer先生成类无关掩码再分类，流程复杂且依赖掩码生成器质量；单阶段方法如ZegCLIP、CLIP-RC和OTSeg通过提示学习或Sinkhorn注意力优化解码器，但均假设CLIP的Patch特征已具备足够的空间定位能力，仅通过调整注意力权重来匹配文本。这一假设忽略了CLIP Patch特征本身缺乏物体中心性的根本局限。OC-ZSS的切入点在于，不改变CLIP骨干，而是通过外部自监督信号引导编码器内部生成物体级特征，并以此迭代精炼Patch表示，从源头提升视觉特征的空间语义质量。

## 核心方法

### 方法参照系

OC-ZSS基于CLIP ViT-B/16骨干，采用视觉提示微调（Visual Prompt Tuning, VPT）与多提示Sinkhorn注意力（MPSA）解码器。与CLIP-RC等使用固定网格区域提示的方法不同，OC-ZSS的核心差异在于引入动态的、由自监督聚类引导的物体提示，并设计了专门的模块来迭代精炼这些提示与Patch特征之间的交互，而非简单的特征融合。

### 自监督引导的物体提示

设计动机在于解决无监督条件下如何定位物体区域的问题。传统Slot Attention依赖随机初始化，易发生Slot Collapse；CLIP-RC使用固定网格，无法适应物体形状。OC-ZSS利用预训练DINO模型的特征进行Voronoi聚类，生成注意力掩码 $M_{ssl}$。该掩码引导冻结的物体提示 $O$ 在CLIP编码器中通过掩码注意力机制关注特定的物体区域：

$$ O_{coarse} = \text{MaskAttn}(O, H, M_{ssl}) $$

其中 $H$ 为CLIP的Patch嵌入。这一机制使得物体提示无需标注即可捕获粗略的物体特征，为后续精炼提供了结构化的初始化，避免了随机初始化的不稳定性。

### 双阶段物体精炼注意力（ORA）

设计动机在于解决粗略物体特征与物体无关Patch特征之间的语义鸿沟。ORA模块通过迭代交叉注意力，同时更新物体特征 $O$ 和Patch特征 $H$。在第 $s$ 次迭代中，Patch特征通过物体特征进行语义增强，物体特征通过Patch特征进行空间细化：

$$ H^{(s+1)} = H^{(s)} + \text{CrossAttn}(H^{(s)}, O^{(s)}, O^{(s)}) $$

$$ O^{(s+1)} = O^{(s)} + \text{CrossAttn}(O^{(s)}, H^{(s)}, H^{(s)}) $$

这种双向精炼机制促进了更紧密的语义分组。此外，ORA内部引入粒度注意力机制，使用多膨胀率的深度可分离空洞卷积替代线性投影，以捕捉不同空间尺度的物体特征，提升了对大小不一物体的鲁棒性。

## 实验评估

| 方法 | VOC 2012 hIoU (Inductive) | PASCAL Context hIoU (Inductive) | COCO-Stuff 164K hIoU (Inductive) |
| :--- | :--- | :--- | :--- |
| ZegCLIP | 81.9 | 57.3 | 41.5 |
| CLIP-RC | 80.7 | 55.0 | 40.6 |
| OTSeg | 86.2 | 60.4 | 41.6 |
| OC-ZSS | 89.2 | 58.7 | 42.5 |

OC-ZSS在归纳设置下于VOC 2012取得89.2%的hIoU，显著优于OTSeg（86.2%）和CLIP-RC（80.7%）。在PASCAL Context上，OC-ZSS的58.7%略低于OTSeg的60.4%，但在COCO-Stuff上以42.5%领先。这表明物体中心精炼在类别数量较少、物体结构清晰的VOC上收益最大，而在复杂背景较多的Context上，其优势被OTSeg的Sinkhorn注意力机制部分抵消。

| 组件 | VOC 2012 hIoU | PASCAL Context hIoU |
| :--- | :--- | :--- |
| Baseline (No ORA, No Prompt) | 87.1 | 58.0 |
| + ORA (Random Init) | 88.3 | 58.4 |
| + DINO-guided Prompts | 89.2 | 58.7 |

消融实验显示，仅添加ORA模块（随机初始化）在VOC上带来+1.2%的提升，而引入DINO引导的提示后进一步提升至89.2%。这证实了DINO聚类提供的结构先验对于物体定位至关重要，随机初始化的物体特征无法有效引导Patch精炼。在PASCAL Context上，增益较小（+0.7%），暗示在复杂场景中，物体提示的引导作用受到背景干扰的限制。

评估协议采用标准的seen/unseen划分，指标为mIoU与hIoU。代码已开源，使用单张A100或四张RTX 3090训练。局限在于未报告计算效率的详细对比（仅提及参数3.35G），且未评估在物体严重重叠或极端小目标场景下的性能，DINO掩码的偏差可能在此类场景中放大。

## 关联研究分析

从方法设计看，OC-ZSS与ProxyCLIP和CLIP-DINOiser形成鲜明对比。后者试图通过蒸馏或代理注意力使CLIP特征模仿DINO的局部结构，本质上是在特征空间进行对齐；而OC-ZSS不模仿DINO特征，仅利用DINO聚类生成掩码来引导物体提示的注意力，随后通过ORA在CLIP内部迭代精炼。这种“引导而非模仿”的策略保留了CLIP的全局语义优势，同时注入了物体中心结构，避免了蒸馏过程中可能丢失的语义信息。

从问题动机看，OC-ZSS与Slot Attention系列工作（如OVSegmentor）存在根本差异。OVSegmentor生成独立的Group Tokens用于分类，需端到端训练；OC-ZSS则不生成新的Token，而是利用物体提示作为“锚点”来精炼现有的Patch特征，使其更物体中心。这种设计使得OC-ZSS能在冻结骨干上运行，降低了训练成本，但代价是依赖外部DINO模型，引入了额外的计算依赖和潜在的域偏移风险。

## 总结

OC-ZSS针对CLIP Patch特征缺乏物体中心结构这一核心矛盾，提出通过自监督引导的物体提示与双阶段ORA模块进行特征精炼。该方法在VOC 2012归纳设置下达到89.2%的hIoU，证明了物体中心精炼对零样本分割的有效性。然而，其性能依赖于DINO聚类掩码的质量，在PASCAL Context等复杂场景下增益有限，且固定数量的物体提示难以适应图像中物体数量的动态变化。当图像中物体数量远超提示数量或物体边界极度模糊时，DINO引导的掩码是否仍能提供有效的结构先验，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_38118991)