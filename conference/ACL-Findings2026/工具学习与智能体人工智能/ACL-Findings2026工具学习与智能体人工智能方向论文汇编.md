# ACL-Findings2026 · 工具学习与智能体人工智能方向论文汇编

> 本方向共 17 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning ｜工具查询规划器

研究机构：美国麻省理工学院

作者：Wei Fang、James Glass

论文原文见 [arXiv](https://arxiv.org/abs/2601.07782)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07782)

> 大规模动态工具库中，静态单次检索无法弥合用户抽象意图与工具技术文档间的语义鸿沟，且难以处理多工具组合依赖。现有密集检索器在复杂组合任务上失效，本文切入点是将检索重构为交互式规划过程。TOOLQP 通过轻量模型分解子任务并迭代生成查询，结合 RLVR 优化策略。其价值在于以极低参数量实现了跨检索器的鲁棒泛化，但迭代查询带来的推理延迟在实时场景下的权衡尚存疑。

】

---

【Dynamic Tool Dependency Retrieval for Lightweight Function Calling ｜动态工具依赖检索

研究机构：美国马里兰大学帕克分校

作者：Bhrij Patel、Davide Belli、Amir Jalalirad 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.17052)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17052)

> 端侧大语言模型在调用外部工具时，面临内存与延迟的严格约束，无法将全量工具描述载入提示词。现有检索方法仅依赖静态语义相似度或固定依赖图，忽略了多步任务中不断演变的调用历史，导致检索结果包含无关工具或重复调用。本文提出动态工具依赖检索（Dynamic Tool Dependency Retrieval, DTDR），通过联合条件化用户查询与实时工具调用轨迹，从演示数据中恢复任务特定的最小依赖子图。该方法在端侧小模型上显著提升了函数选择准确率，但其在长程规划中的泛化能力与计算开销的平衡仍需进一步验证。

】

---

【EMTIR-GRPO: Efficient Multi-Tool Augmented Large Language Models via Reinforcement Learning ｜成本感知的多工具集成推理强化学习

研究机构：哈尔滨工业大学

作者：Shixin Jiang、Zhihao Zhu、Jiafeng Liang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2add66b6d72c)

> 工具集成推理（Tool-Integrated Reasoning, TIR）旨在让大语言模型（LLM）调用外部工具解决超出其内部能力边界的任务，但现有方法往往陷入“工具滥用”陷阱，导致高昂的计算开销与内在推理能力退化。针对多工具场景下异构成本被忽视、单工具效率优化无法泛化的问题，本文提出 EMTIR-GRPO，一种基于组相对策略优化（Group Relative Policy Optimization, GRPO）的成本感知强化学习算法。该算法通过引入轨迹成本估计与组最优成本估算，构建复合奖励机制以平衡准确率与调用成本。实验表明其在保持准确率的同时显著提升了工具生产力，但组内最优成本的动态估计在训练初期的稳定性及跨域泛化能力仍存疑。

】

---

【Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions ｜结构化反思增强工具调用鲁棒性

研究机构：美团

作者：Junhao Su、Yuanliang Wan、Junwei Yang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18847)

> 工具增强大语言模型在多轮交互中常因单次参数错误导致级联失败，而现有监督微调或粗粒度强化学习仅优化单步调用，缺乏对错误根因的定位与修复机制。本文切入点在于将“错误-反思-修复”过程显式化为可训练动作，通过扰动注入生成失败轨迹，并设计多维奖励函数引导模型学习诊断与修正。该方法在 BFCL v3 上提升了多轮准确率，但在通用基准上仍落后于 SOTA，其价值在于提供了错误恢复的专项训练范式，存疑点在于反思机制对正常调用流程的潜在干扰。

】

---

【Feasible is Not Enough: Cost-Aware Optimal Tool-Chain Planning on Multi-Solution Tool Graphs ｜多解工具图上的成本感知最优规划

作者：Liangliang Liu、Yanming Li、Yigang Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d03aa10b9cd1)

> 工具增强大语言模型（Tool-Augmented LLMs）在大规模工具库中常面临候选路径爆炸与上下文窗口受限的双重压力，现有方法多将工具调用视为单解问题，忽略同一任务存在多条有效路径且成本差异巨大的现实。本文切入点在于将工具学习（Tool Learning, TL）重构为多解图上的最优路径选择问题，通过强化学习（Reinforcement Learning, RL）驱动的两阶段渐进式图扩展与推理框架，在构建紧凑任务相关子图的同时执行成本感知规划。该框架在自建基准上显著提升了任务成功率与解的最优性，但其泛化能力受限于特定领域API的静态结构，且未与最新RLVR基线进行同协议对比。

】

---

【GOAT: A Training Framework for Goal-Oriented Agent with Tools ｜目标导向智能体工具训练框架

研究机构：韩国高丽大学、韩国科学技术院

