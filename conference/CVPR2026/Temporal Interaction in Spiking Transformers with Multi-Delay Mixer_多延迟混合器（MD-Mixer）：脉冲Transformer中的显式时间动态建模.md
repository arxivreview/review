# CVPR2026最新论文 ｜Temporal Interaction in Spiking Transformers with Multi-Delay Mixer ｜多延迟混合器（MD-Mixer）：脉冲Transformer中的显式时间动态建模

研究机构：电子科技大学、新加坡国立大学

作者：Kexin Shi、Hanwen Liu、Zeyang Song 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c6c8e6dc6c4)

> 脉冲Transformer旨在利用事件驱动特性降低边缘设备能耗，但现有自注意力机制仅捕捉单时间步内的空间关系，缺乏对历史脉冲的显式交互，导致动态视觉任务性能受限。本文通过引入多分支可学习延迟机制，在Key和Value路径中聚合多尺度历史信息，实现了时空混合。该方法作为即插即用模块，在动态基准上刷新了SOTA，但在静态大规模分类中未超越最新架构，其能效收益在真实硬件上的表现仍存疑。

## 研究背景

脉冲神经网络（SNN）通过离散脉冲编码信息，其稀疏激活特性在神经形态硬件上具有显著的能效优势。然而，将Transformer架构引入SNN时，核心的脉冲自注意力（Spiking Self-Attention, SSA）机制通常仅在当前时间步内计算Query、Key和Value的交互，时间依赖完全依赖LIF神经元的膜电位衰减隐式处理。这种“空间优先”的设计导致模型难以捕捉长程时间依赖，尤其在动态视觉传感器（DVS）数据等需要跨时间步整合信息的场景中表现不佳。

现有解决方案主要分为两类：一类是显式时空建模，如STAtten采用块级策略，但增加了计算开销；另一类是轻量级增强，如TIM仅将历史信息注入Query分支，建模能力有限。这些方法要么牺牲效率，要么无法充分挖掘多尺度时间模式。本文的切入点在于，现有机制缺乏对时间交互能力的量化评估，且未利用生物神经系统中轴突延迟这一天然的时间处理机制。通过提出时间交互系数（Temporal Interaction Coefficient, TIC）量化现有机制的时间盲区，并设计多延迟混合器（Multi-Delay Mixer, MD-Mixer）显式建模多尺度时间依赖，本文旨在解决脉冲Transformer中时间动态建模不足的核心瓶颈。

## 核心方法

### 方法参照系

标准脉冲Transformer流程中，输入张量 $X \in \mathbb{R}^{T \times N \times C}$ 经过线性投影生成Q、K、V，再经LIF神经元层输出。本文的关键差异在于，K和V的生成路径中插入了MD-Mixer模块，而Q保持原始时间对齐，从而在注意力计算前引入时间维度的信息聚合。

### 时间交互系数（TIC）

现有脉冲自注意力机制的时间依赖是隐式的，缺乏量化指标。本文提出TIC来度量注意力输出对历史时间步的依赖程度。在时间步 $q$，TIC定义为依赖分布 $\hat{R}_q$ 的信息熵：

$$ TIC_q = H(\hat{R}_q) $$

其中 $\hat{R}_q$ 是依赖向量 $R_q = [R_{q \to 1}, \dots, R_{q \to q}]$ 经L1归一化后的分布，$R_{q \to p} = \frac{\partial Z_q}{\partial X_p}$ 衡量输出 $Z_q$ 对历史输入 $X_p$ 的敏感度。TIC值越高，表明时间依赖分布越广，时间交互能力越强。实验显示，SSA、QKTA和SDSA的TIC值在1.47至2.35之间，且依赖分布尖锐地集中在当前时间步，证实了历史贡献可忽略。

### 多延迟混合器（MD-Mixer）

MD-Mixer借鉴生物轴突延迟机制，通过多个可学习延迟分支聚合多尺度历史信息。对于通道 $i$，引入 $K$ 个可学习延迟 $\{d_i^{(k)}\}_{k=1}^K$ 和权重 $\{\alpha_i^{(k)}\}_{k=1}^K$，聚合特征为：

$$ \tilde{X}_{t,i} = \sum_{k=1}^K \alpha_i^{(k)} X_{t-d_i^{(k)},i} $$

该公式表明，每个通道的当前特征由不同延迟的历史特征加权求和而成，实现了通道自适应的多尺度时间建模。为优化离散延迟，本文采用软到硬优化策略，引入三角形延迟分布 $\phi(d; d^*)$ 和温度退火机制：

$$ I_{t,j} = \sum_{k=1}^K \alpha_j^{(k)} \sum_{d=0}^{T-1} \phi(d; d_j^{(k)*}) \cdot X_{t-d,j} $$

