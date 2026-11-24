# ACL-Findings2026 · 软件工程中的大语言模型智能体方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ABC-Bench: Benchmarking Agentic Backend Coding in Real-World Development ｜后端全生命周期智能体基准

研究机构：复旦大学

作者：Jie Yang、Honglin Guo、Li Ji 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11077)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11077)

> 后端开发涉及代码逻辑、环境配置与服务部署的强耦合，现有基准多将环境预置，仅评估局部代码修改，无法反映生产级交付能力。本文切入点在于构建一个强制智能体自主完成从仓库探索到容器化部署全流程的评估体系。通过自动化流水线从开源仓库提取任务，并以外部API测试作为唯一验证标准，ABC-Bench揭示了当前模型在环境配置环节的显著短板。该基准填补了全生命周期评估空白，但其任务生成依赖GPT-5辅助，可能引入特定模型偏好。

】

---

【OmniCode: A Benchmark for Evaluating Software Development Agents ｜全生命周期软件工程智能体基准

研究机构：美国康奈尔大学、美国纽约大学

作者：Atharv Sonwane、Eng-Shen Tu、Wei-Chung Lu 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a20366a07501)

> 现有代码智能体基准聚焦于单一补丁生成任务，无法评估模型在测试编写、代码审查响应及风格合规等真实开发环节的综合能力。本文通过合成负样本与多任务扩展，构建覆盖Python、Java、C++三语言的1794项任务基准，揭示当前SOTA模型在非Python语言及测试生成上的显著短板。其价值在于暴露了单一指标评估的盲区，但$2/instance的成本约束可能低估高复杂度任务的真实性能。

】

---

【SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning Context ｜动态推理上下文管理

研究机构：厦门大学

作者：Shuquan Lian、Juncheng Liu、Yazhe Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11716)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11716)

> 长程软件工程智能体在保留深度推理时面临上下文爆炸与注意力稀释的双重困境，而丢弃推理轨迹又导致每步冗余重算。SWE-AGILE 通过滑动窗口保留近期完整思维链、将历史思维压缩为摘要，并引入轨迹快照训练与压缩率奖励，在 8B 模型上以 2.2k 轨迹实现 24.1% 的 SWE-bench Verified 解决率。该框架有效平衡了推理深度与 token 效率，但其性能上限仍受限于小模型基座，且未验证外部记忆机制的协同效应。

】

---

【SWE-Mutation: Can LLMs Generate Reliable Test Suites in Software Engineering? ｜软件变异测试基准

研究机构：中国科学技术大学、北京航空航天大学

作者：Yuxuan Sun、Yuze Zhao、Yufeng Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22175)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22175)

> 软件工程智能体的核心瓶颈并非代码生成能力，而是验证信号的可靠性。现有基准依赖人工测试或简单规则变异，无法量化模型生成测试套件对细微语义缺陷的判别力。本文通过智能体对抗筛选机制构建高保真变异体，揭示当前大语言模型在测试生成上的严重短板。该基准为强化学习提供了更可靠的评估工具，但其单智能体架构在复杂多语言场景下的泛化边界仍存疑。

】

---

【SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution ｜多技能分解与两阶段强化学习配方

研究机构：北京大学、MiniMax

作者：Zhenyu He、Qingping Yang、Wei Shen 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_91e76523f802)

> 导读 仓库级软件修复的核心瓶颈在于开源模型缺乏针对真实工程环境的系统性训练数据与策略优化机制，导致其在 SWE-bench 等基准上的表现显著落后于闭源大模型。现有方法或依赖静态文本匹配，或采用单一任务蒸馏，未能有效整合定位、修复与验证的协同能力。本文提出 SWE-Swiss 配方，通过多任务监督微调（SFT）建立基础技能，再针对修复任务实施基于执行反馈的强化学习（RL），实现开源 32B 模型在 SWE-bench Verified 上 60.2% 的解决率。该结果确立了开源模型在该规模下的新标准，但其性能提升是否完全归因于训练策略而非骨干模型潜力，仍需进一步隔离验证。

】
