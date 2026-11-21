# CVPR2026最新论文 ｜Brewing Stronger Features: Dual-Teacher Distillation for Multispectral Earth Observation ｜双教师蒸馏驱动的多光谱地球观测表征学习

研究机构：斯洛文尼亚卢布尔雅那大学

作者：Filip Wolf、Blaž Rolih、Luka Čehovin Zajc

论文原文见 [arXiv](https://arxiv.org/abs/2602.19863)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19863)

> 地球观测（EO）基础模型需同时处理光学与多光谱（MS）数据，但现有掩码图像建模（MIM）预训练侧重局部重建，导致全局语义结构薄弱，难以直接迁移视觉基础模型（VFM）的光学先验。DEO 指出 MIM 与 VFM 训练目标不兼容是跨模态知识转移失效的根源，提出对比自蒸馏双教师框架，将 MS 教师与光学 VFM 教师联合注入学生网络。该方法在分割、变化检测与分类任务上平均提升 3.64、1.2 和 1.31 个百分点，验证了目标兼容性对表征质量的关键作用，但其对 SAR 等非光学模态的扩展性仍受限于教师模型的缺失。

## 研究背景

EO 数据涵盖光学、合成孔径雷达（SAR）及高光谱等多种传感器，空间分辨率从厘米级延伸至公里级。传统监督学习依赖大量人工标注，难以应对跨地域、跨传感器的泛化挑战。自监督预训练通过无标注数据构建通用特征提取器，成为解决标注稀缺的核心路径。其中，掩码图像建模（Masked Image Modeling, MIM）通过重建被遮挡的图像块学习局部特征，是 EO 领域的主流范式。然而，MIM 强调像素级重建，对全局语义结构的约束较弱，导致特征空间缺乏线性可分性，不利于下游密集预测任务。

主流 EO 基础模型如 Prithvi、CROMA 均采用 MIM 或混合目标，虽在多模态融合上取得进展，但特征空间与通用 VFM（如 DINOv3）存在显著差异。VFM 通过对比自蒸馏塑造全局语义，其特征空间高度结构化，适合直接迁移。现有工作如 Copernicus-FM 尝试将 VFM 蒸馏至 MIM 模型，但因目标不兼容，蒸馏效果受限。DEO 的切入点在于：若学生模型的预训练目标与 VFM 教师一致，则光学先验可更高效地迁移至 MS 学生，实现跨模态表征的协同优化。

## 核心方法

### 对比自蒸馏基础框架

DEO 基于 DINO 自蒸馏范式，通过指数移动平均（EMA）更新教师权重，防止师生权重发散。为防止表示坍缩，引入编码率正则化（Coding Rate Regularizer, CR）惩罚低秩协方差矩阵，强制特征在维度上分散。该框架为 MS 分支提供全局语义约束，替代 MIM 的局部重建目标。

### 双教师联合蒸馏机制

MS 分支采用对比自蒸馏，教师仅接收全局视图，学生接收全局与局部视图，损失函数为：

$$ \mathcal{L}_{MS} = \mathcal{L}_{cos}(\mathbf{z}_{MS}^{g \cup l}, \mathbf{z}_{MS}^{g}) + \gamma \mathcal{L}_{CR}(\mathbf{z}_{MS}^{g \cup l}) $$

其中 $\mathcal{L}_{cos}$ 为余弦相似度损失，$\mathcal{L}_{CR}$ 为编码率正则化项。光学分支引入冻结 VFM 教师（DINOv3），蒸馏其类令牌（class token）与补丁令牌（patch token）至学生对应层，损失函数为：

$$ \mathcal{L}_{Opt} = \alpha_1 \mathcal{L}_{distill}(\mathbf{z}_{Opt}^{cls}, \mathbf{z}_{VFM}^{cls}) + \alpha_2 \mathcal{L}_{distill}(\mathbf{z}_{Opt}^{p1}, \mathbf{z}_{VFM}^{p1}) + \alpha_3 \mathcal{L}_{distill}(\mathbf{z}_{Opt}^{p2}, \mathbf{z}_{VFM}^{p2}) $$

该设计解决了 MIM 学生与 VFM 教师特征空间不匹配的问题，使光学先验以兼容方式注入 MS 表征，提升全局语义一致性。

## 实验评估

实验在 GEO-Bench、SpaceNetv1、Sen1Floods11 等数据集上评估，基线覆盖 VFM（DINOv2/v3）、MIM（Scale-MAE、GFM）及 MS 专用模型（CROMA、TerraFM）。DEO 在光学与 MS 分割任务上均取得最优，平均 mIoU 达 80.83（光学）与 69.72（MS），超越 DINOv3-LS（76.40）与 CROMA（62.70）。

| 方法 | 光学 Avg. mIoU | MS Avg. mIoU | 变化检测 F1 |
|---|---|---|---|
| DINOv3-LS | 76.40 | 63.40 | 73.5 |
| CROMA | 63.17 | 53.33 | 72.7 |
| DEO | 80.83 | 69.72 | 75.9 |

消融实验显示，引入 DINOv3 蒸馏使光学性能提升 1.20 点，MS 性能提升 2.37 点；分离光学路径进一步将光学性能提升至 81.20。高解析度光学数据替换低解析度 Sentinel-2 数据后，MS 性能额外提升 0.50 点，表明高分辨率光学特征作为特权知识对 MS 任务有正向迁移。

评估协议采用冻结骨干+微调解码器，指标为 mIoU/F1，但未报告计算效率与内存占用。代码开源，预训练使用 16 块 A100 GPU，50 万图像，100 轮训练。缺乏 SAR 模态实验，且未对比 RAMEN、THOR 等 2025-2026 最新架构，限制了与当前 SOTA 的全面比较。

## 关联研究分析

从预训练目标看，DEO 与 Copernicus-FM 均使用 VFM 蒸馏，但后者基于 MIM，导致特征空间与 VFM 不兼容。DEO 采用对比自蒸馏，使学生特征空间与 DINOv3 对齐，PCA 可视化显示其特征分布更接近 VFM，而非 MIM 模型。这一差异源于目标兼容性：MIM 的局部重建约束弱于对比学习的全局语义约束，导致蒸馏时光学先验无法有效注入 MS 表征。

从骨干网络看，DEO 采用 Swin Transformer 而非标准 ViT，利用其层级结构与 4 像素补丁大小获取细粒度特征。ViT 固定 16 像素补丁限制特征分辨率，不利于密集预测。Swin 的层级设计允许多尺度特征融合，与 VFM 蒸馏的细粒度需求匹配。这一选择解决了 ViT 在分割任务上的分辨率瓶颈，但增加了计算复杂度，论文未报告 FLOPs，部署成本存疑。

## 总结

DEO 针对 MIM 与 VFM 目标不兼容导致的跨模态知识转移失效，提出对比自蒸馏双教师框架，将 MS 教师与光学 VFM 教师联合注入学生网络。该方法在分割、变化检测与分类任务上平均提升 3.64、1.2 和 1.31 个百分点，验证了目标兼容性对表征质量的关键作用。其边界在于依赖光学 VFM 的强度，且假设输入空间对齐，对 SAR 等非光学模态缺乏强教师支持。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19863)