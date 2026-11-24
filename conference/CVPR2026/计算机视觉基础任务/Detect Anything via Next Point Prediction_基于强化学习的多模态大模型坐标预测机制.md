# CVPR2026最新论文 ｜Detect Anything via Next Point Prediction ｜基于强化学习的多模态大模型坐标预测机制

作者：Qing Jiang、Junan Huo、Xingyu Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12798)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12798)

> 开放词汇检测长期受限于传统回归检测器浅薄的语言理解能力，难以处理复杂语义描述；而多模态大语言模型（MLLMs）虽具备强语言推理能力，却因离散坐标预测与连续几何空间的优化失配，导致定位精度远低于回归模型。本文切入点在于识别出MLLM定位失效的两个根源：离散token映射连续像素的学习难度，以及监督微调（SFT）教师强制机制引发的训练-推理行为不匹配。通过量化相对坐标特殊token、大规模数据引擎及SFT+GRPO两阶段训练，Rex-Omni在3B规模下实现了与传统检测器竞争力的零样本定位精度。其价值在于统一了感知任务框架，但GRPO对坐标精度的直接增益有限，主要收益来自行为修正，这一发现对MLLM检测器的训练范式具有启发意义。

## 研究背景

当检测器面对“戴红帽子的狗”这类复杂描述时，传统开放词汇检测器（如Grounding DINO）依赖CLIP等视觉-语言模型（VLMs）进行特征对齐，但其语言理解深度有限，往往忽略修饰语，导致检测所有苹果而非仅红苹果。这一局限源于VLMs的浅层语义解析能力，而MLLMs凭借底层大语言模型（LLMs）的强推理能力，理论上能精准解析此类描述。然而，MLLMs将坐标预测视为离散分类任务，通过交叉熵损失监督绝对坐标token，这种离散-连续映射的学习难度远高于回归模型的L1或GIoU损失，导致定位精度显著落后。

开放词汇检测的主流路线分为回归检测器与MLLM检测器。回归检测器（如DINO, Grounding DINO）通过连续几何损失实现高精度定位，但缺乏复杂语义理解；MLLM检测器（如SEED1.5-VL, Qwen2.5-VL）具备语言优势，却受困于低召回率、坐标漂移及重复预测。现有MLLM方法多采用SFT进行教师强制训练，模型在训练中始终依赖真值前缀，未暴露于自身潜在错误的预测中，导致自由推理时无法调节输出结构，产生异常坐标序列。Rex-Omni针对这一训练-推理不匹配及离散坐标优化难题，提出统一坐标预测框架与强化后训练机制。

## 核心方法

### 量化相对坐标表示

MLLM坐标预测的通用流程是将图像特征与文本提示输入LLM，通过Next-Token Prediction生成坐标序列。传统方法（如Qwen2.5-VL）采用绝对坐标，将像素值（如1921）分解为数字token，导致token长度长且学习空间无界。Rex-Omni采用相对坐标与特殊token策略，将坐标量化为0-999的离散值，每个值对应词表中一个专用特殊token。该设计将分类任务限制在1,000个有界类别内，降低学习复杂度；同时，单个边界框仅需4个token（对比无特殊token方案的15个），显著提升密集场景下的推理效率。

### 数据引擎与SFT+GRPO两阶段训练

SFT阶段通常使用大规模图文对训练模型基础定位能力，但教师强制机制导致模型无法学习自我纠错。Rex-Omni设计Grounding、Referring、Pointing等数据引擎，生成约8.9M公共数据与22M自动标注数据，用于SFT阶段。SFT后，引入基于组相对策略优化（GRPO）的强化后训练，使用三个几何感知奖励函数。GRPO通过采样多条轨迹并计算相对优势，更新策略以最大化几何精度并抑制重复预测。

$$
\mathcal{L}_{GRPO} = -\mathbb{E}_{x \sim \mathcal{D}, y \sim \pi_{old}} \left[ \min \left( \frac{\pi_{new}(y|x)}{\pi_{old}(y|x)} A(x,y), \text{clip}\left(\frac{\pi_{new}(y|x)}{\pi_{old}(y|x)}, 1-\epsilon, 1+\epsilon\right) A(x,y) \right) \right]
$$

该公式中，$A(x,y)$ 为基于几何奖励（如IoU、MAE）计算的相对优势，通过裁剪机制稳定策略更新，直接优化连续几何指标而非离散分类损失。

## 实验评估

实验在COCO、LVIS、VisDrone等基准上进行零样本评估，对比Grounding DINO、SEED1.5-VL、DINO等基线。基线覆盖回归检测器与MLLM检测器，但缺乏YOLO-World等轻量级实时检测器对比。

| 方法 | F1@IoU 0.5 | F1@IoU 0.95 | F1@mIoU |
| --- | --- | --- | --- |
| Rex-Omni | 72.0 | 34.6 | 58.8 |
| SEED1.5-VL | 72.6 | 19.9 | 57.8 |
| Grounding DINO | 71.1 | 34.6 | 58.8 |

Rex-Omni在mIoU指标上达到SOTA，F1@0.5与SEED1.5-VL持平，但F1@0.95显著优于SEED1.5-VL，表明其边界框精度更高。

消融实验显示，GRPO对坐标精度的直接提升有限（Table 15），主要贡献在于消除重复预测（Table 13）和大框预测（Table 14）。SFT-Sampling-Vote在COCO上F1@0.5达72.6，超过GRPO的72.0，暗示SFT具备潜在精度，GRPO的核心价值在于行为稳定性而非精度上限。

评估指标以F1为主，缺乏AP指标与传统检测器的直接公平比较。代码开源，但GRPO训练需8 A100 GPU约24小时，计算成本较高。

## 关联研究分析

从问题动机看，Rex-Omni与Grounding DINO均解决开放词汇检测，但Grounding DINO依赖CLIP特征蒸馏与回归头，语言理解受限；Rex-Omni利用LLM推理能力处理复杂描述，但定位精度依赖强化学习修正。差异根源在于任务特性：回归检测器擅长几何优化，MLLM擅长语义解析，Rex-Omni通过GRPO弥合两者，但未探索CLIP骨干与LLM推理的融合。

从方法设计看，Rex-Omni与SEED1.5-VL同属MLLM检测器，但SEED1.5-VL采用绝对坐标与SFT，Rex-Omni采用相对量化坐标与SFT+GRPO。Rex-Omni的GRPO阶段针对SFT行为缺陷，而SEED1.5-VL未涉及强化学习。SEED1.5-VL在F1@0.5上略高，但Rex-Omni在F1@0.95和mIoU上显著领先，表明量化坐标与GRPO对高精度定位更有效。

## 总结

Rex-Omni旨在解决MLLM检测器语言理解强但定位精度低的矛盾，抓住离散坐标优化失配与SFT行为缺陷两个关键点。通过量化相对坐标特殊token降低学习难度，利用数据引擎提供大规模监督，采用SFT+GRPO两阶段训练修正行为偏差。实验证明其在mIoU指标上达到SOTA（58.8），F1@0.95显著优于SEED1.5-VL。其边界在于GRPO对坐标精度的直接增益有限，主要收益来自行为修正，且缺乏AP指标与传统检测器的公平比较。当支持集增大时，SFT-Sampling-Vote的精度超过GRPO，暗示SFT具备潜在精度，GRPO的必要性是否随数据规模变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12798)