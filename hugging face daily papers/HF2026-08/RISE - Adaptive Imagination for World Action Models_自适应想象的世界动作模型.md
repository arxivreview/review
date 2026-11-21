# HuggingFace最新推荐论文 ｜RISE: Adaptive Imagination for World Action Models ｜自适应想象的世界动作模型

研究机构：上海交通大学

论文原文见 [arXiv](https://arxiv.org/abs/2608.20430)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.20430)

> 自动驾驶中的世界动作模型（WAM）通过预测未来潜状态辅助规划，但现有方法对所有场景分配固定的想象预算，导致简单场景计算浪费、复杂场景预测不足。RISE 提出基于“未来规划增益”的逐步 Roll/Stop 决策机制，动态调整每个场景的 rollout 深度，并构建反事实数据集 CounterDrive 提供风险监督。该框架在 NAVSIM 和 nuScenes 上取得 SOTA 规划性能，但其增益是否完全归因于调度器而非数据增强，以及连续潜变量在长时程驾驶预测中的稳定性，仍存疑。

## 研究背景

当自动驾驶智能体面对相似视觉上下文却需做出不同决策时，仅依赖当前观察的轨迹回归失效，必须引入未来预测以评估动作后果。这种预测通常通过世界动作模型（WAM）实现，其核心是编码-预测-规划架构：编码器将像素观察压缩为潜变量，预测器生成未来潜状态序列，规划器基于这些潜状态输出轨迹。然而，固定深度的 rollout 假设所有场景需要同等量的未来推理，忽略了场景复杂度的异质性。

主流 WAM 路线包括共享骨干的“想象并规划”、级联的“先想象后规划”以及无想象的直接规划，但它们的推理调度均为全局静态设定。这种静态调度无法在部分 rollout 后重新评估当前前缀是否足以支撑规划，导致在简单场景中产生无效计算延迟，在复杂场景中因预测不足而规划质量下降。RISE 的切入点在于将想象深度从架构超参数转化为场景依赖的运行时决策变量，通过逐步评估继续 rollout 的预期规划收益与计算成本之比，实现自适应的想象预算分配。

## 核心方法

### 方法参照系

标准 WAM 流程为：编码器提取观察潜变量 $z_{obs}$，预测器自回归生成固定长度 $H$ 的未来潜变量序列 $\hat{Z}_{1:H}$，规划器基于 $\hat{Z}_{1:H}$ 生成轨迹。本文的关键差异在于引入调度器（Scheduler），将固定 $H$ 替换为动态终止条件，使有效 horizon $K$ 成为场景函数。

### 未来规划增益与风险画像

传统方法缺乏评估“继续预测是否值得”的信号。RISE 引入 Latent Evaluator 预测两个信号：风险画像 $R_h$ 和 未来规划增益画像 $B_h$。增益画像定义为在 rollout 步 $h$ 时，继续预测相对于当前停止带来的规划分数变化。其训练目标基于全 horizon 枚举的规划分数差：

$$
g^*_h = \max_{j \in \{h+1, \dots, H_D\}} [(q_j - q_h) - \lambda(c_j - c_h)]
$$

其中 $q_j$ 为在深度 $j$ 停止时的规划分数，$c_j$ 为计算成本，$\lambda$ 为成本权重。该公式的物理含义是：只有当继续预测带来的规划分数提升超过其计算成本时，增益才为正。风险画像 $R_h$ 则通过 CounterDrive 反事实数据监督，量化当前前缀已揭示的安全风险，弥补事实日志中缺失的潜在危险场景。

### 滚动门控与自适应调度

Rollout Gate 基于 Evaluator 输出执行二元决策。在步 $h$，若预测增益 $g^*_h > 0$，则执行 Roll，预测器追加一个未来潜变量；否则执行 Stop，将当前前缀传入规划器。有效 horizon $K(c; \lambda)$ 定义为：

$$
K(c; \lambda) = \min \left( \{h \mid d_h = \text{Stop}\} \cup \{H\} \right)
$$

这一设计避免了预先选择固定深度，使 horizon 从重复的 Roll/Stop 决策中涌现。与固定深度方法相比，该机制在简单场景（$K=0$）直接规划，在复杂场景（$K=H$）完整预测，中间场景按需分配，从而在规划质量与推理延迟之间取得场景依赖的平衡。

## 实验评估

实验在 NAVSIM v1/v2 和 nuScenes 上进行，基线覆盖 DAWN、DreamerAD、DriveFuture、EponaV2 等主流 WAM，但缺失纯 Model-Free 基线以隔离世界模型贡献。

| 方法 | NC↑ | DAC↑ | EP↑ | C↑ | TTC↑ | PDMS↑ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DAWN | 98.7 | 95.9 | 84.3 | 96.0 | 89.1 | 89.1 |
| DriveFuture | 98.8 | 99.1 | 95.4 | 84.2 | 90.7 | 90.7 |
| RISE | 99.1 | 97.7 | 98.3 | 98.6 | 91.5 | 91.5 |

RISE 在 NAVSIM v1 上以 91.5 PDMS 领先，超越 DriveFuture 的 90.7 和 DAWN 的 89.1，且在碰撞率（C）和 TTC 上均取得最优。

| 配置 | EPDMS↑ | PDMS↑ |
| :--- | :--- | :--- |
| Baseline | 88.9 | 89.7 |
| + CounterDrive | 89.8 | 90.5 |
| + Scheduler | 90.4 | 91.2 |
| + Both | 90.8 | 91.5 |

消融显示，Scheduler 单独贡献 1.5 EPDMS，CounterDrive 单独贡献 0.9 EPDMS，两者结合达到 90.8。在自适应 rollout 方法对比中，Scheduler 以 2.40 次平均 rollout 和 287.429 ms 延迟取得 90.8 EPDMS，优于 Random Stop（2.03 次，264.075 ms，89.5 EPDMS）和 Latent Margin（2.98 次，308.532 ms，89.7 EPDMS），证明基于规划增益的停止策略优于随机分配或潜变量收敛判据。

评估边界方面，NAVSIM 指标提升是否完全归因于 Scheduler 而非 CounterDrive 的数据增强贡献，论文未提供单独移除 Scheduler 但保留 CounterDrive 的完整对比。可复现性上，代码已开源，使用 8×A100 GPU 训练，超参数包括 $\lambda=0.005$ 和 V-JEPA 2 冻结编码器。

## 关联研究分析

从问题动机看，RISE 与 DriveFuture 同属潜空间 WAM，但 DriveFuture 使用固定深度 rollout，而 RISE 将深度作为运行时决策变量。这一差异源于对“想象成本”的认知：DriveFuture 假设固定深度是规划质量的必要保障，RISE 则认为多数场景的规划质量在早期前缀即可稳定，继续预测仅增加延迟。根源在于驾驶场景的异质性：简单直行场景与复杂交互场景对未来预测的需求差异巨大，固定深度无法适应这种分布。

从方法设计看，RISE 与 DreamerAD 同基于潜空间动力学，但 DreamerAD 依赖 RL 训练策略，RISE 采用端到端规划。RISE 的 Latent Evaluator 预测风险画像，而 DreamerAD 通过 RL 值函数隐式学习风险。差异在于监督信号：RISE 使用 CounterDrive 反事实数据提供显式风险标签，DreamerAD 依赖环境奖励。RISE 的显式风险监督在安全关键场景可能更鲁棒，但依赖高质量反事实数据生成，而 DreamerAD 的隐式学习无需额外数据但可能收敛缓慢。

## 总结

RISE 解决的核心矛盾是固定想象预算与场景异质性之间的冲突。其切入点在于将想象深度从架构超参数转化为基于“未来规划增益”的运行时决策，通过 Latent Evaluator 预测规划收益与风险，Rollout Gate 执行成本感知的 Roll/Stop 决策。实验证明该机制在 NAVSIM 上取得 91.5 PDMS，超越固定深度基线 0.8-2.4 个点，且平均 rollout 次数低于全深度方法。边界在于，Scheduler 的增益部分依赖 CounterDrive 数据增强，两者贡献未完全解耦；且方法依赖 V-JEPA 2 冻结编码器，未探索编码器与调度器的联合优化。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.20430)