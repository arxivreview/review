# CVPR2026最新论文 ｜You Only Erase Once: Erasing Anything without Bringing Unexpected Content ｜单次擦除无幻觉：基于无配对监督的物体移除框架

研究机构：中山大学

作者：Yixing Zhu、Qing Zhang、Wenju Xu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27599)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27599)

> 图像修复中的物体擦除旨在移除指定物体并补全背景，但现有扩散模型常因训练数据缺乏真实擦除对而生成“幻觉”物体。YOEO通过蒸馏少步扩散模型，结合无配对真实数据与实体分割监督，解决了缺乏Ground Truth时的擦除引导难题。该方法在COCO与EntitySeg基准上显著降低了幻觉率，但依赖预训练分割模型的泛化边界尚待考察。

## 研究背景

图像修复任务要求模型在移除目标物体后，无缝补全缺失区域并保持语义一致性。传统GAN方法虽能处理小面积缺失，但纹理模糊且易产生伪影；扩散模型虽能生成逼真细节，却常因过度生成而在擦除区域插入非目标物体，即“幻觉”现象。这种不一致性源于训练数据与真实场景的错位：现有方法多依赖合成配对数据（如遮挡干净图像），而真实世界中不存在“擦除后”的Ground Truth，导致模型仅学会去噪而非“擦除”。

主流扩散擦除方法依赖监督微调（SFT），使用MSE或LPIPS等像素级损失训练模型重建干净图像。然而，SFT未显式约束“移除物体”这一任务目标，导致模型在复杂开放场景下易产生上下文不一致。YOEO的切入点在于引入无配对真实数据与基于实体分割的无监督信号，通过蒸馏少步模型实现端到端的幻觉抑制，从而在缺乏Ground Truth的情况下引导模型学习“擦除”而非“去噪”。

## 核心方法

### 方法参照系

YOEO基于Stable Diffusion Inpainting 1.5构建，采用Flash Diffusion的蒸馏框架。与标准概念擦除修改交叉注意力层不同，YOEO聚焦于去噪过程的输出约束，通过引入无配对监督信号解决真实场景下的擦除引导缺失问题。

### 少步蒸馏与端到端优化

标准多步扩散模型在早期去噪阶段产生模糊图像，无法直接应用实体分割检测器。YOEO将多步教师模型蒸馏为少步学生模型，使其在早期步骤即可生成清晰结果，从而支持端到端的幻觉检测与抑制。蒸馏过程结合LPIPS损失、分布匹配蒸馏（DMD）及GAN损失，确保学生模型在减少步数的同时保持生成质量。

$$
\mathcal{L}_{distill} = \mathbb{E}_{t, \mathbf{x}_t} \left[ d\left( G_\theta(\mathbf{x}_t, t, \mathbf{c}), \text{ODE}(G_{init}(\mathbf{x}_t, t, \mathbf{c})) \right) \right]
$$

该公式通过最小化学生模型单步输出与教师模型多步ODE预测之间的LPIPS距离，实现少步生成与质量保持的平衡。

### 无配对擦除监督

YOEO引入两项无配对损失：Sundries Suppression (SS) Loss与Entity Feature Coherence (EFC) Loss。SS Loss利用预训练Mask2Former检测生成图像中的非目标实体（Sundries），通过惩罚其像素激活抑制幻觉；EFC Loss计算擦除区域与周围实体的特征余弦相似度，确保语义一致性。

$$
\mathcal{L}_{SS} = \sum_{i \in \mathcal{I}_{sundry}} \alpha_i \left( -\log p_i^0 + \sum_{x,y \in m_i} m_{i,x,y} \right)
$$

该公式通过最大化非Sundries概率并惩罚Sundries掩码内的像素激活，直接抑制非目标物体的生成。

## 实验评估

YOEO在COCO val2017（3,985样本）与EntitySeg（670样本）上评估，基线涵盖GAN（MAT）与扩散模型（SD-Inpainting, ASUKA, OmniPaint等）。YOEO在COCO上MSN（Mean Sundries Num）为0.049，MARS（Mean Area Ratio of Sundries）为0.005，CFD（Context Fidelity Distance）为0.311，显著优于EntityErasure（MSN 0.151, MARS 0.115, CFD 0.453）与ASUKA（MSN 0.728, MARS 0.173, CFD 0.577）。

| 方法 | 参数 | COCO MSN↓ | COCO MARS↓ | COCO CFD↓ | EntitySeg MSN↓ | EntitySeg MARS↓ | EntitySeg CFD↓ |
|---|---|---|---|---|---|---|---|
| EntityErasure | 2608M | 0.151 | 0.115 | 0.453 | 0.554 | 0.115 | 0.453 |
| ASUKA | 11902M | 0.728 | 0.173 | 0.577 | 0.679 | 0.130 | 0.504 |
| OmniPaint | 11902M | 0.336 | 0.045 | 0.407 | 0.600 | 0.146 | 0.508 |
| YOEO | 860M | 0.049 | 0.005 | 0.311 | 0.336 | 0.045 | 0.407 |

消融实验显示，仅使用蒸馏损失（Baseline）时MSN为0.330，加入EFC Loss后降至0.193，再加入SS Loss后进一步降至0.049，表明SS Loss对幻觉抑制贡献最大。无配对数据$D_2$的引入使CFD从0.434降至0.311，验证了真实数据对上下文一致性的关键作用。

评估指标MSN/MARS/CFD聚焦幻觉与一致性，但未覆盖生成质量（FID）的细粒度分析。YOEO在COCO上FID为22.7，略高于OmniPaint的22.1，表明幻觉抑制可能以轻微质量损失为代价。代码已开源，训练使用单A100 GPU，超参数（学习率$1 \times 10^{-5}$，权重衰减0.01）已公开，可复现性良好。

## 关联研究分析

从问题动机看，YOEO与EntityErasure同属物体擦除任务，但EntityErasure依赖合成配对数据与几何先验，而YOEO通过无配对真实数据与分割监督解决Ground Truth缺失问题。这一差异源于真实场景的不可控性：合成数据无法覆盖开放世界的复杂背景，导致EntityErasure在COCO上MSN高达0.151，而YOEO通过SS Loss直接抑制幻觉，将MSN降至0.049。

从方法设计看，YOEO与Flash Diffusion同属扩散蒸馏框架，但Flash Diffusion聚焦于少步生成的效率，YOEO则在此基础上引入任务特定的无配对监督。Flash Diffusion未解决擦除任务的幻觉问题，而YOEO通过EFC Loss确保语义一致性，MSN从0.330（仅蒸馏）降至0.049（蒸馏+SS+EFC），表明任务特定监督对擦除性能的必要性。

## 总结

YOEO解决的核心矛盾是真实场景中缺乏Ground Truth导致的擦除引导缺失。其切入点在于利用无配对真实数据与预训练分割模型，通过少步蒸馏实现端到端的幻觉抑制。YOEO在COCO上MSN降至0.049，MARS降至0.005，显著优于现有SOTA。其边界在于依赖预训练Mask2Former的泛化能力，若分割模型在特定领域（如医学图像）失效，SS Loss的幻觉抑制效果可能退化。当实体分割模型面对未见过的物体类别时，Sundries检测的准确率是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27599)