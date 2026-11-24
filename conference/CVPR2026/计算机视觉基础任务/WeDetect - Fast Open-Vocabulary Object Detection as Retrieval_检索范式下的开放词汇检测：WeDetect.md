# CVPR2026最新论文 ｜WeDetect: Fast Open-Vocabulary Object Detection as Retrieval ｜检索范式下的开放词汇检测：WeDetect

作者：Shenghao Fu、Yukun Su、Fengyun Rao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12309)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12309)

> 开放词汇目标检测（OVOD）旨在利用视觉-语言模型（VLMs）的跨模态对齐能力，实现对新类别的零样本识别。现有主流方法依赖深度融合层提升精度，但导致推理速度骤降且特征无法跨查询共享。本文切入点是将检测重构为检索问题，通过双塔架构与点积匹配替代融合，结合多粒度数据工程实现高效推理。该范式在效率与精度上取得平衡，但其对大规模标注数据的依赖及细粒度场景下的上限仍存疑。

## 研究背景

当检测器面对训练集未出现的新类别时，其闭集假设失效，需借助 VLMs 提供的共享语义嵌入空间进行零样本识别。这一过程的核心是跨模态对齐，即让区域视觉特征与文本嵌入在统一空间中可比较。然而，对齐质量受限于特征提取方式：若采用深度融合，视觉特征会被特定文本查询“污染”，导致不同查询间无法复用计算结果，推理延迟随类别数线性增长。

OVOD 领域长期存在精度与效率的权衡困境。GLIP 和 Grounding DINO 等基于短语定位范式的方法，通过大规模区域-文本预训练提升了细粒度语义理解，但其 Transformer 架构中的跨模态融合层（如交叉注意力）使得单张图像评估 1,203 个类别需多次前向传播，Grounding-DINO 在 LVIS 上耗时数秒。YOLO-World 虽引入单阶段架构提升速度，但仍保留融合机制。本文抓住“非融合范式”被低估的潜力，指出其本质是检索问题——在共享嵌入空间中匹配区域与文本，从而天然支持特征共享与并行计算。

## 核心方法

### 双塔架构与点积分类

本文摒弃了 GLIP 和 Grounding DINO 中的跨模态融合层，采用 CLIP 风格的双塔架构。视觉编码器基于 ConvNeXt 骨干提取多尺度特征，语言编码器基于 XLM-RoBERTa 编码类别名称。分类不再通过复杂的注意力交互，而是直接计算图像网格特征与类别文本嵌入的点积。这一设计动机在于消除融合层带来的计算开销，并使得视觉特征独立于具体查询，支持一次前向传播处理所有类别。

$$
S_{cls} = \mathbf{f}_{img} \cdot \mathbf{t}_{cls}
$$

其中 $\mathbf{f}_{img}$ 为区域视觉特征向量，$\mathbf{t}_{cls}$ 为类别文本嵌入向量，$S_{cls}$ 为匹配得分。该公式表明，检测退化为在预训练语义空间中的最近邻检索，物理含义是衡量区域视觉内容与文本描述的语义相似度。

### 多粒度标签采样与分阶段训练

为解决非融合架构在细粒度对齐上的潜在短板，本文构建了包含 15M 图像和 330M 边界框的数据集，并引入多粒度标签采样策略。每个物体标注为层级结构（如“animal, dog, a yellow dog”），训练时随机采样其中一个标签作为监督信号。这一设计动机在于，静态类别名称无法捕获类内视觉变化，而动态采样的细粒度描述提供了更丰富的负样本和更精准的语义约束。

$$
\mathcal{L}_{total} = \mathcal{L}_{contrastive} + \lambda \mathcal{L}_{box}
$$

其中 $\mathcal{L}_{contrastive}$ 为区域-文本对比损失，$\mathcal{L}_{box}$ 为边界框回归损失。多粒度采样通过增加文本词汇多样性，间接优化了对比损失中的负样本分布，使得模型在训练过程中能接触到更广泛的语义变体，从而提升零样本泛化能力。

### 通用提案生成与 LLM 分类

WeDetect-Uni 冻结整个检测器，仅训练一个可学习的物体性提示（objectness prompt），用于生成通用提案。由于检测器冻结，提案的边界框嵌入保持类特异性，可缓存用于后续检索。WeDetect-Ref 则利用 LLM 作为分类器，对 WeDetect-Uni 生成的提案进行并行二分类，替代传统的 next-token prediction。这一设计动机在于，LLM 的自回归解码速度慢且易遗漏多实例，而并行分类避免了序列依赖，实现了单次前向传播完成复杂表达理解。

