# ICLR2026 · 基于LLM的Web智能体与基准测试方向论文汇编

> 本方向共 9 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AGENTFOLD: LONG-HORIZON WEB AGENTS WITH PROACTIVE CONTEXT FOLDING ｜主动上下文折叠的长程Web智能体

研究机构：上海交通大学

作者：Rui Ye、Zhongwang Zhang、Kuan Li 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_72470046)

> 长程Web信息检索任务中，智能体面临上下文饱和与关键信息丢失的双重困境。ReAct范式因累积原始噪声导致推理退化，而固定步长摘要则可能不可逆地抹除细节。AgentFold引入多尺度状态摘要与主动折叠机制，将上下文管理内化为智能体的核心推理步骤。该架构在BrowseComp等基准上以30B参数模型超越了671B规模的开源模型，但其有效性局限于信息检索场景，在动态Web交互任务中的泛化能力尚存疑。

】

---

【GO-BROWSE: TRAINING WEB AGENTS WITH STRUCTURED EXPLORATION ｜结构化探索驱动的智能体数据合成

研究机构：美国卡内基梅隆大学

作者：Apurva Gandhi、Graham Neubig

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_21288597)

> Web智能体在开放环境中的核心瓶颈并非模型推理能力，而是缺乏针对特定网站交互逻辑的预训练数据。现有自动化数据生成方法要么依赖昂贵的人工标注，要么因缺乏全局视野导致探索冗余与任务幻觉。GO-BROWSE将数据收集重构为图搜索问题，通过维护URL前沿并解耦导航与局部执行，实现了无监督环境下的高质量轨迹自动采集。该方法证明了小参数模型在特定域内可超越通用大模型，但其泛化边界与仅依赖文本树状结构的感知局限仍存疑。

】

---

【HackWorld _ : EVALUATING COMPUTER-USE AGENTS ON EXPLOITING WEB APPLICATION VULNERABILITIES ｜计算机使用智能体在Web漏洞利用中的能力评估

研究机构：浙江大学、澳大利亚新南威尔士大学

作者：Xiaoxue Ren、Penghao Jiang、Kaixin Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_4935641)

> 现有Web智能体基准普遍假设环境安全且功能完整，忽略了智能体在真实脆弱网络中作为攻击代理的潜在风险。这种“净化”环境导致无法量化智能体发现并利用漏洞的实际能力，而传统渗透测试又因依赖人工专家而缺乏可扩展性。本文通过构建包含真实漏洞的CTF式评估框架，将安全工具编排纳入核心评估维度，系统性地测量了前沿多模态智能体的对抗性探索极限。实验揭示了感知并非瓶颈，推理与工具策略才是核心短板，但当前智能体在复杂攻击链构建上仍显脆弱，其结论对防御侧的威胁建模具有直接参考价值。

】

---

【Test-Time Adaptation for LLM Agents via Environment Interaction ｜环境交互驱动的测试时适应

研究机构：加拿大滑铁卢大学、Salesforce AI研究院

作者：Arthur Chen、Zuxin Liu、Jianguo Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.04847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04847)

> LLM智能体在部署于未见环境时，常因预训练知识与目标环境的语法及动态机制错位而失效。现有方案或依赖昂贵的离线标注与模型微调，或采用重参数化的世界模型，难以在零标注条件下实现快速适应。本文切入点在于利用部署时的无监督交互，将适应解耦为语法分布对齐与语义动态接地两个独立过程。通过轻量级适应向量与一次性探索规则生成，本文以极低成本显著提升了复杂环境下的任务成功率，但其对简单环境的负向干扰及两策略组合的失效揭示了当前适应机制的局限性。

】

---

【WALT: Web Agents that Learn Tools ｜基于工具逆向工程的Web智能体自动化

研究机构：Salesforce AI研究院

作者：Viraj Prabhu、Yutong Dai、Matthew Fernandez 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.01524)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01524)

> 导读 当前Web智能体依赖逐步UI交互，在动态布局与长程任务中因元素定位失效而频繁中断，且推理开销巨大。现有技能挖掘方法仅复现成功轨迹，缺乏对网站底层功能的抽象，导致执行脆弱且效率低下。WALT通过离线逆向工程将网站固有功能转化为确定性工具，使智能体从“模拟点击”转向“调用接口”。该方法在VisualWebArena与WebArena上刷新了成功率纪录，但其离线工具发现机制对网站动态更新的适应性仍存疑。

】

---

【WARC-Bench：基于Web Archive的GUI子任务执行基准，填补单步接地与长程导航间的评估空白

作者：Sanjari Srivastava、Gang Li、Cheng Chang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.09872)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09872)

> 现有GUI智能体评估体系存在断层：单步视觉接地任务过于简单，无法反映多步交互能力；而WebArena等长程导航基准又因任务复杂度过高，难以定位智能体在具体UI组件上的失效点。本文提出GUI子任务这一中间复杂度层级，并构建基于Web Archive（WARC）文件回放的沙箱化基准WARC-Bench，以确定性奖励函数评估智能体在真实网站快照上的短程任务执行能力。通过监督微调（SFT）与可验证奖励强化学习（RLVR）训练开源模型，验证了子任务训练对长程导航的迁移价值，但WARC静态回放与真实动态网页间的分布差异对鲁棒性的影响仍未被量化。

】

---

【WEB-COGREASONER: TOWARDSOWARDS MULTIMODALULTIMODAL KNOWLEDGE-INDUCED COGNITIVE REASONING FOR WEB AGENTS ｜基于布卢姆分类法的Web智能体认知推理框架

研究机构：上海交通大学、中南大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_8703016)

> Web智能体在开放网络中执行长程任务时，常因缺乏对页面元素语义与交互逻辑的深层理解而陷入重复循环或动作失效。现有方法多依赖端到端模仿学习或即时上下文拼接，忽视了“先积累知识、后应用推理”的认知构建过程，导致模型在未见过的复杂场景下泛化能力不足。本文借鉴布卢姆分类法，将Web知识解构为事实、概念与程序三层，并通过课程学习与知识驱动思维链（KCoT）训练多模态智能体。该框架在认知密集型任务上显著优于基线，但在通用导航成功率上仍落后于当前多模态SOTA，其知识内化机制对长程自主探索的支撑力尚存疑。

】

---

【WebArbiter: A Principle-Guided Reasoning Process Reward Model for Web Agents ｜WebArbiter：基于原则诱导推理的Web过程奖励模型

研究机构：德国慕尼黑大学、德国慕尼黑工业大学

作者：Yao Zhang、Shijie Tang、Zeyu Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21872)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21872)

> 导读 长程Web交互中，结果奖励模型（ORM）仅提供稀疏且延迟的反馈，无法指导推理时的搜索策略，而现有过程奖励模型（WebPRM）要么将进度压缩为不可解释的标量分数，要么依赖在动态布局下极易失效的固定检查表。WebArbiter将过程奖励建模重构为文本生成任务，通过动态从用户意图和当前状态中诱导评估原则，生成包含结构化理由的偏好裁决，从而提供可审计的步骤级信号。其训练采用推理蒸馏与强化学习两阶段流水线，并在首个跨环境基准WEBPRMBENCH上验证了性能优势。该工作填补了Web智能体细粒度评估的空白，但其仅依赖文本可访问性树的输入模态，在复杂视觉UI下的接地能力存疑。

】

---

【WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents ｜WebFactory：基于离线高保真环境的智能体智能压缩流水线

研究机构：复旦大学、香港中文大学

作者：Sicheng Fan、Qingyun Shi、Shengze Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05044)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05044)

> 导读

】
