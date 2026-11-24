# ACL-Findings2026最新论文 ｜D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation ｜大规模SFT模型增量参数压缩

研究机构：哈尔滨工业大学、香港理工大学

作者：Junlin Li、Shuangyong Song、Guodong Du 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16940)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16940)

> 多模型部署场景下，存储全量微调模型导致内存开销呈线性增长，增量压缩旨在仅存储基座模型与压缩后的差值（Delta）以解决此问题。现有方法在处理大规模数据微调产生的高幅度Delta参数时，因量化误差与低秩近似误差随数值尺度放大而失效。本文提出D-QRELO，通过先进行1-bit量化缩小残差数值范围，再对残差执行SVD低秩近似，实现训练与数据无关的压缩。该方法在强SFT模型上显著优于基线，但其压缩率存在物理下限，且对早期层敏感性的处理尚未完全解决。

## 研究背景

多模型协同部署面临存储瓶颈，直接存储 $K$ 个全精度微调模型需 $K \times M$ 内存。增量压缩利用微调模型与预训练基座模型权重的差异（Delta参数）进行压缩，将存储降至 $(1 + \rho K) \times M$，其中 $\rho$ 为压缩比。Delta参数的统计特性直接决定压缩难度：若Delta幅度小且低秩，传统方法有效；若幅度大且复杂度高，误差累积将导致性能崩塌。

现有Delta压缩方法主要分为剪枝、量化与低秩近似三类。BitDelta（Liu et al., 2024a）采用1-bit量化，Delta-CoMe（Ping et al., 2024）采用混合精度SVD。这些方法在早期小规模SFT数据上表现良好，但假设Delta参数幅度较小（通常 $< 0.0008$）。随着SFT数据规模扩大至百万级，Delta参数的平均绝对值增至0.002-0.004，奇异值与熵同步上升。这种数值尺度的扩张打破了原有方法的误差假设，导致量化绝对误差与SVD重构误差成比例放大，现有方法在Qwen3、DeepSeek-R1等强SFT模型上性能显著退化。

本文切入点在于揭示SFT数据规模与Delta参数复杂度之间的正相关关系，并针对高幅度Delta参数设计鲁棒压缩策略。通过实证分析发现，单纯量化或SVD均无法有效抑制高幅度下的绝对误差累积。D-QRELO提出两阶段残差校准框架，利用量化快速降低数值尺度，再利用SVD恢复细粒度结构，从而在无需训练与校准数据的前提下，突破现有方法在大SFT场景下的性能瓶颈。

## 核心方法

### 增量压缩参照系

增量压缩的标准流程是将Delta参数 $\Delta$ 映射为压缩表示 $\hat{\Delta}$，满足目标压缩比 $\rho$。主流方法直接对 $\Delta$ 应用量化或SVD，假设 $\Delta$ 的数值分布稳定且低秩。本文的关键差异在于处理 $\Delta$ 幅度随SFT数据规模动态增大的特性，传统单阶段方法在此条件下误差不可控。

### 1-bit量化降尺度

针对高幅度Delta参数直接量化导致绝对误差过大的问题，D-QRELO首先执行粗粒度1-bit量化。设计动机在于利用符号函数快速捕捉主导方向，并通过缩放因子 $\alpha$ 最小化Frobenius范数误差，从而将数值范围压缩至最小。

$$ \hat{\Delta}_{quant} = \alpha \cdot \text{sign}(\Delta), \quad \alpha = \frac{1}{nm} \sum_{i,j} |\Delta_{ij}| $$

该公式中 $\alpha$ 取Delta平均绝对值，确保量化近似 $\hat{\Delta}_{quant}$ 在Frobenius范数意义下最优。量化后的残差矩阵 $R = \Delta - \hat{\Delta}_{quant}$ 数值范围显著缩小，为后续低秩近似创造了有利条件。

### 残差低秩近似

量化后的残差 $R$ 虽幅度小，但仍包含细粒度信息。D-QRELO对 $R$ 执行SVD截断，设计动机在于残差的低秩结构在幅度缩小后更易被捕捉，避免了直接SVD高幅度Delta时高频分量丢失的问题。

