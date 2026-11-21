# ACL2026最新论文 ｜Mitigating Structural Knowledge Collapse in Domain-Specific LLMs via Morpheme-Aware KV-Aggregation ｜结构知识崩塌下的词素感知注意力聚合

研究机构：浙江大学、美国康奈尔大学

作者：Yuxuan Si、Zheqi Lv、Chengxi Zang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc09296ead5d)

> 大语言模型在医疗、法律等垂直领域面临预训练语料分布偏差，导致领域术语理解能力不足。现有持续预训练或参数高效微调方法虽能注入知识，但往往忽视子词分词器对复杂术语的过度碎片化，引发注意力机制无法重组语义的结构性缺陷。本文提出词素感知KV聚合注意力（MorphKA），通过双阶段适配器在注意力空间内动态修复碎片化表示，无需修改分词器或重训练嵌入。该方法在术语密集任务上显著优于基线，但其效果高度依赖分词器特定的边界标记，跨分词器泛化能力存疑。

## 研究背景

当模型处理“immunohistochemistry”这类长复合词时，字节对编码（BPE）分词器将其切割为“immun”、“o”、“hist”等无意义子词，破坏了词素间的语义关联。这种碎片化导致注意力机制难以在后续层中重建完整概念，形成结构知识崩塌（Structural Knowledge Collapse, SKC）。SKC不仅降低领域任务准确率，还加剧了微调过程中的灾难性遗忘，因为模型被迫依赖浅层碎片相关性而非深层语义整合。

领域适应的主流路线包括持续预训练（CPT）和参数高效微调（PEFT）。CPT通过无监督训练注入知识，但易导致容量饱和与通用能力退化；PEFT如LoRA通过低秩矩阵更新降低计算成本，但其线性层更新缺乏对词素结构的归纳偏置，无法修复注意力内部的语义断裂。现有词表扩展方法虽能减少未登录词（OOV）率，但需重训练嵌入层，破坏预训练特征空间对齐，且计算开销巨大。本文切入点在于将形态学感知引入注意力机制内部，通过KV空间的动态聚合实现碎片化词素的语义重组，从而在不改变分词器的前提下缓解SKC。

## 核心方法

### 方法参照系

本文问题置于参数高效微调（PEFT）框架下，但关键差异在于干预位置：标准LoRA仅更新线性层权重，而本文在注意力计算的Key-Value（KV）空间插入结构感知操作，直接修复表示层面的语义断裂，而非仅优化参数更新方向。

### 组合语义单元发现与门控

标准PEFT假设所有token具有同等重要性，但SKC表明碎片化术语需要特殊处理。本文首先通过混合神经与词法线索发现组合语义单元（Compositional Semantic Units, CSUs），并引入可微门控机制选择性干预。CSU边界由混合显著性分数 $\rho_i$ 确定：

$$ \rho_i = \lambda(1 - \cos(\bar{h}_i, \bar{h}_{i+1})) + (1 - \lambda)\eta(t_i, t_{i+1}) $$

其中 $\cos$ 项捕捉表示空间的不连续性，$\eta$ 项融合表面词法线索（如前缀延续）。当 $\rho_i > \delta$ 时标记为边界。随后，通过碎片化强度与几何分散度计算门控值 $\gamma_j$，仅对高碎片化单元激活MorphKA，避免对完整词素引入噪声。这一设计解决了标准LoRA对完整与碎片化token一视同仁导致的表示干扰问题。

### 双阶段KV聚合

早期层负责局部同步，深层层负责全局概念归纳。输入级词素聚合（Input-Level Morpheme Aggregation, IMA）在早期层通过门控插值同步CSU内KV向量：

$$ \tilde{k}'_i = (1-\beta_\ell\gamma_{u(i)})\tilde{k}_i + \beta_\ell\gamma_{u(i)}\tilde{k}_{u(i)} $$

该公式将分散的子词KV向量拉向单元级原型，确保共享语义核心同时保留位置信息。自适应多尺度路由融合（Adaptive Multiscale Routing Fusion, AMRF）在深层层引入可学习语义锚点 $C=\{c_k\}$，通过路由分布 $p_{i,k}$ 聚合全局证据：

