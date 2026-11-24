# ICLR2026最新论文 ｜Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute ｜蛋白结合剂原子级生成与推理时计算扩展

研究机构：英国牛津大学、韩国首尔大学

作者：Kieran Didi、Zuobai Zhang、Guoqing Zhou 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27950)

> 蛋白结合剂设计需在巨大序列-结构空间中生成物理稳定且具备特定结合功能的分子，现有方法受限于训练数据稀缺或推理时优化缺乏生成先验。本文指出“生成式”与“幻觉式”设计是虚假二分法，提出 Proteína-Complexa 框架，通过构建大规模合成数据集 Teddymer 训练原子级流匹配基础模型，并引入推理时计算扩展算法统一生成与优化。该框架在多个基准上刷新了计算成功率，但其性能高度依赖结构预测器作为奖励函数的准确性，且未涉及湿实验闭环验证。

## 研究背景

蛋白结合剂设计面临的核心困境在于，实验解析的多聚体结构（PDB）数据量有限，难以支撑大规模生成模型的训练。为突破数据瓶颈，AlphaFold Database (AFDB) 提供了海量单链预测结构，但这些单链无法直接提供结合剂-靶标对的相互作用信息。结构域（Domain）作为蛋白质的独立折叠单元，其间的相互作用在生物物理性质上近似于多聚体链间相互作用，这为从单链数据中挖掘结合信息提供了可能。

当前结合剂设计方法分为两类：生成式方法（如 RFDiffusion）将设计视为条件生成任务，但受限于训练数据规模，生成多样性与成功率受限；幻觉式方法（如 BindCraft）利用结构预测器的置信度分数通过梯度反馈优化序列，无需训练生成器，但缺乏生成先验，导致在复杂靶标上优化效率低且计算成本高。Proteína-Complexa 的切入点在于打破这一二分法，借鉴自然语言处理与视觉生成领域的“推理时计算扩展”范式，将强大的生成先验与推理时搜索结合，实现高效可控的原子级结合剂设计。

## 核心方法

### 方法参照系

本文基于 La-Proteína 的部分潜变量流匹配框架。该框架通过变分自编码器（VAE）将蛋白原子坐标与氨基酸身份编码为连续潜变量 $z$ 与 $\alpha$-碳坐标 $\mathbf{x}_{[C][\alpha]}$，联合去噪生成全原子结构。与 La-Proteína 生成单链不同，本文需引入靶标条件，且需解决推理时计算效率问题。

### 潜变量靶标条件化与翻译噪声

**设计动机**：传统条件生成中，靶标特征直接拼接易导致模型忽略结合剂的全局定位，且单链预训练模型缺乏多聚体定位能力。
本文修改去噪器，将靶标的 Atom37 坐标、氨基酸身份及热点标记嵌入为条件向量 $\mathbf{c}_{[target]}$，与结合剂的噪声嵌入 $\mathbf{x}_{[C][\alpha]}, \mathbf{z}$ 在 Token 维度拼接，通过 Pair-biased Attention 联合处理。为强制模型学习结合剂在界面的全局定位，引入翻译噪声 $\vec{d}$：

$$ \mathbf{x}_{[C]_{t_x}[\alpha]} = t_x \mathbf{x}_{[C][\alpha]} + (1 - t_x)(\mathbf{x}_{[C]_0[\alpha]} + \vec{d}) $$

其中 $\vec{d} \sim \mathcal{N}(\vec{0}, c_d^2 I_{xyz})$。该噪声迫使模型在生成初期即修正结合剂的全局位置，而非仅优化局部构象，显著提升了界面定位的准确性。

### 推理时计算扩展

**设计动机**：单次生成成功率有限，且幻觉式方法缺乏生成先验导致搜索空间盲目。
本文引入 Beam Search、Feynman-Kac Steering (FKS) 和 Monte Carlo Tree Search (MCTS) 等算法，在去噪过程中利用结构预测器（如 AlphaFold2-Multimer）的 ipAE 分数或氢键数作为奖励 $R(\mathbf{x}, \mathbf{s})$。以 Beam Search 为例，在去噪步 $t$，对每个状态生成 $L$ 个候选，Rollout 至 $t=1$ 计算奖励，保留 Top-$N$ 状态继续去噪：

