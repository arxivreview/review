# HuggingFace最新推荐论文 ｜PixelPrune: Pixel-Level Adaptive Visual Token Reduction via Predictive Coding ｜像素级预测编码剪枝

作者：Nan Wang、Zhiwei Jin、Chen Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.00886)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.00886)

> 视觉语言模型在处理高分辨率文档与GUI界面时，因像素级重复导致的计算冗余被现有语义级剪枝方法忽视。主流方案依赖ViT特征或注意力分数，需先执行前向传播才能决策，无法消除视觉编码器本身的二次方开销。PixelPrune利用无损压缩中的预测编码原理，在ViT之前直接移除像素完全相同的Patch，实现了全流水线加速。该方法在结构化场景中实现了近乎无损的精度保持与显著的效率提升，但其对非结构化自然图像的适用性存疑。

## 研究背景

高分辨率输入迫使视觉编码器处理海量Patch，其中大量区域为纯色背景或重复纹理。这种像素层面的精确重复构成了最底层的冗余源，但传统视觉Transformer将其视为独立Token处理，导致计算资源浪费。为压缩序列长度，研究界发展出多种Token剪枝策略，核心在于确定哪些Token可被安全移除。

现有剪枝方法主要依赖语义或特征信号。FastV等Intra-LLM方法利用浅层注意力分数，VisionZip等Pre-LLM方法结合显著性评分与合并策略，这些方法均需先经过ViT或投影层计算得到特征向量，再基于特征相似度或重要性进行筛选。这种“先计算后剪枝”的范式存在固有局限：它无法降低ViT编码器自身的计算负载，而数据显示在高分辨率下ViT耗时占比高达86%。此外，固定剪枝比率难以适应不同图像的冗余程度，导致简单图像过度计算或复杂图像信息丢失。PixelPrune的切入点在于绕过特征计算，直接在像素空间识别冗余，将剪枝位置前移至ViT之前，从而加速整个推理链路。

## 核心方法

### 方法参照系

本文问题属于Pre-LLM剪枝范畴，但区别于依赖ViT特征的方法。标准流程是在视觉编码器后或LLM内部基于特征重要性剪枝，而本文在ViT输入前基于像素统计剪枝，关键差异在于无需前向传播即可确定保留子集，且具备像素级无损恢复保证。

### 预测编码剪枝机制

针对结构化图像中大量像素相同Patch的问题，PixelPrune引入预测编码（Predictive Coding）机制。扫描每个$M p \times M p$像素块时，利用已访问的因果邻居预测当前块内容。若预测值与真实值距离小于阈值$\tau$，则丢弃该块。默认$\tau=0$表示严格相等，确保无损。该设计解决了特征级剪枝需先计算ViT特征的瓶颈，直接利用像素冗余实现零开销决策。

$$
\text{omit}(P_{r,c}) \iff \text{dist}(P_{r,c}, \hat{P}_{r,c}) \le \tau
$$

其中$\hat{P}_{r,c}$为基于邻居$A, B, C$的预测值。当$\tau=0$时，仅当像素完全一致时丢弃，保证了信息零损失。

### 二维预测策略与位置保持

为捕获二维空间冗余，PixelPrune采用Pred-2D策略，从左侧$A$、上方$B$、左上$C$三个邻居中选择最可能的预测源。规则基于邻居间的一致性：若$B$与$C$相同，预测为$A$；若$A$与$C$相同，预测为$B$；否则默认$A$。该策略同时利用水平与垂直连续性，比一维Raster扫描捕获更多冗余。剪枝后保留的Patch保持原始2D坐标，通过2D RoPE和MRoPE确保空间布局在ViT和LLM中正确编码，避免了重索引导致的语义错位。

$$
\hat{P}_{r,c} = \begin{cases} A & \text{if } B=C \text{ or } A=C \text{ (default)} \\ B & \text{if } A=C \text{ and } B \neq C \\ \dots & \text{other cases} \end{cases}
$$

此规则通过邻居一致性判断目标块更可能跟随哪个方向，实现了二维冗余的高效压缩。

## 实验评估

