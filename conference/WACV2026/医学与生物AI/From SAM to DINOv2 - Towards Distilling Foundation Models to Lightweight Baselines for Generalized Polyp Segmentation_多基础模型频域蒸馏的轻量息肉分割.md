# WACV2026最新论文 ｜From SAM to DINOv2: Towards Distilling Foundation Models to Lightweight Baselines for Generalized Polyp Segmentation ｜多基础模型频域蒸馏的轻量息肉分割

作者：Shivanshu Agnihotri、Snehashis Majhi、Deepak Ranjan Nayak 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09307)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09307)

> 结肠镜息肉分割面临临床部署中算力受限与跨域泛化弱的双重约束，现有轻量网络缺乏全局语义先验，而大规模基础模型直接迁移则因参数冗余与领域差距难以落地。Polyp-DiFoM 通过多基础模型特征频域分解与双阶段蒸馏，将语义先验注入 U-Net 等轻量骨干，在未见数据集上显著提升泛化能力。该方法以极低计算开销实现了接近重型模型的精度，但其对干净基准的精度提升有限，且未验证视频时序场景下的有效性。

## 研究背景

息肉分割的核心难点在于息肉形态多变、边界模糊且常与黏膜纹理混淆，导致传统卷积网络难以捕捉长程依赖与精细边界。解决此问题需引入全局上下文建模，但 Vision Transformer (ViT) 等架构虽能提升精度，却因二次方计算复杂度无法满足实时临床需求。基础模型（Foundation Models, FMs）如 SAM 和 DINOv2 在自然图像上展现了强大的跨域泛化能力，但其直接应用于医学影像时，受限于数据稀缺、领域差距及高昂的推理成本，无法直接部署于资源受限的内窥镜设备。

当前领域主流路线分为两类：一是追求极致精度的重型模型（如 SAM-Mamba，103M 参数），二是追求轻量化的专用 CNN（如 U-Net，16.7M 参数）。前者精度高但算力开销巨大（423 GFLOPs），后者部署灵活但泛化能力弱，在未见数据集上性能大幅衰减。Polyp-DiFoM 的切入点在于弥合这一鸿沟：不直接微调基础模型，而是将其作为教师，通过蒸馏将富含语义与结构信息的特征迁移至轻量学生模型，从而在保持低计算成本的同时获得跨域鲁棒性。

## 核心方法

### 方法参照系

标准知识蒸馏通常直接对齐教师与学生网络的 Logits 或特征图，旨在让学生模仿教师的输出分布。本文的关键差异在于，它不直接对齐原始特征，而是引入频域编码作为中间层，将教师特征分解为高频与低频分量后分别对齐，并采用多基础模型联合蒸馏策略，以解决单一教师模型信息冗余或噪声干扰的问题。

### 多基础模型语义特征融合

设计动机在于单一基础模型（如仅用 SAM）可能无法覆盖息肉分割所需的全部语义维度，且不同模型的特征空间存在冗余。Polyp-DiFoM 首先从 SAM、DINOv2、OneFormer 和 Mask2Former 中提取高维语义嵌入 $E \in \mathbb{R}^{H \times W \times D}$，通过双线性插值统一空间分辨率至 $32 \times 32$，并在通道维度拼接形成统一表示 $e^* \in \mathbb{R}^{32 \times 32 \times D^*}$。这一操作将多个模型的互补先验聚合为一个紧凑的语义向量，为后续频域分解提供丰富的信息源。

### 频域分解与双阶段蒸馏

设计动机在于空间域特征混合了全局语义与局部细节，直接对齐可能引入噪声。本文对 $e^*$ 应用二维快速傅里叶变换 (FFT) 得到频域表示 $E_{freq}$，并通过径向频率掩码 $M_{HFC}$ 和 $M_{LFC}$ 分离出高频分量（HFC，对应边界细节）和低频分量（LFC，对应全局形状）。随后，通过逆 FFT 重构空间特征：

$$ E_{HFC}^{-1} = \text{IFFT}(M_{HFC} \cdot E_{freq}), \quad E_{LFC}^{-1} = \text{IFFT}(M_{LFC} \cdot E_{freq}) $$

