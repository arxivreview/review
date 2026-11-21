# HuggingFace最新推荐论文 ｜GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed ｜块状双向扩散解码的视觉定位基础模型

研究机构：北京大学、美国加州大学伯克利分校

作者：Qize Yu、Lianrui Fan、Bowen Ping 等 22 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.39600)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.39600)

> 视觉定位任务要求模型根据自然语言或视觉提示，在图像中精确输出对象边界框、点或文本区域。自回归（AR）解码将空间预测序列化为文本Token，导致串行延迟随输出长度线性增长，在密集场景下成为主要瓶颈。本文提出GroundAnything，通过块状双向扩散解码实现并行空间假设生成与联合去噪，在保持4B参数规模下同时优化精度与速度。该模型在30项基准上刷新了同规模AR模型的整体SOTA，但其扩散分支在OCR与布局任务上的精度损失揭示了并行生成与精细几何约束间的固有张力。

## 研究背景

当定位模型面对包含数十个实例的密集场景时，自回归解码需逐个生成坐标Token，每个Token的预测依赖前序所有Token的隐状态，形成严格的因果链。这种串行机制导致解码延迟与输出长度成正比，而实际应用中密集检测、批量OCR等任务往往需要长坐标列表，使得推理时间成为系统级瓶颈。为打破这一限制，多Token预测（MTP）通过并行生成多个Token来降低延迟，但MTP的并行度受限于预测窗口大小，且缺乏对已生成Token的联合修正能力。

视觉定位领域的主流范式已从专用检测器转向基于多模态大语言模型（MLLMs）的自回归坐标生成，如Pix2Seq、Florence-2和Rex-Omni。这些模型将边界框表示为量化坐标Token序列，利用语言模型的上下文推理能力处理复杂空间关系，但在密集场景下暴露出串行延迟与累积误差的双重瓶颈。LocateAnything引入MTP机制实现并行框解码，但其并行度受限于固定窗口，且无法对已提交的坐标进行迭代修正。扩散视觉语言模型（Diffusion VLMs）支持双向注意力与并行生成，但现有工作主要聚焦于多模态理解或GUI定位，未将其统一应用于多任务视觉定位基础模型。GroundAnything的切入点在于：将定位重构为结构化视觉证据提取问题，利用块状双向扩散的并行去噪特性，使空间假设能够同时涌现并基于共享视觉证据联合精炼，从而在解码效率与定位精度间取得平衡。

## 核心方法

### 块状双向扩散解码架构

GroundAnything基于Qwen3-4B语言骨干与MoonViT-V2视觉编码器，引入块状双向扩散解码机制。与标准AR解码的严格因果注意力不同，该架构将响应序列划分为固定大小的块（B=32），块内采用双向注意力实现并行去噪，块间保持因果依赖以支持KV缓存复用。这种设计允许模型在单个前向传播中同时预测块内所有坐标Token，而非逐个生成。其核心创新在于AR-to-Diffusion转换过程：从预训练的AR检查点出发，通过联合优化AR损失与掩码去噪损失，使模型同时具备因果生成与双向去噪能力，且两个模式共享全部模型权重。

$$
\mathcal{L}_{\text{joint}} = \frac{1}{|T|} \sum_{i \in T} -\log p_\theta(y_i | V, P, y_{<i}) + \frac{1}{|M^{(1)}| + |M^{(2)}|} \sum_{a=1}^{2} \sum_{i \in M^{(a)}} -\log p_\theta(y_i | x, w^{(a)}; A_a)
$$

该公式表明，训练过程同时监督因果预测（第一项）与掩码去噪（第二项），其中$M^{(a)}$为第$a$个噪声视图中被掩码的目标位置集合，$A_a$强制注意力可见性规则，确保噪声视图无法读取当前或未来的干净响应目标。这种联合目标使模型在保持AR生成能力的同时，习得并行去噪的几何约束。

### 熵引导并行提交与自投机解码

为在推理时平衡速度与精度，GroundAnything引入熵引导解码（Entropy-Guided Decoding）机制。该策略根据模型预测分布的熵值动态决定并行提交程度：低熵Token（高置信度）可批量提交，高熵Token（低置信度）则保留AR验证。具体而言，设定熵阈值$\tau$，当块内Token的预测熵低于$\tau$时，允许并行提交；否则回退至AR验证。这一机制解决了纯扩散解码中“过早提交”导致的精度损失问题，同时避免了纯AR解码的串行延迟。

$$
\text{TPS} = \frac{1}{\text{TPF}} \cdot \text{base\_throughput}, \quad \text{TPF} = \frac{\text{committed\_tokens}}{\text{forward\_calls}}
$$

其中TPF（Tokens Per Forward）衡量每次前向传播提交的Token数，TPS（Tokens Per Second）为输出吞吐量。熵引导解码通过自适应调整TPF，在COCO基准上实现127.0 TPS，较AR基线49.6 TPS提升2.56倍，同时F1mIoU仅下降2.98个百分点。自投机模式进一步结合扩散草稿与AR验证，在COCO上实现4.51倍加速，F1mIoU仅下降0.74个百分点，验证了并行解码在保持精度的同时显著降低延迟的可行性。

## 实验评估