实验在Qwen3-VL 2B/4B/8B模型上进行，覆盖DocVQA、ScreenSpot等文档与GUI基准。基线包括Full、Random、Resize和ConnComp，缺失FastV、VisionZip等特征级剪枝强基线，限制了与主流方法的直接对比。

| 模型 | 方法 | DocVQA | InfoVQA | ChartQA | Avg |
|---|---|---|---|---|---|
| Qwen3-VL-2B | Full | 92.7 | 72.3 | 78.8 | 69.2 |
| Qwen3-VL-2B | PixelPrune | 92.0 | 71.5 | 77.0 | 68.3 |
| Qwen3-VL-4B | Full | 94.8 | 79.5 | 82.9 | 74.1 |
| Qwen3-VL-4B | PixelPrune | 94.7 | 79.2 | 82.4 | 73.7 |

在文档基准上，PixelPrune在2B/4B/8B规模下平均准确率仅比Full低0.2-0.9个百分点，而保留率仅为23-50%。相比Resize，PixelPrune在4B规模下平均准确率更高（73.7 vs 72.8），证明其保留了分辨率缩放丢失的细节。GUI基准中，Training-free PixelPrune在ScreenSpot V2上达到90.6%（Full为90.6%），但在ScreenSpot Pro上存在差距，经知识蒸馏后恢复至47.6%（Full为50.2%）。

| 数据集 | 方法 | Retain (%) | TTFT Speedup | FLOPs Reduction |
|---|---|---|---|---|
| MML-Doc | Full | 100.0 | 1.0× | 1.0× |
| MML-Doc | PixelPrune | 50.3 | 3.0× | 3.5× |
| SS-Pro Sci. | Full | 100.0 | 1.0× | 1.0× |
| SS-Pro Sci. | PixelPrune | 26.2 | 4.2× | 6.6× |

消融实验显示，Pred-2D策略比Raster和Serpentine保留率更低且精度相当。ViT深度消融表明，在ViT前剪枝与在ViT后不同层剪枝精度差异不大，但ViT前剪枝节省100% ViT FLOPs，而ViT后剪枝仅节省0-96%。训练效率方面，PixelPrune实现2.0×前向/反向加速，峰值内存降低33.6%。

评估边界方面，实验仅覆盖文档和GUI结构化场景，未测试自然图像。代码已开源，使用8块H20 GPU，但缺乏置信区间报告，且未与量化等加速技术联合评估。

## 关联研究分析

从问题动机看，PixelPrune与ShowUI同属利用GUI空间冗余的方法，但ShowUI在ViT自注意力内部跳过Token，仍需执行ViT前向传播；PixelPrune在ViT前移除，加速范围覆盖整个流水线。这一差异源于对冗余本质的不同理解：ShowUI认为冗余体现在特征相似性，需计算特征判断；PixelPrune认为冗余体现在像素重复，可直接统计判断。在结构化图像中，像素重复是更确定且低成本的信号，但在非结构化图像中，像素重复率低，该假设可能失效。

从方法设计看，PixelPrune与ToMe同属Token压缩，但ToMe基于特征相似度合并，需ViT特征；PixelPrune基于像素相等性丢弃，无需特征。ToMe适用于通用图像，通过合并保留信息；PixelPrune适用于高冗余图像，通过丢弃消除冗余。两者互补：ToMe处理语义冗余，PixelPrune处理像素冗余。PixelPrune的无损恢复保证是其独特优势，但这也限制了其压缩率上限，仅能移除完全重复的Patch，无法处理近似重复。

## 总结

PixelPrune针对高分辨率文档与GUI场景中像素级冗余导致的计算浪费，提出在ViT前基于预测编码剪枝的方法。其核心在于利用像素精确重复这一底层冗余源，无需特征计算即可决策，实现了全流水线加速。实验证明在结构化场景中，该方法以23-50%的保留率维持了近乎无损的精度，并实现4.2×推理加速。其边界在于依赖像素重复假设，在自然图像中冗余率低时效果未知。当输入图像为非结构化自然场景时，像素级剪枝的压缩率与精度权衡如何变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.00886)