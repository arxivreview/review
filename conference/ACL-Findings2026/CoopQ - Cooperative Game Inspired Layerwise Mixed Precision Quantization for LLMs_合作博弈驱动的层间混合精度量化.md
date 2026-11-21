# ACL-Findings2026最新论文 ｜CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs ｜合作博弈驱动的层间混合精度量化

研究机构：美国加州大学尔湾分校

作者：Junchen Zhao、Ali Derakhshan、Jayden Kana Hyman 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15455)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15455)

> 大语言模型（LLM）在极低比特部署时，传统基于单层敏感度的混合精度量化因忽略层间误差传播导致精度崩塌。CoopQ 将量化建模为层间合作博弈，通过渐进量化估计 Shapley 值以捕捉交互效应，并利用混合整数线性规划求解全局最优位宽分配。该方法在 2-4 bit 区间显著降低了困惑度，但其离线计算开销与二元位宽限制构成了实际部署的边界。

## 研究背景

LLM 量化压缩的核心矛盾在于内存预算与模型精度的权衡。后训练量化（Post-Training Quantization, PTQ）因无需重训练成为主流，但均匀位宽假设无法适应不同层对量化误差的敏感度差异。混合精度量化（Mixed-Precision Quantization, MPQ）旨在为敏感层保留高位宽，为容忍层分配低位宽，从而在固定内存预算下最小化任务损失。然而，MPQ 本质上是 NP-hard 的组合优化问题，其求解难度随层数指数级增长，且层间误差传播使得局部敏感度评估失效。

早期方法如 HAWQ 利用 Hessian 矩阵迹评估层敏感度，通过线性规划求解位宽分配，确立了“敏感度驱动”的逻辑，但假设层间误差独立且可加，忽略了深层网络中的误差累积效应。随着 LLM 参数量激增，Hessian 计算成本不可接受，且低比特下的精度悬崖暴露了单纯算法优化的局限。现有 PTQ 方法多依赖孤立指标（如权重分布、余弦相似度），未能捕捉量化误差在网络中的传播路径，导致高精度资源被错误分配。CoopQ 的切入点在于引入合作博弈论，将层间交互效应显式纳入优化目标，解决局部最优陷阱。

## 核心方法

### 方法参照系

MPQ 的标准流程包含敏感度评估、位宽分配与量化执行。传统方法将敏感度评估简化为单层指标计算，位宽分配采用贪心或线性规划。CoopQ 的关键差异在于将敏感度评估升级为全局交互敏感度，并将位宽分配建模为考虑层间耦合的二次优化问题，而非独立的线性约束。

### 渐进量化 Shapley 估计

传统 Shapley 值估计依赖层剪枝，导致模型性能急剧下降且估计方差极大。CoopQ 提出渐进量化 Shapley 估计（Shapley-based Progressive Quantization Estimation, SPQE），通过逐步降低层精度而非直接移除层，维持模型稳定性。对于层 $i$，其 Shapley 值 $\hat{\phi}_i$ 定义为在所有随机排列 $\pi$ 中，层 $i$ 从高位宽 $b_{high}$ 降至低位宽 $b_{low}$ 时，模型价值函数（每 token 负对数似然）的平均边际变化：

$$ \hat{\phi}_i = \frac{1}{M} \sum_{\pi \in \Pi} \left[ v(S_{\pi, i} \cup \{i\}) - v(S_{\pi, i}) \right] $$

其中 $S_{\pi, i}$ 为排列 $\pi$ 中层 $i$ 之前已量化的层集合。该设计通过渐进式精度降低避免了剪枝导致的性能崩塌，确保了 Shapley 估计的低方差与准确性。

### 二次优化与 MILP 求解

基于 SPQE 估计的 Shapley 值，CoopQ 构建二次代理模型以量化层间交互。通过二阶泰勒展开，损失变化 $\Delta L$ 近似为线性敏感度 $\mathbf{a}$ 与交互矩阵 $\mathbf{K}$ 的函数。位宽分配被建模为二元二次规划问题，其中二元变量 $q_i$ 指示层 $i$ 是否保留高位宽：

