# ACL-Findings2026 · 机器人、自动驾驶与具身智能方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
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

---

【Text-to-TrajVis: Enabling Trajectory Data Visualizations from Natural Language Questions ｜自然语言轨迹可视化查询

研究机构：吉林大学、香港科技大学

作者：Tian Bai、Huiyan Ying、Kailong Suo 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e0fa0feabc2d)

> 轨迹数据可视化长期依赖专业数据库查询语言与编程技能，非专家用户难以直观表达分析需求。现有自然语言到可视化（NL2VIS）方法虽能处理通用图表，但缺乏针对轨迹时空语义的结构化解析能力，导致地理实体与时间表达解析错误频发。本文提出 Text-to-TrajVis 任务，定义轨迹可视化语言（TVL）作为中间表示，并构建首个基准数据集 TrajVL。通过引入检索增强与标准化后处理框架 TRCAT，显著提升了大语言模型在复杂时空查询下的代码生成准确率，但该方法依赖外部检索库，其泛化边界尚待验证。

】

---

【TravelBehaviorQA: A Benchmark Dataset for Behavioral Interpretation of GPS Trajectories ｜轨迹行为问答基准

研究机构：美国马里兰大学帕克分校

作者：Dongyang Zhen、Niping Duan、Huan Zhou 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_62220a8bf809)

> 轨迹理解旨在从非文本的GPS序列中提取人类移动意图，但现有方法多聚焦于下一位置预测或模式分类，缺乏对长程行为叙事能力的系统性评估。当前大语言模型（LLM）虽具备语义推理能力，却难以直接处理连续时空坐标，导致事实提取与行为抽象之间存在显著鸿沟。本文通过将轨迹重构为语言推理任务，构建了包含143,238个问答对的大规模基准，以量化模型在确定性事实检索与开放式叙事生成上的表现。该工作揭示了模型规模并非解决轨迹理解瓶颈的唯一因素，但单一数据集的局限使其泛化能力存疑。

】

---

【Where Did It Go Wrong? Capability-Oriented Failure Attribution for Vision-and-Language Navigation Agents ｜具身智能体能力级故障归因测试

研究机构：中国科学院、中国科学院大学

作者：Jianming Chen、Yawen Wang、Junjie Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.25161)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.25161)

> 具身智能体在视觉语言导航（Vision-Language Navigation, VLN）等安全关键任务中，因感知、记忆、规划与决策能力的强耦合导致错误级联，传统系统级测试无法定位具体失效环节。现有模糊测试框架仅能判定任务失败，缺乏对能力级错误的独立评估与归因机制，阻碍了针对性修复。CanTest 通过自适应指令变异生成测试用例，构建独立能力预言机（Oracle）并引入反事实归因机制，实现了从任务失败到具体能力错误的精准映射。该方法在三个先进 VLN 模型上发现了比最强基线多 23.34% 至 33.70% 的故障案例，但预言机对端到端模型内部状态的捕捉准确性及真实世界无监督测试的可行性仍存疑。

】
