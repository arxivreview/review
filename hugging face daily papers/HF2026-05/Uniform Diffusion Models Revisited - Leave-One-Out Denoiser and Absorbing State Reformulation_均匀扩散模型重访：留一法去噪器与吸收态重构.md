# HuggingFace最新推荐论文 ｜Uniform Diffusion Models Revisited: Leave-One-Out Denoiser and Absorbing State Reformulation ｜均匀扩散模型重访：留一法去噪器与吸收态重构

作者：Samson Gourevitch、Yazid Janati、Dario Shariatian 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22765)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22765)

> 离散扩散模型在语言生成中面临参数化选择与训练目标错位的理论盲区，导致均匀扩散模型（UDM）性能长期落后于掩码扩散模型（MDM）。现有研究将差距归因于边际分布差异，但忽略了反向核参数化对最优解的影响。本文通过证明UDM中ELBO最优解为留一法后验而非标准去噪后验，并构建吸收态重构框架，解耦了参数化与训练目标。这一发现揭示了MDM优势源于参数化设计而非掩码机制本身，但其在长序列计算复杂度上的实际影响尚存疑。

## 研究背景

离散扩散模型通过前向加噪与反向去噪过程处理文本等离散数据，其核心在于定义从参考分布到数据分布的马尔可夫链。在反向过程中，模型需估计条件分布 $q_{s|0,t}(\mathbf{x}_s|\mathbf{x}_0, \mathbf{x}_t)$，该分布被称为“桥接”（Bridge），它连接了干净数据 $\mathbf{x}_0$ 与噪声状态 $\mathbf{x}_t$。对于均匀扩散模型（UDM），每个位置被均匀采样的token替换，其桥接公式包含复杂的归一化项，导致桥接函数关于 $\mathbf{x}_0$ 呈非线性。这种非线性使得直接应用标准去噪后验作为反向核参数化时，无法保证训练目标的最优性，构成了理解UDM性能瓶颈的关键数学障碍。

早期研究聚焦于离散扩散的基础框架，如D3PM和MDLM，确立了掩码扩散模型（MDM）在大规模词汇表下的优越性。主流观点认为MDM优于UDM是因为掩码符号提供了更清晰的信号，但这一解释掩盖了参数化选择的深层影响。现有方案在UDM中通常采用“桥接插件”（Bridge Plug-in）参数化，即直接用网络预测的 $\hat{\mathbf{x}}_0$ 代入桥接公式，却未严格分析该参数化下ELBO的最优解究竟是什么。本文切入点在于揭示这一参数化与训练目标之间的错位：标准交叉熵目标优化的是去噪后验，而ELBO在桥接插件参数化下实际优化的是留一法后验（Leave-One-Out Posterior, LOO Posterior）。

## 核心方法

### 方法参照系

离散扩散模型的标准训练流程基于负对数似然下界（ELBO），通过最小化期望ELBO来学习反向转移核。在MDM中，由于桥接函数关于 $\mathbf{x}_0$ 是仿射的，去噪后验与桥接插件参数化的最优解重合，因此标准交叉熵训练是有效的。然而，在UDM中，桥接函数的非线性破坏了这种等价性，导致标准流程中“网络预测即最优反向核”的假设失效。本文的核心差异在于识别并量化了这种失效，并提出了基于LOO后验的新参数化方案。

### 留一法后验的最优性证明

在桥接插件参数化下，ELBO的最优解并非去噪后验 $p_{0|t}(\mathbf{x}_0|\mathbf{x}_t)$，而是留一法后验 $p_{0|t}^{loo}(\mathbf{x}_0|\mathbf{x}_t)$。LOO后验定义为预测位置 $\ell$ 的干净token时，仅使用除 $\ell$ 以外的所有噪声token $\mathbf{x}_{t-\ell}$。其数学表达为：

$$
p_{0|t}^{loo, \ell}(\mathbf{x}_0^\ell | \mathbf{x}_{t-\ell}) \propto p_0(\mathbf{x}_0) \prod_{j \neq \ell} q_{t|0}^j(\mathbf{x}_t^j | \mathbf{x}_0^j)
$$

这一设计动机在于解决UDM中桥接非线性导致的训练目标错位。标准去噪后验依赖于 $\mathbf{x}_t^\ell$，而LOO后验显式排除了 $\mathbf{x}_t^\ell$ 的影响，从而匹配了ELBO在桥接插件参数化下的真实最小化目标。通过推导去噪后验、LOO后验与得分函数之间的精确转换公式，本文实现了参数化与训练目标的解耦，允许使用标准交叉熵损失训练LOO预测器，同时保持ELBO的理论最优性。

### 吸收态重构与采样改进

基于LOO后验的性质，本文提出了吸收态均匀扩散模型（AUDM）和掩码均匀扩散模型（MUDM）。AUDM通过引入辅助变量 $\mathbf{u} \sim \text{Uniform}(\{1, K\})^L$，将UDM的前向过程重构为条件吸收态扩散。在给定 $\mathbf{u}$ 的条件下，每个坐标 $\ell$ 的演化遵循吸收态动力学，吸收态固定为 $\mathbf{u}^\ell$。这种重构保留了UDM的联合分布，但继承了MDM的结构简化，使得去噪后验在吸收态位置退化为Dirac分布，从而简化了采样过程。此外，利用LOO后验与边际分布 $p_t$ 的关系，本文设计了无需额外训练的预测-校正（Predictor-Corrector）采样器，通过Gibbs更新迭代校正采样轨迹，提升了生成质量。

