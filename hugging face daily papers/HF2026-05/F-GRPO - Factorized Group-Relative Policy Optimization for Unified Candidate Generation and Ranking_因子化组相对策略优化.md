# HuggingFace最新推荐论文 ｜F-GRPO: Factorized Group-Relative Policy Optimization for Unified Candidate Generation and Ranking ｜因子化组相对策略优化

研究机构：Adobe研究院、美国加州大学圣迭戈分校

作者：Rohan Surana、Gagan Mundada、Junda Wu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.12995)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.12995)

> 传统检索-重排流水线将候选生成与排序解耦，导致下游效用优化受限于上游候选池的覆盖质量。现有 LLM 重排方法要么在固定候选集上直接排序，要么采用多模块独立优化，均无法端到端解决“选什么”与“怎么排”的耦合决策。本文提出 F-GRPO，在单次自回归生成中通过两阶段信用分配机制，将覆盖奖励与排序奖励解耦，使模型能同时优化候选集构建与列表排序。该方法在小模型上显著优于标准 GRPO 和监督微调，但仅在覆盖受限场景下增益明显，对排序主导型任务的提升有限。

## 研究背景

当 LLM 被用作重排器时，其输入通常是预检索的固定候选集，模型仅负责排序。然而，若上游检索遗漏了关键文档，下游排序无论多精准都无法弥补覆盖缺失。这一困境源于“列表到排序”（list-to-rank）问题的耦合性：系统需同时决定候选集内容（slate）及其排列顺序（permutation），而传统多阶段流水线将二者分离，各自优化代理目标，导致端到端效用无法最大化。

LLM 的生成能力为统一解决此问题提供了可能：模型可在单次自回归轨迹中先构建候选集再排序。但序列级奖励（如 NDCG）作用于完整输出，无法区分性能下降是源于候选集覆盖不足还是排序错误，造成信用分配模糊。标准 GRPO 将单一奖励均匀施加于所有 token，导致覆盖与排序的梯度信号相互干扰。本文切入点在于：将策略因子化为生成与排序两个阶段，并分别为其计算组相对优势，从而消除跨阶段梯度污染。

## 核心方法

### 因子化策略建模

本文将“列表到排序”问题形式化为因子化策略 $\pi_\theta(\tau, \sigma | x) = \pi_\theta[\text{slate}](\tau | x) \cdot \pi_\theta[\text{rank}](\sigma | x, \tau)$，其中 $\tau$ 为候选集，$\sigma$ 为排列。该设计动机在于打破固定候选池假设，使排序阶段能直接条件于生成的候选集，实现端到端优化。

### 两阶段信用分配

标准 GRPO 对每个 rollout 计算单一组相对优势 $\hat{A}_{\text{joint}}^{[i]} = \frac{R_{\text{joint}}^{[i]} - \bar{R}_{\text{joint}}}{\sigma_R}$，并均匀施加于所有 token。本文将其替换为两阶段独立优势：

$$
\hat{A}_{\text{slate}}^{[i]} = \frac{R_{\text{slate}}^{[i]} - \bar{R}_{\text{slate}}}{\sigma_{\text{slate}}}, \quad \hat{A}_{\text{rank}}^{[i]} = \frac{R_{\text{rank}}^{[i]} - \bar{R}_{\text{rank}}}{\sigma_{\text{rank}}}
$$

其中 $R_{\text{slate}}$ 为顺序无关的覆盖奖励，$R_{\text{rank}}$ 为位置敏感的排序奖励。该设计确保生成器仅从覆盖质量获得梯度，排序器仅从排序质量获得梯度，消除了标准 GRPO 中“高排序质量但低覆盖”被错误强化或“高覆盖但低排序”被错误惩罚的跨阶段梯度污染。

### 联合损失函数

总损失为 $L(\theta) = L_{\text{slate}} + \lambda L_{\text{rank}} + \beta_{\text{KL}} D_{\text{KL}}(\pi_\theta \| \pi_{\text{ref}})$，其中 $L_{\text{slate}}$ 和 $L_{\text{rank}}$ 分别使用 $\hat{A}_{\text{slate}}$ 和 $\hat{A}_{\text{rank}}$ 作为优势。该公式的物理含义是：在共享参数 $\theta$ 上，两个阶段的梯度信号被独立缩放，实现一阶可分离性，避免单一奖励导致的信号混淆。

## 实验评估

实验在 MovieLens、LastFM（序列推荐）和 HotpotQA、MuSiQue（多跳问答）上进行，使用 Qwen3-4B 和 Qwen3.5-2B 模型。基线覆盖零样本、监督微调（SFT）、解耦 SFT 和标准 GRPO，但缺失 MVP、E2Rank 等高效推理基线，也未与 RankGPT 等生成式重排器直接对比。

| 数据集 | 模型 | 方法 | Recall@3 | NDCG@3 |
| :--- | :--- | :--- | :--- | :--- |
| LastFM | Qwen3-4B | GRPO | 55.1 | 44.4 |
| LastFM | Qwen3-4B | F-GRPO | 73.9 | 53.6 |
| LastFM | Qwen3.5-2B | GRPO | 60.4 | 50.7 |
| LastFM | Qwen3.5-2B | F-GRPO | 71.3 | 61.1 |
| MuSiQue | Qwen3-4B | GRPO | 63.0 | 71.3 |
| MuSiQue | Qwen3-4B | F-GRPO | 71.3 | 78.5 |

F-GRPO 在 LastFM Recall@3 上较 GRPO 提升 18.8 个百分点，在 MuSiQue NDCG@3 上提升 7.2 个百分点。消融实验显示，F1 奖励在 k=3 时饱和，而召回奖励单调提升，表明覆盖奖励的设计对高 cutoff 性能至关重要。训练动态分析证实，生成器在 step 150 达到峰值召回的 90%，而排序器在 step 200 才达到峰值 NDCG 的 90%，验证了因子化策略中排序器依赖生成器的条件结构。

评估边界方面，论文未报告推理延迟，未提供置信区间，且仅在 2B-4B 小模型上验证，未探索更大规模模型下的效率。代码未公开，超参数细节仅在附录中部分披露，可复现性受限。

## 关联研究分析

从问题动机看，本文与 RankGPT 等生成式重排器的核心差异在于候选集来源。RankGPT 假设候选集由上游检索器提供，模型仅负责排序；而本文将候选集生成纳入优化范围，解决了“上游覆盖不足导致下游排序失效”的瓶颈。这一差异源于任务特性：在推荐和多跳问答中，候选集构建与排序的耦合性更强，固定候选池假设更易失效。

从方法设计看，本文与 CapCal 等去偏框架均关注偏差消除，但路径不同。CapCal 通过后处理校准消除位置偏差，而本文通过训练时因子化优化消除跨阶段梯度污染。前者是推理时干预，后者是训练时优化。本文未探索位置偏差问题，其因子化策略是否隐含位置偏差缓解效果，论文未给出回答。

## 总结

本文要解决的核心矛盾是 LLM 重排中候选生成与排序的耦合优化问题。现有方法要么固定候选池，要么解耦优化，均无法端到端最大化效用。本文通过因子化策略和两阶段信用分配，使模型能同时优化覆盖与排序。实验证明，在覆盖受限场景下，F-GRPO 较 GRPO 在 LastFM Recall@3 上提升 18.8 个百分点，在 MuSiQue NDCG@3 上提升 7.2 个百分点。但本文的边界在于：仅在 2B-4B 小模型上验证，未报告推理延迟，且增益在排序主导型任务（如 HotpotQA 4B 模型）上不显著。当候选集覆盖已足够高时，因子化信用分配的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.12995)