# ICLR2026最新论文 ｜In-Context Learning of Temporal Point Processes with Foundation Inference Models ｜基于基础推断模型的时序点过程上下文学习

研究机构：德国波恩大学

作者：David Berghaus、Patrick Seifner、Kostadin Cvejoski 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24762)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24762)

> 标记时序点过程（Marked Temporal Point Process, MTPP）的建模长期受困于“单数据集拟合”范式，每个新场景均需从头训练，导致模型无法跨域泛化。现有神经架构虽提升了单域精度，但缺乏对事件动力学机制的通用先验，难以实现零样本推断。本文提出FIM-PP，通过在随机化合成MTPP先验上预训练Transformer，使模型能从上下文序列中直接推断条件强度函数。该工作验证了合成数据预训练在事件序列推断中的可行性，但其在标记不平衡与分布偏移下的鲁棒性仍存疑。

## 研究背景

理解本文需厘清条件强度函数（Conditional Intensity Function, CIF）与基础推断模型（Foundation Inference Model, FIM）的关联。CIF定义了给定历史下事件发生的瞬时速率，是MTPP概率建模的核心。传统方法通过最大似然估计拟合CIF，但依赖数值积分且无法迁移。FIM范式则直接估计动力学系统的微分算子，保留可解释性并支持上下文学习。将FIM引入MTPP，意味着不再拟合特定数据集的似然，而是学习从事件上下文到CIF参数的映射，从而实现对未知动力学的零样本推断。

MTPP领域的主流路线分为参数化核扩展与生成式采样。Hawkes过程及其神经变体（如NHP、THP）通过线性或注意力机制捕捉历史依赖，但每个数据集需独立训练，且自回归采样存在误差累积。扩散模型（如CDiff）尝试通过联合分布建模突破顺序依赖，但计算开销大且缺乏对底层动力学机制的显式估计。本文切入点在于：利用合成数据构建覆盖多种动力学机制（兴奋、抑制、中性）的MTPP先验，训练模型从上下文推断CIF，而非直接预测事件序列。

## 核心方法

### 方法参照系

本文问题属于时序点过程推断，但区别于传统“单数据集似然拟合”，其目标是“跨数据集动力学机制推断”。标准流程为：编码历史→估计CIF→薄化采样。本文差异在于：CIF参数由预训练网络从上下文序列推断，而非由单数据集训练得到。

### 合成先验构建

设计动机：解决传统方法缺乏通用动力学先验、无法跨域泛化的问题。本文定义CIF分布：

$$ \lambda(t, \kappa | H_t) = \mu_\kappa(t) + \sum_{\kappa' \in K} \gamma_{\kappa\kappa'}(t - t') $$

其中 $\mu_\kappa(t)$ 为基线强度（常数、正弦、Gamma分布），$\gamma_{\kappa\kappa'}$ 为交互核（指数、Rayleigh分布），交互类型 $z_{\kappa\kappa'} \in \{-1, 0, 1\}$ 随机采样。该公式通过随机化基线、核函数与交互类型，构建覆盖兴奋、抑制、中性动力学的MTPP先验，使预训练模型能学习通用动力学机制。

### 上下文推断架构

设计动机：解决传统方法需单数据集训练、无法零样本推断的问题。FIM-PP采用Transformer编码器-解码器结构：

$$ \hat{\lambda}(t, \kappa | H_t) = \text{softplus}(\Phi([h_t^{hist}, \phi_\kappa(\kappa')])) $$

其中 $h_t^{hist}$ 为历史事件嵌入（查询），上下文序列嵌入（键值）经Transformer解码器融合，$\phi_\kappa(\kappa')$ 为标记嵌入。该公式将历史与上下文信息融合，输出非负CIF参数（$\mu, \alpha, \beta$），直接推断条件强度，无需单数据集训练。

## 实验评估

实验在TAXI、StackOverflow、Amazon、Retweet、Taobao数据集上评估，基线覆盖NHP、THP、CDiff等强度与生成式方法，但缺失最新时空模型（如GLIDE）与流匹配方法（如SurF）。

| 方法 | TAXI OTD | TAXI sMAPE | StackOverflow OTD | StackOverflow sMAPE |
| :--- | :--- | :--- | :--- | :--- |
| CDiff | 21.01±0.16 | 88.0±0.2 | 41.25±1.40 | 106.18±0.34 |
| FIM-PP(zs) | 23.15±0.07 | 76.8±0.4 | 49.26±0.06 | 96.36±0.05 |
| FIM-PP(f) | 17.91±0.12 | 76.8±0.5 | 39.80±0.04 | 88.25±0.19 |

FIM-PP(zs)在sMAPE上优于CDiff，但OTD略逊；微调后FIM-PP(f)在OTD与sMAPE上均领先，验证了预训练+微调范式的有效性。

消融实验显示，零样本模式下FIM-PP在TAXI标记预测Acc仅0.41，微调后升至0.69；在Taobao上零样本Acc仅0.09，微调后0.39。这表明合成先验对标记不平衡与特定模式（如TAXI双标记交替、Taobao单标记主导）覆盖不足，微调是弥补分布偏移的关键。

评估边界：指标覆盖OTD、sMAPE、RMSE、Acc，但缺乏置信区间报告；代码开源（fim4science.github.io），但预训练数据规模与超参数细节未完全披露，可复现性依赖附录补充。

## 关联研究分析

从问题动机看，FIM-PP与CDiff同属MTPP预测，但路线迥异：CDiff通过扩散模型直接采样事件序列，FIM-PP通过推断CIF参数再薄化采样。差异根源在于任务特性：CDiff适合长程多模态生成，FIM-PP适合需概率校准与动力学解释的场景。FIM-PP保留Hawkes结构，符合“结构化神经内核”观点，而CDiff为黑盒生成，可解释性弱。

从方法设计看，FIM-PP与NHP/THP同属强度推断，但预训练范式不同：NHP/THP单数据集训练，FIM-PP合成数据预训练。差异根源在于泛化需求：NHP/THP依赖单域数据拟合，FIM-PP依赖合成先验覆盖动力学机制。FIM-PP的上下文学习机制使其能零样本推断，但合成先验的覆盖范围是否足以支撑真实数据的分布偏移，论文未给出量化边界。

## 总结

FIM-PP要解决的核心矛盾是MTPP建模的“单数据集拟合”与“跨域泛化”需求。其切入点在于：利用合成数据构建覆盖多种动力学机制的MTPP先验，训练模型从上下文推断CIF参数，而非直接预测事件序列。本文通过Transformer架构实现上下文学习，证明了零样本推断在事件序列中的可行性。核心数字：FIM-PP(f)在TAXI OTD 17.91、StackOverflow OTD 39.80，优于CDiff基线。边界在于：合成先验对标记不平衡与特定模式覆盖不足，零样本标记预测Acc低（TAXI 0.41、Taobao 0.09），依赖微调弥补。当合成先验的交互类型分布与真实数据标记分布出现系统性偏差时，零样本推断的鲁棒性边界如何量化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24762)