## 实验评估

实验在WikiText、PTB、LM1B、AG News、Lambada和PubMed六个语言建模数据集上进行，评估指标为困惑度（Perplexity, PPL）。基线包括标准UDM（去噪器/LOO）、MDM和最大耦合UDM。本文未对比自回归模型（如GPT系列）或最新SOTA离散扩散模型（如MDLM变体），限制了与领域SOTA的直接可比性。

| 方法 | 损失 | 参数化 | OWT | AG News | Lambada | LM1B | PTB | PubMed | WikiText |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Absorbing Uniform Diffusion | ELBO | Denoiser | 23.32 | 61.37 | 45.87 | 72.02 | 72.21 | 43.01 | 33.22 |
| Uniform Diffusion | Cross-Entropy | Denoiser | 25.45 | 74.03 | 49.04 | 83.43 | 84.13 | 44.66 | 39.17 |
| Uniform Diffusion | Cross-Entropy | LOO-Denoiser | 25.18 | 72.66 | 46.91 | 81.54 | 87.79 | 43.72 | 36.67 |
| Uniform Diffusion | ELBO | Denoiser | 25.20 | 73.33 | 46.80 | 80.33 | 84.94 | 45.75 | 37.44 |
| Uniform Diffusion | ELBO | LOO-Denoiser | 25.30 | 73.82 | 46.22 | 82.03 | 83.24 | 44.52 | 37.23 |
| Max Coupling Uniform Diffusion | ELBO | Denoiser | 32.96 | 112.64 | 64.71 | 109.97 | 62.44 | 112.70 | 106.53 |
| Max Coupling Uniform Diffusion | ELBO | LOO-Denoiser | 32.21 | 117.21 | 110.78 | 65.82 | 51.40 | 106.53 | 49.41 |
| Masked Diffusion | ELBO | Denoiser | 22.90 | 64.57 | 48.79 | 73.06 | 74.99 | 43.13 | 35.16 |

在UDM框架内，LOO参数化一致优于标准去噪器参数化。例如，在WikiText上，ELBO训练的LOO-Denoiser PPL为37.23，优于ELBO训练的Denoiser的37.44；Cross-Entropy训练的LOO-Denoiser PPL为36.67，优于Cross-Entropy训练的Denoiser的39.17。AUDM（ELBO/Denoiser）在WikiText上取得33.22的PPL，优于MDM的35.16，证明了吸收态重构的有效性。然而，在AG News上，AUDM的61.37优于MDM的64.57，但在Lambada上，AUDM的45.87略优于MDM的48.79，差异较小。

消融实验显示，LOO参数化在大多数数据集上带来1-3个PPL点的提升，但在PTB上，Cross-Entropy训练的LOO-Denoiser（87.79）反而劣于Denoiser（84.13），表明LOO优势并非在所有数据集上单调。这一反直觉结果可能源于PTB数据集的特定结构或训练动态，论文未深入分析。此外，最大耦合UDM的LOO参数化在Lambada上PPL从64.71降至51.40，降幅显著，说明LOO对复杂耦合结构的改进潜力更大。

评估边界方面，论文未报告置信区间或多次运行的方差，数值比较需谨慎。代码已开源，但超参数细节未完全披露，限制了可复现性。此外，实验未覆盖长序列（如超过1024 token）场景，LOO参数化在长序列中的计算复杂度是否抵消并行优势，论文未给出回答。

## 关联研究分析

从问题动机看，本文挑战了MDM优于UDM的传统解释。MDLM（Austin et al., 2021）和D3PM（Ahn et al., 2021）等早期工作将MDM的优势归因于掩码符号提供的清晰信号，但本文证明这种优势源于参数化选择而非掩码本身。MDM中桥接函数关于 $\mathbf{x}_0$ 是仿射的，使得去噪后验与桥接插件最优解重合，而UDM中桥接的非线性导致错位。这一发现暗示，若UDM采用LOO参数化，其性能可媲美甚至超越MDM，从而重新定义了离散扩散模型的设计空间。

从方法设计看，本文的LOO参数化与连续扩散中的得分匹配（Score Matching）有相似性，但应用于离散空间。在连续扩散中，得分函数 $\nabla_x \log p_t(x)$ 是训练目标的核心，而在离散扩散中，LOO后验扮演了类似角色。然而，LOO参数化要求网络预测时忽略当前位置的噪声输入，这在架构上可通过Hollow Transformer实现，但论文指出标准注意力机制更易训练，因此LOO不变性需通过训练学习而非架构强制。这种设计选择与Consistency Models（Song et al., 2023）不同，后者通过蒸馏实现单步生成，而本文通过参数化改进提升多步采样质量。

## 总结

本文要解决的核心矛盾是UDM中训练目标与参数化最优解的错位，现有方法因忽略桥接非线性而未能识别这一错位。本文抓住的切入点是证明ELBO在桥接插件参数化下的最优解为LOO后验，并推导了精确转换公式。通过构建吸收态重构框架，本文实现了UDM与MDM的统一，证明了MDM优势源于参数化而非掩码机制。实验表明，LOO参数化在WikiText上将UDM PPL从37.44降至37.23，AUDM在WikiText上取得33.22，优于MDM的35.16。本文的边界在于未覆盖长序列场景，且LOO在PTB上的性能退化未得到解释。当序列长度增加时，LOO参数化的计算复杂度是否抵消并行优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22765)