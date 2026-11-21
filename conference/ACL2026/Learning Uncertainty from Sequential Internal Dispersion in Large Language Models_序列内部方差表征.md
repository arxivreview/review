# ACL2026最新论文 ｜Learning Uncertainty from Sequential Internal Dispersion in Large Language Models ｜序列内部方差表征

研究机构：新加坡南洋理工大学、上海交通大学

作者：Ponhvoan Srey、Xiaobao Wu、Cong-Duy Nguyen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15741)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15741)

> 大语言模型（LLM）在生成流畅文本时频繁产生事实性错误，即幻觉，这严重阻碍了其在医疗、法律等高风险领域的可靠部署。现有白盒探测方法依赖对隐藏状态演化路径的强假设或仅利用末位/均值Token，导致跨任务泛化性差且丢失序列级动态信息。本文提出序列内部方差表征（SIVR），通过计算全序列Token的跨层方差特征并引入Transformer Encoder聚合，以最小假设捕捉不确定性。该方法在多个基准上超越强基线，但受限于监督学习范式，其泛化边界仍需更大规模模型验证。

## 研究背景

当LLM面对知识边界外的问题时，其输出概率分布往往呈现高置信度，传统的基于Logits的熵值或困惑度指标无法有效区分“一致的错误”与“正确的答案”。这种高置信度幻觉的失效促使研究转向模型内部隐藏状态，假设其中蕴含了关于事实真伪的可解码信号。然而，直接利用隐藏状态进行探测面临两个核心困境：一是特征提取往往压缩至末位或均值Token，忽略了序列中特定错误Token引发的局部动态变化；二是现有无监督方法如Chain-of-Embeddings (CoE) 对隐藏状态在层间的幅值与角度变化施加了严格约束，导致其在不同模型或任务间性能剧烈波动。

内部表征探测路线旨在利用隐藏状态中的可解码信号实现实时检测，SAPLMA等工作证明了线性探针的有效性，但受限于单层或末位Token的信息瓶颈。CoE等无监督方法试图通过层间差异度量不确定性，但其假设的普适性不足，在OOD（Out-of-Distribution）场景下性能显著下降。本文的切入点在于解耦“特征提取”与“序列聚合”：不再假设隐藏状态遵循特定的几何演化路径，而是将其视为高维空间中的点云，通过统计其跨层分散度（Internal Variance）来量化不确定性，并保留Token顺序以学习序列级模式。

## 核心方法

### 方法参照系

标准内部表征探测流程通常提取LLM最后一层或均值隐藏状态，训练轻量级分类器（如逻辑回归）预测幻觉概率。本文的关键差异在于：特征提取从单一向量转向跨层统计量，序列处理从池化转向保留顺序的Transformer编码，旨在解决末位Token信息丢失与跨层假设过强导致的泛化失效。

### 内部方差特征提取

针对CoE方法对层间幅值与角度变化的强假设失效，本文提出内部方差特征，仅假设不确定性反映为隐藏状态在层间的分散程度。对于序列中第 $t$ 个Token，其在第 $l$ 层的隐藏状态为 $\mathbf{h}_t^{[l]} \in \mathbb{R}^d$。首先计算正则化协方差矩阵 $\Sigma' = \Sigma + \alpha I_d$ 的对数伪行列式，作为广义方差（CovDet）以捕捉体积容量：

