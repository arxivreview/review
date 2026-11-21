# HuggingFace最新推荐论文 ｜CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing ｜结构质量驱动稀疏预填充

研究机构：美国俄勒冈大学、Adobe研究院

作者：Huu Huy Nguyen、Chien Van Nguyen、Franck Dernoncourt 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.01925)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.01925)

> 长上下文大语言模型推理的预填充阶段受限于自注意力的二次方计算复杂度，传统固定稀疏模式无法适应输入依赖的注意力结构。现有动态路由方法依赖间接信号且累积阈值在长序列下失效，本文切入点在于利用注意力质量分布的结构特性替代冗余计算。CRISP 通过结构质量代理实现零开销路由，并引入噪声地板阈值规避质量悬崖。该方法在检索任务上达到全注意力精度上限，但其对聚合任务的轻微性能损失揭示了保守阈值在特定分布下的适用边界。

## 研究背景

长上下文推理中，自注意力机制需计算所有 Token 对之间的交互，导致计算量随序列长度 $N$ 呈 $O(N^2)$ 增长。为缓解此瓶颈，稀疏注意力通过限制交互范围降低复杂度，但固定模式在推理时往往破坏训练时学习的全局依赖。动态稀疏方法试图实时调整选择策略，但其路由信号的计算开销与索引选择的累积误差成为新的瓶颈。

动态稀疏路由的核心挑战在于如何以低成本识别注意力分布的集中程度，并据此分配计算预算。FlexPrefill 等前沿方法使用 Jensen-Shannon Divergence (JSD) 作为路由信号，但这需要额外的矩阵乘法与 Softmax 计算。更关键的是，其索引选择采用累积覆盖率阈值 $\gamma$，该机制假设所有注意力质量语义等价，忽视了 Softmax 归一化后形成的“质量悬崖”——即架构 Sink、任务信号与背景噪声之间的尖锐边界。当 Sink 质量占比过高时，累积阈值会在到达信号块前终止；当 Sink 质量分散时，阈值会跨越悬崖累积大量噪声 Token。这种结构性失效在长序列下尤为严重，导致精度损失与延迟增加。

CRISP 针对上述两个结构性缺陷提出解决方案。它不再依赖间接的 JSD 信号，而是直接测量注意力质量在结构可预测位置（Sink 与局部窗口）的分布，以此作为路由依据。同时，它摒弃累积阈值，引入基于噪声地板的 Sink 感知阈值，显式区分信号与背景噪声。这一设计旨在消除路由计算冗余，并从理论上避免 $O(N)$ 的噪声累积，从而在保持稀疏性的同时恢复检索任务的精度上限。

## 核心方法

### 动态稀疏路由参照系

动态稀疏预填充的标准流程包含两个阶段：路由决策与索引选择。路由阶段需判断每个注意力头是集中型（Vertical-Slash, VS）还是分散型（Pooled-Estimation, PE），以决定采用细粒度方向选择还是全局池化估计。索引选择阶段则根据路由结果，从代理注意力图中选取重要 Token 块。FlexPrefill 作为基线，使用 JSD 衡量池化估计与逐查询平均的偏差进行路由，并采用累积覆盖率 $\gamma$ 确定选择数量。CRISP 的关键差异在于替换了这两个环节的核心度量：路由信号从统计偏差转为结构质量，索引阈值从累积覆盖转为噪声地板。

### 结构质量代理路由

FlexPrefill 使用 JSD 路由需计算池化估计 $\bar{a}$ 与逐查询平均 $\hat{a}$ 的散度，涉及额外的 $O(nd/b)$ 矩阵乘法与 Softmax。CRISP 指出，在具有 Sink 特性的架构中，集中型头部的质量天然聚集于结构可预测位置。因此，CRISP 引入结构质量代理 $C_{struct}$，直接测量代理注意力图 $\hat{A}$ 在锚点位置的质量总和：

$$ C_{struct} = \frac{1}{|\hat{Q}|} \sum_{i \in \hat{Q}} \sum_{j \in S_{anchor}} \hat{A}[i, j] $$

其中 $S_{anchor}$ 包含架构 Sink（前 $w_{sink}$ 个 Token）与局部近期窗口（后 $w_{local}$ 个 Token）。该公式的物理含义是：若头部质量高度集中于这些结构位置，则 $C_{struct}$ 值高，路由至 VS 路径；否则路由至 PE 路径。这一设计消除了 JSD 所需的额外矩阵乘法，因为 $\hat{A}$ 已在索引选择阶段计算，$C_{struct}$ 仅需对已存在矩阵的固定切片进行归约，时间复杂度为 $O(w_{sink} + w_{local})$，与序列总长 $N$ 无关。实验表明，该代理在 Llama 和 Qwen 模型上分别以 94.0% 和 88.1% 的准确率复现了 JSD 的路由决策，验证了结构质量与注意力集中度的强相关性。

### 噪声地板索引选择

VS 路径的索引选择面临质量悬崖问题。累积阈值 $\gamma$ 在 Sink 质量 $a_{sink} \ge \gamma$ 时导致“Sink 独占崩溃”，在 $a_{sink} + a_{important} < \gamma$ 时导致“噪声累积”。CRISP 提出基于噪声地板的阈值机制，首先计算非保留块（排除首尾块）的背景质量均值 $\mu$：

$$ \mu = \frac{\max(1 - a_{first} - a_{last}, 0)}{N_b - 2} $$

其中 $N_b$ 为总块数。随后，块 $j$ 被选中的条件是其质量 $p_j$ 超过噪声地板 $\alpha \cdot \mu$：

$$ \text{block } j \text{ is important} \iff p_j > \alpha \cdot \mu $$

