# WACV2026最新论文 ｜Referring Change Detection in Remote Sensing Imagery ｜指代变化检测

研究机构：美国约翰斯·霍普金斯大学

作者：Yilmaz Korkmaz、Jay N. Paranjape、Celso M. de Melo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.11719)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.11719)

> 遥感影像变化检测旨在从双时相数据中解耦真实地表变化与光照、季节等伪变化，但传统二元检测无法区分变化类型，语义检测又受限于固定类别定义与数据稀缺。本文提出指代变化检测（Referring Change Detection, RCD）任务，通过自然语言提示动态指定检测目标，解耦模型架构与类别数量。其核心是构建Mamba-Transformer混合网络RCDNet，并设计基于扩散模型的合成数据生成管线RCDGen以缓解标注不足。该范式突破了固定输出通道的限制，但在复杂场景下的伪变化抑制能力与最新视觉基础模型路线相比仍显薄弱。

## 研究背景

当检测器面对不同数据集时，同一物理特征可能因标注体系差异被划分为不同类别——这一现象称为类别定义不一致。类别定义不一致导致语义变化检测（Semantic Change Detection, SCD）模型难以跨域泛化，因为模型输出通道数直接绑定类别数量，混合训练不同数据集变得不可行。解决此类问题的经典思路是引入外部语义约束，而自然语言提示恰好提供了灵活且解耦的语义接口，使得模型无需修改架构即可适配任意类别查询。

SCD领域长期面临两大瓶颈：一是数据集规模小且类别严重不平衡，例如SECOND数据集中“playground”类仅占0.38%面积且仅出现129次，而“non-vegetated ground surface”类占43%；二是跨数据集类别定义不统一，如“impervious surface”与“bare ground”在不同数据集中被合并或拆分。现有SCD方法如BiSRNet和SCanNet虽在单一数据集上表现良好，但无法处理类别定义冲突，且受限于固定分类头，难以扩展至新类别。本文的切入点在于将用户意图作为条件输入，通过语言嵌入替代固定类别标签，从根本上解耦了检测目标与模型结构。

## 核心方法

### 方法参照系

本文问题可置于多模态条件分割框架下，其标准流程为：双时相特征提取→跨时相融合→条件解码。与通用流程的关键差异在于，解码条件从固定类别索引变为可变长度的文本嵌入，且训练数据需通过生成式管线合成以覆盖任意类别组合。

### RCDGen合成数据生成

传统SCD训练依赖真实标注数据，但类别不平衡导致稀有类样本不足。RCDGen通过修改InstructPix2Pix管线，以预变化图像和随机选择的类别名作为条件，同时生成后变化图像与变化掩码。其训练目标为最小化去噪误差：

$$\mathcal{L} = \mathbb{E}_{\epsilon \sim \mathcal{N}(0,1), t, z_0} \left[ \| \epsilon - \epsilon_\theta(z_t, t, c_T) \|^2 \right]$$

其中 $z_t$ 为后变化图像潜变量与下采样掩码的通道拼接，$c_T$ 为CLIP文本嵌入。该设计避免了依赖语义分割掩码的推理开销，通过15,000次迭代微调生成29,500张SECOND合成样本、17,500张CNAM-CD样本及8,300张修复样本，显著扩充了训练分布。

### RCDNet跨模态融合解码

RCDNet采用VMamba孪生编码器提取双时相特征，通过Concat & Selective Scan模块实现跨分支长程依赖建模。关键创新在于Mask Decoder Block（MDB）引入交叉注意力机制，以CLIP文本嵌入为Key/Value引导视觉Query选择：

$$Q_{vis} = \text{CrossAttn}(Q_{vis}, K_{text}, V_{text})$$

其中 $K_{text}, V_{text}$ 来自文本编码器，$Q_{vis}$ 为融合特征。该设计解决了固定分类头无法处理动态类别查询的问题，使模型仅需一次前向传播即可生成针对特定类别的二元变化掩码，且可通过多次前向传播聚合为完整语义图。

## 实验评估

实验在SECOND、CNAM-CD（SCD）及LEVIR-CD、WHU-CD（BCD）上进行，基线覆盖HRSCD、BAN、BiSRNet、SCanNet等经典SCD方法及ChangeFormer、ChangeMamba等BCD方法，但缺失2024-2026年PeftCD、ChangeRWKV等最新VFM/SSM混合架构基线。

| 数据集 | 方法 | mIoU (%) | SeK (%) | OA (%) | Fscd (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SECOND | RCDNet (synthetic) | 73.47 | 25.25 | 89.24 | 68.90 |
| SECOND | BiSRNet | 73.04 | 22.26 | 88.19 | 65.21 |
| CNAM-CD | RCDNet (synthetic) | 75.32 | 33.81 | 88.95 | 73.50 |
| CNAM-CD | SCanNet | 71.38 | 22.68 | 84.69 | 61.21 |

RCDNet (synthetic) 在SECOND上SeK较BiSRNet提升2.99，在CNAM-CD上mIoU较SCanNet提升3.94，表明合成数据预训练显著改善了稀有类检测能力。

消融实验显示，合成数据预训练在CNAM-CD上带来mIoU 2.49的提升（75.32 vs 72.83），而在SECOND上仅提升0.43（73.47 vs 73.04），提示合成数据对类别更不平衡的数据集收益更大。混合数据集训练（RCDNet (mixed)）在CNAM-CD上mIoU达73.39，略低于独立训练（72.83），表明跨数据集类别定义冲突仍对性能产生负面影响。

评估协议采用标准SCD指标，但未报告置信区间或多次运行方差。代码未公开，超参数（如学习率 $6 \times 10^{-5}$、batch size 4）在NVIDIA RTX A6000上可复现，但合成数据生成依赖InstructPix2Pix预训练权重，复现成本较高。

## 关联研究分析

从问题动机看，RCD与SeFi-CD同属语言引导变化检测，但SeFi-CD使用冻结视觉基础模型生成视觉提示，而RCDNet训练Mamba编码器以避免基础模型在遥感域的幻觉。这一差异源于任务特性：SeFi-CD依赖基础模型的强先验，适合数据充足场景；RCDNet则通过轻量级编码器适配数据稀缺场景，但牺牲了部分特征表示质量。

从方法设计看，RCDNet与ChangeMamba共享孪生SSM骨干，但ChangeMamba仅处理二元变化，而RCDNet引入交叉注意力解码器支持文本条件。这一扩展解决了固定输出通道限制，但引入了额外计算开销。在LEVIR-CD上，RCDNet (synthetic) IoU为85.8%，低于ChangeRWKV的95.85%（据领域综述），表明语言引导机制在单一类别检测中未带来性能增益，其价值主要体现在灵活性与跨域能力而非精度提升。

## 总结

本文核心矛盾在于SCD固定类别定义与数据稀缺导致的泛化失效。RCD通过语言提示解耦检测目标与模型架构，RCDGen通过扩散模型合成数据缓解标注不足。实验证明其在CNAM-CD上mIoU达75.32%，SeK达33.81%，显著优于基线。但边界在于：缺乏显式伪变化抑制模块，在光照剧烈变化场景下鲁棒性未经验证；BCD任务上性能落后于最新SSM架构，表明语言引导在单一类别检测中效率较低。当支持集增大到5-shot时，合成数据的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.11719)