# ICLR2026最新论文 ｜InternSVG: Towards Unified SVG Tasks with Multimodal Large Language Models ｜统一SVG建模：从碎片化任务到多模态大语言模型

研究机构：上海交通大学、南京大学

作者：Haomin Wang、Jinhui Yin、Qi Wei 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11341)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11341)

> 通用矢量图形建模长期受困于数据集任务割裂、方法跨域泛化能力弱以及长序列结构复杂度难以处理。现有LLM生成方法虽在静态图标上取得进展，但无法同时覆盖理解、编辑与动态动画生成，导致模型在专业领域如化学结构式上表现脆弱。本文通过构建16M规模的多任务数据集SAgoge，并设计带有SVG专用特殊Token的统一MLLM架构InternSVG，实现了理解、编辑与生成的正向迁移。该工作验证了统一建模在提升长序列生成质量上的有效性，但其对极端复杂拓扑结构的鲁棒性仍受限于骨干网络的上下文窗口。

## 研究背景

SVG作为XML标准的2D图形格式，具备分辨率无关与细粒度可编辑性，但其本质是嵌套的几何原语与属性代码序列。当模型直接处理原始SVG字符串时，冗长的路径坐标与重复标签会导致序列长度爆炸，使得标准Transformer的注意力机制在长序列上发生稀释，难以捕捉全局几何约束。为解决这一序列效率与语义保真度的矛盾，引入领域专用Token化策略成为关键，它通过压缩高频结构单元来降低计算负担，同时保留层级结构信息。

SVG建模领域的主流路线已从早期的优化式光栅化（如DiffVG）转向基于LLM的代码生成范式。StarVector与OmniSVG等方法证明了LLM在Text-to-SVG任务上的潜力，但这些工作大多局限于单一生成任务，缺乏对理解与编辑任务的联合建模。这种碎片化的监督导致模型无法在任务间共享语义表示，且在面对长序列插图或动态动画时，由于训练数据中缺乏此类复杂样本，模型泛化能力显著下降。本文的切入点在于打破任务壁垒，通过大规模多任务数据集与统一架构，迫使模型在理解、编辑与生成之间建立内在联系，从而提升对复杂SVG结构的整体建模能力。

## 核心方法

### 方法参照系

本文遵循“ViT–MLP–LLM”的多模态大语言模型范式，以InternViT-300M为视觉编码器，Qwen2.5-7B为语言模型。与通用MLLM处理自然语言不同，本文的核心差异在于输入模态包含结构化代码（SVG）与渲染图像，且输出需满足严格的语法与几何约束，这要求模型具备对代码结构的精细感知能力。

### SVG专用Token化与子词初始化

在标准Tokenizer处理SVG代码时，长路径字符串被拆分为大量无意义的子词，导致序列冗长且语义碎片化。本文引入55个标签Token、42个属性Token及数值Token，将高频结构单元映射为单一语义单元。对于新引入的特殊Token $t_{new}$，其嵌入向量 $\mathbf{e}_{t_{new}}$ 并非随机初始化，而是通过预训练Tokenizer将其分解为 $n$ 个子词 $\{s_1, ..., s_n\}$，并取这些子词嵌入的均值：

$$ \mathbf{e}_{t_{new}} = \frac{1}{n} \sum_{i=1}^{n} \mathbf{e}_{s_i} $$

该公式的物理含义是利用预训练词表中的语义先验来锚定新Token的初始位置，避免随机初始化导致的训练不稳定。这一设计解决了此前方法在长序列SVG上因Token数量过多导致的注意力稀释问题，显著缩短了序列长度，加速了收敛过程。

### 两阶段渐进式训练策略

