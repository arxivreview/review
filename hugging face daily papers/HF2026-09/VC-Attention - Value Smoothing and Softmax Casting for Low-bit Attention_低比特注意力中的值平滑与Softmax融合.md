# HuggingFace最新推荐论文 ｜VC-Attention: Value Smoothing and Softmax Casting for Low-bit Attention ｜低比特注意力中的值平滑与Softmax融合

研究机构：美国麻省理工学院、美国卡内基梅隆大学

作者：Xingyang Li、Dongyun Zou、Shining Zhang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.15810)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.15810)

> 视频扩散模型（Video Diffusion Models）在高分辨率长序列下，注意力计算占据推理时间的64%以上，而低比特量化虽能提升Tensor Core峰值吞吐，却因值张量（Value Tensor）异常值与Softmax标量路径瓶颈导致精度损失与速度停滞。现有低比特注意力方法仅优化查询-键（Query-Key, QK）乘积，忽视值乘积（PV）误差主导输出失真，且未解决指数运算阻塞流水线的问题。本文提出VC-Attention，通过在线聚类重排值Token并融合概率编码，以训练无关方式同时突破精度与速度瓶颈。该方法在B200上实现1.59倍注意力加速与20.2dB PSNR，但仅验证了四个特定模型，未覆盖稀疏注意力组合场景。

## 研究背景

视频扩散模型将潜空间视频展平为时空Token序列，每层执行全自注意力。当序列长度达到70K Token时，二次方复杂度使注意力成为计算主导项。低比特量化旨在利用Tensor Core的FP8/FP4峰值吞吐，但量化器为每个硬件块分配共享缩放因子，导致块内少数异常值（Outliers）固定缩放尺度，使其余Token有效位宽骤降。

视频DiT中，QK乘积的异常值可通过通道旋转或均值减法消除，但值张量的异常值无固定通道或时空模式，随头、层、去噪步动态变化。SageAttention2等方法仅平滑QK，导致PV误差占输出总误差的82%。同时，B200的Tensor Core吞吐翻倍，但MUFU单元指数运算速度未变，FP32指数与FP32-to-FP8转换成为最长流水线阶段，使低比特内核无法转化为实际加速。

本文切入点在于：值异常值需动态分组而非静态布局，Softmax标量路径需融合消除。VC-Attention通过在线K-means聚类重排值Token，使硬件块内均值有效，并设计ExpCast-FP8直接映射对数域分数至E4M3编码，绕过指数运算。

## 核心方法

### 低比特注意力量化参照系

标准低比特注意力将QK与PV乘积量化至INT8/FP8，通过FlashAttention内核流式计算。关键差异在于：现有方法假设值张量在序列顺序下块内共享组件，但视频DiT中值异常值分散于不同Token，静态布局下块均值仅移除8%能量，导致量化残差过大。

### V-Smooth：值引导Token平滑

V-Smooth针对值量化瓶颈，在FlashAttention内核中插入在线K-means聚类步骤。对每个批处理与头，计算值Token标签 $z_t$，生成置换 $\pi = \text{argsort}(z)$，同步重排K与V：

$$
K' = K[\pi], \quad V' = V[\pi], \quad P' = \text{softmax}\left(\frac{QK'^\top}{\sqrt{d}}\right)
$$

置换保持非因果自注意力输出不变，因 $P'V' = PV$。重排后，每个硬件块（128行）减去均值 $\mu_j = \frac{1}{B_v} V'_j^\top \mathbf{1}$，仅量化残差 $R_j = V'_j - \mathbf{1}\mu_j^\top$。设计动机在于：静态布局下块均值移除能量仅8%，而聚类后升至36%，使残差范数降低1.5倍，直接减少PV量化误差。

### ExpCast-FP8：融合概率编码

ExpCast-FP8针对Softmax瓶颈，将FP32指数与FP32-to-FP8转换融合为单次FMA运算。对对数域分数 $z$，计算：

$$
c = 8z + 56 + \beta, \quad \text{code} = \text{round}(\text{clip}(c, 0, 120)), \quad p_{\text{fp8}} = \text{view\_as\_e4m3}(\text{code})
$$

其中 $\beta = -0.35$ 为中心化常数。该公式将E4M3指数尺度、偏置与行最大值缩放折叠为线性映射，消除MUFU单元指数运算。行级误差界为3.64%加下溢尾部，实测204.8K行平均总变差1.6%，低于FP32指数路径的1.1%误差但无流水线阻塞。

## 实验评估

实验在Wan2.2、LongCat-Video、HunyuanVideo-1.5、MiniMax-H3四个视频DiT上评估，基线包括BF16 FlashAttention-4、SageAttention2、Attn-QAT。主结果如下：

| 硬件 | 精度 | 方法 | 注意力加速比 (vs BF16 FA-4) | PSNR (dB) |
| :--- | :--- | :--- | :--- | :--- |
| B200 | 8-bit | VC-Attention | 1.59× | 20.2 |
| B200 | 8-bit | SageAttention2 | 0.29× | 19.9 |
| H200 | 8-bit | VC-Attention | 1.46× | — |
| RTX 5090 | 4-bit | V-Smooth | 3.58× | — |

VC-Attention在B200上注意力加速1.59倍，PSNR 20.2dB，较SageAttention2的0.29倍与19.9dB显著提升。端到端生成Wan2.2片段在B200上加速1.19倍，RTX 5090上加速1.70倍。

消融显示，V-Smooth聚类开销占注意力时间16.5%，但仅在前1/4去噪步执行，整体开销可控。ExpCast-FP8融合后，MiniMax-H3上PSNR下降0.6dB，但速度提升5.5倍（vs SageAttention2）。设计决策验证表明，值聚类对精度贡献大于QK平滑，而ExpCast-FP8在速度-精度权衡中牺牲部分保真度换取流水线效率。

评估边界：未报告置信区间，未覆盖稀疏注意力组合场景，代码未开源。指标限于PSNR与加速比，缺乏时序一致性专项评测。

## 关联研究分析

从问题动机看，VC-Attention与SageAttention2均针对低比特注意力精度，但SageAttention2假设值张量静态布局下块内共享组件，而视频DiT中值异常值动态分布，导致其PV误差占82%。本文通过在线聚类解决动态性，根源在于视频Token的时空非均匀性，而非算法缺陷。

从方法设计看，VC-Attention与DeltaQuant均使用均值减法，但DeltaQuant固定时空立方体布局，仅移除12%能量；本文动态聚类移除36%能量。差异源于值异常值的无固定模式特性，静态布局无法适配。与FlashAttention-4相比，本文未改变内核结构，仅优化Softmax阶段，使其与稀疏注意力正交组合，但论文未验证组合效果。

## 总结

VC-Attention解决低比特注意力中值异常值精度损失与Softmax吞吐瓶颈的双重矛盾。现有方法仅优化QK，忽视PV误差主导性，且未解决指数运算阻塞；本文通过在线聚类重排值Token使块均值有效，并融合概率编码消除标量路径。在B200上实现1.59倍注意力加速与20.2dB PSNR，端到端加速1.19倍。边界在于仅验证四个模型，未覆盖稀疏注意力组合，且ExpCast-FP8在MiniMax-H3上牺牲0.6dB PSNR。当序列长度超过100K Token时，在线K-means聚类开销是否成为新瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.15810)