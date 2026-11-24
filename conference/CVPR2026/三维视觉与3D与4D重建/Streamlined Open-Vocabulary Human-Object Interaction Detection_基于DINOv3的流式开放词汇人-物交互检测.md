# CVPR2026最新论文 ｜Streamlined Open-Vocabulary Human-Object Interaction Detection ｜基于DINOv3的流式开放词汇人-物交互检测

研究机构：华南理工大学

作者：Chang Sun、Dongliang Liao、Changxing Ding

论文原文见 [arXiv](https://arxiv.org/abs/2603.27500)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27500)

> 开放词汇人-物交互（HOI）检测旨在从图像中识别训练集未见的交互三元组，核心难点在于视觉定位的细粒度与语义分类的泛化性难以兼得。现有方法或依赖双模型协作导致结构冗余，或受限于CLIP等视觉-语言模型（VLM）缺乏密集空间细节。SL-HOI利用DINOv3骨干的细粒度特征与文本对齐头的语义能力，通过冻结骨干并引入轻量级交互查询桥接表示间隙，实现单模型端到端检测。该架构在公平对比下刷新了基准SOTA，但其对ViT计算成本的依赖及封闭集性能与强预训练基线的差距，提示了效率与精度的权衡边界。

## 研究背景

HOI检测需同时解决实例定位与关系分类。定位依赖密集的空间特征以区分重叠的人-物对，而分类依赖全局语义以理解动作意图。传统CNN骨干擅长前者但语义泛化弱，CLIP等VLM擅长后者但空间分辨率低。这种特征属性的错位，使得单一模型难以同时满足检测的精度与开放词汇的泛化需求。

主流开放词汇HOI方法分为两类：VLM协作型（如GEN-VLKT）保留独立检测器，通过特征融合引入VLM语义，但跨模型表示差异导致融合困难；VLM-only型（如SGC-Net）直接改造VLM为检测器，但CLIP的全局对齐目标牺牲了局部细节，导致定位性能下降。SL-HOI的切入点在于发现DINOv3内部存在功能互补：其自监督骨干保留密集空间细节，而文本对齐头提供语义抽象。通过解耦这两个组件的功能，并设计机制桥接二者间的表示鸿沟，可在单一冻结骨干上实现高性能检测。

## 核心方法

### 方法参照系

SL-HOI属于单阶段DETR风格HOI检测范式，但摒弃了传统的ResNet+CLIP双骨干结构。其关键差异在于：不依赖外部VLM进行特征蒸馏，而是利用DINOv3 dino.txt变体内部的“骨干-视觉头”功能分化，将定位与分类任务映射到同一冻结特征空间的不同子空间。

### 细粒度定位与交互查询生成

设计动机在于解决VLM-only方法因缺乏局部细节导致的定位失败。SL-HOI首先将DINOv3骨干输出的图像token $\mathbf{X}_b$ 降维并添加位置编码，通过一个包含 $L_E$ 层自注意力的检测适配器处理，生成用于定位的特征 $\mathbf{F}$。随后，使用两组可学习查询 $\mathbf{Q}_h, \mathbf{Q}_o$ 对 $\mathbf{F}$ 进行交叉注意力，得到人体与物体嵌入 $\mathbf{E}_h, \mathbf{E}_o$。交互查询 $\mathbf{Q}_r$ 由二者均值投影生成：

$$ \mathbf{Q}_r = \text{Proj}(\frac{\mathbf{E}_h + \mathbf{E}_o}{2}) $$

该公式将空间定位信息压缩为低维查询向量，作为后续语义分类的锚点，避免了直接对原始图像token进行高维分类的计算开销。

### 语义引导与分层精炼

设计动机在于消除交互查询 $\mathbf{Q}_r$ 与视觉头输出间的表示间隙。SL-HOI提出“语义引导”策略，将 $\mathbf{Q}_r$ 与骨干图像token $\mathbf{X}_b$ 共同输入冻结的视觉头。视觉头内的自注意力层使 $\mathbf{Q}_r$ 吸收全局语义，同时 $\mathbf{X}_b$ 被查询调制，生成富含上下文的图像token $\mathbf{X}_{head}$ 与精炼后的查询 $\mathbf{Q}'_r$。

$$ \mathbf{Q}'_r, \mathbf{X}_{head} = \text{VisionHead}([\mathbf{Q}_r; \mathbf{X}_b]) $$

此步骤强制查询与图像特征共享表示空间。随后，通过一个单层可学习交叉注意力解码器 $G_{decoder}$，以 $\mathbf{Q}'_r$ 为Query、$\mathbf{X}_{head}$ 为Key/Value，生成最终分类嵌入 $\mathbf{E}_r$：

$$ \mathbf{E}_r = G_{decoder}(\mathbf{Q}'_r, \mathbf{X}_{head}) $$

这种“粗粒度语义对齐+细粒度可学习精炼”的两步过程，既利用了冻结视觉头的预训练语义先验，又通过轻量级参数适配HOI特定任务，实现了开放词汇分类。

## 实验评估

SL-HOI在SWiG-HOI与HICO-DET上验证了架构有效性。基线覆盖VLM协作型（GEN-VLKT）与VLM-only型（SGC-Net），但未包含MLLM推理类方法（如AgentHOI），限制了跨范式对比。在HICO-DET开放词汇设置下，SL-HOI在无COCO预训练条件下，Unseen mAP达40.53%，显著优于同条件基线SGC-Net（23.27%）；在封闭集设置下，Full mAP达45.05%，超越使用BLIP-2骨干的BC-HOI（43.01%）。

| 数据集 | 设置 | 方法 | Backbone | Unseen | Seen | Full |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| HICO-DET | Open-Vocab | SGC-Net | CLIP-ViT-B/16 | 23.27 | 28.34 | 27.22 |
| HICO-DET | Open-Vocab | SL-HOI | DINOv3-ViT-L/16 | 40.53 | 42.99 | 42.49 |
| HICO-DET | Closed | BC-HOI | ResNet50 + BLIP-2-ViT-G/14 | - | - | 43.01 |
| HICO-DET | Closed | SL-HOI | DINOv3-ViT-L/16 | - | - | 45.05 |

消融实验显示，语义引导步骤贡献了最大的性能增益。在SWiG-HOI上，仅使用基线架构的Full mAP为21.82%，加入语义引导后提升至23.28%，进一步加入分层精炼后达到24.67%。这表明桥接表示间隙比单纯增加解码器复杂度更关键。然而，对比Late Fusion变体，SL-HOI在Unseen类别上优势明显（19.04% vs 16.55%），但在Rare类别上增益较小（24.69% vs 21.66%），暗示语义引导对长尾类别的泛化能力有限。

评估边界方面，SL-HOI未报告推理速度，仅指出ViT骨干计算成本高于CNN。代码已开源，超参数设置（如学习率 $1 \times 10^{-4}$，8卡RTX 4090）完整披露，可复现性良好。但实验未涵盖多视角或视频序列，仅针对单帧图像，限制了其在动态场景中的适用性评估。

## 关联研究分析

从方法设计看，SL-HOI与GEN-VLKT的核心差异在于特征融合机制。GEN-VLKT通过独立训练的检测器与CLIP进行特征拼接，面临跨模型表示对齐难题；SL-HOI则利用DINOv3内部组件的功能分化，通过“语义引导”在单一模型内实现特征共享。这种差异源于任务特性：HOI检测需要细粒度定位，而CLIP的全局对齐目标与此冲突，DINOv3的自监督预训练保留了密集细节，使得内部融合成为可能。

从问题动机看，SL-HOI与SGC-Net同属VLM-only路线，但SGC-Net直接改造CLIP，受限于其视觉编码器分辨率；SL-HOI选用DINOv3，其Gram锚定策略在大规模自监督训练中保留了空间细节。这一选择并非偶然，而是针对HOI检测中“人-物重叠”这一高频难点的针对性设计。然而，SL-HOI在封闭集性能上仍低于使用强预训练（如COCO）的BC-HOI，提示DINOv3的自监督特征在特定HOI类别上的语义丰富度可能不及对比学习预训练的CLIP，这一差距是否可通过增加HOI特定预训练数据弥补，论文未给出回答。

## 总结

SL-HOI旨在解决开放词汇HOI检测中定位精度与语义泛化的矛盾，其切入点在于利用DINOv3骨干与视觉头的功能互补，通过冻结骨干与轻量级交互查询桥接表示间隙。该方法在HICO-DET封闭集上以45.05%的mAP超越BC-HOI，在开放词汇无预训练条件下以40.53%的Unseen mAP大幅领先SGC-Net。其边界在于ViT骨干的高计算成本，以及封闭集性能对强预训练数据的依赖。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27500)