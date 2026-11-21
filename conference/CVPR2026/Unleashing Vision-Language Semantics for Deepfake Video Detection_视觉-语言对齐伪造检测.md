# CVPR2026最新论文 ｜Unleashing Vision-Language Semantics for Deepfake Video Detection ｜视觉-语言对齐伪造检测

研究机构：新加坡管理大学、英国华威大学

作者：Jiawen Zhu、Yunqi Miao、Xueyi Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24454)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24454)

> 深度伪造视频检测面临跨数据集泛化瓶颈，传统方法依赖低层伪影或单一视觉编码器适配，难以捕捉高保真生成内容的细微身份不一致。现有VLM适配方案仅利用视觉特征，忽视了模型内在的视觉-语言对齐语义。VLAForge通过独立伪造感知器与身份先验文本提示，将VLM的全局语义对齐转化为细粒度patch级真实性判别。该方法在九个基准上刷新了视觉单模态检测SOTA，但其对音频模态的缺失限制了其在原生音视频伪造场景下的适用性。

## 研究背景

当检测器面对新生成模型时，其训练域与测试域的数据分布出现系统性差异——这一现象称为分布偏移。分布偏移导致传统分类器决策边界失效，而实际场景中往往能获取少量目标域样本，这恰好构成了小样本学习的条件：仅凭每个类别极少量标注样本泛化到新任务。解决此类问题的经典框架是原型网络，它计算各类别支持样本的特征均值作为"原型"，再通过距离度量完成分类。

深度伪造视频检测的核心挑战在于跨生成器泛化能力不足。主流路线分为两类：一类基于空间或频域伪影检测，如Xception和FFD，但这类方法在跨数据集场景下性能急剧下降；另一类利用VLM（如CLIP）的大规模预训练语义，通过适配器微调视觉编码器，如ForAda和RepDFD。然而，现有VLM适配方法仅关注视觉模态，未充分利用VLM内在的视觉-语言对齐（VLA）语义。VLAForge的切入点在于：通过身份先验注入文本提示，将VLM的全局语义对齐转化为细粒度patch级真实性判别，从而增强跨数据集泛化能力。

## 核心方法

### 方法参照系

VLM适配检测的标准流程是：使用CLIP骨干提取视觉特征，通过适配器微调视觉编码器以增强伪造伪影的判别性。本文问题与该通用流程的关键差异在于：不仅微调视觉编码器，还引入独立伪造感知器与身份先验文本提示，将VLM的视觉-语言对齐语义转化为细粒度patch级真实性判别。

### ForgePerceiver：独立伪造感知器

ForgePerceiver作为独立学习器，捕获多样且细微的伪造线索，同时保留VLM预训练知识。其设计动机在于：VLM的视觉编码器主要训练于理解语义对象，对低层伪造伪影不敏感，导致注意力分散到与伪造无关的区域。ForgePerceiver通过可学习查询令牌与视觉令牌交互，生成两类伪造先验：伪造感知掩码（用于全局真实性学习）和伪造定位图（用于局部区域线索）。

伪造感知掩码的计算公式为：

$$M_i = \text{softmax}\left(\frac{Q_i \cdot V_i^\top}{\sqrt{d_v}}\right)$$

其中 $Q_i$ 和 $V_i$ 分别为第 $i$ 个注意力头的查询和视觉特征投影。该公式通过测量查询令牌与头特定视觉特征的相似度，生成头特定的伪造感知掩码，确保不同查询捕获互补的伪影先验。

### Identity-Aware VLA Scoring：身份感知VLA评分

Identity-Aware VLA Scoring模块利用VLM内在的视觉-语言对齐，学习判别性patch级真实性线索。其设计动机在于：仅依赖低层视觉线索限制了VLM检测器利用内在跨模态语义的能力，而身份先验注入文本提示可增强文本-视觉对齐的细粒度性。该模块首先通过身份先验增强文本提示，生成ID感知文本嵌入，然后与patch令牌嵌入对齐生成VLA注意力图。

VLA注意力图的计算公式为：

$$M_{VLA}(i,j) = \frac{F_r^\top \phi(P_{i,j})}{\|F_r\| \|\phi(P_{i,j})\|} - \frac{F_f^\top \phi(P_{i,j})}{\|F_f\| \|\phi(P_{i,j})\|}$$

其中 $F_r$ 和 $F_f$ 分别为真实和伪造类的ID感知文本特征，$\phi(\cdot)$ 为可学习适配器，$P_{i,j}$ 为位置 $(i,j)$ 的patch令牌嵌入。该公式通过计算真实与伪造类文本特征与patch嵌入的余弦相似度差，生成细粒度VLA注意力图，突出伪造区域。

## 实验评估

实验在FF++、CDF-v1/v2、DFDC、DFD等九个基准上进行，采用跨数据集评估协议，训练集为FF++ c23压缩版本。基线覆盖Xception、ForAda、RepDFD等16种SOTA方法，但缺失多模态音视频基线（如MDS）。

| 数据集 | 方法 | Frame AUROC | Video AUROC |
|---|---|---|---|
| CDF-v2 | VLAForge | 93.9 | 96.8 |
| DFDC | VLAForge | 97.2 | 89.6 |
| DFD | VLAForge | 93.6 | 97.2 |
| VQGAN | VLAForge | 98.4 | 99.7 |
| SiT | VLAForge | 77.4 | 85.9 |

VLAForge在DFDC上Frame AUROC达97.2%，较ForAda（96.5%）提升0.7%；在VQGAN上Frame AUROC达98.4%，较RepDFD（80.5%）提升17.9%。消融实验显示，ForgePerceiver（T1）贡献最大，在CDF-v2上Frame AUROC从58.3%提升至64.0%；Identity-Aware VLA Scoring（T4）进一步将CDF-v2 Frame AUROC提升至91.2%。

评估边界：指标仅报告AUROC，未提供置信区间；评估协议未包含社交媒体压缩退化场景；代码已开源，但超参数与GPU配置未在正文中详细列出。

## 关联研究分析

从问题动机看，VLAForge与ForAda同属VLM适配检测路线，但ForAda仅微调视觉编码器，而VLAForge引入独立伪造感知器与身份先验文本提示。这一差异的根源在于：ForAda假设视觉编码器微调足以捕获伪造伪影，而VLAForge认为VLM内在的视觉-语言对齐语义可提供互补的细粒度真实性线索。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，VLAForge与RepDFD均利用文本提示，但RepDFD仅实现全局余弦相似度对齐，而VLAForge实现patch级VLA对齐。这一差异的根源在于：RepDFD假设全局对齐足以捕获伪造线索，而VLAForge认为patch级对齐可突出伪造区域的细粒度不一致。身份先验是否导致对特定身份过拟合，论文未给出回答。

## 总结

VLAForge要解决的核心矛盾是VLM适配检测中视觉-语言对齐语义的未充分利用。现有方法仅微调视觉编码器，忽视了VLM内在的跨模态语义；VLAForge通过独立伪造感知器与身份先验文本提示，将全局语义对齐转化为细粒度patch级真实性判别。该方法在DFDC上Frame AUROC达97.2%，在VQGAN上Frame AUROC达98.4%，显著优于ForAda和RepDFD。本文的边界在于仅处理视觉模态，未验证音频驱动伪造场景下的性能。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24454)