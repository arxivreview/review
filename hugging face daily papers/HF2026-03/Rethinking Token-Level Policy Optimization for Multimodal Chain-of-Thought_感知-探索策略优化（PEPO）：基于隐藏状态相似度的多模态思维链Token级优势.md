# HuggingFace最新推荐论文 ｜Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought ｜感知-探索策略优化（PEPO）：基于隐藏状态相似度的多模态思维链Token级优势重加权

研究机构：南开大学、快手

作者：Yunheng Li、Hangyi Kuang、Hengrui Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22847)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22847)

> 多模态大模型在强化学习后训练中面临的核心矛盾是：序列级奖励信号无法区分推理链中哪些Token真正锚定了视觉证据，导致模型依赖语言先验产生幻觉。现有感知对齐方法或依赖额外的注意力掩码分支，或仅利用文本域熵信号，未能同时捕捉视觉接地与推理探索的互补动态。PEPO通过计算响应Token与视觉Token隐藏状态的余弦相似度构建感知先验，并与Token级熵经平滑门控融合，生成Token级优势以重加权策略梯度更新。该方法在3B规模模型上相对GRPO基线取得3.5-3.7点的平均提升，但其隐藏状态相似度能否在更大规模模型中替代显式注意力机制捕捉细粒度视觉依赖，尚缺乏验证。

## 研究背景

当视觉-语言模型执行几何推理时，其生成的思维链（Chain-of-Thought, CoT）中部分Token直接引用图像中的几何实体，而另一些Token仅执行代数推导。这种差异在组相对策略优化（Group Relative Policy Optimization, GRPO）的序列级优势函数中被抹平：所有Token共享同一优势值，导致视觉接地Token与纯文本推理Token获得相同的梯度更新权重。这一结构性缺陷源于可验证奖励强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）范式的固有局限——奖励信号仅作用于最终答案，无法为中间步骤提供差异化监督。为缓解此问题，文本域研究引入了Token级熵优势，但熵仅反映语言不确定性，与视觉语义缺乏对应关系；而现有感知感知对齐方法（如VPPO）虽引入视觉信号，却依赖额外的掩码分支或注意力度量，增加了计算开销且与高效加速框架不兼容。

多模态推理优化的主流路线已从结果监督转向过程级与感知级监督，但两条路线存在结构性割裂：过程奖励模型（Process Reward Model, PRM）细化信用分配却未显式锚定视觉证据，感知对齐优化强化视觉接地却未建模推理过程中的探索动态。PEPO的切入点在于揭示视觉接地与探索动态在Token层面的互补性：正确推理依赖紧凑的视觉对齐Token子集锚定感知，同时高熵Token标记需要探索的推理转折点。这一观察将感知对齐与探索优化统一于同一Token级框架中，避免了辅助分支的引入。

## 核心方法

### 方法参照系

GRPO通过采样G个响应并计算组内相对奖励获得序列级优势 $A_{(i)}$，该优势均匀应用于响应中所有Token。本文的关键差异在于：将序列级优势分解为Token级优势，通过视觉相似度与熵的融合权重对每个Token的梯度贡献进行差异化调制，而非修改奖励函数或引入额外网络分支。

### 感知先验与探索信号的Token级融合

PEPO在策略模型前向传播中提取响应Token与视觉Token的隐藏状态，计算每个响应Token的视觉相似度（Visual Similarity, VS）作为感知先验。VS定义为响应Token隐藏状态与所有视觉Token隐藏状态在全部Transformer层上的平均余弦相似度：

$$VS_{t}^{(i)} = \frac{1}{L \cdot N} \sum_{l=1}^{L} \sum_{n=1}^{N} \cos(h_{l,t}^{(i)}, v_{l,n}^{(i)})$$

该公式的物理含义是：若某响应Token的隐藏状态在多层表示空间中持续接近视觉Token，则该Token的推理过程高度依赖视觉证据。设计动机在于解决现有感知对齐方法依赖注意力机制或额外掩码分支导致的计算开销问题——隐藏状态相似度仅需一次前向传播即可获取，无需修改模型架构。

探索信号由Token级熵 $H_t^{(i)} = -\sum_{x \in V} p_\theta(x|s_t^{(i)}) \log p_\theta(x|s_t^{(i)})$ 提供，其中 $V$ 为词表，$p_\theta$ 为模型预测概率。高熵Token对应推理转折点，如验证、修正或分析等决策点。感知与探索信号经逐响应min-max归一化后，通过平滑门控机制融合：

$$w_t^{(i)} = \hat{VS}_t^{(i)} \cdot \sigma(\alpha \cdot \hat{H}_t^{(i)})$$

其中 $\sigma$ 为Sigmoid函数，$\alpha$ 为调节探索强度的超参数。该门控机制的设计动机在于：直接相加会导致感知与探索信号的尺度冲突，而乘性门控确保高视觉接地Token在低熵时仍保持高权重，高熵Token仅在视觉接地充分时才获得探索激励。融合权重 $w_t^{(i)}$ 将序列级优势 $A_{(i)}$ 细化为Token级优势 $A_t^{(i)} = A_{(i)} \cdot w_t^{(i)}$，使策略梯度更新聚焦于视觉接地且处于探索状态的推理Token。

## 实验评估

