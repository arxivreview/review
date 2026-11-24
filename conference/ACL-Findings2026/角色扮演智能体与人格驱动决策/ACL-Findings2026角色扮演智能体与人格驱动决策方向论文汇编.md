# ACL-Findings2026 · 角色扮演智能体与人格驱动决策方向论文汇编

> 本方向共 13 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ActorMind: Emulating Human Actor Reasoning for Speech Role-Playing ｜语音角色扮演：基于多智能体思维链的无训练推理框架

研究机构：香港科技大学

作者：Xi Chen、Wei Xue、Yike Guo

论文原文见 [arXiv](https://arxiv.org/abs/2604.11103)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11103)

> 语音角色扮演旨在让模型以特定角色的音色、情感与语调自发地生成对话，而非仅合成文本。现有大语言-音频模型（LLAMs）受限于极小的音色库，而文本转语音（TTS）模型缺乏对场景与角色情感的深层推理能力，导致生成的语音虽清晰却缺乏“人格”。本文提出 ActorMind，一个模拟人类演员表演过程的多智能体思维链（CoT）推理框架，通过“眼-耳-脑-口”四个智能体协同工作，在无训练条件下实现语音角色的情感自发表达。该框架在自建基准上显著优于基线，但其有效性高度依赖特定剧集数据，跨场景泛化能力存疑。

】

---

【AdaMARP: An Adaptive Multi-Agent Interaction Framework for General Immersive Role-Playing ｜自适应多智能体交互框架

研究机构：浙江大学

作者：Zhenhua Xu、Dongsheng Chen、Shuo Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11007)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11007)

> 通用角色扮演旨在让大语言模型模拟任意用户定义的角色，但现有系统多局限于静态场景与固定角色，缺乏对动态环境信息的建模，导致叙事沉浸感不足。本文切入点在于将环境状态作为一等公民信号，并引入独立的场景管理器代理，通过离散动作空间实现多角色编排、场景切换与动态角色引入。具体做法是构建包含思维、动作、环境与言语的沉浸式消息格式，并训练专用数据集以监督演员模型与场景管理器。该框架在轨迹级评估中展现了小模型超越部分闭源大模型的能力，但其对长程认知保真度的贡献尚未在标准基准上得到验证。

】

---

【HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing ｜双层思维与生成式奖励的角色扮演强化学习

研究机构：复旦大学、MiniMax

作者：Chengyu Du、Xintao Wang、Aili Chen 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21459)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21459)

> 导读 角色扮演智能体（Role-Playing Agents, RPAs）的核心矛盾在于模型能模仿角色语气，却难以复现驱动行为的内在动机，导致长程对话中认知逻辑断裂。现有方法要么缺乏显式推理轨迹的监督数据，要么依赖静态规则或可验证事实构建奖励信号，无法适应场景动态变化。本文提出 HER 框架，通过分离系统思维与角色思维的双层结构，结合反向合成数据管道与生成式奖励模型（Generative Reward Model, GenRM），在 Qwen3-32B 上实现认知层面的角色模拟。该框架在 CoSER 基准上取得 53.12 分，显著优于同规模基线，但绝对性能仍落后于顶级商业模型，且其原则集静态化限制了长程场景适应性。

】

---

【MA2P: A Meta-Cognitive Autonomous Intelligent Agents Framework for Complex Persuasion ｜元认知自主智能体框架

研究机构：东南大学

作者：Dingyi Zhang、Ziqing Zhuang、Linhai Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_731518519446)

> 复杂说服对话要求说服者不仅识别被说服者的潜在心理状态，还需将其转化为可执行的多轮策略行动，现有大语言模型往往止步于泛化建议或出现跨域性能剧烈波动。MA2P 通过引入元认知配置器与结构化知识库，将说服过程重构为“规划-行动-反思”的闭环，实现了从状态识别到策略落地的跨越。该框架以无训练、即插即用的方式显著提升了说服成功率并降低了跨域方差，但其元策略选择仅依赖历史成功计数，缺乏对策略语义相似性的考量，在冷启动场景下的鲁棒性仍存疑。

