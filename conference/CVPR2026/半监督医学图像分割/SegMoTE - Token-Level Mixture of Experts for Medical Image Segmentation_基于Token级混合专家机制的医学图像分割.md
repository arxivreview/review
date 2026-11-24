# CVPR2026最新论文 ｜SegMoTE: Token-Level Mixture of Experts for Medical Image Segmentation ｜基于Token级混合专家机制的医学图像分割

研究机构：四川大学、阿里巴巴达摩院

作者：Yujie Lu、Jingwen Li、Sibo Ju 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19213)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19213)

> 医学图像分割面临模态异构与标注成本的双重约束，现有基础模型适配方法依赖大规模数据微调导致分布偏移与表征同质化。SegMoTE通过冻结SAM编码器并引入Token级混合专家（MoTE）机制，以极小参数代价实现模态特异性适配。该方法在0.15M数据上训练17M参数，在域外数据集上超越基线1%-6%。其核心价值在于验证了“结构创新替代数据规模”的可行性，但缺乏对极端少样本场景的验证。

## 研究背景

交互式分割模型通过用户交互缓解标注负担，但跨模态泛化能力受限。Segment Anything Model (SAM) 凭借大规模预训练具备通用分割能力，但其原始输出Token在处理CT、MRI等异构医学图像时逐渐同质化，导致模态特异性表征区分度不足。这种表征退化源于全参数微调或解码器微调引发的分布偏移，使模型向新数据分布漂移，削弱了原始零样本泛化能力。

主流路线如MedSAM与IMIS通过扩大数据集规模（如IMed-361M）提升性能，但忽视了数据冗余与模态差异导致的监督噪声。这种“数据规模竞赛”未能解决表征设计的根本问题，且在临床部署中面临计算资源与标注成本的高昂代价。SegMoTE的切入点在于：不依赖数据规模扩张，而是通过Token级动态路由机制，在保持SAM原始能力的前提下，以最小参数增量实现模态自适应，从而在低标注成本下达成高性能分割。

## 核心方法

### 方法参照系

本文问题属于基础模型协同学习路线，但区别于MedSAM等全参数微调范式。标准流程通常更新SAM的Mask Decoder或引入Adapter层，而SegMoTE冻结SAM编码器与解码器，仅引入轻量级MoTE与PPT模块，核心差异在于将模态适配从“参数更新”转向“Token动态选择”。

### Token级混合专家机制

传统SAM Mask Decoder使用统一输出Token处理所有模态，导致异构数据下特征混淆。SegMoTE引入可学习专家Token集合，维度为$[N \times 256]$，与原始SAM输出Token及提示Token拼接后进入解码器。通过路由门控网络计算每个Token在$E$个专家上的Logits，采用Noisy Top-K策略注入高斯噪声$\epsilon=1e-2$以防止路由过早收敛：

$$
\text{logits}_{b,t} = \mathbf{x}_{b,t} W_g^T + \sigma(\mathbf{x}_{b,t} W_n^T) \mathbf{Z}
$$

其中$\mathbf{Z}$为高斯随机噪声。该机制通过动态激活最适配当前模态的专家Token，实现模态特异性表征提取，解决了统一Token在异构数据下的区分度不足问题。

### 渐进式提示Token化

稀疏类别分割任务中，用户交互提示增加操作负担。PPT机制随机采样Mask与文本提示作为前景先验，通过多头注意力引导可学习查询$Q$捕获前景-背景关系。训练过程中，特征Token逐步学习区分前景与背景，经MLP投影与残差融合生成语义对齐的特征条件提示Token。该设计使模型在推理时无需人工交互即可实现自动分割，特别适用于ISIC等二分类任务，降低了标注依赖。

## 实验评估

实验在MedSeg-HQ（0.15M掩码）上训练，评估域内（AMOS, CHAOS等）与域外（ISLES, SegThor, TotalSegmentator MRI）数据集。基线覆盖SAM、MedSAM、IMIS等基础模型适配方法，但缺失FixMatch、Mean Teacher等半监督学习（SSL）基线，限制了与SSL路线的直接对比。

| 数据集 | 方法 | Dice |
| :--- | :--- | :--- |
| ISLES | IMIS | 71.24 |
| ISLES | SegMoTE | 77.30 |
| SegThor | IMIS | 80.52 |
| SegThor | SegMoTE | 83.39 |
| TotalSegmentator (MRI) | IMIS | 70.62 |
| TotalSegmentator (MRI) | SegMoTE | 71.48 |

SegMoTE在ISLES上较IMIS提升6.06%，在SegThor上提升2.87%，验证了MoTE机制在域外泛化上的优势。消融实验显示，专家数量$N=4$时性能最优，$N=12$时显著下降，表明专家数超过模态数会导致过拟合。PPT在ISLES上较无PPT提升6.28%，证明自动提示在跨域场景下的有效性。

评估指标仅使用Dice系数，未报告边界精度或临床可用性指标。训练使用8块RTX 4090 GPU，Batch Size为10，学习率1e-4，7/12 Epoch减半。代码未公开，但超参数完整披露，可复现性中等。

## 关联研究分析

从问题动机看，SegMoTE与SC-SAM同属基础模型适配路线，但SC-SAM通过Adapter层微调SAM图像编码器以缓解域差距，而SegMoTE冻结编码器仅训练Token级MoTE。这一差异源于SC-SAM关注域适应，SegMoTE关注模态特异性表征。SegMoTE的冻结策略可能限制了对复杂解剖结构的精细拟合，但换取了计算效率与原始能力保留。

从方法设计看，SegMoTE与CoDiR均关注伪标签/提示质量优化，但CoDiR利用扩散模型进行结构级精修以消除拓扑错误，SegMoTE通过PPT实现无交互提示生成。CoDiR依赖生成式模型的高计算成本，SegMoTE依赖轻量级注意力机制。在极端少样本（<10例）场景下，CoDiR的生成式精修可能更具鲁棒性，而SegMoTE的Token路由可能因数据不足导致专家激活失衡，论文未提供此类对比。

## 总结

SegMoTE解决了基础模型适配中数据规模扩张与分布偏移的矛盾，通过Token级MoTE机制以17M参数实现模态自适应，在ISLES上达到77.30 Dice，较IMIS提升6.06%。其边界在于仅验证了二分类任务的PPT有效性，多分类任务中类干扰问题未解决，且缺乏与SSL方法的直接对比。当支持集规模进一步缩减至单例时，MoTE的专家激活稳定性是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19213)