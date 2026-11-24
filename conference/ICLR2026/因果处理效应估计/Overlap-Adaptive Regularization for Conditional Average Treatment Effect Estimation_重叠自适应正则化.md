# ICLR2026最新论文 ｜Overlap-Adaptive Regularization for Conditional Average Treatment Effect Estimation ｜重叠自适应正则化

研究机构：德国慕尼黑大学

作者：Valentyn Melnychuk、Dennis Frauen、Jonas Schweisthal 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24962)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24962)

> 低重叠观测数据中，条件平均处理效应（CATE）估计器因反事实样本稀疏而失效，现有常值正则化无法区分高低重叠区域的异质性需求。本文提出重叠自适应正则化（Overlap-Adaptive Regularization, OAR），将正则化强度与局部重叠权重动态绑定，在低重叠区强制模型平滑，在高重叠区保留拟合灵活性。通过去偏版本保持Neyman正交性，OAR在77个ACIC 2016半合成实验中，76.62%的场景显著优于常值正则化。该方法解决了固定超参数无法适应协变量空间异质性的核心矛盾，但其性能高度依赖重叠权重的准确估计，在真实医疗数据中的鲁棒性尚待验证。

## 研究背景

当患者协变量分布导致治疗分配高度偏向某一组时，观测数据中该区域的反事实结果近乎缺失，这构成了低重叠性（Low Overlap）困境。低重叠性使得倾向得分（Propensity Score, $\pi(x)$）接近0或1，导致逆概率加权（IPW）方差爆炸，且第一阶段Nuisance函数（如结果模型 $\mu_a(x)$）的外推误差被放大。为缓解此问题，两阶段Neyman正交元学习器（如DR-learner）通过构造伪结果 $\phi(Z, \eta)$ 实现双重稳健性，但其第二阶段目标风险中的正则化项通常采用全局常数 $\lambda$，无法感知局部重叠程度的差异。

现有处理低重叠性的主流策略分为重定向（Retargeting）与常值正则化（Constant Regularization）。重定向通过截断或加权误差项将估计目标限制在重叠子群，但导致目标模型在低重叠区行为不可预测或收敛至加权平均处理效应（WATE）而非CATE；常值正则化虽能抑制整体异质性，却对高重叠区施加了不必要的约束，造成欠拟合，且对低重叠区的过拟合抑制不足。本文切入点在于将正则化机制从“全局固定”转变为“局部自适应”，直接利用重叠权重 $\nu(x) = \pi(x)(1-\pi(x))$ 作为正则化强度的输入，填补了元学习器在正则化项中显式利用重叠信息的空白。

## 核心方法

### 方法参照系

标准两阶段元学习器（如DR-learner）的第一阶段估计Nuisance函数 $\hat{\eta} = (\hat{\mu}_0, \hat{\mu}_1, \hat{\pi})$，第二阶段最小化目标风险 $L(g, \eta) = E + \Lambda$ 以拟合CATE模型 $g(x)$。本文问题与该通用流程的关键差异在于：传统正则化项 $\Lambda$ 仅依赖模型复杂度（如 $\|g\|_{\mathcal{H}}^2$），未引入对数据分布 $P(X, A)$ 中重叠结构的依赖，导致在低重叠区无法动态调整模型平滑度。

### 重叠自适应正则化框架

OAR的核心改动发生在第二阶段目标风险的正则化项 $\Lambda$ 中，将常数 $\lambda$ 替换为依赖重叠权重 $\nu(x)$ 的函数 $\lambda(\nu(x))$。设计动机是解决常值正则化在低重叠区“盲目”施加固定约束，导致过拟合（方差大）与欠拟合（偏差大）并存的问题。OAR定义正则化函数 $\lambda(\nu) \propto 1/\nu$，具体形式包括乘性 $\lambda_m(\nu(x)) = \frac{1}{4\nu(x)} - 1$、对数 $\lambda_{\log}(\nu(x)) = -\log(4\nu(x))$ 及平方乘性 $\lambda_{m2}(\nu(x)) = \frac{1}{16\nu(x)^2} - 1$。

$$
\Lambda_{\text{OAR}} = \Lambda(g; P(X, A); \lambda(\nu(X)))
$$

该公式表明，当 $\nu(x) \to 0$（低重叠）时，$\lambda(\nu) \to \infty$，正则化强度急剧增加，迫使模型 $g(x)$ 趋向常数（即ATE）；当 $\nu(x) \to 1/4$（完美重叠）时，$\lambda(\nu) \to 0$，正则化减弱，允许模型捕捉局部CATE异质性。这种机制将模型灵活性集中分配给重叠良好的子群体，而在治疗决策已高度确定的低重叠区保持保守估计，避免了反事实稀疏导致的噪声放大。

### 去偏OAR与Neyman正交性保持

原始OAR对重叠权重估计误差 $\hat{\nu}(x)$ 敏感，若 $\hat{\pi}$ 误设，正则化强度将偏离最优值。为保持Neyman正交性，本文提出去偏OAR（dOAR），通过一阶偏差校正项 $C_{\diamond}$ 消除 $\hat{\nu}$ 误差对目标风险的一阶影响。设计动机是确保在Nuisance函数误设下，估计量仍具一致性，这是元学习器鲁棒性的理论基石。

