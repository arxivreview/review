# Others2026 · 大语言模型与智能体方向论文汇编

> 本方向共 42 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agentic AI for Human Resources: LLM-Driven Candidate Assessment ｜基于LLM的主动列表式锦标赛候选人评估系统

作者：Kamer Ali Yuksel、Abdul Basit Anees、Ashraf Elneima 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.26710)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26710)

> 传统招聘系统依赖关键词匹配或浅层语义相似度，难以捕捉候选人多维能力的复杂权衡，且独立打分或成对比较在大规模候选池中噪声大、扩展性差。本文切入点在于将LLM视为“模糊裁判”，通过小群体列表式排序获取更丰富的偏好信号，并利用概率模型聚合为全局效用。具体做法是构建多智能体框架生成角色特定评分标准，结合主动学习循环动态选择最具信息量的候选子集进行列表式评估，最终通过Plackett-Luce模型推断全局排名。该框架在减少LLM查询次数的同时提升了排序稳定性，但其公平性保证仅停留在结构化标准层面，缺乏因果层面的偏见阻断机制，且未提供与主流检索基准的可比数值。

】

---

【MRGEN：基于大语言模型的混合现实教育内容生成框架

作者：Mohammed Oussama Seddini、Mohamed Ez-Zaouia、Ngoc Luyen Le 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15341)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15341)

> 导读 混合现实（MR）教育内容创作长期受限于教师编程技能缺失与多模态资源制作的高时间成本，导致沉浸式学习体验难以规模化落地。现有生成式AI（GAI）工具虽能产出文本或图像，但缺乏针对MR场景的教学目标对齐机制，且未解决教师从灵感激发到内容组装的全流程辅助问题。本文提出MRGEN框架，通过解耦学习目标、MR模态与AI辅助层级三个维度，构建了从资源生成到个性化交互的完整工作流。该框架在降低创作门槛上展现出显著效用，但其对生成内容事实准确性的验证机制缺失，限制了其在严谨学科教学中的直接应用。

】

---

【NLP Privacy Risk Identification in Social Media (NLP-PRISM): A Survey ｜社交媒体NLP隐私风险识别框架

研究机构：美国乔治梅森大学

作者：Dhiman Goswami、Jai Kruthunz Naveen Kumar、Sanchari Das

论文原文见 [arXiv](https://arxiv.org/abs/2602.15866)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15866)

> 社交媒体NLP任务在处理用户生成内容时，常因模型记忆或推理泄露个人身份信息（PII）、行为线索及人口统计属性，导致监控与画像风险。现有隐私研究多聚焦于通用大语言模型（LLM）的训练数据提取，缺乏针对特定NLP任务（如方言识别、情感分析）的细粒度风险评估标准。本文提出NLP-PRISM框架，通过六个维度系统化梳理203篇文献中的隐私漏洞，并量化隐私保护对模型效用的影响。该工作填补了任务级隐私评估的空白，但其基于小模型的实验结果能否推广至生产级LLM，仍存疑。

】

---

【Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments ｜串行两阶段层限制遗忘框架

作者：Esen Kurt、Haithem Afli

论文原文见 [arXiv](https://arxiv.org/abs/2604.12459)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12459)

> 大语言模型在政治敏感场景下的部署面临“被遗忘权”合规与通用能力保持的结构性冲突。现有联合优化方法因保留与遗忘梯度方向冲突导致训练不稳定或效用崩溃，而完全重训练在计算上不可行。本文提出一种串行两阶段优化策略，先通过正向微调锚定良性能力，再对高层参数执行受限负向微调以抑制敏感模式。该框架在GPT-2上实现了行为层面的有效抑制，但其机制深度与对抗鲁棒性未经验证，且实验局限于小模型规模。

】

---

【PATHWAYS: Evaluating Investigation and Context Discovery in AI Web Agents ｜调查能力评估基准

作者：Shifat E. Arman、Syed Nazmus Sakib、Tapodhir Karmakar Taton 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.05354)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05354)

> 现有 Web 智能体基准主要考察指令执行或恶意拒绝，忽略了真实场景中智能体需主动挖掘隐藏证据以做出正确决策的“调查能力”。当前模型在信息不对称环境下普遍存在导航与证据获取脱节、表面线索误导下决策崩溃及虚构调查过程等系统性缺陷。本文构建包含 250 个多步决策任务的 PATHWAYS 基准，通过强制过程依赖指标量化智能体在电商客服与社区审核中的调查、推理与决策全轨迹。该工作揭示了现有智能体作为“模式匹配器”而非“审慎调查者”的本质局限，但其评估结果高度依赖任务设计中的信息不对称强度，且未提供解决该缺陷的架构方案。

