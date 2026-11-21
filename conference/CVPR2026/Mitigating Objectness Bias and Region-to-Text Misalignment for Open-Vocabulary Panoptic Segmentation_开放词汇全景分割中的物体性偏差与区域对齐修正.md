# CVPR2026最新论文 ｜Mitigating Objectness Bias and Region-to-Text Misalignment for Open-Vocabulary Panoptic Segmentation ｜开放词汇全景分割中的物体性偏差与区域对齐修正

研究机构：斯洛文尼亚卢布尔雅那大学、瑞士苏黎世联邦理工学院

作者：Nikolay Kormushev、Josip Šarić、Matej Kristan

论文原文见 [arXiv](https://arxiv.org/abs/2603.21386)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21386)

> 开放词汇全景分割旨在突破固定类别限制，实现任意文本描述的实例级与背景级像素预测，但现有掩码Transformer架构存在物体性分数偏差，导致未见类别掩码被错误丢弃。CLIP等视觉-语言模型的全局对齐特性缺乏区域级定位能力，直接应用时分类精度受限。本文提出OVRCOAT框架，通过CLIP条件物体性调整（COAT）修正掩码选择偏差，并结合开放词汇掩码-文本精炼（OVR）增强区域对齐。该方法在ADE20K上取得28.6的PQ，较SOTA提升5.5%，但语义分割性能略低于专用模型，且微调策略对闭集任务存在轻微负迁移。

## 研究背景

全景分割要求模型同时区分实例（things）与背景（stuff），传统方法受限于训练集固定词汇，无法处理开放世界中的新类别。掩码Transformer（Mask2Former）通过生成掩码提案并分类实现全景解析，但其物体性头在闭集数据上训练，对未见类别的掩码赋予极低分数，导致有效实例被误判为背景。这一偏差源于void token在训练数据未标注区域形成的背景偏置，使得测试时新类别掩码的物体性分数被系统性压低。

CLIP等视觉-语言模型通过对比学习建立图像-文本共享嵌入空间，但其训练目标仅为全局匹配，导致patch特征缺乏空间局部性，直接用于区域级分类时定位模糊。早期开放词汇分割方法依赖冻结CLIP骨干，通过掩码池化提取特征，但计算开销大且泛化能力有限。MAFT+等近期工作通过微调CLIP增强语义理解，但在全景分割任务上改进有限，且架构复杂、内存占用高。本文切入点在于同时解决物体性偏差与区域对齐不足两个耦合问题，通过轻量级模块修正掩码选择，并通过高效微调策略增强CLIP的区域级理解能力。

## 核心方法

### 掩码Transformer全景分割参照系

标准掩码Transformer流程包括：生成掩码提案、计算物体性分数、丢弃低分掩码、对剩余掩码进行类别分类。本文问题与该通用流程的关键差异在于：物体性分数计算依赖闭集训练的void token，对开放词汇类别存在系统性偏差；CLIP区域特征与文本嵌入的对齐精度不足，影响分类准确性。

### CLIP条件物体性调整（COAT）

COAT模块作用于掩码选择环节，修正物体性分数偏差。标准流程中，物体性分数 $p_{obj}$ 定义为 $1 - p_{void}$，其中 $p_{void}$ 是掩码特征与void token的相似度。本文引入CLIP分类置信度 $p_{cer}$ 作为修正因子，调整后的物体性分数为：

$$p'_{obj} = p_{obj} + \gamma \cdot (p_{cer} - p_{obj})$$

其中 $\gamma$ 为CLIP信任因子（设为0.5）。该公式的物理含义是：当CLIP对掩码内容的分类置信度高时，提升其物体性分数，保留可能被误判为背景的未见类别掩码。设计动机在于解决void token在闭集训练下对未见类别的抑制效应，利用CLIP的大规模预训练知识消除词汇偏差。

### 开放词汇掩码-文本精炼（OVR）

OVR模块作用于掩码分类环节，增强CLIP的区域级对齐。标准流程中，掩码特征通过池化后与文本嵌入匹配，但CLIP的全局训练导致区域特征定位模糊。本文提出两阶段微调策略：第一阶段冻结CLIP图像编码器，预训练掩码Transformer；第二阶段解冻CLIP图像编码器，联合优化掩码生成与区域-文本对齐。总损失函数为：

$$\mathcal{L} = \mathcal{L}_{M2F} + \alpha \cdot \mathcal{L}_{cls}$$

其中 $\mathcal{L}_{M2F}$ 为掩码Transformer标准损失，$\mathcal{L}_{cls}$ 为掩码分类交叉熵损失，$\alpha$ 设为0.1。该公式的物理含义是：通过联合优化掩码生成精度与区域-文本对齐，使CLIP特征更适应区域级分类任务。设计动机在于解决CLIP全局对齐特性导致的区域定位模糊问题，通过有限微调增强区域理解能力，同时保持泛化性。

## 实验评估

实验在ADE20K、Cityscapes、Mapillary Vistas三个开放词汇全景分割数据集上评估，对比MaskCLIP、FC-CLIP、MAFT+等SOTA方法。基线覆盖掩码Transformer路线，但缺失免训练方法（如OV-Stitcher、NERVE）的直接对比，因任务指标不同（PQ vs mIoU）。

| 方法 | ADE20K PQ | Cityscapes PQ | Mapillary Vistas PQ |
| --- | --- | --- | --- |
| FC-CLIP | 23.4 | 32.9 | 15.7 |
| MAFT+pan | 23.1 | 38.3 | 19.8 |
| OVRCOAT | 28.6 | 45.3 | 19.6 |

OVRCOAT在ADE20K上PQ 28.6，较MAFT+pan的23.1提升5.5；Cityscapes上PQ 45.3，较MAFT+pan的38.3提升7.0；Mapillary Vistas上PQ 19.6，较MAFT+pan的19.8略低0.2。

| 配置 | ADE20K PQ | Cityscapes PQ | Mapillary Vistas PQ |
| --- | --- | --- | --- |
| Baseline (FC-CLIP) | 26.8 | 44.0 | 18.3 |
| +COAT | 27.6 | 44.6 | 18.8 |
| +OVR | 27.6 | 44.5 | 19.2 |
| +COAT+OVR (OVRCOAT) | 28.6 | 45.3 | 19.6 |

消融显示COAT单独贡献1.4-3.0 PQ提升，OVR单独贡献1-5 PQ提升，两者结合达到最优。反直觉发现：OVR在COCO闭集任务上PQ下降1.4%，因COAT模块在闭集场景下引入CLIP置信度噪声；语义分割性能略低于专用模型，因全景分割的实例区分需求消耗模型容量。

评估指标完备（PQ/SQ/RQ），但缺失计算效率维度（仅报告内存占用）。可复现性良好：代码开源，超参数明确（AdamW, lr=1e-4/5e-5, 3x A100 GPU, batch size=9），训练数据为COCO闭集全景分割数据集。

## 关联研究分析

从问题动机看，OVRCOAT与MAFT+同属掩码Transformer微调路线，但MAFT+聚焦于CLIP骨干微调以增强语义理解，而OVRCOAT额外引入COAT模块专门解决物体性偏差问题。这一差异源于任务特性：全景分割的掩码选择环节对物体性分数敏感，闭集训练的void token对新类别的抑制效应比语义分割更显著。MAFT+未显式处理此偏差，导致其在未见类别上的检测率受限，而OVRCOAT通过CLIP置信度修正，在ADE20K未见类别上实现25%的平均相对提升。

从方法设计看，OVRCOAT与FC-CLIP共享冻结CLIP骨干与掩码池化设计，但FC-CLIP依赖集成策略（掩码Transformer+CLIP）进行分类，而OVRCOAT通过OVR微调使CLIP本身具备区域级分类能力。这一差异源于计算效率考量：FC-CLIP的集成策略需多次评估CLIP骨干，内存占用高；OVRCOAT的OVR微调通过两阶段训练，避免内容依赖词汇嵌入，内存占用降低56%（16.1 GB/image）。查询侧增强在数据充足时是否仍有增益，论文未给出回答，因OVR微调依赖COCO闭集数据，其在更大规模开放词汇数据上的泛化能力未验证。

## 总结

本文要解决的核心矛盾是掩码Transformer物体性偏差与CLIP区域对齐不足在全景分割任务中的耦合失效。现有方法如MAFT+通过微调CLIP增强语义理解，但未显式处理物体性偏差，导致未见类别掩码被错误丢弃；本文凭借COAT模块利用CLIP置信度修正物体性分数，并通过OVR两阶段微调增强区域对齐，实现了对两个问题的联合解决。实验证明OVRCOAT在ADE20K上PQ 28.6，较SOTA提升5.5，在Cityscapes上PQ 45.3，较SOTA提升7.0。本文的边界在于：OVR微调在COCO闭集任务上引入1.4%的PQ下降，语义分割性能略低于专用模型，且微调策略依赖COCO闭集数据，其在更大规模开放词汇数据上的泛化能力未验证。当训练数据从COCO扩展到包含更多未见类别的开放词汇数据集时，COAT模块的CLIP置信度修正是否仍能有效抑制物体性偏差，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21386)