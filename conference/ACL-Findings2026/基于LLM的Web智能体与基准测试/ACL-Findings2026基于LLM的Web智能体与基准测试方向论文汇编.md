# ACL-Findings2026 · 基于LLM的Web智能体与基准测试方向论文汇编

> 本方向共 9 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ExpSeek: Self-Triggered Experience Seeking for Web Agents ｜自触发经验寻求框架

研究机构：中国科学院、中国科学院大学

作者：Wenyuan Zhang、Xinghua Zhang、Haiyang Yu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.08605)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08605)

> 开放网络中的搜索智能体常因证据稀疏与噪声干扰而在多轮交互中迷失，现有经验注入方法将历史教训作为全局上下文一次性喂给模型，无法适应交互过程中动态变化的认知状态。本文切入点在于利用模型自身的输出熵作为内在置信度信号，在智能体真正“困惑”时才主动检索并生成针对性经验指导。ExpSeek 通过基于 Bootstrap 重采样的熵阈值估计确定介入时机，并由独立经验模型生成步级指导，实现了从被动全局注入到主动步级寻求的范式转换。该框架在四个搜索基准上验证了有效性，但其依赖离线构建的经验库与特定骨干模型，在跨域泛化与实时性上存在边界。

】

---

【From Imitation to Discrimination: Progressive Curriculum Learning for Robust Web Navigation ｜从模仿到判别：渐进式课程学习下的鲁棒网页导航

研究机构：北京交通大学、北京航空航天大学

作者：Chuang Peng、Wei Zhang、Renshuai Tao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12666)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12666)

> 文本型网页智能体在噪声DOM环境下面临判别缺失与泛化受限的双重瓶颈，标准监督微调仅能教会模型“做什么”，却无法抑制其在密集页面中选中结构相似但错误元素的幻觉。本文切入点在于通过数据构造与训练课程的协同设计，将判别能力与长程一致性作为独立优化目标。具体做法是构建包含硬负样本与合成跨域任务的Triton数据集，并实施SFT-ORPO-GRPO三阶段渐进训练。该方法以32B参数量在Mind2Web上取得58.7%的步骤成功率，超越GPT-4.5，但受限于纯文本模态与静态快照评估，其结论在动态多模态环境中的普适性存疑。

】

---

【How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors ｜视觉属性对Web智能体决策影响的量化评估

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国哥伦比亚大学

作者：Kuai Yu、Naicheng Yu、Han Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21961)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21961)

> 现有Web智能体研究多聚焦于对抗攻击下的鲁棒性，却忽视了良性场景中视觉布局对决策的隐性偏置。VAF通过仅修改CSS属性生成语义一致的网页变体，量化了背景色、尺寸、位置等视觉因素对点击行为的影响。该框架揭示了智能体决策高度依赖视觉显著性而非文本语义，但单步点击评估能否代表长程任务中的视觉稳定性仍存疑。

】

---

【MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs ｜恶意URL伪装攻击基准与轻量级防御模块

研究机构：浙江大学、重庆大学

作者：Dezhang Kong、Zhuxi Wu、Shiqi Liu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18113)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18113)

> 大语言模型（LLM）驱动的Web智能体在访问网页前需判断URL合法性，但现有安全基准仅关注网页内容中的提示注入，忽略了URL结构本身被操纵的风险。本文指出LLM对伪装URL的识别能力极弱，导致智能体入口失守。通过构建包含61,845个实例的MalURLBench并微调轻量级模型URLGuard，证明了该威胁的普遍性及微调防御的有效性。尽管验证了前置过滤的可行性，但缺乏与系统级沙箱的横向对比及误报率评估，其实际部署中的任务成功率影响仍存疑。

】

---

【SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents ｜安全评估基准 SecureWebArena

研究机构：北京航空航天大学、中国科学院

作者：Zonghao Ying、Yangguang Shao、Jianle Gan 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10073)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10073)

> LVLM Web智能体在开放网络中面临多源攻击，但现有基准仅孤立评估用户指令或单一环境威胁，缺乏统一框架。本文切入点在于构建覆盖用户级与环境级双重威胁的全景评估体系，通过多层诊断协议定位失效根源。其价值在于揭示了模型特化与安全鲁棒性间的权衡，但模拟环境与真实网络的迁移有效性仍存疑。

】

---

【WebAnchor: Anchoring Agent Planning to Stabilize Long-Horizon Web Reasoning ｜锚定规划以稳定长程网络推理

作者：Xinmiao Yu、Liwen Zhang、Xiaocheng Feng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d9ccb4a8a33a)

> 长程网络信息检索任务中，智能体常因早期规划失误导致后续轨迹级联失败，现有强化学习算法因均匀分配奖励而忽视首步决策的结构性影响。本文识别出“计划锚点”现象，即首步推理对全局成功率的非对称支配作用，并据此提出两阶段强化学习框架 Anchor-GRPO。该框架通过从自博弈经验中迭代学习规划评分标准，将密集奖励聚焦于首步规划优化，再以稀疏奖励对齐执行轨迹。这一设计在 GAIA 基准上实现了 76.4% 的 Pass@1，但其在无外部记忆依赖下的长程一致性仍存疑。

】

---

【WebDART: Dynamic Decomposition and Re-planning for Complex Web Tasks ｜动态分解与自适应重规划

研究机构：美国加州大学圣塔芭芭拉分校

作者：Jingbo Yang、Bairu Hou、Wei Wei 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06587)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06587)

> 长程网页任务中，智能体因需同时处理导航、信息提取与约束推理而陷入“认知过载”，导致成功率在复杂基准上骤降。现有线性推理-行动架构无法解耦这些异构能力，致使错误在步骤间级联放大。WEBDART 将任务强制拆解为导航、提取、执行三个串行子任务，并引入动态重规划机制以利用新发现的界面元素优化路径。该框架在复杂任务上显著提升了成功率，但其纯文本设定与串行解耦是否牺牲了实时反馈耦合，仍存疑。

】

---

【WebUncertainty: Dual-Level Uncertainty Driven Planning and Reasoning For Autonomous Web Agent ｜双层不确定性驱动的Web智能体规划与推理

研究机构：合肥工业大学

作者：Lingfeng Zhang、Yongan Sun、Jinpeng Hu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17821)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17821)

> 长程Web任务中，静态规划难以适应动态界面，而线性推理易因幻觉导致错误级联。现有方法要么僵化执行预定义步骤，要么盲目信任LLM生成的动作，缺乏对“环境未知”与“模型无知”的区分。WebUncertainty通过任务不确定性驱动规划模式切换，并结合动作不确定性量化MCTS搜索，实现了在复杂交互中的鲁棒决策。该方法在WebArena上取得46.9%成功率，显著优于基线，但其纯文本设定与高计算开销限制了实际部署的泛化性。

】

---

【中国人民大学团队提出WASP协议：预构建站点地图注入上下文，无需训练提升Web智能体导航

研究机构：中国人民大学

作者：Yuyao Zhang、Hongyu Lu、Jiajie Jin 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f6f66507cc6)

> 现有LLM Web智能体在真实开放网络中因缺乏网站结构先验，导致导航低效与接地误差，任务成功率远低于人类水平。主流路线聚焦于增强模型内部推理或构建动态世界模型，但忽视了静态结构化知识对长程规划的支撑作用。WASP通过预构建双粒度站点地图，将全局导航结构与局部交互指引作为外部知识注入智能体上下文，无需额外训练即可提升鲁棒性与效率。该方案在WebVoyager上取得58.3%成功率，但依赖静态快照，未验证网页动态更新下的时效性。

】
