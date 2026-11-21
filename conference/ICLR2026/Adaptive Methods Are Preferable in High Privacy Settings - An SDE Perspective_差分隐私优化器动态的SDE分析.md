# ICLR2026最新论文 ｜Adaptive Methods Are Preferable in High Privacy Settings: An SDE Perspective ｜差分隐私优化器动态的SDE分析

研究机构：瑞士巴塞尔大学、美国国家标准与技术研究院

作者：Enea Monzio Compagnoni、Alessandro Stanghellini、Rustem Islamov 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.03226)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03226)

> 差分隐私训练的核心矛盾在于隐私噪声方差随模型维度线性增长，导致高隐私预算下模型效用急剧下降。现有理论分析多聚焦于期望收敛或泛化界，未能揭示隐私噪声与优化器自适应机制之间的结构性交互，导致无法解释为何在相同隐私预算下，不同优化器的性能表现存在显著差异。本文通过随机微分方程（SDE）框架，首次量化了DP-SGD与DP-SignSGD在固定超参下的收敛速度及隐私-效用权衡对隐私预算 $\epsilon$ 的依赖关系。该工作为理解自适应优化器在隐私约束下的优势提供了动力学解释，但其理论结论主要基于线性模型与简单任务，向复杂深度网络的推广性尚存疑。

## 研究背景

差分隐私（Differential Privacy, DP）通过向梯度注入校准噪声来保证个体数据机密性，其核心机制是逐样本梯度裁剪与高斯噪声注入。然而，噪声幅度与模型维度成正比，导致高隐私预算（小 $\epsilon$）下信号被噪声淹没。为缓解此问题，研究者引入自适应优化器（如DP-Adam），利用二阶矩估计动态调整学习率，但DP噪声污染了矩估计，导致收敛行为偏离非隐私场景。

DP-SGD作为基准范式，其收敛性分析长期局限于期望收敛或高概率界，缺乏对优化轨迹动态特性的刻画。现有理论未能回答一个关键问题：隐私噪声如何结构性地改变自适应与非自适应优化器的收敛动力学？这一问题在超参数调优中尤为紧迫，因为DP-SGD的最优学习率对 $\epsilon$ 极度敏感，而自适应优化器是否具备天然的鲁棒性尚不明确。本文切入点在于利用SDE近似，将离散优化迭代映射为连续时间过程，从而隔离 $\epsilon$ 对收敛速度与平稳分布的影响，揭示自适应机制在隐私噪声下的内在优势。

## 核心方法

### SDE近似框架

本文采用Li et al. (2017)建立的SDE弱近似框架，将离散优化器迭代 $x_{k+1} = x_k - \eta \nabla f_{\gamma_k}(x_k)$ 映射为连续时间过程。对于DP-SGD，其SDE形式为：

$$
dX_t = -\nabla f(X_t)dt + \sqrt{\frac{2}{\eta}} \Sigma(X_t) dW_t
$$

其中 $\Sigma(X_t)$ 包含梯度噪声协方差与DP噪声项。该框架允许通过分析SDE的平稳分布与收敛速率，推导离散算法的渐近行为。与标准非隐私SDE分析不同，本文在噪声项中显式纳入逐样本裁剪后的DP噪声方差，从而捕捉隐私预算 $\epsilon$ 对动态的影响。

### 隐私预算对收敛速度的影响

在固定超参协议（Protocol A）下，本文推导了DP-SGD与DP-SignSGD的收敛速度及隐私-效用权衡。对于DP-SGD，收敛速度独立于 $\epsilon$，但隐私-效用权衡以 $O(1/\epsilon^2)$ 缩放：

$$
\mathbb{E}[f(X_T) - f^*] \lesssim \frac{L}{T} + \frac{C^2 \sigma_{DP}^2}{\epsilon^2}
$$

这表明DP-SGD的效用损失随 $\epsilon$ 减小呈平方增长。相比之下，DP-SignSGD的收敛速度线性依赖于 $\epsilon$，且隐私-效用权衡仅为 $O(1/\epsilon)$：

$$
\mathbb{E}[f(X_T) - f^*] \lesssim \frac{L}{T} + \frac{C \sigma_{DP}}{\epsilon}
$$

这一差异源于SignSGD的符号操作天然抑制了噪声幅度的累积，使其对隐私噪声的敏感度低于SGD。当批次噪声 $\sigma_\gamma^2$ 足够大时，DP-SignSGD始终优于DP-SGD；当批次噪声较小时，存在临界隐私水平 $\epsilon^\star$，使得 $\epsilon < \epsilon^\star$ 时自适应方法更优。

### 最优学习率的缩放律

在最优调参协议（Protocol B）下，本文推导了两种优化器的最优学习率缩放律。DP-SGD的最优学习率 $\eta^\star$ 与 $\epsilon$ 成正比：

