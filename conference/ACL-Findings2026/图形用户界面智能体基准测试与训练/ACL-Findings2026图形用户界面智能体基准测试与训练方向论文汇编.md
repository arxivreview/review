# ACL-Findings2026 · 图形用户界面智能体基准测试与训练方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【D-Artemis: A Deliberative Cognitive Framework for Mobile GUI Multi-Agents ｜移动GUI智能体的执行前对齐框架

研究机构：天津大学、香港中文大学

作者：Hongze Mi、Yibo Feng、Wenjie Lu 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21799)

> 移动GUI智能体在长程任务中面临单步错误导致轨迹偏离的累积效应，现有框架多依赖执行后反思，无法在动作生效前拦截失效。D-Artemis通过引入执行前对齐阶段，在动作执行前校验思维与动作的一致性并主动修正，解决了延迟检测带来的高恢复成本。该框架无需大规模轨迹数据训练，仅通过轻量级模块增强通用多模态大语言模型（MLLM）的GUI操作能力。其在AndroidWorld上取得75.8%的成功率，但相比在线强化学习（RL）方法仍存差距，且未验证极端分布外场景下的泛化边界。

】

---

【Does Chain-of-Thought Reasoning Help Mobile GUI Agents? An Empirical Study ｜推理增强对移动GUI智能体有效性的实证评估

作者：Li Zhang、Longxi Gao、Mengwei Xu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_44409ae599a2)

> 移动GUI智能体在真实动态环境中面临多步交互与视觉布局复杂性，现有基于监督微调或强化学习的模型在长程任务中仍存在错误累积与泛化不足。本文切入点在于质疑“推理能力必然提升GUI操作性能”的假设，通过对比六组具备与不具备推理能力的视觉语言模型（VLM）在静态与动态基准上的表现，量化推理带来的性能增益与资源开销。研究发现推理在静态基准上收益微弱甚至负向，仅在特定动态场景下对特定模型有效，且伴随显著的Token膨胀。该研究揭示了推理机制在GUI任务中的局限性，但受限于未训练新模型，其结论对推理与训练范式协同作用的解释力有限。

】

---

【FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems ｜联邦GUI智能体异构基准

研究机构：浙江大学、上海交通大学

作者：Wenhao Wang、Haoting Shi、Mengying Yuan 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14956)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14956)

> 联邦学习（Federated Learning, FL）旨在解决GUI交互数据因隐私限制无法集中存储的困境，但现有基准仅覆盖单一移动平台，无法量化跨Web、桌面及多操作系统间的分布偏移。FedGUI通过构建覆盖900+移动应用、40+桌面应用及200+网站的六类数据集，系统建模了跨平台、跨设备、跨OS及跨数据源四种异构性。实验证实跨平台协作能挽救单域模型的失效，但联邦训练在极端偏斜分布下的性能仍显著低于集中式训练。该基准填补了分布式GUI训练评测空白，但其绝对性能上限受限于缺乏强化学习机制。

】

---

【LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark ｜移动端GUI智能体的少样本演示学习框架

研究机构：浙江大学、香港中文大学

作者：Guangyi Liu、Pengxiang Zhao、Liang Liu 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9b5b11b14d92)

> 移动端GUI智能体在长尾场景下泛化能力不足，传统预训练或微调难以覆盖所有应用与用户任务组合，导致未见场景执行失败。现有基于结构化元数据（如UI Tree）的方法在移动端因数据缺失而失效，纯视觉端到端模型则缺乏从少量人类演示中提取可复用知识的机制。本文提出LearnAct框架，通过纯视觉输入解析演示、检索相似知识并指导执行，构建首个移动端少样本演示学习基准LearnGUI。该框架验证了非训练式知识迁移的有效性，但其绝对性能仍远低于全量强化学习模型，且依赖高质量演示的可用性。

】

---

【MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment ｜移动图形用户界面智能体真实环境基准

研究机构：小米、北京大学

作者：Qinzhuo Wu、Zhizhuo Yang、Hanhao Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20335)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20335)

