# ACL-Findings2026 · 大语言模型安全对齐与拒答机制方向论文汇编

> 本方向共 13 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Characterizing Selective Refusal Bias in Large Language Models ｜选择性拒绝偏见

研究机构：美国罗格斯大学

作者：Adel Khorramrouz、Sharon Levy

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9536a9646709)

> 大语言模型（LLM）的安全护栏旨在拦截有害内容，但现有评估多聚焦于“是否拒绝”的鲁棒性，忽视了“拒绝谁”的公平性。主流护栏在训练数据分布狭窄的影响下，对不同人口统计学群体的保护力度存在系统性差异，导致对边缘群体过度拒绝，而对主流群体合规生成有害内容。本文通过构建平行反事实提示集量化这种选择性拒绝偏见，并设计间接提示攻击验证其脆弱性。该工作揭示了护栏公平性的严重缺陷，但未提供修复机制，且攻击成功率高度依赖特定模型的对齐强度。

】

---

【Cognitive Analysis Graph-Guided Multi-Turn Safety Enhancement for Large Language Models ｜认知图引导的多轮安全对齐

作者：Lanxue Zhang、Yuqiang Xie、Fang Fang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_538a931f73b2)

> 多轮对话中，孤立无害的查询在历史上下文叠加下可能演变为有害请求，而现有推理时对齐方法因缺乏对问题-响应因果关系的显式建模及历史信息的结构化复用，难以阻止此类“语境性越狱”。CogGSE 通过构建检索式认知分析图并跨轮剪枝历史安全节点，将安全决策从隐式概率操控转为显式认知步骤引导。该方法在开源小模型上显著提升了多轮安全性，但其绝对安全上限仍低于前沿专用对齐方法，且图检索噪声对复杂攻击的鲁棒性存疑。

】

---

【Conflicts Make Large Reasoning Models Vulnerable to Attacks ｜冲突注入与推理模型安全脆弱性

研究机构：香港科技大学、香港城市大学

作者：Honghao Liu、Chengjin Xu、Xuhui Jiang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09750)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09750)

> 大型推理模型（LRMs）在思维链（CoT）中暴露了新的攻击面，但现有越狱方法多依赖多轮交互或外部大语言模型，且缺乏对内部机制的解释。本文切入点在于利用对齐目标间的内在张力，通过单轮、非叙事的冲突注入直接瓦解安全对齐。具体做法是构造内部冲突与道德困境模板，结合层间与神经元级激活分析揭示表示干扰机制。该工作揭示了LRM安全对齐的浅层性，但其攻击效率与优化型攻击的对比缺失，且对强对齐模型的失效原因仅做了初步归因。

】

---

【Guardian-as-an-Advisor: Advancing Next-Generation Guardian Models for Trustworthy LLMs ｜守护模型作为顾问

研究机构：美国圣母大学、美国加州大学洛杉矶分校

作者：Yue Huang、Haomin Zhuang、Jiayi Ye 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07655)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07655)

> 大语言模型（LLMs）部署中的安全守护通常依赖硬门控分类器，这种机制在守护模型与部署模型规范不一致时，会因过度拒绝而损害有用性。现有方案将安全检测局限于有害性标签，忽略了鲁棒性与诚实性等信任维度，且刚性阻断无法保留下游模型的生成自主性。本文提出GaaA范式，通过外部守护模型生成风险标签与自然语言解释并前置到提示中，以软门控方式引导而非阻断生成。该范式在检测精度上接近闭源模型，并显著提升了鲁棒性与诚实性场景下的响应质量，但其有效性高度依赖基础模型的指令遵循能力，且在标准越狱防御基准上的表现尚待验证。

】

---

【Health-ORSC-Bench: A Benchmark for Measuring Over-Refusal and Safety Completion in Health Context ｜医疗领域过度拒绝与安全完成基准

