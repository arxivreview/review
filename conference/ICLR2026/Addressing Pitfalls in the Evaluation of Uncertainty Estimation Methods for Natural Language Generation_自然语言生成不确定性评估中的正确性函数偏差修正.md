# ICLR2026最新论文 ｜Addressing Pitfalls in the Evaluation of Uncertainty Estimation Methods for Natural Language Generation ｜自然语言生成不确定性评估中的正确性函数偏差修正

研究机构：奥地利林茨约翰·开普勒大学

作者：Mykyta Ielanskyi、Kajetan Schweighofer、Lukas Aichberger 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02279)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02279)

> 自然语言生成（NLG）不确定性估计旨在量化模型预测分布的熵以检测幻觉，但现有评估协议依赖近似正确性函数，导致方法排名受标签噪声扭曲。本文指出选择性预测（Selective Prediction）中未对正确性函数的随机性进行边际化是主要缺陷，提出混合判决边际化（SP-MoJI）与Elo评分聚合机制。该工作通过引入结构化任务与多模型集成，提升了评估的鲁棒性，但其结论仍受限于特定数据集与模型规模，未完全解决开放域泛化问题。

## 研究背景

当大语言模型（LLM）生成无事实支持的“虚构”（Confabulation）内容时，预测不确定性（Predictive Uncertainty）成为检测此类幻觉的关键信号。不确定性通常分解为偶然不确定性（Aleatoric Uncertainty，源于数据固有噪声）与认知不确定性（Epistemic Uncertainty，源于模型参数未知）。在NLG任务中，评估不确定性估计方法（UE Methods）的有效性依赖于“风险关联实验”（Risk Correlation Experiment），即计算不确定性分数与预测正确性之间的秩相关系数（如AUROC）。然而，NLG的正确性判定并非二元分类那样简单，而是依赖于近似正确性函数（Approximate Correctness Functions），如ROUGE、BLEU或LLM-as-a-Judge，这些函数本身具有参数依赖性与随机性。

现有研究普遍将QA数据集作为标准基准，假设正确性标签是固定的真值。然而，Santilli et al. (2024) 与 Zheng et al. (2023) 已指出LLM-as-a-Judge存在固有偏差，且不同近似函数间存在显著不一致。这种不一致性导致不确定性方法的排名随正确性函数的选择而剧烈波动，使得基于单一QA基准的SOTA结论缺乏稳健性。本文的切入点在于揭示这种“正确性黑客”（Correctness Hacking）现象：通过对抗性选择正确性函数，可以人为提升特定UE方法的表观性能。因此，研究重点从“构建更优的UE方法”转向“构建更鲁棒的评估协议”，以隔离方法贡献与评估噪声。

## 核心方法

### 风险关联实验与正确性偏差

