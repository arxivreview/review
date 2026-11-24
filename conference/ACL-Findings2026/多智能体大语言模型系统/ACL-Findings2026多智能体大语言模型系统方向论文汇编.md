# ACL-Findings2026 · 多智能体大语言模型系统方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Identifying Collective Intelligence Factor in LLM Agent Groups for Generalizable Multi-Agent System Design ｜人工集体智能（ACI）因子提取与泛化预测

作者：Zhilun Zhou、Zihan Liu、Jiahe Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ecf56b8171c8)

> 多智能体系统（MAS）研究长期聚焦于特定任务的性能优化，却忽略了群体是否具备跨任务的通用能力。现有方法如 GPTSwarm 和 G-Designer 虽能优化拓扑，但其性能提升依赖于特定任务分布，缺乏对群体“通用智力”的量化度量。本文借鉴人类集体智能（CI）理论，通过因子分析从 108 个 LLM 智能体群体中提取出解释 66.3% 方差的人工集体智能（ACI）因子，并验证其作为正则项可提升 MAS 优化算法在未见任务上的泛化能力。这一发现为 MAS 设计提供了超越单任务指标的通用性视角，但其预测模型在复杂异构场景下的鲁棒性仍存疑。

】

---

【Interactive Learning for LLM Reasoning ｜交互式学习用于大语言模型推理

研究机构：香港科技大学、中山大学

作者：Hehai Lin、Shilei Cao、Sudong Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26306)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26306)

> 多智能体大语言模型系统（Multi-Agent LLM Systems, MAS）旨在通过协作突破单模型推理局限，但现有方法在推理阶段仍需重新执行整个智能体系统，导致部署成本高且与人类“通过交流内化知识后独立解题”的认知模式不符。ILR 提出在训练阶段引入多智能体交互，使单个大语言模型（Large Language Model, LLM）在推理时能独立解决复杂问题。该方法通过动态交互模块模拟人类讨论，结合感知校准模块优化奖励信号，利用组相对策略优化（Group Relative Policy Optimization, GRPO）更新模型参数。ILR 在数学推理基准上超越了单智能体与多智能体基线，但其效果依赖于特定模型组合，且未验证在更广泛任务类型上的泛化能力。

】

---

【LinguaGame: A Linguistically Grounded Game-Theoretic Paradigm for Multi-Agent Dialogue Generation ｜基于信号博弈的多智能体对话生成

作者：Yuxiao Ye、Yiming Zhang、Yiran Rex Ma 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_42ec25bbbb9a)

> 多智能体系统（MAS）在复杂任务中常因智能体间语义对齐失败导致沟通低效，现有架构优化方法忽视了交互过程本身的策略性。本文切入点在于将对话建模为信号博弈，通过意图-策略抽象与无训练均衡近似算法，在推理时动态调整话语选择以最大化语义传达效率。该方法在模拟法庭与辩论场景中显著提升了对话质量，但其泛化性受限于特定领域意图库的设计，且缺乏通用推理基准的验证。

】

---

【TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems ｜一次性异构拓扑生成

研究机构：中国科学技术大学、华东师范大学

作者：Rui Sun、Jie Ding、Chenghua Gong 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10120)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10120)

> 多智能体系统（MAS）在复杂任务中依赖通信拓扑协调，但主流时空迭代范式因多轮对话导致Token开销激增且存在结构冗余。现有方法在效率与性能间难以兼得，本文切入点在于将多轮交互压缩为单步异构图生成。TOPODIM通过自回归解码器一次性生成包含条件、反馈、辩论三种边类型的稀疏拓扑，并采用去中心化蒸馏实现本地决策。该方法在降低46.41% Token消耗的同时提升1.50%平均性能，但其对强骨干模型的依赖及单次生成缺乏错误修正机制的潜在风险尚存疑。

】