$$ \tilde{k}_{A(k)} = \frac{\sum_i p_{i,k}\tilde{k}'_i}{\sum_i p_{i,k} + \epsilon} $$

锚点作为全局记忆token参与注意力计算，实现细粒度子词证据与高层概念摘要的对齐。这一双阶段策略解决了单一聚合深度无法兼顾局部一致性与全局语义整合的瓶颈，使模型能在不同层深度动态修复SKC。

## 实验评估

实验在Qwen3-8B与Llama-3.1-8B上评估，涵盖MedQA、PubMedQA、CaseHOLD、BillSum四个术语密集任务，基线覆盖PEFT（LoRA, Wise-FT）、词表扩展（DV）及动态合并（Dynamic Merging），但缺失持续预训练（CPT）与检索增强生成（RAG）基线，限制了与主流领域适应范式的全面对比。

| 方法 | MedQA (Qwen3) | PubMedQA (Qwen3) | CaseHOLD (Qwen3) | BillSum (Qwen3) |
| :--- | :--- | :--- | :--- | :--- |
| LoRA SFT | 78.43 | 55.38 | 80.26 | 47.18 |
| DV (Vocab-Exp) | 81.26 | 58.94 | 83.57 | 50.16 |
| MorphKA | 83.58 | 60.87 | 85.79 | 52.28 |

MorphKA在Qwen3-8B上平均领域性能超越最强非MorphKA基线（SPM+ATT_EG）约1.5-2.5个百分点，且在Llama-3.1-8B上同样领先。消融实验显示，移除早期IMA导致领域平均性能下降3.6%，移除保真度正则化使通用能力保持分数（GCI Score）骤降6.1%，表明双阶段设计与保真约束对平衡领域适应与通用能力至关重要。

| 变体 | Domain Avg. (Qwen3) | GCI Score (Qwen3) |
| :--- | :--- | :--- |
| Full MorphKA | 70.55 | 83.30 |
| w/o IMA | 66.95 | 82.20 |
| w/o Fidelity Reg. | 70.15 | 77.30 |

评估边界方面，论文未报告计算效率指标（如推理延迟、显存占用），且CSU发现依赖SentencePiece等分词器的特定标记（如下划线），在跨分词器或跨语言场景下的泛化性未验证。代码未公开，超参数（如LoRA rank r=16）固定，可复现性受限。

## 关联研究分析

从问题动机看，MorphKA与词表扩展方法（如DV）形成鲜明对比。DV通过添加领域token减少OOV率，但需重训练嵌入层，破坏预训练特征空间对齐，且无法动态捕捉词素组合性。MorphKA则通过内部KV聚合实现语义重组，避免了嵌入重训练的计算开销，且参数量仅为词表扩展方法的20%。这一差异根源在于任务特性：术语密集领域需要动态语义整合，而非静态词表覆盖。MorphKA的CSU门控机制使其能选择性干预碎片化单元，而DV对所有token一视同仁，导致对完整词素的表示干扰。

从方法设计看，MorphKA与动态合并（Dynamic Merging）同属结构干预路线，但作用阶段不同。Dynamic Merging在推理时合并子词，缺乏训练时的形态学整合，导致表示不一致。MorphKA则在训练与推理阶段均通过IMA和AMRF实现结构感知聚合，且引入保真度约束防止通用能力退化。这一差异源于设计目标：Dynamic Merging侧重推理效率，MorphKA侧重表示稳定性。MorphKA的AMRF通过可学习锚点实现全局概念归纳，而Dynamic Merging仅做局部合并，无法捕捉跨单元的高阶语义关联。

## 总结

本文核心矛盾在于子词碎片化导致的结构知识崩塌（SKC）阻碍领域语义连贯性重建，而现有PEFT方法缺乏结构归纳偏置。MorphKA通过双阶段KV聚合在注意力空间内动态修复碎片化表示，无需修改分词器或重训练嵌入。实验证明其在术语密集任务上超越词表扩展基线，且通用能力保持优于标准LoRA。然而，CSU发现依赖分词器特定标记，跨分词器泛化能力未验证。当分词器标记不一致或缺失时，CSU边界检测的鲁棒性如何，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_cc09296ead5d)