】

---

【QueStER: Query Specification for Generative keyword-based Retrieval ｜生成式查询规格检索

研究机构：法国巴黎萨克雷大学、法国国家科学研究中心

作者：Arthur Satouf、Yuxuan Zong、Habiboulaye Amadou-Boubacar 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.05301)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.05301)

> 信息检索模型需在语义理解与计算效率间取得平衡，传统词汇匹配模型受限于词汇不匹配问题，而神经检索器因索引维护成本高难以动态更新。现有基于大语言模型的查询重写方法虽提升了效果，但依赖庞大参数与复杂提示，导致推理延迟高且结果不稳定。QUESTER 将生成式检索的目标从文档标识符转向关键词查询规格，利用强化学习微调轻量级大语言模型生成检索指令，由标准倒排索引执行。该方法在保持毫秒级检索延迟的同时，显著超越了基线词汇模型，但在域内绝对精度上仍低于专用神经检索器，其泛化边界尚待复杂查询场景验证。

】

---

【Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics ｜拒绝转向：基于岭正则化激活引导的政治敏感话题细粒度控制

作者：Iker García-Ferrero、David Montero、Roman Orus

论文原文见 [arXiv](https://arxiv.org/abs/2512.16602)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16602)

> 导读 大语言模型在政治敏感话题上常表现出意识形态偏见，导致对合法信息的过度拒绝，而传统微调方法因成本高且易破坏通用能力而难以精准修正。现有激活引导方法依赖简单的均值差或模式匹配，无法处理现代推理模型中复杂的、非显式的拒绝行为（如宣传式回答）。本文提出一种推理时干预方法，通过LLM-as-a-judge量化拒绝置信度，并引入岭正则化变体计算更鲁棒的转向向量，在不重训练的前提下实现政治拒绝的移除或引入。该方法在80B模型上有效降低了政治拒绝率并保持了安全性，但在小模型上安全性显著下降，其解耦能力的边界尚存疑。

】

---

【Retrieval as Generation: A Unified Framework with Self-Triggered Information Planning ｜检索即生成：基于自触发信息规划的统一框架

研究机构：北京大学

作者：Bo Li、Mingda Wang、Gexiang Fang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11407)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11407)

> 智能体搜索旨在解决静态检索增强生成（RAG）在多步推理中无法动态调整查询的局限，但现有方法多依赖外部控制器或启发式规则，导致检索时机与生成过程割裂。GRIP 提出“检索即生成”范式，将检索决策内化为模型解码过程中的控制令牌，实现端到端的自主规划。该方法通过结构化监督与规则奖励强化学习，在五个问答基准上超越了同规模基线，但其性能仍受限于骨干模型规模，且未验证其在长程复杂任务中相比多智能体架构的稳定性。

】

---

【Towards Disentangled Preference Optimization Dynamics Beyond Likelihood Displacement ｜解耦偏好优化动态：从似然位移到奖励校准

研究机构：华南理工大学、日本理化学研究所

作者：Wei Chen、Yubing Wu、Junmei Yang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18239)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18239)

> 偏好优化旨在将人类价值观内化至大语言模型，但主流基于边际的目标函数（如DPO）常导致获胜响应概率与落败响应同步下降，即“似然位移”。现有解耦方法虽能缓解此问题，但缺乏统一理论解释其动力学差异，且无法直接应用于已部署的纠缠目标。本文通过激励-分数分解揭示目标函数仅通过标量系数控制更新方向，进而提出解耦带（DB）作为可测试条件，并设计即插即用的奖励校准（RC）以重平衡梯度。该框架在理论上统一了纠缠与解耦目标，但在高维非局部纠缠及在线设置下的有效性尚未验证。

】

---

【Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs ｜回合级优势估计的PPO变体

研究机构：美国德克萨斯大学奥斯汀分校

作者：Junbo Li、Peng Zhou、Rui Meng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.17008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17008)

> 多轮智能体强化学习（Agentic RL）面临的核心困境是：在长程交互中，稀疏且延迟的奖励信号难以准确归因到具体的决策步骤，导致策略优化陷入不稳定甚至崩溃。当前主流算法组相对策略优化（Group Relative Policy Optimization, GRPO）因依赖采样均值估计优势，在高方差的多轮环境中表现脆弱，而传统近端策略优化（Proximal Policy Optimization, PPO）若沿用Token级建模，则因状态转移不连续导致Critic学习失效。本文通过重构马尔可夫决策过程（Markov Decision Process, MDP）的粒度，将状态-动作对从Token级提升至Turn级，提出Turn-PPO，利用可学习Critic在回合边界进行价值估计，从而获得更稳定的优势信号。该方案在防止训练崩溃方面表现出显著优势，但其绝对性能仍远低于多智能体协作方法，且对模型推理长度的敏感性揭示了其泛化边界的模糊性。