单一阶段训练难以平衡简单图标与复杂插图的分布差异。本文采用两阶段策略：第一阶段在短序列的Icon与Chemistry数据上训练，学习基础语法与几何结构；第二阶段扩展至长序列的Illustration与Animation数据，学习复杂布局与时序动态。这种渐进式训练解决了直接在全量数据上训练时，简单样本主导梯度更新导致复杂样本学习不足的问题。通过先建立稳定的语法基础，再引入复杂结构，模型在长序列生成任务上的FID指标显著降低，证明了任务难度递进对跨域泛化的正向作用。

## 实验评估

实验在SArena基准上进行，覆盖Icon、Illustration、Chemistry与Animation四个域。基线包括GPT-4o、Claude-Sonnet-4等专有模型，以及StarVector、OmniSVG等LLM-SVG专用方法。在SArena-Icon理解任务中，InternSVG以85.1的Overall Accuracy超越Claude-Sonnet-4的77.1；在Text-to-SVG任务中，其FID为8.715，远低于Claude-Sonnet-4的15.840。

| 模型 | Understanding (Overall) | Editing (PSNR) | Text-to-SVG (FID) | Image-to-SVG (SSIM) |
| :--- | :--- | :--- | :--- | :--- |
| Claude-Sonnet-4 | 77.1 | 57.595 | 15.840 | 0.665 |
| GPT-4o | 71.0 | 55.255 | 15.178 | 0.616 |
| OmniSVG 3B | – | – | 28.292 | 0.756 |
| InternSVG 8B | **85.1** | **77.331** | **8.715** | **0.811** |

消融实验显示，统一建模（G+U+E）相比仅生成（G）任务，在Understanding Overall Accuracy上从62.9提升至75.4，在Editing PSNR上从42.131提升至54.618。这表明理解与编辑任务为生成任务提供了有效的语义约束。然而，在Style Transfer这一高难度编辑子任务上，InternSVG的SSIM为0.808，仍低于Claude-Sonnet-4的0.867，说明模型在复杂风格迁移上的语义对齐能力仍有局限。

评估协议采用渲染后的图像指标（FID, SSIM, LPIPS）与代码结构指标（Path Count, Tokens）相结合。不可渲染的SVG被替换为黑图作为惩罚，确保了评估的公平性。代码开源，但16M数据集的构建依赖多个MLLM进行标注，标注质量的波动可能影响训练稳定性。

## 关联研究分析

从问题动机看，本文与StarVector同属LLM-based SVG生成路线，但StarVector聚焦于静态图标的Text-to-SVG，而本文扩展至动态动画与化学结构式。这一差异源于任务特性的不同：静态图标结构相对简单，单任务优化即可达到较高精度；而动态动画与时序变化要求模型具备更强的时序推理能力，单任务模型难以捕捉帧间一致性。本文通过引入Animation域数据，迫使模型学习时序动态，这是StarVector未探索的盲区。

从方法设计看，本文与OmniSVG均采用MLLM架构，但OmniSVG主要依赖通用Tokenizer处理SVG代码，而本文引入SVG专用Token。这一设计选择的根源在于序列长度对性能的影响：在长序列Illustration任务中，通用Tokenizer产生的Token数量是专用Tokenizer的数倍，导致注意力机制无法有效覆盖全局结构。本文的专用Token化策略通过压缩序列长度，缓解了这一问题，但在极端长序列（如超过10k Token）下的表现仍需进一步验证。

## 总结

本文旨在解决SVG建模中任务割裂与长序列泛化难的核心矛盾。通过构建16M规模的多任务数据集SAgoge，并设计带有SVG专用Token与子词初始化的统一MLLM架构InternSVG，实现了理解、编辑与生成的正向迁移。实验表明，InternSVG在SArena-Icon理解任务上达到85.1的准确率，在Text-to-SVG任务上FID低至8.715，显著优于专有模型。然而，模型在Style Transfer等复杂编辑任务上的表现仍落后于Claude-Sonnet-4，且长序列生成依赖两阶段训练策略，其泛化边界尚不明确。当支持集增大到更复杂的拓扑结构时，专用Token的压缩效率是否足以抵消注意力稀释，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11341)