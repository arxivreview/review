# ICLR2026最新论文 ｜Circuit Insights: Towards Interpretability Beyond Activations ｜基于权重与电路结构的自动解释框架

作者：Elena Golimblevskaia、Aakriti Jain、Bruno Puri 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.14936)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.14936)

> 大语言模型内部特征的自动解释长期依赖外部大模型对激活值的语义归纳，导致解释结果受数据集分布与提示词策略的强干扰。现有方法无法区分特征激活的结构性原因与偶然性噪声，且在处理上下文依赖特征时失效。本文提出 WeightLens 与 CircuitLens 框架，利用 Transcoder 的权重矩阵与电路归因结构直接生成特征描述，剥离对解释 LLM 的依赖。该方法在 Token 级特征上匹配或超越基线，但在上下文依赖特征的纯度与因果忠实度上存在显著局限。

## 研究背景

理解大语言模型内部机制需解决神经元多义性问题，即单个神经元对多个无关概念同时响应。稀疏自编码器（Sparse Autoencoder, SAE）通过过完备字典将密集激活分解为稀疏单义特征，成为解决这一难题的核心工具。然而，SAE 仅重构激活值，无法区分特征激活是由输入内容驱动还是由模型内部权重结构驱动，导致自动解释时难以定位真正的触发机制。

主流自动解释流水线（如 Bills et al., 2023）通过收集最大化激活样本并交由解释 LLM 生成描述，但该方法将黑盒问题转移至另一个黑盒 LLM，且解释质量高度依赖数据集覆盖度。当特征激活于特定上下文模式时，仅分析激活值无法揭示因果路径，导致描述模糊或幻觉。Transcoder 架构通过稀疏近似 MLP 层，将归因分解为输入依赖与权重依赖两部分，为结构化解释提供了基础。本文切入点在于利用 Transcoder 的权重不变性与电路归因能力，构建无需大规模数据集与外部 LLM 的解释框架。

## 核心方法

### 方法参照系

本文问题属于自动解释（Auto-interpretability）范畴，但区别于基于激活值统计的传统流程。标准流程依赖数据集采样与 LLM 语义归纳，而本文利用 Transcoder 架构特有的权重分解特性，将解释任务转化为权重投影与电路归因计算，关键差异在于解释证据来源于模型参数而非数据分布。

### WeightLens：权重不变性解释

设计动机在于解决激活值分析无法区分结构性连接与噪声的问题。WeightLens 利用 Transcoder 编码器与解码器权重，通过嵌入矩阵投影识别特征关联的 Token。核心公式为：

$$ \text{Outliers} = \{ t \in V \mid z(W_{emb} \cdot f_{enc}^{(l,i)})_t > \tau \} $$

其中 $f_{enc}^{(l,i)}$ 为特征编码器向量，$W_{emb}$ 为嵌入矩阵，$z(\cdot)$ 为 Z-score 标准化，$\tau$ 为异常值阈值。该公式通过统计离群点识别直接激活特征的 Token，随后通过前向传播验证 Token 在孤立状态下是否激活特征，确保描述的上下文无关性。

### CircuitLens：电路归因解释

设计动机在于解决上下文依赖特征无法通过静态权重解释的问题。CircuitLens 利用 Transcoder 的跨层归因公式，识别导致特征激活的注意力头与 Token 组合。核心公式为：

$$ A_{(l',h) \to (l,i)} = \sum_{s} r_{pre}^{(l')}[s] W_{OV}^{(l',h)} f_{enc}^{(l,i)} \cdot \alpha_{s \to t} $$

其中 $r_{pre}^{(l')}[s]$ 为注意力前残差流，$W_{OV}$ 为输出值矩阵，$\alpha_{s \to t}$ 为注意力分数。该公式量化特定注意力头对目标特征激活的贡献，通过 Jaccard 相似度对贡献集合进行 DBSCAN 聚类，将多义性特征解耦为单一语义簇，再由 LLM 生成统一描述。

## 实验评估

实验在 GPT-2 Small、Gemma-2 2B 与 Llama-3.2-1B 的 Transcoder 上进行，采用 FADE 框架评估 Clarity、Responsiveness、Purity 与 Faithfulness。基线包括 Neuronpedia 与 MaxAct* 激活最大化方法。

| 方法 | Clarity | Responsiveness | Purity | Faithfulness |
| :--- | :--- | :--- | :--- | :--- |
| WeightLens | 优于 MaxAct* | 优于 MaxAct* | 低于 MaxAct* | 低 |
| MaxAct* | 较低 | 较低 | 较高 | 低 |

WeightLens 在 Clarity 与 Responsiveness 上优于激活最大化基线，表明权重投影能更清晰地表达概念并触发特征激活。然而，Purity 较低，说明权重方法易将上下文依赖特征误判为 Token 级特征，导致描述泛化不足。Faithfulness 在所有方法中均较低，且随层深增加而上升，这归因于 Transcoder 架构中单特征对输出影响的微弱性，模型冗余性使得单点干预难以产生显著效应。

消融实验显示，引入输出 Token（WeightLens+Out）与 LLM 精炼（WeightLens+Out+LLM）对 Clarity 与 Responsiveness 提升有限，表明权重本身已包含足够信息。CircuitLens 在较小数据集（24M tokens）上表现与大数据集相当，验证了电路归因对数据规模的鲁棒性。然而，CircuitLens 在 Purity 上仍低于激活方法，表明电路聚类未能完全消除多义性干扰。

评估边界方面，FADE 框架依赖 LLM-as-a-judge，可能存在评估者偏差。论文未报告重构误差（MSE），无法直接对比 Transcoder 与 SAE 的特征保真度。代码已开源，但超参数（如 Z-score 阈值 4/4.5）针对不同模型硬编码，缺乏统一调参协议。

## 关联研究分析

从问题动机看，本文与 FADE Framework（Puri et al., 2025）同属自动解释评估体系，但 FADE 聚焦于描述质量指标设计，而本文聚焦于解释证据来源。FADE 依赖激活值与 LLM 交互，本文则通过权重与电路结构前置过滤，减少了 LLM 的搜索空间。这一差异源于 Transcoder 架构的归因分解能力，SAE 无法提供此类结构信息，因此本文方法不可直接迁移至标准 SAE。

从方法设计看，本文与 Automated Interpretation Pipeline（Bills et al., 2023）同属 LLM 辅助解释路线，但 Bills 方法将全量激活值输入 LLM，本文仅输入电路聚类后的稀疏模式。这一设计简化了 LLM 任务，但引入了电路归因的计算开销。与 Transcoder 原始工作（Dunefsky et al., 2024）相比，本文未优化 Transcoder 训练，而是利用其预训练权重进行解释，因此特征质量受限于 Transcoder 本身的稀疏性约束，未解决特征收缩或死特征问题。

## 总结

本文要解决的核心矛盾是自动解释对数据集与外部 LLM 的过度依赖，以及上下文依赖特征的解释失效。切入点在于利用 Transcoder 权重不变性与电路归因结构，将解释证据从数据分布转移至模型参数。WeightLens 通过权重投影识别 Token 级特征，CircuitLens 通过电路聚类解耦多义性特征。实验证明 WeightLens 在 Clarity 与 Responsiveness 上匹配或超越基线，但 Purity 与 Faithfulness 较低，暴露了权重方法对上下文依赖特征的漏检与单特征干预效应的微弱性。当特征激活依赖于复杂的注意力交互而非静态 Token 时，电路归因能否完全替代激活值分析，论文未给出定量回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.14936)