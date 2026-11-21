# HuggingFace最新推荐论文 ｜Pythagoras-Prover: Advancing Efficient Formal Proving via Augmented Lean Formalisation ｜增强形式化证明：Pythagoras-Prover 与 ALF 数据增强

研究机构：英国帝国理工学院、英国爱丁堡大学

作者：Joshua Ong Jun Leang、Zheng Zhao、Mihaela Cătălina Stoian 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.12594)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.12594)

> 导读 形式化定理证明的核心矛盾在于，大语言模型（LLM）的生成能力与交互式定理证明器（ITP）的严格验证之间存在算力鸿沟，现有高性能模型往往依赖数百亿参数或昂贵的推理时搜索。Pythagoras-Prover 的切入点在于，通过构建经 Lean 验证的种子语料库并引入增强 Lean 形式化（Augmented Lean Formalisation, ALF）机制，以数据效率替代模型规模扩张。该方法通过课程学习、动态过滤与自蒸馏，在 4B 和 32B 参数规模下实现了开源非智能体模型的性能突破。其价值在于证明了小模型通过数据增强可超越大模型基线，但 ALF 变体的逻辑等价性依赖轻量级检查，其鲁棒性边界尚待更严苛的验证。

## 研究背景

当 LLM 生成形式化证明时，自然语言推理的幻觉无法被人工审查可靠捕捉，必须依赖 Lean 等 ITP 内核的确定性类型检查器进行机器验证。这一验证机制确立了正确性标准，但也引入了算力瓶颈：长程推理链导致监督微调（SFT）与采样成本高昂，而验证器吞吐量限制了高质量证明数据的规模。为突破数据稀缺与算力限制，研究者通常采用大规模预训练或推理时搜索策略，但这使得高性能证明器难以在有限算力下部署。

现有主流路线存在显著瓶颈。DeepSeek-Prover-V2 等模型依赖 671B 参数规模，Goedel-Prover-V2 则采用推理时自修正与大规模采样预算，两者均将性能提升建立在算力扩张之上。智能体框架如 Hilbert 通过多轮工具调用提升研究级定理成功率，但推理延迟高且架构复杂。这些方法共同假设“更强形式化推理需要前沿规模模型”，忽视了数据质量与训练效率对性能的决定性作用。Pythagoras-Prover 的切入点在于，通过结构化数据增强与参数高效微调，在保持 Lean 验证正确性的前提下，将性能提升从“模型规模”转向“数据效率”，挑战了算力决定论的隐含共识。

## 核心方法

### 方法参照系

本文问题属于“强化学习训练”与“数据工程”混合路线，与 DeepSeek-Prover 等大规模模型路线的关键差异在于：不依赖全参数训练或推理时搜索，而是通过 Lean 验证的种子语料库与 ALF 变体生成，在 8K 上下文预算内实现高效 SFT 与 RL 训练。

### 动态证明-推理过滤

在 SFT 阶段，8K 上下文预算对长推理链构成硬约束，传统截断或丢弃策略会损失关键推理信息。Pythagoras-Prover 引入动态证明-推理过滤机制，根据推理链与形式化证明的长度关系决定训练样本构成：

$$
\text{Training Sample} = \begin{cases}
\text{Reasoning} + \text{Proof} & \text{if } L_{\text{reasoning}} + L_{\text{proof}} \leq 8192 \\
\text{Proof} & \text{if } L_{\text{reasoning}} + L_{\text{proof}} > 8192 \text{ and } L_{\text{proof}} \leq 8192 \\
\text{Discard} & \text{if } L_{\text{proof}} > 8192
\end{cases}
$$

该公式确保在预算内保留最大信息量：当推理链与证明均可容纳时，完整序列提供推理轨迹；当推理链过长时，仅保留证明以维持形式化正确性；当证明本身超预算时，丢弃实例以避免噪声。这一设计解决了固定截断导致的推理链断裂问题，使 4B 模型在 MiniF2F-Test 上达到 86.1% 的 pass@32 准确率，超越 671B 基线 3.6 个百分点。

### 增强 Lean 形式化（ALF）

种子语料库规模受限于验证器吞吐量，ALF 通过结构化变异扩展数据分布，避免逐实例 Lean 验证的计算开销。对每个验证实例，ALF 生成五种变异类型：简化、泛化、引理提议、证明步骤分解与重构，使用轻量级 sanity check 而非完整 Lean 验证：

