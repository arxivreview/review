# ACL2026 · 基于LLM的Web智能体与基准测试方向论文汇编

> 本方向共 12 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces ｜电商欺骗性界面下的Web智能体安全评估

作者：Zijing Shi、Meng Fang、Ling Chen

论文原文见 [arXiv](https://arxiv.org/abs/2606.13686)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_47fe36917bd7)

> 现有Web智能体基准主要评估任务成功率，忽略了真实电商环境中普遍存在的误导性UI设计（如价格漂移、强制加购）对智能体决策的干扰。主流安全研究聚焦于恶意指令注入，缺乏对非对抗性但具欺骗性的界面状态篡改的系统化评估。本文提出WebDecept框架，通过在VisualWebArena环境中动态注入七类可配置的欺骗模式，解耦任务完成与安全违规指标，量化了多模态智能体在受控欺骗下的脆弱性。该工作揭示了提示词约束在隐蔽状态操纵面前的失效，但缺乏与系统级防御机制的对比，且评估局限于单一电商域。

】

---

【Branch-and-Browse: Efficient and Controllable Web Exploration with Tree-Structured Reasoning and Action Memory ｜分支浏览：基于树结构推理与动作记忆的Web智能体高效探索

研究机构：美国密歇根大学、阿里巴巴集团

作者：Shiqi He、Yue Cui、Xinyu Ma 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.19838)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.19838)

> 长程Web任务中，线性推理轨迹一旦早期步骤出错便导致级联失败，而传统树搜索因分支独立探索产生大量冗余计算。本文切入点在于将树结构探索与页面级共享记忆结合，通过子任务管理器、最近URL状态回放及背景推理机制，在保持多分支回溯能力的同时显著降低执行开销。该方法在WebArena基准上实现了35.8%的任务成功率，并将平均执行时间减少40.4%，但在绝对成功率上仍低于部分策略型基线，其效率-成功率权衡的边界尚待更严苛的动态环境验证。

】

---

【Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces ｜欺骗性UI防御与评估校准

研究机构：中国人民大学

作者：Yilin Zhang、Yingkai Hua、Chunyu Wei 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.09497)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.09497)

> 视觉语言模型驱动的Web智能体在真实网页中极易被暗模式（Dark Patterns）诱导执行错误操作，现有检测工具缺乏任务语义整合，而简单拒绝策略又导致良性任务失败。本文提出DUDE框架，通过混合奖励学习校准评估器置信度，并结合经验总结实现无参数更新的防御增强。该方案在自建基准上显著降低欺骗率，但其对动态交互环境的适应性及跨基准泛化能力仍存疑。

】

---

【Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning ｜规划经验探索与利用

研究机构：中国科学院、中国科学院大学

作者：Tianyi Men、Zhuoran Jin、Pengfei Cao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.27330)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.27330)

> 多模态网页智能体在开放网络中执行复杂任务时，小参数模型因规划能力薄弱且跨网站泛化受限，难以替代高成本商业大模型。现有数据合成方法要么训练原子级动作导致高层规划失效，要么使用粗粒度任务但轨迹与约束不对齐。本文提出 PEEU，通过自主探索构建规划树，并利用后见经验反向对齐任务与轨迹，生成严格约束的高层训练数据。该方法在同等数据规模下显著提升了小模型的跨域规划能力，但其泛化上限是否受限于探索阶段的 GPT-4o 依赖仍存疑。

】

---

【GTA: Generating Long-Horizon Tasks for Web Agents at Scale ｜基于站点图检索种子的多跳任务生成

研究机构：美国南加州大学、Salesforce AI研究院

作者：Tenghao Huang、Kung-Hsiang Huang、Prafulla Kumar Choubey 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.29218)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.29218)

> 现有 Web 智能体基准面临数据稀缺与过程监督缺失的双重困境，人工标注成本高且无法覆盖长程推理轨迹，而早期自动生成分布偏差大、任务浅层化。GTA 通过解耦爬取与生成环节，利用站点图检索种子构建组合性任务，实现了可执行轨迹的规模化产出。该框架在 50 个网站上的实验揭示了智能体在跨域与非英语环境下的显著性能断层，但其评估仍受限于单一文本模态与有限基线覆盖，对复杂 UI 布局的接地能力验证不足。

】

---

【Mango: Multi-Agent Web Navigation via Global-View Optimization ｜基于全局视图优化的多智能体网页导航

作者：Weixi Tong、Yifeng Di、Tianyi Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2604.18779)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5aeaed18360d)

> 现有网页智能体从根 URL 开始线性探索，在深层级网站中易陷入导航陷阱或耗尽预算。MANGO 通过预构建网站全局结构，将 URL 选择建模为多臂老虎机问题，利用 Thompson Sampling 动态分配导航预算，从而在有限步骤内定位目标信息。该方法在 WebVoyager 上取得 63.6% 成功率，但在 WebWalkerQA 多源任务中仍低于领域最高水平，其全局爬取成本与实时性权衡尚存疑。

】

---

【MirrorCAPTCHA: Wild CAPTCHA, Wild Distribution, Wild Web-based Platform Meet Multimodal LLM Agents ｜镜像验证码基准与智能体鲁棒性评估

研究机构：南京大学、阿里巴巴集团

