# ICLR2026最新论文 ｜On the Benefits of Weight Normalization for Overparameterized Matrix Sensing ｜权重归一化在过参数化矩阵感知中的线性收敛理论

研究机构：瑞士苏黎世联邦理工学院

作者：Yudong Wei、Liang Zhang、Bingcong Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.01175)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01175)

> 过参数化矩阵感知旨在从线性测量中精确恢复低秩半正定矩阵，但标准梯度下降（GD）受限于子线性收敛下界，且过参数化往往导致收敛减速。本文切入点在于利用权重归一化（Weight Normalization, WN）将参数解耦为方向与幅度，从而重塑损失景观。通过引入黎曼梯度下降（RGD）优化Stiefel流形上的方向变量，本文证明了WN能实现线性收敛，并首次量化了过参数化水平对迭代复杂度的多项式加速效应。这一理论突破填补了WN在矩阵感知领域的空白，但其结论是否适用于非凸神经网络的实际训练动力学，仍存疑。

## 研究背景

低秩矩阵感知是信号处理与机器学习中的核心问题，其非凸损失景观充满鞍点，且缺乏全局平滑性。解决该问题的标准参数化方法是Burer-Monteiro分解，即将目标矩阵 $\mathbf{A}$ 表示为 $\mathbf{Y}\mathbf{Y}^\top$，其中 $\mathbf{Y} \in \mathbb{R}^{m \times r}$。当 $r > r_A$（$r_A$ 为 $\mathbf{A}$ 的秩）时，模型处于过参数化状态，这允许在未知真实秩的情况下实现精确恢复。然而，过参数化引入了优化挑战：已有研究（Xiong et al., 2024）证明，在无限样本下，随机初始化的GD收敛率存在 $\Omega(1/t)$ 的子线性下界，且过参数化程度越高，GD的收敛速度越慢，甚至可能陷入局部极小值或鞍点附近。

归一化层通常被视为稳定训练的手段，但其理论机制在简单问题上尚不清晰。权重归一化（WN）将参数分解为方向与幅度并分别优化，近期因与LoRA的无缝集成而在大语言模型微调中受到关注。然而，WN的理论支持主要局限于最小二乘问题的隐式正则化（Wu et al., 2020）或对角线性网络（Chou et al., 2024），缺乏对复杂非凸问题如矩阵感知的收敛性保证。本文旨在解决这一理论空白，探究WN如何改变过参数化矩阵感知的优化动力学，特别是它能否突破GD的子线性下界，并将过参数化从“减速因素”转化为“加速因素”。

## 核心方法

### 方法参照系

标准矩阵感知问题定义为从测量 $\{(\mathbf{M}_i, y_i)\}_{i=1}^n$ 中恢复 $\mathbf{A}$，其中 $y_i = \text{Tr}(\mathbf{M}_i^\top \mathbf{A})$。常规做法使用Burer-Monteiro分解 $\mathbf{Y}\mathbf{Y}^\top \approx \mathbf{A}$，并通过GD优化 $\mathbf{Y}$。本文的关键差异在于引入WN，将 $\mathbf{Y}$ 进一步分解为方向变量 $\mathbf{X}$ 和幅度变量 $\mathbf{\Theta}$，并将优化问题转化为在Stiefel流形上的黎曼优化问题。

### WN的矩阵扩展与黎曼优化

设计动机在于解决GD在过参数化下收敛缓慢且对初始化幅度敏感的问题。WN通过极分解将 $\mathbf{Y}$ 写为 $\mathbf{X}\tilde{\mathbf{\Theta}}$，其中 $\mathbf{X} \in \text{St}(m, r)$ 是Stiefel流形上的正交基（方向），$\tilde{\mathbf{\Theta}} \in S_r^+$ 是半正定矩阵（幅度）。为简化计算，本文将 $\tilde{\mathbf{\Theta}}\tilde{\mathbf{\Theta}}^\top$ 合并为对称矩阵 $\mathbf{\Theta} \in S_r$，并放松PSD约束仅为对称性，得到目标函数：

$$
f(\mathbf{X}, \mathbf{\Theta}) = \frac{1}{2n} \sum_{i=1}^n \left( \text{Tr}(\mathbf{M}_i^\top \mathbf{X}\mathbf{\Theta}\mathbf{X}^\top) - y_i \right)^2
$$

该公式将原非凸问题解耦为流形上的方向优化和欧氏空间上的幅度优化。对于方向变量 $\mathbf{X}$，由于约束 $\mathbf{X}^\top \mathbf{X} = \mathbf{I}_r$，本文采用黎曼梯度下降（RGD）。RGD将欧氏梯度投影到切空间，并通过极收缩（Polar Retraction）映射回流形：

$$
\mathbf{X}_{t+1} = (\mathbf{X}_t + \eta \mathbf{G}_t) (\mathbf{I}_r + \mathbf{G}_t^\top \mathbf{G}_t)^{-1/2}
$$

其中 $\mathbf{G}_t$ 是 $\mathbf{X}_t$ 的黎曼梯度，$\eta$ 是步长。对于幅度变量 $\mathbf{\Theta}$，使用标准GD更新 $\mathbf{\Theta}_{t+1} = \mathbf{\Theta}_t - \mu \mathbf{K}_t$。这种混合优化策略确保了 $\mathbf{X}$ 始终保持在流形上，而 $\mathbf{\Theta}$ 保持对称性，从而避免了GD中常见的范数爆炸或消失问题。

