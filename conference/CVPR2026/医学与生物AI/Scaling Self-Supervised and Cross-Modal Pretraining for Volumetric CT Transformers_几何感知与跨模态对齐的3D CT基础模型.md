# CVPR2026最新论文 ｜Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers ｜几何感知与跨模态对齐的3D CT基础模型

研究机构：荷兰埃因霍温理工大学

作者：Cris Claessens、Christiaan Viviers、Giacomo D'Amicantonio 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.17209)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17209)

> 3D CT影像分析面临体素各向异性导致的几何失真与临床报告噪声引发的语义对齐失效，现有单一自监督或视觉语言模型难以兼顾空间精度与临床语义。SPECTRE通过引入各向异性3D Patch与RoPE抖动显式编码几何信息，并采用DINOv3自蒸馏与SigLIP对齐的两阶段预训练策略，解决了标准Transformer在体积数据上的计算瓶颈与语义缺失问题。该模型在检索与分割任务上展现了优于现有CT基础模型的泛化能力，但其胸腹部数据分布不均与报告噪声敏感性仍制约着其在复杂临床场景中的鲁棒性。

## 研究背景

3D CT影像的体素间距在层厚方向通常为轴面方向的两倍，这种各向异性几何结构使得直接应用2D或各向同性3D Patch会导致空间信息失真。为保留解剖连续性，模型需显式编码体素尺度信息，而临床放射报告作为弱监督信号，其文本描述与影像特征之间存在多对多映射关系，传统对比学习中的负样本噪声会削弱语义对齐效果。

当前CT基础模型主要分为两类：一类如CT-CLIP与Merlin，依赖视觉语言对齐（VLA）学习语义，但受限于单一解剖区域且缺乏细粒度空间特征；另一类如CT-FM与VoCo，采用自监督学习（SSL）捕捉图像结构，但缺乏显式临床语义且未解决3D体积数据的计算复杂度问题。主流方法在几何异质性处理上多依赖插值或简单平移不变性假设，导致跨扫描协议泛化能力不足。SPECTRE的切入点在于将几何感知架构与两阶段预训练结合，通过局部-全局Transformer分层设计平衡计算效率与上下文建模，同时利用SigLIP损失处理报告噪声，实现空间精度与临床语义的统一。

## 核心方法

### 方法参照系

标准3D Vision Transformer（ViT）通过均匀3D Patch分割体积数据，并采用全局自注意力机制建模长距离依赖。该流程在CT影像中面临两大失效：一是Token数量随分辨率立方增长导致计算爆炸，二是各向同性位置编码无法反映层厚与轴面间距的差异。SPECTRE在保留ViT骨干的基础上，针对几何异质性与计算瓶颈进行了架构重构。

### 几何感知Tokenization与分层注意力

针对3D体积数据Token数量立方增长的问题，SPECTRE采用各向异性Patch尺寸 $H_p \times W_p \times D_p = 16 \times 16 \times 8$，其中深度方向Patch尺寸减半以匹配层厚间距，将典型 $128 \times 128 \times 64$ 体积压缩为512个Token，与2D $256 \times 256$ 图像Token数相当。为平衡局部细节与全局语义，模型引入局部ViT（$ViT_l$）与全局ViT（$ViT_g$）分层结构。局部ViT在 $G$ 个窗口内执行受限注意力，每个窗口生成一个[cls] Token $c_w$ 与平均池化特征 $\bar{t}_w$，拼接后形成窗口级表示：

$$
\mathbf{u}_w = \text{Concat}(c_w, \bar{t}_w)
$$

全局ViT对 $G$ 个窗口表示执行全注意力，由于 $G \ll m$（$m$为窗口内Token数），计算复杂度从 $O(N^2)$ 降至 $O(G^2 + Gm)$，实现了大规模体积数据的可计算性。该设计解决了标准全局注意力在3D数据上的内存瓶颈，同时保留了扫描级上下文信息。

### 两阶段预训练：DINOv3自蒸馏与SigLIP对齐

第一阶段采用DINOv3框架进行自监督预训练，通过学生-教师模型对与掩码自蒸馏学习局部几何特征。针对3D数据空间邻域更多的特性，掩码比例 $\rho$ 调整为 $U(0.2, 0.7)$，高于DINOv3的 $U(0.1, 0.5)$，以增强任务难度。损失函数结合DINO、iBOT与KoLeo项，权重比为 $1:1:0.1$，其中iBOT项对掩码位置进行Token级交叉熵预测：

