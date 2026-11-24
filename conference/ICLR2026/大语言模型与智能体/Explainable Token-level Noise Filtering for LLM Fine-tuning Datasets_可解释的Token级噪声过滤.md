# ICLR2026最新论文 ｜Explainable Token-level Noise Filtering for LLM Fine-tuning Datasets ｜可解释的Token级噪声过滤

研究机构：浙江大学、清华大学

作者：Yuchen Yang、Wenze Lin、Enhao Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.14536)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.14536)

> 大语言模型微调通常以句子为标签单位，但优化过程在Token粒度上进行，导致标签中无价值Token引入梯度噪声，限制性能上限。现有数据优化方法仅操作于样本级，无法消除Token级噪声。XTF通过分解推理重要性、知识新颖性与任务相关性三个属性，对噪声Token进行梯度掩码。该方法在数学与医学任务上显著提升微调效果，但其依赖静态评分机制，未验证与强化学习在线探索的兼容性。

## 研究背景

微调大语言模型时，模型在每个Token位置计算损失并更新参数，但训练数据通常以完整句子作为目标输出。这种粒度不匹配意味着标签中部分Token对性能提升无贡献，甚至误导收敛方向。为量化Token价值，需区分模型已掌握的知识与需学习的新知识，这涉及模型内部状态（如注意力分布、预测概率）与任务目标的关联分析。

现有数据优化方法分为数据过滤与数据增强两类，均操作于样本级。数据过滤（如DF）基于样本质量筛选，数据增强（如DA）通过变换扩充数据，但均无法识别句子内部Token的异质性。部分研究探索Token级差异，如预训练中的损失值分析（Lin et al., 2024b）或知识蒸馏中的Logits对比（Wei et al., 2024），但这些方法假设数据集无噪声或依赖特定场景（如DPO需预知标签对），不适用于通用微调任务。XTF的切入点在于：将Token价值分解为可独立评估的属性，利用基座模型内部信号构建评分机制，实现Token级噪声的显式过滤。

## 核心方法

### 方法参照系

微调数据优化通常遵循“样本筛选-训练”流程，即基于样本级指标（如困惑度、长度）过滤低质量样本。本文问题与该流程的关键差异在于：优化粒度从样本降至Token，且需同时考虑基座模型认知、数据新颖性与任务相关性，而非单一质量指标。

### 三属性分解与噪声定义

XTF将Token对微调的贡献分解为推理重要性（RI）、知识新颖性（KN）与任务相关性（TR）。RI衡量Token对模型推理结果的影响，KN衡量Token对基座模型的新颖程度，TR衡量Token与任务目标的关联度。噪声Token定义为完全缺乏任一属性的Token，即$D_{noise} = D_{RI\downarrow} \cup D_{KN\downarrow} \cup D_{TR\downarrow}$。这一分解解决了单一指标无法捕捉多维价值的问题，例如一个Token可能高RI但低TR（影响推理但无关任务），需通过多属性联合判断。

### 评分机制与梯度掩码

针对RI，XTF计算基座模型对输入-输出序列的注意力分数，低分Token视为低RI。针对KN，引入正确Token预测概率（PCP），高PCP（>95%）Token视为低KN（模型已掌握）。针对TR，计算Token嵌入向量与任务域向量的距离，大距离Token视为低TR。评分公式如下：

$$S_{RI}(k) = A_\theta(I, O_k)$$

$$S_{KN}(k) = P_\theta(O_k | I, O_{<k})$$

$$S_{TR}(k) = D(E(O_k), \bar{E}(D))$$

其中$A_\theta$为注意力函数，$P_\theta$为预测概率，$D$为距离函数，$\bar{E}(D)$为任务域向量。基于评分，XTF采用保守策略过滤噪声Token：RI用四分位法，KN用95%阈值，TR用Multi-Otsu聚类。过滤后，在微调中掩码噪声Token的梯度，仅更新有价值Token的参数。这一设计避免了样本级过滤的粗粒度问题，通过梯度掩码实现Token级优化，提升收敛方向准确性。

## 实验评估

实验在GSM8K（数学）、CodeExercise/HumanEval（代码）、PubMedQA（医学）三个任务上，使用7个LLM（Llama-3.2/3.1、Mistral-7B、DeepSeek-1.5B/7B/14B）进行微调。基线包括Normal SFT、DF（数据过滤）、DA（数据增强）、SLM、TC等样本级方法，但未包含RL基线（如GRPO）或DPO。

| 模型 | 任务 | Normal | DF | XTF |
| :--- | :--- | :--- | :--- | :--- |
| DeepSeek-1.5B | Math | 42.9 | 37.4 | **56.2** |
| Llama-3.1-8B | Math | 55.4 | **60.3** | 58.7 |
| Llama-3.1-8B (LoRA) | Medicine | 34.3 | 31.4 | **37.9** |
| DeepSeek-7B (LoRA) | Math | 67.9 | 68.2 | **71.8** |

XTF在多数模型-任务组合上优于Normal SFT与DF，尤其在DeepSeek-1.5B数学任务上提升13.3%。但Llama-3.1-8B数学任务中，DF（60.3）优于XTF（58.7），表明Token级过滤并非普适。

消融实验显示，三属性联合过滤（XTF）优于单属性或双属性组合。例如，DeepSeek数学任务中，仅RI过滤得44.7%，RI+KN得46.8%，三属性得56.2%。医学任务中，属性组合的最优选择随模型变化，Llama-3.1-8B（LoRA）中RI+KN优于三属性，表明属性权重需任务自适应。

评估边界：未报告置信区间，数值比较需谨慎。代码任务使用pass@k协议，但未提供具体k值下的详细分布。可复现性方面，论文未提供代码URL，超参数（如PCP阈值95%）固定，未探索动态调整。

## 关联研究分析

与ASFT（Anchored Supervised Fine-Tuning）相比，XTF与ASFT均关注SFT数据质量，但ASFT依赖奖励模型加权Token，XTF依赖基座模型内部信号（注意力/PCP/嵌入）。ASFT需训练独立奖励模型，计算成本高且依赖奖励准确性；XTF无需额外模型，但评分机制静态，无法适应在线探索。这一差异源于任务特性：ASFT面向偏好对齐，需动态奖励；XTF面向通用微调，需低成本静态评估。

与TMS（Trajectory Mixture Supervision）相比，XTF与TMS均旨在提升SFT数据有效性，但TMS混合专家与自生成轨迹，XTF过滤专家轨迹中的噪声Token。TMS通过轨迹混合缓解遗忘，XTF通过Token过滤提升收敛效率。TMS依赖自生成轨迹质量，早期阶段噪声大；XTF依赖基座模型内部信号，对模型能力有要求。两者均未验证与RLVR的结合，Token级过滤在在线探索中是否有效，论文未给出回答。

## 总结

XTF解决的核心矛盾是SFT标签粒度与优化粒度不匹配导致的Token级噪声问题。现有样本级方法无法识别Token异质性，XTF通过三属性分解与基座模型内部信号评分，实现Token级噪声过滤。实验表明，XTF在数学与医学任务上提升显著（最高13.7%），但Llama-3.1-8B数学任务中DF优于XTF，表明方法普适性有限。边界在于：评分机制静态，未验证与RL在线探索的兼容性；属性权重固定，未探索任务自适应调整。当基座模型能力较弱时，内部信号（如注意力）是否仍能有效区分Token价值，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.14536)