作者：Hyunji Min、Sangwon Jung、Junyoung Sung 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12218)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12218)

> 目标导向任务要求智能体将高层意图分解为多步依赖的API调用，但此类任务缺乏人工标注数据，导致开源模型在零样本推理中表现脆弱。现有合成数据方法多采用“指令优先”策略，生成的查询与API调用逻辑脱节，无法有效传递依赖关系。GOAT通过构建经验证的API依赖图，采用“调用优先”策略反向生成训练数据，实现了无标注条件下的有效微调。该框架在多个基准上使开源模型性能超越部分闭源模型，但其依赖静态API文档的假设限制了在动态环境中的适用性。

】

---

【Invocation Refiner: A Plug-and-Play Module for Rectifying LLM Tool Invocations ｜工具调用纠错的解耦式后处理模块

作者：Qirui Jiao、Dian Jiao、Nan Du 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ba55c27392fd)

> 工具增强大语言模型（Tool-Augmented LLMs）在生成工具调用时频繁出现参数错误、格式畸形或顺序颠倒，导致下游执行失败。现有监督微调（SFT）与强化学习（RL）范式需直接修改基座模型参数，跨模型部署时面临高昂的重训成本。本文提出 Invocation Refiner，一个冻结上游模型、独立训练的解耦式纠错模块，通过规则奖励强化学习提升调用可靠性。该方案验证了模块化增强的可行性，但其对复杂多轮交互的泛化能力及额外推理延迟的权衡尚存疑。

】

---

【JTPRO: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents ｜联合工具-提示反思优化

作者：Sandip Ghoshal、Anshul Mittal、Jyotika Singh 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19821)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19821)

> 大规模工具库场景下，LLM智能体常因工具描述模糊与指令泛化导致选错工具或填错参数。现有微调方法需重训，纯提示优化又无法协同调整全局规则与局部Schema。JTPRO通过迭代反思机制，同时优化全局指令与每个工具的参数描述，在不更新模型权重的前提下提升调用准确性。该方法在复杂Schema任务上显著提升了参数填充准确率，但其效果高度依赖初始轨迹质量，且未解决多步依赖问题。

】

---

【MemTR: Enhancing Tool-Calling Reliability via Uncertainty-Triggered FFN-Space Retracing ｜基于不确定性触发的FFN空间重迹工具调用纠错

作者：Hongtao Duan、Lu Jiang、Minying Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_391d6837fe68)

> 工具调用中单token错误导致硬失败，现有训练式方法成本高且无法适应动态API更新，语法约束无法修正语义值错误。MemTR切入解码时干预，利用层熵识别脆弱token，在FFN输出层混合工具库证据以刷新记忆。该方法无需更新权重，仅增加1%-2%运行时开销，但绝对性能上限受限于骨干模型，且未与强化学习基线对比。

】

---

【Meta-Tool: Efficient Few-Shot Tool Adaptation for Small Language Models ｜少样本工具适配中的参数更新冗余性

作者：Sachin Kumar

论文原文见 [arXiv](https://arxiv.org/abs/2604.20148)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20148)

> 小语言模型（SLM）在接入新工具时面临适配瓶颈：前沿模型延迟高企，而监督微调（SFT）依赖稀缺标注且泛化差。现有研究倾向于通过复杂参数更新机制提升小模型能力，但本文指出在少样本场景下，精心设计的提示工程已充分指定任务，额外的参数空间适配可能冗余。Meta-Tool 通过控制实验对比超网络生成的 LoRA 权重与少样本提示，验证了后者的充分性。该负面结果挑战了“参数更新优于提示”的假设，但在单轮任务边界内，其结论对多步复杂任务的普适性存疑。

】

---

【Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation ｜经验知识增强与激活的工具执行框架

作者：Yupu Hao、Zhuoran Jin、Huanxuan Liao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e4f9388ab97a)

> 多步工具调用失败常源于模型缺乏具体执行经验，而非推理能力不足。现有方法多聚焦于提示工程或监督对齐，忽视了经验知识在推理时的激活效率与训练时的内化机制。本文提出KATE框架，通过实例级轨迹检索、并行采样宽度扩展及知识增强后训练，系统解决知识获取、激活与内化问题。该框架在BFCL-V3上将Qwen3-8B平均准确率从34.5%提升至45.17%，但缺乏与主流强化学习基线的直接对比，其泛化边界尚存疑。

】

---

【Supplement Generation Training for Enhancing Agentic Task Performance ｜补充生成训练

研究机构：美国宾夕法尼亚大学

作者：Young Min Cho、Daniele Bonadiman、Divya Bhargavi 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20727)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20727)

