# ICLR2026最新论文 ｜FLASHDLM: ACCELERATING DIFFUSION LANGUAGE MODEL INFERENCE VIA EFFICIENT KV CACHING AND GUIDED DIFFUSION ｜免训练加速扩散语言模型推理：FreeCache与引导去噪

研究机构：美国康奈尔大学

作者：Zhanqiu Hu、Jian Meng、Yash Akhauri 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_21607548)

> 扩散语言模型（DLMs）虽具备并行解码与双向上下文优势，但迭代去噪导致的高延迟阻碍了其实际部署。现有加速方案多依赖额外训练或启发式调参，难以直接应用于大规模预训练模型。本文提出免训练的FreeCache与Guided Diffusion，通过冻结稳定KV投影及引入轻量自回归模型引导去噪，在保持精度的同时实现显著加速。该方法首次使DLM推理速度追平同级自回归模型，但其性能上限仍受限于骨干DLM自身的推理能力。

## 研究背景

自回归模型（AR）通过串行预测下一个Token实现生成，其计算复杂度随序列长度线性增长，但无法利用双向上下文。扩散语言模型（DLMs）将生成视为从全掩码序列逐步去噪的过程，理论上支持并行解码。然而，DLM每一步需对全序列进行前向传播，计算复杂度为$O(L^2)$，远高于AR的$O(l^2)$（其中$l$为已生成长度），导致推理延迟极高。此外，并行去噪缺乏因果约束，易产生Token语义不连贯，且现有启发式采样策略在减少去噪步数时精度骤降。

当前DLM加速研究主要沿两条路线展开：一是基于块扩散（Block Diffusion）的KV缓存，但需额外微调且可扩展性存疑；二是基于置信度阈值的并行解码（如Fast-dLLM），但依赖任务特定的超参数调优。这两类方法均无法直接应用于现成的大规模DLM（如Dream-7B、LLaDA-8B）。本文切入点在于揭示已确定Token的KV投影具有时间稳定性，并探索DLM与AR模型的协同机制，旨在无需任何训练或微调的情况下，直接加速现成DLM的推理过程。

## 核心方法

### 方法参照系

DLM推理加速的通用流程通常涉及修改去噪调度或引入缓存机制。标准AR缓存基于因果性，仅缓存已生成Token的KV；而DLM因双向注意力需处理全序列，传统缓存策略不适用。本文的关键差异在于：不改变DLM权重，而是利用去噪过程中的动态特性，将AR模型作为外部引导信号源，而非校正器。

### FreeCache：基于KV时间稳定性的窗口缓存

FreeCache针对DLM每步全序列计算的瓶颈，利用已确定Token的KV投影在后续去噪步中变化极小的特性。设计动机在于解决DLM无法直接复用AR缓存的问题，通过冻结已确定块的KV，动态缩小活跃计算窗口。具体而言，将生成序列划分为固定大小的块$B_1, \dots, B_N$。在生成块$B_i$时，仅对$B_i$及后续块$B_{i+1}, \dots, B_N$重新计算KV投影，而$B_1, \dots, B_{i-1}$的KV保持冻结。这一过程可形式化为：

$$
\text{ActiveWindow}(t) = \{B_i, B_{i+1}, \dots, B_N\} \quad \text{where } B_i \text{ is the current block}
$$

随着$B_i$完成去噪，其KV被冻结，活跃窗口缩小，计算成本逐步降低。该策略避免了Block Diffusion所需的微调，直接利用现成DLM的KV稳定性，实现了4.42x至6.32x的加速，且精度损失极小。

### Guided Diffusion：AR引导的自适应去噪

Guided Diffusion解决并行去噪导致的Token不连贯问题。设计动机在于现有启发式方法（如Top-K Margin）在少步采样时精度大幅下降，而本文通过引入轻量AR模型作为“引导者”，利用模型间一致性决定去噪步数。具体流程为：DLM先对全序列进行一次去噪预测，得到候选Token集合；随后，轻量AR模型对这些候选Token进行前向传播，计算其概率分布。若DLM预测的Token与AR模型预测的Top-1 Token一致，则接受该Token并解除掩码；否则，仅接受第一个Token。匹配长度$k$定义为：

$$
k = \max \{ j \mid \text{tok}_{\text{DLM}}[i_1:j] = \text{top1}(\text{logits}_{\text{AR}}[i_1:j]) \}
$$

若$k>0$，则解除$i_1$至$i_k$位置的掩码；若$k=0$，仅解除$i_1$。这一机制将AR模型从“校正者”转变为“引导者”，避免了推测解码中的重复校正开销，同时保留了DLM的并行优势。

