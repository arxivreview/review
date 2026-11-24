# CVPR2026最新论文 ｜Accelerating Streaming Video Large Language Models via Hierarchical Token Compression ｜流式视频大语言模型的分层Token压缩

研究机构：上海交通大学、华中科技大学

作者：Yiyu Wang、Xuyang Liu、Xiyan Gui 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.00891)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00891)

> 流式视频理解要求模型在帧连续到达时实时响应，但现有视频大语言模型（VideoLLM）因视觉Transformer（ViT）编码与LLM预填充的双重计算瓶颈，无法满足低延迟部署需求。现有Token压缩方法多假设离线全视频可见或依赖未来用户指令，在因果流式约束下失效。本文提出STC框架，通过ViT内部特征缓存复用与LLM前双锚点剪枝，在保持语义完整性的同时降低延迟。该框架在ReKV上保留99%准确率并降低45.3%预填充延迟，但其精度增益依赖于特定的缓存间隔与复用率超参数，在极端动态场景下的泛化能力存疑。

## 研究背景

流式视频理解（Streaming Video Understanding, SVU）的核心困境在于计算延迟与实时性的矛盾。当视频帧以0.5fps连续输入时，每帧需独立经过ViT编码生成视觉Token，再进入LLM进行自回归推理。ViT编码占推理总时间的59%-70%，是图像理解的2-3倍；32帧视频产生6,272个视觉Token，远超图像任务的1,900个，导致LLM预填充阶段自注意力复杂度呈二次方增长。这种双重瓶颈使得现有VideoLLM在直播解说、AR眼镜等毫秒级延迟场景中无法部署。

现有Token压缩方法分为离线与流式两类。离线方法如ToMe在ViT层内合并相似Token，但破坏了编码过程，导致流式场景性能下降；VidCom2等依赖全局视频特征选择Token，无法在帧未完全到达时决策。流式方法如TimeChat-Online基于相邻帧相似度丢弃Token，但仅捕捉短程冗余，保留大量重复内容。这些方法共同忽略了流式场景的两个关键特性：ViT编码中相邻帧特征的高度时间冗余（深层余弦相似度达0.85），以及模型无法预知完整视频与用户指令的因果约束。STC的切入点在于，将压缩从单一LLM端扩展至ViT编码端，设计因果无关的双阶段加速框架，在不依赖未来信息的前提下联合优化两个阶段的延迟。

## 核心方法

### 方法参照系

标准VideoLLM流式推理将视频分为长度为L的块，每块经ViT编码为Token序列$Z_c \in \mathbb{R}^{L \times N \times D}$，投影后输入LLM，KV状态缓存于记忆库$M$以维持时序一致性。该流程的关键差异在于：现有压缩方法仅在LLM端操作，忽略了ViT编码阶段的重复计算冗余，且多数依赖全局上下文或用户查询，违背流式因果约束。

### STC-Cacher：ViT选择性重计算

STC-Cacher在ViT编码阶段引入缓存复用机制，解决相邻帧静态内容重复计算的问题。对于参考帧$f_{ref}$，执行完整前向传播并缓存各层中间表示$C_{ref}^{[l]}$。对于非参考帧$F_{new}$，计算当前Key投影$K_{curr}^{[l]}$与缓存参考$K_{ref}^{[l]}$的余弦相似度，选取相似度最低的$k$个Token作为动态集$I_f$，其中$k = \lfloor T \cdot r \rfloor$，$r$由复用率$R_{Cacher}$决定。仅对动态Token计算Query与Key，通过散射更新（scatter-update）将新Key值插入缓存Key矩阵，再计算注意力输出并散射至缓存注意力矩阵。该机制将ViT计算量从全帧$N$个Token降至动态Token数$k$，在$R_{Cacher}=75\%$时仅计算25%的Token，显著降低编码延迟。

$$
S(z_j) = d_{cos}(z_j, a_{temporal}) \times d_{cos}(z_j, a_{spatial})
$$

该公式计算Token $z_j$ 的动态性得分，为STC-Pruner提供剪枝依据。

### STC-Pruner：双锚点显著性剪枝

