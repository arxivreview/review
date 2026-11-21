# HuggingFace最新推荐论文 ｜DrugGen 2: A disease-aware language model for enhancing drug discovery ｜疾病条件化分子生成模型

作者：Ali Motahharynia、Mohammadreza Ghaffarzadeh-Esfahani、Mahsa Sheikholeslami 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.08404)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.08404)

> 现有药物生成模型通常仅以靶点蛋白序列为条件，忽略了同一靶点在不同疾病状态下因微环境差异导致的结合特异性变化，导致生成的分子在特定病理场景中失效。DrugGen-2 通过引入医学主题词（MeSH）层级结构作为疾病本体条件，填补了疾病语境下的分子设计空白。该模型基于预训练 GPT-2，采用监督微调（SFT）与组相对策略优化（GRPO）两阶段训练策略，在糖尿病肾病相关靶点上实现了优于基线的唯一性生成与结合亲和力。尽管其序列生成范式在化学有效性上表现稳健，但缺乏三维空间坐标的显式建模，限制了其对立体化学互补性的精确捕捉。

## 研究背景

当针对同一蛋白靶点（如 PPARγ）设计药物时，其在 2 型糖尿病中的代谢获益与在结肠癌中的潜在风险源于疾病特异性通路（如 Wnt/β-catenin）的交互差异。这种“同靶点不同病”的现象要求生成模型不仅理解靶点序列，还需感知疾病本体（Disease Ontology）。传统基于靶点的生成方法（Target-based Generation）将输入简化为氨基酸序列，丢失了病理上下文信息，导致生成的分子虽能结合靶点，却可能无法适应特定疾病状态下的构象或微环境需求。

主流序列生成路线（如 Mol-LLM、DrugGPT）依赖大语言模型处理 SMILES 字符串，虽能捕捉结构-性质关系，但普遍缺乏疾病条件化机制。现有强化学习微调方法（如 DrugGen）多采用 PPO 算法，需维护独立的价值函数，计算开销大且易出现策略偏移。此外，多数模型在生成阶段仅优化化学有效性，对新颖性与多样性的平衡不足，导致输出高度重复。DrugGen-2 的切入点在于将 MeSH 有向无环图（DAG）编码与靶点序列联合作为条件输入，并引入 GRPO 算法替代 PPO，通过组内统计量计算优势函数，在降低显存占用的同时，通过多目标奖励函数协同优化结合亲和力、新颖性与多样性。

## 核心方法

### 序列生成参照系

本文问题属于基于序列的分子生成（Sequence-based Molecular Generation），其标准流程为：以靶点序列为条件，利用自回归语言模型生成 SMILES 字符串。与通用序列生成不同，本文的关键差异在于条件输入扩展为“MeSH DAG + 蛋白序列”，且训练目标从单一的语言建模损失扩展为包含物理化学属性的多目标强化学习优化。

### 疾病本体条件化输入

为将疾病语境注入生成过程，DrugGen-2 将 MeSH 术语映射为层级 DAG 结构，并与蛋白序列拼接为统一提示词。设计动机在于解决静态靶点假设导致的疾病特异性缺失：同一靶点在不同疾病中可能涉及不同的功能域或结合模式，MeSH DAG 提供了从器官系统到具体病理的层级上下文。输入格式定义为：

$$ \text{Input} = \langle \text{start} \rangle + \langle D \rangle + \text{MeSH\_DAG} + \langle P \rangle + \text{Sequence} + \langle L \rangle + \text{SMILES} + \langle \text{end} \rangle $$

其中 $\langle D \rangle, \langle P \rangle, \langle L \rangle$ 为特殊分隔符。该设计使模型在解码 SMILES 时，能够隐式对齐疾病层级信息，从而生成更符合特定病理需求的分子骨架。

### GRPO 强化学习优化

SFT 阶段仅使模型对齐领域数据分布，无法直接优化结合亲和力等物理属性。DrugGen-2 引入 GRPO 替代传统 PPO，其核心创新在于消除价值函数，利用组内输出统计量计算优势。对于每个提示 $q$，采样 $G$ 个输出 $\{o_i\}_{i=1}^G$，目标函数为：

$$ J_{\text{GRPO}}(\theta) = \mathbb{E}_{q \sim P(Q), \{o_i\} \sim \pi_{\theta_{\text{old}}} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \left( \text{clip}\left( \frac{\pi_\theta(o_{i,t} | q, o_{i,<t})}{\pi_{\theta_{\text{old}}}(o_{i,t} | q, o_{i,<t})}, 1-\epsilon, 1+\epsilon \right) \hat{A}_{i,t} - \beta D_{\text{KL}}[\pi_\theta \| \pi_{\text{ref}}] \right) \right] $$

