# CVPR2026最新论文 ｜LottieGPT: Tokenizing Vector Animation for Autoregressive Generation ｜矢量动画自回归生成

研究机构：清华大学、香港理工大学

作者：Junhao Chen、Kejun Gao、Yuehan Cui 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11792)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11792)

> 现有视频生成模型局限于像素空间，无法产出具备无限分辨率、结构可编辑及参数化运动特性的矢量动画，而传统矢量生成方法又缺乏时序建模能力。本文切入点在于将矢量动画视为结构化程序而非像素序列，通过设计层级化Lottie Tokenizer与构建大规模动画数据集，实现从文本到可编辑矢量动画的自回归生成。其价值在于填补了矢量动画生成的空白，但自回归范式在长序列依赖与复杂运动协调上的泛化能力仍存疑。

## 研究背景

矢量动画生成面临的核心困境是表征空间的割裂：像素视频生成模型（如Sora、Kling）虽具备高保真度，但输出为固定分辨率的位图，无法支持专业设计工作流中必需的无限缩放与图层级编辑；而静态矢量图形生成方法（如OmniSVG、StarVector）虽能输出SVG代码，却仅处理单帧图像，缺乏对关键帧、缓动函数及时间轴逻辑的建模能力。这种割裂导致现有工具无法直接生成Lottie格式等工业标准动态矢量内容，迫使设计师依赖After Effects等重型软件手动制作，阻碍了AI在UI/UX动效、品牌动画等场景的自动化落地。

矢量动画生成的研究脉络正从“像素空间扩散”向“结构化数据自回归”迁移。早期工作聚焦于静态SVG的代码合成，将矢量图形视为文本序列进行生成，但这类方法无法表达时间依赖的变换逻辑。随着视觉语言模型（VLM）在3D网格、CAD模型等结构化数据生成上的突破，研究者意识到矢量动画本质上是由层级图层、几何基元、关键帧及插值函数组成的结构化程序，这为自回归建模提供了可能。然而，直接套用文本Tokenizer或静态SVG Tokenizer会丢失层级语义或无法编码运动曲线，且缺乏大规模矢量动画训练数据。本文的切入点在于解决这两个根本障碍：设计能统一编码层级几何与时间运动的Lottie Tokenizer，并构建首个大规模Lottie动画数据集，从而在自回归框架下实现原生矢量动画生成。

## 核心方法

### 方法参照系

本文问题可归类为“结构化数据自回归生成”，其标准流程为：将目标结构（如3D网格、CAD模型）Token化为离散序列，利用VLM进行下一Token预测。与3D网格生成等通用流程的关键差异在于，矢量动画不仅包含空间几何结构，还包含时间维度的参数化运动逻辑（关键帧、缓动函数），且需保持层级嵌套关系以支持编辑性。现有静态SVG生成方法（如OmniSVG）仅处理空间结构，缺乏时间压缩机制；而像素视频生成方法虽有时序建模，但输出不可编辑。本文需在Token化阶段同时解决空间层级编码与时间运动压缩问题。

### 层级化结构编码

针对静态SVG Tokenizer将代码视为纯文本、丢失图层组语义的问题，本文设计Lottie Tokenizer，利用Lottie JSON的严格层级结构（Animation Meta → Assets → Layers → Shapes → Properties）进行层级化编码。每个层级使用专用Token（如`<|LAYER|>`, `<|ITEM_sh|>`）标记边界，几何基元（路径、椭圆、填充等）按类型特定格式编码，避免像OmniSVG那样将复杂形状分解为原子线段。这种编码方式使模型能学习结构模式而非任意文本序列，保留组合结构以支持VLM推理。例如，路径形状编码为`<|ITEM_sh|><|KS_STATIC|><|i|>...<|o|>...<|v|>...<|c|>`，直接对应Lottie schema，确保解码后的JSON结构完整可编辑。

### 关键帧运动压缩

针对逐帧存储导致序列过长、无法自回归建模的问题，本文引入关键帧运动压缩机制，仅存储关键帧（Keyframes）与插值函数（Easing Functions），而非密集逐帧数据。每个动画属性遵循统一编码模式：`<|PROP_ANIMATED|><|PROP_KF_START|><keyframe_1>...<keyframe_n><|PROP_KF_END|>`。每个关键帧包含时间戳`<|t|>`、属性值Token及可选的贝塞尔缓动参数`<|ease|>`。该设计实现显著压缩：对于300帧/5关键帧的动画，压缩率达98%。缓动函数作为一等公民被显式编码，允许相同关键帧产生不同运动质感（线性、缓入、弹跳等），这是像素表示中完全缺失的关键信息。解码时通过递归解析重建JSON，实现无损往返，确保渲染结果与原始动画一致。

## 实验评估

