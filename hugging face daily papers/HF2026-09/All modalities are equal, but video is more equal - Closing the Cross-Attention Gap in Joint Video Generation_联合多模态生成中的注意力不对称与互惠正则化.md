# HuggingFace最新推荐论文 ｜All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation ｜联合多模态生成中的注意力不对称与互惠正则化

作者：Ohad Rahamim、Dvir Samuel、Idan Schwartz 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.27901)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.27901)

> 联合多模态生成旨在让视频与伴随模态（如动作、音频）在去噪过程中相互约束，但现有模型常出现“架构双向、信息单向”的失效，导致生成结果内部一致性差。本文发现预训练模型中视频到模态的注意力远强于反向路径，提出 RecCAR 这一轻量级 KL 正则化策略，利用强路径作为弱路径的内部监督目标。该方法在不改变架构的前提下提升了跨模态一致性，但其效果是否依赖特定骨干的注意力分布形态，仍存疑。

## 研究背景

联合多模态生成要求视频 $V$ 与伴随模态 $M$ 在同一扩散或流匹配过程中交互。Transformer 块内的交叉注意力提供了 $V \to M$ 与 $M \to V$ 两条信息通路，理论上允许双向约束。然而，标准生成目标仅优化去噪误差，不约束每条通路携带的信息量，导致模型可能过度依赖其中一条路径而忽略另一条。这种不对称性使得一个模态无法有效纠正另一个模态的不一致，削弱了联合生成相对于级联流水线的核心优势。

早期研究多将动作或音频作为固定条件输入视频生成器，或采用级联方式先生成视频再预测其他模态。随着扩散 Transformer（DiT）的普及，EchoMotion、LTX-2 等模型实现了真正的联合去噪，但均默认双向注意力能自动平衡信息流。现有后训练对齐方法如 ITS 通过迭代优化同步指标，但未触及注意力机制内部的结构性偏差。本文切入点在于识别出这种“功能不对称”是预训练模型的固有属性，而非训练数据不足所致，并证明强路径中已包含弱路径所需的监督信号。

## 核心方法

### 方法参照系

本文问题属于联合生成中的后训练对齐范畴，标准流程通常通过外部奖励或额外数据微调生成损失。关键差异在于，RecCAR 不引入外部监督，而是将模型内部已有的强注意力分布转化为弱路径的训练目标，实现了自监督式的结构对齐。

### 互惠对应差距定义

设计动机在于量化双向注意力的失衡程度，为正则化提供可优化的标量指标。对于 Transformer 块 $\ell$，视频与模态的预 softmax 兼容性分数分别为 $S^{(\ell)}_{V \to M}(j, i)$ 和 $S^{(\ell)}_{M \to V}(i, j)$。为消除归一化维度差异，本文将两个方向的注意力均重新归一化为视频 token 上的分布：

$$ C^{(\ell)}_{V \to M}(i | j) = \text{softmax}_i S^{(\ell)}_{V \to M}(j, i) $$

$$ C^{(\ell)}_{M \to V}(i | j) = \text{softmax}_i S^{(\ell)}_{M \to V}(i, j) $$

该公式将两个方向统一为“模态 token $j$ 对应哪些视频 token”的概率分布，使得二者可直接比较。互惠对应差距定义为所有层和头部的 KL 散度均值：

$$ \Delta^{corr}_{V,M} = \frac{1}{|R|N_M} \sum_{\ell \in R} \sum_{j=1}^{N_M} D_{KL} \left( C^{(\ell)}_{V \to M}(\cdot | j) \middle\| C^{(\ell)}_{M \to V}(\cdot | j) \right) $$

该指标衡量了两个方向在空间对应关系上的分歧程度，值越大表示不对称性越严重。

### 方向性 KL 正则化

设计动机在于利用强路径的稳定性来引导弱路径，避免双向同时优化导致的震荡。RecCAR 将 $V \to M$ 分布设为固定参考（stop-gradient），仅优化 $M \to V$ 路径向其对齐：

$$ \mathcal{L}_{RecCAR} = \frac{1}{|R|N_M} \sum_{\ell \in R} \sum_{j=1}^{N_M} D_{KL} \left( \text{sg}[C^{(\ell)}_{V \to M}(\cdot | j)] \middle\| C^{(\ell)}_{M \to V}(\cdot | j) \right) $$