其中 $\phi(d; d^*) = \frac{1}{N} \sigma(\frac{1-|d-d^*|}{\tau})$，$\tau$ 随训练进度按平方余弦调度退火。初始时 $\tau$ 较大，分布平坦，允许探索多种延迟；训练后期 $\tau$ 趋近0，分布收敛至最优延迟的One-hot分布，实现了离散延迟的连续梯度优化。

## 实验评估

实验在ImageNet、CIFAR10-DVS、N-Caltech101、s-CIFAR10/100等基准上进行，基线覆盖Spikformer、QKFormer、SDT-V1/V2及STAtten、TIM等主流方法，但未包含CSDformer等转换类方法。

| 方法 | 架构 | CIFAR10-DVS (%) | N-Caltech101 (%) |
| :--- | :--- | :--- | :--- |
| Spikformer | Spikformer-2-256 | 80.90 | 80.23 |
| STAtten + Spikformer | Spikformer-2-256 | 82.40 | 83.12 |
| MD-Mixer + Spikformer | Spikformer-2-256 | 83.37 | 84.57 |
| QKFormer | QKFormer-2-256 | 84.10 | 79.69 |
| MD-Mixer + QKFormer | QKFormer-2-256 | 85.20 | 82.06 |
| SDT-V1 | SDT-V1-2-256 | 80.00 | 81.80 |
| MD-Mixer + SDT-V1 | SDT-V1-2-256 | 82.40 | 84.59 |

在动态视觉任务上，MD-Mixer+QKFormer在CIFAR10-DVS达到85.20%，较基线提升1.10%；在N-Caltech101上，MD-Mixer+SDT-V1达到84.59%，较基线提升2.79%。在长序列任务s-CIFAR10上，MD-Mixer+SDT-V1达到86.65%，较基线83.65%提升3.00%，显著优于STAtten的83.90%。

| 数据集 | 模型 | 精度 (%) |
| :--- | :--- | :--- |
| s-CIFAR10 | Baseline | 83.65 |
| s-CIFAR10 | + Random Delay | 84.39 |
| s-CIFAR10 | + MD-Mixer | 86.65 |
| CIFAR10-DVS | Baseline | 80.00 |
| CIFAR10-DVS | + Random Delay | 80.52 |
| CIFAR10-DVS | + MD-Mixer | 82.44 |

消融实验显示，随机延迟仅带来0.74%（s-CIFAR10）和0.52%（CIFAR10-DVS）的提升，而可学习延迟带来3.00%和2.44%的提升，证实了自适应延迟优化的关键作用。延迟分支数在3-4个时性能最优，过多分支导致性能下降，表明多尺度建模存在复杂度上限。

评估边界方面，论文未报告置信区间，且未在真实神经形态硬件上验证能效。MD-Mixer将K/V计算复杂度从 $O(TD^2)$ 降至 $O(KTD)$，但增加了时间步内的分支计算，其实际能效收益需硬件验证。代码未公开，超参数细节在补充材料中，可复现性受限。

## 关联研究分析

从问题动机看，MD-Mixer与STAtten均旨在解决时间动态建模不足，但STAtten采用块级策略，将时间步分组处理，而MD-Mixer通过多延迟分支实现通道自适应的时间聚合。STAtten在ImageNet上达到78.11%（SDT-V1-8-768），MD-Mixer达到78.23%，两者接近，但在s-CIFAR10上MD-Mixer（86.65%）显著优于STAtten（83.90%），表明多延迟机制在长序列任务中更具优势。这一差异可能源于STAtten的块级策略限制了跨块时间交互，而MD-Mixer的延迟分支可跨越任意时间步。

从方法设计看，MD-Mixer与TIM均基于Spikformer，但TIM仅将历史信息注入Query分支，而MD-Mixer同时增强Key和Value。TIM在CIFAR10-DVS上达到82.00%，MD-Mixer达到83.37%，提升1.37%。这一差异表明，仅增强Query不足以捕捉完整的时间依赖，Key和Value的增强对注意力计算中的时空混合至关重要。MD-Mixer的TIC分析也证实，增强K/V后，TIC值从1.74提升至2.86（QKTA），时间依赖分布显著变宽。

## 总结

本文针对脉冲Transformer中时间动态建模不足的问题，提出TIC量化指标和多延迟混合器（MD-Mixer）。通过多分支可学习延迟和温度退火优化，MD-Mixer在Key和Value路径中显式聚合多尺度历史信息，实现了时空混合。实验显示，MD-Mixer在CIFAR10-DVS上达到85.20%（QKFormer），在s-CIFAR10上达到86.65%（SDT-V1），刷新了动态和长序列任务的SOTA。然而，在ImageNet静态分类上，MD-Mixer+SDT-V2达到80.02%，未超越SAFformer的80.44%，表明其优势主要在动态场景。MD-Mixer的额外计算开销在真实神经形态硬件上是否抵消了精度收益，论文未给出硬件级能效验证，这一局限限制了其在边缘部署中的实际价值评估。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_5c6c8e6dc6c4)