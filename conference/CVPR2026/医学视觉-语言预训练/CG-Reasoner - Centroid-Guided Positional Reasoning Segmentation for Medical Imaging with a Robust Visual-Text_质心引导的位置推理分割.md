# CVPR2026最新论文 ｜CG-Reasoner: Centroid-Guided Positional Reasoning Segmentation for Medical Imaging with a Robust Visual-Text Consistency Metric ｜质心引导的位置推理分割

作者：Lakshmikar Reddy Polamreddy、Ming Ma

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_974a9d7ade2a)

> 医学影像分割模型长期面临“像素准确但语义空洞”的困境，即能画出病灶边界却无法用人类可理解的语言描述其空间位置，导致自动化报告生成缺乏临床可信度。现有方法将分割与语言推理视为独立任务，缺乏几何一致性约束，导致推理文本与掩码位置脱节。本文通过引入Text2Centroid模块将文本映射为空间坐标，并设计PRScore指标联合评估语义与空间对齐，实现了分割与位置推理的统一。该框架在六类模态上取得了领先的分割精度与推理一致性，但其依赖2D质心假设，对复杂非凸病灶的适应性存疑。

## 研究背景

当分割网络输出高精度掩码时，临床医生仍需人工解读病灶相对于解剖结构的位置关系，这一过程无法被纯像素级指标量化。位置推理（Positional Reasoning）要求模型不仅预测边界，还需生成如“左上角”或“邻近主动脉”的空间描述，这构成了视觉接地（Visual Grounding）在医学领域的具体化。然而，语言模型生成的空间描述往往缺乏几何约束，导致文本与视觉定位出现系统性偏差，这种偏差在现有基于BLEU或ROUGE的评估中无法被捕捉，因为传统指标仅关注词汇重叠，忽略空间几何正确性。

医学影像分割与语言推理的联合建模是当前的研究热点，但主流路线存在明显割裂。LISA与PixelLM等方法侧重于通用场景或token-pixel对齐，缺乏对医学解剖术语的专门适配；PRSMed虽然引入了医学QA数据，但其推理评估依赖ChatGPT的二元判断，缺乏对空间误差的细粒度惩罚。这些方法的共同瓶颈在于：语言模块与视觉模块之间缺乏显式的几何桥梁，导致模型可能生成语义正确但空间错误的描述（如将“左上”误述为“右下”而未被惩罚）。CG-Reasoner的切入点在于构建一个显式的几何约束机制，将文本推理转化为可计算的空间坐标，从而在训练和评估阶段同时强制语义与几何的一致性。

## 核心方法

### 方法参照系

本文问题属于“语言引导的交互式分割”范畴，标准流程通常由视觉编码器提取特征、语言模型生成提示、解码器融合两者生成掩码。关键差异在于，现有流程中语言提示仅作为语义条件输入，未参与空间几何的显式监督，导致推理文本与掩码质心缺乏直接关联。

### Text2Centroid空间接地模块

设计动机在于解决语言模型生成的空间描述缺乏几何约束的问题，此前方法中“top-left”与“bottom-right”在嵌入空间中可能距离很近，导致空间错误未被惩罚。本文引入Text2Centroid（T2C）模块，将描述性推理文本映射为归一化的2D空间坐标。该模块由冻结的Sentence-BERT编码器与多层回归头组成，训练时使用分割掩码的质心作为监督信号。其损失函数定义为：

$$
\mathcal{L}_{\text{T2C}} = \frac{1}{N}\sum_{i=1}^{N} \mathcal{S}_{\text{L1}}\left( (\hat{x}_{c,i}, \hat{y}_{c,i}), (x_{c,i}, y_{c,i}) \right)
$$

其中 $\mathcal{S}_{\text{L1}}$ 为Smooth L1损失，$(\hat{x}_{c,i}, \hat{y}_{c,i})$ 为预测坐标，$(x_{c,i}, y_{c,i})$ 为归一化至 $[-1, 1]$ 的掩码质心。训练完成后，T2C模块权重冻结，作为空间接地信号源，将文本嵌入转化为几何坐标，为后续的空间一致性评估提供基础。

### 空间接地损失与PRScore指标

设计动机在于现有评估指标无法区分“语义正确但空间错误”的输出，且训练过程中缺乏对语言模块空间能力的直接监督。本文提出空间接地损失 $\mathcal{L}_{\text{spatial}}$，通过T2C模块计算预测文本与参考文本的空间向量相似度，反向传播至LoRA适配器，强制LLM学习几何接地的表示。同时，提出PRScore指标，联合评估语义保真度、空间推理与视觉接地。PRScore计算公式为：

