# CVPR2026最新论文 ｜Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models ｜稀疏多模态离散扩散语言模型

研究机构：美国加州大学洛杉矶分校

作者：Shufan Li、Jiuxiang Gu、Kangning Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.14008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.14008)

> 统一多模态模型在推理阶段因反复处理冗余掩码Token而面临严重的计算瓶颈，现有加速方案往往牺牲双向上下文或依赖启发式规则导致性能不可控。本文切入点在于通过稀疏参数化与专用寄存器Token，在保留掩码离散扩散模型（MDM）双向上下文优势的同时实现高效KV缓存。具体做法是动态截断非关键掩码Token并引入压缩表示，配合步因果注意力掩码确保训练推理一致性。该方案在保持生成质量的前提下实现了近2倍加速，但其加速收益是否随序列长度线性增长，以及跨任务泛化能力仍存疑。

## 研究背景

当视觉生成任务要求模型同时处理图像与文本时，掩码离散扩散模型（MDM）将二者统一为离散Token序列，通过前向掩码与反向去噪实现联合建模。然而，MDM在推理时采用全注意力机制，每个采样步都需处理完整序列中的所有Token，包括大量尚未解码的掩码Token。这种密集参数化导致计算冗余：例如一张1024×1024图像由4096个Token表示，初期采样步仅解码少量Token，却仍需处理全部4096个位置。

主流加速路线分为两类：一类是训练无关的启发式方法（如Fast-dLLM），通过修改注意力模式引入KV缓存，但性能退化不可预测且依赖左到右解码顺序；另一类是训练相关方法（如Block Diffusion），采用块因果注意力掩码强制左到右生成，虽支持KV缓存却牺牲了MDM核心的双向上下文能力，导致图像修复等任务失效。现有方案无法同时满足“保留双向上下文”与“支持高效KV缓存”两个条件，而这两者恰是MDM在视觉生成任务中优于自回归模型的关键。

本文针对这一矛盾，提出Sparse-LaViDa框架。其核心洞察是：掩码Token本身不携带实质信息，仅指示位置被掩码，因此可通过稀疏表示压缩。通过动态截断非关键掩码Token并引入寄存器Token作为压缩表示，结合步因果注意力掩码，Sparse-LaViDa在保留双向上下文的同时实现KV缓存，填补了现有加速方法在视觉生成任务上的空白。

## 核心方法

### 方法参照系

标准MDM采用密集参数化：在中间采样步 $0 < t < 1$，所有 $L$ 个Token（含掩码与非掩码）均输入网络 $p_\theta$，输出密集张量 $y \in \mathbb{R}^{L \times V}$。本文问题与该通用流程的关键差异在于：仅对部分位置 $C \subset \{1, \dots, L\}$ 需要预测，但标准流程仍处理全部 $L$ 个位置，造成计算浪费。

### 稀疏参数化与寄存器Token

标准MDM中，部分掩码序列 $X_t$ 需完整物化所有 $L$ 个Token。本文创新在于：利用掩码Token的信息冗余性，仅保留非掩码Token、其位置及序列总长度，即可唯一表示部分掩码序列。具体地，对于序列“[I, have, [m], dog, [m], [m], [m]]”，仅需编码“I”（位置1）、“have”（位置2）、“dog”（位置4）及总长度7，掩码位置由剩余位置隐式确定。

$$
\text{Sparse Representation} = \left\{ (x_i, \text{pos}_i) \mid x_i \neq M \right\} \cup \{ L_{\text{total}} \}
$$

该公式的物理含义是：部分掩码序列可由非掩码Token集合、其位置索引及总长度唯一确定，无需显式存储掩码Token。然而，直接截断会导致模型容量下降，尤其当初始采样步仅解码少量Token时。为此，本文引入64个寄存器Token（Register Tokens），其位置ID连续排列在序列末尾。寄存器Token作为截断Token的压缩表示，通过注意力机制恢复被截断信息，且数量恒定，不随截断Token数增长。

### 步因果注意力掩码与采样策略

标准MDM训练采用全注意力，与推理时的KV缓存行为不一致。本文设计步因果注意力掩码（Step-Causal Attention Mask）：将序列分为 $M+N$ 个块，Prompt为块0，干净Token随机分配块 $1 \dots M$，掩码Token随机分配块 $M+1 \dots M+N$。干净Token仅可关注块 $j \le i$，掩码Token仅可关注同块及块 $j \le M$。

