# ICLR2026最新论文 ｜BEYOND RAW DETECTION SCORES: MARKOV - INFORMED CALIBRATION FOR BOOSTING MACHINE GENERATED TEXT DETECTION ｜基于马尔可夫随机场校准的机器生成文本检测

研究机构：香港浸会大学、华南理工大学

作者：Chenwang Wu、Yiu-ming Cheung、Shuhai Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_49007174)

> 机器生成文本检测旨在区分人类写作与大语言模型（LLM）生成内容，核心挑战在于LLM采样随机性导致token级统计分数噪声大，传统直接聚合策略失效。本文切入点在于揭示并建模上下文token分数的邻域相似性与初始不稳定性，通过轻量级马尔可夫随机场（Markov Random Field, MRF）校准层修正分数偏差。该方法作为即插即用模块叠加于现有指标法检测器，无需重训底层模型。其价值在于以极小参数开销提升跨模型鲁棒性，但绝对性能仍低于监督学习SOTA，且对非token级输出方法不适用。

## 研究背景

理解本文需把握两个核心概念：token级检测分数与分布偏移。指标法检测器（如Log-Likelihood）依赖代理模型计算每个token的统计量作为分数，但LLM采样机制引入的随机性使这些分数偏离理论假设，产生高噪声。当检测器从训练模型迁移至未见模型时，这种噪声被放大，导致跨模型泛化能力急剧下降。

现有指标法检测路线面临根本瓶颈：尽管DetectGPT、DNA-GPT等方法通过引入扰动或再生成文本缓解单文本误差，但它们仍直接聚合token级分数，未修正底层分数的系统性偏差。模型法检测器虽在分布内精度更高，但易过拟合特定生成器，跨模型性能骤降。本文切入点在于识别出token分数间的结构性依赖关系——邻域相似性与初始不稳定性，并证明这些关系可被MRF建模以校准分数，从而在不改变底层特征提取逻辑的前提下提升检测精度。

## 核心方法

### 统一框架下的指标法局限

指标法检测器共享阈值判定机制，其有效性直接依赖token级分数的精度。Log-Likelihood、Log-Rank、Entropy仅使用原始文本，计算高效但易受采样随机性干扰；DetectGPT、Fast-DetectGPT、DNA-GPT引入辅助文本以降低方差，但计算开销增加。所有方法均直接聚合token分数，未修正单个token的偏差，导致最终检测分数不准确。

### 邻域相似性与初始不稳定性的理论揭示

本文通过简化Transformer模型推导Theorem 1，证明注意力分数在相邻步骤间存在正反馈循环，导致邻域token分数方差显著低于远距离token（邻域相似性）；同时，序列初始位置的分数波动幅度大，随位置推进逐渐稳定（初始不稳定性）。这一理论发现为分数校准提供了物理依据：相邻token分数应平滑过渡，初始token分数需降权处理。

### 马尔可夫随机场校准模块

基于上述性质，本文构建二元MRF模型，其中单节点势函数$\Psi_U(s_t, y_{s_t}) = -\log p(s_t)$反映原始检测器输出，成对势函数$\Psi_P(y_{s_t}, y_{s_j}) = -w \cdot \beta(t) \cdot I(y_{s_t} \neq y_{s_j})$惩罚相邻token标签不一致，$\beta(t)$为Sigmoid位置权重函数，抑制初始不稳定分数的影响。通过均值场近似，将MRF推理转化为轻量级迭代矩阵乘法：

$$Q^{[t+1]} = \text{Softmax}\left(-\log H + A_{corr} Q^{[t]} (W_{mrf} \odot \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix})\right)$$

其中$H$为原始分数矩阵，$A_{corr}$为加权邻接矩阵，$W_{mrf} \in \mathbb{R}^{2 \times 2}$为可学习参数。该公式通过迭代平滑token分数，使相邻分数趋近，同时降低初始位置权重，最终校准分数$Q^{final}$用于阈值判定。设计动机在于解决直接聚合策略对噪声分数的敏感性，通过结构化约束修正偏差，提升跨模型鲁棒性。

## 实验评估

实验在Essay、Reuters、DetectRL、TruthfulQA四个数据集上进行，覆盖跨LLM、跨域、混合文本及改写攻击场景。基线包括Log-Likelihood、Log-Rank、Entropy、DetectGPT、Fast-DetectGPT、DNA-GPT等指标法，以及RepreGuard、Binoculars、Lastde、FourierGPT等最新方法。本文方法（后缀-M/-E）作为校准层叠加于所有基线。

| 方法 | Essay AUROC (Avg) | DetectRL AUROC (Avg) |
| :--- | :--- | :--- |
| Likelihood | 96.17 | 72.20 |
| Likelihood-M | 97.79 | 80.84 |
| DetectGPT | 44.09 | 48.60 |
| DetectGPT-M | 91.95 | 72.95 |
| DNA-GPT | 95.26 | 67.79 |
| DNA-GPT-M | 98.07 | 69.75 |

在Essay数据集上，DNA-GPT-M达到98.07% AUROC，较基线95.26%提升2.81%；DetectGPT-M从44.09%跃升至91.95%，提升47.86%。在DetectRL上，Likelihood-M从72.20%提升至80.84%，提升8.64%。校准模块对低基线方法增益显著，对高基线方法增益递减。

消融实验表明，移除MRF层或位置权重函数均导致性能显著下降，证明两个组件均有效。在Back-Translation和DeepWordBug改写攻击下，校准方法仍保持优势，如DetectGPT-M在Back-Translation下从15.93%提升至54.20%。计算开销方面，校准模块引入的额外训练时间约1-2秒，推理时间增加约10-15秒，相对底层检测器可忽略。

评估边界方面，本文未对比SENTRA、GPTZero等监督学习SOTA，仅聚焦指标法内部改进。代码已开源，但超参数$T$（迭代次数）和$W_{mrf}$的敏感性分析未详细报告。

## 关联研究分析

从问题动机看，本文与DivEye、Binoculars等零样本统计检测方法同属指标法路线，但差异在于本文不提出新统计量，而是校准现有统计量。DivEye利用token多样性构建轻量分类器，Binoculars比较双模型对数似然差异，两者均直接聚合分数；本文通过MRF建模分数间依赖关系，修正聚合前的偏差。这一差异源于本文对token分数噪声来源的深入分析，而现有方法多关注特征设计而非分数校准。

从方法设计看，本文与FourierGPT、Lastde等局部模式学习方法不同。FourierGPT和Lastde提出独立的新指标，本文则是通用插件，不替换底层指标。本文的MRF校准基于注意力动力学理论推导，而FourierGPT基于频谱功率差异的经验观察。这种理论驱动的设计使本文方法更具可解释性，但也限制了其适用范围——仅适用于提供token级输出的检测器，无法用于文档级分类器。

## 总结

本文核心矛盾在于指标法检测器token级分数噪声大导致跨模型泛化不足。切入点在于揭示邻域相似性与初始不稳定性，通过MRF校准模块修正分数偏差。方法以2x2参数开销实现即插即用，在Essay数据集上DNA-GPT-M达98.07% AUROC，DetectGPT-M提升47.86%。边界在于仅适用于token级输出方法，且绝对性能低于监督学习SOTA。当检测器输出为文档级分数而非token级时，MRF校准是否仍有效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_49007174)