】

---

【VL-KGE: Vision-Language Models Meet Knowledge Graph Embeddings ｜视觉-语言知识图谱嵌入

研究机构：荷兰阿姆斯特丹大学

作者：Athanasios Efthymiou、Stevan Rudinac、Monika Kackovic 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.02435)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.02435)

> 多模态知识图谱嵌入旨在将实体与关系映射至低维连续空间，以解决大规模结构化数据中符号推理计算复杂度高的问题。现有方法在处理真实世界数据时，常因模态独立编码导致语义错位，且假设所有实体具备完整模态，这在艺术品等异构场景中失效。本文提出VL-KGE，利用预训练视觉-语言模型（VLM）提供对齐的跨模态表示，结合结构嵌入实现统一实体表示。该方法在模态不对称场景下显著提升了链接预测性能，但其对VLM骨干的依赖及缺乏GNN结构编码的对比，限制了其在复杂层级结构上的通用性验证。

】

---

【When LLM meets Fuzzy-TOPSIS for Personnel Selection through Automated Profile Analysis ｜基于DistilRoBERTa与模糊TOPSIS的自动化人员筛选框架

作者：Shahria Hoque、Ahmed Akib Jawad Karim、Md. Golam Rabiul Alam 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.22433)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22433)

> 导读 传统招聘依赖主观人工判断，导致评估不一致且难以规模化，而现有AI工具往往牺牲可解释性以换取自动化效率。本文切入点在于将Transformer模型的文本理解能力与模糊多准则决策理论结合，以显式建模人类评估中的主观性与不确定性。具体做法是微调DistilRoBERTa对LinkedIn档案属性进行分类打分，再通过模糊TOPSIS算法聚合为最终排名。该框架在自建数据集上实现了与专家判断的高一致性，但其泛化能力与公平性审计缺失限制了工业级应用的可靠性。

】

---

【伦敦玛丽女王团队新研究：对话事实核查中的语义一致性门控

研究机构：英国伦敦玛丽女王大学

作者：Hyunkyung Park、Arkaitz Zubiaga

论文原文见 [arXiv](https://arxiv.org/abs/2604.14389)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14389)

> 对话事实核查需处理口语化噪声导致的检索与验证冲突，现有重写方法因语义漂移损害验证精度。本文通过分阶段去口语化与双向NLI一致性门控，在保留检索增益的同时抑制验证错误。该方法在DialFact上实现了端到端性能的稳健提升，但其绝对性能受限于单证据检索瓶颈，且未解决多跳逻辑依赖问题。

】

---

【兰卡斯特团队新研究：黑盒多模态大语言模型下的视觉隐私保护

研究机构：英国兰卡斯特大学、英国布里斯托大学

作者：Xiaofei Hui、Qian Wu、Haoxuan Qu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13978)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13978)

> 多模态大语言模型（MLLM）云服务要求用户上传原始图像或视频，导致面部、肤色等敏感属性直接暴露，而现有隐私保护方法多依赖白盒访问或牺牲效用。本文切入点在于将MLLM视为不可访问内部参数的黑盒函数，通过输入端匿名化在保护隐私的同时维持模型效用。方法核心是构建基于Pareto最优性的多目标优化框架，结合关键历史增强零阶优化以解决黑盒梯度估计的不稳定性。该工作验证了黑盒场景下隐私-效用平衡的可行性，但其缺乏形式化隐私保证，且依赖特定隐私审查器，在合规严格场景下的适用性存疑。

】

---

【动态秩强化学习

作者：Caner Erden

论文原文见 [arXiv](https://arxiv.org/abs/2512.15973)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15973)

> 大语言模型（LLM）中多头自注意力（Multi-Head Self-Attention, MHSA）的计算复杂度随序列长度平方增长，静态低秩近似因无法适应输入语义复杂度的动态变化，导致在长序列推理中陷入计算冗余与信息损失的帕累托困境。现有方法将秩视为固定超参数，忽略了不同层、不同注意力头对语义依赖捕获需求的实时差异。DR-RL 将秩选择重构为马尔可夫决策过程，利用强化学习智能体结合在线矩阵扰动理论，在推理时动态调整谱秩以平衡保真度与计算开销。该框架在长序列场景下实现了显著的计算节省，但其依赖离线训练的复杂策略网络，且缺乏与主流静态压缩方法的直接横向对比，实际部署的硬件友好性存疑。

】

---

【华盛顿团队新研究：基于编译器反馈的Lean证明修复

研究机构：美国华盛顿大学

作者：Evan Wang、Simon Chess、Daniel Lee 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.02990)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02990)