$$
\text{Attention Mask}(i, j) = \begin{cases} 1 & \text{if } j \le i \text{ (for clean tokens)} \\ 1 & \text{if } j = i \text{ or } j \le M \text{ (for masked tokens)} \\ 0 & \text{otherwise} \end{cases}
$$

该公式确保训练时模拟推理时的增量缓存行为：已解码Token的表示不受后续掩码Token影响，从而支持KV缓存。采样时，对于图像生成任务，采用LaViDa-O的分层随机采样器预生成解码顺序；对于文本生成，采用半自回归策略，将序列分块后左到右采样，块内基于置信度动态解码。关键区别在于：Sparse-LaViDa保留双向上下文，支持文本填充等任务，而Block Diffusion因块因果掩码仅支持单向生成。

## 实验评估

| 任务 | 指标 | LaViDa-O | Sparse-LaViDa | 加速比 |
| :--- | :--- | :--- | :--- | :--- |
| Text-to-Image | GenEval Overall | 0.77 | 0.78 | 1.95× |
| Text-to-Image | Latency (s) | 21.27 | 10.86 | - |
| Image Editing | ImgEdit Overall | 3.71 | 3.79 | 2.83× |
| Image Editing | Latency (s) | 63.98 | 22.55 | - |
| Math Reasoning | MathVista | 56.9 | 56.7 | 2.80× |
| Math Reasoning | Latency (s) | 10.41 | 3.72 | - |

实验覆盖文本到图像生成、图像编辑及视觉数学推理三类任务，基线包括LaViDa-O、Flux-Dev、BAGEL等。Sparse-LaViDa在GenEval上以0.78略超LaViDa-O的0.77，ImgEdit上以3.79超越3.71，MathVista上56.7与56.9接近，同时实现1.95×至2.83×加速。对比方法中，Flux-Dev（12B参数）GenEval为0.68，BAGEL（14B参数）为0.82，但二者未报告加速比，且BAGEL延迟45.1s远高于Sparse-LaViDa的10.86s。

消融实验显示，KV缓存与Token截断的协同效应显著：单独使用缓存Prompt加速1.29×，单独截断结果加速1.19×，二者结合加速1.51×，再叠加截断结果加速至1.96×。寄存器Token数量从0增至64时，GenEval从0.76升至0.78，FID从9.32降至7.63，表明寄存器Token对恢复截断信息至关重要。移除步因果注意力掩码后，GenEval降至0.71，DPG降至78.9，验证了训练-推理一致性的重要性。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码未公开，超参数（如寄存器Token数量64）的敏感性未充分探索。GPU型号与训练细节缺失，可复现性受限。加速比是否随序列长度线性增长，论文未提供不同分辨率下的对比数据。

## 关联研究分析

从问题动机看，Sparse-LaViDa与Block Diffusion均针对MDM推理效率，但设计哲学截然不同。Block Diffusion通过块因果掩码强制左到右生成，牺牲双向上下文以换取KV缓存，适用于语言建模但失效于图像修复；Sparse-LaViDa通过稀疏参数化保留双向上下文，支持任意解码顺序，更适配视觉生成任务。这一差异根源在于任务特性：图像Token无自然顺序，双向上下文对空间一致性至关重要，而文本Token具有左到右语义依赖，块因果掩码可接受。

从方法设计看，Sparse-LaViDa与Fast-dLLM等训练无关方法形成对比。Fast-dLLM通过启发式修改引入KV缓存，但性能退化不可预测且依赖左到右解码；Sparse-LaViDa通过训练步因果掩码确保一致性，加速更稳定。然而，Sparse-LaViDa需额外训练，而Fast-dLLM无需训练。这一权衡是否合理，取决于训练成本与推理频率的比值，论文未提供成本效益分析。

## 总结

Sparse-LaViDa解决的核心矛盾是MDM推理效率与双向上下文保留的冲突。现有方法要么牺牲双向性（Block Diffusion），要么性能不可控（Fast-dLLM），而本文通过稀疏参数化与寄存器Token，在保留双向上下文的同时实现KV缓存。实验证明，该方案在保持生成质量（GenEval 0.78 vs 0.77）的前提下，实现1.95×至2.83×加速。其边界在于：加速收益依赖寄存器Token数量与截断策略，且未验证跨分辨率泛化能力。当序列长度从4096增至16384时，寄存器Token的压缩效率是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.14008)