】

---

【Memory-Driven Role-Playing: Evaluation and Enhancement of Persona Knowledge Utilization in LLMs ｜记忆驱动角色扮演：基于结构化Schema与显式检索协议的评估与增强

研究机构：哈尔滨工业大学、澳大利亚麦考瑞大学

作者：Kai Wang、Haoyang You、Yang Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19313)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19313)

> 长程对话中角色身份漂移的核心瓶颈在于模型无法自主从扁平化角色档案中检索并应用特定情境下的知识。现有方法依赖额外场景提示或整体评分，掩盖了记忆检索失效的具体环节。本文提出记忆驱动角色扮演（Memory-Driven Role-Playing, MDRP）范式，将角色知识视为长期记忆（LTM），对话上下文视为短期记忆（STM），通过结构化叙事Schema与Magic-If协议实现无参数检索。该框架在单轮基准上验证了提示工程的有效性，但其对多轮动态状态演化的适用性存疑。

】

---

【MENTOR: Mitigating Identity Drift in Dynamic Role-Playing via Dual-Chain Structured Memory ｜双链结构化记忆缓解动态角色扮演身份漂移

研究机构：中国科学院、中国科学院大学

作者：Zhu Zhuoning、Xingyu Gao、Hailong Shi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9465be4e47c6)

> 长程多用户交互中，大语言模型（LLM）常因上下文污染导致角色边界模糊，即身份漂移。现有检索增强生成（RAG）依赖语义相似度，无法区分角色归属，导致跨角色信息泄露。MENTOR 提出无参数双链记忆架构，通过物理隔离角色工作记忆与全局事件日志，并结合知识图谱验证信息可接受性，在高频切换场景下将平均得分从 0.46 提升至 0.75。该架构有效抑制了“伪对齐”现象，但其对静态单角色场景的适用性及门控阈值敏感性尚未充分验证。

】

---

【PED: Route-Decoupled Diagnostics for Persona Consistency in Spoken Agents ｜语音角色扮演智能体路由解耦诊断框架

研究机构：华为、天津大学

作者：Weihao Liu、Junrui Wei、Zhao Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcea27350d73)

> 语音角色扮演智能体在长程交互中常出现角色失真，但现有评估仅报告聚合分数，无法定位故障源于文本生成还是声学实现。PED 框架将角色表达解耦为文本与音频两条独立路由，通过共享情感空间投影实现轮次级、路由级的故障归因。该框架在端到端与级联两种架构下验证了路由分离性受限于参考锚点重叠，且文本-音频一致性呈弱耦合。其诊断价值在于将黑盒评分转化为可操作的调试信号，但受限于单一对话脚本与固定投影器，结论的普适性尚待检验。

】

---

【PersonaArena: Dynamic Simulation for Evaluating and Enhancing Persona-Level Role-Playing in Large Language Models ｜动态社交模拟评估与增强框架

研究机构：深圳大学、微软研究院

作者：Wenlong Shi、Jianxun Lian、Mingqi Wu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17044)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17044)

> 角色扮演大语言模型（LLM）在长程交互中面临身份漂移与认知浅层化问题，现有基准多聚焦于虚构角色的静态问答，难以衡量日常社交互动的真实性与适应性。PersonaArena 通过构建基于真实用户生成内容的人格库，利用多智能体沙盒环境激发动态多轮交互，并引入多智能体辩论裁判机制进行多维评估。该框架不仅提供了评估工具，还通过自生成轨迹进行监督微调（SFT）与直接偏好优化（DPO），验证了数据增强对模型人格一致性的提升作用。其价值在于填补了“人格级”评估空白，但缺乏与虚构角色基准的交叉验证，且高计算成本限制了大规模筛选的实用性。

】

---

【PersonaForge: Psychology-Grounded Dual-Process Architecture for Personality-Consistent Role-Playing Agents ｜基于心理学双过程架构的角色扮演智能体

研究机构：武汉大学