> 现有Lean证明数据集仅包含最终验证通过的正确证明，导致模型缺乏对编译错误诊断与修复的监督信号，无法有效执行迭代修正。本文切入点在于将“证明修复”从智能体框架中的隐式环节剥离，定义为独立的监督学习任务，通过系统化变异正确证明生成26万条错误-正确配对数据，并联合监督代码修复与自然语言诊断。该方法在单步修复评估中使4B模型性能超越32B基线，但变异生成的错误分布是否覆盖真实开发中的长程依赖错误，仍存疑。

】

---

【南非开普敦团队新研究：基于答案集编程的可废止条件句声明式编码

研究机构：南非开普敦大学

作者：Racquel Dennison、Jesse Heyninck、Thomas Meyer

论文原文见 [arXiv](https://arxiv.org/abs/2601.03840)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03840)

> 可废止推理旨在从包含例外情况的不完整信息中推导合理结论，传统命令式算法在处理大规模知识库时面临效率与可维护性的双重瓶颈。本文切入点在于利用答案集编程（Answer Set Programming, ASP）的声明式范式重构理性闭包（Rational Closure, RC）算法，通过最小化指令自动构建最小排名模型。该方法在保持逻辑严谨性的同时，显著提升了蕴含推理的计算效率。尽管实验显示其性能优于现有基线，但其在极大规模知识库下的可扩展性边界尚未得到充分验证。

】

---

【博洛尼亚团队新研究：大语言模型推理能效解析模型

研究机构：意大利博洛尼亚大学

作者：Hiari Pizzini Cavagna、Andrea Proia、Giacomo Madella 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.05695)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05695)

> 大语言模型推理能耗预测长期依赖线性假设，忽略了Transformer自回归结构中预填充与解码阶段计算特性的非线性差异，导致生产环境无法精准定位能效峰值配置。现有仿真器虽能模拟硬件动态，但缺乏可解释的解析公式，且精度受限于离散时间步长模拟。本文基于FLOPs与内存访问复杂度推导了SweetSpot解析模型，通过非线性最小二乘拟合验证其在1B-9B参数模型上的预测精度。该模型为能效优化提供了理论工具，但其单卡静态负载假设限制了在动态调度场景下的适用性。

】

---

【卡内基梅隆团队新研究：速度换质量：LLM 代理助手对项目级开发速度与代码复杂度的因果影响

研究机构：美国卡内基梅隆大学

作者：Hao He、Courtney Miller、Shyam Agarwal 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.04427)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04427)

> 该方向旨在量化 LLM 代理助手在真实开源项目中对开发速度与代码质量的长期因果影响，以解决现有研究局限于短期任务完成时间或单一代码片段质量评估的盲区。现有方法多基于受控实验或静态代码分析，无法捕捉代理工具引入后项目级技术债务的累积动态及其对后续开发速度的反馈效应。本文通过扫描 GitHub 仓库中的 `.cursorrules` 配置文件识别 Cursor 代理模式的采用时间，构建交错采用差异中差异（Difference-in-Differences, DiD）模型，并结合动态面板广义矩估计（Generalized Method of Moments, GMM）分析速度与质量的交互机制。该研究提供了首个大规模实证证据，表明代理工具带来的速度增益是短暂的，而代码复杂度的增加是持久的，且后者会显著抵消前者的收益。

】

---

【印第安纳团队新研究：局部差分隐私下的分类优化：模型反转与平均

研究机构：美国印第安纳大学

作者：Caihong Qin、Yang Bai

论文原文见 [arXiv](https://arxiv.org/abs/2602.05797)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05797)

> 局部差分隐私（LDP）通过数据源扰动消除对可信服务器的依赖，但引入的高噪声常导致分类器性能低于随机猜测，且传统方法难以在无目标数据观测下量化这种效用损失。现有LDP分类算法多聚焦于基础估计器，缺乏对“负迁移”现象的系统性修正机制。本文切入点在于将LDP私有学习重构为转移学习问题，利用含噪数据作为源域，通过基于随机响应的二值反馈评估数据集效用，并引入模型反转（MR）与模型平均（MA）技术，在固定隐私预算下显著提升分类准确率。该框架在低隐私预算下表现优异，但其理论边界是否适用于高维连续特征空间仍存疑。

】

---

【哈尔滨工业团队新研究：任务导向对话的Schema感知指令微调

研究机构：哈尔滨工业大学、中南大学

作者：Dechuan Teng、Chunlin Lu、Libo Qin 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09691)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09691)

