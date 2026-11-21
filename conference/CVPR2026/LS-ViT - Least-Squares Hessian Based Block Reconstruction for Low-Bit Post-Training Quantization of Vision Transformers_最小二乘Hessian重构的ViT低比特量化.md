# CVPR2026最新论文 ｜LS-ViT: Least-Squares Hessian Based Block Reconstruction for Low-Bit Post-Training Quantization of Vision Transformers ｜最小二乘Hessian重构的ViT低比特量化

研究机构：韩国首尔大学

作者：Hyunha Hwang、Xuan Truong Nguyen、Hyuk-Jae Lee

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e6849f8816a5)

> 视觉Transformer（ViT）在极低比特后训练量化（Post-Training Quantization, PTQ）中面临精度崩塌，根源在于现有二阶重构方法对Hessian矩阵的近似忽略了样本间协方差项。LS-ViT将Hessian估计重构为线性最小二乘问题，通过单次反向传播拟合全局最优Hessian，消除了独立假设带来的偏差。该方法在W2/A3配置下将Swin-B的Top-1准确率提升至67.73%，较基线FIMA-Q提升4.58个百分点，但其在W4/A4高比特下的增益微弱，且未验证动态场景下的鲁棒性。

## 研究背景

PTQ的核心在于利用少量校准数据优化量化参数，以最小化量化引入的任务损失增量。在基于泰勒展开的重构框架中，二阶Hessian项决定了参数扰动对损失的影响，是低比特下保持精度的关键。然而，计算完整Hessian矩阵的复杂度极高，迫使研究者采用对角近似或低秩近似。

现有主流路线如APHQ-ViT和FIMA-Q，通过假设样本间独立，将逐样本Hessian取平均以降低梯度方差。这一策略在W4/A4下有效，但在W2/A3等极低比特下，Hessian在样本间的剧烈波动（如Figure 2所示）使得独立假设失效，导致协方差项被忽略，近似误差显著增大。此外，FIMA-Q的低秩近似需多次全模型前向传播，计算开销大。LS-ViT的切入点在于：既然Hessian随样本变化，为何不直接寻找一个能最佳拟合所有样本梯度-扰动对的单一Hessian，而非简单平均？

## 核心方法

### 二阶重构参照系

基于QDrop基线的块级重构流程，通过最小化量化前后块输出的二阶差异来更新权重舍入与激活缩放。标准流程假设Hessian为样本无关常数或逐样本独立，本文差异在于将Hessian估计前置为独立的最小二乘优化步骤，而非在重构过程中隐式处理。

### 对角最小二乘Hessian估计

传统对角近似中，逐样本计算 $H_{i,i} = g_i / \Delta z_i$ 因 $\Delta z_i$ 极小导致数值不稳定。LS-ViT将问题转化为求解单一共享Hessian，最小化所有样本的残差平方和。设计动机在于消除逐样本估计的高方差，同时保留样本间相关性。

$$
\widehat{H}_{i,i} = \frac{\sum_{n=1}^{N} g_i^{(n)} \Delta z_i^{(n)}}{\sum_{n=1}^{N} (\Delta z_i^{(n)})^2}
$$

该公式通过加权平均梯度与扰动的乘积，隐式包含了协方差信息，使得估计值在低比特下更稳定。

### 低秩最小二乘Hessian估计

针对低秩近似，FIMA-Q假设样本独立导致协方差项缺失。LS-ViT将Hessian表示为秩1形式 $H = uu^\top$，并通过最小二乘求解向量 $u$。设计动机在于避免直接对 $u$ 的高阶项进行最小二乘带来的计算复杂性，转而利用标量内积关系。

$$
\widehat{u} = \frac{\sum_{n=1}^{N} g^{(n)} \sqrt{\Delta z^{(n)\top} g^{(n)}}}{\sum_{n=1}^{N} \Delta z^{(n)\top} g^{(n)}}
$$

此解法仅需一次反向传播获取所有样本的 $g$ 和 $\Delta z$，随后通过代数运算求解 $u$，大幅降低了相比FIMA-Q多次前向传播的计算成本，同时更准确地捕捉了Hessian的低秩结构。

## 实验评估

实验在ImageNet-1K分类、COCO检测与分割上进行，覆盖ViT、DeiT、Swin等架构。基线包括PTQ4ViT、GPTQ、FIMA-Q等，但缺失QAT类及正交变换类强基线。

| 模型 | 比特 (W/A) | FIMA-Q | LS-ViT | 提升 |
| :--- | :--- | :--- | :--- | :--- |
| Swin-B | 2/3 | 63.15 | 67.73 | +4.58 |
| Swin-S | 2/3 | 59.57 | 65.77 | +6.20 |
| ViT-S | 3/3 | 64.09 | 64.10 | +0.01 |
| DeiT-B | 2/4 | 73.32 | 73.78 | +0.46 |

在W2/A3极低比特下，LS-ViT在Swin系列模型上取得显著优势，平均提升2.89个百分点，验证了协方差项在分布高方差场景下的关键作用。而在W3/A3及以上，增益微乎其微（如ViT-S仅+0.01），表明高比特下独立假设的误差可忽略。

消融实验显示，逐样本估计 $g_i/\Delta z_i$ 在ViT-S上仅23.59%，而LS-ViT达到63.25%，证明简单除法在低比特下完全失效。训练时间方面，LS-ViT比FIMA-Q快1.8至2.7倍，得益于单次反向传播设计。

评估边界在于：未报告置信区间，且仅在静态校准集上验证。代码已开源，但超参数（如学习率4e-5/1e-3）未随模型规模自适应调整。

## 关联研究分析

从问题动机看，LS-ViT与SmoothQuant形成互补。SmoothQuant通过离线重参数化将激活离群值迁移至权重，解决的是分布非均匀性的一阶问题；而LS-ViT聚焦于二阶Hessian估计的统计偏差，解决的是重构过程中的近似误差。两者分别作用于量化前的分布治理与量化后的参数优化，但LS-ViT未处理激活离群值本身，若结合SmoothQuant可能进一步提升极低比特性能，论文未探索此组合。

从方法设计看，LS-ViT与GPTQ同属二阶重构范式，但GPTQ基于Hessian对角元素进行逐层误差补偿，假设Hessian局部常数；LS-ViT则通过最小二乘拟合全局Hessian，显式处理样本间变异。差异根源在于ViT的注意力机制导致Hessian在样本间波动远大于CNN，GPTQ的局部假设在ViT低比特下失效，而LS-ViT的全局拟合更适应这种高方差特性。

## 总结

LS-ViT旨在解决ViT低比特PTQ中Hessian近似忽略协方差项导致的精度损失。现有方法依赖样本独立假设，在极低比特下失效，而LS-ViT通过最小二乘拟合单一Hessian，以单次反向传播实现更优估计。实验证明其在W2/A3下Swin-B准确率提升4.58个百分点，但W4/A4下增益微弱。其边界在于静态校准假设，未验证动态输入分布下的鲁棒性。当校准集分布与测试集存在显著偏移时，最小二乘拟合的全局Hessian是否仍能保持最优，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e6849f8816a5)