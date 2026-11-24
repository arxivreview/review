# ACL-Findings2026 · 大语言模型作为裁判的评估方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【All Prompts Are Created Equal? Evaluating Robustness of LLM Judges Against Non-Adversarial Prompt Variations ｜非对抗性提示变体下的LLM裁判鲁棒性评估

作者：Savita Bhat、Vasudeva Varma

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c2d4823dc908)

> 导读 大语言模型评估者（LLM-as-a-Judge）旨在利用大语言模型替代昂贵的人类评估，为开放式生成任务提供可扩展的自动化反馈。尽管现有研究已证实强模型与人类判断具有较高一致性，但评估指令的微小语义等价改写往往导致评分剧烈波动，这一“指令敏感性”问题在真实多团队协作场景中普遍存在却未被系统量化。本文通过构建包含约115,000次评估的基准，首次将属性可验证性作为核心变量，揭示了准确率与鲁棒性的脱节现象，并提出了基于该属性的诊断框架。该工作填补了非对抗性鲁棒性评估的空白，但其结论是否适用于对抗性攻击或专用微调模型，仍需进一步验证。

】

---

【Contrastive Decoding Mitigates Score Range Bias in LLM-as-a-Judge ｜分数范围偏差的对比解码缓解

作者：Yoshinari Fujinuma

论文原文见 [arXiv](https://arxiv.org/abs/2510.18196)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18196)

> 导读 LLM-as-a-Judge在直接评估任务中面临评分尺度不稳定的问题，现有偏差缓解方法多聚焦于位置或长度偏差，忽略了评分区间平移对模型输出的系统性干扰。本文发现LLM评判存在“分数范围偏差”，即相同内容在不同评分区间（如0-4与1-5）下相关性波动剧烈，且同家族模型共享相似的偏差模式。通过引入对比解码机制，利用同家族小模型的logit分布抵消主模型的偏差，实现了跨区间评分稳定性的提升。该策略在摘要任务上验证了推理时优化的有效性，但绝对相关性仍低于成对比较标准，且未覆盖复杂推理场景。

】

---

【How Hypocritical Is Your LLM judge? Listener-Speaker Asymmetries in the Pragmatic Competence of Large Language Models ｜语用听-说解耦：LLM 判断与生成能力不对称分析

作者：Judith Sieker、Sina Zarrieß

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_05e2793400c7)

> 导读 大语言模型（LLM）在语用任务中常被同时要求“判断”他人输出的恰当性与“生成”恰当输出，但现有评估往往将二者混同，默认判断能力可代理生成能力。这一假设在语用推理中缺乏验证，导致模型能力评估出现系统性偏差。本文通过构建同一语料上的平行“听”（判断）与“说”（生成）任务，量化了二者间的性能落差。研究揭示了当前 LLM 存在显著的听-说不对称，判断表现远优于生成，挑战了以单一角色评估模型语用能力的常规做法，但受限于特定语用现象与强制格式约束，其结论的泛化性仍需进一步检验。

】

---

【LRBench and Judge-R1: Principled Evaluation and Training of LLM-Based Judges for Long-Context Reasoning ｜长上下文推理评判基准与检索增强训练框架

作者：Xinyi Zhao、Haoqi Hu、Ziyu Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_554e21d2f6d6)

> 现有 LLM 评判器在长上下文推理任务中常因证据缺失而误判逻辑正确性，且缺乏细粒度的原则违规标注。本文指出，仅依赖最终答案或粗粒度偏好的评估协议无法捕捉推理链中的细微缺陷。为此，作者构建了包含 10 万+ 实例的 LRBENCH 基准，并提出结合多轮检索与强化学习的 Judge-R1 训练框架。该框架在长上下文推理评估上显著优于通用大模型，但其对检索延迟的忽略及测试集规模限制，使其在工程落地与统计严谨性上仍存疑。

】

---

【MAPLE: Multi-Aspect Panels of LLM Evaluators for Open-Ended Questions ｜多标准异构评估者面板

作者：Michinori Jinji、Kyohei Atarashi、Koh Takeuchi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_13b5830e63e1)

> 大语言模型评估者（LLM-as-a-Judge）旨在利用大语言模型替代昂贵的人类评估，为开放式生成任务提供可扩展的自动化反馈。现有方法要么依赖单一骨干模型的提示工程，要么采用无差别投票的多智能体集成，均无法在评估者能力参差不齐时保证结果的统计可靠性。MAPLE 将评估标准分解与多模型成对比较结合，通过扩展的 Crowd-BT 模型联合学习标准权重与评估者可靠性参数，实现可靠性感知的统计聚合。该框架在作文评分任务上验证了优于单模型及简单投票的鲁棒性，但其性能上限受限于聚合机制对多数派偏差的敏感性，且未覆盖复杂推理或代码生成场景。

】

---

【Mitigating Judgment Preference Bias in Large Language Models through Group-Based Polling ｜基于群组轮询优化的大语言模型评判偏好偏差缓解

作者：Shuliang Liu、Zhipeng Xu、Zhenghao Liu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b98b4bfe9702)

> 大语言模型作为自动评估者（LLM-as-a-Judge）在替代人类标注时，常因自我偏好偏差（Self-Preference Bias）高估自身生成的响应，导致评估信号失真。现有推理时集成或提示去偏方法无法从根本上消除该偏差，且往往依赖强模型指导弱模型。本文提出无监督多智能体群组轮询优化框架（Genii），通过异构模型间的客户端-服务器交互生成一致性偏好对，利用直接偏好优化（DPO）更新模型参数。该方法在无人类标注条件下优于有监督微调，但其在复杂推理任务上的绝对准确率仍低于领域SOTA，且未验证大规模模型的扩展性。

】

---

【SenseJudge: Human-Centric Preference-Driven Judgment Framework ｜基于显式偏好蒸馏的个性化大语言模型评判框架

研究机构：北京大学

作者：Rui Li、Junfeng Liu、Xiangwen Kong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03189)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_21bc3541862b)

> 大语言模型评判（LLM-as-a-Judge）旨在替代昂贵的人类评估，但现有方法依赖固定偏好数据，难以适配异构用户的个性化价值。本文切入点在于将隐式人类偏好显式化，通过动态筛选偏好子集实现训练-free的定制化评判。具体做法是从少量标注对中蒸馏偏好文本，利用多数投票聚合优化评判一致性。该框架在真实多轮对话场景下显著提升了小模型评判精度，但其对通用基准的泛化能力及偏好子集选择的过拟合风险仍存疑。

】
