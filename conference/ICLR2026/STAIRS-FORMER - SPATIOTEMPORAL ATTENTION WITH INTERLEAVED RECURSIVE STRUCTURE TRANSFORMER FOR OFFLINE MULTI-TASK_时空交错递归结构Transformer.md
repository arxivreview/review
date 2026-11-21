# ICLR2026最新论文 ｜STAIRS-FORMER: SPATIOTEMPORAL ATTENTION WITH INTERLEAVED RECURSIVE STRUCTURE TRANSFORMER FOR OFFLINE MULTI-TASK MULTI-AGENT REINFORCEMENT LEARNING ｜时空交错递归结构Transformer

研究机构：韩国科学技术院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_67266774)

> 离线多任务多智能体强化学习（Offline MT-MARL）面临智能体数量动态变化与部分可观测性下长时程依赖建模的双重挑战。现有基于Transformer的方法仅利用其处理变长观测维度的能力，却未挖掘其建模复杂Token关系与历史序列的潜力，导致注意力分布均匀且历史信息利用不足。本文提出STAIRS-Former，通过引入空间递归模块、分层时间模块及Token-Dropout机制，重构了Transformer在离线MT-MARL中的信息处理流程。该架构在SMAC等基准上实现了SOTA性能，但其对连续动作空间的支持及与显式保守正则化方法的对比尚存疑。

## 研究背景

多智能体系统在实际部署中常面临智能体数量不固定的场景，例如无人机集群在部分节点失效后仍需维持协作。这种可变性要求策略网络能够适应不同长度的观测Token序列，同时，部分可观测性（Partial Observability）迫使智能体依赖历史观测来推断全局状态，这对长时程依赖的捕捉提出了严格要求。

离线多智能体强化学习（Offline MARL）旨在从固定数据集学习策略以避免在线交互的风险，但面临分布偏移与过拟合问题。主流方法如ODIS和HiSSD采用UPDeT架构，利用Transformer处理变长观测，但仅将其视为维度适配器，未深入利用其建模Token间复杂关系的能力。实验分析表明，HiSSD的注意力权重在已知与未知任务中均呈均匀分布，且单一历史Token仅执行简单RNN操作，无法有效整合长时程信息。本文切入点在于重构Transformer内部结构，通过空间与时间维度的递归与分层设计，增强对关键实体的选择性注意力及历史依赖的捕捉能力。

## 核心方法

### 方法参照系

离线MT-MARL的标准流程基于UPDeT架构，将智能体观测分解为自身、队友与环境实体Token，经线性变换后输入单层Transformer，输出局部Q值并通过Qatten网络聚合。该流程的关键局限在于单层结构表达力不足，且历史Token仅作为线性组合输入，无法捕捉部分可观测环境下的长时程依赖。

### 空间递归模块

针对单层Transformer无法捕捉实体间复杂关系导致注意力均匀分布的问题，STAIRS-Former引入空间递归模块（Spatial Recursive Module）。该模块通过多层递归Transformer结构，在每一层内对实体Token进行多次自注意力计算，逐步细化实体间的相关性推理。其核心公式为：

$$ h^{(l)}_{r+1} = \text{Transformer}(h^{(l)}_r; \theta_S) $$

其中 $h^{(l)}_r$ 表示第 $l$ 层第 $r$ 次递归后的隐藏状态。这一设计使得模型能够迭代地聚焦于最相关的实体，解决了此前方法在异构任务中无法区分关键队友与环境噪声的问题，提升了策略对未知实体配置的泛化能力。

### 分层时间模块与Token-Dropout

空间模块处理了当前时刻的实体关系，但部分可观测性要求智能体整合历史观测。STAIRS-Former引入分层时间模块，结合GRU与时间焦点层（TFL），以步长 $T_H$ 进行周期性更新，捕捉短期与长期依赖。同时，为应对智能体数量变化导致的过拟合，引入Token-Dropout机制，在训练时随机丢弃实体Token。其时间更新公式为：

