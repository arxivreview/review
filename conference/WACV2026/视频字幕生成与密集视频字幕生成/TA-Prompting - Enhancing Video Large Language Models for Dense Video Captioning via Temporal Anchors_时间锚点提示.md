# WACV2026最新论文 ｜TA-Prompting: Enhancing Video Large Language Models for Dense Video Captioning via Temporal Anchors ｜时间锚点提示

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Wei-Yuan Cheng、Kai-Po Chang、Chi-Pin Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02908)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02908)

> 密集视频字幕生成（Dense Video Captioning, DVC）要求模型在未修剪长视频中同时定位事件并生成描述，核心矛盾在于计算资源受限与细粒度时空对齐需求之间的张力。现有VideoLLM依赖文本时间标记，易受语言先验干扰导致时间戳幻觉，本文切入点是将时间定位解耦为独立模块，通过数值时间锚点直接约束生成。方法采用两阶段训练：先训练事件定位器预测归一化时间中心与跨度，再以此作为提示引导LLM生成连贯字幕。该方案在事件定位精度上具有竞争力，但字幕质量显著落后于SOTA，且未解决长视频计算瓶颈。

## 研究背景

当VideoLLM处理长视频时，其有限的上下文长度限制了多事件建模能力。传统方法使用文本token表示时间（如"0-5s"），但LLM倾向于依赖语言先验而非视觉输入，导致生成的时间戳与视频内容错位。这种时间接地（Temporal Grounding）失效直接破坏了字幕的时空一致性，使得模型无法准确区分语义相似的事件边界。

DVC任务要求模型预测事件集合 $\mathcal{E} = \{e_i\}_{i=1}^N$，其中每个事件 $e_i = (t_i^{start}, t_i^{end}, c_i)$ 包含起止时间戳与字幕文本。早期PDVC（Wang et al., 2021）基于DETR风格架构实现了端到端集合预测，但各事件字幕独立生成，缺乏叙事连贯性。VTimeLLM（Cheng et al., 2024）与TimeChat（Yao et al., 2024）通过引入时间感知指令微调提升了时间敏感性，但文本时间标记仍易引发幻觉。本文针对这一失效，提出将时间定位与字幕生成解耦，通过数值时间锚点替代文本标记，从源头抑制语言先验偏差。

## 核心方法

### 方法参照系

本文问题属于DVC中的时间接地子任务。标准流程为：视觉编码器提取特征→LLM生成字幕。关键差异在于本文在LLM前插入事件定位器，将时间定位从隐式文本生成转变为显式数值预测，形成"定位-提示-生成"的三阶段架构。

### 时间锚点预测

事件定位器 $\theta_E$ 采用轻量级Transformer解码器，包含 $M$ 个可学习事件查询，通过交叉注意力机制与视频特征交互，输出归一化时间锚点 $\hat{Y} = \{(\hat{c}_i, \hat{d}_i)\}_{i=1}^M$，其中 $\hat{c}_i$ 为时间中心，$\hat{d}_i$ 为跨度，均归一化至 $[0, 1]$。设计动机是解决文本时间标记的离散化误差与语言先验干扰。锚点损失定义为：

$$
\mathcal{L}_{anchor} = \lambda_1 \mathcal{L}_{seg} + \lambda_2 \mathcal{L}_{span}
$$

其中 $\mathcal{L}_{seg}$ 为 $L_1$ 损失，惩罚锚点中心与真值的绝对偏移；$\mathcal{L}_{span}$ 基于IoU概念，最大化预测跨度与真值的重叠。匈牙利匹配算法用于配对 $M$ 个预测锚点与 $N$ 个真值事件（$M > N$），确保每个真值事件匹配到最优预测。该损失函数直接约束时间边界精度，避免了文本生成中的语义漂移。

### 时间感知字幕生成

时间锚点通过时间嵌入层 $\theta_T$ 转换为LLM token嵌入，作为提示注入LLM。设计动机是解决独立事件字幕缺乏叙事连贯性的问题。LLM输出预测时间戳 $\tilde{Y}$ 与字幕 $\hat{C}_i$，训练采用双重损失：

$$
\mathcal{L}_{denoise} = \lambda_1 \mathcal{L}_{seg}(\tilde{Y}, Y) + \lambda_2 \mathcal{L}_{span}(\tilde{Y}, Y)
$$

$$
\mathcal{L}_{caption} = -\sum_{i=1}^N \log P(C_i | v, \hat{Y})
$$