实验在自建LottieBench上进行，包含230个动画样本（按Token数分层：Simple 150, Medium 40, Complex 40）和400个静态图形样本。基线覆盖静态矢量生成（OmniSVG-7B, StarVector-8B）、像素视频生成（Sora2, Kling, Veo3.1）及通用VLM（GPT-5, Claude Sonnet 4.5, Gemini 2.5 Pro）。在静态矢量图形生成任务上，LottieGPT-7B-Stage1在Text-Only输入下CLIP得分0.2893，优于OmniSVG-7B的0.2676；在Text+Image输入下CLIP得分0.2871，优于OmniSVG-7B的0.2772。在矢量动画生成任务上，LottieGPT-7B-Stage2在Text-Only输入下CLIP得分0.2985，JSON结构得分0.8062，Valid Rate 96.96%，显著优于Few-shot VLM（如GPT-5 CLIP 0.2640, Valid Rate 10.87%）和像素视频模型（Sora2 CLIP 0.8903但JSON/N/A）。

| 任务 | 方法 | CLIP↑ | SSIM↑ | LPIPS↓ | DINOv2↑ | JSON↑ | Valid Rate(%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Text-Only Static | OmniSVG-7B | 0.2676 | 0.5123 | 0.7274 | N/A | N/A | N/A |
| Text-Only Static | LottieGPT-7B-Stage1 | 0.2893 | 0.8103 | 0.1755 | 0.8572 | 0.8239 | 98.25 |
| Text-Only Animation | GPT-5 | 0.2640 | 0.0358 | 0.2640 | 0.3115 | 45.22 | 10.87 |
| Text-Only Animation | LottieGPT-7B-Stage2 | 0.2985 | 0.9776 | 0.0366 | 0.9301 | 0.8062 | 96.96 |

消融实验显示，仅使用Lottie JSON直接微调（Finetuned w. Lottie JSON）的模型在动画任务上表现较差（CLIP 0.2236, Valid Rate 22.61%），验证了Lottie Tokenizer的必要性。LottieGPT-7B-Stage1（仅静态训练）在动画任务上表现不佳，证明Static-to-Dynamic两阶段训练策略的有效性：先学习静态矢量构图，再引入时序动态，避免联合训练时因动画样本Token数远大于静态样本导致的收敛不稳定。

评估边界方面，LottieBench缺乏与像素视频生成模型的直接可比性，因输出格式不同（矢量JSON vs 像素帧）。JSON结构指标（Key-F1, ValueMatch）虽能衡量结构正确性，但可能掩盖视觉细节缺失。可复现性上，论文提供Project Page，但代码未明确开源；训练使用8×H20 GPUs，Stage 1用750K MMSVG-icon样本，Stage 2用60K Lottie动画样本，数据规模受限。

## 关联研究分析

从问题动机看，本文与OmniSVG同属矢量图形生成，但OmniSVG聚焦静态SVG代码合成，将矢量图形视为文本序列，缺乏时间维度建模；本文则通过Lottie Tokenizer引入关键帧与缓动函数，解决动态矢量生成的时序协调问题。这一差异源于任务特性：静态图形无需时间逻辑，而动画需显式编码运动曲线。OmniSVG的原子化SVG Tokenizer在静态场景下足够，但在动画中会丢失层级语义与运动质感，本文的层级化编码正是对此失效的修正。

从方法设计看，本文与3D网格生成（如MeshGPT, EdgeRunner）同属结构化数据自回归生成，但3D网格生成处理空间几何拓扑，本文处理空间+时间双维度结构。3D网格Token化通常基于顶点/边序列，而本文Lottie Tokenizer需同时编码层级嵌套与时间关键帧。这一差异导致本文需设计更复杂的压缩机制（关键帧运动压缩），而3D网格生成可依赖空间局部性。本文的Static-to-Dynamic训练策略借鉴了课程学习思想，但具体应用于矢量动画的时序引入，与3D生成中从粗到细的网格细化策略不同，前者解决静态/动态任务间的分布差异，后者解决空间分辨率差异。

## 总结

本文要解决的核心矛盾是像素视频生成与矢量动画生成在表征空间上的割裂：前者高保真但不可编辑，后者可编辑但缺乏时序建模。本文抓住的切入点是矢量动画的结构化程序本质，通过Lottie Tokenizer统一编码层级几何与时间运动，并构建大规模数据集，使自回归VLM能直接生成可编辑矢量动画。实验证明，LottieGPT-7B-Stage2在动画生成上CLIP得分0.2985、Valid Rate 96.96%，显著优于Few-shot VLM和像素视频模型，且在静态SVG生成上超越OmniSVG。本文的边界在于：自回归范式对长序列依赖的建模能力未充分验证，复杂多图层动画的生成质量可能受限于序列长度；Static-to-Dynamic训练策略的必要性虽经消融验证，但联合训练在更大算力下的表现未知。当动画复杂度（Token数）超过40K时，模型性能是否急剧下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11792)