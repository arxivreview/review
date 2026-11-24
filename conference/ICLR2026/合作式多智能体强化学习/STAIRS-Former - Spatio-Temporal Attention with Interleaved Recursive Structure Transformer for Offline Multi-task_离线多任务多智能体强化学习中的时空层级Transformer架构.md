# ICLR2026最新论文 ｜STAIRS-Former: Spatio-Temporal Attention with Interleaved Recursive Structure Transformer for Offline Multi-task Multi-agent Reinforcement Learning ｜离线多任务多智能体强化学习中的时空层级Transformer架构

研究机构：韩国科学技术院

作者：Jiwon Jeon、Myungsik Cho、Youngchul Sung

论文原文见 [arXiv](https://arxiv.org/abs/2603.11691)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11691)

> 离线多任务多智能体强化学习（Offline MT-MARL）旨在从固定数据集训练能应对智能体数量动态变化且泛化至未见任务的策略，但现有方法仅将Transformer用于观测维度适配，未能利用其建模长程历史与复杂实体关系的潜力。本文通过引入空间递归模块、时间层级结构与Token-Dropout机制，重构了Transformer在部分可观测环境下的信息处理流程。该架构在SMAC与SMAC-v2基准上超越了基于单层Transformer的基线，但在连续控制任务中的泛化能力与计算开销的平衡仍存疑。

## 研究背景

多智能体系统在部分可观测环境中，单个智能体无法获取全局状态，必须依赖历史观测推断队友意图与环境动态。这种信息缺失导致策略难以捕捉长时程依赖，而传统递归神经网络（RNN）在处理高维实体关系时效率低下。Transformer架构通过自注意力机制并行处理序列，理论上能同时建模空间实体关联与时间历史依赖，但其参数共享特性要求输入结构固定，难以直接适应智能体数量变化的多任务场景。

现有离线MT-MARL方法如ODIS与HiSSD采用UPDeT架构，将观测分解为实体Token并输入单层Transformer，仅解决了观测维度变化问题。然而，单层结构无法捕捉深层实体关系，且单一历史Token仅执行简单RNN操作，导致注意力分布均匀，无法聚焦关键信息。本文切入点在于指出Transformer在离线MT-MARL中被“降维使用”，通过增加空间递归深度与时间层级结构，释放其建模复杂依赖的潜力，同时引入Token-Dropout应对智能体数量变化。

## 核心方法

### 方法参照系

标准离线MT-MARL流程基于UPDeT架构，将智能体观测线性投影为实体Token，输入单层Transformer计算局部Q值，再通过Qatten网络聚合。该流程假设观测维度变化可通过线性投影适配，但忽略了实体间深层关系与历史依赖的建模，导致在部分可观测环境下策略泛化能力受限。

### 空间递归模块

空间递归模块替代单层Transformer，通过递归步骤深化实体关系推理。设计动机是解决单层结构无法捕捉复杂实体交互的问题。模块将观测嵌入为实体向量，通过递归Transformer层逐步精炼注意力权重：

$$
\mathbf{h}^{(l+1)} = \text{Transformer}(\mathbf{h}^{(l)}, \mathbf{E})
$$

其中 $\mathbf{E}$ 为实体嵌入，$\mathbf{h}^{(l)}$ 为第 $l$ 层隐藏状态。递归结构使模型能区分关键实体与背景噪声，提升对未见任务中实体配置的适应性。

### 时间层级与Token-Dropout

时间模块结合GRU与时间焦点层（TFL），通过步级与周期性更新捕捉长短依赖。设计动机是解决单一历史Token无法保留长程信息的问题。GRU维护历史状态，TFL通过门控机制强化关键时间步的注意力：

$$
\mathbf{z}_t = \sigma(W_z [\mathbf{h}_{t-1}; \mathbf{o}_t] + b_z)
$$

Token-Dropout在训练时随机丢弃实体Token，迫使模型不依赖特定智能体数量，提升对智能体缺失场景的鲁棒性。该机制通过随机正则化，使策略在智能体数量剧烈变化时保持稳定。

## 实验评估

实验在SMAC、SMAC-v2、MPE与MAMuJoCo基准上进行，对比UPDeT-m、ODIS与HiSSD。基线覆盖离线MT-MARL主流方法，但缺失CoFlow等生成式模型对比。

| 基准 | 数据集质量 | STAIRS-Former | HiSSD | ODIS |
| :--- | :--- | :--- | :--- | :--- |
| SMAC Marine-Hard | Medium | 57.9 | 49.5 | 37.5 |
| SMAC-v2 | Medium | 30.3 | 24.4 | 11.5 |
| MAMuJoCo HalfCheetah | Medium | 759.4 | - | 331.4 |

STAIRS-Former在SMAC Marine-Hard（Medium）上达到57.9%，较HiSSD提升8.4个百分点；在SMAC-v2上达到30.3%，较HiSSD提升5.9个百分点。MAMuJoCo结果因协议差异未直接对比，但显著优于ODIS。

| 消融组件 | Seen任务均值 | Unseen任务均值 | 总均值 |
| :--- | :--- | :--- | :--- |
| STAIRS-Former | 77.9 | 64.0 | 67.4 |
| w/o Spatial | 72.4 | 60.2 | 63.1 |
| w/o Temporal | 76.2 | 60.6 | 64.6 |
| w/o Dropout | 76.0 | 61.8 | 65.4 |

空间模块移除导致Seen任务性能下降5.5个百分点，Unseen任务下降3.8个百分点，表明空间递归对已知环境结构化交互至关重要。时间模块移除对Unseen任务影响更大（3.8个百分点），验证其在部分可观测环境下捕捉长程依赖的作用。Token-Dropout移除导致Unseen任务性能下降2.2个百分点，证明其对智能体数量变化的鲁棒性贡献。

评估指标涵盖胜率与Episode Return，但未报告计算效率与通信开销。代码开源，超参数包括隐藏层维度64、递归步数2、时间间隔3、Dropout率0.1。SMAC-v2上30.3%的绝对胜率较低，可能受限于数据集质量而非算法上限。

## 关联研究分析

从问题动机看，STAIRS-Former与HiSSD均解决离线MT-MARL泛化问题，但HiSSD侧重技能分解与共享，STAIRS-Former侧重架构增强。差异根源在于任务特性：HiSSD假设技能可分解，STAIRS-Former假设关系可递归建模。在智能体数量剧烈变化时，HiSSD的技能共享可能失效，而STAIRS-Former的Token-Dropout通过随机正则化提供鲁棒性，但论文未验证极端数量变化（如从10智能体到1智能体）下的性能衰减。

从方法设计看，STAIRS-Former与CoFlow同属离线MARL路线，但CoFlow采用生成式模型缓解分布偏移，STAIRS-Former采用保守Q分解。差异根源在于数据质量：CoFlow适用于数据丰富场景，STAIRS-Former适用于数据有限且智能体数量变化场景。STAIRS-Former未对比CoFlow，可能因生成式模型计算开销大，但论文未给出计算效率对比，无法判断架构增强是否以牺牲效率为代价。

## 总结

STAIRS-Former解决的核心矛盾是离线MT-MARL中智能体数量变化与长程历史依赖的联合建模。现有方法仅用Transformer适配观测维度，未能利用其建模复杂依赖的潜力，而本文通过空间递归与时间层级结构释放了这一潜力。方法在SMAC Marine-Hard（Medium）上达到57.9%，较HiSSD提升8.4个百分点，在SMAC-v2上达到30.3%。边界在于SMAC-v2绝对胜率较低，且未验证极端智能体数量变化下的鲁棒性。当智能体数量从10降至1时，Token-Dropout的随机正则化是否足以维持策略稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11691)