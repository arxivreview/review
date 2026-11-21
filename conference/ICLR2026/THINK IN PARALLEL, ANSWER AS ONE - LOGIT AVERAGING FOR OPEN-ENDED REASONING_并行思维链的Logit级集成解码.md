# ICLR2026最新论文 ｜THINK IN PARALLEL, ANSWER AS ONE: LOGIT AVERAGING FOR OPEN-ENDED REASONING ｜并行思维链的Logit级集成解码

研究机构：新加坡国立大学

作者：Haonan Wang、Chao Du、Kenji Kawaguchi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10471075)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段计算量提升大语言模型（LLM）性能，但主流并行采样方法依赖答案级多数投票，在代码生成等无唯一标准答案的开放域任务中失效。本文切入点在于将聚合粒度从完整输出下沉至Token级别，通过平均多条思维链的预Softmax Logits生成单一连贯答案。该免训练策略在LiveCodeBench Hard子集上使DeepCoder-14B-Preview的Pass@1提升8.28%，但在低置信度场景下Logit平均是否放大错误仍存疑。

## 研究背景

当LLM面对复杂推理任务时，单条思维链（Chain-of-Thought, CoT）常因早期错误累积导致最终答案偏差，而增加推理长度又引发过度思考（Overthinking）现象，造成算力浪费。为突破单路径局限，并行采样通过生成多条独立推理轨迹来增加计算广度，利用多样性降低随机误差。然而，现有并行扩展方法主要依赖答案级聚合，如Self-Consistency采用多数投票机制，这要求任务存在离散且唯一的正确答案。

在数学竞赛或选择题等封闭域任务中，多数投票能有效过滤噪声，但在代码生成、深度研究等开放域任务中，有效输出极少重复，"投票"在语义上定义不明。这一缺口阻碍了并行测试时计算在真实世界工作负载中的应用。本文针对此问题，提出在答案生成阶段对多条思维链的Token级Logits进行集成，从而在无唯一标准答案的场景下实现并行推理的收益转化。

## 核心方法

### 方法参照系

标准并行采样流程包含轨迹生成与答案聚合两阶段，通常采用Best-of-N或多数投票在完整输出层面进行选择。本文的关键差异在于摒弃答案级选择，将聚合操作前移至答案解码的每个自回归步骤，直接在Logit空间融合多条推理路径的信息。

### 多样化思维链生成

设计动机在于解决单条CoT路径探索空间有限的问题。给定问题 $Q$，模型以较高温度（如0.5-0.7）采样 $K$ 条独立思维链 $R_1, \dots, R_K$，直至遇到分隔符（如 `</think>`）。此阶段保持各路径完全独立，利用采样随机性探索不同解题视角，无需任何微调，直接复用模型自身分布。

### Logit级集成解码

设计动机在于解决开放域任务中答案级投票定义不明的问题。在分隔符之后，模型进入答案生成阶段。在每个自回归步骤 $i$，对于每条思维链上下文，计算下一Token的预Softmax Logits向量 $\mathbf{z}_i^{[k]} = M_\theta(Q, R_k, y_{<i}) \in \mathbb{R}^{|V|}$。随后，对所有 $K$ 条链的Logits进行算术平均，再应用Softmax得到聚合概率分布：

$$ P_{\bar{}}(y_i) = \text{softmax}\left( \frac{1}{K} \sum_{k=1}^{K} \mathbf{z}_i^{[k]} \right) $$

该公式的物理含义是，在决策每个Token时，模型同时参考了 $K$ 种不同推理路径的预测倾向，通过Logit空间的线性融合实现"并行思考，统一发声"。选定的Token被注入所有 $K$ 个上下文，确保后续预测基于共同的局部答案前缀，从而生成单一连贯的最终输出。

## 实验评估

实验在AIME 2025、GPQA Diamond（封闭域）及LiveCodeBench、GAIA、Xbench-DeepSearch（开放域）上进行，基线包括多数投票（MV）及其变体，但缺乏过程奖励模型（PRM）引导的搜索方法对比。

| 模型 | 任务 | K | MV | ThinkMerge (Direct) | ThinkMerge (Shortest-K) |
|---|---|---|---|---|---|
| Qwen3-14B | AIME'25 | 8 | 74.0 | 78.0 | 80.0 |
| R1-Distill-Qwen-7B | AIME'25 | 2 | 40.7 | 41.3 | 50.7 |
| DeepCoder-14B-Preview | LiveCodeBench | 2 | 55.32 | 58.36 | 61.09 |
| WebSailor-7B | Xbench-DeepSearch | 4 | 37.80 | 48.00 | 47.20 |

在封闭域任务上，ThinkMerge在Qwen3-14B上达到80.0%，略高于MV的74.0%；在开放域任务上，DeepCoder-14B-Preview在LiveCodeBench Hard子集上Pass@1从55.32%提升至61.09%（+5.77%），其中Hard难度提升最显著（+8.28%）。

消融实验显示，Logit平均（ThinkMerge）优于概率平均（Prob-Merge）。在AIME'25上，R1-Distill-Qwen-7B的Prob-Merge在K=4时准确率降至32.7%，远低于MV的47.3%，表明在归一化前聚合Logits对弱模型更鲁棒。此外，"Shortest-K Merge"策略（仅集成最先完成推理的轨迹）在多数情况下优于"Direct-Merge"，暗示早期完成的推理路径可能包含更简洁有效的信息。

评估边界方面，论文未报告置信区间，且未对比基于PRM的自适应分配方法。代码未开源，但方法兼容vLLM/SGLang框架。实验主要依赖高温度采样保证多样性，未验证低温采样下的表现。

## 关联研究分析

从问题动机看，Self-Consistency（Wang et al., 2022）确立了并行采样在封闭域任务的有效性，但其多数投票机制在开放域任务中失效。ThinkMerge通过Logit级集成解决了这一语义定义问题，但其有效性依赖于模型在答案阶段对Token预测的一致性。与Best-of-Majority（BoM）相比，BoM依赖奖励模型筛选高频答案，而ThinkMerge无需额外模型，计算开销更低，但缺乏显式的质量评估机制，可能在模型置信度校准不佳时引入噪声。

从方法设计看，ThinkMerge借鉴了Product-of-Experts（PoE）的概率融合思想，但将其应用于Logit空间而非概率空间。与M-Ped（Guo et al., 2024）等概率级集成方法不同，ThinkMerge仅在答案阶段进行集成，思考阶段保持独立，这避免了在推理过程中过早收敛导致的多样性损失。然而，论文未探讨Logit平均在低置信度场景下是否会导致错误放大，即当多条思维链对同一Token预测分歧较大时，平均操作是否会产生不稳定的概率分布。

## 总结

本文核心矛盾在于并行测试时计算在开放域任务中缺乏有效的聚合机制。ThinkMerge通过Logit级集成解决了多数投票在自由文本任务中定义不明的问题，证明了在无需训练的情况下，Token级融合能提升代码生成和深度研究任务的性能。实验显示，在LiveCodeBench Hard子集上，DeepCoder-14B-Preview的Pass@1提升8.28%，在AIME 2025上Qwen3-14B达到80.0%。然而，论文未验证Logit平均在模型置信度校准不佳时的鲁棒性，且缺乏与PRM引导方法的对比。当多条思维链对关键Token预测存在显著分歧时，Logit平均是否会导致概率分布不稳定，进而影响最终答案质量，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10471075)