$$ \min_{\mathbf{q}} \mathbf{a}^T \mathbf{q} + \mathbf{q}^T \mathbf{K} \mathbf{q} \quad \text{s.t.} \quad \sum_{i=1}^L c_i q_i \le B $$

为求解该组合优化问题，CoopQ 引入辅助变量 $y_{ij}$ 线性化二次项 $q_i q_j$，将其转化为混合整数线性规划（Mixed-Integer Linear Program, MILP）。这一转换使得标准求解器（如 SCIP）能够获取全局最优位宽分配，克服了贪心算法的局部最优局限。

## 实验评估

实验在 Llama-3、Gemma-2 和 Qwen-3 模型上进行，使用 WikiText-2 验证集评估困惑度（Perplexity, PPL），对比基线包括 GPTQ、Quanto 和 HQQ 框架下的 Activation、Sensitivity、LIM 和 Z-Score 方法。CoopQ 在低比特区间表现突出，例如在 Gemma-2-2B 2.01–2.5 bits 区间，CoopQ 的 PPL 为 233.98，较 Sensitivity（1120）和 LIM（1250）分别降低 79% 和 81%。

| 模型 | 位宽区间 | GPTQ Sens. | GPTQ LIM | GPTQ CoopQ |
|---|---|---|---|---|
| Gemma-2-2B | 2.01–2.5 | 1.12×10³ | 1.25×10³ | 233.98 |
| Gemma-2-9B | 2.01–2.5 | 189.55 | 214.03 | 48.52 |
| Llama-3.2-3B | 2.5–3.0 | 343.64 | 164.43 | 73.11 |
| Qwen3-4B | 2.01–2.5 | 1.56×10³ | 2.38×10³ | 697.28 |

消融实验表明，SPQE 采样数对性能影响显著。在 Llama-3.1-8B 上，采样数从 10 增至 50 时，平均 PPL 相对变化从 -0.04% 降至 -2.84%，几何均值相对变化从 -4.10% 降至 -19.93%。超过 50 次采样后，收益边际递减，100 次采样时几何均值相对变化为 -19.88%，表明 50-100 次采样是计算成本与精度的平衡点。

评估边界方面，CoopQ 仅评估了 2-bit 和 4-bit 的二元分配，未探索中间位宽（如 3-bit）或细粒度块级量化。实验未在真实 NPU/FPGA 硬件上验证延迟与能耗，MILP 求解的离线时间复杂度随层数增长，可能限制其在超大模型上的可扩展性。代码未公开，但提供了固定种子与超参数（$\alpha=0.5$）以保证可复现性。

## 关联研究分析

从问题动机看，CoopQ 与 HAWQ 均基于敏感度驱动位宽分配，但 HAWQ 依赖 Hessian 迹的局部近似，而 CoopQ 通过 Shapley 值捕捉全局交互。HAWQ 在视觉模型上有效，但在 LLM 低比特下因忽略误差传播导致次优分配；CoopQ 的博弈论框架直接回应了层间耦合效应，但计算成本更高。从方法设计看，CoopQ 与 GAMMA 均追求全局最优，但 GAMMA 采用可微分松弛（Gumbel-Softmax）实现连续优化，CoopQ 采用 MILP 求解离散优化。GAMMA 允许任意位宽组合，灵活性更高，但缺乏全局最优性保证；CoopQ 提供最优解，但受限于二元位宽假设，无法适应需要 3-bit 等中间精度的场景。

## 总结

CoopQ 旨在解决 LLM 低比特量化中层间误差传播导致的精度崩塌问题。现有方法依赖局部敏感度，忽略层间交互，导致全局次优；CoopQ 通过合作博弈论显式建模交互效应，利用 SPQE 估计 Shapley 值，并通过 MILP 求解全局最优位宽分配。实验证实，在 2-4 bit 区间，CoopQ 较局部指标方法降低 PPL 20-80%，验证了全局交互建模的有效性。然而，其二元位宽限制与 MILP 离线计算开销构成了实际部署的边界。当模型层数增加至数百层时，MILP 求解时间是否呈指数增长，从而限制其在超大 LLM 上的适用性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15455)