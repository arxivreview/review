# ACL-Findings2026最新论文 ｜Multi-Drafter Speculative Decoding with Alignment Feedback ｜多草稿器投机解码与对齐反馈

作者：Taehyeon Kim、Hojung Jung、Se-Young Yun

论文原文见 [arXiv](https://arxiv.org/abs/2604.05417)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e5336fb8d57e)

> 投机解码（Speculative Decoding, SD）旨在通过草稿-验证机制无损加速大语言模型（LLM）推理，但单一草稿器在动态多任务场景下泛化能力受限。现有静态路由或独立草稿器方案无法实时适应输入分布变化，导致接受率波动。METASD 将草稿器选择建模为多臂老虎机（Multi-Armed Bandit, MAB）问题，利用块散度（Block Divergence, BD）奖励实现在线动态路由。该框架在混合任务负载下显著优于静态基线，但其理论假设的平稳性在极端非平稳场景下的鲁棒性尚存疑。

## 研究背景

LLM 自回归解码受内存带宽限制，SD 通过引入轻量级草稿器并行预测候选 Token，再由目标模型单次并行验证，将串行瓶颈转化为并行计算。草稿器与目标模型的分布对齐度直接决定接受率，进而决定加速比上限。然而，单一草稿器通常针对特定领域（如代码或数学）训练，其内在偏置导致在分布外（Out-of-Distribution, OOD）输入上表现急剧下降。

早期 SD 研究聚焦于独立草稿器与目标模型的分布对齐，或采用树状验证提升硬件利用率。随着 LLM 路由（LLM Routing）趋势兴起，部署异构专家模型成为常态，但静态路由依赖输入级嵌入进行一次性分配，无法捕捉解码过程中的实时对齐动态。METASD 的切入点在于利用验证阶段产生的对齐反馈作为奖励信号，将草稿器选择转化为在线决策问题，从而在无需预训练路由器的情况下，动态适应不断变化的任务分布。

## 核心方法

### 方法参照系

标准 SD 流程中，草稿器固定不变，验证阶段仅执行拒绝采样。METASD 的关键差异在于引入“元草稿”（Meta-drafting）层：在每次 SD 周期开始前，从异构草稿器池中动态选择最优草稿器。这一选择过程不依赖静态分类器，而是基于历史对齐反馈的在线学习，解决了单一草稿器在动态负载下泛化失效的问题。

### 块散度奖励机制

传统方法常使用块效率（Block Efficiency, BE，即接受 Token 数与最大草稿长度之比）作为反馈信号，但 BE 方差大且信息量有限。METASD 提出块散度（BD）奖励，直接度量草稿器与目标模型概率分布的总变差距离（Total Variation Distance, TV Distance）。BD 奖励定义为草稿序列中每个位置对齐度的平均值：

$$
r_{BD}^{i,t} = \frac{1}{N_{max}} \sum_{j=0}^{N_{max}-1} \left( 1 - d_{TV}(p_{l(t)+j}, q_{l(t)+j}^{i}) \right)
$$

其中 $d_{TV}$ 为总变差距离。该设计动机在于 BD 提供了比 BE 更强的统计信号，理论上能更快速收敛至最优草稿器，减少探索次数的浪费。

### 停止时间遗憾与 UCB 策略

由于 SD 的总轮次 $T$ 是随机的（取决于接受率），标准 MAB 的固定轮次遗憾界不适用。METASD 定义停止时间遗憾（Stopping Time Regret）：

$$
REG(\pi, B) = E[\tau(\pi, B)] - E[\tau(\pi^{\star}, B)]
$$

其中 $\tau(\pi, B)$ 为生成 $B$ 个 Token 所需的总轮次。最小化该遗憾等价于最大化期望接受 Token 数。算法采用上置信界（Upper Confidence Bound, UCB）策略，在每轮选择草稿器时平衡利用（历史高奖励）与探索（不确定性高）：

$$
a_t \leftarrow \arg \max_{i \in [K]} \left( \hat{\mu}_{i,t} + \beta \sqrt{\frac{2 \ln t}{n_i}} \right)
$$

该策略无需预训练，通过在线更新均值估计 $\hat{\mu}_{i,t}$ 和计数 $n_i$，实现了对动态任务分布的自适应路由。

## 实验评估

实验基于 Vicuna 7B 目标模型，涵盖代码（MT-Bench）、摘要（CNN/Daily）、翻译（WMT16）、问答（Natural Questions）和数学（GSM8K）五类任务，以及多语翻译场景。基线包括单一专用草稿器、OFA（One-For-All）、PLD、Lookahead、Medusa 及静态 BERT 路由。METASD 在混合任务负载下表现显著优于静态方法。

| 任务 | MetaSpS-UCB (Black-box) | MetaEagle-UCB (White-box) | 最佳专用草稿器 (White-box) |
| :--- | :--- | :--- | :--- |
| Code | 2.300 | 3.724 | 3.934 |
| Trans | 1.587 | 2.318 | 2.496 |
| Sum | 1.971 | 3.057 | 3.382 |
| QA | 1.711 | 2.641 | 2.916 |
| Math | 2.280 | 3.520 | 3.903 |

在 White-box 设置下，MetaEagle-UCB 在 Code 任务达到 3.724x 加速比，虽略低于最佳专用草稿器（3.934x），但在混合负载下优势明显。消融实验显示，BD 奖励在 Code 任务上比 BE 奖励提升加速比约 0.4x（3.661 vs 3.228），验证了 BD 信号的有效性。然而，在 White-box 设置中，BD 与 BE 的性能差距缩小，归因于 EAGLE 的树注意力机制已部分缓解了 BE 的局限性。

评估边界方面，论文未提供代码开源链接，且实验仅使用贪心解码，未涵盖温度采样场景。此外，论文未与 EAGLE-2 或 HASS 等最新特征对齐 SOTA 在相同多任务混合负载下进行直接对比，限制了其在当前 SOTA 坐标系中的精确定位。

## 关联研究分析

从问题动机看，METASD 与 LLM Routing（Hu et al., 2024）共享“动态分配计算资源”的目标，但根源差异显著。LLM Routing 依赖输入级嵌入进行静态分类，假设任务类型在输入时即可确定；而 METASD 利用解码过程中的实时对齐反馈，捕捉了任务分布的动态变化。这种差异源于 SD 的验证机制天然提供了对齐信号，而通用 LLM 路由缺乏此类细粒度反馈。METASD 的在线学习机制因此更适合处理 OOD 输入和动态用户查询，这是静态路由无法解决的盲区。

从方法设计看，METASD 与 BanditSpec（Hou et al., 2025）同属 MAB 框架，但理论贡献不同。BanditSpec 聚焦于控制 UCB 的置信范围以估计接受 Token 数均值，而 METASD 揭示了奖励设计的重要性，证明 BD 奖励在理论和实证上均优于 BE。这一差异暗示了 MAB 在 SD 中的应用中，奖励函数的信息量比算法本身的复杂度更关键。METASD 的停止时间遗憾界也更为通用，适用于更广泛的奖励整形场景，而 BanditSpec 的分析局限于特定均值估计。

## 总结

METASD 解决了单一草稿器在动态多任务场景下泛化能力不足的核心矛盾。其切入点在于利用 SD 验证阶段天然产生的对齐反馈，将草稿器选择转化为在线 MAB 问题，避免了静态路由对输入分布的强假设。通过引入 BD 奖励和停止时间遗憾界，METASD 在混合任务负载下实现了比静态方法更稳定的加速比，White-box 设置下 Code 任务加速比达 3.724x。然而，论文实验仅覆盖贪心解码，且未与最新特征对齐 SOTA 在相同动态负载下对比，其理论假设的平稳性在极端非平稳场景下的鲁棒性尚待验证。当任务分布发生剧烈突变时，UCB 的探索-利用平衡是否仍能维持低遗憾，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e5336fb8d57e)