> 任务导向对话（Task-Oriented Dialog, TOD）系统需精准执行多轮交互中的状态追踪与数据库查询，但现有端到端模型往往绑定特定数据集的标注结构，难以迁移至新场景。传统预训练对话模型（Pre-trained Conversation Models, PCMs）通过多任务预训练提取通用知识，却忽略了数据标注与底层数据库Schema的强耦合，导致跨域适配能力薄弱。本文提出ESAinsTOD框架，通过指令对齐与Schema对齐机制，将异构TOD数据统一为指令微调语料，使大语言模型（Large Language Models, LLMs）在保持通用能力的同时精准遵循特定Schema。该框架在MultiWOZ等基准上显著优于基线，但其对全参数微调的依赖及缺乏与通用指令微调方法的横向对比，限制了其结论的普适性。

】

---

【圣母团队新研究：基于言语行为与人际欺骗理论的多智能体语言欺骗实证分析

研究机构：美国圣母大学

作者：Maria Milkowski、Tim Weninger

论文原文见 [arXiv](https://arxiv.org/abs/2603.26635)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26635)

> 多智能体博弈中的策略性欺骗长期被简化为胜负结果或内部激活探针，忽视了语言微观结构对欺骗意图的承载作用。现有基准多关注“是否欺骗”的二元判定，缺乏对“如何欺骗”的机制性语言学解构。本文切入点在于将言语行为理论与人际欺骗理论（IDT）引入LLM多智能体交互，通过大规模模拟量化话语类型与欺骗策略的分布及其对胜负的影响。其价值在于提供了黑盒文本层面的欺骗行为描述框架，但受限于单一模型架构与自动标注的可靠性边界，其结论的普适性存疑。

】

---

【多模型共识驱动的系统性文献综述语料筛选

作者：Lucas Joos、Daniel A. Keim、Maximilian T. Fischer

论文原文见 [arXiv](https://arxiv.org/abs/2510.11409)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11409)

> 系统性文献综述（SLR）的语料筛选环节长期依赖人工逐篇阅读标题与摘要，面对数千篇候选文献时耗时数月且易受疲劳影响。现有自动化方案多依赖单一模型或简单关键词匹配，难以在保持高召回率（避免漏掉相关文献）的同时控制假阳性（误留无关文献）。本文切入点在于利用多个大语言模型（LLM）的互补性，通过保守共识投票机制平衡召回与精确。具体做法是构建一个由人类监督的半自动流水线，让多个LLM独立分类后，仅当所有模型均判定排除时才剔除文献。该方法在8,323篇真实语料上验证了可行性，但100%召回率是以显著增加人工复核假阳性为代价的，其实际效率增益需结合具体场景评估。

】

---

【天津团队新研究：大语言模型预训练数据混合优化综述

研究机构：天津大学、中国科学院

作者：Zhuo Chen、Yuxuan Miao、Supryadi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16380)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16380)

> 预训练数据混合旨在有限算力下通过调整领域采样权重最大化模型泛化能力，但现有方法在静态规则与动态学习间存在显著的性能-成本权衡缺口。本文切入点在于构建统一的概率单纯形双层优化形式化框架，将分散的启发式与学习式方法纳入“静态/动态”与“规则/学习”二维分类体系。通过解析代理模型依赖与在线信号驱动的机制差异，本文揭示了方法迁移性瓶颈的根源。该综述提供了可复用的概念分析工具，但其对最新在线重加权方法的覆盖度及跨配置迁移性的实证验证仍存疑。

】

---

【庆应义塾团队新研究：控制屏障函数对齐大语言模型

研究机构：日本庆应义塾大学

作者：Yuya Miyaoka、Masaki Inoue

论文原文见 [arXiv](https://arxiv.org/abs/2511.03121)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.03121)

> 现有安全对齐方法多依赖参数更新或静态规则过滤，难以在免训练条件下提供形式化的安全保证。本文切入点在于将文本生成视为离散动力系统，引入控制论中的控制屏障函数（Control Barrier Function, CBF）作为推理时安全滤波器。通过构建语言约束函数并施加CBF不等式约束，该方法在不修改基座模型参数的前提下，动态干预Token分布以抑制有害输出。其价值在于提供了首个基于控制理论的安全对齐框架，但缺乏与主流基准（如AdvBench）的量化对比，有效性验证仍停留在可行性层面。

】

---

【心理测量学驱动的LLM评估平台

作者：Zhiye Jin、Yibai Li、K. D. Joshi 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13126)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13126)

