# ACL-Findings2026 · 知识追踪与认知诊断方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Behavior-Aware Item Modeling via Dynamic Procedural Solution Representations for Knowledge Tracing ｜行为感知题目建模

研究机构：瑞士苏黎世联邦理工学院

作者：Jun Seo、Sangwon Ryu、Heejin Do 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08260)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08260)

> 知识追踪（KT）旨在通过历史交互预测学生未来表现，但现有方法多将题目视为静态向量，忽略了求解过程中的动态认知需求。本文指出，静态嵌入无法区分同一知识点下不同解题阶段的难度差异，导致模型在重复作答时缺乏适应性。BAIM 利用推理语言模型（RLM）离线提取题目在Polya四阶段解题过程中的嵌入轨迹，并通过上下文条件路由机制动态选择关键阶段。该框架在XES3G5M数据集上实现了83.21 AUC，显著优于预训练基线，但其依赖离线RLM推理的假设是否适用于实时交互场景仍存疑。

】

---

【RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation ｜检索增强跨平台知识追踪

作者：Zhiyi Duan、Hongyu Yuan、Rui Liu

论文原文见 [arXiv](https://arxiv.org/abs/2604.10960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10960)

> 知识追踪（Knowledge Tracing, KT）旨在从历史交互中预测学生未来表现，但传统深度模型受限于封闭标识符与黑盒隐状态，难以跨平台迁移且缺乏教学可解释性。现有大语言模型（LLM）方案在提示工程中易产生幻觉，在微调中则加剧对源平台分布的依赖，无法同时满足泛化与可靠性需求。RAG-KT通过构建多源异构图并引入多视图融合检索，将LLM推理锚定在结构化外部知识上，实现了零样本下的跨平台预测与归因解释。该方法在冷启动场景下显著优于基线，但其推理延迟与外部知识库构建成本是否抵消了精度收益，仍缺乏量化验证。

】

---

【Tracing Mathematical Proficiency Through Problem-Solving Processes ｜基于解题过程的知识追踪

研究机构：韩国延世大学、韩国首尔大学

作者：Jungyang Park、Suho Kang、Jaewoo Park 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.00311)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00311)

> 知识追踪（Knowledge Tracing, KT）旨在通过历史交互预测学生未来表现，但传统方法仅依赖二值正确率，无法区分粗心与概念误解，导致教学干预缺乏针对性。现有深度模型虽提升了精度，却因黑盒性质难以提供错误归因，且冷启动场景下预测不稳定。本文提出KT-PSP任务与STATUSKT框架，利用三阶段大语言模型（LLM）流水线从手写解题过程中提取数学能力（Mathematical Proficiency, MP）信号作为辅助输入。该方案在自建数据集上验证了过程信号对预测精度与可解释性的双重增益，但受限于数据规模与单一学科领域，其跨平台泛化能力尚存疑。

】
