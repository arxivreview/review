# HuggingFace最新推荐论文 ｜Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation ｜离线在线策略蒸馏

作者：Yecheng Wu、Song Han、Hai Cai

论文原文见 [arXiv](https://arxiv.org/abs/2604.13010)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13010)

> 在线策略蒸馏（On-Policy Distillation, OPD）通过密集token级监督提升大语言模型推理能力，但依赖实时教师服务器导致算力开销巨大。现有离线化尝试因忽视“教师一致性”约束而性能受损。本文提出Lightning OPD，强制SFT与OPD阶段使用同一教师并预计算log-prob，实现4.0倍加速。该方法在AIME 2024上达到69.9%，但固定rollout分布可能限制模型探索教师分布外的新路径。

## 研究背景

在线策略蒸馏（OPD）是后训练阶段的关键技术，其核心机制是让学生模型在当前策略生成的轨迹上，匹配更强教师模型的token级分布。与基于可验证奖励的强化学习（RLVR）相比，OPD提供密集监督信号，训练更稳定且成本更低。然而，标准OPD要求教师在每个梯度步实时评分学生rollout，这需要部署多GPU教师服务器，成为学术研究的算力瓶颈。

后训练领域长期关注SFT与RL的协同，但OPD特有的“双教师”结构被忽视。SFT阶段使用教师A生成数据，OPD阶段使用教师B提供参考分布，这种不一致在RLVR中不存在，因为RLVR仅依赖单一奖励信号。现有流水线常沿用RLVR惯例，随意选择高质量SFT数据而忽略OPD教师匹配，导致训练目标出现不可约偏差。本文切入点在于揭示这一被忽略的结构性缺陷，并证明在教师一致性约束下，离线预计算教师log-prob可完全替代实时服务器。

## 核心方法

### 方法参照系

标准OPD流程包含SFT冷启动与在线蒸馏两阶段。SFT阶段用教师轨迹微调基座模型得到参考策略 $\pi_{ref}$；OPD阶段从当前策略 $\pi_\theta$ 采样rollout，实时查询教师计算优势函数。本文问题与该通用流程的关键差异在于：将在线rollout替换为SFT阶段预计算的固定rollout，并强制SFT与OPD教师一致。

### 教师一致性约束

标准OPD中，SFT教师与OPD教师可独立选择，但本文发现这种不一致会引入梯度偏差。设SFT教师为 $\pi_{T}^{SFT}$，OPD教师为 $\pi_{T}^{OPD}$，定义教师不匹配量 $\Delta_t = \log \pi_{T}^{SFT}(a_t|s_t) - \log \pi_{T}^{OPD}(a_t|s_t)$。当 $\Delta_t \neq 0$ 时，训练目标存在不可约偏差，导致在线与离线OPD均收敛至次优固定点。该约束解决了此前方法中因教师错配导致的性能衰减，例如Thinking Machines Lab使用QwQ-32B生成SFT数据却用Qwen3-32B作为OPD教师，造成8B模型AIME 2024准确率下降3.7至6.8个点。

### 离线预计算机制

在教师一致性成立时，Lightning OPD将OPD阶段分为预处理与训练两阶段。预处理阶段从 $\pi_{ref}$ 采样rollout，一次性计算并存储教师log-prob：

$$
\mathcal{D}_{OPD} = \{ (q_j, x_j, \{\log \pi_T(a_t^j|s_t^j)\}_{t=1}^T) \}
$$

训练阶段学生 $\pi_\theta$ 初始化自 $\pi_{ref}$，优势函数计算为 $A_t(\theta) = \log \pi_T(a_t|s_t) - \log \pi_\theta(a_t|s_t)$，其中教师项直接读取预存值，学生项在线计算。该设计消除了实时教师服务器需求，且理论证明在教师一致性下，离线目标与在线目标共享最优解，梯度差异有界，并引入隐式正则化防止策略漂移。

## 实验评估

实验在Qwen3-4B与8B模型上验证，数学推理使用AIME 2024/2025、HMMT 2025，代码生成使用LiveCodeBench v5/v6。基线包括标准OPD、ExOPD及SFT，但缺失GRPO、PPO等RLVR强基线，无法直接对比OPD与RLVR的范式差异。

| 模型规模 | 方法 | AIME 2024 | AIME 2025 | HMMT 2025 | LCB v5 | LCB v6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 4B | SFT | 56.7 | 52.1 | 34.0 | 33.8 | 31.5 |
| 4B | OPD | 65.4 | 57.9 | 39.9 | 44.2 | 39.3 |
| 4B | Lightning OPD | 68.1 | 58.4 | 39.8 | 42.8 | 40.3 |
| 4B | ExOPD | 61.0 | 56.0 | 34.4 | – | 29.0 |
| 8B | SFT | 63.7 | 51.7 | 36.9 | 44.7 | 36.8 |
| 8B | OPD | 68.5 | 59.0 | 39.4 | 47.3 | 41.2 |
| 8B | Lightning OPD | 69.9 | 59.2 | 41.9 | 49.5 | 43.9 |

Lightning OPD在8B模型AIME 2024上达69.9%，超越标准OPD的68.5%；4B模型上68.1%显著优于ExOPD的61.0%。训练成本方面，8B模型从120 GPU小时降至30小时，实现4.0倍加速；4B模型从72降至20小时，加速3.6倍。

| 模型规模 | 方法 | GPU小时 | 加速比 |
| :--- | :--- | :--- | :--- |
| 4B | OPD | 72 | – |
| 4B | Lightning OPD | 20 | 3.6× |
| 8B | OPD | 120 | – |
| 8B | Lightning OPD | 30 | 4.0× |

消融实验验证教师一致性：8B模型中，SFT用Qwen3-32B、OPD用QwQ-32B时，Lightning OPD从69.9%降至63.1%（-6.8点），标准OPD从68.5%降至64.8%（-3.7点）。离线设置对教师错配更敏感，因固定rollout分布同时反映错误教师，偏差无法通过在线更新部分恢复。

评估边界：未报告置信区间，数值比较需谨慎；未提供代码与完整超参数，可复现性受限；缺失RLVR基线，无法量化OPD相对RLVR的范式优势。

## 关联研究分析

从问题动机看，本文与统一策略梯度（Unified Policy Gradient）路线共享“SFT与后续阶段目标统一”的思想，但聚焦于OPD特有的教师-学生动态。统一策略梯度通过数学推导模糊SFT与RL边界，而本文通过教师一致性约束解决OPD中双教师错配的结构性缺陷。差异根源在于任务特性：RLVR依赖单一奖励信号，不存在教师错配问题；OPD依赖教师分布，教师选择成为关键超参数。

从方法设计看，本文与RollPacker均关注训练效率，但解决不同瓶颈。RollPacker通过异步同步机制缓解长尾rollout导致的GPU气泡，优化数据并行效率；Lightning OPD通过消除实时教师服务器，优化基础设施开销。前者针对计算资源调度，后者针对模型服务依赖。固定rollout分布是否导致模型无法发现教师分布外的新推理路径，论文未给出回答，这与RLVR通过探索突破SFT上限的共识存在潜在张力。

## 总结

本文要解决的核心矛盾是OPD的高性能与高算力开销之间的冲突。现有方法因忽视教师一致性约束，离线化尝试性能受损；本文通过强制SFT与OPD教师一致并预计算log-prob，实现离线OPD与在线OPD最优解等价。实验证明8B模型AIME 2024达69.9%，训练成本降至30 GPU小时，实现4.0倍加速。边界在于固定rollout分布可能限制探索性，且缺失RLVR基线对比。当教师模型能力接近学生模型时，密集监督的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13010)