作者：Xiangyu Wu、Yuwei Hu、Tianyu Cui 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_64966e8cf2d2)

> 多模态网络智能体在自动化执行注册、登录等高频任务时，常被图形验证码（CAPTCHA）阻断，导致端到端任务链断裂。现有基准多依赖合成数据或忽略此类交互，无法反映真实网络中验证码的分布差异与难度梯度。本文构建基于真实流量加权的 MirrorCAPTCHA 基准，并训练专用小模型 Ovis2-Agent-CAPTCHA-8B 以验证微调策略的有效性。该工作揭示了当前闭源大模型在特定视觉接地任务上的脆弱性，但其评估范围局限于桌面端静态快照，对动态异步加载场景的覆盖仍存疑。

】

---

【SynthAgent: Adapting Web Agents with Synthetic Supervision ｜合成监督下的Web智能体环境适应

研究机构：美国普渡大学

作者：Zhaoyang Wang、Yiming Liang、Xuchao Zhang 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.06101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.06101)

> Web智能体在新环境中因缺乏特定任务演示而难以泛化，现有合成数据方法要么任务幻觉严重，要么轨迹噪声过大。SynthAgent通过“分类探索”与“任务-轨迹双重精炼”机制，在无需人工标注的情况下生成高质量监督数据。该方法在WebArena上以7B开源模型达到31.67%成功率，优于其他合成基线，但其绝对性能仍显著低于基于更强骨干或强化学习的SOTA方法，且数据规模扩展的边际收益尚未完全揭示。

】

---

【WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning ｜基于图剪枝的Web智能体效率进化

作者：Junjie Wang、Zequn Xie、Dan Yang 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.12852)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.12852)

> Deep Research类Web智能体在追求高准确率时，往往陷入工具调用轮次激增与上下文膨胀的效率陷阱，导致实际部署成本高昂。现有训练范式仅关注端到端任务成功率，忽视了轨迹内部的冗余结构，导致智能体在长程搜索中频繁陷入循环推理或无效分支。本文切入点在于不重建智能体，而是将现有智能体的搜索轨迹建模为状态图，通过挖掘最小必要有向无环图（MNDAG）剪除冗余步骤，并基于修剪后的轨迹进行微调。该方法在保持准确率的同时显著降低了资源消耗，但其对复杂推理中“探索性冗余”的误删风险及跨任务泛化能力尚存疑。

】

---

【WebSynthesis: World Model-Guided Monte Carlo Tree Search for Efficient WebAgent Trajectory Synthesis ｜离线轨迹合成框架 WebSynthesis

研究机构：北京交通大学、新加坡南洋理工大学

作者：Yifei Gao、Junhong Ye、Yifan Yang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c9b7e8b56498)

> 大语言模型（LLM）驱动的 Web 智能体训练长期受限于高质量交互轨迹获取的高昂成本与真实环境动作不可逆导致的探索局限。现有方法依赖实时网络请求或线性采样，难以兼顾数据规模与多样性。WebSynthesis 通过构建基于 LLM 的世界模型（LWM）模拟状态转移，并引入蒙特卡洛树搜索（MCTS）实现可回溯的离线探索，从而生成高覆盖率的训练数据。该框架在纯监督微调（SFT）设定下验证了合成数据的有效性，但其对世界模型预测精度的依赖及仅采用 SFT 的训练范式，限制了其在复杂推理任务上的上限。

】

---

【When Efficiency Becomes a Vulnerability: Computational Cost Attacks on WebAgents ｜计算成本攻击

作者：Liang-Bo Ning、Yuchen Zhu、Heqing Huang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_103e9e1d87b5)

> 现有 Web 智能体研究聚焦于提升任务成功率，却忽视了计算效率作为独立脆弱性维度的存在。当攻击者不再试图让智能体执行错误动作，而是通过注入恶意提示诱导其生成冗长推理时，智能体虽能完成任务，但算力消耗与延迟将呈指数级增长，导致在金融、医疗等时效敏感场景中失效。CostBomb 提出一种“生成-选择”攻击框架，利用大语言模型生成候选恶意提示，并通过强化学习优化选择策略，以最大化受害智能体的 Token 消耗。该工作首次系统化了计算成本攻击，但仅验证了攻击的有效性，未探讨防御机制，且未报告任务成功率是否因推理过长而受损。

】

---

【Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective ｜分层规划视角下的LLM Web智能体失败归因

研究机构：美国乔治梅森大学

作者：Mohamed Aghzal、Gregory J. Stein、Ziyu Yao

论文原文见 [arXiv](https://arxiv.org/abs/2603.14248)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14248)

> 现有LLM Web智能体在真实动态网站上的可靠性远低于人类水平，但主流评估仅依赖端到端成功率，无法定位失败究竟源于任务理解偏差、高层策略错误还是底层执行偏差。本文切入点在于将智能体能力解耦为高层规划、低层执行与重规划三个独立维度，通过引入形式化表示与后条件检查机制实现过程级诊断。其核心做法是构建一个基于PDDL（Planning Domain Definition Language）的分层评估框架，在Mind2Web-Live基准上对三个主流LLM进行模块化测试。该框架揭示了低层执行是主要瓶颈，但受限于小模型骨干与单一文本输入，其结论的普适性存疑。

】