## 实验评估

实验在NVIDIA RTX 6000 Ada GPU上进行，使用Dream-7B-Instruct和LLaDA-8B-Instruct作为骨干DLM，Qwen2.5-1.5B/7B-Instruct作为AR引导器。基线包括Vanilla DLM及AR模型，但缺失与Fast-dLLM、FLASHDLM等同类免训练加速方法的直接对比。

| 模型 | 方法 | GSM8K (8-shot) 准确率 (%) | 原始延迟 (s) | 加速比 |
| :--- | :--- | :--- | :--- | :--- |
| Dream-7B-Instruct | Baseline | 79.68 | 48.05 | 1.0x |
| Dream-7B-Instruct | FreeCache | 77.40 | 10.87 | 4.42x |
| LLaDA-8B-Instruct | Baseline | 79.30 | 56.89 | 1.0x |
| LLaDA-8B-Instruct | FreeCache | 77.18 | 9.02 | 6.32x |

FreeCache单独使用时，Dream-7B延迟从48.05s降至10.87s，准确率从79.68%微降至77.40%。结合Guided Diffusion后，GSM8K准确率恢复至80.33%（使用Qwen-1.5B引导），延迟进一步降至2.70s，加速比达17.80x。在MMLU-PRO上，FreeCache+Qwen-1.5B的准确率为46.64%，高于Baseline的46.92%（注：此处原文数据为46.64 vs 46.92，实际为略降，但文中称“negligible drop”），延迟从20.73s降至1.66s，加速比12.48x。

消融实验显示，AR引导器的大小对精度影响有限：Qwen-1.5B与Qwen-7B在GSM8K上的准确率分别为80.33%和81.41%，但延迟分别为2.70s和2.74s，表明轻量模型足以提供有效引导。然而，在GPQA等复杂推理任务上，FreeCache+Qwen-1.5B的准确率（49.55%）低于Baseline（39.29%）？此处数据需核对：原文Table 3显示GPQA Baseline为39.29%，FreeCache Only为43.30%，FreeCache+Qwen-1.5B为49.55%，FreeCache+Qwen-7B为49.33%。这表明AR引导显著提升了复杂推理任务的精度，但加速比从2.12x降至1.78x，存在精度-速度权衡。

评估边界方面，实验仅覆盖单GPU环境，未报告多GPU或分布式场景下的性能。代码已开源，但超参数（如块大小、匹配策略）未详细披露，可能影响复现性。此外，实验未包含与Fast-dLLM等同类方法的直接对比，难以全面评估其在免训练加速领域的相对优势。

## 关联研究分析

从方法设计看，本文与Fast-dLLM同属免训练加速路线，但核心机制不同。Fast-dLLM依赖置信度阈值决定并行解码步数，需任务特定调参；本文则利用DLM与AR模型的一致性作为唯一信号，避免了阈值调优。这一差异源于对“不确定性”的不同建模：Fast-dLLM假设高置信度Token可安全并行，而本文假设模型间一致性是更鲁棒的连贯性先验。然而，本文方法引入了对AR引导器分布的依赖，若AR模型与DLM的语义空间差异较大，引导效果可能受限，论文未对此进行系统分析。

从问题动机看，本文与Speculative Decoding（SDD）形成鲜明对比。SDD中AR模型作为目标模型，DLM作为草稿模型，需AR模型进行逐Token校正；本文反转角色，DLM作为主生成器，AR模型仅做引导，无需校正。这一设计避免了SDD中校正步骤的高开销，但牺牲了SDD的无损性保证。本文通过实验表明，AR引导器的大小对精度影响有限，暗示DLM的推理能力主导最终输出质量，AR模型仅起“过滤器”作用。这与SDD中AR模型决定输出质量的范式根本不同，但论文未深入探讨这种角色反转的理论基础。

## 总结

本文旨在解决DLM推理延迟高且难以直接加速的矛盾，抓住已确定Token KV投影的时间稳定性及DLM与AR模型的一致性信号，提出免训练的FreeCache与Guided Diffusion。实验证明，该方法在Dream-7B和LLaDA-8B上实现了平均12.14x和13.29x的加速，且精度损失可忽略，首次使DLM推理速度追平同级AR模型。然而，实验显示在GPQA等复杂推理任务上，加速比随AR引导器增大而下降，且未与Fast-dLLM等同类方法直接对比，限制了其相对优势的全面评估。当AR引导器与DLM的语义空间差异增大时，一致性信号的可靠性是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_21607548)