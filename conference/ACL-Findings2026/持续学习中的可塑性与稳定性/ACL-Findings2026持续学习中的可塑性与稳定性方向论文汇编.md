# ACL-Findings2026 · 持续学习中的可塑性与稳定性方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning ｜Agent-Dice：基于几何共识的参数融合框架

研究机构：上海交通大学

作者：Zheng Wu、Xingyu Lou、Xinbei Ma 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8a2ea586e066)

> 导读 LLM Agent在动态环境中持续适应新任务时，面临稳定性与可塑性的根本矛盾：过度保护旧知识阻碍新技能习得，而激进更新则引发灾难性遗忘。现有方法多依赖外部记忆模块或顺序迭代训练，但未能显式区分任务间的共同知识与冲突知识，导致信息干扰或丢失。Agent-Dice通过两阶段参数融合解决此问题：先以几何共识过滤剔除方向冲突的更新，再以曲率加权放大共享语义方向。该方法在GUI与工具使用Agent上验证了有效性，但其离线融合范式能否替代在线动态适应，仍存疑。

】
