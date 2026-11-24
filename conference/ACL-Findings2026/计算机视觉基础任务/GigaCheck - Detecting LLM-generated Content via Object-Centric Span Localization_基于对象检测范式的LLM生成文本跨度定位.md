# ACL-Findings2026最新论文 ｜GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization ｜基于对象检测范式的LLM生成文本跨度定位

作者：Irina Tolstykh、Aleksandra Tsybina、Sergey Yakubson 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.23728)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5474e7dbf1d3)

> 人机协作文本中AI片段的精确边界识别是现有文档级检测器无法解决的痛点，传统序列标注方法依赖繁琐的后处理且对句子结构敏感。GigaCheck将文本跨度检测重构为一维目标检测问题，利用DETR架构直接回归字符区间，消除了对句子边界的依赖。该方法通过共享LoRA微调骨干同时支持细粒度定位与文档级分类，在三个定位基准上显著优于基线，但其对多语言及极端长文本的适用性仍存疑。

## 研究背景

当检测器面对人机混合文本时，传统二元分类只能输出整体标签，无法区分“纯AI生成”与“AI润色”，这一局限源于文档级特征聚合丢失了局部作者身份变化的信息。为捕捉这种变化，早期研究转向Token级序列标注，但该方法需依赖CRF或启发式规则将离散Token分组为连续跨度，且性能高度依赖句子边界划分，在缺乏明确结构的自由文本中失效。

AI生成文本检测领域长期聚焦于文档级二元分类，主流路线包括基于统计特征（如困惑度）的零样本方法与基于预训练编码器的监督学习。前者模型无关但鲁棒性弱，后者分布内精度高但跨域泛化差。随着生成模型能力提升，简单统计特征失效，研究重心转向语义表征与对抗鲁棒性。然而，针对人机协作场景的细粒度定位研究仍处早期，现有方法如TriBERT依赖距离度量，Sci-SpanDet依赖IMRaD结构，均缺乏通用性。GigaCheck的切入点在于引入视觉目标检测范式，将AI片段视为离散“对象”，实现结构无关的端到端跨度预测。

## 核心方法

### 统一文本表征骨干

本文采用LoRA微调Mistral-7B作为统一骨干，替代传统RoBERTa编码器。设计动机在于LLM的深层语义表征比浅层编码器更能捕捉生成文本的细微统计异常，且LoRA参数高效微调在小数据集上泛化性优于全量微调。骨干输出Token嵌入 $E$，经线性投影与Transformer编码器得到上下文特征 $R$，该特征同时馈送至检测头与分类头，验证了表征在细粒度定位与全局分类任务间的可迁移性。

### 对象中心跨度定位（DN-DAB-DETR）

传统序列标注需后处理分组Token，本文将其替换为DETR风格的直接回归。设计动机在于消除对句子边界的依赖，实现字符级精确定位。采用DN-DAB-DETR架构，初始化 $N$ 个锚点查询 $q$，通过交叉注意力迭代优化中心 $c$ 与宽度 $w$。损失函数为匈牙利匹配后的L1、gIoU与Focal损失加权和：

$$
\mathcal{L} = \sum_{i \in \mathcal{M}} (\mathcal{L}_{L1}^{(i)} + \mathcal{L}_{gIoU}^{(i)} + \mathcal{L}_{Focal}^{(i)}) + \lambda \sum_{j \in \mathcal{N}} (\mathcal{L}_{L1}^{(j)} + \mathcal{L}_{gIoU}^{(j)})
$$

其中 $\mathcal{M}$ 为匹配预测，$\mathcal{N}$ 为去噪GT查询。该设计直接输出连续字符区间，无需投影至句子边界，在RoFT-ChatGPT上将MSE从3.06降至1.03，验证了端到端回归的精度优势。

### 文档级分类头

在骨干的<EOS>隐藏状态上附加两层MLP，以二元交叉熵训练。设计动机在于验证共享骨干的通用性，证明同一表征既能支持细粒度定位也能支持全局分类。该头与检测头独立训练，但共享LoRA权重，确保表征学习的一致性。

## 实验评估

实验在RoFT、RoFT-ChatGPT、TriBERT三个定位基准及TuringBench、TweepFake、MAGE三个分类基准上进行。基线覆盖RoBERTa、TDA、Perplexity等路线，但缺失SENTRA、DivEye等最新SOTA的直接对比。

| 方法 | RoFT Acc | RoFT-ChatGPT Acc | RoFT-ChatGPT MSE |
| :--- | :--- | :--- | :--- |
| RoBERTa + SEP | 0.50 | 0.55 | 3.06 |
| GigaCheck (DN-DAB-DETR) | 0.65 | 0.68 | 1.03 |

GigaCheck在RoFT-ChatGPT上Acc提升13%，MSE降低约3倍，显著优于RoBERTa基线。在TriBERT上，2-3边界文本的F1@3达0.801，高于TriBERT模型的0.622，且随边界数增加性能稳定，而基线性能下降。

| 方法 | MAGE AvgRec | MAGE AUROC |
| :--- | :--- | :--- |
| GigaCheck (Mistral-7B) | 0.9611 | 0.9923 |
| GigaCheck (Mistral-12B) | 0.9630 | 0.9941 |
| GigaCheck (Qwen-72B) | 0.8338 | 0.9697 |

骨干规模消融显示，7B至12B性能微升，但72B Qwen出现显著过拟合（AvgRec降至0.8338），表明小数据集上过大骨干反而损害泛化性。

评估边界方面，论文仅测试英语文本，未验证多语言场景；MAGE上0.99 AUROC可能受数据规模影响，未报告置信区间；代码已开源，但超参数细节需查阅附录。

## 关联研究分析

从问题动机看，GigaCheck与Sci-SpanDet均针对细粒度定位，但后者依赖IMRaD结构，仅适用于科学论文；GigaCheck采用结构无关的DETR范式，可处理任意文本。这一差异源于任务特性：科学文档有固定章节结构，而通用文本缺乏显式组织，迫使方法必须放弃结构先验，转向纯数据驱动的区间回归。

从方法设计看，GigaCheck与TriBERT均解决人机边界检测，但TriBERT使用距离度量识别转换点，GigaCheck直接回归跨度。TriBERT在1边界文本上表现较好（F1@3 0.455 vs 0.444），但在2-3边界文本上性能骤降，而GigaCheck保持稳定。这暗示距离度量对多边界场景的敏感性高于直接回归，但论文未深入分析这一差异的根源，也未探讨DETR锚点机制在变长文本中的计算冗余问题。

## 总结

GigaCheck解决的核心矛盾是细粒度定位对句子结构的依赖与通用文本结构缺失之间的冲突。其切入点在于引入视觉目标检测范式，将AI片段视为离散对象，通过DETR架构直接回归字符区间，消除了后处理与结构先验。实验证明该方法在RoFT-ChatGPT上MSE降至1.03，在TriBERT上2-3边界F1@3达0.801，显著优于基线。但论文仅测试英语文本，且72B骨干出现过拟合，暴露了小数据集上规模扩展的局限。当支持集增大到多语言场景时，DETR锚点机制的计算效率与泛化性是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_5474e7dbf1d3)