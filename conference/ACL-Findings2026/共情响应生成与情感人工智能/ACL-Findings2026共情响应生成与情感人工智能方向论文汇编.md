# ACL-Findings2026 · 共情响应生成与情感人工智能方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AEQ-Bench: Measuring Empathy of Omni-Modal Large Models ｜全模态共情评估基准

研究机构：香港理工大学、哈尔滨工业大学

作者：Xuan Luo、Lewei Yao、Lanqing Hong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd4374077722)

> 全模态大模型（OLMs）在生成共情响应时，往往忽略音频中的副语言线索，导致评估体系失效。现有基准多依赖文本转录或单一模态，无法量化“语调”对共情质量的决定性影响。本文构建AEQ-BENCH，通过上下文与语调的并行变体设计，直接评估OLMs在音频-文本联合输入下的共情生成与判断能力。该基准揭示了OLMs在细粒度副语言共情上的显著局限，为多模态情感计算提供了必要的评估坐标，但其对生成策略的区分度仍存疑。

】

---

【Beyond Semantic Similarity: Appraisal-Guided Chain-of-Thought Reasoning and Retrieval for Multimodal Emotional Support Conversations ｜认知评价引导的链式推理与检索

研究机构：合肥工业大学、新加坡管理大学

作者：Yuqi Chu、Lizi Liao、Jinggui Liang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dab706d54c41)

> 情感支持对话系统常因无法区分用户话语背后的心理评估机制，导致生成表面相关但治疗上不当的回复。现有检索增强生成方法依赖语义相似度，加剧了这种“认知差距”。本文通过显式建模认知评价链并以此作为检索查询，将范式从语义匹配转向认知共鸣。该方法在两个基准上超越了现有基线，但其评估指标与最新强化学习方法的缺失限制了结论的普适性。

】

---

【Emotion Trajectory-aware Retrieval for Markov-driven Emotion Anticipation in LLM-based Emotional Support Conversation ｜基于情感轨迹检索的马尔可夫情感预测框架

研究机构：国防科技大学、重庆大学

作者：Hongyan Wu、Zhiliang Tian、Zhen Huang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8a1a273650b9)

> 情感支持对话（ESC）的核心挑战在于策略规划往往局限于当前轮次，忽视用户情感的动态演进，导致回复虽流畅但缺乏长期适应性。现有检索增强方法仅匹配单点情感状态，无法捕捉跨轮次的情感依赖关系。本文通过构建动态情感记忆并引入马尔可夫链预测未来情感，将策略选择从即时反应转变为前瞻规划。该框架在ESConv和ExTES数据集上显著优于基线，但其依赖词典提取的情感轨迹精度及马尔可夫假设的长程有效性仍存疑。

】

---

【EMPATH: An Ensemble Method for Automatic Fine-Grained Turn-Level Dialogue Empathy Evaluation with a Novel Emotional Distance Metric ｜基于情感距离与霍夫曼顺序集成的细粒度共情对话评估框架

作者：Dongning Rao、Zhihua Liang、Zhihua Jiang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_630cd3b13a0d)

> 共情对话评估长期受困于自动指标与人类判断的低相关性，现有微调模型虽精度高但缺乏可解释性且未充分利用经典对话指标。本文切入点在于构建一个融合心理学理论、情感对齐度量与经典指标的集成框架，通过霍夫曼顺序策略整合多源信号以克服单一模型的偏差。EMPATH 在 WASSA 和 EX 数据集上均优于冠军基线，但其对预训练情感分类器的依赖及 LLM 裁判的潜在偏见仍构成评估鲁棒性的主要隐患。

】

---

【Empathy Applicability Modeling for General Health Queries ｜共情适用性框架

研究机构：美国密歇根大学

作者：Shan Randhawa、Agha Ali Raza、Kentaro Toyama 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09696)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fe743943bf4d)

