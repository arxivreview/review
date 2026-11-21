# HuggingFace最新推荐论文 ｜On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics ｜解耦蒸馏动态：Rollout Policy 与 KL 方向的因果归因

研究机构：英国剑桥大学

作者：Julianna Piskorz、Antonin Berthon、Mihaela van der Schaar

论文原文见 [arXiv](https://arxiv.org/abs/2609.35259)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.35259)

> 大语言模型后训练领域长期存在“在线策略蒸馏优于离线策略”的共识，但既有研究往往混淆了数据生成策略、散度度量与优化超参数的独立贡献。本文通过强到弱蒸馏控制实验，将 Rollout Policy（轨迹生成策略）与 KL 方向（散度类型）解耦，发现前向 KL 对策略变化具有鲁棒性，而灾难性遗忘主要由学习率决定。这一发现挑战了在线策略蒸馏的普适优越性，为低成本离线蒸馏提供了理论依据，但其结论在长链推理任务中的泛化性仍存疑。

## 研究背景

自回归语言模型在训练时依赖教师或真实标签，推理时却依赖自身生成的前缀，这种训练-推理分布失配导致误差累积，即曝光偏差。为缓解此问题，在线策略蒸馏（On-Policy Distillation, OPD）让学生模型在自生成轨迹上接受教师反馈，而离线策略蒸馏（Off-Policy Distillation, OffPD）则使用固定的教师生成数据。然而，OPD 需要实时生成序列并计算教师 Logits，计算成本远高于 OffPD。若 OPD 的优势并非源于策略本身，而是源于其他混杂变量，则其高昂的计算开销可能是不必要的。

现有研究常将 OPD 与反向 KL 散度（Reverse KL, RKL）配对，将 OffPD 与前向 KL 散度（Forward KL, FKL）配对，导致无法区分是“在线采样”还是“RKL 度量”带来了性能提升。SFT 与 RLVR 的对比同样存在目标函数、监督密度等多重变量混杂，使得 Rollout Policy 的因果贡献难以隔离。本文切入点在于利用强到弱蒸馏作为受控测试床，在保持其余训练管道固定的前提下，独立变化 Rollout Policy 与 KL 方向，从而厘清各因素对任务精度、灾难性遗忘及参数更新稀疏性的真实影响。

## 核心方法

### 方法参照系

标准强到弱蒸馏流程假设教师与学生共享词表，通过最小化师生输出分布的散度来迁移知识。传统范式通常固定“FKL 配 OffPD”或“RKL 配 OnPD”的组合。本文的关键差异在于打破这种绑定，将 Rollout Policy（教师生成 vs. 学生生成）与 KL 方向（FKL vs. RKL）作为独立变量进行全因子实验设计，并引入连续插值机制以分析策略影响的边界。

### 独立变量解耦与散度梯度分析

为隔离 Rollout Policy 的效应，本文在 Llama 3 和 Qwen2.5 模型族上，独立变化轨迹来源（OffPD/OnPD）与散度方向（FKL/RKL），同时控制学习率。核心创新在于对 Token 级 KL 梯度的理论分析，揭示了散度方向对策略敏感性的不对称性。前向 KL 的梯度定义为：

$$ \nabla_\theta D_{F-KL}(\pi_S^\theta, \pi_T) = -E_{y_n \sim \pi_T} \nabla_\theta \log \pi_S^\theta(y_n) $$

该公式表明 FKL 的梯度仅依赖于教师分布采样的 Token，其数值大小不受学生当前策略 $\pi_S^\theta$ 的影响，因此对 Rollout Policy 的变化具有鲁棒性。相比之下，反向 KL 的梯度为：

$$ \nabla_\theta D_{R-KL}(\pi_S^\theta, \pi_T) = E_{y_n \sim \pi_S^\theta} \left( \log \frac{\pi_S^\theta(y_n)}{\pi_T(y_n)} \right) \nabla_\theta \log \pi_S^\theta(y_n) $$

RKL 梯度包含无界对数概率比项，当学生策略与教师分布差异较大时，单个 Token 可能产生巨大梯度，导致优化不稳定。这一设计动机在于解释为何 RKL 在 OnPD 下表现敏感，而 FKL 在 OffPD 下依然稳定，从而为选择低成本 OffPD 提供理论支撑。

### 连续策略谱系与鲁棒性验证

为进一步量化策略影响，本文引入 Student-Teacher Rollout Spectrum，通过参数 $\lambda$ 在教师偏好与学生偏好之间插值，甚至外推至偏向某一模型的 Token 区域。实验显示，FKL 在整个谱系上保持高精度（波动仅 5.2 个百分点），而 RKL 性能随策略偏移显著下降。此外，通过移除梯度裁剪和使用单样本 KL 估计器进行消融，验证了上述结论并非由优化技巧或全词表计算引入的偏差所致，确认了散度方向本身是决定策略敏感性的根本因素。

## 实验评估

| 配置 | Held-out ID Accuracy (%) | Mean OOD Accuracy Change (pts) | Update Sparsity (%) |
| :--- | :--- | :--- | :--- |
| OnPD · F-KL (LR 1e-5) | 72 | -1.3 | 89.6 |
| OffPD · F-KL (LR 1e-5) | 73 | -1.3 | 88.8 |
| OnPD · R-KL (LR 1e-5) | 35 | -1.3 | 88.5 |
| OffPD · R-KL (LR 1e-5) | 72 | -1.3 | 90.0 |
| OnPD · F-KL (LR 5e-5) | 71 | -11.2 | 51.9 |
| OffPD · F-KL (LR 5e-5) | 73 | -14.0 | 60.0 |

实验在 Countdown、Science 和 MedReason 任务上进行，基线覆盖 OnPD/OffPD 与 FKL/RKL 的所有组合，但缺乏与 GKD、MiniLLM 等具体算法变体的直接对比，仅对比策略类型。数据显示，在低学习率下，OnPD 与 OffPD 的最终精度几乎相同（72% vs 73%），且遗忘程度一致；在高学习率下，OffPD 的遗忘程度甚至低于 OnPD。

消融实验表明，学习率是遗忘和稀疏性的主导因素。当学习率从 $1 \times 10^{-5}$ 增至 $5 \times 10^{-5}$ 时，更新稀疏性从 85.3%-89.6% 降至 51.9%-60.0%，而 Rollout Policy 的差异在此范围内可忽略不计。反直觉发现是，移除梯度裁剪后，RKL 性能大幅下降，而 FKL 保持稳定，证实了 RKL 对优化稳定性的脆弱性。

评估边界方面，本文主要使用 Accuracy 和 Sparsity 指标，未报告 ROUGE-L 等生成质量指标，可能掩盖了文本流畅性的差异。代码未公开，但提供了详细的超参数和种子设置，可复现性较高。然而，实验主要基于短序列算术和科学推理任务，未涵盖长链推理场景，限制了结论的泛化范围。

## 关联研究分析

从问题动机看，本文与 MiniLLM (Hsieh et al., 2024) 形成直接冲突。MiniLLM 主张 RKL 结合 On-Policy 能解决 FKL 的长尾过估计问题，隐含假设 On-Policy 是 RKL 生效的必要条件。本文通过解耦实验证明，RKL 的性能优势高度依赖于策略匹配，而在 FKL 下，Off-Policy 即可达到同等精度。这一差异根源在于 MiniLLM 未控制学习率变量，其观察到的“On-Policy 优势”可能部分源于优化稳定性而非策略本身。

从方法设计看，本文与 GKD (Agarwal et al., 2023) 的在线策略采样机制不同。GKD 将 On-Policy 视为消除曝光偏差的标准手段，而本文指出在短序列任务中，Off-Policy 的分布偏移影响有限，且 FKL 的鲁棒性使其对采样来源不敏感。GKD 未探讨散度方向与策略的交互作用，导致其无法解释为何在某些配置下 Off-Policy 表现更好。本文的连续谱系分析填补了这一空白，但其在长链推理任务中的适用性，GKD 的框架未提供参照，需进一步验证。

## 总结

本文旨在解决强到弱蒸馏中 Rollout Policy 因果贡献不清的问题，通过解耦策略与散度方向，揭示了 FKL 对策略变化的鲁棒性以及学习率对遗忘的主导作用。实验证明，在短序列任务中，Off-Policy 蒸馏在精度和稳定性上不劣于 On-Policy，且计算成本更低。然而，本文实验局限于短序列算术与科学推理，未覆盖长链推理场景，且未对比具体算法变体。当任务长度增加至数百 Token 时，Off-Policy 的分布偏移是否会导致精度显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.35259)