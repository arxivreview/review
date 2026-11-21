# HuggingFace最新推荐论文 ｜LoomVideo: Unifying Multimodal Inputs into Video Generation and Editing ｜LoomVideo：基于零开销条件注入的高效统一视频生成与编辑架构

研究机构：北京大学、阿里巴巴集团

作者：Jianzong Wu、Hao Lian、Jiongfan Yang 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.06042)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.06042)

> 统一视频生成与编辑旨在解决多模态输入下模型参数冗余与计算复杂度爆炸的矛盾。现有框架依赖13B以上大模型及Token拼接机制，导致推理成本呈指数级上升，难以满足实时交互需求。LoomVideo通过引入MLLM深层特征注入与零开销Scale-and-Add条件机制，在5B参数规模下实现了与13B模型持平的性能。该架构在效率与能力间取得了关键平衡，但其对极端非刚性编辑的鲁棒性及RL后训练的泛化边界尚存疑问。

## 研究背景

视频生成模型从单模态文本驱动向多模态交互演进，核心挑战在于如何高效融合视频、图像与细粒度指令。Diffusion Transformer (DiT) 作为主流骨干，其自注意力机制的计算复杂度与序列长度的平方成正比。当引入源视频作为编辑条件时，传统做法将源视频Token与目标视频Token沿序列维度拼接，使序列长度翻倍，计算量随之四倍增长，成为制约实时应用的主要瓶颈。

统一生成与编辑框架（如UniVideo、OmniWeaving）虽已验证多模态条件注入的可行性，但普遍依赖13B以上参数规模以维持语义对齐精度，且未解决序列拼接带来的效率瓶颈。这些模型在电商、时尚等需高频交互的场景中，推理延迟高达数千秒，无法满足实际部署需求。LoomVideo的切入点在于解耦“语义理解”与“条件注入”的计算成本：通过轻量化MLLM替代重型文本编码器，并设计零额外Token的条件机制，在保持编辑精度的同时大幅压缩推理路径。

## 核心方法

### 方法参照系

统一视频生成编辑框架通常采用“文本编码器+DiT”架构，通过交叉注意力注入条件信息。本文的关键差异在于：将T5文本编码器替换为多模态大语言模型（MLLM），并重构条件注入路径以消除序列拼接开销，从而在5B参数规模下实现多任务统一。

### Deepstack多层特征注入

传统方法仅使用MLLM最后一层嵌入作为条件，导致中间层丰富的层级语义信息丢失，限制了模型对细粒度指令的遵循能力。LoomVideo提出Deepstack机制，提取MLLM每一层的隐藏状态，经MLP投影后注入DiT对应层的交叉注意力模块。该设计解决了单层嵌入无法捕捉多粒度语义依赖的问题，使模型能同时理解宏观场景与微观细节。

$$
\mathbf{c}_{[l]} = \text{MLP}(\mathbf{h}_{\text{mllm}}^{[l]})
$$

其中 $\mathbf{h}_{\text{mllm}}^{[l]}$ 为MLLM第 $l$ 层隐藏状态，$\mathbf{c}_{[l]}$ 为投影后的条件特征，作为DiT第 $l$ 层交叉注意力的Key和Value。此公式表明，MLLM各层语义被逐层对齐至生成过程，实现了深层语义耦合。

### Scale-and-Add零开销条件注入

现有编辑框架通过拼接源视频Token提供条件，导致序列长度翻倍。LoomVideo采用Scale-and-Add机制，将源视频潜变量按时间步缩放后直接加到目标噪声潜变量上，不增加任何Token。该设计解决了拼接机制带来的计算瓶颈，同时验证了轻量条件足以驱动非刚性编辑。

$$
\mathbf{h}_{\text{merged}} = \phi(\mathbf{z}_{\text{target}}) + t \cdot \phi'(\mathbf{z}_{\text{source}})
$$