STC-Pruner在LLM预填充前压缩Token序列，解决长上下文冗余导致的二次方计算开销。其核心是建立两个锚点：时间上下文锚点（Temporal Context Anchor, TCA）$a_{temporal} = \frac{1}{|H|}\sum_{h \in H} h$，为过去$W$帧Token均值的聚合；空间上下文锚点（Spatial Context Anchor, SCA）$a_{spatial} = \frac{1}{N}\sum_{i=1}^{N} z_i$，为当前帧Token均值。每个Token $z_j$ 的显著性得分$S(z_j)$为其到两个锚点的余弦距离之积，保留得分最高的Token。该设计同时捕捉帧内冗余（与SCA相似）与帧间动态（与TCA不同），避免了单一锚点导致的性能失衡。在$R_{Pruner}=75\%$时，序列长度压缩至25%，LLM预填充延迟降低45.3%。

## 实验评估

实验在OVO-Bench、StreamingBench、EgoSchema、MLVU-dev、VideoMME五个基准上评估，基线覆盖ToMe、VisionZip、VidCom2等Token压缩方法，但缺失InfoTok、VideoFlexTok等最新离散化器基线。主实验显示，STC-Cacher & Pruner在OVO-Bench上Overall得分52.0%，较VidCom2的50.4%提升1.6；在StreamingBench上Overall得分65.2%，较VidCom2的63.6%提升1.6。ViT编码延迟从103.7s降至78.3s（↓24.5%），LLM预填充延迟从482.4s降至263.7s（↓45.3%）。

| 方法 | OVO-Bench Overall | StreamingBench Overall | ViT Enc. Latency (s) | LLM Pref. Latency (s) |
| :--- | :--- | :--- | :--- | :--- |
| ReKV (ICLR25) | 50.4 | 63.6 | 103.7 | 482.4 |
| +VidCom2 (EMNLP25) | 50.4 | 63.6 | 103.7 | 259.1 (↓46.3%) |
| +STC-Pruner | 50.6 | 61.8 | 103.7 | 259.2 (↓46.3%) |
| +STC-Cacher & Pruner | 52.0 | 65.2 | 78.3 (↓24.5%) | 263.7 (↓45.3%) |

消融实验表明，STC-Cacher中复用Attention与MLP特征优于单独复用任一，验证了选择性重计算需保留位置与语义信息。STC-Pruner中联合使用SCA与TCA优于单独使用，单独SCA导致帧间新颖性缺失，单独TCA导致帧内冗余保留。余弦相似度作为动态性度量优于L1/L2距离，因其对特征尺度不敏感。

评估边界方面，实验未报告置信区间，数值比较需谨慎；超参数$N=4, R_{Cacher}=75\%$在OVO-Bench上最优，但在其他数据集上可能需调整；代码已开源，但GPU型号与训练细节未详述，可复现性受限。

## 关联研究分析

从问题动机看，STC与DyCoke均关注KV缓存压缩，但DyCoke侧重LLM端动态压缩，假设离线全视频可见；STC针对流式因果约束，将压缩扩展至ViT编码端，解决了DyCoke在帧未完全到达时无法决策的问题。这一差异源于任务特性：流式场景要求因果无关，而离线场景可利用全局信息。STC的双锚点设计比FastV的浅层注意力剪枝更适应流式约束，因FastV依赖模型内部注意力分数，而STC基于时空显著性，无需访问LLM内部状态。

从方法设计看，STC-Cacher与ToMe均操作于ViT层内，但ToMe合并相似Token导致信息丢失，STC-Cacher缓存复用静态Token并仅计算动态Token，保留了完整时序信息。这一改进源于对ViT编码冗余的精确量化：流式视频深层特征余弦相似度达0.85，远高于离线视频，使得缓存复用成为可能。STC-Pruner与VidCom2均压缩LLM输入序列，但VidCom2依赖全局视频特征，STC-Pruner基于因果锚点，无需未来帧信息。这种设计选择牺牲了全局最优性，换取了流式场景的实时性，其精度损失是否可接受，论文未给出明确阈值。

## 总结

STC解决的核心矛盾是流式视频理解中ViT编码与LLM预填充的双重计算瓶颈与实时性需求之间的冲突。现有方法因依赖全局上下文或用户指令，在因果约束下失效；STC通过ViT内部特征缓存复用与LLM前双锚点剪枝，在不依赖未来信息的前提下联合优化两个阶段。实验证明，STC在ReKV上保留99%准确率，降低45.3%预填充延迟，验证了分层压缩的有效性。其边界在于，超参数$N$与$R_{Cacher}$对性能影响显著，在极端动态场景下缓存复用可能导致信息丢失；双锚点设计假设时空冗余可分解，但复杂运动场景下的锚点稳定性未验证。当视频内容从静态背景主导转为高频动态变化时，STC-Cacher的缓存复用率是否需动态调整，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00891)