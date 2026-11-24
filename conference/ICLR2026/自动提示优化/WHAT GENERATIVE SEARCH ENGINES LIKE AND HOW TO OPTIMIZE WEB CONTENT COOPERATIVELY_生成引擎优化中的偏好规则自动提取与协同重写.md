# ICLR2026最新论文 ｜WHAT GENERATIVE SEARCH ENGINES LIKE AND HOW TO OPTIMIZE WEB CONTENT COOPERATIVELY ｜生成引擎优化中的偏好规则自动提取与协同重写

研究机构：美国卡内基梅隆大学

作者：Yujiang Wu、Shanshan Zhong、Yubin Kim 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60800832)

> 生成引擎优化（Generative Engine Optimization, GEO）旨在通过重写网页文档提升其在大型语言模型（LLM）合成回答中的引用可见性，以解决内容提供商在新型搜索范式下的流量获取难题。现有方法依赖人工设计启发式规则或对抗性注入，缺乏对引擎底层偏好的系统性理解，且往往牺牲回答质量。AutoGEO 通过 LLM 自动提取引擎偏好规则，并以此构建提示驱动与强化学习驱动的两种重写模型，实现了可见性与引擎效用的协同优化。该方法在三个基准上平均提升 35.99% 的 GEO 指标，但其规则提取的完备性与跨引擎泛化能力仍存疑。

## 研究背景

当用户向 Google AI Overview 或 ChatGPT 提问时，系统并非简单返回链接列表，而是检索文档并生成带有引用的合成答案。这种生成引擎（Generative Engine, GE）的普及使得传统搜索引擎优化（SEO）失效，内容提供商转而关注 GEO，即如何让文档在 GE 的回答中获得更高权重。然而，GE 的偏好是黑盒的，且不同 LLM 后端（如 Gemini、GPT、Claude）对文档内容的偏好存在显著差异，这导致人工设计的通用重写策略往往无效。

现有 GEO 研究主要沿两条路线展开：一是基于人工启发式的重写，如 Aggarwal et al. (2024) 提出的关键词堆砌、引用来源等规则，这些规则缺乏数据驱动的依据，难以适应特定引擎的偏好；二是对抗性方法，如 Nestaas et al. (2024) 的 Hijack 攻击，通过注入指令操纵 GE 行为，但这类方法严重损害回答质量，违背了“合作式优化”的原则。主流路线的瓶颈在于缺乏从大规模 GE 交互中自动发现偏好的机制，以及缺乏同时优化可见性与回答质量的多目标框架。AutoGEO 的切入点在于将 GE 偏好显式化为可解释的规则集，并以此作为重写模型的指导信号或奖励函数，从而在提升文档可见性的同时保持引擎效用（Generative Engine Utility, GEU）。

## 核心方法

### 方法参照系

本文问题可置于“反馈驱动优化”的通用框架下，但关键差异在于优化对象从提示（Prompt）转向文档内容（Document），且反馈信号从任务性能指标转向引擎偏好规则。标准流程通常直接优化目标函数，而本文引入中间层“规则提取”，将隐式偏好转化为显式约束。

### 偏好规则自动提取

传统方法依赖人工设计规则，无法覆盖引擎的细微偏好。AutoGEO 通过四阶段流水线自动提取规则：Explainer 对比高可见性与低可见性文档对，生成自然语言解释；Extractor 将解释蒸馏为简洁洞察；Merger 采用层级合并策略将数万条洞察聚合为候选规则；Filter 筛选出可靠规则。这一过程解决了人工规则覆盖率低且不可扩展的问题。规则提取的核心在于利用 LLM 的推理能力从对比数据中归纳模式，其公式化表达为规则集 $S$ 的构建过程，其中 $S$ 是通过对文档对 $(d_i, d_j)$ 的可见性差异 $\Delta V$ 进行语义聚合得到的：

$$ S = \text{Filter}(\text{Merge}(\text{Extract}(\text{Explainer}(d_i, d_j, a)))) $$

该公式表明，规则集 $S$ 并非直接优化目标，而是通过语义推理从原始交互数据中提炼出的中间表示，其物理含义是将黑盒引擎的偏好转化为可操作的文本约束。

### 规则引导的协同重写

提取的规则 $S$ 被用于构建两种 GEO 模型。AutoGEOAPI 将 $S$ 直接注入 LLM 提示，实现免训练部署；AutoGEOMini 则通过强化学习（RL）训练紧凑模型，其中 $S$ 作为奖励信号。RL 训练采用 Group Relative Policy Optimization (GRPO)，其目标函数为：

