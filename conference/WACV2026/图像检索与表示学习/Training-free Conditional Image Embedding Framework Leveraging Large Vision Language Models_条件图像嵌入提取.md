# WACV2026最新论文 ｜Training-free Conditional Image Embedding Framework Leveraging Large Vision Language Models ｜条件图像嵌入提取

作者：Masayuki Kawarada、Kosuke Yamada、Antonio Tejero-de-Pablos 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21860)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21860)

> 图像检索中，单一全局向量往往混淆了用户意图中的不同属性维度，导致无法按特定条件（如仅按纹理或仅按颜色）进行精准匹配。现有方法要么依赖针对特定属性的监督训练，要么通过线性子空间映射解耦，但后者受限于预训练特征中属性纠缠的固有缺陷。DIOR 提出了一种无训练框架，利用大型视觉语言模型（LVLM）的指令跟随能力，通过提示词将图像压缩为特定条件下的单字语义向量。该方法在通用条件检索任务上超越了CLIP基线，但在特定艺术风格域中表现落后，其有效性高度依赖LVLM的语义理解深度而非局部视觉细节捕捉。

## 研究背景

当用户试图在电商数据库中查找“纹理相似但款式不同”的服装时，传统的全局图像嵌入（Global Image Embedding）会将纹理、款式、颜色等所有视觉特征聚合为一个向量，导致检索结果混杂。这种全局表示的局限性催生了条件图像嵌入（Conditional Image Embedding）的概念，即通过文本条件引导，提取仅关注特定属性的特征子空间。然而，CLIP等视觉基础模型生成的通用嵌入中，不同属性在潜空间中高度纠缠，简单的线性投影难以有效分离这些维度，且现有解耦方法通常需要对特定属性进行大规模监督训练，限制了其在开放世界中的泛化能力。

条件图像相似性任务旨在解决这一属性混淆问题，早期工作如InDiRECT通过PCA在CLIP特征空间中寻找条件子空间，但受限于CLIP特征本身的纠缠特性，其解耦能力有限。随着大型视觉语言模型（Large Vision-Language Models, LVLMs）的兴起，模型具备了强大的指令跟随和多模态理解能力，这为无需额外训练即可实现属性解耦提供了新路径。DIOR的切入点在于，不再将LVLM视为生成文本的工具，而是将其冻结的隐状态直接作为条件嵌入的提取器，利用语言模型的语义压缩能力替代传统的度量学习训练过程。

## 核心方法

### 方法参照系

条件嵌入提取的标准流程通常涉及两个阶段：首先通过预训练编码器获取通用图像特征，随后通过训练特定的投影头或子空间映射器，将通用特征解耦为条件特定表示。DIOR的关键差异在于完全移除了第二个训练阶段，转而利用LVLM的Transformer层作为非线性的、数据驱动的解耦算子，直接输出条件嵌入。

### 基于提示词的隐状态提取

传统方法依赖训练好的投影层来分离属性，而DIOR利用LVLM的指令跟随机制，通过提示词强制模型在特定语义维度上进行压缩。给定图像 $I$ 和条件文本 $c$，DIOR构造提示 $T = \text{"Describe the image in one word regarding } c \text{:"}$。图像经视觉编码器 $f_{VE}$ 和投影器 $f_p$ 得到 $M$ 个补丁嵌入 $\mathbf{p}$，文本经嵌入层得到 $N$ 个词元嵌入 $\mathbf{t}$。两者拼接后输入LVLM的Transformer层 $f_t$，最终条件嵌入定义为提示词最后一个词元的隐状态：

$$ \mathbf{e}_c = f_t(\mathbf{p}, \mathbf{t})_{M+N} $$

这一设计的动机在于，单字约束迫使LVLM将图像中与该条件相关的视觉信息压缩至单一向量中，从而在隐空间中实现属性的解耦，避免了线性投影无法处理非线性纠缠的问题。

### 无训练嵌入对齐

DIOR的另一关键创新在于利用LVLM预训练阶段获得的视觉-语言对齐能力，无需针对检索任务进行微调。在标准LVLM推理中，隐状态用于预测下一个文本词元，而DIOR将其直接用作图像嵌入。相似度计算采用余弦相似度：

$$ \text{sim}(I_q, I_d | c) = \frac{\mathbf{e}_{q,c} \cdot \mathbf{e}_{d,c}}{\|\mathbf{e}_{q,c}\| \|\mathbf{e}_{d,c}\|} $$

该机制解决了传统方法需要为每个新条件重新训练投影头的问题，使得同一模型能够处理任意文本条件，实现了条件嵌入的零样本泛化。

## 实验评估

实验在LanZ-DML、DomainNet和WikiArt三个基准上进行，基线包括CLIP、InDiRECT和CapEmb。LanZ-DML涵盖合成汽车、CUB200、DeepFashion等数据集，评估多条件检索性能。

