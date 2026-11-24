# ACL-Findings2026 · 事件抽取与关系学习方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Causal Evidence Extraction and Triangulation in Crisis Reports using Large Language Models: A ReliefWeb-based Study ｜人道主义报告中的因果证据提取与三角测量

作者：Yuanjun Zhang、Mourad Oussalah

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22879c8d5061)

> 人道主义危机报告冗长且多主题，传统关键词检索与无约束抽取导致大量噪声关系，难以支撑跨情境的决策支持。现有证据合成框架多针对主题纯净的文本，无法处理报告中心的复杂语境。本文提出查询条件化与片段接地两阶段流水线，并引入保留上下文的三角测量方法量化证据收敛性。该方法在专家标注集上实现了高加权F1，但评估规模小且局限于单一干预类型，其泛化能力存疑。

】

---

【CVRH: Cross-modal Variational Role Hypergraph Network via Semantic Enhancement for Multi-modal Event Argument Extraction ｜跨模态变分角色超图网络

作者：Bangze Pan、Yang Li、Ruili Pu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2cd7f2e1137)

> 多模态事件论元抽取（MEAE）旨在从图文混合新闻中识别特定事件的所有参数及其角色，核心难点在于视觉实体与文本实体在语义上的混淆与跨模态关联缺失。现有方法多依赖单模态向量的弱对齐或数据增强，忽略了事件角色作为高阶结构对参数绑定的约束作用。CVRH 通过构建以角色为中心的变分超图，利用 LLM 生成的角色语义先验与动态变分向量初始化超边，显式建模跨模态参数间的高阶关联。该方法在 M2E2 基准上取得了 50.5 的 F1 分数，但缺乏与最新多智能体架构的绝对数值对比，其结构优势在复杂绑定场景下的泛化能力仍存疑。

】

---

【ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction ｜渐进式通用信息抽取

研究机构：小米

作者：Wenda Liu、Song Zhigang、Shuai Nie 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6e7842063e87)

> 通用信息抽取（UIE）旨在用单一模型统一处理命名实体识别（NER）、关系抽取（RE）与事件抽取（EE），但现有大语言模型（LLM）方法常依赖外部辅助信息或复杂验证管线，导致训练复杂且增益有限。ProUIE 提出一种无需外部信息的宏观-中观-微观渐进式学习框架，通过任务难度排序的完整建模、简化目标格式的对齐以及基于步进细粒度奖励的强化学习探索，在 36 个公开数据集上以 4B 参数骨干超越了 11B 参数的指令微调基线。该方法在 NER 和 RE 任务上表现稳健，但在 EE 任务上存在波动，其“无外部约束”的设计假设在复杂结构推理中的普适性仍存疑。

】
