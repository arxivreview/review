# ACL-Findings2026最新论文 ｜microCLIP: Unsupervised CLIP Adaptation via Coarse-Fine Token Fusion for Fine-Grained Image Classification ｜microCLIP：无监督CLIP适应中的粗-细粒度Token融合

研究机构：阿联酋扎耶德大学、印度理工学院德里分校

作者：Sathira Silva、Eman Ali、Chetan Arora 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02270)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02270)

> 无监督适应（Unsupervised Adaptation, UA）旨在利用未标注数据提升CLIP在细粒度分类上的表现，但现有方法依赖全局[CLS] token，无法捕捉区分近邻类别所需的局部空间细节。本文指出，仅靠文本侧的细粒度描述无法弥补视觉侧的空间缺失，必须从图像patch token中提取局部线索。microCLIP通过显著性导向注意力池化（Saliency-Oriented Attention Pooling, SOAP）构建细粒度[FG] token，并与[CLS] token对称融合，结合动态知识聚合实现自训练。该方法在13个细粒度数据集上平均提升2.90%，验证了视觉局部线索的必要性，但其性能上限受限于ViT-B/32骨干的patch分辨率。

## 研究背景

细粒度图像分类要求模型区分如“Common Gallinule”与“Purple Gallinule”这类仅凭细微局部特征（如颈部颜色、羽毛纹理）才能区分的类别。CLIP通过对比学习对齐全局图像表示与文本嵌入，其[CLS] token捕获高层语义，但缺乏像素级空间精度。在无标签场景下，模型需生成伪标签进行自训练，此时[CLS] token的粗粒度特性导致其无法与LLM生成的细粒度文本描述有效对齐，造成伪标签噪声。

现有UA方法如DPA通过缓存图像原型构建视觉先验，LaFTer利用LLM描述微调视觉提示，但均局限于[CLS] token的全局表示。WCA虽引入多视图对齐，但计算开销巨大且未解决视觉侧的空间缺失。本文切入点在于：[CLS] token保留了预训练的全局知识，不应丢弃，而应作为强先验，与从patch token中提取的局部细粒度线索协同工作，以解决无监督细粒度分类中视觉-文本对齐的空间精度瓶颈。

## 核心方法

### 方法参照系

标准UA流程通常冻结CLIP编码器，仅微调分类器或提示，依赖[CLS] token生成伪标签。本文的关键差异在于：不依赖单一全局token，而是引入局部[FG] token，并通过自训练框架联合优化视觉与文本表示，实现粗-细粒度协同。

### SOAP与TokenFusion模块

此前方法忽略patch token，仅使用[CLS] token，导致细粒度特征丢失。本文在CLIP视觉编码器中，通过绕过注意力机制保留空间信息，利用归一化割（Normalized Cut, NCut）算法筛选显著性patch token，构建显著性查询向量$q_{sal}$，进而通过单头注意力池化生成[FG] token。该设计解决了[CLS] token缺乏空间定位能力的问题，使模型能聚焦于语义关键区域。

$$
v_{[FG]} = f_{\text{AttnPool}}(q_{sal}, v_{patch}) = \text{softmax}\left(\frac{q_{sal} W_Q (v_{patch} W_K)^T}{\sqrt{d}}\right) (v_{patch} W_V)
$$

其中，$q_{sal}$为NCut筛选后的显著性token均值，$v_{patch}$为保留空间信息的patch token序列。[FG] token与[CLS] token通过CLIP投影矩阵$P_{CLIP}$映射至共享嵌入空间，分别计算局部与全局logits，最终通过平均融合：

$$
\text{logits}_{fused} = \frac{1}{2} \left( s(P_{CLIP}(v_{[FG]}), W_{LLM}^*) + s(P_{CLIP}(v_{[CLS]}), W_{LLM}^*) \right)
$$

该对称融合确保全局与局部特征在自训练中接受同等监督，避免单一模态主导。

### 动态知识聚合

此前伪标签生成依赖固定先验或单一动态logits，导致稳定性或适应性不足。本文提出动态知识聚合，凸组合固定LLM/CLIP先验（通过多视图对齐生成）与TokenFusion的动态logits。该机制解决了自训练中伪标签噪声累积问题，通过平衡静态先验与动态学习，实现稳定且自适应的伪标签迭代。

$$
\text{pseudo-label} = \gamma \cdot \text{logits}_{multi-view} + (1-\gamma) \cdot \text{logits}_{TokenFusion}
$$

其中，$\gamma$为权重系数，实验表明$\gamma=0.5$时性能最优，表明静态与动态知识同等重要。

## 实验评估

实验在13个细粒度数据集上进行，使用ViT-B/32骨干，对比CLIP、DPA、ReCLIP等8种基线。microCLIP在整体准确率上达到68.68%，较最强基线DPA提升2.90%。在Cars数据集上提升8.98%，在FGVC上提升2.64%，表明局部线索对细粒度区分至关重要。

| 方法 | Birdsnap | Cars | DTD | FGVC | Flowers | Pets | UCF101 | Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DPA | 31.54 | 57.44 | 58.84 | 20.10 | 78.64 | 93.35 | 74.44 | 65.78 |
| microCLIP | 38.59 | 65.81 | 60.00 | 22.74 | 75.84 | 90.24 | 70.98 | 68.68 |

消融实验显示，移除SOAP导致平均准确率下降1.97%，替换为朴素token平均下降1.71%，表明显著性引导的注意力池化是关键。移除动态知识聚合（$\gamma=0$）导致性能降至58.03%，证明静态先验的必要性。

评估边界方面，实验仅使用ViT-B/32骨干，未与ViT-B/16下的SOTA方法（如TuneCLIP）直接对比，限制了绝对性能评估。代码已开源，但NCut参数与$\gamma$值需针对数据集调整，可复现性依赖超参数敏感性分析。

## 关联研究分析

从问题动机看，本文与WCA同属多视图对齐路线，但WCA依赖大量随机裁剪（$N \approx 60$）作为视觉提示，计算开销大；本文将其重构为弱增强，仅用8个裁剪，通过动态知识聚合平衡效率与精度。这一差异源于任务特性：UA场景下计算资源受限，而WCA面向训练-free场景，可容忍更高开销。

从方法设计看，本文与MaskCLIP同属细粒度对齐增强路线，但MaskCLIP依赖有监督区域标注，本文采用无监督NCut提取显著性区域。这一差异暗示无监督显著性提取在缺乏标注时可能引入噪声，但本文通过动态知识聚合缓解了这一问题。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文解决的核心矛盾是CLIP全局[CLS] token缺乏空间细节，导致无监督细粒度分类失效。现有方法仅依赖文本侧细粒度描述或全局视觉先验，无法弥补视觉侧的空间缺失。本文通过SOAP构建[FG] token，与[CLS] token对称融合，结合动态知识聚合实现自训练，在13个数据集上平均提升2.90%。其边界在于：ViT-B/32的粗粒度patch限制了[FG] token的细粒度潜力，且NCut显著性提取在无监督下可能引入噪声。当支持集增大到5-shot时，局部[FG] token的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02270)