# ACL-Findings2026 · 生成式多智能体社会模拟方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CAMO: An Agentic Framework for Automated Causal Discovery from Micro Behaviors to Macro Emergence in LLM Agent Simulations ｜从微观行为到宏观涌现的因果发现框架

研究机构：天津大学

作者：Xiangning Yu、Yuwei Guo、Yuqi Hou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14691)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14691)

> 生成式多智能体社会模拟能复现宏观涌现现象，但无法解释其背后的微观-宏观因果机制，导致干预策略缺乏可泛化性。现有方法或依赖静态变量空间的统计因果发现，或仅做定性演示，均无法在动态自适应环境中恢复可干预的因果结构。CAMO 通过分离“因果识别”与“机制解释”，利用多智能体协作与模拟器内部反事实干预，自动恢复目标涌现结果的最小充分因果接口。该框架在自建基准上实现了高保真的结构恢复与干预排序，但其有效性受限于模拟器内部日志的完备性，且未验证跨模拟器的泛化能力。

】

---

【From Script to Stage: Automating Experimental Design for Social Simulations with LLMs ｜从剧本到舞台：LLM社会模拟实验设计的自动化框架

研究机构：天津大学、山东大学

作者：Yuwei Guo、Zihan Zhao、Xiaowei Liu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1d59bef85a8d)

> 生成式多智能体社会模拟旨在通过大语言模型（LLM）复现复杂社会动力学，但传统实验设计依赖跨学科专家的高成本介入，导致研究门槛高且难以规模化。现有LLM驱动框架虽降低了操作壁垒，却因缺乏结构化约束而难以保证实验的科学严谨性与变量可控性。FSTS框架借鉴电影制作流程，将实验设计解耦为剧本创作、定稿与演员生成三个阶段，通过多智能体协作自动编译高层研究意图为可执行脚本。该框架在古巴导弹危机场景中实现了与历史结局的一致性复现，但其对单一历史事件的依赖及语义相似度指标的局限性，使其在通用科学验证层面的有效性仍存疑。

】

---

【Law in Silico: Simulating Legal Society with LLM-Based Agents ｜法律社会模拟：Law in Silico

研究机构：北京大学

作者：Yiding Wang、Yuxuan Chen、Fanxu Meng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24442)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24442)

> 法律系统作为复杂社会子系统，其动态演化难以通过传统分析法学直接观测，亟需一种能同时捕捉宏观统计规律与微观制度交互的仿真范式。现有通用社会模拟框架缺乏对立法、司法、执法闭环机制的建模，而专用法律智能体研究又局限于单一司法环节，无法反映法律环境对个体行为的系统性影响。Law in Silico 通过分层采样构建基于真实统计分布的智能体画像，并引入 LLM 驱动的 Game Master 模块处理多轮法律交互，实现了从宏观犯罪率复现到微观制度演化的双层验证。该框架在宏观统计保真度上表现稳健，但微观机制的因果解释力与跨模型鲁棒性仍存疑。

】

---

【MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation ｜记忆增强社会模拟

研究机构：天津大学

作者：Yongrui Liu、Deyi Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2606.09198)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09198)

> 自动化社会科学研究长期受限于“检索-生成”范式，导致产出缺乏实证深度与原创性。现有Deep Research智能体仅能重组既有文献，无法产生“一手”经验数据，而纯社会模拟框架又缺乏科研导向。MASS将社会模拟嵌入研究流水线，通过ODD协议标准化实验设计与Ebbinghaus遗忘机制维持智能体认知连贯，从而生成支撑论文写作的原始行为数据。该方法在Insight维度显著优于基线，但其模拟数据的科学有效性尚未接受独立审计。

】

---

【SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution ｜社交智能强化学习中的合作博弈信用分配

研究机构：哈尔滨工业大学

作者：Xiachong Feng、Yi Jiang、Xiaocheng Feng 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18982)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18982)

> 多轮社交对话中，单句对最终结果的贡献难以量化，导致强化学习信号稀疏且缺乏理论依据。现有方法依赖大语言模型进行启发式回溯归因，忽略了语句的前瞻策略价值。本文引入合作博弈论，通过期望效用评估策略潜力，并利用Shapley值实现公平信用分配。该框架在SOTOPIA基准上刷新了7B模型的性能上限，但其高昂的Rollout计算成本限制了实时交互的可行性。

】

---

【Sentipolis: Emotion-Aware Agents for Social Simulations ｜情感状态化智能体架构

研究机构：美国卡内基梅隆大学、日本东京大学

作者：Chiyuan Fu、Lyuhao Chen、Yunze Xiao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18027)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18027)

> 生成式多智能体社会模拟旨在复现高保真人工社会，但现有架构普遍缺乏长时程情感连续性，导致智能体在跨会话交互中出现“情感遗忘”，即被侮辱后后续回合易怒度不增，或重复正向互动无法累积为更强纽带。本文切入点是将情感作为一等持久状态，而非短期信号或离散标签，通过引入连续 Pleasure-Arousal-Dominance (PAD) 向量、双速动态衰减及情感-记忆耦合机制，构建可解释且骨干无关的情感模块。该架构在通信与连续性指标上带来显著提升，但其收益高度依赖底层模型容量，且对社交规范遵守的影响呈现非系统性波动，其科学有效性仍受限于沙盒规模与评估协议的泛化边界。

】

---

【Simulating Crisis Cognition: A Computational Framework for Hypothesis Generation in Crisis Communication ｜危机通信中的生成式结构因果模拟

作者：Changsen Yuan、Yanghao Zhou、Chong Feng 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6b2448378c9a)

> 生成式社会模拟长期停留在对恐慌或谣言传播等宏观现象的定性描述，缺乏对具体干预策略因果效应的定量评估，导致政策制定者在无法开展随机对照试验的高风险场景中缺乏科学依据。现有基于检索增强生成（RAG）或规则启发式的系统往往忽视急性压力下的心理语言接受度，无法区分信息内容本身与呈现顺序对个体行为的不同影响。本文提出 CRISIS COGNITION 框架，将大语言模型（Large Language Model, LLM）重构为反事实实验室，通过生成式结构因果模型（Generative Structural Causal Model, Generative SCM）形式化危机交互，利用分层分析隔离人格混杂变量，以估计语言策略的个体处理效应。该框架在计算层面验证了“情感支架先于事实信息”的处方性假设，但其结论局限于 LLM 内部生成过程，能否外推至真实人类行为仍存疑。

】