## 实验评估

| 方法 | 骨干 | LVIS minival AP | LVIS AP | COCO AP | ODinW13 AP | FPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| YOLO-World-L | YOLOv8-L | 35.4 | 26.8 | 44.9 | 38.4 | 54.6 |
| WeDetect-Tiny | ConvNext-T | 37.4 | 31.4 | 44.9 | 46.4 | 62.5 |
| WeDetect-Large | ConvNext-L | 55.0 | 49.4 | 54.5 | 53.4 | 6.0 |
| Grounding-DINO | Swin-T | 27.4 | 20.1 | 45.8 | 51.4 | 6.0 |

WeDetect-Tiny 在 LVIS minival 上以 37.4 AP 超越 YOLO-World-L 的 35.4 AP，且推理速度从 54.6 fps 提升至 62.5 fps。WeDetect-Large 在 LVIS 上达到 49.4 AP，显著高于 Grounding-DINO 的 20.1 AP，验证了非融合架构在大规模数据支持下的精度上限。基线覆盖包括 YOLO-World、Grounding DINO 和 GLIP，但缺乏基于 DETR 的轻量级基线（如 DeCo-DETR）对比，可能低估了其他高效架构的竞争力。

| 消融实验 | RefCOCO Avg | COCO AP |
| :--- | :--- | :--- |
| WeDetect-Ref 4B | 93.0 | 47.5 |
| w/o negative det data | 93.1 | 42.1 |
| BCE loss | 92.8 | 43.1 |

消融实验显示，移除负检测数据导致 COCO AP 下降 5.4 点，表明负样本监督对鲁棒性至关重要。将 Sigmoid Focal Loss 替换为 BCE Loss 导致 AP 下降 4.4 点，验证了 Focal Loss 在处理类别不平衡时的有效性。多粒度标签采样中，仅使用细粒度标签导致 AP 下降 1.6 点，仅使用粗粒度标签下降 2.2 点，证明混合粒度策略的必要性。

实验在 LVIS、COCO、ODinW 等标准基准上进行，指标为 AP。代码已开源，但论文未报告置信区间，且训练数据包含 COCO 数据（灰色数字标注），可能导致评估协议不公。WeDetect-Ref 在 RefCOCO 上达到 93.2 平均分，超越 Qwen3-VL 4B 的 86.6 分，但推理速度仅为 5.3 fps，远低于 WeDetect 主模型，限制了其实时应用潜力。

## 关联研究分析

从方法设计看，WeDetect 与 YOLO-World 同属单阶段检测器，但关键差异在于融合层的移除。YOLO-World 保留视觉-语言融合以增强对齐，而 WeDetect 依赖数据工程弥补对齐损失。这一差异的根源在于任务特性：当类别数较少时，融合层的计算开销可接受；但当类别数增至 1,203（LVIS）时，融合层的延迟成为瓶颈。WeDetect 通过 ConvNeXt 骨干提供多尺度特征，部分替代了融合层在空间细节上的作用，但其在极端细粒度场景（如 FG-OVD）的表现未经验证。

从问题动机看，WeDetect-Ref 与 Grounding DINO 均处理指代表达理解（REC），但路线截然不同。Grounding DINO 基于检测器直接定位，而 WeDetect-Ref 基于 LLM 分类提案。这一差异源于 LLM 的自回归机制缺陷：next-token prediction 导致推理速度慢且易遗漏多实例。WeDetect-Ref 通过并行分类规避了这一缺陷，但其性能依赖于 WeDetect-Uni 的提案质量。若提案召回率低，LLM 分类器无法纠正，这构成了该范式的潜在盲区。

## 总结

WeDetect 旨在解决 OVOD 中精度与效率的矛盾，抓住“非融合范式”被低估的潜力，通过双塔架构与多粒度数据工程实现高效推理。实验证明，WeDetect-Tiny 在 LVIS minival 上以 37.4 AP 超越 YOLO-World-L，且推理速度提升 14.5%。其边界在于对大规模标注数据的依赖，以及 WeDetect-Ref 在实时性上的不足。当支持集规模缩小至弱监督场景时，多粒度标签采样的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12309)