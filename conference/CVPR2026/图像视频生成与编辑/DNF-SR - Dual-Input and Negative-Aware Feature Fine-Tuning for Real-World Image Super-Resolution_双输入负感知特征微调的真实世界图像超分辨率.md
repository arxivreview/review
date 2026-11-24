# CVPR2026最新论文 ｜DNF-SR: Dual-Input and Negative-Aware Feature Fine-Tuning for Real-World Image Super-Resolution ｜双输入负感知特征微调的真实世界图像超分辨率

研究机构：南开大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e945ea6d9a51)

> 真实世界图像超分辨率（Real-ISR）的核心矛盾在于单步扩散模型推理效率与重建保真度、感知真实感之间的平衡。现有单步方法直接将低分辨率（LR）潜变量输入扩散模型，因高频信息缺失导致分布差距，引发伪影或细节丢失。DNF-SR通过双输入策略（噪声LR+原始LR）弥合分布差距，并引入负感知特征微调（NF2T）在图像与特征空间优化，实现单步高效重建。该方法在感知质量指标上超越基线，但全参考指标（PSNR）未报告，保真度验证存在盲区。

## 研究背景

扩散模型通过逐步去噪学习数据分布，但其多步迭代导致推理延迟，难以满足实时应用需求。流匹配（Flow Matching）通过预测速度场 $v$ 实现单步映射，成为加速推理的关键路径。然而，LR图像高频信息稀疏，与扩散模型原生噪声输入存在显著分布差距，直接替换输入导致预训练参数失效，重建结果出现网格伪影或结构失真。

单步扩散超分的主流路线分为两类：一是蒸馏多步模型（如SinSR），增加参数量且限制性能；二是直接微调T2I模型（如OSEDiff、OMGSR），但LR潜变量在任意中间时间步 $t$ 的高频成分均少于HR潜变量，分布差距无法消除。OMGSR虽在中间时间步注入LR，仍面临高频信息缺失问题。DNF-SR的切入点在于：通过双输入策略同时提供噪声LR（弥合分布差距）和原始LR（保持保真度），并利用图像编辑模型（Flux-Kontext）而非T2I模型，更有效地利用LR条件信息。

## 核心方法

### 方法参照系

单步扩散超分的标准流程是将LR潜变量 $z_{LR}$ 作为输入，在中间时间步 $t_{mid}$ 预测速度场 $v_\theta$，通过 $\hat{z}_{HR} = z_{mix} - t_{mid}v_\theta$ 重建HR潜变量。本文的关键差异在于：输入从单一 $z_{LR}$ 扩展为双输入 $z_{mix}$（噪声LR）与 $z_{LR}$（原始LR），并采用图像编辑模型而非T2I模型，以解决分布差距与保真度的冲突。

### 双输入策略与中间时间步去噪

设计动机：直接输入 $z_{LR}$ 导致高频信息缺失，而加噪 $z_{LR}$ 会破坏内容。双输入策略通过 $z_{mix} = (1-t_{mid})z_{LR} + t_{mid}\epsilon$ 提供与扩散模型原生输入分布一致的噪声LR，同时保留原始 $z_{LR}$ 作为条件，确保内容保真。

$$
\hat{z}_{HR} = z_{mix} - t_{mid}v_\theta(z_{mix}, z_{LR}, c)
$$

其中 $c$ 为文本条件，$v_\theta$ 为DiT块预测的速度场。该设计使模型在 $t_{mid}=0.5$ 时平衡低频结构（保真度）与高频细节（真实感），避免 $t=0$ 时无法优化或 $t=1$ 时内容丢失的问题。

### 负感知特征微调（NF2T）

设计动机：DiffusionNFT在潜空间优化导致网格伪影，且仅利用成对偏好数据。NF2T将优化转移至图像与特征空间，利用多指标奖励聚合的正负样本隐式方向，提升优化稳定性。

$$
\mathcal{L}_{NF^2T} = \mathbb{E}_{\pi_{old}(\hat{z}_{HR}|z_{LR}), z_{LR}} \left[ r\mathcal{L}_{Rec}(\hat{x}_{\theta}^+, \hat{x}_{HR}) + (1-r)\mathcal{L}_{Rec}(\hat{x}_{\theta}^-, \hat{x}_{HR}) \right]
$$

其中 $\hat{x}_{\theta}^{\pm} = D_\phi(z_{mix} - t_{mid}v_\theta^{\pm})$，$r$ 为奖励分数，$\mathcal{L}_{Rec}$ 包含MSE与DISTS损失。该公式通过图像空间重建损失替代潜空间速度场损失，消除网格伪影，并利用多指标（LPIPS、DISTS、CLIPIQA、MUSIQ、MANIQA）聚合的奖励 $r$ 提供更清晰的优化信号。

## 实验评估

实验在RealSR、DRealSR、DIV2K-Val、RealLQ250四个基准上评估，基线覆盖DiffBIR、SeeSR、OMGSR等单步/多步方法，但缺失频域增强类方法（如HDW-SR）。主结果显示，DNF-SR在无参考指标（MUSIQ、MANIQA、QALIGN）上全面领先，例如RealSR上MUSIQ达72.04，超越Disentangled Textual Priors的71.84（据领域综述）。

| 方法 | LPIPS↓ | MUSIQ↑ | MANIQA↑ | QALIGN↑ |
|---|---|---|---|---|
| DNF-SR (SFT) | 0.2925 | 70.6717 | 0.6903 | 3.9162 |
| NF2T (NR+FR) | 0.3239 | 72.0396 | 0.693 | 4.0718 |

消融实验表明，双输入策略（$z_{mix}, z_{LR}$）在 $t=0.5$ 时LPIPS最低（0.2925），MUSIQ最高（70.6717）；NF2T后训练使MUSIQ提升1.37（70.6717→72.0396），QALIGN提升0.1556（3.9162→4.0718），但LPIPS上升0.0314（0.2925→0.3239），反映保真度-真实感权衡。

评估边界：论文未报告PSNR，仅用LPIPS作为全参考指标，无法量化像素级保真度；RealLQ250无参考HR，仅评估无参考指标；代码开源但超参数（如 $\lambda_1=5, \lambda_4=0.5$）未详细讨论，可复现性依赖特定Flux-Kontext版本。

## 关联研究分析

从问题动机看，DNF-SR与OMGSR均针对单步扩散的分布差距，但OMGSR仅注入LR潜变量，依赖中间时间步 $t$ 的隐式对齐；DNF-SR通过显式双输入解耦分布差距与保真度，根源在于图像编辑模型（Flux-Kontext）对条件信息的感知能力更强，而非T2I模型的生成先验主导。从方法设计看，NF2T与DiffusionDPO同属偏好对齐，但DiffusionDPO限于成对数据且需概率建模；NF2T利用多指标奖励聚合的正负样本，在图像/特征空间优化，避免了潜空间伪影，根源在于SR任务对高频细节的敏感性要求优化信号更稳定。

## 总结

DNF-SR解决单步扩散超分中分布差距与保真度的冲突，通过双输入策略（噪声LR+原始LR）和NF2T后训练，在RealSR上MUSIQ达72.04，QALIGN达4.0718，超越基线。其边界在于未报告PSNR，保真度验证依赖LPIPS，且双输入策略增加计算开销（参数量未量化）。当LR图像退化程度极端（如严重模糊+噪声）时，双输入策略中噪声LR的内容破坏是否导致保真度下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e945ea6d9a51)