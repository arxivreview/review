# ICLR2026最新论文 ｜TRANSFORMERS WITH ENDOGENOUS IN-CONTEXT - LEARNING: BIAS CHARACTERIZATION AND MITIGA TION ｜内生上下文学习：偏差刻画与双重去偏

研究机构：国防科技大学、清华大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66856410)

> 上下文学习（In-Context Learning, ICL）理论长期假设噪声外生，即标签噪声与输入特征独立，这一假设在真实数据中常被隐藏混杂因子（Hidden Confounders, HCs）打破。现有基于隐式梯度下降（Implicit Gradient Descent, GD）的解释框架无法量化这种内生性导致的系统性预测偏差。本文提出内生ICL（Endogenous ICL, EICL）设定，证明预训练Transformer的预测偏差与混杂强度成正比，并设计无梯度双重去偏（Double-Debiasing, DDbias）方法，仅用极少量无混杂样本即可修正冻结模型的预测。该工作填补了因果推断与ICL理论的空白，但其理论严格性依赖于线性注意力简化，非线性场景下的偏差比例关系是否依然成立尚存疑。

## 研究背景

理解ICL机制需先厘清隐式优化与因果充分性的关系。Transformer通过前向传播隐式执行GD，其收敛权重决定了预测结果。然而，这一等价性建立在因果充分性假设之上，即噪声 $\epsilon$ 与输入 $X$ 独立（$\epsilon \perp X$）。当存在隐藏混杂因子时，$\epsilon$ 同时影响 $X$ 和 $Y$，导致观测到的 $X-Y$ 关系包含虚假相关，传统OLS理论中的偏差推导无法直接迁移至基于注意力机制的ICL场景，因为注意力参数 $K, Q, V$ 的交互动态缺乏闭式解。

主流ICL理论如 Von Oswald et al. (2023) 和 Ahn et al. (2023) 均假设数据生成过程无混杂，从而得出Transformer可实现无偏GD的结论。这一假设在合成线性回归中成立，但在真实世界任务（如在线评论预测）中，混杂因子普遍存在，导致模型继承系统性偏差。Liang et al. (2024) 虽指出此问题并引入工具变量（Instrumental Variables, IV）去偏，但IV方法依赖有效工具变量的存在，且在弱工具或无效工具场景下失效。本文切入点在于：不依赖外部工具变量，仅利用少量无混杂提示样本，通过纯前向传播修正预训练偏差，实现无梯度去偏。

## 核心方法

### 方法参照系

本文基于线性注意力Transformer的隐式GD框架，参照 Von Oswald et al. (2023) 的预训练动态分析。关键差异在于数据生成过程：标准框架假设 $\epsilon \perp X$，本文允许 $\epsilon \not\perp X$，定义混杂强度 $r_j = E[X_j \epsilon]$，并分析其对注意力参数收敛及下游预测的影响。

### 无偏注意力权重构造

为量化偏差，首先需定义“无偏”的参考参数。在混杂存在时，直接求解OLS无偏估计不可行，本文构造特定注意力参数 $\mathbf{S}_u, \mathbf{T}_u$，使得诱导的元权重 $\mathbf{w}_u$ 能实现无偏预测。

$$
\hat{y}_{(n+1)} = \langle \mathbf{x}_{(n+1)}, \mathbf{w}_u \rangle, \quad \mathbf{w}_u \leftarrow \mathbf{w}_u - \eta \nabla_{\mathbf{w}} \frac{1}{n} \sum_{i=1}^n (\mathbf{w}^\top \mathbf{x}_{(i)} - \mathbf{w}_\star^\top \mathbf{x}_{(i)})^2
$$

该公式表明，通过特定参数配置，Transformer的前向传播等价于对真实参数 $\mathbf{w}_\star$ 的梯度下降，从而在混杂数据上仍能得到无偏预测。这一构造解决了此前方法无法定义“无偏基准”的问题，为偏差量化提供了参照系。

### 偏差刻画与双重去偏

