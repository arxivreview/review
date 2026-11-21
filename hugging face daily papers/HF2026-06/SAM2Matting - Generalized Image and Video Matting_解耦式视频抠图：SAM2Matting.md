# HuggingFace最新推荐论文 ｜SAM2Matting: Generalized Image and Video Matting ｜解耦式视频抠图：SAM2Matting

研究机构：复旦大学

作者：Ruiqi Shen、Guangquan Jie、Chang Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.27339)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.27339)

> 视频抠图（Video Matting）旨在从动态序列中分离前景目标并预测像素级透明度（Alpha Matte），其核心矛盾在于高层时序跟踪与低层细节感知的冲突。现有方法依赖昂贵且领域狭窄的视频抠图数据集，导致模型泛化性受限且牺牲了跟踪鲁棒性。本文提出SAM2Matting，通过冻结VOS骨干负责时序一致性，仅训练轻量级Matting组件处理细节，实现了零样本视频抠图。该框架在保持实时性的同时刷新了SOTA，但其对长视频身份漂移的鲁棒性尚未得到充分验证。

## 研究背景

视频抠图要求模型在维持目标身份一致性的同时，精确捕捉发丝、半透明物体等细微结构。这一需求引出了两个核心概念：时序一致性（Temporal Consistency）与像素级透明度估计（Alpha Estimation）。前者依赖高层语义理解以应对遮挡与运动，后者则要求低层视觉特征对边界进行亚像素级解析。传统方法试图在单一模型中同时优化这两者，但发现高层跟踪所需的粗粒度特征与低层抠图所需的细粒度特征在表征空间上存在冲突，导致模型难以兼顾全局稳定性与局部细节。

主流视频抠图路线依赖大规模视频Matting数据集（如VideoMatte、HIM）进行端到端训练。然而，像素级Alpha标注成本极高，现有数据集规模有限且主要聚焦于人类中心场景，缺乏对复杂动态环境的覆盖。这种数据瓶颈导致从零训练模型无法建立鲁棒的跟踪能力，而微调预训练VOS模型则会破坏其原有的时序稳定性。本文切入点在于解耦这两个子任务：利用已在大规模视频分割数据上训练成熟的VOS模型（如SAM2、SAM3）提供时序一致的粗掩码，再引入专门针对图像Matting数据训练的组件进行细节细化，从而规避视频Matting数据稀缺的限制。

## 核心方法

### 方法参照系

视频抠图的标准流程通常包含目标定位、时序传播与Alpha预测三个环节。本文问题与该通用流程的关键差异在于：不再将Alpha预测视为时序传播的附属输出，而是将其重构为基于静态图像Matting能力的独立模块，通过接口对齐实现与动态跟踪的解耦。

### ROI检测器

传统方法通过形态学操作（如膨胀腐蚀）生成感兴趣区域（ROI），隐含假设边界重要性均匀，易遗漏复杂结构或包含确定前景。本文引入ROI检测器，将其重构为像素级二分类任务，以识别包含精细细节或半透明性的“Matting关键区域”。该设计解决了规则化ROI在复杂纹理下失效的问题，同时修正了VOS掩码的跟踪误差。对于帧 $t$ 的尺度 $i$，ROI Logit图 $L_{t,i}$ 由图像特征 $F_{t,i}$、帧 $I_{t,i}$ 及掩码 $M_{t,i}$ 经卷积头 $f_{R,i}$ 生成：

$$ L_{t,i} = f_{R,i}(F_{t,i}, I_{t,i}, M_{t,i}) $$

多尺度Logit图经层级卷积聚合后，通过Sigmoid激活与阈值 $\theta$ 得到最终ROI $R_t$。这一机制使模型能动态聚焦于真正需要精细处理的区域，而非盲目处理全图。

### 渐进式Alpha预测器

ROI确定后，Alpha估计被建模为从粗到细的级联细化过程。与并行处理不同，该预测器将前一尺度的Alpha作为下一尺度的引导输入，逐步捕捉更精细的细节。在尺度 $i$，复合输入 $X_{t,i}$ 拼接了图像特征、帧、伪Trimap及上采样后的前一尺度Alpha $A_{t,i-1}$：