作者：Jizhou Tong、Sirui Zou

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_14ea4afcb1b5)

> 角色扮演智能体在长程交互中面临身份漂移与认知浅层化的双重困境，现有微调或检索方法难以兼顾风格稳定性与心理逻辑自洽。本文切入点在于将心理学理论中的大五人格与防御机制转化为可计算的结构化约束，而非依赖自然语言描述。通过构建三层人格架构与选择性双过程生成机制，PersonaForge 在无需微调的情况下实现了长程一致性。该方法在RoleBench上取得73.2%的胜率，但其在极端长程场景下的稳定性及跨文化框架的普适性仍存疑。

】

---

【RoleCDE: Benchmarking and Mitigating Role–Alignment Trade-offs in Role-Playing Agents ｜角色-对齐价值解耦评估与缓解

研究机构：中国人民大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4d7d6b053209)

> 角色扮演智能体（Role-Playing Agents, RPAs）在长程交互中面临的核心挑战不仅是风格漂移，更在于当角色特定利益与模型内置的对齐原则发生冲突时，模型往往丧失角色决策逻辑。现有基准多聚焦于表面保真度，缺乏对深层价值权衡能力的量化手段，导致无法区分模型是真正理解了角色动机，还是机械遵循安全护栏。本文提出 RoleCDE，通过构建大规模结构化认知困境数据集，将角色扮演评估从“风格一致性”转向“价值冲突决策”，并验证了基于该数据的微调能有效缓解模型的对齐偏向。该工作揭示了“角色-价值解耦”这一系统性失效模式，但其单步决策设定是否足以反映真实多轮交互中的动态价值演化，仍存疑。

】

---

【SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation ｜稳定人格驱动智能体模拟

研究机构：英国利兹大学、以色列内盖夫本-古里安大学

作者：Han Luo、Guy Laban

论文原文见 [arXiv](https://arxiv.org/abs/2604.09212)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09212)

> 多轮LLM交互中，智能体常因上下文累积而偏离预设角色，表现为身份漂移与回声现象。现有合成对话框架缺乏对长程稳定性的显式控制，导致生成数据污染下游训练。SPASM通过自我中心上下文投影（ECP）机制，在推理时重构对话历史视角，无需修改模型权重即可抑制漂移。该框架在消除回声方面表现显著，但其在复杂推理场景下的泛化能力尚待验证。

】

---

【Think Before you Write: QA-Guided Reasoning for Character Descriptions in Books ｜问答引导推理用于长文本角色描述生成

研究机构：英国爱丁堡大学

作者：Argyrios Papoudakis、Mirella Lapata、Frank Keller

论文原文见 [arXiv](https://arxiv.org/abs/2604.11435)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11435)

> 长文本角色描述生成要求模型从数十万词的小说中整合分散的角色证据，但现有长上下文模型在直接生成时往往引入幻觉或遗漏关键细节。本文发现，当前大语言模型（LLM）的内置推理模式在该任务上反而降低忠实度，空轨迹表现更优。为此，作者提出解耦推理与生成的两阶段框架，通过问答（QA）轨迹作为中间表示引导描述生成。该框架在忠实度与信息覆盖上优于基线，但其收益高度依赖上下文选择策略，且在增量处理场景中失效。

】

---

【Understanding Generalization in Role-Playing Models via Information Theory ｜角色扮演模型分布偏移下的泛化度量

研究机构：武汉大学

作者：Yongqi Li、Hao Lang、Fei Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.17270)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17270)

> 角色扮演模型在真实部署中因用户、角色或对话结构的分布偏移而性能骤降，现有基于大语言模型裁判的评估方法仅能给出整体分数，无法诊断具体偏移来源。本文切入点在于构建一个信息论框架，将性能下降与分布偏移的统计量直接关联。通过引入推理变量并推导理论上界，该方法实现了可解释的泛化风险量化。这一框架提供了诊断工具，但其对模型实际性能提升的间接性，以及推理机制在训练中的负迁移现象，限制了其作为独立优化策略的适用性。

】
