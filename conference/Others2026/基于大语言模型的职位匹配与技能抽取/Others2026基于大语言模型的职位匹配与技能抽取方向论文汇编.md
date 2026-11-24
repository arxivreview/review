# Others2026 · 基于大语言模型的职位匹配与技能抽取方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agentic AI for Human Resources: LLM-Driven Candidate Assessment ｜基于LLM的主动列表式锦标赛候选人评估系统

作者：Kamer Ali Yuksel、Abdul Basit Anees、Ashraf Elneima 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.26710)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26710)

> 传统招聘系统依赖关键词匹配或浅层语义相似度，难以捕捉候选人多维能力的复杂权衡，且独立打分或成对比较在大规模候选池中噪声大、扩展性差。本文切入点在于将LLM视为“模糊裁判”，通过小群体列表式排序获取更丰富的偏好信号，并利用概率模型聚合为全局效用。具体做法是构建多智能体框架生成角色特定评分标准，结合主动学习循环动态选择最具信息量的候选子集进行列表式评估，最终通过Plackett-Luce模型推断全局排名。该框架在减少LLM查询次数的同时提升了排序稳定性，但其公平性保证仅停留在结构化标准层面，缺乏因果层面的偏见阻断机制，且未提供与主流检索基准的可比数值。

】

---

【When LLM meets Fuzzy-TOPSIS for Personnel Selection through Automated Profile Analysis ｜基于DistilRoBERTa与模糊TOPSIS的自动化人员筛选框架

作者：Shahria Hoque、Ahmed Akib Jawad Karim、Md. Golam Rabiul Alam 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.22433)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22433)

> 导读 传统招聘依赖主观人工判断，导致评估不一致且难以规模化，而现有AI工具往往牺牲可解释性以换取自动化效率。本文切入点在于将Transformer模型的文本理解能力与模糊多准则决策理论结合，以显式建模人类评估中的主观性与不确定性。具体做法是微调DistilRoBERTa对LinkedIn档案属性进行分类打分，再通过模糊TOPSIS算法聚合为最终排名。该框架在自建数据集上实现了与专家判断的高一致性，但其泛化能力与公平性审计缺失限制了工业级应用的可靠性。

】
