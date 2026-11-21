# HuggingFace最新推荐论文 ｜VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization ｜视频灵活长度粗到细分词

研究机构：瑞士洛桑联邦理工学院

作者：Andrei Atanov、Jesse Allardice、Roman Bachmann 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12887)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12887)

> 视频建模的计算瓶颈源于原始像素信号的高维性，传统固定网格分词器迫使下游模型无论内容复杂度如何，均需预测全部低层细节，导致学习复杂度冗余。VideoFlexTok 通过引入可变长度、粗到细结构的Token序列，将抽象语义与运动信息前置，使下游生成模型仅需预测少量Token即可重建视频。该方法结合嵌套Dropout与生成式流解码器，在类到视频与文到视频任务中实现了数量级的计算效率提升。其价值在于解耦了表示复杂度与内容复杂度，但极端压缩下的时序一致性维持机制仍依赖启发式重叠帧策略。

## 研究背景

视频离散化器将高维像素映射为低维潜空间表示，是连接视觉数据与生成模型的关键接口。向量量化自编码器（Vector Quantization Variational Autoencoder, VQ-VAE）奠定了离散表示基础，但固定码本与固定压缩率难以应对动态内容变化。当视频内容从静态场景切换至剧烈运动时，固定网格分词器无法区分信息密度差异，导致静态区域Token浪费与动态区域信息不足并存。

主流视频分词器如VidTok FSQ与Cosmos-DV均采用时空3D网格结构，每个Token对应局部空间块，任何视频均被映射为相同数量的Token。这种设计假设所有视频具有均匀的信息分布，忽略了语义抽象层级与细节层级的非均匀性。下游自回归模型必须同时预测低层像素细节与高层语义结构，造成不必要的计算开销。VideoFlexTok的切入点在于打破固定网格约束，通过架构设计诱导Token的层级结构，使前几个Token捕获语义与运动，后续Token补充细节，从而允许下游模型根据需求截断序列。

## 核心方法

### 方法参照系

标准视频分词器流程为：编码器将视频映射为连续潜变量，量化器生成固定长度离散Token，解码器重建视频。VideoFlexTok的关键差异在于，其Token序列长度可变且具备粗到细的层级结构，而非固定网格的局部空间对应关系。

### 时间因果2D寄存器结构

传统1D扁平结构（如LARP）使用全自注意力，虽提升重建质量但破坏时序因果性，导致下游生成性能下降。VideoFlexTok采用时间因果2D寄存器结构，将视频潜变量与可学习寄存器Token沿时间维度交错，形成二维结构：第一维对应时间，第二维对应粗到细层级。编码器使用时间因果注意力掩码，确保当前帧Token仅关注过去帧，支持流式处理并提升生成性能。

$$
\text{Input Sequence} = [p_1, r_1, \dots, p_T, r_T]
$$

其中 $p_t$ 为第 $t$ 帧的VAE潜变量，$r_t$ 为第 $t$ 帧的寄存器Token。该结构保留了原始信号的时序因果性，使Token预测具备自监督预测目标，每个 $r_t$ 需编码当前帧重建信息及未来帧预测信息。

### 嵌套Dropout与语义偏置蒸馏

仅靠嵌套Dropout诱导层级结构时，重建目标偏向低层细节，导致初始Token缺乏语义信息。VideoFlexTok引入嵌套Dropout，随机丢弃每个寄存器序列末尾的 $K-k$ 个Token，强制模型在任意截断长度下均能重建视频。同时，采用REPA损失蒸馏DINOv2自监督特征，将语义信息注入早期Token。

$$
\mathcal{L}(\theta) = \mathcal{L}_{\text{Flow}} + \lambda \cdot \mathcal{L}_{\text{REPA}}
$$

其中 $\mathcal{L}_{\text{Flow}}$ 为整流流重建损失，$\mathcal{L}_{\text{REPA}}$ 为解码器早期层与DINOv2特征的余弦相似度损失。该设计使前几个Token涌现出语义与运动信息，后续Token补充细节，实现内容自适应压缩。

## 实验评估

| Tokenizer | # Tokens | rFVD (↓) | gFVD (↓) | Cls. Score (↑) |
| :--- | :--- | :--- | :--- | :--- |
| VidTok FSQ | 1280 | 84.1 | 131.7 | 0.799 |
| Cosmos-DV | 1280 | 220.5 | 187.6 | 0.825 |
| Omnitokenizer | 1280 | 63.6 | 102.6 | 0.858 |
| LARP | 1024 | 42.1 | 87.5 | 0.739 |
| VideoFlexTok | 5-1280 | 48.7 | 80.0 | 0.833 |

实验在Kinetics-600类到视频与Panda70M文到视频任务上进行，基线覆盖固定网格（VidTok, Cosmos-DV）与1D扁平结构（LARP, Omnitokenizer），但未对比InfoTok、TivTok等最新自适应分词器。VideoFlexTok在160 Token时gFVD为80.0，优于LARP的87.5，接近Omnitokenizer的102.6，同时Cls. Score达到0.833，表明语义对齐能力较强。

消融实验显示，1D扁平结构rFVD为48.9，优于时间因果2D结构的69.9，但gFVD为352.1，远差于2D结构的287.6。这表明1D结构虽提升重建质量，但破坏时序因果性导致生成性能显著下降。时间因果结构在生成任务上的优势源于其自监督预测目标，使Token具备更强的时序一致性。

评估指标包括rFVD、gFVD、Cls. Score与ViCLIP，侧重生成质量与语义对齐，但未报告计算效率的具体数值（如FLOPs、延迟）。代码已开源，但超参数与GPU配置未在摘要中详述，可复现性依赖完整技术报告。

## 关联研究分析

从问题动机看，VideoFlexTok与InfoTok均解决固定压缩率与内容动态性的矛盾，但InfoTok依赖信息熵估计动态调整Token数量，而VideoFlexTok通过架构设计诱导层级结构，放弃信息论严谨性换取训练简化。InfoTok在长视频序列缩短上更具理论优势，但计算开销较高；VideoFlexTok在生成任务中验证了层级结构对计算效率的提升，但未在理解任务中对比。

从方法设计看，VideoFlexTok与FlexTok共享寄存器Token与嵌套Dropout机制，但FlexTok聚焦图像域，VideoFlexTok扩展至视频域并引入时间因果结构。与LARP相比，VideoFlexTok的时间因果2D结构在生成任务上显著优于1D扁平结构，根源在于时序因果性对自回归预测的必要性。LARP的全自注意力虽提升重建质量，但破坏了Token间的时序依赖，导致下游生成性能下降。

## 总结

VideoFlexTok解决的核心矛盾是固定网格分词器中信息密度与Token数量的非匹配问题。其切入点在于通过嵌套Dropout与时间因果结构诱导粗到细层级，使前几个Token捕获语义与运动，后续Token补充细节，从而允许下游模型截断序列。该方法在Kinetics-600上以160 Token实现gFVD 80.0，优于LARP的87.5，验证了层级结构对生成效率的提升。其边界在于极端压缩（如1-4 Token/帧）时对齐性能饱和，且长视频时序一致性依赖重叠帧启发式策略。当Token数量降至1-4/帧时，生成视频的时序连贯性是否仍能维持，论文未给出定量回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12887)