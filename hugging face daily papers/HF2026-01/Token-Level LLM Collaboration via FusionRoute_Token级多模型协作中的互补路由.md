# HuggingFace最新推荐论文 ｜Token-Level LLM Collaboration via FusionRoute ｜Token级多模型协作中的互补路由

研究机构：Meta AI、美国卡内基梅隆大学

作者：Nuoya Xiong、Yuhang Zhou、Hanqing Zeng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05106)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05106)

> 大语言模型（LLM）在单一任务上表现优异，但跨领域通用能力往往依赖高昂的超大模型或脆弱的多智能体系统。现有Token级协作方法仅做专家选择，无法修正局部失效，导致性能上限受限于最弱专家。本文提出FusionRoute，通过轻量路由器在每步解码时同时选择专家并输出互补Logits进行修正。该框架在理论上突破了纯专家路由的局限，但在大规模查询级路由的成本效益验证上仍存疑。

## 研究背景

当多个领域专家模型（如数学、代码专用LLM）试图协同生成通用响应时，核心挑战在于如何动态分配每个Token的生成权。若采用序列级协作，每个智能体独立生成完整响应再融合，不仅计算冗余，且长上下文会稀释关键信息。Token级协作虽能细粒度利用专家优势，但传统方法（如Collab）仅基于外部奖励信号选择专家，缺乏对专家局部错误的修正能力，导致在专家失效时整体性能崩塌。

LLM路由领域长期聚焦于“查询级”决策，即判断哪个模型处理整个请求以平衡成本与质量。然而，这种粗粒度决策无法捕捉生成过程中的动态难度变化。多智能体系统（MAS）虽引入协作概念，但多停留在响应级辩论或投票，未能深入Token生成机制。本文切入点在于揭示纯专家路由的理论缺陷：即使路由器能正确选择专家，若专家本身在特定Token上产生次优分布，最终策略仍无法达到最优值函数。FusionRoute通过引入可训练的互补生成器，将协作从“选择”升级为“选择+修正”，解决了专家局部失效导致的性能瓶颈。

## 核心方法

### 方法参照系

本文问题属于多智能体路由的Token级变体。标准查询级路由流程为“查询→模型选择→生成”，优化全局成本；本文流程为“Token→专家选择+Logits融合→生成”，优化局部生成质量。关键差异在于决策粒度从序列级降至Token级，且路由器不仅输出离散选择，还输出连续修正信号。

### 互补Logits融合机制

纯专家路由的脆弱性在于，即使选对专家，其输出分布仍可能偏离最优策略。FusionRoute在解码步 $t$ 引入路由器 $\pi_\theta$，其输出路由权重 $w_\theta \in \mathbb{R}^n$ 和互补Logits $\log \pi_{\theta_{LM}}(\cdot | x, y_{\le t})$。最终下一Token分布通过Logits加法融合：

$$ \log \pi_{final}(y_{t+1} | x, y_{\le t}) = \log \pi_{expert}(y_{t+1} | x, y_{\le t}) + \log \pi_{\theta_{LM}}(y_{t+1} | x, y_{\le t}) $$

此设计允许路由器在专家可靠时保持其优势，在专家失效时提供修正，从而扩展了有效策略类，使系统能恢复最优值函数。

### CDPO训练策略

SFT阶段仅训练路由选择，无法学习互补修正行为。CDPO（Complemented Direct Preference Optimization）阶段通过偏好优化训练路由器基座参数 $\theta_{LM}$，同时冻结路由层以避免过拟合。损失函数定义为：

$$ L_{CDPO}(\theta_{LM}) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_{\theta_{LM}}(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_{\theta_{LM}}(y_l|x)}{\pi_{ref}(y_l|x)} \right) \right] $$

该公式通过对比偏好对，迫使路由器在专家弱项上产生更强的修正梯度，而在专家强项上保持低干预，实现了训练目标与推理时“选择+修正”行为的一致性。

## 实验评估

实验基于Llama-3和Gemma-2家族，使用PerfectBlend数据集（500测试样本）和OpenHermes偏好数据。基线覆盖序列级协作、Token级协作（Collab）、模型合并（DARE, TaskArithmetic）及直接微调。由于论文未提供RouterBench等标准路由基准的数值，且【论文实验数据】区未包含具体表格数值，无法构建主实验表格。文字结果显示，FusionRoute在数学、代码和指令遵循任务上均优于Collab和模型合并基线，且与领域专家在各自任务上的性能相当。

消融实验表明，移除互补Logits后，性能显著下降，尤其在代码和指令遵循任务上，验证了修正机制对局部次优Token的必要性。CDPO阶段相比纯SFT阶段，在GPT4o胜率上带来显著提升，证明偏好优化有效增强了路由器的互补能力。然而，论文未报告推理延迟或GPU利用率，无法评估Token级路由在大规模部署中的计算开销。

评估边界在于缺乏跨基准的绝对性能参照。PerfectBlend测试集规模较小（500样本），可能高估泛化能力。代码开源（GitHub），但超参数（如 $\lambda=1/3$）固定，未探索不同专家组合下的鲁棒性。可复现性受限于外部奖励模型（如Ray2333/reward-model-Mistral-7B）的依赖，不同奖励模型可能导致结果波动。

## 关联研究分析

从问题动机看，FusionRoute与查询级路由（如RouteLLM）存在根本差异。RouteLLM优化全局成本-质量帕累托前沿，而FusionRoute优化局部生成质量，忽略全局预算约束。这种差异源于任务特性：查询级路由适用于异构查询池，而Token级协作适用于单一复杂任务的多专家协同。FusionRoute未解决新模型接入问题，其路由器需针对特定专家组合重新训练，而ZeroRouter等零样本方法通过潜在空间实现快速适应，两者在适应效率上形成鲜明对比。

从方法设计看，FusionRoute与MoE（Mixture of Experts）共享路由思想，但MoE需联合训练所有专家，而FusionRoute解耦了专家训练与路由训练。MoE的路由器仅输出门控权重，而FusionRoute路由器输出互补Logits，这一设计源于MoE无法修正专家内部失效的局限。与Collab相比，FusionRoute摒弃了外部奖励模型依赖，通过内部互补Logits实现自监督修正，提升了训练稳定性，但牺牲了对专家质量的显式评估能力。

## 总结

FusionRoute旨在解决Token级多模型协作中专家局部失效导致的性能瓶颈。现有方法仅做专家选择，无法修正次优分布，而本文通过互补Logits机制，使路由器能动态修正专家错误，理论上突破了纯专家路由的局限。实验证明该框架在Llama-3和Gemma-2家族上优于Collab和模型合并基线，尤其在代码和指令遵循任务上表现突出。然而，论文未报告推理延迟，且测试集规模较小，无法验证其在大规模查询级路由中的成本效益。当专家模型数量增加至10个以上时，互补Logits的修正能力是否仍能有效抑制参数干扰，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05106)