实验在Qwen2.5-VL-3B-Instruct与InternVL3-2B-Instruct两个骨干上开展，覆盖几何推理（Geometry3K、MathVista-mini、MathVerse-mini、LogicVista）、视觉定位（RefCOCO、LISA-Grounding）、少样本分类（FGVC Aircraft、Flower102）与视觉谜题（PuzzleVQA、AlgoPuzzleVQA）。基线包括GRPO、DAPO与High-Entropy RL，但缺失VPPO、PEARL等感知对齐专用方法的直接对比。

| 方法 | Geometry3K val | MathVista-mini | MathVerse-mini | LogicVista | Avg |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GRPO (Qwen2.5-VL-3B) | 19.00 | 51.56 | 40.54 | 28.30 | 32.64 |
| PEPOG (Qwen2.5-VL-3B) | 21.91 | 54.45 | 45.42 | 34.45 | 36.70 |
| GRPO (InternVL3-2B) | 22.08 | 49.36 | 42.09 | 28.84 | 33.74 |
| PEPOG (InternVL3-2B) | 25.84 | 52.36 | 44.89 | 31.88 | 37.25 |

PEPOG在Qwen2.5-VL-3B上相对GRPO的平均提升为+4.06点，在InternVL3-2B上为+3.51点。MathVerse与LogicVista上的增益（+4.88与+6.15点）大于MathVista-mini（+2.89点），表明PEPO在需要视觉-符号集成推理的任务上收益更显著。

| 变体 | Geometry3K val | PuzzleVQA |
| :--- | :--- | :--- |
| GRPO (baseline) | 19.00 | 43.20 |
| Exploration-only | 20.18 | 41.60 |
| Perception-only | 21.07 | 43.20 |
| PEPOG | 22.80 | 45.00 |

消融实验显示，仅使用探索信号（Exploration-only）导致PuzzleVQA性能下降1.60点，验证了纯熵优化在多模态任务上的不稳定性；仅使用感知信号（Perception-only）在Geometry3K上提升2.07点但PuzzleVQA无增益，表明感知接地对几何推理有效但对抽象关系推理不足。完整PEPOG在两项任务上均取得最优，证实感知-探索耦合的必要性。超参数 $\alpha$ 在0.05时取得Geometry3K最优（36.70），但FGVC Aircraft在 $\alpha=0.02$ 时最优（75.79），表明感知密集型与推理密集型任务对探索强度的偏好不同。

评估边界存在三处局限：第一，所有实验限于3B/2B规模模型，隐藏状态相似度在更大模型中是否仍能有效区分视觉接地Token未经验证；第二，MathVista-mini与MathVerse-mini为子集评测，与领域综述中VPPO在完整MathVista上66.10%的结果不可直接比较；第三，论文未报告训练稳定性指标（如KL散度曲线或奖励方差），仅以"stable optimization"定性描述。代码已开源，使用8块NVIDIA A40 GPU，DeepSpeed ZeRO-2，bfloat16精度，超参数 $\alpha$ 按数据集单独调优。

## 关联研究分析

从方法设计看，PEPO与VPPO（Huang et al., 2025）均基于GRPO引入视觉信号，但机制路径根本不同：VPPO通过视觉依赖分数生成二元梯度掩码，仅对高依赖Token计算策略梯度，属于硬过滤；PEPO通过平滑门控生成连续权重，对所有Token进行软重加权。这一差异源于对"视觉依赖"的建模假设不同——VPPO假设存在明确的视觉依赖阈值，PEPO假设视觉接地程度是连续谱。PEPO的软重加权避免了硬掩码可能导致的梯度稀疏问题，但代价是低视觉接地Token仍获得非零梯度，可能削弱视觉锚定的强度。PAPO（ICLR 2026）同样在GRPO框架下引入感知信号，但PAPO将感知准确性纳入优势估计的序列级计算，PEPO则在Token级进行融合，粒度更细但计算复杂度更高。

从问题动机看，PEPO与High-Entropy RL（作为直接基线）的对比揭示了多模态推理中探索与感知的非对称性：High-Entropy RL在RefCOCO上三次运行均崩溃，而PEPOG稳定取得83.46的IoU@50。这一结果并非偶然——熵信号在视觉定位任务中缺乏约束力，因为定位错误往往源于感知失败而非推理不确定性。PEPO通过视觉相似度门控，确保高熵Token仅在视觉接地充分时才获得探索激励，从而避免了纯熵优化在感知敏感任务上的失效。然而，PEPO未探索跨模态冲突场景（如文本提示与视觉证据矛盾），其隐藏状态相似度在冲突条件下是否仍能正确区分视觉接地Token，论文未给出回答。

## 总结

PEPO针对RLVR中序列级优势无法区分视觉接地Token与纯文本推理Token的结构性缺陷，利用隐藏状态相似度构建无监督感知先验，并与Token级熵经平滑门控融合生成Token级优势。在3B规模模型上，PEPOG相对GRPO在几何推理平均提升3.5-4.1点，在视觉定位上避免纯熵优化的崩溃，且额外计算开销低于1%。其边界在于：所有验证限于小模型与子集基准，隐藏状态相似度作为视觉接地代理的有效性未在大模型或跨模态冲突条件下检验。当模型规模扩展至7B以上时，隐藏状态空间中视觉与语言表示的分离度是否足以支撑Token级区分，这一前提假设尚未被实验证实。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22847)