$$
\eta^\star_{SGD} \propto \epsilon
$$

而DP-SignSGD的最优学习率与 $\epsilon$ 无关：

$$
\eta^\star_{SignSGD} \propto 1
$$

这一结果解释了为何自适应优化器在隐私训练中更具实用性：其超参数可跨不同隐私预算迁移，无需重新调优。相比之下，DP-SGD的学习率需随 $\epsilon$ 线性调整，若调参网格未覆盖“正确”值，性能将显著退化。该缩放律为隐私训练中的超参数选择提供了理论指导，降低了计算成本与隐私预算消耗。

## 实验评估

实验在Quadratic、IMDB和StackOverflow数据集上进行，验证理论预测的 $\epsilon$ 缩放律。基线包括DP-SGD、DP-SignSGD和DP-Adam，覆盖了非自适应与自适应两条路线，但缺失知识库中SOTA方法（如NoiseCurve、DP-AdamW-BC）的对比。

| 数据集 | 方法 | $\epsilon$ | 训练损失 |
| :--- | :--- | :--- | :--- |
| IMDB | DP-SGD | 1.0 | 0.75 |
| IMDB | DP-SignSGD | 1.0 | 0.70 |
| IMDB | DP-Adam | 1.0 | 0.70 |
| StackOverflow | DP-SGD | 1.0 | 3.8 |
| StackOverflow | DP-SignSGD | 1.0 | 3.6 |
| StackOverflow | DP-Adam | 1.0 | 3.6 |

在IMDB数据集上，当 $\epsilon=1.0$ 时，DP-SignSGD与DP-Adam的训练损失均为0.70，低于DP-SGD的0.75，验证了自适应方法在高隐私下的优势。在StackOverflow数据集上，DP-SignSGD与DP-Adam的损失为3.6，同样优于DP-SGD的3.8。这些结果与理论预测一致：DP-SGD的效用损失随 $\epsilon$ 减小呈平方增长，而自适应方法呈线性增长。

消融实验通过改变批次大小 $B$ 验证了批次噪声对临界隐私水平 $\epsilon^\star$ 的影响。当 $B$ 从48增加到80时，$\epsilon^\star$ 向左移动，表明批次噪声越大，DP-SignSGD在更宽松的隐私预算下仍具优势。这一发现与Theorem 4.5一致，即批次噪声主导时，自适应方法始终占优。

评估边界方面，实验仅使用线性模型（逻辑回归）与简单任务，未涉及深度神经网络。指标仅包含训练损失，未报告测试损失或泛化误差。代码基于Li et al. (2023)的DP2库，但未提供本文特定实验的超参数配置，可复现性受限。

## 关联研究分析

从问题动机看，本文与DP-AdamW-BC（Chooi et al., 2025）均关注自适应优化器在DP下的性能，但路径不同。DP-AdamW-BC通过偏差校正机制修复二阶矩估计的噪声污染，属于“修复”路线；本文则通过SDE分析揭示自适应机制本身对噪声的结构性鲁棒性，属于“解释”路线。前者提供工程解决方案，后者提供理论依据。本文的发现解释了为何DP-AdamW-BC在高隐私下优于DP-SGD：自适应机制天然抑制噪声累积，而偏差校正进一步消除了残余偏差。

从方法设计看，本文与NoiseCurve（Gu et al., 2025）形成互补。NoiseCurve通过曲率校正改善隐私-效用权衡，属于“增强”路线；本文则揭示了噪声与自适应机制交互的本质，为NoiseCurve的有效性提供了动力学解释。本文未直接采用噪声相关技术，而是通过SDE分析证明自适应方法在固定超参下具有 $O(1/\epsilon)$ 的权衡，而NoiseCurve的曲率校正可能进一步降低常数因子。两者结合，可能实现更优的隐私-效用平衡。

## 总结

本文核心矛盾是DP噪声方差随维度增长导致高隐私下效用下降，现有理论未能揭示自适应机制的结构性优势。本文通过SDE框架，首次量化了DP-SGD与DP-SignSGD在固定超参下的收敛速度与隐私-效用权衡对 $\epsilon$ 的依赖关系，证明DP-SGD的权衡为 $O(1/\epsilon^2)$，而DP-SignSGD为 $O(1/\epsilon)$。实验在IMDB与StackOverflow上验证了理论预测，显示自适应方法在 $\epsilon=1.0$ 时损失更低。本文边界在于仅分析线性模型与简单任务，未涉及深度神经网络，且未报告测试损失。当模型复杂度增加至Transformer规模时，SDE弱近似假设是否仍成立，以及自适应机制的鲁棒性是否被高维非凸景观削弱，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03226)