传统NLG不确定性评估采用选择性预测（SP）协议，计算不确定性分数 $\hat{u}$ 与正确性指示器 $c$ 的AUROC。标准流程假设 $c$ 是确定性的，但在NLG中，$c$ 是参数化函数 $c(\mathbf{y}', \mathbf{y}, \mathbf{x}; \boldsymbol{\theta}_c)$，其输出受阈值 $d$ 与n-gram参数 $n$ 影响。本文指出，若不对 $c$ 的随机性进行边际化，标签中的伯努利噪声（Bernoulli Noise）会转化为样本依赖的偏差，导致AUROC估计量 $\xi_{SP}$ 出现系统性偏移。具体而言，独立噪声对所有方法影响均等，但正确性函数的偏差（Bias）会因方法对特定错误模式的敏感度不同而差异化影响排名。

### SP-MoJI：混合判决边际化

为消除近似正确性函数的随机性，本文提出选择性预测混合判决边际化（Selective Prediction using Mixture of Judges and Instructions, SP-MoJI）。该机制不再依赖单一LLM-as-a-Judge的输出，而是对多个不同模型（如Llama-3 405B, Qwen2.5）与提示词（QA/Gen prompt）的判决结果进行平均。其核心公式为：

$$ \xi_{SP-MoJI} = \mathbb{E}_{\boldsymbol{\theta}_c} \left[ \text{AUROC}(\hat{u}, c(\cdot; \boldsymbol{\theta}_c)) \right] $$

这一设计将正确性标签视为随机变量，通过外层期望（Outer Expectation）对判决模型的采样方差进行积分。与直接计算MoJI标签的AUROC（内层期望）不同，SP-MoJI在代数上等价于对不确定性分数与真实风险的相关性进行无偏估计，从而降低了因单一Judge模型偏好（如位置偏差）导致的排名失真。

### Elo评分聚合机制

针对跨数据集、跨模型评估结果难以直接比较的问题，本文引入Elo评分系统对UE方法进行全局排名。每个独立的数据集/模型组合被视为一场“对局”，方法A与方法B根据其在该对局中的AUROC高低决定胜负。Elo评分通过迭代更新收敛至平稳分布，其优势在于支持间接比较（Indirect Comparison），即使方法在部分任务上缺失数据，仍可通过传递性获得相对排名。该机制解决了传统表格中因高亮不同结果而导致的结论冲突问题，提供了单一标量化的客观性能总结。

## 实验评估

实验覆盖QA（CoQA, SQuAD, TriviaQA）、结构化任务（BigCodeBench, COLLIE）及OOD/扰动检测。基线包括语义熵（Semantic Entropy）、困惑度（Perplexity）、序列长度（Sequence Length）及P(True)等主流方法。模型涵盖Llama-3 8B/70B、Phi-3.5、Qwen2.5等。

| 方法 | 参考正确性函数 Top-3 频率 | 对抗性正确性函数 Top-3 频率 | 增幅 |
| :--- | :--- | :--- | :--- |
| Min Token Log-Probability | 0.125 | 0.500 | +0.375 |
| G-NLL | 0.375 | 0.688 | +0.312 |
| Perplexity | 0.125 | 0.444 | +0.319 |
| Semantic Entropy | 0.125 | 0.333 | +0.208 |

数据显示，Min Token Log-Probability在对抗性选择正确性函数时，Top-3频率从0.125激增至0.500，表明其性能高度依赖评估协议而非内在判别力。相比之下，Semantic Entropy的增幅为+0.208，虽也受协议影响，但相对稳定性略高。SP-MoJI实验表明，使用4个Judge模型可将性能估计的标准差降低约两倍，显著提升了评估的置信度。

消融分析显示，在结构化任务（如COLLIE）上，近似正确性函数与精确正确性（Exact Correctness）的排名相关性极低，仅当使用特定提示词的大模型（如Llama-3 405B）时，相关性才达到0.70以上。这证实了QA基准中近似函数的偏差在开放域生成中更为严重。Elo评分聚合结果进一步揭示，不同任务分区（QA vs. Code vs. OOD）下的最优方法不同，单一基准无法代表方法的全局效用。

评估边界方面，本文未报告单一方法的绝对AUROC SOTA，而是聚焦于排名稳定性。实验依赖Beam Search (n=10) 生成，计算资源约为600 GPU-hours。代码未公开，但SP-MoJI逻辑可基于现有API复现。主要局限在于结构化任务（代码/约束生成）的“精确正确性”可能过度简化了NLG的开放域特性，且未验证SP-MoJI在极小模型（<7B）上的边际收益。

## 关联研究分析

从问题动机看，本文与Kuhn et al. (2023) 的语义熵研究形成互补。语义熵通过聚类解决词法噪声导致的虚假不确定性，假设正确性标签是固定的；而本文指出，即使语义熵本身是鲁棒的，其评估结果仍受正确性函数偏差的污染。两者的差异根源在于任务特性：语义熵关注“如何估计不确定性”，本文关注“如何验证估计的有效性”。这种错位意味着，若正确性函数存在系统性偏差（如LLM-Judge对长答案的偏好），语义熵的SOTA结论可能在其他协议下失效。

从方法设计看，本文的SP-MoJI与传统的温度缩放（Temperature Scaling）或Platt Scaling不同。后者是后处理校准，旨在修正模型输出的概率分布；前者是评估协议修正，旨在修正标签的随机性。与Farquhar et al. (2024) 使用单一LLM-Judge相比，本文的多模型集成（MoJI）引入了额外的计算成本，但换取了标签方差的降低。然而，SP-MoJI是否掩盖了Judge模型本身的系统性偏差（如所有LLM共享的训练数据偏差），论文未给出回答。此外，Elo评分的引入借鉴了LLM竞技场（LMArena）的机制，但将其应用于UE方法排名，解决了跨域比较的难题，但其收敛性依赖于对局数量的充足性，在小样本场景下可能不稳定。

## 总结

本文要解决的核心矛盾是NLG不确定性评估中正确性函数的非确定性偏差对方法排名的系统性扭曲。现有方法如语义熵虽在判别力上表现优异，但其评估结论高度依赖近似正确性函数的选择，导致“正确性黑客”现象频发。本文通过SP-MoJI对判决模型进行边际化，并引入Elo评分进行跨域聚合，证明了评估协议的鲁棒性对方法比较至关重要。实验表明，Min Token Log-Probability的性能增幅（+0.375）远超语义熵（+0.208），揭示了部分方法的高排名源于协议偏差而非内在优势。本文的边界在于结构化任务可能无法完全代表开放域QA的复杂性，且SP-MoJI的计算成本随Judge数量线性增加。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02279)