研究机构：澳大利亚麦考瑞大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Zhihao Zhang、Liting Huang、Guanghao Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17642)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17642)

> 医疗大语言模型的安全对齐常陷入两难：拒绝有害请求时往往连带拒绝良性咨询，导致用户转向不可靠信息源。现有通用基准缺乏医疗垂直领域的细粒度评估，且仅关注二元拒绝行为，无法区分“过度拒绝”与“低质量的安全响应”。本文构建了一个包含31,920条边界提示的医疗专用基准，通过自动化改写与人工验证流程，首次引入“安全完成率”指标以量化模型在提供有用信息同时保持安全警告的能力。该基准揭示了前沿模型在医疗场景下的“安全悲观主义”现象，为校准医疗AI助手提供了评估标准，但其单语言限制与主观评分协议仍制约了结论的普适性。

】

---

【Incomplete Prompt Jailbreaks in Large Language Models ｜不完整提示越狱（IPJ）的神经元级终止控制

研究机构：韩国科学技术院

作者：Yeonjea Kim、Bumjin Park、Jaesik Choi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b06b4e3f6c37)

> 导读 大语言模型在自回归生成中优先维护句子连贯性，导致面对不完整有害提示时，模型往往先完成有害内容生成，再在句末输出拒绝，这一现象被称为不完整提示越狱（Incomplete Prompt Jailbreaks, IPJ）。现有基于参数微调的安全对齐方法难以泛化至未见过的攻击结构或拒绝风格，暴露出浅层对齐的脆弱性。本文通过识别并缩放介导句子终止与延续的特定神经元，在解码阶段实现细粒度的生成控制。该机制验证了神经元级干预对IPJ的有效性，但其泛化边界与计算开销仍存疑。

】

---

【Knowing-but-Doing: Diagnosing and Defending Role-Play-Driven LLMs Jailbreaks via Moral Disengagement ｜道德脱离视角下的角色扮演越狱诊断与防御

研究机构：深圳大学、微软研究院

作者：Haiming Qin、Jianxun Lian、Qimin Zhong 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7c0c434854b9)

> 角色扮演场景下，模型常因维持人设一致性而绕过安全对齐，现有防御往往以牺牲角色保真度为代价。本文切入点在于揭示模型在思维链中“识别风险却仍执行”的知行不一机制，将其映射为道德脱离理论中的合理化模式。通过构建诊断基准MD-Trace与内省式防御MD-Shield，在降低攻击成功率的同时维持高角色保真度。该工作将安全对齐从行为层下沉至推理语义层，但其依赖思维链文本的可见性，对非推理模型或隐藏思维链场景的适用性存疑。

】

---

【PsychEthicsBench: Evaluating Large Language Models Against Australian Mental Health Ethics ｜心理健康大语言模型伦理评估基准

作者：Yaling Shen、Stephanie Fong、Yiwen Jiang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e7a927a55924)

> 现有安全对齐研究将“拒绝有害请求”视为安全性的核心指标，但这一范式在心理健康场景中失效，因为缺乏共情的拒绝本身即构成伦理违规。本文指出，通用基准无法捕捉司法辖区特异性与伦理行为的多维性，因此构建了首个基于澳大利亚心理健康伦理原则的评估基准。通过引入质量门控与规则违反分类，该基准将评估重心从“是否拒绝”转移至“是否合乎伦理”。其价值在于揭示了领域微调导致的伦理退化现象，但受限于单一司法辖区与LLM评判机制，其结论的普适性仍需跨域验证。

】

---

【Reasoning Up the Instruction Ladder for Controllable Language Models ｜指令层级推理

研究机构：美国俄亥俄州立大学、微软研究院

作者：Zishuo Zheng、Vidhisha Balachandran、Chan Young Park 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.04694)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04694)

