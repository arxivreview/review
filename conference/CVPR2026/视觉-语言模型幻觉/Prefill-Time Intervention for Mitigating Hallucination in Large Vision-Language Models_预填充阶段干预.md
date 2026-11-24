# CVPR2026最新论文 ｜Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language Models ｜预填充阶段干预

研究机构：中国科学技术大学、中国科学院

作者：Chengsheng Zhang、Chenghao Sun、Xinyan Jiang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.25642)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.25642)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉，现有解码时干预（DTI）方法虽能降低幻觉频率，却往往加剧剩余幻觉的严重程度，形成“雪崩效应”。本文指出，DTI在解码阶段连续、反应式地干预隐藏状态，导致初始错误在自回归过程中累积，且其模态无关的引导向量忽视了视觉与文本表征的敏感性差异。PTI将干预点前移至预填充阶段，通过模态感知的Key-Value（KV）缓存编辑，在错误累积前重塑初始状态。该范式在CHAIR等生成基准上表现优异，但在POPE等判别基准上未超越最新SOTA，其长序列生成后期的视觉信号衰减问题仍存疑。

## 研究背景

LVLMs的幻觉根源在于语言先验与视觉证据的冲突。当视觉输入模糊时，模型依赖文本共现关系而非视觉观察，导致生成不存在的物体。这一现象在自回归解码中尤为严重：初始token的微小偏差会通过注意力机制传播，影响后续所有token的生成，形成级联错误。理解这一过程需把握两个核心概念：一是KV缓存，它在预填充阶段存储初始表征，并在解码阶段为每一步注意力计算提供上下文；二是模态解耦，即视觉与文本信号在模型内部具有不同的敏感性和分布特性，需要差异化处理。

现有缓解幻觉的主流路线是解码时干预（DTI），如VCD和VISTA。这些方法通过对比原始与扰动输入的logits或隐藏状态，动态调整生成概率。然而，DTI存在三个根本局限：首先，干预时机滞后，作用于初始错误已经形成之后；其次，干预目标粗糙，主要作用于高层隐藏状态，难以纠正细粒度的视觉感知错误；最后，干预方式模态无关，使用统一的引导向量，忽视了视觉与文本表征的差异。这些局限导致DTI在降低幻觉频率的同时，可能加剧剩余幻觉的严重程度，即“雪崩效应”。PTI的切入点在于，将干预从解码阶段的连续校正，转变为预填充阶段的一次性状态塑形，从源头抑制错误累积。

## 核心方法

### 方法参照系

PTI属于推理时干预范式，但区别于DTI在解码阶段修改隐藏状态或logits，PTI直接操作预填充阶段生成的KV缓存。这一差异源于对幻觉累积机制的理解：DTI试图在错误发生后进行校正，而PTI旨在错误发生前重塑初始条件。

### 模态感知的方向提取

PTI的核心创新在于从视觉和文本模态中独立提取方向向量。对于视觉模态，利用MSCOCO的物体分割掩码，构建物体-only（$I_{pos} = I \odot M_{obj}$）和背景-only（$I_{neg} = I \odot (1 - M_{obj})$）的对比图像对。通过两次预填充前向传播，计算视觉token位置的Key和Value缓存差异，经平均池化和PCA去噪后，得到视觉Key方向 $S_{k,img}$ 和Value方向 $S_{v,img}$。对于文本模态，利用NLP工具识别描述中的锚点词（如“cat”），构建包含锚点词（$T_{pos}$）和不含锚点词（$T_{neg}$）的对比文本对。同样通过两次预填充，提取最后一个文本token位置的Key和Value方向 $S_{k,txt}$ 和 $S_{v,txt}$。这一设计解决了DTI模态无关引导向量导致的模态错位问题，使干预能精准针对视觉感知错误和文本接地偏差。

### KV缓存的解耦干预

在下游推理时，PTI将提取的方向向量注入初始KV缓存。对于视觉token位置 $I_{img}$，Key和Value缓存分别更新为：

$$ K_{\tilde{l}}[I_{img}] = K_l[I_{img}] + \lambda_{k,img} \cdot \text{Norm}(S_{k,img}) $$

$$ V_{\tilde{l}}[I_{img}] = V_l[I_{img}] + \lambda_{v,img} \cdot \text{Norm}(S_{v,img}) $$

对于文本token位置 $I_{txt}$，仅对最后一个文本token应用类似更新。Key向量控制注意力“关注何处”，Value向量控制“聚合什么”。通过物体-背景对比，Key方向引导注意力聚焦于视觉接地的物体，Value方向过滤背景噪声。这种解耦干预利用了注意力机制的内在结构，实现了比隐藏状态更细粒度的控制。由于干预仅在预填充阶段执行一次，后续解码过程无需额外计算开销，避免了DTI的延迟累积问题。

## 实验评估

