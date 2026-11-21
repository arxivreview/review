# ACL2026最新论文 ｜AdaJudge: Adaptive Multi-Perspective Judging for Reward Modeling ｜自适应多视角评判框架

研究机构：美国埃默里大学、香港中文大学

作者：Yongliang Miao、Yangyang Liang、Mengnan Du

论文原文见 [arXiv](https://arxiv.org/abs/2601.08097)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08097)

> 奖励模型（Reward Model, RM）旨在将人类偏好转化为标量信号以指导大语言模型对齐，但主流架构依赖固定池化策略压缩序列表示，导致数学推理等局部信号任务与安全对齐等全局信号任务间产生结构性冲突。现有方案通过数据清洗或骨干扩容提升性能，却忽视了评分头部的归纳偏置与任务证据分布的错配。本文提出 AdaJudge，通过深度门控精炼表示与域感知混合池化动态适配不同任务粒度。该框架在 JudgeBench 上超越强基线，但在 RM-Bench 上仍受限于训练数据规模，其架构改进能否完全弥补数据差距尚存疑。

## 研究背景

当奖励模型处理“计算 12×5+3”这类数学题时，正确答案往往集中在末尾 token，而处理“如何偷窃”这类安全提示时，危害性散布于整个响应。这种证据空间分布的任务依赖性，要求模型具备动态调整聚合策略的能力。然而，传统 RM 采用固定池化（如 last-token pooling），将高维 token 表示压缩为单一标量，这一静态归纳偏置迫使模型在局部精度与全局鲁棒性之间做出系统性妥协。

主流 RM 范式基于 Bradley-Terry 模型，假设单一池化机制能通用捕捉偏好信号。近期研究聚焦于提升数据质量或骨干容量，但评分头部设计长期未变。这种结构刚性导致模型在复杂基准上出现优化不稳定，例如小模型在多样化数据上发生表示崩溃。本文切入点在于解耦表示精炼与证据聚合，通过自适应机制替代固定压缩，解决生成式骨干表示与判别式目标之间的错位。

## 核心方法

### 方法参照系

标准 RM 流程为：预训练 Transformer 骨干编码提示-响应对，经固定池化（如 last-token）提取序列表示，再由线性头映射为标量奖励。本文关键差异在于将静态池化替换为两阶段自适应过程，分别解决表示空间错位与聚合策略僵化问题。

### 自适应表示精炼

固定池化假设骨干隐藏状态已包含足够判别信息，但骨干优化目标为下一词预测，导致细微偏好线索（如逻辑不一致）在原始空间中模糊。AdaJudge 在骨干后引入 K 个轻量 Transformer 块，通过深度门控机制动态组合中间状态。精炼表示 $\tilde{\mathbf{H}}$ 定义为：

$$ \tilde{\mathbf{H}} = \sum_{k=1}^{K} \alpha_k \mathbf{H}^{(k)} $$

其中 $\alpha \in \Delta_K$ 由全局上下文经 softmax 生成。该设计允许模型根据样本难度选择浅层线索或深层推理轨迹，避免单一 token 压缩导致的优化不稳定，尤其在小模型上防止表示崩溃。

### 域感知混合池化

静态池化无法同时捕捉数学任务的局部稀疏信号与安全任务的全局风格特征。AdaJudge 构建三个并行池化专家：last-token（$z_L$）、mean（$z_M$）、attention（$z_A$），并引入提示条件路由网络。最终奖励 $r$ 为：

$$ r = \sum_{v \in \{L,M,A\}} \pi_v s_v $$

其中 $\pi \in \Delta_3$ 由拼接向量 $[z_L; z_M; z_A; z_P]$ 经 softmax 生成，$s_v$ 为各视角 MLP 输出。该机制使模型根据提示意图动态加权不同粒度证据，解决固定策略在复杂实例上的性能瓶颈。

## 实验评估

实验基于 HelpSteer3 数据集（40.5K 偏好对），使用 Phi-3.5-mini、Qwen3-4B/8B 骨干，对比 Skywork-Reward 等强基线及同骨干固定池化基线。基线覆盖标量 RM 主流路线，但缺失生成式 RM 与因果去偏方法的直接对比。

| 模型 | RM-Bench Overall | JudgeBench Overall |
| :--- | :--- | :--- |
| Skywork-Reward-Llama-3.1-8B | 70.1 | 62.3 |
| Qwen3-8B + last token | 67.3 | 63.1 |
| Qwen3-8B + AdaJudge | 71.1 | 66.0 |

Qwen3-8B AdaJudge 在 RM-Bench 上较同骨干基线提升 3.8 点，在 JudgeBench 上提升 2.9 点，超越 Skywork-Reward-Llama-3.1-8B。

| 方法 | RM-Bench Hard | JudgeBench Math |
| :--- | :--- | :--- |
| Last-Token | 37.0 | 75.0 |
| Mean-Pool | 34.8 | 78.6 |
| AdaJudge | 43.7 | 80.4 |

消融显示，移除表示精炼模块后，JudgeBench 整体下降 3.4 点，Math 子集下降 5.4 点。Hard 子集上 AdaJudge 较最佳静态基线（Attention-Pooling）高 5.0 点，表明自适应聚合在复杂实例上收益显著。

评估边界方面，论文未报告置信区间，且 RM-Bench 结果低于领域 SOTA（Skywork-Reward-V2 82.4%），可能源于训练数据规模差异。代码未公开，超参数细节仅在附录提供，复现性受限。

## 关联研究分析

从问题动机看，InfoRM（Li et al., 2025）通过信息瓶颈过滤虚假特征，侧重数据层面的去偏；AdaJudge 则通过架构自适应解决任务依赖的归纳偏置错配。二者均针对 RM 的虚假相关性问题，但 InfoRM 假设偏差源于冗余信息，AdaJudge 假设偏差源于聚合策略僵化。这种差异暗示，当任务证据分布高度异构时，架构自适应可能比特征过滤更有效，但论文未对比二者在相同数据上的表现。

从方法设计看，DPO（Rafailov et al., 2023）绕过显式 RM 训练，直接优化策略；AdaJudge 保留显式 RM 以维持可解释性。DPO 牺牲了奖励信号的调试能力，而 AdaJudge 通过动态路由增强信号粒度。在计算受限场景下，DPO 的效率优势可能抵消 AdaJudge 的架构开销，但论文未评估端到端 RLHF 流程中的计算成本差异。

## 总结

本文核心矛盾在于固定池化策略与任务依赖证据分布的结构性错配。现有方法通过数据或骨干优化无法解决评分头部的归纳偏置僵化，AdaJudge 凭借深度门控精炼与域感知混合池化，在表示空间与聚合策略上实现双重自适应。实验证明其在 JudgeBench 上超越强基线，RM-Bench Hard 子集提升 5.0 点。边界在于训练数据规模受限导致 RM-Bench 整体低于 SOTA，且未评估在线 RLHF 中的推理延迟。当训练数据扩展至百万级时，架构自适应的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08097)