> 当前LLM评估工具过度依赖开发者视角，导致心理学家与认知科学家难以介入模型内部结构的量化分析。现有基准面临饱和与污染，且缺乏面向非技术专家的集成化心理测量接口。本文通过设计科学三循环构建云原生平台，将经典测试理论与认知负荷理论嵌入评估流程。该工作实现了评估工具的工程化落地，但其效度验证仅覆盖技术接受度维度，未触及深层认知能力的区分度。

】

---

【慕尼黑工业团队新研究：旅游推荐中的智能体反事实解释

研究机构：德国慕尼黑工业大学、德国卡尔斯鲁厄理工学院

作者：Ashmi Banerjee、Adithi Satish、Wolfgang Wörndl 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14223)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14223)

> 对话式推荐系统长期面临用户偏好与系统目标冲突的困境，传统方法往往将可持续性视为次要约束或硬性过滤条件，导致用户体验受损或推荐僵化。TRACE 切入点在于利用多智能体架构动态推断用户的“妥协意愿”，并通过反事实解释在尊重用户显式偏好的前提下，隐性引导其关注更可持续的选项。系统通过 Orchestrator-Worker 范式协调澄清、意图分类、推荐生成与解释生成四个专用智能体，实现了从静态打分到动态行为引导的范式转换。该工作验证了 LLM 智能体在复杂决策支持中的可行性，但其评估缺乏客观精度指标，且存在“可持续悖论”这一未解的系统性风险。

】

---

【新西兰奥克兰团队新研究：基于关系预言的大语言模型测试

研究机构：新西兰奥克兰大学

作者：Valerio Terragni

论文原文见 [arXiv](https://arxiv.org/abs/2603.24774)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24774)

> 大语言模型（LLM）嵌入软件系统后，其输出开放、非确定且缺乏标准答案，导致传统基于人工标注的测试预言（Test Oracle）在规模上不可行。现有自动化测试方法多依赖执行反馈或文档断言，难以覆盖 LLM 行为中的细微逻辑违背。本文切入点在于利用元测试（Metamorphic Testing, MT）中的关系预言，通过定义输入变换与输出预期关系，实现无需 Ground Truth 的大规模自动化验证。该方法通过 LLMORPH 框架在三个主流 LLM 上执行了 56 万次测试，暴露了平均 18% 的故障率，但 62% 的真阳性率揭示了语义歧义带来的假阳性瓶颈，其作为 CI 流水线回归信号的有效性仍受限于输出比较器的精度。

】

---

【新西兰奥克兰团队新研究：天体力学约束下的 LLM 策略生成与执行断裂

研究机构：新西兰奥克兰大学

作者：Iñaki del Campo、Pablo Cuervo、Victor Rodriguez-Fernandez 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03630)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03630)

> 该方向旨在评估大语言模型在物理硬约束与高维组合优化环境中的自主规划能力。现有基准多聚焦于静态知识或博弈胜率，无法量化模型在复杂工程任务中从“概念框架”到“可执行代码”的转化效率，本文切入点在于引入天体力学竞赛作为高难度物理约束测试场。通过改造 AIDE 架构并建立基于专家量表的 LLM 裁判评估体系，量化了模型策略理解的层级差异。该研究揭示了推理模型在策略层面的显著优势，但所有模型均未能生成通过验证器的有效解，暴露了当前 LLM 在物理实现层面的根本性执行壁垒。

】

---

【智利天主教团队新研究：拉美文化基准构建：基于 Wikidata 本体与社会学筛选的 LatamQA

研究机构：智利天主教大学

作者：Yannis Karmim、Renato Pino、Hernan Contreras 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10001)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10001)

> 大语言模型在跨文化部署中普遍存在西方中心主义偏差，但针对拉丁美洲（Latam）的细粒度评估资源长期匮乏，现有数据集或规模过小，或地理粒度粗糙，无法区分区域内不同国家的文化特异性。本文切入点在于利用 Wikidata 知识图谱的结构化本体与社会学专家筛选机制，构建一个覆盖 20 个拉美国家、包含 23,499 道选择题的大规模基准 LatamQA。通过结合维基百科类别递归抓取、Longformer 微调过滤及 LLM 生成问答，本文量化了模型在拉美与伊比利亚西班牙文化知识上的性能差异。该工作填补了拉美文化评估的空白，但其依赖选择题形式且未解决深层价值观对齐问题，其结论的普适性仍受限于事实性知识范畴。

】

---

【条件评论预测的操作效度评估

作者：Nils Schwager、Simon Münker、Alistair Plum 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22752)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22752)

