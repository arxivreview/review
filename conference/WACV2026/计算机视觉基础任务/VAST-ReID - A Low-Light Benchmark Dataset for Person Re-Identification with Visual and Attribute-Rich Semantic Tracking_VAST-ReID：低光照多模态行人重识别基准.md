# WACV2026最新论文 ｜VAST-ReID: A Low-Light Benchmark Dataset for Person Re-Identification with Visual and Attribute-Rich Semantic Tracking ｜VAST-ReID：低光照多模态行人重识别基准

研究机构：印度理工学院、韩国科学技术研究院

作者：Hammad Khan、Rakesh Kumar Giri、Kamalakar Vijay Thakare 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_daf50d52d3c2)

> 行人重识别（Person Re-Identification, ReID）在真实监控场景中常面临低光照与语义缺失的双重挑战，现有基准多局限于理想光照下的静态图像匹配，难以评估模型在视觉退化环境下的鲁棒性。本文切入点在于构建一个融合低光照视频、密集属性标注与语言描述的多模态测试床，以量化现有方法在极端域偏移下的性能崩塌。通过采集12路同步摄像头的夜间监控数据并引入大语言模型（Large Language Model, LLM）生成语义标签，VAST-ReID为低光照ReID提供了标准化评估协议。该基准揭示了主流模型在低光场景下的泛化失效，但其语义标注未参与训练，限制了其对多模态融合机制的直接验证。

## 研究背景

当监控摄像头在夜间或阴影区域运行时，图像信噪比急剧下降，导致传统基于纹理与颜色的特征提取器失效。这种视觉退化构成了低光照ReID的核心困境，而解决该问题通常需要结合时序动态信息以补偿单帧特征的缺失。然而，现有数据集如Market-1501仅包含日间静态图像，缺乏对光照变化的建模；视频数据集如MARS虽有时序信息，但缺乏语义标注与低光照场景，无法支撑多模态检索任务。

ReID领域的主流路线已从静态图像匹配转向视频时序建模与视觉-语言模型（Vision-Language Model, VLM）对齐，但这两条路线在低光照场景下的有效性尚未被系统评估。现有夜间数据集如NightReID虽聚焦低光，但仅提供单模态RGB图像，缺乏属性与语言维度的语义丰富性，导致模型无法利用高层语义线索进行身份判别。VAST-ReID的切入点在于填补这一空白，通过整合低光照视频、25类属性标注及LLM生成的自然语言描述，构建了一个能够同时评估视觉鲁棒性、语义理解与时序一致性的综合基准。

## 核心方法

### 数据构建与多模态标注体系

VAST-ReID的数据构建遵循“视觉采集-自动追踪-语义增强”的流水线，其核心差异在于将VLM从特征提取工具转化为数据标注工具。采集阶段使用12路同步摄像头覆盖24个室内外场景，确保跨视角与跨光照的多样性。标注阶段采用YOLOv9自动检测结合人工修正的混合策略，生成412,500+个边界框。语义增强层引入25个属性类别与181个子属性，并针对每个视频生成4条自然语言描述（1条人工，3条由Gemini、ChatGPT、DeepSeek生成）。这一设计解决了现有数据集仅含身份标签、缺乏细粒度语义信息的问题，使得模型能够利用属性与语言线索进行条件检索。

$$
\mathcal{D} = \{ (I_t, y, \mathcal{A}, \mathcal{L}) \}_{t=1}^{T}
$$

其中 $I_t$ 为第 $t$ 帧图像，$y$ 为身份ID，$\mathcal{A}$ 为属性向量，$\mathcal{L}$ 为语言描述集合。该公式定义了VAST-ReID的多模态样本结构，强调视觉、属性与语言的联合表示。

### 评估协议与迁移学习框架

评估协议采用标准ReID划分（Train/Query/Gallery），并引入三种迁移学习设置以量化域偏移影响：Inference（Market→VAST）、Fine-tuned（Market→VAST）与Trained from Scratch（VAST→VAST）。该设计动机在于区分模型在源域预训练下的泛化能力与在目标域微调后的适应性。Inference设置直接测试预训练模型在低光下的鲁棒性，Fine-tuned设置评估微调对域偏移的缓解效果，Trained from Scratch设置则验证模型在低光数据上的内在学习能力。这种分层评估框架比单一测试协议更能揭示模型在不同训练条件下的性能边界。

