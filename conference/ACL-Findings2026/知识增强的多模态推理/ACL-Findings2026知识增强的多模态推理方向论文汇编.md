# ACL-Findings2026 · 知识增强的多模态推理方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG ｜从场景到元素：多粒度证据检索的可验证多模态RAG

研究机构：澳门大学

作者：Guanhua Chen、Chuyue Huang、Yutong Yao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a8df6276edb)

> 多模态检索增强生成（Retrieval-Augmented Generation, RAG）旨在通过外部证据缓解大语言模型（Large Language Models, LLMs）的幻觉，但现有方法常以整图或页面为检索单元，导致细粒度查询与粗粒度证据间的归因断裂。本文指出，可验证性要求将视觉元素作为一等检索目标，而非隐式注意力区域。GranuRAG 通过“检测-检索-归因”三阶段框架，实现了元素级证据的透明审计。该工作填补了部分观测场景下的细粒度对齐空白，但其对静态地标领域的依赖限制了通用性验证。

】

---

【Ground Then Rank: Revisiting Knowledge-Based VQA with Training-Free Entity Identification ｜解耦实体识别与证据重排：训练无关的KB-VQA工作流重构

研究机构：美国伦斯勒理工学院

作者：Qian Ma、Qiong Wu、Zhengyi Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.23881)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.23881)

> 知识增强视觉问答（Knowledge-Based Visual Question Answering, KB-VQA）要求模型在图像像素之外定位细粒度实体并提取支撑证据，但现有多模态检索增强生成（Multimodal Retrieval-Augmented Generation, MM-RAG）方法将实体判别与段落重排耦合于单一评分函数，导致高计算成本与泛化受限。本文切入点在于发现多模态大语言模型（Multimodal Large Language Models, MLLMs）在开放生成中难以命名实体，但在给定候选集时具备显著的判别能力。通过引入“先识别后回答”（Identify-Before-Answer, IBA）框架，将实体选择与文本重排解耦，本文在无需微调的情况下超越了训练式基线，但其性能上限仍受限于静态检索范式，未触及动态多步推理的边界。

】

---

【MDocRAG-RL: Empowering Multi-Modal Document RAG via Complex Visual Reasoning with Reinforcement Learning ｜视觉文档检索增强生成中的细粒度感知与协同优化

研究机构：北京航空航天大学

作者：Zhongyu Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f500bfbaa8f6)

> 多模态大语言模型（MLLMs）在处理包含复杂图表与密集文本的视觉文档时，常因检索嵌入质量低劣及生成阶段视觉细节丢失而陷入推理瓶颈。现有视觉检索增强生成（Visual RAG）系统多将图像直接插入上下文，导致模型无法对关键区域进行细粒度聚焦，且检索器与生成器缺乏协同优化。MDocRAG-RL 通过设计视觉感知动作空间与强化学习（RL）框架，实现了从粗到细的动态信息获取与检索-生成联合训练。该方法在文档问答基准上显著优于现有 RL 基线，但其对长尾实体跨文档关联的适用性仍存疑。

】

---

【VIDA: A Visual Intent-driven Design Assistant for Proactive Multimodal Clarification ｜视觉意图驱动的设计助手

研究机构：香港科技大学

作者：Yanshan Liu、Hongbo Zhang、Zhen Sun 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcba72e613fe)

> 在室内设计等专业咨询场景中，用户初始请求往往存在概念模糊与信息缺失，导致通用视觉语言模型（VLM）生成的澄清问题缺乏策略性且易产生视觉幻觉。现有澄清问题生成（Clarification Question Generation, CQG）方法多依赖文本模态或静态检索，无法在有限轮次内动态权衡关键约束的优先级。本文提出 VIDA，通过两阶段训练框架结合层级化强化学习奖励，使模型在生成澄清问题时严格遵循专家优先级协议。该框架在自建基准上将策略对齐分数提升 20.59%，但受限于单一领域数据规模，其跨领域泛化能力存疑。

】

---

【WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering ｜WikiSeeker：重构视觉语言模型在知识增强多模态推理中的角色

研究机构：中国科学院大学、中国科学院

作者：Yingjian Zhu、Xinming Wang、Kun Ding 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05818)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05818)

> 知识增强多模态推理（Knowledge-Augmented Multimodal Reasoning, KAMR）旨在解决多模态大语言模型在复杂视觉问答中因依赖内部参数化知识而导致的幻觉与知识滞后问题。现有方法普遍将视觉语言模型（Vision-Language Model, VLM）仅作为答案生成器，且检索键局限于图像，导致在视觉内容模糊时检索失效，且VLM在整合检索文本时表现弱于纯文本大语言模型（Large Language Model, LLM）。本文切入点在于重新定义VLM的角色，将其拆分为负责查询改写的Refiner与负责证据验证的Inspector，并引入强化学习优化查询生成。这一架构在静态检索框架内实现了性能跃升，但其单步检索机制与硬路由策略是否限制了其在长程推理任务中的潜力，仍存疑。

】
