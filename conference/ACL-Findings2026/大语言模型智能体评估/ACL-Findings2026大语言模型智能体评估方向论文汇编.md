# ACL-Findings2026 · 大语言模型智能体评估方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Survey on Evaluation of LLM-based Agents ｜LLM智能体评估综述：从静态基准到动态轨迹审计

研究机构：以色列耶路撒冷希伯来大学、IBM研究院

作者：Asaf Yehudai、Lilach Eden、Alan Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a8c7105e8291)

> 大语言模型（LLM）智能体评估面临的核心矛盾是静态基准无法捕捉动态交互中的过程质量。现有方法多聚焦单一任务或孤立能力，导致评估碎片化且难以区分模型能力与框架效应。本文切入点在于构建统一评估基础设施并引入全路径过程审计。通过模块化组件与声明式规范，系统性整合了从能力测试到应用部署的多维评估体系。该综述提供了领域认知地图，但其对长时程状态漂移的量化方法仍显不足。

】

---

【AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation ｜环境感知智能体评估基准

研究机构：中国科学技术大学、新加坡国立大学

作者：Wentao Shi、Yu Wang、Yuyang Zhao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18240)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18240)

> 随着强化学习（RL）在长程智能体训练中的规模化应用，如何在新环境中可靠验证智能体行为成为核心瓶颈。现有规则验证器无法泛化至复杂场景，而 LLM-as-a-Judge 仅依赖表面文本信号，缺乏对环境状态的直接访问。本文提出 AJ-Bench，首个系统评估 Agent-as-a-Judge 能力的多域基准，通过赋予评估者工具与环境交互权限，实现从静态文本判断到动态证据获取的范式转变。该基准填补了评估者能力量化空白，但其绝对性能（平均 F1 0.72）仍远未饱和，揭示了当前评估智能体在复杂多步行为验证中的显著局限。

】

---

【SafeEvalAgent: Toward Agentic and Self-Evolving Safety Evaluation of LLMs ｜法规驱动的自演化智能体安全评估

研究机构：复旦大学、华东师范大学

作者：Yixu Wang、Xin Wang、Yang Yao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26100)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26100)

> 现有LLM安全评估依赖静态人工基准，无法应对快速演变的攻击向量与动态更新的法规标准，导致“合规”模型在新兴威胁下失效。SafeEvalAgent通过多智能体协作，将非结构化法规自动转化为可测试知识库，并引入自演化循环，根据目标模型的失败模式动态生成更具针对性的测试用例。该框架在11个前沿模型上验证了自演化机制能显著降低模型安全评分，揭示静态评估的盲区。其价值在于实现了从“一次性审计”到“持续对抗”的范式转变，但评估结果对初始种子问题的敏感性及计算成本未得到充分控制。

】

---

【The Agent's First Day: Benchmarking Learning, Exploration, and Scheduling in the Workplace Scenarios ｜动态职场环境下的智能体鲁棒性评估：Trainee-Bench

研究机构：复旦大学、浙江大学

作者：Daocheng Fu、Jianbiao Mei、Rong Wu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.08173)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08173)

> 现有智能体基准多聚焦于静态环境下的性能上限，忽视了真实部署中流式任务调度、不确定性探索及持续学习失效等鲁棒性问题。Trainee-Bench 通过规则模板与随机实例化构建动态复合场景，强制智能体在部分可观测条件下进行多任务并发处理与经验迁移。该基准揭示了当前 SOTA 模型在动态环境中的显著短板，特别是持续学习机制可能导致的性能负迁移。其价值在于将评估从“能否做对”转向“能否在混乱中稳定做对”，但受限于人工规则的可扩展性，其结论在更复杂因果链场景中的普适性尚存疑。

】