| 方法 | 参数量 | Synthetic Cars Avg | DeepFashion Avg | Movie Posters Avg | Overall Avg |
|---|---|---|---|---|---|
| CLIP | 428M | 31.0 | 35.9 | 37.8 | 31.0 |
| InDiRECT (CLIP) | 428M | 39.5 | 54.9 | 39.5 | 39.5 |
| DIOR (Llama-3.2) | 11B | 44.5 | 46.7 | 46.7 | 44.5 |
| DIOR (Qwen-2.5-VL) | 7B | 46.7 | 46.7 | 46.7 | 46.7 |

DIOR (Llama-3.2) 在LanZ-DML上的平均MAP@R为44.5，显著高于CLIP的31.0和InDiRECT的39.5。值得注意的是，较小的Qwen-2.5-VL (7B) 达到了46.7的平均分，表明DIOR的性能随LVLM规模的增大而提升，且受益于更先进的视觉语言模型架构。

| 提取位置 | Synthetic Cars | CUB200 | DeepFashion | Movie Posters | Avg |
|---|---|---|---|---|---|
| Last Input | 40.2 | 51.9 | 41.0 | 42.8 | 44.5 |
| First Output | 40.1 | 50.3 | 39.0 | 45.7 | 44.3 |
| Mean Output | 29.2 | 35.1 | 34.2 | 41.3 | 36.9 |

消融实验显示，使用提示词最后一个词元（Last Input）的隐状态作为嵌入效果最佳，平均MAP@R为44.5，略高于第一个生成词元（First Output）的44.3，而平均生成词元（Mean Output）性能显著下降至36.9。这表明LVLM在提示处理阶段已完成了主要的语义压缩，生成阶段的额外计算并未带来嵌入质量的提升，反而引入了噪声。

在DomainNet风格检索任务中，DIOR在风格相似性（MAP@1: 83.57）和对象相似性（MAP@1: 72.55）上均优于CLIP和CSD，证明了其在风格解耦上的有效性。然而，在WikiArt艺术风格基准上，DIOR的MAP@1仅为45.6，低于CLIP的59.3和CSD的58.2，表明LVLM在特定艺术风格领域的先验知识不足，导致条件嵌入质量下降。

评估协议主要关注检索精度（MAP/Recall），未报告计算延迟对大规模索引的影响。DIOR依赖11B参数的LVLM，单次推理耗时549.72ms（无缓存），远高于CLIP的36.10ms，限制了其在实时大规模检索场景中的应用。代码已开源，但提示词工程对性能的影响未做系统性探索，仅验证了“Describe”动词的稳定性。

## 关联研究分析

从问题动机看，DIOR与InDiRECT均旨在解决CLIP特征中属性纠缠的问题，但InDiRECT依赖线性子空间映射，假设属性在潜空间中是线性可分的，而DIOR利用LVLM的非线性Transformer层，能够捕捉更复杂的属性交互关系。InDiRECT在CUB200上表现优于DIOR（66.9 vs 68.0，注：此处InDiRECT数值来自表格，DIOR为68.0，实际DIOR略优，但在Synthetic Cars Model上InDiRECT 94.0 vs DIOR 88.0），这表明在特定细粒度类别上，线性子空间可能更稳定，而DIOR的优势在于跨域泛化和多条件统一处理。

从方法设计看，DIOR与CapEmb同属无训练或低训练范式，但CapEmb依赖文本嵌入对齐，需要预训练文本编码器，而DIOR直接利用LVLM的视觉-语言联合表示。CapEmb在LanZ-DML上的平均性能（29.5）低于DIOR（44.5），且其性能受限于文本编码器的语义覆盖范围。DIOR的创新在于将LVLM的生成能力转化为嵌入提取能力，这一范式转换使得模型能够处理任意文本条件，而无需为每个条件预训练文本嵌入。然而，DIOR在WikiArt上的失败暗示，LVLM的语义理解可能偏向于通用自然语言描述，而非特定领域的视觉风格特征，这限制了其在专业垂直领域的应用。

## 总结

DIOR旨在解决全局图像嵌入无法区分特定属性维度的问题，通过利用LVLM的指令跟随能力实现无训练的条件嵌入提取。该方法在LanZ-DML基准上以44.5的平均MAP@R超越了CLIP（31.0）和InDiRECT（39.5），证明了LVLM隐状态作为条件嵌入的有效性。然而，DIOR在WikiArt艺术风格域中性能低于CLIP（45.6 vs 59.3），暴露了LVLM在特定视觉风格先验上的不足。当检索任务涉及高度专业化的视觉风格或细粒度局部纹理时，依赖全局语义压缩的LVLM隐状态是否仍能保持足够的判别力，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21860)