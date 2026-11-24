# ICLR2026最新论文 ｜AlphaFlow: Understanding and Improving MeanFlow Models ｜α-Flow：解耦流匹配与一致性损失的统一框架

研究机构：美国密歇根大学

作者：Huijie Zhang、Aliaksandr Siarohin、Willi Menapace 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.20771)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20771)

> 少步生成模型在从多步扩散模型蒸馏或从零训练时，常面临推理效率与生成保真度的权衡，现有方法如 MeanFlow 虽提升了稳定性，但其内部优化机制尚不清晰。本文切入点在于揭示 MeanFlow 目标函数中轨迹流匹配与轨迹一致性两项损失存在严重的梯度负相关，导致联合优化缓慢且不稳定。通过引入 α-Flow 统一框架，利用课程学习策略平滑过渡这两项损失，实现了更高效的收敛。该工作确立了少步生成中解耦优化目标的新范式，但其对特定骨干网络依赖及超参数敏感性的影响仍需进一步验证。

## 研究背景

流匹配（Flow Matching, FM）通过回归确定性常微分方程（ODE）的速度场，取代了传统扩散模型依赖随机微分方程（SDE）模拟的训练范式。在少步生成场景中，模型需直接预测从噪声到数据的平均速度场，而非瞬时速度。这一过程涉及两个核心概念：轨迹流匹配（Trajectory Flow Matching, TFM）负责建立噪声到数据的映射基础，而轨迹一致性（Trajectory Consistency, TCc）则确保模型在不同时间步间的预测保持一致性。TFM 提供了边界条件，防止 TCc 收敛至平凡解，但二者在优化过程中存在内在张力。

现有少步生成方法如一致性模型（Consistency Models, CM）和 Shortcut Models 虽实现了单步或几步生成，但性能与多步模型仍有显著差距。MeanFlow 框架通过估计平均速度场显著缩小了这一差距，但其成功机制缺乏理论解释。具体而言，MeanFlow 训练中将 75% 的计算资源分配给边界情况（$r=t$）的流匹配监督，这一启发式策略的有效性未被充分理解。本文的核心切入点是分析 MeanFlow 目标函数的分解结构，揭示 TFM 与 TCc 之间的梯度冲突，并据此设计更高效的优化策略。

## 核心方法

### 方法参照系

MeanFlow 的训练目标 $L_{MF}$ 可视为一致性模型与流匹配的混合体。标准流程中，模型 $u_\theta(z_t, r, t)$ 学习从时间 $t$ 到 $r$ 的平均速度。本文将其置于“映射学习”路线下，关键差异在于 MeanFlow 联合优化 TFM 与 TCc，而本文旨在通过解耦这两项损失来消除优化冲突。

### 目标分解与梯度冲突分析

MeanFlow 损失可代数分解为 TFM 损失 $L_{TFM}$ 和 TCc 损失 $L_{TCc}$ 之和：

$$ L_{MF}(\theta) = L_{TFM}(\theta) + L_{TCc}(\theta) + C $$

其中 $C$ 为与参数无关的常数。$L_{TFM}$ 对应带有额外输入 $r$ 的流匹配损失，$L_{TCc}$ 则是无边界条件的轨迹一致性损失。实验分析表明，$L_{TFM}$ 与 $L_{TCc}$ 的梯度余弦相似度通常低于 -0.4，呈现强负相关。这种冲突源于 $L_{TCc}$ 缺乏显式边界条件，其最优解流形极大，而 $L_{TFM}$ 的流形狭窄。联合优化时，模型被拉向 $L_{TCc}$ 的宽泛流形，难以收敛至两者的交集。MeanFlow 中 75% 的计算用于 $r=t$ 的流匹配监督（$L'_{FM}$），这实际上是 $L_{TFM}$ 的代理损失，因其仅在 $r=t$ 处作用，与 $L_{TCc}$ 的梯度干扰较小，从而缓解了冲突，但计算效率低下。

### α-Flow 统一框架与课程学习

为解决上述冲突，本文提出 α-Flow 损失，通过引入中间时间步 $s$ 统一 TFM、Shortcut Models 和 MeanFlow：

$$ L_\alpha(\theta) = \mathbb{E}_{t,r} \left[ \| u_\theta(z_t, r, t) - (\alpha v + (1-\alpha) u_\theta(z_s, r, s)) \|^2 \right] $$

