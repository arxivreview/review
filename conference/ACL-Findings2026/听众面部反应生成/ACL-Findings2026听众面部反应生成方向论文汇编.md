# ACL-Findings2026 · 听众面部反应生成方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Affectron: Emotional Speech Synthesis with Affective and Contextually Aligned Nonverbal Vocalizations ｜情感对齐的非语言发声合成

研究机构：韩国高丽大学、美国麻省理工学院

作者：Deok-Hyeon Cho、Hyung-Seok Oh、Seung-Bin Kim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f0795c70d176)

> 现有情感语音合成系统难以在开放设置下生成自然且位置合理的非语言发声（Nonverbal Vocalizations, NVs），主要受限于对齐标注的缺失与数据分布偏差。Affectron 提出了一种基于情感驱动匹配与路由的训练时增强策略，结合结构掩码机制，解决了 NV 类型与位置的情感一致性问题。该方法通过微调预训练神经编解码语言模型（Neural Codec Language Model, NCLM），实现了无需显式检测器即可生成多样化 NV 的能力。其价值在于以小规模开放语料实现了高质量 NV 合成，但缺乏与主流扩散模型 TTS 的直接对比，且依赖伪标签的情感对齐精度尚存疑。

】

---

【Dual-Reasoner: Bridging Interleaved Atomicity and Streaming Latency via Thinking-while-Talking ｜流式思维链的原子性重建与延迟掩盖

研究机构：厦门大学、吉林大学

作者：Yangzhuo Li、Shengpeng Ji、Yifu Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b82f9c862b80)

> 语音对话模型引入思维链（Chain-of-Thought, CoT）以提升推理能力，但串行推理导致首包延迟（Time-to-First-Audio, TTFA）高达20秒，违背实时交互要求。现有“边想边说”方法通过机械截断降低延迟，却破坏了推理步骤的语义完整性，导致逻辑断裂与幻觉。本文提出Dual-Reasoner架构，通过流式掩盖机制解决物理延迟，并引入原子一致性恢复框架重建逻辑连贯性。该方案在保持高推理准确率的同时将TTFA降至3.65秒，但其在长程多步推理中的全局记忆保持能力仍存疑。

】

---

【Mirage: A Diagnostic Framework for Evaluating the Realism of Synthetic Contact Center Dialogue Generation ｜合成呼叫中心对话真实性诊断框架

作者：Rishikesh Devanathan、Varun Nathan、Ayush Kumar

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e2a5d2c42aeb)

> 呼叫中心合成对话生成旨在解决隐私约束下的数据稀缺问题，但现有方法生成的文本虽具表面流畅性，却缺乏真实交互中的情感动态与微观行为特征。本文切入点在于指出“可信度不等于真实性”，通过构建包含17项指标的诊断框架，量化合成数据在情感弧线、语言复杂度、交互风格及会话属性上的分布失真。该框架结合属性引导的生成流水线，验证了当前合成策略在下游任务中的效用缺口。其价值在于提供了细粒度的评估工具，但受限于私有数据与单一LLM架构，结论的普适性存疑。

】

---

【Reading Between the Lines: The One-Sided Conversation Problem ｜单侧对话推断：从隐私约束到文本重建

研究机构：美国华盛顿大学

作者：Victoria Ebert、Rishabh Singh、Tuochao Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.03056)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.03056)

> 单侧对话推断（One-Sided Conversation, 1SC）旨在解决仅能获取对话一方话语时，如何推断缺失方内容或生成忠实摘要的问题。现有文本填充技术仅处理短片段缺失，无法应对整段对话缺失带来的语义断裂与幻觉风险。本文通过引入占位符机制与多粒度上下文策略，利用大语言模型（LLM）在单侧可观测性下重建缺失话语并生成摘要。该工作确立了1SC问题的形式化定义与评估基准，但重建结果在事实准确性上仍显著低于意图一致性，且未验证其在实时交互系统中的延迟可行性。

】

---

【Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models ｜语音风格遗忘：多轮对话中副语言指令的持续性失效诊断

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Yu-Xiang Lin、Cheng-Han Chiang、Hung-yi Lee

论文原文见 [arXiv](https://arxiv.org/abs/2512.23578)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_35b717aef5b8)

> 多轮语音交互中，模型能否在首轮接收风格指令后，于后续所有轮次持续保持该风格？现有评估多聚焦单轮或预定义对话，无法捕捉风格随轮次衰减的动态过程。本文通过构建基于用户模拟器的多轮交互框架，量化了五个主流语音语言模型（SLM）在情感、口音、音量与语速上的风格遵循率（IF rate）衰减现象，并证实显式召回机制可部分缓解该问题。该工作揭示了SLM在长程副语言控制上的系统性缺陷，但其缓解策略依赖额外提示开销，未触及模型内部注意力锚定机制的根本修复。

】
