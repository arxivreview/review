# ACL-Findings2026 · 大语言模型中的偏见检测与缓解方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Scalable Entity-Based Framework for Auditing Bias in Large Language Models ｜实体替换不变性审计框架

研究机构：法国巴黎萨克雷大学

作者：Akram Elbouanani、Aboubacar Tuo、Adrian Popescu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f728652a6a57)

> 大语言模型在政治、地缘及经济等高风险决策场景中，其输出常受实体名称而非文本证据驱动，导致系统性偏见。现有基准依赖静态模板，牺牲了生态效度，难以反映真实部署中的偏见动态。本文提出基于实体替换不变性的黑盒审计框架，通过合成数据控制变量，量化模型对实体身份的依赖程度。该框架实现了19亿数据点的大规模审计，验证了合成数据作为真实偏见代理的有效性，但其对复杂推理链中偏见放大的覆盖仍存疑。

】

---

【Audit Me If You Can: Query-Efficient Active Fairness Auditing of Black-Box LLMs ｜有界主动公平审计

研究机构：德国柏林工业大学、比利时鲁汶大学

作者：David Hartmann、Lena Pohlmann、Lelia Hanslik 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03087)

> 黑盒大语言模型（LLM）在部署后常因查询成本与隐私限制无法进行全量公平性评估，传统静态基准无法捕捉动态系统中的群体性能差异。现有被动采样方法在严格精度阈值下查询效率极低，导致独立审计难以在有限预算内完成。本文提出有界主动公平审计（Bounded Active Fairness Auditing, BAFA），通过约束优化构建代理模型版本空间并主动选择高不确定性查询，以最小化查询次数估计排序公平性指标。该方法在两个案例研究中将查询成本降低最高41倍，但其有效性依赖于代理模型与黑盒模型的分布匹配度，在极低预算场景下表现不稳定。

】

---

【Bias Dynamics in BabyLMs: Towards a Compute-Efficient Sandbox for Democratising Pre-Training Debiasing ｜低成本代理模型用于预训练去偏

研究机构：英国剑桥大学

作者：Filip Trhlik、Andrew Caines、Paula Buttery

论文原文见 [arXiv](https://arxiv.org/abs/2601.09421)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09421)

> 大语言模型（LLM）偏见研究长期受限于高昂的重训练成本，导致主流方法聚焦于后训练干预，难以触及偏见形成的根源。本文提出利用低资源BabyLMs作为沙箱，验证其在偏见获取与去偏响应上能否替代标准BERT模型。通过建立BabyLMs与BERT在去偏行为上的高相关性，本文实现了将预训练去偏实验成本从500 GPU-hours降至30 GPU-hours。这一基础设施贡献降低了研究门槛，但其代理效应的绝对值映射能力仍存疑。

】

---

【BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization ｜组相对策略优化在偏见缓解中的应用

作者：Saket Reddy、Ke Yang、ChengXiang Zhai

论文原文见 [arXiv](https://arxiv.org/abs/2606.04807)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.04807)

> 大语言模型（LLM）偏见缓解面临高方差、主观性强的奖励景观，导致传统偏好优化算法在去偏与通用能力保持间难以平衡。直接偏好优化（DPO）因离线静态对限制泛化，近端策略优化（PPO）因独立评估器模型引入训练不稳定性，现有方法无法兼顾去偏效果与训练鲁棒性。本文提出BiasGRPO框架，通过组相对策略优化（GRPO）替代评估器模型，利用组内奖励归一化稳定高方差奖励信号，并配套自定义偏见奖励模型与合成数据集。该方法在Phi-2模型上实现了多基准偏见分数下降与知识保持，但缺乏与内部机制干预方法的横向对比，其优势在更大规模模型上的可迁移性存疑。

】

---

【C2PO: Diagnosing and Disentangling Bias Shortcuts in LLMs ｜因果对比偏好优化

研究机构：新加坡南洋理工大学

作者：Xuan Feng、Bo An、Tianlong Gu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_51fd16dff4e1)

> 大语言模型在推理任务中常依赖词汇重叠或刻板印象等捷径，导致输出系统性偏差，而现有对齐方法往往在消除偏见时牺牲通用能力。直接偏好优化（DPO）等整体优化范式无法解耦语义质量与虚假关联，导致模型在复杂推理中失效。本文提出C2PO，通过挖掘因果反事实三元组并引入公平敏感的双动态目标函数，在优化过程中同时发现并抑制偏见捷径。该方法在打破偏见-能力权衡方面表现优异，但其对教师模型的依赖及单轮对话的局限仍需审视。

】

---

【Debiasing LLMs by Masking Unfairness-Driving Attention Heads ｜差分激活掩码去偏

研究机构：南京大学、澳大利亚新南威尔士大学

作者：Tingxu Han、Wei Song、Ziqi Ding 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10142)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10142)

> 大语言模型（LLM）在直接回答模式下常输出带有社会偏见的文本，而思维链（Chain-of-Thought, CoT）提示虽能降低偏见，但其内部机制长期缺乏解释。现有去偏方法多依赖外部分类器或静态探针，无法揭示提示策略与内部组件激活之间的因果联系。本文提出DIFFHEADS，通过对比直接回答与CoT两种提示下的注意力头激活差异，定位并掩码“偏见头”，在不重训练的前提下实现去偏。该方法在两个开源模型上显著降低了不公正率，但仅验证了特定架构与提示格式，其泛化边界尚不明确。

】

---

【Distilling the Essence, Discarding the Dross: Improving Fairness in Multimodal Large Language Models via Historical Reflection-Guided Prompt Optimization ｜历史反思引导提示优化

研究机构：吉林大学、南开大学

作者：Juncheng Hu、Jiming Yu、Rui Song 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2c69ca94dc7)

> 多模态大语言模型（MLLMs）的黑盒去偏面临手工提示模板僵化且易陷入优化死循环的困境。现有静态提示无法适应复杂偏见类型，而动态优化常因遗忘有效历史路径导致性能震荡。本文提出历史反思引导提示优化框架，通过构建正负历史链对比机制，引导模型在离散提示空间中高效收敛。该方法在多数模型上将偏见分数降至近零，但缺乏与白盒内部机制干预方法的直接对比，其泛化边界尚待验证。

】

---

【Fairness Evaluation and Inference Level Mitigation in LLMs ｜动态神经元抑制

研究机构：澳大利亚麦考瑞大学

作者：Afrozah Nadeem、Mark Dras、Usman Naseem

论文原文见 [arXiv](https://arxiv.org/abs/2510.18914)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18914)

> 多轮对话中，LLM的偏见并非静态存在，而是随上下文累积与记忆携带动态演化，现有静态剪枝或推理时干预方法无法区分“当前轮次的局部偏见”与“历史轮次的记忆偏见”，导致过度抑制或漏检。本文切入点在于将偏见视为动态累积过程，通过记忆一致性探针与自适应门控机制，在推理时实时、可逆地调节特定神经元的影响。该方法在多语言多轮对话中显著降低偏见分数，同时保持语义连贯性，但其效果依赖于归因精度与探针阈值，对长程依赖的捕捉能力尚存疑。

】