> 临床沟通中的核心矛盾在于，医生常因过度聚焦诊断而忽略患者的情感需求，导致共情缺失。现有共情响应生成研究默认“共情总是必要的”，缺乏对“何时不应共情”的前置判断机制。本文提出共情适用性框架（Empathy Applicability Framework, EAF），通过二元分类预测患者查询中情感反应与认知解释的必要性。该框架填补了异步单轮医疗场景下的前置决策空白，但其二元标签是否足以捕捉临床共情的细微程度差异，仍存疑。

】

---

【FreezeEmpath: Efficient Training for Empathetic Spoken Chatbots with Frozen LLMs ｜冻结大语言模型的语音共情对话生成

研究机构：中国科学院、中国科学院大学

作者：Yun Hong、Yan Zhou、Yang Feng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c26962761650)

> 语音共情对话系统旨在让机器捕捉语音韵律中的情感线索并生成具有共鸣的语音回复，但现有方法依赖高成本的情感语音指令数据且微调大语言模型易导致灾难性遗忘。FreezeEmpath 抓住“大语言模型已具备固有共情能力”这一被忽略的前提，通过语义-情感解耦编码与两阶段对齐训练，在完全冻结大语言模型的前提下实现语音共情对话。该方法以低成本自监督数据替代人工标注，验证了冻结架构在情感表达与通用能力保持上的有效性，但其对复杂情感动态的深层推理能力仍受限于未微调的骨干网络。

】

---

【I Don’t Need Solution. I Need Emotional Support : Empathetic LLMs based on Emotional Validation ｜情感验证对齐的共情大语言模型

研究机构：韩国高丽大学

作者：Suhyune Son、Jungwoo Lim、Myunghoon Kang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f2df579865a)

> 导读 共情响应生成（Empathetic Response Generation, ERG）旨在让模型理解用户情感并生成具有共鸣与适当性的回复，其核心驱动力在于提升人机交互中的信任感与心理健康支持效果。现有大语言模型（LLMs）在生成流畅文本时往往陷入“过度迎合”与“模式化建议”的陷阱，缺乏对情感支持时序动态性的把握，导致回复虽流畅但缺乏心理深度。本文提出EVA框架，通过引入基于辩证行为疗法（Dialectical Behavior Therapy, DBT）的情感验证理论，构建层级化偏好数据集并采用直接偏好优化（Direct Preference Optimization, DPO）进行对齐，强制模型随对话进度动态调整共情层级。该方法在情感验证遵循度上表现优异，但其评估指标对分类器准确性的依赖及DPO在长对话时序建模上的局限性仍存疑。

】

---

【PERM: Psychology-grounded Empathetic Reward Modeling for Large Language Models ｜心理学导向的共情奖励建模

研究机构：中国科学技术大学、新加坡国立大学

作者：Chengbing Wang、Wuqiang Zheng、Yang Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8ca496d4883)

> 大语言模型在心理支持场景中常因缺乏深层认知而生成模板化或过度迎合的回复，现有强化学习方法多依赖单一视角的奖励信号，无法捕捉共情交互的双向闭环特性。本文基于共情循环理论，提出从支持者、求助者及旁观者三个视角分解奖励信号，以解决单视角优化导致的共情浅层化问题。通过多视角奖励聚合与组相对策略优化，PERM 在情感智能基准上实现了超过10%的性能提升。该框架验证了心理学理论对奖励建模的指导价值，但其单轮对话设定与纯文本模态限制了在复杂动态交互中的泛化能力。

】

---

【Self-EmoQ: Plutchik-Guided Value-based Planning to Drive Streaming Emotional TTS ｜流式情感对话中的前置规划

作者：Yue Zhao、Hongyan Li、Yong Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.09837)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09837)

> 实时语音交互系统面临的核心矛盾是：情感语调必须在文本生成开始前确定，而传统情感识别只能在文本生成结束后完成。现有基于提示或监督预测的方法无法优化长期对话收益，且受限于静态标签模仿。Self-EmoQ 将情感决策重构为基于 Plutchik 理论奖励的强化学习规划问题，在文本生成前输出情感标签以驱动流式 TTS。该方法在情感决策排序指标上优于基线，但其单步值函数决策是否足以捕捉复杂情感因果链，仍存疑。

】