该公式的物理含义是：只有显著高于背景噪声水平的块才被视为包含任务信号。$\alpha=1.0$ 作为无校准默认值，意味着任何高于平均背景质量的块均被保留。与累积阈值不同，该机制不依赖预设覆盖率，而是根据实际质量分布动态确定选择数量。当 Sink 质量增加时，$\mu$ 自动降低，保持对信号的敏感性；当质量分散时，阈值有效过滤背景噪声。这一设计从理论上避免了 $O(N)$ 的噪声 Token 累积，解决了累积阈值在长序列下的结构性失效。

## 实验评估

实验在 Meta-Llama-3.1-8B-Instruct 和 Qwen2.5-7B-Instruct 上进行，基准包括 InfiniteBench (131K)、RULER (4K–131K) 和 LongBench (4K–16K)。基线覆盖 FlashAttention (FA)、MInference (离线稀疏) 和 FlexPrefill (动态稀疏)。CRISP 在检索密集型任务上表现突出，InfiniteBench 上 Llama 得分 48.7，Qwen 得分 28.7，均持平或超越 FA (48.6/24.0)，显著优于 FlexPrefill (47.4/25.5)。RULER 上 CRISP $\alpha=1.0$ 在 Llama 上得分 47.77，优于 FlexPrefill 的 46.92。

| 基准 | 方法 | Llama-3.1-8B | Qwen2.5-7B |
| :--- | :--- | :--- | :--- |
| InfiniteBench | FlashAttn (FA) | 48.6 | 24.0 |
| | MInference | 36.5 | 25.1 |
| | FP $\gamma=0.95$ | 47.4 | 25.5 |
| | CRISP $\alpha=1.0$ | 48.7 | 28.7 |
| RULER | FlashAttn (FA) | 48.82 | 48.80 |
| | FP $\gamma=0.95$ | 46.92 | 45.57 |
| | CRISP $\alpha=1.0$ | 47.77 | 47.23 |

消融实验显示，$\alpha$ 值对精度-延迟权衡有显著影响。$\alpha=1.5$ (速度优先) 在 512k 上下文下比 FlexPrefill 快 18%，但精度略降；$\alpha=1.0$ (精度优先) 在 512k 下实现 5.17× 加速，且精度持平 FA。值得注意的是，FlexPrefill 将 $\gamma$ 从 0.95 提升至 0.97 时，Llama RULER 得分从 46.92 微升至 47.12，但延迟显著增加，且 InfiniteBench 得分下降至 47.3，证实了累积阈值无法通过参数调优克服质量悬崖。CRISP 在检索任务上相比 FlexPrefill 恢复了最高 +28.0pp 的精度，主要源于消除了 Sink 独占崩溃导致的信号缺失。

评估边界方面，论文未报告置信区间，数值比较需谨慎。实验仅覆盖 Llama 和 Qwen 两个模型家族，未测试 Mamba 等线性注意力架构作为基线。代码未公开，但提供了详细的算法伪代码与超参数设置（$\tau_{proxy}=0.2, \gamma=0.95, B=128$）。延迟测量仅在单张 H100 上进行，未考虑多卡并行或不同硬件配置的影响。

## 关联研究分析

从问题动机看，CRISP 与 FlexPrefill 均致力于解决动态稀疏路由的计算开销与精度损失，但二者对“注意力质量分布”的理解存在根本差异。FlexPrefill 假设质量分布是平滑的，可通过累积覆盖率近似；CRISP 则揭示质量分布存在尖锐的“质量悬崖”，即 Sink、信号与噪声之间存在不可逾越的边界。这一差异源于 CRISP 对 Softmax 归一化后 Token 层级结构的显式建模，而 FlexPrefill 将其视为均质背景。CRISP 的噪声地板阈值直接针对这一悬崖设计，而 FlexPrefill 的累积阈值在悬崖处失效。这种设计选择反映了从“统计近似”到“结构感知”的范式转变，但 CRISP 对 Sink 特性的依赖也限制了其在非 Sink 架构上的泛化能力。

从方法设计看，CRISP 与 StreamingLLM 在利用 Attention Sink 方面形成互补。StreamingLLM 利用 Sink 的稳定性优化 KV 缓存，保留初始 Token 以实现无限长序列生成；CRISP 则利用 Sink 的质量集中特性优化索引选择，通过 $C_{struct}$ 识别集中型头部。两者均将 Sink 从“病理现象”转化为“可利用特性”，但作用阶段不同：StreamingLLM 作用于缓存管理，CRISP 作用于预填充计算。CRISP 的 $C_{struct}$ 代理实际上是对 Sink 位置质量的直接测量，这与 StreamingLLM 中 Sink 作为“注意力汇聚点”的解释一致。然而，CRISP 未探讨解码阶段的 Sink 利用，其方法仅针对预填充阶段，这与 StreamingLLM 的全流程优化形成对比。

## 总结

CRISP 旨在解决动态稀疏预填充中路由信号冗余与累积阈值失效的矛盾。其切入点在于利用注意力质量在结构位置（Sink 与局部窗口）的集中特性，替代间接的 JSD 路由，并引入噪声地板阈值规避质量悬崖。方法上，CRISP 通过 $C_{struct}$ 实现零开销路由，并通过 $\alpha \cdot \mu$ 阈值显式区分信号与噪声。实验证明，CRISP 在 InfiniteBench 上达到 48.7 (Llama) 和 28.7 (Qwen)，持平全注意力，且在 512k 上下文下实现 5.17× 加速。然而，CRISP 在 RULER 聚合任务上相比 FlexPrefill 有 -0.40pp 的轻微下降，表明保守阈值在需要广泛覆盖中质量块的任务中可能欠选择。当 Sink 质量分布极度分散或任务依赖中质量块时，噪声地板阈值是否仍能保持精度-延迟的最优平衡，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.01925)