# Neurocomputing2026最新论文 ｜Odin: Oriented Dual-module Integration for Text-rich Network Representation Learning ｜Odin：层级对齐的双模块融合架构

作者：Kaifeng Hong、Yinglong Zhang、Xiaoying Hong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.21416)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.21416)

> 文本属性图（TAGs）建模面临图神经网络（GNN）浅层结构与预训练语言模型（PLM）深层语义的层数不匹配困境，导致高阶结构信息无法有效注入深层语义空间。现有 LLM-as-Aligner 方法因参数共享导致刚性注入，且受限于单跳邻域，难以捕捉多跳结构线索。Odin 通过解除参数共享约束，将阶段特异性 GNN 聚合层与简单聚合层交替插入 Transformer 的关键与非关键深度，实现结构抽象与语义层级的精准对齐。该框架在标准基准上优于部分基线，但受限于 BERT 骨干网络，其性能上限低于当前基于大语言模型（LLM）的原生架构 SOTA。

## 研究背景

理解本文需厘清 TAGs 建模中的深度鸿沟。GNN 通过消息传递提取拓扑结构，但为避免过平滑，通常仅使用 2-3 层，导致其感知范围局限于低阶邻域。PLM 则依赖 12 层以上的 Transformer 堆叠，从浅层词汇关联逐步抽象至深层全局语义。这种结构深度（M）远小于语义深度（L）的错位，使得在 PLM 深层注入结构信息时，要么因过早注入被后续文本编码稀释，要么因过晚注入缺乏足够的结构上下文支持。

TAGs 研究旨在融合拓扑与文本，主流范式分为 LLM-as-Enhancer、LLM-as-Predictor 和 LLM-as-Aligner。其中，LLM-as-Aligner 试图在统一架构内联合建模，代表工作 GraphFormers 和 Patton 将 GNN 模块嵌入 Transformer 层间。然而，这些方法存在两个核心缺陷：一是所有 Transformer 层共享同一组 GNN 参数，导致结构注入方式僵化，无法适应不同语义层级的需求；二是为控制计算成本，通常仅部署单跳 GNN，使得高阶结构信息缺失，无法为深层 Transformer 提供必要的多跳语境线索。Odin 的切入点在于打破参数共享约束，提出“层级对齐”策略，即根据结构抽象的阶数（低、中、高）将其分别注入到 Transformer 的浅、中、深层，以解决深度不匹配与刚性注入问题。

## 核心方法

### 方法参照系

Odin 属于 LLM-as-Aligner 范式，其标准流程是在 Transformer 层间插入 GNN 模块以融合结构信息。与 GraphFormers 等基线不同，Odin 的关键差异在于摒弃了全局参数共享，采用“TG 层”（Text-Graph Fusion）与“TS 层”（Text-Simple Aggregation）交替出现的层级化设计，并引入阶段特异性参数。

### 层级对齐的双模块架构

Odin 的核心创新在于将结构注入位置与 Transformer 的语义层级进行一一对应。设计动机是解决传统方法中结构信息在深层被稀释或浅层缺乏高阶线索的问题。Odin 包含 $L$ 层，其中 $M$ 层为 TG 层，其余为 TS 层。在 TG 层，节点表示 $T_v^{[l]}$ 的 [CLS] 令牌通过阶段特异性 GNN 卷积聚合邻居信息，生成增强令牌 $\text{agg}_v^{[l]}$，其计算公式为：

$$ \text{agg}_v^{[l]} = W_1^{[l]} \cdot \text{mean}_{j \in N(v)} T_j^{[l]} + W_2^{[l]} \cdot T_v^{[l]} $$

该公式表明，每个 TG 层拥有独立的权重矩阵 $W_1^{[l]}$ 和 $W_2^{[l]}$，使得不同深度的结构聚合能够针对该层特定的语义抽象级别进行优化，而非使用统一的浅层聚合逻辑。生成的 $\text{agg}_v^{[l]}$ 与原始令牌拼接后进入下一层文本编码，实现了结构信息在特定语义深度的精准注入。

### 轻量级变体与简单聚合机制

为平衡效率与性能，Odin 在非关键层引入 TS 层，使用简单聚合（Simple Aggregation）替代 GNN 卷积。设计动机是避免在所有层都进行昂贵的 GNN 计算，同时保持结构信息的连续引导。TS 层的聚合过程为：

$$ \text{agg}_v^{[l]} = \text{SimpleAggregate}(T_v^{[l]}, \{T_j^{[l]} \mid j \in N(v)\}) $$

