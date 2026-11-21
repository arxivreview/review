# WACV2026最新论文 ｜ENCORE: A Neural Collapse Perspective on Out-of-Distribution Detection in Deep Neural Networks ｜基于神经坍缩的能量分数改进

研究机构：美国东北大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_26766719)

> 分布外检测（Out-of-Distribution Detection, OOD）旨在识别训练分布之外的样本，以消除模型对未见数据的高置信度错误预测。现有后验方法多依赖经验性特征统计，缺乏对深度神经网络（DNN）内在几何属性的理论连接，导致在模型校准不佳时失效。本文切入点在于利用训练末期涌现的神经坍缩（Neural Collapse, NC）现象，通过自适应特征缩放修正能量分数。该方法无需重训练即可提升近邻 OOD 检测性能，但其效果高度依赖 NC 假设的近似成立，在长尾分布下的鲁棒性尚存疑。

## 研究背景

当 DNN 面对未见类别时，其输出层往往给出高置信度预测，这种过度自信源于训练过程中决策边界的激进扩张。为量化这种不确定性，能量分数（Energy Score）利用 Log-Sum-Exp 形式计算 logits 的标量值，成为广泛采用的后验检测基线。然而，当模型校准不佳或 logits 异常偏高时，能量分数仍可能赋予 OOD 样本低能量（即高置信度），暴露出其在边界区域的失效。

后验 OOD 检测的主流路线包括基于置信度的 MSP 和基于特征空间的距离度量。MSP 仅利用最大概率，丢弃其余类别信息；特征方法虽考察内部表示，但多依赖经验性阈值或马氏距离，缺乏对 DNN 训练动态的理论解释。这种理论与方法的脱节使得难以 pinpoint 检测器失效的具体条件。本文切入点在于引入神经坍缩理论，该理论描述了 DNN 训练末期类特征与权重形成的对称几何结构，为理解能量分数在 ID 与 OOD 输入上的行为差异提供了新的理论视角。

## 核心方法

### 方法参照系

本文问题属于后验检测中的能量分数改进路线。标准流程直接利用预训练模型的 logits 计算能量分数，本文的关键差异在于不直接修改 logits，而是通过调整中间层特征的几何属性（范数与角度）来重构 logits，从而间接修正能量分数。

### 神经坍缩下的能量间隙分析

设计动机在于解释为何简单特征缩放能提升 ID/OOD 分离度。在完美神经坍缩假设下，ID 特征坍缩至类均值，OOD 特征正交于类均值空间。本文推导表明，ID 与 OOD 的能量间隙 $\Delta E$ 随类均值范数 $r$ 的增加而增大。具体而言，当 $\alpha r^2$ 足够大时，间隙简化为与 $r$ 成正比的项。这意味着，通过增加特征范数，可以放大 ID 与 OOD 在能量空间中的距离，从而提升检测性能。

$$
\Delta E \approx \alpha r^2 - \alpha r \cos(\theta_{ood})
$$

该公式表明，能量间隙主要由特征范数的平方项主导，验证了特征缩放的有效性。

### 自适应余弦 Logit 与缩放机制

设计动机在于解决实际 DNN 未完全收敛导致 NC 假设失效的问题。本文提出 ENCORE，首先利用余弦相似度替代原始 logits，以消除范数依赖并隔离角度信息。随后，引入自适应缩放因子 $\kappa$，其值取决于特征向量在 ID 主子空间上的投影范数与总范数之比。最终能量分数定义为：

$$
S(x) = -\log \left( \sum_{c=1}^{C} \exp(\kappa \cos(\theta_c)) \right)
$$

其中 $\kappa = \exp(\lambda \frac{\|x_p\|}{\|x\|})$。该机制通过衰减弱对齐 ID 特征的影响，增强了 OOD 样本的能量值，从而在无需重训练的情况下实现了更鲁棒的 ID/OOD 分离。

## 实验评估

