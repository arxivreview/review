# HuggingFace最新推荐论文 ｜X2SAM: Any Segmentation in Images and Videos ｜统一图像与视频像素级分割的多模态大语言模型

研究机构：中山大学、美团

作者：Hao Wang、Limeng Qiao、Chi Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.00891)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.00891)

> 现有多模态大语言模型（MLLMs）擅长全局语义理解，却难以生成像素级密集输出，而基础分割模型如SAM系列虽能生成高质量掩码，却依赖低层视觉提示且无法解析复杂对话指令。本文切入点在于构建一个统一框架，同时支持文本指令与视觉提示，覆盖图像与视频的多类分割任务。通过耦合LLM与Mask Memory模块，X2SAM实现了时序一致的掩码生成。该工作填补了图像与视频分割MLLM的结构碎片化空白，但其未采用强化学习训练，在复杂时序推理上的潜力存疑。

## 研究背景

当MLLMs处理视频时，其自注意力机制难以捕捉帧间细粒度的空间变化，导致像素级定位不准。这一局限源于视觉编码器多基于静态图像预训练，缺乏动态特征提取优化，使得模型在区分物体运动与相机运动时表现薄弱。为解决此问题，研究者引入显式时空建模机制，如时间门控或时空编码器，但现有分割MLLMs仍局限于单一模态：图像分割模型（如LISA）缺乏视觉提示支持，视频分割模型（如VISA）无法统一处理静态图像。

视频时间理解领域正从粗粒度问答向精确时空推理演进，核心矛盾在于模型依赖语言先验而非视觉证据，导致时间幻觉与逻辑不一致。主流路线通过强化学习（RL）与可验证奖励缓解过拟合，但计算成本高且训练不稳定。X2SAM的切入点在于绕过RL的复杂性，通过架构设计（Mask Memory）直接解决时序一致性，将任意分割范式从图像扩展至视频，支持文本与视觉提示的混合输入。

## 核心方法

### 方法参照系

本文问题属于时空联合理解架构，但关键差异在于：传统架构依赖LLM自注意力捕捉时序依赖，而X2SAM引入独立的Mask Memory模块存储引导视觉特征，实现帧间掩码一致性，同时支持文本与视觉提示的统一处理。

### Mask Memory模块

设计动机：独立帧解码导致视频掩码时序不一致，现有方法缺乏显式时序缓存机制。X2SAM在Mask Decoder前插入Mask Memory模块，其数据流包括：Memory Attention关注前K帧引导视觉特征，生成时序精炼特征$Z_w[t]$；Mask Decoder结合$Z_w[t]$与LLM生成的<SEG>嵌入$Z_p$，输出当前帧掩码$Y_m = g_\psi(Q_m, Z_w, Z_p)$；Memory Encoder编码下采样视觉特征与掩码logits，更新Memory Bank。该模块通过FIFO策略限制记忆容量（K=6），平衡计算成本与时间覆盖，解决独立帧解码的时序断裂问题。

### Region Sampler与Token-to-Image Attention

设计动机：视觉提示（如点、框）与文本指令的模态差异导致对齐失效，现有方法缺乏局部视觉提示的显式注入机制。X2SAM引入无参数Region Sampler，从Mask Encoder的高分辨率特征$Z_m$中点采样并自适应池化，生成区域级表示$H_r$；同时，Mask Decoder采用Token-to-Image Attention，将<SEG>嵌入$Z_p$转化为掩码查询$Q_m$，与视觉特征交互。公式$Y_m = g_\psi(Q_m, Z_w, Z_p)$中，$Q_m$直接注入语义条件，确保掩码空间准确且语义对齐，解决视觉提示与文本指令的混合输入对齐问题。

## 实验评估

实验设置覆盖COCO、RefCOCO、YT-VIS19等14个图像与视频分割基准，基线包括SAM2、X-SAM、PSALM等，但缺失ReferFormer-B等专用视频分割SOTA的完整对比。主结果显示，X2SAM在视频分割任务上优势显著：V-Ref. Seg.达78.5 J&F，优于UniPixel-7B的71.0；V-GCG Seg. mIoU 75.8，较VideoGLaMM提升21.5点。

| 任务 | 基准 | X2SAM | 对比基线 | 提升幅度 |
| :--- | :--- | :--- | :--- | :--- |
| V-Ref. Seg. | Ref-YT21-Val | 78.5 J&F | UniPixel-7B 71.0 J&F | +7.5 |
| V-GCG Seg. | V-GLaMM | 75.8 mIoU | VideoGLaMM 54.3 mIoU | +21.5 |
| I-OV Seg. | ADE20K | 31.2 PQ | X-SAM 20.9 PQ | +10.3 |
| V-VGD Seg. | YT-VIS19 Box | 74.4 AP | SAM2-H 54.0 AP | +20.4 |

消融实验表明，Mask Encoder特征优于Vision Encoder特征（I-Int. mIoU从64.7%提升至66.2%），且K=4的局部核优于全局聚合（K=∞），验证了Region Sampler的局部性设计。然而，Mask Memory容量K=6与K=8的差异未显著影响性能，暗示FIFO策略在长程依赖建模上可能存在瓶颈。

评估边界：指标完备性覆盖PQ、mIoU、J&F等，但缺乏时序幻觉专项评估；评估协议遵循标准基准，但未控制骨干网络预训练贡献；可复现性良好，提供代码与超参数（32 H800 GPUs，LoRA r=128）。

## 关联研究分析

从问题动机看，X2SAM与TempR1同属时空联合理解，但TempR1通过RL优化时序推理精度，而X2SAM依赖架构设计解决时序一致性。差异根源在于任务特性：TempR1聚焦时间定位的精确性，需过程奖励捕捉细粒度时序线索；X2SAM聚焦像素级分割的稳定性，Mask Memory的FIFO缓存足以应对帧间掩码一致性，无需RL的复杂优化。这一选择暗示，在分割任务中，架构设计的时序建模可能比RL更高效，但其在复杂时序推理（如因果链预测）上的有效性未验证。

从方法设计看，X2SAM与GroundVTS同属长视频高效推理，但GroundVTS通过查询引导Token采样保留关键时序线索，而X2SAM通过Mask Memory存储引导视觉特征。差异根源在于输入瓶颈的解决路径：GroundVTS针对均匀采样导致的关键帧丢失，采用过滤策略；X2SAM针对帧间掩码不一致，采用缓存策略。两者在“保留”与“增强”时序线索上形成互补，但X2SAM的FIFO策略是否限制了长程依赖建模，论文未给出回答。

## 总结

X2SAM要解决的核心矛盾是MLLMs像素级感知能力与基础分割模型指令解析能力的割裂。其切入点在于统一框架设计，通过Mask Memory与Region Sampler实现文本与视觉提示的混合输入处理，以及图像与视频分割任务的统一建模。实验证明，X2SAM在视频分割任务上表现强劲（V-Ref. Seg. 78.5 J&F，V-GCG Seg. 75.8 mIoU），但边界在于未采用RL训练，且在通用Chat任务上略低于纯Chat模型（如VideoMME 74.4% vs. Qwen3-VL 68.9%）。当视频时长超过Mask Memory容量K=6时，FIFO策略导致的长程依赖丢失是否显著影响掩码一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.00891)