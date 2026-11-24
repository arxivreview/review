# ACL-Findings2026 · 大语言模型安全攻击方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【False Sense of Security: Why Probing-based Malicious Input Detection Fails to Generalize ｜探测分类器失效机制：表面模式而非语义理解

作者：Cheng Wang、Zeming Wei、Qin Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c134b436dcb0)

> 基于内部表征的恶意输入检测长期被视作LLM安全的有效防线，但现有评估仅关注分布内性能，掩盖了泛化能力的缺失。本文指出探测分类器实际依赖浅层词汇模式而非语义有害性，导致其在真实场景中失效。通过引入朴素贝叶斯基线对比、语义清洗对照实验及模式依赖分析，系统性地证伪了“表征可分性即语义理解”的假设。该研究揭示了当前安全检测范式的根本缺陷，但受限于单轮静态表征，其结论在多轮动态交互场景下的普适性尚存疑问。

】

---

【From Attack Surfaces to Actual Operations: A Survey of Modern LLM Jailbreaks ｜基于漏洞机制的LLM越狱攻击双轴分类框架

研究机构：德国慕尼黑工业大学、新加坡国立大学

作者：Ruikang Zhou、Changsheng Sun、Mark Huasong Meng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dd84080b93b1)

> 现有越狱攻击综述多按“如何执行”（如提示工程、梯度优化）分类，导致无法解释“为何成功”，防御设计缺乏针对性。本文提出“技术-操作”双轴分类框架，将攻击映射至LLM生命周期中的具体漏洞（训练/推理衍生），并量化其与部署约束的关联。该框架通过相关性分析揭示了攻击策略与模型架构缺陷的结构性耦合，为预测性防御提供了机制依据，但其分类边界对多模态及系统级隔离场景的覆盖仍显不足。

】

---

【InferPilot: Autonomous Inference Attacks Against ML Services With LLM-Based Agents ｜自动化推理攻击代理

作者：Yixin Wu、Rui Wen、Chi Cui 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_739487a9ea85)

> 机器学习服务部署后，非专家难以独立完成成员推断、模型窃取等推理攻击以评估隐私与知识产权风险，而现有通用代理框架在复杂配置搜索中频繁失效。InferPilot 通过多代理隔离架构与任务特定动作空间，将黑盒推理攻击自动化，使非专家能以极低门槛获得接近专家水平的风险评估报告。该工作验证了大语言模型代理在安全评估领域的可行性，但其对目标服务内部结构的依赖与对特定攻击类型的覆盖局限，限制了其在真实异构环境中的泛化能力。

】

---

【Know Thy Enemy: Securing LLMs Against Prompt Injection via Diverse Data Synthesis and Instruction-Level Chain-of-Thought Learning ｜指令级思维链对齐防御提示注入

研究机构：中国科学院、中国科学院大学

作者：Zhiyuan Chang、Mingyang Li、Yuekai Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04666)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04666)

> 提示注入（Prompt Injection, PI）防御的核心困境在于模型无法区分系统指令与外部数据，且现有模型增强方法仅依赖隐式的角色边界学习，难以应对语义边界模糊的复杂注入。本文切入点在于将防御任务从“区分来源”转化为“分析指令冲突”，通过构建覆盖多向量、多位置的合成数据集，并引入基于情境意识模型的指令级思维链（Instruction-Level Chain-of-Thought, IL-CoT）进行监督微调。该方法在四个开源大语言模型（LLM）上实现了92.5%至98.0%的防御率，但未在标准代理基准上验证其泛化性，且推理时的计算开销未量化。

】

---

【Pattern Enhanced Multi-Turn Jailbreaking: Exploiting Structural Vulnerabilities in Large Language Models ｜模式增强多轮越狱攻击

研究机构：日本东京科学大学、日本理化学研究所

作者：Ragib Amin Nihal、Rui Wen、Kazuhiro Nakadai 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08859)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08859)

> 多轮越狱攻击旨在利用对话上下文累积效应突破大语言模型的安全对齐，但现有方法多依赖启发式随机探索，缺乏对模型结构性弱点的系统性揭示。本文切入点在于将语言学对话模式引入攻击框架，通过预定义的五种模式约束搜索空间，实现从“盲目试探”到“结构化探测”的转变。其核心做法是构建模式管理器监控阶段进展与语义依从度，在十二个模型上验证了模式-危害类别的交互脆弱性。该框架揭示了单一防御无法泛化至所有对话模式的局限，但其攻击效率受限于单次尝试预算，且未与最新强化学习基线进行同协议对比，SOTA地位存疑。

】

---

【RAP-ID: Mechanistic Prompt Injection Detection via Impostor Behavior Analysis ｜基于内部状态动态的提示注入检测

作者：Yuchen Yang、Lei Peng、Yujie He 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6ec8d7052439)

> 大语言模型（LLM）在代理系统中难以区分系统指令与外部数据，导致提示注入攻击频发。现有外部护栏模型引入高延迟，而单一内部启发式方法误报率过高。RAP-ID 将注入攻击形式化为“语义模仿”与“注意力劫持”双过程，通过单次前向传播融合三个内部信号实现无训练检测。该方法在直接注入场景下表现优异，但在复杂代理间接注入场景中的防御能力仍显不足，其通用性边界尚待厘清。

】

---

【Rejection-to-Acceptance Transition: Model Editing-Based Jailbreak Backdoor Injection Not Limited to Few Output Tokens ｜表示转移引导的越狱后门注入

作者：Shiji Yang、Min Cai、Hao Xiong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4167d275552)

> 大语言模型（LLM）的安全对齐机制常被外部提示优化攻击绕过，但此类攻击缺乏持久性且易被检测。现有基于模型编辑的越狱后门方法依赖绑定特定短语，导致攻击效率随绑定数量增加而急剧下降。JEST 摒弃短语绑定，通过主成分分析（PCA）建模拒绝与接受域，直接劫持 LLM 内部表示实现域转移。该方法在白盒场景下显著提升了攻击效率与成功率，但其对模型内部状态的破坏是否会被现有系统级防御机制识别，仍存疑。

】

---

【Rethinking Assessments of Prompt Injection Attacks ｜提示注入攻击评估框架的重构

作者：Chi Cui、Yixin Wu、Michael Backes 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e97da3ed2323)

> 提示注入（Prompt Injection）评估长期受限于实验室场景的简化假设，导致对真实应用风险的严重低估。现有基准多聚焦于合规任务与简单指令，无法捕捉非合规内容在复杂系统提示下的绕过机制。本文通过构建涵盖真实 GPTs 应用、非合规注入任务及复杂越狱指令的八维评估框架，量化了不同组件对攻击成功率的影响。该工作揭示了真实场景下防御机制的脆弱性，但其结论受限于未纳入系统级隔离防御的对比。

】

---

【Robustness via Referencing: Defending against Prompt Injection Attacks by Referencing the Executed Instruction ｜指令引用过滤防御

作者：Yulin Chen、Haoran Li、Yuan Sui 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2504.20472)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_254d4f83bdb4)

> 提示注入攻击利用大语言模型（LLM）无法区分指令与数据的缺陷，导致模型执行恶意指令。现有防御多采用抑制策略，强行约束模型遵循原始指令，但实验表明这种抑制往往失效且损害通用能力。本文切入点在于利用而非抑制模型的指令遵循能力，通过提示模型显式引用所执行指令的标签，再基于标签过滤无关响应。该方法在QA场景下将攻击成功率（ASR）降至接近0%，但未验证代理工具调用场景下的鲁棒性，其依赖模型正确生成引用的假设在复杂交互中是否成立存疑。

】
