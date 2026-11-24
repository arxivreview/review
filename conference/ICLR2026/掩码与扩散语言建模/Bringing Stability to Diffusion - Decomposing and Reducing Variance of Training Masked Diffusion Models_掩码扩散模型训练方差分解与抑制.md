# ICLR2026最新论文 ｜Bringing Stability to Diffusion: Decomposing and Reducing Variance of Training Masked Diffusion Models ｜掩码扩散模型训练方差分解与抑制

研究机构：英国剑桥大学、阿里巴巴集团

作者：Mengni Jia、Mengyu Zhou、Yihao Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18159)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18159)

> 掩码扩散模型（Masked Diffusion Models, MDMs）在预训练阶段与自回归模型（ARMs）性能相当，但在下游任务微调后往往大幅落后，且不同随机种子下的结果波动剧烈。现有缓解策略多为启发式或局限于特定优化场景，缺乏统一的理论解释。本文通过首次系统分解MDM训练方差来源，提出Pareto最优的掩码率采样策略（P-POTS）与互补采样机制（MIRROR），从根源上降低训练噪声。该工作填补了MDM训练稳定性的理论空白，但其效果高度依赖预训练模型的初始质量，且在长序列生成中的泛化边界尚待进一步验证。

## 研究背景

掩码扩散模型通过随机掩码输入token并学习重构来生成文本，其训练目标是对数似然下界（ELBO）的蒙特卡洛估计。由于掩码率 $t$ 和具体掩码模式 $x_t$ 的随机性，单次迭代的损失值波动极大。这种高方差导致梯度估计噪声大，优化过程不稳定，表现为跨运行结果差异显著（Across-run variability）以及单次运行内的次优收敛（Within-run sub-optimality）。相比之下，自回归模型仅受数据噪声影响，训练过程更为平滑且可预测。

MDM训练方差问题长期被视为“黑箱”现象，先前工作如Zhu et al. (2025)仅在偏好优化中通过固定时间步消除蒙特卡洛误差，Arriola et al. (2025)则采用启发式区间重拟合，均缺乏普适性。本文切入点在于从基础定义出发，建立首个系统性的方差分解框架，揭示MDM比ARM多出的两个噪声源：掩码模式噪声（Masking Pattern Noise）与掩码率噪声（Masking Rate Noise）。基于此理论，设计理论上最优的采样策略，旨在以最小计算成本实现训练稳定性的根本提升。

## 核心方法

### 方差分解与参照系

MDM标准训练流程中，掩码率 $t$ 通常从均匀分布 $U[0,1]$ 采样。本文指出，该过程引入了额外的方差来源。通过条件期望分解，MDM训练损失方差 $\text{Var}(l_\theta)$ 可表示为：

$$ \text{Var}(l_\theta) = \underbrace{\mathbb{E}_{x_0}[\text{Var}_{t,x_t}(l_\theta|x_0)]}_{A+B} + \underbrace{\text{Var}_{x_0}(\mathbb{E}_{t,x_t}(l_\theta|x_0))}_{C} $$

其中 $A$ 为掩码模式噪声，$B$ 为掩码率噪声，$C$ 为数据噪声。ARM仅受 $C$ 影响，而MDM的额外方差 $A+B$ 是训练不稳定的根源。

### P-POTS：Pareto最优掩码率采样

P-POTS（Parametric-Pareto Optimal Time-step Sampling）旨在最小化 $A+B+C$。设计动机在于均匀采样 $t$ 未考虑不同掩码率下的损失方差差异，导致高方差区域训练不足或噪声过大。P-POTS通过重要性采样，将 $t$ 的采样分布 $p(t)$ 设为与 $\sqrt{g(t)^2 + v(t)}$ 成正比，其中 $g(t)$ 和 $v(t)$ 分别为条件期望与方差。

$$ p^*(t) \propto \sqrt{g(t)^2 + v(t)} $$

