# ACL-Findings2026 · 自动化事实核查与声明验证方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ContextCheck: Sentence-Level Faithfulness Verification with Context-Aware Disambiguation ｜上下文条件化忠实度验证

研究机构：美国德克萨斯大学奥斯汀分校、美国密歇根大学

作者：Yueqin Yin、Yaxi Li、Xin Liu 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_059a03b8a380)

> 大语言模型生成的文本常因指代不明导致事实性错误，现有验证器要么孤立检查单句，要么整体处理段落，均无法在保持句子级精度的同时解决跨句指代消解。ContextCheck通过将前置句子作为条件输入直接参与验证，避免了显式去语境化重写的额外成本与误差累积。该方法在封闭域忠实度验证任务上实现了句子级精度与上下文感知的统一，但在开放域多跳推理场景下的泛化能力尚未得到验证。

】

---

【Decide less, communicate more: On the construct validity of end-to-end fact-checking in medicine ｜医疗事实核查的构造效度危机：从端到端分类到交互式对话

作者：Sebastian Antony Joseph、Lily Chen、Barry Wei 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2506.20876)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5e6e6a86997e)

> 自动化事实核查（Automated Fact-Checking, AFC）旨在通过算法替代人工，解决海量医疗错误信息验证效率低下的问题。现有基于大语言模型（LLM）与检索增强生成（RAG）的端到端范式假设声明可被直接映射为“支持/反驳”标签，却忽视了真实社交媒体中声明的语境缺失与证据不可得性，导致系统在临床场景中失效。本文通过专家标注研究揭示医疗声明验证的构造效度缺陷，主张将事实核查重构为交互式对话过程，以澄清意图并处理不可验证性。该视角挑战了领域对“准确率”的单一追求，但缺乏自动化系统的性能验证，其理论价值高于工程落地性。

】

---

【From Fragments to Facts: A Curriculum-Driven DPO Approach for Generating Hindi News Veracity Explanations ｜印地语新闻真实性解释生成：基于课程学习与增强DPO的框架

研究机构：印度理工学院、奥地利因斯布鲁克大学

作者：Pulkit Bansal、Raghvendra Kumar、Shakti Singh 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2507.05179)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_177d9d417208)

> 自动化事实核查旨在解决海量错误信息传播与人工核查效率之间的张力，但现有系统多聚焦英语等高资源语言，导致印地语等低资源语言缺乏可规模化的自动解释生成工具。主流LLM在低资源场景下常产生表面流畅但事实脱节的解释，且标准偏好优化方法未显式约束事实准确性与生成稳定性。DeFactoX通过构建合成偏好数据集，结合课程学习策略与引入事实性、幻觉度量的增强DPO损失函数，实现了对印地语新闻真实性解释的可靠生成。该框架在低资源解释生成任务上提供了有效路径，但其对动态事实验证能力的边界尚待明确。

】

---

【GAVEL: Evidence-Contract Debate with Mechanized Scrutiny for Provenance-Grounded Fact-Checking ｜证据锁定辩论与机械化审查

作者：Ruoyu Xu、Gaoxiang Li、Victor S. Sheng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a89ab2e8fea6)

> 自动化事实核查的核心挑战在于，模型常生成流畅但缺乏来源支撑的结论，尤其在需要引用具体表格单元格或跨文档证据链时，现有方法难以保证证据的细粒度准确性。本文切入点在于将证据绑定从语义层下沉至标识符层，通过强制原子子声明与显式证据单元绑定，并在推理过程中引入确定性校验。GAVEL 构建了一个多智能体辩论框架，结合证据契约与机械化审查链，确保每个论断都有可验证的物理来源。该方法在 FEVEROUS 和 HOVER 基准上显著提升了证据完整性指标，但其性能上限受限于底层小模型的推理能力，且未涵盖实时网络证据场景。

】

---

【Large Language Models Require Curated Context for Reliable Political Fact-Checking—Even with Reasoning and Web Search ｜政治事实核查中LLM的可靠性与引用偏见

研究机构：美国斯坦福大学、美国德州农工大学

作者：Matthew R. DeVerna、Kai-Cheng Yang、Harry Yaojun Yan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0715b2f7e60f)

> 自动化事实核查旨在替代人工以应对海量错误信息，但主流大语言模型（LLMs）在政治声明验证中表现不佳，且内置网络搜索引入系统性偏见。现有检索增强生成（RAG）方法依赖实时网络，噪声大且缺乏对证据源政治倾向的审计。本文构建基于PolitiFact专业核查文章摘要的静态向量库，通过对比15个LLM在零样本、推理及网络搜索模式下的表现，验证了精选上下文对性能的显著提升。该研究揭示了通用网络检索在政治领域的局限性，但静态库的时效性覆盖能力存疑。

】

---

【LoReFact: Bridging the Logic Gap in Fact-Checking ｜逻辑事实性耦合的事实核查框架

研究机构：南京大学

作者：Qiming Xie、Wenjie Zheng、Xiangqing Shen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83dc2353baf3)

> 长文本事实核查长期受困于“原子事实正确但逻辑推导错误”的盲区，导致含谬误文本被误判为真实。现有分解-验证范式仅关注事实覆盖率，无法捕捉声明间的因果或条件依赖失效。本文提出内容-逻辑耦合范式，通过并行评估原子事实与逻辑关系有效性，并引入新数据集LOREFACT与指标LoReFactScore。该工作揭示了现有方法对逻辑谬估的系统性高估，但受限于合成数据分布与单一逻辑类型覆盖，其结论在自然文本中的普适性存疑。

】

---

【MedScore: Generalizable Factuality Evaluation of Open-ended Long-form Medical Answers by Domain-adapted Claim Decomposition and Verification ｜医疗开放域长文本事实性评估：MedScore

研究机构：美国约翰斯·霍普金斯大学

作者：Heyuan Huang、Alexandra DeLucia、Vijay Murari Tiyyala 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_398b3efcb301)

> 导读 现有分解-验证框架在传记等实体中心文本上表现良好，但面对医疗对话中语境依赖、主观且结构复杂的回答时，分解质量严重退化，导致事实性得分失真。本文指出通用分解方法无法处理“如果疼痛加剧”这类假设性语句，提出MedScore，通过领域适配的条件感知分解与多源验证解决该问题。实验显示其有效声明提取量达现有方法3倍，但外部语料验证得分显著低于内部知识，暴露了检索覆盖度对评估可靠性的制约。

】

---

【Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning ｜在线强化学习驱动的事实核查

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、复旦大学

作者：Qi He、Cheng Qian、Xiusi Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_59928245aac4)

> 在线事实核查要求模型在缺乏直接证据时主动检索并推理，但现有方法多依赖预定义工作流或静态微调，难以适应动态检索环境。Veri-R1 通过在线强化学习（Online RL）让模型在训练中实时交互搜索引擎，以奖励信号塑造检索与判决行为。该框架在中小模型上显著提升了联合准确率，但其对大模型过度自信问题的揭示，暗示了置信度校准在事实核查中的潜在价值。

】