该公式的物理含义是将频域中不同尺度的信息解耦，使高频分量专门指导学生模型学习息肉边缘，低频分量指导其理解整体形态。在蒸馏损失中，L1 阶段对齐 LFC 以优化语义抽象，L2 阶段对齐 HFC 以锐化结构边界，总损失为 $\mathcal{L}_{distill} = \alpha_1 \mathcal{L}_{L1} + \alpha_2 \mathcal{L}_{L2}$，其中 $\alpha_1=1.0, \alpha_2=0.5$，优先保证语义一致性。

## 实验评估

实验在 Kvasir-SEG 和 CVC-ClinicDB（Seen）以及 CVC-300、CVC-ColonDB、ETIS（Unseen）上进行。基线覆盖 U-Net、PraNet 等轻量模型及 SAM-Mamba 等重型 SOTA，但缺失与其他蒸馏方法（如 LiteBounD）的直接对比。

| 方法 | Params (M) | FLOPs (G) | Kvasir-SEG mDice | CVC-ClinicDB mDice |
|---|---|---|---|---|
| U-Net | 16.7 | 73.9 | 81.8 | 82.3 |
| U-Net + Ours | 16.9 | 74.7 | 88.5 | 94.9 |
| PraNet | 30.4 | 13.1 | 89.8 | 89.9 |
| PraNet + Ours | 31.4 | 13.5 | 91.2 | 95.3 |
| SAM-Mamba | 103.0 | 423.0 | 92.4 | 94.2 |

U-Net + Ours 在 CVC-ClinicDB 上 mDice 从 82.3 提升至 94.9，超越 SAM-Mamba 的 94.2，且参数量仅为后者的 1/6。

| 消融配置 | Kvasir-SEG mDice | CVC-ClinicDB mDice |
|---|---|---|
| MSE + FFT | 88.5 | 94.9 |
| MSE + DCT | 72.8 | 83.8 |
| MSE + KL + FFT | 77.8 | 82.5 |

消融显示，FFT 相比 DCT 带来显著增益（+15.7% Dice），表明傅里叶变换在分离医学图像局部细节上优于余弦变换。此外，仅使用 MSE 损失优于 MSE+KL 组合，说明复杂的分布对齐可能引入噪声。

评估指标涵盖 mDice、mIoU 等六项，但缺乏置信区间报告。训练使用单卡 V100，120 个 epoch，代码已开源。未见数据集上的表现验证了泛化能力，但 Seen 数据集上的精度提升幅度（如 U-Net +6.7%）远小于 Unseen 数据集（如 CVC-300 +15.2%），暗示蒸馏主要收益来自跨域鲁棒性而非单纯精度提升。

## 关联研究分析

从问题动机看，Polyp-DiFoM 与 LiteBounD 同属基础模型蒸馏路线，但前者聚焦于频域分解以增强结构细节，后者侧重边界引导蒸馏。Polyp-DiFoM 在 CVC-ClinicDB 上取得 94.9% mDice，略高于 LiteBounD 的 94.8%，但两者在 Kvasir-SEG 上均低于 EndoCaver 的 92.21%。这一差异根源在于 Polyp-DiFoM 的频域分解可能更有效地抑制了教师模型中的高频噪声，而 LiteBounD 的边界引导可能在复杂形态息肉上存在局限。

从方法设计看，Polyp-DiFoM 与 SAM-Mamba 形成鲜明对比。SAM-Mamba 通过适配器直接微调基础模型，追求极致精度（92.4% mDice），但参数量高达 103M。Polyp-DiFoM 则通过蒸馏将先验注入轻量骨干，以 16.9M 参数实现 88.5% mDice。这种取舍反映了临床部署对实时性的硬性约束：Polyp-DiFoM 牺牲了部分峰值精度，换取了 CPU 实时推理的可行性，而 SAM-Mamba 更适合离线高精度分析场景。

## 总结

Polyp-DiFoM 旨在解决轻量息肉分割模型在跨域场景下泛化能力弱的问题，通过多基础模型频域蒸馏将语义先验注入 U-Net 等轻量骨干。该方法在未见数据集上显著提升了分割精度，例如 U-Net + Ours 在 CVC-300 上 mDice 从 71.0% 提升至 86.2%，验证了频域分解在抑制教师噪声、增强边界细节方面的有效性。然而，论文实验仅覆盖静态图像，未涉及视频时序建模，且 Seen 数据集上的精度提升幅度有限，表明蒸馏主要收益在于跨域鲁棒性而非绝对精度。当支持集增大或成像条件进一步退化时，频域分解的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09307)