该分布使训练聚焦于高方差区域（通常对应高 $t$ 值），同时通过权重 $1/p^*(t)$ 抑制其更新幅度，防止优化震荡。P-POTS在所有无偏采样器中实现Pareto最优，即无法在不增加其他方差源的情况下进一步降低总方差。

### MIRROR：互补掩码采样

MIRROR针对掩码模式噪声 $A$，构造两个互补的掩码输入 $x_t$ 和 $x_{1-t}$。设计动机在于单一掩码样本的随机性导致损失估计偏差，而互补样本具有负相关性，可抵消部分噪声。

$$ \hat{l}_{\text{MIRROR}} = \frac{1}{2} \left( l_\theta(x_0, t, x_t) + l_\theta(x_0, 1-t, x_{1-t}) \right) $$

通过联合使用 $t$ 和 $1-t$ 的掩码模式，MIRROR显式降低了 $A$ 的贡献。P-POTS与MIRROR具有强协同效应，前者优化采样分布，后者优化样本构造，二者结合在长响应数据集上效果尤为显著。

## 实验评估

实验在LLaDA-8B-Instruct和MMaDA-8B-MixCoT上进行，覆盖OpenScience、GSM8K、HiTab及text-to-image-2M数据集。基线包括Standard MDM、Clipped MDM及ARM（Qwen2.5-7B-Instruct等）。P-POTS+MIRROR在GSM8K上将准确率从50.6%-53.7%提升至58.6%-62.0%，HiTab从52.9%-62.6%提升至66.0%-68.6%，且运行间波动降至ARM水平。

| 方法 | GSM8K Avg | HiTab Avg | OpenScience Avg |
| :--- | :--- | :--- | :--- |
| Standard | 52.51 | 58.68 | 45.52 |
| P-POTS | 58.58 | 61.37 | 46.80 |
| MIRROR | 53.70 | 64.48 | 46.38 |
| P-POTS+MIRROR | 60.53 | 67.10 | 52.53 |

消融实验显示，P-POTS+MIRROR的增益超过单独使用之和，证实了协同效应。在text-to-image-2M上，CLIP score从28.61-34.28收窄至34.10-35.27，表明方法在多模态任务上的通用性。

评估边界方面，实验未报告计算开销增加的具体倍数，且P-POTS需预训练前估计 $g(t)$ 和 $v(t)$，增加了预处理步骤。代码未公开，超参数如EPR拟合的 $b=70$ 依赖经验规则，可复现性受限。

## 关联研究分析

从问题动机看，本文与Zhu et al. (2025)和Arriola et al. (2025)均关注MDM训练方差，但前者局限于偏好优化中的蒙特卡洛误差抵消，后者依赖启发式区间重拟合。本文通过理论分解提供普适框架，其差异根源在于是否将方差视为可分解的结构性问题而非局部噪声。Zhu et al.的方法无法推广至通用微调，而本文的P-POTS适用于任何基于ELBO的训练阶段。

从方法设计看，本文与Sahoo et al. (2024)的MDM训练目标一致，但后者未涉及方差优化。P-POTS的非均匀采样与Arriola et al.的自适应重拟合形成对比：前者基于理论最优分布，后者基于经验区间选择。P-POTS的Pareto最优性依赖于损失函数的二阶矩结构，若损失函数形式改变（如引入对比损失），其最优性是否保持，论文未给出回答。

## 总结

本文核心矛盾在于MDM训练方差导致微调后性能落后于ARM，且结果不稳定。切入点在于首次系统分解方差来源，揭示掩码模式与掩码率噪声的额外贡献。通过P-POTS和MIRROR，本文在GSM8K和HiTab上将准确率提升7-8%，并显著降低运行间波动。边界在于方法依赖预训练模型质量，且P-POTS的预估计步骤增加计算开销。当损失函数形式偏离标准ELBO时，P-POTS的Pareto最优性是否依然成立，论文未提供验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18159)