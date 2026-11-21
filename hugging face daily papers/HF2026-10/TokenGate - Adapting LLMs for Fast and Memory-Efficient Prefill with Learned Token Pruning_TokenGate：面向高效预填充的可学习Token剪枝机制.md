# HuggingFace最新推荐论文 ｜TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning ｜TokenGate：面向高效预填充的可学习Token剪枝机制

研究机构：美国斯坦福大学

作者：Liana Patel、Rishabh Ranjan、Ion Stoica 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.26754)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.26754)

> 导读
> 长上下文推理中，Transformer 的自注意力机制导致计算复杂度随输入长度二次方增长，且 KV Cache 内存占用线性增加，严重制约了大语言模型（Large Language Models, LLMs）在长文档处理与代码生成等场景的部署效率。现有优化方案主要分为两类：免训练 Token 剪枝依赖启发式注意力评分，虽部署成本低但加速比有限且易导致精度下降；架构修改类方法虽能实现自适应计算，但需从头预训练或高昂微调，难以直接应用于现有模型。TokenGate 提出了一种即插即用的可学习 Token 剪枝组件，通过引入受混合专家模型（Mixture-of-Experts, MoE）启发的 Token-Gated Attention 机制，解决了 Top-K 选择算子非可微导致的梯度断裂问题，实现了端到端的 Token 重要性学习。该工作确立了“可学习硬压缩”的新范式，在保持精度的前提下显著提升了预填充效率，但其与软压缩方法在复杂推理任务上的信息保留能力对比尚缺直接证据。

## 研究背景

当 LLM 处理包含数万 Token 的代码库或长文档时，每一层网络都必须对所有输入 Token 进行全量计算，无论这些 Token 是否包含关键信息。这种“全量读取”模式导致预填充（Prefill）阶段的时间到首字延迟（Time-to-First-Token, TTFT）和峰值内存占用成为服务瓶颈。为了缓解这一压力，研究者提出了 Token 剪枝策略，即在模型中间层剔除低重要性 Token，仅将高重要性 Token 传递至后续层。然而，传统的 Token 剪枝方法如 FastKV 和 SlimInfer 通常依赖注意力分数的启发式规则进行筛选，这种非可微的离散操作切断了梯度传播路径，使得模型无法通过任务损失反向优化 Token 选择策略，导致在激进剪枝下精度显著受损。

与此同时，另一类通过修改 Transformer 架构以实现稀疏计算的方法，虽然理论上能降低复杂度，但往往需要从头预训练或引入复杂的辅助损失函数，难以直接适配现有的预训练模型生态。这就形成了一个两难困境：免训练方法无法实现模型与剪枝策略的协同优化，而架构修改方法则面临高昂的适配成本。TokenGate 正是在此背景下提出，旨在通过一种轻量级的即插即用组件，赋予现有预训练模型端到端学习 Token 剪枝的能力，从而在效率与精度之间寻找更优的帕累托前沿。

## 核心方法

### 方法参照系：中间层 Token 剪枝流程

在标准的 Transformer 预填充过程中，所有 Token 均通过所有层。TokenGate 将这一流程修改为三段式结构：首先，Token 通过门控模块（Gate Module）之前的层进行标准前向传播；其次，门控模块对所有 Token 进行评分并执行 Top-K 选择，仅保留高分 Token；最后，门控模块之后的层仅处理这些保留的 Token。这一流程与传统的硬压缩（Hard Compression）类似，但关键差异在于 TokenGate 引入了可微的评分机制，使得整个剪枝过程可以参与端到端训练。

### 门控模块与评分网络

门控模块的核心是一个轻量级的评分网络，用于量化每个 Token 的重要性。该网络读取 Token 在门控层 $L$ 的归一化后注意力残差 $\tilde{a}_L^j$，并通过一个多层感知机（MLP）输出标量分数 $\tilde{b}_j$。为了消除序列长度对分数分布的影响，分数经过 RMSNorm 归一化得到最终的重要性分数 $b_j$：

$$
\tilde{b}_j = \text{MLP}_\theta(\tilde{a}_L^j), \quad b_j = \frac{\tilde{b}_j}{\sqrt{\frac{1}{|P|} \sum_{j' \in P} \tilde{b}_{j'}^2 + \epsilon}}
$$

其中 $P$ 为可剪枝 Token 集合。该评分网络初始化为输出零，确保训练初期模型行为与原始模型一致。随后，Top-K 选择器根据 $b_j$ 选出前 $K$ 个 Token 集合 $S$。这一设计动机在于替代 FastKV 等方法的启发式注意力评分，通过可学习的参数捕捉任务特定的 Token 重要性模式，例如在问答任务中保留答案关键词，而在摘要任务中保留句尾停用词。

### Token-Gated Attention 机制

Top-K 选择算子本身是非可微的，这阻碍了梯度从任务损失回传至评分网络。为解决此问题，TokenGate 引入了 Token-Gated Attention，借鉴 MoE 中路由器加权专家输出的思想，将 Token 的重要性分数融入注意力计算中。在门控层之后的层 $\ell > L$ 中，注意力权重 $\alpha_{ij}$ 被重新定义为：