$$ A_{t,i} = f_{A,i}(g_{A,i}(X_{t,i})) $$

其中 $g_{A,i}$ 为投影层，$f_{A,i}$ 为Matting头。最终尺度 $n$ 的Alpha上采样至原始分辨率。该设计通过多尺度监督（Deep Supervision）确保中间预测的质量，避免了单尺度预测在细节恢复上的局限，同时通过Matte-Mask一致性损失 $L_{con}$ 锚定Alpha与VOS掩码，防止前景内部出现空洞。

## 实验评估

实验在V-HIM60与VideoMatte基准上以零样本方式评估，对比MatAnyone2、MaGGIe等基于视频Matting数据训练的SOTA方法。基线覆盖了从早期RVM到最新MatAnyone2的多种路线，但未包含基于MLLM的VOS方法，这可能低估了语义推理对复杂场景的影响。

| 方法 | V-HIM60-Hard MAD↓ | V-HIM60-Hard dtSSD↓ | VideoMatte-SD MAD↓ | VideoMatte-SD dtSSD↓ |
| :--- | :--- | :--- | :--- | :--- |
| MatAnyone2 | 13.71 | 4.24 | 4.83 | 1.15 |
| SAM2Matting (SAM3) | 11.77 | 3.81 | 4.44 | 1.11 |

SAM2Matting (SAM3) 在V-HIM60-Hard上MAD为11.77，优于MatAnyone2的13.71；在VideoMatte-SD上MAD为4.44，优于MatAnyone2的4.83。dtSSD指标显示其时序一致性继承自VOS骨干，显著优于依赖视频数据训练的基线。

消融实验表明，性能提升主要源于架构与监督设计，而非更大的训练数据或更强的骨干。在控制训练数据与骨干相同的条件下，SAM2Matting仍优于MAM与Matte Anything。ROI策略的消融显示，基于学习的ROI检测器优于形态学操作，特别是在处理发丝等精细结构时。

评估边界方面，指标涵盖MAD、MSE、Grad、Conn及dtSSD，但未报告计算效率的具体FPS数值（仅定性描述为实时）。代码已开源，超参数（如 $\theta=0.65$）明确，可复现性良好。然而，实验未包含超过1000帧的长视频测试，无法验证冻结骨干在长时序下的身份漂移问题。

## 关联研究分析

从问题动机看，SAM2Matting与MatAnyone2的核心差异在于数据依赖策略。MatAnyone2依赖大规模视频Matting数据以学习时序Alpha动态，而SAM2Matting假设时序一致性可由VOS骨干独立解决，仅需图像Matting数据学习空间细节。这一差异源于对“时序一致性来源”的不同假设：前者认为Alpha动态需显式学习，后者认为VOS掩码已隐含足够的时序信息。若VOS掩码在快速形变或遮挡下出现误差，SAM2Matting的ROI检测器虽能部分修正，但无法完全弥补骨干的跟踪失败，这构成了其泛化性的潜在盲区。

从方法设计看，SAM2Matting与基于MLLM的VOS方法（如Sa2VA）在解耦粒度上存在差异。Sa2VA解耦语义推理（MLLM）与像素分割（SAM2），而SAM2Matting解耦时序跟踪（VOS）与细节估计（Matting）。前者关注语义对齐，后者关注低层感知。SAM2Matting未引入MLLM，而是依赖SAM3的文本提示能力，这意味着其对复杂指令的理解能力受限于SAM3的预训练范围。在需要细粒度语义区分（如“穿红衣服的人” vs “穿蓝衣服的人”）的场景中，SAM2Matting可能不如MLLM-based方法灵活，但其轻量化设计在实时性上具有优势。

## 总结

SAM2Matting旨在解决视频抠图中高层跟踪与低层细节的冲突，通过解耦VOS骨干与Matting组件，利用图像Matting数据实现零样本视频抠图。该方法在V-HIM60-Hard上MAD达11.77，优于MatAnyone2的13.71，证明了解耦设计的有效性。其边界在于依赖VOS骨干的跟踪鲁棒性，当骨干在长视频或极端遮挡下失效时，Matting组件无法独立恢复身份一致性。当支持集增大到长视频序列时，冻结骨干的身份漂移是否会导致Alpha Matte的时序不一致，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.27339)