预训练在混杂数据上收敛的权重 $\mathbf{S}_b, \mathbf{T}_b$ 会偏离无偏权重 $\mathbf{S}_u, \mathbf{T}_u$。Theorem 1 证明偏差与混杂强度 $r_j$ 成正比。基于此，DDbias 方法通过两次提示实现去偏：第一次提示获取有偏预测 $\hat{y}_b$，第二次提示使用残差 $y - \hat{y}_b$ 作为标签。

$$
\mathbf{w}_{DEB}^{(l+1)} = \mathbf{w}_{DEB}^{(l)} - \eta \nabla_{\mathbf{w}} \frac{1}{n_b} \sum_{i=1}^{n_b} (y_{rc(i)} - \hat{y}_{b(i)} - \mathbf{w}^\top \mathbf{x}_{rc(i)})^2
$$

该公式表明，第二次提示隐式执行了对残差的GD，从而抵消了预训练引入的偏差。设计动机在于避免IV方法对工具变量的依赖，仅利用少量无混杂样本即可修正冻结模型，且对部分混杂样本具有鲁棒性。

## 实验评估

实验在合成线性/非线性回归及Yelp情感数据集上进行，基线包括Vanilla TF、IV方法（Liang et al., 2024）及传统OLS。在Yelp RPI任务上，DDbias (60 ICL) 达到16.7的预测误差，优于Vanilla LLaMA的23.8和DMCEE的21.2。

| 方法 | RPI 误差 | ROR 误差 |
| :--- | :--- | :--- |
| Vanilla LLaMA | 23.8 | 0.46 |
| DMCEE | 21.2 | 0.28 |
| DDbias (60 ICL) | 16.7 | 0.16 |

消融实验显示，DDbias 对提示样本比例敏感。在弱混杂（Conf@0.10）下，样本比例从 $1.6 \times 10^{-3}$ 增至 $6.4 \times 10^{-3}$，预测误差从0.090降至0.080，边际收益递减。在混合样本（$\rho=0.5$）下，误差从0.290降至0.235，表明方法对部分混杂具有鲁棒性，但强混杂下效果减弱。

| 混杂强度 | 样本比例 ($\times 10^{-3}$) | 预测误差 |
| :--- | :--- | :--- |
| Conf@0.10 | 1.6 | 0.090 |
| Conf@0.10 | 6.4 | 0.080 |
| Conf@0.50 | 1.6 | 0.182 |
| Conf@0.50 | 6.4 | 0.167 |

评估边界方面，理论分析基于线性注意力，实验虽扩展至Softmax非线性架构，但未提供大规模LLM（如GPT-3）上的验证。代码未公开，超参数（如混杂强度 $r_j$ 的分布）依赖合成数据设定，真实数据中的混杂结构未知，限制了可复现性。

## 关联研究分析

从问题动机看，本文与 Liang et al. (2024) 的IV方法同属因果去偏路线，但DDbias 不依赖工具变量，而是利用无混杂样本的残差修正。IV方法在有效工具下表现优异（如L=3时误差0.102），但在弱工具（Corr(Z, $\epsilon$)=0.1）下误差飙升至0.423，而DDbias 保持0.090。这一差异源于IV对工具外生性的强依赖，而DDbias 仅需少量无混杂样本，更适合工具变量不可得的场景。

从方法设计看，本文与 Von Oswald et al. (2023) 的隐式GD框架同属“ICL即优化”路线，但本文挑战了其外生性假设。Von Oswald 证明线性注意力可实现无偏GD，本文则证明在混杂下，GD收敛至有偏解，偏差与 $r_j$ 成正比。这一差异揭示了隐式GD框架的边界：其无偏性依赖于数据生成过程的因果充分性，而非模型架构本身。

## 总结

本文核心矛盾在于ICL理论的外生性假设与真实数据内生性的冲突。切入点在于利用注意力参数的动态特性，构造无偏基准并量化偏差，进而通过残差提示实现无梯度去偏。DDbias 在Yelp RPI任务上将误差从23.8降至16.7，证明了少量无混杂样本的有效性。边界在于理论严格性依赖线性注意力简化，非线性场景下的偏差比例关系未获严格证明，且缺乏大规模LLM验证。当混杂强度超过2.0时，DDbias 的误差是否仍显著低于Vanilla TF，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66856410)