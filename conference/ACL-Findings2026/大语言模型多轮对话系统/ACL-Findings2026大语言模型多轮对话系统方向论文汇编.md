# ACL-Findings2026 · 大语言模型多轮对话系统方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ACR: Adaptive Context Refactoring via Context Refactoring Operators for Multi-Turn Dialogue ｜自适应上下文重构

研究机构：阿里巴巴集团、香港科技大学

作者：Jiawei Shen、Jia Zhu、Hanghui Guo 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05589)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05589)

> 多轮对话中，模型常因早期错误假设的累积或关键约束被噪声稀释而陷入逻辑死循环，现有方法仅增加信息量却缺乏纠错机制。ACR 指出，被动拼接历史无法解决“上下文惯性”与“状态漂移”，需主动重构历史。该框架通过语义路由动态选择六种重构算子，并采用教师引导自进化训练，将上下文管理与推理解耦。其在QA任务上以极低的Token消耗逼近强化学习性能，但尚未验证在开放式对话中的泛化能力。

】

---

【Context-Agent: Dynamic Discourse Trees for Non-Linear Dialogue ｜动态话语树

研究机构：山东大学

作者：Junan Hu、Shudan Guo、Wenqi Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05552)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05552)

> 多轮对话中，用户常进行话题跳跃或指令细化，导致线性上下文追加产生冗余与注意力稀释，使模型在长程交互中丢失关键约束。现有方法或依赖语义相似度聚类，或采用静态树结构，均无法实时捕捉话语意图驱动的分支演化。本文提出Context-Agent，将对话历史建模为基于话语意图动态演化的话题树森林，并通过路径感知检索实现高效上下文选择。该方法在自建NTM基准上显著提升了任务完成率并降低了Token消耗，但其对轻量级决策模型的依赖及缺乏与主流结构化记忆方法的对比，限制了结论的普适性。

】

---

【LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents ｜多轮智能体技能瓶颈的反事实量化

研究机构：加拿大多伦多大学

作者：Amin Rakhsha、Thomas Hehn、Pietro Mazzaglia 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.16649)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16649)

> 多轮智能体在长程任务中成功率远低于单步准确率，但现有基准无法区分是规划、状态跟踪还是上下文管理导致了失败。传统消融实验因真实环境路径不唯一而难以精确归因，本文通过程序化生成环境实现反事实Oracle干预，量化了三种核心技能的相对重要性。该框架揭示了技能贡献随模型规模与环境特性动态变化，但受限于受控环境的低噪声特性，其结论向真实开放域对话的迁移性仍存疑。

】

---

【MT-OSC: Path for LLMs that Get Lost in Multi-Turn Conversation ｜一次性顺序压缩框架

作者：Jyotika Singh、Fang Tu、Miguel Ballesteros 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0c6fc0e88a13)

> 多轮对话中，用户指令与关键上下文分散在多个轮次，导致大语言模型（LLM）性能显著衰减，而全量追加历史又迅速耗尽上下文窗口并增加延迟。现有压缩方法依赖微调、复杂层级结构或实时检索，难以在不牺牲信息保真度的前提下实现低延迟部署。MT-OSC 提出一种后台异步执行的一次性顺序压缩框架，通过少样本提示的 Condenser 与基于重叠度规则的 Decider 动态精简历史，在 10 轮对话中实现最高 72% 的 Token 削减，同时保持或提升任务准确率。该方案在工程集成上具有显著优势，但其压缩保真度边界与 Decider 规则的泛化能力仍存疑。

】

---

【Progra: Progress-Aware Reinforcement Learning for Multi-Turn Function Calling ｜进度感知强化学习

研究机构：上海交通大学

作者：Huacan Chai、Zijie Cao、Maolin Ran 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_23175b7799fb)

> 多轮函数调用面临的核心困境是模型无法维持对任务全局状态的连贯表征，导致局部动作与全局目标脱节。现有方法要么将多轮轨迹拆解为独立单轮样本训练，要么依赖端到端强化学习却缺乏显式的进度建模，两者均无法解决长程依赖中的状态追踪失效。本文提出PROGRA框架，通过合成包含历史摘要与未来规划的“进度感知”数据，并将其作为条件变量注入基于GRPO的强化学习训练中。该框架在τ-bench和BFCL-V3上显著优于基线，但其性能增益是否完全源于进度感知机制本身，还是受限于特定骨干模型的预训练质量，仍需更严格的控制实验来验证。

】
