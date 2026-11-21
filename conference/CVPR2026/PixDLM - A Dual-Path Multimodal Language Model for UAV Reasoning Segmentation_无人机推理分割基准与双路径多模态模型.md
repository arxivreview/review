# CVPR2026最新论文 ｜PixDLM: A Dual-Path Multimodal Language Model for UAV Reasoning Segmentation ｜无人机推理分割基准与双路径多模态模型

研究机构：厦门大学

作者：Shuyan Ke、Yifan Mei、Changli Wu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15670)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15670)

> 无人机高空视角下的推理分割任务面临视角畸变、极端尺度变化与超高分辨率细节丢失的三重挑战，现有地面视角推理分割模型因低分辨率Token压缩导致小目标语义断裂。本文通过构建首个专用基准DRSeg并提出双路径视觉编码器PixDLM，将高分辨率结构特征注入低分辨率语义推理流程，在不增加视觉Token成本的前提下实现像素级指令驱动分割。该工作填补了UAV推理分割的评估空白，但缺乏对计算效率与动态场景时序一致性的验证，其基准的GPT-5标注鲁棒性仍需更严格的交叉验证。

## 研究背景

推理分割要求模型根据自由形式的自然语言指令生成像素级掩码，其核心在于将隐含的空间配置、视觉状态或场景意图转化为精确的几何区域。当这一任务从地面视角迁移至无人机（UAV）高空视角时，传统多模态大模型（MLLM）的视觉Token压缩机制成为瓶颈：UAV图像中车辆、行人等关键目标往往仅占数十像素，在低分辨率Token化过程中极易丢失高频边界信息，导致模型无法区分“最靠近人行横道的车辆”与“背景中的静止车辆”等细粒度空间关系。

现有推理分割基准如LISA、PixelLM均基于地面或垂直俯视（Nadir-view）图像构建，其视觉假设（中等分辨率、有限尺度变化、稳定相机朝向）在UAV场景中全面失效。UAV图像的高空斜视视角导致透视几何连续变化，超高分辨率场景同时包含全局环境上下文与细粒度结构线索（如屋顶、车道、围栏），要求模型在全局语义与微小高频细节间进行联合推理。然而，VisDrone、DroneVehicle等现有UAV数据集缺乏细粒度标注、多样化语义覆盖及推理导向的文本监督，无法支撑指令依赖的目标定义任务。本文切入点在于形式化UAV推理分割任务，构建包含思维链（CoT）监督的专用基准DRSeg，并设计针对UAV视觉统计特性的双路径基线模型PixDLM。

## 核心方法

### 方法参照系

本文任务属于指令驱动的像素级预测范畴，与标准指代分割（Referring Segmentation）的关键差异在于类别无关性（Category-agnostic）与隐含语义推理。标准指代分割通常依赖显式物体提及（如“红色卡车”），而UAV推理分割指令强调空间配置（“最靠近人行横道的车辆”）、视觉状态（“有破损电池的光伏板”）或场景意图（“适合着陆的区域”），要求模型从场景上下文与推理线索中推断分割目标，而非表面类别识别。

### 双路径视觉编码器

传统MLLM采用单一低分辨率视觉编码器（如CLIP ViT-L），其Token压缩导致UAV图像中占图像面积<2%的小目标边界信息丢失。PixDLM在视觉编码阶段引入双路径架构，Global-Scope Path使用CLIP ViT-L处理448×448低分辨率图像以捕获长程语义上下文，Fine-Scope Path使用SAM Hiera-LSAM处理1024×1024高分辨率图像以保留密集结构细节。两路径通过三阶段潜空间融合（Three-stage latent fusion）实现跨分辨率对齐，在第k阶段（k∈{1,2,3}）将Fine-Scope Path特征对齐至Global-Scope Path当前潜空间的通道维度与空间分辨率后，执行门控残差融合：

$$F_{g}^{[k]} = B_k(F_{g}^{[k-1]}) + G_k(\tilde{F}_{s}^{[k]}) \odot F_{g}^{[k-1]}$$

其中$B_k$为第k阶段Global-Scope Path的变换函数，$G_k$为可学习门控函数，$\odot$表示逐元素缩放。该设计使高分辨率结构线索在编码器全程而非仅在输出端影响表示学习，解决了低分辨率Token化导致的小目标边界断裂问题。

### 层级推理解码器

LLM输出的Mask Token包含跨模态推理信号但缺乏细粒度空间信息。PixDLM引入层级推理解码器（Hierarchical Reasoning Decoder），在第l层接收视觉特征图$F_l$与更高层预测掩码$M_{l+1}$，通过掩码调制特征重要性：

$$\hat{F}_l = F_l \odot \sigma(M_{l+1})$$

其中$\sigma$为Sigmoid函数，该操作将注意力引导至高置信度区域并抑制噪声。所有n个中间掩码$\{M_1, ..., M_n\}$通过可学习层级系数融合为最终掩码：

$$M_{final} = \sum_{l=1}^{n} \alpha_l M_l$$

