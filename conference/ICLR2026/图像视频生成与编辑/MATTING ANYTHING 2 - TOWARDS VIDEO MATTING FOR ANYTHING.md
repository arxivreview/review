# 南大等提出MAM2：基于SAM2双模解码器，解决透明物体视频抠图时序崩溃难题

研究机构：南京大学、北京交通大学

作者：Chenyi Zhang、Yiheng Lin、Yunchao Wei 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69754992)

> 导读 视频抠图旨在从动态序列中精确提取前景Alpha Matte，其核心难点在于处理透明物体时，传统掩码引导机制导致的时序预测崩溃。现有方法多局限于人像领域，且依赖难以获取的首帧高质量掩码，无法泛化至自然场景。本文基于SAM2架构，提出双模解码器与记忆分离孪生机制，实现了对任意物体的交互式视频抠图。该方法在自然物体基准上显著优于现有SOTA，但其在极端透明场景下的计算开销与长序列稳定性仍存疑。

## 研究背景

视频抠图任务要求模型在仅获得首帧用户提示的情况下，预测整个视频序列中前景物体的Alpha通道。这一过程依赖于对物体边界与透明度的精确感知，而Alpha Matte的预测通常需要一个中间表示——Trimap（修剪图），它定义了前景、背景及未知区域。Trimap为后续精细的Alpha预测提供了强结构先验，是连接粗分割与高精度抠图的关键桥梁。

当前视频抠图研究面临两大瓶颈：领域特定性与掩码依赖。主流模型如MatAnyone主要聚焦于人像，缺乏对植物、火焰等自然场景物体的泛化能力。同时，半监督视频目标分割（VOS）框架要求用户提供首帧掩码，但对于烟雾、气泡等透明物体，像素级掩码的获取极具挑战性。本文切入点在于利用SAM2的交互式提示能力（点、框、掩码）替代单一掩码输入，并解决透明物体在时序传播中Trimap预测不稳定的问题。

## 核心方法

### 方法参照系

标准视频抠图流程通常包含两阶段：首帧掩码/Trimap预测与后续帧传播。本文基于SAM2的Transformer架构，继承其记忆机制以处理时序依赖，但关键差异在于将解码器改造为同时输出Mask与Trimap，并引入机制隔离记忆干扰。

### Promptable Dual-mode Decoder (PDD)

PDD旨在解决简单并行分支预测Trimap时产生的边界锯齿噪声。设计动机在于利用SAM2稳定的Mask预测作为语义引导，增强Trimap解码的鲁棒性。PDD将预测的Mask经Sigmoid归一化后通过卷积层生成“Mask增强特征”，该特征与分割特征、Trimap特征拼接，经轻量融合模块处理后，与Trimap输出Token点积得到最终Trimap。

$$ T[t] = \text{Dot}(\text{Fusion}(F_{seg}, F_{trimap}, \text{Conv}(\sigma(M[t]))), \mathbf{t}_{trimap}) $$

此公式表明，Trimap预测并非独立进行，而是被Mask预测动态调制，从而继承了Mask的语义稳定性。

### Memory-Separable Siamese (MSS)

MSS针对透明物体在后续帧中Trimap“未知”区域被误判为“前景”的时序崩溃问题。设计动机在于SAM2的记忆机制将前帧Mask嵌入当前帧图像特征，这种嵌入导致特征空间偏移，干扰了Trimap解码。MSS采用递归策略：第一遍PDD预测Mask；第二遍PDD利用第一遍预测的Mask作为提示，但关键地使用**未嵌入记忆**的预保存图像特征进行Trimap解码。

$$ T[t] = f_{PDD}(F[t]_{non-mem}, M[t-1]) $$

该公式强调，第二遍解码绕过了记忆注意力机制，直接使用原始图像特征，从而消除了Mask记忆对Trimap预测的干扰。由于两遍共享参数，MSS不增加额外参数量。

## 实验评估

实验在NOVM（自然物体）、YoutubeMatte（人像）及VM240K上进行，基线包括MatAnyone、TCVOM、FTP-VM等。MAM2在NOVM上将MAD从39.44降至14.72，在YoutubeMatte上将MAD从2.05降至1.16，表明其在自然物体与人像场景均具优势。

| 方法 | 提示类型 | NOVM MAD↓ | YoutubeMatte MAD↓ |
|---|---|---|---|
| MatAnyone | Mask | 39.44 | 2.05 |
| MAM2 | Mask | 14.72 | 1.16 |
| MAM2 | Box & Point | 15.19 | 1.16 |

消融实验显示，PDD相比并行结构在NOVM上MAD降低24%，在YoutubeMatte上降低29%。MSS相比记忆一致孪生（MCS）进一步降低了透明物体的预测误差，验证了“无记忆特征”对Trimap稳定性的关键作用。

评估边界方面，NOVM数据集虽涵盖多样自然物体，但标注质量对透明细节的精细度支撑有限。代码已开源，训练使用44.7M可训练参数，LoRA秩为16，优化器为AdamW。

## 关联研究分析

从问题动机看，MAM2与MatAnyone均基于SAM2，但MatAnyone依赖首帧Mask，而MAM2支持Box/Point提示，解决了透明物体掩码获取难的问题。根源在于MAM2引入了Trimap作为中间表示，使得粗提示（Box）也能通过PDD生成高质量Trimap，进而驱动Alpha预测。

从方法设计看，MAM2与SEMatte（图像抠图）均使用并行分支预测Trimap，但SEMatte未解决时序记忆干扰。MAM2的MSS机制是视频任务特有的创新，源于视频时序传播中记忆嵌入对特征空间的扭曲。这种扭曲在图像任务中不存在，因此MSS无法直接迁移至静态图像抠图，但其“特征隔离”思想可能启发其他时序任务中的记忆管理策略。

## 总结

MAM2解决的核心矛盾是透明物体视频抠图中，掩码引导的时序传播与Trimap预测稳定性之间的冲突。其切入点在于识别出SAM2记忆机制对Trimap解码的干扰，并通过MSS机制隔离该干扰。方法上，PDD利用Mask引导Trimap预测，MSS通过无记忆特征二次解码确保时序一致性。实验证明其在NOVM上MAD 14.72，YoutubeMatte上MAD 1.16，显著优于SOTA。边界在于，MSS的双遍解码增加了计算开销，且NOVM数据集的透明物体标注精度可能限制了性能上限。当视频序列长度超过数百帧时，MSS的递归特征保存是否会导致内存溢出或精度衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69754992)