### 过参数化的加速效应

设计动机在于量化WN如何从过参数化中获益。本文证明，WN下的收敛行为分为两个阶段：初始阶段（Burn-in）和线性收敛阶段。在初始阶段，迭代从随机初始化移动到全局最优邻域，可能穿越鞍点；在线性收敛阶段，重建误差以指数速率衰减。关键发现是，过参数化水平 $r$ 的增加会多项式地降低迭代复杂度。设 $r = p r_A$ ($p > 1$)，Burn-in时间 $t_0$ 的上界为 $O(\kappa^4 m^2 p^8 / (p-1)^8 r_A^2)$，线性收敛率为 $\exp(-O(\kappa^4 m^2 p^2 t / r_A^4))$。这表明，与GD不同，WN下更高的过参数化水平 $p$ 直接导致更快的收敛速度和更低的样本复杂度，将过参数化转化为优化优势。

## 实验评估

实验在合成数据和真实图像重构任务上进行，验证WN-RGD的理论预测。基线包括标准GD（Stöger & Soltanolkotabi, 2021; Xiong et al., 2024），未对比其他归一化方法（如LN/BN），因为任务域为矩阵感知而非神经网络训练。

| 算法 | WN | 精确收敛 (E.C.) | 初始化要求 | 收敛率 | 过参数化加速 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GD (UB) (Stöger & Soltanolkotabi, 2021) | ✗ | ✗ | 小且随机 | 常数误差 (Early Stopping) | ✗ |
| GD (LB) (Xiong et al., 2024) | ✗ | ✓ | 小且随机 | $\Omega(\log(m r_A^2)/t)$ | ✗ |
| RGD (Theorem 3.2) | ✓ | ✓ | 随机 | $\exp(-O(\kappa^4 m^2 r^2 r_A t / (r-r_A)^4))$ | ✓ |

表格显示，WN-RGD实现了精确收敛（E.C.），且收敛率为指数级，显著优于GD的子线性下界。在合成数据实验中，当 $m=10, r=5, r_A=3$ 时，WN-RGD的平方重建误差随迭代次数呈线性下降（对数尺度），而GD收敛缓慢。在噪声测量实验中（$\xi = 10^{-1}, 10^{-3}, 10^{-5}$），WN-RGD在所有噪声水平下均保持线性收敛，最终误差稳定在 $O(\xi^2)$，而GD受限于其慢收敛率。图像重构实验（CIFAR-10马图像，$32 \times 32$）进一步验证了WN在真实数据上的有效性，RGD在相同迭代次数下重建质量优于GD。

消融实验表明，不同的收缩方法（Polar, Cayley, QR）在数值性能上几乎一致，说明结果对收缩选择鲁棒。全秩情况（$r=m$）下，收敛速度最快，因为初始 $\mathbf{X}_0$ 已对齐目标子空间，仅需优化幅度 $\mathbf{\Theta}$，这暗示学习方向比学习幅度更具挑战性。

评估边界方面，实验仅验证了理论收敛率，未报告计算时间或内存开销。代码未公开，但算法步骤清晰。样本复杂度依赖RIP假设，实际应用中需满足 $n = O(mr/\delta^2)$。

## 关联研究分析

从问题动机看，本文与DeepNorm（Li et al., 2024）同属通过归一化改善深层/复杂优化稳定性的策略，但DeepNorm针对Transformer激活值，旨在解决梯度爆炸，而本文针对参数归一化，旨在解决矩阵感知的鞍点逃逸。DeepNorm通过缩放残差连接保持Post-Norm稳定性，而WN通过流形约束重塑损失景观。两者的差异源于任务特性：Transformer训练关注前向/反向传播的数值稳定性，而矩阵感知关注非凸优化的全局收敛性。WN在矩阵感知中的成功是否意味着其在Transformer参数微调（如LoRA）中也能带来线性收敛优势，论文未给出回答。

从方法设计看，本文与SALU（Zaied, 2026）同属“免归一化”或“参数化重构”路线，但SALU用可学习激活函数替代归一化层以提升可塑性，而WN保留归一化结构并优化其几何性质。SALU在CIFAR-10上达到97.35%准确率，但依赖特定初始化；WN在矩阵感知中实现精确收敛，且对随机初始化鲁棒。差异根源在于：SALU关注表示学习的多样性，WN关注优化动力学的稳定性。WN的流形优化策略是否适用于SALU所处理的视觉分类任务，或反之，两者是否存在互补性，是未探索的盲区。

## 总结

本文核心矛盾是过参数化矩阵感知中GD的子线性收敛下界与精确恢复需求之间的冲突。现有方法无法突破该下界，且过参数化往往导致收敛减速。本文抓住WN的方向-幅度解耦特性，利用Stiefel流形上的RGD优化，证明了WN能实现线性收敛，并将过参数化转化为加速因素。核心数字显示，WN-RGD的收敛率为 $\exp(-O(\kappa^4 m^2 r^2 r_A t / (r-r_A)^4))$，显著优于GD的 $\Omega(\log(m r_A^2)/t)$。本文边界在于仅验证了矩阵感知这一特定问题，未涉及神经网络的实际训练动力学，且实验规模较小（$m \le 50$）。当矩阵维度 $m$ 增大到数千时，WN-RGD的计算开销是否仍具优势，以及其理论结论能否迁移至高维非线性网络，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01175)