> 社交媒体用户模拟的核心难题在于，模型生成的文本往往看似合理，却无法复现特定个体的真实行为模式，即缺乏操作效度。现有方法多依赖属性描述进行提示，但这一假设从未在真实数据上得到严格检验。本文提出条件评论预测（Conditioned Comment Prediction, CCP）任务，通过对比模型生成与真实用户回复来量化这种对齐能力。其价值在于揭示了低资源语言下微调的语义退化风险，但结论受限于8B参数模型与单一平台数据。

】

---

【石溪团队新研究：语法易，语义难：LLM 翻译线性时态逻辑的评估

研究机构：美国石溪大学

作者：Priscilla Kyei Danso、Mohammad Saqib Hasan、Niranjan Balasubramanian 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07321)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07321)

> 自然语言到形式逻辑的自动翻译是连接大语言模型（LLM）与符号分析工具的关键桥梁，但现有评估多聚焦于静态逻辑，忽视了时序逻辑中算子作用域的复杂性。本文针对命题线性时态逻辑（LTL）这一安全领域核心形式化语言，构建了六层评估框架，系统解耦语法与语义正确性。通过对比三种提示接口，发现将翻译任务重构为Python代码补全能显著提升性能，但语义等价率仍低于75%。该研究揭示了LLM在时序推理上的结构性缺陷，为安全关键系统的自动化规格生成提供了实证边界。

】

---

【社会科学人文领域引用处理基准与混合部署策略

作者：Yurui Zhu、Giovanni Colavizza、Matteo Romanello

