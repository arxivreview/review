# CVPR2026最新论文 ｜DBMSolver: A Training-free Diffusion Bridge Sampler for High-Quality Image-to-Image Translation ｜扩散桥采样器

研究机构：韩国首尔大学

作者：Sankarshana Venugopal、Mohammad Mostafavi、Jonghyun Choi

论文原文见 [arXiv](https://arxiv.org/abs/2605.05889)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05889)

> 图像到图像（I2I）翻译任务中，扩散桥模型（DBM）虽能处理非高斯先验，但采样过程需数十次函数评估，导致推理延迟高企。现有加速方案或依赖蒸馏重训，或采用数值近似，均存在训练开销大或精度损失问题。本文通过解析推导DBM底层SDE/ODE的半线性结构，提出无训练解析求解器DBMSolver，将采样步数压缩至6次。该方法在多个I2I基准上实现了效率与质量的双重提升，但其优势在复杂语义任务中是否依然成立，仍需进一步验证。

## 研究背景

扩散模型从噪声生成图像（N2I）时，假设先验分布为高斯噪声。然而，I2I翻译任务要求从一张具体图像（非高斯分布）映射到另一张图像，这一先验假设失效导致传统N2I求解器（如DDIM）在I2I任务中理论无效。为了解决这一问题，扩散桥模型（DBM）通过Doob's h-transform构建连接两个任意分布的“桥”，但其反向去噪过程涉及复杂的条件概率项，使得采样过程变得极其缓慢。

当前I2I翻译的主流加速路线分为两类：一是基于蒸馏的方法（如CDBM、IBMD），通过训练小模型来拟合大模型的多步轨迹，虽然能实现1-2步生成，但需要额外的训练开销且存在训练-推理不一致风险；二是基于数值优化的方法（如Hybrid Heun、DBIM），通过改进ODE/SDE求解器来减少步数，但多采用线性多步法或低阶近似，在低步数下精度下降明显。本文的切入点在于，DBM的SDE和ODE具有被忽视的半线性结构，可以通过指数积分器（EI）获得解析解，从而在不引入任何训练成本的前提下，实现高阶、高精度的少步采样。

## 核心方法

### 方法参照系

DBM的采样过程由Bridge SDE和Bridge PF ODE共同描述。传统求解器（如Hybrid Heun）交替使用Euler-Maruyama和Heun方法，属于数值近似。本文的关键差异在于，不再依赖数值迭代，而是直接推导SDE/ODE的解析解，利用其半线性特性消除线性项的离散化误差。

### 半线性结构解析

DBM的Bridge SDE和ODE在形式上表现为关于状态变量 $x_t$ 的线性项与非线性得分项的叠加。这种半线性结构允许使用指数积分器（EI）精确求解线性部分。对于Bridge SDE，通过泰勒展开EI解，得到一阶近似解：

$$
\tilde{x}_t = \frac{\alpha_t}{\alpha_s} x_s + \frac{\sigma_t^2 - \alpha_t^2 \sigma_s^2}{\alpha_s^2} \nabla_{x_s} \log p_t(x_s|x_T) \Delta t + \sigma_t z_t
$$

该公式表明，状态更新由线性缩放、条件得分引导和噪声项组成，其中线性项通过EI精确处理，避免了Euler-Maruyama方法在长步长下的累积误差。

### 高阶ODE求解

Bridge PF ODE同样具有半线性结构。通过变量替换 $\lambda_t = \log(\alpha_t/\sigma_t)$，将ODE转化为指数加权积分形式。对积分项进行二阶泰勒展开，得到二阶解析解：

$$
\tilde{x}_t = e^{\lambda_t - \lambda_s} x_s + \int_{\lambda_s}^{\lambda_t} e^{\lambda_t - \lambda} \left( D_\theta(x_\lambda) + \frac{d D_\theta}{d \lambda}(x_\lambda) (\lambda - \lambda_s) \right) d\lambda
$$

这一设计解决了DBIM等线性多步法在低NFE下精度不足的问题。通过解析处理指数权重，DBMSolver在6次函数评估内即可达到Hybrid Heun 119次评估的生成质量，且无需任何模型重训。

## 实验评估

实验在Edges2Handbags (E2H)、DIODE、Face2Comics、CelebAMask-HQ和ImageNet Inpainting五个数据集上进行，基线包括Hybrid Heun、DBIM-1/2/3、ODES3以及蒸馏方法CDBM/IBMD。

| 数据集 | 方法 | NFE | FID |
| :--- | :--- | :--- | :--- |
| DIODE (256×256) | Hybrid Heun | 119 | 4.43 |
| DIODE (256×256) | DBMSolver | 6 | 3.38 |
| DIODE (256×256) | DBMSolver | 20 | 2.06 |
| E2H (64×64) | Hybrid Heun | 119 | 1.83 |
| E2H (64×64) | DBMSolver | 6 | 0.93 |
| E2H (64×64) | DBMSolver | 20 | 0.53 |

在DIODE数据集上，DBMSolver在6 NFE时FID为3.38，优于Hybrid Heun在119 NFE时的4.43；在20 NFE时FID降至2.06，显著优于DBIM-2的4.40。E2H数据集上，DBMSolver 6 NFE的FID 0.93也大幅领先于Hybrid Heun的1.83。

| 数据集 | 方法 | NFE | FID |
| :--- | :--- | :--- | :--- |
| Face2Comics (256×256) | Hybrid Heun | 119 | 2.36 |
| Face2Comics (256×256) | DBMSolver | 20 | 0.96 |
| CelebAMask-HQ (256×256) | DBIM-1 | 6 | 44.92 |
| CelebAMask-HQ (256×256) | DBMSolver | 6 | 34.76 |
| ImageNet Inpainting (256×256) | DBIM-1 | 20 | 4.13 |
| ImageNet Inpainting (256×256) | DBMSolver | 6 | 4.98 |

在Face2Comics上，DBMSolver 20 NFE的FID 0.96远优于Hybrid Heun 119 NFE的2.36。CelebAMask-HQ上，6 NFE时DBMSolver FID 34.76优于DBIM-1的44.92。然而，在ImageNet Inpainting任务中，DBMSolver 6 NFE的FID 4.98略高于DBIM-1 20 NFE的4.13，表明在复杂语义填充任务中，少步采样的质量优势有所减弱。

评估协议主要依赖FID和NFE，未报告置信区间。代码已开源，但论文未提供不同GPU架构下的延迟对比，且ImageNet Inpainting的基线复现基于官方代码，可能存在实现差异。

## 关联研究分析

从问题动机看，DBMSolver与蒸馏方法（如CDBM）的根本差异在于是否引入训练开销。蒸馏方法通过训练小模型来近似多步轨迹，虽然能实现1-2步生成，但需要额外的训练数据和计算资源，且存在训练-推理不一致的风险。DBMSolver则完全基于解析推导，无需任何重训，直接利用预训练DBM的权重。这种差异源于任务特性：I2I任务的先验分布非高斯，使得蒸馏过程中的轨迹对齐更加复杂，而解析求解则规避了这一难题。

从方法设计看，DBMSolver与N2I求解器（如DPMSolver++）的关键差异在于对先验分布的假设。DPMSolver++假设先验为高斯分布，因此在I2I任务中理论无效。DBMSolver通过推导Bridge SDE/ODE的半线性结构，显式处理了非高斯先验带来的条件概率项。这一设计解决了N2I求解器在I2I任务中失效的问题，但论文未探讨该解析解在更复杂条件生成任务（如文本引导）中的适用性，半线性结构是否在所有DBM参数化下均成立，仍需进一步验证。

## 总结

DBMSolver旨在解决I2I翻译中DBM采样慢且现有加速方法训练开销大的矛盾。其切入点在于发现DBM SDE/ODE的半线性结构，通过指数积分器推导解析解，避免了数值近似的误差累积。该方法在DIODE和E2H等数据集上，以6次函数评估实现了优于119次评估基线的生成质量（FID 3.38 vs 4.43）。然而，在ImageNet Inpainting等复杂语义任务中，其少步采样的质量优势减弱（6 NFE FID 4.98 vs DBIM 20 NFE FID 4.13）。当任务涉及更复杂的语义组合时，解析求解的精度是否仍能保持优势，论文未给出明确答案。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05889)