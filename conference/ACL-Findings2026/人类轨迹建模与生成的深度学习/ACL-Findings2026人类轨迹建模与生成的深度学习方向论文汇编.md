# ACL-Findings2026 · 人类轨迹建模与生成的深度学习方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

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