其中 $\hat{A}_{i,t}$ 为基于组内平均奖励计算的优势值，$\beta$ 为 KL 散度惩罚系数。奖励函数 $R$ 由三部分加权组成：PLAPT 预测的结合亲和力（无效分子奖励为 0）、相对于批准药物的二元新颖性奖励、以及批次内唯一性奖励。该机制通过抑制重复输出并引导策略向高亲和力区域探索，解决了 SFT 模型生成多样性不足的问题。

## 实验评估

实验基于糖尿病肾病（DN）相关的五个靶点（ACE, PPARγ, NOS3, PAI-1, TGF-β1）进行评估，对比基线为 DrugGPT（无 RL）与 DrugGen（PPO 微调）。基线覆盖审计显示，本文仅对比了序列生成路线的前作，未包含 3D 生成基线（如 Pocket2Mol）或最新离散扩散模型（如 MolHIT），限制了跨范式比较的有效性。

| 指标 | DrugGen-2 | DrugGen | DrugGPT |
| :--- | :--- | :--- | :--- |
| 唯一生成数 (500次) | 409–444 | 50 | 219 |
| 结合亲和力中位数 (pKd) | 9.26–9.97 | 7.15–8.49 | 5.86–6.22 |
| 相似度中位数 | 0.70 | 0.64 | 0.30 |
| 化学有效性 (%) | 99–100 | - | - |

在 ACE 靶点上，生成配体 P12821-293 的 GLIDE XP 对接分数为 -9.917 kcal/mol，优于参考药 Enalapril 的 -8.283 kcal/mol；但在 PPARγ 上，生成配体未超越参考药 Rosiglitazone（-7.422 kcal/mol）。消融分析表明，GRPO 阶段显著提升了唯一生成数（从 SFT 后的较低水平提升至 400+），且奖励曲线在 10 个 epoch 内收敛，表明多目标奖励未发生严重冲突。

评估边界方面，本文仅使用 PLAPT 预测亲和力与 GLIDE 对接分数，缺乏湿实验验证；蛋白序列截断至 768 tokens 可能丢失远端变构域信息；二元新颖性奖励可能低估对已知骨架的细微改进。代码与数据已公开，但 GPU 资源需求未明确报告。

## 关联研究分析

从问题动机看，DrugGen-2 与 SculptDrug 代表了序列生成与 3D 几何生成的两条分叉路径。SculptDrug 通过空间条件感知贝叶斯流模型显式建模原子坐标，旨在解决立体化学互补性；而 DrugGen-2 仅处理 1D SMILES，其疾病条件化依赖于 MeSH 文本语义，而非空间几何约束。这种差异源于任务特性：序列生成更易于整合大规模文本本体数据，但牺牲了空间精度。DrugGen-2 未验证 1D 序列是否足以捕捉疾病特异性的立体结合模式，这是其与 3D 方法的核心分歧。

从方法设计看，DrugGen-2 与 MolHIT 同属序列生成，但优化策略截然不同。MolHIT 采用层级离散扩散，通过掩码去噪逐步细化结构，侧重化学有效性的稳定性；DrugGen-2 采用 GRPO 强化学习，侧重结合亲和力与多样性的优化。MolHIT 的扩散过程是概率性的，而 GRPO 是策略梯度的，前者在训练稳定性上可能更优，但后者在特定目标（如高亲和力）的定向优化上更具优势。DrugGen-2 未对比扩散模型在序列生成中的表现，无法判断 RL 微调是否优于扩散采样在保持有效性的同时提升亲和力的效率。

## 总结

DrugGen-2 旨在解决同一靶点在不同疾病状态下结合特异性差异导致的分子设计偏差，其切入点在于将 MeSH 疾病本体作为条件输入，弥补了纯靶点序列生成的语境缺失。通过 SFT 对齐领域数据并引入 GRPO 优化多目标奖励，模型在糖尿病肾病靶点上实现了 409–444 的唯一生成数与 9.26–9.97 的结合亲和力中位数，显著优于 DrugGPT 与 DrugGen。然而，其边界在于仅依赖 1D SMILES 表示，缺乏 3D 坐标的显式建模，且蛋白序列截断可能丢失关键变构信息。当 MeSH 层级深度增加或靶点序列超过 768 tokens 时，疾病语境与空间信息的丢失对生成质量的负面影响程度，论文未给出量化回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.08404)