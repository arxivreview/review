# ACL-Findings2026 · 大语言模型政治偏见与说服方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Learning Through Dialogue: Engagement and Efficacy Matter More Than Explanations ｜交互过程驱动的政治学习机制

研究机构：新加坡国立大学

作者：Shaz Furniturewala、Gerard Christopher Yeo、Kokil Jaidka

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_461a362ca416)

> 现有LLM政治研究聚焦于模型输出的静态偏见测量或单轮说服效果，忽视了多轮对话中用户认知参与对知识获取的中介作用。本文通过构建包含397段人机对话的实验系统，利用多层回归与中介-调节分析，证明LLM解释丰富度对政治知识增益的影响完全经由用户的认知投入传递，而对信心变化的影响则部分经由反思性洞察传递。这一发现将研究视角从“模型说了什么”转向“用户如何回应”，但缺乏人类导师对照组，难以排除对话形式本身带来的基线效应。

】

---

【PolicyLLM: Towards Excellent Comprehension of Public Policy for Large Language Models ｜政策理解基准与专家路由模型

研究机构：美国圣母大学

作者：Han Bao、Penghao Zhang、Yue Huang 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c50d34b8dd3)

> 大语言模型（LLMs）在公共政策决策辅助中面临认知能力评估缺失的困境，现有通用基准无法区分事实回忆、概念理解与情境应用等分层能力。本文切入点在于构建首个中美跨系统政策理解基准 PolicyBench，并基于 Bloom 分类法设计三级认知任务，同时提出 PolicyMoE 通过低秩适配（LoRA）专家模块解耦不同认知层级。该方法通过路由机制动态分配任务至特定专家，旨在提升模型在复杂政策情境下的推理可靠性。其价值在于建立了政策领域的细粒度诊断框架，但应用层的高准确率是否源于对表面逻辑的拟合而非深层政策理解，仍存疑。

】

---

【Propaganda Signals in LLMs: Perspectival Divergence and Narrative Framing in the Russia-Ukraine War ｜冲突叙事中的视角偏离与宣传机制分析

研究机构：以色列理工学院、以色列内盖夫本-古里安大学

作者：Ofir Shabat、Ido Guy、Kira Radinsky

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_50439ccfdad9)

> 大语言模型在翻译或总结地缘政治冲突时，往往隐含地复现特定信息生态系统的叙事框架，而现有偏见评估多聚焦于宏观左右翼倾向，难以捕捉这种微观的、冲突特定的修辞对齐。本文通过构建俄罗斯-乌克兰冲突的配对参考数据集，提出了一种基于语义距离的视角偏离度量协议，并结合五类宣传手法分类法，量化了模型输出与不同阵营叙事的接近程度及其实现机制。该方法揭示了模型间存在稳定的、特异性的叙事“签名”，表明标准事实性评估无法完全识别这些隐性偏见。这一工作为冲突感知的模型审计提供了新维度，但其结论局限于单一冲突与翻译任务，跨语境泛化性尚待验证。

】

---

【Vulnerability of LLMs’ Stated Belief? LLMs Belief Resistance Check Through Strategic Persuasive Conversation Interventions ｜大语言模型信念鲁棒性评估：基于SMCR框架的说服防御研究

研究机构：美国印第安纳大学

作者：Fan Huang、Haewoon Kwak、Jisun An

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f52039d784d0)

> 大语言模型在持续对话压力下会采纳反事实信念，现有评估仅关注最终是否翻转，忽略了信念衰减的时序动态与多因素交互。本文引入SMCR（Source-Message-Channel-Receiver）框架，系统解耦来源、消息与接收者维度对信念稳定性的影响，并探索口头化置信度与对抗性微调的防御效果。实验揭示小模型极端易感、置信度提示反而降低鲁棒性的悖论，以及微调效果的模型依赖性。该工作为信念防御提供了微观机制视角，但其防御策略的普适性仍受限于特定模型家族与二元任务设定。

】
