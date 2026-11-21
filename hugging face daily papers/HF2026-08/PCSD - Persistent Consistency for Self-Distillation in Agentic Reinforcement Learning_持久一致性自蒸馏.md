# HuggingFace最新推荐论文 ｜PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning ｜持久一致性自蒸馏

研究机构：北京理工大学、美团

作者：Chunji Lv、Yangguang Wei、Junlin Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.01837)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.01837)

> 导读 Agentic RL 的核心瓶颈在于长程轨迹仅获得单一稀疏奖励，导致中间步骤的信用分配失效。现有 On-policy Self-Distillation (OPSD) 虽引入教师信号，但单点估计易受采样噪声干扰，而步级聚合又丢失位置细节。本文提出 PCSD，通过评估教师支持信号在局部窗口的持久性，动态生成 Token 级蒸馏权重。该方法在 ALFWorld 上显著优于 GRPO 基线，但其固定超参数与冻结教师设定限制了其对动态环境变化的适应能力。

## 研究背景

多轮智能体任务中，策略 $\pi_\theta$ 需在部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP）下最大化累积回报。由于环境仅在轨迹末端提供标量奖励，模型难以区分关键决策与无关动作，导致梯度信号噪声大。为缓解此问题，On-policy Self-Distillation (OPSD) 引入特权上下文教师，在策略采样轨迹上提供密集 Token 级监督。然而，教师信号并非处处可靠：检索噪声或任务歧义可能导致教师在特定位置偏好次优 Token，盲目蒸馏会传递错误偏好。

Agentic RL 的主流路线已从单纯的强化学习转向 RL 与蒸馏的混合优化。Group Relative Policy Optimization (GRPO) 通过组内相对优势估计替代价值函数，降低了计算开销，但其监督仍停留在轨迹级粗粒度。现有可信度感知蒸馏方法面临两难：Token 级方法（如 SDAR）对单点差异敏感，易将采样波动误判为分布分歧；步级方法虽平滑噪声，却掩盖了教师可信度在位置间的显著变化。PCSD 的切入点在于识别“持久一致性”这一被忽略的特征：真正的教师优势应在局部邻域内持续存在，而孤立尖峰更可能源于噪声。

## 核心方法

### 方法参照系

本文基于 GRPO 框架，标准流程仅使用轨迹级优势估计。关键差异在于引入 Token 级教师-学生 Log-Prob Gap 计算，并新增持久一致性评估模块，将离散差异转化为连续蒸馏权重，与 GRPO 目标联合优化。

### 自适应聚合机制

固定窗口无法适应响应中异质的 Gap 模式。短窗口保留位置细节但敏感，长窗口平滑噪声但损失分辨率。PCSD 通过局部方差自适应插值短长窗口估计，解决单一窗口在噪声与分辨率间的权衡失效。

$$
\bar{\delta}^{adaptive}_{k,i} = (1 - r_{k,i})\bar{\delta}^{(N_{min})}_{k,i} + r_{k,i}\bar{\delta}^{(N_{max})}_{k,i}
$$

该公式根据局部 Gap 方差 $r_{k,i}$ 在短窗口（高分辨率）与长窗口（强平滑）间连续插值，方差低时侧重位置精度，方差高时侧重鲁棒性。

### 趋势调制与连续门控

指数衰减聚合虽强调邻近位置，但当前大 Gap 后接快速下降的教师支持仍会主导估计。PCSD 引入单侧趋势调制，抑制局部支持度下降时的噪声干扰，防止蒸馏信号引入优化震荡。

$$
w_{k,i} = \sigma(\beta_{gate} \cdot \bar{\delta}^{adaptive}_{k,i}) \cdot \eta_{k,i}
$$

该公式将自适应估计映射为有界连续权重，Sigmoid 门控分配蒸馏强度，趋势因子 $\eta_{k,i}$ 衰减负斜率位置，确保仅对持久支持信号进行强化。

## 实验评估

实验在 ALFWorld 与 WebShop 上进行，使用 Qwen2.5-3B-Instruct 与 Qwen3-1.7B-Instruct 骨干。基线覆盖 GRPO、OPSD、RLSD、SDAR 等主流蒸馏与 RL 方法，但缺失 Tree-GRPO 等树搜索类信用分配基线。

| 方法 | ALFWorld Overall (%) | WebShop Score |
| :--- | :--- | :--- |
| GRPO | 75.0 | 79.8 |
| SDAR | 84.4 | 83.4 |
| PCSD | 90.6 | 85.0 |

PCSD 在 ALFWorld 上以 90.6% 超越 GRPO 15.6 点，较最强基线 SDAR 提升 6.2 点，验证了持久一致性权重在细粒度信用分配上的有效性。

| 变体 | ALFWorld Overall (%) |
| :--- | :--- |
| Fixed N=1 | 82.8 |
| w/o trend | 83.6 |
| w/o decay | 85.1 |
| PCSD | 90.6 |

消融显示，移除趋势调制导致性能下降 7.0 点，表明抑制局部支持度下降对防止噪声干扰至关重要。固定窗口 N=1 性能最低，证实自适应聚合在平衡精度与鲁棒性上的必要性。

评估边界方面，论文未报告置信区间，且仅在 128 个 WebShop 验证实例上测试，样本量较小。代码未开源，超参数 $\lambda_{PCSD}=0.01$ 与 $\beta_{gate}=5.0$ 固定，未探索随训练动态调整的可能性。

## 关联研究分析

从问题动机看，PCSD 与 SDAR 均针对教师信号局部不可靠问题，但 SDAR 依赖单点 Token 差异，对采样噪声敏感；PCSD 通过局部持久性评估，将噪声敏感的单点估计转化为鲁棒的连续权重。这一差异源于对“可信度”定义的不同：SDAR 视单点差异为信号，PCSD 视局部一致性为信号。在噪声较高的长程任务中，PCSD 的鲁棒性优势更为显著，但其在低噪声短程任务上的边际收益是否递减，论文未给出回答。

从方法设计看，PCSD 与 RLSD 同属 GRPO+蒸馏混合框架，但 RLSD 采用均匀或简单加权，PCSD 引入自适应窗口与趋势调制。PCSD 在 ALFWorld 上以 90.6% 优于 RLSD 的 79.7%，表明精细的 Token 级权重分配比粗粒度混合策略更有效。然而，PCSD 的固定超参数设定与 RLSD 的简单加权相比，增加了调参复杂度，且在教师信号高度稳定的场景下，其自适应机制可能引入不必要的计算开销。

## 总结

PCSD 旨在解决 Agentic RL 中稀疏奖励导致的信用分配难题，抓住教师信号局部持久性这一被忽略的特征，通过自适应聚合与趋势调制生成 Token 级蒸馏权重。实验证明其在 ALFWorld 上超越 GRPO 15.6 点，较 SDAR 提升 6.2 点，验证了持久一致性评估的有效性。然而，论文采用固定超参数与冻结教师，未探索权重机制随策略演化的动态调整，也未在分布外任务上充分验证泛化能力。当训练轨迹统计特性发生显著漂移时，固定阈值的自适应聚合是否仍能准确区分信号与噪声，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.01837)