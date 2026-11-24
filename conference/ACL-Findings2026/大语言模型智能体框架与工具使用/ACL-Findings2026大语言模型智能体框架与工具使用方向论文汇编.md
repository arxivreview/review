# ACL-Findings2026 · 大语言模型智能体框架与工具使用方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading ｜AlphaQuanter：端到端工具增强智能体强化学习框架用于股票交易

作者：Zheye Deng、Weixiang Yan、Changlong Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d56c89d7f4c1)

> 自动化交易的核心矛盾在于如何整合多源异构信号并实现风险校准的决策，而现有大语言模型（LLM）智能体因缺乏主动工具编排与证据可追溯性，难以在部分可观测市场中建立可信决策轨迹。AlphaQuanter 将 ReAct 范式改造为“规划-获取-推理-行动”循环，并采用可验证奖励的强化学习（Reinforcement Learning, RL）端到端优化单智能体策略。该框架在回测中实现了显著的年化收益率提升，但其有效性局限于特定历史区间，且未解决实时市场中的延迟与过拟合风险。

】

---

【EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis ｜程序化环境合成框架 EnvScaler

研究机构：中国人民大学

作者：Xiaoshuai Song、Haofei Chang、Guanting Dong 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05808)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05808)

> 大语言模型智能体在长程任务中依赖外部工具交互，但真实环境访问受限、LLM模拟环境存在幻觉、人工构建沙箱难以规模化，导致高质量训练数据稀缺。现有环境合成方法或依赖预置工具集，或缺乏自动化质量评估，无法支撑大规模强化学习训练。EnvScaler 通过程序化代码生成可执行沙箱，结合双智能体迭代评估与规则化轨迹验证，实现了从文本资源到可训练环境的自动化闭环。该框架验证了合成环境对多轮多工具任务性能的显著提升，但其绝对性能仍低于当前 SOTA，且环境多样性对泛化的具体贡献机制尚未量化。

】

---

【FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments ｜失败感知元智能体框架

研究机构：美国亚利桑那州立大学

作者：Amir Saeidi、Venkatesh Mishra、Souradeep Mukhopadhyay 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.25135)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_910474489371)

> 交互式工具使用场景中，开源小模型因上下文窗口受限与推理能力不足，在长程对话中面临严重的错误累积问题。现有静态多智能体框架（如IRMA）通过全量注入辅助智能体来缓解此问题，但引入了高昂的Token开销且未能针对特定模型的失败模式进行优化，导致性能波动。本文提出FAMA框架，通过两阶段机制先诊断基线智能体的主导失败类型，再动态激活最小化的专用智能体子集以注入针对性上下文。该方法在资源受限条件下实现了显著的准确率提升，但其依赖预定义智能体池与错误分类体系，对未知失败模式的泛化能力存疑。

】

---

【MAXS: Meta-Adaptive Exploration with LLM Agents ｜元自适应探索框架

研究机构：新加坡南洋理工大学、新加坡国立大学

作者：Jian Zhang、Zhiyuan Wang、Zhangqi Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09259)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09259)

> 大语言模型智能体在推理时面临局部短视与轨迹不稳定两大瓶颈，导致工具调用决策缺乏前瞻且易发散。现有方法如思维链（Chain-of-Thought, CoT）缺乏全局视野，而蒙特卡洛树搜索（Monte Carlo Tree Search, MCTS）计算成本过高。MAXS通过轻量级前瞻滚动与复合价值函数，在推理阶段动态平衡探索深度与稳定性。该框架在数学推理任务上以极低Token成本实现了性能突破，但其对非数学类开放域工具调用的泛化能力存疑。

】

---

【ToolCPT: Improving Tool Utilization in LLM Agents via Continuous Pre-training ｜工具持续预训练

作者：Yifan Yang、Jinghui Lu、Evadeng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7952d3e0eb5)

> 大语言模型智能体在分布外工具调用中表现受限，根源在于现有后训练与测试时方法仅让模型学习调用模式，而非内化工具功能知识。ToolCPT 将工具知识获取前移至持续预训练阶段，通过挖掘真实代码库构建代理工具并合成结构化知识语料，使模型在权重层面建立对工具实现、交互协议及错误反馈的深层理解。该方法在 7B/8B 基座模型上验证了预训练内化工具知识的有效性，但其静态模拟特性与缺乏真实执行反馈的局限，使其在动态环境适应性与长程任务泛化上仍存疑。

】
