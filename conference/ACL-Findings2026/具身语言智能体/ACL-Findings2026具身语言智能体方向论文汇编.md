# ACL-Findings2026 · 具身语言智能体方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GaLa: Hypergraph-Guided Visual Language Models for Procedural Planning ｜超图引导的视觉语言模型程序规划

研究机构：哈尔滨工业大学、丰田研究所

作者：Kun Wang、Li Yiming、Mingcheng Qu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7f543526250b)

> 具身智能体在执行复杂指令时，常因视觉场景语义碎片化而陷入逻辑死锁，现有视觉语言模型（VLM）仅依赖显式几何坐标，忽略了物体属性隐含的高阶空间关系。GaLa 通过引入超图结构将孤立物体聚合为功能区域，并利用三视图对比学习强化语义一致性，解决了 VLM 在程序规划中缺乏结构化场景认知的问题。该方法在 ActPlan-1K 和 ALFRED 基准上显著提升了执行成功率，但其性能增益是否完全归因于超图结构而非骨干模型优势，仍需更严格的消融实验验证。

】

---

【Seeing Isn't Believing: Mitigating Belief Inertia via Active Intervention in Embodied Agents ｜具身智能体信念惯性缓解机制

研究机构：香港理工大学、四川大学

作者：Hanlin Wang、Chak Tou Leong、Jian Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17252)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17252)

> 具身智能体在长时程任务中常因内部信念与外部观察脱节而执行冗余动作，这一认知偏差被命名为信念惯性。现有基于提示或强化学习的方法虽能优化动作生成，却默认信念更新是隐式且被动的，导致智能体在环境状态变化时仍固守旧有预期。本文提出估计-验证-更新（Estimate-Verify-Update, EVU）机制，通过显式文本信念状态主动干预认知过程。该机制在多个基准上显著提升了任务成功率，但其有效性主要局限于文本模态的小模型场景，向视觉-语言-动作（Vision-Language-Action, VLA）大模型的迁移能力尚存疑。

】
