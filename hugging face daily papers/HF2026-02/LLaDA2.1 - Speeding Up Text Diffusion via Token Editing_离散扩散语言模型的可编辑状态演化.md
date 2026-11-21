# HuggingFace最新推荐论文 ｜LLaDA2.1: Speeding Up Text Diffusion via Token Editing ｜离散扩散语言模型的可编辑状态演化

研究机构：浙江大学、西湖大学

作者：Tiwei Bie、Maosong Cao、Xiang Cao 等 50 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.08676)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08676)

> 离散扩散语言模型（dLLM）旨在通过并行解码突破自回归生成的串行瓶颈，但标准吸收态框架强制单调的掩码到Token转换，导致并行采样中的局部错误无法修正，进而引发后续步骤的保守化与速度衰减。现有置信度重掩码或外部引导模型方案仅能缓解部分不一致，无法在保持并行加速优势的同时实现保真度的动态调控。本文提出可编辑状态演化框架，通过引入Token-to-Token（T2T）编辑机制与双阈值控制，将解码过程重构为“快速草稿-迭代修正”的连续可调过程。该方案在100B参数规模下实现了显著的速度提升，但其编辑能力对复杂推理任务的泛化边界尚存疑。

## 研究背景

离散扩散语言模型（Discrete Diffusion Large Language Models, dLLMs）通过并行处理多个Token位置来加速生成，其核心机制是在每一步$t$中，根据当前上下文预测所有掩码位置的概率分布，并依据置信度阈值$\tau_{mask}$决定是否将掩码替换为具体Token。然而，这种并行独立性导致各位置预测缺乏全局一致性，一旦早期步骤产生错误Token，模型在后续步骤中会因条件分布的扭曲而变得过度保守，显著降低生成速度。为应对这一暴露偏差（Exposure Bias），传统方法如置信度重掩码（Wang et al., 2025b）仅能重新标记低置信度位置，无法修正已确定的错误Token；外部引导模型（Lee et al., 2025）则引入额外计算开销，且难以适应动态变化的上下文。

dLLM领域长期面临速度与保真度的刚性权衡：降低阈值以加速生成会引入大量错误，提高阈值以保真则牺牲并行优势。LLaDA2.0虽验证了100B级模型的扩展潜力，但未解决解码过程中的错误累积问题。本文切入点在于将解码过程从单调的“掩码到Token”扩展为可逆的“草稿-编辑”范式，允许模型在生成过程中回溯修正已确定的Token，从而在保持并行加速的同时，通过累积错误校正实现保真度的动态提升。

## 核心方法

### 双阈值可编辑解码框架

标准dLLM解码仅包含掩码到Token（M2T）操作，即当预测概率超过$\tau_{mask}$时，将$[MASK]$替换为最高概率Token。本文引入Token-to-Token（T2T）编辑操作，允许已确定的Token在后续步骤中被替换。该设计动机在于解决并行解码中局部错误导致的后续保守化问题，通过回溯修正打破错误累积链条。

在时间步$t$，定义两个更新集合：解掩码集合$\Gamma_t$和编辑集合$\Delta_t$。对于位置$i$，若其当前为$[MASK]$且预测概率$p_\theta(v_i | \mathbf{x}_t) > \tau_{mask}$，则$i \in \Gamma_t$；若其当前为Token $v_j$且新预测概率$p_\theta(v_k | \mathbf{x}_t) > \tau_{edit}$且$v_k \neq v_j$，则$j \in \Delta_t$。状态更新公式为：

$$
\mathbf{x}_{t+1}[i] = \begin{cases}
\arg\max_v p_\theta(v | \mathbf{x}_t) & \text{if } i \in \Gamma_t \\
\arg\max_v p_\theta(v | \mathbf{x}_t) & \text{if } i \in \Delta_t \\
\mathbf{x}_t[i] & \text{otherwise}
\end{cases}
$$

该公式表明，模型同时执行新Token生成与旧Token修正，双阈值$\tau_{mask}$和$\tau_{edit}$分别控制草稿速度与编辑精度，实现了速度与保真度的解耦。

### 混合训练与块级策略优化

为培养编辑能力，本文在持续预训练（CPT）和监督微调（SFT）阶段采用M2T与T2T混合目标。M2T流训练模型预测掩码位置的正确Token，T2T流训练模型从随机噪声中恢复原始Token，使模型在单一参数空间中兼具快速草稿与精确编辑能力。