$$ R \approx U_r \Sigma_r V_r^T, \quad \hat{\Delta} = \hat{\Delta}_{quant} + U_r \Sigma_r V_r^T $$

其中 $r$ 为满足目标压缩比 $\rho_1$ 的秩。最终压缩表示 $\hat{\Delta}$ 由量化项与低秩残差项相加构成。这种顺序确保了量化处理大尺度信号，SVD处理小尺度细节，二者互补而非竞争，有效缓解了绝对误差累积。

## 实验评估

实验在8个模型上进行，涵盖Dense与MoE架构，任务包括数学推理、代码生成、知识问答等。基线覆盖剪枝（Random, Magnitude, Wanda）、SVD、BitDelta及Delta-CoMe。在OpenMath2模型上，D-QRELO在GSM8K任务保留率84.84%，优于Delta-CoMe（75.69%）与BitDelta（73.87%），接近SFT全精度（88.93%）。

| 方法 | OpenMath2 GSM8K | OpenMath2 MATH | DS-R1-Qwen3-8B AIME24 | DS-R1-Qwen3-8B GPQA |
|---|---|---|---|---|
| SVD | 25.2 | 33.8 | 21.50 | 47.31 |
| BitDelta | 50.34 | 27.6 | 37.83 | 57.06 |
| Delta-CoMe | 75.69 | 50.4 | 61.47 | 57.06 |
| D-QRELO | 84.84 | 57.4 | 62.71 | 59.65 |

消融实验验证了两阶段顺序的必要性。先SVD后量化（SVD + One-bit + SVD）在OpenMath2 GSM8K上仅43.97%，显著低于先量化后SVD（84.84%）。这表明量化先行能有效降低SVD处理的数值尺度，而SVD先行则导致残差高频分量难以被1-bit量化准确捕捉。此外，D-QRELO在Qwen3-30B-A3B-Instruct上IFEval保留率83.73%，略高于SFT的83.18%，显示其在特定任务上可能优于全精度微调。

评估边界方面，论文未提供代码与超参数细节，可复现性受限。指标侧重下游任务保留率，未报告WikiText-2 PPL，难以与全量权重量化方法直接对比。压缩比固定为1/8，未探索更低压缩比下的性能衰减曲线，且未分析RLHF等非SFT场景下的Delta特性。

## 关联研究分析

从问题动机看，D-QRELO与CALDERA（Saha et al., 2024）均采用量化+低秩分解框架，但CALDERA针对全量权重且需交替优化，而D-QRELO针对Delta参数且无需训练。差异根源在于Delta参数幅度随SFT数据动态变化，全量权重分布相对静态，因此D-QRELO的“先量化降尺度”策略对Delta更关键，而CALDERA的交替优化在全量权重上更稳定。

从方法设计看，D-QRELO与BitDelta（Liu et al., 2024a）均使用1-bit量化，但BitDelta将其作为最终压缩形式，D-QRELO将其作为残差分解的第一步。BitDelta在小幅度Delta上接近无损，但在大幅度Delta上绝对误差过大；D-QRELO通过引入SVD残差恢复，弥补了量化损失。这种设计差异源于对Delta参数复杂度随数据规模变化的洞察，BitDelta未考虑此动态特性，导致其在强SFT模型上失效。

## 总结

D-QRELO解决了大规模SFT模型Delta参数幅度增大导致的压缩失效问题，通过1-bit量化降尺度与残差SVD的组合，在无需训练与数据的情况下实现了高保留率。实验显示其在OpenMath2 GSM8K上保留率84.84%，优于现有SOTA方法Delta-CoMe。然而，其压缩比受限于1/16的物理下限，且对早期层压缩敏感，未探索更低压缩比下的性能边界。当SFT数据规模进一步增大至十亿级时，Delta参数熵是否继续线性增长，以及D-QRELO的两阶段策略是否仍能维持误差可控，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16940)