$$ \mathcal{L}_{GRPO} = \mathbb{E}_{q \sim \mathcal{D}} \left[ \frac{1}{G} \sum_{i=1}^{G} \left( \min(r_i(\theta) A_i, \text{clip}(r_i(\theta), 1-\epsilon, 1+\epsilon) A_i) - \beta D_{KL}(\pi_\theta || \pi_{ref}) \right) \right] $$

其中 $A_i$ 是基于规则 $S$ 计算的组内相对优势，$r_i(\theta)$ 是重要性采样比，$D_{KL}$ 是 KL 散度正则项。这一设计解决了 API 调用成本高且无法离线部署的问题，同时通过规则奖励确保重写文档符合引擎偏好，而非仅追求表面可见性。

## 实验评估

实验在 GEO-Bench、Researchy-GEO 和 E-commerce 三个数据集上进行，基线包括人工启发式方法（如 Fluency Optimization）和对抗性方法（Hijack/Poisoning）。AutoGEOAPI 在 Researchy-GEO 上的 Overall 指标达到 43.76，显著优于最强基线 Fluency Optimization 的 22.99，提升幅度达 50.99%。AutoGEOMini 在相同数据集上取得 38.53 的 Overall 指标，虽略低于 API 版本，但成本仅为后者的 0.0071 倍，且可在 CPU 上离线运行。

| 方法 | Researchy-GEO Word | Researchy-GEO Pos | Researchy-GEO Overall | E-commerce Overall | GEO-Bench Overall |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Vanilla | 20.11 | 20.13 | 20.18 | 18.32 | 19.44 |
| Fluency Optimization | 22.53 | 22.79 | 22.99 | 21.38 | 23.73 |
| AutoGEOAPI | 42.87 | 43.53 | 43.76 | 34.05 | 34.92 |
| AutoGEOMini | 37.50 | 38.37 | 38.53 | 25.25 | 27.12 |

消融实验显示，规则奖励在 AutoGEOMini 中贡献最大，移除规则奖励后 Overall 指标从 38.53 降至 31.41，降幅达 18.47%。相比之下，移除语义奖励仅导致 1.12% 的下降。这一结果验证了规则提取是性能提升的核心驱动力，而非 RL 训练本身。此外，规则在不同 LLM 引擎间存在显著重叠，Gemini 与 GPT 的规则重叠率为 78.95%，表明部分偏好是通用的，但特定引擎仍有独特规则。

评估边界方面，GEU 指标仅包含 KPR、KPC、Precision、Recall、Clarity 和 Insight 六个维度，未涵盖延迟或内存占用等工程指标。代码已开源，但规则提取过程依赖 Gemini-2.5-pro 作为教师模型，其成本在大规模部署中可能成为瓶颈。

## 关联研究分析

从问题动机看，AutoGEO 与 ProTeGi 均利用 LLM 反馈指导优化，但 ProTeGi 优化提示以改变模型行为，而 AutoGEO 优化文档以改变检索引用。ProTeGi 的文本梯度是局部优化信号，缺乏全局收敛保证，而 AutoGEO 的规则提取通过层级合并实现了全局模式归纳，这源于文档重写任务需要覆盖多种偏好维度，而非单一任务性能。从方法设计看，AutoGEO 与 GEPA 均关注成本与性能权衡，但 GEPA 使用帕累托选择进化算法，而 AutoGEO 使用 RL 奖励。GEPA 的评估过程需要多次并行推理以计算共识，计算复杂度较高，而 AutoGEO 的规则奖励仅需单次 LLM 调用，成本更低。然而，AutoGEO 的规则提取依赖大规模 GE 交互数据，这在数据稀缺场景下可能失效，而 GEPA 的进化搜索对数据量要求较低。

## 总结

AutoGEO 解决了 GEO 中偏好黑盒化与人工规则低效的核心矛盾，通过自动提取引擎偏好规则并构建协同重写模型，实现了可见性与效用的平衡。该方法在 Researchy-GEO 上取得 43.76 的 Overall 指标，较最强基线提升 50.99%，且 AutoGEOMini 成本仅为 API 版的 0.0071 倍。其边界在于规则提取依赖大规模 GE 交互数据，且未验证规则在引擎模型迭代后的稳定性。当 GE 后端 LLM 更新后，提取的规则是否仍能保持有效性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60800832)