# ACL-Findings2026 · 提示工程与优化方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Prompt Engineering: A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality ｜提示词敏感性的统计归因与鲁棒性机制分析

研究机构：香港理工大学、香港中文大学

作者：Qipeng Xie、Zi Liang、Jiafei Wu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8e5171758430)

> 提示词工程长期面临“蝴蝶效应”，即微小的词汇扰动导致模型输出剧烈波动，现有方法多聚焦于黑盒优化或模板级评估，缺乏对底层词汇机制的统计解释。本文切入点在于将提示词敏感性视为一种可量化的统计现象，而非需消除的噪声。通过构建132,000个提示词变体数据集，利用n-gram统计识别出“领域特定术语”与“显式行动指令”作为鲁棒性的语言支柱，并据此设计自动化的模式注入代理。该工作提供了从经验直觉到统计原则的转变，但其结论是否适用于非结构化或低资源语言场景仍存疑。

】

---

【Lost in the Prompt Order: Revealing the Limitations of Causal Attention in Language Models ｜因果注意力下的提示词顺序敏感性机制分析

作者：Hyunjong Ok、Jaeho Lee

论文原文见 [arXiv](https://arxiv.org/abs/2601.14152)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.14152)

> 提示词工程长期面临模型对输入结构微小变化产生剧烈性能波动的难题，现有研究多停留在现象描述或黑盒优化层面，缺乏对底层机制的归因。本文聚焦于多选题问答中上下文、问题与选项的排列顺序，指出解码器架构中的因果掩码是造成性能差异的核心物理约束。通过架构对比与干预实验，论文证实了选项token在特定顺序下无法访问上下文信息这一结构性瓶颈。该发现将提示词敏感性从经验性观察提升为可解释的架构属性，但仅提供了推理时缓解手段，未解决训练时的根本修复问题。

】

---

【Strategy-Induct: Task-Level Strategy Induction for Instruction Generation ｜无标签任务指令归纳

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Po-Chun Chen、Hen-Hsen Huang、Hsin-Hsi Chen

论文原文见 [arXiv](https://arxiv.org/abs/2605.20924)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20924)

> 指令归纳旨在让大语言模型从少量示例中自动推导任务规则，但现有方法普遍依赖输入-输出对，这在标注数据稀缺或获取成本高昂的场景下构成硬性约束。STRATEGY-INDUCT 通过引入“策略生成”作为中间表示，将归纳信号从“答案”置换为“解题思路”，从而在仅拥有问题集合的条件下实现任务级指令的自动合成。该框架在多个基准上超越了依赖标签的基线，证明了无标签归纳的可行性，但其跨模型泛化能力是否源于策略的语义抽象而非表面形式，仍需进一步验证。

】

---

【What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts ｜提示词欠定：需求感知优化与稳定性治理

研究机构：美国卡内基梅隆大学

作者：Chenyang Yang、Yike Shi、Qianou Ma 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4054c1974d7b)

> 提示词工程面临的核心矛盾在于，开发者难以穷尽所有业务需求，而大语言模型（LLM）对未明确指定的行为表现出高度不稳定性。现有自动优化方法（如 APE、TextGrad）仅关注整体性能指标，缺乏对单一需求满足率的细粒度反馈，导致优化结果在模型更新后极易回归。本文切入点在于将传统软件工程中的“需求工程”引入提示词优化，通过需求感知优化器（Requirements-Aware Optimizers）显式管理“指定”与“未指定”需求的边界。其价值在于揭示了“全量指定”的反模式，但其在通用推理基准上的泛化能力仍存疑。

】

---

【What Tokens Truly Matter? The Logit Conflation Problem in LLM Sampling ｜信号提取与主动相关性采样

研究机构：英国杜伦大学

作者：Pinlong Zhao、Huijun Tang、Pengfei Jiao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_35466b354d48)

> 大语言模型在指令遵循任务中常出现“高置信度但答非所问”的现象，根源在于采样策略仅依据Logit幅值筛选Token，忽略了Logit中混杂的语言流畅性与提示相关性。现有Top-p或Top-nσ等统计过滤方法无法区分这两种信号，导致模型在约束生成中频繁遗漏关键信息。本文提出SEAL-Sampling，通过注意力加权归因机制在解码阶段显式提取提示相关性信号，过滤掉统计显著但语义无关的Token。该方法在无需额外前向传播的前提下提升了指令遵循质量，但其对逻辑推理任务的增益有限，且依赖最终层注意力的语义对齐假设。

】