$$ \text{CovDet}_t = \log \det(\Sigma') = \sum_{i=1}^d \log \lambda_i $$

其中 $\lambda_i$ 为 $\Sigma'$ 的特征值。该公式聚合了整个特征谱，避免了单一维度主导。其次，计算归一化层向量的圆形方差（CircVar）以捕捉方向多样性：

$$ c_t = 1 - \frac{\left| \sum_{l=0}^L \hat{\mathbf{h}}_t^{[l]} \right|}{L+1} $$

最后，结合Token预测熵 $e_t$，构成三维内部方差向量 $\mathbf{v}_t = [v_t, c_t, e_t]^\top$。这一设计通过分离幅值、方向与输出空间不确定性，解决了CoE在特定任务（如Qwen在SciQ上）因假设不成立导致的性能崩溃，提供了更鲁棒的跨层分散度度量。

### 序列聚合与分类

针对末位或均值Token聚合丢失序列动态信息的问题，本文引入Transformer Encoder对全序列内部方差特征进行建模。给定变长序列 $\mathbf{s}_i$ 及其标签 $y_i$，提取特征 $\mathbf{x}_i$ 后，通过嵌入层投影至128维隐藏空间，经Transformer Encoder块处理后，由线性层输出不确定性分数：

$$ p_\theta(y=1|\mathbf{x}) = \sigma(\mathbf{W} \cdot \text{Encoder}(\mathbf{E}(\mathbf{x}))) $$

其中 $\sigma$ 为Sigmoid函数，$\mathbf{E}$ 为嵌入层。该架构保留了Token顺序，使模型能够捕捉如“Praia is a city in Portugal”中特定错误Token引发的方差尖峰，而非被整体均值掩盖。相比RNN，Transformer Encoder在并行计算与长程依赖建模上更具优势，且实验表明其精度优于RNN变体。

## 实验评估

实验在TriviaQA、SciQ、MedMCQA等12个数据集上进行，基线覆盖Logit-based（Max Prob）、Sampling-based（Semantic Entropy）、Confidence elicitation（P(True)）及Internal states（SAPLMA, TAD, CoE）。SIVR在Llama-3.2-3B、Llama-3.1-8B及Ministral-8B上均取得最优平均排名。

| 模型 | 方法 | TriviaQA AUC | SciQ AUC | MedMCQA AUC | Avg AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Llama-3.2-3B | SAPLMA | 77.94 | 83.62 | 65.63 | 74.72 |
| Llama-3.2-3B | TAD | 88.25 | 85.16 | 63.56 | 78.34 |
| Llama-3.2-3B | **SIVR** | **89.31** | **85.70** | **66.59** | **79.53** |
| Llama-3.1-8B | SAPLMA | 83.70 | 87.41 | 63.53 | 76.72 |
| Llama-3.1-8B | TAD | 87.02 | 83.60 | 65.09 | 75.75 |
| Llama-3.1-8B | **SIVR** | **89.48** | **87.79** | **75.95** | **80.86** |
| Ministral-8B | SAPLMA | 80.62 | 73.55 | 49.24 | 73.30 |
| Ministral-8B | TAD | 83.29 | 75.54 | 58.73 | 75.24 |
| Ministral-8B | **SIVR** | **87.29** | **80.81** | **61.12** | **78.11** |

SIVR在Llama-3.1-8B上平均AUC达80.86%，较最强基线TAD（75.75%）提升5.11个百分点，且在MedMCQA等高风险领域优势显著。

消融实验显示，仅使用内部方差特征（CovDet, CircVar）的AUC为71.31%，与SAPLMA（74.72%）接近，证明内部方差本身具备强判别力。加入隐藏状态（PCA）后性能提升至78.11%，表明两者互补。在OOD评估中，内部方差特征的AUC下降幅度（12.18%）显著小于隐藏状态（21.72%），验证了其跨任务泛化优势。

评估指标包含AUC、FPR@95及AUPR，覆盖了安全关键场景的召回需求。代码已开源，但实验仅覆盖3B-14B规模模型，未报告置信区间。与领域综述中CausalGaze在TriviaQA上的0.8614 AUROC相比，SIVR在Llama-3.2-3B上达到0.8931，但骨干网络差异使得直接对比需谨慎。

## 关联研究分析

从特征提取假设看，SIVR与CoE形成鲜明对比。CoE依赖层间幅值与角度的特定相关性，这种强假设在模型架构或任务分布变化时极易失效，导致其性能在不同基准间波动剧烈。SIVR通过广义方差与圆形方差解耦幅值与方向，仅假设分散度反映不确定性，这种弱假设设计是其OOD泛化优于CoE的根本原因。然而，SIVR仍属于监督学习范式，需要标注数据训练Transformer Encoder，而CoE等无监督方法在零样本场景下更具部署灵活性，两者在“精度-数据依赖”上存在权衡。

从序列处理机制看，SIVR与SAPLMA等探针方法的关键差异在于Token聚合策略。SAPLMA通常使用末位或均值Token，忽略了序列中局部错误引发的动态变化，导致在长文本或复杂推理任务中检测精度受限。SIVR引入Transformer Encoder保留Token顺序，能够捕捉如“特定错误Token引发的方差尖峰”等序列级模式。这种设计使得SIVR在TriviaQA等自由形式问答任务上表现优于SAPLMA，但在MedMCQA等多选任务上，SAPLMA的简洁性可能更具计算效率，SIVR的Transformer开销是否在所有场景下都必要，论文未给出充分论证。

## 总结

本文旨在解决白盒探测方法中跨层假设过强与序列信息丢失导致的泛化失效问题。通过提出内部方差特征并引入Transformer Encoder聚合全序列动态，SIVR在Llama-3.1-8B上实现了80.86%的平均AUC，较基线TAD提升5.11个百分点，并在OOD场景中展现出更小的性能衰减。然而，该方法仍依赖监督学习，且实验局限于3B-14B规模模型，未验证在更大参数模型中内部方差特征是否会被模型自身更强的校准能力稀释。当支持集规模扩大或模型参数增加时，Transformer Encoder的序列建模增益是否依然显著，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15741)