其中 $s = \alpha r + (1-\alpha) t$，$\alpha \in (0, 1]$ 为一致性步长比。当 $\alpha=1$ 时，$L_\alpha$ 退化为 TFM；当 $\alpha \to 0$ 时，退化为 MeanFlow。该框架的核心创新在于课程学习策略：训练初期 $\alpha=1$，优先优化 TFM 以建立可靠的噪声-数据映射；随后 $\alpha$ 从 1 平滑退火至 0，逐步引入 TCc 优化。这种策略解耦了 TFM 与 TCc 的优化过程，避免了早期训练中的梯度冲突，减少了对外部流匹配监督的依赖，从而提升了收敛速度与最终性能。

## 实验评估

实验在 ImageNet-1K 256×256 类条件生成任务上进行，使用 DiT-XL/2 骨干网络，在 SD-VAE 潜空间中训练。基线包括 MeanFlow、Shortcut Models 和 FACM。本文方法 α-Flow-XL/2+ 在 1-NFE 下取得 2.58 FID，2-NFE 下取得 2.15 FID，显著优于 MeanFlow-XL/2 的 3.47 FID（1-NFE）和 2.46 FID（2-NFE）。

| 方法 | 参数量 | Epochs | NFE 1 FID | NFE 2 FID |
| :--- | :--- | :--- | :--- | :--- |
| MeanFlow-XL/2 | 676M | 240 | 3.47 | 2.46 |
| α-Flow-XL/2 | 676M | 240 | 2.95 | 2.34 |
| α-Flow-XL/2+ | 676M | 240+60 | 2.58 | 2.15 |

消融实验显示，α 的退火调度对性能至关重要。固定 TFM 比例为 25% 时，Sigmoid 调度从 0K 到 400K 步的退火策略在 NFE 1 下取得 40.0 FID，优于恒定 0.0 调度的 44.4 FID。这表明平滑过渡比突然切换更利于优化。此外，增加 TFM 比例至 50% 时，NFE 2 FID 降至 37.1，但 NFE 1 FID 略升至 40.2，显示不同 NFE 下最优 TFM 比例存在差异。

评估边界方面，本文仅使用 FID 和 FDD 指标，未报告多样性指标如 IS 或 CLIPScore。实验局限于 DiT 骨干和 SD-VAE 潜空间，未验证在其他架构或潜空间中的泛化性。代码已开源，但超参数如 α 退火速率和 TFM 比例需针对具体任务调整，复现成本较高。

## 关联研究分析

从问题动机看，本文与 Consistency Models（CM）共享“少步生成”目标，但 CM 依赖蒸馏或复杂的时间步划分，而 α-Flow 通过统一框架从零训练，避免了蒸馏对教师模型的依赖。CM 的离散时间一致性训练需精心设计 $\Delta t$ 调度器，而 α-Flow 的连续时间框架通过 α 参数自然实现平滑过渡，简化了训练流程。这一差异源于任务特性：CM 侧重单步生成的精确性，而 α-Flow 兼顾少步生成的灵活性与稳定性。

从方法设计看，本文与 Shortcut Models 同属“映射学习”路线，但 Shortcut Models 通过“捷径”步骤的一致性训练，而 α-Flow 通过中间时间步 $s$ 的插值实现一致性。Shortcut Models 的 $L_{SC}$ 是 α-Flow 在 $\alpha=1/2$ 时的特例，但本文进一步揭示了其与 MeanFlow 的统一关系。与 MeanFlow 相比，α-Flow 的关键改进在于解耦 TFM 与 TCc 的优化，而非简单增加流匹配监督。这一设计选择解决了 MeanFlow 中梯度冲突导致的收敛缓慢问题，但 α 参数的引入也增加了超参数调优的复杂度，其在非 DiT 骨干下的表现尚不明确。

## 总结

本文要解决的核心矛盾是少步生成中 TFM 与 TCc 的梯度冲突导致的优化不稳定。现有方法如 MeanFlow 通过增加流匹配监督缓解冲突，但计算效率低下。本文抓住的切入点是目标函数的分解结构，通过 α-Flow 统一框架和课程学习策略，实现了 TFM 与 TCc 的解耦优化。实验证明，α-Flow-XL/2+ 在 1-NFE 下取得 2.58 FID，2-NFE 下取得 2.15 FID，显著优于 MeanFlow。本文的边界在于实验局限于 DiT 骨干和 SD-VAE 潜空间，未验证在其他架构中的泛化性，且 α 退火调度需精细调优。当骨干网络从 DiT 切换至 U-Net 时，α 退火速率的最优值是否发生显著变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20771)