$$
\text{mAP} = \frac{1}{|Q|} \sum_{q \in Q} \text{AP}(q)
$$

其中 $Q$ 为查询集，$\text{AP}(q)$ 为单个查询的平均精度。该公式用于衡量模型在低光照场景下的检索性能，mAP综合了Rank-1至Rank-10的累积精度，对低光下的特征退化更为敏感。

## 实验评估

实验在VAST-ReID数据集上进行，基线覆盖CLIP-ReID、TransReID、PAT、SOLIDER、UFFM与TF-CLIP，但缺失ICRE、BIT等最新跨模态SOTA方法，限制了与当前最优方法的直接对比。主实验结果显示，在Inference设置下，TransReID的Rank-1仅为10.0%，mAP为8.3%，表明Transformer架构在极端域偏移下的脆弱性；而CLIP-ReID达到75.0% Rank-1与53.5% mAP，显示VLM预训练特征的相对鲁棒性。

| 方法 | Inference R-1 | Inference mAP | Fine-tuned R-1 | Fine-tuned mAP | Scratch R-1 | Scratch mAP |
|---|---|---|---|---|---|---|
| CLIP-ReID | 75.0 | 53.5 | 91.3 | 78.1 | 90.0 | 79.4 |
| TransReID | 10.0 | 8.3 | 10.3 | 8.3 | 46.3 | 39.4 |
| PAT | 63.7 | 46.1 | 85.0 | 71.7 | 87.5 | 69.0 |
| SOL.S-TINY | 6.2 | 4.4 | 83.7 | 70.5 | 40.0 | 37.3 |
| TF-CLIP | 78.95 | 65.15 | - | - | - | - |

Fine-tuned设置下，CLIP-ReID以91.3% Rank-1领先，较Inference提升16.3个百分点，表明微调对低光域偏移的显著缓解作用。TransReID在微调后仅提升至10.3% Rank-1，几乎无改善，暗示其架构缺乏适应低光退化的内在机制。反向迁移实验（VAST→Market）中，PAT达到67.6% Rank-1，而CLIP-ReID骤降至12.4%，揭示VLM特征对源域预训练的强依赖，低光训练反而损害了其在日间场景的泛化能力。

评估边界方面，论文未报告计算效率指标（FLOPs、Latency），且语义标注未参与训练，仅用于评估，这限制了其对多模态融合机制的验证深度。代码已开源，但超参数配置未完全披露，可复现性依赖社区复现。

## 关联研究分析

从问题动机看，VAST-ReID与NightReID均聚焦低光照场景，但NightReID仅提供静态RGB图像，缺乏时序与语义维度，而VAST-ReID通过视频轨迹与属性标注构建了更丰富的测试空间。这一差异源于任务定义的不同：NightReID旨在评估低光下的视觉特征鲁棒性，而VAST-ReID旨在评估多模态语义在低光下的联合鲁棒性。VAST-ReID的语义标注未参与训练，导致其无法验证属性或语言线索对低光ReID的实际增益，这与CLIP-ReID等VLM方法将语言作为特征骨干的设计形成对比。

从方法设计看，VAST-ReID的评估协议与Market-1501标准兼容，但引入了低光照这一关键变量，使得现有SOTA如ICRE、BIT等跨模态方法无法直接迁移。ICRE在SYSU-MM01上达到79.13% Rank-1，但其依赖可见光-红外模态对齐，而VAST-ReID仅包含RGB低光数据，缺乏红外模态，导致ICRE等VI-ReID方法无法适用。这一限制暴露了当前ReID方法在单模态低光场景下的泛化盲区，即跨模态对齐策略在缺乏辅助模态时是否仍有效，论文未给出回答。

## 总结

VAST-ReID要解决的核心矛盾是低光照环境下视觉特征退化与语义信息缺失的双重挑战。现有方法在日间静态图像上表现优异，但在低光视频场景中性能崩塌，而本文通过构建融合低光照视频、属性标注与语言描述的多模态基准，量化了这一崩塌程度。实验证明，CLIP-ReID在微调后达到91.3% Rank-1，而TransReID仅10.3%，揭示了架构对域偏移的敏感性差异。本文的边界在于语义标注未参与训练，且缺乏红外模态，限制了其对多模态融合与跨模态对齐机制的验证。当低光照场景引入红外辅助模态时，现有VLM特征是否仍能保持鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_daf50d52d3c2)