实验在LLaVA-1.5、Qwen-VL-Chat和DeepSeek-VL-Chat三个架构迥异的LVLMs上进行，评估基准包括CHAIR、POPE、AMBER、MMHAL和MME。基线覆盖VCD、OPERA、PAI、VTI和VISTA，但缺失知识库中提到的HulluEdit（表征编辑）和RUDDER（残差更新）等最新方法。

| 模型 | 解码策略 | 方法 | CHAIRs ↓ | CHAIRi ↓ |
| :--- | :--- | :--- | :--- | :--- |
| LLaVA-1.5 | Greedy | Vanilla | 47.4 | 13.7 |
| LLaVA-1.5 | Greedy | VISTA | 20.4 | 6.9 |
| LLaVA-1.5 | Greedy | PTI | 15.4 | 5.4 |
| Qwen-VL-Chat | Greedy | Vanilla | 41.6 | 12.0 |
| Qwen-VL-Chat | Greedy | PTI | 20.6 | 7.0 |
| DeepSeek-VL-Chat | Greedy | Vanilla | 25.6 | 6.5 |
| DeepSeek-VL-Chat | Greedy | PTI | 19.2 | 6.7 |

在CHAIR基准上，PTI在LLaVA-1.5 Greedy解码下将CHAIRs从47.4降至15.4，降幅32.0，显著优于VISTA的20.4。在Qwen-VL-Chat上，PTI的CHAIRs为20.6，同样优于VISTA的39.0。这表明PTI在自由形式描述任务中能有效抑制幻觉。

| 模型 | 方法 | POPE Adversarial Acc ↑ | POPE Average Acc ↑ |
| :--- | :--- | :--- | :--- |
| LLaVA-1.5 | Vanilla | 75.40 | 80.26 |
| LLaVA-1.5 | VCD | 76.63 | 81.53 |
| LLaVA-1.5 | PTI | 77.40 | 82.21 |
| Qwen-VL-Chat | Vanilla | 80.26 | 83.69 |
| Qwen-VL-Chat | PTI | 85.69 | 85.14 |

在POPE基准上，PTI在LLaVA-1.5 Adversarial子集上取得77.40%准确率，优于VCD的76.63%，但低于知识库中HDD的89.2%。在Qwen-VL-Chat上，PTI的Adversarial准确率为85.69%，显著高于Vanilla的80.26%。这显示PTI在对象存在性判断上有效，但未达到最新SOTA水平。

消融实验揭示了模态干预的差异化效果。仅视觉干预（Last token & All visual tokens）在LLaVA-1.5上取得CHAIRs 16.8，CHAIRi 6.2，但F1分数降至70.3，表明过度强调视觉模态可能损害生成质量。加入文本干预（PTI完整方法）后，CHAIRs进一步降至15.4，F1恢复至72.7。这说明文本干预不仅补充了视觉概念，还恢复了生成质量，验证了模态解耦设计的必要性。

评估边界方面，PTI未报告推理延迟和计算开销的详细数据，仅声称“可忽略不计”。超参数 $\lambda$ 通过网格搜索确定，但未提供具体值。代码已开源，但实验仅限静态图像，未涉及视频或多图像场景。POPE低分可能源于PTI侧重生成质量而非二分类判别，但论文未对此进行明确讨论。

## 关联研究分析

从问题动机看，PTI与VCD共享对比解码的思想，但干预层级不同。VCD在解码阶段对比原始与扰动图像的logits，而PTI在预填充阶段对比物体与背景在KV缓存中的表征。这一差异源于对幻觉累积机制的不同理解：VCD试图在每一步生成时校正偏差，而PTI认为初始状态的偏差是后续错误的根源。PTI的预填充干预可能更有效地抑制错误累积，但牺牲了对解码过程中动态变化的适应能力。

从方法设计看，PTI与HulluEdit同属表征编辑路线，但干预对象不同。HulluEdit在激活空间中编辑幻觉相关子空间，而PTI在KV缓存中编辑模态特定方向。HulluEdit依赖对幻觉子空间的准确定位，可能面临细粒度幻觉的解耦困难；PTI则利用注意力机制的Key-Value结构，实现更底层的控制。然而，PTI未与HulluEdit进行直接对比，无法判断哪种表征编辑方式在细粒度幻觉上更优。此外，PTI的模态解耦设计是否适用于其他多模态任务（如视频理解），论文未给出回答。

## 总结

PTI要解决的核心矛盾是DTI方法在降低幻觉频率时加剧剩余幻觉严重程度的“雪崩效应”。现有DTI方法因干预时机滞后、目标粗糙和模态无关，无法从源头抑制错误累积。PTI抓住预填充阶段KV缓存这一关键干预点，通过模态感知的Key-Value解耦编辑，在错误累积前重塑初始状态。实验证明，PTI在CHAIR基准上显著优于VISTA等DTI方法，LLaVA-1.5 Greedy解码下CHAIRs从47.4降至15.4。然而，PTI在POPE基准上未超越最新SOTA，且其长序列生成后期的视觉信号衰减问题未得到验证。当生成序列长度超过512 token时，预填充阶段的初始状态是否仍能有效约束后续解码，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.25642)