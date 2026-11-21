# ICLR2026最新论文 ｜FAST-DIPS: Adjoint-Free Analytic Steps and Hard-Constrained Likelihood Correction for Diffusion-Prior Inverse Problems ｜无伴随算子的硬约束扩散逆问题求解

作者：Minwoo Kim、Seunghyeok Shin、Hongki Lim

论文原文见 [arXiv](https://arxiv.org/abs/2603.01591)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01591)

> 训练免费扩散先验逆问题求解面临非线性算子下数据一致性强制的高计算成本，传统方法依赖手工伴随算子或长迭代内环，导致推理时间不可控。本文切入点在于将软惩罚似然替换为硬约束可行性球，并通过无伴随算子的ADMM分裂与解析步长实现固定预算修正。该方法在保持重建质量接近SOTA的前提下，实现了最高19.5倍的速度提升，但其仅输出MAP点估计的局限削弱了扩散模型在不确定性量化上的理论优势。

## 研究背景

逆问题求解的核心困境在于前向算子 $A$ 的病态性，导致从观测 $y$ 恢复信号 $x$ 需要强先验约束。扩散模型作为学习式先验，通过反向时间SDE引导采样轨迹满足测量约束，确立了“训练免费”的求解范式。然而，当 $A$ 为非线性或无闭式伴随算子时，数据一致性步骤通常退化为多次梯度下降或MCMC内环，每次迭代需调用去噪器与算子导数，计算开销随噪声级别线性累积。

现有主流路线在效率与鲁棒性间存在显著权衡。DPS等梯度引导方法依赖Tweedie公式近似似然梯度，在低噪声级别稳定性差且需可微性；PnP-ADMM框架虽引入分裂优化，但将去噪器视为近端算子，缺乏对测量空间硬约束的显式处理。本文针对非线性算子下“伴随算子不可得”与“内环迭代次数不可控”两大瓶颈，提出以硬约束投影替代软惩罚，以解析步长替代固定学习率，旨在将每级修正的计算量压缩至常数级。

## 核心方法

### 方法参照系

本文基于解耦重退火（Decoupled Re-annealing）框架，该框架将扩散采样分解为去噪锚点计算、似然修正与噪声注入三步。与标准DPS使用软惩罚 $\lambda\|Ax-y\|^2$ 不同，本文核心差异在于将似然项建模为测量空间可行性球的指示函数，并通过ADMM分裂求解硬约束优化问题。

### 硬约束可行性修正

传统方法在非线性算子下需手工推导伴随算子 $A^*$ 或执行长梯度内环，导致计算成本不可控。本文引入辅助变量 $v \approx A(x)$，将问题转化为带约束的ADMM分裂形式。其核心创新在于 $v$-更新采用闭式欧几里得投影，$x$-更新采用解析步长的最速下降，避免了内环MCMC与手工伴随算子。

$$
\min_{x, v} \frac{1}{2\sigma_t^2} \|x - x_{0|t}\|^2 + \iota_C(v) \quad \text{s.t.} \quad v = A(x)
$$

该公式将去噪器预测 $x_{0|t}$ 作为局部高斯先验中心，$\iota_C(v)$ 为可行性球 $C = \{v : \|v-y\| \le \epsilon\}$ 的指示函数，强制测量残差在预算 $\epsilon$ 内。

### 无伴随算子解析步长

ADMM的 $x$-更新通常需计算 $A(x)$ 的雅可比矩阵或其伴随，但在自动微分框架中，直接计算高维雅可比内存开销巨大。本文利用局部二次模型最小化推导解析步长 $\alpha^*$，仅需一次VJP（向量-雅可比积）与一次JVP（雅可比-向量积）或前向差分探针，无需显式构造雅可比矩阵。

$$
\alpha^* = \frac{\|g\|^2}{\|J_A(x)^\top g\|^2 + \rho \|J_A(x) g\|^2}
$$

该步长公式通过最小化局部二次近似目标函数获得，结合Armijo回溯线搜索保证下降性，将每级修正的算子调用次数固定为常数，消除了对算子可微性结构的依赖。

## 实验评估

实验在FFHQ与ImageNet数据集上评估8个线性与非线性逆问题任务，基线覆盖DAPS、SITCOM、HRDIS等主流训练免费方法，但未包含盲反演专用基线如PRISM，因本文侧重可微非线性算子。

| 任务 | 方法 | PSNR (dB) | Run-time (s) |
| :--- | :--- | :--- | :--- |
| Gaussian Deblurring (FFHQ) | FAST-DIPS | 29.406 | 2.612 |
| Gaussian Deblurring (FFHQ) | HRDIS | 30.455 | 21.591 |
| Motion Deblurring (FFHQ) | FAST-DIPS | 31.736 | 2.616 |
| Motion Deblurring (FFHQ) | SITCOM | 31.172 | 36.684 |
| Phase Retrieval (FFHQ) | FAST-DIPS | 29.253 | 10.354 |
| Phase Retrieval (FFHQ) | DAPS | 30.253 | 122.100 |

FAST-DIPS在Gaussian Deblurring中PSNR低于HRDIS约1.05 dB，但运行时间缩短至1/8；在Motion Deblurring中PSNR超越SITCOM 0.56 dB，速度提升14倍。Phase Retrieval任务中，FAST-DIPS PSNR低于DAPS 1.0 dB，但速度提升11.8倍，表明硬约束对非线性相位信息的拟合存在精度损失。

消融实验显示，增加ADMM内环迭代次数 $K$ 可单调提升PSNR，但边际收益递减；像素-潜空间混合调度中，早期像素修正节省解码器反向传播成本，后期潜空间修正保持流形保真，单一空间执行均导致质量或速度显著下降。

评估指标仅包含PSNR/SSIM/LPIPS，缺乏后验分布校准性指标，无法验证不确定性量化能力。代码未公开，超参数 $\epsilon$ 与 $\rho$ 的敏感性分析未在正文中详细展开，可复现性依赖附录细节。

## 关联研究分析

从问题动机看，FAST-DIPS与DAPS同属解耦重退火框架，但DAPS依赖迭代梯度下降求解软惩罚目标，而FAST-DIPS采用硬约束投影。这一差异源于对噪声方差 $\beta$ 鲁棒性的不同假设：DAPS需精确校准 $\beta$ 以设定惩罚权重 $\lambda$，而FAST-DIPS通过可行性球 $\epsilon$ 提供显式残差预算，在 $\beta$ 未知时更具鲁棒性，但牺牲了似然函数的平滑性，导致Phase Retrieval等强非线性任务精度略降。

从方法设计看，FAST-DIPS借鉴PnP-ADMM的分裂思想，但将去噪器从近端算子降级为锚点。PnP-ADMM假设去噪器是正则化项的近端映射，而FAST-DIPS仅将其作为局部高斯先验中心，通过ADMM分裂显式处理数据一致性。这一设计解耦了先验建模与数据保真，使得方法可适用于任意非线性算子，但引入了额外的分裂变量 $v$ 与对偶变量 $u$，增加了内存开销，且硬约束在噪声方差未知时 $\epsilon$ 的选取缺乏理论指导。

## 总结

FAST-DIPS针对训练免费扩散逆问题中非线性算子下计算效率与算子可微性的矛盾，通过硬约束可行性球与无伴随算子ADMM分裂，将每级修正计算量压缩至常数级。该方法在FFHQ Gaussian Deblurring中实现2.612秒运行时间，较HRDIS的21.591秒提升8.3倍，同时在Motion Deblurring中超越SITCOM 0.56 dB PSNR。其边界在于仅输出MAP点估计，未利用扩散模型的多模态采样能力，且硬约束在强非线性任务中精度略降。当噪声方差 $\beta$ 未知时，可行性球半径 $\epsilon$ 的自适应选取策略是否影响后验分布的校准性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01591)