# ACL-Findings2026最新论文 ｜Low-probability Tokens Sustain Exploration in Reinforcement Learning with Verifiable Reward ｜低概率Token正则化

研究机构：清华大学、北京大学

作者：Guanhua Huang、Tingqiang Xu、Mingze Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03222)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03222)

> 导读 强化学习可验证奖励（RLVR）旨在通过客观二元奖励提升大语言模型的长思维链推理能力，但训练常因策略熵坍缩导致性能平台期。现有熵控制方法试图通过全局随机性维持探索，却往往放大无关噪声并加速崩溃。本文识别出低概率探索性Token（Reasoning Sparks）被系统性消除是核心瓶颈，提出低概率正则化（Lp-Reg）通过构建过滤噪声的代理分布进行KL散度约束，精准保护关键Token。该方法在Qwen3-14B上实现了60.17%的平均准确率，但其在非数学任务及弱骨干模型上的泛化能力尚存疑。

## 研究背景

RLVR训练依赖组相对策略优化（GRPO）估计优势函数，其核心假设是组内奖励方差能提供有效梯度信号。当模型在长思维链中生成低概率Token时，若这些Token被过度惩罚，策略分布将迅速锐化。这种锐化不仅导致熵下降，更直接切断了模型探索新推理路径的能力，表现为Pass@k指标停滞。

RLVR领域长期将策略熵视为探索能力的代理指标，主流方法如DAPO、80/20及KL-Cov均通过调整裁剪范围或限制高熵Token更新来延缓熵坍缩。然而，这些方法混淆了“随机性”与“有效性”，盲目提升全局熵会同时放大语义无关的低概率噪声Token（如“cost”、“fine”），导致训练不稳定甚至性能加速崩溃。本文切入点在于区分低概率Token中的“信号”与“噪声”，指出熵下降是结果而非原因，真正的瓶颈在于有价值探索路径的微观消除。

## 核心方法

### 方法参照系

本文基于GRPO框架，针对其裁剪机制中低概率探索动作被过度限制的问题进行改进。与直接修改熵正则化系数或裁剪边界不同，Lp-Reg引入外部代理分布作为软约束，将探索保护从全局统计量下沉至Token级概率分布。

### 代理分布构建

传统方法直接对策略分布施加熵惩罚，无法区分Token语义价值。Lp-Reg首先利用模型自身预测分布构建代理分布 $\pi_{\text{proxy}}$，通过Min-p阈值 $\tau = \kappa \cdot \max_{o' \in V} \pi_\theta(o'| \cdot)$ 过滤掉概率低于阈值的噪声Token，并将剩余概率质量重新归一化：

$$ \pi_{\text{proxy}}(o| \cdot) = \begin{cases} \frac{\pi_\theta(o| \cdot)}{\sum_{o' \in V, \pi_\theta(o'| \cdot) > \tau} \pi_\theta(o'| \cdot)} & \text{if } \pi_\theta(o| \cdot) > \tau \\ 0 & \text{otherwise} \end{cases} $$

该设计动机在于利用低概率区间内“有意义Token平均概率高于噪声”的统计特性，通过过滤噪声提升代理分布的信噪比，为后续正则化提供纯净参考。

### 选择性KL正则化

在GRPO目标函数中，Lp-Reg增加了一项仅在特定条件下激活的正则化项。该惩罚项仅作用于满足三个条件的Token：采样概率低于批次内最低 $\rho$ 分位数、在代理分布中概率非零、且接收负优势信号。最终目标函数为：

$$ \mathcal{L} = \mathbb{E} \left[ \min \left( r_t A_t, \text{clip}(r_t, 1-\epsilon, U) A_t \right) - \beta D_{KL}(\pi_{\text{ref}} \| \pi_\theta) - \lambda \mathbb{I}[\pi_\theta < \delta_\rho, \pi_{\text{proxy}} > 0, A_t < 0] D_{KL}(\pi_{\text{proxy}} \| \pi_\theta) \right] $$

使用前向KL散度 $D_{KL}(\pi_{\text{proxy}} \| \pi_\theta)$ 而非反向KL，旨在当策略概率趋近于零时施加显著惩罚，从而阻止Reasoning Sparks被彻底消除，同时避免强制策略严格模仿代理分布。仅对负样本正则化是因为关键探索Token在失败轨迹中更频繁出现，保护它们能更有效地恢复探索能力，而对正样本正则化仅引入轻微噪声并减缓训练进度。

## 实验评估

实验在Qwen3-14B-Base和Qwen2.5-32B-Base上进行，覆盖AIME24/25、MATH-500、Minerva及OlympiadBench五个基准。基线包括GRPO、Clip-Higher、80/20、KL-Cov及GSPO，但未对比Risk-Sensitive RL或VERL等2026年前沿探索方法。

| 方法 | AIME24 | AIME25 | Math-500 | Minerva | Olympiad | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GRPO (on.) | 46.04 | 34.38 | 93.00 | 48.53 | 65.19 | 57.43 |
| 80/20 (on.) | 47.29 | 32.50 | 91.60 | 50.37 | 65.78 | 57.51 |
| Lp-Reg (on.) | 50.83 | 37.92 | 94.40 | 49.26 | 68.44 | 60.17 |

Lp-Reg在Qwen3-14B上以60.17%的平均准确率领先，较次优方法80/20提升2.66%。消融实验显示，移除噪声过滤阈值导致性能崩溃，验证了过滤机制对稳定训练的关键作用；仅对负样本正则化的性能优于对正负样本同时正则化，证实了负样本中关键Token的稀缺性与重要性。

评估边界方面，实验仅覆盖数学推理任务，未涉及代码或开放域生成，限制了结论的泛化性。代码已开源，但超参数 $\kappa$ 和 $\rho$ 的敏感性分析未详细展开，且81,204 GPU-hours的计算成本较高，复现门槛较大。

## 关联研究分析

从问题动机看，Lp-Reg与80/20（Wang et al., 2025）均关注Token级选择，但80/20限制更新至高熵Token以维持随机性，而Lp-Reg保护低概率Token以维持探索路径。差异根源在于对“探索”的定义：80/20假设高熵Token承载探索信息，Lp-Reg则证明低概率但语义相关的Token才是关键。80/20在Qwen3-14B上平均准确率57.51%，低于Lp-Reg的60.17%，表明在高基线模型上，盲目维持高熵不如精准保护低概率信号有效。

从方法设计看，Lp-Reg与VERL（2026）均试图超越全局熵指标，但VERL利用隐藏状态矩阵的有效秩量化探索，Lp-Reg利用Token概率分布。VERL关注语义空间动态，Lp-Reg关注预测分布尾部。Lp-Reg未引用VERL，可能因VERL依赖隐藏状态计算，而Lp-Reg仅依赖前向传播概率，计算开销更低。然而，Lp-Reg在长序列任务中是否因序列长度增加导致Min-p阈值失效，论文未给出回答。

## 总结

本文核心矛盾在于RLVR训练中探索能力丧失与噪声放大的权衡。现有熵控制方法因混淆随机性与有效性而失效，Lp-Reg凭借低概率区间内信号与噪声的概率差异，通过代理分布KL正则化实现精准保护。实验证明其在Qwen3-14B上实现60.17%平均准确率，较基线提升2.66%。边界在于仅验证数学任务，且依赖强骨干模型的高基线能力。当骨干模型预训练能力较弱时，低概率Token中噪声占比可能更高，Lp-Reg的过滤机制是否仍能有效区分信号与噪声，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03222)