论文原文见 [arXiv](https://arxiv.org/abs/2603.13651)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13651)

> 构建大规模学术引用索引的前提是可靠的参考文献提取与解析，但现有评估体系过度依赖清洁的英文尾注，掩盖了社会科学人文（SSH）文献中脚注密集、多语言混排及缩写变体带来的系统性失效。本文切入点在于指出这种“实验室式”数据与真实SSH文档之间的分布错位，并构建了一个覆盖三种典型SSH场景的统一基准。通过对比监督基线GROBID与前沿大语言模型（LLM），本文验证了LLM在分布外场景下的鲁棒性优势，并提出了基于路由的混合部署策略。该工作填补了SSH引用处理评估的空白，但其对长文档截断问题的处理仍依赖工程妥协，未从模型层面根本解决结构化输出的稳定性。

】

---

【端侧隐私保护自主谈判智能体

作者：Joyjit Roy、Samaresh Kumar Singh

论文原文见 [arXiv](https://arxiv.org/abs/2601.00911)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.00911)

> 导读

】

---

【自适应Web渗透测试框架

作者：Akshat Singh Jaswal、Ashish Baghel

论文原文见 [arXiv](https://arxiv.org/abs/2603.00960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00960)

> 现代Web应用开发速度远超传统安全工具的静态检测能力，导致注入类漏洞在快速部署中持续存在。现有基于模式的扫描器缺乏推理能力，而通用LLM智能体虽具推理力但成本高、行为不稳定且缺乏领域特异性。AWE通过嵌入漏洞专用分析流水线与持久记忆机制，在LLM编排下实现目标化、可解释的漏洞发现。该框架在注入类漏洞上显著优于通用智能体，但其整体覆盖率仍受限于专用架构的泛化边界。

】

---

【语义融合：去中心化多智能体系统的可验证对齐

作者：Sofiya Zaichyk

论文原文见 [arXiv](https://arxiv.org/abs/2601.12580)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12580)

> 去中心化多智能体系统（MAS）面临的核心矛盾是：智能体需独立决策以维持适应性，但缺乏全局观测导致行为难以验证。现有符号系统缺乏动态鲁棒性，而基于大语言模型（LLM）的神经组件虽具灵活性，却因输出缺乏显式结构而无法追溯合规性。本文提出“语义融合”框架，通过本体切片（Ontology Slice）限制智能体对共享内存的访问范围，并强制所有更新经过本地语义验证，从而在无中心控制、无显式消息传递的条件下实现全局语义一致性。该框架提供了双模拟（Bisimulation）定理以证明局部执行与全局语义的行为等价性，但其有效性依赖于预定义的本体约束，在应对LLM输出的语义漂移及动态本体演化方面存在显著局限。

】

---

【赫尔辛基团队新研究：基于图结构探索的交互式推理基准求解

研究机构：芬兰赫尔辛基大学、南非开普敦大学

作者：Evgenii Rudakov、Jonathan Shock、Benjamin Ultan Cowley

论文原文见 [arXiv](https://arxiv.org/abs/2512.24156)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24156)

> ARC-AGI-3 旨在评估智能体在无指令环境下通过交互发现游戏机制的能力，现有前沿大语言模型（LLM）因缺乏状态追踪与系统性假设测试机制，在此类稀疏反馈任务中表现远逊于随机策略。本文切入点在于摒弃 LLM 的语义推理，转而采用纯视觉特征提取与图结构状态空间探索，以解决 LLM 在动态交互中“知道-做”差距导致的策略失效。该方法通过维护已探索状态的有向图并基于视觉显著性优先选择动作，实现了无训练条件下的有效机制发现。其价值在于证明了结构化探索在特定稀疏反馈场景下优于当前最佳 LLM 基线，但该方法对确定性环境的依赖及其在大规模状态空间下的计算瓶颈，限制了其作为通用智能体架构的普适性。

】

---

【选择性LLM引导正则化

作者：Shanglin Yang、Zhan Shi

论文原文见 [arXiv](https://arxiv.org/abs/2512.21526)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21526)

> 推荐系统在冷启动与长尾场景下因协同信号稀疏而失效，LLM虽能提供语义先验，但直接部署成本高昂且存在位置偏差，全局蒸馏则强制模型模仿不可靠的LLM输出。本文指出LLM信号具有“局部可靠性”，仅在特定稀疏区域有效，而非全局可信。S-LLMR通过可学习门控机制筛选可靠信号，并以成对排序损失替代全局模仿，实现零推理开销的知识注入。该方法在稀疏场景下显著优于全局蒸馏，但其收益是否源于LLM语义本身还是仅作为正则项，尚存疑。

】

---

【金融语言模型偏见检测的成本优化

作者：Firas Hadj Kacem、Ahmed Khanfir、Mike Papadakis

论文原文见 [arXiv](https://arxiv.org/abs/2603.08267)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08267)

> 金融语言模型在招聘与信贷决策中应用时，其内部编码的性别与种族偏见可能导致歧视性结果，但现有检测手段依赖对海量输入进行全量变异测试，计算成本高昂且难以适配持续迭代场景。传统反事实测试范式假设所有输入具有同等揭示偏见的概率，忽视了偏见触发输入的稀疏性与跨模型分布差异。本文利用轻量级分类模型预测概率分布的偏移量作为代理指标，对测试输入进行优先级排序，从而在大幅缩减推理成本的前提下高效定位大型生成模型的偏见行为。该方法在金融领域实现了检测效率的突破，但其跨架构迁移能力与对隐性偏见的覆盖度仍存疑。

】

---

【面向实证软件工程的LLM标注操作化框架

作者：Mia Mohammad Imran、Tarannum Shaila Zaman

论文原文见 [arXiv](https://arxiv.org/abs/2512.15979)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15979)

> 实证软件工程（ESE）中LLM标注的可复现性危机源于配置细节缺失与测量属性未定义，现有指南仅覆盖通用建议而未建立操作化标准。本文切入点是将LLM标注重构为可审计的测量过程，提出OLAF框架以标准化可靠性、校准、漂移等核心构念。该框架通过六维指标体系与六种工作流配置，为ESE研究提供透明化标注协议。其价值在于填补了ESE领域方法论空白，但作为立场论文缺乏实证验证，框架有效性仍待后续研究确认。

】

---

【面向软件工程的LLM代码评估基础设施

作者：Daniel Rodriguez-Cardenas、Xiaochang Li、Marcos Macedo 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21070)

> 现有LLM代码评估体系面临静态基准饱和、指标单一及数据管道碎片化的三重困境，导致无法区分模型的真实推理能力与记忆效应。本文指出当前评估过度依赖准确率，忽视了可解释性、公平性等软件工程核心属性，且缺乏统一的数据工程标准。作者提出BEHELM框架，通过定义“软件场景”与“多维指标”的笛卡尔积空间，构建了一个标准化的评估基础设施。该框架在理论上整合了分散的评估维度，但尚未提供具体的自动化实现或大规模实验验证，其实际效用取决于社区对标准化协议的采纳程度。

】

---

【麦吉尔团队新研究：分词税的经济量化与推理模型缓解效应

研究机构：加拿大麦吉尔大学

作者：Jessica M. Lundin、Ada Zhang、Nihal Karim 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.05486)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.05486)

> 多语言大语言模型（LLM）中，低资源语言因分词碎片化导致序列长度激增，进而引发计算成本与模型性能的双重劣势。现有研究多聚焦于分词算法的技术改进或单纯的准确率差距描述，缺乏将分词效率（Fertility）转化为具体经济成本并评估推理模型缓解能力的系统性框架。本文通过扩展AfriMMLU基准至10个模型与16种非洲语言，建立Fertility与准确率的线性回归关系，并推导二次方计算复杂度下的成本放大效应。该工作揭示了分词偏差的经济实质，但未能提供消除该偏差的技术路径，其结论是否适用于非非洲语言体系仍存疑。

】