该层级细化机制在UAV推理分割中至关重要，因为目标尺度与外观变化剧烈，跨尺度语义一致性需通过渐进式空间精度提升来保证。

## 实验评估

实验在自建DRSeg基准上进行，包含10,000张高分辨率UAV图像与10,000个实例掩码，训练/验证/测试集按3:2:5划分。基线覆盖LISA-7B/13B、PixelLM-7B/13B、SegEarth-R1等主流推理分割模型，但缺失UAV专用检测/跟踪基线（如YOLO系列），因任务范式不同。SFT设置下，PixDLM在Attribute Reasoning维度取得62.80% gIoU与62.84% cIoU，优于LISA-7B-v1（59.22%/57.35%）与PixelLM-7B（59.66%/55.19%）；Scene Reasoning维度取得61.75% gIoU与64.03% cIoU，Spatial Reasoning维度取得62.51% gIoU与62.80% cIoU。

| 设置 | 模型 | Attribute gIoU | Attribute cIoU | Scene gIoU | Scene cIoU | Spatial gIoU | Spatial cIoU |
|---|---|---|---|---|---|---|---|
| SFT | LISA-7B-v1 | 59.22 | 57.35 | 53.25 | 54.29 | 55.38 | 54.47 |
| SFT | PixelLM-7B | 59.66 | 55.19 | 54.29 | 55.92 | 56.25 | 56.21 |
| SFT | PixDLM | 62.80 | 62.84 | 61.75 | 64.03 | 62.51 | 62.80 |

消融实验显示，仅使用DRSeg训练（无RRSIS-D）配合CoT监督取得最佳配置（Attribute: 62.80%/62.84%），混合RRSIS-D训练反而降低Scene Reasoning性能（55.92% vs 61.75%），表明UAV专用数据与通用指代分割数据存在分布冲突。双路径编码器消融中，激活第4层（完整双路径）相比仅激活第1层（仅Global-Scope）在Scene Reasoning维度提升6.56% gIoU（55.19%→61.75%），验证高分辨率路径对场景级推理的关键作用。解码器深度从2层增至3层，ALL维度gIoU从56.43%提升至62.35%，cIoU从58.01%提升至63.23%。

评估指标仅包含gIoU与cIoU，缺乏FPS、参数量等效率指标，无法验证SWaP约束下的实时性。DRSeg的CoT标注由GPT-5生成并经人工验证，论文报告对10%样本的CoT进行掩码、洗牌与语义破坏实验后性能变化有限，但未提供具体数值。代码与模型已开源，训练使用8块RTX 3090 GPU，DeepSpeed ZeRO-2，batch size 2，10个梯度累积步，10 epochs。

## 关联研究分析

从问题动机看，PixDLM与LISA、PixelLM共享推理分割范式，但核心差异在于视觉Token处理策略。LISA采用<SEG> token与embedding-as-mask解码器，PixelLM集成轻量像素解码器与分割码本，两者均依赖低分辨率视觉Token，在UAV小目标场景下因Token压缩导致边界信息丢失。PixDLM通过Dual-Path Encoder将高分辨率SAM特征注入CLIP潜空间，解决了这一特定失效。然而，LISA与PixelLM在地面视角指代分割任务上仍具优势，PixDLM在RefCOCOs等标准基准上的性能虽具竞争力，但未证明其Dual-Path设计在通用场景下优于单一高分辨率编码器（如LLaVA-HR的直接高分辨率处理），UAV特性是否迫使双路径设计而非通用改进，论文未给出对照实验。

从方法设计看，PixDLM与GeoPix、GeoPixel等遥感推理分割模型同属地理空间推理分支，但任务定义存在根本差异。GeoPix与GeoPixel针对卫星垂直俯视图像，依赖空间先验与拓扑线索，类别体系相对封闭；PixDLM针对UAV斜视视角，强调类别无关的隐含语义推理，指令涉及空间配置、视觉状态与场景意图。这一差异源于UAV低空动态场景的复杂性，但PixDLM未探索GeoPix的空间先验机制是否可迁移至UAV场景，也未评估其模型在卫星视角下的性能退化程度，跨视角泛化能力存疑。

## 总结

本文核心矛盾在于UAV高空视角下极端尺度变化与超高分辨率细节需求同MLLM低分辨率Token压缩机制的冲突。现有推理分割模型因视觉假设不匹配导致小目标语义断裂，PixDLM通过双路径视觉编码器将高分辨率结构特征注入低分辨率语义推理流程，在不增加视觉Token成本的前提下实现像素级指令驱动分割。DRSeg基准上SFT后PixDLM在Attribute Reasoning维度取得62.80% gIoU，Scene Reasoning维度取得64.03% cIoU，验证了双路径架构对UAV小目标分割的有效性。论文边界在于缺乏计算效率指标、未验证动态场景时序一致性，且DRSeg的GPT-5标注鲁棒性仅通过10%样本的破坏实验间接验证。当支持集从10k图像扩展至百万级规模时，Dual-Path Encoder的门控融合机制是否仍能有效平衡全局语义与局部细节，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15670)