$$
\text{PRScore} = \alpha S_{\text{sem}} + \beta S_{\text{spatial}} + \gamma S_{\text{vis}}
$$

其中 $S_{\text{sem}}$ 为SBERT语义相似度，$S_{\text{spatial}}$ 为预测文本与参考文本的空间坐标相似度，$S_{\text{vis}}$ 为预测文本与掩码质心的空间相似度，权重 $\alpha=\beta=\gamma=1/3$。该指标显式惩罚空间错误，例如当参考文本为“top-left”而预测为“bottom-right”时，$S_{\text{spatial}}$ 与 $S_{\text{vis}}$ 将显著降低，从而准确反映模型的空间推理能力。

## 实验评估

实验在六类医学影像模态（CT、MRI、X-ray、超声、内镜、RGB）上进行，基线包括LISA-7B/13B、PRS-Med、PixelLM及BiomedParse等代表性方法。CG-Reasoner在Lung X-ray数据集上取得0.977的mDice与0.958的mIoU，优于PRS-Med的0.969与0.942，以及BiomedParse的0.972与0.949。在Brain MRI上，CG-Reasoner的mDice为0.819，略高于PRS-Med的0.803，但低于BiomedParse的0.294（注：此处BiomedParse数值异常低，可能为数据录入错误或特定子集结果，需结合原文核实，但根据表格数据，CG-Reasoner在多数模态上保持领先）。

| 方法 | Lung X-ray mDice | Lung X-ray mIoU | Brain MRI mDice | Brain MRI mIoU |
| :--- | :--- | :--- | :--- | :--- |
| PRS-Med | 0.969 | 0.942 | 0.803 | 0.757 |
| BiomedParse | 0.972 | 0.949 | 0.294 | 0.245 |
| CG-Reasoner | 0.977 | 0.958 | 0.819 | 0.731 |

消融实验显示，引入Text2Centroid模块后，CG-Reasoner在Lung CT上的PRScore从0.832提升至0.847，在Brain MRI上从0.705提升至0.722。这表明T2C模块对空间推理一致性的提升具有显著贡献，尤其在复杂解剖结构区域。然而，在Polyp Endoscopy上，提升幅度仅为0.009（0.723至0.732），暗示T2C模块对边界清晰、形状规则的病灶增益有限，而对形状不规则或位置模糊的病灶适应性可能受限。

评估边界方面，PRScore指标虽解决了空间惩罚缺失问题，但其依赖T2C模块的预训练质量，若质心计算对非凸病灶存在偏差，可能引入系统性误差。可复现性方面，论文提供了GitHub代码，使用2块NVIDIA A100 80GB GPU训练20个epoch，LoRA秩为16，超参数设置明确，但缺乏跨数据集泛化验证，结论可能依赖于特定数据集的标注质量。

## 关联研究分析

从问题动机看，CG-Reasoner与PRSMed均聚焦医学影像的位置推理分割，但PRSMed依赖ChatGPT进行二元判断，缺乏对空间误差的细粒度量化，而CG-Reasoner通过T2C模块将空间推理转化为几何坐标，实现了可计算的空间一致性评估。这一差异源于任务特性的不同：PRSMed侧重语义正确性，而CG-Reasoner强调几何精确性，后者更符合临床对定位精度的要求。

从方法设计看，CG-Reasoner与PixelLM均借鉴了token-pixel对齐思想，但PixelLM采用密集的token-pixel对应，计算成本高且缺乏医学领域适配，而CG-Reasoner简化为质心回归，降低了计算复杂度，并通过LoRA适配器实现医学语言的高效适配。这一简化是否牺牲了对复杂病灶的细粒度定位能力，论文未给出回答，但其在Lung X-ray上的高mDice表明，对于边界清晰的病灶，质心假设是有效的。

## 总结

CG-Reasoner要解决的核心矛盾是医学影像分割中像素精度与空间语义一致性的脱节，现有方法缺乏显式的几何约束机制。本文通过引入Text2Centroid模块将文本映射为空间坐标，并设计PRScore指标联合评估语义与空间对齐，实现了分割与位置推理的统一。实验证明，该方法在Lung X-ray上取得0.977的mDice，PRScore在Lung CT上达到0.847，优于基线方法。然而，其依赖2D质心假设，对非凸或形状不规则病灶的适应性未经验证，且缺乏跨数据集泛化测试。当病灶形状高度不规则时，质心坐标是否仍能准确反映空间位置，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_974a9d7ade2a)