> 大语言模型在处理多源指令时，常因将系统提示与用户输入视为同等文本而陷入优先级冲突，导致安全策略被越狱攻击绕过。现有对齐方法多将安全视为独立标签进行训练，忽略了指令间固有的层级结构，且缺乏显式推理机制来动态解析冲突。本文提出将指令层级（IH）重构为元推理任务，通过构建含冲突对的VerIH数据集，利用可验证奖励强化学习（RLVR）训练模型在执行前显式推理指令优先级。该方法在无需安全数据的情况下实现了安全基准的零样本泛化，但其对复杂多轮交互及非结构化冲突的鲁棒性仍存疑。

】

---

【Self-Reflection Improves Safety of Large Reasoning Models ｜自我反思机制

研究机构：复旦大学、北京邮电大学

作者：Qiang Huang、Wei Zhai、Feng Huang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e10a37998c2c)

> 大型推理模型（LRMs）在长程思维链中易产生有害中间状态，而现有对齐方法仅能预防初始输出，无法干预生成过程中的风险漂移。本文提出在生成过程中插入显式反思标记，使模型在检测到有害信号时自主中断并修正，而非回退重生成。该方法通过监督微调与直接偏好优化组合训练，将有害内容率从13.8%降至4.1%，同时保持有用性。其价值在于将安全对齐从静态过滤转向动态修正，但单次反思能否覆盖长程推理中的多次漂移仍存疑。

】

---

【Simple Role Assignment is Extraordinarily Effective for Safety Alignment ｜角色条件化安全对齐

研究机构：美国加州大学洛杉矶分校、天津大学

作者：Zhou Ziheng、Jiakun Ding、Zhaowei Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00061)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00061)

> 大语言模型（LLM）的安全对齐长期依赖固定原则列表，但原则枚举的完备性不足且缺乏情境认知机制，导致模型在复杂语境下拒绝行为僵化或失效。现有测试时对齐方法多聚焦于解码优化或奖励信号，忽略了评估标准来源本身的可塑性。本文提出以社会角色作为价值观与情境认知的联合载体，通过零训练的生成-批评迭代管线实现上下文敏感的安全对齐。该方法在多个基准上显著优于原则基线，但其有效性高度依赖角色选择，且未验证内部机制层面的鲁棒性。

】

---

【Thinking Twice Makes Large Language Models Safer and More Helpful ｜安全感知反思推理优化

研究机构：北京大学

作者：Yutao Mou、Yuxiao Luo、Shikun Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b1564abe6d9)

> 大语言模型（LLM）安全对齐长期受困于安全性与有用性的零和博弈，强化安全训练往往导致良性请求的过度拒绝。现有基于结果偏好的优化方法缺乏对推理过程的细粒度监督，难以在复杂越狱攻击下保持鲁棒且避免误拒。SaRO 通过引入步骤级自我反思机制，将安全约束内化为模型的推理习惯，实现了安全与效用的双优。该方法在缓解过度拒绝上表现优异，但在极端对抗鲁棒性上尚未超越当前前沿，其推理延迟增加是否可接受仍需权衡。

】

---

【When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models ｜推理轨迹中的自我越狱与链式护栏

研究机构：中国科学院、中国科学院大学

作者：Yingzhi Mao、Chunkang Zhang、Junxiang Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21285)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21285)

> 大型推理模型（LRMs）在生成最终答案前会经历漫长的思维链（CoT）过程，这一过程引入了传统大语言模型（LLMs）不存在的安全盲区。现有对齐方法通常将CoT视为整体进行全局约束，导致模型为规避风险而牺牲推理连贯性，形成安全与能力的零和博弈。本文发现模型常在正确识别风险后，于后续推理步骤中自我说服推翻判断，即“自我越狱”（Self-Jailbreak），并提出链式护栏（Chain-of-Guardrail, CoG）框架，通过定位并修正特定失效步骤实现细粒度对齐。该框架在保持高推理精度的同时显著降低攻击成功率，但其依赖外部分类器进行轨迹诊断，在自动化与泛化性上仍存疑。

】