$$
L_{\text{dOAR}}^{\diamond}(g, \eta) = L_{\text{OAR}}^{\diamond}(g, \eta) + E_{\xi} [ C_{\diamond}(X; A; \xi; \nabla_{\xi} g; \eta) ]
$$

其中 $C_{\diamond}$ 包含高效影响函数（Efficient Influence Function） $\text{IF}(\lambda(\nu(x)); X, A)$，具体形式取决于OAR实例化（噪声正则化或Dropout）。以噪声正则化为例，$C_{+\xi} = -2w(X)(\mu_1(X) - \mu_0(X) - g(X+\xi)) \cdot \nabla_{\xi} g(X, \xi) \cdot \text{IF}(\lambda(\nu(x)); X, A)$。该校正项通过链式法则将正则化函数对 $\nu$ 的梯度与Nuisance函数的影响函数耦合，使得最终风险对 $\hat{\eta}$ 的一阶扰动不敏感，从而在保留自适应正则化优势的同时，继承了DR-learner等正交学习器的统计保证。

## 实验评估

实验基于ACIC 2016（77个半合成数据集）、HC-MNIST（高维图像数据）及IHDP数据集，基线涵盖Trimming、Balancing（MMD/WM）及常值正则化（CR）。对比方法未包含Causal Forests或Robust X-Learner，但覆盖了处理低重叠性的主要统计策略。在ACIC 2016实验中，dOAR（Dropout, $\lambda_{m2}$）在76.62%的数据集上显著优于CR（$\alpha=0.1$），而OAR（Noise reg, $\lambda_m$）在31.17%的数据集上显著优于CR，表明去偏版本在复杂分布下更具优势。

| 方法 | ACIC 2016 显著优于CR比例 (%) | HC-MNIST rPEHEout (DR-learner) |
| :--- | :--- | :--- |
| CR (const) | — | 0.743 ± 0.039 |
| OAR (Noise, $\lambda_m$) | 31.17 | 0.731 ± 0.035 |
| dOAR (Dropout, $\lambda_m$) | 70.13 | 0.712 ± 0.033 |
| dOAR (Dropout, $\lambda_{m2}$) | 76.62 | 0.705 ± 0.031 |

消融实验显示，正则化函数形式对性能影响显著：$\lambda_{m2}$（平方乘性）在低重叠区提供更强的正则化梯度，优于 $\lambda_m$ 和 $\lambda_{\log}$。在HC-MNIST上，dOAR（Dropout, $\lambda_m$）的rPEHEout为0.712，较CR降低0.031，接近Oracle值0.513。然而，在R-learner中，Balancing方法（$\alpha=5.0$）表现优于OAR，表明OAR的优势主要依赖于DR-learner的伪结果结构，而非普适于所有元学习器。

评估边界方面，实验仅使用半合成数据，缺乏真实医疗数据验证；指标聚焦rPEHEout，未报告置信区间或计算效率对比（除IHDP运行时间外）。代码已开源，超参数通过随机网格搜索确定，但重叠权重估计误差对dOAR性能的影响未进行敏感性分析。

## 关联研究分析

从问题动机看，OAR与Robust X-Learner（Uehara, 2026）均针对低重叠/重尾分布下的估计稳定性，但路径不同：Robust X-Learner通过鲁棒损失函数（如Huber）抑制极端值影响，属于误差项层面的修正；OAR则通过正则化项动态调整模型复杂度，属于结构层面的约束。Robust X-Learner在处理组极度不平衡时更直接，而OAR在重叠程度连续变化时提供更平滑的过渡。两者差异根源在于对“低重叠”的建模假设：前者假设异常值主导偏差，后者假设方差主导偏差。

从方法设计看，OAR与Causal Forests（Wager & Athey, 2018）的诚实分裂机制形成互补。Causal Forests通过数据划分解决过拟合，但正则化强度由树深度隐式决定，无法显式利用重叠信息；OAR则显式引入 $\nu(x)$，但依赖Nuisance函数的准确估计。Causal Forests在重叠良好时提供渐近有效置信区间，而OAR在低重叠区通过强正则化牺牲部分精度换取稳定性。若将OAR应用于Causal Forests的叶节点估计，是否能结合两者的优势，论文未给出回答。

## 总结

本文核心矛盾在于常值正则化无法适应协变量空间中重叠程度的异质性，导致低重叠区过拟合与高重叠区欠拟合并存。OAR通过 $\lambda(\nu) \propto 1/\nu$ 将正则化强度与局部重叠权重绑定，并在去偏版本中保持Neyman正交性，解决了固定超参数无法动态调整模型复杂度的问题。实验证明，dOAR在76.62%的ACIC 2016数据集上显著优于常值正则化，rPEHEout降低0.031。其边界在于性能高度依赖重叠权重 $\hat{\nu}(x)$ 的准确性，且在R-learner中优势不明显。当真实医疗数据中重叠权重估计存在系统性偏差时，dOAR的偏差校正项是否足以抵消正则化强度的误设，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24962)