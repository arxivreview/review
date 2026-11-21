# HuggingFace最新推荐论文 ｜Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models ｜扩散语言模型跨架构蒸馏

研究机构：北京大学、浙江大学

作者：Gongbo Zhang、Wen Wang、Ye Tian 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.26951)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.26951)

> 扩散语言模型（Diffusion Large Language Models, dLLMs）虽具备并行解码优势，但高性能模型参数量巨大，部署成本高昂。现有蒸馏方法仅关注单一架构内的步数压缩，无法解决教师与学生模型在架构、注意力机制及分词器上的异构性难题。本文提出 TIDE 框架，通过双轴调度、互补演示与反向块级似然匹配，首次实现异构 dLLM 间的知识迁移。该框架在代码生成任务上显著超越同规模自回归模型，但其对连续状态扩散模型的适用性及教师匹配度机制尚存疑。

## 研究背景

dLLM 通过迭代去噪完全掩码序列实现并行解码，其训练过程涉及随机采样的扩散时间步 $t$。在 $t \approx 1$ 的高噪声阶段，教师模型因上下文缺失而预测可靠性急剧下降，导致蒸馏信号质量随时间步剧烈波动。同时，不同模型家族的分词器词表差异使得标准 Token 级 KL 散度在数学上不可用，传统自回归（AR）蒸馏中的曝光偏差理论在此场景下需重新定义，因为 dLLM 的误差累积源于空间表示的稀疏而非序列生成的自回归依赖。

主流 AR 蒸馏方法如 MiniLLM 和 GKD 已解决散度选择与在线策略问题，但 dLLM 蒸馏此前局限于 CDLM 等步压缩技术，未触及跨架构迁移。这一空白源于 dLLM 特有的时序动态不一致性：教师信号可靠性随掩码率变化，且高噪声下上下文稀缺导致空间表示迁移失效。本文切入点在于将蒸馏问题解耦为时序调度、上下文增强与词表对齐三个正交维度，针对 dLLM 的掩码机制设计专用组件，而非直接迁移 AR 蒸馏的散度框架。

## 核心方法

### 方法参照系

标准跨架构蒸馏流程假设教师与学生共享词表，通过 Token 级 Logits 对齐实现知识迁移。本文问题的关键差异在于教师（LLaDA2.0-mini, MoE）与学生（Qwen3-0.6B-BD3LM, Dense）词表不匹配，且教师信号可靠性随扩散时间步 $t$ 动态变化，导致静态 Logits 对齐失效。

### 双轴 Lambda 调制（TIDAL）

针对教师信号可靠性随时间步波动的问题，TIDAL 在训练进度与扩散时间步两个轴上动态调整蒸馏强度。设计动机是避免学生在高噪声阶段拟合教师不可靠的猜测。插值目标 $r_t$ 由教师 Logits $t$ 与学生 Logits $s$ 加权合成：

$$ r_t = \lambda_t \cdot \text{softmax}(t/T) + (1-\lambda_t) \cdot \text{softmax}(s/T) $$

其中 $\lambda_t = \lambda_{\text{train}} \times (1-t)$，$\lambda_{\text{train}}$ 随训练进度呈余弦上升。该公式确保 $t \approx 1$ 时 $\lambda_t \approx 0$，目标由学生主导，防止噪声信号污染；$t \approx 0$ 时 $\lambda_t$ 接近最大值，学生充分学习教师的高置信度预测。

### 互补演示与反向 CALM

COMPDEMO 通过随机分割掩码集 $M$ 为 $M_A, M_B$，执行两次教师前向传播以增强上下文。Pass 1 揭示 $M_A$ 预测 $M_B$，Pass 2 对称操作，合并 Logits 后提供比单次前向更丰富的空间表示。针对跨分词器对齐，Reverse CALM 将 Token 级对齐转化为块级（Chunk）似然匹配。设计动机是前向 BCE 梯度在 $p_s[c] \to 0$ 时发散，而反向形式梯度系数 $\log \frac{1}{1-p_t[c]}$ 仅依赖固定教师，有界且具备双端噪声过滤能力。损失函数定义为：

