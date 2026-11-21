# CVPR2026最新论文 ｜Reasoning Diffusion for Unpaired Test Time Out-of-distribution Text-Image to Video Generation ｜非配对文本-图像到视频生成中的推理扩散

研究机构：清华大学

作者：Zirui Pan、Xin Wang、Yipeng Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2d4da8ec327f)

> 现有文本-图像到视频生成模型隐含假设输入图像与文本在语义上严格配对且时间对齐，导致在真实场景中常见的“非配对”输入下生成结果语义断裂。本文提出ReasonDiff，利用多模态大语言模型推理非配对输入的潜在时序关系，并通过专用模块将推理信号注入生成过程。该方法在自建非配对数据集上显著提升了文本语义对齐度，但其对配对数据上的增益来源及推理模块的泛化边界尚存疑。

## 研究背景

视频生成模型通常依赖扩散过程在潜在空间逐步去噪，其中Flow Matching范式通过学习速度场将高斯噪声映射至数据分布，成为当前DiT架构的主流训练目标。然而，这一过程高度依赖条件信号与目标帧的时空一致性。当条件图像并非视频首帧，且其语义与文本描述存在时间错位时，模型缺乏推断两者内在因果或时序联系的能力，导致生成视频出现元素混杂或逻辑缺失。

主流T2V方法如CogVideoX和Wan2.1均建立在“配对”假设之上，即图像作为首帧或关键帧，文本描述与之同步发生。这种假设在用户提供的图像与文本来自不同时间点或不同事件时失效，例如文本描述“猫在房间玩耍”而图像为“破碎的花瓶”，模型无法推断花瓶破碎是猫玩耍的结果，也无法定位图像在视频中的合理位置。现有提示词优化方法仅扩展文本细节，未解决跨模态时序对齐问题。ReasonDiff针对这一测试时分布外（OOD）场景，首次提出通过外部推理机制重建非配对输入的完整叙事场景。

## 核心方法

### 方法参照系

本文问题属于可控视频生成范畴，但区别于标准的图像到视频（I2V）任务。标准I2V流程中，条件图像固定为第一帧，文本描述与图像内容同步。本文的关键差异在于条件图像位置未知且语义与文本非同步，要求模型在生成前推断图像在视频序列中的索引及逐帧语义演变。

### VisionNarrator：跨模态时序推理

VisionNarrator模块旨在解决非配对输入中语义关联缺失的问题。传统方法直接将图像嵌入与文本嵌入拼接，导致模型无法区分图像是起始状态还是结束状态。本文利用多模态大语言模型（MLLM）的推理能力，输入非配对的图像和文本，要求MLLM估计图像在$f$帧视频中的最可能位置$j$，并生成逐帧描述序列。该模块不直接参与像素生成，而是输出结构化的叙事脚本，将隐式的时序关系显式化为文本序列，为后续生成提供语义骨架。

### AlignFormer：推理信号注入

AlignFormer负责将VisionNarrator输出的文本叙事转化为潜在空间特征，以指导去噪过程。其核心是Multi-stage Temporal Anchor Attention（MTAA）机制。该机制将条件图像特征$c_i$作为Query，将逐帧叙事嵌入$h_j$作为Key和Value，通过交叉注意力预测非条件帧的潜在表示$c_j^*$。公式如下：

$$
c_j^* = \text{Softmax}\left(\frac{W_Q \tilde{c}_i (W_K \tilde{h}_j)^T}{\sqrt{d}}\right) W_V \tilde{h}_j
$$

其中$\tilde{c}_i$和$\tilde{h}_j$分别添加了时间位置编码。这一设计使得条件图像作为“锚点”，通过注意力机制将叙事语义扩散至其他帧，实现了帧级别的细粒度控制。训练阶段引入辅助重建损失，确保预测的潜在表示与真实潜在表示对齐：

$$
\mathcal{L} = \mathbb{E} \left[ ||u_{\theta}(x_t, h, c^*) - v(x_t)||_2^2 + \beta \cdot ||c^* - c||_2^2 \right]
$$

其中$\beta=0.2$，该损失仅在微调AlignFormer时启用，避免干扰基础模型的Flow Matching目标。

## 实验评估

实验在自建ActivityNet非配对数据集和公开MSR-VTT配对数据集上进行。基线包括Dynamicrafter、LTX-Video、CogVideoX和Wan2.1，覆盖了当前主流的开源视频生成模型。在ActivityNet上，ReasonDiff在CLIP Score (Text)上取得0.261，显著高于最佳基线Wan2.1的0.224，提升16.5%；User Rank从2.692降至1.743，表明用户偏好度更高。在MSR-VTT上，ReasonDiff的CLIP Score (Text)为0.214，同样优于Wan2.1的0.191。

| 数据集 | 方法 | CLIP Score (Text) | User Rank |
| :--- | :--- | :--- | :--- |
| ActivityNet | Wan2.1 | 0.224 | 2.692 |
| ActivityNet | ReasonDiff | 0.261 | 1.743 |
| MSR-VTT | Wan2.1 | 0.191 | 2.743 |
| MSR-VTT | ReasonDiff | 0.214 | 1.769 |

消融实验显示，移除辅助损失或逐帧叙事均导致性能下降，验证了推理信号注入的必要性。然而，论文未报告置信区间，且ActivityNet数据集为自建，规模有限，限制了统计显著性的判断。

评估指标主要依赖CLIP Score，该指标对语义对齐敏感，但无法完全捕捉时序逻辑的连贯性。论文未提供代码开源链接，且MLLM推理引入额外延迟，未讨论实时性影响。

## 关联研究分析

从问题动机看，ReasonDiff与LayoutGPT等利用LLM生成布局的方法不同。LayoutGPT聚焦空间布局的生成，而ReasonDiff聚焦时序位置的推断。这种差异源于任务特性：I2V生成中，空间布局通常由首帧决定，而时序关系在非配对场景中是缺失的关键信息。ReasonDiff通过MLLM推断图像位置，解决了传统方法无法处理时间错位的问题。

从方法设计看，ReasonDiff与Kaleido等主体一致性方法存在交叉。Kaleido通过参考图像保持身份一致，而ReasonDiff通过叙事保持语义一致。两者均利用外部信息引导生成，但ReasonDiff的AlignFormer模块将文本叙事转化为潜在特征，而非直接注入图像特征。这种设计使得ReasonDiff能够处理更复杂的语义演变，但依赖于MLLM推理的准确性。若MLLM推断错误，生成视频将偏离预期，这一风险在论文中未充分讨论。

## 总结

ReasonDiff针对非配对文本-图像到视频生成中的语义断裂问题，通过VisionNarrator推断时序关系，AlignFormer注入推理信号，在ActivityNet上将CLIP Score (Text)提升16.5%。其边界在于依赖MLLM推理的准确性，且自建数据集规模有限，未验证在大规模真实OOD场景下的泛化能力。当MLLM对复杂因果关系的推断出现偏差时，AlignFormer的注意力机制是否会产生错误的潜在表示，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_2d4da8ec327f)