$$
\alpha_{ij} = \frac{\exp(z_{ij}) g_j}{\sum_{j' \in S, j' \le i} \exp(z_{ij'}) g_{j'}}, \quad g_j = \text{softmax}_{j \in S}(b_j)
$$

其中 $z_{ij}$ 为标准注意力 logits，$g_j$ 为由重要性分数 $b_j$ 生成的门控值。该公式的物理含义是：高重要性 Token 在注意力计算中获得更高的权重，从而在后续层中主导信息聚合。通过这种软加权机制，即使 Top-K 选择是离散的，梯度仍可通过 $g_j$ 对 $b_j$ 的依赖关系回传至评分网络，实现了端到端训练。此外，该方法还引入了头级缩放（Head-wise Scaling）和温度缩放（Temperature Scaling）以增强模型在不同剪枝比率下的鲁棒性。

## 实验评估

实验在 2WikiMultihopQA、MultiNews、RepoBench-P 等五个数据集上进行，对比了 TokenGate 与 FastKV、SlimInfer 等免训练剪枝基线以及标准预填充方法。评估指标包括任务精度（F1-score, ROUGE-L 等）和效率指标（TTFT, 峰值内存）。

| 方法 | 骨干模型 | 数据集 | 相对标准预填充加速比 (TTFT) | 相对标准预填充内存降低比 |
| :--- | :--- | :--- | :--- | :--- |
| TokenGate | Qwen3-1.7B | 2WikiMultihopQA | 3.0× | 2.7× |
| TokenGate | Qwen3.5-2B | NIAH 32K | 3.8× | - |
| FastKV | Qwen3-1.7B | 2WikiMultihopQA | < 3.0× | < 2.7× |

*注：表中数据基于论文图1及正文描述，TokenGate 在保持 95% 全上下文精度的前提下实现上述加速。*

消融实验揭示了 TokenGate 性能提升的两个关键来源：可学习选择器与骨干网络协同适应。在 2WikiMultihopQA 上，使用随机 Token 选择的 TokenGate 模型性能显著低于使用训练后评分网络的选择器，证明了端到端训练评分网络的有效性。更有趣的是，即使使用相同的随机选择器，TokenGate 训练后的模型性能仍优于仅用 LoRA 微调的基线模型，这表明端到端训练促使模型骨干重新分布信息，增强了对 Token 剪枝的鲁棒性。

评估边界方面，论文主要对比了免训练剪枝方法，但未与 GIST、ICAE 等软压缩方法进行直接对比。由于软压缩将上下文映射为连续向量，而 TokenGate 保留离散 Token，两者在可解释性和下游任务适配性上存在本质差异，缺乏统一基准使得难以直接量化 TokenGate 在复杂推理中的信息保留优势。此外，实验主要在 A100 GPU 上进行，未报告在资源受限边缘设备上的延迟开销。

## 关联研究分析

从问题动机看，TokenGate 与 LLMLingua 系列同属硬压缩路线，旨在通过剔除冗余 Token 降低计算成本。然而，LLMLingua 依赖外部小型语言模型计算困惑度进行筛选，属于推理时的后处理操作，无法与主模型协同优化。TokenGate 将评分网络内嵌于主模型中，并通过 Token-Gated Attention 实现梯度回传，使得模型能够学习任务特定的 Token 重要性分布。这种差异源于对“可训练性”的不同追求：LLMLingua 追求零训练成本，而 TokenGate 追求效率与精度的帕累托最优。

从方法设计看，TokenGate 借鉴了 MoE 的稀疏激活思想，但将稀疏性从参数空间迁移至 Token 空间。与 FastKV 等免训练方法相比，TokenGate 的核心创新在于解决了离散选择的可微性问题。FastKV 依赖注意力分数的启发式规则，在早期层注意力信号较弱时容易误剪关键 Token。TokenGate 通过端到端训练，使评分网络能够利用深层语义信息指导早期层的剪枝决策，从而在激进剪枝下保持精度。然而，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

TokenGate 针对长上下文预填充中计算效率与模型精度的权衡矛盾，提出了可学习 Token 剪枝方案。通过引入 Token-Gated Attention 机制，该工作突破了传统硬压缩方法因 Top-K 算子非可微而无法端到端训练的局限，实现了评分网络与模型骨干的协同优化。实验表明，TokenGate 在 Qwen3-1.7B 上实现了 3.0 倍的 TTFT 加速和 2.7 倍的内存降低，且精度无显著损失，显著优于 FastKV 等免训练基线。然而，该方法的边界在于其仍属于离散 Token 筛选，缺乏软压缩方法的语义平滑性，且未与主流软压缩方法在统一基准下进行对比。当面对需要高度语义连贯性的复杂多跳推理任务时，离散剪枝导致的语义断裂风险是否可通过端到端训练完全消除，仍有待进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.26754)