$$ L_{\text{Rev-CALM}} = \sum_{c \in \mathcal{C}} \left[ p_t[c] \log \frac{p_t[c]}{p_s[c]} + (1-p_t[c]) \log \frac{1-p_t[c]}{1-p_s[c]} \right] $$

该公式等价于 Bernoulli KL 散度，在标量空间实现模式寻求，避免直接 Token 映射的不稳定性。

## 实验评估

实验在 GSM8K、HumanEval 等 8 个基准上评估，基线包括 AR 模型 Qwen3-0.6B-Base 与非蒸馏 BD3LM。主结果显示，TIDE-Cross（跨分词器）平均得分 34.20，较非蒸馏基线 32.67 提升 1.53 分；TIDE-Shared（共享分词器）平均得分 33.55。在 HumanEval 上，TIDE-Shared 得分 48.78，显著高于 AR 基线的 32.30，表明 dLLM 并行解码特性在代码生成中更具优势。

| Benchmark | AR Baseline | BD3LM No Distill | TIDE-Shared | TIDE-Cross |
| :--- | :--- | :--- | :--- | :--- |
| GSM8K | 59.60 | 48.07 | 48.90 | 52.24 |
| HumanEval | 32.30 | 45.73 | 48.78 | 48.17 |
| MBPP | 36.60 | 38.60 | 37.80 | 38.60 |
| Avg | 40.91 | 32.67 | 33.55 | 34.20 |

消融实验表明，移除时间步轴导致 HumanEval 下降 3.05 分，验证了 TIDAL 对时序动态的关键作用；移除 COMPDEMO 对 GSM8K 影响较小（48.90 vs 48.90），但在 MATH 上略有波动。TIDE-Shared 在共享分词器管道中优于 TIDE-Cross 2.76 分，而 TIDE-Cross 在跨分词器管道中优于 TIDE-Shared 0.37 分，证实不同管道偏好不同策略。

评估边界方面，论文未报告置信区间，且缺乏与 LSD 等其他 dLLM 蒸馏方法的直接对比。代码与模型已开源，但 0.6B 学生模型的容量限制可能掩盖了框架在更大规模下的性能潜力。

## 关联研究分析

从问题动机看，TIDE 与 SRA 均解决跨分词器对齐，但 SRA 基于 Span 表示的质心对齐，适用于 AR 模型；TIDE 则针对 dLLM 的掩码机制，通过块级似然匹配处理时间步依赖的噪声。差异根源在于 dLLM 的并行解码特性使得 Token 级对齐在低噪声下仍受上下文缺失影响，而 AR 模型的自回归特性允许更稳定的局部对齐。TIDE 的 Reverse CALM 借鉴了 MiniLLM 的 RKL 思想，但将其从 Token 级 KL 扩展至块级 Bernoulli KL，以适配 dLLM 的离散扩散过程。

从方法设计看，TIDAL 与 TAID 均使用插值调度，但 TAID 仅沿训练进度单轴调制，忽略教师信号的时间步依赖性。TIDE 引入扩散时间步轴，是因为 dLLM 中教师可靠性随 $t$ 剧烈变化，而 AR 模型中教师始终拥有完整左上下文，信号可靠性恒定。这一差异源于 dLLM 的掩码去噪机制，而非模型架构本身。TIDE 未探索教师匹配度对蒸馏效果的影响，仅验证了异构可行性，这与领域共识中“教师-学生匹配度比绝对性能更重要”的观点存在潜在冲突。

## 总结

TIDE 解决了 dLLM 跨架构蒸馏中时序动态不一致、上下文稀缺与词表不匹配三大矛盾，通过双轴调度、互补演示与反向块级似然匹配实现知识迁移。实验证明其在代码生成上超越同规模 AR 模型 16.48 分，但仅验证了 0.6B 学生模型的性能，未探讨框架在更大规模或连续状态扩散模型中的泛化能力。当学生模型容量扩展至 8B 时，TIDAL 的时间步权重是否仍需动态调整，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.26951)