$$
\mathcal{L}_{iBOT} = -\frac{1}{|M|} \sum_{m \in M} \sum_{c=1}^{C} q_t^{[c]}(m) \log p_s^{[c]}(m)
$$

该公式通过教师模型在掩码位置提供的软标签，迫使学生在局部窗口内重建被遮挡的几何结构，强化了空间一致性。第二阶段引入SigLIP损失对齐CT与放射报告，替代CLIP的InfoNCE损失。SigLIP采用对称Sigmoid二元交叉熵，缓解了临床报告中多标签共现导致的负样本噪声问题，使模型在弱监督下学习更鲁棒的语义映射。

## 实验评估

实验在KiTS23、LiTS、CT-RATE与Merlin数据集上评估，基线涵盖nnU-Net、SwinUNETRv2等分割模型及CT-CLIP、Merlin等基础模型。SPECTRE在KiTS23上以86.64% Dice超越nnU-Net的85.99%，在LiTS上达到80.14%，接近全监督SOTA但低于领域综述中Spatial-Aware Self-Supervision的92.23%（据领域综述，后者可能采用不同预训练协议或微调策略）。在CT-RATE检索任务中，SPECTRE的Recall@5为17.5%，显著优于CT-CLIP的2.9%，验证了联合预训练在语义检索上的优势。

| 数据集 | 方法 | Dice (%) / Recall@5 (%) |
| :--- | :--- | :--- |
| KiTS23 | nnU-Net | 85.99 |
| KiTS23 | SPECTRE | 86.64 |
| LiTS | SPECTRE | 80.14 |
| CT-RATE | CT-CLIP | 2.9 |
| CT-RATE | SPECTRE | 17.5 |

消融实验未在正文中详细展开，但论文指出SigLIP阶段对检索性能的贡献大于分割任务，暗示VLA目标主要增强语义对齐而非空间精度。评估边界方面，预训练数据偏向胸部CT（NLST 132,985例 vs AMOS 2,238例），导致腹部任务性能相对较弱；报告噪声与机构间术语差异未通过额外数据清洗或去偏策略处理，可能影响跨中心泛化。代码与预训练配方已开源，但GPU配置与训练时长未在正文中披露，可复现性依赖补充材料。

## 关联研究分析

从方法设计看，SPECTRE与TAP-CT（Veenboer et al., 2025）均基于DINOv2/v3架构，但TAP-CT仅采用SSL目标，而SPECTRE引入VLA阶段以注入临床语义。这一差异源于任务目标的不同：TAP-CT聚焦分割与分类的结构捕捉，SPECTRE则需兼顾检索与语义理解。SPECTRE的各向异性Patch与RoPE抖动设计是针对CT几何异质性的特有改进，TAP-CT未显式处理层厚差异，这可能解释SPECTRE在跨扫描协议泛化上的潜在优势。

从问题动机看，SPECTRE与MedGMAE（ICLR 2026）均试图解决3D预训练的计算效率问题，但MedGMAE采用高斯基元重建替代体素级重建，属于生成式SSL路线；SPECTRE则通过分层注意力降低计算复杂度，属于判别式SSL+VLA路线。MedGMAE在AMOS上以0.82 DSC领先，但缺乏语言对齐能力；SPECTRE在检索任务上显著优于MedGMAE（未直接对比，但基于CT-CLIP基线推断），表明两阶段预训练在语义任务上的必要性。查询侧增强在数据充足时是否仍有增益，论文未给出回答，但SigLIP对噪声的鲁棒性暗示其在弱监督场景下的优势。

## 总结

SPECTRE旨在解决3D CT影像中几何异质性与临床语义对齐的矛盾，通过各向异性Patch与分层Transformer架构克服计算瓶颈，利用DINOv3自蒸馏与SigLIP对齐的两阶段预训练实现空间精度与语义理解的统一。实验显示其在KiTS23分割（86.64% Dice）与CT-RATE检索（17.5% Recall@5）上优于现有基线，验证了联合预训练的有效性。然而，预训练数据胸部偏重与报告噪声未处理，导致腹部任务性能受限且跨中心泛化能力存疑。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17209)