> 移动图形用户界面智能体（Mobile GUI Agent）需在动态、含噪的真实设备上执行多步操作，但现有在线基准多依赖模拟器且忽略环境噪声，导致评测与部署存在断层。本文提出MobileBench-OL，通过80个中文应用中的1080个任务及5个子集，覆盖基础能力、长程推理、GUI探索与噪声鲁棒性。其核心机制是结合基于XPath规则的自动评估框架与细粒度重置机制，确保评测的可重复性。该基准揭示了当前智能体在真实噪声下的显著性能衰减，但其缺乏跨应用任务且仅限中文生态，限制了结论的普适性。

】

---

【OpenPhone: Mobile Agentic Foundation Models ｜端云协同移动GUI智能体

作者：Yangqin Jiang、Chao Huang

论文原文见 [arXiv](https://arxiv.org/abs/2510.22009)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22009)

> 移动端GUI智能体面临算力与成本的结构性矛盾：4B以下模型能力不足，7B以上模型无法端侧部署或云端调用成本过高。现有方案要么牺牲性能追求轻量化，要么依赖昂贵的大模型，缺乏在两者间动态切换的机制。OpenPhone通过3B端侧模型与云端大模型的实时协同编排，在保持接近云端性能的同时大幅降低调用成本。该框架验证了小模型经强化学习优化后的可行性，但其动态切换策略的泛化边界与通信延迟影响尚不明确。

】

---

【SOLAR-RL: Semi-Online Long-horizon Assignment Reinforcement Learning ｜半在线长程信用分配强化学习

研究机构：香港中文大学、美国普林斯顿高等研究院

作者：Jichao Wang、Liuyang Bian、Yufeng Zhou 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22558)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.22558)

> GUI智能体在长程任务中面临在线强化学习（Reinforcement Learning, RL）交互成本高昂与离线强化学习（Offline RL）时序短视的双重困境，导致稀疏奖励下的信用分配失效。SOLAR-RL通过离线轨迹重构与回溯性信用分配，在静态数据中模拟伪在线反馈，解决了长程任务中的梯度消失问题。该方法以94K步数据在AndroidWorld上取得33.7%成功率，虽低于在线SOTA，但显著优于同等数据规模的离线基线，其核心在于将轨迹级质量转化为密集步骤级奖励。

】

---

【Towards Scalable Lightweight GUI Agents via Multi-role Orchestration ｜轻量级GUI智能体的多角色编排

研究机构：浙江大学

作者：Ziwei Wang、Junjie Zheng、Leyang Yang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13488)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13488)

> 该方向旨在解决轻量级多模态大语言模型（MLLM）在资源受限设备上部署时，因参数容量瓶颈与端到端学习范式导致的任务可扩展性不足问题。现有方案或依赖大规模模型的高昂推理成本，或受限于单一模型在长程任务中的错误累积与上下文丢失。本文切入点在于通过参数共享实现单模型多角色编排，将高维推理解耦为可协同的子任务流。具体做法是结合角色导向数据合成与两阶段训练（SFT+RL），使轻量模型既能独立执行，又能作为高级规划器的可插拔执行器。其价值在于以3B参数规模实现了接近大模型的在线执行能力，但独立端到端性能仍显著低于专用大模型，且高度依赖外部规划器。

】

---

【WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments ｜WindowsWorld：面向专业跨应用工作流的GUI智能体过程感知基准

研究机构：哈尔滨工业大学

作者：Jinchao Li、Yunxin Li、Chenrui Zhao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27776)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27776)

> 现有GUI智能体基准多聚焦单应用导航，无法反映真实办公场景中跨应用协同的认知负荷，且“全有或全无”的评分机制掩盖了长程任务中的部分进展。WindowsWorld通过构建181个以16种职业角色为锚点的跨应用任务，并引入中间检查点评分，填补了专业级多应用工作流评估的空白。其核心贡献在于将评估粒度从终态匹配推进至过程诊断，但20%左右的最高成功率也暴露了当前模型在跨应用状态维护上的根本缺陷。

】