实验基于 OpenOOD 基准，涵盖 CIFAR-10 与 ImageNet，指标为 FPR95 与 AUROC。基线覆盖 MSP、Energy、ViM、KNN 等经典后验方法，但缺失训练时正则化方法（如 GCOS）及扩散模型方法（如 SCOPED）的直接对比。在 CIFAR-10 ResNet-18 上，ENCORE 在 Near-OOD 的 FPR95 为 36.27%，AUROC 为 91.23%；在 Far-OOD 的 FPR95 为 21.11%，AUROC 为 94.56%。

| 方法 | Near-OOD FPR ↓ | Near-OOD AUROC ↑ | Far-OOD FPR ↓ | Far-OOD AUROC ↑ |
| :--- | :--- | :--- | :--- | :--- |
| MSP | 53.61 | 87.69 | 31.22 | 91.03 |
| Energy | 46.04 | 86.79 | 24.31 | 92.46 |
| ViM | 39.42 | 88.73 | 23.73 | 93.13 |
| ENCORE | 36.27 | 91.23 | 21.11 | 94.56 |

ENCORE 在 Near-OOD 上比 Energy 降低 9.77% FPR，在 Far-OOD 上比 ViM 降低 2.62% FPR，验证了特征缩放对近邻检测的显著增益。

消融实验显示，仅使用余弦相似度效果最弱，仅使用范数缩放有显著提升，二者结合达到最佳性能。在 ImageNet ViT-Huge 上，结合策略的 Near-OOD FPR 为 43.55%，Far-OOD FPR 为 14.62%。

| 组件 | Near-OOD FPR ↓ | Near-OOD AUROC ↑ | Far-OOD FPR ↓ | Far-OOD AUROC ↑ |
| :--- | :--- | :--- | :--- | :--- |
| Only Norm Scaling | 59.68 | 85.15 | 37.76 | 90.37 |
| Only Cosine Similarity | 79.27 | 73.88 | 60.85 | 78.32 |
| Combined | 43.55 | 89.47 | 14.62 | 96.89 |

评估边界方面，论文未报告置信区间，且未对比最新几何专用方法（如 GEODE）。代码已开源，超参数 $\lambda$ 在 0-11 范围内稳定，最优值约为 3。

## 关联研究分析

从方法设计看，ENCORE 与 ViM 均利用主特征空间，但 ViM 关注空空间能量，ENCORE 关注主空间内的几何对齐。ViM 将空空间能量作为额外 logit，而 ENCORE 利用主空间投影比例自适应缩放 logit。这种差异源于对神经坍缩不同属性的利用：ViM 依赖特征正交性，ENCORE 依赖特征范数与角度的联合约束。ENCORE 在 CIFAR-10 Near-OOD 上比 ViM 降低 3.15% FPR，表明主空间几何对齐比空空间能量更能捕捉近邻偏移。

从理论根基看，ENCORE 与 GEODE 同源于神经坍缩理论，但 GEODE 侧重边界区分度的几何分析，ENCORE 侧重能量分数的理论修正。GEODE 在 Near-OOD 上取得 95.02% AUROC，高于 ENCORE 的 89.47%（ImageNet ViT-Huge）。这一差距可能源于 GEODE 对长尾分布的显式建模，而 ENCORE 依赖 NC 假设的近似成立，在类别不平衡场景下可能失效。

## 总结

本文核心矛盾在于能量分数在模型校准不佳时的过度自信问题。切入点在于利用神经坍缩理论揭示特征范数与能量间隙的正相关关系，从而通过自适应缩放修正 logits。ENCORE 通过余弦相似度与投影范数缩放重构能量分数，在 CIFAR-10 Near-OOD 上实现 36.27% FPR，在 ImageNet Far-OOD 上实现 14.62% FPR。其边界在于依赖 NC 假设的近似成立，且在 ImageNet Near-OOD 上 AUROC 低于 GEODE。当训练数据存在严重长尾分布时，NC 假设的对称性被破坏，ENCORE 的自适应缩放机制是否仍能维持有效的 ID/OOD 分离，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_26766719)