$$ p(c) = \frac{\exp\{\beta R(c)\}}{\sum_{c' \in C} \exp\{\beta R(c')\}} $$

该机制将生成过程转化为受奖励引导的搜索过程，利用生成先验缩小搜索空间，比纯幻觉优化更高效地找到高质量结合剂。

## 实验评估

实验在 19 个蛋白靶标、4 个小分子靶标及 41 个酶设计任务上进行，基线包括 RFDiffusion、Protpardelle、APM（生成式）及 BindCraft、BoltzDesign（幻觉式）。Complexa 在蛋白靶标上平均 Unique Successes 达 9.10（Self），远超 RFDiffusion 的 4.68（MPNN）；在小分子靶标 IAI 上达 19，优于 RFDiffusionAA 的 8。

| 模型 | 蛋白靶标 Unique Successes (Self) | 小分子 IAI Unique Successes (Self) | 酶设计成功率 (Self) |
| :--- | :--- | :--- | :--- |
| RFDiffusion | 4.68 (MPNN) | 8 (MPNN) | 30/41 (MPNN-8) |
| Complexa | 9.10 | 19 | 41/41 |

消融实验显示，移除 Teddymer 数据后，Unique Successes 从 9.10 骤降至 0.15，证明合成数据对模型泛化至关重要；移除翻译噪声后，成功率从 9.10 降至 1.47，验证了全局定位学习的重要性。在推理时扩展中，Best-of-N 在简单靶标上表现最佳，而 Beam Search 和 MCTS 在困难靶标上优势明显，表明搜索算法的必要性随靶标难度增加。

评估边界方面，指标依赖 AlphaFold2-Multimer 的 ipAE 分数，若预测器对特定靶标存在系统性偏差，奖励函数将失效。论文未报告湿实验验证结果，且未对比 ESM All-Atom 等纯 PLM 基线。代码、模型权重及 Teddymer 数据集将公开，超参数详见 Table 14，训练使用 96 块 A100 GPU。

## 关联研究分析

从问题动机看，Complexa 与 BindCraft 均旨在提升结合剂设计成功率，但 BindCraft 依赖梯度优化序列，缺乏生成先验，导致在复杂靶标上计算成本高且易陷入局部最优。Complexa 通过生成先验引导搜索，将优化过程嵌入生成轨迹，实现了“生成-优化”闭环。这一差异源于任务特性：结合剂设计需要同时满足结构稳定性与界面特异性，纯优化方法难以平衡两者，而生成式先验提供了物理合理的初始分布。

从方法设计看，Complexa 与 RFDiffusion 同属生成式路线，但 RFDiffusion 仅生成骨架，需依赖 ProteinMPNN 进行序列重设计，导致结构-序列一致性受损。Complexa 采用全原子生成，直接输出序列与坐标，避免了重设计步骤。此外，Complexa 引入的推理时计算扩展在 RFDiffusion 中缺失，后者仅依赖单次采样或简单重设计，无法在推理阶段动态调整生成策略。这种设计差异使得 Complexa 在困难靶标上具有显著优势，但也引入了对结构预测器奖励函数的依赖。

## 总结

Proteína-Complexa 解决了结合剂设计中数据稀缺与推理效率低下的矛盾，通过构建 Teddymer 合成数据集训练原子级流匹配模型，并引入推理时计算扩展统一生成与优化。该框架在蛋白、小分子及酶设计基准上刷新了 SOTA，蛋白靶标 Unique Successes 达 9.10，酶设计成功率 41/41。然而，其性能高度依赖结构预测器作为奖励函数的准确性，且未涉及湿实验闭环验证。当靶标结构高度动态或预测器置信度低时，推理时搜索是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27950)