$$ g_t = \text{GRU}(g_{t-T_H}, h_t; \psi) $$

其中 $g_t$ 为时间状态，$h_t$ 为空间模块输出。Token-Dropout通过随机缺失实体信息，迫使模型学习不依赖特定数量智能体的鲁棒表示，解决了离线数据中智能体数量固定导致的分布偏移问题。

## 实验评估

实验在SMAC、SMAC-v2、MPE及MAMuJoCo基准上进行，基线包括UPDeT-m、ODIS及HiSSD，覆盖了离线MT-MARL的主要架构路线，但未对比MAGIC或CoFlow等最新生成式或因果分配方法。

| 基准 | 任务集 | 数据集质量 | STAIRS-Former | HiSSD | ODIS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SMAC | Marine-Hard | Medium | 57.9 | 49.5 | 37.5 |
| SMAC | Stalker-Zealot | Medium | 38.2 | 19.4 | 22.5 |
| SMAC-v2 | Total Mean | Medium | 30.3 | 24.4 | 11.5 |
| MAMuJoCo | HalfCheetah | Medium | 759.4 | - | 331.4 |

在SMAC Marine-Hard任务中，STAIRS-Former在Medium数据集下达到57.9%的胜率，较HiSSD提升8.4个百分点，显示出空间递归模块对复杂实体关系的捕捉优势。SMAC-v2上30.3%的总均值虽低于领域综述中MAGIC的92.10%，但需注意SMAC-v2指标定义及子集差异，且本文相对基线提升显著。

消融实验表明，空间模块对已知任务性能影响最大，移除后性能从77.9%降至72.4%；而在未知任务中，空间、时间模块与Token-Dropout三者协同作用，移除任一组件均导致性能下降，其中Token-Dropout对泛化能力贡献显著。

评估边界方面，论文未报告计算效率与GPU内存占用细节，仅提供了参数数量对比。代码已开源，超参数包括隐藏层维度64、递归步数2及Dropout率0.1。MAMuJoCo连续控制任务中，STAIRS-Former在(1,1,1,1,1,1)任务上达到1006.0，但部分未知任务表现波动较大，显示其在连续动作空间下的稳定性有待验证。

## 关联研究分析

从问题动机看，STAIRS-Former与HiSSD均致力于解决离线MT-MARL中的智能体数量可变性，但HiSSD依赖分层技能学习提取可迁移模式，而STAIRS-Former聚焦于架构层面的注意力机制优化。差异根源在于对Transformer能力的理解：HiSSD将其视为技能容器，STAIRS-Former则将其视为关系推理引擎。这种差异导致STAIRS-Former在需要精细实体交互的任务中表现更优，但在技能复用性上可能不如HiSSD。

从方法设计看，STAIRS-Former与CoFlow同属离线MARL路线，但CoFlow采用生成式模型直接学习联合动作分布，而STAIRS-Former基于价值分解架构。CoFlow通过门控注意力学习协调修正，STAIRS-Former通过空间递归细化实体关系。两者均未显式使用CQL等保守正则化，而是依赖架构泛化或生成模型约束分布偏移。STAIRS-Former的Token-Dropout机制在功能上类似于数据增强，但其针对智能体数量变化的设计更具针对性，而CoFlow的少步采样更关注推理效率。

## 总结

STAIRS-Former旨在解决离线MT-MARL中智能体数量动态变化与长时程依赖建模的矛盾。现有方法如HiSSD仅利用Transformer处理变长维度，未挖掘其关系推理潜力，导致注意力均匀且历史利用不足。本文通过空间递归模块、分层时间模块及Token-Dropout机制，重构了信息处理流程，在SMAC Marine-Hard上达到57.9%胜率，较HiSSD提升8.4%。其边界在于连续动作空间下的稳定性未充分验证，且缺乏与显式保守正则化方法的对比。当智能体数量极端变化或环境动态剧烈时，Token-Dropout的随机性是否足以替代显式通信机制以维持协调精度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_67266774)