其中 $\mathbf{z}_{\text{target}}$ 为当前时间步 $t$ 的目标噪声潜变量，$\mathbf{z}_{\text{source}}$ 为源视频干净潜变量，$\phi$ 和 $\phi'$ 分别为原始和新增的Patch嵌入层（$\phi'$ 零初始化）。该公式表明，源视频贡献随去噪进程动态衰减，早期强引导、后期弱干扰，实现了零Token开销的条件注入。

## 实验评估

LoomVideo在VBench、OpenVE-Bench、RefVIE-Bench等基准上对比了UniVideo、OmniWeaving、VINO等13B/8.3B模型。基线覆盖统一生成模型与专用编辑模型，但缺乏对最新Sora 2等闭源模型的直接对比。

| 基准 | 模型 | 参数量 | 关键指标 | 数值 |
| :--- | :--- | :--- | :--- | :--- |
| VBench | LoomVideo (RL) | 5B | Average | 63.15 |
| VBench | UniVideo | 13B | Average | 63.01 |
| OpenVE-Bench | LoomVideo (RL) | 5B | Overall | 3.36 |
| OpenVE-Bench | OmniWeaving | 8.3B | Overall | 2.92 |
| RefVIE-Bench | LoomVideo (RL) | 5B | Overall | 3.78 |
| RefVIE-Bench | VINO | 13B | Overall | 3.38 |

LoomVideo (RL) 在VBench平均分63.15，略高于UniVideo的63.01；在OpenVE-Bench整体得分3.36，显著优于OmniWeaving的2.92。在RefVIE-Bench参考图编辑任务中，LoomVideo (RL) 得分3.78，超越VINO的3.38，验证了5B模型在复杂编辑任务上的竞争力。

消融实验显示，RL后训练对指令遵循能力提升显著。在IntelligentVBench的TIV2V任务中，LoomVideo (Stage 3) 平均分为4.14，而LoomVideo (RL) 提升至4.24。在Compositional MI2V任务中，RL版本在3Subjects子任务上平均分达4.03，较Stage 3的3.67提升0.36。这表明RL有效优化了多参考图场景下的语义对齐，但提升幅度随任务复杂度增加而递减。

评估边界方面，论文未报告置信区间，且FashionVideoBench为内部构建基准，外部可复现性受限。代码与模型已开源，但训练数据（如Taobao时尚域数据）未公开，限制了独立验证。

## 关联研究分析

从条件注入机制看，LoomVideo的Scale-and-Add与OmniWeaving的Channel Concat形成鲜明对比。OmniWeaving通过通道拼接融合源视频信息，虽保留部分时序结构，但仍需额外计算；LoomVideo则通过潜变量加法实现零Token开销，其根源在于将条件信息视为噪声调制的辅助信号而非独立序列。这种设计在电商等高频编辑场景中更具优势，但在需要精确时空对齐的复杂动作编辑中，是否因缺乏显式时序建模而失效，论文未给出充分验证。

从多模态融合策略看，LoomVideo的Deepstack机制与UniVideo的单层嵌入注入存在本质差异。UniVideo依赖MLLM最后一层输出，假设高层语义足以驱动生成；LoomVideo则逐层对齐，捕捉层级语义依赖。这一差异源于任务特性：电商编辑需同时理解“替换衣服”（宏观）与“保持姿势”（微观），单层嵌入易丢失细粒度约束。然而，Deepstack机制增加了MLLM与DiT间的参数耦合，在数据分布偏移时是否导致过拟合，尚需更多实验佐证。

## 总结

LoomVideo旨在解决统一视频生成编辑框架中参数冗余与计算复杂度高的核心矛盾。现有13B模型依赖Token拼接导致推理延迟过高，而LoomVideo通过MLLM深层特征注入与零开销Scale-and-Add机制，在5B参数下实现了性能持平与效率跃升。实验表明，其在VBench平均分63.15、OpenVE-Bench整体得分3.36，均优于或持平于13B基线，且推理速度提升5.41倍。然而，论文未充分验证Scale-and-Add在极端非刚性编辑（如大幅动作变化）中的鲁棒性，且RL后训练的提升是否依赖特定数据分布仍存疑问。当源视频与目标视频存在显著时空结构差异时，零Token条件注入是否足以维持编辑精度，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.06042)