> 当大语言模型以闭源API形式部署且无法获取梯度时，如何在不修改权重的情况下提升其任务表现？现有提示优化方法主要在全局模板或固定候选池中进行搜索与重排，缺乏针对单个输入实例动态生成新推理结构的能力。本文提出补充生成训练（Supplement Generation Training, SGT），通过训练一个1.7B的小模型生成实例特定的文本补充，利用冻结大模型的输出正确性作为代理奖励，以SFT加迭代DPO的方式优化生成策略。该方法在五个基准上实现了21%的平均性能提升，但其有效性局限于静态文本推理任务，在动态工具调用场景下的泛化能力尚存疑。

】

---

【ToolDNA: Autonomous Evolution of Tool Metadata for Robust Dialogue Agents ｜工具元数据动态演化框架

作者：Qiuyuan Ai、Cong Wang、Jiaqi Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fea393aa8d6d)

> 任务导向对话（TOD）系统依赖外部工具执行精确操作，但静态人工维护的工具元数据常因定义模糊导致调用错误，且传统强化学习（RL）奖励信号稀疏，无法诊断具体失效原因。ToolDNA 提出策略网络与工具元数据的协同演化机制，通过双闭环结构实现元数据的自主迭代优化。该框架在真实客服对话场景中显著提升了问题解决率，但其泛化性受限于特定领域数据，且缺乏通用基准验证。

】

---

【ToolGate: Contract-Grounded and Verified Tool Execution for LLMs ｜基于Hoare逻辑的工具调用契约验证框架

研究机构：浙江大学、东南大学

作者：Yanming Liu、Xinyue Peng、Jiannan Cao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04688)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04688)

> 工具增强大语言模型（Tool-Augmented LLMs）在复杂多步任务中常因缺乏对工具调用前提与结果有效性的形式化保证，导致幻觉参数或无效输出污染推理状态。现有基于自然语言推理或强化学习（RL）的框架虽能提升泛化性，但无法在推理时提供逻辑安全边界，错误易在长程依赖中级联传播。ToolGate 通过引入显式符号状态空间与 Hoare 风格契约，将工具调用转化为受前置条件（Precondition）与后置条件（Postcondition）约束的逻辑执行过程，确保状态仅通过验证过的工具结果演化。该框架在 ToolBench 与 MCP-Universe 上显著提升了任务成功率与执行稳定性，但其性能高度依赖骨干模型的推理能力，且未涉及模型参数更新，在资源受限或需跨域泛化场景下的适用性存疑。

】

---

【ToolGrad: Efficient Tool-use Dataset Generation with Textual “Gradients ｜工具使用数据集生成：从查询驱动到答案优先的范式反转

作者：Zhongyi Zhou、Kohei Uehara、Haoyu Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ad996b6abb2f)

> 工具增强大语言模型（Tool-Augmented LLMs）的训练依赖高质量“用户查询-工具调用链”配对数据，但现有合成方法受限于深度优先搜索（DFS）的高昂计算成本与低通过率，导致数据稀缺且分布偏差。ToolGrad 提出“答案优先”范式，先通过迭代链式构建有效工具工作流，再反推用户查询，以近乎 100% 的通过率生成复杂轨迹。该方法将文本梯度概念迁移至数据合成，验证了小模型在特定数据下可超越专有大模型，但其缺乏记忆机制导致数据多样性受限，规模化扩展存在性能饱和风险。

】

---

【ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents ｜工具使用智能体过程奖励模型评估基准

研究机构：美国亚利桑那州立大学

作者：Dawei Li、Yuguang Yao、Zhen Tan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12294)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12294)

> 工具使用智能体在多步任务中常因早期错误导致级联失败，而仅依赖最终结果奖励无法定位具体失效步骤。现有过程奖励模型（Process Reward Model, PRM）基准多局限于数学推理或网页导航，缺乏针对API工具调用的标准化评估体系。本文构建了ToolPRMBench，通过离线与在线轨迹采样结合多LLM验证，将智能体轨迹转化为步骤级偏好对，并训练了基于监督微调与强化学习的专用PRM变体。该基准填补了工具使用场景下PRM评估的空白，但合成数据的有效性边界及大规模工具库下的检索协同机制仍未解决。

】

---

【ToolRM: Towards Agentic Tool-Use Reward Modeling ｜工具使用奖励模型

研究机构：澳门大学、澳大利亚新南威尔士大学

作者：Renhao Li、Jianhong Tu、Yang Su 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26167)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26167)

> 工具增强大语言模型（Tool-Augmented LLMs）的强化学习训练依赖可靠的奖励信号，但现有方法多依赖人工标注轨迹或简单规则，难以泛化至未见工具场景。本文切入点在于构建无需 ground-truth 标签、具备因果推理能力的专用奖励模型（Reward Model, RM）。通过规则基评分与平衡多维采样构建偏好数据，训练轻量级生成式与判别式 RM。该工作填补了工具使用领域专用 RM 的空白，但其规则基评分在复杂非结构化 API 返回下的鲁棒性存疑。

】
