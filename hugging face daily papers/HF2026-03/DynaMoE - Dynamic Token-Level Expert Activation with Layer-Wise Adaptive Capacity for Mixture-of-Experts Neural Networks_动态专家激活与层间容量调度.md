# HuggingFace最新推荐论文 ｜DynaMoE: Dynamic Token-Level Expert Activation with Layer-Wise Adaptive Capacity for Mixture-of-Experts Neural Networks ｜动态专家激活与层间容量调度

作者：Gökdeniz Gülmez

论文原文见 [arXiv](https://arxiv.org/abs/2603.01697)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01697)

> 混合专家架构在扩展模型容量时面临固定路由粒度与均匀层间分配的刚性约束，导致计算资源无法匹配不同输入复杂度及网络深度的实际需求。现有方案通过辅助损失或固定Top-k机制维持稳定性，却牺牲了动态适应能力。本文提出DynaMoE，通过百分位阈值实现变K值动态路由，并引入六种层间专家容量调度策略。该框架在极小规模MLP上验证了调度策略的任务依赖性，但在标准大模型基准上缺乏证据，其理论贡献与工程可行性存疑。

## 研究背景

当混合专家模型处理复杂输入时，固定激活K个专家的路由机制无法区分简单Token与复杂Token的计算需求差异。这种刚性约束源于标准MoE架构对路由离散性的依赖，而离散选择导致的梯度流中断迫使研究者引入辅助负载均衡损失来防止专家坍缩。然而，辅助损失与主任务梯度的冲突抑制了专家专业化，且各层专家数量相同的均匀分配假设忽略了网络深度对特征抽象能力的不同要求。

MoE路由机制的核心矛盾在于解耦参数容量与计算成本的同时，维持训练稳定性与专家功能分化。2020年GShard引入辅助损失解决坍缩问题，2022年Switch Transformer简化为Top-1路由确立工业范式，但均假设K值与层间容量恒定。2024-2025年，ReMoE与Soft-MoE尝试通过可微路由恢复梯度流动，但仍未解决层间容量分配的静态问题。DynaMoE的切入点在于同时放松两个刚性约束：让激活专家数随输入动态变化，并允许不同层拥有不同数量的专家，从而探索容量分布对模型性能的影响。

## 核心方法

### 标准MoE路由参照系

标准MoE层包含N个专家，门控网络计算门控值后通过Top-k选择激活K个专家。该流程的关键假设是K值固定且各层专家数相同，导致路由决策无法适应输入复杂度变化，层间容量分配无法匹配特征抽象需求。

### 动态百分位阈值路由

固定Top-k选择无法区分简单与复杂输入的计算需求，DynaMoE在门控值计算后引入百分位阈值机制替代硬Top-k选择。给定门控值向量 $\mathbf{g} \in \mathbb{R}^N$ 和阈值 $\tau \in (0,1)$，动态选择集定义为：

$$S_\tau(\mathbf{x}) = \{i \in \{1,...,N\} \mid g_i \geq \text{percentile}_\tau(\mathbf{g})\}$$

激活专家数 $K(\mathbf{x}) = |S_\tau(\mathbf{x})|$ 随输入动态变化，范围从 $K_{\min}=1$ 到 $K_{\max}=\lceil(1-\tau)N\rceil$。该设计通过连续阈值替代离散选择，实现了变K值路由的可微性，使路由器能通过端到端梯度优化适应输入复杂度分布。

### 层间专家容量调度

动态路由解决了单Token内的激活数量问题，但各层专家数量相同的均匀分配仍无法匹配网络深度的特征抽象需求。DynaMoE引入调度函数 $S: \{1,...,L\} \to [N_{\min}, N_{\max}]$ 映射层索引到专家数量，定义六种策略。以Descending调度为例，其公式为：

$$N_\ell = N_{\max} - \lfloor t \cdot (N_{\max} - N_{\min}) \rfloor, \quad t = \frac{\ell}{L-1}$$

该公式使早期层拥有更多专家，后期层专家数递减。设计动机在于早期层负责基础特征提取，需要更高容量处理多样输入模式，而后期层处理抽象特征，容量需求降低。这种层间非均匀分配打破了标准MoE的均匀假设，允许模型根据深度特性优化计算资源分布。

## 实验评估

实验在MNIST、Fashion-MNIST、CIFAR-10图像分类和Recycling-the-Web语言建模上评估，基线仅包含MLP和Uniform MoE，缺失Switch Transformer、GShard等标准MoE基线。

| 数据集 | MLP | Uniform | Descending | 提升 |
|---|---|---|---|---|
| MNIST | 89.42 | 91.35 | 92.68 | +3.26% |
| Fashion-MNIST | 84.15 | 86.82 | 88.34 | +4.19% |
| CIFAR-10 | 62.38 | 65.12 | 67.85 | +5.47% |

Descending调度在图像分类上一致优于Uniform和MLP，复杂任务增益更大。

| 模型规模 | 最优调度 | 最佳PPL | MLP PPL |
|---|---|---|---|
| Tiny | Descending | 1011.80 | 1003.08 |
| Small | Ascending | 2308.29 | 2311.02 |
| Medium | Uniform | 2383.89 | 2468.16 |

语言建模显示最优调度随规模变化：Tiny用Descending，Small用Ascending，Medium用Uniform。Small的Ascending调度以2308.29 PPL微弱超越MLP基线2311.02，Medium的Uniform调度比MLP降低3.4% PPL。

评估边界存在显著局限：语言建模仅用1000个训练样本，PPL值（1000-2500范围）远高于标准基准（WikiText-103约12-19），反映模型严重欠拟合。所有Small和Medium模型变体达到近乎相同的next-token准确率（≈5.05%），接近50k词表unigram基线，表明准确率非区分性指标。论文未提供代码，超参数（温度T=0.5，噪声σ=0.1）固定，未报告GPU配置或训练时间细节，可复现性受限。

## 关联研究分析

从问题动机看，DynaMoE与Soft-MoE（Puigcerver et al., 2024）同属可微路由路线，但解决不同失效。Soft-MoE用软分配替代硬Top-k恢复梯度流动，但牺牲稀疏性硬约束；DynaMoE通过百分位阈值在保持硬稀疏的同时实现变K值可微路由，其动态激活机制直接针对输入复杂度差异，而Soft-MoE的软分配对所有Token施加相同稀疏度。这一差异源于任务特性：DynaMoE在极小规模MLP上验证，输入复杂度变化显著；Soft-MoE面向大规模Transformer，稀疏性硬约束对计算效率至关重要。

从方法设计看，DynaMoE与GShard（Lepikhin et al., 2020）形成鲜明对比。GShard引入辅助负载均衡损失防止专家坍缩，DynaMoE完全放弃辅助损失，依赖动态激活自然平衡负载。这一冲突暗示：在极小规模模型中，动态路由的探索机制（高斯噪声+温度缩放）可能足以维持专家分化，无需显式正则化；但在大规模训练中，缺乏辅助损失是否必然导致专家坍缩，论文未给出回答。DynaMoE的层间调度策略是GShard等标准MoE未探索的维度，其有效性仅在MLP架构上验证，Transformer中注意力机制与MoE路由的耦合可能改变最优调度模式。

## 总结

DynaMoE要解决的核心矛盾是固定路由粒度与均匀层间分配对计算资源动态适应性的限制。现有方法通过辅助损失或固定Top-k维持稳定性，但无法同时放松K值与层间容量两个约束。本文通过百分位阈值实现变K值动态路由，并引入六种层间调度策略，在极小规模MLP上验证了调度策略的任务依赖性：图像分类中Descending调度比Uniform提升3.26-5.47%，语言建模中最优调度随规模从Descending转向Ascending再转向Uniform。本文的边界在于实验仅在85K-5.6M参数MLP上进行，语言建模使用1000样本导致严重欠拟合，且缺失标准MoE基线对比。当模型规模扩展至Transformer架构且训练数据达到标准基准规模时，动态路由的梯度方差优势与层间调度策略的最优性是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01697)