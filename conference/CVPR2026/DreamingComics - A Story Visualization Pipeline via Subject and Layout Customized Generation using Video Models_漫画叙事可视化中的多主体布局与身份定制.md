# CVPR2026最新论文 ｜DreamingComics: A Story Visualization Pipeline via Subject and Layout Customized Generation using Video Models ｜漫画叙事可视化中的多主体布局与身份定制

作者：Patrick Kwon、Chen Chen

论文原文见 [arXiv](https://arxiv.org/abs/2512.01686)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01686)

> 故事可视化旨在从文本叙事生成连贯的视觉序列，但现有方法难以同时实现多角色精确空间定位与艺术风格一致性。传统图像生成模型偏向写实渲染，且缺乏像素级空间控制能力，导致角色重叠或身份混淆。本文基于视频扩散Transformer构建框架，通过区域感知旋转位置编码与掩码条件损失实现布局控制。该方法在角色一致性上取得显著优势，但单帧细节清晰度是否因视频模型特性而受损仍存疑。

## 研究背景

故事可视化的核心挑战在于将离散的角色身份与连续的空间布局统一建模。文本提示仅提供粗粒度全局语义，无法指定角色在画面中的具体坐标，而传统图像生成模型（如Stable Diffusion）在缺乏显式空间条件时，往往依赖隐式注意力机制定位物体，导致多主体场景下出现位置错乱或属性泄漏。为解决此问题，研究者引入边界框作为空间条件，但现有方法多基于U-Net架构，通过ControlNet或适配器注入控制信号，难以适配新兴的Diffusion Transformer (DiT) 全局注意力结构。

主流路线存在明显瓶颈：基于U-Net的方法（如StoryDiffusion）计算开销大且风格泛化性差；基于DiT的定制方法（如DreamO、UNO）虽能保持身份，但缺乏显式空间接地，角色位置由隐式学习决定，无法精确遵循指定布局。此外，图像生成模型普遍存在向写实渲染偏移的倾向，难以保持漫画、卡通等非写实艺术风格。DreamingComics 的切入点在于利用视频生成模型的时空先验，将图像定制重构为“下一帧预测”任务，从而在保持风格一致性的同时，通过改造位置编码机制实现显式布局控制。

## 核心方法

### 方法参照系

本文问题属于布局条件生成与多主体身份保持的交叉领域。标准流程通常采用ControlNet或交叉注意力将边界框注入U-Net，或在DiT中通过区域掩码限制注意力。本文的关键差异在于：不引入额外控制分支，而是直接修改DiT的位置编码机制，并将视频模型的时序一致性先验用于单帧图像的风格保持。

### RegionalRoPE 空间接地机制

传统RoPE为所有参考帧分配相同的起始坐标，导致模型感知所有主体源自同一区域，引发空间纠缠。本文提出RegionalRoPE，将每个参考潜变量的RoPE索引映射至其目标布局边界框。对于参考潜变量 $c_i \in \mathbb{R}^{h_i \times w_i \times d}$ 及其目标区域 $\text{BOX}_i = [w_{start}, h_{start}, w_{end}, h_{end}]$，计算缩放因子 $s = \min(\frac{W_{box}}{w_i}, \frac{H_{box}}{h_i})$ 以维持长宽比，调整后的RoPE网格尺寸为 $(W', H') = (s w_i, s h_i)$。该机制通过显式坐标偏移，使模型在注意力计算中直接感知主体的空间位置，解决了隐式定位导致的角色重叠问题。

### 掩码条件损失与视频模型重构

仅靠RegionalRoPE仍可能导致身份失真。本文引入掩码条件损失，监督每个主体的交叉注意力图（CAM）尊重布局边界。定义二值空间掩码 $\text{MASK}_i$，其中布局内像素为1，外部为0。针对DiT第2层的CAM，损失函数定义为：

$$ \mathcal{L}_{mask} = \frac{1}{n_c} \sum_{i=1}^{n_c} \text{ReLU}(\text{CAM}_{c_i, \text{block}_2} - \text{MASK}_i) $$

该公式仅惩罚超出布局区域的注意力泄漏，避免抑制有效区域聚焦。同时，本文利用FramePack将视频生成重构为单帧定制：给定 $t=0$ 的参考图像，生成 $t=t'$ 的目标帧。通过选择 $t'=3$，在身份保持与风格变化间取得平衡，利用视频模型的时序先验增强跨帧风格一致性，避免图像模型向写实风格偏移。

## 实验评估

实验在ViStoryBench和DreamBench上进行，基线涵盖StoryDiffusion、DreamO、UNO等主流方法，但缺乏ControlNet类U-Net基线的直接对比。

| 方法 | 基础模型 | CIDS (Cross) ↑ | CSD (Cross) ↑ | OCCM ↑ | Layout Precision ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DreamO | FLUX | 51.6 | 38.3 | 85.7 | - |
| UNO | FLUX | 46.2 | 39.3 | 83.8 | - |
| Eligen | FLUX | 35.9 | 29.7 | 78.5 | 39.7 |
| **Ours** | FramePack | **66.6** | **53.6** | **86.7** | **61.6** |

DreamingComics 在CIDS-cross上达到66.6，较DreamO提升29.2%，在CSD-cross上达到53.6，显著优于其他方法，验证了视频模型在风格保持上的优势。Layout Precision达到61.6，表明布局控制有效。

消融实验显示，移除RegionalRoPE导致CIDS-cross从58.5降至38.7，降幅最大，证明空间接地是性能核心。移除掩码条件损失后，CIDS-cross降至56.6，CSD-cross降至50.5，表明该损失对细节保真有边际贡献。时间步 $t=3$ 取得最佳平衡，$t=1$ 结果僵硬，$t=9$ 出现风格漂移。

评估边界方面，ViStoryBench侧重故事一致性，缺乏通用布局基准（如COCO-MIG）对比，难以判断方法在复杂密集布局下的泛化性。代码与超参数已公开，但视频模型的高计算成本限制了实时应用。

## 关联研究分析

从方法设计看，DreamingComics 与Eligen均针对DiT架构，但Eligen采用刚性区域掩码限制注意力，而本文通过RegionalRoPE进行软性空间接地。Eligen的掩码可能导致细节丢失，而RoPE重索引保留了全局上下文，这源于任务特性：漫画生成需要角色与背景的交互，刚性掩码会破坏这种交互。从问题动机看，本文与TheaterGen均使用LLM生成布局，但TheaterGen针对单图像，本文针对多面板漫画结构。TheaterGen未解决面板间布局逻辑，而本文通过微调LLM理解漫画阅读顺序（从上到下，从右到左），这反映了漫画叙事特有的空间逻辑需求，而非通用布局生成的简单扩展。

## 总结

DreamingComics 解决了故事可视化中多主体空间定位与风格一致性的矛盾，利用视频DiT的时空先验与RegionalRoPE实现显式布局控制。实验证明其在角色一致性（CIDS 66.6）和风格相似度（CSD 53.6）上显著优于现有DiT定制方法。然而，方法依赖视频模型的高计算成本，且缺乏通用布局基准对比，单帧细节清晰度是否因视频模型特性而受损未得到充分验证。当支持集增大到多面板复杂场景时，RegionalRoPE的空间接地精度是否会因角色数量增加而下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01686)