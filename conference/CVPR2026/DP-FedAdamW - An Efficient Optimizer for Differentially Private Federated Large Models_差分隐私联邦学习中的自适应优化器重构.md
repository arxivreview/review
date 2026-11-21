# CVPR2026最新论文 ｜DP-FedAdamW: An Efficient Optimizer for Differentially Private Federated Large Models ｜差分隐私联邦学习中的自适应优化器重构

研究机构：西安电子科技大学、天津大学

作者：Jin Liu、Yinbin Miao、Ning Xi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19945)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19945)

> 联邦学习（Federated Learning, FL）结合差分隐私（Differential Privacy, DP）时，标准自适应优化器 AdamW 因噪声污染与数据异质性导致二阶矩估计失效，性能甚至劣于随机梯度下降（SGD）。现有 DPFL 算法多基于 SGD，缺乏对大规模 Transformer 模型的高效优化支持，而直接应用 AdamW 会引发方差放大、系统性偏差与客户端漂移。本文提出 DP-FedAdamW，通过块级二阶矩聚合、无偏校正与局部-全局对齐机制恢复 AdamW 在 DPFL 中的有效性。该方法在严格隐私预算下显著优于现有基线，但其块级聚合粒度对收敛速率的理论影响尚未完全量化。

## 研究背景

联邦学习允许客户端在本地训练模型并仅上传更新，避免原始数据集中存储，但模型更新仍面临隐私泄露风险。差分隐私通过注入高斯噪声提供形式化保护，然而噪声方差随模型维度线性增长，导致大规模模型训练困难。在 FL 场景中，非独立同分布（non-IID）数据进一步加剧了梯度异质性，使得标准 DP-SGD 的收敛性恶化。

主流 DPFL 算法如 DP-FedAvg 和 DP-SCAFFOLD 均基于 SGD 优化器，通过逐样本裁剪与噪声注入实现隐私保证。然而，SGD 在处理大规模 Transformer 模型时效率低下，且无法利用自适应学习率加速收敛。近期研究尝试将自适应优化器引入 FL，如 FedOpt 和 FedLADA，但这些工作主要评估 CNN 模型，且未考虑 DP 噪声对二阶矩估计的污染。本文指出，直接应用 AdamW 到 DPFL 会导致二阶矩估计方差放大、系统性偏差及客户端漂移，使得 AdamW 在 Transformer 模型上表现劣于 SGD。

## 核心方法

### 方法参照系

标准 DPFL 流程中，客户端计算逐样本梯度，执行裁剪与噪声注入，服务器聚合更新。本文问题与该通用流程的关键差异在于：引入 AdamW 优化器后，二阶矩估计 $v$ 受 DP 噪声与非-IID 数据双重影响，导致自适应学习率失真，需专门设计校正机制。

### 块级二阶矩聚合

针对二阶矩估计方差放大问题，本文提出块级聚合策略。传统方法需传输与模型参数同维度的二阶矩向量，通信开销巨大。本文将参数划分为 $B$ 个块（如注意力头、MLP 层），仅传输每块的二阶矩均值：

$$ \bar{v}_b = \frac{1}{|b|} \sum_{i \in b} v_i $$

该设计将通信成本从 $O(d)$ 降至 $O(B)$，同时通过块内平均抑制非-IID 数据导致的方差波动，稳定自适应缩放。

### 无偏二阶矩校正

DP 噪声引入系统性偏差，导致二阶矩估计偏高。本文提出偏差校正（Bias-Corrected, BC）机制，从二阶矩估计中减去噪声方差贡献：

$$ \hat{v}_{i[t,k]} = v_{i[t,k]} - \frac{\sigma^2 C^2}{(sR)^2} $$

其中 $\sigma$ 为噪声乘子，$C$ 为裁剪阈值，$sR$ 为批大小。该公式移除了 DP 噪声引入的常数偏差，恢复了非隐私 AdamW 的缩放行为，确保自适应学习率准确反映真实梯度曲率。

### 局部-全局对齐

客户端漂移源于非-IID 数据与 DP 噪声共同作用，使局部更新偏离全局方向。本文引入对齐项 $\gamma \Delta_G^t$，其中 $\Delta_G^t = \frac{1}{S} \sum_{i=1}^S (\theta_{i[t,K]} - \theta_{i[t,0]})$ 为全局更新估计：

$$ \theta_{i[t,k+1]} = \theta_{i[t,k]} - \eta \left( \hat{m}_{i[t,k]} \odot \vartheta_{i[t,k]} + \gamma \Delta_G^t \right) $$