这种轻量级设计允许模型在保持全阶段结构引导的同时，显著降低计算开销。Light Odin 进一步将 Transformer 层数压缩至 6 层，通过保留层级对齐的核心逻辑，在大幅减少参数规模（约 60%）的情况下，维持了超过 85% 的性能，解决了大规模 TAGs 部署中的效率瓶颈。

## 实验评估

实验在 Cora、CiteSeer、ArXiv2023 等五个数据集上进行，任务涵盖节点分类与链接预测。基线覆盖 PLM（如 BERT、SciBERT）、GNN（如 GraphSAGE）及融合模型（如 Patton、LLaGA）。值得注意的是，基线中未包含当前领域基于 LLM 原生架构的 SOTA 方法（如 TAG-DLM、NAG），这限制了性能上限的对比。

| 方法 | Cora 分类 (ACC) | Cora 链接预测 (PREC) | CiteSeer 分类 (ACC) |
| :--- | :--- | :--- | :--- |
| Odin PG | 0.724±0.009 | 0.783±0.031 | 0.571±0.01 |
| Odin ME | 0.677±0.02 | 0.744±0.007 | 0.677±0.02 |
| Patton | 0.758±0.02 | 0.814±0.02 | 0.608±0.01 |
| GraphSAGE | 0.348±0.03 | 0.162±0.03 | 0.507±0.08 |

Odin PG 在 Cora 链接预测上达到 0.783，优于 GraphSAGE 的 0.162，但低于 Patton 的 0.814。在 CiteSeer 上，Odin ME 的分类准确率 0.677 高于 Patton 的 0.608，但论文指出 Patton 在稀疏图（平均度 1.34）上表现更优，归因于 Odin 的多跳采样在稀疏结构下难以获取足够子图。

消融实验显示，TG 层的位置对性能影响显著。在 12 层配置中，TG 层位于 [1,4,8,11] 时链接预测 PREC 最高（0.796），而位于 [1,2,3] 时仅为 0.735。这表明均匀分布的结构注入优于集中于浅层或深层。简单聚合策略中，PG（Parameterized Graph）策略在 TG 层表现最佳，而 TS-ALL 3jump（全简单聚合）性能骤降至 0.423，证明 GNN 卷积在关键层不可替代。

评估边界方面，论文未报告置信区间以外的统计显著性检验，且未提供 GPU 型号与训练时长等复现细节。代码已开源，但超参数搜索范围未完全披露。

## 关联研究分析

从方法设计看，Odin 与 GraphFormers 和 Patton 同属 LLM-as-Aligner 路线，但核心差异在于参数共享机制。GraphFormers 和 Patton 采用全局共享 GNN 参数，导致结构注入方式在所有层一致，无法适应 Transformer 从浅层词汇到深层语义的抽象变化。Odin 通过阶段特异性参数，允许不同深度的结构聚合具有不同的归纳偏置，从而解决了刚性注入问题。然而，Odin 仍依赖外部 GNN 模块，而 NAG 等原生架构通过修改自注意力机制直接注入拓扑，避免了外部编码器的概念割裂。Odin 的改进是否足以弥补与原生架构在零样本泛化上的差距，论文未给出回答。

从问题动机看，Odin 聚焦于静态图上的层级对齐，而领域共识指出零样本与少样本学习是重要方向。Odin 使用 BERT 作为骨干，其语义推理能力弱于 LLaMA 等 LLM，这限制了其在跨域迁移任务上的潜力。相比之下，UniGTE 等基于 LLM 的方法在零样本任务上表现更优。Odin 的层级对齐策略在标签充足场景下有效，但在标签稀缺场景下，其依赖多跳采样的结构获取方式可能因数据稀疏而失效，这一局限性在 CiteSeer 实验中得到体现。

## 总结

Odin 旨在解决 TAGs 建模中 GNN 浅层结构与 PLM 深层语义的层数不匹配问题，通过层级对齐的双模块架构，将阶段特异性 GNN 聚合与简单聚合交替插入 Transformer，实现了结构抽象与语义层级的精准匹配。实验表明，Odin 在 Cora 链接预测上达到 0.783，优于 GraphSAGE 但低于 Patton，且在 CiteSeer 稀疏图上表现不及 Patton。其边界在于依赖 BERT 骨干，限制了语义推理深度，且多跳采样在稀疏图下效率低下。当图结构极度稀疏时，Odin 的层级对齐策略是否仍能维持性能优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.21416)