$\mathcal{L}_{denoise}$ 鼓励LLM从含噪锚点中恢复精确时间戳，强化时间接地能力；$\mathcal{L}_{caption}$ 为标准交叉熵损失，确保字幕质量。推理阶段引入事件连贯采样（ECS），通过评分函数 $S = S_{cs} + \alpha S_{as}$ 选择高置信度事件字幕，其中 $S_{cs}$ 为LLM生成置信度，$S_{as}$ 为视觉-文本对齐分数。该策略解决了任意数量事件下的序列连贯性问题，确保全局叙事一致性。

## 实验评估

实验在ActivityNet Captions与YouCook2上进行DVC评估，在ActivityNet与Charades-STA上进行时刻检索（Moment Retrieval），在ActivityNet-RTL上进行时间问答（TemporalQA）。基线覆盖VTimeLLM、TimeChat、LITA、VTG-LLM等时间感知VideoLLM，但缺失Sali4Vid等显著性重加权方法。

| 方法 | ActivityNet CIDEr | YouCook2 CIDEr | ActivityNet F1 | YouCook2 F1 |
|---|---|---|---|---|
| VTimeLLM-7B | 27.6 | 13.4 | 39.8 | - |
| VTG-LLM-7B | 28.6 | 8.6 | 39.8 | - |
| TA-Prompting-7B | 29.2 | 15.6 | 40.7 | 34.1 |

TA-Prompting在ActivityNet CIDEr上达到29.2，较VTimeLLM提升1.6；YouCook2 CIDEr为15.6，较VTimeLLM提升2.2。事件定位F1在ActivityNet上达40.7，较VTimeLLM提升0.9。YouCook2 F1为34.1，显著高于VTimeLLM的未报告值。

| 配置 | SODA_c | CIDEr | METEOR |
|---|---|---|---|
| Full | 6.1 | 29.2 | 7.0 |
| w/o ECS | 5.9 | 27.0 | 6.9 |
| w/o ECS & TA | 5.7 | 26.7 | 6.7 |

移除ECS导致CIDEr下降2.2，移除时间锚点（TA）进一步下降0.3，表明ECS对叙事连贯性贡献最大，时间锚点提供基础时间接地。ECS权重 $\alpha=1/5$ 时性能最优，CIDEr达29.2，$\alpha=1$ 时降至28.7，显示视觉-文本对齐比生成置信度更重要。

评估协议使用CIDEr、METEOR、SODA_c在多个IoU阈值（0.3, 0.5, 0.7, 0.9）上平均，SODA_c直接衡量序列级连贯性。可复现性方面，论文提供完整超参数（ActivityNet 10 queries, YouCook2 50 queries, 512维交叉注意力），训练在单张RTX-3090 GPU上完成，但未提供代码URL。

## 关联研究分析

从时间表示方式看，VTimeLLM与TimeChat使用文本token表示时间，本文改用数值时间锚点。差异根源在于文本标记的离散化误差：文本"0-5s"无法精确表达边界，而数值锚点 $(c, d)$ 可直接约束连续时间空间。VTimeLLM在ActivityNet CIDEr上为27.6，本文29.2，提升1.6，验证了数值表示的精度优势。但本文YouCook2 CIDEr仅15.6，远低于Sali4Vid的68.63（据领域综述），差距源于骨干网络差异：本文使用ViT-L/14提取全局特征，Sali4Vid采用显著性重加权突出关键帧，本文未解决长视频关键信息稀释问题。

从定位-生成耦合方式看，PDVC采用端到端集合预测，定位与生成联合优化；本文解耦为两阶段，先定位后生成。差异根源在于叙事连贯性：PDVC各事件字幕独立生成，缺乏序列依赖；本文通过ECS在推理阶段选择连贯事件序列，ActivityNet F1达40.7，较PDVC未报告值具有竞争力。但解耦架构牺牲了联合优化的全局性，YouCook2 CIDEr 15.6低于PDVC的未报告值，表明解耦在复杂场景下可能损失局部细节捕捉能力。

## 总结

本文要解决的核心矛盾是VideoLLM时间接地失效导致的字幕时空错位。切入点是将时间定位解耦为独立模块，通过数值时间锚点替代文本标记，从源头抑制语言先验偏差。方法采用两阶段训练：事件定位器预测归一化时间中心与跨度，时间嵌入层将其转换为LLM提示，ECS在推理阶段选择连贯事件序列。实验证明ActivityNet CIDEr达29.2，事件定位F1达40.7，较VTimeLLM分别提升1.6与0.9。边界在于YouCook2 CIDEr仅15.6，显著落后于Sali4Vid的68.63，且未解决长视频计算瓶颈，仍依赖ViT-L/14全局特征提取。当视频时长超过300秒时，数值时间锚点的精度是否随序列长度增加而衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02908)