该机制软正则化局部步长，当客户端更新偏离全局趋势时，对齐项将其拉回，抑制客户端漂移，提升全局收敛稳定性。

## 实验评估

实验在 CIFAR-10/100、Tiny-ImageNet 及 GLUE 基准上进行，使用 ResNet-18、ViT-Base、Swin-Tiny/Base 及 RoBERTa-Base 模型，采用 Dirichlet 分布模拟 non-IID 数据（$\alpha \in \{0.1, 0.6, 0.8\}$）。基线覆盖 DP-FedAvg、DP-SCAFFOLD、DP-FedAvg-LS、DP-FedSAM 及 DP-LocalAdamW，但未包含集中式 SOTA 如 NoiseCurve 或 DP-Muon，可能因 FL 协议差异导致无法直接对比。

| 方法 | CIFAR-10 (Swin-B, ε=1) | CIFAR-100 (Swin-B, ε=1) | Tiny-ImageNet (Swin-B, ε=1) |
| :--- | :--- | :--- | :--- |
| DP-FedAvg | 66.52±0.89 | 19.66±1.52 | 20.65±0.77 |
| DP-SCAFFOLD | 66.39±0.68 | 22.38±0.67 | 20.93±0.66 |
| DP-FedAvg-LS | 71.57±1.02 | 25.77±0.61 | 26.89±0.46 |
| DP-FedSAM | 53.51±1.39 | 12.33±0.64 | 10.88±0.95 |
| DP-LocalAdamW | 66.57±1.35 | 24.69±0.88 | 28.40±0.72 |
| DP-FedAdamW | 77.50±0.54 | 30.06±0.41 | 34.23±0.50 |

DP-FedAdamW 在 ε=1 下显著优于所有基线，尤其在 Tiny-ImageNet 上领先 DP-FedAvg-LS 7.34 个百分点，表明自适应优化器在严格隐私预算下的优势。消融实验显示，偏差校正（BC）贡献最大，移除后 CIFAR-100 精度从 67.42% 降至 67.02%，块级聚合（Agg）与对齐项（Align）分别带来 0.41% 和 0.37% 增益，三者协同实现最佳性能。

评估边界方面，论文未报告计算效率与内存开销，仅声明代码在附录但未提供 URL。超参数选择（如 $\gamma=0.5$）基于经验调优，缺乏理论指导。隐私预算 $\delta$ 设置为 $10^{-5}$（CIFAR）或 $10^{-6}$（Tiny-ImageNet），未讨论不同 $\delta$ 对结果的影响。

## 关联研究分析

从问题动机看，DP-AdamW-BC（Chooi et al., 2025）在集中式训练中通过偏差校正解决 DP 噪声对二阶矩的污染，但本文将其扩展至联邦场景，额外处理非-IID 数据导致的方差放大与客户端漂移。DP-AdamW-BC 未考虑通信效率，而本文通过块级聚合将通信成本从 $O(d)$ 降至 $O(B)$，这是 FL 场景特有的约束。差异根源在于任务特性：集中式训练无客户端漂移问题，而 FL 中非-IID 数据使局部更新偏离全局方向，需对齐机制抑制。

从方法设计看，FedLADA（Tasnim et al., 2026）通过聚合二阶矩估计降低通信成本，但未考虑 DP 噪声引入的偏差，导致二阶矩估计偏高，自适应学习率失真。本文的 BC 机制显式移除噪声偏差，确保二阶矩估计无偏，这是 FedLADA 缺失的关键组件。此外，DP-SCAFFOLD 使用控制变量缓解客户端漂移，但基于 SGD 优化器，无法利用自适应学习率加速收敛。本文的对齐项 $\gamma \Delta_G^t$ 功能类似，但基于 AdamW 动量，更适用于大规模 Transformer 模型。

## 总结

本文核心矛盾是 DP 噪声与非-IID 数据共同导致 AdamW 二阶矩估计失效，现有 DPFL 算法基于 SGD 无法高效训练大规模模型。本文切入点在于识别二阶矩估计的方差放大、系统性偏差与客户端漂移三大问题，通过块级聚合、无偏校正与局部-全局对齐机制恢复 AdamW 有效性。实验证明 DP-FedAdamW 在 ε=1 下 CIFAR-10 精度达 77.50%，Tiny-ImageNet 达 34.23%，显著优于基线。其边界在于块级聚合粒度对收敛速率的理论影响未完全量化，且未评估计算效率。当块数 $B$ 增大时，块内平均的方差抑制效果是否线性提升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19945)