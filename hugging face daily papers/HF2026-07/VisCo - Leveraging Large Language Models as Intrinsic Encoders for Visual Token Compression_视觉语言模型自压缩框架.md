# HuggingFace最新推荐论文 ｜VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression ｜视觉语言模型自压缩框架

研究机构：中国科学技术大学

作者：Yupeng Zheng、Kai Zou、Bin Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.12756)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.12756)

> 视觉语言模型在处理高分辨率图像时，视觉Token数量激增导致计算成本与内存占用成为部署瓶颈。现有训练-free方法在极端压缩下语义丢失严重，而外部模块方法需高昂重训练成本且破坏预训练先验。VisCo利用预训练VLM自身作为内在编码器，通过可学习记忆Token与层级KV缓存传递实现自压缩。该框架在单Token极限下仍保持85.3%性能，但仅验证了图像场景，未探索视频时空冗余。

## 研究背景

高分辨率图像输入使视觉编码器输出的Token序列从数百激增至数千，引发Transformer自注意力计算的二次方增长与KV缓存内存瓶颈。这一困境源于视觉Token中存在的空间冗余，但冗余消除不能以牺牲细粒度语义为代价。视觉Token压缩的核心矛盾在于：如何在保持视觉-语言语义对齐的前提下，以最低计算开销动态确定最优保留子集。

主流训练-free方法如FastV依赖LLM浅层注意力分数剪枝，但注意力信号受位置偏差影响，在压缩率超过50%时性能急剧下降；VisionZip通过Token合并保留全局语义，但在极端压缩下增益有限。训练-based方法如VoCo-LLaMA引入外部压缩模块，需大规模重训练且改变VLM原生处理模式。VisCo的切入点在于：预训练VLM本身已具备强大的信息编码能力，无需外部模块，仅通过轻量级适配即可利用其内在先验实现自压缩。

## 核心方法

### 非对称VLM自编码器架构

VisCo将视觉Token压缩重构为非对称自编码器问题，区别于传统外部模块压缩。编码阶段引入LoRA适配器与可学习记忆Token，解码阶段冻结整个VLM骨干。该设计动机在于：外部模块强制VLM适应新压缩机制，破坏预训练先验；而自编码器复用VLM自身参数，保持原生处理模式。

$$
\Phi_E(\cdot; X_m, \theta_{LoRA}) = \text{Encoder}(X_v, X_m; \theta_{LoRA})
$$

其中 $X_v$ 为视觉Token序列，$X_m$ 为记忆Token，$\theta_{LoRA}$ 为LoRA参数。编码阶段仅训练 $X_m$ 和 $\theta_{LoRA}$，解码阶段移除LoRA适配器，直接复用预训练VLM作为解码器。

### 层级KV缓存传递机制

传统压缩方法仅传递编码器最终输出，丢失层级结构信息。VisCo在编码阶段收集每层记忆Token的KV值，构建层级记忆库，并在解码阶段直接注入KV缓存。该设计动机在于：Transformer各层具有功能 specialization，浅层编码局部纹理，深层编码抽象语义；仅传递最终输出会坍缩层级结构，导致极端压缩下细节丢失。

$$
K_{mem} = \{K_{mem}^{(l)}\}_{l=1}^L, \quad V_{mem} = \{V_{mem}^{(l)}\}_{l=1}^L
$$

其中 $K_{mem}^{(l)}$ 和 $V_{mem}^{(l)}$ 为第 $l$ 层记忆Token的键值矩阵。解码阶段将层级记忆库直接填充至解码器KV缓存，实现多层级语义的无损传递。

## 实验评估

实验在LLaVA-1.5-7B、Qwen2-VL-2B/7B三个骨干上，使用GQA、MMB、MME、POPE、MMVet、MMB-CN六个基准评估。基线覆盖训练-free（FastV、SparseVLM、VisionZip）与训练-based（PruMerge+、VoCo-LLaMA），但缺失ZOO-Prune等梯度敏感类方法。

| 方法 | Token | GQA | MMB | MME | POPE | Avg. |
|---|---|---|---|---|---|---|
| LLaVA-1.5-7B | 576 | 62.0 | 64.3 | 1510.7 | 85.9 | 100.0% |
| FastV | 32 | 41.5 | 37.8 | 884.6 | 32.5 | 57.6% |
| VisCo | 32 | 58.5 | 62.3 | 1152.9 | 81.9 | 91.8% |
| VisCo | 1 | 58.2 | 59.0 | 1191.2 | 78.2 | 85.3% |

VisCo在32Token下保持91.8%性能，显著优于FastV的57.6%和PruMerge+的77.5%；在单Token极限下仍保持85.3%，超过PruMerge+的35.4%和VisPruner的48.8%。

消融实验验证了层级KV传递的有效性：Our-HierKVPass在36Token下GQA达61.1%，Our-ValuePass仅51.8%；在18Token下，前者59.7% vs 后者49.6%。记忆Token位置分析显示，前18个Token承载主要物体信息，后18个Token捕获背景细节，丢弃前18个导致MMB从64.0降至55.7，丢弃后18个仅降至60.0。

评估边界：未报告计算效率指标（压缩时间、解码延迟、KV缓存大小），仅定性提及“解码速度与VisionZip一致”；未提供代码与超参数细节，LoRA rank=64、α=128、学习率5×10⁻⁵，训练数据为LLaVA-665K的10%子集；未验证跨模型泛化性，仅在三个特定骨干上评估。

## 关联研究分析

从问题动机看，VisCo与VoCo-LLaMA同属VLM内部压缩路线，但VoCo依赖大规模对齐与指令微调，改变VLM原生操作模式；VisCo仅LoRA微调，保持骨干冻结。差异根源在于：VoCo假设压缩需重学习多模态生成过程，VisCo认为预训练先验已包含编码能力，仅需轻量适配。这一假设在极端压缩下成立，但在中等压缩率（如128Token）下，VoCo是否仍具优势，论文未给出对比。

从方法设计看，VisCo与FastV同利用LLM注意力信号，但FastV直接剪枝低注意力Token，VisCo通过记忆Token聚合信息。差异根源在于：FastV假设注意力分数是Token重要性的良好代理，VisCo认为注意力信号不稳定，需通过可学习Token聚合多层级信息。这一设计在单Token极限下优势显著，但在中等压缩率下，注意力剪枝的计算效率是否仍具竞争力，论文未量化对比。

## 总结

VisCo解决的核心矛盾是极端压缩下的语义保真度与计算效率平衡。其切入点在于利用预训练VLM自身作为内在编码器，避免外部模块的重训练成本与先验破坏。方法通过可学习记忆Token与层级KV缓存传递，在单Token极限下保持85.3%性能，32Token下达91.8%。边界在于：仅验证图像场景，未探索视频时空冗余；未报告计算效率指标，无法评估实际部署价值；未验证跨模型泛化性。当记忆Token数量从36降至1时，层级KV传递的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.12756)