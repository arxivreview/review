# ICLR2026 · AI智能体记忆架构方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ASSOMEM: SCALABLE MEMORY QA WITH MULTI SIGNAL ASSOCIATIVE RETRIEVAL ｜关联记忆图驱动的多信号检索框架

研究机构：美国伍斯特理工学院

作者：Kai Zhang、Xinyuan Zhang、Ejaz Ahmed 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_20515880)

> 大规模个人助理记忆库面临相似项累积导致的检索退化，现有基于语义距离的RAG方法难以区分高度相似的噪声记忆。AssoMem通过构建“线索-话语”二部图，引入重要性维度，弥补了纯相关性检索在推荐类查询中的失效。该方法利用互信息动态融合相关性、重要性与时间信号，并配合去噪微调提升生成鲁棒性。其在LongMemEval-large上显著优于基线，但绝对准确率仍低于当前SOTA，且依赖合成数据验证，真实场景泛化能力存疑。

】

---

【MEMGEN: WEAVING GENERATIVE LATENT MEMORY FOR SELF-EVOLVING AGENTS ｜生成式潜在记忆框架

研究机构：新加坡国立大学

作者：Guibin Zhang、Muxin Fu、Shuicheng YAN

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_45129363)

> 智能体记忆旨在解决大语言模型（LLM）原生无状态性与长程任务需求间的矛盾，但现有参数化与检索式记忆均无法实现推理与记忆的动态交织。MemGen 提出一种生成式潜在记忆框架，通过强化学习训练的触发器与记忆编织器，在推理过程中动态生成机器原生的潜在记忆。该框架在多个基准上显著超越基线，并自发演化出类人记忆层级，但其对长程对话一致性的影响及隐私合规性仍存疑。

】

---

【REMem: Reasoning with Episodic Memory in Language Agent ｜情景记忆推理框架 REMem

研究机构：美国俄亥俄州立大学

作者：Yiheng Shu、Saisri Padmaja Jonnalagedda、Xiang Gao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.13530)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.13530)

> 语言智能体长期依赖语义记忆范式，导致其无法在时空轴上精确重构具体事件并进行跨事件逻辑推理。现有方法或丢失连贯情境，或仅做简单相似度匹配，缺乏显式的事件建模与复杂推理能力。REMem 通过构建包含时间感知摘要与事实的混合记忆图，并引入代理式多步工具调用推理，解决了这一瓶颈。该框架在时间推理基准上取得突破，但其在通用对话记忆任务上的表现仍落后于当前最先进系统，且多步推理带来的计算开销尚未被充分量化。

】
