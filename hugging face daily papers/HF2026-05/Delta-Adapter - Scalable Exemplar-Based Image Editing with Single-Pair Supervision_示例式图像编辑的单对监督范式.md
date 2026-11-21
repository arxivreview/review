# HuggingFace最新推荐论文 ｜Delta-Adapter: Scalable Exemplar-Based Image Editing with Single-Pair Supervision ｜示例式图像编辑的单对监督范式

研究机构：中山大学、香港理工大学

作者：Jiacheng Chen、Songze Li、Han Fu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.07940)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07940)

> 示例式图像编辑旨在通过源-目标图像对定义视觉变换，并将其迁移至新查询图像，以解决自然语言难以精确描述细微外观变化与编辑幅度的局限。现有方法依赖“成对监督”，要求两对图像共享相同编辑语义，导致数据策展困难且泛化受限。本文提出Delta-Adapter，通过提取语义Delta替代完整目标图像作为条件，实现无文本引导的单对监督训练。该方法在数据规模与泛化性上展现出优势，但其性能上限受限于视觉编码器的语义表达能力。

## 研究背景

当用户希望将一张照片的“去模糊”效果迁移到另一张清晰照片时，自然语言指令往往无法精确界定模糊的程度与范围。这种语义模糊性催生了示例式图像编辑（Exemplar-based Image Editing），即利用一对源-目标图像（Exemplar Pair）直观定义变换规则。然而，现有扩散模型方法通常采用“成对监督”范式：模型需同时观察两对图像 $\{a, a'\}$ 和 $\{b, b'\}$，通过对比 $a \to a'$ 的变换来预测 $b \to b'$。这种架构要求两对图像间的变换必须严格对齐，任何细微差异都会引入噪声，使得高质量训练数据的获取成本极高，且限制了可学习编辑类型的多样性。

指令式图像编辑领域已确立扩散模型作为主流骨干，并强调非编辑区域的内容一致性。然而，在示例编辑中，直接暴露目标图像 $a'$ 作为条件会导致模型“抄写”而非“学习”变换，因此必须引入第二对图像进行监督。这种数据依赖构成了该子领域的核心瓶颈。Delta-Adapter的切入点在于重构条件输入：不再让模型看到完整的目标图像，而是提取源图与目标图在特征空间中的差异（Semantic Delta）。这一改动使得单个图像对即可自监督，从而解除了对成对数据的依赖，使模型能直接复用大规模指令编辑数据集进行训练。

## 核心方法

### 方法参照系

本文问题属于参考引导编辑（Reference-guided Editing）范畴，但与传统方法的关键差异在于条件信号的提取方式。传统方法（如RelationAdapter）将完整的目标图像 $a'$ 编码后注入骨干网络，迫使模型依赖第二对图像进行监督。本文则通过提取特征差值 $\Delta_{a \to a'}$ 作为唯一条件，将任务转化为单对监督下的自重构问题。

### 语义Delta提取与门控精炼

设计动机在于消除原始特征空间中实例相关的幅度差异，保留纯粹的变换方向。本文使用预训练SigLIP编码器提取源图 $a$ 和目标图 $a'$ 的Patch级特征 $f_a, f_{a'}$。首先对每个Token进行层归一化（LayerNorm），再计算差值，得到归一化语义Delta：

$$ \Delta_{a \to a'} = \text{LN}(f_{a'}) - \text{LN}(f_a) $$

该公式通过归一化抑制了图像整体亮度或风格带来的幅度波动，仅保留特征空间中的方向性变化。随后，引入门控残差投影（Gated Residual Projection）进一步精炼信号：