总损失为 $\mathcal{L}_{total} = \mathcal{L}_{gen} + \lambda_{RecCAR} \mathcal{L}_{RecCAR}$，其中 $\mathcal{L}_{gen}$ 为原始去噪目标。通过 LoRA 微调注意力投影层，该方法在不改变骨干参数的前提下，将强路径中已学习到的跨模态结构迁移至弱路径，使推理时双向信息流均能有效参与约束。

## 实验评估

实验在 VBench（视频-动作）、T2AV-Compass 和 AVGen-Bench（视频-音频）上进行，基线覆盖 EchoMotion、CoMoVi、FlowMo 及 LTX-2、JavisDiT++ 等主流联合生成模型，但未包含 BAGEL 等统一理解生成模型，因任务性质不同不可比。

| 方法 | Human Anatomy | Motion Smoothness | Dynamic Degree | Aesthetic Quality |
|---|---|---|---|---|
| EchoMotion | 0.70 | 0.98 | 0.85 | 0.56 |
| EchoMotion + RecCAR | 0.78 | 0.99 | 0.85 | 0.57 |
| CoMoVi | 0.9208 | 0.9802 | 0.2184 | 0.43 |
| FlowMo | 0.9339 | 0.9883 | 0.2647 | 0.62 |

RecCAR 在 Human Anatomy 上从 0.70 提升至 0.78，同时保持动态度与美学质量不变，表明改进源于跨模态一致性而非运动简化。

| 方法 | AV Desync (Abs.) | CLAP | AV-CLIP |
|---|---|---|---|
| LTX-2 | 0.804 | 0.22 | 0.74 |
| LTX-2 + RecCAR | 0.752 | 0.22 | 0.74 |
| JavisDiT++ | 1.078 | 0.21 | 0.72 |
| JavisDiT++ + RecCAR | 1.046 | 0.23 | 0.74 |

消融实验显示，标准微调在相同数据上不仅未降低 AV Desync，反而使 N-MPJPE 和 Human Anatomy 恶化，证明增益特异性来自 RecCAR 正则化而非额外训练。评估边界方面，论文未报告生成多样性指标，且仅在两个特定骨干上验证，未测试离散 Token 化架构下的适用性。代码未公开，但提供了 LoRA 秩 128、学习率 1e-5、48 GPU-hours 等完整超参数，具备可复现性基础。

## 关联研究分析

从问题动机看，RecCAR 与 ITS 均针对音视频同步问题，但 ITS 通过迭代优化外部同步指标，属于黑盒优化；RecCAR 则直接干预注意力机制内部结构，属于白盒正则化。ITS 在 LTX-2 上仅带来边际改善，而 RecCAR 显著降低 Desync，根源在于同步问题本质是注意力对应关系错位，而非单纯的时间偏移。这种机制差异暗示，对于依赖空间对应关系的任务（如动作-视频），注意力对齐可能比时间同步优化更有效。

从方法设计看，RecCAR 与知识库中提到的“后训练对齐”路线一致，但区别于 RecA 等依赖重构对齐的方法。RecA 需要外部重构目标，而 RecCAR 利用模型内部已有的强路径作为监督，无需额外标注。这一设计选择源于联合生成模型中强路径已包含充分跨模态信息的假设，但该假设在弱预训练模型中是否成立，论文未给出验证。与 Transfusion 等混合架构相比，RecCAR 不改变架构复杂度，仅增加轻量级正则项，更适合已有大规模预训练模型的增量优化。

## 总结

本文核心矛盾在于联合生成模型架构双向但信息流单向，导致跨模态一致性不足。现有方法如 ITS 仅优化外部指标，未触及注意力内部结构；RecCAR 抓住强路径已含弱路径监督信号这一被忽略的点，提出方向性 KL 正则化。实验证明该方法在视频-动作和视频-音频任务上均有效，Human Anatomy 从 0.70 升至 0.78，AV Desync 从 0.804 降至 0.752。其边界在于仅验证了连续潜空间 DiT 架构，未测试离散 Token 化模型，且未报告多样性指标。当预训练模型的强路径本身存在偏差时，RecCAR 是否会放大这种偏差而非纠正，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.27901)