实验覆盖30项基准，包括COCO、LVIS、Dense200、VisDrone、RefCOCO/+/g、ScreenSpot-Pro、DocLayNet等，对比44个基线，涵盖专用检测器（GroundingDINO）、AR定位模型（Rex-Omni、LocateAnything）、MTP模型及通用VLMs（Qwen3-VL、GPT-6 Astra）。基线覆盖全面，但缺乏纯扩散VLM在定位任务上的直接对比，如BAGEL在定位基准上的表现未纳入主表。

| 模型 | COCO F1mIoU | LVIS F1mIoU | Dense200 F1mIoU | RefCOCOg val | RefCOCOg test |
|---|---|---|---|---|---|
| GroundAnything-VLM | 63.70 | 56.63 | 75.55 | 84.37 | 83.56 |
| GroundAnything | 60.72 | 52.59 | 70.04 | 91.61 | 91.10 |
| Rex-Omni | 56.28 | 46.74 | 53.29 | 73.90 | 74.76 |
| LocateAnything Hybrid | 59.12 | 49.56 | 50.07 | 76.43 | 77.67 |
| GPT-6 Astra | 62.75 | 54.97 | 65.04 | 74.98 | 78.91 |

GroundAnything-VLM在COCO上达到63.70 F1mIoU，超越Rex-Omni（56.28）与LocateAnything Hybrid（59.12），与GPT-6 Astra（62.75）相当。GroundAnything扩散分支在RefCOCOg val/test上达到91.61/91.10，显著高于其AR变体（84.37/83.56），表明扩散解码在指代表达理解任务上具有优势。然而，在Dense200上，GroundAnything（70.04）低于GroundAnything-VLM（75.55），揭示扩散分支在密集小目标定位上的精度损失。

消融实验显示，替换量化坐标为文本坐标导致AR分数从73.03降至71.60，扩散分数从61.66降至55.98，证明紧凑坐标词汇对扩散解码的精度贡献更大。移除Stage III训练阶段使GroundAnything分数从61.66降至45.04，降幅16.62个百分点，远大于AR变体的1.29个百分点降幅，表明该训练阶段对扩散分支的几何约束习得至关重要。熵阈值$\tau$从0.2增至1.2时，COCO F1mIoU先升后降，在$\tau=0.8$时达到峰值60.72，验证了熵引导解码的速度-精度权衡存在最优操作点。

评估协议采用F1mIoU（IoU 0.50-0.95聚合）作为主指标，但未报告置信区间，且多数基线仅运行3次取平均，而GroundAnything运行10次，统计严谨性存在差异。代码与模型权重已开源，训练细节（GPU数量、学习率、批次大小）完整披露，可复现性较高。然而，基础设施加速实验（SGLang、CUDA Graph、FP8）仅报告延迟，未验证FP8量化对精度的影响，选择性量化可能改变Logits分布，进而影响提交或验证决策。

## 关联研究分析

从问题动机看，GroundAnything与LocateAnything均针对AR解码的串行延迟，但解决路径根本不同。LocateAnything采用MTP机制，通过固定窗口并行生成多个Token，其并行度受限于窗口大小，且无法对已提交Token进行联合修正。GroundAnything则利用块状双向扩散，允许块内所有Token同时涌现并基于共享视觉证据迭代精炼，其并行度理论上不受窗口限制，且具备联合修正能力。这一差异源于任务特性：密集场景下，对象间存在强空间相关性，MTP的独立预测假设失效，而扩散的联合去噪机制能捕获这种相关性。然而，GroundAnything在Dense200上的精度损失（70.04 vs 75.55）表明，扩散分支在极小目标定位上仍受限于块内双向注意力的感受野，而MTP的局部窗口可能更适合小目标的精细边界预测。

从方法设计看，GroundAnything与Rex-Omni同属MLLM定位框架，但解码范式截然不同。Rex-Omni采用纯AR解码，其精度优势源于因果注意力的长程依赖建模，但延迟随输出长度线性增长。GroundAnything通过AR-to-Diffusion转换，使模型同时具备因果与双向能力，其扩散分支在RefCOCOg上超越AR变体（91.61 vs 84.37），表明双向注意力在指代表达理解任务上能更好地捕获语言-视觉对齐。然而，在OCR任务上，GroundAnything（33.31 HierText）显著低于GroundAnything-VLM（41.33），揭示扩散解码在文本转录与区域定位联合任务上的精度损失。这一差异可能源于OCR任务对字符顺序的严格依赖，而扩散的并行生成机制难以保证字符的因果顺序，尽管论文未明确探讨这一机制。

## 总结

GroundAnything要解决的核心矛盾是自回归解码的串行延迟与密集场景下长坐标列表的推理成本。其切入点在于将定位重构为结构化视觉证据提取问题，利用块状双向扩散的并行去噪特性，使空间假设能够同时涌现并联合精炼，从而在4B参数规模下同时优化精度与速度。该模型通过AR-to-Diffusion转换与联合训练，在30项基准上刷新同规模AR模型的整体SOTA，GroundAnything-VLM达到72.42%平均分，GroundAnything扩散分支在RefCOCOg上达到91.61/91.10。然而，其边界在于扩散分支在OCR与密集小目标任务上的精度损失，以及熵引导解码在$\tau>0.8$时的非单调质量曲线。当块大小B从16增至32时，熵引导解码的COCO F1mIoU从61.58降至60.72，而自投机模式在B=32时达到峰值，这一操作点依赖性是否在其他任务上普遍存在，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.39600)