$$ \tilde{\Delta}_{a \to a'} = \Delta_{a \to a'} + \tanh(g) \cdot \text{Linear}(\Delta_{a \to a'}) $$

其中 $g$ 为初始化为0的可学习标量门控。这一设计允许模型在训练初期稳定学习基础Delta表示，逐步引入残差修正以捕捉更复杂的变换细节，避免了直接线性投影可能引入的噪声。

### Perceiver重采样与解耦注意力注入

设计动机在于解决全局池化（Global Pooling）丢失局部空间关系的问题。传统IP-Adapter风格方法将视觉特征池化为单一向量，导致细粒度编辑信号丢失。本文采用Perceiver Resampler，将 $\tilde{\Delta}_{a \to a'}$ 重采样为固定长度的编辑Token序列 $E$。具体地，$N$ 个可学习查询Token通过交叉注意力聚合Delta信息，并采用逐Token投影（Per-token Projection）映射至DiT骨干的条件空间。

$$ E_i = W_i r_i + b_i, \quad i=1,\dots,N $$

这种逐Token投影允许每个编辑Token编码变换的不同方面，增强了表示的专用性。编辑Token通过解耦交叉注意力分支注入冻结的FLUX.2-klein-4B骨干，输出 $Z_{new} = Z + \lambda_{ca} Z_{\Delta}$，其中 $\lambda_{ca}$ 控制注入强度。此外，引入语义Delta一致性损失 $\mathcal{L}_{sdc}$，约束生成图像的特征差值与真实Delta在方向上对齐，确保编辑语义的忠实迁移。

## 实验评估

实验在Relation数据集（16K/1M对）上进行，对比RelationAdapter、LoRWeB、VisualCloze和Edit Transfer四个基线。评估指标包括CLIP-I（语义对齐）、LPIPS（感知相似度）及GPT-5.4评分（内容一致性GPT-C与编辑准确性GPT-A）。

| 方法 | CLIP-I↑ | LPIPS↓ | GPT-C↑ | GPT-A↑ |
| :--- | :--- | :--- | :--- | :--- |
| Edit Transfer | 0.764 | 0.408 | 2.839 | 2.843 |
| LoRWeB | 0.898 | 0.254 | 4.198 | 3.033 |
| RelationAdapter | 0.858 | 0.327 | 3.201 | 3.417 |
| **Ours-16K** | **0.896** | **0.249** | **3.939** | **4.234** |

在Seen任务上，Delta-Adapter在CLIP-I和LPIPS上均优于所有基线，尤其在GPT-A（编辑准确性）上显著领先，表明其更忠实地迁移了示例变换。在Unseen任务上，Ours-16K的CLIP-I为0.882，优于RelationAdapter的0.862；而Ours-1M（1M对训练）的GPT-A达到4.008，显示大规模单对数据训练带来的泛化收益。

| 变体 | CLIP-I↑ | LPIPS↓ | GPT-C↑ | GPT-A↑ |
| :--- | :--- | :--- | :--- | :--- |
| w/o semantic delta | 0.866 | 0.337 | 3.228 | 3.839 |
| w/o perceiver | 0.891 | 0.260 | 3.876 | 4.059 |
| w/o L_sdc | 0.879 | 0.287 | 3.743 | 4.162 |
| **Ours** | **0.896** | **0.249** | **3.939** | **4.234** |

消融实验显示，移除Perceiver Resampler（w/o perceiver）导致Unseen任务性能显著下降，验证了保留空间结构对泛化性的关键作用。移除语义Delta一致性损失（w/o L_sdc）导致GPT-A从4.234降至4.162，表明该损失对编辑准确性的贡献不可忽视。

评估边界方面，GPT-5.4评分虽贴近人类感知，但缺乏置信区间报告，且未覆盖计算效率指标。代码已开源，训练配置（4×H200, 100K steps）明确，具备可复现性。

## 关联研究分析

从问题动机看，Delta-Adapter与ReEdit均利用语义Delta，但ReEdit是Training-free方法，依赖文本提示融合，而本文是训练式方法，纯视觉条件。这一差异源于任务特性：ReEdit适用于简单变换的即时推理，而本文通过训练适配器捕捉复杂变换的统计规律，更适合需要泛化性的场景。从方法设计看，本文与RelationAdapter同属参考引导编辑，但RelationAdapter依赖成对数据，本文通过Delta提取解除了数据依赖。这种设计选择暗示了视觉编码器（SigLIP）在捕捉细粒度变换上的局限性，因为Delta的表达能力受限于编码器的语义层级，无法完全替代MLLM对复杂逻辑的显式推理。

## 总结

Delta-Adapter解决了示例式图像编辑中成对监督导致的数据策展瓶颈，通过提取语义Delta实现单对监督，使模型能复用大规模指令编辑数据集。在Seen任务上，其CLIP-I达0.896，GPT-A达4.234，显著优于基线；在Unseen任务上，1M对训练版本展现出更强的泛化能力。然而，方法边界在于语义Delta受限于SigLIP编码器的语义表达能力，难以捕捉文字渲染等细粒度视觉细节。当编辑任务涉及复杂文字或高精度纹理时，纯视觉Delta是否足以替代文本引导，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07940)