$$
\mathcal{D}_{\text{ALF}} = \bigcup_{i=1}^{5} \text{Mutate}_i(\mathcal{D}_{\text{seed}}) \quad \text{s.t. } \text{SanityCheck}(\text{Mutate}_i(x)) = \text{True}
$$

该公式表明 ALF 变体仅通过轻量级检查保证形式正确性，而非 Lean 编译验证，从而将语料库规模扩展约 2.5 倍。这一设计解决了验证器吞吐量瓶颈，使自蒸馏阶段获得更丰富的训练信号，同时通过 MiniF2F-ALF 基准验证了模型对形式变体的鲁棒性。

## 实验评估

实验在 MiniF2F-Test、PutnamBench 与 MiniF2F-ALF 上进行，基线覆盖 DeepSeek-Prover-V2、Goedel-Prover-V2 与 Kimina-Prover，但遗漏了智能体框架代表 Hilbert。主实验结果如下：

| 方法 | 参数量 | MiniF2F-Test Pass@32 | PutnamBench 解题数 |
|---|---|---|---|
| Pythagoras-Prover-4B | 4B | 86.1 | 48 (Pass@32) |
| Pythagoras-Prover-32B | 32B | 89.8 | 93 (Pass@2048) |
| DeepSeek-Prover-V2-671B | 671B | 82.4 | 47 (Pass@1024) |
| Goedel-Prover-V2-32B | 32B | 88.1 | 86 (Pass@184, 自修正) |

Pythagoras-Prover-4B 在 MiniF2F-Test 上超越 671B 基线 3.6 个百分点，32B 模型在 PutnamBench 上以 93 题超越 Goedel-Prover-V2 的 86 题，但后者使用了自修正机制。消融实验显示，动态过滤机制相比朴素截断提升了 SFT 性能，ALF 变体在 MiniF2F-ALF 上使所有评估模型准确率下降，表明性能未完全迁移至形式变体。

评估协议使用 Lean 4.9.0-rc1，证明正确性要求编译无错且目标陈述逐字匹配。可复现性方面，论文提供 HuggingFace 链接，但未报告 GPU 数量与训练时长。MiniF2F-ALF 作为新基准，其变异操作依赖 Claude Code 判断良构性，引入了外部模型依赖。

## 关联研究分析

从数据增强策略看，Pythagoras-Prover 的 ALF 与 ProofOptimizer 的证明重构存在本质差异。ProofOptimizer 通过专家迭代简化已验证证明，目标是提升可读性与库维护性，其变异操作受限于原始证明的逻辑结构。ALF 则从验证实例出发生成结构化变体，目标是扩展训练分布，其轻量级 sanity check 牺牲了部分逻辑严谨性以换取数据规模。这一差异源于任务目标不同：前者服务于库维护，后者服务于模型训练。ALF 的变异类型（如引理提议）是否足以覆盖复杂证明的结构多样性，论文未给出定量分析。

从训练效率看，Pythagoras-Prover 的 LoRA 微调与 DeepSeek-Prover 的全参数训练形成对比。DeepSeek-Prover 依赖大规模预训练数据与全参数优化，其性能提升部分源于模型容量；Pythagoras-Prover 通过参数高效微调与课程学习，在 4B 规模下实现超越，表明数据质量与训练策略对性能的影响可能超过模型规模。这一发现挑战了“规模决定性能”的假设，但 LoRA 在复杂证明结构上的表达能力是否受限，论文未通过消融实验验证。

## 总结

Pythagoras-Prover 要解决的核心矛盾是形式化证明中算力与性能的权衡，其切入点在于通过 ALF 数据增强与动态过滤机制，将性能提升从模型规模转向数据效率。该方法通过 Lean 验证的种子语料库、课程学习 SFT 与 GRPO 强化学习，在 4B 参数下实现 MiniF2F-Test 86.1% 的 pass@32 准确率，超越 671B 基线 3.6 个百分点；32B 模型在 PutnamBench 上解决 93 题，超越 Goedel-Prover-V2 的 86 题。其边界在于 ALF 变体的逻辑等价性依赖轻量级 sanity check，而非完整 Lean 验证，MiniF2F-ALF 上所有模型的性能下降表明形式变体的鲁棒性尚未完全解决。当 ALF 变异类型扩展到更复杂的证明结构时，轻量级检查是否仍能保证变体的逻辑正确性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.12594)