# ACL-Findings2026最新论文 ｜Bayesian Active Learning with Gaussian Processes Guided by LLM Relevance Scoring for Dense Passage Retrieval ｜贝叶斯主动学习引导的LLM密集段落检索

研究机构：韩国成均馆大学、加拿大多伦多大学

作者：Junyoung Kim、Anton Korikov、Jiazhou Liang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17906)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17906)

> 密集段落检索（Dense Passage Retrieval, DPR）面临LLM重排成本高且无法覆盖语义分散簇的困境。现有LLM重排范式被动依赖第一阶段候选集，导致召回率受限且信号无法传播。本文提出BAGEL框架，利用高斯过程（Gaussian Process, GP）在嵌入空间中主动探索以平衡探索与利用。该方法在固定预算下显著提升了检索性能，但其对GP平滑性假设与LLM离散打分兼容性的验证尚显不足。

## 研究背景

当LLM用于查询-段落相关性打分时，其零样本能力虽强，但计算成本禁止对大规模语料库进行穷举推理。这迫使检索任务被形式化为预算约束下的全局优化问题：在有限的LLM调用次数内，从海量搜索空间中识别相关段落。传统密集检索器基于向量相似度获取Top-K候选，但相关段落往往分布在嵌入空间中多个语义迥异的簇内，且可能远离查询嵌入的局部邻域，导致标准密集检索器无法检测这些全局结构。

主流LLM重排范式（如RankGPT）被动依赖第一阶段候选集，存在两大瓶颈：一是第一阶段检索器限制了召回上限，遗漏远端高相关簇；二是缺乏从已打分段落向未打分段落传播相关性信号的机制，忽视了嵌入空间中相邻段落相关性隐含的语义结构。BAGEL的切入点在于将检索视为主动学习过程，利用GP的内核机制传播稀疏LLM信号，并通过不确定性量化指导新段落的采样，从而突破局部邻域的限制。

## 核心方法

### 方法参照系

标准LLM重排流程为“密集检索Top-K -> LLM重排”，其核心局限在于候选集固定且无全局探索能力。BAGEL的关键差异在于引入GP代理模型，将静态重排转化为基于后验分布的迭代式主动采样过程，允许模型在预算内动态选择最具信息量的段落进行LLM打分。

### 查询特异性高斯过程建模

设计动机在于解决LLM信号稀疏且无法覆盖远端簇的问题。BAGEL为每个查询构建特异性GP，以密集嵌入为输入，LLM相关性得分为输出。GP通过核函数建模数据点间的相关性，实现相关性信号在嵌入空间中的插值与传播。

$$ f_q^{[LLM]}(\mathbf{x}_p) \sim \mathcal{GP}(0, k(\mathbf{x}_p, \mathbf{x}_q)) $$

该公式表明，查询-段落相关性函数被建模为均值为零、协方差由核函数决定的高斯过程。通过条件于已观测的LLM得分，GP能预测未观测段落的相关性均值与方差，从而在仅少量LLM调用的情况下推断全局相关性结构。

### 基于UCB的主动探索策略

设计动机在于平衡“利用”高置信度区域与“探索”高不确定性区域，避免陷入局部最优。在Warm-start初始化后，BAGEL使用上置信界（Upper Confidence Bound, UCB）获取函数迭代选择下一个待打分段落。

$$ a_t(\mathbf{x}_p) = \mu_q(\mathbf{x}_p) + \sqrt{\beta} \sigma_q(\mathbf{x}_p) $$

其中 $\mu_q$ 为GP预测均值，$\sigma_q$ 为预测标准差，$\beta$ 为平衡探索与利用的超参数。该公式通过最大化预测相关性加不确定性奖励，引导模型优先选择那些可能具有高相关性或当前认知模糊的段落，从而高效导航整个嵌入空间。

## 实验评估

实验在BEIR基准（Covid, NFCorpus, Robust04）及TravelDest数据集上进行，基线涵盖BM25、密集检索器、交叉编码器及Pointwise/Listwise LLM重排。BAGEL在固定预算50下，所有数据集均超越基线。

| Dataset | LLM | Method | N@50 | R@50 |
| :--- | :--- | :--- | :--- | :--- |
| TravelDest | GPT-4o | Point. LLM | 29.3 | 3.9 |
| TravelDest | GPT-4o | BAGEL | 41.6 | 6.9 |
| Robust04 | GPT-4o | Point. LLM | 45.9 | 24.9 |
| Robust04 | GPT-4o | BAGEL | 48.7 | 33.2 |

BAGEL在TravelDest上NDCG@50从29.3提升至41.6，Recall@50从3.9提升至6.9，表明其有效发现了密集检索器遗漏的远端相关段落。

消融实验显示，RBF核优于Linear核，证实了平滑核函数对多模态相关性结构的捕捉能力。在获取函数方面，UCB在多数数据集上表现最佳，但TS（Thompson Sampling）在NFCorpus上Recall@50达到29.0，略高于UCB的26.4，暗示不确定性量化策略需根据数据分布特性调整。

评估边界方面，论文未报告计算延迟与GPU资源消耗，仅以LLM调用次数为预算单位。代码已开源，但GP超参数（如长度尺度 $\ell$）的优化过程未详细披露，可能影响复现稳定性。

## 关联研究分析

从问题动机看，BAGEL与RE-GAR-AD均旨在降低LLM推理成本，但RE-GAR-AD侧重通过生成增强检索改善嵌入匹配质量，而BAGEL侧重通过主动学习优化采样策略。RE-GAR-AD假设检索质量取决于嵌入相似度，BAGEL则揭示在预算约束下，采样位置的策略性比嵌入本身的精度更关键。这一差异源于任务特性：RE-GAR-AD处理的是分类式关系抽取，而BAGEL处理的是排序式检索，后者对全局覆盖率的敏感度更高。

从方法设计看，BAGEL与Two-Stage APO均涉及两阶段优化，但Two-Stage APO的第二阶段是梯度引导的提示精炼，属于参数空间优化；BAGEL的第二阶段是GP引导的实例空间探索，属于数据空间优化。Two-Stage APO依赖提示空间的平滑性假设，BAGEL依赖嵌入空间的局部平滑性假设。当LLM打分呈现离散跳跃时，GP的平滑假设可能失效，而Two-Stage APO的梯度信号可能更直接地反映LLM的非线性行为。

## 总结

BAGEL解决了LLM重排中候选集固定与信号传播缺失的矛盾，通过GP主动学习在有限预算内实现全局探索。其核心贡献在于将检索问题转化为贝叶斯优化问题，利用不确定性量化平衡探索与利用。实验证明其在TravelDest等复杂数据集上显著优于Pointwise LLM基线。然而，GP的平滑性假设与LLM离散打分的兼容性未得到充分验证，且在NFCorpus上TS优于UCB的现象暗示单一获取函数可能不适配所有分布。当LLM相关性得分呈现高度非平滑分布时，GP后验的可靠性是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17906)