针对dLLM中序列对数似然不可计算导致强化学习（RL）难以应用的问题，本文提出基于证据下界（ELBO）的块级策略优化（EBPO）。通过向量化似然估计并行计算块条件概率，EBPO将策略梯度更新分解为块级贡献：

$$
\nabla_\theta J(\theta) \approx \sum_{n=1}^N w_n \sum_{b=1}^B \nabla_\theta \log p_\theta(\mathbf{y}_{t_n}^{(b)} | \mathbf{y}_0^{(b)}, \mathbf{z}_n) \hat{A}_t
$$

其中$\mathbf{z}_n$为块条件输入，$\hat{A}_t$为优势函数估计。该公式通过块因果掩码确保每个块仅关注有效历史，使RL可扩展至长上下文dLLM，解决了传统策略梯度在高方差与计算成本上的瓶颈。

## 实验评估

实验覆盖33个基准，涵盖知识、推理、代码、数学及智能体对齐五个维度。基线包括LLaDA2.0、Qwen3-30B-A3B及Ling-flash-2.0，但未对比DecoCal或AHD等其他SOTA扩散解码方法，缺乏跨架构公平对比。在Flash系列中，Q Mode下LLaDA2.1在MMLU-Pro上得分75.31，高于LLaDA2.0的66.67；S Mode下得分72.55，TPF（每前向Token数）达4.30，显著高于LLaDA2.0的3.95。

| 基准 | LLaDA2.0-flash (Score/TPF) | LLaDA2.1-flash S Mode (Score/TPF) | LLaDA2.1-flash Q Mode (Score/TPF) |
| :--- | :--- | :--- | :--- |
| MMLU-Pro | 66.67 / 3.95 | 72.55 / 4.30 | 75.31 / 2.92 |
| HumanEval+ | 88.41 / 6.45 | 89.63 / 13.81 | 89.63 / 9.18 |
| AIME 2025 | 60.00 / 4.57 | 63.33 / 5.36 | 63.33 / 3.46 |

多块编辑（MBE）机制在S Mode下带来一致性能提升，如LiveCodeBench从44.05提升至46.48，但TPF从6.48降至5.62，表明跨块修正以轻微速度损失换取全局一致性。量化后，LLaDA2.1-flash在HumanEval+上达到891.74 TPS，LLaDA2.1-mini达到1586.93 TPS，验证了编辑机制在加速并行解码中的有效性。

评估边界方面，论文未报告置信区间，且S Mode在指令遵循任务（IFEval）中速度最低（219.37 TPS），表明编辑机制在结构化任务中效率更高。代码未公开，超参数$\tau_{mask}$和$\tau_{edit}$的具体设置未详细披露，可复现性受限。

## 关联研究分析

从问题动机看，本文与DecoCal均关注dLLM解码中的置信度问题，但DecoCal侧重校准瞬时置信度以避免早期过度承诺，而本文通过T2T编辑实现事后修正。DecoCal的校准机制无法修正已确定的错误Token，仅能防止错误发生，而本文的编辑机制允许模型在错误发生后回溯修正，这源于dLLM并行解码中错误累积的固有特性，而非单纯置信度估计偏差。

从方法设计看，本文与AHD（Anchor-based History-stable Decoding）均追求加速，但AHD基于历史稳定锚点选择解码路径，属于前向优化；本文基于T2T编辑，属于后向修正。AHD的锚点机制依赖于历史状态的一致性，当并行解码产生局部不一致时，锚点可能失效；本文的编辑机制通过双阈值动态调整，允许在低置信度下快速草稿，再通过高置信度编辑修正，这种“先错后改”的策略在结构化任务中表现更优，但在开放域生成中可能引入额外延迟，论文未充分探讨其在非结构化任务中的适用性。

## 总结

LLaDA2.1旨在解决dLLM并行解码中速度与保真度的刚性权衡，其切入点在于将单调的掩码到Token转换扩展为可编辑状态演化，通过T2T机制允许模型回溯修正错误。该方法在100B参数规模下，Q Mode MMLU-Pro得分75.31，S Mode HumanEval+ TPS达891.74，验证了编辑机制在加速与保真中的双重价值。然而，S Mode在指令遵循任务中速度最低，且MBE机制带来轻微TPF下降，表明编辑能力在复杂非结构化任务中可能引入额外开销。当支持集增大到长上下文时，T2T编辑的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08676)