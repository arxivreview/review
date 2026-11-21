# WACV2026最新论文 ｜DOTGraph: CLIP-Driven Feature Disentanglement and Optimal Transport based Graph Learning for Few-Shot Segmentation ｜DOTGraph：基于CLIP特征解耦与最优传输图学习的少样本分割

研究机构：美国石溪大学

作者：Shreya Biswas、Zhaozheng Yin

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_edf28474b5c6)

> 少样本语义分割（Few-Shot Segmentation, FSS）旨在利用极少量标注样本泛化至新类别，其核心难点在于支持集与查询集间的分布差异导致特征对齐失效。现有方法依赖像素级余弦相似度或静态文本嵌入，难以克服背景偏差与姿态尺度差异，导致细粒度结构丢失。本文提出DOTGraph，通过CLIP提示特征解耦背景，并利用最优传输（Optimal Transport, OT）在图结构上实现全局分布对齐。该方法在PASCAL-5i和COCO-20i上取得SOTA，但优势微弱且计算开销未充分评估，其泛化边界仍存疑。

## 研究背景

FSS通常采用元学习范式，模型在基础类上训练，测试时仅凭少量支持样本（Support Set）分割查询图像（Query Image）。这一过程要求模型从支持集提取判别性特征，并建立其与查询图像的空间对应关系。然而，支持集样本极少，且往往与查询图像在姿态、尺度或背景上存在显著差异，导致基于简单相似度匹配的特征对齐不可靠。

传统FSS方法如PFENet和HDMNet依赖像素级余弦相似度或低维先验来引导解码器，这种局部匹配策略在支持集与查询集存在显著姿态或尺度偏差时失效，无法捕获全局物体结构。同时，模型易受支持集背景干扰，产生背景偏差（Background Bias），即模型依赖背景上下文而非物体本身进行预测。近期引入CLIP等视觉语言模型的方法虽提供了语义先验，但多采用静态融合，未能动态解决支持-查询间的分布对齐问题。DOTGraph的切入点在于将特征对齐从局部像素匹配升级为全局分布传输，并显式解耦背景特征，以同时应对上述两类偏差。

## 核心方法

### 特征提取与解耦参照系

标准FSS流程使用预训练编码器提取支持集与查询集特征，并通过像素级相似度生成查询物体特征。本文的关键差异在于引入CLIP文本编码器，利用类别标签生成前景与背景提示（Prompt），通过Softmax-GradCAM提取语义特征，并与图像特征相加，实现背景与物体特征的初步解耦。

### CLIP驱动的特征解耦

设计动机在于消除支持集背景对查询物体特征的干扰。传统方法直接利用支持集全图特征，导致背景信息混入物体表示。本文利用CLIP文本编码器生成两个提示：$P_{obj}$（“This is an image of <class label>”）和$P_{bg}$（“This is an image without <class label>”）。通过Softmax-GradCAM，分别提取支持物体特征$C_{obj}^S$、支持背景特征$C_{bg}^S$及查询物体特征$C_{obj}^Q$。最终支持物体总特征为$T_{obj}^S = F_{obj}^S + C_{obj}^S$，支持背景总特征为$T_{bg}^S = C_{bg}^S$。这一解耦机制确保后续对齐过程仅基于物体语义，从源头抑制背景偏差。

### 基于最优传输的图特征细化

设计动机在于克服姿态尺度差异导致的全局对齐失效。解耦后的特征仍缺乏细粒度空间对应。本文将支持物体、支持背景及查询物体特征重塑为图结构，节点为空间位置特征向量。构建成本矩阵$C_{obj}$和$C_{bg}$，分别计算查询物体与支持物体、支持背景间的欧氏距离。求解熵正则化OT问题：

$$
\Pi^* = \arg \min_{\Pi \ge 0} \langle \Pi, C \rangle - \epsilon H(\Pi) \quad \text{s.t.} \quad \Pi \mathbf{1} = \mu, \Pi^\top \mathbf{1} = \nu
$$

其中$\mu, \nu$为均匀分布，$\epsilon$为正则系数。通过Sinkhorn-Knopp算法得到传输计划$T_{obj}$和$T_{bg}$（取负值以分离背景）。最终消息$M = T_{obj} + T_{bg}$结合支持-查询注意力机制，更新图节点特征。OT实现了全局分布匹配，而非局部像素匹配，从而在姿态变化下保持物体结构完整性。

## 实验评估

实验在PASCAL-5i和COCO-20i上进行，采用1-shot和5-shot设定，指标为mIoU。基线覆盖PFENet、BAM、HDMNet及CLIP驱动的PI-CLIP+HDMNet，但缺失SAM-based方法（如PerSAM）的直接对比。

| 方法 | 骨干 | PASCAL-5i (1-shot) Mean | COCO-20i (1-shot) Mean |
| :--- | :--- | :--- | :--- |
| HDMNet | ResNet-50 | 69.4 | 50.0 |
| PI-CLIP + HDMNet | ResNet-50 | 76.8 | 56.8 |
| DOTGraph | ResNet-50 | 77.1 | 57.3 |

DOTGraph在PASCAL-5i 1-shot上以77.1%超越PI-CLIP+HDMNet的76.8%，在COCO-20i上以57.3%超越56.8%。优势微弱，表明OT带来的增益有限。

| 消融组件 | PASCAL-5i mIoU | COCO-20i mIoU |
| :--- | :--- | :--- |
| 仅FD | 73.5 | 53.8 |
| 仅FR | 74.7 | 55.1 |
| FD + FR | 77.9 | 57.3 |
| 仅SQA | 72.3 | 54.2 |
| 仅OT | 75.2 | 55.7 |
| SQA + OT | 77.9 | 57.3 |

消融显示，特征解耦（FD）与特征细化（FR）缺一不可，单独使用均显著低于组合效果。在FR内部，OT与SQA（Support-Query Attention）协同作用，单独使用OT比SQA提升约2.9%（PASCAL-5i），表明全局对齐对细粒度分割至关重要。

评估边界方面，论文未报告计算效率指标，OT的二次复杂度在高分辨率图像下的开销未知。代码已开源，使用ResNet-50和VGG-16骨干，训练50-100 epochs，超参数透明。

## 关联研究分析

从问题动机看，DOTGraph与PI-CLIP同属CLIP驱动FSS路线，但PI-CLIP采用静态文本嵌入作为插件，未解决支持-查询间的动态对齐问题。DOTGraph引入OT实现全局分布匹配，其根源在于静态融合无法适应姿态尺度变化，而OT通过传输计划显式建模分布差异。这一改进是否在所有场景下优于静态融合，论文未提供大规模跨域实验验证。

从方法设计看，DOTGraph与HDMNet均使用图结构，但HDMNet依赖像素级相关，DOTGraph使用OT传输。HDMNet的局部匹配在姿态一致时高效，但在姿态差异大时失效；DOTGraph的OT计算开销更高，但鲁棒性更强。这种取舍反映了FSS中精度与效率的权衡，OT是否违背了度量类方法“简单高效”的共识，需结合部署场景评估。

## 总结

DOTGraph旨在解决FSS中背景偏差与姿态尺度差异导致的特征对齐失效问题。其切入点在于利用CLIP解耦背景，并通过OT实现全局分布对齐，克服了传统像素级匹配的局限。实验表明，该方法在PASCAL-5i 1-shot上达到77.1% mIoU，较PI-CLIP+HDMNet提升0.3%。然而，优势微弱且未评估计算开销，暴露了OT在高分辨率场景下的效率瓶颈。当支持集增大至5-shot时，OT的全局对齐增益是否被更多样本的局部匹配所抵消，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_edf28474b5c6)