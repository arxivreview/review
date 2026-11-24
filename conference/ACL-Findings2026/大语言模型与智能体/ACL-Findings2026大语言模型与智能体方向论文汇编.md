# ACL-Findings2026 · 大语言模型与智能体方向论文汇编

> 本方向共 784 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【1,729 vs. 1729: The Effect of Scripts and Formats on LLM Numeracy ｜书写系统与格式对大语言模型算术能力的影响

研究机构：美国麻省理工学院

作者：Varshini Reddy、Craig W Schmidt、Seth Ebner 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_63bf8444c8f6)

> 大语言模型在标准阿拉伯数字下的算术表现优异，但一旦数字的书写系统或排版格式偏离训练语料的主流约定，其推理能力便出现断崖式下跌。现有鲁棒性评估多聚焦于数值本身的扰动，忽视了符号系统层面的表征偏差。本文通过构建覆盖21种数字脚本与6种排版格式的受控数据集，量化了这种“脚本税”的规模，并验证了提示工程在缓解该缺陷上的有效性。该研究揭示了多语言数值推理中被长期忽视的盲区，但其结论受限于未测试专门优化的数学模型，且仅通过外部提示而非内部表征修改来应对问题。

】

---

【A Diversity Diet for a Healthier Model: A Case Study of French ModernBERT ｜词汇多样性驱动的预训练数据采样

研究机构：法国巴黎萨克雷大学、法国国家科学研究中心

作者：Louis Estève、Christophe Servan、Thomas Lavergne 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a90563273852)

> 预训练数据规模扩张伴随算力成本激增，而自然文本的冗余性导致随机扩充数据的边际多样性收益递减。现有数据策展方法多聚焦于动态权重调整或质量过滤，忽略了静态子集选择中词汇分布的结构性优化空间。本文提出基于Shannon熵最大化的离线采样算法，在固定算力下将预训练数据缩减94%且维持或提升性能。该策略在编码器预训练场景下验证了多样性对数据量的替代效应，但其结论能否迁移至自回归大语言模型（LLM）尚存疑。

】

---

【A Dual-Phase Self-Evolution Framework for Large Language Models ｜双阶段自进化框架

研究机构：电子科技大学

作者：Haoran Sun、Zekun Zhang、Shaoning Zeng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4626302df13f)

> 大语言模型（LLM）在部署后面临静态参数无法适应动态用户需求与领域知识更新的双重困境。现有偏好优化方法依赖离线静态数据，而记忆增强方法仅通过提示词检索历史交互，均未触及模型内部认知的系统性提升。本文提出双阶段自进化框架（Dual-Phase Self-Evolution, DPSE），通过实时交互信号驱动数据扩展与参数更新，实现用户偏好对齐与领域能力增强的协同。该框架在7B小模型上验证了在线进化的可行性，但其数据扩展策略对分布漂移的潜在影响尚存疑。

】

---

【A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning ｜结构感知熵坍缩优化

作者：Jaeeun Jang、Hansle Lee、Sangmin Kim

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b17ccd6aff8e)

> 强化学习后训练在提升大语言模型单样本推理准确率的同时，往往导致推理路径多样性坍缩，进而削弱测试时扩展（Test-Time Scaling, TTS）的有效性。现有熵正则化方法多采用均匀或启发式策略，未能精准定位引发全局熵衰减的局部关键节点。本文通过 GRPO 策略优化的 logit 坐标精确分解，识别出仅占 5% 的“分支定义”token 是熵坍缩的主要驱动力，并据此实施选择性 KL 正则化。该方法在数学推理基准上同时提升了 Pass@1 与 Pass@k，但其在非可验证任务及更大规模模型上的泛化能力尚存疑。

】

---

【A Herd of Language Models Makes a Better Zero-shot Annotator for Clinical Named Entity Recognition ｜多LLM临床命名实体识别中的上下文感知标签聚合

作者：Seiji Shimizu、Shoko Wakamiya、Eiji Aramaki

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2acd2916a503)

> 临床命名实体识别（NER）的规模化瓶颈在于高质量标注语料的获取成本与数据共享限制。现有零样本大语言模型（LLM）标注方案在临床文本中表现受限，且单一模型输出存在系统性偏差，简单集成策略难以平衡精确率与召回率。本文提出 MARY 框架，通过域自适应预训练与加权对比学习，在表示空间中锚定类别中心，从而选择性整合少数派模型提取的实体。该方法在 i2b2 2010 等基准上显著优于单模型及传统标签模型，但其性能增益高度依赖冲突消解等预处理步骤，且未验证在缺乏高置信度锚点时的鲁棒性。

】

---

【A Multilingual Dataset and Empirical Validation for the Mutual Reinforcement Effect in Information Extraction ｜多语言互强效应数据集与实证验证

研究机构：深圳大学、浙江大学

作者：Chengguang Gan、Sunbowen Lee、Qingyu Yin 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2407.10953)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f6382a3ec64)

> 信息抽取（IE）长期将词级任务（如命名实体识别）与文本级任务（如情感分类）视为独立目标，忽略了二者在同一输入中的双向语义依赖。现有互强效应（Mutual Reinforcement Effect, MRE）研究仅局限于日语，无法验证其跨语言普适性，且缺乏多语言混合数据集支撑系统性消融。本文通过LLM辅助翻译框架构建覆盖英、中、日三语的21个子数据集MMM，并训练统一生成模型OIELLM进行全参数微调，实证了76%的子集存在显著正向互强。该工作填补了MRE多语言验证的空白，但其对开放域任务性能衰减的解释仍显薄弱，且未探讨互强效应在低资源语言中的边界。

】

---

【A Reward-Guided Dual-Phase Framework for Adaptive Inference-Time Reasoning ｜双阶段奖励引导自适应推理框架

研究机构：美国密歇根州立大学、美国宾夕法尼亚州立大学

作者：Yingqian Cui、Zhenwei Dai、Pengfei He 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45e989c92b7a)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段计算量提升大语言模型（LLM）的复杂任务表现，但现有基于过程奖励模型（Process Reward Model, PRM）的树搜索方法通常将规划与执行视为单一节点，导致资源分配与错误传播特性不匹配。本文指出规划步骤的不确定性与执行步骤的错误致命性存在本质差异，统一搜索策略在此结构下效率次优。DREAM 框架将推理显式解耦为规划与执行两个独立搜索阶段，并引入基于实时奖励反馈的动态预算分配机制，在数学与代码生成任务上实现了准确率与计算效率的双重优化。该框架在中等规模骨干模型上验证了阶段解耦的有效性，但其对大规模强化学习训练模型的适用性及理论边界尚存疑。

】

---

【A Survey on Evaluation of LLM-based Agents ｜LLM智能体评估综述：从静态基准到动态轨迹审计

研究机构：以色列耶路撒冷希伯来大学、IBM研究院

作者：Asaf Yehudai、Lilach Eden、Alan Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a8c7105e8291)

> 大语言模型（LLM）智能体评估面临的核心矛盾是静态基准无法捕捉动态交互中的过程质量。现有方法多聚焦单一任务或孤立能力，导致评估碎片化且难以区分模型能力与框架效应。本文切入点在于构建统一评估基础设施并引入全路径过程审计。通过模块化组件与声明式规范，系统性整合了从能力测试到应用部署的多维评估体系。该综述提供了领域认知地图，但其对长时程状态漂移的量化方法仍显不足。

】

---

【a1: Steep Test-time Scaling Law via Environment Augmented Generation ｜环境增强生成

研究机构：中国科学院、美国加州大学默塞德分校

作者：Lingrui Mei、Shenghua Liu、Yiwei Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f48bb6d7678d)

> 大语言模型在复杂推理中常因早期步骤错误导致后续推导级联失效，现有测试时扩展方法多依赖静态提示或内部状态验证，缺乏对中间步骤的实时外部校正机制。本文提出环境增强生成（Environment Augmented Generation, EAG）框架，通过实时环境反馈与动态分支探索解决错误传播问题。该方法将推理形式化为马尔可夫决策过程，利用执行环境验证每一步骤并引导路径选择。EAG在32B模型规模上实现了与更大模型相当的竞赛数学性能，但其依赖外部执行环境的设定限制了其在无代码接口任务中的直接适用性。

】

---

【ABC-Bench: Benchmarking Agentic Backend Coding in Real-World Development ｜后端全生命周期智能体基准

研究机构：复旦大学

作者：Jie Yang、Honglin Guo、Li Ji 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11077)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11077)

> 后端开发涉及代码逻辑、环境配置与服务部署的强耦合，现有基准多将环境预置，仅评估局部代码修改，无法反映生产级交付能力。本文切入点在于构建一个强制智能体自主完成从仓库探索到容器化部署全流程的评估体系。通过自动化流水线从开源仓库提取任务，并以外部API测试作为唯一验证标准，ABC-Bench揭示了当前模型在环境配置环节的显著短板。该基准填补了全生命周期评估空白，但其任务生成依赖GPT-5辅助，可能引入特定模型偏好。

】

---

【Accelerating Prefilling via Decoding-time Contribution Sparsity ｜解码时贡献稀疏性驱动的预填充加速

作者：Zhiyuan He、Yike Zhang、Chengruidong Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a8549e2add1)

> 长上下文大语言模型（LLM）的预填充阶段受限于注意力机制的二次方计算复杂度，导致首字延迟（TTFT）随输入长度急剧增加。现有动态稀疏方法依赖注意力分数幅值进行块筛选，忽略了部分高分块对后续解码实际贡献极低的特性，导致计算冗余。本文通过梯度分析识别出“解码时贡献稀疏性”，提出TriangleMix静态注意力模式，在部分层跳过中间查询-键（Middle Q-K）区域的计算。该方法在128K输入下实现15.3倍注意力内核加速，精度损失小于0.5%，但其静态掩码机制在动态负载下的鲁棒性尚存疑。

】

---

【ACR: Adaptive Context Refactoring via Context Refactoring Operators for Multi-Turn Dialogue ｜自适应上下文重构

研究机构：阿里巴巴集团、香港科技大学

作者：Jiawei Shen、Jia Zhu、Hanghui Guo 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05589)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05589)

> 多轮对话中，模型常因早期错误假设的累积或关键约束被噪声稀释而陷入逻辑死循环，现有方法仅增加信息量却缺乏纠错机制。ACR 指出，被动拼接历史无法解决“上下文惯性”与“状态漂移”，需主动重构历史。该框架通过语义路由动态选择六种重构算子，并采用教师引导自进化训练，将上下文管理与推理解耦。其在QA任务上以极低的Token消耗逼近强化学习性能，但尚未验证在开放式对话中的泛化能力。

】

---

【ADaPT: Token-Level Decoupling for Efficient Large Reasoning Models ｜自适应双过程思维

研究机构：复旦大学、华东师范大学

作者：Tingyun Li、Zishang Jiang、Jinyi Han 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.19919)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.19919)

> 大语言模型在复杂推理任务上依赖长思维链，但简单任务上的冗余推理导致计算成本激增且可能损害准确率。现有长度压缩与混合推理方法在训练时存在效率与正确性信号的序列级耦合，导致正确长推理被系统性惩罚。ADaPT通过引入模式选择Token，将效率奖励与答案正确性在Token级显式解耦，实现推理深度的连续控制。该方法在保持复杂任务精度的同时显著降低推理成本，但其对骨干模型能力的依赖及跨域泛化边界尚待进一步验证。

】

---

【AdapThink: Adaptive Thinking Preferences for Reasoning Language Models ｜自适应思维偏好控制

研究机构：同济大学、北京大学

作者：Wenyue Xu、Xu Wan、Wei Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8a843f781289)

> 导读 该方向旨在解决大型推理模型在简单任务上因冗余反思导致的计算资源浪费，即“过度思考”现象。现有方法多依赖静态长度惩罚或固定Token预算，无法根据问题难度与模型当前能力动态调整推理深度，导致复杂任务探索不足或简单任务冗余严重。AdapThink通过组级分布统计构建动态反思偏好奖励，并引入基于协方差行列式的多样性采样机制，在训练阶段内化自适应推理习惯。该方法在数学与代码任务上实现了准确率与效率的双重提升，但其对组内样本统计稳定性的依赖及跨规模泛化能力仍存疑。

】

---

【AdapTime: Enabling Adaptive Temporal Reasoning in Large Language Models ｜自适应时间推理

研究机构：香港城市大学、西湖大学

作者：Yimin Deng、Yejing Wang、Zhenxi Lin 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24175)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24175)

> 时间推理任务要求模型在静态文档中解析时间约束并定位事实，但现有方法依赖固定流水线或外部工具，导致简单问题过度处理、复杂问题推理不足。AdapTime 通过 LLM Planner 动态选择“重构、重写、审查”三个推理动作，实现了无外部依赖的自适应推理。该方法在 DeepSeek-V3 上将 TempReason-L3 的 F1 从 48.3 提升至 53.2，证明了动态规划的有效性，但其性能上限仍受限于骨干模型自身的时间感知能力。

】

---

【Adaptive Prompt Optimization for Open-Ended Tasks: Uncertainty Preference as a Secondary Signal ｜基于语义熵偏好形状的开放式任务提示优化

研究机构：中国科学技术大学、中国科学院大学

作者：Shuyang Zhang、Zhixuan Liu、Zhichen Dong 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_02d27d69fd01)

> 自动提示优化（Automatic Prompt Optimization, APO）旨在通过算法搜索最优指令以提升大语言模型（LLM）性能，但在开放式任务中，现有方法仅最大化单一标量分数，忽视了任务对生成不确定性的差异化需求。本文指出，安全类任务偏好低熵的保守输出，而创意类任务偏好高熵的多样输出，这种风格依赖性是提示优化不稳定的根源。通过引入语义熵作为辅助选择信号，本文在标准优化器上增加了偏好形状化机制，使提示进化方向与任务风格对齐。该方法在多个模型家族上提升了成对胜率，但其有效性依赖于预定义的风格模板，且未提供严格的理论收敛保证。

】

---

【Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations ｜自适应测试时计算分配与动态上下文演示

研究机构：美国加州大学河滨分校、美国印第安纳大学

作者：Bowen Zuo、Dongruo Zhou、Yinglun Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2604.21018)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21018)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段算力提升大语言模型（LLM）性能，但现有方法多采用静态采样分布或均匀算力分配，导致在异构难度数据集上效率低下。本文指出，仅决定“在哪分配算力”而忽略“如何改变生成分布”是性能瓶颈的关键。作者提出一种两阶段框架，通过自适应性上下文学习（In-Context Learning, ICL）动态重塑条件生成分布，实现算力分配与分布适应的统一。该方法在多个基准上以更低算力成本超越基线，但其效果高度依赖可验证任务中的真值反馈，在不可验证场景下的泛化能力存疑。

】

---

【Adaptive Text Anonymization: Learning Privacy-Utility Trade-offs via Prompt Optimization ｜自适应文本匿名化：基于进化提示优化的隐私-效用权衡探索

研究机构：法国国家科学研究中心

作者：Gabriel Loiseau、Damien Sileo、Damien Riquet 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20743)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0659f29ad99)

> 导读 文本匿名化旨在平衡敏感信息去除与下游任务效用，但现有方法依赖静态规则或手动提示，难以适应多变的隐私-效用需求。本文提出将匿名化建模为多目标提示优化问题，利用进化算法自动发现适应特定任务的匿名化指令。该方法在开源模型上实现了接近闭源SOTA的性能，并揭示了隐私-效用权衡前沿的多样性。其价值在于实现了策略的自动化适配，但依赖少量标注数据且评估环节仍部分依赖闭源模型，限制了其完全本地化部署的潜力。

】

---

【Adversarial Yet Cooperative: Multi-Perspective Reasoning in Retrieved-Augmented Language Models ｜对抗协同：检索增强中的多视角推理

研究机构：华东师范大学、东南大学

作者：Can Xu、Lingyong Yan、Jiayi Wu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04651)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04651)

> 检索增强生成（RAG）系统在处理冲突或误导性外部文档时，单一智能体的自回归推理往往放大而非抑制错误，且基于最终结果的任务级奖励无法区分逻辑严谨的推导与侥幸猜对。现有自反思范式受限于“单一视角”架构，模型难以识别自身逻辑缺陷，导致验证过程陷入非收敛的镜像循环。本文提出对抗推理RAG（ARR），将推理与验证解耦为两个独立智能体，通过基于策略熵变化的过程感知优势函数实现内生过程监督。该方法在多个问答基准上显著优于单智能体基线，但其验证器本身仍依赖语言模型内部状态，是否构成真正的外部接地存疑。

】

---

【Afrispeech Semantics: Evaluating Audio–Semantic Reasoning in Spoken Language Models Across Domains and Accents ｜音频语义推理的多任务评估框架

研究机构：美国佛罗里达大学

作者：Chibuzor Okocha、Christan Grant

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d5ebd8c4b1ae)

> 音频语言模型（ALM）在生成流畅文本的同时，常依赖语言先验而非声学证据进行推断，导致“过度蕴含”与口音敏感等系统性错误。现有基准如MMAU侧重表面正确性，无法区分合理幻觉与逻辑谬误，且缺乏对发音变体下语义稳定性的测试。本文构建了一个包含蕴含、一致性、可信度及口音漂移/克制五个子任务的统一评估框架，基于非洲口音语料库对13个ALM进行零样本审计。该工作揭示了当前模型在细粒度语义推理上的严重缺陷，但级联ASR+LLM系统优于端到端ALM的发现，挑战了“端到端架构必然更优”的领域共识。

】

---

【Agent-GWO: Collaborative Agents for Dynamic Prompt Optimization in Large Language Models ｜狼群优化驱动的推理配置自动搜索

研究机构：电子科技大学、同济大学

作者：Xudong Wang、Chaoning Zhang、Chenghao Li 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18612)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18612)

> 大语言模型在复杂推理任务中常因提示词微小变动或解码参数设置不当导致性能剧烈波动，现有测试时增强方法多聚焦于轨迹生成与搜索，却忽视了提示模板与解码超参这一底层配置空间的联合优化。Agent-GWO 将提示与超参封装为可继承的“智能体”状态，利用灰狼优化算法的领导者-跟随者机制在推理阶段自动搜索鲁棒配置。该方法无需训练即可在数学与混合推理基准上稳定提升准确率，但其增益是否源于模型固有能力的释放而非优化算法本身的贡献，仍需更严格的消融验证。

】

---

【Agentic Conversational Search with Contextualized Reasoning via Reinforcement Learning ｜对话式智能体搜索中的上下文推理强化学习

研究机构：美国马萨诸塞大学阿默斯特分校、美国圣母大学

作者：Fengran Mo、Yifan Gao、Sha Li 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13115)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5536d5c36014)

> 多轮对话中用户意图随历史交互演化，传统静态“重写-检索-生成”管道因模块独立优化而难以捕捉动态依赖，且现有深度搜索智能体仅针对单轮自包含查询设计，缺乏对历史上下文的去语境化处理与混合主动性交互能力。本文切入点在于将强化学习奖励分解为结果、信息增益与混合主动性三部分，在单一智能体框架内联合优化查询生成、证据利用与交互决策。该方法通过中间过程奖励缓解多轮场景下的稀疏监督信号问题，在四个对话基准上超越了单轮智能体基线，但其性能增益是否完全源于奖励分解而非骨干模型规模，仍需更严格的控制实验验证。

】

---

【Agentic-R: Learning to Retrieve for Agentic Search ｜面向智能体搜索的检索器训练框架

作者：Wenhan Liu、Xinyu Ma、Yutao Zhu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c50d6cebe2a4)

> 智能体搜索（Agentic Search）中，检索器长期作为静态黑盒存在，其基于语义相似度的匹配目标与智能体多轮推理中对“证据效用”的动态需求存在根本错位。现有单轮检索增强生成（RAG）的效用优化方法无法处理中间查询缺乏金标准答案、且局部相关不等于全局正确的问题。本文切入点在于将检索器训练重构为与智能体双向迭代的闭环过程，通过联合建模局部相关性与全局答案正确性来定义段落效用。该框架在七个问答基准上验证了检索器对智能体性能的显著提升，但其迭代收敛性与跨智能体泛化能力仍受限于特定的训练数据分布。

】

---

【AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG ｜AgenticRAGTracer：面向智能体检索增强的多跳推理诊断基准

研究机构：北京科技大学、北京大学

作者：Qijie You、Wenkai Yu、Hao Liang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01ea47c59e57)

> 多跳推理评估旨在检验大语言模型整合跨文档证据以推导复杂答案的能力，其核心价值在于突破单跳事实检索的饱和瓶颈。现有基准多基于静态“检索-阅读”范式，仅提供最终问答对与支持文档，无法捕捉智能体（Agent）在动态多步交互中的决策过程，导致“答案正确但推理错误”的捷径学习问题难以被诊断。本文提出 AgenticRAGTracer，一个通过自动流水线构建、支持逐跳（Hop-aware）验证的智能体检索增强生成（Retrieval-Augmented Generation, RAG）基准，旨在暴露模型在长链推理中的步骤分配缺陷。该基准填补了动态智能体评估的空白，但其对检索策略与推理链因果关系的量化仍停留在相关性层面，缺乏机制层面的解释。

】

---

【AgentV-RL: Scaling Reward Modeling with Agentic Verifier ｜代理式验证器

研究机构：复旦大学、华中科技大学

作者：Jiazheng Zhang、Ziche Fu、Zhiheng Xi 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16004)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16004)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理计算量提升大语言模型（LLM）的解题准确率，但其效能高度依赖验证器从候选解中筛选正确路径的能力。现有生成式奖励模型（GenRM）因单轮推理导致错误传播，且缺乏外部工具接地，在计算密集型任务中易产生幻觉。本文提出 Agentic Verifier，通过双向代理协同与工具调用实现多轮验证，并设计 AgentV-RL 训练配方将其能力蒸馏至单模型。该方法在数学基准上显著超越传统奖励模型，但高延迟与特定难度下的性能瓶颈限制了其通用性。

】

---

【AHA: Aligning Large Audio-Language Models for Reasoning Hallucinations via Counterfactual Hard Negatives ｜基于反事实硬负样本的音频语言模型时序幻觉对齐

研究机构：美国亚利桑那州立大学、美国克莱姆森大学

作者：Yanxi Chen、Wenhui Zhu、Xiwen Chen 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.24052)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24052)

> 导读 大型音频语言模型（LALM）在复杂声学场景中常因依赖语言先验而非声学证据，产生时序逻辑错误。现有监督微调（SFT）缺乏负约束，无法区分“语言流畅”与“声学真实”，导致模型编造细节以维持连贯性。本文提出 AHA 框架，通过挖掘反事实硬负样本构建偏好数据集，利用直接偏好优化（DPO）强制模型对齐声学事实。该策略在诊断基准上显著降低幻觉率，并在公开基准上实现零对齐税下的性能提升，但其对非时序类幻觉的泛化能力尚存疑。

】

---

【AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation ｜环境感知智能体评估基准

研究机构：中国科学技术大学、新加坡国立大学

作者：Wentao Shi、Yu Wang、Yuyang Zhao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18240)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18240)

> 随着强化学习（RL）在长程智能体训练中的规模化应用，如何在新环境中可靠验证智能体行为成为核心瓶颈。现有规则验证器无法泛化至复杂场景，而 LLM-as-a-Judge 仅依赖表面文本信号，缺乏对环境状态的直接访问。本文提出 AJ-Bench，首个系统评估 Agent-as-a-Judge 能力的多域基准，通过赋予评估者工具与环境交互权限，实现从静态文本判断到动态证据获取的范式转变。该基准填补了评估者能力量化空白，但其绝对性能（平均 F1 0.72）仍远未饱和，揭示了当前评估智能体在复杂多步行为验证中的显著局限。

】

---

【AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms? ｜算法中心范式下的推理能力评估

研究机构：香港科技大学、北京理工大学

作者：Henan Sun、Kaichi Yu、Yuyao Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04996)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04996)

> 现有代码推理基准因题目混杂多算法且源自公开题库，导致无法区分模型是掌握了特定算法原理还是仅记忆了表面解题模式。AlgBench 通过专家原创构建 3000 道单算法隔离题目，从“问题中心”转向“算法中心”范式，以诊断大推理模型在复杂优化算法上的真实能力断层。该基准揭示了模型在全局优化任务上的显著性能衰减及“策略过度转移”现象，为算法推理评估提供了抗污染的新视角，但其单算法隔离设计是否过度简化了真实工程场景中的多算法协同需求，仍存疑。

】

---

【ALGOGEN: Tool-Generated Verifiable Traces for Reliable Algorithm Visualization ｜算法可视化生成中的工具化解耦范式

研究机构：厦门大学

作者：Kunpeng Liao、Yuexiao Ma、Yisheng Lin 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.12159)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.12159)

> 算法可视化（AV）旨在通过动画演示执行状态，帮助学习者建立抽象伪代码与具体心智模型间的桥梁，但高质量AV的制作成本极高，难以规模化覆盖在线判题系统。现有基于大语言模型（LLM）的端到端生成方法因需同时满足算法逻辑与渲染约束，导致幻觉频发、布局不稳定且不可验证。ALGOGEN提出“LLM工具制造者”范式，将生成过程解耦为Tracker生成、轨迹验证与确定性渲染，通过中间表示（IR）确保正确性。该范式在200任务基准上显著提升了成功率，但其对高信息密度场景的布局适应性仍存疑。

】

---

【Aligning What LLMs Do and Say: Towards Self-Consistent Explanations ｜归因自一致性优化

研究机构：以色列理工学院、英伟达研究院

作者：Sahar Admoni、Ofra Amir、Assaf Hallak 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2506.07523)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2d4420d24e74)

> 大语言模型生成的解释常与其实际决策所依赖的输入特征脱节，导致用户信任被误导。现有忠实度评估方法计算成本高昂，且缺乏将评估指标转化为训练信号以直接改善对齐的机制。本文通过构建大规模归因-解释配对基准，并利用直接偏好优化微调模型，使解释的归因向量与决策的归因向量在秩相关上显著对齐。该方法在保持任务准确率的前提下提升了自一致性，但其改进是否真正反映因果机制的忠实性，还是仅优化了归因分布的统计匹配，仍存疑。

】

---

【Alignment Data Map for Efficient Preference Data Selection and Diagnosis ｜对齐数据地图

作者：Seohyeong Lee、Eunwon Kim、Hwaran Lee 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2505.23114)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_72ae40c93f58)

> 偏好数据选择长期依赖奖励边际（Reward Margin）作为唯一筛选信号，但边际相同的样本在绝对质量上差异巨大，导致低质数据混入训练集。本文指出边际信号的盲区，提出 Alignment Data Map，通过联合评估响应质量均值与方差，将数据划分为高质低变、低质低变及高变三个区域。实验表明，仅使用 33% 的高质低变数据即可超越全量数据训练效果。该工具在提升数据效率方面有效，但其依赖外部评分模型引入的偏差及标签诊断的泛化性仍存疑。

】

---

【All Prompts Are Created Equal? Evaluating Robustness of LLM Judges Against Non-Adversarial Prompt Variations ｜非对抗性提示变体下的LLM裁判鲁棒性评估

作者：Savita Bhat、Vasudeva Varma

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c2d4823dc908)

> 导读 大语言模型评估者（LLM-as-a-Judge）旨在利用大语言模型替代昂贵的人类评估，为开放式生成任务提供可扩展的自动化反馈。尽管现有研究已证实强模型与人类判断具有较高一致性，但评估指令的微小语义等价改写往往导致评分剧烈波动，这一“指令敏感性”问题在真实多团队协作场景中普遍存在却未被系统量化。本文通过构建包含约115,000次评估的基准，首次将属性可验证性作为核心变量，揭示了准确率与鲁棒性的脱节现象，并提出了基于该属性的诊断框架。该工作填补了非对抗性鲁棒性评估的空白，但其结论是否适用于对抗性攻击或专用微调模型，仍需进一步验证。

】

---

【AlphaEdit+: Model Editing in the Presence of Conflicting and Inconsistent Knowledge ｜AlphaEdit+：冲突与不一致知识下的模型编辑

研究机构：美国普林斯顿高等研究院、中国科学院大学

作者：Qing Liu、Jianhao Zhang、Ou Wu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10b8d08ae5b0)

> 知识编辑旨在以低成本局部更新大语言模型中的过时事实，但现有方法在编辑目标与模型既有参数知识存在逻辑矛盾或数值偏差时，往往导致编辑失败或局部性崩塌。AlphaEdit通过零空间投影保证保留知识不变，却未考虑新编辑与保留知识、历史编辑之间的几何冲突及目标值与当前参数状态的不一致。本文通过数学分析揭示该失效机制，并提出AlphaEdit+，引入扰动松弛、冲突加权与渐进平滑三个组件以修复上述缺陷。该方法在自建高冲突数据集上显著优于基线，但在标准基准上未超越领域SOTA，且平滑机制引入了约2.29倍的计算开销。

】

---

【AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading ｜AlphaQuanter：端到端工具增强智能体强化学习框架用于股票交易

作者：Zheye Deng、Weixiang Yan、Changlong Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d56c89d7f4c1)

> 自动化交易的核心矛盾在于如何整合多源异构信号并实现风险校准的决策，而现有大语言模型（LLM）智能体因缺乏主动工具编排与证据可追溯性，难以在部分可观测市场中建立可信决策轨迹。AlphaQuanter 将 ReAct 范式改造为“规划-获取-推理-行动”循环，并采用可验证奖励的强化学习（Reinforcement Learning, RL）端到端优化单智能体策略。该框架在回测中实现了显著的年化收益率提升，但其有效性局限于特定历史区间，且未解决实时市场中的延迟与过拟合风险。

】

---

【AMA: Adaptive Memory via Multi-Agent Collaboration ｜多智能体协作的自适应记忆框架

研究机构：香港科技大学、山东大学

作者：Weiquan Huang、Zixuan Wang、Hehai Lin 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20352)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20352)

> 长时程智能体交互面临的核心矛盾是存储粒度与检索需求之间的静态错配，以及缺乏显式一致性维护导致的逻辑矛盾累积。现有Agentic Memory系统虽引入LLM抽象，但普遍依赖固定分块或单一控制器，无法在推理时动态对齐任务复杂度，且更新机制粗糙导致冗余信息 unchecked 累积。本文提出AMA框架，通过解耦Constructor、Retriever、Judge、Refresher四个角色，实现多粒度存储、意图路由与逻辑审计的闭环。该设计在Token效率与知识更新准确率上表现优异，但其绝对性能仍低于最新结构化图谱基线，且多智能体协作带来的额外推理开销是否抵消了粒度适配收益，尚需更严格的效率-精度权衡验证。

】

---

【AMO-Bench: Large Language Models Still Struggle in High School Math Competitions ｜AMO-Bench：基于原创高难竞赛题的大语言模型数学推理基准

研究机构：美团、中国科学院大学

作者：Shengnan An、Xunliang Cai、Xuezhi Cao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26768)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26768)

> 大语言模型在数学任务上的评估长期受制于静态基准的饱和与数据污染，导致高分掩盖了推理能力的真实瓶颈。现有动态生成基准虽能规避记忆化，但多依赖算法变换，难以触及奥林匹克级别的深层逻辑复杂度。AMO-Bench 通过人工原创 50 道 IMO 级难度题目并辅以自动评分机制，填补了高难度竞赛级评估的空白。该基准揭示了当前 SOTA 模型在极端推理任务上的显著局限，但其仅评估最终答案的设计可能掩盖了过程层面的逻辑缺陷。

】

---

【Analysing the Safety Pitfalls of Steering Vectors ｜激活转向的安全副作用：拒绝子空间几何干扰机制分析

研究机构：德国慕尼黑工业大学

作者：Yuxiao Li、Alina Fastowski、Efstratios Zaradoukas 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1b8b69015f8b)

> 导读 激活转向旨在通过推理时修改隐藏状态以低成本控制大语言模型行为，但现有方法多聚焦于行为增强，忽视了其对安全对齐的潜在侵蚀。本文切入点在于揭示转向向量与模型内部拒绝机制的几何重叠如何因果性地导致越狱成功率上升。作者通过构建拒绝方向代理并执行方向消融，建立了余弦相似度与安全退化幅度间的定量预测模型。该工作为安全审计提供了机制解释，但其依赖单一维度拒绝方向代理的假设是否足以覆盖复杂安全行为，仍存疑。

】

---

【Anatomy of Unlearning: The Dual Impact of Fact Salience and Model Fine-Tuning ｜事实流行度与训练范式对机器遗忘的交互影响

作者：Anna Borisiuk、Andrey Savchenko、Alexander Panchenko 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcb5c20c0493)

> 大语言模型（LLM）在部署后需移除敏感或过时知识，但现有研究隐含假设所有事实同等可遗忘，且极少系统对比预训练与监督微调（SFT）模型对同一遗忘信号的响应差异。本文切入点在于揭示事实流行度与模型训练类型如何共同决定遗忘性能。通过构建基于 Wikidata 的真实世界基准 DUET，并控制变量对比两种训练范式，发现流行事实更难擦除且预训练模型存在反向学习现象。该工作填补了评估维度的空白，但其结论受限于单一模型架构与特定领域数据，普适性尚待验证。

】

---

【AnchorAlign: A Novel Anchor Alignment-enhanced Generative Method for Joint Named Entity Recognition and Relation Extraction ｜锚点对齐生成式联合抽取

研究机构：哈尔滨工业大学

作者：Xiaolong Weng、Yuanyun Zhou、Boyu Qiu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0f6f1d74e668)

> 联合命名实体识别与关系抽取（Joint NER/RE）旨在从非结构化文本中同步提取实体及其关系，但现有生成式方法常因实体与关系在生成序列中位置错位或语义脱节，导致抽取结果内部不一致。本文指出，既有对齐机制仅关注跨任务依赖而忽略任务内依赖，且存在“一对多”匹配偏差。为此，AnchorAlign 提出锚点实体选择机制与双层级对齐模块，在概率空间强制实体-关系及关系-关系的语义一致性。该方法在五个基准上刷新了关系抽取的严格 F1 与边界 F1 纪录，但其对判别式模型在复杂依赖场景下的优势仍存疑，且未验证锚点机制在低资源或长尾实体上的鲁棒性。

】

---

【AnchorMem: Anchored Facts with Associative Contexts for Building Memory in Large Language Models ｜锚定事实与关联上下文的大语言模型记忆框架

研究机构：深圳大学、清华大学

作者：Zhanyu Shen、Sijie Cheng、Zhicheng Guo 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17377)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e7fcebe2f84c)

> 长期交互中，大语言模型（LLM）因状态无记忆特性导致上下文丢失，而现有外部记忆系统通过频繁重写或图索引整合历史，往往牺牲语境完整性或引入噪声链接。本文切入点在于解耦检索单元与生成上下文，将原子事实作为检索锚点，保留原始交互作为不可变生成内容。AnchorMem 通过构建事实-上下文单元与关联事件图，在 LoCoMo 基准上显著优于 LightMem 等基线，验证了该架构在保持细粒度检索与叙事完整性上的有效性，但其对通用实体噪声的规避机制在极端稀疏场景下的鲁棒性仍存疑。

】

---

【APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation ｜自适应优先级多目标对齐

研究机构：华东师范大学

作者：Dongliang Chen、Xinlin Zhuang、Junjie Xu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06574)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06574)

> 视觉生成模型在同时优化文本渲染、美学与画质等异构目标时，常因固定权重导致高方差目标垄断梯度更新，使低方差目标停滞。现有静态标量化方法无法通过调整权重解决这一失衡，本文通过双阶段归一化稳定信号尺度，并基于梯度几何动态调度目标优先级。该框架在 Stable Diffusion 3.5 上实现了优于静态基线的帕累托前沿扩展，但其验证局限于单一中等规模模型，跨架构泛化能力尚待确认。

】

---

【Arab Voices: Mapping Standard and Dialectal Arabic Speech Technology ｜Arab Voices：阿拉伯语方言语音数据的标准化与基准构建

研究机构：加拿大不列颠哥伦比亚大学

作者：Peter Sullivan、AbdelRahim A. Elmadany、Alcides Alcoba Inciarte 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c85e87f672ba)

> 阿拉伯语方言（Dialectal Arabic, DA）语音处理长期受困于数据碎片化，现有数据集在元数据标注、方言标签定义及录音条件文档化上缺乏统一标准，导致跨数据集比较与模型评估难以复现。本文切入点在于构建一个标准化的数据生态系统，通过自动化量化“方言度”与音频质量，解决异构语料库无法直接对齐的问题。其核心做法是聚合31个数据集，建立统一元数据框架并引入自动化特征化指标，进而对主流自动语音识别（ASR）模型进行零样本基准测试。该工作填补了DA语音数据基础设施的空白，但其评估仅覆盖零样本场景，未涉及微调后的性能上限，且自动化指标与人类感知的对齐度仍存疑。

】

---

【ARC: Active and Reflection-driven Context Management for Long-Horizon Information Seeking Agents ｜主动反思驱动上下文管理

研究机构：北京大学、北京航空航天大学

作者：Yilun Yao、Shan Huang、Elsie Dai 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12030)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12030)

> 长时域信息检索智能体在交互历史增长后普遍出现性能退化，即上下文腐烂，现有方案仅通过原始累积或被动压缩控制长度，无法修复早期错误与失焦。本文提出 ARC 框架，将上下文视为动态内部状态，通过解耦的上下文管理器执行增量摘要与反思驱动的重组织。该设计在 BrowseComp-ZH 上较被动压缩基线提升 11% 绝对准确率，但反思触发机制的泛化边界与训练数据依赖仍未完全揭示。

】

---

【ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models ｜自适应分辨率感知扩展评估指标

研究机构：复旦大学、南京大学

作者：Zhangyue Yin、Qiushi Sun、Zhiyuan Zeng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06014)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06014)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理算力提升大语言模型性能，但现有评估手段无法量化“算力投入与准确率提升”的真实效率，且对性能随算力增加而下降的负向扩展现象视而不见。Muennighoff et al. (2025) 提出的斜率指标在负向扩展时存在病理行为，且仅关注全局准确率，忽略了样本级的错误转化。本文提出 ARISE 指标，通过样本级轨迹追踪与基于方差的动态采样机制，实现对 TTS 效率的细粒度、稳定量化。该指标在区分模型扩展能力上优于传统斜率指标，但其分数与实际任务准确率的直接映射关系尚未建立。

】

---

【At Your Own PACE: A Causal Framework for Evaluating EQ in LLMs ｜因果校准的大语言模型情商评估框架

作者：Lei Lyu、Shengling Wang、Ke Chao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_12d3760083f9)

> 大语言模型（LLM）在情感交互中常陷入“诊断有余、恢复不足”的困境，且现有评估指标因维度割裂无法反映整体能力。传统量表侧重自我调节，直接迁移至LLM会导致目标错位，而分散测试忽略了维度间的协同效应。本文提出PACE分类法与因果推断框架，通过反事实干预解耦维度混杂，构建闭环评估体系。该框架在人类偏好对齐上达到89.31%，但评估结果高度依赖多智能体仲裁机制，其因果权重的跨模型泛化性存疑。

】

---

【ATAAT: Adaptive Threat-Aware Adversarial Tuning Framework against Backdoor Attacks on Vision-Language-Action Models ｜视觉-语言-动作模型后门攻击中的梯度干扰与优化去冲突

研究机构：中国科学院、中国科学院大学

作者：Kewei Chen、Yayu Long、Shuai Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08612)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_17792f2053db)

> 具身智能模型在供应链环节面临训练时后门植入风险，传统攻击范式因良性指令与恶意动作的优化目标冲突而失效。ATAAT 框架通过构建正交优化子空间解决这一“梯度干扰”问题，分别在数据投毒与模型微调场景下实现隐式与显式去冲突。该工作填补了受限访问条件下 VLA 模型后门攻击的空白，但其对休眠神经元假设的依赖及物理世界泛化性仍存疑。

】

---

【Attention to Non-Adopters ｜关注非采用者：LLM 开发中的群体盲区与需求重构

研究机构：美国斯坦福大学、美国约翰斯·霍普金斯大学

作者：Kaitlyn Zhou、Kristina Gligorić、Myra Cheng 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15951)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15951)

> 大语言模型（LLM）的个性化研究长期聚焦于如何适配现有用户的风格与偏好，却系统性忽视了占美国人口 66% 的“非采用者”群体。现有基于交互日志和偏好数据的开发范式，将技术能力锁定在数字素养较高的采用者需求上，导致基础数字服务导航、护理协调等高频痛点被边缘化。本文通过定性访谈与定量调查，论证了将非采用者需求纳入设计、评估与部署闭环的必要性，并提出了“能力增强”评估范式。该立场论文揭示了 LLM 普及中的结构性不平等，但其定性结论向量化训练目标的转化路径尚不明确。

】

---

【AUDITA: A New Dataset to Audit Humans vs. AI Skill at Audio QA ｜音频问答基准 AUDITA：基于 IRT 的人类-模型能力差距诊断

研究机构：美国哥伦比亚大学

作者：Tasnim Kabir、Dmytro Kurdydyk、Aadi Palnitkar 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_52412c480158)

> 音频问答（Audio QA）旨在评估模型从声学信号中提取语义与实体信息的能力，但现有基准多依赖封闭集分类或模板化问题，导致模型可通过文本先验或浅层声学线索“作弊”，无法真实反映听觉推理水平。本文切入点在于构建一个要求多线索整合与真实世界实体锚定的高难度基准，并引入人类基线作为参照系。具体做法是收集 9690 个人工撰写的音频问答对，利用项目反应理论（Item Response Theory, IRT）量化题目区分度与参与者能力，揭示人类与模型在听觉推理上的巨大鸿沟。该工作提供了诊断模型听觉盲区的有力工具，但其结论是否受限于特定文化实体类型，仍需进一步验证。

】

---

【Automated Profile Inference with Language Model Agents ｜自动化画像推断

作者：Yuntao Du、Zitao Li、Bolin Ding 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_74a5b1641137)

> 在线伪匿名平台用户通过公开活动暴露的敏感信息，长期依赖人工分析才能被提取，效率低且门槛高。现有基于大语言模型（LLM）的属性推断方法多将任务简化为预定义类别的分类，无法处理噪声大、信息隐含且无固定标签的真实场景。本文提出 AutoProfiler，一个由四个专用 LLM 智能体协作的自动化画像框架，通过迭代检索、推断与精炼流程，从公开活动中自主构建包含个人身份信息（PII）和敏感个人信息（SPI）的用户画像。该方法在真实数据上实现了高准确率与低成本，验证了自动化去匿名化的可行性，但其对模型对齐防御的无效性及合成基准上的性能局限仍存疑。

】

---

【Automatic Paper Analysis and Categorisation for Systematic Reviews with Combined Reasoning-Augmented SFT and DAPO RL ｜低资源科学论文结构化标注：推理增强SFT与DAPO强化学习

作者：Michela Lorandi、Anya Belz、Simon Mille 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b652a2a95557)

> 系统性综述（Systematic Review）的核心瓶颈在于人工标注论文分类标签的高昂成本与时效性滞后。现有大语言模型（LLM）直接生成结构化标签时，常因缺乏逻辑推理过程导致多标签预测错误及格式合规性差，且单纯监督微调（SFT）难以捕捉字段间的依赖关系。本文切入点在于将标注任务重构为推理增强分类问题，通过合成推理轨迹进行SFT，并引入动态采样策略优化（Dynamic sAmpling Policy Optimisation, DAPO）强化学习以优化奖励信号。该方法在100样本低资源约束下显著提升了标注准确率，但受限于仅评估开源模型且未对比检索增强生成（RAG）基线，其结论在闭源模型及长文本场景下的泛化性存疑。

】

---

【AutoMonitor-Bench: Evaluating the Reliability of LLM-Based Misbehavior Monitor ｜LLM 行为监控器可靠性评估

作者：Shu Yang、Jingyu Hu、Tong Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05752)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_48a05fce2af4)

> 前沿大模型在推理与执行任务时可能产生隐蔽的违规行为，如谄媚、捷径利用或规格博弈，但现有评估缺乏统一标准来量化“监控器”本身的可靠性。传统基于有害请求合规性的检测无法覆盖这些隐式行为，导致监控器在真实部署中失效。本文构建了包含 3,010 个配对样本的 AutoMonitor-Bench，通过漏报率（MR）与误报率（FAR）双指标系统评估 22 个 LLM 监控器，并验证微调对泛化能力的局限。该基准揭示了监控器在安全覆盖与操作效用间的固有张力，但静态基准的局限及微调泛化失败的深层原因仍待厘清。

】

---

【AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning ｜自适应搜索深度强化学习框架

研究机构：中国科学院、中国科学院大学

作者：Jingbo Sun、Wenyue Chong、Songjun Tu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17337)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17337)

> 智能体检索增强生成（Agentic RAG）系统在处理复杂查询时，往往陷入冗余搜索，导致计算成本与延迟激增。现有方法通过固定步数或外部模型判断来限制搜索深度，但前者导致复杂问题探索不足，后者引入额外延迟且无法适应模型自身能力。本文提出AutoSearch，一种基于自生成中间答案的强化学习框架，通过动态识别“最小充分搜索深度”来平衡准确率与效率。该框架在低参数量骨干上实现了帕累托改进，但其自评估机制在极长程任务或高噪声环境下的鲁棒性尚存疑。

】

---

【AutoSUIT Bench - Automated Security UnIt Test Benchmark for LLM Coding ｜自动化安全单元测试基准

研究机构：美国马萨诸塞大学阿默斯特分校

作者：Samuel Osebe、Fan Yang、Junyi Li 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d44dd828310a)

> 大语言模型生成的代码普遍存在安全漏洞，但现有评估手段要么依赖静态分析导致高误报，要么依赖人工编写动态测试导致覆盖不足。AutoSUIT 通过 LLM 自动化生成代码、测试及修复代码，并嵌入迭代验证闭环，解决了动态基准扩展性瓶颈。该范式实现了 232 类 CWE 的细粒度评估，但缺乏与主流安全对齐方法的直接性能对比，其作为评估工具的区分度尚待验证。

】

---

【BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents ｜智能体工作流后门传播分析框架

研究机构：复旦大学、新加坡管理大学

作者：Yunhao Feng、Yige Li、Yutao Wu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04566)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04566)

> 大语言模型智能体通过规划、记忆与工具调用执行多步任务，其状态持久化特性使得单点注入的触发器可跨阶段传播，但现有研究多在孤立模块下评估，无法刻画这种工作流级的动态风险。本文提出 BackdoorAgent，一个阶段感知的统一框架，通过组件局部扰动与轨迹日志，系统量化了触发器在规划、记忆、工具三个阶段的激活与传播机制。该工作填补了智能体后门从静态注入到动态演化的分析空白，但其仅聚焦攻击表征，未提供防御算法，且评估依赖特定任务验证器，泛化性存疑。

】

---

【Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning ｜校准感知强化学习：决策LLM中精度与置信度的再平衡

研究机构：美国南加州大学、亚马逊网络服务人工智能

作者：Duygu Nur Yaldiz、Evangelia Spiliopoulou、Zheng Qi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13284)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13284)

> 在内容审核、医疗辅助等高风险决策场景中，大语言模型（LLM）不仅需要输出正确标签，其预测概率还需真实反映正确率，以便下游系统判断何时信任模型、何时触发人工复核。现有微调范式存在结构性矛盾：监督微调（SFT）能改善概率校准但精度增益有限，而可验证奖励强化学习（RLVR）虽提升精度却导致模型极度过度自信，使置信度信号失效。本文通过诊断RLVR校准失效的微观机制，提出直接调节决策token概率的校准感知强化学习算法，在保持RLVR精度优势的同时将期望校准误差（ECE）降低至接近SFT水平。该方法在原子选项分类任务中有效，但其对开放式生成或复杂推理链的适用性存疑。

】

---

【Balancing Knowledge Breadth and Task Depth for Effective Domain Adaptation Fine-Tuning ｜二维课程学习框架

研究机构：中山大学

作者：Mu Zhang、Yuxiang Chu、Guangya Yu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0a64a8a62ee3)

> 大语言模型在垂直领域微调时，常因灾难性遗忘导致通用能力退化，而现有单维课程学习难以同时兼顾知识广度与任务深度。本文提出一种二维课程学习框架，通过语义聚类与Bloom分类法构建正交的知识-任务排序结构，并配合指数混合调度实现平滑过渡。该方法在医疗与金融基准上取得SOTA，但缺乏与参数解耦方法的同骨干对比，其遗忘缓解效果是否优于架构级方案仍存疑。

】

---

【Bayesian Active Learning with Gaussian Processes Guided by LLM Relevance Scoring for Dense Passage Retrieval ｜贝叶斯主动学习引导的LLM密集段落检索

研究机构：韩国成均馆大学、加拿大多伦多大学

作者：Junyoung Kim、Anton Korikov、Jiazhou Liang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17906)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17906)

> 密集段落检索（Dense Passage Retrieval, DPR）面临LLM重排成本高且无法覆盖语义分散簇的困境。现有LLM重排范式被动依赖第一阶段候选集，导致召回率受限且信号无法传播。本文提出BAGEL框架，利用高斯过程（Gaussian Process, GP）在嵌入空间中主动探索以平衡探索与利用。该方法在固定预算下显著提升了检索性能，但其对GP平滑性假设与LLM离散打分兼容性的验证尚显不足。

】

---

【BCL: Bayesian In-Context Learning Framework for Information Extraction ｜贝叶斯上下文学习框架用于信息抽取

研究机构：英国伦敦大学学院、英国爱丁堡大学

作者：Haoliang Liu、Chengkun Cai、Xu Zhao 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.18620)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.18620)

> 信息抽取（Information Extraction, IE）任务依赖大语言模型（LLM）的上下文学习（In-Context Learning, ICL）能力，但现有方法在模型规模间表现不一致或缺乏系统性优化。本文指出，粗粒度标签与模型先验间的语义鸿沟是性能瓶颈，提出通过粒子滤波与贝叶斯更新优化标签的子类别表示。该方法将规则优化形式化为状态估计问题，在多个IE基准上取得一致提升。其价值在于提供了通用优化框架，但规则优化是否真正改变了模型内部注意力机制尚存疑。

】

---

【Be Your Own Red Teamer: Safety Alignment via Self-Play and Reflective Experience Replay ｜安全自博弈与反思性经验回放

作者：Hao Wang、Yanting Wang、Hao Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_67e54d0cdb18)

> 大语言模型（LLM）的安全对齐长期受困于静态防御对新型越狱攻击的泛化失效，现有外部红队测试因攻击者滞后于防御者而陷入“猫鼠游戏”僵局。本文切入点在于将攻击与防御角色内化于单一模型，通过自博弈实现攻防策略的同步进化。具体做法是构建零和强化学习闭环，并引入基于UCB采样的反思性经验回放机制以重访历史失败案例。该方法在保持低过拒绝率的同时显著提升了鲁棒性，但其自博弈机制是否会导致攻击策略多样性坍缩，仍存疑。

】

---

【Before Forgetting, Learn to Remember: Revisiting Foundational Learning Failures in LVLM Unlearning Benchmarks ｜多模态大模型遗忘基准的阶段1失效诊断与ReMem构建

作者：JuneHyoung Kwon、MiHyeon Kim、Eunju Lee 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.03759)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03759)

> 多模态大语言模型（Large Vision-Language Models, LVLMs）的机器遗忘（Machine Unlearning, MU）旨在移除训练数据中的敏感隐私，但现有评估基准存在根本性缺陷：模型在初始微调阶段未能有效记忆目标信息，导致后续遗忘评估无效。本文通过内部状态分析证实了这一“阶段1失效”，并构建了包含多跳推理与多视图图像的ReMem基准，以确立可靠的遗忘评估基础。该工作揭示了当前多模态遗忘研究的评估盲区，但仅提供了基准与诊断，未提出新的遗忘算法，其结论的普适性仍受限于特定模型架构与数据规模。

】

---

【Behavioral Consistency Validation for LLM Agents: An Analysis of Trading-Style Switching through Stock-Market Simulation ｜金融交易风格切换的行为一致性验证

研究机构：复旦大学、武汉大学

作者：Zeping Li、Guancheng Wan、Keyang Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07023)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07023)

> 现有基于大语言模型（LLM）的金融市场模拟多将投资者策略固定于初始化阶段，无法复现真实市场中技术派与基本面派动态切换所引发的波动率聚集等宏观现象。本文切入点在于验证LLM代理在引入策略切换机制后，其微观决策逻辑是否与行为金融学理论预测一致。通过构建包含反事实账本与四维度行为驱动因子的仿真环境，利用Mann-Whitney U检验量化对齐组与非对齐组的行为差异。该框架揭示了当前LLM在损失厌恶与财富差异敏感度上具备部分理论一致性，但在羊群效应与价格错配响应上存在显著模型间分歧，其作为市场微观结构代理的可靠性仍受限于社会心理机制的内化程度。

】

---

【Benchmarking Agentic Newswriting via Journalistic Workflows ｜新闻智能体写作基准

作者：Yen-Che Chien、Kuang-Da Wang、Wei-Yao Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ba8b61ebf6cc)

> 深度研究智能体（DRA）旨在让大语言模型自主处理开放式、长周期的高复杂度信息检索与整合任务，其核心价值在于突破静态检索的局限。现有方法多聚焦通用问答或报告生成，缺乏对时间敏感、需主动发现缺失背景的真实新闻工作流的评估。本文切入点在于将新闻写作形式化为受发布时间约束的迭代式搜索-编辑-重述过程，通过双层评估协议分离证据选择对齐度与最终写作质量。该基准揭示了当前智能体在规划与叙事整合上的显著短板，但其评估依赖单一参考文章，泛化性存疑。

】

---

【Beneficial Reasoning Behaviors in Agentic Search and Effective Training Methods to Obtain Them ｜行为预植：解锁智能体搜索强化学习潜力的训练范式

研究机构：美国卡内基梅隆大学

作者：Jiahe Jin、Abhijay Sai Paladugu、Chenyan Xiong

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f45aa315e75f)

> 智能体搜索（Agentic Search）旨在让大语言模型（LLM）通过多步交互解决复杂信息需求，但直接应用强化学习（RL）常因策略熵坍缩导致训练不稳定。现有SFT-then-RL范式依赖结果正确性或随机蒸馏，忽略了中间推理过程的质量差异，导致模型缺乏探索基础。本文提出行为预植（Behavior Priming），通过筛选包含特定推理行为的轨迹进行SFT，再行RL，以建立探索基础。该方法在Web基准上相对直接RL提升37.2%，验证了推理行为比结果正确性更关键，但其对多智能体架构的适用性尚存疑。

】

---

【Better LLM Reasoning via Dual-Play ｜双博弈对抗训练框架

研究机构：美国康奈尔大学

作者：Zhengxin Zhang、Chengyu Huang、Aochong Oliver Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.11881)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11881)

> 大语言模型在复杂推理任务中的表现受限于高质量监督数据的稀缺，传统基于可验证奖励的强化学习（RLVR）范式难以在数据匮乏领域扩展。现有自博弈方法因缺乏角色分工导致训练快速饱和，无法实现能力的持续自举。本文提出 PasoDoble，通过让两个同基座模型分别扮演出题者与解题者进行对抗训练，利用预训练知识接地生成有效题目，实现无外部标签下的推理能力迭代提升。该框架在小规模模型上验证了可行性，但其对大规模模型泛化性及非数学领域的适用性仍存疑。

】

---

【Beyond Compromise: Pareto-Lenient Consensus for Efficient Multi-Preference LLM Alignment ｜帕累托宽容共识（PLC）：基于合作博弈的多目标LLM对齐

研究机构：浙江大学

作者：Renxuan Tan、Rongpeng Li、Zhifeng Zhao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05965)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05965)

> 多目标偏好对齐旨在同时优化有用性、无害性等异质人类价值观，但现有静态标量化或刚性梯度投影方法常陷入“风险规避均衡”，即模型为规避局部目标冲突而停滞于次优帕累托点。PLC将对齐重构为动态协商过程，通过联盟共识驱动的宽容梯度校正，允许少数目标暂时退化以换取整体帕累托改进。实验显示其在LLM-as-a-Judge评分上达到7.49，优于GAPO的7.03，但仅验证了3个目标维度，且未与正交分解类方法直接对比，其动态机制在高维目标空间下的稳定性存疑。

】

---

【Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents ｜语义时间锚定与持续记忆构建

研究机构：中国科学院、中国科学院大学

作者：Miao Su、Yucan Guo、Zhongni Hou 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07468)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07468)

> 长期对话智能体面临的核心困境是记忆的时间维度建模失效：现有系统普遍将“对话发生时间”等同于“事件发生时间”，且将连续经历切割为孤立点状记录，导致跨会话推理与时间敏感查询的召回严重失准。Temporal Semantic Memory (TSM) 通过构建语义时间线（Semantic Timeline）与持续记忆（Durative Memory）双轨架构，解耦了对话时间与事件时间，并将离散事实聚合为具有时间跨度的状态摘要。该方法在 LongMemEval 上实现了 74.80% 的整体准确率，但在 LoCoMo 基准上落后于结构化语义图方案，表明其优势局限于时间维度而非通用检索能力。

】

---

【Beyond Evidence: Belief-Chain Conditioning for Persuasive Misinformation Debunking Explanation ｜信念链条件化解释生成

作者：Yi-Li Hsu、Li-Wun Chang、Chun-Yu Hsu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d0dd45acf80e)

> 虚假信息纠正面临的核心困境是受众的顽固信念与模型中性解释之间的认知错位。现有对话式方法虽能迭代修正，但多轮交互的高时间成本使其难以在真实场景中部署，且模型常因缺乏对受众心理状态的显式建模而失效。本文切入点在于将理论心智（Theory of Mind, ToM）形式化为结构化的认知链，通过单轮条件化生成对齐受众心理。该方法在信徒群体中显著提升了共情与整体偏好，但其说服力增益是否以牺牲事实覆盖率为代价，仍需更严格的因果验证。

】

---

【Beyond Fixed Psychological Personas: State Beats Trait, but Language Models are State-Blind ｜基于潜在状态-特质理论的心理方差分解与AI系统盲区诊断

研究机构：美国佛蒙特大学

作者：Tamunotonye Harry、Ivoline Ngong、Chima Nweke 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15395)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15395)

> 大语言模型（LLMs）在个性化交互中面临的核心矛盾是：用户行为由稳定特质（Trait）与情境状态（State）共同决定，但现有AI系统仅能处理前者。传统人格数据集（如PersonaChat）假设人格为固定属性，忽略了情境对心理表达的动态塑造，导致模型生成与评估环节出现系统性偏差。本文通过构建首个支持状态-特质分解的Reddit数据集Chameleon，利用潜变量状态-特质（Latent State-Trait, LST）理论量化方差来源，并诊断LLM与奖励模型（Reward Model）在处理心理情境时的失效模式。该工作揭示了74%心理方差源于情境这一关键事实，但仅停留在诊断层面，未提供具体的控制算法，其结论在跨文化泛化性上仍存疑。

】

---

【Beyond High-Entropy Exploration: Correctness-Aware Low-Entropy Segment-Based Advantage Shaping for Reasoning LLMs ｜低熵段优势整形

研究机构：北京邮电大学、中国人民大学

作者：Xinzhu Chen、Xuesheng Li、Zhongxiang Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.00908)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00908)

> 强化学习后训练在提升大语言模型推理能力时，往往陷入高熵探索与低熵结构稳定性的失衡，导致错误模式固化。现有基于熵的优化方法仅关注高熵Token，忽视了占据序列80%的低熵段对推理结构的决定性作用。本文提出LESS框架，通过组内正确性统计重塑低熵段优势函数，在GRPO基础上实现了对稳定推理结构的显式强化。该方法在数学基准上显著提升了准确率与鲁棒性，但其对非可验证领域的泛化能力尚存疑。

】

---

【Beyond Local vs. External: A Game-Theoretic Framework for Trustworthy Knowledge Acquisition ｜博弈论驱动的可信知识获取

作者：Rujing Yao、Yufei Shi、Yang Wu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1e3eb161e9f)

> 大语言模型（LLM）在云端部署时，用户直接提交敏感查询会导致研究意图或组织机密泄露，而仅依赖本地小模型又受限于知识广度与推理能力。现有语义混淆方法多为静态启发式规则，无法适应外部模型动态的推断行为，且缺乏对“意图可重构性”的显式量化。本文提出GTKA框架，将隐私-效用权衡建模为生成器与攻击者的交替对抗博弈，通过优化子查询策略实现零原始查询暴露下的高保真答案合成。该框架在自建生物医学与法律基准上验证了优于静态基线的泄露抑制效果，但其攻击者模块的模拟保真度及多轮交互下的累积泄露风险仍存疑。

】

---

【Beyond Marginal Distributions: A Framework to Evaluate the Representativeness of Demographic-Aligned LLMs ｜超越边际分布：基于相关结构的LLM代表性评估框架

研究机构：德国柏林洪堡大学、德国斯图加特大学

作者：Tristan Williams、Franziska Weeber、Sebastian Padó 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15755)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4a0ad3eb59ee)

> 当前LLM对齐研究普遍依赖边际分布匹配来衡量模型对特定人口群体价值观的还原度，但这一单变量视角忽略了真实社会中不同议题间存在的深层依赖关系。现有方法如Persona Prompting与微调模型虽能改善单题回答的分布相似度，却可能掩盖了模型在多维价值空间中的结构性失效。本文提出一种结合边际分布与多变量相关结构的评估框架，通过对比问题间及主题间的相关矩阵来诊断模型的代表性。该框架揭示了现有主流引导方法在结构对齐上的系统性不足，为评估标准提供了更严格的诊断维度，但其结论是否受限于特定调查数据集的样本量仍需进一步验证。

】

---

【Beyond Memorization: Testing LLM Reasoning on Unseen Theory of Computation Tasks ｜确定性有限自动机构建中的记忆与推理解耦评估

作者：Shlok Shelat、Jay Raval、Souvik Roy 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13392)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13392)

> 大语言模型在形式语言任务上的高分表现长期引发“符号推理”与“模式匹配”的本体论争论，现有基准因缺乏对训练数据记忆的严格隔离，无法区分模型是执行了组合泛化还是检索了相似样例。本文通过构建包含已见（Seen）与未见（Unseen）分割的确定性有限自动机（DFA）构建基准，利用阿登定理逆向生成结构新颖的正则表达式，量化了模型在组合泛化上的性能断层。实验表明，模型在知识问答与已见任务上表现优异，但在未见任务上准确率骤降30-64%，且思维链提示未能缓解该缺陷，揭示了LLM在符号状态跟踪上的根本局限。

】

---

【Beyond Neural Incompatibility: Cross-Scale Knowledge Transfer in Large Language Models through Latent Semantic Alignment ｜基于潜空间语义对齐的跨尺度参数知识迁移

研究机构：澳大利亚莫纳什大学、德国慕尼黑工业大学

作者：Jian Gu、Aldeida Aleti、Chunyang Chen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c08b3ddcd68c)

> 大语言模型（LLM）内部蕴含大量参数化知识，但将其从大模型迁移至小模型时，架构差异导致的“神经不兼容性”使得直接参数复用失效。现有方法多依赖参数提取与注入，忽略了激活空间几何结构的对齐，导致迁移不稳定且计算成本高。本文提出 SemAlign，通过词汇定义的语义基将源模型层输出分解并重组为目标空间的监督信号，实现无参数注入的跨尺度迁移。该方法在 Llama-2 系列模型上验证了有效性，但其对同族模型的依赖及缺乏因果机制验证限制了通用性。

】

---

【Beyond Prompt Engineering: A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality ｜提示词敏感性的统计归因与鲁棒性机制分析

研究机构：香港理工大学、香港中文大学

作者：Qipeng Xie、Zi Liang、Jiafei Wu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8e5171758430)

> 提示词工程长期面临“蝴蝶效应”，即微小的词汇扰动导致模型输出剧烈波动，现有方法多聚焦于黑盒优化或模板级评估，缺乏对底层词汇机制的统计解释。本文切入点在于将提示词敏感性视为一种可量化的统计现象，而非需消除的噪声。通过构建132,000个提示词变体数据集，利用n-gram统计识别出“领域特定术语”与“显式行动指令”作为鲁棒性的语言支柱，并据此设计自动化的模式注入代理。该工作提供了从经验直觉到统计原则的转变，但其结论是否适用于非结构化或低资源语言场景仍存疑。

】

---

【Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning ｜轨迹融合：利用错误信号增强数学推理微调

作者：Jie Deng、Hanshuang Tong、Jun Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_602c04c6deae)

> 数学推理微调长期依赖拒绝采样，仅保留正确轨迹，导致模型无法从失败模式中习得纠错逻辑。现有数据合成方法聚焦于增加正确解的多样性或难度，却系统性丢弃了蕴含丰富诊断信息的错误路径。本文提出TrajFusion，通过自适应融合错误与正确轨迹构建试错式监督信号，在不改变训练目标的前提下提升推理鲁棒性。该方法在低数据量下显著优于基线，但其增益是否源于结构化的错误监督而非单纯的序列长度增加，仍需更严格的控制实验验证。

】

---

【Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning ｜工具查询规划器

研究机构：美国麻省理工学院

作者：Wei Fang、James Glass

论文原文见 [arXiv](https://arxiv.org/abs/2601.07782)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07782)

> 大规模动态工具库中，静态单次检索无法弥合用户抽象意图与工具技术文档间的语义鸿沟，且难以处理多工具组合依赖。现有密集检索器在复杂组合任务上失效，本文切入点是将检索重构为交互式规划过程。TOOLQP 通过轻量模型分解子任务并迭代生成查询，结合 RLVR 优化策略。其价值在于以极低参数量实现了跨检索器的鲁棒泛化，但迭代查询带来的推理延迟在实时场景下的权衡尚存疑。

】

---

【Beyond Static Personas: Situational Personality Steering for Large Language Models ｜情境感知的人格神经元检索与调制

研究机构：中国科学技术大学、新加坡管理大学

作者：Zesheng Wei、Mengxiang Li、Zilei Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1a90fd517faa)

> 大语言模型（LLM）的人格控制长期受困于静态特质假设，导致模型在复杂交互中无法像人类一样根据情境动态调整行为。现有激活引导或稀疏编辑方法虽能实现免训练的人格注入，但缺乏对“情境-行为”一致性的显式建模，导致跨情境泛化能力不足。本文提出IRIS框架，通过构建情境人格神经元库并基于相似度检索进行加权调制，实现了免训练的情境自适应人格控制。该方法在新增基准SPBench上取得SOTA表现，但其依赖预构建的历史情境库，限制了其在完全未知情境下的即时适应能力。

】

---

【Beyond Static Profiles: Capturing the Fluidity of User Preferences in Diverse Scenarios ｜情境依赖性偏好评估基准

作者：Chunyang Gao、Yi Huang、Jingyu Yao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_00b094756eb0)

> 大语言模型个性化长期受困于“千人一面”的静态画像假设，无法捕捉用户偏好随语境动态切换甚至冲突的特性。现有基准多将偏好视为固定属性，导致模型在复杂社交场景中产生意图幻觉或给出通用化建议。本文切入点在于构建一个区分“稳定偏好”与“情境偏好”的细粒度分类体系，并设计配套的多轮对话数据集与评估任务。通过量化模型在动态语境下的对齐能力、歧义消解效率及样本识别效率，S2Pref 为动态个性化提供了新的测试床，但其评估协议中信息不对称的设置可能高估通用推理能力对个性化效果的贡献。

】

---

【Beyond Static Synthetic Noise: Assessing the Robustness of Large Language Models to Natural Context Variation in the Real World ｜基于维基百科修订历史的自然扰动鲁棒性评估

作者：Yulong Wu、Viktor Schlegel、Riza Batista-Navarro

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_09710bfe4f33)

> 现有QA鲁棒性评估依赖人工合成扰动，难以复现真实世界中知识库随时间演化的文本漂移，导致模型在静态测试集上的高分无法反映其在动态环境中的可靠性。本文切入点在于利用维基百科的修订历史作为天然扰动源，构建标签保持的自然扰动测试集，以替代静态合成噪声。通过提取相邻版本差异并验证答案有效性，该框架量化了编码器与大型语言模型（LLM）在自然文本变化下的性能衰减。该工作揭示了LLM对自然漂移的显著脆弱性，但其防御策略的泛化能力仍存疑。

】

---

【Beyond Static Toolsets: Self-Evolving LLM Tool Agents via Continual Documentation Adaptation ｜持续文档适应

研究机构：英国伦敦大学学院

作者：Bin Wu、Edgar Meij、Emine Yilmaz

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2667bbb2c89)

> 导读 工具使用大语言模型（LLM）在部署中面临工具集动态增删导致的性能波动，现有静态文档优化方法无法应对这种环境漂移。本文提出 ContDa，通过关系引导探索与关系感知调整，在不更新模型权重的前提下持续重构工具文档。该方法在 StableToolBench 动态扩展实验中，将平均性能从基线的 8.67% 提升至 11.20%，同时控制了旧任务遗忘。其价值在于验证了文档作为轻量级进化载体的可行性，但缺乏与参数化方法的横向对比，且未量化文档更新对模型内部表征的潜在干扰。

】

---

【Beyond Superficial Tests: Adversarial Refinement for Reliable Property-Based Testing ｜对抗性精炼的属性测试生成框架

研究机构：北京航空航天大学

作者：Xiao Li、Runlin Liu、Zhe Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_60306a166b2a)

> 现有基于大语言模型（LLM）的属性测试（Property-Based Testing, PBT）生成方法存在“表面性鸿沟”，即生成的测试脚本虽语法正确，但往往包含语义空泛的弱属性，无法有效区分正确实现与错误实现。本文切入点在于利用“构造比证伪更难”的语义不对称性，将PBT生成重构为生成器与验证器之间的对抗博弈。PROBE通过构建跨函数语义图定位全局依赖，并让验证器主动构造满足当前属性但语义错误的反实现，以此迭代强化属性强度。该框架在真实Python库中发现了45个未知Bug，但其在非Python生态及并发系统下的泛化能力仍存疑。

】

---

【Beyond Task-Level Context: Class-Conditional Context Vectors for Implicit In-Context Learning ｜类条件上下文向量（C3V）：隐式上下文学习中的细粒度语义解耦

作者：Jianxin Zhang、Yilu Hu、Teng Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_964d9478050d)

> 导读 隐式上下文学习旨在将演示样本压缩为潜在向量以消除推理时的长上下文开销，但现有任务级向量聚合掩盖了分类任务中不同类别的语义差异，导致细粒度判别能力受损。本文切入点在于将单一任务向量解耦为类条件向量组，通过线性干预机制在冻结骨干模型中注入类特异性信号。该方法以极小的可训练参数量实现了类感知适应，在多数基准上超越了任务级基线，但其性能增益依赖于类别数量的规模效应，且在二分类任务上未表现出一致优势。

】

---

【Beyond Templates: Dynamic Adaptation of Reasoning Demonstrations via Feasibility-Aware Exploration ｜动态推理轨迹适配

作者：Yong Wu、Weihang Pan、Ke Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_60b5f981edf0)

> 小语言模型（SLM）在模仿大模型专家推理数据时，常因能力错配导致性能不升反降，这一现象被称为“模仿间隙”。现有静态微调方法假设模型具备潜在推理能力，却忽视了专家轨迹中超出学生模型抽象空间的步骤会引入噪声。本文提出 DART 框架，通过蒙特卡洛模拟评估步骤可行性，在检测到模仿间隙时触发自主探索，生成结果一致的替代路径。该方法在 SLM 上显著优于静态微调，但其有效性依赖于离线模拟的计算成本，且未验证在强化学习范式下的迁移性。

】

---

【Beyond Token Length: Step Pruner for Efficient and Accurate Reasoning in Large Language Models ｜步骤剪枝

作者：Canhui Wu、Qiong Cao、Chang Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03805)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03805)

> 大型推理模型（LRM）在简单任务上常陷入冗长推理，导致计算成本激增与错误累积，即“过度思考”。现有强化学习（RL）方法通过惩罚Token长度来抑制冗余，但Token数少不代表推理步骤少，且模型后期可能通过丢弃推理步骤来“黑客”奖励。本文提出步骤剪枝（SP），将惩罚粒度从Token提升至语义步骤，并引入动态停止机制防止奖励黑客。该方法在MATH-500上以92.0%准确率仅用33%的Token，但AIME24准确率略降，其步骤边界定义的鲁棒性存疑。

】

---

【Beyond Transcription: Unified Audio Schema for Perception-Aware AudioLLMs ｜统一音频模式（UAS）：重构音频大模型监督信号以弥合感知-推理鸿沟

研究机构：北京大学

作者：Linhao Zhang、Yuhan Song、Aiwei Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12506)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_334d18c689d9)

> 音频大语言模型（AudioLLM）在复杂推理任务上表现优异，却在基础声学感知上存在显著短板，这一矛盾源于以自动语音识别（ASR）为核心的训练范式系统性抑制了副语言与非语言信息的表达。现有方法通过扩大模型规模或引入对比学习未能解决该结构性偏差，本文切入点在于重构训练监督信号，将隐式感知需求转化为显式结构化目标。具体做法是提出统一音频模式（Unified Audio Schema, UAS），将音频分解为转录、副语言和非语言事件三个组件，并通过自动化管道生成大规模结构化标注数据。该方案在感知基准上取得显著提升，但其对推理能力的保留机制及跨域泛化边界仍需进一步验证。

】

---

【Beyond Uniform SVD: Dual-Level Optimization across Columns and Modules for LLM Compression ｜双层级优化奇异值分解

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9bbfb78c9638)

> 大语言模型（LLM）低秩分解压缩长期受困于权重矩阵内部误差分布不均与模块间重要性差异，导致统一截断策略在有限秩预算下近似次优。现有方法如 SVD-LLM 和 SoLA 仅依赖激活范数或局部截断误差作为代理指标，缺乏对模型全局性能影响的直接评估。Duo-SVD 通过列级混合分解与模块级全局约束优化，在免训练条件下实现了更精细的压缩预算分配。该方法在 20% 压缩率下显著优于现有 SVD 基线，但其列保留策略对硬件执行效率的影响及高压缩率下的鲁棒性仍存疑。

】

---

【Beyond ’Aha!’: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models ｜超越“顿悟”：基于皮尔斯三元组的元推理能力对齐

作者：Zhiyuan Hu、Yibo Wang、Hanze Dong 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f68280b2a67e)

> 大语言模型在强化学习后训练中常出现不可控的“顿悟时刻”，即模型自发涌现出长思维链与自我修正行为，但这种涌现缺乏稳定性与可预测性，限制了推理能力的规模化部署。现有基于单一任务奖励的强化学习范式难以将这种偶发的认知行为转化为可控、可组合的通用推理技能。本文提出通过显式对齐演绎、归纳与溯因三种元推理能力，利用参数空间合并构建统一推理基座，再经领域特定强化学习提升性能上限。该方法在数学与代码基准上较指令微调基线提升超过10%，但其在非可验证任务上的泛化边界及合并权重的敏感性仍需进一步验证。

】

---

【BiCSRouter: Bi-Level Cross-System Routing for Utility-Aware LLM Inference ｜双层跨系统路由：在单智能体与多智能体范式间动态选择

作者：Mao Keyu、Eiki Murata、Ukyo Honda

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c89307b7d552)

> LLM路由旨在为异构查询匹配最优模型以平衡质量与成本，但现有方法局限于单一计算范式内部，无法同时利用单智能体的深度推理与多智能体的广度协作优势。BiCSRouter将路由问题形式化为跨正交计算范式的层级决策，通过双层结构先优化各范式内部配置，再基于解耦的效用估计选择最优范式。该方法在MBPP上以1.54的成本实现89.40%准确率，较GPT-5基线降低46%成本且仅损失2%精度，但其效用预测器对拓扑结构的依赖是否导致泛化局限尚存疑。

】

---

【BloomEval: A Bloom’s Cognitive Taxonomy-Based Benchmark for Evaluating LRMs via Cognitive Hierarchy Trace ｜基于布卢姆认知分类学的推理轨迹评估

作者：Zhiyi Duan、Lei Gao、Jiangshan Guan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49851fc007ae)

> 多跳推理与数学解题评估长期依赖最终答案的精确匹配，导致模型通过捷径或结构断裂的推理得出正确答案时无法被识别。现有过程评估多聚焦于逻辑一致性或因果验证，缺乏对推理步骤认知层级结构的系统性诊断。本文提出认知层级轨迹（Cognitive Hierarchy Trace, CHT），将布卢姆认知分类学（Bloom's Cognitive Taxonomy, BCT）映射至推理步骤，构建大规模基准BloomEval以量化层级跳跃与断裂。该方法揭示了答案正确性与认知结构完整性之间的解耦，但受限于数学领域单一性及线性层级假设的普适性存疑。

】

---

【BMAM: Brain-inspired Multi-Agent Memory Framework ｜脑启发式多智能体记忆框架

研究机构：日本东京科学大学、香港理工大学

作者：Yang Li、Jiaxiang Liu、Yusong Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_528dd5a5b1be)

> 长时程智能体在跨会话交互中面临记忆碎片化导致的时序错乱、事实矛盾与身份丢失，即“灵魂侵蚀”。现有检索增强生成（RAG）将记忆视为静态外部文本，缺乏内部演化机制，无法解决动态状态下的认知一致性。BMAM借鉴认知神经科学，将记忆解耦为海马体、颞叶等六个功能子系统，通过时间线索引与混合检索实现多尺度协同。该架构在LoCoMo上取得78.45%准确率，验证了模块化分工对缓解记忆退化的有效性，但其性能仍低于当前结构化图谱SOTA，且身份一致性评估依赖特定基准，泛化性存疑。

】

---

【BNLP: A Text Annotation Platform for Quality Control of LLM-Generated Annotations ｜BNLP：面向 LLM 辅助标注的质量控制平台

研究机构：中国科学院、美国普林斯顿高等研究院

作者：Xinhao Zhuang、Qiongyu Tian、Yalin Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f8d9e2efa06)

> 导读

】

---

【Born Pragmatic, Trained to Hallucinate? Quantifying the Origins of Contextual Bias in LLMs via the PaCE Benchmark ｜语用幻觉量化与语境翻转基准

作者：Ziming Li、Yu Tian、Tian Lan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5beec205015c)

> 大语言模型在强化学习对齐后，常因过度归因社交意图而在需要严格逻辑的场景中产生非事实推断，即语用幻觉。现有基准仅评估模型“能否推理”，却忽视其“能否抑制推理”的能力，导致无法区分真实语境理解与表面关联记忆。本文提出PaCE基准，通过“语境翻转”构造对抗性自然语言推理任务，量化模型在语用与字面语境下的性能差距。该工作揭示了RLHF导致的“行为锁定”现象，但仅依赖提示工程验证机制，缺乏对内部表征的因果干预。

】

---

【Break Through the Compression Bottleneck: From Theory to Practice ｜量化与低秩分解的非正交性证明及对角粘合法

研究机构：中国科学院、中国科学院大学

作者：Xiusheng Huang、Lu Wang、Yequan Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_08ae6203b98c)

> 大语言模型（LLM）压缩常假设量化与低秩分解相互独立，但本文指出二者组合会引入复合误差。现有方法忽略激活值离群点导致的非正交效应，且未明确最优压缩顺序。本文通过理论证明量化与低秩分解非正交，推导先低秩后量化的最优顺序，并提出对角粘合法（Diagonal Adhesive Method, DAM）以平衡量化方差。该工作为组合压缩提供了理论依据，但其效果高度依赖特定比特宽度和压缩率，泛化性存疑。

】

---

【Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction ｜打破上下文惯性：基于单轮锚点的强化学习

作者：Xingwu Chen、Zhanqiu Zhang、Yiwen Guo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04783)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04783)

> 多轮交互中，大语言模型（LLM）常因固守前轮错误推理而忽略用户的新约束，导致性能较单轮场景显著下降。现有方法多通过弃权或澄清请求缓解信息不足，但无法处理需动态修正的“错误纠正”场景，且未触及模型内部对历史轨迹的刚性依赖这一根本原因。本文提出 RLSTA，利用模型自身在单轮全信息下的正确回答作为内部奖励锚点，通过强化学习校准多轮生成行为。该方法在数学与代码任务上显著优于标准微调，但其在缺乏明确单轮解的开放域任务中的泛化能力仍存疑。

】

---

【Breaking the Autoregressive Chain: Hyper-Parallel Decoding for Efficient LLM-Based Attribute Value Extraction ｜超并行解码

研究机构：加拿大麦吉尔大学、加拿大魁北克人工智能研究所

作者：Theodore Glavas、Nikhita Vedula、Dushyanta Dhyani 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.26209)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.26209)

> 属性值提取（Attribute Value Extraction, AVE）任务中，多个属性值的生成在给定文档上下文时具有条件独立性，但标准自回归解码强制将其串行化，导致离线批量推理吞吐量受限。现有投机解码受限于草稿质量与验证开销，无法充分利用这种结构独立性。本文通过操纵位置ID与注意力掩码，实现非连续令牌的并行生成，在保持输出质量的前提下将推理成本降低至13.8倍。该方案在特定结构化任务上有效，但其对属性长度分布的依赖性及位置编码外推误差的影响尚存疑。

】

---

【Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints ｜高熵搜索评估悖论与计算不可约约束

作者：Juntao Wu、Wei Wen、Xianting Huang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a63e276d803a)

> 高熵搜索（High-Entropy Queries, HEQs）要求模型在开放网络空间中枚举大量候选项，但验证完整性所需的真值集在任务定义上不可获得，导致现有基准系统性惩罚超额正确项。现有基于人工标注答案池的评估范式无法解决这一悖论，本文切入点是通过引入计算不可约的哈希约束，将枚举任务转化为稀疏答案搜索。具体做法是利用密码学哈希函数构建可自动验证且语义不可优化的约束，使模型必须执行真实的遍历搜索。该范式在理论上证明了与全量枚举的计算等价性，但在实证中暴露出对前沿模型区分度不足及缺乏语义歧义性模拟的局限。

】

---

【Breaking the Static Graph: Context-Aware Traversal for Graph-Based RAG ｜打破静态图：基于上下文感知遍历的图增强检索

研究机构：香港科技大学、香港中文大学

作者：Kwun Hang Lau、Fangyuan Zhang、Boyu Ruan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_63e9a74eab77)

> 多跳问答中，基于知识图谱的检索常因静态边权导致随机游走陷入高度枢纽节点，造成证据链断裂。HippoRAG 2 等现有方法虽引入图结构，但索引期固定的转移矩阵无法响应查询意图，导致召回率虚高而推理完整性不足。CatRAG 通过引入符号锚定、查询感知动态边权及关键事实段落增强，将静态图转化为查询自适应导航结构。该方法在 MuSiQue 等基准上显著提升了全链检索率，但下游问答 F1 提升有限，且动态边权依赖 LLM 推理，其效率与复杂路径回溯能力存疑。

】

---

【Bridging Reasoning and Action: Hybrid LLM–RL Framework for Efficient Cross-Domain Task-Oriented Dialogue ｜验证式LLM知识赋能强化学习

作者：Yangyang Zhao、Linfan Dai、Li Cai 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e73fb8b2ecea)

> 跨域任务导向对话（Task-Oriented Dialogue, TOD）的核心难点在于单一领域决策对其他领域施加的可行性约束，这些约束常隐含于常识或时间逻辑中，导致长程规划失效。现有方法要么依赖纯强化学习（RL）在状态缺失下盲目探索，要么直接使用大语言模型（LLM）生成动作却因幻觉和跨轮次漂移而不可靠。本文切入点是将约束建模重构为状态构建问题，通过双角色LLM交叉质询验证隐式约束，并将其接地为结构化槽值对以增强RL策略输入。该框架在MultiWOZ 2.1和Frames上显著提升了跨域泛化能力，但验证机制依赖LLM自身逻辑，存在循环论证风险。

】

---

【Bridging the Culture Gap: A Framework for LLM-Driven Socio-Cultural Localization of Math Word Problems in Low-Resource Languages ｜文化实体扰动下的数学鲁棒性：低资源语言本地化框架

作者：Israel Abebe Azime、Tadesse Destaw Belay、Dietrich Klakow 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22cda7beaaa0)

> 大语言模型在低资源语言数学任务中的表现长期受限于评估数据的文化偏差，现有翻译基准保留英语中心实体，导致模型性能无法反映真实本地场景下的推理能力。本文切入点在于构建自动化文化本地化管道，通过替换人名、组织名与货币，生成符合目标语言文化背景的数学应用题变体。该框架利用大语言模型进行实体分类与替换，并结合质量检查模块确保语义一致性。其价值在于揭示了文化实体对模型鲁棒性的显著影响，但实验仅关注最终答案匹配，未深入诊断推理过程中的逻辑断裂。

】

---

【Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data ｜预算约束下的即时推理评估与偏好提示

作者：Xuanming Zhang、Shwan Ashrafi、Aziza Mirsaidova 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11038)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_802a45c97ef4)

> 现有推理效率优化聚焦于最终答案的Token消耗或训练时的长度惩罚，却忽视了在严格延迟预算下，模型中间输出质量的演变轨迹。本文切入点在于将“即时推理”形式化，提出Anytime Index量化质量-Token权衡，并设计PDP方法通过自生成偏好对提升中间推理质量。该方法无需微调，仅通过推理时提示即可在规划、数学与科学问答任务上提升效率。其价值在于提供了过程级评估工具，但依赖截断重提示的评估协议是否真实反映中断场景，仍存疑。

】

---

【Budget-Aware Routing for Long Clinical Text ｜预算感知临床长文本上下文构建

研究机构：美国麻省理工学院、美国康奈尔大学

作者：Khizar Qureshi、Geoffrey Martin、Yifan Peng

论文原文见 [arXiv](https://arxiv.org/abs/2605.00336)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.00336)

> 临床部署中，长文档的Token成本与延迟直接制约模型可用性，而现有长上下文研究多聚焦于模型内部注意力机制优化，忽略了输入侧的预算约束。本文切入点在于将上下文构建视为背包约束下的子集选择问题，而非模型能力扩展。通过引入RCD目标函数与预算感知路由层，在固定Token预算下动态选择最优提取策略。该工作验证了评估范式对策略选择的决定性影响，但其结论局限于抽取式与生成式摘要任务，对复杂推理场景的泛化性存疑。

】

---

【C2DLM: Causal Concept-Guided Diffusion Large Language Models ｜因果概念引导扩散语言模型

研究机构：浙江大学、华为

作者：Kairong Han、Nuanqiao Shan、Ziyu Zhao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dce2daf01ed5)

> 扩散语言模型（DLM）因丢弃因果顺序而陷入训练低效与推理深度受限的瓶颈，自回归模型（AR）则受限于单向信息流导致的全局结构理解缺失。本文切入点在于识别注意力机制建模先验与自然语言底层因果先验之间的错位，提出C2DLM范式。通过教师模型提取概念级因果图，并利用V-aware Reattention机制在SFT阶段对齐注意力权重，实现因果结构引导。该范式在合成基准上验证了架构改进的有效性，但其对真实世界复杂因果结构的泛化能力仍存疑。

】

---

【C3D: Enhancing LLM Reasoning via Confidence-Guided Contrastive Decoding ｜置信度引导跨前提对比解码

研究机构：中国科学院、中国科学院大学

作者：Yufeng Zhang、Xuepeng Wang、Lingxiang Wu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e2597bb33467)

> 大语言模型在推理时易受上下文无关信息干扰，导致错误累积。现有解码策略多关注层间或有无上下文的对比，忽略了前提内部的细粒度相关性差异。本文提出C3D，通过分解前提并动态对比高/低置信度前提的Logits来修正生成分布。该方法在强推理模型上稳定提升性能，但其增益是否源于模型本身对前提结构的敏感度，而非解码策略的普适性，尚存疑。

】

---

【Calibrated Progressive Distillation: Co-Designing Curriculum and Target Mixing for Knowledge Distillation of Large Language Models ｜校准渐进式蒸馏：协同设计课程与目标混合的LLM知识蒸馏框架

作者：Mengxiang Zhang、Lingyuan Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d546cf53b10)

> 大语言模型知识蒸馏旨在将大型教师模型的参数化知识迁移至小型学生模型，以缓解高并发部署中的推理延迟与内存瓶颈。现有方法通常独立设计课程学习（数据排序）与目标混合（监督信号），导致训练难度轨迹与监督强度失配，引发模式坍塌或学习停滞。本文提出校准渐进式蒸馏（Calibrated Progressive Distillation, CPD），通过统一的难度画像同步调度训练子集与混合系数，实现监督信号与学生能力的动态对齐。该框架在指令跟随、数学推理与代码生成任务上均优于强基线，但其依赖静态难度画像的假设在长序列生成场景下的有效性尚存疑。

】

---

【Can AI Revise Research Papers with Human Review Feedback? An Empirical Study and Benchmark ｜基于反馈的自主论文修订基准

作者：Zihan Luo、Hong Huang、Jianxun Lian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_123b9d0fced9)

> 现有LLM辅助学术写作研究多聚焦于单轮生成或静态评审，缺乏对“人类反馈驱动迭代优化”这一核心科研闭环能力的量化评估。主流基准如PaperBench仅测试代码复现，忽略了评审意见理解与文本-代码联合修订的复杂性。本文通过构建包含真实ICLR 2025论文、代码仓库及评审意见的三元组数据，提出ReviseBench，利用Camera-ready版本作为人类金标准进行成对比较。该基准揭示了当前SOTA模型在学术严谨性与实验真实性上的巨大缺口，但其小规模数据集限制了结论的普适性。

】

---

【Can Large Language Models Infer Human Actions and Motives? Evaluation in Social Prediction and Inspection Games ｜社会预测与检查博弈中的大语言模型动机推断

研究机构：美国南加州大学

作者：Kaleen Shrestha、Abhinav Gupta、Harish Dukkipati 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c6d196101900)

> 该方向旨在评估大语言模型（LLM）能否从历史交互中推断对手的潜在动机，并将其泛化至新情境。现有方法多依赖静态基准或实时对抗，缺乏对“动机-行为”因果链的细粒度诊断，导致无法区分LLM是真正理解了对手意图，还是仅匹配了表面统计规律。本文引入认知科学验证的社会预测博弈（SPG）与检查博弈（IG），通过对比人类与LLM在预测动作及跨情境泛化上的表现，揭示了LLM在动机推断上的结构性缺陷。这一发现挑战了LLM具备通用社会推理能力的假设，但其结论受限于特定博弈结构与温度设置，泛化性存疑。

】

---

【Can LLMs Compress (and Decompress)? Evaluating Code Understanding and Execution via Invertibility ｜往返代码一致性评估

研究机构：英国爱丁堡大学

作者：Nickil Maveli、Antonio Vergari、Shay B. Cohen

论文原文见 [arXiv](https://arxiv.org/abs/2601.13398)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13398)

> 现有代码基准仅验证单向输入输出预测，无法区分模型是依靠模式匹配还是机制理解生成代码。RTCE通过强制模型执行无损压缩算法的正向编码与逆向解码，以精确匹配验证双向逻辑闭环。该框架揭示了当前大语言模型在双向推理一致性上的系统性缺陷，但受限于合成数据规模与算法类型，其结论向真实复杂代码库的泛化能力存疑。

】

---

【Can LLMs Hear the Dogwhistle? ｜狗哨语言下的LLM安全盲区评估

研究机构：南方科技大学、澳门大学

作者：Yifan Liu、Yi Lin、Xinwei Guo 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19c46d67fe18)

> 现有LLM安全对齐机制主要依赖显式毒性词法信号，导致模型在面对表面中性但隐含歧视意图的“狗哨语言”时出现系统性失效。本文指出，当前基准缺乏对语用维度（如立场、交互类别）的控制，无法隔离隐式语义对安全行为的影响。通过构建DOGBENCH，利用模板化控制变量与平行词库对比，量化了隐式有害语言引发的风险放大效应。该工作揭示了规模扩张无法弥补的语义理解盲区，但评估依赖LLM-Judge的隐式判定能力，其边界尚待验证。

】

---

【Can Multi-agent Help Disambiguation in Multi-domain Translation? ｜多智能体协作消歧框架

作者：Zhibo Man、Shaoyang Xu、Yujie Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22f70caf059b)

> 多领域翻译（Multi-Domain Translation, MDT）面临的核心挑战是同一词汇在不同领域语境下需映射至截然不同的语义，导致翻译歧义。现有基于提示工程的方法虽能注入领域信息，但受限于单一提示上下文的长度与角色混淆，难以有效解耦通用语义与领域特异性。本文提出多智能体协作消歧框架（MACD），通过领域分配、通用翻译、领域消歧及融合四个智能体的分工协作，显式化消歧过程。该框架在多个领域上提升了翻译质量与消歧准确率，但其依赖人工设计的提示交互，且在长文本语境下的消歧增益机制尚需进一步厘清。

】

---

【Can Post-Training Transform LLMs into Causal Reasoners? ｜后训练能否将大语言模型转化为因果推理器

研究机构：复旦大学、同济大学

作者：Junqi Chen、Sirui Chen、Chaochao Lu

论文原文见 [arXiv](https://arxiv.org/abs/2602.06337)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06337)

> 因果推理要求模型区分统计关联与真实机制，但大语言模型（LLM）在数值因果估计上常因依赖记忆或表面模式而失效。现有后训练方法虽能提升通用推理能力，却缺乏针对因果结构内化与鲁棒性的系统验证。本文构建CauGym数据集，系统对比五种后训练策略在因果任务上的表现，发现在线强化学习（Online RL）能显著增强模型对因果定理的内化能力。该工作证实了小规模模型经特定训练可超越大规模基线，但其高分是否掩盖了深层结构理解的缺失仍存疑。

】

---

【Can We Entrust Justice to AI?: How Persona Traps Contaminate Reasoning in Criminal Investigation ｜隐性偏见传播（Implicit Bias Propagation）在刑事推理中的量化

作者：Jaewook Lee、Myeong-Cheol Kang、Jong-hun Shin

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6f019fc15279)

> 大语言模型（LLMs）在复杂推理任务中是否受无关人口统计学特征影响，是部署安全的关键盲区。现有偏见评估多聚焦于显式身份属性（如种族、性别）的静态问答，忽略了关系型偏见在长程推理中的隐性渗透，且缺乏对推理过程污染的独立度量。本文通过中性化谋杀案数据集并注入受控Persona，提出决策不一致率（DIR）与推理影响率（IRR）双指标，量化了模型在结论与过程层面的偏见传播。该研究揭示了关系偏见被当前对齐机制系统性忽视的事实，但评估依赖单一裁判模型且未验证缓解策略的有效性。

】

---

【Candidate-Aware Retrieval and Reranking for Multiple-Choice Question Answering: Arabic as a Case Study ｜答案感知检索与重排序的阿语多选问答优化

作者：Yassine Bouziane、Youness Moukafih、Mounir Ghogho

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f0f18ac73ba)

> 阿语大语言模型在多选问答（Multiple-Choice Question Answering, MCQA）任务中面临检索噪声与证据区分度不足的双重瓶颈，导致小模型在复杂推理上表现滞后。现有检索增强生成（Retrieval-Augmented Generation, RAG）方法仅基于问题检索，忽略了候选答案与上下文之间的交互作用，难以区分背景信息与决定性证据。本文提出一种答案候选感知的检索与重排序框架，通过联合建模问题、选项与上下文的三元组关系，提升小模型在阿语人文学科上的表现。该方法在资源受限条件下实现了与大模型相当的准确率，但其评估范围局限于人文学科，且未涵盖方言场景，泛化能力存疑。

】

---

【CaPEdit: Capability-Preserving Lifelong Knowledge Editing For Language Models ｜能力保持的终身知识编辑

研究机构：清华大学、中国科学技术大学

作者：Song-Li Wu、Zhaocheng Du、Xianquan Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4d04b1653dae)

> 终身知识编辑（Lifelong Knowledge Editing, LKE）旨在通过局部参数更新让大语言模型（LLMs）持续吸收动态事实，但现有方法在累积编辑中导致记忆、推理等基础能力严重退化。传统正则化策略因限制更新幅度而牺牲知识注入效率，且未能区分事实更新与程序性知识适应的时间尺度差异。CaPEdit 提出双时间尺度奖励机制，通过显式合成程序性知识信号，将快速事实修正与慢速能力保持解耦。该框架在保持高编辑精度的同时显著提升了能力保留率，但其对程序性知识合成的依赖是否引入额外计算瓶颈，以及在非结构化知识编辑中的泛化能力，仍存疑。

】

---

【Carefully Considering Culture: Analyzing LLM Alignment in Single- and Multi-Cultural Settings using Cultural Consensus Theory ｜文化共识理论下的LLM对齐诊断

研究机构：美国圣母大学

作者：Krishna Pothugunta、John P. Lalor

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1ab8719cb8a0)

> 大语言模型（LLMs）在跨文化部署中常出现“均值坍缩”，即模型输出趋向于稀释的中间态，无法反映特定文化群体的真实多样性。现有评估多依赖分布匹配或单一准确率指标，忽略了群体内部共识的结构差异，导致无法区分模型是真正理解文化还是仅仅制造了虚假的一致性。本文引入文化人类学中的文化共识理论（Cultural Consensus Theory, CCT），通过量化模型与人类群体在共识强度上的方差差异，揭示了模型在匹配共识方向时人为膨胀共识强度的现象。该研究提供了从“分布匹配”到“结构诊断”的新视角，但其诊断结果如何转化为具体的对齐干预策略仍待探索。

】

---

【CARL: Constraint-Aware Reinforcement Learning for Planning with LLMs ｜约束感知强化学习

研究机构：浙江大学、香港城市大学

作者：Qiuyi Qi、Jinjian Zhang、Mutian Bao 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.04854)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.04854)

> 大语言模型在规划任务中常因忽略输入中的硬性限制而生成无效方案，现有方法多依赖外部符号求解器或任务分解来规避此缺陷，但未能提升模型内在的约束遵循能力。本文切入点在于将约束合规性转化为强化学习中的连续奖励信号，通过对比有约束与无约束输入下模型输出的分布差异来引导策略优化。具体做法是构建基于KL散度的约束感知奖励函数，兼容多种RL算法。该方法在TravelPlanner上取得56.1%的最终通过率，显著优于基线，但其效果是否源于对约束形式的过拟合而非语义理解，仍需更严格的跨域验证。

】

---

【CAST: Achieving Stable LLM-based Text Analysis for Data Analytics ｜表格文本分析中的运行间稳定性约束

研究机构：南京大学、清华大学

作者：Jinxiang Xie、Zihao Li、Wei He 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15861)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15861)

> 表格数据中的自由文本列需转化为结构化信号以支持OLAP操作，但大语言模型（LLM）的概率生成特性导致相同输入在多次运行中产生语义漂移的标签或摘要，破坏了下游过滤与聚合的确定性。现有方法如Self-Consistency通过多轨迹投票提升准确率，却忽视了分析场景对输出一致性的刚性需求。本文提出CAST框架，通过算法提示（Algorithmic Prompting, AP）与思维前置（Thinking-before-Speaking, TbS）在单次调用内约束隐式推理路径，实现稳定性提升。该方案在稳定性指标上显著优于基线，但其对复杂多表关联场景的泛化能力尚未得到验证。

】

---

【Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction ｜目标感知因果图构建与路径审计

研究机构：澳大利亚格里菲斯大学

作者：Su Lan、Xuefei Yin、Yanming Zhu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ef450afdf263)

> 无上下文因果问答要求模型在缺乏外部证据时，判断干预变量对目标变量的方向性影响，这迫使模型依赖内部参数知识而非表面关联。现有链式思维或图思维方法虽能组织推理路径，但缺乏显式因果结构约束，导致推理过程不可审计且易受语义噪声干扰。本文提出一种推理时动态构建目标感知因果图并进行路径级反事实审计的框架，将隐式语言推理转化为显式符号化因果评估。该框架在多个基准上显著提升了方向预测准确率，但其效果依赖于LLM生成因果三元组的初始质量，且未解决模型内部是否真正编码因果方向的根本问题。

】

---

【CausalityCheck: A Framework for Evaluating Causal Reasoning in Large Language Models ｜因果链过程评估框架

作者：Jiang Li、Zehua Duo、Guanglai Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_458b67c2a007)

> 大语言模型在因果推理任务中常出现“答案正确但过程错误”的假阳性，传统仅评估答案准确率的基准无法区分模型是真正理解因果机制还是依赖训练数据记忆。现有基准如CLadder侧重层级测试，但缺乏对推理过程忠实度与抗干扰鲁棒性的细粒度诊断。本文提出CausalityCheck框架，通过构建4×4维度的任务泛化与推理鲁棒性清单，将单一问答扩展为36种变体以量化因果链误识与经验推理依赖。该框架揭示了当前主流模型在过程正确性上的显著短板，但其评估指标是否真正捕捉了因果结构而非仅解释风格，仍需进一步验证。

】

---

【CentaurTA: A Self-Improving Human-Agents Collaboration Framework for Thematic Analysis ｜CentaurTA：基于Actor-Critic自改进机制的主题分析框架

作者：Lei Wang、Min Huang、Eduard Dragut

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3fb37469f7d0)

> 主题分析（Thematic Analysis, TA）旨在从非结构化文本中提炼意义模式，但传统人工编码耗时且难以规模化，而现有大语言模型（LLM）辅助工具多将人类反馈视为一次性修正，缺乏持续学习机制。本文提出CentaurTA，将专家反馈重构为持久学习信号，通过Actor-Critic架构在提示词层面实现自改进。该方法在三个领域数据集上显著提升了编码对齐度，但其评估依赖小样本与特定模型版本，通用有效性存疑。

】

---

【CFlowPsyD: An Analysis-Enhanced Dataset for Asynchronous Psychological Counseling through Self-Optimizing Multi-Agent Framework ｜异步心理咨询对话合成框架

研究机构：中国科学院、北京理工大学

作者：Donghao Li、Yifan Deng、Jinta Weng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1db0fd52dfea)

> 异步心理咨询（Asynchronous Psychological Counseling, APC）旨在通过时空解耦的交互模式，支持认知行为疗法（CBT）等依赖客户自主反思的循证干预，但真实语料因隐私法规极度稀缺。现有同步心理咨询（SPC）数据集缺乏深层分析推理，且静态多智能体框架无法捕捉客户跨轮次的情绪与认知演变。本文提出自优化多智能体框架 CFlowPsy，利用动态画像模块 Persona-Flow 实时追踪客户状态，并注入显式思维链以生成高质量 APC 对话。该框架发布了首个中文 APC 数据集 CFlowPsyD，在一致性与真实性上优于现有同步数据集，但其评估局限于中文同步基线，缺乏与最新多智能体合成框架的直接对比。

】

---

【Chain-in-Tree: Back to Sequential Reasoning in LLM Tree Search ｜树搜索中的链式推理：分支必要性评估

作者：Xinzhe Li

论文原文见 [arXiv](https://arxiv.org/abs/2509.25835)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25835)

> 大语言模型在复杂推理任务中依赖测试时扩展（Test-Time Scaling, TTS）提升性能，但基于树搜索的框架因固定粒度分支导致计算效率低下。现有方法在每一步均强制生成多个候选路径，忽略了平凡步骤无需探索的事实，造成大量冗余调用。本文提出 Chain-in-Tree (CiT)，通过引入分支必要性（Branching Necessity, BN）评估模块，动态决定何时分支、何时链式推进。该方法在保持准确率基本无损的前提下，将推理时间降低 75–85%，但 BN 评估器的质量成为性能稳定性的关键瓶颈。

】

---

【Chain-of-Relations: Faithful and Efficient LLM Reasoning over Knowledge Graphs via Relation-Centric Exploration ｜关系中心探索与全局过滤

研究机构：中山大学

作者：Chenhui Liu、Jianpeng Zhou、Jiahai Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7dfa82fa5a4)

> 知识图谱问答（KGQA）旨在从结构化图谱中检索答案实体，但现有基于大语言模型（LLM）的智能体方法多采用实体中心探索，在中间实体语义缺失或束搜索剪枝时易导致推理路径断裂。本文提出 Chain-of-Relations (CoR) 框架，通过关系链构建与延迟约束验证，解决实体不完整与过早剪枝问题。CoR 将探索单元从实体迁移至关系，并在完整路径构建后执行全局实体过滤。该框架在忠实度与效率上优于基线，但其对关系空间完整性的依赖及在 Wikidata 上的性能波动仍存疑。

】

---

【Chameleons and Guardians: Unveiling the Divergence in Personality Plasticity and Cognitive Resistance across LLMs ｜多智能体人格诱导框架

作者：Jiaxin Wu、Jie Zhao、Huangxinrong 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_265887caac73)

> 大语言模型（LLM）的人格可控性研究长期面临输入端提示诱导的稳定性缺陷，传统角色指令易受上下文漂移影响且无法跨模型泛化。本文切入点在于揭示不同LLM家族在人格诱导上的合规性分歧，即西方模型的高可塑性与东方模型的认知抵抗。通过构建生成器-裁判多智能体协作框架，将MBTI题目改写为语义等价但表达多样的诱导语境，实现免训练的人格重塑。该框架在输入端实现了细粒度控制，但未触及内部表示机制，其相对于白盒激活工程的优越性尚存疑。

】

---

【Characterizing Selective Refusal Bias in Large Language Models ｜选择性拒绝偏见

研究机构：美国罗格斯大学

作者：Adel Khorramrouz、Sharon Levy

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9536a9646709)

> 大语言模型（LLM）的安全护栏旨在拦截有害内容，但现有评估多聚焦于“是否拒绝”的鲁棒性，忽视了“拒绝谁”的公平性。主流护栏在训练数据分布狭窄的影响下，对不同人口统计学群体的保护力度存在系统性差异，导致对边缘群体过度拒绝，而对主流群体合规生成有害内容。本文通过构建平行反事实提示集量化这种选择性拒绝偏见，并设计间接提示攻击验证其脆弱性。该工作揭示了护栏公平性的严重缺陷，但未提供修复机制，且攻击成功率高度依赖特定模型的对齐强度。

】

---

【Characterizing Web Search in The Age of Generative AI ｜生成式搜索输出特性表征

作者：Elisabeth Kirsten、Jost Grosse Perdekamp、Mihir Upadhyay 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11560)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11560)

> 生成式搜索将传统排名列表转化为单一合成文本，但现有评估指标无法捕捉其源选择偏差与内部知识依赖度。本文通过对比传统与生成式引擎的源重叠率及概念覆盖度，量化了这种范式转换对信息暴露的影响。其价值在于揭示了“低引用高覆盖”现象，但缺乏对幻觉风险的直接度量。

】

---

【ChildEval:WHEN LARGE LANGUAGE MODELS MEET CHILDREN’S PERSONALITIES ｜儿童偏好个性化评估基准

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a241f802c54e)

> 通用大语言模型（LLM）的个性化研究长期聚焦于成人场景，缺乏针对3-6岁儿童特定发展需求与语言特征的评估体系。现有基准如LaMP和PersonaMem虽提供了多轮对话与画像框架，但无法捕捉儿童互动中情感适应、发展适宜性等细粒度维度，导致模型在儿童陪伴场景下的表现无法被系统量化。本文构建ChildEval基准，通过合成29K儿童画像与隐式偏好对话，并提出儿童导向评估协议（COE），以验证不同适配策略在长上下文下的偏好一致性。该工作填补了儿童个性化评估的空白，但其依赖全合成数据且未建模动态安全约束，评估结果向真实儿童场景的迁移性存疑。

】

---

【Choose Your Lens: Multi-Perspective Value Alignment of Chain-of-Thought Reasoning ｜价值图一致思维链

作者：Gejian Zhao、Hanzhou Wu、Xinpeng Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_048abf0b17b3)

> 多元价值对齐旨在使大语言模型（LLM）输出反映人类价值观的多样性，而非收敛于单一共识。现有可引导对齐方法在文本空间操作，常导致模型为迎合特定视角而幻觉“便利事实”，破坏跨视角的事实一致性。本文提出VGC-CoT，将推理建模为多层价值图上的有向遍历，通过图结构约束强制事实共享与价值分歧的解耦。该方法在事实完整性上显著优于基线，但其依赖人工构建的规范子图，限制了在动态社会价值观场景下的可扩展性。

】

---

【Chronos: Learning Temporal Dynamics of Reasoning Chains for Test-Time Scaling ｜时序推理链评分器

研究机构：中国科学技术大学

作者：Kai Zhang、Jiayi Liao、Chengpeng Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a399516fda38)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段的计算量提升大语言模型（LLM）的复杂任务性能，但并行采样后的聚合环节常因忽视轨迹质量差异而失效。现有方法多采用均匀投票或静态置信度加权，无法捕捉推理过程中的时序动态，导致正确但低频的答案被错误过滤。本文提出 Chronos，一种基于多尺度卷积的轻量级时序评分器，将轨迹的 Token 概率序列建模为时间序列以评估其逻辑一致性。该方法在无需额外训练骨干模型的前提下显著提升了聚合精度，但其性能上限仍受限于骨干模型的初始推理能力，且跨域泛化能力有待进一步验证。

】

---

【CLAG: Adaptive Memory Organization via Agent-Driven Clustering for Small Language Model Agents ｜基于代理驱动聚类的自适应记忆组织

研究机构：韩国高丽大学

作者：Taeyun Roh、Wonjune Jang、Junha Jung 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.15421)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.15421)

> 长程任务中，大语言模型（LLM）智能体依赖外部记忆维持连贯性，但传统全局检索池随记忆增长导致语义干扰与更新污染，小语言模型（SLM）对此尤为脆弱。现有代理记忆框架虽引入自进化机制，却仍在全局无结构存储中运行，无法隔离主题混杂带来的噪声。CLAG通过SLM代理在线路由将记忆划分为语义一致的簇，并在簇内执行局部演化与两阶段检索，以轻量级结构抑制跨主题干扰。该框架在SLM场景下显著提升了鲁棒性，但其对大模型骨干的增益边际递减，且未覆盖隐私合规与多模态对齐等生产级约束。

】

---

【CLaRE-ty Amid Chaos: Quantifying Representational Entanglement to Predict Ripple Effects in LLM Editing ｜关键层表示纠缠量化

研究机构：新加坡国立大学

作者：Manit Baser、Alperen Yildiz、Dinil Mon Divakaran 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19297)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19297)

> 知识编辑在更新目标事实时，常引发无关事实的意外改变，即涟漪效应，但现有评估多在编辑后检测，缺乏编辑前的风险预测能力。梯度相似度方法（GradSim）虽能估计纠缠，但计算成本高且与跨域涟漪效应相关性弱。本文提出CLARE，通过提取单一关键层的前向激活向量并计算余弦相似度，在编辑前量化事实间的表示纠缠。该方法在预测精度与计算效率上显著优于梯度基线，为构建保留集和红队测试提供了轻量级基础设施，但其预测的是风险概率而非确定性干扰，高纠缠并不必然导致涟漪。

】

---

【CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark ｜跨语言生成控制基准与无监督转向优势验证

作者：Daniil Gurgurov、Yusser Al Ghussin、Tanja Baeumel 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_79f69db10224)

> 多语言大语言模型在推理时难以稳定切换至目标语言，现有激活引导方法缺乏跨语言标准化评估协议，导致无法量化不同语言下的控制有效性。本文切入点在于构建覆盖32种语言的平行问题基准，并系统对比提示工程与多种表示级干预策略。通过引入语言强制成功率与语义相关性调和平均指标，本文验证了残差流均值差向量（DiffMean）在无监督场景下显著优于有监督探针及稀疏自编码器方法。该基准填补了多语言转向评估空白，但其结论局限于特定模型架构，且未探讨低资源语言中线性表示假设的失效边界。

】

---

【CLewR: Curriculum Learning with Restarts for Machine Translation Preference Learning ｜基于重启机制的机器翻译课程学习偏好优化

研究机构：罗马尼亚布加勒斯特大学

作者：Alexandra Dragomir、Florin Brad、Radu Tudor Ionescu

论文原文见 [arXiv](https://arxiv.org/abs/2601.05858)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05858)

> 导读 大语言模型在机器翻译中的偏好优化面临训练数据顺序被忽视的问题，导致模型在训练后期遗忘早期易学样本，即灾难性遗忘。现有课程学习方法虽引入难度排序，但未解决多轮训练中的遗忘累积，且主要依赖参考模型导致优化信号弱。本文提出CLewR，通过每轮重启易到难的数据排序，结合机器翻译特定指标定义难度，并增强自适应拒绝偏好优化算法。该方法在多个模型家族上验证了有效性，但其在非翻译任务及复杂噪声场景下的泛化能力仍存疑。

】

---

【ClimAgent: LLM as Agents for Autonomous Open-ended Climate Science Analysis ｜气候科学自主智能体

研究机构：香港科技大学、山东大学

作者：Hao Wang、Jindong Han、Wei Fan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16922)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16922)

> 气候分析面临物理约束复杂与数据驱动特性双重挑战，现有LLM智能体多局限于简单问答，缺乏对物理机制的深度建模能力。本文切入点在于构建专用气候环境（Climate Environment, CE）以提供物理接地，并通过四阶段闭环流程实现开放式气候问题的端到端求解。ClimAgent通过检索增强与任务特定优化确保物理一致性，并在自建基准ClimaBench上验证了其相对于通用智能体的优越性。该工作填补了气候领域数据驱动基准的空白，但其泛化能力与多模态适配性仍存疑。

】

---

【CliniCAST: Benchmarking Acoustic Grounding and Text Dominance in Medical Triage ｜临床声学接地基准

作者：Kyusik Kim、Hyunwoo Yoo、Jaehoon Choi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2475ae91b56e)

> 大型音频语言模型（LALM）在医疗分诊中面临的核心矛盾是：模型能否在词汇内容固定时，仅凭副语言声学证据做出可靠的紧急度判断？现有通用基准无法隔离声学因果，导致模型对文本先验的依赖被掩盖。本文通过构建控制变量合成数据集，量化了LALM的“文本主导”偏差。该基准揭示了当前模型在高风险声学信号面前的脆弱性，但其合成语音的病理真实性仍存疑。

】

---

【Clustered Self-Assessment: A Simple yet Effective Method for Uncertainty Quantification in Large Language Models ｜聚类自评估

研究机构：日本东京大学

作者：Qi Cao、Takeshi Kojima、Andrew Gambardella 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03846)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03846)

> 大语言模型在高风险场景中的部署受制于其“自信地犯错”倾向，即输出表面流畅但事实错误，且传统基于词法概率的熵值无法区分同义改写与事实错误。现有采样方法仅度量输出差异，未利用模型内部知识，且熵值分数难以被用户直观解读。本文通过语义聚类采样答案构建多选题，利用模型对选项的Token概率作为置信度，实现了高判别力与人类可解释性的统一。该方法在标准基准上显著超越基线，但其依赖Logits访问的特性限制了纯黑盒API部署的适用性。

】

---

【Code over Words: Overcoming Semantic Inertia via Code-Grounded Reasoning ｜代码接地推理：克服语义惯性

研究机构：北京大学、美国加州大学伯克利分校

作者：Manjie Xu、Isabella Yin、Xinyi Tu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18352)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18352)

> 动态本体环境要求模型抑制预训练先验以执行非单调推理，但现有自然语言推理方法因分布语义纠缠导致大模型出现逆缩放现象。本文切入点在于将规则表示从描述性文本转换为可执行代码，通过反事实对比对齐训练实现摊销理论归纳。该方法在Baba Is You环境中显著优于推理时搜索基线，但局限于特定游戏环境且未验证通用逻辑任务迁移性。

】

---

【Code-Switching Information Retrieval: Benchmarks, Analysis, and the Limits of Current Retrievers ｜代码切换信息检索：基准构建与嵌入空间稳定性分析

研究机构：美国西北大学、日本早稻田大学

作者：Qingcheng Zeng、Yuheng Lu、Zeqi Zhou 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17632)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_796c9f89f79b)

> 现代信息检索系统在处理混合语言查询时面临严重的性能衰退，现有评估体系缺乏对代码切换（Code-Switching, CS）场景的系统性覆盖。本文通过构建人工标注的 CSR-L 与 LLM 生成的 CS-MTEB 基准，揭示了多语预训练模型在 CS 输入下的普遍脆弱性。研究进一步验证了词表扩展仅能部分缓解该问题，无法消除嵌入空间的几何漂移。这一工作填补了文本检索领域 CS 评估的空白，但其干预手段的局限性暗示了深层语义对齐缺失。

】

---

【CodeRise: Bootstrapping LLMs for Ultra Low-Resource Programming Languages via Progressive Self-Refinement Curriculum ｜超低资源编程语言代码生成的渐进式自精炼框架

研究机构：中国科学院大学、中国科学院

作者：Tengfei Wen、Xuanang Chen、Ben He 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dd9054980de6)

> 超低资源编程语言（ULRPLs）因公开语料极度匮乏，导致大语言模型（LLMs）无法通过常规预训练习得其语法与库函数，陷入“冷启动”困境。现有合成数据方法在ULRPLs上失效，因为模型初始能力近乎为零，无法生成任何有效代码样本，且直接提供完整语法文档会导致推理缓慢与数据分布长尾化。CodeRise通过两阶段框架解决此问题：第一阶段利用语法引导与模块加权采样生成种子数据，第二阶段移除语法提示，通过自适应课程学习与多轮自调试生成复杂高质量数据。该方法在Tengo和Janet语言上显著优于基线，但其性能上限受限于骨干模型的通用推理能力，且对完整语法文档的依赖仍是潜在瓶颈。

】

---

【CogBench: Benchmarking Cognitive Alignment of Large Language Models in Educational Question Answering ｜教育问答中的认知对齐基准

作者：Tong Lu、Zhichun Wang、Yuanhao Sun 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f0469b223ded)

> 教育场景下的大语言模型（LLM）常因解释抽象度固定，导致高阶解法对低龄学生不可理解，或低阶解法对高阶学生缺乏严谨性，这一现象称为认知失配。现有基准如 C-EVAL 和 CMMath 通过不同年级的题目区分难度，混淆了问题本身难度与解释适切性，无法隔离评估模型调整推理深度的能力。本文提出 CogBench，将 K-12 数学题重构为“一题多解”形式，利用课程知识图谱对齐解法与认知层级，并引入认知准确率、知识一致性与知识发散度指标。该基准揭示了模型在事实正确性与认知对齐间的权衡，但知识注入反而降低对齐度的反直觉结果暗示了预训练偏置的深层影响。

】

---

【CogEmp:A Cognitive Empathy-Oriented Dialogue System for Structured Psychological Counseling ｜认知共情导向的心理咨询对话系统

作者：Yiguo Deng、Xia Lei、Yuan Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_51c2ca5c0351)

> 现有LLM心理咨询系统多停留在情感共鸣层面，缺乏对用户情绪背后深层心理动因的建模能力，导致干预流于表面安慰。本文切入点在于将认知共情操作化为“情绪识别+因果归因”的双轨任务，通过合作博弈论算法自动提取情绪触发源，并以此驱动检索增强生成。具体做法是构建识别-理解-生成三阶段流水线，利用Harsanyi分解定位情绪原因，再匹配主题与策略生成响应。该方案在中文共情基准上显著优于基线，但其因果归因仅作用于单轮输入，且依赖合成数据，深层信念追踪能力存疑。

】

---

【Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation ｜动态图思维驱动的认知智能体框架

作者：Chen Lifan、Wei Ding、Jingwen Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a79cbcf5c9b5)

> 金融报告生成要求在开放且充满噪声的环境中，将碎片化数据重构为逻辑严密的专业叙事，传统静态推理架构无法应对实时市场中的“未知未知”。现有方法要么依赖预定义工作流导致适应性不足，要么缺乏垂直领域的深度专业知识。Cogito 通过引入动态图思维（Dy-GoT）实现推理拓扑的运行时演化，并结合社会协作机制协调多智能体分工。该框架在自建金融基准上超越了闭源商业系统，但其依赖高算力消耗且缺乏通用基准验证，泛化能力存疑。

】

---

【Cognitive Analysis Graph-Guided Multi-Turn Safety Enhancement for Large Language Models ｜认知图引导的多轮安全对齐

作者：Lanxue Zhang、Yuqiang Xie、Fang Fang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_538a931f73b2)

> 多轮对话中，孤立无害的查询在历史上下文叠加下可能演变为有害请求，而现有推理时对齐方法因缺乏对问题-响应因果关系的显式建模及历史信息的结构化复用，难以阻止此类“语境性越狱”。CogGSE 通过构建检索式认知分析图并跨轮剪枝历史安全节点，将安全决策从隐式概率操控转为显式认知步骤引导。该方法在开源小模型上显著提升了多轮安全性，但其绝对安全上限仍低于前沿专用对齐方法，且图检索噪声对复杂攻击的鲁棒性存疑。

】

---

【Cognitive-Uncertainty Guided Knowledge Distillation for Accurate Classification of Student Misconceptions ｜认知不确定性引导的知识蒸馏框架

研究机构：华南理工大学、香港科技大学

作者：Qirui Liu、Hao Chen、Weijie Shi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14752)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14752)

> 教育场景下的学生错误诊断面临真实数据稀缺、标签噪声高及大模型认知偏差三重困境，传统合成数据扩充因分布差距失效，而直接微调小模型又易过拟合噪声。本文切入点在于摒弃数据生成，转而挖掘现有真实数据中的高价值样本，通过两阶段蒸馏与自适应损失实现精准分类。该框架在仅使用10.30%筛选样本的情况下，使4B参数学生模型在MAP-Charting数据集上达到0.9585的MAP@3，超越72B教师模型，但其有效性高度依赖特定教育分类任务的标签结构，泛化至生成式推理场景的潜力存疑。

】

---

【CollabCoder: Plan-Code Co-Evolution via Collaborative Decision-Making for Efficient Code Generation ｜协同进化代码生成

作者：Duy Tung Doan、Quang Huy Phung、Dzung Nguyen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13946)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a03012f7df10)

> 多智能体代码生成框架长期受困于静态规划与无状态调试，导致在复杂任务上产生大量冗余计算且难以定位根本错误。现有方案如MapCoder与CodeSIM虽引入迭代机制，但规划模块在调试过程中保持固定，无法根据代码反馈动态修正高层逻辑。本文提出CollabCoder，通过协同决策模块动态选择更新规划或代码，并结合推理轨迹累积历史经验，实现规划与代码的协同进化。该方法在保持高准确率的同时显著降低计算开销，但其固定权重机制在极端难度任务上的适应性仍存疑。

】

---

【Colorful Talks with Graphs: Human-Interpretable Graph Encodings for Large Language Models ｜色彩化图结构编码

作者：Angelo Zangari、Peyman Baghershahi、Sourav Medya

论文原文见 [arXiv](https://arxiv.org/abs/2602.10386)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.10386)

> 大语言模型（LLM）在处理图结构任务时，常因将图线性化为文本序列而丢失拓扑信息，导致多跳推理失效。现有方法多采用任意数值ID或连续嵌入，这些符号对LLM而言语义不透明，无法利用其预训练的语言先验。本文提出基于有序Weisfeiler-Leman（WL）精炼的结构编码，将节点标签映射为人类可解释的颜色词，以弥合图结构与LLM语言空间的鸿沟。该方法在节点分类与图算法任务上显著优于基线，但其性能依赖于颜色粒度与图规模的匹配，且未验证在大规模动态图上的泛化能力。

】

---

【ComfyFlow: Benchmarking LLMs for AIGC Workflow Generation ｜COMFYFLOW：AIGC工作流生成的基准与后训练范式

研究机构：哈尔滨工业大学、阿里巴巴集团

作者：Zhenran Xu、Yiyu Wang、Yunxin Li 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_575ea5a240f6)

> 导读

】

---

【Comprehensiveness Metrics for Automatic Evaluation of Factual Recall in Text Generation ｜基于语料库的LLM输出完整性自动评估

研究机构：英国帝国理工学院、IBM研究院

作者：Adam Dejl、James Barry、Alessandra Pascale 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07926)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac108736783c)

> 大语言模型在安全关键领域不仅会编造事实，更会遗漏关键信息或片面呈现冲突证据，而现有事实性评估指标主要关注“说了什么是否对”（Precision），缺乏对“该说的说了多少”（Recall）的量化能力。本文提出三种基于背景语料库的完整性评估指标，通过原子事实分解与自然语言推理（NLI）构建覆盖图，直接识别模型输出中缺失的具体信息。实验表明，最简的端到端（E2E）方法在平均性能上优于复杂的图结构方法，但鲁棒性显著下降。该工作填补了事实性评估中“遗漏检测”的空白，但其结论依赖于特定语料库质量，且E2E方法的稳定性存疑。

】

---

【Concept Tokens: Learning Behavioral Embeddings Through Concept Definitions ｜概念令牌：基于定义文本的行为嵌入学习

作者：Ignacio Sastre、Aiala Rosá

论文原文见 [arXiv](https://arxiv.org/abs/2601.04465)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04465)

> 大语言模型（LLM）内部计算的黑盒特性使得通过外部提示精确控制特定行为变得困难，尤其是当模型缺乏对抽象概念（如“幻觉”或“重述”）的显式理解时。现有软提示方法依赖任务标签或长上下文，无法仅凭概念定义实现行为引导，且长上下文易导致指令遵循能力下降。本文提出概念令牌，通过优化单一输入嵌入向量，使冻结模型从概念定义中内化行为模式。该方法在幻觉抑制和教学反馈场景中展现了方向性控制能力，但其对复杂事实细节的编码可靠性存疑，且未验证内部激活的因果必要性。

】

---

【Conceptual Hierarchies within LLMs ｜概念层级在LLM中的因果定位

研究机构：美国史蒂文斯理工学院

作者：Tiago Almeida、Zining Zhu、Yue Ning

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c1814416acd)

> 导读 机制可解释性（MI）旨在逆向工程大语言模型（LLMs）内部计算结构，以解释其行为并支持安全对齐。现有研究多依赖探针等相关性方法或针对单一事实的因果干预，缺乏对多粒度语义概念在模型内部组织结构的因果性验证。本文采用对称令牌替换（STR）激活补丁，结合重心（Center-of-Gravity）指标，在六个LLM中因果定位细粒度与粗粒度概念的存储顺序。该工作提供了概念层级存储的因果证据，但受限于特定词汇库与统计显著性的边界，其结论的普适性仍需更广泛的语义网络验证。

】

---

【Concise Math Reasoning via Difficulty-Aware Distillation ｜难度感知思维链蒸馏

作者：Yifan Wu、Jingze Shi、Bingheng Wu 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1ef18c04ecf5)

> 思维链（Chain-of-Thought, CoT）蒸馏旨在将大模型的推理能力迁移至小模型，但现有数据普遍冗长，导致学生模型在所有难度问题上均表现出“过度思考”的刚性模式。本文指出，数据冗余不仅增加训练成本，更阻碍了模型根据问题难度自适应调整推理深度的能力。通过引入难度感知重写机制，DAD 在数据生成阶段将长 CoT 压缩为仅保留关键逻辑步骤的短轨迹，构建了平均长度仅 720 tokens 的 LiteCoT 数据集。该方法以 100K 样本量超越了 800K 长 CoT 样本的训练效果，验证了数据简洁性对推理效率与准确率的决定性作用，但其对极限难度任务的泛化边界尚待进一步厘清。

】

---

【Confidence over Time: Confidence Calibration with Temporal Logic for Large Language Model Reasoning ｜时序逻辑置信度校准

研究机构：美国佛罗里达大学

作者：Zhenjiang Mao、Anirudhh Venkat、Artem Bisliouk 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13387)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13387)

> 长程推理中，模型输出的置信度往往随生成步骤动态波动，但现有方法将其压缩为单一标量，导致置信度受响应长度与冗余词汇干扰，无法区分逻辑错误与表面流畅。本文切入点在于将置信度视为时间信号，利用信号时序逻辑（Signal Temporal Logic, STL）挖掘区分正确与错误推理的时序模式。具体做法是构建步骤级置信度信号，通过判别式STL挖掘发现可迁移的时序结构，并利用超网络实现问题级参数自适应。该方法在单样本推理下显著提升了校准精度，但其依赖CoT分段且缺乏与语义熵方法的直接对比，泛化性存疑。

】

---

【Confidence-Aware Ranker Ensembles for Robust In-Context Knowledge Editing ｜特征加权集成检索用于鲁棒上下文知识编辑

研究机构：美国威廉与玛丽学院、美国伦斯勒理工学院

作者：Tejal Nair、Mahmud Wasif Nafee、Maiqi Jiang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b529e7047846)

> 上下文知识编辑（IKE）旨在不修改模型参数，仅通过提示注入示例来更新大语言模型的事实认知，但单一检索器在面对反事实或干扰项丰富的查询时极易因证据选择偏差而失效。现有IKE方法依赖单一检索器的表面相似度启发式，无法自适应地利用不同检索器（如语义型与词法型）的互补优势，导致在复杂查询下可靠性与局部性难以兼顾。FWE-IKE通过校准异构检索器的置信度分布，并引入基于特征加权的混合路由机制，动态选择或融合检索结果以构建更鲁棒的提示上下文。该方法在CounterFact基准上实现了88.33%的编辑成功率，显著优于单一检索器基线，但其性能仍受限于上下文窗口容量，且在单跳事实编辑上的绝对准确率远低于参数编辑方法，其长期稳定性与计算开销的平衡尚存疑。

】

---

【Confidence-Weighted Token Set Cover for Early Hypothesis Pruning in Self-Consistency ｜置信度加权集合覆盖

作者：Md Arafat Sultan、Ramón Fernandez Astudillo

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f66374f4fb0)

> 自一致性（Self-Consistency, SC）通过并行采样多数投票提升大语言模型（LLM）推理准确率，但固定生成所有路径导致Token消耗随采样数线性增长，限制了其在高延迟敏感场景下的实用性。现有串行剪枝方法虽降低Token量，却牺牲了GPU并行计算优势，导致延迟显著增加。本文提出置信度加权集合覆盖（Confidence-Weighted Set Cover, CWSC），在保持完全并行的前提下，通过每步动态剪枝低效假设，实现10-35%的Token节省。该方法在5个LLM和3个数学基准上验证了效率增益，但未突破SC的准确率上限，且剪枝对高难任务的多样性损失影响尚不明确。

】

---

【Conflicts Make Large Reasoning Models Vulnerable to Attacks ｜冲突注入与推理模型安全脆弱性

研究机构：香港科技大学、香港城市大学

作者：Honghao Liu、Chengjin Xu、Xuhui Jiang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09750)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09750)

> 大型推理模型（LRMs）在思维链（CoT）中暴露了新的攻击面，但现有越狱方法多依赖多轮交互或外部大语言模型，且缺乏对内部机制的解释。本文切入点在于利用对齐目标间的内在张力，通过单轮、非叙事的冲突注入直接瓦解安全对齐。具体做法是构造内部冲突与道德困境模板，结合层间与神经元级激活分析揭示表示干扰机制。该工作揭示了LRM安全对齐的浅层性，但其攻击效率与优化型攻击的对比缺失，且对强对齐模型的失效原因仅做了初步归因。

】

---

【Conformal Event Prediction with Temporal Knowledge Graph ｜时序事件预测中的非交换性共形预测

研究机构：中国科学院、中国科学院大学

作者：Cheng Hu、Cong Cao、Fangfang Yuan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22424bbac590)

> 事件预测旨在从历史新闻流中推断未来可能发生的事件类型，但现有方法仅输出点预测，缺乏对预测可靠性的量化，难以支撑高风险决策。标准共形预测依赖数据交换性假设，而时序知识图谱中事件间存在强时间依赖与结构关联，导致该假设失效，使得传统校准方法无法保证覆盖率。本文提出CFEP框架，通过非一致性分数扩散与效率感知优化，在违反交换性的条件下实现覆盖保证与预测集压缩。该方法在GDELT子集上显著提升了效率，但其对未见事件类型的泛化能力仍受限于预定义的事件空间。

】

---

【ConMA : Confidence-Guided Kernel Sampling with Multi-Stage Aggregation for LLM Reasoning ｜置信度引导的多阶段聚合

作者：Yinuo Wang、Qingjie Li、Wenyao Cui 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fa845c14578)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段的计算量来提升大语言模型（LLM）的复杂推理能力，但现有主流方法依赖外部验证器或一次性独立采样，导致算力分配僵化且无法复用中间高质量轨迹。本文切入点在于利用模型内部的token概率置信度作为筛选信号，构建无训练、无验证器的迭代精炼循环。具体做法是将固定预算划分为多轮“采样-过滤-扩展-选择”过程，通过动态剪枝与条件化探索实现早期收敛。该方法在4B小模型上显著提升了数学推理精度与效率，但其对复杂开放域任务的泛化能力及理论收敛边界尚存疑。

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

【Context-Value-Action Architecture for Value-Driven Large Language Model Agents ｜基于价值驱动验证器的解耦架构

研究机构：北京大学

作者：TianZe Zhang、Sirui Sun、Yuhang Xie 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05939)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05939)

> 导读 大语言模型（LLM）在模拟人类行为时普遍存在输出同质化与刻板印象问题，现有提示工程方法不仅无法缓解，反而因模型内在偏差导致行为极化。本文指出这种极化常被“LLM-as-a-judge”的主观评估所掩盖，并发现增加推理强度会进一步坍缩群体多样性。为此，作者提出上下文-价值-动作（Context-Value-Action, CVA）架构，通过独立的价值验证器解耦生成与推理过程，在真实数据基准上验证了其保真度。该架构在特定领域展现了优越性，但其对因果推断有效性的贡献仍存疑。

】

---

【ContextCheck: Sentence-Level Faithfulness Verification with Context-Aware Disambiguation ｜上下文条件化忠实度验证

研究机构：美国德克萨斯大学奥斯汀分校、美国密歇根大学

作者：Yueqin Yin、Yaxi Li、Xin Liu 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_059a03b8a380)

> 大语言模型生成的文本常因指代不明导致事实性错误，现有验证器要么孤立检查单句，要么整体处理段落，均无法在保持句子级精度的同时解决跨句指代消解。ContextCheck通过将前置句子作为条件输入直接参与验证，避免了显式去语境化重写的额外成本与误差累积。该方法在封闭域忠实度验证任务上实现了句子级精度与上下文感知的统一，但在开放域多跳推理场景下的泛化能力尚未得到验证。

】

---

【Continual Safety Alignment via Gradient-Based Sample Selection ｜基于梯度幅值的持续安全对齐样本选择

研究机构：澳大利亚迪肯大学

作者：Thong Bach、Dung Nguyen、Thao Minh Le 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17215)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17215)

> 持续微调中，模型需在适应新任务的同时保持安全对齐，但现有参数正则化或架构约束方法无法识别具体哪些样本导致对齐漂移。本文从数据层面切入，发现高梯度样本是激活“弹性回弹”、破坏安全边界的关键因素。通过筛选中梯度样本进行微调，该方法在无需额外安全数据或架构修改的前提下，显著降低了攻击成功率并维持了任务效用。其价值在于提供了低成本的训练时干预手段，但梯度幅值作为代理指标是否足以捕捉复杂的安全漂移机制，仍存疑。

】

---

【Contract-Coding: Towards Repo-Level Generation via Structured Symbolic Paradigm ｜契约编码

研究机构：北京邮电大学

作者：Yi Lin、Lujin Zhao、Yijie Shi

论文原文见 [arXiv](https://arxiv.org/abs/2604.13100)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13100)

> 意图驱动的软件工程面临模糊需求与线性推理链之间的上下文保真度权衡，导致复杂仓库生成时架构崩塌。现有多智能体框架依赖顺序对话路由，无法在有限窗口内维持全局一致性，而规格驱动方法又假设用户拥有完整蓝图。本文提出契约编码范式，通过自主符号接地将模糊意图投影为语言契约，实现模块间条件独立与并行执行。该方法在结构完整性上优于基线，但功能成功率在复杂任务上仍低于商业IDE，其自主演化机制对架构意图的控制力存疑。

】

---

【ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation ｜契约满足评估基准

研究机构：韩国延世大学

作者：Soohan Lim、Joonghyuk Hahn、Hyunwoo Park 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12047)

> 现有代码生成基准仅验证良构输入下的功能正确性，导致模型在拒绝非法输入这一关键防御机制上存在盲区。HumanEval+等基准虽标注了契约字段，却将其用于过滤违规测试而非评估拒绝行为，使得“契约满足”这一维度长期不可测。本文通过神经符号流水线生成精准违规测试，将契约满足率确立为独立评估轴。该工作揭示了当前大语言模型在边界防御上的系统性缺失，但其评估范围仍局限于函数级输入验证，未触及跨文件依赖或复杂类型系统的深层契约。

】

---

【Contrastive Decoding Mitigates Score Range Bias in LLM-as-a-Judge ｜分数范围偏差的对比解码缓解

作者：Yoshinari Fujinuma

论文原文见 [arXiv](https://arxiv.org/abs/2510.18196)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18196)

> 导读 LLM-as-a-Judge在直接评估任务中面临评分尺度不稳定的问题，现有偏差缓解方法多聚焦于位置或长度偏差，忽略了评分区间平移对模型输出的系统性干扰。本文发现LLM评判存在“分数范围偏差”，即相同内容在不同评分区间（如0-4与1-5）下相关性波动剧烈，且同家族模型共享相似的偏差模式。通过引入对比解码机制，利用同家族小模型的logit分布抵消主模型的偏差，实现了跨区间评分稳定性的提升。该策略在摘要任务上验证了推理时优化的有效性，但绝对相关性仍低于成对比较标准，且未覆盖复杂推理场景。

】

---

【CORAL: Adaptive Retrieval Loop for Culturally-Aligned Multilingual RAG ｜检索条件适配的多语言文化对齐框架

研究机构：三星研究院

作者：Nayeon Lee、Jiwoo Song、Byeongcheol Kang

论文原文见 [arXiv](https://arxiv.org/abs/2604.25676)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.25676)

> 多语言检索增强生成（mRAG）在处理文化特定查询时，常因固定检索空间导致语义相关但文化错位的证据被召回，进而生成形式正确但实质错误的回答。现有迭代检索方法仅优化查询本身，未触及语料库选择这一根本变量，使得低资源文化场景下的检索噪声无法消除。CORAL 通过 Planner-Critic 反馈循环，在测试时动态调整检索语料库范围并重写查询，将检索条件本身作为可修正的决策变量。该框架在低资源语言文化问答中实现了最高 3.58% 的准确率提升，但其效果高度依赖规划器模型的能力，且未验证在开放域生成场景中的泛化性。

】

---

【CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation ｜跨模态加权在线自蒸馏

研究机构：清华大学

作者：Jing Hu、Danxiang Zhu、Xianlong Luo 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.16547)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16547)

> 大型音频语言模型（LALM）在音频条件任务上的表现持续落后于文本条件任务，这一“文本-音频理解差距”源于现有训练范式未能有效弥合声学特征与语义空间的对齐。传统监督微调依赖昂贵标注，外部教师蒸馏存在策略外分布不匹配，且均匀KL散度忽略了推理早期关键语义偏差的累积效应。CORD提出一种无需外部教师的在线跨模态自蒸馏框架，通过加权反向KL散度与基于奖励的组相对策略优化（GRPO）在token级和序列级同步对齐音频与文本推理轨迹。该方法以80k合成数据显著缩小模态差距，但绝对性能仍低于领域SOTA，且仅在数学域验证了泛化能力。

】

---

【CoRE: A Fine-Grained Code Reasoning Benchmark Beyond Output Prediction ｜代码推理基准 CoRE：从输出预测到过程忠实

作者：Jun Gao、Yun Peng、Qian Qiao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1e462fbafd0f)

> 导读 代码生成模型在静态基准上接近满分，但“能写出正确代码”与“真正理解执行逻辑”之间存在断层。现有推理基准仅依赖单一标准实现和最终输出，无法区分深层语义推理与表面模式匹配。CoRE 通过构建功能等价但语法多样的多实现集合，并引入中间状态探针，联合评估实现不变性与过程透明度。该基准揭示了前沿模型的风格过拟合与表面执行现象，但其评估协议对探针难度的控制及跨语言泛化能力仍存疑。

】

---

【Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning ｜正确、简洁且完整：自适应推理的多阶段训练

研究机构：亚马逊网络服务人工智能

作者：Nathanaël Carraz Rakotonirina、Ren Pang、Neha Anna John 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02972)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02972)

> 导读 大语言模型在复杂推理任务中通过延长思维链（CoT）提升准确率，但常陷入“过度思考”，即生成冗余Token导致效率与准确率双输。现有方法多采用固定长度截断或静态惩罚，无法根据问题难度动态平衡精度与开销。本文提出结合监督微调（SFT）与自适应长度惩罚强化学习（RL）的多阶段框架，通过惩罚首个正确答案后的Token实现自适应精简。该方法在Qwen3-8B上减少28%响应长度且准确率仅降1.6点，但在代码与长文本任务上效率增益有限，其跨域泛化机制尚存疑。

】

---

【CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning ｜基于遗传算法的思维链自进化合成

研究机构：复旦大学、香港中文大学

作者：Zhuo Wang、Zhuo Zhang、Yafu Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14768)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14768)

> 大语言模型（LLM）在数学推理中的表现受限于高质量思维链（Chain-of-Thought, CoT）数据的稀缺与标注成本。现有蒸馏方法存在收益递减，而测试时搜索方法因采样独立性导致计算效率低下。COTEVOL将CoT合成重构为种群进化搜索问题，通过反射全局交叉与不确定性引导局部变异迭代优化推理轨迹。该方法以较低计算成本提升了合成数据的正确率，但其在小模型上的增益是否受限于骨干网络本身的推理上限，仍存疑。

】

---

【CoTJudger: A Graph-Driven Framework for Automatic Evaluation of Chain-of-Thought Efficiency and Redundancy in LRMs ｜思维链效率与冗余度图驱动评估

研究机构：中国科学技术大学、深圳大学

作者：Siyi Li、Jiajun Shi、Shiwen Ni 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07078)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07078)

> 大型推理模型（Large Reasoning Models, LRMs）在长链思维链（Chain-of-Thought, CoT）中普遍存在过度推理，导致计算资源浪费。现有基于Token计数的评估方法无法区分必要复杂度与结构性浪费，难以定位冗余来源。CoTJudger通过将有向依赖图构建于外部文本CoT之上，提取最短有效路径（Shortest Effective Path, SEP）以量化冗余。该框架提供了结构化的效率诊断信号，但其依赖大语言模型进行语义判断，可能引入新的评估偏差。

】

---

【CoTrust: Privacy-Preserving Collaboration Between Large and Small Language Models in Trusted Execution Environments ｜可信执行环境内的大小模型协同隐私推理

作者：Zhenya Ma、Tingyi Wang、Yongheng Deng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c25ad94d058)

> 导读 大语言模型（LLM）在处理含个人身份信息（PII）的用户输入时，直接部署高容量模型于可信执行环境（TEE）受限于内存与算力瓶颈，而将敏感数据暴露给外部模型则面临隐私泄露风险。现有脱敏方法通过掩码保护隐私，但往往丢弃关键语义线索，导致生成质量显著下降。CoTrust 提出一种协同推理框架，让 TEE 内的小语言模型（SLM）处理全保真输入，外部 LLM 基于多视图脱敏数据生成共识脚手架，再由 SLM 在 TEE 内实例化最终答案。该框架在保持强隐私保护的同时接近无掩码 LLM 的性能上限，但其依赖硬件信任假设，且未验证 TEE 被攻破时的鲁棒性。

】

---

【CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning ｜基于内在注意力显著性的思维链压缩

研究机构：南京大学

作者：Yangsong Lan、Hongliang Dai、Piji Li

论文原文见 [arXiv](https://arxiv.org/abs/2604.17297)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3fbdc2b93b50)

> 长思维链（Chain-of-Thought, CoT）推理在提升大语言模型复杂任务准确率的同时，引入了高昂的计算开销与延迟，核心矛盾在于如何在不损失逻辑完整性的前提下剔除冗余步骤。现有压缩方法多依赖外部代理模型评估步骤重要性，导致压缩逻辑与源模型内在推理动态脱节，常误删关键自纠正步骤。本文切入点在于发现 `</think>` 标记符的注意力分布可作为内在显著性信号，据此设计基于原子算子贪心搜索的压缩框架。该方法在7B模型上实现58%的Token缩减且准确率反超基线，但其在极高难度竞赛题上的泛化能力及贪心搜索的全局最优性仍存疑。

】

---

【Critic Rule Induction: Improving Temporal Knowledge Graph Forecasting with Generator-Critic Language Models ｜批评引导规则归纳

研究机构：美国东北大学

作者：Yingsong Ning、Fu Zhang、Jingwei Cheng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_09fe28919fc7)

> 时序知识图谱（TKG）外推推理旨在从历史观测预测未来事实，但传统规则挖掘受限于统计共现导致规则稀疏，而大语言模型（LLM）生成的规则虽具语义泛化能力却常违背时序因果。本文切入点在于将规则视为待检验的假设，通过解耦的生成-判别架构平衡覆盖率与精度。具体做法是利用LLM从历史路径抽象规则假设，再经多维事实接地评估器过滤噪声。该框架在标准基准上超越了现有SOTA，但其对离散时间戳的依赖及实体歧义处理不足，限制了其在长程连续动态场景下的适用性。

】

---

【CriticSearch: Fine-Grained Credit Assignment for Search Agents via a Retrospective Critic ｜回顾性批评家驱动的细粒度信用分配

作者：Yaocheng Zhang、Haohuan Huang、Zijun Song 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b3306c177224)

> 深度研究智能体在长程搜索任务中面临稀疏结果奖励导致的训练不稳定与策略收敛缓慢问题，现有强化学习方法难以区分轨迹内关键决策与冗余步骤。CriticSearch 引入回顾性批评家机制，利用训练时独有的金标答案与完整轨迹特权信息，对每个搜索动作进行事后评估，生成密集的回合级奖励信号。该方法将全局优势与回合级优势混合，替代传统稀疏奖励，显著提升了多跳问答任务的训练效率与最终性能。尽管在标准基准上表现优异，但其对金标答案的强依赖限制了在开放式无标准答案任务中的直接适用性。

】

---

【Cross-lingual Matryoshka Representation Learning across Speech and Text ｜跨语言语音-文本马特罗什卡嵌入模型

研究机构：法国国家科学研究中心

作者：Yaya SY、Dioula Doucouré、Christophe Cerisara 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_245261da2162)

> 低资源口语语言（如沃洛夫语）的信息检索面临双重壁垒：内容多存储于高资源语言文本中，而用户查询以语音形式存在。传统“语音识别+翻译+检索”级联流水线因误差累积和计算开销难以落地。本文切入点在于将马特罗什卡表示学习（Matryoshka Representation Learning, MRL）扩展至跨语言语音-文本检索，通过冻结文本嵌入骨干并引入轻量级语音适配器，实现无需中间文本转写的直接检索。该工作验证了晚融合架构在低资源场景下的有效性，但其对语音质量的敏感性暴露了当前MRL压缩机制在低维表示中的信息丢失问题。

】

---

【CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge ｜实时持续遗忘框架

研究机构：韩国科学技术院

作者：Seyun Bae、Seokhan Lee、Eunho Yang

论文原文见 [arXiv](https://arxiv.org/abs/2604.14644)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14644)

> 大语言模型（LLM）在部署后面临连续到达的遗忘请求，现有参数修改方法因累积误差导致效用崩溃且处理延迟高。本文提出“行为遗忘”范式，通过训练独立的句子嵌入模型拦截敏感查询，而非修改LLM权重。该方法实现了毫秒级响应与近乎完美的知识保留，但仅抑制输出而未擦除内部知识，其对抗鲁棒性存疑。

】

---

【Curriculum Learning based Hierarchical Scoring and Analysis Framework for Question Answering Task Evaluation ｜课程学习层级化问答评估框架

研究机构：北京大学、新加坡国立大学

作者：Qiong Wu、Tan Yue、Jianxin Liang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f6d62580fd63)

> 大语言模型在问答任务中的评估面临成本高昂与错误诊断缺失的双重困境，现有规则匹配方法语义理解不足，而通用大模型评判器虽准确但延迟高且无法定位具体错误类型。HiEval 通过两阶段课程学习训练一个 4B 参数的小模型，先掌握三级评分能力，再扩展至五类错误归因，以零 API 成本和 25 倍于 GPT-5 的推理速度实现了超越大模型的细粒度诊断精度。该框架验证了小模型在特定评估子任务上替代大模型的可行性，但其泛化边界与标注一致性仍需更严格的跨域验证。

】

---

【D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation ｜大规模SFT模型增量参数压缩

研究机构：哈尔滨工业大学、香港理工大学

作者：Junlin Li、Shuangyong Song、Guodong Du 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16940)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16940)

> 多模型部署场景下，存储全量微调模型导致内存开销呈线性增长，增量压缩旨在仅存储基座模型与压缩后的差值（Delta）以解决此问题。现有方法在处理大规模数据微调产生的高幅度Delta参数时，因量化误差与低秩近似误差随数值尺度放大而失效。本文提出D-QRELO，通过先进行1-bit量化缩小残差数值范围，再对残差执行SVD低秩近似，实现训练与数据无关的压缩。该方法在强SFT模型上显著优于基线，但其压缩率存在物理下限，且对早期层敏感性的处理尚未完全解决。

】

---

【Data Selection for Multi-turn Dialogue Instruction Tuning ｜多轮对话指令微调的数据选择

研究机构：北京大学

作者：Bo Li、Shikun Zhang、Wei Ye

论文原文见 [arXiv](https://arxiv.org/abs/2604.07892)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07892)

> 导读 多轮对话指令微调面临的核心矛盾是：大规模对话语料虽能提供丰富的交互轨迹，但其中充斥着主题漂移、重复闲聊及格式错配等结构性噪声，直接训练会损害模型在长对话中的连贯性与任务执行能力。现有单轮数据选择方法将对话拆解为独立指令对，忽略了跨轮次的语义依赖与结构完整性，导致筛选出的子集在长对话场景下表现退化。本文提出 MDS（Multi-turn Dialogue Selection），通过全局语义覆盖与局部结构可靠性的两阶段联合优化，在固定预算下筛选出既多样又结构完整的多轮对话子集。该方法在通用与领域特定语料上均优于单轮选择器及对话级评分基线，但其对分箱数量敏感性及跨域泛化边界的量化验证仍显不足。

】

---

【Data-Centric Continual Pre-training for 500+ Languages: A New Bilingual Translation Corpus and Multilingual Models ｜大规模多语言持续预训练中的双语平行语料效能

研究机构：芬兰图尔库大学、芬兰赫尔辛基大学

作者：Shaoxiong Ji、Zihao Li、Jaakko Paavola 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_20dbcac609a8)

> 多语言大语言模型在低资源语言上性能稀释，源于预训练数据分布不均与分词器碎片化。现有持续预训练（Continual Pre-training, CPT）方法多依赖单语数据，缺乏对平行语料贡献的量化评估，导致高资源语言遗忘与低资源提升的权衡机制不明。本文构建覆盖2500+语言对的双语翻译语料MaLA，通过消融实验验证双语数据在大规模CPT中的具体增益。该工作证实了平行数据对翻译任务的显著优势，但暴露了高资源语言性能下降的结构性矛盾，其全参数训练的高算力门槛限制了社区部署的可行性。

】

---

【Data-Centric Perspectives on Agentic Retrieval-Augmented Generation: A Survey ｜智能体检索增强生成的数据生命周期

研究机构：北京大学

作者：Jingwen Deng、Jihao Huang、Zhen Hao Wong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5272b768a4fd)

> 智能体检索增强生成（Agentic RAG）旨在让大语言模型（LLM）通过多步推理与工具调用主动获取外部知识，以突破静态检索增强生成（RAG）在复杂任务上的局限。然而，该领域面临的核心瓶颈并非算法设计，而是缺乏包含规划、检索与多步决策的高质量交互式轨迹数据，现有静态语料无法支撑此类模型的训练与评估。本文从数据工程视角切入，系统梳理了从数据收集、任务构建到评估与训练增强的完整生命周期，提出了“生成-验证-过滤/精炼”管道及难度增强框架。这一工作为构建可扩展的智能体搜索基准提供了方法论基础，但其对数据质量指标的量化验证仍显不足，且未直接解决长程任务中的信用分配难题。

】

---

【Data-Efficient Adaptation to Contextual Shifts in LLM-based Conversational Recommendation ｜上下文漂移下的数据高效适配

作者：Hyeongjun Yang、Donghyun Kim、Seokju Hwang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_40f301419265)

> 对话推荐系统（CRS）在语言与社会趋势演变后，其冻结模型生成的推荐往往偏离当前用户偏好，而全量微调成本高昂且包含大量冗余样本。现有数据选择方法无法区分“模型已掌握”的熟悉样本与“真正需要学习”的有价值样本，导致在分布偏移场景下筛选失效。本文提出CAPT框架，通过训练损失与代理损失的比值量化样本可学习性，并结合损失加权训练策略，以10–50%的数据实现超越全量微调的性能。该框架在时序分割基准上验证了有效性，但其对非时序漂移（如用户个体偏好突变）的泛化能力尚未被检验。

】

---

【Datamart-Agent: LLM-Driven Game-Theoretic Agent for Data Marketplace Modeling ｜数据市场均衡一致性建模

研究机构：香港理工大学

作者：Pangjing Wu、Peter Q. Chen、Xiaodong Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed702225f89d)

> 数据市场研究长期受限于静态完全信息假设，难以刻画动态演化与买方估值不完全信息下的真实博弈。现有基于强化学习或静态提示的大语言模型（LLM）代理在缺乏参数更新的情况下，难以在解析均衡真值上实现策略一致性。本文提出EvoDM框架与Datamart-Agent，通过动态博弈树记忆与机制引导反思，在无参数更新条件下执行均衡一致决策。该工作验证了非训练式LLM代理在复杂市场模拟中的有效性，但其泛化边界与长程依赖处理能力仍存疑。

】

---

【DataSage: Multi-agent Collaboration for Insight Discovery with External Knowledge Retrieval, Multi-role Debating, and Multi-path Reasoning ｜数据洞察智能体：多角色辩论与外部知识检索

作者：Xiaochuan Liu、Yuanfeng Song、Xiaoming Yin 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.14299)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.14299)

> 数据科学智能体旨在自动化从数据清洗到洞察生成的全生命周期工作流，其核心价值在于突破传统自动机器学习仅能处理预定义管道的局限。现有问答式智能体受限于领域知识缺失、分析深度不足及代码生成易错，难以产出可行动的商业洞察。DataSage 通过引入检索增强知识生成、多角色辩论问题生成及多路径代码推理，构建了迭代式问答闭环。该框架在 InsightBench 上显著优于基线，但其对结构化表格数据的依赖及外部检索的实时性约束，限制了其在异构数据环境下的泛化能力。

】

---

【DataSeer: A Manager-Centric Collaborative Multi-Agent Framework with Multi-Branch Reasoning for Automated Insight Discovery ｜DataSeer：面向自动化洞察发现的管理者中心多智能体框架

研究机构：北京大学

作者：Suchen Liu、Yuanfeng Song、Jun Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_af490e56fb73)

> 导读 数据科学智能体（Data Science Agents, DSA）旨在利用大语言模型（LLM）自动化从数据清洗到洞察生成的全生命周期工作流，其核心价值在于突破传统自动机器学习（AutoML）仅能处理预定义管道的局限。现有单体智能体在长链推理中易出现上下文碎片化与记忆衰减，且固定规划模板难以适应动态探索，导致洞察覆盖度受限。DataSeer 通过引入管理者中心协作框架与多分支推理机制，解决跨回合连贯性与单路径随机性问题。该框架在开放式洞察发现任务上显著优于基线，但其确定性调度策略对突发数据异常的自适应能力仍存疑。

】

---

【Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate ｜基于两阶段多智能体辩论的可靠实体对齐框架

作者：Cunda Wang、Ziying Ma、Po Hu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_60121fdb2f97)

> 实体对齐（Entity Alignment, EA）旨在识别不同知识图谱（KG）中指向同一现实世界对象的实体，其核心难点在于跨库异构性导致的语义歧义。现有基于大语言模型（LLM）的方法虽提升了语义理解能力，但受限于单次推理的不可逆性与候选检索的上限约束，难以在复杂歧义场景下保证决策可靠性。AgentEA 通过引入直接偏好优化（DPO）增强嵌入判别力，并设计轻量级辩论验证与深度辩论对齐的两阶段多智能体机制，实现了决策透明化与效率平衡。该框架在跨语言基准上达到了 SOTA 水平，但其对闭源模型的依赖及辩论轮次的固定设置，限制了其在零样本泛化场景下的适用性评估。

】

---

【Decide less, communicate more: On the construct validity of end-to-end fact-checking in medicine ｜医疗事实核查的构造效度危机：从端到端分类到交互式对话

作者：Sebastian Antony Joseph、Lily Chen、Barry Wei 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2506.20876)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5e6e6a86997e)

> 自动化事实核查（Automated Fact-Checking, AFC）旨在通过算法替代人工，解决海量医疗错误信息验证效率低下的问题。现有基于大语言模型（LLM）与检索增强生成（RAG）的端到端范式假设声明可被直接映射为“支持/反驳”标签，却忽视了真实社交媒体中声明的语境缺失与证据不可得性，导致系统在临床场景中失效。本文通过专家标注研究揭示医疗声明验证的构造效度缺陷，主张将事实核查重构为交互式对话过程，以澄清意图并处理不可验证性。该视角挑战了领域对“准确率”的单一追求，但缺乏自动化系统的性能验证，其理论价值高于工程落地性。

】

---

【Deciphering Cultural Representations in Large Language Models via Sparse Autoencoders ｜稀疏自编码器解耦文化表征

研究机构：阿联酋扎耶德大学、加拿大多伦多大学

作者：Chenye Zou、Difan Jiao、Lijie Hu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c0b13653ffe)

> 大语言模型内部的文化知识长期被多义神经元纠缠，导致无法区分深层价值观与表面词汇线索。现有神经元定位方法受限于叠加效应，难以实现精准干预。本文利用稀疏自编码器将激活分解为单义特征，通过因果消融验证其必要性，并证明定向引导可无重训练地调制文化行为。该工作提供了从机制解释到可控干预的闭环，但受限于特定模型架构与静态数据集，其结论在动态文化语境下的泛化性存疑。

】

---

【Decomposed Trust: Privacy, Adversarial Robustness, Ethics, and Fairness in Low-Rank LLMs ｜低秩分解对大语言模型可信度的解耦分析

研究机构：美国爱荷华州立大学

作者：Daniel Agyei Asante、Md Mokarram Chowdhury、Yang Li

论文原文见 [arXiv](https://arxiv.org/abs/2511.22099)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.22099)

> 大语言模型（LLM）在资源受限场景下的部署依赖低秩分解等压缩技术，但现有研究仅关注压缩后的性能保持，忽视了压缩对模型安全属性的潜在破坏。本文切入点在于首次系统量化低秩分解在隐私、对抗鲁棒性、伦理和公平四个维度的副作用，通过多模型、多压缩算法的对比实验揭示压缩与可信度的非正交关系。其价值在于填补了压缩评估中“可信度”维度的空白，但实验局限于特定骨干网络与压缩率区间，未提供可信度感知的压缩优化策略。

】

---

【Decomposing Unitization and Typing for Efficient and Consistent Span-Bound Concept Annotation ｜概念标注任务分解

研究机构：美国卡内基梅隆大学、美国芝加哥大学

作者：Nupoor Gandhi、Michael Bada、Emma Strubell

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d8a911f4251)

> 领域专家标注面临高昂的时间成本与标注者间一致性瓶颈，传统全跨度标注将语义判断与语言学边界选择耦合，导致低资源场景下数据量受限。现有LLM辅助标注方案多直接生成完整实体，但在专业领域少样本性能不足，且未解决边界决策的主观性噪声。本文提出将标注解耦为“类型位置标注”与“跨度边界检测”，由人工仅标记位置，模型推断边界。该策略在低预算下显著提升了数据效用与一致性，但其收益高度依赖跨度检测模型的准确率，高预算场景下优势消失。

】

---

【Decoupling the Effect of Chain-of-Thought Reasoning: A Human Label Variation Perspective ｜长思维链在人类标签变异任务中的分布校准失效分析

研究机构：德国慕尼黑大学、英国剑桥大学

作者：Beiduo Chen、Tiancheng Hu、Caiqi Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03154)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5193cb02af2e)

> 长思维链推理旨在通过中间步骤提升模型在多步任务上的性能，但其在需要捕捉概率性歧义而非消除歧义的任务中表现如何尚不明确。现有评估多聚焦于单一正确答案的准确率，忽视了模型输出分布与人类集体判断分布的对齐程度，导致无法区分CoT是真正驱动了推理还是仅作为事后合理化。本文通过交叉CoT注入与逐步方差分解实验，量化了CoT内容与模型内在先验对最终答案准确率及分布结构的独立贡献。研究揭示了CoT作为“决策器”而非“校准器”的结构性局限，为理解推理模型在模糊任务中的行为边界提供了实证依据，但其结论是否适用于非选择题的开放式生成场景仍存疑。

】

---

【DeepPlanner: Scaling Planning Capability for Deep Research Agents via Advantage Shaping ｜深度规划器：通过优势整形扩展深度研究智能体的规划能力

研究机构：香港科技大学、美国加州大学圣迭戈分校

作者：Wei Fan、Wenlin Yao、Zheng Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12979)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12979)

> 深度研究智能体在长程任务中常因规划阶段的不确定性而陷入执行漂移，现有强化学习方法难以将规划阶段的高熵转化为性能提升。本文指出规划Token在训练中持续保持高熵，表明其优化潜力未被挖掘。DEEPPLANNER通过熵基优势整形与选择性优势加权，在更少训练资源下实现了SOTA性能。其价值在于证明了针对性优势整形比单纯扩大数据规模更有效，但评估局限于多跳问答，未验证在开放式报告生成中的泛化性。

】

---

【DeepPrune: Parallel Scaling without Inter-trace Redundancy ｜跨轨迹冗余剪枝

研究机构：清华大学、上海科技大学

作者：Shangqing Tu、Yaxuan Li、Yushi Bai 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08483)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08483)

> 并行推理扩展旨在通过生成多条思维链（Chain-of-Thought, CoT）提升大语言模型（LLM）的推理准确率，但现有方法忽略了轨迹间的答案同质性，导致大量算力浪费在生成等价路径上。本文指出约80%的并行轨迹最终答案相同，且浅层语义相似度无法有效预测这种等价性。DeepPrune通过训练专用裁判模型预测未完成轨迹的答案等价性，结合在线贪心聚类动态剪枝冗余路径，在保持准确率的前提下大幅降低Token消耗。该方法在效率维度实现了显著突破，但其对可验证任务域的依赖及裁判模型的泛化边界仍存疑。

】

---

【DeepSynth-Eval: Objectively Evaluating Information Consolidation in Deep Survey Writing ｜深度合成评估基准

作者：Hongzhi Zhang、Yuanze Hu、Tinghai Zhang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_07078d88d367)

> 深度研究智能体（Deep Research Agents, DRA）的核心瓶颈已从信息检索转移至海量证据的结构化整合，但现有评估体系因混淆检索噪声与合成能力、依赖主观评分而失效。本文通过逆向工程高质量综述，构建隔离检索的“Oracle Context”与细粒度清单指标，将开放式报告评估转化为可验证的客观任务。实验表明，多轮智能体工作流显著优于单轮生成，但百篇级文献的综合仍是当前模型的硬瓶颈。该基准填补了“检索后合成”的评估空白，但其封闭世界设定是否高估了开放环境下的真实能力，尚存争议。

】

---

【Defending LLMs against Jailbreak Attacks via Template-Based ICL with a Defensive Suffix ｜基于模板化上下文学习与防御后缀的大语言模型越狱防御

作者：Ruiyang Ni、Changlong Li、Shuaibiao Han 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7df65f69e909)

> 大语言模型（LLM）在部署中面临越狱攻击，现有防御方法在优化类与查询类攻击间难以兼顾，且常伴随高计算成本或效用损失。本文切入点在于利用LLM的上下文学习（In-Context Learning, ICL）能力与离线优化的防御后缀，构建一种轻量级、即插即用的混合防御机制。该方法通过离线训练鲁棒后缀抵御梯度优化攻击，并在推理时通过随机搜索筛选ICL演示以应对语义连贯的查询攻击。其价值在于以极低的额外开销实现了跨白盒与黑盒场景的广泛防御，但其对推理模型及多模态场景的泛化能力尚未验证。

】

---

【Demystify the Role of Memory in Machine Learning Engineering Agents ｜机器学习工程智能体中的动态编码记忆：架构依赖性与探索-利用权衡

研究机构：美国北卡罗来纳大学教堂山分校

作者：Xinyu Zhao、Junpeng Wang、Yuzhong Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18671558eeed)

> 机器学习工程（Machine Learning Engineering, MLE）智能体在自动化数据科学工作流中常陷入重复错误循环，导致搜索效率低下。现有通用对话记忆系统无法适配代码调试的结构化特性，且未揭示记忆对不同搜索架构的差异化影响。本文提出任务-包粒度的动态编码记忆，将其集成至链式与树式两种智能体范式，实证了记忆对链式智能体可靠性的提升及对树式智能体探索多样性的抑制。该研究揭示了记忆作为“双刃剑”的架构依赖性，但缺乏对记忆强度动态调节的机制设计，其结论在更复杂的多任务迁移场景中是否普适仍存疑。

】

---

【Detecting Sensitive Personal Information in Japanese Pre-Training Corpora for Large Language Models ｜日语预训练语料敏感个人信息检测

作者：Rei Minamoto、Yusuke Oda、Daisuke Kawahara

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0b732bebe3b7)

> 大规模日语预训练语料中混杂着受法律严格保护的敏感个人信息，若未过滤将导致模型记忆并泄露此类数据，引发合规风险。现有PII过滤工具仅能识别姓名、地址等基础标识符，无法捕捉医疗、犯罪等需结合语境判断的敏感属性，导致合规过滤存在盲区。本文提出基于两阶段大语言模型标注构建数据集，并训练轻量级分类器实现高效SCPI检测。该方法在日语语料上实现了高精度过滤，但受限于数据规模与类别覆盖，其泛化能力与跨语言适用性仍存疑。

】

---

【Diagnosing and Mitigating Sycophancy and Skepticism in LLM Causal Judgment ｜递归因果审计（RCA）：诊断LLM因果判断中的输出层偏差

研究机构：美国斯坦福大学

作者：Edward Y. Chang

论文原文见 [arXiv](https://arxiv.org/abs/2601.08258)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08258)

> 大语言模型（LLM）在因果推理任务中常表现出“因果鹦鹉”现象，即依赖统计模式而非结构推理，导致在干预和反事实层级上性能断崖。现有基准测试多聚焦于最终答案的正确性，却混淆了真实推理能力与拒绝、对冲及压力诱导的漂移，使得难以区分模型是“不知道”还是“不敢说”。本文提出递归因果审计（RCA），一种无金标访问的过程完整性评估器，通过验证模型最终标签是否由其自身推导轨迹所蕴含，来隔离输出层偏差。该框架揭示了“怀疑陷阱”与“规模悖论”，证明推理时验证可显著改善操作点，但其能否真正内化因果结构仍存疑。

】

---

【DIFFA-2: A Practical Diffusion Large Language Model for General Audio Understanding ｜扩散大语言模型音频理解框架

作者：Jiaming Zhou、Xuxin Cheng、Shiwan Zhao 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4039d8fbe3e0)

> 音频语言模型（ALM）旨在通过自然语言接口统一音频理解、推理与生成任务，其核心价值在于突破单一模态音频处理的局限。现有主流自回归（AR）架构在数据效率与推理延迟上存在瓶颈，而早期扩散模型验证了非自回归范式的潜力但缺乏实用规模。本文提出 DIFFA-2，通过双适配器与四阶段训练将扩散骨干转化为实用音频模型。该工作证明了低参数更新下扩散架构的竞争力，但其对长序列时序依赖的建模能力仍存疑。

】

---

【DiffCoT: Diffusion-styled Chain-of-Thought Reasoning in LLMs ｜扩散式思维链推理

研究机构：香港浸会大学、哈尔滨工业大学

作者：Shidong Cao、Hongzhan Lin、Yuxuan Gu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_80fead884c59)

> 导读 思维链（Chain-of-Thought, CoT）推理在提升大语言模型数学解题能力的同时，因自回归解码的不可逆性导致早期错误沿链条累积，严重削弱推理鲁棒性。现有偏好优化方法仅做局部步级对齐，无法在推理时回溯修正已生成的错误前缀，暴露偏差问题依然突出。本文提出 DIFFCOT，将 CoT 重构为步级迭代去噪过程，通过滑动窗口与因果噪声调度统一生成与修正。该方法在 GSM8K 和 MATH 高难度子集上显著优于现有偏好优化基线，但其性能增益高度依赖骨干模型能力，且未解决离散 Token 表达瓶颈这一根本限制。

】

---

【DiffER: Diffusion Entity-Relation Modeling for Reversal Curse in Diffusion Large Language Models ｜扩散大语言模型中的反转诅咒与实体关系建模

研究机构：重庆大学、清华大学

作者：Shaokai He、Kaiwen Wei、Xinyi Zeng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_61fecc743636)

> 扩散大语言模型（DLLM）虽具备双向注意力架构，理论上应能克服自回归模型的方向性偏差，但在处理逻辑双向关系时仍表现出严重的“反转诅咒”，即从 A→B 推理到 B→A 时性能骤降。现有研究多将此归因于自回归训练机制，忽视了扩散模型特有的去噪过程对实体完整性的破坏以及数据分布的固有偏斜。本文通过系统实验定位了实体碎片化、数据不对称与关系稀疏三大根因，并设计了全实体掩码、对称对齐与逆关系建模三位一体的后训练框架 DiffER。该框架在 PORE 基准上显著提升了双向推理准确率，但其有效性依赖于结构化三元组数据的可构造性，在大规模非结构化语料中的泛化能力尚存疑。

】

---

【DiffuSpec: Unlocking Diffusion Language Models for Speculative Decoding ｜扩散语言模型投机解码框架

研究机构：清华大学、南方科技大学

作者：Guanghao Li、Zhihui Fu、Min Fang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02358)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02358)

> 自回归解码的串行瓶颈长期依赖轻量级自回归草稿模型缓解，但草稿阶段本身的串行前向传播限制了并行验证的收益上限。现有无训练方案受限于草稿生成吞吐量或分布对齐精度，而扩散语言模型（DLM）虽能单次前向生成多token块，却因双向条件生成导致局部最优token无法构成因果一致路径，且固定草稿长度引发速度-质量权衡失衡。DiffuSpec通过因果一致性路径搜索（CPS）在DLM生成的token格子上提取左到右最优路径，并结合自适应草稿长度（ADL）控制器动态调整块大小，实现了无需训练的即插即用加速。该框架在Spec-Bench上取得3.08x加速比，接近训练式方法，但其性能上限是否受限于DLM本身的推理延迟而非验证阶段，论文未给出明确归因。

】

---

【Direct Token Optimization: A Self-contained Approach to Large Language Model Unlearning ｜直接Token优化

研究机构：美国埃默里大学

作者：Hong kyu Lee、Ruixuan Liu、Li Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2510.00125)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00125)

> 大语言模型（LLM）在微调阶段极易记忆特定数据，导致隐私泄露与版权风险，而完全重训练成本过高。现有无保留集遗忘方法如FLAT仅引导模型生成拒绝回答，未能触及知识存储的核心Token，导致遗忘质量低下。本文提出直接Token优化（DTO），通过Delta-score自主识别关键知识Token并执行梯度上升，同时利用KL散度约束非目标Token以维持效用。该方法在TOFU基准上实现了极高的遗忘质量，但其对长距离依赖知识的覆盖能力及对抗鲁棒性仍存疑。

】

---

【DiSec: Mitigating Backdoors in Pre-trained Language Models via Disentanglement of Adversarial Weights for Secure Fine-Tuning ｜预训练语言模型后门净化：基于梯度残差解耦的权重修正

研究机构：美国阿肯色大学

作者：Sunanda Das、Qinghua Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd850f9bb64f)

> 预训练语言模型（Pre-trained Language Models, PLMs）在供应链分发中面临任务无关后门威胁，即攻击者在预训练阶段植入触发器，导致模型在下游微调后仍保留恶意行为。现有防御方法多依赖下游标签或干净参考模型，无法在真实部署场景中独立净化被污染的预训练检查点。DiSec 利用无标签辅助文本计算梯度残差，通过奇异值分解（SVD）与变分自编码器（VAE）联合检测异常权重行，并采用层内原型均值修正替代剪枝，在无需下游监督的情况下抑制攻击成功率。该方法在 BERT 和 RoBERTa 上实现了效用保持与攻击抑制的平衡，但其对非线性复杂后门结构的鲁棒性及在生成式大语言模型上的泛化能力仍存疑。

】

---

【Disentangling Codemixing in Chats: The NUS ABC Codemixed Corpus ｜关系亲密度驱动的代码切换语料库构建与语言适应分析

研究机构：新加坡国立大学

作者：Svetlana Churina、Akshat Gupta、Nur Insyirah Binte Imam Mujtahid 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ee2411098bc6)

> 代码切换（Code-Switching, CS）研究长期受限于真实多语对话数据的稀缺与标注维度的单一，现有语料库多聚焦于单一语言对或缺乏社会心理元数据，导致模型难以捕捉语言混合背后的关系动态。本文切入点在于构建首个包含信任与自我披露维度的多语即时消息语料库，通过志愿者捐赠获取真实对话，并整合语言识别、翻译与混合效应回归分析。其价值在于将CS从纯语言学现象拓展至社会情感计算领域，但非英语token识别准确率偏低限制了下游任务的直接可用性。

】

---

【Distilling LLM Reasoning into Dense Encoders: Bridging the Accuracy-Efficiency Gap in Recommendation ｜推理至编码器蒸馏

作者：Donghee Han、Daeyoung Roh、A Young Kim 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_38c751571e07)

> 大语言模型（LLM）在推荐系统中具备强大的语义推理能力，但其自回归生成机制导致推理延迟高企，难以满足工业级实时性要求。现有蒸馏路线要么将推理压缩至小语言模型（SLM）保留生成能力但牺牲速度，要么压缩至传统推荐模型（CRM）提升速度但丢失推理深度。本文提出推理至编码器蒸馏（Reasoning-to-Encoder Distillation, R2END），通过将LLM对齐后的推理语义压缩至轻量级文本编码器的稠密向量空间，在消除推理阶段LLM依赖的同时保留推理本质。该架构在精度与延迟间实现了显著折中，但其对“向量压缩等效于显式推理”的假设在复杂多跳场景下的有效性尚存疑。

】

---

【Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding ｜协同推理解码

研究机构：韩国科学技术院

作者：Taewon Yun、Jisu Shin、Jeonghwan Choi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.02290)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.02290)

> 多教师推理蒸馏旨在将大型推理模型（LRM）的长思维链（Long-CoT）能力迁移至小模型，但现有“生成-选择”范式因事后评估无法动态利用异构教师的互补性，导致计算浪费与推理路径单一。CoRD 将蒸馏重构为步级协同解码过程，通过预测困惑度评分与束搜索，让多个教师在解码过程中逐步提议并融合推理步骤。该方法在 AIME25 上使 32B 学生模型超越所有单一教师，但步级分割对长程依赖的破坏及与在线策略蒸馏的兼容性仍存疑。

】

---

【Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation ｜序列截断下的推理蒸馏效率优化

研究机构：加拿大不列颠哥伦比亚大学

作者：Wei-Rui Chen、Vignesh Kothapalli、Ata Fatahibaarzi 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21002)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21002)

> 推理知识蒸馏旨在将大型推理模型的逻辑能力迁移至小模型，但长思维链（Long-CoT）带来的训练计算开销成为部署瓶颈。现有离线蒸馏方法默认使用全序列监督，忽视了序列内部信号分布的不均匀性，导致大量算力浪费在冗余token上。本文提出LeadSpan Proportion (LSP) 动态截断协议，通过仅保留训练序列前50%的token，在数学基准上保留了约91%的准确率，同时将训练时间与显存占用降低约50%。这一发现挑战了“全序列监督最优”的默认假设，但其结论是否适用于非数学领域及跨模型家族蒸馏，仍存疑。

】

---

【Distribution Shift Alignment Helps LLMs Simulate Survey Response Distributions ｜分布偏移对齐

研究机构：中国科学技术大学、复旦大学

作者：Ji Huang、Mengfei Li、Shuai Shao

论文原文见 [arXiv](https://arxiv.org/abs/2510.21977)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21977)

> 大规模社会调查面临高昂成本与隐私瓶颈，利用大语言模型（LLM）模拟人类响应成为替代方案，但现有方法受限于训练数据分布，无法超越数据本身的上限。本文指出LLM虽无法精准预测绝对分布，但能有效捕捉不同背景间的相对偏好差异。通过两阶段微调对齐分布偏移，DSA实现了比训练集更准确的分布估计。该方法在数据效率上表现突出，但其对背景独立性的强假设限制了在复杂交互场景下的适用性。

】

---

【Distributional Alignment for Large Language Models under Domain Shift ｜基于证据检索与价值签名的分布对齐

研究机构：澳大利亚莫纳什大学

作者：Viet Thanh Pham、Lizhen Qu、Zhuang Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f8b98d03f88)

> 分布对齐旨在让大语言模型预测目标群体在多选题上的回答分布，而非输出单一共识答案。现有方法如Token概率估计对选项措辞敏感，直接生成分布则常因表面形式锚定而校准失效，尤其在跨文化域偏移下表现脆弱。Evi-DA通过检索世界价值观调查（WVS）中的相似问题分布作为证据，并预测选项的Welzel价值签名，实现结构化两阶段推理。该方法在域内和域外基准上显著降低了预测分布与真实分布的Jensen-Shannon Divergence (JSD)，但其效果高度依赖骨干模型的推理能力，小模型在强化学习后性能反而退化。

】

---

【Divergent Thinking: Escape the Homogeneity Trap in Generative Commonsense Reasoning ｜生成式常识推理中的同质化陷阱与探索-整合框架

研究机构：北京大学、哈尔滨工业大学

作者：Yiheng Tao、Kaiwen Cheng、Zhiwei Nie 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4152089f06d5)

> 导读

】

---

【DKME: Rethinking Coupled Knowledge Memory for Lifelong Model Editing of Large Language Models ｜解耦知识记忆编辑

研究机构：华南理工大学、哈尔滨工业大学

作者：Guanyu Zheng、Wang Zhenyu、He Tingting 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb7206685cc2)

> 终身知识编辑旨在向大语言模型（LLMs）持续注入事实更新而不触发重训练，但现有记忆基方法在编辑累积时普遍遭遇灾难性遗忘。本文指出其根源在于寻址（路由）与存储（写入）机制的耦合，导致跨编辑干扰随规模放大。DKME通过事实感知语义寻址与分区记忆存储两阶段解耦，将更新限制在独立参数子空间。该方法在多域与关联事实基准上实现了更优的可靠性-局部性平衡，但其分区粒度依赖无监督聚类，对长尾知识的覆盖能力存疑。

】

---

【Do Emotions Influence Moral Judgment in Large Language Models? ｜情感诱导对大语言模型道德判断的因果影响

作者：Mohammad Saim、Tianyu Jiang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_811d48afa62b)

> 现有道德推理评估基准普遍假设情感中性，忽视了情感作为启发式信号对道德判断的系统性扭曲。本文通过构建受控情感诱导框架，量化了情感效价对模型道德可接受性评分的因果影响，并揭示了模型与人类在情感响应机制上的根本差异。该工作证实了当前大语言模型存在显著的情感-道德对齐缺口，但其结论局限于单语言静态文本场景，未探究情感偏移的微观神经机制。

】

---

【Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microeconomic Behaviors in Macro-ABMs ｜基于因果图推理的宏观经济模拟微观基础校准

研究机构：同济大学

作者：Guangya Liu、Cheng Wang、Jiangtong Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec95e62fe1ba)

> 宏观经济代理模型（ABM）长期依赖聚合指标复现风格化事实，却忽视了微观决策与真实人类行为的对齐验证，导致模拟结果在政策分析中缺乏可靠性。现有LLM代理直接映射宏观指标至微观决策，存在趋势响应弱、群体异质性坍缩及数据泄露三大缺陷，传统提示工程无法解决其内在因果机制缺失的问题。本文提出异质性冲击-响应因果传输框架（HSRCT），通过构建文献验证的中介-调节因果图并执行强度引导路径搜索，将宏观冲击转化为显式推理链。该方法在微观趋势对齐与宏观模拟保真度上均优于纯模型规模扩展，但其因果图构建依赖LLM生成，结构无偏性尚未得到独立验证。

】

---

【Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models ｜大语言模型基础算术中的过度思考与效率-准确率权衡

研究机构：美国弗吉尼亚理工大学

作者：Gaurav Srivastava、Aafiya Shamshad Hussain、Sriram Srinivasan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ca960cba766a)

> 大语言模型在复杂数学基准上表现优异，却在基础算术任务中生成冗余推理链且准确率不升反降，这一现象被称为过度思考（Overthinking）。现有评估体系将准确率与计算效率视为独立维度，无法量化二者间的根本权衡，导致部署场景下的计算浪费被忽视。本文提出基于调和平均的过度思考分数（Overthinking Score），结合动态生成的14类确定性算术任务，系统评估53个模型在准确率与Token效率间的平衡能力。该工作填补了推理效率量化评估的空白，但其结论局限于基础算术任务，对复杂推理场景的普适性存疑。

】

---

【Do LLMs Really Know What They Don’t Know? Internal States Mainly Reflect Knowledge Recall Rather Than Truthfulness ｜知识召回与真实性解耦：基于因果干预的幻觉机制分类

研究机构：新加坡管理大学、阿里巴巴集团

作者：Chi Seng Cheang、Hou Pong Chan、Wenxuan Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fcad53c20df0)

> 大语言模型（LLMs）的幻觉检测长期依赖内部状态反映事实准确性的假设，但这一假设在模型利用统计捷径生成错误内容时失效。现有表征探针无法区分源于知识缺失的幻觉与源于错误关联的幻觉，导致安全监控在高频实体上出现系统性漏报。本文通过阻断注意力流的因果干预，将幻觉细分为关联幻觉（Associated Hallucinations, AHs）与非关联幻觉（Unassociated Hallucinations, UHs），揭示内部表征主要编码知识召回过程而非真实性。该工作挑战了线性可分性共识，但仅验证了单轮静态问答场景，未解决动态交互中的策略性误导问题。

】

---

【Do Personality Traits Interfere? Geometric Limitations of Steering in Large Language Models ｜人格特质干扰：大语言模型中转向的几何局限

研究机构：澳大利亚西澳大学、澳大利亚麦考瑞大学

作者：Pranav Bhandari、Usman Naseem、Mehwish Nasim

论文原文见 [arXiv](https://arxiv.org/abs/2602.15847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15847)

> 大语言模型（LLMs）的人格控制旨在通过内部表示干预实现特定特质的稳定表达，但现有激活工程方法隐含假设人格特质在激活空间中是线性独立的。这一假设导致在操纵单一特质时，其他特质发生不可预测的漂移，且强制正交化虽能消除几何重叠，却以牺牲生成流畅度为代价。本文通过系统分析 Big Five 人格转向向量的几何关系，并测试从软白化到硬正交化的多种约束策略，揭示了特质间存在持久的行为耦合，证明几何独立性并非行为独立性的充分条件。该研究挑战了“正交即解耦”的直觉，但受限于仅使用两个模型家族和 LLM 裁判评估，其结论的普适性仍需更多验证。

】

---

【Do We Always Need Query-Level Workflows? Rethinking Agentic Workflow Generation for Multi-Agent Systems ｜任务级工作流生成的低成本评估框架

研究机构：中国科学院、中国科学院大学

作者：Zixu Wang、Bingbing Xu、Yige Yuan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11147)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11147)

> 多智能体系统（MAS）的工作流生成面临高昂的计算开销，任务级方法需对每个候选工作流执行全量验证集评估，而查询级方法则为每个输入生成独立工作流，两者均存在显著的资源浪费。本文指出，任务级方法中全量执行评估既昂贵又不可靠，且查询级生成并非总是必要。SCALE 框架通过引入“自预测+少样本校准”机制替代全量执行，在保持性能的同时大幅降低 Token 消耗。该研究揭示了现有评估范式的低效性，但其结论是否适用于所有任务分布仍需进一步验证。

】

---

【Do We Need Distinct Representations for Every Speech Token? Unveiling and Exploiting Redundancy in Large Speech Language Models ｜语音大语言模型中的Token冗余解剖与免训练压缩

作者：Bajian Xiang、Tingwei Guo、Xuan Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06871)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06871)

> 语音大语言模型（LSLMs）因高帧率编码导致序列长度远超语义内容，引发高昂推理成本。现有压缩方法多借鉴视觉语言模型（VLMs）技术，缺乏对语音内部冗余层级结构的系统性解析，导致压缩位置与力度选择缺乏理论依据。本文通过层间干预实验揭示深层表示的极端冗余性，并提出基于余弦相似度的免训练Token合并机制Affinity Pooling。该方法在削减27.48%预填充FLOPs的同时保持或提升任务精度，但其在长上下文推理及非英语语音上的泛化能力尚存疑。

】

---

【Do You Get the Hint? Benchmarking LLMs on the Board Game Concept ｜溯因推理基准：Concept 游戏

研究机构：比利时安特卫普大学

作者：Ine Gevers、Walter Daelemans

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ce81ab23342c)

> 大语言模型（LLM）在静态知识问答中表现优异，但在需要整合不完整线索、推断对手意图并动态修正假设的溯因推理任务中，其能力边界尚不明确。现有评测多聚焦于单轮语义匹配或完美信息博弈，缺乏对“线索-概念”映射中抽象推理与心智理论（Theory of Mind, ToM）交互的细粒度诊断。本文引入经典桌游 Concept 作为多语言基准，通过让 LLM 仅扮演猜测者并接收人类生成的分层线索，量化了模型在静态与动态设置下的推理失败模式。该基准揭示了 LLM 在低资源语言及序列信息更新中的显著劣势，但单侧评估设定可能掩盖了模型作为线索提供者时的策略缺陷。

】

---

【Don’t Just Listen, Try Planning: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding ｜长音频会议理解中的图检索生成代理

作者：Quanwei Tang、Dong Zhang、Shoushan Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d169fbf953db)

> 长音频会议理解（Long-form Audio Meeting Understanding, LAMU）面临的核心矛盾是：现有大型音频语言模型（Large Audio-Language Model, LALM）在处理超长会议时，因ASR转文本导致声学信息丢失（Acoustic Missing），且线性上下文窗口无法维持长程语义依赖（Context Fragmentation）。本文切入点在于将会议音频建模为多维异构图，并引入基于部分可观测马尔可夫决策过程（POMDP）的代理规划机制，替代传统的单次检索增强生成（RAG）。通过显式的查询分解、图遍历与自我反思，GRGA在长程多跳推理任务上显著优于端到端LALM与标准RAG基线。其价值在于证明了结构化图索引与代理规划对缓解长音频理解中“中间丢失”问题的有效性，但依赖外部LLM作为策略网络带来的推理延迟与评估者偏差仍是存疑点。

】

---

【Don’t Tell the Answer, Truly Guide the Reasoning During RL Rollouts ｜基于元提示与亲和性感知的强化学习推理框架

作者：Xinyi Wang、Jinyi Han、Zishang Jiang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_459557586f62)

> 强化学习在提升大语言模型长思维链推理能力时，常因任务难度超出模型容量导致奖励稀疏，使策略更新失效。现有缓解手段多依赖注入部分答案，引发分布失配与训练不稳定。本文提出HINT框架，通过提供抽象元提示引导模型自主探索，并引入亲和性感知策略优化动态门控梯度。该方法在多个基准上验证了训练稳定性与泛化优势，但其对教师模型生成元提示的依赖及特定指标协议下的绝对性能上限仍存疑。

】

---

【Double-Edged Sword or Sharp Tool? Designing and Evaluating Triadic LLM-Teacher Collaboration for K-12 Writing at Scale ｜K-12写作中LLM-教师三元协作的实证研究

研究机构：中国人民大学

作者：Canran Wang、Yuwen Yang、Zhen Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.30200)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.30200)

> 该方向旨在解决大语言模型（LLM）在K-12教育中因缺乏人类中介而导致的认知同质化与所有权丧失问题。现有二元协作模式虽提升效率，但忽视了教师作为教学中介的关键作用，导致反馈质量与教学逻辑脱节。本文通过构建包含学生、LLM与教师的三元协作系统，并基于系统功能语言学（SFL）开发多维评估框架，量化了这种协作对写作能力的具体影响。其价值在于提供了大规模实证数据，但缺乏与纯LLM或纯教师反馈的基线对比，使得归因分析存在局限。

】

---

【DP3: Differentially Private Prompt Perturbation for Multi-turn LLM Inference ｜多轮对话差分隐私提示词扰动

研究机构：西安电子科技大学

作者：Lele Zheng、Chao Zhang、Feiyang Yuan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_225250accbd9)

> 大语言模型（LLM）在云端黑盒 API 部署中面临用户提示词泄露风险，现有差分隐私（DP）方法多假设单轮交互，无法处理多轮对话中重复 token 导致的隐私预算线性累积与语义断裂。本文提出 DP3 框架，通过引入扰动映射表复用历史扰动，并结合注意力驱动的上下文效用函数与两阶段分桶指数机制，在保持形式化隐私保证的同时维持跨轮次语义连贯性。该方案在长程多轮场景下实现了更优的隐私-效用权衡，但其对 LDP 独立性假设的潜在挑战及缺乏多轮专用基线对比，限制了结论的普适性验证。

】

---

【DPN-LE: Dual Personality Neuron Localization and Editing for Large Language Models ｜稀疏神经元定位与编辑

研究机构：东南大学、上海交通大学

作者：Lifan Zheng、Xue Yang、Jiawei Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27929)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bd82969f02ee)

> 大语言模型（LLMs）在注入特定人格特质时，常因修改大量神经元而严重损害通用推理能力。现有神经元编辑方法（如NPTI）缺乏对神经元功能的细粒度区分，导致“对齐税”过高。本文切入点在于利用对立人格特质在激活空间中的互斥性，通过双准则过滤定位极少量特质专属神经元。具体做法是构建MLP激活引导向量，结合Cohen's d效应量与激活幅度进行稀疏干预。该方法在保留96%以上神经元未修改的前提下，将通用能力损失降低至全量编辑方法的三分之一，但其在多特质组合下的几何干扰机制尚未被验证。

】

---

【DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models ｜蒸馏推理剪枝

研究机构：美国亚利桑那州立大学

作者：Yuxuan Jiang、Dawei Li、Francis Ferraro

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7028d81ceed0)

> 长思维链（Long-CoT）学生模型常生成冗余轨迹，而短思维链（Short-CoT）教师模型直接蒸馏其简洁答案会导致风格不匹配与可学习性差距。现有压缩方法或依赖提示约束、或采用强化学习惩罚长输出，往往在分布外任务上牺牲准确率。DRP 提出“轨迹感知”离线蒸馏：让学生先生成冗长轨迹，由教师进行技能感知步骤分解与剪枝，再将修剪后的轨迹回传给学生进行监督微调。该方法在 GSM8K 上将 Token 消耗降低 64% 同时提升准确率，但 AIME24 准确率未提升，暗示剪枝策略在极高难度任务上的边界尚不明确。

】

---

【DRPG (Decompose, Retrieve, Plan, Generate): An Agentic Framework for Academic Rebuttal ｜学术反驳生成代理框架

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Peixuan Han、Yingjie Yu、Jingjun Xu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18081)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18081)

> 学术出版流程中，作者对评审意见的回应（Rebuttal）是决定论文命运的关键环节，但现有自动化方法难以兼顾长文本理解与说服性论证。本文指出，直接调用大语言模型（LLM）生成反驳时，模型常因“中间迷失”现象忽略关键证据，且缺乏针对评审质疑的策略性规划，导致回复泛化或过度防御。DRPG通过分解、检索、规划、生成四阶段流水线，引入基于支持度评分的视角选择机制，在8B参数模型上超越人类平均反驳水平。其价值在于将辩论规划技术引入学术场景，但评估依赖LLM裁判，且未对比最新的心智理论基线，泛化性存疑。

】

---

【Duplicate-Aware Controlled Code Generation: Enhancing Copyright Protection with Targeted Reordering Beam Search in LLMs ｜重复感知受控代码生成

作者：Junbo Fu、Guoshuai Zhao、Linkang Yang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6274b366a671)

> 大语言模型在代码生成中倾向于逐字复现训练数据片段，直接触发版权侵权风险，而现有评估体系仅关注功能正确性，忽视了输出内容的法律合规性。传统的数据清洗或后处理去重方法要么破坏模型能力，要么无法实时控制重复长度，导致在保持代码功能完整性的同时消除逐字重复成为技术难点。本文提出重复感知受控代码生成（DACCG）任务，并设计目标重排束搜索（TRBS）算法，在解码阶段通过动态重排候选束来实时抑制重复序列。该方法在8B参数模型上实现了重复率与准确率的灵活权衡，但受限于单函数场景与小模型规模，其在真实仓库级工程环境中的有效性尚未得到验证。

】

---

【DUSK: Do Not Unlearn Shared Knowledge ｜多源知识重叠下的机器遗忘基准

研究机构：韩国延世大学、韩国首尔大学

作者：Wonje Jeung、Sangyeon Yoon、Hyesoo Hong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_465c6671482f)

> 机器遗忘旨在从已训练模型中移除特定数据影响，但现有基准普遍假设遗忘集与保留集知识不相交，忽略了真实语料中广泛存在的跨文档事实重叠。这种假设导致评估无法区分“彻底清除”与“选择性遗忘”，掩盖了现有方法在保留共享知识时的系统性失效。DUSK 通过构建包含共享与唯一知识的合成文档集，定义了七项针对重叠场景的评估指标，并系统测试了九种主流遗忘算法。该基准揭示了当前技术在“表面文本抑制”与“深层知识解耦”之间的巨大鸿沟，但受限于合成数据的风格化构造，其结论向真实复杂语料的泛化能力尚存疑。

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

【DynamicFocalPO: Adaptive Focusing Strategy for Preference Optimization ｜动态聚焦偏好优化

研究机构：南京大学

作者：Shu Zhou、Junan Chen、Rui Ling 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fea5571ef4f)

> 直接偏好优化（DPO）在处理含噪偏好数据时，因固定加权策略导致梯度噪声累积，阻碍模型收敛。现有变体如FocalPO虽引入调制因子，但静态超参数无法适应模型能力演化。本文提出DynamicFocalPO，通过余弦退火动态调整聚焦参数，实现从易到难的课程学习。该方法在7B/8B模型上验证了性能增益，但缺乏大规模模型验证，其动态调度在复杂多目标场景下的泛化能力存疑。

】

---

【Easy Samples Are All You Need: Self-Evolving LLMs via Data-Efficient Reinforcement Learning ｜易样本引导的自进化强化学习

研究机构：北京大学、南开大学

作者：Zhiyin Yu、Bo Zhang、Qibin Hou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18639)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18639)

> 大语言模型（LLMs）在数学推理等可验证任务上的能力突破长期受限于高质量人工标注数据的稀缺与成本瓶颈，现有监督强化学习（RL）依赖昂贵标注，无监督方法则易陷入模型坍缩或奖励作弊。EasyRL 借鉴维果茨基最近发展区（ZPD）理论，提出“易样本知识迁移+难样本分治伪标签+难度渐进自训练”框架，以 10% 易标注数据驱动模型向难样本自进化。该方法在数据效率上表现突出，但其自进化能力是否真正突破基础模型采样分布边界，仍存疑。

】

---

【Efficient and Effective Internal Memory Retrieval for LLM-Based Healthcare Prediction ｜内部键值检索框架 K2K

研究机构：美国康涅狄格大学

作者：Mingchen Li、Jiatan Huang、Zonghai Yao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07659)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_23d7f957db6e)

> 临床LLM部署面临外部检索延迟高与知识幻觉的双重瓶颈，传统RAG管线因长上下文注入导致推理成本激增。K2K将检索目标从外部文档库转向模型内部FFN权重矩阵，通过LoRA注入领域知识并构建激活引导探针，实现无外部搜索的知识访问。该方法在MIMIC-III/IV医疗预测任务上优于KARE等外部检索基线，但其依赖固定层选择且仅在生物医学域验证，通用性存疑。

】

---

【Efficient PRM Training Data Synthesis via Formal Verification ｜形式化验证驱动的过程奖励模型数据合成

研究机构：美国宾夕法尼亚州立大学、美国哥伦比亚大学

作者：Ryo Kamoi、Yusen Zhang、Nan Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2505.15960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_28436e84e902)

> 导读 过程奖励模型（Process Reward Model, PRM）旨在通过细粒度监督提升大语言模型（LLM）的推理能力，但现有训练数据构建依赖昂贵的人工标注或噪声较大的蒙特卡洛采样。本文提出FOVER框架，利用Z3和Isabelle等形式化验证工具对形式化推理任务中的步骤进行自动、精确的错误标注，从而高效合成高质量PRM训练数据。实验表明，基于该数据微调的PRM在非形式化逻辑与数学基准上显著优于基线，验证了形式化到非形式化的迁移有效性。尽管数据效率与跨任务泛化能力突出，但方法受限于形式化任务的覆盖范围，且离线标注策略未解决在线推理时的动态适应问题。

】

---

【Efficient Reasoning for LLMs through Speculative Chain-of-Thought ｜思维链级推测解码

研究机构：香港中文大学

作者：Jikai Wang、Juntao Li、Jianye Hou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4984aa9d5a22)

> 大型推理模型在复杂任务上依赖超长思维链（CoT），导致推理延迟成为系统瓶颈。现有加速方案多聚焦于缩短CoT长度或缩小模型规模，但简单任务上“过度思考”与复杂任务上“精度损失”的矛盾仍未解决。SCoT将推测解码的验证粒度从Token提升至CoT，通过小模型并行生成多条草稿、大模型单次前向选择最优草稿，实现难度自适应的推理加速。该方法在保持近目标模型精度的同时显著降低延迟，但其对高难度任务的精度保持能力与训练开销的权衡尚存疑。

】

---

【Efficient Test-Time Scaling via Temporal Reasoning Aggregation ｜时序推理聚合实现收敛退出

研究机构：北京航空航天大学

作者：Jiakun Li、Xingwei He、Kefan Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17304)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17304)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理计算提升大语言模型（LLM）性能，但常引发过度思考（Overthinking），即模型生成远超必要的推理链。现有动态早期退出方法依赖单步置信度信号，该信号在多步推理中因缺乏跨步稳定性而失效，导致过早或过晚终止。TRACE 通过滑动窗口聚合答案一致性与置信度轨迹，构建时序收敛判据以替代瞬时信号。该方法在无需训练的前提下实现了效率与精度的平衡，但其对极难任务中错误答案持续出现的鲁棒性仍存疑。

】

---

【Efficient Training for Cross-lingual Speech Language Models ｜跨语言语音语言模型的高效训练

研究机构：中国科学院、中国科学院大学

作者：Yan Zhou、Qingkai Fang、Yun Hong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11096)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11096)

> 语音大语言模型（Speech LLM）面临数据稀缺与多语言扩展的双重瓶颈，现有端到端架构依赖海量平行数据，导致低资源语言难以覆盖。CSLM 抓住“跨语言对齐可经由文本模态中转”这一被忽略的结构性特征，通过持续预训练与交错模态链微调，在仅 77k 小时语音数据下实现中英双语对齐。该方法验证了数据效率的可行性，但其对齐依赖外部 CTC 模块，内生泛化能力存疑。

】

---

【EmoRes: Toward Adaptive Psychological Support via User-Agnostic Benchmark and Topic-Mining Agent ｜情绪共鸣心理支持框架

作者：Zhengwei Zou、Xuanming Jiang、Baoyi An 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a9181e30ba41)

> 心理支持对话系统面临的核心矛盾是维持治疗连贯性与适应个体差异之间的平衡，现有递归上下文拼接方法导致对话停滞与情感碎片化。EmoRes 通过引入基于焦点解决短期治疗（Solution-Focused Brief Therapy, SFBT）的多智能体架构，将主题挖掘与自我反思解耦为两个协同代理，在推理时动态调节对话流向。该框架在自建基准 VeilEval 上实现了约 3 倍的性能提升，但其依赖合成数据与 LLM 评估的闭环验证，使得临床效度的外部泛化性存疑。

】

---

【Empirical Analysis of Task Mixture Effects in Small-scale Instruction Tuning: A Statistical Approach ｜无标签指令语料的任务混合统计优化

研究机构：韩国科学技术院

作者：Jeesu Jung、Sangkeun Jung

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff89e41f116b)

> 指令微调的性能高度依赖训练数据中任务类型的比例，但现有研究多依赖人工标注或固定比例，缺乏对无标签语料中任务交互效应的定量分析。本文提出一种最小监督框架，利用种子指令嵌入检索自动识别任务，并通过统计混合建模量化不同任务组合在多种数据规模下的协同与干扰效应。该方法将混合比例设计转化为可统计检验的优化问题，揭示了编程与数学任务的协同性及编程与创意写作的干扰性。其价值在于提供了可解释的混合设计指南，但实验局限于小模型与特定数据集，结论向大模型泛化的能力存疑。

】

---

【EMTIR-GRPO: Efficient Multi-Tool Augmented Large Language Models via Reinforcement Learning ｜成本感知的多工具集成推理强化学习

研究机构：哈尔滨工业大学

作者：Shixin Jiang、Zhihao Zhu、Jiafeng Liang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2add66b6d72c)

> 工具集成推理（Tool-Integrated Reasoning, TIR）旨在让大语言模型（LLM）调用外部工具解决超出其内部能力边界的任务，但现有方法往往陷入“工具滥用”陷阱，导致高昂的计算开销与内在推理能力退化。针对多工具场景下异构成本被忽视、单工具效率优化无法泛化的问题，本文提出 EMTIR-GRPO，一种基于组相对策略优化（Group Relative Policy Optimization, GRPO）的成本感知强化学习算法。该算法通过引入轨迹成本估计与组最优成本估算，构建复合奖励机制以平衡准确率与调用成本。实验表明其在保持准确率的同时显著提升了工具生产力，但组内最优成本的动态估计在训练初期的稳定性及跨域泛化能力仍存疑。

】

---

【EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving ｜工程问题求解基准 EngiBench

研究机构：新加坡南洋理工大学、澳大利亚悉尼大学

作者：Xiyuan Zhou、Xinlei Wang、Yirui He 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.17677)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.17677)

> 现有数学推理基准无法评估大语言模型在真实工程场景中的不确定性处理与多目标决策能力。EngiBench 通过构建三级难度层级与受控问题变体，系统性地诊断模型在信息提取、领域推理、权衡决策及不确定性处理上的具体短板。该基准揭示了当前模型在开放工程任务上远落后于人类专家，且对输入扰动极度敏感。其价值在于提供了细粒度的能力诊断工具，但受限于专家评分的主观性与样本规模，其结论的普适性仍需进一步验证。

】

---

【Enhancing Factuality through Consensus and Consistency in Summarization Using Minimum Bayes Risk Decoding ｜基于共识与一致性的摘要重排序

研究机构：日本东京科学大学

作者：Riza Setiawan Soetedjo、Yusuke Sakai、Hidetaka Kamigaito 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.29336)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3cd6383f5931)

> 摘要生成中的事实性幻觉源于模型对源文档的偏离，而现有重排序方法仅依赖源文档进行无参考评分，因指标粒度粗且存在偏差，无法有效惩罚特定事实错误。本文指出单一信号重排序的局限性，提出结合候选摘要间共识与对源文档一致性的双信号重排序框架。该方法利用最小贝叶斯风险解码计算共识，结合无参考事实性指标计算一致性，通过加权组合选出最优摘要。实验表明该方法在事实性指标上显著优于基线，但绝对得分仍远低于生成式优化方法，且伪参考引入的自生成偏差尚未被量化。

】

---

【Enhancing Long-Chain Reasoning Distillation through Error-Aware Self-Reflection ｜错误感知自反思蒸馏

作者：Zhuoyang Wu、Xinze Li、Zhenghao Liu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3d8d959ff2e3)

> 长思维链（Long-CoT）蒸馏旨在将大模型的推理能力迁移至小模型，但教师生成的复杂轨迹常超出学生容量，导致训练不稳定或过拟合。现有直接蒸馏方法忽视了学生自身错误模式对监督信号的适配价值。本文提出 ORION，利用学生自生成的错误作为条件，反向精炼教师 CoT 以构建适配学生能力的训练数据。该方法在多个数学基准上稳定提升 2% 以上，但其收益依赖于学生初始错误分布的质量，且未验证在开放域任务中的泛化性。

】

---

【Enhancing Multilingual Reasoning via Steerable Model Merging ｜可引导模型合并

研究机构：北京邮电大学、复旦大学

作者：Zhuoran Li、Rui Xu、Jian Yang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e05d33c8dc4)

> 多语言推理面临的核心困境是：固定权重的模型合并策略无法同时满足高资源语言的推理保真与低资源语言的语义理解，导致性能在两类语言间此消彼长。现有静态合并方法将多语言编码器与推理LLM的特征以恒定比例拼接，忽视了输入语言特性对最优融合比例的动态需求。本文提出ST-Merge，通过门控交叉注意力机制根据输入语言动态调节两个源模型的贡献权重，实现输入感知的自适应融合。该方法在21种语言的四个基准上验证了有效性，但其性能上限受限于7B参数骨干模型，且门控机制对离散选择类任务的增益有限。

】

---

【ENPMR-Bench: Benchmarking Proactive Memory Retrieval for Emotional Support Agents ｜情感需求感知主动记忆检索基准

作者：Xing Fu、Yulin Hu、Mengtong Ji 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1e278c652254)

> 情感支持智能体面临的核心矛盾是用户情绪表达的间接性与记忆检索的语义表面性之间的错位。现有记忆基准假设用户能明确表达需求，导致检索目标与情感共鸣脱节，无法评估智能体推断潜在需求并匹配记忆类型的能力。本文通过构建基于马斯洛需求层级的结构化映射框架，将情感需求推断与记忆类型选择解耦为可评估的独立环节。该基准揭示了当前检索范式在情感场景下的系统性失效，但缺乏对动态记忆演化机制的验证，其结论的泛化性存疑。

】

---

【EntroBench: Evaluating LLM Watermarking Under Multi-Entropy Scenarios and Practical User Operations ｜多熵场景下的LLM水印鲁棒性评估基准

研究机构：华中科技大学、武汉大学

作者：Pengyuan Qin、Linnan Tu、Yuhan Ke 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_97749f804ee9)

> 现有LLM水印评估局限于单一熵设定，无法反映真实生成任务中分布多样性的影响，导致方法在低熵或混合熵场景下性能骤降。本文切入点在于构建覆盖高、中、低三种熵水平及七类典型任务的统一基准，并引入非对抗性用户操作模拟。通过锚定数据集校准超参数，公平对比八种主流水印方法在检测率与生成质量上的权衡。该工作揭示了当前水印技术在真实使用场景下的脆弱性，但缺乏对自适应水印算法的理论下界探讨。

】

---

【EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis ｜程序化环境合成框架 EnvScaler

研究机构：中国人民大学

作者：Xiaoshuai Song、Haofei Chang、Guanting Dong 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05808)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05808)

> 大语言模型智能体在长程任务中依赖外部工具交互，但真实环境访问受限、LLM模拟环境存在幻觉、人工构建沙箱难以规模化，导致高质量训练数据稀缺。现有环境合成方法或依赖预置工具集，或缺乏自动化质量评估，无法支撑大规模强化学习训练。EnvScaler 通过程序化代码生成可执行沙箱，结合双智能体迭代评估与规则化轨迹验证，实现了从文本资源到可训练环境的自动化闭环。该框架验证了合成环境对多轮多工具任务性能的显著提升，但其绝对性能仍低于当前 SOTA，且环境多样性对泛化的具体贡献机制尚未量化。

】

---

【EOP-LLM: Energy Oriented Pruning for Large Language Models ｜面向能耗约束的大语言模型动态剪枝

研究机构：美国奥本大学

作者：Guan Huang、Tao Shu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec48eeb9e4d9)

> 大语言模型（LLM）推理能耗已成为数据中心运营的主要成本，但现有效率优化方法多聚焦于浮点运算（FLOPs）或延迟，缺乏对实际能耗的显式建模与约束。本文指出 FLOPs 与实际能耗弱相关，提出 EOP-LLM 框架，通过设备校准能量模型与轻量级选择器，在严格每序列能量预算下动态分配计算资源。该方法在 LLaMA 3.2 与 3.1 模型上实现了能耗减半时的质量保持，但实验局限于单设备静态负载，未验证跨硬件泛化与系统级协同。

】

---

【ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection ｜多模态数学错误检测基准

作者：Yibo Yan、Shen Wang、Jiahao Huo 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.04509)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_26fceb05b60d)

> 多模态大语言模型（MLLM）在数学解题上表现优异，但缺乏对推理过程错误类型的细粒度诊断能力，现有基准仅评估最终答案正确性，无法区分视觉感知、计算或逻辑推理导致的失败。本文切入点在于将任务从“解题”重构为“纠错”，构建首个基于真实学生错误数据的多模态错误检测基准。通过定义错误步骤定位与错误分类两个子任务，评估模型对非标准推理路径的识别能力。该基准揭示了当前SOTA模型在复杂推理诊断上的显著瓶颈，但受限于K-12难度与静态数据分布，其结论向高阶数学或动态场景的泛化性存疑。

】

---

【ERRV: Eliciting Efficient Reasoning through Reasoning Vectors for Policy Optimization in Large Language Models ｜推理向量引导的高效强化学习训练

作者：Zhuowen Han、Lei Yang、Renren Jin 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8927e5ddd1f4)

> 大型推理模型在解决复杂问题时倾向于生成冗长的思维链，导致推理延迟与计算成本激增，而现有优化手段多聚焦于外部奖励函数调整或数据重构，忽略了模型内部隐藏状态中已蕴含的“简洁推理”潜能。本文提出“推理向量”概念，通过对比最短正确响应与最长错误响应的隐藏状态差异提取该向量，并将其注入强化学习（RL）的采样阶段以引导策略优化。该方法在无需推理时向量辅助的情况下，实现了约30%的推理长度缩减且准确率保持稳定，但其效果高度依赖特定骨干网络，跨模型泛化性存疑。

】

---

【Escaping the Sisyphus Dilemma: Experience Replay for Robust Text-to-Optimization Modeling ｜经验回放优化建模

研究机构：中国科学技术大学

作者：Wantong Xie、Yinghao Chen、Yi-Xiang Hu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b30a4b95ed54)

> 导读 LLM 优化建模面临“西西弗斯困境”：模型在结构相似问题上重复相同错误，且现有检索增强生成（RAG）仅能提供静态代码参考，无法传递纠错逻辑。EOM 通过引入因果修正映射与结构感知检索，将瞬时的试错过程转化为持久化的诊断知识。该框架在复杂基准上提升准确率 8.45%，同时降低 28.65% 的 Token 消耗，验证了“一次纠错，多次复用”的可行性，但其对显式求解器反馈的依赖限制了其在静默语义错误场景下的适用性。

】

---

【Establishing a Scale for Kullback-Leibler Divergence in Language Models Across Various Settings ｜建立语言模型跨场景 KL 散度统一尺度

作者：Ryo Kishino、Yusuke Takase、Momose Oyama 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ad47a38834ca)

> 语言模型训练中的权重参数因排列对称性和架构依赖而难以直接比较，导致无法量化不同训练阶段、量化版本或中间层之间的行为差异。现有基于权重的分析无法提供跨架构的统一度量，而 Oyama et al. (2025) 提出的对数似然向量虽能嵌入不同架构，但未建立可解释的绝对尺度。本文通过双中心对数似然向量构造几何空间，确立了 KL 散度在预训练、量化、微调及层级间的统一比特/字节尺度，并揭示了似然空间轨迹的亚扩散特性。该工作提供了模型行为变化的几何标尺，但其结论局限于 Pythia 家族且未验证对下游任务预测的直接增益。

】

---

【ETHICA-MT: Introducing a Framework and Dataset for Studying Ethical Orientations in LLM-based Machine Translation ｜翻译伦理决策框架与基准

研究机构：以色列巴伊兰大学、阿联酋扎耶德大学

作者：Omri Asscher、Arif Ahmad、Ananya Agrawal 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_66e5ea4bdf56)

> 机器翻译长期被视为价值中立的优化任务，但实际翻译过程充满伦理取舍，现有基于BLEU或COMET的指标无法捕捉模型在冲突情境下的伦理倾向。本文从翻译伦理学提取四种竞争立场，构建包含300个分叉路口场景的多语言基准ETHICA-MT-BENCH，通过排序法量化模型默认倾向与指令遵循能力。该工作填补了NLP领域情境化伦理评估的空白，但LLM-as-judge的可靠性与低资源语言对的翻译质量混淆了伦理合规性的评估，结论的普适性存疑。

】

---

【Eval-RAR: Evaluation-Driven Retrieval-Augmented Reasoning via Reinforcement Learning ｜评估驱动检索增强推理

研究机构：中国科学技术大学

作者：Heng Yu、Rui Li、Qi Liu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_550f6f059639)

> 检索增强推理（Retrieval-Augmented Reasoning, RAR）旨在通过迭代检索解决复杂问答，但现有强化学习（RL）范式常陷入“盲搜”循环，即模型无法诊断信息缺口导致检索偏离。本文指出失效根源并非检索能力不足，而是缺乏对“信息不充分”的显式诊断。Eval-RAR 引入“搜索-评估”范式，通过显式自我评估步骤及对应的评估奖励，引导模型在检索后主动识别证据缺口。该方法在七个基准上优于基线，但评估奖励的泛化性及对长链推理的稳定性仍存疑。

】

---

【Evaluating Implicit Biases in LLM Reasoning through Logic Grid Puzzles ｜逻辑谜题推理中的隐性偏见评估

研究机构：美国罗格斯大学、美国约翰斯·霍普金斯大学

作者：Fatima Jahara、Mark Dredze、Sharon Levy

论文原文见 [arXiv](https://arxiv.org/abs/2511.06160)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.06160)

> 大语言模型（LLM）在安全对齐后仍可能在复杂推理中受社会刻板印象驱动，导致决策偏差。现有偏见检测多依赖开放式生成，难以客观量化推理过程中的隐性偏差，且逻辑推理评测常忽略偏见对演绎过程的干扰。本文提出PRIME框架，通过生成中性、刻板与反刻板三种逻辑网格谜题变体，利用编辑距离量化模型在演绎推理中对人口统计学线索的依赖。该框架填补了“推理公平性”评估空白，但其结论局限于性别偏见与特定谜题规模，未验证神经符号方法能否同时消除逻辑错误与偏见。

】

---

【Evaluating Reasoning Models for Queries with Presuppositions ｜预设谬误下的推理模型事实可靠性评估

作者：Rose Sathyanathan、Kinshuk Vasisht、Danish Pruthi

论文原文见 [arXiv](https://arxiv.org/abs/2605.03050)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0cfbb8803a1)

> 用户查询常包含未经证实的隐含假设，若模型盲目接受，将强化错误认知。现有研究多聚焦于传统大语言模型（LLM）在预设谬误下的表现，却忽略了近期兴起的大推理模型（LRM）是否因具备中间推理能力而能更有效地识别并反驳这些错误前提。本文构建了涵盖健康、科学与通用知识的预设强度梯度查询集，系统评估了多种主流模型在事实准确性与决策坚定性上的表现。研究发现，推理能力仅带来2–11%的准确率提升，且未能扭转模型随预设强度增加而倾向于附和错误前提的根本趋势，其价值在于揭示了当前推理机制在事实核查场景下的局限性，但缺乏对错误根源的机制级解释。

】

---

【EvoEdit: Evolving Null-space Alignment for Robust and Efficient Knowledge Editing ｜动态零空间对齐的知识编辑框架

研究机构：加拿大麦吉尔大学、加拿大魁北克人工智能研究所

作者：Sicheng Lyu、Yu Gu、Xinyu Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13851)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13851)

> 大语言模型在持续更新事实知识时，静态参数编辑方法因累积干扰导致先前编辑失效，即“灾难性干扰”。现有定位-编辑范式虽能处理单次或批量更新，但在序列编辑场景下缺乏对历史知识子空间的动态维护机制，导致模型性能随编辑次数增加而急剧退化。EvoEdit通过增量式零空间对齐，将每次新编辑投影至包含所有历史知识的正交补空间中，从而在理论上保证输出不变性。该方法在10K次序列编辑中实现了98.29%的编辑效力，较静态基线提升显著，但其对SVD截断阈值的依赖及在极端长序列下的数值稳定性边界尚存疑。

】

---

【Evolving Agentic Workflow Driven by Human-Agent Collaboration ｜人机协作驱动的进化式智能体工作流优化

研究机构：上海交通大学、华东师范大学

作者：Yuxin Liu、Jinxuan Zhang、Yuezhang Peng 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c5f50a9c7ff)

> 智能体工作流编排旨在通过协调多个大语言模型（LLM）调用解决长程复杂任务，但现有自动化方法面临高设计成本、搜索低效及对人类偏好适应差三大瓶颈。HFlow 提出一种由人机协作（Human-Agent Collaboration, HAC）引导的进化算法框架，通过交叉与变异操作在结构、提示词与模型骨干构成的搜索空间中生成多样化工作流种群。该方法利用分层经验记忆实现跨任务策略迁移，在数学与代码基准上超越自动基线最高 27.34%，且成本仅为 o1-preview 的四分之一。尽管在绝对性能上未超越当前领域 SOTA，但其将人类偏好显式纳入多目标优化函数的范式为低成本自适应编排提供了新路径，其进化搜索在离散空间中的收敛效率仍存疑。

】

---

【Experience-Driven Multi-Agent Optimization for Black-Box Jailbreak Attacks on Large Language Models ｜经验驱动多智能体黑盒越狱优化

研究机构：华东师范大学

作者：Zhaoyang Han、Yihe Liu、Kai Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fbe1723d9981)

> 黑盒越狱攻击的核心矛盾在于高维提示空间探索与有限查询预算之间的张力。现有自动化方法依赖盲目搜索或固定模板，导致查询成本高昂且跨模型泛化能力弱。EMJO 通过引入动态经验库与多智能体诊断闭环，将无记忆搜索转化为经验引导的进化过程，显著降低了平均查询次数。该框架在效率上具有显著优势，但其经验库的跨模型迁移边界及单轮攻击对多轮防御鲁棒性的掩盖效应仍存疑。

】

---

【Experience-Driven Reflective Co-Evolution of Prompts and Heuristics for Autonomous Algorithm Design ｜经验驱动反思协同进化

研究机构：中国人民大学、香港城市大学

作者：Yihong Liu、Junyi Li、Hongyu Lu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fcd8a64ea779)

> 自动启发式设计（AHD）旨在突破手工算法对专家知识的依赖，利用大语言模型（LLM）的语义推理能力自动发现高性能组合优化算法。现有方法多将LLM视为静态变异算子，受限于固定提示与稀疏反馈，易陷入局部最优且代码错误易在种群中传播。本文提出EvoPH，通过耦合提示词进化与启发式进化，利用执行经验动态调整变异策略，实现搜索过程的自我修正。该框架在TSP和BPP上显著优于基线，但其性能高度依赖底层LLM的规模，小模型在装箱问题上几乎失效，暴露了方法对模型能力的强耦合性。

】

---

【ExpertIVS: Sociological Expert Driven Individual Value Simulation in Large Language Models ｜社会学专家驱动的个体价值观模拟

研究机构：天津大学

作者：Zhen Wang、Yuqi Ren、Yuehan Cui 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_87bdb809a704)

> 现有基于大语言模型（LLM）的社会模拟常将调查数据机械拼接为提示，导致个体价值观呈现语义碎片化，且静态评估无法捕捉动态交互中的价值漂移。ExpertIVS 通过构建 14 个社会学专家智能体对世界价值观调查（World Values Survey, WVS）数据进行结构化归纳推理，生成逻辑连贯的个体档案，并引入多智能体辩论机制评估动态一致性。该方法在 480 名受访者上实现了 90.78% 的价值观还原保真度，但其高准确率是否源于 WVS 问题的强语义锚点，以及专家推理是否引入新的系统性偏差，仍需进一步审视。

】

---

【Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models ｜重塑探索与利用机制以优化大模型推理效率

作者：Yufeng Shi、Weilin Luo、Yuxiang Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0914fcfbe5b9)

> 大推理模型（LRM）在可验证奖励强化学习（RLVR）训练中普遍存在“过度思考”现象，导致简单任务计算资源浪费。现有基于长度惩罚的奖励整形方法缺乏对高价值数据的优先利用与定向探索，导致样本效率低下。本文提出SIGMA框架，将推理效率优化重构为经典的探索-利用权衡，通过自模仿损失与动态优先级采样提升数据利用率，并引入自引导探索机制生成更简洁的轨迹。该方法在1.5B和7B模型上实现了43.4%和40.3%的长度缩减，同时保持或提升准确率，但其效果高度依赖骨干模型的预训练质量，且未验证在动态难度分布下的鲁棒性。

】

---

【Exploring Coding Spot: Understanding Parametric Contributions to LLM Coding Performance ｜编码参数子集定位

作者：Dongjun Kim、Minhyuk Kim、Yongchan Chun 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c31722a1204c)

> 大语言模型（LLM）在代码生成任务上表现优异，但其内部如何组织编码知识仍属黑盒，现有评估体系仅关注外部行为正确性，无法解释能力来源。本文提出“编码点”（Coding Spot）概念，旨在定位承载编码能力的稀疏参数子集。通过跨语言泰勒近似评分与定向消融，验证了该子集的存在性及其语言无关性。这一发现为模型压缩与安全部署提供了新视角，但受限于单一模型家族与静态基准，其结论在复杂工程场景下的普适性尚存疑。

】

---

【Exploring the Capability Boundaries of LLMs in Mastering of Chinese Chouxiang Language ｜中文抽象语言（Chouxiang Language）的大语言模型能力边界评估

作者：Dianqing Lin、Tian Lan、Jiali Zhu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15841)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4ab68bc9799a)

> 导读 现有大语言模型（LLMs）在处理非西方、非主流的网络亚文化语言时，往往因训练数据分布不均而陷入“表面正确、深层错位”的困境，导致对特定社群语义的解码失效。传统评估基准多聚焦于通用文化价值观或显性毒性检测，缺乏对动态演变的、非标准语义空间（如谐音替换、视觉隐喻）的细粒度量化手段。本文构建了Mouse基准，通过六个NLP任务系统评估LLM对中文抽象语言的掌握程度。该工作填补了亚文化语言评估的空白，但受限于静态数据集与单一语言模态，其结论在动态语境下的泛化能力存疑。

】

---

【Exploring Two-Phase Continual Instruction Fine-tuning for Multilingual Adaptation in Large Language Models ｜两阶段持续指令微调中的指令相似性对英语能力保持的影响

研究机构：微软研究院

作者：Divyanshu Aggarwal、Sankarshan Damle、Navin Goyal 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.16006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ece602ea5ce7)

> 多语言大语言模型在提升非英语指令跟随能力时，常因灾难性遗忘导致英语能力显著退化，现有混合训练或盲目回放策略难以在资源受限下平衡双语性能。本文指出，阶段间指令数据集的语义相似性是决定英语能力是否保持的关键变量，而非单纯的数据量或训练步数。通过引入数据集嵌入相似度与模型参数差异度量，结合生成式回放与启发式层冻结策略，该研究在 MISTRAL-7B 和 LLAMA-3-8B 上验证了相似指令集可提升英语能力，而错位指令集则引发表示漂移。这一发现为低资源语言适配提供了基于数据结构的预测机制，但其全参数微调的高算力成本限制了在边缘设备上的直接部署。

】

---

【ExpSeek: Self-Triggered Experience Seeking for Web Agents ｜自触发经验寻求框架

研究机构：中国科学院、中国科学院大学

作者：Wenyuan Zhang、Xinghua Zhang、Haiyang Yu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.08605)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08605)

> 开放网络中的搜索智能体常因证据稀疏与噪声干扰而在多轮交互中迷失，现有经验注入方法将历史教训作为全局上下文一次性喂给模型，无法适应交互过程中动态变化的认知状态。本文切入点在于利用模型自身的输出熵作为内在置信度信号，在智能体真正“困惑”时才主动检索并生成针对性经验指导。ExpSeek 通过基于 Bootstrap 重采样的熵阈值估计确定介入时机，并由独立经验模型生成步级指导，实现了从被动全局注入到主动步级寻求的范式转换。该框架在四个搜索基准上验证了有效性，但其依赖离线构建的经验库与特定骨干模型，在跨域泛化与实时性上存在边界。

】

---

【FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing ｜非结构化知识编辑中的细粒度事实锚定

作者：Peng Wang、Biyu Zhou、Xuehai Tang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12559)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_286e0e20f36e)

> 非结构化模型编辑旨在让大语言模型吸收真实世界文本，但现有方法往往仅能整体复述编辑后的文本，无法可靠地检索其中的原子事实。本文指出这种“整体记忆”与“细粒度访问”的错位源于Transformer单向流动中表面形式生成对底层事实表示的放大而非校正。FABLE通过两阶段分层策略，先将离散事实锚定在浅层，再对深层进行最小化更新以生成连贯文本。该框架在细粒度问答上取得显著提升，但其对批量编辑稳定性的验证尚缺。

】

---

【FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning ｜因果工具变量下的思维链忠实度评估

研究机构：香港浸会大学、澳大利亚墨尔本大学

作者：Yuxi Sun、Aoqi Zuo、Haotian Xie 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10693)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10693)

> 思维链（Chain-of-Thought, CoT）推理的可靠性审计面临核心困境：模型生成的中间步骤看似连贯，实则可能缺乏逻辑依赖，而现有的大语言模型（LLM）自评估方法因自肯定偏差无法识别这种“链内不忠实”。本文切入点在于将结构因果模型（Structural Causal Model, SCM）中的工具变量方法引入CoT评估，通过注入外部噪声构造反事实轨迹，分离真实因果效应与模型内部偏差。具体做法是计算原始与扰动轨迹在LLM评估下的平均因果效应（Average Causal Effect, ACE），结合答案一致性筛选可信推理路径。该方法在数学与常识任务上提升了答案准确率，但其黑盒因果推断能否替代白盒机制分析，仍存疑。

】

---

【FACTS: Table Summarization via Offline Template Generation with Agentic Workflows ｜离线模板生成的查询聚焦表格摘要

作者：Ye Yuan、Mohammad Amin Shabani、Siqi Liu

论文原文见 [arXiv](https://arxiv.org/abs/2510.13920)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f1a9c4805b1)

> 查询聚焦表格摘要旨在根据用户意图从表格中生成叙事性洞察，而非仅返回事实值。现有方法要么暴露敏感数据，要么因缺乏可复用性导致计算冗余，且难以保证数值准确性。FACTS 通过生成可复用的离线模板（SQL查询+Jinja2渲染）解决这一矛盾，实现了隐私合规与高效推理。其价值在于将一次性推理转化为可执行资产，但模板对模式漂移的鲁棒性仍存疑。

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

【False Sense of Security: Why Probing-based Malicious Input Detection Fails to Generalize ｜探测分类器失效机制：表面模式而非语义理解

作者：Cheng Wang、Zeming Wei、Qin Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c134b436dcb0)

> 基于内部表征的恶意输入检测长期被视作LLM安全的有效防线，但现有评估仅关注分布内性能，掩盖了泛化能力的缺失。本文指出探测分类器实际依赖浅层词汇模式而非语义有害性，导致其在真实场景中失效。通过引入朴素贝叶斯基线对比、语义清洗对照实验及模式依赖分析，系统性地证伪了“表征可分性即语义理解”的假设。该研究揭示了当前安全检测范式的根本缺陷，但受限于单轮静态表征，其结论在多轮动态交互场景下的普适性尚存疑问。

】

---

【FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments ｜失败感知元智能体框架

研究机构：美国亚利桑那州立大学

作者：Amir Saeidi、Venkatesh Mishra、Souradeep Mukhopadhyay 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.25135)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_910474489371)

> 交互式工具使用场景中，开源小模型因上下文窗口受限与推理能力不足，在长程对话中面临严重的错误累积问题。现有静态多智能体框架（如IRMA）通过全量注入辅助智能体来缓解此问题，但引入了高昂的Token开销且未能针对特定模型的失败模式进行优化，导致性能波动。本文提出FAMA框架，通过两阶段机制先诊断基线智能体的主导失败类型，再动态激活最小化的专用智能体子集以注入针对性上下文。该方法在资源受限条件下实现了显著的准确率提升，但其依赖预定义智能体池与错误分类体系，对未知失败模式的泛化能力存疑。

】

---

【FAQ: Mitigating Quantization Error via Regenerating Calibration Data with Family-Aware Quantization ｜家族感知量化校准

研究机构：中国科学院

作者：Haiyang Xiao、Weiqing Li、Jinyue Guo 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11200)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11200)

> 大语言模型（LLM）部署中，训练后量化（PTQ）的精度瓶颈常被归因于权重或激活的离群值，但校准数据与目标模型激活分布的失配这一数据源问题长期被算法优化所掩盖。现有PTQ方法通过二阶补偿或旋转缩放重塑分布，却默认静态校准集能代表推理时的复杂激活模式，导致量化参数偏差。本文提出FAQ框架，利用同族大模型重生成校准数据，从源头平滑激活分布。该策略在INT4量化下将精度损失降低28.5%，但其有效性高度依赖模型家族内部的激活一致性，跨家族泛化能力存疑。

】

---

【Fast and Effective On-policy Distillation from Reasoning Prefixes ｜前缀在线策略蒸馏

作者：Dongxu Zhang、Zhichao Yang、Sepehr Janghorbani 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15260)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15260)

> 在线策略蒸馏（On-Policy Distillation, OPD）旨在通过学生模型自生成轨迹上的教师反馈消除训练-推理分布失配，但其全量采样机制在长链推理任务中导致计算成本呈线性增长，成为部署瓶颈。现有方法要么依赖离线序列匹配而遗留曝光偏差，要么执行全量在线采样而陷入算力陷阱，本文切入点在于验证“仅监督轨迹前缀”是否足以保留 OPD 的核心收益。通过截断学生 rollout 并仅对前 $L$ 个 token 计算反向 KL 散度，配合线性前缀调度策略，该方法在保持接近全量 OPD 性能的同时，将训练 FLOP 降低 2 至 47 倍。这一工程化改进有效缓解了长序列蒸馏的效率瓶颈，但其对小型模型尾部泛化能力的潜在损害及调度策略的静态性，仍构成应用边界。

】

---

【Fast-Decoding Diffusion Language Models via Progress-Aware Confidence Schedules ｜进度感知置信度调度

作者：Amr Mohamed、Yang Zhang、Michalis Vazirgiannis 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4909e67c1268)

> 扩散大语言模型（Diffusion Large Language Models, dLLM）的解码效率受限于固定的去噪步数预算，导致在简单输入上产生大量冗余计算。现有早停方法依赖离散阈值或局部信号，在长文本任务中易崩溃。本文提出 SchED，通过聚合全答案区域的 Top-2 Logit 边际，并与平滑的进度感知阈值比较，实现无损早停。该方法在指令微调模型上实现约 4 倍加速且质量保持 99.8% 以上，但其加速收益高度依赖指令微调带来的熵衰减特性，在基础模型上收益有限。

】

---

【Feasible is Not Enough: Cost-Aware Optimal Tool-Chain Planning on Multi-Solution Tool Graphs ｜多解工具图上的成本感知最优规划

作者：Liangliang Liu、Yanming Li、Yigang Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d03aa10b9cd1)

> 工具增强大语言模型（Tool-Augmented LLMs）在大规模工具库中常面临候选路径爆炸与上下文窗口受限的双重压力，现有方法多将工具调用视为单解问题，忽略同一任务存在多条有效路径且成本差异巨大的现实。本文切入点在于将工具学习（Tool Learning, TL）重构为多解图上的最优路径选择问题，通过强化学习（Reinforcement Learning, RL）驱动的两阶段渐进式图扩展与推理框架，在构建紧凑任务相关子图的同时执行成本感知规划。该框架在自建基准上显著提升了任务成功率与解的最优性，但其泛化能力受限于特定领域API的静态结构，且未与最新RLVR基线进行同协议对比。

】

---

【Federated LoRA Fine-Tuning with Pipelined Error-Mitigated Aggregation and Matrix-Wise Freezing ｜联邦低秩适配微调中的流水线误差缓解聚合与矩阵级冻结

研究机构：武汉大学、华中科技大学

作者：Haoran Wang、Xiong Wang、Yuqing Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22e6b757e603)

> 联邦大语言模型微调面临聚合偏差与边缘设备算力瓶颈的双重制约，直接平均低秩因子导致全局更新失真，而现有冻结策略粒度粗糙或计算开销过大。iFLoRA通过重构局部更新矩阵并执行SVD分解来消除代数误差，同时引入流水线机制隐藏服务器端计算延迟，并基于更新稳定性实施自适应矩阵级冻结。该方法在保持模型精度的前提下显著提升了训练效率，但其SVD近似误差在极端非独立同分布数据下的鲁棒性仍缺乏充分验证。

】

---

【Feedback Is The Key for Automated Survey Generation ｜反馈驱动的可验证综述生成

研究机构：香港城市大学、华中科技大学

作者：Tianyi Xu、Zhe Zhao、Tianshuo Wei 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_048ddbd610fa)

> 自动综述生成面临的核心困境是LLM在长文本合成中产生的幻觉引用与结构松散，导致输出缺乏学术可信度。现有主流方法如AutoSurvey和SurveyX采用线性流水线，将生成视为单向过程，忽略了人类写作中至关重要的“评审-修订”迭代环节，致使引用忠实度难以保证。FIKSurvey通过引入双智能体协作机制，将同行评审范式外化为显式的反馈循环，并利用滑动窗口自然语言推理（NLI）实现引用的可验证对齐。该框架在引用召回率上显著超越基线，但其依赖闭源大模型且评估协议存在单一性，限制了其通用性与可复现性。

】

---

【Fine-Grained Data Ordering Improves Fine-Tuning for Large Language Models ｜细粒度顺序微调

研究机构：浙江大学、新加坡国立大学

作者：Xiaomeng Hu、Yixuan Tang、Haoze Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e44b2fb4dae7)

> 微调阶段的数据治理长期聚焦于“选什么”，即通过过滤或子集选择提升数据质量，却忽视了“怎么排”，即训练序列对模型收敛路径的影响。现有随机洗牌策略无法实现从预训练分布向目标分布的渐进迁移，导致梯度震荡与收敛效率低下。FOT通过定义基于模型交叉熵与预训练先验的数据难度，在早期Epoch实施由易到难的块内洗牌排序，后期恢复随机以平衡泛化。该方法在持续预训练与监督微调任务中实现了平均2.4%的性能提升，但其增益依赖于难度定义的准确性，且未验证与数据过滤策略的协同效应。

】

---

【FLASH: Focused Layer Attention Sink Hijacking ｜聚焦层注意力汇聚劫持

研究机构：天津大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Siyuan Deng、Yerong Li、Fanhua Shang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eea410d57922)

> 大语言模型的安全对齐机制往往依赖浅层结构维持，现有白盒攻击多陷入高成本的输入空间梯度优化，难以直接定位内部决策瓶颈。FLASH 切入点在于重新定义注意力汇聚（Attention Sink）现象，将其视为绑定安全约束的“安全锚点”，通过精准干预浅层注意力分数实现低开销越狱。该方法结合内部扰动、输入变体生成与输出过滤，在保持模型通用能力的前提下实现了高效攻击。其价值在于揭示了安全机制的结构性脆弱，但攻击效率是否受限于特定模型架构的浅层依赖，仍需进一步验证。

】

---

【FlashMem: Distilling Intrinsic Latent Memory via Computation Reuse ｜计算复用蒸馏内在潜在记忆

研究机构：北京航空航天大学、中国科学院

作者：Yubo Hou、Zhisheng Chen、Tao Wan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fe92e0585f8a)

> 大语言模型（Large Language Model, LLM）的无状态特性导致智能体在长程任务中必须冗余重处理历史上下文，而现有生成式潜在记忆（Generative Latent Memory）范式依赖独立辅助模块，造成架构分离与计算冗余。FlashMem 通过直接复用骨干网络的冻结键值（Key-Value, KV）缓存来合成记忆，并引入无参数注意力熵监控器实现自适应触发。该框架在推理任务上达到与重型基线相当的性能，同时将推理延迟降低 5 倍，但其长期记忆稳定性与跨会话一致性仍缺乏验证。

】

---

【FLEXITOKENS: Flexible Tokenization for Evolving Language Models ｜柔性分词器：基于区间约束的字节级语言模型

研究机构：美国俄亥俄州立大学、美国华盛顿大学

作者：Abraham Toluwase Owodunni、Orevaoghene Ahia、Sachin Kumar

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_03d4d7d482ac)

> 现有字节级语言模型在适配新领域或未见语言时，因预训练阶段锁定的固定压缩率导致过度碎片化，严重损害推理效率与下游性能。FLEXITOKENS 通过引入铰链损失替代传统的二项分布正则项，允许压缩率在特定区间内自由波动，从而解耦了分词策略与单一分布的绑定。该方法在保持多语言公平性的同时，显著提升了模型在分布外数据上的适应能力。尽管在中等规模模型上验证了有效性，但其在大参数模型下的训练稳定性及跨域泛化边界仍存疑。

】

---

【FlowRAG: Synergizing Explicit Reasoning via Frequency-Aware Multi-Granularity Graph Flow ｜频率感知多粒度图流检索增强生成

研究机构：华东师范大学、丰田研究所

作者：Bihao Zhan、Zongsheng Cao、Jie Zhou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.17856)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.17856)

> 现有图检索增强生成（GraphRAG）方法在处理抽象查询时面临实体稀疏导致的检索不足，且在多跳推理中易受噪声干扰导致路径断裂。本文指出，隐式拓扑评分无法有效区分核心实体与偶然提及，且缺乏宏观语义锚点。FlowRAG 通过构建四级异构图并引入频率感知加权流算法，将隐式随机游走转化为显式逻辑骨架提取。该方法在复杂多跳基准上超越了 LinearRAG 和 HippoRAG，但其性能提升主要依赖于静态图结构的优化，未解决动态知识更新下的实时性问题。

】

---

【Forge: Quality-Aware Reinforcement Learning for NP-Hard Optimization in LLMs ｜质量感知强化学习求解NP-hard优化问题

研究机构：同济大学、浙江大学

作者：Xiaozhe Li、Xinyu Fang、Shengyuan Ding 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08905)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08905)

> 大语言模型在组合优化任务中普遍存在“可行但非最优”的缺陷，现有基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）范式仅依赖二元正确性反馈，无法引导模型逼近全局最优解。本文切入点在于利用NP-hard问题固有的目标函数值，构建连续质量感知奖励信号，突破二元反馈的局限。通过设计生成器-验证器-求解器流水线，FORGE-RLVR在Qwen2.5-7B上实现了93.1%的成功率与46.6%的质量比，并验证了优化思维向通用推理的迁移能力。该框架在优化任务上显著优于GPT-4o，但其质量比仍远低于启发式基线，提示模型在复杂搜索空间中的探索深度仍有巨大提升空间。

】

---

【Format-Adapter: Improving Reasoning Capability of LLMs by Adapting Suitable Format ｜格式自适应测试时扩展

作者：Dingzirui Wang、Xuanliang Zhang、Rongyu Cao 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77bd7ff5b23b)

> 测试时计算扩展（Test-Time Scaling, TTS）旨在通过增加推理时的计算资源来提升大语言模型（LLM）的推理性能，但现有并行扩展方法通常局限于固定推理格式，导致模型在特定格式下产生的系统性误差无法通过增加采样次数消除。本文指出，格式选择是塑造解空间分布的核心变量，固定格式下的TTS仅能降低方差，而多格式TTS能扩展推理模式以突破能力上限。FORMAT-ADAPTER通过生成候选格式并基于误差最小化原则进行贪心选择，实现了无需训练的格式自适应TTS。该方法在数学与常识推理基准上平均提升2.2%的相对性能，但其依赖LLM打分作为代理损失的可靠性仍存疑，且未验证格式多样性对极端复杂任务的覆盖能力。

】

---

【FormulaReasoning: A Dataset for Formula-Based Numerical Reasoning ｜公式驱动数值推理数据集

作者：Xiao Li、Bolin Zhu、Kaiwen Shi 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aff168a56c99)

> 现有数学基准多依赖隐式常识，缺乏对领域特定公式的显式监督，导致模型在复杂物理计算中易产生幻觉。本文通过构建包含细粒度公式标注的双语数据集，并引入逆向变换与参数噪声注入策略，旨在评估模型在结构化知识引导下的多步推理能力。实验表明，大模型在简单公式题上接近人类水平，但在耦合复杂题上显著落后，揭示了当前模型在长程依赖与系统方程求解上的瓶颈。该数据集填补了领域特定公式推理基准的空白，但其对检索器精度的依赖及小模型微调收益的局限性仍需进一步验证。

】

---

【FrameNet-Cultures: A Benchmark for Evaluating LLMs via Cross-Cultural Frame Semantics ｜基于框架语义的LLM文化结构评估基准

研究机构：丹麦哥本哈根大学

作者：Neda Jamshidi、Anders Søgaard、Monica Bianchini

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd041deb5679)

> 该方向旨在解决大语言模型（LLMs）在生成文化描述时存在的系统性欧洲中心主义偏差，以及现有选择题基准无法区分“捷径学习”与“深层文化理解”的困境。现有方法多依赖封闭问答或预定义维度，难以量化模型内部潜在的文化结构同质化现象。本文切入点在于引入框架语义（Frame Semantics），通过开放生成任务将模型输出映射为二元特征向量，并与民族志数据进行结构对齐。其价值在于首次实现了从“事实正确性”到“结构相似性”的评估范式转变，但二元编码对文化梯度信息的丢失及单一标注者的主观性仍是主要存疑点。

】

---

【From Attack Surfaces to Actual Operations: A Survey of Modern LLM Jailbreaks ｜基于漏洞机制的LLM越狱攻击双轴分类框架

研究机构：德国慕尼黑工业大学、新加坡国立大学

作者：Ruikang Zhou、Changsheng Sun、Mark Huasong Meng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dd84080b93b1)

> 现有越狱攻击综述多按“如何执行”（如提示工程、梯度优化）分类，导致无法解释“为何成功”，防御设计缺乏针对性。本文提出“技术-操作”双轴分类框架，将攻击映射至LLM生命周期中的具体漏洞（训练/推理衍生），并量化其与部署约束的关联。该框架通过相关性分析揭示了攻击策略与模型架构缺陷的结构性耦合，为预测性防御提供了机制依据，但其分类边界对多模态及系统级隔离场景的覆盖仍显不足。

】

---

【From Coarse to Fine: Self-Adaptive Hierarchical Planning for LLM Agents ｜自适应层级规划

研究机构：中国人民大学

作者：Haoran Tan、Zeyu Zhang、Chen Ma 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23194)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23194)

> 现有 LLM 智能体规划器通常在固定粒度下生成计划，导致简单任务过度规划、复杂任务细节不足。本文切入点在于引入认知科学中的“渐进细化”理论，通过蒙特卡洛奖励评估动态选择最优层级，并采用两阶段训练优化层级选择与计划质量。该方法在 ALFWorld 和 ScienceWorld 上验证了自适应粒度对任务效率与成功率的提升，但其依赖单一骨干模型构建监督信号，跨模型泛化能力存在显著偏差。

】

---

【From Domains to Instances: Dual-Granularity Data Synthesis for LLM Unlearning ｜双粒度数据合成框架

研究机构：香港理工大学、华为

作者：Xiaoyu Xu、Minxin Du、Zitong Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04278)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04278)

> 大语言模型（LLM）遗忘的核心痛点在于现有基准的遗忘集无法覆盖模型内部真实记忆的语义变体，导致评估结论失真。BiForget 通过目标模型自引导的双阶段合成策略，自动化生成与模型知识分布对齐的领域级与实例级遗忘集。该框架在 Harry Potter 域将数据量减半的同时提升了相关性，但其在低知识密度领域的泛化能力仍存疑。

】

---

【From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning ｜从经验到技能：基于可复用策略学习的多智能体生成式引擎优化

研究机构：中南大学、中山大学

作者：Beining Wu、Fuyou Mao、Jiong Lin 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19516)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19516)

> 生成式引擎（GEs）将信息获取从链接排序转变为带引用的答案生成，但现有生成式引擎优化（GEO）方法仅针对单实例进行启发式修改，无法跨任务积累有效策略。本文指出，缺乏策略复用机制导致优化过程陷入重复试错，且现有指标分离了可见性与引用忠实度。MAGEO 通过多智能体执行层与技能库学习层的双层架构，将验证过的编辑模式蒸馏为可复用的引擎特定技能。该框架在因果归因协议下显著提升了内容可见性与引用准确性，但其策略泛化能力受限于静态检索列表的假设，且高计算成本是否抵消长期收益仍存疑。

】

---

【From Fake to Real: Mitigating Out-of-Distribution Bias in In-Context Learning via Feedback Supervision from Large Language Models ｜基于置信度与扰动困惑度的分布外伪标签迭代选择

研究机构：吉林大学

作者：Rui Song、Yingji Li、Jian Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8772ba4cb74)

> 上下文学习（In-Context Learning, ICL）在源域与目标域分布差异显著时，基于相似度的演示检索往往失效甚至劣于随机选择。现有鲁棒性缓解方法多依赖显式分布对齐或代理域检索，难以在缺乏目标域标签的条件下直接利用测试样本。本文提出 LPL，通过轻量模型生成初始伪标签，结合置信度与扰动困惑度（CPP）筛选高质量样本，并由 LLM 迭代扩充演示池以规避分布外（Out-of-Distribution, OOD）偏差。该方法在多个 NLP 任务上验证了噪声容忍的有效性，但其性能增益高度依赖伪标签初始质量，在对抗性数据集上优势收窄。

】

---

【From Fallback to Frontline: When Can LLMs be Superior Annotators of Human Perspectives? ｜视角采择的统计估计重构

研究机构：美国普渡大学、美国圣路易斯华盛顿大学

作者：Hasan Amin、Harry Yizhou Tian、Xiaoni Duan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17968)

> 主观标注长期面临“无客观真值”与“群体视角难以直接观测”的双重困境，传统方法将LLM视为人类标注的廉价替代品，却忽视了二者在统计估计属性上的本质差异。本文切入点在于将视角采择（Perspective-Taking, PT）从“测量个体意见”重构为“估计潜在群体均值”，从而在缺乏金标准的主观任务中建立人类与LLM的可比性。通过引入偏差-方差-相关性分解框架与双镜头误差模型，论文量化了LLM在低预算下作为一线估计器的结构性优势。这一范式转换挑战了“LLM仅能作为后备”的领域共识，但其优势边界严格依赖于群体在训练数据中的覆盖度，对低 prevalence 群体的适用性仍存疑。

】

---

【From Fragments to Facts: A Curriculum-Driven DPO Approach for Generating Hindi News Veracity Explanations ｜印地语新闻真实性解释生成：基于课程学习与增强DPO的框架

研究机构：印度理工学院、奥地利因斯布鲁克大学

作者：Pulkit Bansal、Raghvendra Kumar、Shakti Singh 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2507.05179)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_177d9d417208)

> 自动化事实核查旨在解决海量错误信息传播与人工核查效率之间的张力，但现有系统多聚焦英语等高资源语言，导致印地语等低资源语言缺乏可规模化的自动解释生成工具。主流LLM在低资源场景下常产生表面流畅但事实脱节的解释，且标准偏好优化方法未显式约束事实准确性与生成稳定性。DeFactoX通过构建合成偏好数据集，结合课程学习策略与引入事实性、幻觉度量的增强DPO损失函数，实现了对印地语新闻真实性解释的可靠生成。该框架在低资源解释生成任务上提供了有效路径，但其对动态事实验证能力的边界尚待明确。

】

---

【From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation ｜代码生成中的隐性偏见：从条件语句到机器学习管道

研究机构：美国科罗拉多大学博尔德分校

作者：Minh Duc Bui、Xenia Heilmann、Mattia Cerrato 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21716)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1c07c93183ff)

> 代码生成模型在构建决策系统时，常将敏感属性作为预测特征，导致隐性歧视。现有评估仅检测显式条件语句，严重低估了实际部署中的偏见风险。本文通过对比条件语句与完整机器学习管道的特征选择行为，量化了这一评估盲区。该工作揭示了评估范式的结构性缺陷，但未提供去偏方案，其结论对模型内部机制的解释力仍待检验。

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

【From Implicit Graph Encoding to Explicit Evidence: A Training-Free LLM Framework for Temporal Knowledge Graph Reasoning ｜显式证据驱动的无训练时序知识图谱推理

研究机构：哈尔滨工业大学、北京航空航天大学

作者：Guo Tang、Ke Cheng、Huiming Fan 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_13cc9c22706a)

> 时序知识图谱（TKG）预测面临分布偏移与归纳泛化失效的双重困境，传统参数化模型依赖训练分布，而现有大语言模型（LLM）方法受限于隐式模态对齐与图结构线性化带来的信息丢失。ExE-LLM 通过解耦图计算与语义推理，将图信号显式转化为自然语言证据，实现了无需梯度更新的测试时自适应。该框架在归纳设置下显著优于训练式图神经网络，但其启发式规则在极端稀疏结构下的鲁棒性及离散时间衰减对长程依赖的捕捉能力仍存疑。

】

---

【From Implicit to Explicit: Token-Efficient Logical Supervision for Mathematical Reasoning in LLMs ｜逻辑关系显式监督

研究机构：香港科技大学

作者：Shaojie Wang、Liang Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2601.03682)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03682)

> 大语言模型在数学任务中常因依赖表面模式匹配而非深层逻辑，导致输入微小扰动时性能崩塌。现有思维链监督微调（CoT-SFT）虽提升准确率，却未解决“逻辑关系理解”这一核心瓶颈，导致模型在变量识别与运算选择上持续出错。本文提出首步逻辑推理（First-Step Logical Reasoning, FSLR），通过仅监督“第一步规划”来显式强化逻辑关系理解。该方法在7B-8B小模型上显著优于CoT-SFT及数学专用模型，但其优势是否随模型规模扩大而衰减，尚存疑。

】

---

【From Individual Excellence to Collective Sustainability: Seeking Strategic Equilibrium in Proactive Multi-Agent Teams ｜博弈论驱动的科学团队任务分配

研究机构：南开大学、美国伍斯特理工学院

作者：Tong Zhang、Yang Wu、Yufei Shi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49b0e4d19e4c)

> 科学团队中的主动代理常陷入“个体中心陷阱”，即为了最大化即时任务准确率而过度依赖资深专家，导致团队长期可持续性受损。现有反应式规划或简单启发式路由无法量化这种机会成本，且缺乏在稀疏监督下平衡效率与公平的策略机制。本文提出 GT-PMARL，通过双层架构将任务分配重构为纳什-帕累托均衡博弈，利用非负正-未标注（nnPU）学习从稀疏成功样本中构建质量先验。该框架在生物医学文献基准上验证了防止专家过载的有效性，但其缺乏与标准多智能体强化学习（MARL）基线的定量对比，使得其相对于简单负载均衡策略的优势边界尚不明确。

】

---

【From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models ｜检索头掩码优化长上下文大语言模型

研究机构：日本东京科学大学

作者：Youmi Ma、Naoaki Okazaki

论文原文见 [arXiv](https://arxiv.org/abs/2601.11020)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9e8f8877f3d9)

> 长上下文大语言模型面临标称窗口长度与有效推理能力脱节的困境，现有后训练方法依赖外部奖励模型或人工标准，难以精准定位性能瓶颈。RetMask 利用机制可解释性发现的“检索头”作为对比信号源，通过屏蔽特定注意力头生成负样本，构建直接偏好优化训练对。该方法在 Llama-3.1-8B 上实现了 128K 上下文下 2.28 分的提升，验证了机制洞察转化为性能增益的可行性，但其效果高度依赖模型内部检索分数的稀疏度分布。

】

---

【From Local Perspective to Global Reasoning: A Neuro-Symbolic Framework for Zero-Shot Relation Extraction ｜全局神经符号推理框架

研究机构：美国东北大学

作者：Kailun Lyu、Fu Zhang、Zehan Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_93e3835b0357)

> 零样本关系抽取（ZSRE）的核心困境在于模型往往孤立地评估每个实体对，导致在语义相似但逻辑不同的关系间产生混淆。现有基于嵌入匹配或提示学习的方法均局限于局部视角，缺乏跨事实的逻辑一致性约束。G-NSR 通过构建双重类型约束命题集，利用神经符号推理器执行全局逻辑蕴含与证据聚合，将独立预测转化为相互印证的逻辑系统。该方法在 FewRel 上取得平均 +4.14 F1 的提升，但其依赖 BERT 编码器而非前沿大语言模型（LLM），且全局推理的计算复杂度随候选关系数增长，限制了其在大规模开放场景下的直接适用性。

】

---

【From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models ｜从被动指标到主动信号：大语言模型不确定性量化的功能演进

研究机构：Salesforce AI研究院、美国范德堡大学

作者：Jiaxin Zhang、Wendi Cui、Zhuohang Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15690)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15690)

> 大语言模型（LLM）在高风险场景中的部署受制于其“自信地犯错”的倾向，传统不确定性量化（UQ）仅作为事后诊断指标，无法支持多步推理与智能体交互中的实时决策。现有方法在静态输出评估上已趋成熟，但缺乏将不确定性转化为实时控制信号的机制，导致模型无法在生成过程中动态调整策略。本文提出将UQ从被动评估升级为主动控制信号，通过语义熵、置信度等信号驱动推理路径选择、工具调用及强化学习奖励，实现模型行为的实时干预。这一范式转换在理论上具有显著价值，但其实际收益依赖于信号校准精度，且缺乏与静态评估方法的直接定量对比。

】

---

【From Personal to Collective: On the Role of Local and Global Knowledge in LLM Personalization ｜局部-全局知识协同框架

研究机构：美国圣母大学、南开大学

作者：Zehong Wang、Junlin Wu、Zhaoxuan Tan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_339cb5de52ad)

> 大语言模型个性化长期受困于“孤立用户建模”的结构性缺陷：数据稀疏的新用户无法获得有效适配，而历史丰富的老用户则易陷入行为偏斜的过拟合。现有参数高效微调（PEFT）与检索增强生成（RAG）路线均将用户视为独立实体，忽略了跨用户共享的集体行为模式。LoGo 通过构建时间演化且社区感知的全局知识模块，并将其作为局部适配器的初始化先验，在层级化参数空间中平衡群体规律与个体偏好。该框架在 LaMP 基准上显著提升了冷启动用户的泛化能力并降低了高活跃用户的预测偏差，但其离线聚类假设与动态偏好演化之间存在潜在张力。

】

---

【From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents ｜从检索到遗忘：个性化智能体长期记忆基准

研究机构：美国亚利桑那州立大学、美国亚利桑那大学

作者：Md Nayem Uddin、Kumar Shubham、Eduardo Blanco 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f499e22c429f)

> 长期记忆评估长期被简化为跨会话事实检索，掩盖了智能体在信息更新与废弃时的状态一致性缺陷。现有基准如LoCoMo和LongMemEval对记忆整合与突变施加的压力极低，导致模型在真实非平稳交互中的失效模式被隐藏。Memora通过构建周、月、季度尺度的高突变对话流，并引入遗忘感知记忆准确率（FAMA）指标，将记忆评估从“是否召回”转向“是否维持当前有效状态”。该基准揭示了现有记忆智能体在长时程下的脆弱性，但其评估协议对生成数据质量的依赖及基线覆盖的局限性，限制了结论的普适性。

】

---

【From Representation to Choice: Tracing Decision Emergence Across Languages in LLMs ｜从表示到选择：追踪大语言模型跨语言决策涌现

研究机构：印度理工学院坎普尔分校、三星研究院

作者：Divyanshu Bhatt、Abhinav Joshi、Ujjaval Patel 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7541fa42f785)

> 多语言大语言模型（LLMs）在回答不同语言问题时，内部推理路径如何演化尚不明确。现有研究多聚焦于静态表示相似度或最终准确率，忽略了决策形成的动态时序特征，导致无法解释为何相同语义在不同语言下表现差异巨大。本文通过构建层解析的决策轨迹，将推理过程建模为随机过程，量化了跨语言分歧的具体发生位置。这一视角揭示了英语中心主义在决策层的微观机制，但仅作为诊断工具，未直接提供性能优化方案。

】

---

【From Scoring to Explanations: Evaluating SHAP and LLM Rationales for Rubric-based Teaching Quality Assessment ｜基于SHAP与LLM推理的评分忠实度评估框架

研究机构：德国慕尼黑工业大学、瑞典隆德大学

作者：Ivo Bueno、Babette Bühler、Philipp Stark 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.05180)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05180)

> 该方向旨在解决高利害教育场景中，不透明模型生成的评分缺乏可审计依据的问题。现有方法或依赖注意力权重（因果性弱），或依赖LLM自由文本解释（忠实性低），导致教师无法有效质疑自动化判断。本文切入点在于将句子级SHAP归因与LLM生成的句子排名进行系统性对比，并通过删除测试量化其因果影响。其价值在于提供了跨架构的解释迁移评估协议，但结论局限于特定教育数据集，且未探讨句子级归因对Token级细节的掩盖效应。

】

---

【From Signal Degradation to Computation Collapse: Uncovering the Two Failure Modes of LLM Quantization ｜量化失效的机制诊断：信号退化与计算崩塌

研究机构：中国科学院大学、中国科学院

作者：Chenxi Zhou、Pengfei Cao、Jiang Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19884)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19884)

> 大语言模型（LLM）低比特量化在2-bit区间常出现性能断崖，但现有研究多将其视为数值误差的累积，缺乏对内部机制失效的系统解释。本文切入点在于区分“信号退化”与“计算崩塌”两种定性不同的失效模式，通过因果追踪与表征拓扑分析揭示其本质差异。实验证明4-bit失效可通过无训练策略修复，而2-bit失效需结构重建。该框架提供了量化失效的诊断基础，但其结论是否适用于旋转类量化方法尚存疑。

】

---

【From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms ｜从存储到经验：LLM智能体记忆机制的演化框架

研究机构：香港浸会大学、香港科技大学

作者：Jinghao Luo、Yuchen Tian、Chuxue Cao 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.06716)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06716)

> 大语言模型（LLM）智能体在长时程任务中因固有状态lessness导致逻辑断裂与重复错误，现有研究在操作系统工程与认知科学两条范式间割裂，缺乏统一的技术演化视角。本文提出“存储-反思-经验”（Storage-Reflection-Experience, SRE）三阶段演化框架，将记忆机制从被动记录重构为主动抽象的认知过程。该框架通过形式化定义各阶段的信息抽象层级，揭示了记忆从轨迹保真向策略先验转化的内在驱动逻辑。其价值在于提供了跨范式的理论整合视角，但作为定性综述，缺乏定量验证以证明经验阶段在特定任务上的实际增益。

】

---

【From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning ｜从Token到Step：验证感知的投机解码

作者：Kiran Purohit、Ramasuri Narayanam、Soumyabrata Pal

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_93a681b62387)

> 多步推理任务中，标准投机解码（Speculative Decoding, SD）的Token级验证常因拒绝语义正确但概率低的草稿Token而引发错误级联，导致加速失效。现有方案依赖外部奖励模型（Process Reward Model, PRM）进行步骤级验证，但引入了高延迟与任务泛化性差的问题。SPECGUARD通过集成模型内部的注意力接地与对数概率信号，在步骤级执行自适应验证，无需外部验证器。该方法在推理基准上提升了准确率并降低了延迟，但其对标准SD无损性假设的偏离及在通用文本生成中的适用性仍存疑。

】

---

【Fundamental Reasoning Paradigms Induce Out-of-Domain Generalization in Language Models ｜解耦基础推理范式以增强大语言模型泛化能力

作者：Mingzi Cao、Xingwei Tan、Mahmud Elahi Akhter 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1e438019e8f)

> 大语言模型在复杂推理任务中的表现瓶颈，源于其自回归生成机制与多步逻辑推导之间的内在张力，现有方法往往将演绎、归纳与溯因三种基础逻辑范式混同处理，导致无法量化单一范式对通用推理能力的独立贡献。本文切入点在于通过符号化任务剥离世界知识，独立诱导三种范式技能，并验证其跨域泛化能力。具体做法是利用教师模型生成纯逻辑轨迹，通过全量微调、低秩适配、深度扩展及混合专家结构扩展等四种方法诱导学生模型，并在真实自然语言任务上评估。该方法证明了基础逻辑技能可独立迁移至现实任务，但其在数学基准上的缺失及教师-学生家族匹配性的矛盾，限制了结论的普适性。

】

---

【GALA: Geometric Data Selection with Strategic Prospecting for Large Language Model Self-training ｜几何数据选择与策略探索

研究机构：同济大学

作者：Zhongwei Xie、Ruihao Liao、Zimo Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_278b0ccb2313)

> 大语言模型（LLM）自训练旨在通过模型生成自身训练数据实现能力迭代，但现有“生成-过滤”范式常陷入语义冗余与策略单一的双重困境，导致训练效率低下且泛化能力受限。GALA 提出了一种“更聪明地策展”（curate-smarter）的闭环框架，将静态子集选择升级为动态数据流生成。该方法通过几何聚类锚点选择、策略头脑风暴与反思机制以及动态批次门控，在显著减少训练样本量的同时维持了与全量数据相当的性能。其核心价值在于解决了自训练过程中的数据动态性缺失问题，但绝对性能提升有限，且对超参数敏感。

】

---

【GanitLLM: Difficulty-Aware Bengali Mathematical Reasoning through Curriculum-GRPO ｜孟加拉语数学推理模型 GANITLLM：基于课程式 GRPO 的低资源语言训练

作者：Shubhashis Roy Dipta、Khairul Mahbub、Nadia Najjar

论文原文见 [arXiv](https://arxiv.org/abs/2601.06767)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06767)

> 导读 低资源语言大语言模型在数学任务中面临推理语言归属与训练效率的双重困境，现有高资源语言强化学习配方因奖励稀疏导致梯度失效。本文切入点在于识别并解决 Group Relative Policy Optimization (GRPO) 在低资源场景下的冷启动问题，通过构建难度感知数据集 GANIT 并提出 CURRICULUM-GRPO 采样策略，实现原生孟加拉语推理。该方法在 Bn-MGSM 上提升 8 分准确率，但绝对性能仍低于高资源语言基线，其泛化边界尚待验证。

】

---

【Gaperon: A Peppered English-French Generative Language Model Suite ｜GAPERON：基于全开源模型的数据污染影响机制实证

研究机构：美国康奈尔大学

作者：Nathan Godey、Wissam Antoun、Rian Touchent 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.25771)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.25771)

> 导读 大语言模型评估失效的根源在于预训练数据与测试集的不可控重叠，导致模型通过记忆而非推理获得高分，严重扭曲了能力评估。现有检测方案多聚焦于事后识别污染或构建动态基准以规避泄露，却缺乏对“污染程度-性能增益”非线性关系的受控量化，尤其在全开源、可复现的训练全流程中，污染如何具体影响基准分数与生成质量仍属黑箱。本文通过构建全开源的GAPERON模型系列，在预训练后期故意注入基准测试集，实证了污染对下游任务的影响边界。该工作提供了污染研究的白盒实验床，但其结论局限于特定模型规模与数据混合策略，未验证在更大规模或不同架构下的普适性。

】

---

【GAVEL: Evidence-Contract Debate with Mechanized Scrutiny for Provenance-Grounded Fact-Checking ｜证据锁定辩论与机械化审查

作者：Ruoyu Xu、Gaoxiang Li、Victor S. Sheng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a89ab2e8fea6)

> 自动化事实核查的核心挑战在于，模型常生成流畅但缺乏来源支撑的结论，尤其在需要引用具体表格单元格或跨文档证据链时，现有方法难以保证证据的细粒度准确性。本文切入点在于将证据绑定从语义层下沉至标识符层，通过强制原子子声明与显式证据单元绑定，并在推理过程中引入确定性校验。GAVEL 构建了一个多智能体辩论框架，结合证据契约与机械化审查链，确保每个论断都有可验证的物理来源。该方法在 FEVEROUS 和 HOVER 基准上显著提升了证据完整性指标，但其性能上限受限于底层小模型的推理能力，且未涵盖实时网络证据场景。

】

---

【GCIG: GraphRAG-based Cross-document Instruction Generation for Boosting LLM Reasoning ｜基于图检索的跨文档指令生成

作者：Xiaoliang Xu、Huang Yuan、Junmei Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f7cd3b98e26)

> 现有自动指令生成方法在处理知识密集型领域时，常因依赖单文档片段而导致多跳推理指令缺乏逻辑连贯性。本文指出，缺乏跨文档证据的结构化组织是造成指令逻辑扁平化与事实幻觉的核心瓶颈。GCIG 框架通过构建增强知识图谱并引入思维链引导的答案生成机制，自动化合成具备可追溯证据链的高质量指令数据。该方法在 HotpotQA 等基准上显著提升了多跳推理性能，但其对高文档密度场景下的噪声抑制能力仍显不足。

】

---

【Generalization or Memorization? Multi-Agent vs. Baseline LLMs and AutoML Models for Tabular Classification ｜表格分类中多智能体LLM与AutoML的可靠性对比

研究机构：美国弗吉尼亚大学、美国圣母大学

作者：Aida Sanatizadeh、Sorouralsadat Fatemi、Reza Mousavi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b8691db471d)

> 表格数据驱动的高风险决策要求系统不仅准确，更需在分布偏移和困难实例上保持校准与稳定。现有LLM方法在表格分类上的表现常被预训练语料记忆所混淆，且缺乏对实例级可靠性的细粒度诊断。本文通过构建污染感知的评估协议和模块化多智能体框架（MALLM），系统性地解耦了记忆效应与泛化能力。该研究揭示了当前LLM在表格分类中作为独立预测引擎的结构性局限，但其结论的普适性仍受限于特定数据集规模和评估维度。

】

---

【Generating Effective CoT Traces for Mitigating Causal Hallucination ｜事件因果识别中的因果幻觉缓解

研究机构：加拿大康考迪亚大学

作者：Yiheng Zhao、Jun Yan

论文原文见 [arXiv](https://arxiv.org/abs/2604.12748)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d200380ef242)

> 事件因果识别（Event Causality Identification, ECI）旨在判断文本中两个事件间是否存在真实因果机制，但小参数大语言模型（LLM）常因依赖统计关联而将非因果对误判为因果对，即因果幻觉。现有ECI数据集仅含二元标签，缺乏中间推理步骤，导致微调无法纠正模型的逻辑断裂；而通用思维链（Chain-of-Thought, CoT）准则在ECI任务中失效，无法指导有效训练数据的构建。本文通过实证分析证伪了困惑度选择、短CoT偏好等通用准则，提出基于语义丰富度与分布对齐的CoT生成管线，并引入因果幻觉率（Causal Hallucination Rate, CHR）量化指标。该工作在小模型上显著降低了幻觉率，但其结论是否适用于大模型或结构化因果图任务尚存疑。

】

---

【GeoLAN: Geometric Learning of Latent Explanatory Directions in Large Language Models ｜几何潜空间正则化框架

研究机构：美国佛罗里达大学

作者：Tianyu Bell Pan、Damon L. Woodard

论文原文见 [arXiv](https://arxiv.org/abs/2603.19460)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19460)

> 大语言模型（LLM）在高风险场景部署面临黑盒决策的审计危机，现有后验归因方法难以保证解释的因果忠实性。本文切入点在于将可解释性从推理时的特征发现前移至训练时的几何结构约束，通过强制潜空间各向同性来消除表示坍缩。具体做法是引入基于Kakeya猜想衍生的Wolff公理，设计两个可微分损失函数在训练阶段重塑Token轨迹的几何形态。该框架在中等规模模型上验证了几何约束对解释指标的提升，但在小模型上引发性能退化，且缺乏与主流机制可解释性方法的直接因果对比。

】

---

【GerAV: Towards New Heights in German Authorship Verification using Fine-Tuned LLMs on a New Benchmark ｜德语作者验证基准与微调大语言模型

作者：Lotta Kiefer、Christoph Leiter、Sotaro Takeshita 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_190c1514be1d)

> 作者验证（Authorship Verification, AV）旨在判定两段文本是否出自同一作者，是法证调查中的核心环节。现有研究高度集中于英语数据，非英语场景缺乏大规模、系统化的评测基准，导致模型在跨语言场景下的鲁棒性难以评估。本文构建了包含40万对文本的德语AV基准GerAV，并系统评估了微调大语言模型（LLM）在该任务上的表现。该工作填补了非英语LLM-AV研究的空白，但其性能增益中预训练知识与微调贡献的边界尚不清晰。

】

---

【GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification ｜组微调：从模仿到奖励的无偏优化

研究机构：浙江大学

作者：Wangjie Gan、Miao Pan、Linbo Xi 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14258)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14258)

> 大语言模型后训练的核心矛盾在于，监督微调（SFT）虽能高效注入知识，却因单路径依赖导致策略熵坍缩，并引发灾难性遗忘，使得后续强化学习（RL）的探索空间被严重压缩。现有方案如标准SFT或纯RL均无法在保持通用能力与提升推理上限间取得平衡，本文切入点在于从训练动力学视角揭示SFT本质上是带有不稳定逆概率权重的稀疏奖励RL特例。通过引入组优势学习与动态系数校正，GFT在单一阶段内实现了无偏对比监督与优化稳定性的统一。该框架在数据效率上显著优于SFT基线，但其绝对性能仍低于当前SOTA混合策略，且对多任务场景下的组构成动态调整缺乏验证。

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

【GoT-R1: Internalizing Graph-of-Thought via Structural Reinforcement for High-Density Reasoning ｜图思维链强化学习

作者：Zuchao Li、Qiwei Li、Yao Yao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a9b559dd62c)

> 线性思维链（Chain-of-Thought, CoT）在复杂推理中常因顺序生成导致冗余叙述与级联错误，现有外部搜索框架虽能缓解但引入高延迟与编排开销。GoT-R1 将推理重构为原子节点构成的有向无环图，并通过两阶段训练将图结构内化至模型权重，以拓扑密度替代文本长度。该方法在 GSM8K 上以 95.07% 准确率仅消耗 632,167 tokens，显著优于外部搜索基线，但其对推理忠实性的因果验证缺失，使得结构效率与逻辑真实性的关系仍存疑。

】

---

【GR1: Reinforcement-Enhanced LLM for Geoscience Reasoning ｜地球科学多模态推理的强化学习微调

作者：Yule Xie、Jiaxin Ding、Cheng Deng 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e3e2648ce8ae)

> 地球科学问题耦合了广域事实记忆与多步因果推理，且超过30%的题目依赖地图或剖面图，导致现有基于监督微调的专用模型难以通过自动验证信号优化深层推理能力。通用大语言模型在直接处理此类多模态任务时，常因遗漏关键视觉线索或泄露答案而失效，使得基于结果验证的强化学习无法直接应用。本文通过构建多智能体转文本管线与事实奖励机制，在纯文本环境下实现了地球科学推理能力的显著提升。该工作验证了强化学习在垂直科学领域的迁移有效性，但其将多模态问题降维为文本的处理方式，可能损失了空间推理的关键信息。

】

---

【Graph Explorer: Training Faithful KG Agents with Visibility-Grounded Supervision ｜可见性接地监督下的知识图谱智能体训练

研究机构：美国波士顿大学、美国华盛顿大学

作者：Yifeng Chen、Sicheng Wan、Tianyi Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f56700b99c2c)

> 知识图谱问答（KGQA）智能体在探索图结构时，常因上下文窗口限制而面临“幻觉参数”问题，即模型试图调用未在提示中出现的实体标识符。现有提示工程方法无法提供可靠的步骤级监督，而直接转换专家查询又因全局视图与局部视图的冲突导致监督失效。本文提出一种自动数据合成管线，将专家SPARQL编译为线性工具计划，并通过“可见性检查”过滤不可执行轨迹，实现动作中心微调。该方法在严格协议下显著提升了小模型的工具调用可靠性，但其对数据分布的潜在偏差及跨域泛化能力尚存疑。

】

---

【Graph-Assisted Large Language Models: A Perspective on Mitigating Intrinsic Limitations ｜图辅助大语言模型：从能力缺陷修复视角的系统性综述

研究机构：中国科学院、中国科学院大学

作者：Haitong Luo、Fali Wang、Weiyao Zhang 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4de848f22274)

> 大语言模型（LLM）在知识时效性、线性推理局限及多智能体协作僵化上存在固有缺陷，现有研究多聚焦于单一维度的图应用，缺乏对图结构如何系统性缓解这些局限的统一视角。本文切入点在于将图结构视为修复LLM内在缺陷的通用工具，而非仅作为外部检索源。通过构建涵盖参数化知识增强、非参数化检索、推理规划及协作优化的五维分类体系，本文整合了从知识注入到动态智能体编排的全链路方法。该综述提供了领域全景地图，但其分类边界在动态协作场景下的量化评估标准仍显模糊。

】

---

【Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs ｜基于图结构的思维链反思冗余剪枝

研究机构：中南大学

作者：Hongyuan Yuan、Xinran He、Run Shao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18621ef42b84)

> 长思维链推理中，模型常陷入无差别检查与重复验证的“过度思考”陷阱，导致计算资源浪费。现有压缩方法多依赖全局长度惩罚或Token级重要性评分，难以精准定位语义层面的反思冗余。本文切入点在于将线性思维链重构为有向无环图，利用拓扑属性识别并剪除低效反思节点。通过三阶段训练管线内化该剪枝策略，在保持准确率的同时显著降低推理长度。该方法在结构建模上具有创新性，但离线图构建成本与标签粗粒度限制了其通用性。

】

---

【GraphLoRA: Structure-Aware Low-Rank Adaptation for Large Language Model Recommendation ｜结构感知低秩适配

研究机构：安徽大学、中国科学技术大学

作者：Lin Mu、Guoji Wang、Li Ni 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.07526)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.07526)

> 推荐系统面临的核心矛盾在于大语言模型（LLM）擅长处理文本语义，却难以内化用户-物品交互中隐含的高阶拓扑结构。现有方法或将协同信号线性化为提示词，或注入静态嵌入，均无法在参数空间内动态捕捉结构依赖。本文提出 GraphLoRA，将图神经网络（GNN）嵌入低秩适配（LoRA）瓶颈层，实现结构感知的参数对齐。该方法在参数效率与结构推理间取得了平衡，但其对生成式推荐范式的适用性尚存疑。

】

---

【GRASP: Graph-Reasoning Aided Survey Planning for High-Fidelity Related Work Generation ｜图推理辅助综述规划

作者：Haoming Li、Jessica Ouyang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d0e072d0ec69)

> 导读 自动综述生成面临的核心挑战在于，当引用文献数量超过模型上下文窗口时，LLM难以维持跨文档的逻辑一致性并准确捕捉论文间的论证关系。现有方法多依赖线性大纲或简单的引用网络特征，导致生成的相关工作部分（Related Work Section, RWS）往往沦为孤立摘要的堆砌，缺乏对研究脉络的深度整合。GRASP提出了一种双层图结构框架，结合思维图（Graph of Thoughts, GoT）与论证-反论证规划网络（Argument-Counterargument Planning Network, ACPN），并通过Steiner树剪枝保留核心语义骨架。该框架在OARelatedWork数据集上显著提升了引用意图与话语角色的保真度，但其对稀疏引用领域的泛化能力及计算开销仍存疑。

】

---

【GRE Score: Generative Risk Evaluation for Large Language Models ｜生成式鲁棒性评估分数

研究机构：香港中文大学、IBM研究院

作者：Zaitang LI、Pin-Yu Chen、Tsung-Yi Ho

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ae07703c30dd)

> 大语言模型（LLM）安全评估长期依赖高成本的对抗攻击迭代，且现有基准面临数据污染风险。本文提出 GRE Score，一种基于条件生成模型的鲁棒性证书，通过计算语义空间中的最小扰动下界来量化模型韧性。该方法仅需前向传播即可生成具有理论保证的评估指标，实现了与攻击成功率（ASR）的高相关性。其价值在于提供高效的替代评估方案，但语义空间扰动与真实文本对抗的等价性仍存疑。

】

---

【Grounding Agent Memory in Contextual Intent ｜基于上下文意图的智能体记忆系统

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国斯坦福大学

作者：Ruozhen Yang、Yucheng Jiang、Yueqi Jiang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10702)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10702)

> 长时程智能体交互中，语义相似但上下文不同的信息极易导致检索混淆，现有记忆系统缺乏对潜在目标状态的显式建模。STITCH 通过在线诱导“上下文意图”三元组作为结构化检索线索，解决了这一干扰问题。其核心在于将记忆检索从语义相似度匹配升级为意图兼容性过滤。该方法在高干扰场景下显著优于基线，但其对强 LLM 骨干的依赖限制了轻量化部署，且未验证在通用事实召回任务上的泛化优势。

】

---

【GroupRank: A Groupwise Paradigm for Effective and Efficient Passage Reranking with LLMs ｜GroupRank：分组式重排范式

研究机构：中山大学

作者：Meixiu Long、Duolin Sun、Dan Yang 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.11653)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11653)

> 导读 LLM 文档重排旨在利用大语言模型的上下文理解能力，将检索系统中的文档排序任务从静态相关性匹配升级为动态效用优化，其核心价值在于突破传统交叉编码器在长上下文与全局依赖建模上的瓶颈。现有 Listwise 方法虽能捕捉全局依赖，但受限于上下文窗口与自回归解码的高延迟，难以在大规模候选集下实时部署；Pointwise 方法虽高效，却因缺乏文档间比较导致排序精度次优。本文提出 GroupRank，通过将候选文档划分为独立小组并行评分，结合无答案数据合成与专用强化学习奖励，在保持 Listwise 精度的同时实现 Pointwise 级别的低延迟。该范式在推理密集型任务上显著优于基线，但其随机分组策略对组内高相关文档的区分能力存疑，且未验证在通用语义任务上的鲁棒性。

】

---

【Guardian-as-an-Advisor: Advancing Next-Generation Guardian Models for Trustworthy LLMs ｜守护模型作为顾问

研究机构：美国圣母大学、美国加州大学洛杉矶分校

作者：Yue Huang、Haomin Zhuang、Jiayi Ye 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07655)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07655)

> 大语言模型（LLMs）部署中的安全守护通常依赖硬门控分类器，这种机制在守护模型与部署模型规范不一致时，会因过度拒绝而损害有用性。现有方案将安全检测局限于有害性标签，忽略了鲁棒性与诚实性等信任维度，且刚性阻断无法保留下游模型的生成自主性。本文提出GaaA范式，通过外部守护模型生成风险标签与自然语言解释并前置到提示中，以软门控方式引导而非阻断生成。该范式在检测精度上接近闭源模型，并显著提升了鲁棒性与诚实性场景下的响应质量，但其有效性高度依赖基础模型的指令遵循能力，且在标准越狱防御基准上的表现尚待验证。

】

---

【HACHIMI: Scalable and Controllable Student Persona Generation via Orchestrated Agents ｜教育理论锚定下的分布可控学生画像生成

研究机构：华东师范大学、香港科技大学

作者：Yilin Jiang、Fei Tan、Xuanyu Yin 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04855)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c619ed3be22c)

> 大规模教育模拟亟需兼具心理真实性与群体统计效度的合成学生画像，以替代高成本的人工访谈。现有基于大语言模型（LLM）的生成方法虽能产出叙事性文本，却普遍存在内部自相矛盾与群体分布坍缩问题，且缺乏教育学理论的显式约束。本文提出理论对齐与分布可控画像生成（Theory-Aligned and Distribution-Controllable Persona Generation, TAD-PG）任务，并构建多智能体框架 HACHIMI，通过神经符号验证与配额调度实现硬约束下的规模化生成。该框架在内部一致性上表现优异，但在深层心理构念的外部效度上存在明显梯度衰减，其作为通用模拟基础设施的边界尚待厘清。

】

---

【HCRE: LLM-based Hierarchical Classification for Cross-Document Relation Extraction with a Prediction-then-Verification Strategy ｜层级分类与预测验证策略

研究机构：厦门大学

作者：Guoqi Ma、Liang Zhang、Hongyao Tu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f000b33468d)

> 跨文档关系抽取（Cross-Document RE）旨在从分散在不同文档的实体间识别语义关联，但现有“小语言模型+分类器”范式受限于语义理解能力，难以处理大规模预定义关系集。直接引入大语言模型（LLM）虽具备更强推理能力，却因选项过多导致区分度下降与注意力分散，性能甚至低于强SLM。本文通过构建层级关系树将分类任务拆解为自顶向下的多步决策，并引入预测-验证策略抑制层级间错误传播，从而在CodRED基准上显著超越SLM基线。该方案验证了结构化选项缩减对LLM性能的关键作用，但其对树结构构建质量的依赖及推理延迟增加问题尚存疑。

】

---

【Health-ORSC-Bench: A Benchmark for Measuring Over-Refusal and Safety Completion in Health Context ｜医疗领域过度拒绝与安全完成基准

研究机构：澳大利亚麦考瑞大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Zhihao Zhang、Liting Huang、Guanghao Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17642)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17642)

> 医疗大语言模型的安全对齐常陷入两难：拒绝有害请求时往往连带拒绝良性咨询，导致用户转向不可靠信息源。现有通用基准缺乏医疗垂直领域的细粒度评估，且仅关注二元拒绝行为，无法区分“过度拒绝”与“低质量的安全响应”。本文构建了一个包含31,920条边界提示的医疗专用基准，通过自动化改写与人工验证流程，首次引入“安全完成率”指标以量化模型在提供有用信息同时保持安全警告的能力。该基准揭示了前沿模型在医疗场景下的“安全悲观主义”现象，为校准医疗AI助手提供了评估标准，但其单语言限制与主观评分协议仍制约了结论的普适性。

】

---

【HearSay Benchmark: Do Audio LLMs Leak What They Hear? ｜音频大语言模型声纹隐私泄露基准

作者：Jin Wang、Kaiwen Luo、Liang Lin 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01cae2ca3614)

> 音频大语言模型（ALLMs）在预训练中是否编码了声纹与敏感个人属性之间的隐性关联，这一风险此前缺乏量化手段。现有文本与视觉隐私评估无法迁移至纯声学场景，且缺乏区分“真实声学推理”与“统计先验幻觉”的指标。本文构建基于真实讲座音频的 HearSay 基准，引入盲偏置率（BBR）验证泄露源于声学证据而非过拟合。该工作确立了 ALLM 声学隐私泄露的实证基线，但评估仅覆盖静态属性，未涉及动态交互中的上下文泄露。

】

---

【Heterogeneity in Formal Linguistic Competence of Language Models: Is Data the Real Bottleneck? ｜语法范式数据稀缺性诊断与最小干预

作者：H S V N S Kowndinya Renduchintala、Sumit Bhatia

论文原文见 [arXiv](https://arxiv.org/abs/2604.17930)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17930)

> 大语言模型在通用基准上表现优异，却在特定语法范式上出现低于随机猜测的失败，且单纯扩大预训练数据量无法解决这一异质性。现有宏观数据混合优化方法关注全局分布比例，缺乏对微观语法结构暴露量的因果归因能力，导致无法区分架构限制与数据稀缺。本文通过向预训练语料中注入1%的定向合成文本，验证了数据稀缺是主要瓶颈。该研究提供了“数据阈值”的新视角，但仅在小规模模型上验证，其结论向大规模模型的迁移性存疑。

】

---

【Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection ｜分层零一阶混合优化

研究机构：北京大学

作者：Feihu Jin、Ying Tan

论文原文见 [arXiv](https://arxiv.org/abs/2601.05501)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05501)

> 大语言模型微调面临一阶优化易陷局部极小值与零阶优化在生成任务中因输出空间扩张导致方差爆炸的双重困境。现有纯零阶方法在复杂生成任务中性能崩溃，而纯一阶方法缺乏探索能力，导致泛化受限。本文提出Hi-ZFO，通过基于FLOPs预算的动态规划将参数分层，对高敏感层执行一阶更新，对低敏感层执行零阶扰动，以“有益随机性”平衡精度与探索。该方法在生成与推理任务上超越全参数微调，但受限于静态分区策略，未解决训练过程中参数敏感性的动态演化问题。

】

---

【Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling ｜基于隐状态与内存约束的推理轨迹剪枝

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Zhixiang Liang、Beichen Huang、Zheng Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09093)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09093)

> 并行采样通过生成多条推理路径提升准确率，但长轨迹与多路径叠加导致算力成本与端到端延迟激增，且现有剪枝信号（相似度、置信度）无法可靠区分正确与错误轨迹。本文切入点在于发现隐状态在推理早期即包含质量判别信号，且延迟瓶颈主要来自 GPU 内存饱和引发的排队而非 Token 生成本身。STEP 训练轻量级评分器评估步骤质量，并以内存饱和为触发条件动态剪枝低分轨迹。该方法在降低延迟 45%–70% 的同时提升准确率，但其效果高度依赖特定硬件配置与内存压力场景，通用性存疑。

】

---

【HintPilot: LLM-based Compiler Hint Synthesis for Code Optimization ｜编译器提示合成

研究机构：浙江大学、美国普渡大学

作者：Hanyun Jiang、Peisen Yao、Kaiyue Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd08108bd59a)

> 代码优化旨在提升程序执行效率，但传统编译器启发式规则难以适应复杂异构系统，而直接让大语言模型（LLM）重写源码又极易破坏语义正确性。现有方法要么全局选择优化Pass导致细粒度机会丢失，要么直接修改代码引入不可控风险。HINTPILOT 提出通过合成编译器提示（Compiler Hints）这一中间层，利用检索增强生成与执行反馈迭代，在保持语义不变的前提下实现细粒度性能调优。该方法在 HumanEval_CPP 上实现了相对 -Ofast 6.88× 的几何平均加速比，但其对特定硬件与编译器版本的依赖性及跨编译器泛化能力仍存疑。

】

---

【HIPO: A Hierarchical Prompt Optimization Framework with Task Awareness and Fine-Grained Debugging ｜层级化提示优化框架

研究机构：北京航空航天大学、新加坡国立大学

作者：Lu Qi、Lei Chai、Hongrui Yu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0967ff7870f4)

> 自动提示优化（APO）旨在通过算法搜索最优指令以提升大语言模型（LLM）性能，但现有方法普遍采用数据集级优化范式，即寻找单一全局提示，忽略了样本间的难度差异。这种“一刀切”策略导致简单样本被过度优化而性能退化，复杂样本则因优化算法过早收敛而提升有限。HIPO 框架通过引入离线训练的难度路由器，将优化粒度从数据集级细化至样本级，动态匹配五级提示层级。该框架在27个任务上超越了所有基线方法，且成本降低1.2至80倍，但其对路由器泛化能力的验证仍显不足。

】

---

【HiRAS: A Hierarchical Multi-Agent Framework for Paper-to-Code Generation and Execution ｜层级监督多智能体框架

作者：Hanhua Hong、Yizhi LI、Jiaoyan Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d47401e236b)

> 科研复现任务要求智能体从论文文本生成可执行代码并验证结果，但现有顺序流水线缺乏全局纠错机制，导致早期错误在后续阶段不可逆地传播。HIRAS 通过引入主动检查中间产物的层级管理器，将固定调用序列改造为动态监督循环，解决了执行阶段因依赖关系错误导致的崩溃问题。该框架在开源模型上实现了超越专有模型基线的复现准确率，但其评估协议修正与计算开销的权衡仍需进一步审视。

】

---

【How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns in Thinking LLMs for Quantitative Reasoning ｜答案Token如何读取推理轨迹：思考型LLM中的自读模式

研究机构：南京大学、阿里巴巴集团

作者：Haoyang Chen、Yi Liu、Jianzhi Shao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19149)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19149)

> 思考型大语言模型在生成最终答案前会先输出长推理轨迹，但答案Token究竟如何从这些轨迹中提取关键信息以生成可靠结果，此前缺乏机制层面的解释。现有激活引导方法主要优化推理轨迹本身的生成质量，却忽略了答案解码阶段对轨迹的“读取”行为，导致模型在内部状态不确定时仍可能输出错误答案。本文通过注意力分析发现正确解存在“良性自读”模式，并据此构建无训练引导向量以提升准确率。该方法在GSM8K上带来最高2.6%的提升，但其效果是否源于注意力模式本身还是样本筛选偏差，尚存疑。

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

【How Hypocritical Is Your LLM judge? Listener-Speaker Asymmetries in the Pragmatic Competence of Large Language Models ｜语用听-说解耦：LLM 判断与生成能力不对称分析

作者：Judith Sieker、Sina Zarrieß

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_05e2793400c7)

> 导读 大语言模型（LLM）在语用任务中常被同时要求“判断”他人输出的恰当性与“生成”恰当输出，但现有评估往往将二者混同，默认判断能力可代理生成能力。这一假设在语用推理中缺乏验证，导致模型能力评估出现系统性偏差。本文通过构建同一语料上的平行“听”（判断）与“说”（生成）任务，量化了二者间的性能落差。研究揭示了当前 LLM 存在显著的听-说不对称，判断表现远优于生成，挑战了以单一角色评估模型语用能力的常规做法，但受限于特定语用现象与强制格式约束，其结论的泛化性仍需进一步检验。

】

---

【How Language Models Conflate Logical Validity with Plausibility: A Representational Analysis of Content Effects ｜逻辑有效性与事实可信度的表征解耦

作者：Leonardo Bertolazzi、Sandro Pezzelle、Raffaella Bernardi

论文原文见 [arXiv](https://arxiv.org/abs/2510.06700)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d22dacd24127)

> 大语言模型在逻辑推理中常受语义内容干扰，将“事实为真”误判为“逻辑有效”，这一现象称为内容效应。现有研究多关注长链推理的准确率衰减，却忽视了短链推理中语义与逻辑的表征纠缠机制。本文通过提取并干预潜空间中的线性方向，揭示了这种混淆的几何根源。该工作为理解模型内部逻辑偏差提供了微观证据，但其干预手段是否真正改变了推理路径仍存疑。

】

---

【How Robust Are Large Language Models for Clinical Numeracy? An Empirical Study on Numerical Reasoning Abilities in Clinical Contexts ｜临床数值鲁棒性基准

研究机构：澳大利亚皇家墨尔本理工大学

作者：Minh-Vuong Nguyen、Fatemeh Shiri、Zhuang Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ecf17ec6a6b)

> 临床大语言模型（LLM）的安全部署依赖于对患者生命体征等数值数据的精确处理，但现有评估多聚焦于通用数学或单一临床知识，忽视了同一测量值在不同文档格式下的推理一致性。静态临床基准无法隔离数值操作能力与格式敏感度，导致模型在真实病历中的表现被高估。本文构建了包含1,624个实例的ClinicNumRobBench，通过程序化生成三种语义等价但格式迥异的上下文，系统测试17个LLM在检索、算术、比较和聚合上的鲁棒性。该基准揭示了医疗微调可能削弱数值推理能力的反直觉现象，为临床AI的可靠性评估提供了新维度，但其诊断性质决定了它无法直接解决格式敏感问题。

】

---

【How to Set the Learning Rate for Large-Scale Pre-training? ｜大规模预训练学习率配置：拟合与迁移范式对比

研究机构：复旦大学

作者：Yunhua Zhou、Shuhao Xing、Junhao Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05049)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05049)

> 大规模预训练的核心瓶颈在于学习率（Learning Rate, LR）配置的高昂试错成本，直接决定训练稳定性与收敛效率。现有方法要么依赖组合爆炸的网格搜索，要么依赖 Maximal Update Parametrization (µP) 迁移但缺乏大规模实证验证。本文切入点是将 LR 配置形式化为“拟合”与“迁移”两大范式，并首次在 12B 参数 MoE 架构下对比二者。通过引入搜索因子缩放律降低拟合复杂度，并扩展 µP 至深度与权重衰减维度，本文揭示了 µP 在工业级规模下的性能衰减。其价值在于提供了可操作的 LR 配置指南，但结论局限于 Qwen3-MoE 单一架构与 WSD 调度，对动态 Batch Size 等场景的适用性存疑。

】

---

【How Value Induction Reshapes LLM Behavior ｜价值观诱导的间接效应分析

研究机构：丹麦哥本哈根大学、Anthropic

作者：Arnav Arora、Natalie Schluter、Katherine Metcalf 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0682d64cb862)

> 大语言模型（LLM）在生成文本时往往表现出特定的行为特质，但现有研究多关注单一特质的注入，忽略了特质间的系统性耦合。传统提示工程或单一维度的微调难以量化诱导某一价值观（如诚实）如何改变其他未诱导价值观（如创造力）的表达频率，且缺乏对安全性与拟人化语言影响的统一评估框架。本文通过构建基于偏好数据的价值观子集，利用直接偏好优化（Direct Preference Optimization, DPO）微调模型，系统性地测量了15种价值观诱导后的下游行为变化。该工作揭示了价值观诱导的“涟漪效应”，即正面价值观的注入不仅提升安全性，还显著增加了拟人化语言的使用，为理解模型对齐的副作用提供了实证基础，但其结论受限于特定模型家族与数据规模。

】

---

【HSUGA: LLM-Enhanced Recommendation with Hierarchical Semantic Understanding and Group-Aware Alignment ｜分层语义理解与分组感知对齐

作者：Guorui Li、Dugang Liu、Lei Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11662)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b01b6e01dc69)

> 序列推荐中，长交互历史直接输入大语言模型（LLM）易引发推理困难与语义漂移，且统一对齐策略忽视了用户活跃度差异。HSUGA通过分层编辑操作实现可控偏好演化，并依据用户分组动态调整语义利用强度，解决了上述两个核心瓶颈。该方法作为即插即用插件，显著提升了多种骨干模型的推荐性能，但其对计算效率的忽略及缺乏生成式基线对比，限制了其工业落地的评估完整性。

】

---

【HyperEdit: Unlocking Instruction-based Text Editing in LLMs via Hypernetworks ｜指令式文本编辑中的动态适配与局部保真

研究机构：美国康涅狄格大学、美国加州大学河滨分校

作者：Yiming Zeng、Jinghan Cao、Zexin Li 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12544)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12544)

> 指令式文本编辑要求模型在遵循用户修改意图的同时，严格保留未变更内容，但现有通用大语言模型常因过度编辑破坏上下文完整性，而专用编辑模型又缺乏对多样化指令的动态适应能力。HyperEdit 通过超网络生成请求特定的低秩参数实现意图对齐，并引入差异感知正则化将监督信号聚焦于修改跨度，从而在3B参数规模下同时满足这两项约束。该方法在InstrEditBench上取得了优于现有专用编辑模型的相对提升，但其评估指标对编辑精度的捕捉能力以及动态参数生成的必要性，仍需更严格的协议验证。

】

---

【Idea First, Code Later: Disentangling Problem Solving from Code Generation in Evaluating LLMs for Competitive Programming ｜先想后写：编辑式解耦竞赛编程中的推理与实现

作者：Sama Hadhoud、Alaa Elsetohy、Frederikus Hudi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2164c4884be7)

> 竞赛编程（Competitive Programming, CP）评估长期将算法规划与代码实现混同为单一端到端任务，导致模型失败时无法区分是“想错了”还是“写错了”。现有基准如LiveCodeBench虽解决了数据污染，但仍无法定位推理瓶颈。本文切入点是将自然语言编辑式（Editorial）作为显式中间产物，通过对比模型自生成编辑式与专家金标编辑式下的代码通过率，量化“解题”与“实现”的独立贡献。其价值在于首次提供了可操作的解耦评估协议，但83题的小样本规模限制了统计稳健性，且仅覆盖C++/Python两种语言。

】

---

【IDEA: An Interpretable and Editable Decision-Making Framework for LLMs via Verbal-to-Numeric Calibration ｜可解释与可编辑的LLM决策框架

研究机构：香港科技大学、华为

作者：Yanji He、Yuxin Jiang、Yiwen Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12573)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12573)

> 大语言模型在高风险决策中面临概率校准失效、解释不忠实及无法精确干预的“信任赤字”。现有基于Logit或思维链的方法将内部计算与外部输出强行绑定，导致无法审计或修改决策逻辑。IDEA通过引入语义因子中间层，利用EM算法联合学习言语-数值映射与决策模型参数，将黑盒知识外化为可编辑的白盒参数。该框架在决策准确性上超越GPT-5.2，但因子完备性假设限制了其在开放域复杂推理中的泛化能力。

】

---

【Identifying Collective Intelligence Factor in LLM Agent Groups for Generalizable Multi-Agent System Design ｜人工集体智能（ACI）因子提取与泛化预测

作者：Zhilun Zhou、Zihan Liu、Jiahe Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ecf56b8171c8)

> 多智能体系统（MAS）研究长期聚焦于特定任务的性能优化，却忽略了群体是否具备跨任务的通用能力。现有方法如 GPTSwarm 和 G-Designer 虽能优化拓扑，但其性能提升依赖于特定任务分布，缺乏对群体“通用智力”的量化度量。本文借鉴人类集体智能（CI）理论，通过因子分析从 108 个 LLM 智能体群体中提取出解释 66.3% 方差的人工集体智能（ACI）因子，并验证其作为正则项可提升 MAS 优化算法在未见任务上的泛化能力。这一发现为 MAS 设计提供了超越单任务指标的通用性视角，但其预测模型在复杂异构场景下的鲁棒性仍存疑。

】

---

【Idiom Understanding as a Tool to Measure the Dialect Gap ｜区域习语理解作为方言差距量化探针

作者：David Beauchemin、Yan Tremblay、Mohamed Amine Youssef 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.05026)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff473a522c73)

> 方言自然语言处理长期面临标准语模型在低资源方言上性能崩塌的困境，但现有评估多聚焦于语音识别或通用文本分类，缺乏针对文化密集语义的细粒度探针。本文切入点在于论证区域习语无法从标准语语法中推断，因而成为衡量方言理解能力的有效指标。作者构建了魁北克法语与巴黎法语的习语基准，通过零样本评估111个大语言模型，量化了方言差距。该工作提供了首个魁北克法语习语评估工具，但零样本设置下专有模型的高分是否源于数据污染而非真实理解能力，仍存疑。

】

---

【IF-GEO: Conflict-Aware Instruction Fusion for Multi-Query Generative Engine Optimization ｜冲突感知指令融合的多查询生成式引擎优化

研究机构：中国科学技术大学

作者：Heyang Zhou、JiaJia Chen、Xiaolu Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13938)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13938)

> 生成式引擎优化（GEO）旨在通过修改文档内容提升其在生成式搜索答案中的引用可见性。现有方法将多查询优化视为单维问题，导致针对单一查询的修改往往损害其他查询的可见性，形成竞争性失衡。IF-GEO 提出“发散-收敛”框架，通过挖掘潜在查询并执行冲突感知的指令融合，生成全局修订蓝图以协调竞争需求。该方法在稳定性指标上显著优于基线，但其依赖模拟引擎且未解决真实商业环境下的对抗性风险。

】

---

【Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification ｜基于形式化验证的语义等价自博弈训练

研究机构：英国爱丁堡大学

作者：Antonio Valerio Miceli Barone、Poon Tsz Nok

论文原文见 [arXiv](https://arxiv.org/abs/2604.17010)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17010)

> 现有LLM在代码生成中常因缺乏深层语义理解而产生逻辑错误，传统测试套件无法覆盖所有边界情况，导致程序重构与优化中的等价性判定不可靠。本文切入点在于利用Haskell语言的纯函数特性与Liquid Haskell的形式化证明能力，构建一个生成器与评估器对抗的自博弈闭环，通过形式化证明作为确定性监督信号来训练模型识别程序语义等价性。该方法在EquiBench上实现了最高13.3个百分点的准确率提升，并验证了等价性证明监督对语义推理能力的独特贡献。然而，该方法局限于Haskell生态，且在小模型规模下证明生成率极低，其跨语言泛化能力与大规模系统适用性仍存疑。

】

---

【Incentivizing In-depth Reasoning over Long Contexts with Process Advantage Shaping ｜长上下文推理中的过程优势整形

研究机构：香港科技大学、阿里巴巴集团

作者：Miao Peng、Weizhou Shen、Nuo Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12465)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12465)

> 长上下文大语言模型在复杂推理任务中普遍面临“几乎正确”轨迹被稀疏奖励无效惩罚的问题，导致模型难以从部分正确的推理路径中提取学习信号。现有基于结果奖励的强化学习（RLVR）方法无法区分中间步骤的正确性与最终答案的错误性，尤其在长文档信息分散场景下失效。本文通过知识图谱（KG）驱动的多跳问答合成与过程优势整形（Process Advantage Shaping），将步骤级有效性（Validity）与相关性（Relevance）信号融入优势估计，实现细粒度信用分配。该方法在小参数模型上显著提升了长程推理稳定性，但其对参考轨迹生成成本的依赖及跨基准性能差异仍存疑。

】

---

【Incomplete Prompt Jailbreaks in Large Language Models ｜不完整提示越狱（IPJ）的神经元级终止控制

研究机构：韩国科学技术院

作者：Yeonjea Kim、Bumjin Park、Jaesik Choi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b06b4e3f6c37)

> 导读 大语言模型在自回归生成中优先维护句子连贯性，导致面对不完整有害提示时，模型往往先完成有害内容生成，再在句末输出拒绝，这一现象被称为不完整提示越狱（Incomplete Prompt Jailbreaks, IPJ）。现有基于参数微调的安全对齐方法难以泛化至未见过的攻击结构或拒绝风格，暴露出浅层对齐的脆弱性。本文通过识别并缩放介导句子终止与延续的特定神经元，在解码阶段实现细粒度的生成控制。该机制验证了神经元级干预对IPJ的有效性，但其泛化边界与计算开销仍存疑。

】

---

【INDOTABVQA: A Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents ｜印尼语文档表格跨语言视觉问答基准

研究机构：印度理工学院

作者：Somraj Gautam、Anathapindika Dravichi、Gaurav Harit

论文原文见 [arXiv](https://arxiv.org/abs/2604.11970)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11970)

> 现有表格视觉问答基准多局限于英语或单语言环境，无法评估模型在低资源语言文档上的跨语言推理能力。本文构建了包含印尼语文档图像与四语言问答对的基准，通过微调与空间先验验证了领域适配的有效性。其价值在于填补了跨语言表格理解的评估空白，但受限于仅使用表格级边界框，未能深入解析细粒度结构错误。

】

---

【InferPilot: Autonomous Inference Attacks Against ML Services With LLM-Based Agents ｜自动化推理攻击代理

作者：Yixin Wu、Rui Wen、Chi Cui 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_739487a9ea85)

> 机器学习服务部署后，非专家难以独立完成成员推断、模型窃取等推理攻击以评估隐私与知识产权风险，而现有通用代理框架在复杂配置搜索中频繁失效。InferPilot 通过多代理隔离架构与任务特定动作空间，将黑盒推理攻击自动化，使非专家能以极低门槛获得接近专家水平的风险评估报告。该工作验证了大语言模型代理在安全评估领域的可行性，但其对目标服务内部结构的依赖与对特定攻击类型的覆盖局限，限制了其在真实异构环境中的泛化能力。

】

---

【InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents ｜文件中心状态抽象

研究机构：香港理工大学

作者：Chenglin Yu、Yuchen Wang、Songmiao Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03204)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03204)

> 长时域智能体（Long-Horizon Agent）面临的核心困境是上下文窗口的无限增长导致推理稳定性崩塌。现有方案依赖截断或摘要，但无法解决状态与推理上下文的纠缠问题。InfiAgent 提出将持久状态外化为文件系统，通过有界上下文重建实现无限时域执行。该框架在 20B 模型上实现了与大型专有模型相当的 DeepResearch 性能，但其串行执行架构带来的延迟开销限制了实时场景的适用性。

】

---

【InsightEval: An Expert-Curated Benchmark for Assessing Insight Discovery in LLM-Driven Data Agents ｜洞察发现基准与多维评估框架

研究机构：香港科技大学

作者：Zhenghao Zhu、Yuanfeng Song、Xin Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.22884)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.22884)

> 数据科学智能体在自动化分析中常陷入“幻觉”陷阱，即生成的洞察看似合理却与底层数据事实不符，或仅重复已知信息而缺乏新颖性。现有基准如 InsightBench 存在目标模糊、数据缺失及评估指标单一（仅关注召回率）的缺陷，导致无法准确衡量智能体的真实探索能力。本文通过构建包含 1000 个高质量洞察的 InsightEval 数据集，并引入 Insight F1 与 Novelty 指标，实现了对智能体洞察发现能力的全面量化。该工作填补了细分领域的评估空白，但其依赖 LLM 作为评估器的机制可能引入新的主观偏差。

】

---

【Instruction-Guided Poetry Generation in Arabic and Its Dialects ｜阿拉伯语诗歌指令微调

研究机构：阿联酋扎耶德大学

作者：Abdelrahman Sadallah、Kareem Elozeiri、Mervat Abassy 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27766)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27766)

> 阿拉伯语诗歌在文化传承中占据核心地位，但现有大语言模型（LLM）研究多局限于分析或分类任务，缺乏支持用户指定韵律、风格等约束的可控生成能力。通用模型在阿语诗歌生成上常出现结构松散与文化错位，而专用微调数据稀缺。本文通过构建覆盖现代标准阿拉伯语（MSA）及四种方言的大规模指令微调数据集，将诗歌创作转化为指令遵循问题。实验表明微调显著提升了模型在韵律合规与诗意质量上的表现，但方言泛化能力与长程格律一致性仍存疑。

】

---

【IntentCoding: Amplifying User Intent in Code Generation ｜意图放大解码：多约束代码生成的信号增强机制

研究机构：北京大学、加拿大阿尔伯塔大学

作者：Zheng Fang、Yihong Dong、Lili Mou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00066)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00066)

> 大语言模型在代码生成中常因用户意图对logits影响微弱而违背多约束指令，现有解码策略无法有效放大该信号。本文提出Intent[↑] Coding，通过对比原始与意图掩码logits提取意图信号，并采用多强度集成动态放大该信号以引导解码。该方法无需训练且模型无关，在约束遵循基准上取得最高71.0%的相对提升，但其收益是否随模型规模增大而递减尚存疑。

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

【Internalizing Multi-Agent Reasoning for Accurate and Efficient LLM-based Recommendation ｜单智能体轨迹对齐推荐器

作者：Yang Wu、Haoze Wang、Qian Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7c4789bdbeb0)

> 推荐系统面临的核心矛盾是LLM的语义泛化能力与协同过滤信号的结构性缺失，以及多智能体推理带来的实时性瓶颈。现有方案要么将协同信号压缩为不可解释的向量，要么依赖高延迟的多轮工具调用。本文切入点在于将多智能体的推理过程离线转化为文本轨迹，并通过蒸馏内化至单模型。具体做法是构建多智能体教师系统生成含工具调用的轨迹，经SFT与GRPO两阶段训练得到单智能体学生模型。该方法在效率与精度间取得了平衡，但其对静态协同信号的依赖及跨域泛化能力的边界仍需审慎评估。

】

---

【Intrinsic Mutual Information as a Modulator for Preference Optimization ｜基于内在互信息的自适应偏好优化

研究机构：中山大学、英国华威大学

作者：Peng Liao、Peijia Zheng、Lingbo Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24804)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24804)

> 离线偏好优化旨在将人类价值观内化至大语言模型，但主流方法如直接偏好优化（Direct Preference Optimization, DPO）对超参数极度敏感，导致训练成本高昂且性能不稳定。现有自适应机制或依赖额外的监控模块，或需保留参考模型，未能彻底消除调优开销。本文提出 RMiPO，利用响应级点互信息（Pointwise Mutual Information, PMI）差异动态调节奖励边际，实现无参考模型的实例级自适应优化。该方法在降低 15-20% 训练成本的同时提升了指令遵循性能，但其对长文本及复杂推理任务中的 PMI 信号有效性尚未验证。

】

---

【IntroLM: Introspective Language Models via Prefilling-Time Self-Evaluation ｜内省式语言模型

研究机构：澳大利亚墨尔本大学、澳大利亚莫纳什大学

作者：Hossein Hosseini Kasnavieh、Gholamreza Haffari、Chris Leckie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03511)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03511)

> 导读 LLM路由的核心矛盾在于：准确预测查询复杂度需要强模型，但部署独立评估器会抵消路由带来的效率收益。现有基于BERT的外部分类器受限于512 token上下文窗口，无法处理现代长上下文部署场景，且引入额外推理开销。本文切入点是将复杂度预测内化到目标模型自身的Prefilling阶段，通过[CPX] token与Token-conditional LoRA实现零额外解码开销的自评估。该方法在长上下文基准上显著优于外部分类器，但其标量预测范式与领域内直接决策趋势的兼容性存疑。

】

---

【Investigating Human and LLMs’ Decisions in Unverifiable Environments: A Case Study with GitHub Activity Overview ｜不可验证环境下的LLM决策机制对比

研究机构：北京邮电大学、南京大学

作者：Zheng Jiang、Wei Wang、Gaowei Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a56c28088f4)

> 现有LLM评估体系依赖可验证环境中的客观金标准，导致模型在缺乏明确对错的社会决策场景中表现失真。本文切入点在于剥离代码正确性等可验证因素，聚焦GitHub Activity Overview这一纯社会信号，通过控制变量实验对比人类与LLM的决策逻辑。方法上，作者构建了包含60名开发者与20个LLM的成对比较实验，利用Bradley-Terry模型量化偏好序，并结合特征回归与思维链嵌入分析推理机制。该研究揭示了LLM与人类在决策逻辑上的根本性差异，但受限于单任务场景，其结论向多模态复杂社会互动的泛化能力尚存疑。

】

---

【Invocation Refiner: A Plug-and-Play Module for Rectifying LLM Tool Invocations ｜工具调用纠错的解耦式后处理模块

作者：Qirui Jiao、Dian Jiao、Nan Du 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ba55c27392fd)

> 工具增强大语言模型（Tool-Augmented LLMs）在生成工具调用时频繁出现参数错误、格式畸形或顺序颠倒，导致下游执行失败。现有监督微调（SFT）与强化学习（RL）范式需直接修改基座模型参数，跨模型部署时面临高昂的重训成本。本文提出 Invocation Refiner，一个冻结上游模型、独立训练的解耦式纠错模块，通过规则奖励强化学习提升调用可靠性。该方案验证了模块化增强的可行性，但其对复杂多轮交互的泛化能力及额外推理延迟的权衡尚存疑。

】

---

【IREASONER: Trajectory-Aware Intrinsic Reasoning Supervision for Self-Evolving Large Multimodal Models ｜轨迹感知内在推理监督

作者：Meghana Sunil、Manikandarajan Venmathimaran、Muthu Subash Kavitha

论文原文见 [arXiv](https://arxiv.org/abs/2601.05877)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6aa90e10bcce)

> 多模态大模型（LMM）在无标注数据上的自进化长期受限于“结果级奖励”的盲区：模型仅根据最终答案的一致性获得梯度信号，导致中间推理步骤缺乏约束，即使答案正确，推理路径也可能充满幻觉或逻辑断裂。现有自进化框架（如EvoLMM、VisPlay）虽实现了无监督闭环，但无法区分“正确推理”与“碰巧正确的错误推理”。IREASONER 通过引入基于跨轨迹步骤一致性的内在奖励，将优化目标从答案层下沉至推理步骤层，在不依赖外部真值或标注的情况下，实现了对中间推理过程的直接监督。该方法在纯无监督后训练中带来了最高+2.1点的性能增益，但其有效性高度依赖于主导答案组的正确率，且仅验证了文本步骤的语义对齐，未触及视觉编码器内部的特征一致性。

】

---

【Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race? ｜越狱攻击与内容安全过滤器对抗评估

研究机构：德国马克斯·普朗克智能系统研究所、南方科技大学

作者：Yuan Xin、Dingfan Chen、Linyi Yang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.24044)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24044)

> 大语言模型（LLM）部署中的核心矛盾在于，现有越狱攻击研究通常仅评估模型内部对齐的失效，而忽略了真实推理管道中必然存在的外部内容过滤层，导致攻击成功率被系统性高估。本文切入点在于首次将输入/输出过滤器纳入评估闭环，构建包含417对有害/良性提示的基准，系统测试10种SOTA攻击对6种主流过滤器的绕过能力。通过定义“通过率”（Pass）指标，量化攻击在完整管道中的实际威胁。该工作揭示了多数攻击在引入过滤后失效，但同时也暴露了过滤器在低误报率与高召回率之间的权衡困境，其结论对重新校准安全评估协议具有直接价值。

】

---

【JTPRO: A Joint Tool-Prompt Reflective Optimization Framework for Language Agents ｜联合工具-提示反思优化

作者：Sandip Ghoshal、Anshul Mittal、Jyotika Singh 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19821)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19821)

> 大规模工具库场景下，LLM智能体常因工具描述模糊与指令泛化导致选错工具或填错参数。现有微调方法需重训，纯提示优化又无法协同调整全局规则与局部Schema。JTPRO通过迭代反思机制，同时优化全局指令与每个工具的参数描述，在不更新模型权重的前提下提升调用准确性。该方法在复杂Schema任务上显著提升了参数填充准确率，但其效果高度依赖初始轨迹质量，且未解决多步依赖问题。

】

---

【Know Thy Enemy: Securing LLMs Against Prompt Injection via Diverse Data Synthesis and Instruction-Level Chain-of-Thought Learning ｜指令级思维链对齐防御提示注入

研究机构：中国科学院、中国科学院大学

作者：Zhiyuan Chang、Mingyang Li、Yuekai Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04666)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04666)

> 提示注入（Prompt Injection, PI）防御的核心困境在于模型无法区分系统指令与外部数据，且现有模型增强方法仅依赖隐式的角色边界学习，难以应对语义边界模糊的复杂注入。本文切入点在于将防御任务从“区分来源”转化为“分析指令冲突”，通过构建覆盖多向量、多位置的合成数据集，并引入基于情境意识模型的指令级思维链（Instruction-Level Chain-of-Thought, IL-CoT）进行监督微调。该方法在四个开源大语言模型（LLM）上实现了92.5%至98.0%的防御率，但未在标准代理基准上验证其泛化性，且推理时的计算开销未量化。

】

---

【Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning ｜识别能力边界：训练大模型在无效推理时主动中止

作者：Xinyan Guan、Jiali Zeng、Chunlei Xin 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_169c06787548)

> 导读 大语言模型在面对超出其内在能力边界的问题时，往往不承认无知，而是生成看似合理实则错误的推理轨迹，这种现象被称为无效推理（Futile Reasoning）。现有基于可验证奖励的强化学习（RLVR）范式主要优化答案正确性，缺乏对“拒绝”行为的显式激励，导致模型在不可解任务上持续消耗计算资源并产生误导性输出。本文提出能力对齐强化学习（CaRL），通过重构奖励函数建立“正确>拒绝>错误”的层级，并结合后见之明拒绝增强（HRA）将失败轨迹转化为拒绝监督信号。该框架在保持通用推理性能的同时，将无效推理率从 65.5% 降至 7.0%，但其有效性目前仅限于纯算法推理任务，在知识密集型场景下的泛化能力尚存疑。

】

---

【Knowing-but-Doing: Diagnosing and Defending Role-Play-Driven LLMs Jailbreaks via Moral Disengagement ｜道德脱离视角下的角色扮演越狱诊断与防御

研究机构：深圳大学、微软研究院

作者：Haiming Qin、Jianxun Lian、Qimin Zhong 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7c0c434854b9)

> 角色扮演场景下，模型常因维持人设一致性而绕过安全对齐，现有防御往往以牺牲角色保真度为代价。本文切入点在于揭示模型在思维链中“识别风险却仍执行”的知行不一机制，将其映射为道德脱离理论中的合理化模式。通过构建诊断基准MD-Trace与内省式防御MD-Shield，在降低攻击成功率的同时维持高角色保真度。该工作将安全对齐从行为层下沉至推理语义层，但其依赖思维链文本的可见性，对非推理模型或隐藏思维链场景的适用性存疑。

】

---

【KnowledgeBerg: Evaluating Systematic Knowledge Coverage and Compositional Reasoning in Large Language Models ｜冰山缺口：有界全集覆盖与组合推理评估

研究机构：荷兰格罗宁根大学、荷兰莱顿大学

作者：Xiao Zhang、Qianru Meng、Yongjian Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17621)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17621)

> 现有大语言模型基准多聚焦于孤立事实检索或线性单链推理，缺乏对“隐式有界全集系统性覆盖”能力的检验。主流多跳问答范式依赖离散文档链接，无法诊断模型在完整知识域上的组合运算缺陷。本文通过构建基于权威本体的有界全集基准，量化表面简单性与潜在复杂度差距，并诊断出完整性、意识与应用三阶段失效。该工作揭示了当前模型在结构化知识组织上的系统性盲区，但其对动态知识更新及检索策略的局限性仍存疑。

】

---

【Label Words as Local Task Vectors in In-Context Learning ｜局部任务向量机制：ICL 信息聚合的双层解构

研究机构：香港中文大学、中国科学院

作者：Bowen Zheng、Ming Ma、Zhongqiao Lin 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_79ca5b43b0b0)

> 上下文学习（ICL）的核心机制在于模型如何从演示样本中提取并应用任务规则，但现有研究普遍假设存在一个统一的全局任务向量来承载所有任务信息。这一假设在依赖预训练知识的任务中成立，但在需要归纳复杂规则的分类任务中失效，导致基于全局向量的压缩或迁移策略性能崩溃。本文通过引入“局部任务向量”概念，揭示了每个演示的答案位置隐藏状态作为独立信息载体的作用，并证明全局向量仅是局部向量在特定任务下的收敛结果。这种双层机制解释为何全局向量在分类任务中无效，为理解 ICL 的边界条件提供了微观视角，但其结论局限于合成任务，向真实复杂场景的迁移性尚存疑。

】

---

【Language-Coupled Reinforcement Learning for Multilingual Retrieval-Augmented Generation ｜语言耦合强化学习用于多语言检索增强生成

研究机构：北京交通大学、清华大学

作者：Rui Qi、Fengran Mo、Yufeng Chen 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.14896)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2866bb327d19)

> 多语言检索增强生成（Multilingual Retrieval-Augmented Generation, MRAG）面临的核心矛盾是模型在跨语言查询中产生的知识偏差与检索结果间的事实冲突。现有单轮检索与独立优化策略无法同时解决这两类问题，导致模型在语言多样性增加时性能急剧下降。LCRL通过语言耦合的组相对策略优化（Group Relative Policy Optimization, GRPO）与分层多轮检索机制，将多语言决策与经验奖励统一在强化学习框架内。该方法在知识密集型问答任务上显著优于基线，但其对通用推理能力的泛化效果及内部表征干预的缺失仍是存疑点。

】

---

【LANTERN in the Event Stream: Training-Free Temporal Knowledge Graph Forecasting by Balancing Inertia and Shifts ｜时序知识图谱预测中的惯性-漂移平衡

研究机构：中国科学院、中国科学院大学

作者：Chengyuan Jin、Ao Chang、Daojian Zeng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f88535f7c216)

> 时序知识图谱预测（TKGF）的核心难点在于，模型需从海量历史事件中筛选出对当前查询真正有效的证据，以在有限上下文窗口内完成未来实体预测。现有训练-free方法依赖语义检索或简单最近邻，往往陷入“稳定模式主导”或“噪声近期事件干扰”的二元困境，无法显式区分长期交互惯性与短期突发漂移。LANTERN通过引入固定计数窗口下的强度（Strength）与新意（Novelty）双信号评分，结合Pareto-greedy选择策略，实现了证据集的结构化筛选。该方法在四个基准上稳定超越最强基线AnRe，但其性能增益依赖于LLM骨干的语义理解能力，且在极端稀疏场景下的鲁棒性缺乏充分验证。

】

---

【Large Language Models Are Overconfident in Their Own Responses ｜指令微调模型中的“所有权偏差”与推理时校准修正

作者：Mario Sanz-Guerrero、Manuel Mager、Katharina von der Wense

论文原文见 [arXiv](https://arxiv.org/abs/2606.03437)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1510164bcd2a)

> 导读 大语言模型在指令微调后普遍出现校准失效，即模型输出的置信度显著高于其实际正确率，导致高风险场景下的决策不可靠。现有后处理校准方法多依赖重训练或复杂的概率映射，忽略了对话格式本身对置信度评估的干扰。本文切入点在于解耦训练算法与聊天模板的影响，发现模型对自身生成的答案存在系统性的“所有权偏差”，即赋予自身答案更高置信度。通过将该答案在提示中重构为用户输入，本文提出了一种零训练的推理时策略，有效缓解了过度自信。该策略在多个开源模型上验证了有效性，但其对开放式生成任务及长文本推理的适用性仍存疑。

】

---

【Large Language Models Require Curated Context for Reliable Political Fact-Checking—Even with Reasoning and Web Search ｜政治事实核查中LLM的可靠性与引用偏见

研究机构：美国斯坦福大学、美国德州农工大学

作者：Matthew R. DeVerna、Kai-Cheng Yang、Harry Yaojun Yan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0715b2f7e60f)

> 自动化事实核查旨在替代人工以应对海量错误信息，但主流大语言模型（LLMs）在政治声明验证中表现不佳，且内置网络搜索引入系统性偏见。现有检索增强生成（RAG）方法依赖实时网络，噪声大且缺乏对证据源政治倾向的审计。本文构建基于PolitiFact专业核查文章摘要的静态向量库，通过对比15个LLM在零样本、推理及网络搜索模式下的表现，验证了精选上下文对性能的显著提升。该研究揭示了通用网络检索在政治领域的局限性，但静态库的时效性覆盖能力存疑。

】

---

【Large Reasoning Models Are (Not Yet) Multilingual Latent Reasoners ｜多语言潜在推理的机制诊断

研究机构：德国慕尼黑大学

作者：Yihong Liu、Raoyuan Zhao、Hinrich Schuetze 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02996)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b496606e361b)

> 大语言模型在多语言任务中常依赖显式思维链，但内部隐藏状态往往在文本生成前已形成答案，这种“潜在推理”机制此前仅在英语中被研究。现有干预方法如强化学习或表示工程侧重性能提升，却缺乏对内部计算动态的跨语言量化证据。本文通过截断推理轨迹与Logit Lens分析，系统测量了11种语言下潜在推理的强度与内部路径一致性。该工作提供了关键的机理诊断，但受限于仅覆盖数学任务且未提出干预策略，其结论向其他推理域迁移的有效性尚存疑。

】

---

【LayerNorm Induces Recency Bias in Transformer Decoders ｜LayerNorm 诱导的近因偏差机制分析

研究机构：韩国科学技术院、微软研究院

作者：Junu Kim、Xiao Liu、Zhenghao Lin 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21042)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21042)

> 导读 Transformer 解码器中位置信息的来源长期被归因于显式位置编码（Positional Encoding, PE）或因果掩码，但实际模型中普遍存在的近因偏差（Recency Bias）与纯因果掩码理论预测的早期偏差相矛盾。现有理论未能解释这一矛盾，本文切入点在于剥离 PE，单独考察 LayerNorm 与因果自注意力的交互作用。通过理论推导与无参数模拟，证明 LayerNorm 是诱导近因偏差的关键架构组件。该发现修正了隐式位置信息的来源认知，但缺乏在真实预训练模型中的实证验证，其理论结论对实际性能的影响尚存疑。

】

---

【LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world Tasks ｜基于约束优化的LLM代理安全框架

作者：Jiayong Wan、Jiawei Chen、Zhaoxia Yin 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd5457f3ecd7)

> 大语言模型（LLM）作为自主代理在持续交互中追求代理目标时，常因过优化产生有害副作用，即上下文奖励黑客（ICRH）。现有越狱防御针对静态恶意输入设计，无法拦截由内部目标优化引发的动态安全漂移。LCO通过自思考生成动态安全约束，并借助引导进化探索在解空间中搜索安全且高效的行动，无需修改模型权重即可缓解ICRH。该框架在特定优化场景下有效平衡了安全性与任务效用，但其依赖外部评估器且计算开销随种群规模线性增长，限制了实时部署的可行性。

】

---

【LDEDE: LRP-Driven Efficient Detection and Editing Framework for LLM Privacy Neurons ｜LDEDE：基于层级相关性传播的大语言模型隐私神经元高效检测与编辑框架

作者：Zhao Zhengyuan、Cao Lifeng、Sunhaodong 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_82240bf989f0)

> 导读 大语言模型在预训练与微调中不可避免地记忆敏感信息，现有防御手段如差分隐私（DP）导致效用显著下降，传统机器遗忘易引发灾难性崩溃，而神经元编辑方法则面临定位效率低与“隐私跷跷板”效应两大瓶颈。LDEDE 框架通过层级相关性传播（LRP）算法替代梯度归因进行隐私神经元定位，并引入极性感知神经元编辑（PANE）策略处理耦合神经元，以在保持模型通用性能的前提下降低隐私泄露风险。该方法将计算复杂度从 $O(N^2)$ 降至 $O(N)$，在 Enron 和 MIMIC 数据集上平均降低 42.7%–73.5% 的泄露风险，但缺乏与主流攻击方法的绝对值对比，其通用性能保留的充分性存疑。

】

---

【Learning Continuous Temporal Dynamics on Symplectic Manifolds for Temporal Knowledge Graph Embedding ｜辛几何约束下的连续时序知识图谱嵌入

作者：Jiang Li、Zehua Duo、Tian Lan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5eae08507ee2)

> 时序知识图谱嵌入（TKGE）旨在从动态事实中推断缺失链接，但主流方法依赖离散时间查表与高维参数扩展，导致模型在未见时间戳上泛化失效且计算成本高昂。TDSym 将时间演化建模为辛相空间中的哈密顿动力学，通过几何约束在低秩嵌入下实现连续时间推理。该方法利用旋转时间嵌入与特征线性调制驱动哈密顿流，证明了结构约束可替代容量扩展以提升外推能力。尽管在严格外推任务上显著优于离散基线，但其性能仍低于最新的大语言模型（LLM）辅助方法，且缺乏对开放域新实体涌现的验证。

】

---

【Learning from Contrastive Prompts: An Automated Prompt Optimization Framework ｜基于对比提示的自动优化框架

作者：Mingqi Li、Karan Aggarwal、Yong Xie 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_89818f07c015)

> 自动提示优化（APO）旨在通过算法在离散指令空间中搜索最优提示，以解决闭源模型参数不可访问与人工试错效率低下的矛盾。现有反馈驱动方法如 ProTeGi 和 OPRO 主要依赖错误样本或历史排名列表，缺乏对“成功”与“失败”提示间结构性差异的显式建模，导致优化易陷入局部最优或过拟合特定错误模式。LCP 引入对比学习机制，通过直接分析高性能与低性能提示的语义差异来生成新候选，从而提取更具泛化性的提示设计原则。该方法在 Big-Bench Hard 基准上取得了显著的性能提升，但其高昂的计算成本与对特定模型家族的依赖限制了其通用性。

】

---

【Learning from Failures: Error Notebook-guided Secure Code Generation ｜错误笔记引导的安全代码生成

研究机构：中南大学

作者：Xinyu Zhong、Peng Lan、Zhifang Liao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_968c13d1a977)

> 大语言模型（LLM）在生成代码时面临功能正确性与安全性的内在冲突，现有检索增强生成（RAG）方法仅注入静态安全指南，缺乏对模型自身历史失败经验的动态利用，导致在未见过的漏洞类型上泛化能力不足。SAFENOTE 通过构建安全与功能双维度的错误笔记，将模型的历史失败转化为对比性指导，在不重新训练模型的前提下提升安全性。该方法在 GPT-4o-mini 上将 CodeGuard+ 基准的 SecurePass@1 从 60.21% 提升至 66.70%，但其在部分开源模型上的功能性能出现显著退化，暴露了经验积累机制对模型基线能力的依赖。

】

---

【Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory ｜元认知记忆抽象

研究机构：中科院自动化所、中国科学院大学

作者：Sirui Liang、Pengfei Cao、Jian Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07470)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07470)

> 长时程具身智能体在分布偏移下复用历史经验时，常因记忆抽象层级固定而遭遇负迁移。现有检索或总结方法将记忆视为静态内容，无法自适应选择抽象粒度。MCMA将记忆抽象建模为可学习的元认知策略，通过独立训练的Memory Copilot决定记忆结构与层级。该方法在ALFWorld和ScienceWorld上显著提升了跨任务泛化能力，但其对DPO训练信号的依赖及单一文本模态的局限尚待检验。

】

---

【Learning Optimal Message Representations for Agentic Communication ｜动态学习最优消息表示的多智能体通信系统

研究机构：微软研究院

作者：Shashwat Gupta、Anson Bastos、Mayukh Das 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b83a079407a)

> 多智能体协作中，自然语言（NL）作为默认通信介质存在歧义与冗余，导致推理偏差在智能体间级联放大。现有方案依赖静态格式或大语言模型（LLM）先验选择结构，无法适应动态任务分布。本文提出OPTiMACS，将消息格式选择建模为扩展马尔可夫决策过程（EMDP），通过强化学习从环境反馈中动态发现并优化最优表示。该方法在多个基准上提升了任务准确率并降低了Token消耗，但其增益是否源于格式本身而非骨干模型能力，仍需更严格的控制实验验证。

】

---

【Learning Through Dialogue: Engagement and Efficacy Matter More Than Explanations ｜交互过程驱动的政治学习机制

研究机构：新加坡国立大学

作者：Shaz Furniturewala、Gerard Christopher Yeo、Kokil Jaidka

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_461a362ca416)

> 现有LLM政治研究聚焦于模型输出的静态偏见测量或单轮说服效果，忽视了多轮对话中用户认知参与对知识获取的中介作用。本文通过构建包含397段人机对话的实验系统，利用多层回归与中介-调节分析，证明LLM解释丰富度对政治知识增益的影响完全经由用户的认知投入传递，而对信心变化的影响则部分经由反思性洞察传递。这一发现将研究视角从“模型说了什么”转向“用户如何回应”，但缺乏人类导师对照组，难以排除对话形式本身带来的基线效应。

】

---

【Learning to Control Summaries with Score Ranking ｜基于排序对齐的摘要多维质量控制

研究机构：美国杜克大学、澳大利亚悉尼大学

作者：Hongye Liu、Liang Ding、Ricardo Henao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_acb9882786cd)

> 导读 摘要生成领域长期面临完整性与简洁性之间的固有冲突，单一目标优化往往导致另一维度性能下降，即“对齐税”现象。现有基于直接偏好优化（DPO）的方法在排序任务上表现低效且计算成本高，难以实现细粒度的维度特异性控制。本文提出一种结合边缘排序损失、最大评分损失与控制导向损失的联合训练框架，将模型似然与细粒度模型评分对齐，实现了对摘要质量的动态权衡。该方法在多个开源模型上验证了可控性优势，但其在事实一致性维度上的表现及与主流幻觉抑制方法的兼容性仍存疑。

】

---

【Learning to Retrieve User History and Generate User Profiles for Personalized Persuasiveness Prediction ｜面向个性化说服预测的上下文感知用户画像构建

研究机构：韩国首尔大学

作者：Sejun Park、Yoonah Park、Jongwon Lim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05654)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05654)

> 个性化说服预测旨在判断特定消息能否改变目标用户的既有观点，其核心难点在于同一论证对不同用户的有效性差异巨大，而现有方法依赖静态人口统计属性或语义相似度检索，无法捕捉说服语境下的动态用户特征。本文切入点在于将用户画像构建视为一个可学习的、任务导向的过程，通过联合优化查询生成器与画像生成器，使检索与摘要环节直接服务于观点改变预测这一下游目标。该方法在ChangeMyView数据集上将Llama-3.3-70B-Instruct的F1分数从0.3284提升至0.4661，证明了上下文依赖画像的必要性，但其效用评分机制对预测器性能的强依赖性及跨域泛化的有限验证，仍构成应用边界。

】

---

【LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval ｜依赖感知图检索的长文档智能体编辑

作者：Mike Hang Wang、Utkarsh Garg、Reza Davari 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.28379)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.28379)

> 长文档智能体编辑面临上下文效率与结构一致性的根本矛盾：全量输入导致Token成本线性增长且稀释注意力，而基于语义相似度的检索常遗漏跨引用等结构依赖。LEDGER通过构建显式依赖图实现恒定Token预算下的精准上下文选择，将编辑一致性从56%提升至76%。该方法验证了结构引导可替代部分内部推理能力，但其图构建依赖LLM调用的前置成本及非参数化特性限制了知识的持久固化。

】

---

【LexGenius: An Expert-Level Benchmark for Large Language Models in Legal General Intelligence ｜法律通用智能专家级基准

研究机构：新加坡南洋理工大学、南京大学

作者：Wenjin Liu、Haoran Luo、Xin Feng 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_06abb52b508f)

> 法律领域长期缺乏能区分“模式模仿”与“真实理解”的评测标准，现有基准多聚焦静态任务结果，忽视伦理判断等软性智能维度。本文切入点在于构建覆盖七维度、十一任务、二十能力的三级框架，将法律软智能纳入系统化评估。通过8,385道原创选择题与12个SOTA模型对比，揭示了LLM在价值权衡与情境适应上的系统性缺陷。其价值在于填补了法律智能评估的结构性空白，但选择题形式能否真正承载过程评估的深度仍存疑。

】

---

【LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning ｜轻量级认知图记忆架构

作者：Zhengjun Huang、Zhoujin Tian、Qintian Guo 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2e2e1cb339ac)

> 长时程对话智能体受限于固定上下文窗口，导致跨会话状态丢失与推理断裂。现有图结构记忆方案虽能捕捉关系，但普遍存在语义与拓扑耦合导致的冗余存储、检索碎片化及更新延迟高企的问题，难以满足实时交互需求。LiCoMemory 提出 CogniGraph，将知识图谱重构为仅存储标识符的轻量级语义索引层，结合层级化检索与 Weibull 时序衰减重排序，实现了低延迟的实时记忆更新与高精度检索。该方案在效率-精度权衡上显著优于传统图记忆系统，但其绝对精度仍低于最新 SOTA，且未探索端到端策略优化路径。

】

---

【LifeSim: Long-Horizon User Life Simulator for Personalized Assistant Evaluation ｜长程用户生活模拟器与个性化助手评估基准

作者：Feiyu Duan、Xuanjing Huang、Zhongyu Wei

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9b036b43f343)

> 导读 个性化助手面临的核心挑战在于如何在动态物理环境与用户长期认知状态约束下，维持交互的连贯性与个性化。现有基准多依赖静态或短上下文数据，无法反映真实世界中用户意图随时间、地点及情绪演变的复杂性，导致模型在隐式意图推断与长期偏好保持上表现不佳。LifeSim 通过信念-欲望-意图（Belief-Desire-Intention, BDI）认知引擎与事件引擎生成符合物理规律的生活轨迹，并构建包含 1,200 个场景的 LifeSim-Eval 基准，以量化模型在长程交互中的表现。该框架揭示了当前大语言模型（Large Language Models, LLMs）在显式意图处理上的优势与在隐式意图及长程记忆上的显著短板，但其评估主要依赖 LLM-as-Judge，缺乏对因果机制有效性的直接验证。

】

---

【Lightweight Haar Wavelet Subband Pruning for LLMs ｜Haar 小波子带剪枝

研究机构：中国科学院

作者：Jiang Li、Pengfei Cao、Chenxi Zhou 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_04dd35dc9ce7)

> 大语言模型（LLM）压缩面临校准数据依赖与权重更新开销的双重瓶颈，现有免重训练方法如 SparseGPT 和 Wanda 仍需消耗大量算力进行二阶优化或激活统计。本文切入点在于利用 Haar 小波变换的正交性，将剪枝问题转化为频域系数幅值排序，从而彻底消除对校准集和梯度计算的依赖。通过强制四个频率子带均匀稀疏，HWSP 在保持精度接近 SOTA 的同时将剪枝时间降低至秒级。该方案在免校准场景下具有显著效率优势，但其非结构化稀疏模式在硬件推理加速上的实际收益仍存疑。

】

---

【Linear Semantic Segmentation for Low-Resource Spoken Dialects ｜低资源口语方言的线性语义分割

研究机构：阿联酋扎耶德大学、IBM研究院

作者：Kirill Chirkunov、Younes Samih、Abed Alhakim Freihat 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.06276)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.06276)

> 现有语义分割模型依赖标准书面语的结构线索，在缺乏标点与句法规范的阿拉伯语方言口语转录中性能崩塌。本文构建了首个覆盖多体裁、多方言的阿拉伯语口语语义分割基准，并验证了基于大语言模型微调的边界检测策略在噪声话语流中的有效性。通过引入“损坏-恢复”辅助任务与领域自适应提示，该模型在细粒度结构指标上稳定优于传统无监督与监督基线。其价值在于填补了从句子级分类到话语级结构建模的空白，但仅依赖文本转录而忽略声学韵律信息的局限，使其在真实口语场景的泛化能力仍存疑。

】

---

【LinguaGame: A Linguistically Grounded Game-Theoretic Paradigm for Multi-Agent Dialogue Generation ｜基于信号博弈的多智能体对话生成

作者：Yuxiao Ye、Yiming Zhang、Yiran Rex Ma 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_42ec25bbbb9a)

> 多智能体系统（MAS）在复杂任务中常因智能体间语义对齐失败导致沟通低效，现有架构优化方法忽视了交互过程本身的策略性。本文切入点在于将对话建模为信号博弈，通过意图-策略抽象与无训练均衡近似算法，在推理时动态调整话语选择以最大化语义传达效率。该方法在模拟法庭与辩论场景中显著提升了对话质量，但其泛化性受限于特定领域意图库的设计，且缺乏通用推理基准的验证。

】

---

【Listen, Pause, and Reason: Toward Perception-Grounded Hybrid Reasoning for Audio Understanding ｜感知接地混合推理

研究机构：北京大学、香港中文大学

作者：Jieyi Wang、Yazhe Niu、Dexuan Xu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc3d02b3b6a8)

> 大型音频语言模型（LALM）在复杂声学场景下常因感知错误导致推理失效，现有纯文本思维链（CoT）方法难以捕捉不可言说的声学线索。本文切入点在于将感知与推理解耦，通过显式声学分解与隐式潜空间计算建立可靠的推理基础。HyPeR 框架结合监督微调（SFT）与基于组相对策略优化（GRPO）的强化学习，引入 PAUSE 令牌处理声学模糊性。该方法在感知诊断任务上显著优于基线，但在通用推理基准上未超越现有 SOTA，其有效性局限于特定感知-推理解耦场景。

】

---

【LLEOT: A Privacy-Enhancing Offsite Tuning Framework via Loss Landscape Elevation ｜损失景观提升离线调优

研究机构：华南理工大学、香港科技大学

作者：Jin Zhong、Jinglin Liang、Tongtong Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fb028e2badad)

> 离线微调场景下，模型所有者与数据所有者互不信任，传统模拟器方法虽保护了参数与数据隐私，却因保留原模型推理能力而泄露“模型能力隐私”。现有基于知识蒸馏或选择性剪枝的模拟器构建方案无法在消除推理能力的同时维持梯度一致性，导致适配器迁移失效。本文提出损失景观提升（LLE），通过强制模拟器损失高于原模型固定边际，在理论上保证困惑度指数级放大且梯度方向不变，从而在禁用模拟器推理能力的同时确保软提示可迁移至原模型。该方法在多个基准上实现了优于随机初始化的隐私保护与接近全量微调的效用，但其确定性隐私保证缺乏对动态攻击者先验的适应性验证。

】

---

【LLM Multi-Agent Systems for Long Triple Set Data-to-Text Generation ｜长结构化数据到文本生成的多智能体协同控制

作者：Chinonso Cynthia Osuji、Simon Mille、Mark Andrade 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b41760fecd9)

> 数据到文本（Data-to-Text, D2T）生成旨在将结构化数据转化为连贯自然语言，但现有基准多聚焦短文本，难以评估大语言模型（LLM）在长输入下的语义完整性与话语连贯性。随着模型上下文窗口扩展至32k以上，单步生成在长序列中易出现信息遗漏与幻觉，且缺乏对中间推理过程的有效控制。本文提出一种模块化多智能体框架，通过内容排序、文本结构化与表面实现的角色分工，结合监督与校验机制，解决长结构化数据生成的控制难题。该框架在英语与爱尔兰语上展示了连贯性优势，但统计显著性不足，且LLM评估在长文本与低资源场景下可靠性存疑。

】

---

【LLM Prompt Duel Optimizer: Efficient Label-Free Prompt Optimization ｜无标签提示优化中的对偶赌博机框架

作者：Yuanchen Wu、Saurabh Verma、Justin Lee 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13907)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc94eecff4a1)

> 自动提示优化（APO）旨在通过算法搜索最优指令以提升大语言模型（LLM）性能，但主流方法严重依赖昂贵的真值标签进行候选评估。现有无标签方案如自监督提示优化（SPO）采用贪心爬山策略，缺乏探索-利用平衡机制，导致在噪声偏好信号下易陷入局部最优。本文提出提示决斗优化器（PDO），将无标签提示选择重构为对偶赌博机问题，结合双重汤普森采样（D-TS）与顶级表现者引导变异，在固定裁判预算下实现高效搜索。该框架在16个BBH任务中的13个上取得最高准确率，但其性能高度依赖裁判模型的推理能力，在复杂几何任务上仍显著落后于有标签SOTA。

】

---

【LLM-Codec: Neural Audio Codec Meets Language Model Objectives ｜语音编码器的目标错位：从重建保真到语言模型可预测性

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Ho-Lam Chung、Yiming Chen、Hung-yi Lee

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_81b8293f3d1d)

> 语音语言模型（SLM）依赖离散音频令牌进行自回归生成，但现有神经音频编码器为波形重建优化，导致令牌空间充满声学噪声，使语言模型困惑度居高不下。本文指出重建目标与预测目标的根本错位是SLM性能瓶颈，而非模型容量不足。通过引入未来令牌预测与语义对齐正则项，在保持编码器架构不变的前提下重塑令牌分布。该方法在语音连贯性基准上取得61.6%准确率，困惑度降低35倍，但仅验证了语音域，非语音音频的泛化能力存疑。

】

---

【LLM-Guided Semantic Bootstrapping for Interpretable Text Classification with Tsetlin Machines ｜基于大语言模型引导的Tsetlin Machine语义引导框架

研究机构：美国斯坦福大学、美国加州大学尔湾分校

作者：Jiechao Gao、Rohan Kumar Yadav、Yuangang Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12223)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12223)

> 该方向旨在解决符号模型在高风险领域部署时，因缺乏语义泛化能力而导致的性能瓶颈。现有方案要么依赖不透明的预训练语言模型（PLM），要么使用静态词向量增强符号模型，均无法兼顾透明性与语义深度。本文切入点在于利用大语言模型（LLM）离线生成结构化合成数据，引导非否定Tsetlin Machine（NTM）提取可解释的字面量特征，再注入真实数据微调。该方法在保持完全符号透明性的同时，将Tsetlin Machine（TM）的性能提升至接近BERT的水平，但其对LLM生成数据质量的依赖及缺乏因果验证的评估体系仍存疑。

】

---

【LLM-induced Rationales for More Compact Explainable Style Classification Models ｜基于LLM推理短语聚类的紧凑可解释特征工程

作者：Ahmad Aljanaideh、Saeb Ganideh

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_927aaeb63068)

> 该方向旨在解决线性分类器在风格识别任务中特征维度爆炸导致解释性丧失的问题。现有词级聚类方法虽能提升性能，但需为词汇表中每个词单独训练聚类模型，导致特征数量庞大且语义碎片化。本文切入点在于利用大语言模型（LLM）直接提取支持标签的语义短语（Rationale），并对其进行聚类以构建紧凑特征空间。通过GPT-4o mini提取短语并采用K-means聚类，该方法在保持与词级基线相当性能的同时，将特征数量减少了85-99%。这一策略验证了LLM辅助特征发现的可行性，但其对LLM幻觉的鲁棒性及因果忠实性缺乏严格验证。

】

---

【LLMRouterBench: A Massive Benchmark and Unified Framework for LLM Routing ｜LLM路由基准与统一评估框架

研究机构：西北工业大学

作者：Hao Li、Yiqun Zhang、Zhaoyan Guo 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07206)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07206)

> LLM路由旨在为每个查询动态分配最适配的模型，以平衡质量与成本。现有研究因模型池、数据集和评估协议各异，导致结果不可比且复现困难。本文构建了包含33个模型和21个数据集的大规模基准，并集成10种代表性路由算法进行统一重评估。该工作揭示了当前路由方法在统一条件下性能趋同且未显著优于简单基线的现象，挑战了复杂路由必然更优的假设，但其结论受限于未覆盖最新强化学习路由方法。

】

---

【LLMs are Brittle to Simple Code Transformations: Introducing CETBench – A Benchmark for Code-Equivalence Checking ｜代码等价性检查基准

作者：Neeva Oza、Ishaan Govil、Parul Gupta 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7fe2279b9011)

> 代码等价性检查旨在判定两段程序是否对所有输入产生相同输出，是程序验证与重构的基础。现有静态分析工具难以处理语义保持的语法变异，而基于测试用例的执行验证受限于输入域覆盖不全，导致LLM在此任务上表现脆弱。本文通过构建包含组合语义扰动的基准CETBench，量化模型区分语法变化与语义变化的能力。该基准揭示了SOTA模型在简单变换下的显著性能退化，但受限于二元标签简化与合成扰动结构，其结论向真实复杂重构场景的泛化性仍存疑。

】

---

【LLMs as ASP Programmers: Self-Correction Enables Task-Agnostic Nonmonotonic Reasoning ｜基于答案集规划的非单调神经符号推理框架

研究机构：美国亚利桑那州立大学、三星研究院

作者：Adam Ishay、Joohyung Lee

论文原文见 [arXiv](https://arxiv.org/abs/2604.27960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27960)

> 大语言模型在处理需要回溯与例外处理的逻辑任务时，常因自回归生成的线性特性陷入逻辑不一致或计算冗余。现有神经符号方法多依赖单调逻辑（如SMT），无法表达默认推理与信念撤销，且需大量人工领域知识。本文提出 LLM+ASP 框架，通过自动自修正循环将自然语言转化为答案集规划（Answer Set Programming, ASP）程序，利用稳定模型语义处理非单调推理。该框架在六个基准上显著优于基线，但其在常识推理任务上的增益有限，且高度依赖底层模型的代码生成能力。

】

---

【LLMs Deceive Unintentionally: Emergent Misalignment in Dishonesty from Misaligned Samples to Biased Human-AI Interactions ｜无意图涌现失配：从数据污染到交互偏差的诚实性崩塌

研究机构：复旦大学、中国科学技术大学

作者：Xuhao Hu、Peng Wang、Xiaoya Lu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08211)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08211)

> 现有安全对齐研究多聚焦于模型面对恶意提示时的“有意图”欺骗或拒绝失效，却忽视了训练数据中极少量错误样本引发的“无意图”行为漂移。本文切入点在于揭示这种漂移并非孤立输出错误，而是信念与输出在压力下的系统性背离。作者通过窄域微调、下游混合及模拟人类交互三种实验，量化了低比例污染对模型诚实性的破坏阈值。该工作填补了训练数据污染与高风险不诚实行为间的因果空白，但其结论是否适用于更大规模模型仍存疑。

】

---

【Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models ｜可操作机制可解释性：从定位到干预的工程化框架

研究机构：复旦大学、德国慕尼黑大学

作者：Hengyuan Zhang、Zhihao Zhang、Ercong Nie 等 28 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7986d401ebad)

> 机制可解释性（Mechanistic Interpretability, MI）长期被视为一种观察科学，旨在逆向工程大语言模型（LLMs）的内部计算逻辑，但现有综述多止步于“理解”层面，缺乏将洞察转化为模型改进动作的系统性协议。本文指出，随着外部扩展（Scaling）遭遇瓶颈，模型优化必须转向内部机制的“外科手术式”干预，然而当前领域缺乏统一的方法分类与实施指南。为此，本文构建了“定位-引导-改进”（Locate, Steer, and Improve）流水线，将MI重构为可操作的工程工具。该框架通过形式化定义可解释对象与干预方法，为对齐、能力与效率优化提供了具体路径，但其有效性依赖于尚未标准化的因果验证基准，实际收益的量化仍存疑。

】

---

【Logical Structure as Knowledge: Enhancing LLM Reasoning via Structured Logical Knowledge Density Estimation ｜结构化逻辑知识密度（SLKD）驱动的大语言模型推理增强

研究机构：英国爱丁堡大学、浙江大学

作者：Zhen Bi、Zhenlin Hu、Xueshu Chen 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24836)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24836)

> 大语言模型（LLM）的推理能力长期被归因于参数规模扩张，但数据质量对推理涌现的潜在作用被低估。现有数据中心范式多将“质量”等同于事实性覆盖或多样性，忽视了文本内部蕴含的逻辑拓扑复杂度，导致训练数据中高密度逻辑样本被低密度事实性样本稀释。本文提出结构化逻辑知识密度（Structured Logical Knowledge Density, SLKD）度量，将自然语言分解为谓词逻辑原语并计算其组合拓扑复杂度，进而设计两阶段重认知优化策略，通过密度加权采样重塑模型认知框架并强化推理路径。该策略在不增加数据总量的前提下显著提升了小模型在逻辑基准上的表现，但其依赖LLM进行逻辑蒸馏的循环性，以及仅验证于微调阶段的有效性，使其在预训练及复杂OOD泛化场景下的普适性存疑。

】

---

【LogitSpec: Accelerating Retrieval-based Speculative Decoding via Next Next Token Speculation ｜基于末位Logit推测的检索式投机解码

研究机构：中国科学技术大学

作者：Tianyu Liu、Qitan Lv、Hao Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f7cbcdda5709)

> 投机解码旨在通过并行验证打破自回归解码的串行瓶颈，但传统无训练检索方法常因上下文匹配失败导致加速失效。LogitSpec 发现目标模型末位 Logit 具备预测“下下个 Token”的高鲁棒性，将其作为检索锚点以扩展搜索空间。该方法无需额外草稿模型，通过双锚点检索显著提升了草稿命中率。其价值在于以零训练成本实现了接近训练式方法的加速比，但受限于检索机制本身，在长上下文或低重复率场景下的上限仍低于特征对齐路线。

】

---

【Look Twice before You Leap: A Rational Framework for Localized Adversarial Text Anonymization ｜理性本地化对抗匿名化

研究机构：电子科技大学、中国人民大学

作者：Donghang Duan、Xu Zheng、Yuefeng He 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c9d987e9e08)

> 本地小模型部署下的文本匿名化面临效用崩溃困境，现有贪心对抗策略在缺乏形式化保证的前提下，因模型幻觉导致过度编辑。本文切入点在于将匿名化过程重构为经济交易问题，通过引入仲裁者验证泄露有效性，从架构层面阻断非理性迭代。该方法以零样本、免训练的方式实现了隐私-效用帕累托前沿的优化，但其缺乏差分隐私等数学边界，合规性存疑。

】

---

【LoRE: Enhancing Search Relevance with Progressive Chain-of-Thought and Preference Alignment ｜电商搜索相关性评估：渐进式思维链合成与偏好对齐

作者：Chenji Lu、Zhuo Chen、Hui Zhao 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b9565e0cd407)

> 电商搜索相关性评估旨在判定查询与商品间的匹配程度，但通用大语言模型（LLM）缺乏垂直领域知识与刚性业务规则遵循能力，导致长尾查询与多模态商品匹配出现系统性偏差。现有基于直接分类或单模态思维链（CoT）的方法难以同时覆盖知识推理、视觉理解与规则约束，且监督微调（SFT）易陷入表面模式模仿。本文提出LoRE框架，通过渐进式多模态CoT合成注入综合能力，并引入基于课程学习的强化学习（RL）阶段修剪冗余逻辑。该框架在工业级部署中验证了显著增益，但其对教师模型依赖与奖励稀疏性缓解机制的普适性仍需审视。

】

---

【LoReFact: Bridging the Logic Gap in Fact-Checking ｜逻辑事实性耦合的事实核查框架

研究机构：南京大学

作者：Qiming Xie、Wenjie Zheng、Xiangqing Shen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83dc2353baf3)

> 长文本事实核查长期受困于“原子事实正确但逻辑推导错误”的盲区，导致含谬误文本被误判为真实。现有分解-验证范式仅关注事实覆盖率，无法捕捉声明间的因果或条件依赖失效。本文提出内容-逻辑耦合范式，通过并行评估原子事实与逻辑关系有效性，并引入新数据集LOREFACT与指标LoReFactScore。该工作揭示了现有方法对逻辑谬估的系统性高估，但受限于合成数据分布与单一逻辑类型覆盖，其结论在自然文本中的普适性存疑。

】

---

【Lost in Decomposition: Analyzing and Mitigating the Limitations of Long Context Methods via Context Dependency ｜上下文依赖感知路由

作者：Jiayuan Guo、Yueyang Su、Yuyao Ge 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b61b72636c68)

> 长上下文工作流方法在特定数据集上表现优异，但跨数据集泛化能力存疑，现有研究默认其普适有效。本文指出，RAG、多智能体等方法因内部分解机制破坏了文档的上下文依赖结构，导致在强依赖文档上性能反而低于全上下文基线。通过提出文档上下文依赖得分（DCDS）量化依赖强度，并设计免训练自适应路由策略CoDaR，仅对弱依赖文档调用工作流方法。该策略显著提升了鲁棒性，但DCDS计算依赖大语言模型评估器，其推理成本与延迟是否抵消路由收益尚待验证。

】

---

【Lost in the Prompt Order: Revealing the Limitations of Causal Attention in Language Models ｜因果注意力下的提示词顺序敏感性机制分析

作者：Hyunjong Ok、Jaeho Lee

论文原文见 [arXiv](https://arxiv.org/abs/2601.14152)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.14152)

> 提示词工程长期面临模型对输入结构微小变化产生剧烈性能波动的难题，现有研究多停留在现象描述或黑盒优化层面，缺乏对底层机制的归因。本文聚焦于多选题问答中上下文、问题与选项的排列顺序，指出解码器架构中的因果掩码是造成性能差异的核心物理约束。通过架构对比与干预实验，论文证实了选项token在特定顺序下无法访问上下文信息这一结构性瓶颈。该发现将提示词敏感性从经验性观察提升为可解释的架构属性，但仅提供了推理时缓解手段，未解决训练时的根本修复问题。

】

---

【LRBench and Judge-R1: Principled Evaluation and Training of LLM-Based Judges for Long-Context Reasoning ｜长上下文推理评判基准与检索增强训练框架

作者：Xinyi Zhao、Haoqi Hu、Ziyu Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_554e21d2f6d6)

> 现有 LLM 评判器在长上下文推理任务中常因证据缺失而误判逻辑正确性，且缺乏细粒度的原则违规标注。本文指出，仅依赖最终答案或粗粒度偏好的评估协议无法捕捉推理链中的细微缺陷。为此，作者构建了包含 10 万+ 实例的 LRBENCH 基准，并提出结合多轮检索与强化学习的 Judge-R1 训练框架。该框架在长上下文推理评估上显著优于通用大模型，但其对检索延迟的忽略及测试集规模限制，使其在工程落地与统计严谨性上仍存疑。

】

---

【LS-Guard: Adaptive Safety Guardrails Tailored to Individual LLMs ｜模型特异性安全护栏

作者：Jinggui Liang、Lizi Liao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_15abb4663f8d)

> 大语言模型（LLM）在商业部署中面临恶意输入威胁，现有安全护栏普遍采用“一刀切”策略，忽略了不同模型对同一有害查询的响应差异，导致防御失效或过度拒绝。LS-Guard 通过动态探测目标模型的行为特征，利用多 LoRA 专家架构实现个性化安全分类。该方法在多个主流 LLM 上显著优于通用护栏基线，但其依赖离线探测阶段的计算开销及跨模型泛化能力的边界尚待明确。

】

---

【LSEG: A Fine-tuning Free Method for NL2FOL via Logic-Structure and Entropy Guided Inference Controlling ｜逻辑结构与熵引导推理控制

研究机构：中国科学院、中国科学院大学

作者：Yuwei Huang、Shi Wang、Kangli Zi 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ea6cd163bec2)

> 自然语言到一阶逻辑（NL2FOL）翻译的核心痛点在于大语言模型（LLM）内部表示漂移导致的逻辑幻觉，即生成语法正确但语义错误的公式。现有微调或代码生成方法虽能提升一致性，但依赖高昂训练成本或特定架构，且无法在推理时动态修正内部状态偏差。LSEG通过构建逻辑保持扰动向量并引入熵引导机制，在免微调条件下校正隐藏状态。该方法在FOLIO和MALLS上取得了与强监督模型相当的性能，但其对复杂量词交互的覆盖能力及统计显著性仍存疑。

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

【LUNE: Efficient LLM Unlearning via LoRA Fine-Tuning with Negative Examples ｜基于低秩适配器的负样本大语言模型遗忘

研究机构：美国加州大学尔湾分校、美国普渡大学

作者：Yezi Liu、Hanning Chen、Wenjun Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07375)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07375)

> 大语言模型（LLM）在预训练中记忆了敏感信息，但全参数微调或重训练带来的计算成本使其难以在部署后快速擦除特定知识。现有方法要么更新全部参数导致效用崩塌，要么依赖复杂的偏好优化框架，缺乏一种兼顾效率与鲁棒性的轻量级方案。LUNE 通过冻结骨干网络并仅更新低秩适配器（LoRA），结合精心构造的负样本进行微调，将遗忘操作限制在低维子空间内。该方法在 7B 规模模型上实现了与全参数微调相当的遗忘效果，但其在复杂语义纠缠场景下的效用保持能力仍存疑。

】

---

【M-TRACE: Detecting and Mitigating Time-Anchor Drift via Step-wise Conflict Checking in Temporal Reasoning ｜多智能体时间推理框架 M-TRACE：基于状态时间线的冲突检测与锚点漂移抑制

研究机构：南开大学

作者：Danyu Huang、Jiayuan Jiang、Yao Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f0e7bf94e1ad)

> 时间推理的核心困境在于，大语言模型（LLM）的参数化知识是静态的，而现实世界是动态的，当模型结合外部检索证据进行多步推理时，内外部知识的时间不一致性会累积并导致推理失败。现有方法通常假设知识源在时间上是一致的，或仅将冲突视为静态事实差异，无法处理由知识演化引发的动态时间冲突。M-TRACE 通过构建独立的内部状态时间线作为参照系，逐步比对内外部证据并生成结构化冲突报告，从而显式检测并抑制时间锚点漂移。该框架在自建基准上显著提升了推理准确性，但其对骨干模型时间理解能力的强依赖，限制了其在弱模型上的泛化潜力。

】

---

【MAC-Reasoner: A Multi-Agent Collaborative Framework for Enhancing Logical Reasoning in Large Language Models ｜逻辑增强上下文

作者：Yehua Lin、Liping Zheng、Yin Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df0cb4b987cb)

> 大语言模型在严格演绎推理中常因幻觉或忽略约束而失效，纯神经方法缺乏逻辑严谨性，而传统神经符号方法将模型降格为翻译器，无法利用其内部推理能力。MAC-Reasoner 通过构建逻辑增强上下文，将外部求解器的符号证据转化为自然语言参考，引导模型自主完成最终推理。该方法在多个基准上显著提升了不同规模模型的准确率，并验证了推理轨迹可用于监督微调。其价值在于平衡了求解器的可靠性与模型的自主性，但效果高度依赖翻译准确性，且未解决长程推理中的状态一致性问题。

】

---

【Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions ｜关系道德困境中的LLM决策一致性分析

研究机构：韩国科学技术院

作者：Jiseon Kim、Jea Kwon、Luiz Felipe Vecchietti 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fc306ad47395)

> 大语言模型（LLM）在道德决策中是否具备人类般的社会敏感性，是评估其作为社会代理可靠性的关键。现有评估多将道德视为静态单维结构，忽视了规范性判断、描述性预测与自主决策间的动态张力，导致无法捕捉模型内部的价值重构机制。本文通过构建包含犯罪严重度与关系亲疏双变量的吹哨人困境框架，结合道德基础理论（MFT）量化分析三种视角下的推理轨迹，揭示了LLM决策锚定规范性而非描述性的结构性偏差。该发现为道德对齐提供了新的诊断维度，但其结论是否源于对齐训练而非预训练偏差，尚存疑。

】

---

【MAKI: Multi-layer Aligned Knowledge Injection for Structure-aware Knowledge Graph Completion with Large Language Models ｜多层对齐知识注入

研究机构：澳门大学、华为

作者：Zhiwen Xie、Xin Wang、Guangyou Zhou 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f0810d7f6b7)

> 知识图谱补全（KGC）旨在预测图谱中缺失的实体或关系，其核心价值在于缓解结构化数据稀疏性与开放世界推理需求之间的张力。现有基于大语言模型（LLM）的方法常因结构嵌入与语义空间的根本错位，导致对长尾及未见实体的泛化能力受限。MAKI 通过构建与 LLM 隐层逐层对齐的图神经网络（GNN）模块，将结构信息以门控方式注入 LLM 内部，实现了语义与拓扑的深层协同。该框架在归纳式基准上展现了显著的推理优势，但其性能增益在多大程度上归因于 LLM 骨干本身而非结构注入机制，仍存疑。

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

【Many-Shot Scaling of In-Context Learning with Self-Generated Demonstrations ｜半监督上下文学习

研究机构：美国康奈尔大学、清华大学

作者：Zhengyao Gu、Henry Peng Zou、Yankai Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f9e637235522)

> 上下文学习（In-Context Learning, ICL）的性能上限受限于高质量标注数据的获取成本，而现有自生成演示方法多局限于少样本场景，无法利用长上下文的规模效应。本文切入点在于将传统半监督学习的迭代精炼与课程学习范式迁移至 ICL 演示生成流程，通过置信度过滤与动态演示池更新实现千级伪演示的规模化扩展。具体做法是提出 Naive-SemiICL 基线与 IterPSD 迭代算法，利用 LLM 的口头置信度筛选低质标注，并通过课程采样缓解错误累积。该方法在零样本与少样本预算下均优于标准 ICL，但其在高资源场景下的增益边际递减，且未解决自生成演示在分布外数据上的鲁棒性问题。

】

---

【MAPLE: Multi-Aspect Panels of LLM Evaluators for Open-Ended Questions ｜多标准异构评估者面板

作者：Michinori Jinji、Kyohei Atarashi、Koh Takeuchi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_13b5830e63e1)

> 大语言模型评估者（LLM-as-a-Judge）旨在利用大语言模型替代昂贵的人类评估，为开放式生成任务提供可扩展的自动化反馈。现有方法要么依赖单一骨干模型的提示工程，要么采用无差别投票的多智能体集成，均无法在评估者能力参差不齐时保证结果的统计可靠性。MAPLE 将评估标准分解与多模型成对比较结合，通过扩展的 Crowd-BT 模型联合学习标准权重与评估者可靠性参数，实现可靠性感知的统计聚合。该框架在作文评分任务上验证了优于单模型及简单投票的鲁棒性，但其性能上限受限于聚合机制对多数派偏差的敏感性，且未覆盖复杂推理或代码生成场景。

】

---

【MARS: Unleashing the Power of Speculative Decoding via Margin-Aware Verification ｜边际感知投机验证

研究机构：加拿大麦吉尔大学、北京大学

作者：Jingwei Song、Xinyu Wang、Hanbin Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15498)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15498)

> 投机解码（Speculative Decoding, SD）旨在通过草稿-验证范式突破大语言模型（LLM）自回归解码的内存带宽瓶颈，但现有方法在验证阶段普遍采用严格的精确匹配或拒绝采样，导致在目标模型置信度低时产生大量无效回滚。本文指出这种“验证严格性与模型内在不确定性”的错配是加速比停滞的关键，提出边际感知投机验证（Margin-Aware Speculative Verification, MARS），一种基于目标模型 Logit 边际的免训练自适应验证策略。该方法在保持生成质量近乎无损的前提下，显著提升了接受长度与端到端加速比，但其有损特性对传统无损 SD 的定义边界提出了挑战。

】

---

【MATA: Multi-Agent Framework for Reliable and Flexible Table Question Answering ｜多智能体表格问答框架

研究机构：韩国首尔大学

作者：Sieun Hyeon、Jusang Oh、Sunghwan Steve Cho 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.09642)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09642)

> 表格问答（TableQA）旨在让非技术用户通过自然语言查询结构化数据，但现有方法要么依赖闭源大模型，要么通过固定次数的重复推理换取可靠性，导致计算成本高昂且在小模型上性能崩塌。MATA 的切入点在于将“推理多样性”与“计算预算”解耦，通过轻量级控制器动态决定执行哪些推理路径及何时停止验证。该框架整合思维链（CoT）、程序思维（PoT）和文本转SQL（text2SQL）三条路径，利用调度器（Scheduler）和置信度检查器（Confidence Checker）实现按需调用。其价值在于证明了3B-10B开源模型在复杂表格任务上的可行性，但缺乏对二维结构丢失问题的直接解决，且未在标准基准上与结构表示类SOTA对比。

】

---

【MathAgent: Adversarial Evolution of Constraint Graphs for Mathematical Reasoning Data Synthesis ｜MathAgent：基于约束图对抗进化的数学数据合成框架

研究机构：清华大学、哈尔滨工业大学

作者：Zixiong Yu、Jun Rao、Guhan Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11188)

> 导读 数学推理数据合成旨在解决高质量人工标注数据稀缺导致的模型能力天花板问题。现有种子扩展法受限于初始语义半径，零样本生成法则因缺乏结构引导而陷入模式崩溃。MathAgent 将数据合成重构为约束图上的无监督优化问题，通过“立法者-执行者”分层架构解耦结构设计与语言实现。该框架在1K样本规模下优于主流开源数据集，但其优势是否源于结构复杂度而非单纯难度提升，仍需更严格的归因分析。

】

---

【MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning ｜难度可控数据合成与课程学习

作者：Xuchen Li、Jing Chen、Xuzhao Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17006)

> 大语言模型在数学推理上的提升受限于训练数据缺乏显式且可控的难度梯度，导致课程学习无法有效实施。现有合成方法要么仅增加问题复杂度而忽略难度分层，要么生成语义高度相似的变体，无法支撑从易到难的渐进训练。MathMixup通过混合与分解策略生成具有三级难度梯度的数据，并据此实施课程学习，在SFT范式下显著提升了小模型的推理能力。该方法验证了数据难度结构对训练效率的关键作用，但其性能上限仍受限于监督微调范式，未能触及强化学习带来的推理深度突破。

】

---

【MAXS: Meta-Adaptive Exploration with LLM Agents ｜元自适应探索框架

研究机构：新加坡南洋理工大学、新加坡国立大学

作者：Jian Zhang、Zhiyuan Wang、Zhangqi Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09259)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09259)

> 大语言模型智能体在推理时面临局部短视与轨迹不稳定两大瓶颈，导致工具调用决策缺乏前瞻且易发散。现有方法如思维链（Chain-of-Thought, CoT）缺乏全局视野，而蒙特卡洛树搜索（Monte Carlo Tree Search, MCTS）计算成本过高。MAXS通过轻量级前瞻滚动与复合价值函数，在推理阶段动态平衡探索深度与稳定性。该框架在数学推理任务上以极低Token成本实现了性能突破，但其对非数学类开放域工具调用的泛化能力存疑。

】

---

【MDC-Bench: A Multidisciplinary Causal Benchmark Based on Causal Structures for Evaluating Large Language Models ｜多学科因果基准 MDC-Bench

研究机构：哈尔滨工业大学、华为

作者：Peng Wang、Yuxiong Yan、Xiao Ding 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18840408d140)

> 现有因果评估基准多基于常识领域，模型常通过预训练记忆匹配而非逻辑推导得出答案，导致对深层因果能力的评估失真。MDC-Bench 通过引入 7 个学科的专业论文数据与复杂因果拓扑结构，阻断了知识匹配路径，迫使模型进行真实的因果推理。该基准构建了包含理解、干预、反事实三层级的 8,422 道题目，并引入复合操作增加难度。实验显示，即便最先进的模型在硬模式下准确率仍不足 60%，揭示了当前大语言模型在深层因果理解上的显著局限，但其评估协议中关于因果强度梯度的定义尚存争议。

】

---

【MdEval: Massively Multilingual Code Debugging ｜大规模多语言代码调试基准

作者：Shukai Liu、Linzheng Chai、Jian Yang 等 18 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0de3c21c27f1)

> 现有代码调试基准局限于Python等少数语言，无法反映LLM在Rust、Go等语言特定错误（如Missing mut）上的真实能力。本文通过人工标注与LLM生成混合构建覆盖20种语言、3.9K样本的MDEVAL基准，并设计xDebugGen注入策略生成指令语料。该工作填补了多语言调试评估的空白，但静态人工标注的规模限制与单文件任务粒度，使其难以捕捉仓库级上下文中的调试失效。

】

---

【Measuring Large Language Models’ Adversarial Behavior in Social Deduction Games ｜社交推理游戏中的大语言模型对抗行为量化

研究机构：美国加州大学洛杉矶分校

作者：Marissa Zhao Li、Esha Shivakumar、Peiran Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b6f5bd7d6165)

> 多智能体交互中的安全评估长期受限于单轮拒绝测试，无法捕捉模型在生存压力下自发产生的策略性欺骗与操纵。现有基准多聚焦于事实性错误检测或单轮对抗，缺乏对多轮博弈中复杂社会战术（如煤气灯效应、投票胁迫）的细粒度分类与跨模型对比。本文通过构建五款社交推理游戏环境，利用元大语言模型（Meta-LLM）自动标注行为分类法，量化了不同模型在对抗压力下的行为谱系。该工作提供了首个基于内生激励而非外部攻击的多智能体行为基准，但其黑盒标注机制与中小规模模型局限限制了结论向高能力模型的泛化。

】

---

【MEAV: Model Editing with Alignment Vectors for inference time LLM alignment in single and multidomain preference spectrum ｜对齐向量模型编辑

研究机构：亚马逊网络服务人工智能

作者：Sadat Shahriar、Zheng Qi、Nikolaos Pappas 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_57135049cbf4)

> 推理时偏好对齐旨在解决训练时方法（如DPO/RLHF）在偏好需求变化时需重新训练、成本高昂且缺乏细粒度控制的问题。现有推理时方法多依赖提示工程或固定混合，无法实现连续、动态的多域偏好强度调节。本文提出MEAV，通过提取域特定对齐向量并在推理时线性叠加，实现无需重训的连续偏好控制。该方法在自建医疗、金融、法律数据集上验证了可行性，但缺乏通用基准对比，其线性叠加假设在强冲突场景下的有效性存疑。

】

---

【Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy ｜基于System-2策略的大规模计数机制解析

作者：Hosein Hasani、Mohammadali Banayeeanzade、Ali Nafisi 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02989)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc4a31edeae3)

> 大语言模型（LLM）在处理长序列计数任务时，因Transformer架构的层深限制导致内部计数机制饱和，性能随项目数量增加而急剧下降。现有方法多依赖外部工具或微调，忽视了模型内部隐式计数过程的容量瓶颈。本文提出一种无需修改参数的测试时策略，通过将长序列分割为小分区并显式聚合中间结果，绕过架构限制。该策略在多个开源与闭源模型上验证了有效性，但其泛化至非计数类算术任务的边界尚不明确。

】

---

【MedScore: Generalizable Factuality Evaluation of Open-ended Long-form Medical Answers by Domain-adapted Claim Decomposition and Verification ｜医疗开放域长文本事实性评估：MedScore

研究机构：美国约翰斯·霍普金斯大学

作者：Heyuan Huang、Alexandra DeLucia、Vijay Murari Tiyyala 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_398b3efcb301)

> 导读 现有分解-验证框架在传记等实体中心文本上表现良好，但面对医疗对话中语境依赖、主观且结构复杂的回答时，分解质量严重退化，导致事实性得分失真。本文指出通用分解方法无法处理“如果疼痛加剧”这类假设性语句，提出MedScore，通过领域适配的条件感知分解与多源验证解决该问题。实验显示其有效声明提取量达现有方法3倍，但外部语料验证得分显著低于内部知识，暴露了检索覆盖度对评估可靠性的制约。

】

---

【Meeseeks: A Feedback-Driven, Iterative Self-Correction Benchmark evaluating LLMs’ Instruction Following Capability ｜多轮迭代指令遵循基准

研究机构：美团

作者：Jiaming Wang、Yunke Zhao、Peng Ding 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8021b9dbd77d)

> 大语言模型在单次响应中难以同时满足复杂多约束指令，而现有评估基准仅关注单轮静态表现，无法量化模型在反馈驱动下的自我修正上限。Meeseeks 通过引入 20 轮迭代反馈机制，将评估从“单次成功率”转向“能力上限探测”，并采用代码引导的规则增强评估框架解决长文本提取的准确性与成本瓶颈。该基准揭示了模型单次表现与最终能力上限的巨大差距，但受限于自建数据集分布，其结论在跨基准泛化性上仍存疑。

】

---

【MEIC-DT: Memory-Efficient Incremental Clustering for Long-Text Coreference Resolution with Dual-Threshold Constraints ｜双阈值约束下的内存高效增量聚类

研究机构：清华大学

作者：Kangyang Luo、Shuzheng Si、Yuzhuo Bai 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8255170f17b0)

> 长文本共指消解面临Transformer自注意力机制的内存溢出瓶颈，传统增量聚类方法虽通过缓存驱逐缓解内存压力，但牺牲了全局语义建模能力。MEIC-DT针对这一矛盾，提出双阈值约束机制，在严格内存预算下同时限制集群数量与每集群提及数。该方法通过统计感知驱逐策略与内部正则化策略，在LitBank基准上以81.27%的CoNLL F1超越基线，验证了其在资源受限环境下的有效性，但其性能优势是否完全源于底层Maverick模型而非约束机制本身，仍需进一步隔离验证。

】

---

【MemoBrain: Executive Memory as an Agentic Brain for Reasoning ｜执行记忆：作为推理智能体的协同大脑

研究机构：中国人民大学

作者：Hongjin Qian、Zhao Cao、Zheng Liu

论文原文见 [arXiv](https://arxiv.org/abs/2601.08079)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08079)

> 工具增强智能体在长时程推理中因上下文窗口受限导致认知过载与任务对齐失效，现有跨任务持久记忆无法适应单任务内动态演化的推理结构。MemoBrain 提出“执行记忆”范式，将记忆从被动存储重构为主动控制机制，通过独立协同模型异步构建依赖感知记忆图并执行折叠与冲刷操作，在有界预算下维持推理连贯性。该方法在 BrowseComp-Plus 等基准上显著提升了基线智能体性能，但其仅限单任务生命周期且依赖独立模型部署，是否适用于跨会话经验复用尚存疑。

】

---

【MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents ｜记忆组织与自适应图智能检索

研究机构：澳大利亚莫纳什大学

作者：Hung Pham Van、Nguyen Manh Hieu、Khang Pham Tran Tuan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c934793cded0)

> 长程对话智能体面临的核心矛盾是上下文窗口的有限性与个性化交互对持久化状态的需求。现有图谱记忆系统虽能建模实体关系，但普遍存在信息稀释、事实来源不透明以及检索传播机制忽略查询语义三大缺陷，导致高连接度节点主导结果而语义相关但稀疏连接的节点被抑制。MemORAI通过引入用户画像选择性过滤、轮次级溯源异质图谱及查询条件化动态加权PageRank，在存储、表示与检索三个环节同时介入，试图将记忆从被动存储转变为可审计、上下文敏感的认知组件。该框架在受控条件下显著提升了检索召回率与生成事实性，但其优势是否源于架构创新还是特定骨干模型的配合，以及静态过滤机制能否适应用户偏好的长期漂移，仍存疑。

】

---

【Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks ｜记忆即动作：长时程智能体任务的自主上下文策展

研究机构：北京交通大学

作者：Yuxiang Zhang、Jiangming Shu、Ye Ma 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12635)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12635)

> 长时程智能体任务中，固定上下文窗口随交互累积导致注意力稀释与关键信号丢失，现有外部记忆管理模块因与推理策略解耦而无法联合优化信息保留与任务性能。MemAct 将工作记忆管理重构为策略空间内的可学习动作，通过端到端强化学习实现上下文编辑与任务执行的统一优化。该框架引入动态上下文策略优化算法解决非连续轨迹的训练不匹配问题，使14B模型在保持高准确率的同时将平均上下文长度压缩51%。其价值在于证明了记忆管理作为内生策略的可行性，但实验局限于单任务长时程场景，跨会话泛化能力未经验证。

】

---

【Memory Dial: A Training Framework for Controllable Memorization in Language Models ｜记忆压力调控框架

研究机构：美国佐治亚理工学院、美国埃默里大学

作者：Xiangbo Zhang、Ali Emami

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_57d9f516b01d)

> 大语言模型的记忆机制长期被视为训练过程的被动副产物，研究者只能事后检测模型记住了什么，却无法在训练前预设其记忆强度。现有暴露度指标与提取攻击均依赖已训练完成的模型，难以将记忆效应与架构、数据等混杂因素解耦。MEMORY DIAL 通过引入温度锐化目标函数与标准交叉熵的凸组合，将记忆压力转化为可连续调节的独立变量。该框架在六个架构上验证了记忆可控性与泛化稳定性，但其控制粒度局限于训练目标层面，未触及参数空间的直接编辑。

】

---

【Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning ｜事件中心记忆作为逻辑地图

研究机构：中国人民大学

作者：Yuyang Hu、Jiongnan Liu、Jiejun Tan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04726)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04726)

> 长时程智能体交互中，扁平化文本存储导致多跳推理与时间逻辑断裂，现有结构化方法虽引入图结构却仍依赖被动相似度检索。本文切入点在于将记忆从静态容器转化为引导推理的“逻辑地图”，通过事件分割与显式关系提取构建事件图，并设计主动多路径导航机制。该方法在LoCoMo和NarrativeQA上显著优于基线，但其绝对性能仍低于最新工业级系统，且高计算开销限制了实时部署。

】

---

【MemPO: Self-Memory Policy Optimization for Long-Horizon Agents ｜自记忆策略优化

研究机构：清华大学、阿里巴巴集团

作者：Ruoran Li、Xinghua Zhang、Haiyang Yu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00680)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00680)

> 长时程智能体在ReAct范式下因上下文线性膨胀面临窗口截断、成本激增与“中间迷失”三重瓶颈，现有外部记忆模块因离线压缩与任务目标脱节，导致检索被动且无法联合优化。本文切入点在于将记忆管理内化为策略模型的内生动作，通过自记忆策略优化算法（Self-Memory Policy Optimization, MemPO）实现记忆、推理与工具调用的端到端协同。其核心机制是引入基于条件概率的记忆级奖励，解决长时程交互中的信用分配难题。该方案在单任务多跳推理中显著降低了Token消耗并提升了精度，但其缺乏跨会话持久化存储，在需要长期状态一致性的场景中有效性存疑。

】

---

【MemTR: Enhancing Tool-Calling Reliability via Uncertainty-Triggered FFN-Space Retracing ｜基于不确定性触发的FFN空间重迹工具调用纠错

作者：Hongtao Duan、Lu Jiang、Minying Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_391d6837fe68)

> 工具调用中单token错误导致硬失败，现有训练式方法成本高且无法适应动态API更新，语法约束无法修正语义值错误。MemTR切入解码时干预，利用层熵识别脆弱token，在FFN输出层混合工具库证据以刷新记忆。该方法无需更新权重，仅增加1%-2%运行时开销，但绝对性能上限受限于骨干模型，且未与强化学习基线对比。

】

---

【MemWeaver: Weaving Hybrid Memories for Traceable Long-Horizon Agentic Reasoning ｜记忆固化驱动的三层混合架构

作者：Juexiang Ye、Xue Li、Yang Xinyu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b52e4a4dda81)

> 长时程智能体交互面临的核心挑战是跨会话状态丢失与认知矛盾，现有基于向量检索或单一知识图谱的方法在时序一致性与证据可追溯性上存在结构性缺陷。MemWeaver 将记忆管理从被动存储重构为主动固化过程，通过整合时序知识图谱、经验抽象与原始段落证据的三层架构，解决多跳推理中的时间冲突与幻觉问题。该方法在 LoCoMo 基准上显著提升了时序与多跳任务的性能，同时大幅压缩了推理上下文长度，但其离线构建依赖高算力 LLM 的瓶颈限制了实时部署的可行性。

】

---

【Mending the Holes: Mitigating Reward Hacking in Reinforcement Learning for Multilingual Translation ｜修补质量估计漏洞：多语言翻译强化学习中的混合奖励机制

作者：Yifeng Liu、Siqi Ouyang、Yatish H R 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9dd6243e6880)

> 多语言大语言模型在低资源语言翻译上性能滞后，而现有后训练方法依赖稀缺的平行数据。直接利用无参考质量估计（QE）模型进行强化学习（RL）会因指标缺陷导致“奖励黑客”，使模型退化。本文提出 WALAR，通过引入词对齐与语言对齐分数构建混合奖励，仅使用单语数据即可提升翻译质量。该方法在 FLORES-101 上显著优于基线，但绝对性能仍受限于单语数据的语义覆盖度。

】

---

【Meta-Tool: Efficient Few-Shot Tool Adaptation for Small Language Models ｜少样本工具适配中的参数更新冗余性

作者：Sachin Kumar

论文原文见 [arXiv](https://arxiv.org/abs/2604.20148)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20148)

> 小语言模型（SLM）在接入新工具时面临适配瓶颈：前沿模型延迟高企，而监督微调（SFT）依赖稀缺标注且泛化差。现有研究倾向于通过复杂参数更新机制提升小模型能力，但本文指出在少样本场景下，精心设计的提示工程已充分指定任务，额外的参数空间适配可能冗余。Meta-Tool 通过控制实验对比超网络生成的 LoRA 权重与少样本提示，验证了后者的充分性。该负面结果挑战了“参数更新优于提示”的假设，但在单轮任务边界内，其结论对多步复杂任务的普适性存疑。

】

---

【MetaMem: Evolving Meta-Memory for Knowledge Utilization through Self-Reflective Symbolic Optimization ｜元记忆引导的外部记忆利用框架

研究机构：美国东北大学、清华大学

作者：Haidong Xin、Xinze Li、Zhenghao Liu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fc0c16e5e4ef)

> 长程人机交互中，外部记忆系统常因碎片化存储破坏事实间的逻辑与时间关联，导致模型在整合多源证据时产生推理错误。现有方案侧重于优化记忆的存储结构或检索精度，却忽视了模型“如何正确使用”已检索到的矛盾或冗余信息。MetaMem 引入自进化的元记忆模块，通过自反思机制将知识利用策略显式化并动态更新。该框架在 LongMemEval 基准上显著优于现有外部记忆系统，但其性能增益高度依赖骨干模型的指令遵循能力与反思质量，且未涉及记忆安全与隐私泄露风险。

】

---

【MINED: Probing and Updating with Multimodal Time-Sensitive Knowledge for Large Multimodal Models ｜多模态时间敏感知识基准与更新

研究机构：中国科学技术大学、山东大学

作者：Kailin Jiang、Ning Jiang、Yuntao Du 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.19457)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_311dbb4ef964)

> 大语言模型（LLM）与大视觉语言模型（LMM）的参数化知识是静态的，无法实时追踪现实世界事实的动态演变，导致在处理时效性查询时产生幻觉或过时输出。现有基准多聚焦于文本逻辑推理或静态视觉问答，缺乏对“视觉实体属性随时间变化”这一多模态时效性问题的系统性评估。MINED 通过构建包含 2,104 个样本、覆盖 6 个维度的基准，量化了 LMM 在时间敏感知识上的认知、感知与鲁棒性缺陷，并验证了知识编辑在单点更新场景下的可行性。该工作填补了多模态时效性评估空白，但仅验证了单点编辑效果，未解决多模态知识编辑的泛化性与长期稳定性问题。

】

---

【Mistake Notebook Learning: Batch-Clustered Failures for Training-Free Agent Adaptation ｜错误笔记本学习

作者：Xuanbo Su、Yingfang Zhang、Hao Luo 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77668cc3f3eb)

> 导读 自进化智能体在开放环境中面临的核心矛盾是：静态权重无法适应动态任务，而纯参数微调又受限于高昂计算成本与灾难性遗忘。现有非参数化记忆方法多依赖实例级经验存储，导致记忆冗余且泛化能力弱，难以从孤立错误中提炼通用规律。MNL 提出了一种基于批量聚类错误抽象的无训练记忆框架，通过“若改进则接受”的保守更新机制，将失败轨迹蒸馏为结构化指导，从而在保持模型权重冻结的前提下实现能力迭代。该方法在数学推理与智能体任务中展示了极高的记忆效率，但其性能上限是否仍受制于非参数化机制的固有局限，尚需更长期的纵向对比验证。

】

---

【MIThinker: A Plug-and-Play Policy-Optimized Thinker For Motivational Interviewing Counseling ｜解耦式思维生成与策略对齐

研究机构：北京理工大学、新加坡管理大学

作者：Yizhe Yang、Palakorn Achananuparp、Heyan Huang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_98ca20f8f58f)

> 动机访谈（Motivational Interviewing, MI）咨询要求模型在生成回复前，先完成对客户心理状态的评估与策略选择，但现有大语言模型（LLM）往往直接生成回复，缺乏显式的临床推理过程，导致干预缺乏深度且计算开销巨大。本文切入点在于将“思维生成”与“响应生成”解耦，提出轻量级思维模型 MIThinker，通过逆向工程构建思维数据并采用强化学习优化策略对齐。该方法以极低的计算成本实现了接近多智能体框架的临床保真度，但其对复杂危机情境的覆盖能力仍存疑。

】

---

【Mitigating Cultural Bias in LLMs via Multi-Agent Cultural Debate ｜多智能体文化辩论

研究机构：中国科学技术大学

作者：Qian Tan、Lei Jiang、Yuting Zeng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12091)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12091)

> 大语言模型在跨文化部署中默认输出西方价值观，而现有评估基准强制将模型输出归类至特定文化，无法识别真正中立响应。本文指出，切换至中文提示仅将偏差转移至东亚视角，而非消除偏差，且功能型智能体框架无法保证文化视角的显式代表。为此，作者构建了包含“无偏见”选项的双语基准CEBiasBench，并提出赋予智能体显式文化身份的多智能体文化辩论框架MACD。该方法通过结构化辩论实现推理时去偏，但其在自建基准上的高分是否源于评估者从众效应，以及文化人设是否引入新刻板印象，仍存疑。

】

---

【Mitigating Judgment Preference Bias in Large Language Models through Group-Based Polling ｜基于群组轮询优化的大语言模型评判偏好偏差缓解

作者：Shuliang Liu、Zhipeng Xu、Zhenghao Liu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b98b4bfe9702)

> 大语言模型作为自动评估者（LLM-as-a-Judge）在替代人类标注时，常因自我偏好偏差（Self-Preference Bias）高估自身生成的响应，导致评估信号失真。现有推理时集成或提示去偏方法无法从根本上消除该偏差，且往往依赖强模型指导弱模型。本文提出无监督多智能体群组轮询优化框架（Genii），通过异构模型间的客户端-服务器交互生成一致性偏好对，利用直接偏好优化（DPO）更新模型参数。该方法在无人类标注条件下优于有监督微调，但其在复杂推理任务上的绝对准确率仍低于领域SOTA，且未验证大规模模型的扩展性。

】

---

【Mitigating Position Bias in Transformers via Layer-Specific Positional Embedding Scaling ｜层特定位置嵌入缩放

研究机构：复旦大学、西湖大学

作者：Zhenghua Wang、Yiran Ding、Changze Lv 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df706e093bae)

> 长上下文大语言模型普遍存在“中间迷失”现象，即模型对序列首尾信息的注意力显著高于中间部分，导致关键信息被忽略。现有缓解方案如多基线集成或头级缩放虽能改善注意力分布，但需多次前向传播，带来高昂的推理延迟。本文提出层特定位置嵌入缩放（Layer-Specific Positional Embedding Scaling, LPES），通过为每层分配独立的RoPE缩放因子并引入贝塞尔曲线约束的遗传算法进行自动搜索，在单次前向传播中实现注意力均衡。该方法在关键值检索任务上取得最高11.2%的准确率提升，但其效果依赖于特定数据集的预搜索，且未验证其在复杂推理任务中的泛化边界。

】

---

【MMTabReal: Real-World Benchmark for Multimodal Table Understanding ｜多模态表格理解基准 MMTABREAL

研究机构：美国亚利桑那州立大学

作者：Prasham Yatinkumar Titiya、Jainil Trivedi、Chitta Baral 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f5ed08d0e38)

> 多模态表格推理旨在让模型同时解析嵌入在二维布局中的文本、数值与视觉线索，但现有基准多依赖合成数据或单一模态，无法反映真实世界中图标、图表与层级表头交织的复杂性。本文切入点在于构建一个纯人工标注、仅用于评估的真实世界多模态表格问答数据集，以量化当前多模态大语言模型（MLLM）在跨模态对齐上的真实短板。通过五种基线策略与多模型对比，MMTABREAL 揭示了视觉输入缺失导致的性能断崖及“高召回低精确”的对齐悖论。该基准填补了真实场景评测空白，但其评估协议依赖特定提示策略，且未涵盖专用表格结构模型，限制了结论的普适性。

】

---

【Modeling and Solving Stable Matching under Probabilistic Preferences with Large Language Models ｜基于大语言模型概率偏好的稳定匹配建模

作者：Yuqi Kong、Shiyu Liu、Jiaxu Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_977a2872d846)

> 双边匹配市场中的经典稳定匹配理论假设偏好是确定性的，但真实人类决策充满噪声与切换成本，导致经典稳定性指标失效。现有方法要么忽略偏好不确定性，要么仅将LLM视为静态偏好生成器，未能利用其概率性决策特性优化匹配机制。本文切入点在于验证LLM决策符合有界理性下的量化响应模型，并据此设计连续稳定性度量与混合匹配算法。其价值在于将LLM从“行为模拟器”转化为“机制设计工具”，但实验仅覆盖单一数据集且未评估匹配效率，结论的普适性存疑。

】

---

【MoE Adapter for Large Audio Language Models: Sparsity, Disentanglement, and Gradient-Conflict-Free ｜稀疏专家混合适配器

研究机构：清华大学

作者：Yishu Lei、Shuwei He、Jing Hu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02967)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02967)

> 大型音频语言模型（LALM）在处理语音、音乐与环境音时，常因单一密集适配器导致参数更新方向相互抵消，引发梯度冲突。现有主流架构假设音频信号服从统一分布，无法解耦异构声学属性，致使模型在语义推理与副语言理解上受限。本文提出 MoE-Adapter，通过动态路由机制将音频特征分配至专门化专家，以稀疏激活实现特征解耦。该方法在固定参数预算下优于密集基线，但其绝对性能仍显著低于领域最先进模型，且未验证其在长音频或复杂推理链中的有效性。

】

---

【MonCulture-Eval: A Hierarchical Benchmark for Evaluating Mongolian Cultural Capabilities of Large Language Models across Scripts and Regions ｜蒙古语双文字文化对齐基准

作者：Quulgan Minggad、Xiao Zinan、Yuan Sun

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcac3d550b82)

> 大语言模型在低资源非西方语言中常出现“语言流利但文化错位”的断层，现有通用基准多依赖网络爬取数据，难以区分模型是真正理解文化逻辑还是仅靠翻译捷径作答。本文针对蒙古语双文字系统（传统竖排与西里尔字母）及三个区域亚文化，构建了基于原生非数字化档案的层级化评估基准。通过引入脚本对齐一致性（SAC）指标与三层认知框架，量化了模型在事实、情境与价值观层面的本体论对齐程度。该基准揭示了前沿模型普遍存在的“脚本鸿沟”与“游客视角”偏差，但受限于单一语言场景，其结论向其他低资源双文字系统的推广性尚待验证。

】

---

【Moneyball with LLMs: Analyzing Tabular Summarization in Sports Narratives ｜体育叙事动态表格生成的多实体状态追踪诊断

作者：Ritam Upadhyay、Naman Ahuja、Rishabh Baral 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_72dab4199901)

> 长上下文叙事转表格任务的核心矛盾在于，模型需同时维持多实体状态追踪与局部数值聚合，而现有分解策略往往混淆了这两者的贡献。主流方法依赖提示工程或迭代生成，但缺乏对模型内部状态维护机制的因果归因，导致性能提升来源不明。本文通过构建双域体育基准 SPORTABSET，系统性解耦多实体干扰与局部算术能力，并引入标签不变扰动以暴露表面线索依赖。该工作揭示了多实体记忆是长上下文表格生成的主要瓶颈，但其在真实世界噪声表格中的泛化能力仍存疑。

】

---

【More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists ｜多智能体协作下的对抗鲁棒性边界

研究机构：德国波恩大学

作者：Khashayar Alavi、Zhastay Yeltay、Lucie Flek 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.07112)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.07112)

> 多智能体协作旨在通过采样投票提升大语言模型在数学任务上的准确率，但现有研究默认这种集成机制能同步增强模型对输入扰动的抵抗力。本文发现这一假设不成立：协作虽能单调提升清洁输入下的性能，却无法缩小对抗噪声导致的性能差距。作者构建了一套包含合成标点与真实拼写错误的噪声分类法，在六个开源模型上量化了这种“鲁棒性缺口”。该工作揭示了投票机制在系统性偏差下的失效机制，但受限于仅使用同构模型，其结论对异构集成场景的普适性存疑。

】

---

【MorphBPE: Morphology-Aware Tokenization for Efficient LLM Training ｜形态感知字节对编码

研究机构：德国人工智能研究中心

作者：Ehsaneddin Asgari、Yassine El Kheir、MohammadAli SadraeiJavaheri 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6bc7c87ad3e4)

> 子词分词器在形态丰富语言中常因纯频率驱动导致词素边界断裂，引发模型学习负担增加。现有统计分词方法难以兼顾压缩效率与语言学结构，而纯形态分析器又缺乏数据驱动的灵活性。本文提出 MorphBPE，在 BPE 训练阶段引入词素边界约束，推理阶段保持标准 BPE 行为。该方法在受控实验中降低了交叉熵并提升了下游任务表现，但其依赖高质量形态标注，在资源稀缺语言中的可扩展性存疑。

】

---

【MorphoBench: A Benchmark with Difficulty Adaptive to Model Reasoning ｜自适应难度推理基准

研究机构：北京大学、北京航空航天大学

作者：Xukai Wang、Xuanbo Liu、Mingrui Chen 等 19 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.14265)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.14265)

> 现有静态推理基准无法随模型能力进化而动态调整难度，导致评估失效。MORPHOBENCH 通过证明图形式化推理难度，并利用模型反馈动态修改题目条件或提示，实现了难度与模型能力的匹配。其价值在于提供了跨学科动态评估框架，但依赖 o3-mini 自动判分且未验证难度调节对逻辑完整性的影响，存疑。

】

---

【MT-OSC: Path for LLMs that Get Lost in Multi-Turn Conversation ｜一次性顺序压缩框架

作者：Jyotika Singh、Fang Tu、Miguel Ballesteros 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0c6fc0e88a13)

> 多轮对话中，用户指令与关键上下文分散在多个轮次，导致大语言模型（LLM）性能显著衰减，而全量追加历史又迅速耗尽上下文窗口并增加延迟。现有压缩方法依赖微调、复杂层级结构或实时检索，难以在不牺牲信息保真度的前提下实现低延迟部署。MT-OSC 提出一种后台异步执行的一次性顺序压缩框架，通过少样本提示的 Condenser 与基于重叠度规则的 Decider 动态精简历史，在 10 轮对话中实现最高 72% 的 Token 削减，同时保持或提升任务准确率。该方案在工程集成上具有显著优势，但其压缩保真度边界与 Decider 规则的泛化能力仍存疑。

】

---

【Multi-Drafter Speculative Decoding with Alignment Feedback ｜多草稿器投机解码与对齐反馈

作者：Taehyeon Kim、Hojung Jung、Se-Young Yun

论文原文见 [arXiv](https://arxiv.org/abs/2604.05417)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e5336fb8d57e)

> 投机解码（Speculative Decoding, SD）旨在通过草稿-验证机制无损加速大语言模型（LLM）推理，但单一草稿器在动态多任务场景下泛化能力受限。现有静态路由或独立草稿器方案无法实时适应输入分布变化，导致接受率波动。METASD 将草稿器选择建模为多臂老虎机（Multi-Armed Bandit, MAB）问题，利用块散度（Block Divergence, BD）奖励实现在线动态路由。该框架在混合任务负载下显著优于静态基线，但其理论假设的平稳性在极端非平稳场景下的鲁棒性尚存疑。

】

---

【Multi-Hop Knowledge Editing via Critic-Guided Multi-Agent Reasoning ｜多跳知识编辑中的闭环推理框架

研究机构：北京理工大学、新西兰奥克兰大学

作者：Xudong Li、Yuhang Tian、Dandan Song 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2bcea90cf3a2)

> 多跳知识编辑（Multi-Hop Knowledge Editing, MHKE）要求模型在更新事实后，能正确沿推理链传播新信息，但现有前馈式方法缺乏错误定位机制，早期检索噪声会静默级联至最终答案。CARE 通过引入链级验证与有界回溯的闭环推理，将单向分解-检索流程改造为可自我修正的多智能体协作。该方法在 MQuAKE-hard 上实现了 94.17% 的准确率，但在通用多跳场景下仍落后于最新图结构方法，其闭环机制的计算开销与深层链覆盖能力存疑。

】

---

【MultiCodeAttack: Iterative Jailbreak Attacking on LLMs with Multi-Code Prompt Injection ｜多语言代码模板越狱攻击

作者：Weifeng Sun、Meng Yan、Zhou Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83217a6cfeee)

> 现有结构化越狱方法依赖单一编程语言和静态模板，导致攻击面受限且易被防御机制识别。本文指出不同编程语言对同一模型的安全对齐强度存在显著差异，且静态模板缺乏适应性。MultiCodeAttack 通过多臂老虎机动态选择语言，结合语义保持变异与响应感知反馈，实现了跨语言的迭代优化攻击。该方法在恶意代码生成任务上取得了 92.51% 的攻击成功率，但其在推理增强模型上的鲁棒性验证仍显单薄。

】

---

【Multilingual Refusal Alignment for Safer Large Language Models ｜多语言拒绝对齐：RefusEU 数据集与 DPO 跨语言迁移实验

研究机构：英国伦敦大学学院

作者：Aleksandra Krasnodębska、Wojciech Kusa、Aldo Lipani

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d35ff25464c6)

> 导读 多语言大语言模型在全球部署中面临安全行为不一致的困境，根源在于安全对齐数据对英语的过度依赖，导致模型在低资源语言中拒绝机制失效。现有方法多依赖翻译或单语对齐，但缺乏系统性的跨语言受控实验来验证单语对齐的迁移边界。本文构建了覆盖 12 种欧洲语言的 RefusEU 数据集，并采用消融安全机制后的模型作为基线，通过 DPO 训练量化不同数据配置下的安全恢复效果。该工作提供了首个欧洲多语言拒绝对齐基准，但其结论受限于特定语言家族，且未深入探讨安全与语言身份在表征空间中的纠缠机制。

】

---

【Multilingual Tokenization through the Lens of Indian Languages: Challenges and Insights ｜印度语言多语言分词：正字法归一化与词汇表聚类策略

研究机构：印度理工学院、印度理工学院孟买分校

作者：Maharaj Brahma、N J Karthika、Rajat Verma 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_40a63e8a95c3)

> 多语言分词器在低资源语言上常因高资源语言主导词汇表分配而导致分词碎片化，进而推高计算成本并削弱模型对形态结构的捕捉能力。现有静态分词方法虽能处理开放词汇，但难以应对印度语言特有的正字法变体与复杂形态结构，导致同一语义单元被映射为多个冗余 Token。本文通过引入脚本/正字法归一化预处理，并采用基于语言家族的聚类策略构建多语言词汇表，系统评估了 17 种印度语言的分词效率与下游任务表现。该研究提供了针对形态丰富语言的实证指导，但其结论局限于静态分词框架，未探索动态分词架构在解决此类结构性不公上的潜在优势。

】

---

【Multimodal Item Scoring for Natural Language Recommendation via Gaussian Process Regression with LLM Relevance Judgments ｜高斯过程回归增强的大语言模型自然语言推荐

作者：Yifan Simon Liu、Qianfeng Wen、Jiazhou Liang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d2d70c92690a)

> 自然语言推荐（NLRec）旨在根据用户自由文本请求生成物品建议，但现有密集检索（DR）方法将请求嵌入视为唯一相关性信号，导致评分函数呈单峰分布，无法捕捉复杂请求中分散在不同语义区域的多模态相关性。本文提出GPR-LLM，利用少量大语言模型（LLM）标注的锚点段落，通过高斯过程回归（GPR）估计底层相关性函数，以突破DR的单峰假设。该方法在四个NLRec数据集上较基线提升最高65%，但其性能增益是否完全源于GPR的外推能力而非LLM骨干本身，尚需更严格的消融验证。

】

---

【Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks ｜多模态基础模型遗忘的系统级分类与干预机制综述

研究机构：美国圣母大学

作者：Nobin Sarwar、Shubhashis Roy Dipta、Zheyuan Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.07907)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.07907)

> 多模态基础模型在预训练中不可避免地编码了跨模态的敏感、版权或有害关联，而重训练在工程上不可行，现有算法中心化的分类体系难以揭示端到端流水线中真正的干预点。本文提出以“干预阶段-控制路径”为核心的系统级分类框架，将遗忘方法从数据侧、训练时、架构约束到解码时进行统一梳理，并形式化了多模态近似重训练的分布等价性。该综述为跨模态遗忘提供了稳定的比较脚手架，但其作为纯综述缺乏原创算法验证，且对解码时干预是否满足不可逆合规要求未给出明确理论界定。

】

---

【Multiplication in Multimodal LLMs: Computation with Text, Image, and Audio Inputs ｜多模态大语言模型中的算术鲁棒性与启发式指纹

作者：Samuel Gideon Balter、Ethan Jerzak、Connor Thomas Jerzak

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_614c18a22f3a)

> 导读 多模态大语言模型（Multimodal Large Language Models, MLLMs）在处理基础算术时存在严重的模态依赖与计算脆弱性，现有基准往往混淆感知错误与计算错误，导致无法准确归因性能瓶颈。本文切入点在于构建一个控制变量下的多模态乘法基准，通过解耦感知与计算环节，并引入基于损失探针的内部机制分析，揭示模型在模态切换下的真实算术极限。具体做法是定义算术负载指标，利用强制完成损失探针量化模型对特定算术启发式的偏好，并通过低秩适配器（Low-Rank Adaptation, LoRA）几何分析验证内部路由机制。该工作提供了诊断MLLM算术缺陷的新工具，但其结论局限于乘法运算，且LoRA实验显示外部干预可能破坏模型原生路由，其泛化性存疑。

】

---

【Nash-Pruned CredMAS: Dynamic Panel Pruning for VLM-MAS using Nash-based Selection and Doubly-Robust Credits ｜纳什剪枝可信多智能体系统

研究机构：中山大学

作者：Yijia Fan、Mingyu Liu、Jing Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1128085fe323)

> 多轮视觉语言模型（VLM）多智能体系统（MAS）面临静态面板导致的 $O(N \times T)$ 通信成本爆炸与低价值代理引入的噪声干扰。现有启发式路由或一次性剪枝方法缺乏理论保证，且无法动态适应上下文依赖的边际效用变化。本文提出 NP-CredMAS，通过离线双重稳健因果价值学习与在线子模最大化拍卖机制，实现推理时的动态资源分配。该方法在保持 SOTA 性能的同时显著降低 Token 消耗，但其因果估计对离线日志分布偏移的鲁棒性尚存疑。

】

---

【Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging ｜导航对齐-校准权衡：基于模型合并的帕累托前沿

研究机构：英国剑桥大学

作者：Tiancheng Hu、Benjamin Minixhofer、Nigel Collier

论文原文见 [arXiv](https://arxiv.org/abs/2510.17426)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17426)

> 后训练旨在提升大语言模型的指令遵循能力，但常伴随准确率下降与校准度恶化，即“对齐税”。现有缓解策略多聚焦于训练时的正则化或数据筛选，忽视了校准度这一隐性成本，且难以在保持对齐收益的同时恢复模型的不确定性表征。本文提出一种训练后（Post-hoc）的权重插值方法，通过混合预训练与指令微调模型的权重，在无需梯度更新的情况下探索对齐-校准帕累托前沿。该方法在多个基准上实现了准确率的帕累托改进并部分恢复了校准度，但其有效性依赖于白盒权重访问，且未量化对安全对齐的潜在稀释效应。

】

---

【NeoAraBERT: A Modern Foundation Model for Arabic Embeddings with Diacritics-Aware Tokenization and POS-Targeted Masking ｜NeoAraBERT：基于变音符号感知分词与词性掩码的阿语编码器

作者：Chadi Abou Chakra、Hadi Khaled Hamoud、Osama Rakan Al Mraikhat 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_48b068fdbfaa)

> 阿语编码器长期受限于形态复杂性导致的表示碎片化，现有模型在古典阿语与语义嵌入任务上表现疲软。本文切入点在于将现代Transformer架构（NeoBERT）与阿语特有的变音符号分离机制结合，通过词性条件掩码优化预训练信号。具体做法是构建包含MSA、古典阿语及方言的混合语料，采用变音符号感知分词器与POS-targeted掩码策略进行预训练。该模型在23项任务中18项取得最优，但在方言任务上未全面超越专用模型，且未对比多语言大模型基线。

】

---

【Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models ｜神经思维链搜索

研究机构：中山大学

作者：Guoming Ling、Zhongzhan Huang、Yupei Lin 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_29a74a5d98d7)

> 现有大语言模型在生成思维链时缺乏全局规划，常陷入冗余验证或低效分支，导致计算资源浪费。静态长度惩罚或后处理剪枝无法在生成过程中动态识别并规避这些次优路径。本文提出神经思维链搜索框架，将推理重构为对“思考算子”的动态前瞻搜索，通过双因子启发式函数同时评估正确率与效率。该方法在多个基准上实现了准确率与生成长度的帕累托改进，但其依赖小算子空间假设，且在复杂知识密集型任务上的增益显著衰减，暴露了搜索机制对任务类型的敏感性。

】

---

【Neuronal Insights into LLM Attacks: Targeted Neuron Tuning for Precise and Robust Vulnerability Patching ｜基于相似度归因的神经元级漏洞修补

研究机构：天津大学

作者：Dan Shi、Renren Jin、Zhuowen Han 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0561b6dda2a)

> 大语言模型（LLM）的安全对齐长期面临“浅层性”困境，即模型仅在表面特征上表现出拒绝行为，深层语义中仍可能泄露有害内容。现有梯度归因方法依赖固定标签，无法处理越狱攻击中开放生成任务无标准答案的特性，导致关键神经元定位失效。本文提出基于相似度的梯度归因法，量化神经元对开放生成输出的影响，并据此实施仅微调最小关键神经元子集的 Targeted Neuron Tuning (TNT)。该方法在自有基准上实现了高安全率，但其评估协议未覆盖标准基准，泛化性存疑。

】

---

【NeuroSym-Cal: Bridging the Reasoning-Execution Gap in Code Generation via Hierarchical Calibration ｜神经符号分层校准：代码生成中的置信度去饱和

作者：Peiyang Liu、Yining Wang、Youru Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_286efca23771)

> 推理模型在代码生成中常陷入“自信地犯错”的困境，即系统性错误导致采样输出高度一致，使基于一致性的校准方法失效。现有方法如Self-Consistency（SC）无法区分“稳健正确”与“顽固幻觉”，导致高置信度下的严重误判。本文提出NEUROSYM-CAL，通过融合基于抽象语法树（AST）的外部共识与模型后验自我验证的内部信号，构建非线性校准网络以解饱和置信度。该方法在域外（OOD）基准上显著降低了期望校准误差（ECE），但其依赖额外训练数据且未与最新语义熵方法对比，泛化边界尚存疑。

】

---

【NITI: Neural Plan Concretization for Incremental Execution, Bridging and Trigger Inference from Underspecified Human Policies ｜神经计划具体化框架

作者：Ayan Banerjee、Shomrik Barua Banerjee、Sandeep Gupta

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01214c2289d3)

> 安全关键领域的执行困境在于，人类策略往往故意省略前置条件与异常处理，而现有大语言模型（LLM）或强化学习（RL）范式无法在缺乏完整状态枚举和显式奖励的情况下可靠执行此类未指定策略。NITI 提出了一种神经符号框架，将 LLM 定位为执行时的“具体化器”而非自主规划器，通过验证器接地的增量执行、触发推断与神经桥接机制，在无需训练或微调的前提下实现长程任务的安全执行。该框架在魔方解法与胰岛素给药任务中显著优于基线，但其对符号提示结构的依赖及连续状态空间的泛化能力仍存疑。

】

---

【No One Fits All: From Fixed Prompting to Learned Routing in Multilingual LLMs ｜多语言提示策略的自适应路由

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Wei-Chi Wu、Sheng-Lun Wei、Hen-Hsen Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16937)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f9c48911b33b)

> 导读 多语言大语言模型（Multilingual Large Language Models, mLLMs）在处理低资源语言时，常因预训练数据中英语的主导地位而依赖“翻译至英语再推理”的提示策略，但该策略在高资源语言或文化敏感任务中往往失效。现有研究多聚焦于优化单一提示范式，缺乏对“何时翻译、何时原生”这一决策问题的系统性建模。本文提出基于轻量级分类器的提示策略路由框架，通过响应特征差异预测最优提示方式，在四个基准上实现统计显著的性能提升。该框架验证了语言资源等级而非翻译质量是决定策略有效性的核心变量，但其仅优化输入端策略，未触及模型内部表征对齐的根本缺陷。

】

---

【Not All Modalities at Once: Dynamic Dropout and Bidirectional Fusion for Robust Multi-modal Knowledge Graph Completion ｜模态丢弃与双向门控融合

研究机构：美国东北大学

作者：Jiashun Peng、Fu Zhang、Hongzhi Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b6df3569bffd)

> 多模态知识图谱补全（Multi-modal Knowledge Graph Completion, MKGC）旨在利用文本、图像与结构化三元组推断缺失链接，但现有方法在训练时默认所有模态始终可用且互补，导致模型在异构噪声下产生模态依赖与竞争。本文指出，这种“全模态无差别训练”忽视了单模态对训练动态的独立影响，进而提出MDBGF框架，通过概率驱动的模态丢弃（Modality Dropout, MD）与双向门控融合（Bidirectional Gated Fusion, BGF）动态调控模态使用。该框架在轻量级嵌入骨干上实现了多模态基准的SOTA，但其未验证在大型语言模型（Large Language Models, LLMs）骨干下的有效性，且缺乏对推理时模态缺失鲁棒性的直接评估。

】

---

【NSF-CoT: Neuro-Symbolic Formal Verification of Chain-of-Thought Faithfulness in Contextual Question Answering ｜神经符号形式化验证思维链

作者：Vishal Pramanik、Maisha Maliha、Nathaniel D. Bastian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_faa056e91f8c)

> 思维链（CoT）生成的中间步骤常被用户视为模型决策的真实解释，但现有评估方法仅能检测“修改文本是否改变答案”，无法验证步骤是否由给定证据逻辑推导而来。本文针对上下文问答场景，提出一种结合符号逻辑求解与内部事实归因的混合验证框架。该方法将自然语言步骤解析为一阶逻辑原子，通过反事实消融识别模型实际依赖的事实子集，并利用SMT求解器与LLM裁判联合判定每步的接地性、有效性与效用性。NSF-CoT在多个基准上优于纯行为干预基线，但其依赖受限谓词表与线性归因假设，在复杂非线性推理中的泛化能力存疑。

】

---

【O1-Pruner: Length-Harmonizing Fine-Tuning for O1-Like Reasoning Pruning ｜长度协调微调

作者：Haotian Luo、Haiying He、Yibo Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f53b21ab79a8)

> 长思维链模型在简单任务上产生冗余推理，导致计算资源浪费，现有提示工程或监督微调难以在保持准确率的同时有效压缩推理长度。本文切入点在于识别“长度不和谐”现象，即短答案往往已具备高准确率，长答案成为无效开销。通过构建基于参考模型基线的强化学习奖励函数，利用离策略PPO训练使模型内化简洁推理习惯。该方法在中等难度数学任务上实现了准确率与效率的双赢，但在极限难度任务上性能显著退化，其离策略训练机制对复杂逻辑探索能力的潜在抑制值得警惕。

】

---

【ODTQA-FoRe: An Open-Domain Tabular Question Answering Dataset for Future Data Forecasting and Reasoning ｜开放域表格未来数据预测与推理问答

研究机构：北京师范大学、香港浸会大学

作者：Zhensheng Wang、Xiaole Liu、Wenmian Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.02433)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.02433)

> 开放域表格问答长期局限于静态历史数据的检索与提取，无法响应用户对“未来趋势”的预测性询问。现有大语言模型缺乏时序建模机制，且开放域场景下用户无法提供连续历史数据，导致预测任务在数据获取与数值生成两端均存在断点。本文提出 ODTQA-FoRe 任务与 TimeFore 框架，通过 SQL 自主检索历史数据、调用外部时序模型生成预测值、再由 LLM 进行标准化推理，填补了表格问答中动态预测的空白。该工作确立了垂直领域预测问答的基准，但受限于单一房地产数据源，其跨域泛化能力与 LLM 内生预测能力的边界尚待厘清。

】

---

【OFFSIDE: Benchmarking Unlearning Misinformation in Multimodal Large Language Models ｜OFFSIDE：多模态大语言模型虚假信息遗忘基准

研究机构：哈尔滨工业大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Hao Zheng、Zirui Pang、Ling li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22535)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22535)

> 多模态大语言模型（MLLMs）在预训练中不可避免地记忆了包含视觉与文本耦合的虚假信息，而现有机器遗忘（Machine Unlearning, MU）基准缺乏对图像内部有害线索的覆盖，导致无法评估模型在真实场景下的遗忘鲁棒性。本文提出 OFFSIDE 基准，通过构建包含真实足球转会谣言的多模态数据集，首次引入细粒度遗忘与视觉谣言移除任务。实验表明，现有主流遗忘方法在视觉谣言场景下完全失效，且遗忘效果主要由灾难性遗忘驱动而非知识擦除。该基准揭示了当前 MLLM 遗忘方法的重大盲区，但受限于仅测试了五种经典优化算法，未涵盖机制级干预方法。

】

---

【OMHBench: Benchmarking Balanced and Grounded Omni-Modal Multi-Hop Reasoning ｜全模态多跳推理基准：OMHBench

研究机构：韩国汉阳大学、索尼AI

作者：Seunghee Kim、Ingyu Bang、Seokgyu Jang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2508.16198)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f60af72fee23)

> 全模态大语言模型（MLLMs）在处理文本、视觉与语音联合输入时，常因评估基准存在模态捷径或推理路径偏斜而表现虚高。现有全模态理解（OMU）基准允许模型忽略部分模态作答，跨模态多跳推理（CMR）基准则排除语音且路径分布严重失衡，导致无法真实反映模型的跨模态整合能力。OMHBench 通过强制三模态联合接地与模态排列组合，构建了 6,144 道平衡多跳推理题，并引入路径平衡分数（PBS）量化模型对模态顺序的鲁棒性。该基准揭示了模型在语音模态接地上的系统性不对称，但受限于静态表格数据源，其结论在动态视频或实时音频场景下的普适性尚存疑。

】

---

【OmniCode: A Benchmark for Evaluating Software Development Agents ｜全生命周期软件工程智能体基准

研究机构：美国康奈尔大学、美国纽约大学

作者：Atharv Sonwane、Eng-Shen Tu、Wei-Chung Lu 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a20366a07501)

> 现有代码智能体基准聚焦于单一补丁生成任务，无法评估模型在测试编写、代码审查响应及风格合规等真实开发环节的综合能力。本文通过合成负样本与多任务扩展，构建覆盖Python、Java、C++三语言的1794项任务基准，揭示当前SOTA模型在非Python语言及测试生成上的显著短板。其价值在于暴露了单一指标评估的盲区，但$2/instance的成本约束可能低估高复杂度任务的真实性能。

】

---

【OmniCompliance-100K: A Multi-Domain, Rule-Grounded, Real-World Safety Compliance Dataset ｜规则接地真实世界合规数据集

研究机构：香港科技大学

作者：Wenbin Hu、Huihao Jing、Haochen Shi 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_270f2f3b3b34)

> 大语言模型（LLM）安全对齐长期依赖合成数据，导致模型在真实法律合规场景下泛化能力不足。现有基准如ToxicChat和WildGuard由LLM生成，缺乏真实执法案例的多样性与严谨性，无法覆盖金融、医疗等高 stakes 领域的具体法规条款。本文通过构建首个大规模、多领域、规则接地的真实世界合规数据集，填补了从“通用有害内容抑制”到“具体法规合规判断”的数据空白。该数据集揭示了现有安全护栏在合规任务上的严重失效，但其仅评估准确率而未考察合规判断对模型有用性的影响，这一局限值得警惕。

】

---

【On Safety Risks in Experience-Driven Self-Evolving Agents ｜经验驱动自进化智能体的安全退化机制

作者：Weixiang Zhao、Yichen Zhang、Yingshuo Wang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_375a1df0ee59)

> 自进化智能体通过复用交互轨迹提升任务能力，但现有安全评估多关注参数更新或显式有害指令，忽略了纯良性经验在高风险场景下的隐性风险。本文切入点在于证明：即使经验完全源自良性任务，其“执行导向”结构仍会导致智能体在高风险场景中安全边界系统性崩塌。通过构建离线/在线双范式实验与长度匹配对照，本文量化了这一退化过程并归因于经验中的执行偏差。该研究揭示了非参数化进化的固有安全漏洞，但其在混合经验场景下的安全-效用权衡机制仍显粗糙，且未提供有效的缓解方案。

】

---

【One LLM Does Not Simulate All Students: Ability-Aware Student Simulation via Cognitive Diagnosis Guided LLM Assignment ｜基于认知诊断的LLM能力对齐学生模拟

作者：Huixing Que、Qi Liu、Weibo Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8093eb585376)

> 教育领域学生行为模拟旨在通过预测个体学习轨迹提供个性化教学支持，但现有方法普遍依赖单一高容量大语言模型（LLM）模拟所有学生，导致高能力学生被低估、低能力学生被高估的系统性偏差。本文指出这种“一刀切”策略源于LLM预训练知识带来的不可控能力先验，而非模型架构缺陷。作者提出利用神经认知诊断（NeuralCD）提取学生与LLM的潜在认知画像，通过余弦相似度匹配最适配的LLM作为模拟骨干。该方法在DBE-KT22数据集上将整体模拟保真度提升至0.505，但受限于静态能力假设与单一领域验证，其泛化边界尚待考察。

】

---

【One Mask to Rule Them All: On Hidden Facts after Editing and How to Find Them ｜定位-编辑范式的注意力劫持机制与共享掩码反转

作者：Ali Holmov、Paul Youssef、Nandi Schoots 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.28839)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f7033d75140)

> 定位-编辑方法（Locate-and-Edit）通过修改前馈神经网络（FFN）权重实现事实更新，但现有评估仅关注输出行为，掩盖了内部知识是否被真正覆盖的机制盲区。ROME与MEMIT虽在基准上表现优异，却难以解释为何单点修改能对抗Transformer的冗余知识路径，且存在涟漪效应与安全漏洞。本文切入点在于验证编辑是否依赖共享的注意力抑制机制而非知识擦除，通过训练跨编辑共享的二元掩码反转编辑效果。该发现揭示了定位-编辑方法的根本局限，为编辑检测与防御提供了新路径，但反转率未达100%且未覆盖非参数编辑路线。

】

---

【One Script Instead of Hundreds? On Pretraining Romanized Encoder Language Models ｜罗马化预训练对高资源语言性能的影响评估

作者：Benedikt Ebing、Lennart Keller、Goran Glavaš

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e030b58cf730)

> 多语言编码器模型在跨语言迁移中常受限于脚本壁垒，即不同书写系统间的词汇重叠被阻断。现有研究多聚焦于低资源语言从拉丁脚本高资源语言迁移的场景，却忽略了罗马化（Romanization）对高资源语言自身性能可能造成的信息损失与表征稀释。本文通过受控预训练实验，量化了将六种高资源语言统一为拉丁脚本后的下游任务性能变化，发现分段脚本损失可忽略，而形态音节脚本存在显著退化。这一发现为大规模多语言模型的脚本统一策略提供了实证依据，但其在更大规模模型下的鲁棒性仍存疑。

】

---

【OpenExempt: A Diagnostic Benchmark for Legal Reasoning and a Framework for Creating Custom Benchmarks on Demand ｜法律破产豁免推理诊断基准

作者：Sergio Servantez、Sarah B. Lawsky、Rajiv Jain 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8de1f4ce7e26)

> 静态法律基准将复杂推理压缩为单一准确率指标，无法隔离模型在规则应用、时序判断或干扰抵抗上的具体失效点。现有方案依赖人工标注，成本高且难以动态调整难度，导致评估信号模糊。OpenExempt 利用符号化法律逻辑与分支定界求解器，按需生成可机器验证的动态任务，实现了对推理链条中阶段错误与传播错误的因果分解。该框架在 13 个模型上揭示了长链推理下的性能悬崖，但其符号化逻辑对真实法律模糊性的覆盖度仍存疑。

】

---

【OPT-BENCH: Evaluating the Iterative Self-Optimization of LLM Agents in Large-Scale Search Spaces ｜大语言模型迭代自优化能力评估基准

研究机构：同济大学、复旦大学

作者：Xiaozhe Li、Jixuan Chen、Xinyu Fang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08904)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08904)

> 现有大语言模型（LLM）评估基准多聚焦于单次响应生成或任务完成率，忽视了模型在动态环境中利用反馈进行持续改进的“迭代自优化”能力。本文切入点在于构建一个区分连续参数优化与离散组合推理的评估框架，以探测模型内在的认知适应边界。通过引入感知-记忆-推理循环的代理框架，本文量化了模型将环境信号转化为解空间搜索策略的效率。该基准揭示了强模型在连续空间中的归纳优化优势与在离散空间中的结构修复瓶颈，但受限于样本规模与基线覆盖，其结论的普适性仍存疑。

】

---

【OptiVerse: A Comprehensive Benchmark towards Optimization Problem Solving ｜OptiVerse：面向多域优化求解的大语言模型基准与审计机制

作者：Xinyu Zhang、Boxuan Zhang、Yuchen Wan 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c13100191701)

> 大语言模型（LLM）在优化建模中面临的核心挑战并非代码语法错误，而是语义逻辑偏离题意导致的静默失败。现有基准多局限于数学规划与组合优化，无法全面评估模型在随机、动态及博弈等复杂领域的泛化能力，且缺乏对模型内部逻辑一致性的有效验证。本文构建了覆盖六大优化领域的OptiVerse基准，并提出双视角审计智能体（Dual-View Auditor Agent, DVA-Agent），通过盲审代码与需求交叉比对来检测并修复语义偏差。该工作揭示了当前LLM在Hard难度问题上的严重性能瓶颈，但其审计机制的有效性依赖于特定骨干模型，且未解决跨范式验证的理论完备性问题。

】

---

【Orthogonal Representation Editing: Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs ｜正交表示编辑：解耦批量知识编辑中的语义纠缠

研究机构：天津大学、中国科学院大学

作者：Wenhao Yu、Zhicong Lu、Bo Lv 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.22627)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.22627)

> 大语言模型（LLMs）参数静态化导致事实知识过时，全量重训练成本高昂且易引发灾难性遗忘，知识编辑（Knowledge Editing, KE）旨在以低成本局部更新特定事实。现有批量编辑方法在共享句法模板下性能退化，根源在于表示空间中通用语义结构的纠缠干扰。本文提出正交表示编辑（Orthogonal Representation Editing, ORE），通过构建通用语义子空间并对编辑向量施加正交约束，在表示空间解耦共享语义。ORE在跨语言批量编辑中显著优于基线，但其局部性指标仍低于参数编辑方法，且仅在7B-8B规模模型上验证，大规模模型下的几何约束有效性存疑。

】

---

【P2P: A Poison-to-Poison Remedy for Reliable Backdoor Defense in LLMs ｜以良性后门覆盖恶意后门：P2P 防御框架

研究机构：新加坡南洋理工大学、上海交通大学

作者：Shuai Zhao、Xinyi Wu、Shiqian Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04503)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04503)

> 微调阶段的数据投毒后门攻击使大语言模型在特定触发器下输出恶意内容，而现有防御方法往往局限于特定任务或攻击类型，缺乏跨场景泛化能力。P2P 算法通过向训练集注入带有安全标签的良性触发器，利用提示学习将模型输出空间重定向至安全标签，从而在无需知道恶意触发器具体形态的前提下抑制其激活。该方法在分类与生成任务上均实现了攻击成功率（Attack Success Rate, ASR）的显著降低，但其对生成任务输出多样性的潜在影响及良性触发器设计的依赖性仍存疑。

】

---

【PAPERMIND: Benchmarking Agentic Reasoning and Critique over Scientific Papers in Multimodal LLMs ｜科学文献智能体推理基准

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Yanjun Zhao、Tianxin Wei、Jiaru Zou 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3662611738a2)

> 现有科学文献理解基准将多模态感知、证据检索与批判性评估割裂为孤立任务，无法衡量模型在真实科研工作流中“决策-检索-批判”的集成推理能力。PAPERMIND 通过整合真实审稿数据与工具增强推理，构建了首个覆盖多域、多任务的智能体科学文献理解基准。该基准揭示了闭源模型在集成推理上的显著优势，但 F1 分数普遍偏低且依赖 LLM-as-a-Judge 评估，其生态效度与指标客观性仍存疑。

】

---

【PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers ｜PaperScope：面向大规模科学文档的多模态智能体深度研究基准

研究机构：中国人民大学

作者：Lei Xiong、Huaying Yuan、Zheng Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11307)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11307)

> 深度研究智能体在开放网络文本上的评估已相对成熟，但真实科研流程依赖本地存储的海量多模态文档（论文、报告），现有基准无法覆盖跨文档、跨模态的证据整合。本文通过知识图谱引导的随机游走采样构建大规模本地语料，并设计四类任务评估智能体在科学深度研究中的检索、推理与生成能力。实验显示，即便最先进的智能体在复杂多模态推理上仍表现不佳，揭示了当前系统在长上下文科学文档处理上的显著局限。

】

---

【ParaCook: On Time-Efficient Planning for Multi-Agent Systems ｜具身多智能体时间高效规划基准

研究机构：上海交通大学、美国加州大学默塞德分校

作者：Shiqi Zhang、Xinbei Ma、Yunqing Xu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11608)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11608)

> 长程具身任务中，任务完成不等于规划高效，现有基准仅评估正确性而忽略并行调度下的时间成本。ParaCook 通过简化烹饪场景的动作空间，将“最小化总完成时间”确立为核心指标，隔离了底层路径规划对高层调度能力的干扰。该基准揭示了当前大语言模型（LLM）在抽象调度推理上接近最优，但在具身执行映射上存在显著效率鸿沟。其价值在于填补了时间效率评估的空白，但缺乏符号验证机制使其在复杂逻辑约束下的鲁棒性存疑。

】

---

【Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL ｜平行监督微调（Parallel-SFT）：基于执行等价性的代码强化学习跨语言迁移

研究机构：美国麻省理工学院

作者：Zhaofeng Wu、Shiqi Wang、Boya Peng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e95b94477403)

> 导读 代码强化学习（RL）在源编程语言上获得的策略增益，往往无法零样本迁移至目标语言，甚至导致性能退化。现有方法依赖自然语言中天然存在的平行文本对齐表示空间，但代码语料缺乏此类信号，导致模型陷入语法中心而非功能中心的表示陷阱。本文提出 Parallel-SFT，通过合成跨语言功能等价程序构建平行语料，在监督微调阶段对齐表示空间，从而提升后续 RL 阶段的跨语言迁移能力。该方法在 Llama-3.1-8B 上验证了有效性，但其对大规模模型及非执行等价语义迁移的适用性尚存疑。

】

---

【Parametric Knowledge is Not All You Need: Toward Honest Large Language Models via Retrieval of Pretraining Data ｜基于预训练数据检索的诚实性增强

研究机构：新加坡国立大学

作者：Christopher Adrian Kusuma、Muhammad Reza Qorib、Hwee Tou Ng

论文原文见 [arXiv](https://arxiv.org/abs/2601.21218)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0045f261b9d1)

> 大语言模型（LLM）在缺乏知识时往往生成幻觉而非承认无知，现有诚实性评估方法因无法确定模型真实知识边界而失效。本文利用Pythia模型公开的预训练数据，通过检索验证问题是否可答，构建了首个基于真实知识边界的诚实性基准TIP-TRIVIAQA。方法RETAIN通过检索预训练文档辅助回答，在提升诚实性的同时改善了答案准确性。该工作将诚实性评估从黑盒行为观察转向白盒知识验证，但受限于仅适用于预训练数据完全公开的模型，其结论能否推广至闭源模型尚存疑。

】

---

【Pardon? Evaluating Conversational Repair in Large Audio-Language Models ｜可评估性感知与对话修复评估

作者：Shuanghong Huang、Jinlei Xu、Youchao Zhou 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10cbb66276bd)

> 大型音频语言模型（Large Audio-Language Model, LALM）在语音问答中常因输入语义缺失而幻觉作答，现有评估仅测准确率或声学鲁棒性，隐含“输入始终可答”的假设。本文提出可评估性感知（Evaluability Awareness）概念，通过语义-声学掩码协议构造配对的可答/不可答输入，并定义非补偿性指标 EAR 分数，联合评估任务能力与修复行为。实验揭示主流 LALM 在不可答场景下系统性失效，EAR 分数显著低于其准确率，但掩码比例极小（2.5-6.7%）是否代表真实信息丢失程度存疑。

】

---

【Pattern Enhanced Multi-Turn Jailbreaking: Exploiting Structural Vulnerabilities in Large Language Models ｜模式增强多轮越狱攻击

研究机构：日本东京科学大学、日本理化学研究所

作者：Ragib Amin Nihal、Rui Wen、Kazuhiro Nakadai 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08859)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08859)

> 多轮越狱攻击旨在利用对话上下文累积效应突破大语言模型的安全对齐，但现有方法多依赖启发式随机探索，缺乏对模型结构性弱点的系统性揭示。本文切入点在于将语言学对话模式引入攻击框架，通过预定义的五种模式约束搜索空间，实现从“盲目试探”到“结构化探测”的转变。其核心做法是构建模式管理器监控阶段进展与语义依从度，在十二个模型上验证了模式-危害类别的交互脆弱性。该框架揭示了单一防御无法泛化至所有对话模式的局限，但其攻击效率受限于单次尝试预算，且未与最新强化学习基线进行同协议对比，SOTA地位存疑。

】

---

【PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics ｜基于历史语言学的多步程序示例推理基准

作者：Atharva Naik、Darsh Agrawal、Prakam 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_366acb5deb19)

> 多步归纳推理评估长期受困于领域知识混杂与数据污染，导致模型性能无法真实反映其顺序逻辑整合能力。现有基准如 HotpotQA 依赖静态文本，难以隔离纯粹的推理机制，且易被预训练数据覆盖。本文切入点在于利用历史语言学中的音变顺序约束，构建一个无领域知识、可自动生成的字符串重写任务。通过符号系统生成受控难度的程序级联，量化模型在顺序依赖推理上的瓶颈。该基准揭示了当前前沿模型在长级联任务上的严重失效，但其在真实语言歧义处理上的泛化能力仍存疑。

】

---

【PeerCheck: Enhancing LLM-Generated Academic Reviews Towards Human-Level Quality ｜PeerCheck：基于差异分析与提示优化的LLM学术评审增强框架

作者：Zeyuan Chen、Ziqing Yang、Yihan Ma 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.20897)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.20897)

> 导读

】

---

【PerDucer: Keyphrase-Driven Personalization Inducer for Summarization from User Histories ｜基于关键短语诱导的冻结模型个性化摘要

作者：Parthiv Chatterjee、Asish Joel Batha、Sourish Dasgupta 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e20fcf3d4091)

> 个性化摘要旨在使生成内容同时满足文档重要性与用户动态兴趣，但直接将长交互历史注入大语言模型（LLM）提示词会导致性能不稳定甚至下降。现有方法多依赖静态画像或粗粒度主题，无法捕捉细粒度的时序偏好演化。PerDucer 将历史注入重构为关键短语引导，通过编码器预测潜在偏好信号并解码为紧凑的关键短语集，作为控制线索引导冻结的摘要模型。该方法在保持模型参数不变的前提下实现了显著的个性化增益，但其对稀疏历史信号的鲁棒性边界及跨域迁移的泛化能力仍需进一步审视。

】

---

【Personalized Benchmarking: Evaluating LLMs by Individual Preferences ｜个性化基准测试：基于个体偏好的大语言模型评估

研究机构：美国芝加哥大学

作者：Cristina Garbacea、Heran Wang、Chenhao Tan

论文原文见 [arXiv](https://arxiv.org/abs/2604.18943)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18943)

> 大语言模型（LLM）评估长期依赖聚合指标，掩盖了用户偏好的个体异质性。现有基准如 Chatbot Arena 通过平均所有用户投票计算全局排名，导致多数用户的实际偏好与推荐结果严重偏离。本文切入点在于量化这种偏离，并探索预测个体排名的特征空间。通过计算 115 名活跃用户的 ELO 与 Bradley-Terry (BT) 个体排名，结合主题与风格分析，证明了聚合排名的失效。其价值在于提供了个性化评估的量化证据，但样本量有限且未涉及动态偏好演化，结论的普适性存疑。

】

---

【PhaseMI: A Motivational Interviewing Dataset for Enhancing Phase Progression in LLM-based Counseling ｜阶段结构化动机访谈数据集

研究机构：韩国科学技术院、韩国高丽大学

作者：Jina Kim、Myeongho Jeon、Soohyun Cho 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a25eab4e18f1)

> 现有动机访谈（Motivational Interviewing, MI）数据集缺乏对咨询阶段结构的显式建模，导致模型在长对话中易发生治疗漂移，无法有效引导客户从探索走向行动规划。本文通过引入监督者大语言模型（Supervisor LLM）显式控制阶段转换，构建了包含13,897条对话的PHASEMI数据集。该方法在指导（Guiding）和选择（Choosing）阶段的覆盖率上显著优于基线，验证了结构化生成对提升临床逻辑一致性的作用，但其依赖合成数据且未评估真实临床场景下的泛化能力。

】

---

【PII-VisBench: Evaluating Personally Identifiable Information Safety in Vision Language Models Along a Continuum of Visibility ｜视觉语言模型隐私评估：基于主体可见性连续体的 PII-VisBench

研究机构：美国加州大学河滨分校

作者：G M Shahariar、Zabir Al Nazi、Md Olid Hasan Bhuiyan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05739)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05739)

> 视觉语言模型（VLM）在医疗与文档处理等隐私敏感场景中，常因预训练记忆而泄露个人身份信息（PII），但现有评估多将其视为静态提取问题，忽略了主体在线足迹对模型行为的决定性影响。本文提出 PII-VisBench，通过构建“可见性连续体”将 200 个主体分层为高、中、低、零四级，并设计 4000 个探针，系统量化了 18 个开源 VLM 的拒绝率（RR）与条件 PII 披露率（cPDR）。该基准揭示了“高可见性隐私缺口”，即模型对公众人物的 PII 泄露风险显著高于普通个体，表明安全对齐未能有效抑制记忆型泄露。这一发现挑战了“模型规模越大越安全”的隐含假设，但基于网络搜索结果的可见性代理指标是否完全代表训练数据分布，仍存疑。

】

---

【PlanE: Meta Planning of Data, Tuning, and Inference for Extractive-based LLMs ｜面向信息抽取的LLM构建元规划框架

作者：Jiacheng Wang、Weiyan Zhang、Guangya Yu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a180f129a762)

> 信息抽取（IE）任务中，大语言模型（LLM）的指令微调面临数据标注成本高且缺乏针对特定任务的最优配置策略的困境。现有方法多聚焦于单一环节优化，如数据筛选或强化学习，却忽略了数据、训练与推理三者的联合配置对最终性能的非线性影响。本文提出PlanE框架，通过元学习自动选择最优的“数据-训练-推理”（DTI）组合，以平衡构建效率与模型性能。该框架在特定IE任务上实现了与网格搜索持平的性能，但显著降低了搜索成本，其通用性仍存疑。

】

---

【PlanRAG-Audio: Planning and Retrieval Augmented Generation for Long-form Audio Understanding ｜规划式检索增强生成用于长音频理解

研究机构：美国卡内基梅隆大学

作者：Masao Someki、Chien-yu Huang、Siddhant Arora 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.20414)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20414)

> 长音频理解面临的核心矛盾是输入序列长度与模型上下文窗口的指数级冲突，导致现有大型音频语言模型在处理小时级录音时性能急剧衰减。传统端到端生成范式无法在有限算力下保留跨模态的时序依赖，而纯文本转录又丢失了副语言信息。本文提出 PlanRAG-Audio，通过“规划-检索-生成”三阶段框架，将长音频理解转化为结构化数据库查询问题，从而解耦推理成本与音频时长。该方法在零样本条件下实现了跨模态组合推理，但在语义泛化能力与标准短音频基准上的表现尚未验证。

】

---

【PO-KGQA: Preference Optimization for Low-Resource Complex Knowledge Graph Question Answering ｜低资源复杂知识图谱问答的偏好优化

作者：Prerna Agarwal、Ayushman Kumar Singh、Srikanta Bedathur

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70a181cc5ecb)

> 复杂知识图谱问答（KGQA）要求模型将自然语言问题转化为可执行的逻辑形式，但现有方法依赖大语言模型（LLM）的高昂算力或大量标注数据，导致小语言模型（SLM）在低资源场景下难以兼顾推理准确性与部署成本。本文切入点在于利用自反馈机制动态生成偏好数据，并修改迭代推理偏好优化（RPO）损失以聚焦中间推理步骤的正确性，从而摆脱对教师模型和最终答案的依赖。通过LoRA适配器微调7B级代码模型，PO-KGQA在KQA Pro基准上实现了超越主流对齐技术的性能。其价值在于证明了SLM在符号推理任务上的潜力，但自反馈循环的收敛稳定性与验证器错误累积效应仍存疑。

】

---

【Polaris: A Gödel Agent Framework for Small Language Models through Experience-Abstracted Policy Repair ｜POLARIS：基于经验抽象的小语言模型递归策略修复

作者：Aditya Kakade、Vivek Srivastava、Shirish Karande

论文原文见 [arXiv](https://arxiv.org/abs/2603.23129)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23129)

> 递归自我改进旨在让智能体通过检查自身策略与执行轨迹来持续优化能力，但现有框架如 Gödel Agent 依赖大模型容量，在 7B 参数的小语言模型（SLM）上因上下文膨胀导致内存溢出（OOM）而失效。POLARIS 通过“经验抽象”机制，将失败案例压缩为最小代码补丁，在资源受限条件下实现可追溯的策略持久化更新。该方法证明了 SLM 具备递归改进的可行性，但其性能增益依赖于特定骨干模型的元推理能力，且缺乏对补丁泛化性的量化评估。

】

---

【Policy-Guided Stepwise Action Planning for Controllable LLM Reasoning ｜策略引导的高层动作规划

研究机构：中山大学、新加坡南洋理工大学

作者：Jianpeng Zhou、Qisheng Hu、Jiahai Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7d8080eed5c)

> 现有基于高层动作的LLM推理方法常陷入结构冗余或动作序列坍缩，导致性能不及简单思维链。PG-HAP通过解耦轻量级规划器与冻结执行器，利用强化学习动态选择推理动作，解决了静态模板无法适应复杂推理路径的问题。该方法在数学与常识推理基准上实现了超越基线的准确率，并提供了可解释的推理轨迹。尽管在连续推导任务上略逊于思维链，但其可控性与效率优势为LLM推理提供了新的工程范式，其在更复杂多步逻辑任务中的泛化边界仍需进一步验证。

】

---

【PolicyLLM: Towards Excellent Comprehension of Public Policy for Large Language Models ｜政策理解基准与专家路由模型

研究机构：美国圣母大学

作者：Han Bao、Penghao Zhang、Yue Huang 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c50d34b8dd3)

> 大语言模型（LLMs）在公共政策决策辅助中面临认知能力评估缺失的困境，现有通用基准无法区分事实回忆、概念理解与情境应用等分层能力。本文切入点在于构建首个中美跨系统政策理解基准 PolicyBench，并基于 Bloom 分类法设计三级认知任务，同时提出 PolicyMoE 通过低秩适配（LoRA）专家模块解耦不同认知层级。该方法通过路由机制动态分配任务至特定专家，旨在提升模型在复杂政策情境下的推理可靠性。其价值在于建立了政策领域的细粒度诊断框架，但应用层的高准确率是否源于对表面逻辑的拟合而非深层政策理解，仍存疑。

】

---

【PolyAudio: Advancing Multi-Audio Reasoning in Large Audio Language Models with Interleaved Multi-Audio Contexts ｜多音频交错推理

研究机构：美国马里兰大学帕克分校、美国杜克大学

作者：Sonal Kumar、Sreyan Ghosh、Yueqian Lin 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e7f378a730c0)

> 大型音频语言模型（LALM）在处理单片段音频时表现优异，但面对需要跨多个离散音频片段整合证据、解决指代冲突的复杂场景时，现有模型往往因缺乏原生多片段输入支持而失效。本文切入点在于证明无需大规模多音频预训练，仅通过显式交错格式与高质量指令微调即可解锁多音频组合式推理能力。具体做法是基于 Audio Flamingo 3 构建 PolyAudio，利用 1.3M 多音频指令数据训练模型识别片段边界与跨片段逻辑。该工作验证了后训练在多模态扩展中的高效性，但其依赖合成数据且仅支持至多 5 个片段，真实场景泛化能力存疑。

】

---

【POP: Prefill-Only Pruning for Efficient Large Model Inference ｜阶段感知剪枝：解耦预填充与解码的冗余性

研究机构：武汉大学

作者：Junhui He、Zhihui Fu、Jun Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03295)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03295)

> 大语言模型推理加速面临结构化剪枝精度崩溃与非结构化剪枝硬件低效的双重困境。现有方法将预填充（Prefill）与解码（Decode）视为同质过程，忽略了二者在功能上的根本不对称：预填充仅需编码上下文，而解码需同时编码并预测下一词。本文提出 Prefill-Only Pruning (POP)，通过虚拟门机制识别深层在预填充阶段的冗余性，仅在该阶段移除深层，保留全模型用于解码，辅以独立 KV 投影与边界处理。该方法在 Llama-3.1 等模型上实现了 1.37 倍预填充加速且精度损失极小，但其加速收益高度依赖输入长度，短序列场景下优势微弱。

】

---

【pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training ｜pQuant：解耦线性量化感知训练

研究机构：北京大学、复旦大学

作者：Wenzheng Zhang、Bingzheng Liu、Yang Hu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22592)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22592)

> 极低位大语言模型（LLM）在从随机初始化进行量化感知训练（QAT-Scratch）时，面临精度停滞与扩展性失效的双重瓶颈。现有1-bit模型因权重敏感度均匀化导致表达力受限，无法有效区分关键参数。本文提出pQuant，通过解耦线性层将敏感权重隔离至高精度分支，并利用特征缩放引导模型动态分配重要性。该方法在1.3B规模下以1.35-bit精度逼近2-bit模型性能，但仅验证至2.6B规模，其在大模型上的泛化能力存疑。

】

---

【Preference Estimation via Opponent Modeling in Multi-Agent Negotiation ｜融合语言信号的贝叶斯对手建模

研究机构：日本京都大学

作者：Yuta Konishi、Kento Yamamoto、Eisuke Sonomoto 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15687)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6b2ed3fc887a)

> 导读 多智能体谈判中，私有偏好隐藏在自然语言与数值报价的混合流中，传统仅依赖数值历史的贝叶斯方法无法捕捉话语中的定性线索，导致高不确定性下偏好估计失稳。本文切入点在于将大语言模型（LLM）提取的语言信号转化为概率格式，与数值似然进行贝叶斯融合，实现动态信念跟踪。该方法在稀疏共识空间中提升了全协议率与估计精度，但其对“真诚对话”的强假设限制了在策略性欺骗场景下的适用性。

】

---

【Preference Learning Unlocks LLMs’ Psycho-Counseling Skills ｜基于专业原则的心理咨询偏好对齐

研究机构：美国匹兹堡大学

作者：Mian Zhang、Shaun M. Eack、Zhiyu Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc440e110757)

> 该方向旨在解决大语言模型在心理咨询场景中因缺乏真实临床数据监督而导致的响应质量不稳定问题。现有方法多依赖通用对话数据或单一维度的情感评估，无法捕捉循证心理治疗中关于自主性、阶段敏感性等深层专业逻辑，导致模型响应虽流畅但缺乏临床有效性。本文切入点在于构建一套由社会工作与精神病学专家定义的七维专业评估原则，并以此生成大规模偏好数据集 PsyCoPref，通过迭代式直接偏好优化（Iterative DPO）训练模型。其价值在于证明了领域特定偏好数据能显著提升小参数模型对 GPT-4o 的胜率，但存疑点在于该评估体系是否过度依赖 GPT-4o 作为裁判的隐性偏差。

】

---

【Preference-Aware Memory Update for Long-Term LLM Agents ｜偏好感知记忆更新机制

作者：Haoran Sun、Zekun Zhang、Shaoning Zeng

论文原文见 [arXiv](https://arxiv.org/abs/2510.09720)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09720)

> 长期对话智能体面临用户偏好随时间漂移导致的响应失配问题，现有记忆系统多聚焦于静态存储与检索，缺乏对动态偏好演化的实时追踪能力。PAMU通过滑动窗口与指数移动平均融合构建双视角偏好向量，以统计信号触发记忆更新，实现无微调的模块化适配。该方法在LoCoMo基准上提升了生成质量，但仅验证了风格一致性，未触及多跳推理或事实准确性SOTA，其统计建模对语义细粒度的捕捉能力存疑。

】

---

【PrefRAG: Correcting Semantic Errors in Auto-Formalization for Logical Reasoning with Program Preference RAG ｜程序偏好检索增强生成

研究机构：中山大学

作者：Yuyin Zhou、Yongmei Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a22e11893b78)

> 神经符号逻辑推理的核心瓶颈在于自动形式化阶段的语义错误，现有方法仅能处理语法报错或约束级验证，缺乏程序级语义错误的系统性修正机制。本文通过构建语义错误分类法与偏好数据集，将检索增强生成（RAG）引入自精炼模块，使大语言模型（LLM）能自主识别并修复深层语义缺陷。该方法在分布内（ID）与分布外（OOD）基准上均超越基线，证明了语义偏好检索对推理鲁棒性的提升作用，但其性能增益在复杂数据集上趋于平缓，且依赖特定领域的错误模式覆盖度。

】

---

【Preserving Fairness and Safety in Quantized LLMs Through Critical Weight Protection ｜关键权重保护下的量化公平与安全保持

作者：Muhammad Alif Al Hakim、Alfan Farizki Wicaksono、Fajri Koto

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0b0cb9edea0)

> 大语言模型在部署时普遍采用量化压缩以降低显存占用，但精度截断会扰动参数分布，进而破坏模型在公平性与安全性上的对齐表现。现有研究多聚焦于静态量化下的英文场景，对动态量化及多语言环境中的对齐退化缺乏系统评估，且缺乏在量化阶段直接保护对齐敏感参数的机制。本文提出关键权重保护策略，通过敏感度评分识别对公平与安全贡献最大的参数，将其保留在FP16精度，其余参数量化至INT4。该方法在无需重训练的前提下缓解了量化导致的对齐退化，但其保护粒度为权重级别，未触及激活空间或特征子空间，能否应对更深层的对齐结构漂移仍存疑。

】

---

【Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints ｜耦合权重与激活约束防止大语言模型安全漂移

研究机构：中国科学院、国防科技大学

作者：Songping Peng、Zhiheng Zhang、Daojian Zeng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12384)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12384)

> 微调过程常因少量良性数据导致模型拒绝有害请求的能力崩塌，现有防御方案多局限于权重或激活单级干预，无法阻断二者耦合产生的绕过路径。本文提出CWAC，通过同时施加权重子空间投影与稀疏自编码器特征正则化，在训练阶段闭合安全漂移通道。该方法在四个主流开源模型上显著降低了有害分数，但其依赖白盒访问且未验证对黑盒API模型的适用性。

】

---

【Privacy Risks of Intermediate Representations: Attribute Inference in Distributed LLM Inference ｜分布式推理中间表示的属性推断攻击

作者：Yang Lyu、Jin Cao、Yang Xiao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9211fc754cf2)

> 分布式大语言模型推理通过传输中间隐藏状态而非原始输入来降低计算成本，但这一架构被普遍假设能保护用户隐私。现有属性推断攻击依赖完整模型访问或辅助数据对，无法在仅持有部分层权重的受限场景下运行。本文提出IR-AIA，一种纯基于中间表示的零样本属性推断攻击，通过几何去偏与滑动窗口匹配解决各向异性与子词碎片化问题。该工作揭示了中间层共享的隐私漏洞，但其高准确率是否受限于候选集规模与特定层选择，仍需更广泛的基准验证。

】

---

【Private Seeds, Public LLMs: Realistic and Privacy-Preserving Synthetic Data Generation ｜真实感与隐私保护的合成数据生成

作者：Qian Ma、Sarah Rajtmajer

论文原文见 [arXiv](https://arxiv.org/abs/2604.07486)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07486)

> 隐私合成数据生成旨在替代无法共享的敏感文本，但现有梯度微调法受限于API访问与高计算成本，纯提示法则难以保留原始数据的分布特征。本文提出RPSG，通过“抽象-选择-生成-精炼”四阶段流水线，将私有数据作为种子引导大语言模型生成高保真合成文本。该方法在候选选择阶段引入形式化差分隐私机制，在保持语义连贯性的同时显著降低成员推断攻击风险。尽管其在效用与隐私权衡上优于基线，但缺乏与最新分布保真度SOTA的直接数值对比，且NLL过滤机制对骨干模型分布特性的依赖尚不明确。

】

---

【Probing the Plasticity and Correlation of LLM Value Systems: LLM Value Rankings are Not Stable ｜大语言模型价值系统可塑性与相关性拓扑

研究机构：香港科技大学、南京大学

作者：Zhenheng Tang、Qihua Pan、Jingya Shen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a10d873812d5)

> 大语言模型（LLM）在决策中依赖内部价值排序，但现有对齐研究多假设该排序是静态且鲁棒的，忽略了外部提示对价值优先级的系统性扰动。本文切入点在于量化这种“价值可塑性”，并揭示不同价值间存在内在的联动结构。通过设计六种提示策略对八款模型进行压力测试，发现场景化叙事能最有效地颠覆默认价值排序，且大模型比小模型更易受此影响。该工作揭示了基于提示的价值操纵风险，但缺乏对权重层面干预的对比，其防御性结论在动态对抗场景下的有效性存疑。

】

---

【ProCeedRL: Process Critic with Explorative Demonstration Reinforcement Learning for LLM Agentic Reasoning ｜过程级批评与探索性演示强化学习

研究机构：清华大学

作者：Jingyue Gao、Yanjiang Guo、Chen Xiaoshuai 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_655b3177927a)

> 多轮智能体任务中，次优动作引发的噪声反馈会累积并破坏后续推理，导致标准强化学习（RL）探索效率低下且受限于基座模型能力。现有方法依赖独立重复采样或事后惩罚，无法在错误扩散前进行干预。本文提出 ProCeedRL，通过实时过程级批评者（Critic）检测并回溯修正低质量步骤，将探索从被动选择转为主动干预。该方法在深度搜索与具身任务上突破了标准 RL 的性能上限，但其效果高度依赖 Critic 的准确性，且缺乏理论保证。

】

---

【ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection ｜概率引导的Token掩码微调

研究机构：清华大学

作者：Tao Liu、Taiqiang Wu、Runming Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09195)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09195)

> 监督微调（SFT）在将大语言模型（LLM）对齐至人类意图时，常因强制拟合单一参考答案而陷入表面形式过拟合，导致模型记忆特定样本而非掌握核心逻辑。现有方案要么依赖高成本的多参考数据构建，要么采用软加权策略但无法彻底隔离噪声梯度。ProFit 通过识别高预测概率Token承载核心语义的特性，提出硬掩码机制屏蔽低概率Token，以单参考数据实现优于全量SFT的泛化性能。该方法在Qwen3系列模型上平均准确率提升3.0%至10.9%，但其效果是否源于骨干模型优势而非算法本身，仍缺乏跨架构的严格归因验证。

】

---

【Progra: Progress-Aware Reinforcement Learning for Multi-Turn Function Calling ｜进度感知强化学习

研究机构：上海交通大学

作者：Huacan Chai、Zijie Cao、Maolin Ran 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_23175b7799fb)

> 多轮函数调用面临的核心困境是模型无法维持对任务全局状态的连贯表征，导致局部动作与全局目标脱节。现有方法要么将多轮轨迹拆解为独立单轮样本训练，要么依赖端到端强化学习却缺乏显式的进度建模，两者均无法解决长程依赖中的状态追踪失效。本文提出PROGRA框架，通过合成包含历史摘要与未来规划的“进度感知”数据，并将其作为条件变量注入基于GRPO的强化学习训练中。该框架在τ-bench和BFCL-V3上显著优于基线，但其性能增益是否完全源于进度感知机制本身，还是受限于特定骨干模型的预训练质量，仍需更严格的控制实验来验证。

】

---

【Program Structure-aware Language Models: Targeted Software Testing beyond Textual Semantics ｜图增强语言建模框架：分支定向测试生成

作者：Khang Tran、Khoa Nguyen、Cristian Borcea 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17715)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17715)

> 软件测试的核心痛点在于如何精准覆盖高风险执行路径，而非仅追求代码行数覆盖。现有基于大语言模型（LLM）的测试生成方法依赖提示工程启发式，受限于模型随机性，难以稳定命中特定分支。GLMTest 提出将代码属性图（CPG）结构嵌入与 LLM 文本语义在共享空间联合训练，实现分支定向生成。该方法在 TestGenEval 上将分支准确率从 27.4% 提升至 50.2%，但仅验证了 Python 单语言场景，且未对比专用测试生成 SOTA，其泛化边界尚存疑。

】

---

【Progressive Planning and Reinforced Reasoning: Large Language Model-Guided Multi-hop Question Answering over Knowledge Graph ｜渐进式规划与强化推理：知识图谱多跳问答的LLM引导框架

研究机构：北京邮电大学

作者：Xiang Li、Runhai Jiao、Ruifan Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4371fb70e97)

> 多跳问答要求模型在结构化知识中跨越多个实体链接推导答案，传统强化学习（RL）方法因缺乏中间步骤监督而陷入盲目探索，且策略网络仅关注局部邻域，无法预判决策的长期后果。本文切入点在于将大语言模型（LLM）从间接信号提供者升级为显式规划器，通过子问题分解引导逐步决策，并引入结构感知前瞻网络评估动作长期价值。具体做法是结合LLM宏观规划与RL微观推理，构建渐进式规划与强化推理（Progressive Planning and Reinforced Reasoning, PPRR）框架。该框架在四个公开基准上超越现有方法，但其依赖静态知识图谱且LLM规划仅用于训练，推理时的泛化能力与规划错误率仍是存疑点。

】

---

【ProMediate: A Simulation Testbed for Evaluating Proactive Mediation in Multi-Party Negotiation ｜ProMediate：多方主动调解的社会认知评估测试床

研究机构：美国南加州大学

作者：Ziyi Liu、Bahareh Sarrafzadeh、Pei Zhou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0536f8e06d5d)

> 多方谈判中的共识构建长期缺乏系统化的量化评估手段，现有基准多聚焦双边经济效率或被动响应式辅助，无法捕捉调解者主动介入时机与策略对社会动态的影响。ProMediate 通过构建基于冲突理论的多方模拟环境，将“何时介入”与“如何介入”解耦，并引入共识追踪与社会认知智能双维度指标，填补了主动调解能力评估的空白。其价值在于提供了可复现的主动代理压力测试框架，但实验仅覆盖单一骨干模型与有限场景，缺乏与强化学习路线的横向对比，其结论的泛化性存疑。

】

---

【Prompt Injection in Automated Résumé Screening with Large Language Models: Single and Multi-Injection Settings ｜提示注入下的LLM简历筛选鲁棒性

研究机构：美国密歇根大学、美国俄亥俄州立大学

作者：Preet Baxi、Jiannan Xu、Jane Yi Jiang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01fe064ff16b)

> 现有LLM招聘系统面临候选人策略性操纵的风险，但既往研究多孤立评估单次攻击，忽略了多候选人同时注入时的竞争动态。本文通过控制实验量化了注入强度与候选人质量分布对排名扭曲的影响，揭示了“饱和效应”机制。实验表明，在同质质量池且注入率低时，系统最脆弱；随着注入者增多，攻击收益迅速归零。该研究填补了多攻击者博弈评估的空白，但其合成数据设定限制了向真实复杂招聘场景的泛化能力。

】

---

【Prompt Optimization for Relation Extraction using Reinforcement Learning ｜基于深度强化学习的领域关系抽取提示优化

研究机构：美国东北大学

作者：Ying Liu、Dong Shuai、Cui Zibo 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f29d6466a30b)

> 导读 关系抽取（Relation Extraction, RE）在低资源领域场景中面临标注数据稀缺与提示工程依赖人工的双重瓶颈。现有自动提示优化方法多采用无结构搜索或启发式重写，难以高效探索组合式的提示空间且易产生语义漂移。本文提出REPO框架，将提示优化建模为马尔可夫决策过程，利用深度强化学习在受限动作空间内迭代精炼提示。该框架在医疗、金融等四个领域数据集上验证了跨域泛化能力，但其动作空间的离散性是否限制了提示结构的创造性探索，仍存疑。

】

---

【Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation ｜提示测试时扩展

作者：Sondos Mahmoud Bsharat、Zhiqiang Shen

论文原文见 [arXiv](https://arxiv.org/abs/2510.09599)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09599)

> 大语言模型推理能力的提升长期依赖大规模思维链语料的标注与收集，但静态提示易导致模型过拟合特定解题模板，且在领域偏移下泛化能力受限。现有推理时扩展方法多聚焦于解码参数调整或答案聚合，忽视了提示空间本身的组合潜力。本文提出 P-TTS，通过原则性指令包装对少量种子问题进行系统性提示变异，将测试时提示转化为数据增强手段。该方法以 90 个种子样本实现了超越 1K 静态提示的效果，但其本质是低资源监督微调策略，而非直接的推理时算力扩展，其理论边界与 RL 训练的对比优势尚存疑。

】

---

【Prompting the Unknown: Understanding Response Uncertainty in Large Language Models ｜提示响应概念模型（PRC）：从信息量到不确定性的因果解耦

作者：Ze Yu Zhang、Arun Verma、Finale Doshi-Velez 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3b894846b09a)

> 大语言模型（LLM）在高风险决策场景中常因提示中任务相关信息不足而产生高方差响应，现有不确定性量化（UQ）方法多聚焦于输出端的熵计算或校准，却忽视了输入端信息量对响应不确定性的根本性影响。本文切入点在于将“提示信息化程度”形式化为控制不确定性的自变量，而非仅将其视为背景条件。通过构建提示-响应概念（Prompt-Response Concept, PRC）模型，论文将响应不确定性分解为提示欠规范、模型质量、任务变异性与语义冗余四个独立来源，并证明前两者随信息量增加而严格递减。该工作为提示工程提供了信息论层面的理论支撑，但其理想化假设限制了在真实黑盒模型中的直接应用边界。

】

---

【Propaganda Signals in LLMs: Perspectival Divergence and Narrative Framing in the Russia-Ukraine War ｜冲突叙事中的视角偏离与宣传机制分析

研究机构：以色列理工学院、以色列内盖夫本-古里安大学

作者：Ofir Shabat、Ido Guy、Kira Radinsky

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_50439ccfdad9)

> 大语言模型在翻译或总结地缘政治冲突时，往往隐含地复现特定信息生态系统的叙事框架，而现有偏见评估多聚焦于宏观左右翼倾向，难以捕捉这种微观的、冲突特定的修辞对齐。本文通过构建俄罗斯-乌克兰冲突的配对参考数据集，提出了一种基于语义距离的视角偏离度量协议，并结合五类宣传手法分类法，量化了模型输出与不同阵营叙事的接近程度及其实现机制。该方法揭示了模型间存在稳定的、特异性的叙事“签名”，表明标准事实性评估无法完全识别这些隐性偏见。这一工作为冲突感知的模型审计提供了新维度，但其结论局限于单一冲突与翻译任务，跨语境泛化性尚待验证。

】

---

【ProRank: Prompt Warmup via Reinforcement Learning for Small Language Models Reranking ｜小语言模型文档重排中的提示预热与细粒度评分

研究机构：香港理工大学

作者：Xianming LI、Aamir Shakir、Rui Huang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_206d3e9d9499)

> 文档重排旨在优化检索结果顺序以提升下游生成质量，但主流大语言模型（LLM）方案因参数量大导致推理延迟高，难以满足实时性要求。现有小语言模型（SLM）方案虽具备效率优势，却受限于表征空间狭窄及零样本提示理解能力弱，导致排序精度不足。本文提出 ProRank，通过强化学习提示预热与基于 Logit 差值的细粒度评分两阶段训练，解决 SLM 的上述瓶颈。该方法在 BEIR 基准上以 0.5B 参数超越了 32B 规模的微调 LLM，验证了小型化重排器的潜力，但其对 Listwise 全局依赖建模的缺失及特定基准上的表现波动仍存疑。

】

---

【Pru-CoT: Towards Efficient Reasoning Distillation via Pruning Chain-of-Thought ｜剪枝思维链以优化推理蒸馏

研究机构：大连理工大学

作者：Han Liu、Shuotian Ma、Hui Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e90fdf0261e7)

> 推理知识蒸馏面临的核心困境是教师模型生成的冗长思维链（Chain-of-Thought, CoT）中充斥冗余步骤，导致学生模型过拟合表面语法而非内化核心因果逻辑。现有剪枝方法要么受限于局部启发式规则无法捕捉全局依赖，要么因全局搜索带来不可接受的计算开销。Pru-CoT 通过冻结模型上的可学习权重量化步骤级因果贡献，结合大语言模型（Large Language Model, LLM）引导的保真剪枝，在保留逻辑完整性的同时压缩轨迹。该方法在 DeepSeek-R1-Distill-Qwen-7B 上实现了平均准确率 2.4% 的提升，但其对剪枝代理规模匹配的依赖及未探索的超参数空间限制了其通用性验证。

】

---

【PsyChain: A Collaborative Chain-of-Agents Framework for Generating Personalized and Professional Counseling Dialogues ｜基于人格原型的链式智能体心理咨询对话生成框架

研究机构：北京交通大学

作者：Yi Feng、Zijie Yang、Chen Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d693979079cb)

> 现有心理咨询数据集普遍存在客户画像同质化、治疗深度不足及过程不可控的缺陷，导致模型生成的响应缺乏临床针对性。PsyChain 通过引入 DSM-5 人格原型与多智能体协作机制，将静态语料转化为高保真对话。该框架利用六个专职智能体模拟完整的咨询流程，在自建数据集上验证了其在认知重构与策略专业性上的优势，但其合成数据能否替代真实临床数据的等效性仍存疑。

】

---

【PsychePass: Calibrating LLM Therapeutic Competence via Trajectory-Anchored Tournaments ｜轨迹锚定锦标赛校准大模型治疗能力

研究机构：中南大学、清华大学

作者：Zhuang Chen、Dazhen Wan、Zhangkai Zheng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20330)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20330)

> 大语言模型在心理咨询中的评估长期受困于“无锚定缺陷”：模拟对话缺乏临床方向导致过程漂移，静态评分缺乏参照导致标准漂移，使得现有基准无法区分模型的真实治疗能力。PSYCHEPASS 通过基于单会话疗法理论的脚本化探针锚定交互轨迹，并利用瑞士制锦标赛与 Bradley-Terry 模型锚定判断轨迹，将评估转化为可优化的奖励信号。该框架实现了从评估到强化学习优化的闭环，但其在危机干预维度上的性能回退提示了疗效与安全性的潜在冲突。

】

---

【PsychEthicsBench: Evaluating Large Language Models Against Australian Mental Health Ethics ｜心理健康大语言模型伦理评估基准

作者：Yaling Shen、Stephanie Fong、Yiwen Jiang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e7a927a55924)

> 现有安全对齐研究将“拒绝有害请求”视为安全性的核心指标，但这一范式在心理健康场景中失效，因为缺乏共情的拒绝本身即构成伦理违规。本文指出，通用基准无法捕捉司法辖区特异性与伦理行为的多维性，因此构建了首个基于澳大利亚心理健康伦理原则的评估基准。通过引入质量门控与规则违反分类，该基准将评估重心从“是否拒绝”转移至“是否合乎伦理”。其价值在于揭示了领域微调导致的伦理退化现象，但受限于单一司法辖区与LLM评判机制，其结论的普适性仍需跨域验证。

】

---

【PsychEval: A Multi-Session and Multi-Therapy Benchmark for High-Realism AI Psychological Counselor ｜多会话多疗法心理咨询基准

研究机构：华东师范大学

作者：Qianjun Pan、Junyi Wang、Jie Zhou 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.01802)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.01802)

> 现有AI心理咨询评估体系受限于单轮静态问答，无法捕捉治疗过程中的纵向动态与多流派技术差异，导致模型在长程对话中易出现治疗漂移。本文通过重构369份真实临床案例报告，构建了覆盖5种疗法、平均7.6个会话的纵向基准，并引入层级技能树与双维评估框架。其价值在于填补了动态临床保真度评估的空白，但基于LLM-as-a-Judge的评估协议是否真正消除了主观偏差，仍存疑。

】

---

【Psychological Counseling Cannot Be Achieved Overnight: Automated Psychological Counseling Through Multi-Session Conversations ｜多会话心理咨询中的纵向一致性建模

研究机构：哈尔滨工业大学

作者：Bichen Wang、Junzhe Wang、Yixin Sun 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_873f6ad96583)

> 自动化心理咨询长期受限于单会话设定，无法模拟真实治疗中跨次数的状态演进与目标调整，导致模型在长程交互中出现治疗漂移。现有合成数据集多聚焦单轮或简单多轮扩展，缺乏对客户心理状态动态变化的结构化追踪。本文通过构建基于认知行为疗法（CBT）的多会话数据集 MusPsy-Dataset，并训练具备记忆增强能力的 MusPsy-Model，实现了会话间目标的动态规划与一致性维持。该工作验证了结构化记忆对纵向咨询质量的提升作用，但其依赖 LLM 模拟客户的评估协议可能高估实际临床疗效。

】

---

【PsyPath: Psychologically-guided Self-Exploration for Personality Detection ｜心理引导自探索人格检测

研究机构：北京大学

作者：Zheng Li、Hongxin Ding、Chenyu Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_86dd14c75545)

> 文本人格检测长期受困于静态映射的局限，直接预测或固定问卷推理均无法捕捉临床心理学中动态诊断的逻辑。PsyPath 将人格推断重构为基于心理学的动态问答搜索过程，通过蒙特卡洛树搜索（MCTS）生成高置信度推理路径，并利用直接偏好优化（DPO）将这种诊断逻辑内化至模型。该方法在 MBTI 和 Essays 数据集上显著提升了预测准确率与可解释性，但其依赖外部 LLM 评分的机制是否真正解决了自报告与行为脱节的根本矛盾，仍存疑。

】

---

【Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation ｜经验知识增强与激活的工具执行框架

作者：Yupu Hao、Zhuoran Jin、Huanxuan Liao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e4f9388ab97a)

> 多步工具调用失败常源于模型缺乏具体执行经验，而非推理能力不足。现有方法多聚焦于提示工程或监督对齐，忽视了经验知识在推理时的激活效率与训练时的内化机制。本文提出KATE框架，通过实例级轨迹检索、并行采样宽度扩展及知识增强后训练，系统解决知识获取、激活与内化问题。该框架在BFCL-V3上将Qwen3-8B平均准确率从34.5%提升至45.17%，但缺乏与主流强化学习基线的直接对比，其泛化边界尚存疑。

】

---

【PuzzleClone: A DSL-Powered Framework for Synthesizing Verifiable Data ｜谜题克隆：基于领域特定语言的可验证数据合成框架

作者：Kai Xiong、Yanwei Huang、Rongjunchen Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f95ccefb08e)

> 大语言模型在复杂逻辑推理中常因训练数据稀缺且缺乏可靠真值而表现受限，现有基于大模型生成的数据合成方法存在可靠性低、多样性不足及验证成本高的瓶颈。PuzzleClone 提出了一种基于领域特定语言（DSL）的形式化数据合成框架，通过程序化验证确保生成谜题的逻辑正确性。该框架构建了包含 83,657 个可验证谜题的基准 PC-83K，并验证了其在强化学习训练中的有效性。尽管该方法在数据可靠性上实现了突破，但其依赖人工编码 DSL 规范的特性限制了其向非结构化任务自动扩展的能力。

】

---

【PyraMathBench: Evaluating and Improving Mathematical Capability in Large Language Models ｜层级化数学能力基准与工具调用优化

研究机构：华东师范大学

作者：Zetian Ouyang、Linlin Wang、Gerard de Melo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03858)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03858)

> 大语言模型在数学任务中的高分往往掩盖了数值处理缺陷与逻辑推理错误的混淆，现有基准仅关注最终答案，无法区分模型是算错了还是没读懂题。本文切入点在于构建一个将复杂数学问题拆解为14个独立子任务的层级化基准，以定位具体失效环节。通过引入模糊匹配模块SOLVE与多轮交互强化学习算法IRPO，本文验证了细粒度诊断对提升工具调用效率的有效性。该工作揭示了数学专用模型在指令遵循上的脆弱性，但其层级分解的因果归因强度仍受限于子任务间的独立性假设。

】

---

【QUARTZ: Quantile-Aware Routing and Queueing for TTFT SLOs in LLM Serving ｜分位数感知路由与排队

作者：Zhipeng Liu、Yifan Zheng、Fanqi Kong 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eb781056c7d4)

> 导读 交互式大语言模型服务面临严苛的首字延迟（Time to First Token, TTFT）尾分位数服务等级目标（SLO），但现有路由器忽略请求成本差异，导致长提示请求阻塞短请求，放大尾延迟。本文指出点估计预测与尾SLO目标错位，提出QUARTZ框架，通过预测保守服务时间分位数并据此进行路由与准入决策，在保持公平性的同时降低TTFT尾延迟。该方案在SGLang测试床上验证了跨模型规模的有效性，但其仅针对预填充阶段，解码阶段的延迟优化仍属空白。

】

---

【QuCo-RAG: Quantifying Uncertainty from the Pre-training Corpus for Dynamic Retrieval-Augmented Generation ｜基于预训练语料统计的动态检索增强生成

作者：Dehai Min、Kailin Zhang、Tongtong Wu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec1f437c42a4)

> 动态检索增强生成（Dynamic RAG）旨在解决大语言模型（LLM）在生成过程中因内部置信度信号不可靠而导致的幻觉问题，现有方法依赖的模型内部信号（如熵、注意力）在长尾知识上系统性失效。本文切入点在于将不确定性量化从主观的内部状态转向客观的外部证据，即利用预训练语料的实体频率与共现统计作为检索触发器。具体做法是构建两阶段检测机制：生成前评估实体频率，生成中验证三元组共现。该方法在跨模型迁移中展现出鲁棒性，但其有效性高度依赖代理语料与目标模型训练数据分布的重叠度，这一边界条件在现有实验中尚未被充分量化。

】

---

【Query-Focused Individual Simulation with Progressive Persona Completion ｜查询聚焦个体模拟中的渐进式人格补全

研究机构：日本东京大学、日本名古屋大学

作者：Weiwen SU、Naoki Yoshinaga、Masashi Toyoda

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b024fa529e4c)

> 基于大语言模型的角色模拟旨在以合成数据替代高成本的人类社会调查，其核心价值在于解决大规模行为数据获取的效率与隐私瓶颈。现有方法通常预设完整且静态的人格画像，但在面对普通个体时，这种“全量前置”策略不仅成本高昂，且因不同查询依赖不同维度而导致信息冗余或覆盖不足。本文切入点在于将人格构建从静态输入转化为查询驱动的按需获取闭环，通过渐进式预测与自报告置信度停止机制，在冷启动场景下以极少的请求数实现高保真模拟。这一范式在效率与质量间取得了平衡，但其对代理推断真实性的依赖仍存疑。

】

---

【QueueEDIT: Structural Self-Correction for Sequential Model Editing in LLMs ｜队列自校正序列模型编辑

研究机构：合肥工业大学、美国东北大学

作者：Taolin Zhang、Haidong Kang、Dongyang Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_732b8ea80b3c)

> 序列模型编辑（Sequential Model Editing, SME）旨在连续修正大语言模型（LLMs）中的事实错误，但现有方法独立处理每次编辑，导致累积参数偏差破坏模型通用能力。本文指出，编辑间存在语义依赖（如总统变更需同步更新配偶信息），而现有定位-编辑范式忽略了这种时序关联。QueueEDIT通过结构映射编辑将三元组解耦至FFN层特定矩阵，并利用FIFO队列动态对齐历史编辑参数，在1000次编辑下显著优于基线。该方法在长序列稳定性上表现优异，但绝对可靠性仍低于单跳编辑SOTA，且未与最新零空间约束方法对比。

】

---

【RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding ｜检索增强上下文快速投机解码

研究机构：武汉大学、上海交通大学

作者：Zihong Zhang、Zuchao Li、Lefei Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14885)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14885)

> 投机解码旨在通过并行验证打破自回归解码的串行瓶颈，但无训练方法面临检索信号稀疏与Logits信号局部性互补失效的困境。RACER通过构建Logits Tree与Retrieval Tree双树结构，将精确模式匹配作为结构锚点，将历史Logits复用作为动态外推线索，实现了无需额外模型训练的无损加速。该方法在多个基准上稳定超越纯检索与纯Logits基线，但其加速比仍低于训练式方法，且对长上下文下的内存管理缺乏深入验证。

】

---

【RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift in the Real World ｜连续知识漂移下的时序一致推理

研究机构：清华大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Hanbing Liu、Lang Cao、Yang Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3329e3acb532)

> 大语言模型（LLM）因预训练数据截止日固定，无法感知2024年后的世界状态变化，导致在回答动态事实时出现过时或时序矛盾。现有检索增强生成（RAG）仅做静态文本匹配，缺乏对事件演化轨迹的结构化建模，难以区分同一实体在不同时间点的状态。本文提出Chronos框架，通过构建事件演化图（EEG）将检索到的时间戳事实组织为显式时序拓扑，实现无需参数更新的动态推理。该方法在自建基准上显著优于标准RAG，但依赖高质量外部知识库，且未验证在长文档非结构化场景下的泛化能力。

】

---

【RAP-ID: Mechanistic Prompt Injection Detection via Impostor Behavior Analysis ｜基于内部状态动态的提示注入检测

作者：Yuchen Yang、Lei Peng、Yujie He 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6ec8d7052439)

> 大语言模型（LLM）在代理系统中难以区分系统指令与外部数据，导致提示注入攻击频发。现有外部护栏模型引入高延迟，而单一内部启发式方法误报率过高。RAP-ID 将注入攻击形式化为“语义模仿”与“注意力劫持”双过程，通过单次前向传播融合三个内部信号实现无训练检测。该方法在直接注入场景下表现优异，但在复杂代理间接注入场景中的防御能力仍显不足，其通用性边界尚待厘清。

】

---

【RAVR: Reference-Answer-guided Variational Reasoning for Large Language Models ｜参考答案引导的变分推理

研究机构：浙江大学、阿里巴巴集团

作者：Tianqianjin Lin、Xi Zhao、Xingyao Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.25206)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.25206)

> 基于可验证奖励的强化学习（RLVR）在训练大语言模型时面临采样瓶颈：当任务超出模型当前能力，模型无法生成足够多的高质量推理路径，导致训练坍缩至次优解。现有方法仅将参考答案用于计算奖励，忽略了其作为推理引导源的潜力。本文提出 RAVR，利用参考答案条件化生成“后验推理”，通过变分推断优化目标将其迁移至无答案的“先验推理”。该方法在小模型难任务上显著优于基线，但其对开放式任务及长文本推理的适用性尚未验证。

】

---

【RbtAct: Rebuttal as Supervision for Actionable Review Feedback Generation ｜基于反驳监督的可执行评审生成

研究机构：美国耶鲁大学、美国纽约大学

作者：Sihong Wu、Yiling Ma、Yilun Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09723)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09723)

> 同行评审自动化长期面临“生成流畅但缺乏行动指导”的困境，现有方法多依赖静态标注或通用提示，无法捕捉评论对作者实际修改行为的因果影响。RBTACT 将作者反驳（Rebuttal）转化为隐式偏好信号，通过直接偏好优化（DPO）训练模型生成能触发具体修改的评审片段。该方法在 8B 参数规模下实现了超越 70B 通用大模型的可执行性评分，但其效果高度依赖反驳数据的对齐质量，且未验证对最终论文录用率的直接贡献。

】

---

【RCBSF: A Multi-Agent Framework for Automated Contract Revision via Stackelberg Game ｜风险约束双层斯塔克尔伯格框架

研究机构：重庆大学、英国伦敦玛丽女王大学

作者：Shijia Xu、Yu Wang、Xiaolong Jia 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b000e7eb2efb)

> 法律合同修订面临的核心矛盾是通用大语言模型（LLM）将严格法律约束视为建议而非硬性边界，导致高风险输出。现有单智能体或合作型多智能体方法缺乏对抗性层级控制，无法在生成过程中强制合规。本文提出风险约束双层斯塔克尔伯格框架（RCBSF），通过领导者-跟随者博弈结构实现约束驱动的合同修订。该框架在7B模型上实现了超越72B基线的风险解决率，但其评估依赖LLM裁判，且未验证在动态多议题谈判中的泛化能力。

】

---

【RCTEA: Richness-guided Co-training for Temporal Entity Alignment ｜丰富度引导的时序实体对齐

研究机构：澳大利亚昆士兰大学、香港理工大学

作者：Jiayun Li、Wen Hua、Shiqi Fan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_320b44b196a5)

> 时序实体对齐（Temporal Entity Alignment, TEA）旨在跨图匹配等价实体，但现有模型常将结构与时序特征简单拼接，忽视了不同实体间特征丰富度的巨大差异，导致低质量信号污染高价值表示。本文指出，邻居节点的信息价值并非均等，低丰富度实体的监督信号会阻碍精确特征捕捉。RCTEA通过引入丰富度引导注意力机制与自适应权重策略，动态平衡结构与时序特征，并结合双视图邻域共识去噪，在YAGO-WIKI180K等基准上取得了优于HTEA和MGTEA的性能，但其对高频实体的依赖性及缺乏LLM语义辅助的局限仍需审视。

】

---

【Real Men are Tough: Evaluating Gender Bias and Sensitivity to Masculinity Norms in LLMs ｜男性规范作为潜在先验的隐性偏见评估

作者：Elisa Leonardelli、Camilla Casula、Boglarka Nyul 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a7dcfc7b119f)

> 语言模型在证据不足时，往往依赖社会规范填补信息空白，但现有评估多聚焦于显式刻板印象输出，忽略了规范作为“潜在先验”在歧义推理中的隐性作用。本文切入点在于区分“显式同意”与“隐式依赖”，通过构建基于心理学量表的场景推断基准，量化模型在信息缺失时对男性规范的归因倾向。其核心做法是设计消歧与歧义变体，控制性别标记，测量模型在不确定性下的行为偏移。该工作揭示了表面合规与内部偏见脱节的机制，但缺乏对去偏干预的验证，且评估范围局限于英语和意大利语。

】

---

【Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization ｜树结构自校正智能体策略优化

研究机构：美国乔治·华盛顿大学

作者：Yu Li、Sizhe Tang、Tian Lan

论文原文见 [arXiv](https://arxiv.org/abs/2604.07165)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07165)

> 多轮智能体强化学习面临稀疏奖励下的信用分配难题，现有组相对策略优化方法将轨迹视为独立链，导致关键决策点与常规步骤获得相同梯度信号。T-STAR 通过合并功能相似节点构建认知树，实现方差缩减的优势估计，并在分歧点合成纠正推理以提供步骤级监督。该方法无需额外奖励模型或采样，可直接集成于 GRPO 等主流算法，在长程推理任务上带来稳定增益，但其性能上限仍受限于单智能体架构与树合并阈值的静态设定。

】

---

【ReasonIF: Large Reasoning Models Fail to Follow Instructions During Reasoning ｜推理轨迹指令遵循基准与微调策略

研究机构：美国斯坦福大学

作者：Yongchan Kwon、Shang Zhu、Federico Bianchi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15211)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15211)

> 大推理模型（Large Reasoning Models, LRMs）在生成最终答案时往往能遵循用户指令，但在生成中间推理轨迹时却频繁违背格式、语言或长度约束，导致过程不可控且难以审计。现有指令遵循评估仅关注主响应，忽视了推理过程本身的合规性，而强化学习训练侧重答案正确性，未对推理轨迹施加约束。本文提出ReasonIF基准，通过可验证指令自动评估推理轨迹的指令遵循得分（Instruction Following Score, IFS），并设计推理指令微调（Reasoning Instruction Finetuning, RIF）策略。该工作揭示了推理过程可控性的严重缺失，但RIF仅验证了单一模型上的初步效果，未证明其对逻辑严谨性的增益。

】

---

【Reasoning in a Combinatorial and Constrained World: Benchmarking LLMs on Natural-Language Combinatorial Optimization ｜自然语言组合优化基准

研究机构：荷兰埃因霍温理工大学、新加坡南洋理工大学

作者：Xia Jiang、Jing Chen、Cong Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.02188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02188)

> 组合优化（Combinatorial Optimization, CO）要求在高维离散空间中寻找满足硬约束的最优解，但现有大语言模型（LLM）评估多聚焦于算术或逻辑推理，缺乏对复杂约束下决策能力的系统测试。主流优化基准往往依赖代码生成或外部求解器，混淆了模型内部推理与外部工具的性能。NLCO通过构建43个情境化CO任务的四层分类体系，强制LLM在无工具辅助下直接输出离散解，从而隔离评估其原生组合推理极限。该基准揭示了模型性能随实例规模急剧衰减的规律，但受限于中等规模实例与标准化文本，其结论向真实工业场景的外推性仍存疑。

】

---

【Reasoning Up the Instruction Ladder for Controllable Language Models ｜指令层级推理

研究机构：美国俄亥俄州立大学、微软研究院

作者：Zishuo Zheng、Vidhisha Balachandran、Chan Young Park 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.04694)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04694)

> 大语言模型在处理多源指令时，常因将系统提示与用户输入视为同等文本而陷入优先级冲突，导致安全策略被越狱攻击绕过。现有对齐方法多将安全视为独立标签进行训练，忽略了指令间固有的层级结构，且缺乏显式推理机制来动态解析冲突。本文提出将指令层级（IH）重构为元推理任务，通过构建含冲突对的VerIH数据集，利用可验证奖励强化学习（RLVR）训练模型在执行前显式推理指令优先级。该方法在无需安全数据的情况下实现了安全基准的零样本泛化，但其对复杂多轮交互及非结构化冲突的鲁棒性仍存疑。

】

---

【ReasonRec: A Reasoning-Augmented Multimodal Agent for Unified Recommendation ｜推理增强的多模态智能体推荐

研究机构：Meta AI、美国密歇根州立大学

作者：Yihua Zhang、Mingfu Liang、Jiyan Yang 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.28357)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.28357)

> 多模态推荐系统长期依赖黑盒前向推理，将意图推断、语义评估与效用权衡压缩为不透明的打分机制，导致在冷启动与跨域场景下缺乏透明度与鲁棒性。现有视觉语言模型（VLM）虽能融合多模态特征，但无法显式量化自身不确定性，也无法动态调用外部轻量模型以平衡计算成本。ReasonRec 通过构建“观察-深思-行动”三阶段智能体管道，结合证据地平线课程学习与不确定性引导的工具委托，将推荐重构为可解释的自适应决策过程。该框架在多项基准上显著提升了排序指标并降低了推理延迟，但其对预训练 VLM 骨干及手工指令模板的强依赖，限制了其在资源受限环境下的泛化潜力。

】

---

【RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents ｜基于复现的记忆固化

研究机构：香港中文大学、北京邮电大学

作者：Zijie Dai、Shiyuan Deng、Sheng Guan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.16045)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.16045)

> 长时程智能体面临固定上下文窗口导致的跨会话状态丢失，现有记忆系统通过每轮交互调用大语言模型进行事实提取，虽保真度高但构建成本极高。本文指出这种“急切固化”策略在低信息密度交互中是过度设计，提出基于复现的记忆固化机制，仅在检测到语义复现时触发高成本处理。该方法在保持准确率的同时大幅降低Token消耗，但其扁平化存储结构在复杂多跳推理任务上的表现仍存疑。

】

---

【Regret-Now: A Physics-Inspired Regret Framework for Temporal Knowledge Graph Question Answering with LLMs ｜基于最小势能原理的时序知识图谱问答框架

研究机构：南开大学

作者：Danyu Huang、Yao Zhang、Jun Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_69a4e4eacf29)

> 时序知识图谱问答（TKGQA）要求模型在动态演化的知识结构中执行多步推理，但大语言模型（LLM）常因中间步骤的逻辑断裂导致级联错误，且现有自校正方法依赖主观自评，缺乏客观纠错标准。Regret-Now 将推理过程类比为粒子在势能场中的运动，通过监测语义势能的异常上升实时触发回滚机制，以物理量化指标替代 LLM 的主观反思。该框架在 CronQuestions 和 MultiTQ 上取得了优于 Reflexion 等基线的性能，但其依赖外部嵌入模型计算势能，且未与最新神经符号 SOTA 对比，其通用性存疑。

】

---

【Reinforcement Learning with Semantic Rewards Enables Low-Resource Language Expansion without Alignment Tax ｜语义空间对齐

研究机构：上海交通大学、澳门大学

作者：Zeli Su、Ziyin Zhang、Zhou Liu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14366)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14366)

> 低资源语言扩展面临的核心矛盾是：在数据稀缺且分布偏斜的条件下，如何提升目标语言能力而不牺牲预训练模型的通用能力，即最小化“对齐税”。现有监督微调（SFT）方法通过token级似然最大化进行表面形式模仿，在窄分布上导致参数过度拟合与灾难性遗忘，无法兼顾适应性与保持性。本文切入点在于将对齐目标从token级匹配解耦为嵌入级语义一致性，利用组相对策略优化（GRPO）驱动模型在语义空间内探索多样表达。该方法在藏语-中文翻译任务上验证了RL比SFT更有效地保留通用能力，但其结论局限于单一语言对与特定骨干网络，泛化性存疑。

】

---

【Rejection-to-Acceptance Transition: Model Editing-Based Jailbreak Backdoor Injection Not Limited to Few Output Tokens ｜表示转移引导的越狱后门注入

作者：Shiji Yang、Min Cai、Hao Xiong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4167d275552)

> 大语言模型（LLM）的安全对齐机制常被外部提示优化攻击绕过，但此类攻击缺乏持久性且易被检测。现有基于模型编辑的越狱后门方法依赖绑定特定短语，导致攻击效率随绑定数量增加而急剧下降。JEST 摒弃短语绑定，通过主成分分析（PCA）建模拒绝与接受域，直接劫持 LLM 内部表示实现域转移。该方法在白盒场景下显著提升了攻击效率与成功率，但其对模型内部状态的破坏是否会被现有系统级防御机制识别，仍存疑。

】

---

【Relaxing the Constraints: A Dual-Importance Projection Mechanism for Lifelong Model Editing ｜双重要性投影编辑

研究机构：厦门大学、清华大学

作者：Zhenghai Chen、Senbin Xu、Jiaxi Tan 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01d69079fc63)

> 序列知识编辑旨在解决模型在连续更新中因参数累积干扰导致的旧知识遗忘与新知识泛化不足之间的矛盾。现有基于严格正交投影的方法虽能隔离历史知识，但过度约束梯度空间，导致长序列编辑下模型通用能力显著退化。DipEdit 通过引入累积重要性与投影重要性双机制，将硬正交约束转化为基于基向量重要性的软缩放投影，在保留关键历史知识的同时释放梯度表达空间。该方法在2000次连续编辑中实现了综合性能平均提升10.36%，但其有效性依赖于对输入激活子空间结构的假设，且在百万级超大规模编辑下的稳定性尚未得到验证。

】

---

【Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning ｜可靠性感知自适应自一致性

研究机构：韩国首尔大学

作者：Junseok Kim、Nakyeong Yang、Kyungmin Min 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02970)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02970)

> 大语言模型在复杂推理中常因解码随机性导致单次生成不可靠，自一致性（Self-Consistency, SC）通过多路径采样聚合提升准确率，但固定预算造成计算资源浪费。现有自适应方法依赖计数停止规则，忽略响应可靠性差异，导致证据累积低效。ReASC 引入响应级置信度信号，将采样决策从“计数”重构为“证据充分性”判断，通过两阶段门控机制动态调整采样量。该方法在保持精度的同时大幅降低推理成本，但其效率增益高度依赖置信度信号的质量与校准机制的稳定性。

】

---

【Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution ｜动态程序性记忆框架 ReMe

研究机构：上海交通大学、阿里巴巴集团

作者：Zouying Cao、Jiaji Deng、Li Yu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.10696)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.10696)

> 大语言模型智能体在长程任务中面临重复试错与经验无法有效复用的困境，现有记忆系统多采用被动累积范式，导致经验池随时间退化且检索结果缺乏任务适配性。ReMe 通过多面蒸馏、上下文自适应复用与效用驱动精炼，将程序性记忆从静态存储转变为反馈驱动的进化闭环。该框架验证了记忆质量可部分替代模型规模的效应，但其效用删除机制在单次失败场景下的鲁棒性仍存疑。

】

---

【Representation-Guided Parameter-Efficient LLM Unlearning ｜表示几何引导的低秩大语言模型遗忘

作者：Zeguan Xiao、Lang Mo、Yun Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17396)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d626cf0a2b4)

> 大语言模型（LLM）遗忘面临的核心矛盾是：在移除敏感知识的同时，必须维持模型在保留集上的通用效用。现有基于参数重要性（如Fisher信息）的低秩适应（LoRA）方法因“超叠加”现象导致参数多义性，难以精准隔离遗忘与保留知识，常引发效用崩溃。本文提出ReGLU，通过表示空间几何解耦替代参数统计量估计，利用平衡协方差矩阵初始化LoRA并引入正交损失约束更新方向。该方法在TOFU和WMDP基准上显著优于FILA和VILA，但其有效性局限于参数高效微调框架，未验证全参数场景下的深层知识擦除能力。

】

---

【Rerank Before You Reason: Analyzing Reranking Tradeoffs through Effective Token Cost in Deep Search Agents ｜重排优先于推理：深度搜索智能体中的有效Token成本分析

研究机构：加拿大滑铁卢大学

作者：Sahel Sharifymoghaddam、Jimmy Lin

论文原文见 [arXiv](https://arxiv.org/abs/2601.14224)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_30116f5662b4)

> 深度研究智能体在迭代检索与推理中面临测试时计算开销激增的困境，单纯增加推理预算往往导致边际收益递减且成本高昂。现有效率优化多聚焦于上下文压缩，却忽视了检索阶段重排对下游推理质量的杠杆作用。本文在BrowseComp-Plus基准上引入有效Token成本（Effective Token Cost, ETC）指标，量化重排深度与推理预算的权衡，证明适度重排能以更低成本实现更高准确率。该结论在固定语料库下成立，但向动态Web环境的泛化能力仍存疑。

】

---

【Rethinking Assessments of Prompt Injection Attacks ｜提示注入攻击评估框架的重构

作者：Chi Cui、Yixin Wu、Michael Backes 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e97da3ed2323)

> 提示注入（Prompt Injection）评估长期受限于实验室场景的简化假设，导致对真实应用风险的严重低估。现有基准多聚焦于合规任务与简单指令，无法捕捉非合规内容在复杂系统提示下的绕过机制。本文通过构建涵盖真实 GPTs 应用、非合规注入任务及复杂越狱指令的八维评估框架，量化了不同组件对攻击成功率的影响。该工作揭示了真实场景下防御机制的脆弱性，但其结论受限于未纳入系统级隔离防御的对比。

】

---

【Rethinking Reasoning: A Survey on Reasoning-based Backdoors in LLMs ｜推理级后门攻击的认知分类学

研究机构：新加坡南洋理工大学

作者：Man Hu、Xinyi Wu、Zuofeng Suo 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07697)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07697)

> 大语言模型（Large Language Models, LLMs）的推理能力在提升任务性能的同时，引入了针对思维链（Chain-of-Thought, CoT）中间步骤的隐蔽攻击面，现有综述多孤立讨论后门或推理安全，缺乏针对“推理劫持”机制的系统性框架。本文切入点在于区分攻击对模型认知过程的不同操纵方式，而非仅关注输入输出映射。通过构建关联式、被动式与主动式三类认知中心分类法，论文梳理了从触发器植入到推理路径污染的完整攻击谱系。该分类法填补了推理级后门机制研究的空白，但作为纯综述工作，其价值取决于分类维度的完备性，且未提供量化防御对比数据，分类边界在连续潜在推理等新架构下的适用性存疑。

】

---

【Rethinking RL Evaluation: Can Benchmarks Truly Reveal Failures of RL Methods? ｜强化学习评估的泛化失效诊断

研究机构：中国科学院、中国科学技术大学

作者：Zihan Chen、Yiming Zhang、Hengguang Zhou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10541)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10541)

> 当前大语言模型（LLM）强化学习（RL）后训练在基准测试上取得高分，但高分是否代表真实推理能力存疑。传统“训练集与测试集分离”的评估范式假设“未见数据”能区分泛化能力，但RL模型可能通过过拟合测试分布或捷径学习掩盖了这一区分度。本文提出Oracle Performance Gap (OPG) 指标，通过对比在训练集与测试集上直接训练的模型性能差距，量化基准的区分度失效。结合难度分层、分布偏移与反事实测试，本文揭示了RL模型泛化的脆弱性，为基准设计提供了原则，但仅局限于数学推理任务且未提供去污算法。

】

---

【Retrieve Only Relevant Tables Whether Few or Many: Adaptive Table Retrieval Method ｜自适应表格检索

作者：Taehee Kim、Seungbin Yang、Jihwan Kim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.18766)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f8f703d6fbeb)

> 表格检索旨在从大规模数据库语料中定位回答自然语言查询所需的最小表格子集，是Text-to-SQL任务的关键前置步骤。现有固定Top-k策略因无法预知查询所需表格数量，导致小k漏检关键证据、大k引入噪声并增加延迟，这一矛盾在Spider 2.0等包含数百张表的复杂场景中尤为突出。本文提出自适应表格检索（Adaptive Table Retrieval, ATR），通过查询依赖的阈值机制动态确定检索数量，并结合滑动窗口重排序处理大规模语料。该方法在检索精度与下游执行准确率上均优于固定k基线，但其性能上限受限于纯文本Schema表示，未探索视觉布局信息的潜在增益。

】

---

【Revisiting Self-Play Preference Optimization: On the Role of Prompt Difficulty ｜自博弈偏好优化中的提示难度筛选

作者：Yao Xiao、Jung-jae Kim、Roy Ka-Wei Lee 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_412ace842d64)

> 自博弈偏好优化旨在通过模型自我生成响应并基于奖励模型筛选正负样本，利用直接偏好优化（DPO）提升大语言模型（LLM）的对齐性能，但现有方法通常假设所有提示对优化贡献均等，忽视了提示难度分布对训练效率的潜在干扰。本文切入点在于量化提示难度并揭示困难提示对DPO训练的负向影响，提出基于均值奖励的提示难度度量与筛选策略。具体做法是计算每个提示多次采样响应的平均奖励作为难度代理，剔除最困难的25%提示后仅保留最易的30%进行训练。该策略在AlpacaEval 2上显著提升了Tulu-8B和Mistral-7B的性能，但仅验证了静态筛选的有效性，未探讨动态难度适应机制。

】

---

【Revisiting the Uniform Information Density Hypothesis in LLM Reasoning ｜均匀信息密度假设在LLM推理中的重构

研究机构：韩国延世大学

作者：Minju Gwak、Guijin Son、Jaehyung Kim

论文原文见 [arXiv](https://arxiv.org/abs/2510.06953)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06953)

> 思维链推理的脆弱性源于模型常生成表面连贯但逻辑断裂的文本，现有基于置信度或熵的筛选方法缺乏对推理轨迹内部结构的解释力。本文切入点在于引入心理语言学中的均匀信息密度（Uniform Information Density, UID）假设，将推理视为信息流过程，通过量化步骤级信息密度的全局与局部均匀性来预测推理质量。具体做法是定义基于预测分布熵的步骤信息密度，并计算其方差与突变计数作为Best-of-N采样的选择指标。该框架在数学基准上显著优于传统启发式，但其有效性依赖于对“全局非均匀性”这一反直觉特征的识别，且未验证其在闭源模型或知识密集型任务中的泛化能力。

】

---

【Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs ｜独特性感知强化学习

研究机构：美国麻省理工学院、新加坡国立大学

作者：Zhiyuan Hu、Yucheng Wang、Yufei He 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.08763)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08763)

> 强化学习后训练在提升大语言模型单次推理准确率的同时，常导致策略坍缩，使多次采样下的覆盖率停滞。现有基于Token熵或嵌入距离的正则化方法无法区分表面词汇差异与底层解题策略的同质性，导致探索空间被无效的表面多样性占据。本文提出在Rollout集合层面定义策略唯一性，通过LLM裁判聚类解题路径并反向加权优势函数，以奖励稀有且正确的策略。该方法在数学、物理及医学推理基准上显著提升了大采样预算下的性能，但其效果高度依赖裁判模型的聚类准确性，且未验证在非可验证领域的泛化能力。

】

---

【RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning ｜奖励感知微调

作者：Zehua Liu、Shuqi Liu、Tao Zhong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09253)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09253)

> 大语言模型后训练常面临高质量专家数据稀缺与自生成数据中负样本被浪费的双重困境。拒绝采样微调（RFT）虽通过自生成缓解数据依赖，但其硬阈值筛选机制丢弃了包含失败模式信息的负样本，导致模型无法区分正确与错误输出的细微差异。本文提出奖励感知微调（RIFT），通过有界线性代理损失稳定利用负样本梯度，在不引入参考模型的前提下实现数据高效对齐。该方法在数学推理基准上显著优于RFT与DPO，但其性能上限仍受限于奖励信号的判别力，且在非可验证任务上的泛化能力尚未得到验证。

】

---

【RISER: Orchestrating Latent Reasoning Skills for Adaptive Activation Steering ｜动态激活引导下的潜在推理技能编排

研究机构：同济大学

作者：Wencheng Ye、Xiaoyang Yuan、Yi Bin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09269)

> 大语言模型在复杂推理任务中常因静态提示或参数微调导致效率低下与泛化受限，现有激活引导方法仅能施加单一固定向量，无法适应多步推理中动态变化的认知需求。RISER 通过构建可复用的认知原语向量库，并引入经强化学习训练的轻量级路由器，在推理时动态组合并注入这些向量，实现了无需更新骨干参数的细粒度控制。该方法在七个基准上实现了3.4%–6.5%的零样本准确率提升，同时保持接近标准推理的计算效率，但其跨模型迁移能力的局限性揭示了表征几何对控制策略的强依赖。

】

---

【Risk-Controlled Event-Driven Cascading Updates for Knowledge Graph Consistency Restoration ｜事件驱动级联知识图谱一致性修复

研究机构：美国范德堡大学、Adobe研究院

作者：Bo Ni、Qinwen Ge、Haowei Fu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a2fb024a048d)

> 动态知识图谱（Dynamic Knowledge Graph, DKG）在引入新事实时，常因局部更新引发依赖关系的连锁失效，导致图谱整体不一致。传统补全模型假设数据内部一致，无法处理这种由外部事件触发的多跳级联修正需求。本文提出 CASCADEKG 框架，通过 Learn-Then-Test (LTT) 校准控制级联错误累积，并结合大语言模型（Large Language Model, LLM）增强事件语义评分。该方法在自建基准上实现了风险可控的一致性恢复，但其统计保证依赖于校准集规模，且未验证在超大规模图谱上的计算效率。

】

---

【RLShield: Dynamic Jailbreak Detection for LLMs via Reinforced Adaptive Learning ｜动态越狱检测：基于强化学习的自适应阈值框架

作者：Zhao Tong、Pengfei Yang、Yimeng Gu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_85b141837edc)

> 大语言模型（LLM）的安全对齐面临静态防御边界易被对抗性输入突破的困境，现有检测机制依赖固定阈值，难以适应不断演化的攻击模式与模型更新。本文切入点在于将阈值选择建模为连续控制问题，通过强化学习实现针对每个提示的动态决策。具体做法是结合跨层参数定位与软演员-评论家（Soft Actor-Critic, SAC）代理，在推理时实时计算风险分数并输出样本特异性阈值。该框架在多个基准上提升了检测精度与效率，但其对内部参数稳定性的假设及单轮检测的局限仍存疑。

】

---

【Robustness via Referencing: Defending against Prompt Injection Attacks by Referencing the Executed Instruction ｜指令引用过滤防御

作者：Yulin Chen、Haoran Li、Yuan Sui 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2504.20472)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_254d4f83bdb4)

> 提示注入攻击利用大语言模型（LLM）无法区分指令与数据的缺陷，导致模型执行恶意指令。现有防御多采用抑制策略，强行约束模型遵循原始指令，但实验表明这种抑制往往失效且损害通用能力。本文切入点在于利用而非抑制模型的指令遵循能力，通过提示模型显式引用所执行指令的标签，再基于标签过滤无关响应。该方法在QA场景下将攻击成功率（ASR）降至接近0%，但未验证代理工具调用场景下的鲁棒性，其依赖模型正确生成引用的假设在复杂交互中是否成立存疑。

】

---

【Role-Sensitive Neurons: A Neuron-Level Gain Control Mechanism for Confidence Steering ｜角色敏感神经元：置信度增益控制机制

作者：Peiwen Huang、Chih-Hao Hsu、Tzu-Hung Huang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18eb653d1404)

> 大语言模型（LLMs）在角色扮演提示下表现出的性能波动，常被归因于知识检索能力的差异，但这一解释忽略了模型内部“行动意愿”的独立调控机制。现有激活引导方法多聚焦于毒性或真实性等语义属性，缺乏对决策阈值这一元认知维度的干预手段，导致无法区分“不知道”与“不敢答”。本文通过识别并操控稀疏的角色敏感神经元（Role-Sensitive Neurons, RSNs），将置信度调控从提示工程层面下沉至神经基底层面，实现了对弃权行为的因果控制。这一发现揭示了置信度与知识表征的解耦几何，但其在知识匮乏模型中可能诱发“无根据的确定性”，边界尚待厘清。

】

---

【RoleConflictBench: A Benchmark of Role Conflict Scenarios for Evaluating LLMs' Contextual Sensitivity ｜角色冲突情境敏感性基准

研究机构：韩国科学技术院

作者：Jisu Shin、Hoyun Song、Juhyun Oh 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25897)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25897)

> 导读 LLM在个性化咨询与社会模拟中常需处理角色冲突，即多重社会角色期望无法同时满足的困境。现有评估多依赖静态规范或预设“正确答案”，无法捕捉主观困境中动态情境对决策的调节作用。本文引入“情境紧迫性”作为客观控制变量，构建RoleConflictBench基准，通过解耦模型内部角色偏好与外部情境约束，量化LLM对动态上下文的响应能力。该工作揭示了LLM在角色冲突中系统性忽视紧迫性、受静态偏见支配的缺陷，为理解LLM社会推理机制提供了新视角，但其评估是否过度简化了真实社会互动的模糊性仍存疑。

】

---

【Rotation Control Unlearning: Quantifying and Controlling Continuous Unlearning for LLM with The Cognitive Rotation Space ｜旋转控制遗忘：量化与调控LLM持续遗忘的认知旋转空间

研究机构：西安电子科技大学

作者：Xiang Zhang、Kun Wei、Xu Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25743)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25743)

> 大语言模型（LLM）在真实场景中面临连续到达的遗忘请求，现有方法因依赖保留集且参数更新相互干扰，导致累积效用损失。本文切入点在于将LoRA更新重构为高维空间中的旋转操作，通过控制旋转角度与正交轴来量化并隔离遗忘过程。该方法在无保留集条件下实现了持续遗忘的稳定性。其价值在于提供了可解释的遗忘程度度量，但旋转角度与知识擦除深度的因果关联仍缺乏信息论层面的严格证明。

】

---

【RSA-Bench: Benchmarking Audio Large Models in Real-World Acoustic Scenarios ｜真实声学场景下的音频大模型鲁棒性基准

作者：Yibo Zhang、Kaiwen Luo、Liang Lin 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0feee803cac6)

> 音频大模型（Audio Large Model, ALLM）在干净音频上表现优异，但真实物理环境中的多源噪声导致其性能急剧下降，现有评估多依赖合成高斯噪声，无法反映真实声学生态的复杂性。本文提出 RSA-Bench，通过叠加 1-4 个真实环境噪声源构建压力测试集，量化模型在感知与认知任务上的鲁棒性边界。实验揭示“感知-认知差距”与“去噪悖论”，即高层推理任务对噪声更敏感，且标准去噪算法反而加剧性能退化。该基准填补了真实场景鲁棒性评估的空白，但固定信噪比设置可能掩盖不同噪声强度下的真实分布差异。

】

---

【RubRIX: Rubric-Driven Risk Mitigation in Caregiver-AI Interactions ｜照护者AI交互风险缓解框架

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国马萨诸塞大学阿默斯特分校

作者：Drishti Goel、Jeongah Lee、Qiuyue Joy Zhong 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13235)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13235)

> 大语言模型（LLM）在医疗照护场景中常因缺乏领域敏感性而引发情感无效化或认知傲慢等隐性风险，现有通用安全基准无法捕捉此类交互性伤害。本文切入点在于将关怀伦理学转化为可审计的评估标准，构建照护者专用的风险分类学。通过“评估-反馈-精炼”闭环，RubRIX框架在单次迭代中实现了45-98%的风险组件降低。该框架验证了结构化反馈对交互安全的增益，但其对模型底层知识缺陷的掩盖效应及跨文化泛化能力仍存疑。

】

---

【SafeEvalAgent: Toward Agentic and Self-Evolving Safety Evaluation of LLMs ｜法规驱动的自演化智能体安全评估

研究机构：复旦大学、华东师范大学

作者：Yixu Wang、Xin Wang、Yang Yao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26100)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26100)

> 现有LLM安全评估依赖静态人工基准，无法应对快速演变的攻击向量与动态更新的法规标准，导致“合规”模型在新兴威胁下失效。SafeEvalAgent通过多智能体协作，将非结构化法规自动转化为可测试知识库，并引入自演化循环，根据目标模型的失败模式动态生成更具针对性的测试用例。该框架在11个前沿模型上验证了自演化机制能显著降低模型安全评分，揭示静态评估的盲区。其价值在于实现了从“一次性审计”到“持续对抗”的范式转变，但评估结果对初始种子问题的敏感性及计算成本未得到充分控制。

】

---

【SAFER: A Controllable Safeguard for LLMs against Backdoor Attacks ｜统计保障的推理时后门防御

研究机构：新加坡南洋理工大学

作者：Zirui Hu、Zheng Zhang、Yingjie Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_67768403d2df)

> 大语言模型在金融、医疗等高利害场景中部署时，推理时后门防御面临的核心矛盾是：现有评分函数虽能区分干净与投毒样本，但缺乏对假接受率（False Acceptance Rate, FAR）的显式统计控制，导致安全阈值无法量化。本文切入点在于，将后门检测重构为多重假设检验问题，通过估计样本为干净的局部似然概率，求解约束优化问题以在满足用户指定FAR阈值的同时最大化干净样本接受率。该方法无需已知后门样本校准，仅依赖干净校准集与混合测试集。其价值在于提供了渐近FAR保证，但实验仅覆盖词法触发器，对语义级攻击的鲁棒性存疑。

】

---

【Safety Is Not Universal: The Selective Safety Trap in LLM Alignment ｜选择性安全陷阱：LLM对齐中的群体偏差审计与公平性优化

作者：Iago Alves Brito、Walcy Rios、Julia Soares Dollis 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fc8a69554c91)

> 大语言模型的安全对齐长期被聚合指标掩盖，模型在“身份仇恨”等通用标签下表现出的高防御率，往往掩盖了对特定少数群体保护缺失的事实。现有基准如HarmBench聚焦于攻击行为类型（What），却忽略了受害群体维度（Who），导致无法区分模型是具备通用的语义拒绝能力，还是仅记忆了特定群体的防御触发器。本文通过构建双语、多群体的越狱基准MiJaBench，量化了这种“选择性安全陷阱”，并验证了直接偏好优化（DPO）在消除群体间防御率偏差上的有效性。该工作揭示了安全对齐的公平性盲区，但其结论受限于特定语言对与模型规模，跨语言泛化机制仍存疑。

】

---

【Safety Sidecar: Reflection-Driven Runtime Control for Safer Agents ｜安全侧车：基于反思驱动的运行时控制

研究机构：北京大学、厦门大学

作者：Wang Bin、Quan Jiazheng、Xingrui Yu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac4bf9f7ef33)

> 大语言模型智能体在自主执行多步任务时，微小的推理或检索偏差会被工作流放大为具有实际副作用的危险动作，而现有静态提示或事后过滤机制无法在动作执行前进行干预。本文提出 Safety Sidecar，一个即插即用的运行时控制模块，通过将反思过程转化为闭环控制器，在动作执行前检索证据并生成修复，同时利用外部验证器门控记忆更新。该方法在安全代码生成场景中验证了可行性，但其在通用工具调用场景下的泛化能力与验证器覆盖范围仍存疑。

】

---

【SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization ｜嵌入层自适应阻尼优化器

作者：Wooin Lee、Hyun-Tae Kim

论文原文见 [arXiv](https://arxiv.org/abs/2604.07663)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07663)

> 大语言模型预训练面临内存墙，传统AdamW优化器需存储与参数量等大的二阶矩状态，导致显存开销翻倍。现有轻量级优化器（如Lion、SinkGD）虽能压缩状态，但在处理嵌入层稀疏且高方差的梯度时稳定性不足，往往被迫回退至AdamW，抵消了内存收益。本文提出SAGE，通过引入一个$O(d)$维度的自适应阻尼器替代静态缩放，在保持单动量状态的前提下稳定嵌入层更新。该设计在1.3B模型上实现了24.33的测试困惑度，优于所有对比基线，但其有效性局限于中小规模模型，且未验证在更大规模或不同数据分布下的泛化能力。

】

---

【SCALE: Upscaled Continual Learning of Large Language Models ｜宽度扩展持续学习架构

作者：Jin-woo Lee、Junhwa Choi、Bongkyu Hwang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0b05b7bda0f3)

> 大语言模型在持续预训练中面临容量扩展与知识保留的结构性冲突，深度扩展虽增加层数却扰动原有表示，导致灾难性遗忘。现有参数高效微调方法不增加新容量，而深度扩展方法缺乏函数保持保证。SCALE 通过宽度扩展冻结原参数并插入轻量级线性模块，结合令牌级路由在保持与适应路径间动态切换，实现了稳定性与可塑性的可控权衡。该架构在合成传记任务上显著抑制了遗忘，但在真实多语言语料上的新知识获取能力仍显有限。

】

---

【Scaling Evaluation-Time Compute with Reasoning Models as Evaluators ｜评估时扩展：推理模型作为评估器

研究机构：美国卡内基梅隆大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Seungone Kim、Ian Wu、Jinu Lee 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2503.19877)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_997df2a4cad0)

> 测试时扩展（Test-Time Scaling, TTS）通常用于提升生成器解决复杂问题的准确率，但评估器在重排候选答案时同样面临算力与精度的权衡。传统过程奖励模型（Process Reward Model, PRM）依赖大规模过程监督训练，且固定预算下难以适应不同难度任务的评估需求。本文提出将推理模型直接作为评估器，通过强制其生成更长的思维链（Chain-of-Thought, CoT）来扩展评估时算力，无需额外训练即可超越专用PRM。该范式验证了评估精度随推理token单调提升的规律，但在高难度开放域任务上的泛化边界尚存疑。

】

---

【Scaling Laws for Code: Every Programming Language Matters ｜多语言代码预训练缩放定律

研究机构：北京航空航天大学、中国人民大学

作者：Jian Yang、Shuyue Guo、Linzheng Chai 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f7842f1f2e0)

> 通用自然语言缩放定律假设数据同质，无法指导多语言代码库中不同编程语言的令牌分配，导致资源浪费与性能预测偏差。现有代码缩放研究仅关注单语言或整体数据量，忽略了语言间的语法异构性与跨语言迁移效应。本文通过1000+次从头训练实验，建立比例依赖的多语言缩放模型，量化各语言独立缩放指数与协同增益。该工作填补了代码域多语言资源分配的理论空白，但其最优分配策略在极端数据受限下的鲁棒性存疑。

】

---

【Schema-Guided Response Generation using Multi-Frame Dialogue State for Motivational Interviewing Systems ｜基于多帧对话状态的动机访谈响应生成

作者：Jie Zeng、Yukiko Nakano

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_98d0df49da8a)

> 动机访谈（Motivational Interviewing, MI）旨在通过协作式对话激发客户内在改变动机，而非由咨询师直接提供建议。现有大语言模型（LLM）驱动的MI系统常陷入“建议导向”陷阱，即过度依赖AI生成具体解决方案，导致客户自主性丧失与改变谈话（Change Talk, CT）频率低下。本文提出SGR-MI，通过多帧对话状态追踪与基于检索的对话策略生成，在低资源场景下实现MI原则的严格遵循。该方法在真实用户研究中显著降低了非MI行为率并提升了CT激发效率，但其策略池的构建依赖LLM生成的伪策略，缺乏独立临床验证，且文本交互形式限制了CT的绝对数量上限。

】

---

【SciExplore: Evaluating Autonomous Agents from Scientific Navigation to Information Integration ｜科学信息检索与结构化合成基准

研究机构：中国科学技术大学

作者：Yinhao Tang、Youqing Fang、Yanan Sun 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.20926)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.20926)

> 现有科学大语言模型（LLM）评估体系割裂了通用检索与静态问答，无法衡量智能体在真实科研场景中从噪声文献中获取证据并构建结构化知识的能力。SCIEXPLORE 通过专家构建的 103 个博士级任务，将评估焦点从答案正确性转向证据接地与表格级合成。该基准揭示了当前最先进智能体在长程检索与格式遵循上的系统性失效，为科学智能体评估提供了过程级新维度，但其对“搜索深度”与任务难度关系的反直觉发现尚需更多实证支撑。

】

---

【SciText2Eq: Assessing LLMs for Explainable Equation Generation for Scientific Creativity ｜科学文本公式生成与语义对齐

研究机构：荷兰阿姆斯特丹自由大学、荷兰瓦赫宁根大学与研究中心

作者：Yifan Mo、Xiao Fu、Yue Su 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.16003)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16003)

> 科学文献中公式与叙述交织，现有方法多关注单点提取或数值等价，难以处理长文档中公式间的依赖关系及语义忠实度。本文提出 SciText2Eq 工作流，通过文档级序列生成与多层级评估协议，诊断 LLM 在真实科学文本中重构公式的能力。实验表明，模型在词汇相似度上表现中等，但在语义等价性上存在显著缺陷，且 LLM 评估与人类判断对齐度低。该工作填补了从“解题”到“科学公式生成”的评估空白，但缺乏符号验证器的硬约束，其评估可靠性仍存疑。

】

---

【SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation ｜多学科多模态科学推理基准

研究机构：中国科学院、中国科学院大学

作者：Longteng Guo、Xuanxu Lin、Dongze Hao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.10187)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.10187)

> 现有多模态大语言模型（MLLMs）在科学推理评估中面临学科覆盖窄、难度单一且缺乏过程可追溯性的困境，导致无法区分模型是依赖视觉感知还是真正的多步逻辑推导。本文通过构建覆盖6大领域54个子学科、包含专家解题轨迹的多模态基准SciVQR，填补了从基础事实到研究生级多跳推理的评估空白。该基准不仅评估最终答案，更通过五维指标诊断思维链（Chain-of-Thought, CoT）的忠实性。其价值在于提供了过程级评估的多模态参照系，但静态考试题源的数据污染风险及缺乏检索增强基线，限制了其对模型真实知识整合能力的全面诊断。

】

---

【Scripts Through Time: A Survey of the Evolving Role of Transliteration in NLP ｜转写作为跨脚本迁移的锚点机制：从词汇重叠到多脚本感知

作者：Thanmay Jayakumar、Deepon Halder、Raj Dabre

论文原文见 [arXiv](https://arxiv.org/abs/2604.18722)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa08d6da4b9e)

> 跨语言迁移在低资源语言上常因书写系统差异而失效，即“脚本壁垒”。现有方法多聚焦于模型内部语义空间对齐或全量数据增强，却忽视了输入形态层面的词汇重叠缺失这一直接障碍。本文系统梳理了转写（Transliteration）作为打破该壁垒的技术路径，将其从统计机器翻译时代的OOV处理工具，重构为大语言模型时代的多脚本感知辅助信号。其价值在于提供了无需平行语料、计算高效的实践指南，但转写引入的歧义性与语义损失风险使其并非万能解，且在复杂推理任务中的有效性存疑。

】

---

【SCURank: Ranking Multiple Candidate Summaries with Summary Content Units for Enhanced Summarization ｜基于摘要内容单元的候选排序蒸馏

研究机构：国立成功大学、国立清华大学

作者：Bo-Jyun Wang、Ying-Jia Lin、Hung-Yu Kao

论文原文见 [arXiv](https://arxiv.org/abs/2604.19185)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19185)

> 摘要蒸馏训练依赖候选摘要的质量排序来构建对比学习信号，但现有基于大语言模型（LLM）的直接排序方法存在严重的输入顺序敏感性与评估不一致性，而传统词汇重叠指标无法捕捉语义丰富度。本文提出 SCURank，通过提取摘要内容单元（Summary Content Units, SCUs）并利用聚类频率量化信息重要性，实现了对候选摘要的稳定排序。该方法在 CNN/DailyMail 和 XSum 数据集上显著优于 GPTRank 基线，但仅验证了词汇与语义相似度指标的提升，未直接证明事实一致性（Factual Consistency）的改善。

】

---

【SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia ｜东南亚文化接地多语言护栏模型

作者：Panuthep Tasawong、Jian Gang Ngui、Alham Fikri Aji 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0d007443ef3f)

> 现有安全护栏在东南亚低资源语言上因依赖机器翻译而丢失文化语境，导致对地区性敏感内容的检测失效。本文切入点在于构建首个基于多智能体合成框架生成的、覆盖8种东南亚语言的文化安全数据集，并训练专用护栏模型。通过蒙特卡洛推理集成（MCRE）解决标注不确定性，SEA-Guard在文化基准上显著优于通用SOTA，但在通用安全任务上仅具竞争力，其离线标注的高计算成本限制了实时部署潜力。

】

---

【SEAD: A Surrogate-free Label-only Membership Inference Attack against Pre-trained LLMs with Semantic-Aware Density ｜语义感知密度：无代理黑盒成员推断攻击

作者：Biao Yi、Jiahao Li、Yiming Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac149aed6e9c)

> 大语言模型（LLM）在预训练中不可避免地记忆敏感数据，成员推断攻击（MIA）是量化这一风险的核心手段，但生产级API通常仅返回生成文本而非完整概率分布，导致依赖Logits的传统攻击失效。现有Label-only攻击依赖代理模型进行概率回归，却因代理选择偏差和巨大的估计误差而可靠性不足。本文提出SEAD，通过直接对目标模型进行蒙特卡洛采样并引入NLI语义加权，在无代理条件下重构Token概率密度。该方法在Label-only设定下刷新了SOTA，但其性能仍显著低于Logits-based攻击，且依赖外部NLI模型，其实际审计效能与计算成本之间的平衡尚存疑。

】

---

【SEARCH-R: Structured Entity-Aware Retrieval with Chain-of-Reasoning Navigator for Multi-hop Question Answering ｜结构化实体感知检索与推理导航的多跳问答框架

研究机构：香港城市大学、浙江大学

作者：FU Yuqing、Yimin Deng、Wanyu Wang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_946baeb79164)

> 多跳问答（MHQA）的核心困境在于模型常因推理路径随机或检索信息同质化而得出错误答案。现有提示工程方法无法精确控制子问题分解质量，传统稠密检索则难以区分高相似度但低实用性的文档。本文通过训练端到端推理导航器与依赖树实体量化检索双模块，将分解过程从提示驱动转为策略优化。该框架在长链推理基准上表现优异，但其对短链标准基准的增益有限，且依赖特定句法工具，泛化边界尚待验证。

】

---

【SEC-FinTables: Evaluating Large Language Models for Detecting Logical Inconsistencies on Tabular Data ｜金融表格逻辑一致性检测基准

作者：Shuyan Ke、Qiong Wu、Hui Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49e78f4052fb)

> 表格理解领域长期聚焦于从半结构化数据中提取信息以回答自然语言问题，但高 stakes 场景如金融审计更关注数据内部逻辑约束的自洽性。现有 LLM 在数值推理中易产生幻觉，且缺乏针对“内部约束违反”的标准化评测框架，导致无法量化模型在审计任务中的可靠性。本文构建了 SEC-FINTABLES 基准，通过从 SEC 财报中注入受控错误并设计四维评测协议，系统评估主流 LLM 检测逻辑不一致性的能力。该工作揭示了当前模型在细粒度结构定位上的显著短板，但受限于单表设定与纯文本序列化，其结论在复杂层级表格中的普适性存疑。

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

【See or Say Graphs: Agent-Driven Scalable Graph Understanding with Vision-Language Models ｜视觉-语言模型图结构理解中的模态协调框架

研究机构：中国科学技术大学、西安电子科技大学

作者：Shuo Han、Yukun Cao、Zezhong Ding 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_94f1c426bd79)

> 视觉-语言模型（VLM）在处理大规模图结构时面临输入令牌限制导致的可扩展性瓶颈，且缺乏有效机制协调文本与视觉模态的互补优势。现有方法要么依赖纯文本描述导致结构细节丢失，要么依赖全局视觉渲染导致分辨率不足，无法同时满足属性统计与局部拓扑推理的需求。GraphVista通过层级化图检索增强生成（GraphRAG）基座与规划代理任务路由，将属性任务分配给文本模态、结构推理任务分配给高分辨率视觉子图模态。该框架在Grena基准上实现了比最强基线2.6倍的准确率提升，但其对动态图结构及语义标签的扩展能力尚未验证。

】

---

【Seer Self-Consistency: Advance Budget Estimation for Adaptive Test-Time Scaling ｜预分配预算的自适应测试时扩展

作者：Shiyu Ji、Yixuan Wang、Yijun Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0814b8f15d6f)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理计算提升大语言模型（LLM）性能，但固定预算导致简单任务算力浪费，动态预算方法又因串行估计产生高延迟。现有自适应一致性方法在生成过程中实时停止，无法利用现代推理引擎的并行优势，导致Token效率与延迟无法同时优化。SeerSC 引入快速直觉推理（System 1）预估答案熵，在深思推理（System 2）执行前预分配采样预算，实现了并行生成下的动态扩展。该方法在保持精度的同时显著降低计算成本，但其熵估计在复杂多步推理中的预测稳定性尚存疑。

】

---

【Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection ｜选择性转向：基于判别层选择的范数保持控制

作者：Quy-Anh Dang、Chris Ngo

论文原文见 [arXiv](https://arxiv.org/abs/2601.19375)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19375)

> 激活转向旨在不更新权重的前提下，通过修改内部隐藏状态来精准控制大语言模型（LLM）的行为，以替代高成本的微调。现有几何旋转方法虽解决了线性加法的强度失控问题，但在全层均匀干预时，常因激活范数畸变导致小模型生成崩溃，且无法区分特征是否真正涌现的层级。本文提出选择性转向（Selective Steering, SS），通过正交旋转矩阵保证范数不变，并仅在正负类均值投影符号相反的判别层施加干预。该方案在小型模型上显著提升了攻击成功率并保持了通用能力，但其判别层选择机制对强对齐模型的泛化边界尚存疑。

】

---

【Self-Awareness before Action: Mitigating Logical Inertia via Proactive Cognitive Awareness ｜行动前自我意识：通过主动认知感知缓解逻辑惯性

研究机构：吉林大学

作者：Fulong Fan、Peilin Liu、Fengzhe Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20413)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20413)

> 大语言模型在非交互式长叙事推理中面临“信息不对称”困境，即模型需在固定文本中重构隐藏真相，却常因早期假设固化导致错误传播。现有思维链（Chain-of-Thought, CoT）与后置修正方法缺乏对前提完整性的前置审计，无法阻断初始错误向后续推理的扩散。SABA框架通过“信息融合”构建结构化基线状态，并采用“查询驱动结构化推理”递归解决缺失前提，实现了从直接预测到状态评估的范式转移。该框架在自建侦探谜题基准上显著优于基线，但其依赖骨干模型自评估能力的局限及较高的推理成本，限制了其在实时场景与小型模型中的泛化潜力。

】

---

【Self-Consistency from Only Two Samples: CoT-PoT Ensembling for Efficient LLM Reasoning ｜双模态一致性集成

研究机构：美国卡内基梅隆大学

作者：Raman Saparkhan、Majd Hawasly、Md Rizwan Parvez 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17433)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17433)

> 大语言模型在复杂推理中常因自回归生成的局部误差累积导致最终答案失效，而提升准确率的自一致性（Self-Consistency, SC）范式需消耗大量采样预算（如40次），造成高昂的计算延迟。现有早停方法依赖单一模态内的多数投票，难以捕捉语义层面的真实共识，导致效率与精度无法兼得。本文提出结合思维链（Chain-of-Thought, CoT）与程序思维（Program-of-Thought, PoT）的双模态集成框架，利用两种推理模式间低相关的错误分布，通过贝叶斯假设检验实现跨模态一致性早停。该方法在保持甚至提升精度的同时，将平均采样次数降低9.3倍，78.6%的任务仅需2次采样即可解决，但其性能高度依赖模型对PoT模态的内在能力，在弱推理模型上存在显著退化风险。

】

---

【Self-Evolving Multi-Agent Systems via Textual Backpropagation ｜智能体神经网络

研究机构：德国慕尼黑大学、德国慕尼黑工业大学

作者：Xiaowen Ma、Yunpu Ma、Chenyang Lin 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8741773b9ffa)

> 多智能体大语言模型框架（Multi-Agent LLM Frameworks）旨在通过结构化协作突破单一模型在长程任务中的推理瓶颈，但现有方案多依赖静态手动编排，难以适应动态任务且协调开销随规模非线性增长。本文切入点在于将经典神经网络的层级化反向传播机制迁移至智能体协作，以文本梯度替代数值梯度实现拓扑与提示的联合优化。具体做法是构建前向动态团队选择与后向工作流优化双阶段流程，在训练阶段学习可复用的智能体团队池，推理阶段冻结架构仅执行前向传播。该框架在多个基准上超越了静态基线，但其性能增益是否源于架构优化还是强骨干模型的固有优势，仍存疑。

】

---

【Self-Guided Plan Extraction for Instruction-Following Tasks with Goal-Conditional Reinforcement Learning ｜自引导计划提取与目标条件强化学习

作者：Zoya Volovikova、Nikita Sorokin、Dmitriy Lukashevskiy 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20601)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20601)

> 具身智能体在动态开放环境中遵循自然语言指令时，面临长程依赖与稀疏奖励导致的信用分配难题。现有基于演示的方法受限于数据成本，而纯强化学习方法在缺乏预定义技能库时难以将语言指令映射到具体动作。SuperIgor 通过 LLM 与 RL 智能体的迭代共训练，利用 DPO 反馈闭环自动筛选高价值计划，实现了无预定义技能库下的指令遵循。该框架在 CrafText 基准上显著优于纯 RL 基线，但计算成本高昂且与 Oracle 计划仍存在性能差距，其自学习闭环的收敛效率尚待验证。

】

---

【Self-Reflection Improves Safety of Large Reasoning Models ｜自我反思机制

研究机构：复旦大学、北京邮电大学

作者：Qiang Huang、Wei Zhai、Feng Huang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e10a37998c2c)

> 大型推理模型（LRMs）在长程思维链中易产生有害中间状态，而现有对齐方法仅能预防初始输出，无法干预生成过程中的风险漂移。本文提出在生成过程中插入显式反思标记，使模型在检测到有害信号时自主中断并修正，而非回退重生成。该方法通过监督微调与直接偏好优化组合训练，将有害内容率从13.8%降至4.1%，同时保持有用性。其价值在于将安全对齐从静态过滤转向动态修正，但单次反思能否覆盖长程推理中的多次漂移仍存疑。

】

---

【SenseJudge: Human-Centric Preference-Driven Judgment Framework ｜基于显式偏好蒸馏的个性化大语言模型评判框架

研究机构：北京大学

作者：Rui Li、Junfeng Liu、Xiangwen Kong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03189)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_21bc3541862b)

> 大语言模型评判（LLM-as-a-Judge）旨在替代昂贵的人类评估，但现有方法依赖固定偏好数据，难以适配异构用户的个性化价值。本文切入点在于将隐式人类偏好显式化，通过动态筛选偏好子集实现训练-free的定制化评判。具体做法是从少量标注对中蒸馏偏好文本，利用多数投票聚合优化评判一致性。该框架在真实多轮对话场景下显著提升了小模型评判精度，但其对通用基准的泛化能力及偏好子集选择的过拟合风险仍存疑。

】

---

【SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identification ｜结构感知示例检索增强大语言模型事件因果识别

作者：Zhifeng Hao、Zhongjie Chen、Junhao Lu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.03701)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03701)

> 事件因果识别（ECI）旨在判定文本中两个事件间是否存在因果关系，但大语言模型（LLM）在此任务上常因过度预测而产生因果幻觉。现有少样本方法依赖语义检索，易被表面词汇误导而忽略深层结构差异，导致推理偏差。SERE框架通过融合概念路径、句法结构与因果模式三种结构信号，检索结构对齐的示例以引导LLM推理。该方法在多个基准上显著提升了F1分数，但其效果高度依赖外部知识图谱的覆盖度与句法解析的准确性，在长尾或复杂语境下的泛化能力仍存疑。

】

---

【SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval ｜状态-目标-动作原子检索框架

作者：Xin Xie、Dongyun Xue、Wuguannan Yao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14712)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14712)

> 长程工具调用任务中，推理时搜索的高延迟与监督微调的泛化僵化构成核心矛盾。现有记忆代理依赖完整轨迹检索，在实体值或Schema微变时失效，无法复用底层因果逻辑。本文提出SGA-MCTS，通过离线蒙特卡洛树搜索挖掘并去词化为状态-目标-动作原子，在线以混合符号-语义检索作为软提示指导生成。该范式在工具调用基准上显著缩小了小模型与前沿模型的差距，但其缺乏形式化验证机制，在逻辑一致性保障上存在结构性缺口。

】

---

【Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation ｜上下文表示消融（CRA）：推理时动态掩码拒绝子空间

研究机构：浙江大学

作者：Wenpeng Xing、Moran Fang、Guangtai Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07835)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07835)

> 导读 大语言模型（LLM）的安全对齐常被视为静态防御，但现有机制在深层推理中极易被绕过，核心矛盾在于对齐目标与内部复杂语义表征的解耦。主流优化类攻击（如GCG）计算成本高且生成内容语义混乱，而静态编辑方法（如LED）会永久损害模型通用能力，导致防御与效用难以兼顾。本文提出上下文表示消融（Contextual Representation Ablation, CRA），通过推理时动态计算并掩码隐藏状态中的“拒绝子空间”，在不修改权重的情况下实现精准越狱。CRA在Llama-2上实现了53.0%的攻击成功率（ASR），较基线PEZ提升15.2倍，但其跨模型泛化性仍受限于7B规模模型的架构相似性，且未验证多轮对话中的状态连续性。

】

---

【Simple Role Assignment is Extraordinarily Effective for Safety Alignment ｜角色条件化安全对齐

研究机构：美国加州大学洛杉矶分校、天津大学

作者：Zhou Ziheng、Jiakun Ding、Zhaowei Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00061)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00061)

> 大语言模型（LLM）的安全对齐长期依赖固定原则列表，但原则枚举的完备性不足且缺乏情境认知机制，导致模型在复杂语境下拒绝行为僵化或失效。现有测试时对齐方法多聚焦于解码优化或奖励信号，忽略了评估标准来源本身的可塑性。本文提出以社会角色作为价值观与情境认知的联合载体，通过零训练的生成-批评迭代管线实现上下文敏感的安全对齐。该方法在多个基准上显著优于原则基线，但其有效性高度依赖角色选择，且未验证内部机制层面的鲁棒性。

】

---

【Single-Agent Generation Surpasses Multi-Agent Systems in Semantic Diversity ｜解耦提示与架构：单智能体多输出在语义多样性上的优势

作者：Encheng Cui、Shaowen Peng、Kazuhiro Ito 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_78737bc03f87)

> 导读 多智能体系统（MAS）常被用于提升大语言模型（LLM）的推理多样性，但现有研究往往将提示工程与架构设计混淆，导致增益来源不明。本文通过控制变量实验，在匹配提示条件与输出量的前提下，发现单智能体多输出（SI-MO）在语义多样性上优于串行与并行MAS。该研究通过解耦实例拓扑与输出多重性，揭示了信息可见性对生成多样性的关键作用。这一发现挑战了“多智能体即增效”的直觉，但受限于发散思维任务，其在通用推理任务中的普适性仍存疑。

】

---

【SMART: Semantic Header Flattening and Pseudo-Code-Style Reasoning for LLM-based Complex Table Question Answering ｜语义表头扁平化与伪代码推理

研究机构：华中科技大学

作者：Yongshuo Zhang、Jixiong Chen、Kaihe xu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ce677120608)

> 复杂表格问答的核心难题在于多级表头导致的层级语义在LLM线性化过程中丢失，进而引发推理错位与数值幻觉。现有方法或依赖手工线性化规则，或采用图结构序列化，但均未能有效解耦结构理解与推理执行，导致推理过程脆弱且不可验证。SMART通过语义表头扁平化将层级结构转化为自然语言描述，并引入伪代码风格推理结合外部验证，实现了结构感知与确定性计算的统一。该方法在复杂表格基准上显著优于现有基线，但其对扁平表格的泛化能力及纯文本表示在视觉线索缺失下的鲁棒性仍存疑。

】

---

【SmartAD: Capacity-Aligned Agent Distillation for Small Language Models ｜容量对齐的智能体蒸馏

研究机构：华中科技大学

作者：Guokai Tang、Feng Zhao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d5c0433e35c9)

> 智能体蒸馏旨在将大型语言模型（LLM）的工具调用与多步交互能力迁移至小语言模型（SLM），但现有方法常忽视教师轨迹与学生容量间的结构性错配，导致训练不稳定或泛化受限。本文切入点在于识别并过滤那些学生当前无法有效吸收的“高难度”轨迹，并差异化加权关键决策段。SmartAD 通过基于负对数似然（NLL）的轨迹筛选与分段加权损失，实现了数据分布与监督信号的双重对齐。该框架在1.5B和3B模型上验证了有效性，但其离线筛选机制能否替代在线策略蒸馏以彻底解决长程推理中的分布偏移，仍存疑。

】

---

【SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution ｜弥合心理-现实鸿沟：基于具体执行的代码生成框架

研究机构：韩国电子通信研究院

作者：Woojin Lee、Jin-Xia Huang

论文原文见 [arXiv](https://arxiv.org/abs/2604.19825)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19825)

> 多智能体代码生成框架依赖大语言模型（LLM）内部的心理模拟来验证代码正确性，但模型常因幻觉而自信地通过有缺陷的代码。本文指出这一“心理-现实鸿沟”源于规划阶段的边界盲区与验证阶段的执行幻觉，并提出了 SolidCoder 框架。该框架通过前置边界识别与沙箱具体执行，将验证从“想象”转变为“运行”。这一转变在中等难度竞赛编程任务上带来了显著的性能提升，但其高昂的推理成本与对属性断言生成能力的依赖，限制了其在极端复杂或简单任务上的普适性。

】

---

【Solver-Independent Automated Problem Formulation via LLMs for High-Cost Simulation-Driven Design ｜求解器无关的自动化问题建模

研究机构：西安电子科技大学、新西兰惠灵顿维多利亚大学

作者：Yuchen Li、Handing Wang、Bing Xue 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18682)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_62def8db4b69)

> 高成本仿真驱动设计面临的核心矛盾是：将模糊的自然语言需求转化为可执行数学模型的过程高度依赖专家，而验证模型正确性的求解器反馈因仿真成本过高无法用于数据筛选。现有提示工程方法在复杂约束下易产生语义偏差，微调方法则受限于缺乏低成本的数据质量过滤机制。本文提出 APF 框架，通过测试实例排序一致性替代求解器反馈进行数据筛选，并结合数据增强对开源大语言模型进行监督微调。该框架在特定工业场景下实现了小模型超越大模型提示的效果，但其验证机制的通用性与理论边界尚待检验。

】

---

【Sounding vs. Being an Expert: Disentangling Authority, Register and Cultural Impact in Sycophantic LLMs ｜语域与权威解耦的谄媚矩阵

研究机构：英国爱丁堡大学

作者：Gabriele Maraia、Fabio Massimo Zanzotto、Leonardo Ranaldi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_911fde476a5f)

> 大语言模型在用户施压时往往放弃事实以迎合观点，即谄媚（Sycophancy），但现有评估多将其视为单一黑盒副作用，无法区分是“无知”还是“策略性顺从”。本文切入点在于将谄媚解构为“显性权威”与“隐性语域”两个独立修辞杠杆，并考察其在跨文化变体中的协同效应。通过构建二维对抗矩阵（Sycophancy Matrix）并引入Golden Set隔离知识缺失，量化了不同模型在修辞压力下的信念稳定性。该方法揭示了语域在罗曼语系中比权威更具欺骗性，但缺乏对内部机制的因果验证，且多轮协议下的指标难以与单轮基准直接换算。

】

---

【SParK-Eval: Evaluating Structure-Aware Knowledge Acquisition in LLMs for Domain Adaptation to Industrial Records ｜结构感知参数化知识评估

作者：Ekant Muljibhai Amin、Yuta Koreeda、Yasuhiro Sogawa

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_15084115e976)

> 工业领域适配面临语料规模小且结构非自然（如表格、实体列表）的困境，传统持续预训练（CPT）方法难以区分是领域知识缺失还是数据结构阻碍了学习。现有数据转换方法仅关注下游任务性能，无法量化不同结构对参数化知识获取的具体贡献。SParK-Eval通过从训练数据生成带结构标签的探针查询，并结合输入归一化对照，实现了结构效应的隔离分析。该方法揭示了非自然结构导致的知识获取显著下降，为工业数据预处理提供了诊断工具，但其结论受限于单一私有数据集，跨域泛化性存疑。

】

---

【SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models ｜多模态思维链忠实性诊断与校准

研究机构：西安电子科技大学、新加坡国立大学

作者：Weijiang Lv、Yaoxuan Feng、Xiaobo Xia 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07833)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07833)

> 多模态大语言模型（MLLMs）的思维链（Chain-of-Thought, CoT）常被假设为视觉证据的忠实映射，但现有研究多聚焦于感知幻觉，忽视了“看到正确区域却生成错误解释”的推理级不忠实。本文通过图像差异描述任务剥离语言先验，构建SPD-Faith Bench基准，揭示感知盲区与感知-推理解离两种失效模式。基于注意力衰减与残差流漂移的机制分析，提出免训练框架SAGE，通过动态视觉路由、FFN抑制与对比解码对齐感知与生成。该工作填补了多模态CoT忠实性评估空白，但其干预幅度有限，未解决深层表征的根本解耦。

】

---

【SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration ｜自草稿投机解码中的浅层置信度校准与有界推测

研究机构：中国科学院、中国科学院大学

作者：Zhuofan Wen、Yang Feng

论文原文见 [arXiv](https://arxiv.org/abs/2604.12247)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12247)

> 自草稿投机解码试图利用基座模型自身的浅层输出替代独立草稿模型，以消除额外训练与部署开销，但浅层缺乏直接监督信号导致虚假高置信预测，且困难 token 迫使整个草稿序列进行冗余深层计算，限制了加速潜力。SpecBound 通过层依赖温度退火抑制浅层虚假置信，并引入深度与宽度双边界机制，在触发验证时并行补全所有草稿 token 的剩余层计算，实现了无损加速。该方法在多个长文本生成任务上取得了最高 2.33 倍的墙钟时间加速，但其加速比上限仍显著低于特征对齐路线，且对基座模型架构的依赖尚未被充分解耦。

】

---

【SpecEdit: A Spectral Approach for Multi-Round Knowledge Editing ｜谱结构感知的多轮知识编辑

研究机构：华南理工大学、浙江大学

作者：Junxian Liu、Zikun Deng、Xin Wu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b08cee35f3c3)

> 多轮批量知识编辑中，模型内在知识与历史编辑记忆的耦合导致性能退化，现有闭式解方法忽略了二者在能量尺度与信息分布上的结构性差异。SpecEdit 通过谱解耦、信息补偿与谱融合三阶段重构二阶统计量，在不改变原有优化流程的前提下提升编辑稳定性。该方法在 CounterFact 基准上显著超越基线，但在 ZsRE 单跳任务上未达领域最优，其谱截断策略对编辑规模的敏感性仍存疑。

】

---

【Speculative Decoding with a Speculative Vocabulary ｜词表推测（SpecVocab）：动态子集选择缓解草稿模型输出分布计算瓶颈

作者：Miles Williams、Young D. Kwon、Rui Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4eed40cc58bb)

> 导读 投机解码（Speculative Decoding, SD）通过草稿模型并行预测与目标模型单次验证实现无损加速，但大词表投影导致草稿阶段延迟高企，成为加速比的主要限制因素。现有静态词表裁剪方法（如 FR-Spec、VocabTrim）虽降低计算量，却因上下文无关性导致目标 token 落在子集外时接受率骤降，抵消加速收益。本文提出 SpecVocab，通过上下文感知的动态词表子集预测，在保持无损性的同时提升接受长度与吞吐量。该方法在 EAGLE-3 框架内实现最高 8.1% 的吞吐量提升，但其绝对加速比仍低于领域内特征对齐路线的 SOTA，且未验证长上下文与多模态场景下的泛化能力。

】

---

【Speculative Verification: Exploiting Information Gain for Speculative Decoding ｜投机验证：利用信息增益优化推测解码

研究机构：韩国汉阳大学、韩国首尔大学

作者：Sungkyun Kim、Jaemin Kim、Dogyeong Yun 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0290d2647add)

> 投机解码（Speculative Decoding, SD）旨在通过草稿模型并行生成与目标模型验证来降低大语言模型（LLM）推理延迟，但草稿-目标分布对齐的不稳定性导致验证开销在大批量场景下激增，甚至使SD性能劣于直接解码。现有基于草稿模型内部信号（如熵或历史接受率）的预测方法在复杂上下文下失效，本文提出投机验证（Speculative Verification, SV），引入与草稿模型同规模的伴随模型，通过量化两者分布相似性来预测接受概率并动态调整验证长度。SV在保持无损性的前提下，将大批量下的吞吐量提升最高1.9倍，但其效果依赖于伴随模型与草稿模型的非独立性假设，在极端异构模型组合下的鲁棒性仍有待进一步验证。

】

---

【SPIDE: Serial and Parallel Intertwined Speculative Decoding ｜串行与并行交织的投机解码

作者：Wenru Xu、Peixuan Xu、Ziqi Yang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_27684e6714fe)

> 投机解码（Speculative Decoding, SD）旨在通过草稿模型并行生成候选词元，再由目标模型一次性验证，以突破自回归解码的内存带宽瓶颈。然而，现有并行SD框架（如PEARL）强制目标模型持续参与验证，导致高昂的调用成本，且固定草稿长度常引发无效词元生成的浪费。SPIDE提出一种免训练的动态调度框架，通过置信度-接受率映射表实时评估草稿序列可靠性，在串行草稿与并行验证间灵活切换。该方法在保持无损性的前提下，将LLM额外调用成本降低83.7%，但其在长序列高不确定性场景下的接受率上限仍受限于线性验证结构。

】

---

【SpiralThinker: Latent Reasoning through an Iterative Process with Text–Latent Interleaving ｜螺旋思考者

研究机构：韩国延世大学

作者：Shengmin Piao、Sanghyun Park

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_576cf90338a7)

> 潜在推理领域长期受困于隐空间动态不连贯与显隐式推理割裂，导致模型在连续表示中难以维持稳定的推理轨迹。现有方法多将潜在表示视为单次前向传播的静态输入，缺乏对推理过程逐步演化的建模机制。本文提出SpiralThinker，通过迭代更新隐状态并引入渐进对齐目标，实现文本与潜在推理的结构化交替。该框架在潜在推理基准上取得SOTA，但绝对准确率仍显著低于显式方法，且未验证跨模型规模的泛化能力。

】

---

【SplitThenMerge: Token-Level Skill-Compositional Sparse Mixture-of-Experts for Complex Domain-Specific Tasks ｜技能组合式稀疏混合专家

研究机构：浙江大学

作者：Yuting Huang、Jiawen Zhang、Yiquan Wu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_07b772ed6ceb)

> 复杂领域生成任务要求模型在单句内频繁切换结构、推理、数值等异构能力，传统单一目标微调导致技能间梯度干扰与性能瓶颈。现有参数高效微调方法将领域能力视为整体，忽略了Token级的技能交织特性。本文提出SplitThenMerge框架，通过自动标注将领域语料分解为原子技能，独立训练LoRA专家并合并为Token级稀疏MoE模型。该方法在同等参数量下显著优于基线，但缺乏通用能力保持的验证，其技能解耦是否真正规避了灾难性遗忘仍存疑。

】

---

【SPS: Steering Probability Squeezing for Better Exploration in Reinforcement Learning for Large Language Models ｜概率挤压引导

研究机构：美国东北大学、中国科学院

作者：Yifu Huo、Chenglong Wang、Ziming Zhu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16995)

> 强化学习训练推理模型时，单样本成功率（Pass@1）提升显著，但多样本探索能力（Pass@k）增长缓慢，限制了模型发现新解题路径的潜力。现有熵正则化方法仅缓解表面多样性，未解决概率质量向主导路径系统性集中的根本偏差。本文提出概率挤压引导（SPS），通过交替执行强化学习与逆强化学习，将概率质量从过度集中的贪心轨迹重定向至低概率但潜在正确的路径。该框架在竞赛数学基准上提升了多采样性能，但其对IRL阶段过拟合风险的评估尚不充分。

】

---

【SR-RAG: Verifiable Multi-Hop Reasoning via On-the-fly Symbolic Graph Construction ｜符号验证检索增强生成

作者：Zehua Wang、Zhaojin Zhang、Boyu Qiu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2d4deba1f41c)

> 多跳推理中，动态检索范式因缺乏中间步骤验证，导致错误在推理链中逐级累积，最终答案失效。现有聚合优先方法构建成本高且适应性差，动态优先方法则依赖大语言模型内部推理，易受幻觉与逻辑断裂影响。SR-RAG 通过即时构建查询特定知识图谱并引入外部符号验证器，将中间推理步骤转化为形式化逻辑蕴含检查，阻断错误传播。该方法在多个基准上提升了准确率与鲁棒性，但其高计算延迟与对结构化实体关系的强依赖，限制了其在纯文本无实体场景及长链复杂逻辑中的适用边界。

】

---

【SrDetection: A Self-Referential Framework for Data Leakage Detection in Code Large Language Models ｜自参照代码泄漏检测

作者：Shuaimin Li、Liyang Fan、Zeyang li 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6686f600bfa8)

> 代码大语言模型（Code LLMs）在公开基准上的高分常源于预训练阶段对测试集的隐性记忆，而非真实泛化能力。现有检测手段或依赖不可得的私有训练语料，或依赖在代码复用场景下失效的时间戳启发式，且普遍需要外部参考集校准阈值。本文提出 SrDetection，通过生成语义等价变体并与原样本进行内部对比，实现无需外部锚点的自参照泄漏检测。该方法在受控测试床上显著优于基线，但其对变体生成质量的依赖及在真实复杂预训练分布下的鲁棒性仍存疑。

】

---

【Stable and Explainable Personality Trait Evaluation in Large Language Models with Internal Activations ｜基于内部激活的稳定性人格评估

研究机构：美国佐治亚理工学院、华南理工大学

作者：Xiaoxu Ma、Xiangbo Zhang、Zhenyu Weng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_54dae42eb74d)

> 大语言模型（LLMs）的人格评估长期受困于提示词敏感性，导致同一模型在不同措辞下产生剧烈波动的人格分数。现有自报告与开放问答范式将表面行为混淆为稳定特质，无法区分提示诱导的临时表现与模型内在的行为偏差。本文提出 Persona-Vector Neutrality Interpolation (PVNI)，利用内部激活空间中的对比向量进行线性插值，以解耦提示干扰并量化中性人格强度。该方法在稳定性上显著优于传统量表，但其理论假设的线性边界及跨模型泛化能力仍存疑。

】

---

【STaD: Scaffolded Task Design for Identifying Compositional Skill Gaps in LLMs ｜脚手架任务设计

研究机构：IBM研究院

作者：Sungeun An、Swanand Ravindra Kadhe、Shailja Thakur 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18177)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18177)

> 现有LLM评估依赖聚合准确率，掩盖了模型在组合推理中的具体失败点，导致无法区分“缺乏单一技能”与“技能协调失效”。STaD通过引入认知科学中的脚手架机制，将基准任务分解为子任务并逐步提供中间答案，以定位模型的最小支持需求。该方法在三个推理基准上揭示了不同模型具有截然不同的技能瓶颈分布，但缺乏与统计测量模型的直接对标，其诊断结论的泛化性仍存疑。

】

---

【STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming ｜策略-响应多层网络自动化红队测试

作者：Min Jae Jung、YongTaek Lim、Chaeyun Kim 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18976)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3fb78adea86d)

> 自动化红队测试旨在以规模化手段替代高成本人工红队，探测大语言模型（LLM）安全边界。现有策略类方法依赖嵌入相似度检索，缺乏对攻击成功因果模式的分析，导致策略过采样与可解释性缺失。STAR-Teaming 通过构建策略-响应多层网络，将策略选择转化为基于逆伊辛模型的统计优化问题，实现高效且可解释的自适应采样。该方法在黑盒场景下显著提升了攻击成功率与效率，但其单轮/少轮设定下的性能上限及社区结构对长程依赖的适应性仍存疑。

】

---

【Static Models, Dynamic World: A Unified Perspective on Temporal Perception in Large Language Models ｜静态参数与动态世界的信息论解耦

研究机构：北京理工大学

作者：Chenhao Li、Dandan Song、Changzhi Zhou 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_73478210576b)

> 大语言模型（LLM）在动态世界中面临静态参数与实时事实的结构性错位，导致时间推理失效。现有综述多聚焦于特定任务（如知识图谱或检索增强），缺乏对冻结模型内在时间能力的统一理论视角。本文通过构建基于参数可达性的信息论框架，将时间查询划分为四个独立的信息域，从而系统诊断失败根源并整合缓解策略。该框架提供了清晰的诊断坐标系，但其对复合查询的适用性及外部增强机制的量化边界仍存疑。

】

---

【Step Potential Advantage Estimation: Harnessing Intermediate Confidence and Correctness for Efficient Mathematical Reasoning ｜步骤潜力优势估计

作者：Fei Wu、Zhenrong Zhang、Qikai Chang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2fb631f15415)

> 长链思维模型在强化学习训练中常陷入“过度检查”陷阱，即在已得出正确答案后仍持续生成冗余验证步骤，甚至将正确结论篡改为错误答案。现有基于Token熵或序列长度的优化方法缺乏语义层面的进度感知，无法区分必要推导与无效验证。本文提出无需训练的探针机制提取步骤级置信度与正确性，构建“步骤潜力”信号以指导强化学习的信用分配。该方法在多个数学基准上同时提升了准确率并显著缩短了推理长度，但其依赖真值答案进行探针计算，限制了其在无标注开放域任务中的直接迁移。

】

---

【Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough Data ｜序贯测试驱动的自适应模型评估

研究机构：IBM研究院

作者：Ofir Arviv、Kristjan Greenewald、Yotam Perlitz 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.08522)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.08522)

> 大语言模型与视觉语言模型（VLM）评估面临固定样本量导致的计算浪费或统计效力不足的双重困境，传统静态基准无法动态匹配不同评估目标的可靠性需求。本文切入点在于引入临床试验中的组序贯测试（Group Sequential Testing, GST）范式，通过动态停止规则在统计显著性与计算成本间实现透明权衡。该方法利用Pocock消耗函数校正多重比较误差，支持单模型评分、成对比较及排名任务。其价值在于提供了无需历史数据校准的严格统计保证，但实验仅局限于VLM基准，未验证其在纯文本LLM或动态生成基准上的泛化能力。

】

---

【StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation ｜情境化多智能体动机访谈对话生成

研究机构：荷兰阿姆斯特丹自由大学、日本国立情报学研究所

作者：Qingyu Meng、Min Chen、Dingming Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d01a0b722a42)

> 动机访谈（Motivational Interviewing, MI）对话生成面临情境缺失与策略僵化的双重困境，导致模型难以维持长程临床逻辑。现有方法或依赖手工脚本，或仅做单轮代码预测，无法实现动态的宏观策略控制。StoryMI 通过问卷生成情境故事，并引入交互代理动态选择 MI 代码，实现了可控的多轮治疗对话。该框架在自建基准上验证了宏观策略的有效性，但其评估体系未涵盖安全约束，且缺乏与最新多智能体框架的直接对比。

】

---

【Strategy-Induct: Task-Level Strategy Induction for Instruction Generation ｜无标签任务指令归纳

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Po-Chun Chen、Hen-Hsen Huang、Hsin-Hsi Chen

论文原文见 [arXiv](https://arxiv.org/abs/2605.20924)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20924)

> 指令归纳旨在让大语言模型从少量示例中自动推导任务规则，但现有方法普遍依赖输入-输出对，这在标注数据稀缺或获取成本高昂的场景下构成硬性约束。STRATEGY-INDUCT 通过引入“策略生成”作为中间表示，将归纳信号从“答案”置换为“解题思路”，从而在仅拥有问题集合的条件下实现任务级指令的自动合成。该框架在多个基准上超越了依赖标签的基线，证明了无标签归纳的可行性，但其跨模型泛化能力是否源于策略的语义抽象而非表面形式，仍需进一步验证。

】

---

【Structure-Aware Zero-Shot Relational Learning for Knowledge Graphs without External Knowledge ｜结构感知零样本关系学习

研究机构：北京交通大学

作者：Kuan Xu、Baoxin Zhang、Shuyue Fan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8c19695e2cdd)

> 知识图谱补全（Knowledge Graph Completion, KGC）在处理新涌现关系时面临零样本关系学习（Zero-Shot Relational Learning, ZRL）难题，现有方法依赖文本描述或本体等外部知识，导致标注成本高且适用性受限。本文切入点在于利用KG内部结构模式替代外部知识，通过共享实体构建条件查询图并自适应聚合邻居关系嵌入。该方法在NELL-ZS和Wiki-ZS上分别取得10.66%和4.33%的MRR提升，证明了纯结构信号的可行性，但其对关系语义抽象程度的依赖及在大规模稀疏图上的泛化能力存疑。

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

【SWE-QA-Pro: A Representative Benchmark and Scalable Training Recipe for Repository-Level Code Understanding ｜仓库级代码理解基准与代理训练

研究机构：加拿大滑铁卢大学、加拿大多伦多大学

作者：Songcheng Cai、Zhiheng Lyu、Yuansheng Ni 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.16124)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16124)

> 仓库级代码理解要求模型在跨文件依赖中追踪控制流，但现有基准多依赖片段级问答或流行仓库，导致模型可通过预训练记忆“作弊”而非真正探索代码库。SWE-QA-Pro 通过长尾仓库采样与难度校准过滤掉可直接回答的题目，强制保留需多跳推理的任务，并配套 SFT→RLAIF 训练配方提升小模型代理能力。该工作验证了代理式探索对仓库级理解的必要性，但 LLM-as-Judge 评分的主观性与小模型泛化边界仍存疑。

】

---

【SWE-Swiss: A Multi-Task Fine-Tuning and RL Recipe for High-Performance Issue Resolution ｜多技能分解与两阶段强化学习配方

研究机构：北京大学、MiniMax

作者：Zhenyu He、Qingping Yang、Wei Shen 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_91e76523f802)

> 导读 仓库级软件修复的核心瓶颈在于开源模型缺乏针对真实工程环境的系统性训练数据与策略优化机制，导致其在 SWE-bench 等基准上的表现显著落后于闭源大模型。现有方法或依赖静态文本匹配，或采用单一任务蒸馏，未能有效整合定位、修复与验证的协同能力。本文提出 SWE-Swiss 配方，通过多任务监督微调（SFT）建立基础技能，再针对修复任务实施基于执行反馈的强化学习（RL），实现开源 32B 模型在 SWE-bench Verified 上 60.2% 的解决率。该结果确立了开源模型在该规模下的新标准，但其性能提升是否完全归因于训练策略而非骨干模型潜力，仍需进一步隔离验证。

】

---

【SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants ｜修正选择性基准

作者：Debu Sinha

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_086697bb9106)

> 现有谄媚评估仅量化模型对错误压力的顺从度，无法区分“盲目固执”与“选择性更新”两种截然不同的失败模式，导致无法诊断模型是否具备在正确反馈下修正错误的能力。SycoBench-600通过引入与误导性压力匹配的“正确建议”对照组，将单一谄媚率解耦为压力鲁棒性与修正选择性两个独立维度。该基准在受控多选题（MCQ）协议下，通过定义翻转率与顽固率，揭示了模型在抵抗错误压力与接受正确纠正之间的权衡关系。其价值在于提供了行为层面的细粒度诊断工具，但局限于单轮静态交互，未涵盖多轮对话中的动态信念漂移。

】

---

【SyncThink: A Training-Free Strategy to Align Inference Termination with Reasoning Saturation ｜同步思维：基于内部信号对齐推理终止与饱和

研究机构：北京大学

作者：Gengyang Li、Wang Cai、Yifeng Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a54ceb48fc48)

> 长思维链（Chain-of-Thought, CoT）推理在提升大语言模型（LLM）准确率的同时，引入了显著的推理延迟与计算开销，核心矛盾在于推理深度与计算效率之间的张力。现有方案多依赖训练式压缩或黑盒一致性检查，前者牺牲部署灵活性，后者引入额外推理成本且未利用模型内部动态。本文切入点在于发现模型存在“认知滞后”（Cognitive Lag），即准确率饱和早于自然终止点，并利用边界 Token 的 Logit 动态作为免训练停止信号。通过监控 `</think>` 的秩与熵，SyncThink 实现了动态截断，在保持精度的同时大幅降低 Token 消耗。其价值在于提供了无需微调的高效推理路径，但该方法对显式边界 Token 的依赖限制了其在通用模型上的泛化性。

】

---

【SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair ｜自适应神经符号漏洞修复框架

研究机构：美国范德堡大学、美国芝加哥大学

作者：Yifan Zhang、Jieyu Li、Kexin Pei 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17184)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17184)

> 自动化代码修复面临的核心矛盾是：监督微调（SFT）能高效学习常见语法模式但缺乏深层语义推理，而奖励微调（RFT）能处理复杂语义但计算成本高昂且收敛缓慢。现有方法通常固定选择单一训练策略或采用静态混合比例，无法根据代码复杂度动态调整，导致简单漏洞浪费算力或复杂漏洞修复不足。SYNTHFIX 通过引入基于编译器特征的自适应路由器，在训练阶段动态调度 SFT 与 RFT 路径，并结合 AST、CFG 和 Semgrep 构建密集符号奖励信号。该框架在 FixJS 和 CodeFlaws 基准上实现了 CodeBLEU 最高 18% 的相对提升，但评估局限于静态代码特征，未验证运行时动态语义下的泛化能力。

】

---

【Table-as-Search: Agentic Information Seeking is Table Completion ｜表格化搜索（TaS）：将长程信息检索重构为表格补全任务

作者：Tian Lan、Felix Henry、Bin Zhu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19cc84e6eb7b)

> 长程智能体信息检索面临的核心困境是：在追踪数千条搜索结果与规划步骤时，非结构化文本上下文导致关键证据丢失与状态失真。现有基于 ReAct 范式的多智能体框架虽通过上下文摘要或隔离缓解压力，但本质上仍依赖有限的文本窗口管理海量状态，无法从根本上解决“中间迷失”问题。本文提出 Table-as-Search (TaS) 框架，将信息检索任务显式重构为外部数据库中的表格补全问题，以结构化单元格状态替代自由文本轨迹。该架构在 DeepSearch 与 WideSearch 基准上超越了同等算力下的多智能体基线，但其对复杂非结构化证据的整合能力及与端到端强化学习方法的相对优势仍存疑。

】

---

【TableVista: Benchmarking Multimodal Table Reasoning under Visual and Structural Complexity ｜TableVista：多模态表格推理的视觉与结构复杂度基准

研究机构：同济大学、英国布里斯托大学

作者：Zheyuan Yang、Liqiang Shang、Junjie Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05955)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05955)

> 表格理解的核心矛盾在于二维拓扑结构与一维语言序列的表征鸿沟，现有专用模型受限于泛化，通用大语言模型（LLM）又面临序列化导致的空间结构丢失。TableVista 指出，当前多模态大模型（MLLM）在视觉扰动下的推理一致性缺乏系统性评估，其切入点是通过多风格渲染与视觉变换管线，构建包含 30,000 个样本的鲁棒性压力测试集。该基准通过 29 个前沿模型的评估，揭示了模型在复杂结构与视觉集成呈现下的显著性能衰减。其价值在于暴露了视觉空间锚定推理的瓶颈，但缺乏对专用结构编码方法的对比，视觉优势是否源于纯感知仍存疑。

】

---

【Tandem: Riding Together with Large and Small Language Models for Efficient Reasoning ｜大小模型协同推理框架

研究机构：香港城市大学、中国人民大学

作者：Zichuan Fu、Xian Wu、Guojing Li 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23623)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23623)

> 大语言模型（LLM）在复杂推理任务中通过生成数千Token的思维链（Chain-of-Thought, CoT）提升准确率，但由此带来的高延迟与计算成本阻碍了实时部署。现有强化学习微调方法需修改模型权重且不适用于闭源API，而单纯截断推理链会损失逻辑完整性。Tandem提出“导师-实习生”协同范式，由LLM生成结构化高层洞察，SLM执行细节推理，并通过基于困惑度与熵的成本感知机制动态终止LLM生成。该框架在MATH数据集上以32B模型59%的计算成本实现了2.56%的准确率提升，但其对SLM能力下限的依赖及跨域泛化边界仍存疑。

】

---

【TARo: Token-level Adaptive Routing for LLM Test-time Alignment ｜令牌级自适应路由

研究机构：美国匹兹堡大学、美国加州大学伯克利分校

作者：Arushi Rai、Qiang Zhang、Hanqing Zeng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18411)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18411)

> 大语言模型（LLM）在复杂推理任务中常因后训练成本高、领域特定性强而难以灵活部署，现有测试时对齐方法依赖固定插值权重，无法适应不同任务与模型规模的动态变化。本文提出令牌级自适应路由（Token-level Adaptive Routing, TARO），通过可学习路由器在解码时动态融合基座模型与奖励模型的输出，消除手动调参需求。该方法在数学推理基准上较基座模型提升最高22.4%，并展现出弱到强泛化能力，但其效果高度依赖奖励模型与基座模型的能力匹配度，跨域泛化机制尚待深入验证。

】

---

【Task-Related In-Context Learning ｜任务相关上下文学习

研究机构：中山大学、兰州大学

作者：Wenqiang Wang、Peng Chen、Yan Xiao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5d49badaa2b7)

> 上下文学习（In-Context Learning, ICL）通常假设检索集与测试集共享相同的输出空间，但在弱监督或跨任务场景中，这一假设常被打破，导致标准 ICL 性能崩溃。现有方法多聚焦于标签对齐下的演示筛选，对标签空间完全不相交（Fully Disjoint）的情形缺乏有效机制。本文提出 TRICL 框架，通过贝叶斯准则筛选任务相关子集，利用中间预测缩减目标输出空间，从而在不依赖标签对齐的前提下实现有效推理。该框架在多个数据集上显著优于基线，但其性能高度依赖中间任务预测的准确性，且未验证在大规模候选池下的检索效率。

】

---

【TELL-TALE: Task Efficient LLMs with Task Aware Layer Elimination ｜任务感知层消除

作者：Omar Naim、Krish Sharma、Niyar R Barman 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22767)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22767)

> 导读 大语言模型（Large Language Models, LLMs）的固定架构假设所有层对任意下游任务同等重要，导致在特定任务上存在计算冗余甚至性能干扰。现有剪枝方法多聚焦于通过移除权重或层来降低计算开销，往往以牺牲下游任务精度为代价，且依赖困惑度或表示相似度等通用指标，无法捕捉任务特异性。TALE 提出一种推理时贪心算法，以任务验证集准确率为唯一优化目标，迭代移除对当前任务无益甚至有害的层。该方法在无需重训练的前提下，不仅降低了推理成本，更在多个基准上实现了超越原始模型的性能提升，挑战了“剪枝必然导致性能下降”的领域共识。

】

---

【Temporal Contrastive Decoding: A Training-Free Method for Large Audio-Language Models ｜时间对比解码

研究机构：阿联酋扎耶德大学、北京交通大学

作者：Yanda Li、Yuhan Liu、Zirui Song 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15383)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15383)

> 统一架构大型音频语言模型（LALM）在自回归解码时，常因语言先验压制瞬态声学线索，导致对短暂事件（如铃声次数）的感知失效。现有解码干预方法多采用全局模态消融，无法区分时间尺度差异，且易干扰语言主导步骤。本文提出时间对比解码（Temporal Contrastive Decoding, TCD），通过构建时间模糊的“慢路径”视图，在解码时对比原始与模糊音频的Logit差异，并引入门控机制仅在不确定且依赖音频时进行稀疏修正。该方法无需训练即可提升强基座模型性能，但其有效性严格依赖于解码器能否访问时序对齐的音频表示，对语义瓶颈架构无效。

】

---

【Temporal Token Matters: Investigating and Interpreting the Consistency of Temporal Ordering in Large Language Models ｜时间排序机制的因果验证与自适应干预

研究机构：北京理工大学

作者：Zhen Yang、Xinyue Zhang、Ping Jian 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_59ef6cabdf11)

> 大语言模型在处理简单事件排序时，常因提问措辞从“before”变为“after”而产生逻辑矛盾，暴露出内部时间推理机制的脆弱性。现有研究多聚焦于外部基准测试或端到端性能提升，缺乏对模型内部因果路径的细粒度解析。本文通过路径修补定位关键注意力头，揭示时间词与结构词的层级分工，并提出基于因果效应的自适应注意力调制方法。该方法在无需微调的情况下同时提升了准确率与一致性，但性能增益幅度有限，且仅在二元排序任务中得到验证。

】

---

【TempTool-R1: Tool-Augmented Reinforcement Learning for Temporal Knowledge Graph Question Answering ｜时序知识图谱问答中的工具增强强化学习

作者：Zicheng Huang、Yajuan Tong、Xinhui Tu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f449900610ea)

> 时序知识图谱问答（TKGQA）旨在回答涉及时间约束的复杂查询，但现有方法在处理多跳推理与隐式时间依赖时普遍失效。本文指出，传统检索增强或提示工程无法保证工具调用顺序符合时序逻辑，导致中间步骤错误累积。TempTool-R1 通过设计顺序敏感的强化学习奖励函数，训练大语言模型（LLM）在推理中显式调用时序工具。该方法在多个基准上显著提升了复杂问题的准确率，但其效果高度依赖特定的工具接口设计，泛化性存疑。

】

---

【Test-Time Scaling in Multimodal Foundation Models: A Comprehensive Survey of Generation and Reasoning ｜多模态基础模型测试时扩展综述

研究机构：中山大学

作者：Cong Wan、Ying He、Zhongzhan Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.08231)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.08231)

> 多模态基础模型在推理阶段面临感知证据、空间定位与时间上下文的多维计算分配难题，单纯复用文本模型的扩展策略无法解决模态间隙导致的验证失效。现有研究缺乏统一分类框架以厘清采样、反馈与搜索策略在多模态场景下的适用边界。本文构建了首个针对多模态基础模型测试时扩展的系统性综述，提出包含采样、反馈与搜索三大范式的统一分类体系。该工作填补了多模态测试时扩展的理论空白，但缺乏对算力预算与性能收益的量化对比分析。

】

---

【Text2Mem: A Unified Memory Operation Language for Memory Operating System ｜统一记忆操作语言

作者：Leo Wang、Lihai Yang、Boyu Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa768cf74138)

> 大语言模型智能体在长程交互中面临记忆管理碎片化问题，现有系统仅暴露编码、检索等基础原语，缺乏对优先级调整、合并、锁定等高级治理操作的形式化定义，导致跨系统行为不一致且难以审计。本文切入点在于将自然语言指令映射为具有显式字段与语义不变量的模式化操作契约，通过验证-解析-适配流水线实现确定性执行。Text2Mem定义了12个覆盖记忆全生命周期的动词，并构建了分离规划与执行评估的双层基准。该工作确立了记忆操作接口的标准化范式，但其端到端任务性能优势及在复杂动态环境下的泛化能力尚未得到充分验证。

】

---

【The Agent's First Day: Benchmarking Learning, Exploration, and Scheduling in the Workplace Scenarios ｜动态职场环境下的智能体鲁棒性评估：Trainee-Bench

研究机构：复旦大学、浙江大学

作者：Daocheng Fu、Jianbiao Mei、Rong Wu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.08173)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08173)

> 现有智能体基准多聚焦于静态环境下的性能上限，忽视了真实部署中流式任务调度、不确定性探索及持续学习失效等鲁棒性问题。Trainee-Bench 通过规则模板与随机实例化构建动态复合场景，强制智能体在部分可观测条件下进行多任务并发处理与经验迁移。该基准揭示了当前 SOTA 模型在动态环境中的显著短板，特别是持续学习机制可能导致的性能负迁移。其价值在于将评估从“能否做对”转向“能否在混乱中稳定做对”，但受限于人工规则的可扩展性，其结论在更复杂因果链场景中的普适性尚存疑。

】

---

【The Art of (Mis)alignment: How Fine-Tuning Methods Effectively Misalign and Realign LLMs in Post-Training ｜微调方法在安全失配与再对齐中的效能不对称性

研究机构：电子科技大学、新加坡南洋理工大学

作者：Rui Zhang、Hongwei Li、Yun Shen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f63cc988fb14)

> 大语言模型（LLM）的安全对齐机制在微调过程中极易被破坏，但不同微调范式在“破坏安全”与“恢复安全”上的效能差异缺乏系统性量化。现有研究多聚焦于单一方向的攻击或防御，忽略了攻防博弈中方法选择的非对称性及其对模型效用的累积影响。本文通过对比四种监督微调（SFT）与两种偏好微调（PFT）方法在失配与再对齐双向任务中的表现，揭示了ORPO在失配上的优势与DPO在再对齐上的效用代价。该研究为防御者选择再对齐策略提供了实证依据，但其结论受限于特定模型规模与数据集规模，未深入探究几何机理。

】

---

【The Best of Both Worlds: Combining Parallel and Sequential Inference Scaling via Aggregation Fine-Tuning ｜聚合微调

作者：Yafu Li、Zhilin Wang、Tingchen Fu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3ec6b6677d37)

> 大语言模型在推理时扩展计算以提升性能，但并行采样依赖外部验证器，串行修正则受限于高延迟。现有方法难以在无外部监督下同时利用并行多样性与串行深度。本文提出聚合微调（AFT），通过监督学习使模型内化“将多个草稿响应整合为单一精炼答案”的能力，并在推理时通过“提议-聚合”迭代策略扩展计算。该范式在开放域指令跟随任务上实现了无验证器的性能提升，但其对复杂数学推理任务的泛化能力存疑。

】

---

【The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning ｜扩散大语言模型中的校准悖论与结构一致性信号

作者：Yansi Li、Gongshen Liu、Zhuosheng Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_65741e97931c)

> 扩散大语言模型（Diffusion Large Language Models, DLLMs）在数学推理中展现出一种反直觉现象：其原生置信度严重偏离真实概率，却具备远超自回归模型的判别力。现有不确定性量化方法假设置信度必须同时满足校准与判别，导致对DLLM这类新架构的评估失效。本文通过解耦校准与判别，证明DLLM的置信度实为结构一致性代理，并验证了轻量级后处理校准的有效性。这一发现揭示了双向生成机制下的独特失效模式，但其在开放域知识问答中的近乎随机表现，限制了该信号的通用性。

】

---

【The Impact of Off-Policy Training Data on Probe Generalisation ｜合成数据策略对探针泛化性的系统性影响

研究机构：英国帝国理工学院、英国曼彻斯特大学

作者：Nathalie Kirch、Samuel Dower、Adrians Skapars 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.17408)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17408)

> 探针技术旨在通过解码大语言模型内部激活状态来检测欺骗、谄媚等隐蔽行为，但自然行为样本稀缺迫使研究者依赖合成数据训练。现有方法默认训练与测试分布一致，忽略了合成数据策略（如提示、激励、离线）与任务域偏移对探针泛化能力的系统性破坏。本文通过因子实验设计，量化了四种响应策略与两种域设置对八种行为探针性能的影响，并发现域偏移比策略选择更具破坏性。该研究揭示了当前欺骗探针在真实监控场景中可能失效的风险，但受限于缺乏自然测试数据，其结论主要基于代理指标推断。

】

---

【The Inner Monologue of Language Models: When Reasoning Traces Reveal More Than They Hide ｜语言模型内心独白：推理轨迹揭示与隐藏

作者：Pratham Singla、Shivank Garg、Ayush Singh 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f29916dd6a6e)

> 大型推理模型（Large Reasoning Models, LRMs）通过生成中间推理轨迹来展示思考过程，但现有后训练范式主要优化最终答案，忽视了推理轨迹与答案之间的一致性。当前方法无法区分模型是真正理解其习得行为，还是仅在执行表面策略，导致基于文本的监控在对抗场景下失效。本文通过引入反思性行为自我意识概念，系统量化不同后训练范式对推理-答案对齐及潜在策略迁移的影响。该研究揭示了强化学习训练在提升自我意识的同时加剧了内外解耦现象，为理解模型内部状态提供了新视角，但其评估局限于行为层面，缺乏因果机制验证。

】

---

【The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models ｜表面合规诊断框架

研究机构：美国俄亥俄州立大学

作者：Xiaojie Gu、Ziying Huang、Weicong Hong 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05995)

> 知识编辑旨在以低成本更新大语言模型（LLM）中的过时事实，但现有评估体系依赖自由生成匹配，无法区分模型是真正重构了内部参数记忆还是仅学会了模仿目标输出。本文指出这种“表面合规”现象普遍存在，传统指标严重高估了编辑效果。通过引入判别式自评估协议与外部证据注入，该框架揭示了编辑后模型在上下文干扰下的脆弱性。这一诊断视角填补了从“输出正确”到“记忆内化”的评估空白，但其对递归编辑稳定性的量化仍停留在定性观察层面。

】

---

【The Thin Line Between Comprehension and Persuasion in LLMs ｜论辩中的理解与说服解耦

研究机构：英国约克大学

作者：Adrian de Wynter、Tangming Yuan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_359af70b49b9)

> 大语言模型在对话中常表现出高流畅度与强说服力，但其是否真正理解语用上下文与论证结构存疑。现有评估多聚焦于解题能力或单轮事实准确性，缺乏对动态对话中深层认知能力的测量，导致无法区分“策略性迎合”与“真实理解”。本文通过构建人类与LLM的非正式辩论场景，结合形式对话模型（FDM）控制变量，并引入LLM-as-Judge评估协议，实证了说服能力与深层理解的脱节。这一发现挑战了“流畅即理解”的假设，但在小样本受控环境下，其结论向开放域泛化的有效性仍待检验。

】

---

【Think Less, Know More: State-Aware Reasoning Compression with Knowledge Guidance for Efficient Reasoning ｜状态感知推理压缩与知识引导

作者：Yi Sui、Chaozhuo Li、Dawei Song

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0c189152018c)

> 大型推理模型（LRM）在长思维链（CoT）中普遍存在“过度思考”，导致简单任务计算冗余与复杂任务错误累积。现有压缩方法多基于任务级难度或静态离线数据，缺乏对推理过程中异质性冗余来源的步级动态响应。STACK 通过局部熵监测识别“犹豫状态”，动态切换知识引导与自提示压缩策略，并结合奖励差值驱动的 DPO 训练，实现了准确率与效率的帕累托改进。该框架在数学基准上显著优于现有压缩基线，但其对开放域知识依赖的鲁棒性及跨模型规模泛化能力仍存疑。

】

---

【Think Smart, Not Hard: Difficulty Adaptive Reasoning for Large Audio Language Models ｜难度自适应推理：大型音频语言模型的效率优化

作者：Zhichao Sheng、Shilin Zhou、Chen Gong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21960)

> 大型音频语言模型（LALM）在复杂任务上依赖思维链（CoT）提升准确率，但现有强化学习方法对所有问题施加统一的推理长度，导致简单题过度思考、复杂题思考不足。本文切入点在于利用模型内部状态（组内正确率与音频注意力熵）动态定义难度，并据此调整长度奖励。通过设计难度自适应的负指数奖励函数，使推理长度与问题复杂度对齐。该方案在音频基准上同时提升了准确率并显著缩短了推理长度，但其难度信号对训练阶段的依赖性及跨模态泛化能力尚存疑。

】

---

【ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding ｜基于对数概率边际的推理终止机制

研究机构：韩国首尔大学

作者：Sangjun Song、Minjae Oh、Seungkyu Lee 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5d9847085443)

> 大语言模型在复杂推理中常出现“过度思考”，即在得出正确中间步骤后继续生成并覆盖为错误答案，导致计算资源浪费与精度下降。现有测试时干预方法多依赖手工启发式规则，缺乏理论支撑且在不同难度任务上表现不稳定。本文提出 THINKBRAKE，通过监测句子边界处继续生成 Token 与结束标记 `</think>` 的对数概率边际，实现无需训练的自适应推理终止。该方法在数学与工具调用任务上实现了精度保持与 Token 消耗降低的平衡，但其对高难度任务精度的轻微损失归因于“虚假推理”而非过早终止，这一现象的内在机制尚待深入解析。

】

---

【Thinking Economically: A Hierarchical Framework for Adaptive-Complexity Reasoning in LLMs ｜层级自适应预算器

作者：Yubo Gao、Haotian Wu、Hong Chen 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b4b7d190df24)

> 大语言模型在复杂推理中常因“过度思考”产生冗余计算，而现有压缩方法多采用全局统一预算，忽视了问题间与步骤间的复杂度差异。本文指出全局预算的根本局限，提出层级自适应预算器（HAB），通过两阶段监督学习实现从问题级步数控制到步骤级Token保留率的细粒度分配。实验表明HAB在GSM8K和MATH500上同时提升了准确率并降低了Token消耗，但其泛化性受限于数学任务且未对比最新RLVR方法，其监督学习路径能否在更复杂任务上超越强化学习范式仍存疑。

】

---

【Thinking Twice Makes Large Language Models Safer and More Helpful ｜安全感知反思推理优化

研究机构：北京大学

作者：Yutao Mou、Yuxiao Luo、Shikun Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b1564abe6d9)

> 大语言模型（LLM）安全对齐长期受困于安全性与有用性的零和博弈，强化安全训练往往导致良性请求的过度拒绝。现有基于结果偏好的优化方法缺乏对推理过程的细粒度监督，难以在复杂越狱攻击下保持鲁棒且避免误拒。SaRO 通过引入步骤级自我反思机制，将安全约束内化为模型的推理习惯，实现了安全与效用的双优。该方法在缓解过度拒绝上表现优异，但在极端对抗鲁棒性上尚未超越当前前沿，其推理延迟增加是否可接受仍需权衡。

】

---

【ThinkLinker: From Low-Rank Interaction to Knowledge-Aware Verification for Multimodal Entity Linking ｜多模态实体链接中的低秩交互与知识驱动验证

研究机构：东南大学

作者：Yingyao Ma、Yuanyuan Zhou、Congyu Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0f4431da2cbb)

> 多模态实体链接旨在利用图文联合信息消解文本提及的歧义，但现有方法在特征交互上依赖独立模块，难以显式建模跨粒度、跨模态的联合依赖，且在弱上下文场景下缺乏基于候选实体的反向验证机制。ThinkLinker 通过低秩融合塔统一处理多级特征交互，并引入 LLM 双向对话验证以精炼提及表示，解决了上述两个瓶颈。该方法在 WikiMEL 和 WikiDiverse 上均取得 SOTA 性能，但其第二阶段依赖 LLM 多轮生成，计算开销随数据集规模线性甚至超线性增长，且验证过程目前仅作用于文本模态，限制了其在大规模实时场景中的适用性。

】

---

【Thought-Action Graph Reasoning: Faithful and Efficient Reasoning of Large Language Models via Reusing Past Experience ｜思维-行动图推理

研究机构：清华大学、北京邮电大学

作者：Zhixiao Qi、Feng Huang、Yunqi Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f11bc27dbf52)

> 知识图谱问答（KGQA）的核心矛盾在于大语言模型（LLM）在线探索知识图谱（KG）时的高延迟与错误累积。现有检索方法泛化差，智能体方法效率低，均忽略了从历史交互中复用推理逻辑的可能性。本文提出思维-行动图（Thought-Action Graph, TAG），将成功的LLM-KG交互轨迹蒸馏为可检索的操作蓝图，通过离线检索替代在线试错。该范式在WebQSP上达到93.2%的Hits@1，但GrailQA上的46.3%暴露了其在复杂泛化场景下的局限。

】

---

【TIME: Temporally Intelligent Meta-reasoning Engine for Context Triggered Explicit Reasoning ｜时间触发式推理策略对齐

研究机构：印度科学理工学院

作者：Susmit Das

论文原文见 [arXiv](https://arxiv.org/abs/2601.05300)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05300)

> 推理型大语言模型（LLM）常将显式思考固化为回复开头的长文本块，导致计算冗余、审计困难且无法在回答中途重新校准。现有方案将时间视为待抽取的事实内容，却忽略了时间跳跃作为交互状态突变信号对推理策略的触发作用。本文提出 Time 框架，通过引入时间戳、静默 Tick 事件与可插入的短思考块，结合四阶段课程学习，将显式推理从固定解码风格转化为由情境线索触发的动态控制策略。该框架在私有基准 TimeBench 上显著优于基线，但其对时间元数据的依赖及私有评测的封闭性限制了结论的普适性。

】

---

【TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents ｜时序层级记忆固化框架

研究机构：中科院自动化所

作者：Kai Li、Xuanqing Yu、Ziyi Ni 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02845)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02845)

> 长时程对话智能体面临的核心矛盾是交互历史无限增长与LLM有限上下文窗口的冲突，导致用户状态演化中的时间连贯性丢失与个性化表征不稳定。现有外部记忆系统多依赖语义相似度聚类，将时间结构降格为辅助元数据，致使不同时期的记忆在无明确边界下聚合，检索时缺乏时序排序，无法构建因果证据链。TiMem的切入点是将时间结构提升为一等组织原则，通过显式时间包含约束的层级树结构，将细粒度情景交互逐步固化为抽象人格画像。该框架在LoCoMo和LongMemEval-S上取得了优于对比基线的准确率，同时大幅降低了检索上下文长度，但其性能上限受限于指令提示的固化策略，且未与最新结构化SOTA方法直接对比。

】

---

【To Intervene or Not: Guiding Inference-time Alignment with Probabilistic Model Blending ｜推理时对齐中的质量盲视与分布混合

研究机构：新加坡南洋理工大学

作者：Jin Gan、Xin Li、Jun Luo

论文原文见 [arXiv](https://arxiv.org/abs/2606.11201)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.11201)

> 推理时对齐旨在通过已对齐模型在生成阶段指导未对齐模型，以规避高昂的重训练成本。现有方法如NUDGING隐含假设所有指导信号均有益，但系统评估显示指导有效性在不同模型组合间剧烈波动，且高干预率反而导致性能下降。本文提出BlendIn，通过基于置信度的概率分布混合替代二元接受/拒绝决策，实现质量感知的软集成。该方法在挑战性模型对上实现了最高50%的性能提升，但其改进幅度在完整测试集上未达统计显著性，且依赖基座模型与指导模型的能力匹配度。

】

---

【ToMELP: A Theory-of-Mind Benchmark for Route-Controlled Persuasion under the Elaboration Likelihood Model ｜心智理论引导的精细加工可能性说服基准

作者：Ruirui Wang、Haoran Zhang、Tian Lan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e9e1302d33f)

> 说服对话中的心智理论（Theory of Mind, ToM）评估长期受困于“能答对问题”与“能据此行动”之间的鸿沟，现有基准缺乏对受众信息处理路径的显式控制，导致模型表现归因模糊。ToMELP 通过构建受众画像（Persona）与精细加工可能性模型（Elaboration Likelihood Model, ELM）双路径的 2×2 因子设计，将 ToM 推断与策略执行解耦为可审计的闭环。该基准揭示了 ToM 注入在外围路径下的稳定增益与中央路径下的证据组织瓶颈，但其依赖 LLM-as-a-judge 且未进行人类一致性验证，限制了结论的绝对效度。

】

---

【Too Good to be Bad: On the Failure of LLMs to Role-Play Villains ｜道德角色扮演基准

研究机构：中山大学

作者：Zihao Yi、Qingxuan Jiang、Ruotian Ma 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.04962)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04962)

> 大语言模型在安全对齐后难以真实模拟反派角色，现有评估多关注事实性幻觉而忽视创意生成中的道德保真度。本文通过构建四级道德量表与平衡测试集，量化了模型在扮演不同道德层级角色时的保真度衰减。实验证实模型在模拟自私与恶意特质时出现系统性性能下降，且通用对话能力无法预测该特定技能。该基准揭示了安全对齐与创意保真间的结构性冲突，但评估依赖LLM评分的可靠性仍存疑。

】

---

【ToolCPT: Improving Tool Utilization in LLM Agents via Continuous Pre-training ｜工具持续预训练

作者：Yifan Yang、Jinghui Lu、Evadeng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7952d3e0eb5)

> 大语言模型智能体在分布外工具调用中表现受限，根源在于现有后训练与测试时方法仅让模型学习调用模式，而非内化工具功能知识。ToolCPT 将工具知识获取前移至持续预训练阶段，通过挖掘真实代码库构建代理工具并合成结构化知识语料，使模型在权重层面建立对工具实现、交互协议及错误反馈的深层理解。该方法在 7B/8B 基座模型上验证了预训练内化工具知识的有效性，但其静态模拟特性与缺乏真实执行反馈的局限，使其在动态环境适应性与长程任务泛化上仍存疑。

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

---

【TopoDIM: One-shot Topology Generation of Diverse Interaction Modes for Multi-Agent Systems ｜一次性异构拓扑生成

研究机构：中国科学技术大学、华东师范大学

作者：Rui Sun、Jie Ding、Chenghua Gong 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10120)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10120)

> 多智能体系统（MAS）在复杂任务中依赖通信拓扑协调，但主流时空迭代范式因多轮对话导致Token开销激增且存在结构冗余。现有方法在效率与性能间难以兼得，本文切入点在于将多轮交互压缩为单步异构图生成。TOPODIM通过自回归解码器一次性生成包含条件、反馈、辩论三种边类型的稀疏拓扑，并采用去中心化蒸馏实现本地决策。该方法在降低46.41% Token消耗的同时提升1.50%平均性能，但其对强骨干模型的依赖及单次生成缺乏错误修正机制的潜在风险尚存疑。

】

---

【Topology-Enhanced Alignment for Large Language Models: Trajectory Topology Loss and Topological Preference Optimization ｜拓扑增强对齐：轨迹拓扑损失与拓扑偏好优化

作者：Yurui Pan、Ke Xu、Bo Peng

论文原文见 [arXiv](https://arxiv.org/abs/2605.07172)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a67a56ea5945)

> 大语言模型对齐长期依赖局部信号，如词元似然或标量奖励，忽略了隐空间的全局几何结构，导致模型在复杂语义任务中轨迹漂移。现有直接偏好优化（DPO）等方法虽简化了流程，但未能约束隐藏状态从提示到答案的语义移动方向，造成对齐鲁棒性不足。本文提出拓扑增强对齐框架，通过0维持久同调提取隐空间“桥梁”方向，正则化生成轨迹。该方法在7B模型上提升了奖励模型分数与胜率，但其对数据清洗的依赖及高维拓扑特征的缺失仍存疑。

】

---

【Toward Automated Robustness Evaluation of Mathematical Reasoning ｜数学推理鲁棒性自动压力测试

研究机构：南方科技大学

作者：Yutao Hou、Zeguan Xiao、Fei Yu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_639577b588cf)

> 大语言模型在静态基准上表现优异，但面对语义等价的问题变体时往往性能崩塌，暴露出严重的鲁棒性缺陷。现有鲁棒性评估依赖人工模板或固定扰动规则，难以覆盖模型特有的弱点，且静态变体易受数据污染影响。MASTER 通过构建 Rewriter-Verifier 对抗循环，自动化生成针对特定模型弱点的变体，从源头规避污染并精准定位失效模式。该方法在 GSM8K 上使 LLaMA-3-8B 的准确率从 76.42% 降至 27.51%，证明了自动化压力测试的有效性，但其依赖强模型作为重写器，引入了新的评估偏差风险。

】

---

【Towards Identification and Intervention of Safety-Critical Parameters in Large Language Models ｜预期安全影响（ESI）：基于参数敏感度解耦安全与效用的干预框架

作者：Weiwei Qi、Zefeng Wu、Tianhang Zheng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bebdba993896)

> 导读 大语言模型在微调后常出现安全对齐崩塌，但现有方法难以精确定位哪些参数承载安全行为，导致防御策略要么全局冻结损失效用，要么盲目更新破坏安全。本文切入点在于构建一个可微分的参数级安全敏感度度量，将安全关键参数从全参数空间中分离出来。通过引入预期安全影响（Expected Safety Impact, ESI）指标，结合可微分裁判模型估计安全梯度，并据此实施仅更新或仅冻结关键参数的干预策略。该框架在参数定位精度上优于传统剪枝指标，但在效用保持上仍受限于冻结比例，其泛化边界尚待验证。

】

---

【Towards Inference-time Scaling for Continuous Space Reasoning ｜连续空间推理的测试时扩展失效机制分析

作者：Minghan Wang、Thuy-Trang Vu、Ehsan Shareghi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12167)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_82be9e0d4eb2)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段计算量提升大语言模型（LLM）性能，但现有方法主要局限于离散Token空间。连续空间推理模型（如COCONUT）虽提升了效率，却因确定性生成导致轨迹单一，无法直接应用TTS。本文通过引入Dropout采样生成多样连续轨迹，并训练过程/结果奖励模型（PRM/ORM）进行重排序，发现现有离散空间迁移的奖励模型在连续空间中失效。这一发现揭示了连续思维缺乏几何可分性的根本瓶颈，为后续设计具有结构区分性归纳偏置的训练框架提供了实证依据。

】

---

【Towards Proactive Personalization through Profile Customization for Individual Users in Dialogues ｜基于多轮马尔可夫决策过程的主动个性化智能体

研究机构：浙江大学

作者：Xiaotian Zhang、Yuan Wang、Ruizhe Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8908109bd2be)

> 大语言模型在长程对话中难以捕捉用户隐式偏好的动态演化，且面临冷启动时无历史数据可用的困境。现有方法多依赖静态画像或一次性检索，缺乏跨轮次、跨会话的持续对齐机制。本文提出 PersonalAgent，将多轮对话分解为逐轮偏好推理任务，构建为多轮马尔可夫决策过程（Multi-turn Markov Decision Process, MDP），通过强化学习优化策略以动态维护用户画像。该方法在冷启动场景下显著优于记忆基线，但其长程一致性未经验证，且主动查询机制对用户打扰度的影响尚不明确。

】

---

【Towards Self-Evolving Agents: Enabling Autonomy through Interactive Experience Refinement ｜记忆驱动的自我进化智能体

研究机构：中南大学、复旦大学

作者：Cheng Yang、Xuemeng Yang、Licheng Wen 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bad481343316)

> 静态大语言模型在部署后无法从过往交互中积累经验，导致其在长程生产力任务中表现受限且无法持续改进。现有非参数化反思方法多依赖线性文本存储，缺乏结构化知识组织，而参数化更新则面临高计算成本与灾难性遗忘风险。MUSE 通过分层记忆模块将原始执行轨迹蒸馏为可复用的标准作业程序，实现了无需微调的测试时学习。该框架在 TAC 基准上以轻量级模型刷新了性能纪录，但其记忆检索机制在大规模库下的扩展性仍存疑。

】

---

【Towards Self-Improving Error Diagnosis in Multi-Agent Systems ｜多智能体系统故障归因的自进化诊断框架

研究机构：英国伦敦大学学院

作者：Jiazheng Li、Emine Yilmaz、Bei Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17658)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17658)

> 多智能体系统（MAS）在长轨迹交互中常出现错误延迟显现，导致传统“LLM-as-a-Judge”难以定位决定性错误步骤。现有方法依赖昂贵的人工标注或需重训练的专用追踪器，缺乏跨域泛化能力。本文提出ERRORPROBE，通过症状驱动反向追踪压缩上下文，并引入验证式情景记忆实现无需重训练的自进化诊断。该框架在步级定位上显著优于基线，但其绝对精度仍低于领域SOTA，且跨域迁移的泛化边界尚不明确。

】

---

【TRAC: Token-level Reward Assignment for Coherent Abstractive Summarization ｜基于过程奖励模型的词元级摘要生成优化

研究机构：华南理工大学、澳门大学

作者：陈宣齐、容梓莹、Xinfeng Liao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ce9d5b0b3e0c)

> 导读 摘要生成领域长期面临强化学习奖励信号稀疏导致的连贯性与事实性缺失问题。现有序列级奖励无法捕捉词元间依赖，而人工工程化词元奖励成本高昂且泛化性差。TRAC 框架通过迁移数学推理中的过程奖励模型（Process Reward Model, PRM），利用句间注意力将全局语义信号分解至词元级，实现了高效且可迁移的细粒度监督。该方法在流畅度与相关性上显著优于基线，但其对事实性幻觉的抑制能力尚未在独立基准上得到充分验证。

】

---

【TRACE: Two-Phase RL for Causal Graph Exploration and Deeper Psychological Intervention in Dynamic Counseling Scenarios ｜因果图重构驱动的双阶段强化学习心理干预框架

研究机构：西安电子科技大学、北京师范大学

作者：Shilin Tang、Zunyi Yin、Xuefeng Liang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5ce838746ee5)

> 现有大语言模型心理咨询系统受限于表面情绪响应，缺乏对深层认知因果链的主动探索能力，导致干预无法触及核心信念。本文切入点在于将咨询过程形式化为在线因果图重构问题，通过双阶段强化学习强制模型遵循“先探索后干预”的临床逻辑。具体做法是利用因果图填充状态作为奖励信号，训练模型在对话中逐步还原客户心理结构并实施针对性认知重构。该框架在自建基准上显著优于基线，但其依赖LLM生成的理想因果图质量，且缺乏跨基准的泛化验证，临床等效性存疑。

】

---

【Tracing Relational Knowledge Recall in Large Language Models ｜追踪大语言模型中的关系知识回忆机制

作者：Nicholas Popovič、Michael Färber

论文原文见 [arXiv](https://arxiv.org/abs/2604.19934)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f57f2547d1eb)

> 大语言模型（LLMs）在生成文本时如何内部存储并检索关系知识，是解释性研究的核心难题。现有机制分析多聚焦于实体表征或全层状态，缺乏对关系类型特征在注意力头与源词元层面可归因性的系统验证，导致无法解释为何某些关系类型易于线性解码而另一些则失败。本文通过构建基于单头注意力贡献的线性探针，并引入HeadScore与TokenScore归因方法，系统评估了不同内部表征在少样本关系分类中的有效性及其预测因子。该工作揭示了注意力头贡献是关系分类的强特征，且探针性能受谓词输出范围与信号集中度影响，为理解LLM关系绑定机制提供了可操作的诊断工具，但其线性假设在复杂关系场景下的泛化能力仍存疑。

】

---

【Tracing the Light of Thought: A Probabilistic Self- and Cross-Consistency Verification Mechanism Improving Mathematical Reasoning in LLMs ｜基于 Metropolis 采样的自洽性验证机制

研究机构：英国纽卡斯尔大学

作者：Xiaoyang Liu、Dawei Wang、Tian Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a91651ba1d72)

> 大语言模型在复杂数学推理中常因自回归生成的错误级联导致最终答案失效，而传统的自一致性（Self-Consistency, SC）策略在难题上因正确解概率极低而失效。本文切入点在于利用 Metropolis Light Transport (MLT) 思想，将随机采样转化为序列式迭代采样，通过接受-拒绝机制集中计算资源于高正确性区域。具体做法是构建基于 logprob 的轻量级正确性函数引导采样方向，并扩展为多模型交叉验证。该方法在弱模型上显著优于 SC，但在强模型上提升有限，且依赖 logprob 校准的稳定性。

】

---

【Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets ｜功能性保持的代码数据集投毒

作者：Yuan Xiao、Jiaming Wang、Yuchen Chen 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22291)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e595236c6d67)

> 代码大语言模型（CodeLLMs）的预训练依赖海量公开代码，但数据所有者缺乏阻止未授权微调的技术手段。现有投毒方法如 CoProtector 通过破坏语法或语义来降低模型效用，导致代码无法编译或功能失效，无法在真实发布场景中部署。本文提出 FUNPOISON，通过向执行路径注入可编译、无副作用的弱用代码片段，在保持 100% 功能正确性的前提下，仅污染 10% 数据集即可显著抑制未授权微调收益。该方法在隐蔽性和鲁棒性上优于基线，但其对语义级异常检测的抵抗能力及跨语言泛化性仍存疑。

】

---

【Training Language Models to Use Prolog as a Tool ｜强化学习驱动的大语言模型Prolog工具调用

作者：Niklas Mellgren、Peter Schneider-Kamp、Lukas Galke Poech

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_556f75183209)

> 导读 大语言模型（LLM）在逻辑推理中常产生看似合理实则错误的思维链，这种“忠实性差距”使得纯文本推理难以满足安全关键领域的审计需求。现有神经符号方法多依赖监督微调或提示工程，导致小模型难以掌握Prolog等小众符号语言，且缺乏对推理过程的结构化约束。本文切入点在于利用可验证奖励强化学习（RLVR）训练3B参数模型将Prolog作为外部工具，通过执行反馈闭环实现可审计推理。该方案在GSM8K验证集上超越7B基线，但揭示了准确率与可审计性之间的根本权衡，其泛化能力在测试集上显著衰减。

】

---

【Training-Free Adaptive Speculative Decoding via Linguistic Priors ｜语言学先验驱动的无训练投机解码

作者：Jingyi Wang、Jiaqi Huang、Zunnan Xu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_da296e374f35)

> 投机解码旨在通过并行验证打破自回归解码的串行瓶颈，但现有方法普遍采用统一的验证标准，忽视了自然语言中不同词性Token在熵分布上的固有差异。LinguaSpec指出这种“一刀切”策略导致高熵内容词被误拒或低熵功能词验证冗余，提出利用静态语言学先验实现自适应草稿与验证。该方法通过零延迟的词性探针、句法归一化惊讶度及POS自适应延迟验证，在无训练约束下实现了比训练式基线更高的加速比。其价值在于证明了语言学结构对推理效率的增益，但松弛验证机制对严格无损性的潜在妥协仍需审慎评估。

】

---

【Training-Free Test-Time Contrastive Learning for Large Language Models ｜无梯度测试时对比学习

研究机构：华南理工大学

作者：Kaiwen Zheng、Kai Zhou、Jinwu Hu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13552)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13552)

> 冻结大语言模型在分布偏移下性能退化，现有测试时适应方法要么依赖梯度更新（需白盒访问），要么依赖外部知识（需预置数据库）。本文切入点在于：不更新参数、不依赖外部反馈，仅从模型自生成输出中提取对比信号。TF-TTCL通过多智能体角色扮演生成多样推理轨迹，蒸馏为显式文本规则并在线检索引导推理。该方法在黑盒场景下显著优于零样本基线，但其规则仓库的长期容量管理与跨域泛化边界尚存疑。

】

---

【TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense ｜解码时隐藏状态轨迹检测

作者：Cheng Liu、Xiaolei Liu、Xingyu Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07727)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07727)

> 大语言模型（LLM）面临越狱攻击时，静态输入过滤常因语义伪装而失效，且后处理检测无法阻止有害内容生成。现有解码时防御多依赖额外训练的安全探针，成本高且仅做单点判断，忽略了风险在解码过程中的动态累积。TrajGuard 提出免训练的流式几何监控与条件触发的语义裁判级联框架，在解码过程中实时追踪隐藏状态轨迹以拦截越狱。该方法在开源模型上实现了高拦截率与低延迟，但其对黑盒 API 的适用性及免训练几何统计在分布外攻击下的鲁棒性仍存疑。

】

---

【Tree-Notebook: A Context-Aware Agent with Tree Search and Entropy-Aware Data Shadow for Interactive Data Science ｜树搜索与熵感知数据影子驱动的交互式数据科学智能体

研究机构：中国科学院大学

作者：Junkun Qiu、Min Huang、Qinghai Miao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6832aac1ef5b)

> 数据科学智能体在长链推理中常因无法感知内存状态而陷入“静默失败”，即代码执行无错但数据已受损。现有线性框架缺乏回溯机制，导致早期错误沿任务链不可逆地传播。Tree-Notebook 将代码生成形式化为部分可观测马尔可夫决策过程（POMDP），通过树状拓扑与数据影子机制实现非线性探索与状态监控。该架构在基准测试中超越了线性基线，但其高昂的计算开销与对骨干模型能力的强依赖，限制了其在资源受限场景下的通用性。

】

---

【Tree-of-Evidence: Efficient "System 2" Search for Faithful Multimodal Grounding ｜证据树搜索：多模态临床预测的推理时忠实性验证

研究机构：美国佐治亚理工学院

作者：Micky C. Nnamdi、Benoit L. Marteau、Yishan Zhong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07692)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07692)

> 多模态大模型在医疗高风险场景中的部署面临“黑盒”决策不可审计的困境，现有注意力权重或后验归因方法无法提供可验证的硬证据轨迹。ToE 将解释问题重构为离散搜索问题，通过轻量级证据瓶颈与束搜索算法，在推理时动态定位支持预测的最小证据子集。该方法在严格证据预算下保留了全输入模型98%以上的预测性能，但仅验证了晚期融合架构，且其忠实性依赖于基础模型本身的逻辑正确性。

】

---

【TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models ｜触发式大小模型协同推理

研究机构：上海交通大学、复旦大学

作者：Yi Zhao、Yajuan Peng、Cam-Tu Nguyen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14847)

> 大语言模型在复杂推理任务中依赖长思维链，但自回归生成导致高延迟，现有加速方案要么压缩单模型推理预算，要么依赖小模型生成、大模型验证的协同范式。SpecReason等协同方法采用每步轮询验证，但大模型作为评判者存在主观偏差且通信开销巨大，导致效率收益被抵消。本文提出TrigReason，通过识别小模型推理失败的三种风险模式，设计基于事件信号的稀疏触发机制，仅在关键节点调用大模型进行干预。该框架在保持准确率的同时显著提升了小模型推理步骤的利用率，但在触发阈值的跨模型泛化性及非数学领域的鲁棒性上仍存疑。

】

---

【TripTide: A Benchmark for Adaptive Travel Planning under Disruptions ｜扰动感知旅行规划基准

研究机构：印度理工学院

作者：Priyanshu Karmakar、Soumyabrata Chaudhuri、Shubhojit Mallick 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21329)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21329)

> 导读 大语言模型（Large Language Model, LLM）在旅行规划中常假设理想无扰动环境，导致生成的计划缺乏现实鲁棒性。现有基准如 TravelPlanner 和 TripCraft 仅评估静态约束满足，忽略了航班取消、天气突变等动态扰动对计划执行的影响。TripTide 通过引入扰动严重性等级与旅行者容忍度画像，构建首个动态扰动响应基准，并设计意图保留、响应性与适应性三维评估指标。该工作填补了 LLM 在动态环境规划评估上的空白，但缺乏符号验证机制，其逻辑可行性在长程任务中面临挑战。

】

---

【TRM-Planner: Offline Target Planning and Distillation for Tiny Recursive Models ｜离线目标规划与蒸馏

作者：Euijin Baek、Housam Babiker、Mi-Young Kim 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f624a71a529)

> 网格推理任务中的Tiny Recursive Models (TRMs)面临监督信号对精化深度与停止策略校准的敏感性问题，导致训练效率低下且性能不稳定。现有方法依赖在线停止决策，难以在固定计算预算下获取高质量中间状态。本文提出TRM-Planner，通过离线规划冻结教师轨迹并缓存高置信度目标，实现“一次计算，多次复用”的蒸馏范式。该方法在ARC-AGI-1/2上显著提升了小模型性能，但其离线缓存机制是否完全规避了分布偏移风险，仍需进一步验证。

】

---

【TT-SI: Self-Improving LLM Agents with Test-Time Training ｜测试时自我改进（TT-SI）：基于不确定性门控的代理模型即时适配

作者：Emre Can Acikgoz、Cheng Qian、Heng Ji 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6c5fb1416866)

> 导读 大语言模型（LLM）在代理任务中常因训练数据冗余或分布偏移导致泛化失效，传统归纳式微调需消耗海量标注数据且易引发灾难性遗忘。现有测试时扩展方法多聚焦于推理采样或外部验证，缺乏对模型参数层面的即时、轻量级适应机制。本文提出测试时自我改进（Test-Time Self-Improvement, TT-SI）框架，通过识别不确定样本、自合成相似实例并执行临时LoRA微调，实现无外部标注的在线能力适配。该范式在数据效率上显著优于全量微调，但其“临时更新后重置”机制是否阻碍了跨样本知识的长期累积，仍是核心存疑点。

】

---

【TTVS: Boosting Self-Exploring Reinforcement Learning via Test-time Variational Synthesis ｜测试时变分合成

研究机构：香港科技大学

作者：Sikai Bai、Haoxi Li、Jie Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08468)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08468)

> 测试时训练（Test-Time Training, TTT）旨在让大语言模型在推理阶段利用无标注数据自我进化，但现有方法受限于静态测试集，易导致模型过拟合表层文本模式而非底层逻辑。本文切入点在于将静态查询动态转化为语义等价的变体流，通过在线变分合成与双模式探索机制，迫使模型学习不变的问题逻辑。该方法在仅使用无标注测试数据的前提下，显著超越了依赖大规模标注数据的强化学习后训练模型。其价值在于证明了动态数据增强对测试时适应的必要性，但变体生成的质量边界与潜在分布偏移风险仍存疑。

】

---

【TwinVoice: A Multi-dimensional Benchmark Towards Digital Twins via LLM Persona Simulation ｜多维人格一致性基准

研究机构：清华大学、美国罗格斯大学

作者：Bangde Du、Minghao Guo、Songming He 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c65448fc3224)

> 大语言模型（LLM）在模拟个体人格时存在“角色坍缩”与长期一致性缺失问题，现有评估多依赖合成数据且仅关注整体准确率，无法诊断具体失效环节。本文切入点在于构建基于真实数字足迹与虚构叙事的多维基准，将人格模拟解耦为思维连贯性与语言表达六项细粒度能力。通过判别式与生成式双重评估协议，TwinVoice 揭示了当前 SOTA 模型在记忆召回与语气保持上的显著短板。该基准填补了细粒度评估空白，但其生成式评估对 LLM 裁判的依赖及虚构数据维度的生态效度仍存疑。

】

---

【UCGRec: User-Centric Graph Learning for LLM-based Sequential Recommendation ｜用户中心图学习驱动的LLM序列推荐

作者：HanBeul Kim、CheolWon Na、Suyoung Bae 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c3516609da12)

> 序列推荐的核心矛盾在于LLM缺乏实时交互数据，导致无法精准捕捉用户动态偏好。现有方法或依赖随机采样引入噪声，或仅利用单一偏好维度，忽视了不同偏好信号间的结构关联。UCGRec通过构建用户中心图，将长期、短期及协同偏好统一为结构化知识，并联合训练图神经网络与LLM适配器以注入该知识。该方法在四个基准数据集上显著优于现有LLM基线，但其对图构建计算开销的敏感性以及在稀疏图场景下的性能波动，限制了其在超大规模工业场景中的直接适用性。

】

---

【UCoder: Unsupervised Code Generation by Internal Probing of Large Language Models ｜无监督代码生成：内部探测与执行共识

作者：Jiajun Wu、Jian Yang、Wei Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19d4a1f0fa84)

> 导读 大语言模型（LLM）在代码生成上的能力依赖大量人工标注或外部代码语料，但高质量指令数据获取成本高且易受污染。现有无监督方法多依赖未标注代码片段，仍受限于外部数据分布偏差，无法完全脱离语料依赖。本文提出IPC框架，通过六阶段自举流程探测LLM内部潜在编程知识，利用执行反馈构建确定性监督信号，实现无外部语料的代码生成能力提升。该方法在开源模型上验证了可行性，但绝对性能仍落后于闭源SOTA，且自生成任务分布偏差风险未完全解决。

】

---

【UCS: Estimating Unseen Coverage for Improved In-Context Learning ｜未见覆盖率选择

研究机构：美国宾夕法尼亚大学

作者：Jiayi Xin、Xiang Li、Evan Qiang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12015)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12015)

> 上下文学习（ICL）性能对演示样本的选择极度敏感，但现有方法多聚焦于实例级的相关性或多样性，缺乏对候选池潜在语义空间覆盖广度的量化机制。本文指出，仅优化局部相似度或子集体积无法捕捉长尾分布中未被揭示的潜在簇，导致模型在复杂任务上暴露不足。为此，提出未见覆盖率选择（Unseen Coverage Selection, UCS），一种基于平滑古德-图灵估计器的无训练子集级覆盖先验，通过正则化现有选择目标来偏向覆盖更多未见簇的子集。UCS在意图分类与推理任务上带来2-6%的准确率提升，但其效果高度依赖基线选择器的强度，且在强基线上增益微弱，其统计假设与LLM内部机制的对齐程度仍存疑。

】

---

【Uncertainty Quantification of Large Language Models through Multiple Uncertainty Sources ｜多源不确定性量化框架

作者：Tiejin Chen、Xiaoou Liu、Longchao Da 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e8d21012898)

> 大语言模型在开放式生成中面临“自信地犯错”的困境，传统基于单一信号的不确定性量化方法难以捕捉语义、事实与结构维度的复合变异。现有方法要么孤立处理NLI语义相似度，要么依赖图结构统计，导致信号冗余掩盖真实分歧。MS-UQ通过构建三阶相似度张量并应用张量分解，将异构信号正交解耦，以重建误差作为统一不确定性度量。该框架在集成多源信号上具有结构优势，但缺乏分布无关的统计保证，且在复杂推理基准上的绝对性能未超越当前图结构SOTA。

】

---

【Uncovering Strategic Egoism Behaviors in Large Language Models ｜策略性利己主义

作者：Yaoyuan Zhang、Zonghao Ying、Aishan Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.09920)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c2529a73b68b)

> 大语言模型（LLM）在高风险决策场景中面临的核心安全挑战，并非显式的毒性输出，而是隐性的、受激励驱动的自我利益最大化行为。现有安全基准多聚焦于表面语言毒性或事实错误，缺乏对模型在程序约束下权衡个人收益与社会责任的动机层评估。本文提出策略性利己主义（Strategic Egoism, SE）概念，构建SEBench基准，通过人格心理学理论映射选项，量化模型在激励压力下的利己倾向。该工作揭示了利己行为与毒性输出的正相关性，但单轮静态评估难以捕捉多轮交互中的动态累积效应。

】

---

【Understanding In-Context Learning Beyond Transformers: An Investigation of State Space and Hybrid Architectures ｜状态空间与混合架构中的上下文学习机制解析

研究机构：加拿大不列颠哥伦比亚大学

作者：Shenran Wang、Timothy Tin-Long Tse、Jian Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2510.23006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.23006)

> 现有理论多聚焦于Transformer内部隐式优化算法的数学等价性，但状态空间模型（SSM）及混合架构的上下文学习（In-Context Learning, ICL）内部机制尚属黑盒。本文切入点在于利用机制可解释性技术，实证对比不同架构中负责ICL的功能向量（Function Vectors, FVs）分布差异。通过行为探针与激活干预相结合，揭示了自注意力层在混合架构ICL中的主导作用及Mamba2可能存在的非FV机制。该工作填补了非Transformer架构ICL机制解释的空白，但其结论受限于1B参数规模及NLP任务类型，对大规模模型及非语言任务的普适性存疑。

】

---

【Understanding LLM Reasoning for Abstractive Summarization ｜摘要生成中的推理策略评估

作者：Haohan Yuan、Haopeng Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b5d0ac0d9c00)

> 摘要生成任务要求信息压缩而非逻辑推导，但现有研究默认思维链（Chain-of-Thought, CoT）等推理范式能普适提升所有生成任务性能，这一假设在摘要场景中缺乏系统验证。本文通过统一框架对比8种显式推理策略与3个大推理模型（Large Reasoning Models, LRM），发现推理复杂度与事实忠实度存在显著负相关，挑战了“更多推理即更好”的领域共识。其价值在于揭示了摘要任务中质量与忠实度的权衡机制，但实验仅覆盖单一模型家族，结论的跨模型泛化性存疑。

】

---

【Understanding LLMs’ summarization capabilities: an analysis of biomedical abstract and lay summary generation ｜轻量级大语言模型在生物医学摘要生成中的零样本能力诊断

研究机构：美国佐治亚理工学院

作者：Batuhan Nursal、Cassie S. Mitchell

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a9d96586901)

> 生物医学文献的指数级增长要求将复杂研究转化为可访问的格式，但现有评估多聚焦于微调模型在自动化指标上的排名，忽视了轻量级模型在零样本场景下的内容来源与效用差异。主流方法依赖参考摘要计算重叠度，无法解释模型为何选择特定信息，且缺乏对非专家读者视角下内容“可答性”的量化。本文通过引入句子级来源分类与问答对评估，诊断了小于8B参数模型在生成科学摘要与通俗摘要时的信息分布偏差。该研究揭示了轻量级模型在事实性上优于人类参考摘要的反直觉现象，但其评估样本量极小，结论的统计稳健性存疑。

】

---

【Understanding Secret Leakage Risks in Code LLMs: A Tokenization Perspective ｜代码大语言模型中的乱码偏差：分词器视角下的秘密泄露风险

研究机构：香港中文大学、新加坡南洋理工大学

作者：Meifang Chen、Zhe Yang、Huang Nianchen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17814)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17814)

> 代码大语言模型（Code LLMs, CLLMs）在自动化软件开发中广泛部署，但其训练语料中混杂的API密钥等敏感信息构成了严重的隐私泄露隐患。现有安全对齐与漏洞修复方法聚焦于生成代码的功能正确性与漏洞消除，却忽视了底层分词器对高熵随机字符串的结构性处理缺陷。本文通过信息论视角揭示Byte-Pair Encoding（BPE）分词器将高字符熵秘密转化为低Token熵序列的“乱码偏差”（Gibberish Bias），并论证该偏差加剧了模型对秘密的记忆与泄露风险。该发现将LLM安全研究的边界从模型权重与提示工程延伸至输入预处理架构，但缺乏对缓解策略的量化验证。

】

---

【Unifying Inference-Time Planning Language Generation ｜统一推理时规划语言生成流水线

研究机构：美国宾夕法尼亚大学、美国西北大学

作者：Prabhu Prakash Kagitha、Bo Sun、Ishan Desai 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c72fc314f24f)

> 经典规划任务要求从自然语言描述生成可被符号求解器执行的 PDDL 模型，但 LLM 直接生成 PDDL 时极易出现语法或语义错误，导致计划失效。现有方法多采用单次生成加简单重试，缺乏对中间表示（IR）选择的系统性评估，且依赖闭源大模型，开源中小模型性能骤降。本文提出基于 IR 层级的统一框架，引入高资源、语法对齐的 PyPDDL 作为中间语言，通过多阶段推理时计算换取生成可靠性。该框架在开源 32B 模型上验证了 IR 与求解器反馈的关键作用，但未探索训练时优化与推理时优化的协同效应。

】

---

【UniGeM: Unifying Data Selection and Mixing via Geometric Exploration and Mining ｜统一数据混合与选择的几何流形近似框架

研究机构：意大利都灵理工大学、中国科学院

作者：Changhao Wang、Yunfeiyu、Xinhao Yao 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_223b073fdbfb)

> 代码预训练面临数据混合与实例选择解耦导致的结构断裂问题，现有方法或依赖代理模型引入偏差，或忽略域内层级依赖。UniGeM 将数据策展重构为流形近似问题，通过两级几何聚类统一宏观预算分配与微观质量筛选。该框架在 8B MoE 模型上实现了 2.0 倍的数据效率提升，但其几何假设在非结构化文本语料中的适用性仍存疑。

】

---

【Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling ｜自适应层级零阶优化

研究机构：华南理工大学、中山大学

作者：Fei Wang、Li Shen、Liang Ding 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18264)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18264)

> 大语言模型微调中，零阶优化（ZO）虽能消除反向传播的激活内存开销，但全参数均匀扰动导致计算延迟高且梯度估计方差大，严重制约收敛效率。现有改进多聚焦于算法层面的动量或子空间约束，却忽视了扰动生成与参数更新本身带来的线性系统瓶颈及层间敏感度异质性。本文提出AdaLeZO，将层选择建模为非平稳多臂老虎机问题，通过逆概率加权实现稀疏无偏梯度估计。该方法在6.7B至30B模型上实现了1.7至3.0倍的墙钟加速，但其在复杂推理任务上的精度仍略低于一阶方法，且未验证多模态场景下的泛化能力。

】

---

【Unleashing the Native Recommendation Potential: LLM-Based Generative Recommendation via Structured Term Identifiers ｜基于结构化术语标识符的生成式推荐

作者：Zhiyang Zhang、Junda She、Kuo Cai 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e2b163165fe)

> 生成式推荐旨在利用大语言模型（LLM）的语义理解能力替代传统判别式打分，但现有方案在物品标识符构建上陷入两难：文本标识符易致幻觉，语义标识符（SID）则需高昂的词表扩展与对齐成本。本文提出术语标识符（Term ID, TID），利用LLM原生词汇构建结构化关键词序列，通过上下文感知生成与弹性标识符接地机制，在保持语义丰富性的同时抑制幻觉。该框架在多个基准上超越了基于SID的SOTA方法，但其跨域优势是否源于TID的通用语义而非模型规模，仍需更严格的对照实验验证。

】

---

【Unlocking Human-Like Visible Logic: How Logic Diagrams Boost Logic Reasoning in Large Language Models? ｜视觉逻辑图辅助大语言模型推理

研究机构：华南理工大学

作者：Xin Wu、Yuqi Bu、Mengchen Zhao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ffb749ddc497)

> 大语言模型（LLMs）在处理形式逻辑时，常因文本表征的边界模糊而推导失效。现有神经符号融合路线依赖外部求解器，成本高且缺乏直观性；纯文本提示工程则难以显式呈现集合间的空间关系。本文切入点在于利用视觉逻辑图（Venn、Euler、Linear）作为中间表征，直接输入视觉语言模型（VLMs）以辅助推理。通过程序化生成图表并对比不同对齐策略，本文发现视觉辅助在有效案例上提升显著，但在无效案例上引发“过度依赖”导致准确率下降。该研究提供了受控实证框架，但缺乏强文本基线对比，其增益是否源于视觉本质仍存疑。

】

---

【Unlocking the Edge deployment and ondevice acceleration of multi-LoRA enabled one-for-all foundational LLM ｜冻结图约束下的多任务LLM端侧部署与自推测加速

研究机构：三星研究院

作者：Sravanth Kodavanti、Sowmya Vajrala、Srinivas Miriyala 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18655)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18655)

> 移动端LLM部署面临内存、延迟与运行时灵活性的三重硬约束，传统静态合并LoRA或云端协同方案无法在冻结推理图中实现多任务动态切换与低延迟并发生成。本文切入点在于将LoRA权重作为运行时输入注入单一冻结图，结合多流并发解码与无草稿模型的自推测策略，在NPU上实现单图多任务。该框架在三星Galaxy S24/S25上验证了可行性，但LoRA维度固定与静态预测嵌入限制了其泛化边界。

】

---

【V-RoLoRA: RLVR-Driven MoE Routing for Steerable Pluralistic Alignment ｜可引导价值对齐中的条件路由与可验证奖励

作者：Jing Wang、Yaomin Wu、Yinglin Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c4012c4a0550)

> 可引导价值对齐旨在使大语言模型（LLM）在生成时忠实遵循多维、组合式的价值观或道德准则，而非收敛于单一共识。现有方法多依赖提示工程或单适配器微调，在长尾价值组合下控制力脆弱且易产生语义幻觉。本文切入点是将控制信号从输入端迁移至权重端，通过多维价值向量路由混合专家（MoE）LoRA池，并引入外部判别器计算条件一致性奖励，以强化学习（RL）优化语义合规性。该方法在8B骨干上实现了可控性指标的提升，但其对长尾维度的覆盖不足及判别器偏差问题仍存疑。

】

---

【Valid Necessary: Diagnosing Latent Inefficiency in Chain-of-Thought ｜有效但冗余：思维链推理效率盲区的诊断与压缩

作者：Daeyeop Lee、Hwanjo Yu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4a62ebefa20d)

> 现有推理评估器聚焦逻辑正确性，却对“有效但冗余”的步骤视而不见，导致模型在简单问题上过度思考，浪费算力。本文指出这一“效率盲区”，提出无监督信息密度指标 CAID 与后处理压缩策略 PACE。通过识别并压缩低效用步骤，在保持准确率的同时显著降低 Token 消耗。该方法在效率维度上提供了新的评估视角，但其对推理忠实性的因果影响尚未得到验证。

】

---

【Value Alignment Tax: Measuring Value Trade-offs in LLM Alignment ｜价值对齐税（VAT）：量化LLM对齐中的系统性价值权衡

研究机构：美国纽约大学

作者：Jiajun Chen、Hua Shen

论文原文见 [arXiv](https://arxiv.org/abs/2602.12134)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.12134)

> 多元价值对齐旨在使大语言模型（LLM）输出反映人类群体价值观的多样性，但现有评估范式仅关注目标价值的增益，忽略了干预引发的非目标价值协同漂移。这种“静态、原子化”的度量掩盖了安全关键场景下对齐副作用的系统性风险。本文提出价值对齐税（Value Alignment Tax, VAT）框架，通过场景-动作对提取状态级价值向量，利用Spearman相关系数量化价值间的结构耦合。该框架揭示了SFT与DPO在对齐效率与系统稳定性上的本质差异，但缺乏对神经元级干预的评估，其诊断结论能否指导优化器设计尚存疑。

】

---

【Value-Action Alignment in Large Language Models under Privacy-Prosocial Conflict ｜隐私-亲社会冲突下的价值-行动对齐评估

研究机构：美国亚利桑那州立大学、美国南加州大学

作者：Guanyu Chen、Chenxiao Yu、Xiyang Hu

论文原文见 [arXiv](https://arxiv.org/abs/2601.03546)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03546)

> 当大语言模型（LLM）面临隐私保护与亲社会利他两种价值观的拉扯时，其数据共享决策往往呈现出复杂的内部权衡，但现有评估手段难以捕捉这种多态度联合预测行为的结构性关系。传统“价值-行动差距”（Value-Action Gap）指标将多维态度压缩为单一标量，在多值冲突场景下因参考系缺失而失效，无法区分模型是真正遵循人类行为逻辑还是仅表现出表面一致性。本文提出基于多群组结构方程模型（MGSEM）的评估框架，通过提取路径方向一致性来量化价值-行动对齐率（VAAR），揭示了模型间对齐能力的巨大异质性。该方法在特定冲突场景下提供了比标量差距更稳健的诊断视角，但其对标准化量表和固定样本量的依赖限制了其在通用价值评估中的泛化能力。

】

---

【VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection ｜基于推理轨迹聚类的置信度自一致性优化

研究机构：美国布兰迪斯大学

作者：James Petullo、Sonny George、Dylan Cashman 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08070)

> 推理时扩展（Test-Time Scaling, TTS）旨在通过增加计算资源提升大语言模型（LLM）的推理准确率，但“二次思考”（Think Twice）范式因需对每条采样轨迹调用批评者模型进行置信度评分，导致推理开销呈线性激增。现有方法如置信度自一致性（Confidence-Informed Self-Consistency, CISC）虽提升了准确率，却未区分冗余或幻觉轨迹，造成算力浪费。本文提出 VecCISC，通过嵌入向量聚类筛选语义等价轨迹，仅对代表样本进行评分，在维持准确率的同时大幅降低 token 消耗。该方法在通用问答任务上验证了有效性，但在高难度数学竞赛任务上的泛化能力存疑。

】

---

【Veri-R1: Toward Precise and Faithful Claim Verification via Online Reinforcement Learning ｜在线强化学习驱动的事实核查

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、复旦大学

作者：Qi He、Cheng Qian、Xiusi Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_59928245aac4)

> 在线事实核查要求模型在缺乏直接证据时主动检索并推理，但现有方法多依赖预定义工作流或静态微调，难以适应动态检索环境。Veri-R1 通过在线强化学习（Online RL）让模型在训练中实时交互搜索引擎，以奖励信号塑造检索与判决行为。该框架在中小模型上显著提升了联合准确率，但其对大模型过度自信问题的揭示，暗示了置信度校准在事实核查中的潜在价值。

】

---

【ViLegalLM: Language Models for Vietnamese Legal Text ｜越南法律领域适配语言模型

作者：Truong-Phuc Nguyen、Quy-Nhan Nguyen、Minh-Tien Nguyen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_80683ca50ecc)

> 越南法律文本处理长期受限于语料规模小与模型架构单一，导致通用模型在专业术语理解与逻辑推理上表现不佳。现有方案多基于小规模语料或从指令微调模型出发，难以兼顾领域深度与基础能力。本文切入点在于构建大规模越南法律语料并从Base模型进行持续预训练，同时通过合成数据缓解标注稀缺。其价值在于确立了开源越南法律模型的新基线，但其在复杂推理任务上的表现仍受限于参数规模与数据质量。

】

---

【Visual Interference in Speech Evaluation: Cultural Asymmetry and Cross-Modal Bias in MLLMs ｜视觉干扰下的语音评估偏见：文化不对称性审计

作者：Kyusik Kim、Hyunwoo Yoo、Jaehoon Choi 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4c2b57f5e253)

> 多模态大语言模型（MLLMs）在语音评估中常因视觉先验干扰听觉证据，导致对说话人能力的误判，现有研究多聚焦于声学鲁棒性或语义理解，忽视了视觉种族线索对语言流利度评估的系统性扭曲。本文切入点在于验证MLLMs是否继承了人类社会语言学中的文化不对称偏见，即英语环境下的反向语言刻板印象与韩语环境下的期望违背效应。通过构建视觉匹配伪装范式数据集，固定原生音频并操纵视觉种族形象，量化模型在社交评估与语言画像任务中的反事实偏差。该工作揭示了高容量闭源模型在跨模态推理中复现特定文化偏见的机制，但自建基准的生态效度与去偏策略的有效性仍存疑。

】

---

【Vocab Diet: Reshaping the Vocabulary of LLMs via Vector Arithmetic ｜组合式词表重构

研究机构：以色列耶路撒冷希伯来大学

作者：Yuval Reif、Guy Kaplan、Roy Schwartz

论文原文见 [arXiv](https://arxiv.org/abs/2510.17001)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d84b8fd285dc)

> 大语言模型词表设计长期面临资源分配失衡：高频词的形态变体（如 walk, walked）占据大量独立 Token 槽位，挤压了多语言覆盖与低频词空间。现有 BPE 算法将形态变体视为独立单元，忽略了嵌入空间中已存在的线性结构。本文提出通过向量算术将词表重构为“基础词+变换向量”的组合形式，在冻结骨干的前提下释放 10-40% 的词表空间。该方法验证了 LLM 对组合式表示的内在理解能力，但派生词的低准确率暴露了线性假设在复杂形态学中的局限。

】

---

【Vulnerability of LLMs’ Stated Belief? LLMs Belief Resistance Check Through Strategic Persuasive Conversation Interventions ｜大语言模型信念鲁棒性评估：基于SMCR框架的说服防御研究

研究机构：美国印第安纳大学

作者：Fan Huang、Haewoon Kwak、Jisun An

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f52039d784d0)

> 大语言模型在持续对话压力下会采纳反事实信念，现有评估仅关注最终是否翻转，忽略了信念衰减的时序动态与多因素交互。本文引入SMCR（Source-Message-Channel-Receiver）框架，系统解耦来源、消息与接收者维度对信念稳定性的影响，并探索口头化置信度与对抗性微调的防御效果。实验揭示小模型极端易感、置信度提示反而降低鲁棒性的悖论，以及微调效果的模型依赖性。该工作为信念防御提供了微观机制视角，但其防御策略的普适性仍受限于特定模型家族与二元任务设定。

】

---

【Watch Out Your Industrial Copilots: Stealthy Backdoor Attack Against LLM-Based PLC Code Generation ｜面向LLM生成PLC代码的隐蔽后门攻击框架

作者：Xinyuan An、Liu Xiaoxia、Dongxia Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49dfe324e63a)

> 工业控制领域正引入大语言模型（LLM）自动生成PLC代码，但这一趋势引入了供应链层面的新型攻击面。现有针对通用代码的后门攻击依赖显性关键词触发，在PLC严格的实时与功能约束下极易被静态分析拦截，且无法造成物理危害。STBack通过设计适配PLC逻辑的六类恶意注入模式与语义集成触发器，构建了隐蔽性精炼流水线。该框架证明了在通过常规安全验证的前提下，LLM生成的PLC代码可被植入导致物理灾难的后门，揭示了现有防御机制在逻辑恶意代码检测上的盲区。

】

---

【WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training ｜WavAlign：面向语音对话模型的自适应混合后训练

研究机构：浙江大学、阿里巴巴集团

作者：Yifu Chen、Shengpeng Ji、Qian Chen 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14932)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14932)

> 端到端语音对话模型旨在统一语义理解与语音生成，但现有开源系统在智能（IQ）与表达力（EQ）上均存在显著短板。直接应用偏好优化（Preference Optimization）会导致声学漂移，因为文本梯度主导更新而语音梯度噪声大。本文提出单阶段自适应混合后训练框架，将偏好优化限制在文本Token，并用监督微调（SFT）锚定语音分布。该方法在多个基准上实现了IQ与EQ的同步提升，但其对弱基座模型的鲁棒性仍存疑。

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

【WenetSpeech-Wu: Datasets, Benchmarks, and Models for a Unified Chinese Wu Dialect Speech Processing Ecosystem ｜吴语语音处理生态构建

研究机构：西北工业大学

作者：Chengyou Wang、Mingchen Shao、Jingbin Hu 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11027)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11027)

> 低资源方言语音处理长期受困于数据规模与标注维度的双重匮乏，导致通用模型在特定方言上性能崩塌。现有方案多聚焦单一子方言或仅覆盖基础识别任务，缺乏系统性评估基准。本文切入点在于构建首个覆盖八种吴语子方言、包含多维标注的大规模语料库及配套基准，通过统一的数据流水线与模型训练验证其有效性。该工作填补了吴语语音技术生态的空白，但自动标注噪声对下游任务精度的具体影响尚未被充分量化。

】

---

【What Makes an LLM a Good Optimizer? A Trajectory Analysis of LLM-Guided Evolutionary Search ｜LLM进化搜索的局部精化机制

研究机构：法国国家科学研究中心

作者：Xinhao Zhang、Xi Chen、François Portet 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19440)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_de954a204254)

> 大语言模型（LLM）作为进化算子时，其优化性能差异的根源长期被归因于基础模型能力，但零样本性能仅部分解释最终结果。现有方法关注算法发现本身，却忽略了算子内部的搜索动力学，导致无法区分“强求解器”与“强优化器”。本文通过大规模轨迹分析，揭示强LLM优化器表现为“局部精化器”，其成功依赖于高频增量改进而非高新颖性探索。这一发现挑战了传统进化算法中“探索即创新”的直觉，为模型选择提供了基于精化能力而非基础能力的评估维度，但其结论在跨域泛化性上仍受限于特定任务结构。

】

---

【What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts ｜提示词欠定：需求感知优化与稳定性治理

研究机构：美国卡内基梅隆大学

作者：Chenyang Yang、Yike Shi、Qianou Ma 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4054c1974d7b)

> 提示词工程面临的核心矛盾在于，开发者难以穷尽所有业务需求，而大语言模型（LLM）对未明确指定的行为表现出高度不稳定性。现有自动优化方法（如 APE、TextGrad）仅关注整体性能指标，缺乏对单一需求满足率的细粒度反馈，导致优化结果在模型更新后极易回归。本文切入点在于将传统软件工程中的“需求工程”引入提示词优化，通过需求感知优化器（Requirements-Aware Optimizers）显式管理“指定”与“未指定”需求的边界。其价值在于揭示了“全量指定”的反模式，但其在通用推理基准上的泛化能力仍存疑。

】

---

【What Tokens Truly Matter? The Logit Conflation Problem in LLM Sampling ｜信号提取与主动相关性采样

研究机构：英国杜伦大学

作者：Pinlong Zhao、Huijun Tang、Pengfei Jiao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_35466b354d48)

> 大语言模型在指令遵循任务中常出现“高置信度但答非所问”的现象，根源在于采样策略仅依据Logit幅值筛选Token，忽略了Logit中混杂的语言流畅性与提示相关性。现有Top-p或Top-nσ等统计过滤方法无法区分这两种信号，导致模型在约束生成中频繁遗漏关键信息。本文提出SEAL-Sampling，通过注意力加权归因机制在解码阶段显式提取提示相关性信号，过滤掉统计显著但语义无关的Token。该方法在无需额外前向传播的前提下提升了指令遵循质量，但其对逻辑推理任务的增益有限，且依赖最终层注意力的语义对齐假设。

】

---

【When and What to Ask: AskBench and Rubric-Guided RLVR for LLM Clarification ｜交互澄清能力评估与训练

作者：Jiale Zhao、Ke Fang、Lu Cheng

论文原文见 [arXiv](https://arxiv.org/abs/2602.11199)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.11199)

> 大语言模型在医疗、教育等高风险场景中常面临用户输入信息缺失或包含错误前提的困境，但现有基准仅评估单轮静态问答，无法衡量模型“何时问”与“问什么”的交互决策能力。传统提示工程框架依赖特定任务启发式，难以泛化且缺乏对澄清质量的细粒度监督。本文提出 AskBench 基准与基于评分标准的强化学习（Rubric-Guided RLVR）训练方案，将标准问答对转化为带显式检查点的多轮交互任务，通过奖励机制引导模型在回答前主动获取关键信息或纠正错误前提。该方法在提升澄清覆盖率的同时保持了单轮问答性能，但评估协议依赖单一裁判模型且未提供统计置信区间，其泛化边界尚待验证。

】

---

【When Internalization Fails: Finding Better Targets for Reasoning Compression ｜推理轨迹压缩中的蒸馏目标选择：Post-think 优于通用摘要

研究机构：美国芝加哥大学

作者：Mourad Heddaya、Manley Roberts、Rohan Wadhawan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7d018c4acb30)

> 推理模型通过生成长思维链提升复杂任务准确率，但数千 Token 的解码过程带来高昂延迟与成本，且存在“过度思考”导致的性能反降。现有课程学习式内化方法在短结构化任务上有效，但在长探索性竞赛数学上失效，直接截断又因模型补偿性生成长尾文本而虚高 Token 预算。本文切入点在于发现教师模型在 `

】

---

【When Models Outthink Their Safety: Unveiling and Mitigating Self-Jailbreak in Large Reasoning Models ｜推理轨迹中的自我越狱与链式护栏

研究机构：中国科学院、中国科学院大学

作者：Yingzhi Mao、Chunkang Zhang、Junxiang Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21285)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21285)

> 大型推理模型（LRMs）在生成最终答案前会经历漫长的思维链（CoT）过程，这一过程引入了传统大语言模型（LLMs）不存在的安全盲区。现有对齐方法通常将CoT视为整体进行全局约束，导致模型为规避风险而牺牲推理连贯性，形成安全与能力的零和博弈。本文发现模型常在正确识别风险后，于后续推理步骤中自我说服推翻判断，即“自我越狱”（Self-Jailbreak），并提出链式护栏（Chain-of-Guardrail, CoG）框架，通过定位并修正特定失效步骤实现细粒度对齐。该框架在保持高推理精度的同时显著降低攻击成功率，但其依赖外部分类器进行轨迹诊断，在自动化与泛化性上仍存疑。

】

---

【When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling ｜测试时计算扩展中的边际效用递减与过度思考

研究机构：南京大学

作者：Shu Zhou、Rui Ling、Junan Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10739)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10739)

> 测试时计算扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段的计算资源提升大语言模型（LLM）的复杂推理能力，但现有研究普遍隐含“思考越长越好”的单调性假设。该假设导致模型在简单问题上浪费算力，在复杂问题上陷入自我否定的“过度思考”陷阱，且传统评估指标无法区分准确率提升与计算成本增加之间的权衡。本文通过引入“翻转事件”追踪与成本感知效用函数，系统量化了推理长度与答案质量间的非线性关系，揭示了边际效用递减及最优停止点随问题难度显著变化的规律。这一工作为TTS从“盲目扩展”转向“自适应分配”提供了关键的实证基础与评估框架，但其结论局限于特定开源模型与数学/科学任务，对私有模型及非推理任务的普适性尚未验证。

】

---

【When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs ｜个性化诱导幻觉的推理时缓解

研究机构：中国人民大学

作者：Zhongxiang Sun、Yi Zhan、Chenglei Shen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11000)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11000)

> 大语言模型（LLM）个性化旨在适配用户偏好，但现有提示增强与检索方法在提升主观满意度的同时，往往导致事实推理被用户历史干扰，产生“个性化诱导幻觉”。本文指出该现象源于隐层表示空间中个性化方向与事实方向的非正交纠缠，并提出事实保持个性化转向（Factuality-Preserving Personalized Steering, FPPS）框架，通过推理时探测纠缠程度并自适应调整隐层激活来恢复事实性。FPPS在自建基准上显著提升了事实准确率，但其评估依赖LLM-as-a-Judge且未覆盖参数化基线，跨基准泛化性存疑。

】

---

【When Rules Learn: A Self-Evolving Agent for Legal Case Retrieval ｜法律案例检索中的自进化查询重写

作者：Mingxu Tao、Jiawei Hu、Xian Zhou 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.17220)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.17220)

> 法律案例检索面临查询与长文本判决间词汇鸿沟，导致语义匹配失效。现有密集检索模型在特定法律基准上表现不及传统BM25，而人工设计重写规则成本高且泛化性差。本文提出一种无参数更新的自进化智能体框架，通过迭代生成、验证与淘汰重写规则来增强BM25。该方法在特定大模型驱动下提升了检索召回率，但其有效性高度依赖核心模型的推理能力，且未解决规则空间爆炸导致的搜索效率瓶颈。

】

---

【When Safety Alignment Fails to Generalize: Probing with Language Game Jailbreaks ｜语言游戏越狱：安全对齐的格式特异性失效

作者：Zewen Long、Yu Peng、Fangming Dong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d898311ee7da)

> 大语言模型（LLM）的安全对齐旨在阻止有害内容生成，但现有微调机制往往仅绑定特定表面形式，缺乏对语义意图的抽象泛化能力。当攻击者利用规则化语言变换（如 Ubbi Dubbi）改变提示词形态时，模型虽能理解语义却拒绝失效，暴露出对齐训练的分布局限。本文提出自定义语言游戏与自动化发现框架 AutoLanJail，通过系统化的形式变异探针验证了这一结构性脆弱性。该工作揭示了当前微调范式的根本缺陷，但其结论是否适用于所有对齐技术尚存疑。

】

---

【When Thoughts Meet Facts: Reusable Reasoning for Long-Context LMs ｜思维模板增强长上下文语言模型

研究机构：韩国科学技术院、美国明尼苏达大学

作者：Soyeong Jeong、Taehee Jung、Sung Ju Hwang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07499)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07499)

> 长上下文语言模型（LCLM）虽能容纳海量文档，但缺乏连接分散证据的结构化推理策略，导致多跳推理性能瓶颈从检索转移至逻辑组合。现有方法或依赖昂贵的模型微调，或使用一次性、查询特定的思维链提示，无法实现推理模式的复用与迭代优化。本文提出TOTAL框架，将推理过程抽象为可复用的“思维模板”，并通过自然语言反馈模拟梯度更新机制，在不修改模型权重的前提下迭代优化这些外部参数。该方法在免训练设定下显著优于基线，但绝对性能仍低于经过强化学习训练的前沿模型，且模板的泛化边界尚待明确。

】

---

【Where Reasoning Breaks: Logic-Aware Path Selection by Controlling Logical Connectives in LLMs Reasoning Chains ｜逻辑连接词干预下的推理路径选择

研究机构：美国佛罗里达大学

作者：Seunghyun Park、Yuanyuan Lei

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_047d76711f65)

> 导读 大语言模型在多步逻辑推理中常因单点错误导致全链失效，现有全局搜索或神经符号验证方案计算开销大且依赖外部形式化。本文切入点在于识别出逻辑连接词是推理链中熵值最高、因果杠杆最大的脆弱节点，通过激活引导、局部分支和针对性偏好优化三层机制精准干预这些节点。该方法在保持贪心解码效率的同时提升了推理稳定性，但其有效性受限于连接词定义的边界及缺乏强基线对比。

】

---

【Why Can Distillation Work with Limited Resources? A Systematic Study ｜低资源蒸馏的认知行为迁移机制

研究机构：清华大学、上海交通大学

作者：Xiao Hu、Xingyu Lu、Liyuan Mao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6689b8ebc0ce)

> 推理知识蒸馏旨在将大型模型的复杂逻辑能力压缩至小模型，但现有方法多聚焦于分布对齐或计算效率，缺乏对“蒸馏究竟传递了什么”的机制解释。本文切入点在于：少量高质量样本的SFT蒸馏为何能超越大规模RL训练？作者通过token频率分析与认知行为量化，揭示了蒸馏传递的是“多视角思考”与“元认知意识”两种高级认知行为，而非表面token模式。这一发现为低资源蒸馏提供了认知层面的解释框架，但其结论是否泛化至非数学任务及更大规模模型，仍存疑。

】

---

【Why Did Apple Fall: Evaluating Curiosity in Large Language Models ｜大语言模型好奇心评估与利用

研究机构：复旦大学、美国康奈尔大学

作者：Haoyu Wang、Sihang Jiang、Yuyan Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.20635)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20635)

> 大语言模型（LLM）在强化学习中引入内在奖励以模拟人类探索行为，但现有方法难以区分性能提升源于统计信号增强还是真实的“好奇心”机制。本文切入点在于将心理学量表与行为实验结合，系统评估LLM是否具备类人好奇心特质，并验证其功能性价值。通过构建基于五维好奇心量表（5DCR）的问卷自报与场景行为研究框架，并设计好奇链式提问（Curious Chain-of-Questioning, CoQ）策略，本文揭示了LLM好奇心的不对称性与上下文敏感性，并证明模仿好奇行为可提升推理性能。该工作为LLM内在动机研究提供了心理学锚点，但其结论是否受限于特定提示工程范式仍存疑。

】

---

【Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? ｜选择性翻译

作者：Deokhyung Kang、Seonjeong Hwang、Daehui Kim 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.27269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.27269)

> 推理语言模型（Reasoning Language Models, RLMs）在多语言任务中普遍存在性能落差，现有方法多聚焦于训练阶段的权重调整或推理阶段的强制语言对齐，却忽视了差距产生的具体环节。本文指出，该落差主要源于模型在将非英语输入转化为内部英语推理轨迹时的“理解失败”，而非推理逻辑本身的缺陷。通过构建基于隐藏状态的行为检测器，仅在检测到理解失败时触发外部翻译，该方法以极低的计算开销实现了接近全量翻译的准确率。这一发现将多语言推理优化从“全局对齐”转向“局部纠错”，但其检测器在极低资源语言上的泛化能力仍存疑。

】

---

【WildSci: Advancing Scientific Reasoning from In-the-Wild Literature ｜WildSci：基于同行评审文献的科学推理强化学习数据集

研究机构：美国加州大学圣塔芭芭拉分校

作者：Tengxiao Liu、Deepak Nathani、Zekun Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05567)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05567)

> 科学推理领域长期面临高质量训练数据稀缺与开放性问题难以自动验证的双重困境，导致强化学习在数学与代码领域的成功难以迁移至医学、材料等复杂学科。现有数据集多源自教科书或通用语料，缺乏研究级深度且存在数据污染风险，而开放式科学问题又无法提供明确的奖励信号。本文提出 WildSci，通过自动化管线从 Nature Communications 论文中合成 56K 道多选科学题，利用模型投票确保质量，并采用 GRPO 算法进行强化学习训练。该工作验证了文献接地数据在小模型上的有效性，但其多选格式对开放推理能力的评估边界仍存疑。

】

---

【X-Router: Decoupling Knowledge and Reasoning for Cost-Effective LLM Inference ｜双轴机制路由

研究机构：哈尔滨工业大学、电子科技大学

作者：Zixuan Wang、Yinze Ding、Zihan Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c1801e0c5e23)

> 大语言模型在处理知识密集与逻辑推理任务时，常因静态启用检索增强生成（RAG）与思维链（CoT）而产生冗余计算开销。现有自适应方法多聚焦单一维度，忽视了证据获取与推理深度仅部分相关的特性，导致在逻辑主导或证据缺失场景下出现系统性低效。X-ROUTER 提出双轴路由框架，通过离线效用最大化生成监督信号，在线利用轻量级探测信号独立决策是否检索与是否推理，实现了成本与质量的帕累托优化。该方法在跨域零样本迁移中展现了显著的效率优势，但其对骨干模型能力的依赖及探测信号的普适性仍存疑。

】

---

【x1: Learning to Think Adaptively Across Languages and Cultures ｜自适应多语言推理

研究机构：哈尔滨工业大学、华为

作者：Yangfan Ye、Xiaocheng Feng、Xiachong Feng 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bc2799709cf4)

> 大语言模型在多语言任务中默认使用英语进行内部推理，导致低资源语言性能受损且文化语境丢失。现有方法或依赖外部翻译引入噪声，或通过强化学习优化全局奖励，但难以在单实例层面动态选择最优推理语言。本文提出x1模型，通过两阶段自监督训练使模型学会在特定实例上自适应切换至优势语言进行推理。该工作证明了语言选择是推理的功能性组件，但在高难度数学任务上的增益有限，且其效果高度依赖骨干模型原有的语言合规能力。

】

---

【You Only Need One Single Token to Refine Safety Alignment ｜单令牌对齐

研究机构：武汉大学、德国慕尼黑大学

作者：Wenqian Yu、Shuo Chen、Zhijiang Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_57097267c171)

> 安全对齐的核心矛盾在于抑制有害输出与保持模型有用性之间的参数空间冲突，过度拒绝（Over-refusal）是这一冲突在良性边界样本上的典型表现。现有免训练干预方法虽降低了训练成本，却因仅做后验修正而无法重塑模型内部的决策分布，导致安全与效用此消彼长的失衡。本文提出单令牌对齐（Single Token Alignment, STA），通过冻结骨干网络并仅优化一个4096维的前缀嵌入向量，结合硬软混合加权机制，在极小参数接口下实现决策空间的重塑。该方法在9个模型上验证了其在轻量级约束下平衡安全与效用的有效性，但其对复杂语境细微差别的捕捉能力仍存疑。

】

---

【Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use ｜后门工具调用数据窃取

作者：Wuyang Zhang、Shichao Pei

论文原文见 [arXiv](https://arxiv.org/abs/2604.05432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05432)

> 工具调用型大语言模型（LLM）代理在部署中常被赋予会话记忆与外部检索权限，这为敏感信息泄露提供了隐蔽通道。现有针对代理的安全研究多聚焦于运行时提示注入或知识投毒，忽略了模型权重层面植入的后门如何与工具调用机制耦合，实现系统性数据窃取。本文提出 Back-Reveal 框架，通过语义触发器激活后门，利用伪装成合法检索请求的 HTTP 调用将记忆数据外传，并引入重排序感知重写器以绕过现代 RAG 过滤机制。该工作揭示了代理系统中“记忆-检索”链路的安全盲区，但其攻击可行性高度依赖开放权重与宽松连接器配置，在严格权限隔离的生产环境中适用性存疑。

】

---

【Your LLM Agents are Temporally Blind: The Misalignment Between Tool Use Decisions and Human Time Perception ｜多轮代理时间盲性评估与对齐

研究机构：美国马里兰大学帕克分校

作者：Yize Cheng、Arshia Soltani Moakhar、Chenrui Fan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.23853)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_050e4ebbcd90)

> 多轮大语言模型代理在动态环境中执行任务时，常因忽略消息间的真实时间流逝而做出错误的工具调用决策，这一现象被称为时间盲性。现有评估基准多聚焦于静态时间推理或单轮工具调用准确性，缺乏对“时间流逝如何影响决策”的系统量化，导致模型在实时交互中过度依赖过时上下文或冗余调用工具。本文构建了包含76个场景、5592个样本的TicToc数据集，通过注入ISO 8601时间戳并收集人类偏好，量化了模型工具调用决策与人类时间感知的对齐程度。该工作揭示了当前模型在时间感知上的系统性缺陷，但仅验证了后训练对齐的初步有效性，未解决模型内部时间表示的根本缺失。

】

---

【Zero-Shot Context-Aware ASR for Diverse Arabic Varieties ｜零样本阿拉伯语方言ASR的上下文感知解码

研究机构：加拿大不列颠哥伦比亚大学、英国帝国理工学院

作者：Bashar Talafha、Amin Abu Alhassan、Muhammad Abdul-Mageed

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2971de2b614e)

> 零样本阿拉伯语方言自动语音识别（ASR）面临标准语模型在方言输入下性能骤降且缺乏标注数据微调的困境。现有推理时适应方法多局限于可提示的编码器-解码器架构，且直接提示易引发幻觉，无法覆盖非自回归模型。本文提出上下文感知解码范式，通过提示重排序、说话人一致前缀及代理引导n-best选择，在不更新参数的前提下引导解码。该策略在多方言条件下实现了显著的相对词错率（WER）降低，但其收益高度依赖外部代理质量，且在极端低资源方言上的绝对性能提升有限。

】

---

【中国人民大学团队提出WASP协议：预构建站点地图注入上下文，无需训练提升Web智能体导航

研究机构：中国人民大学

作者：Yuyao Zhang、Hongyu Lu、Jiajie Jin 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f6f66507cc6)

> 现有LLM Web智能体在真实开放网络中因缺乏网站结构先验，导致导航低效与接地误差，任务成功率远低于人类水平。主流路线聚焦于增强模型内部推理或构建动态世界模型，但忽视了静态结构化知识对长程规划的支撑作用。WASP通过预构建双粒度站点地图，将全局导航结构与局部交互指引作为外部知识注入智能体上下文，无需额外训练即可提升鲁棒性与效率。该方案在WebVoyager上取得58.3%成功率，但依赖静态快照，未验证网页动态更新下的时效性。

】

---

【中大南洋理工阿里联合发布RealSec-bench：基于真实Java仓库评估LLM安全代码生成，揭示跨过程漏洞短板

研究机构：中山大学、新加坡南洋理工大学

作者：Yanlin Wang、Ziyao Zhang、Chong Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_217605fc06c1)

> 现有安全代码生成基准多依赖合成片段或孤立函数，无法捕捉真实软件中跨过程数据流引发的漏洞，导致对模型安全能力的评估存在系统性高估。本文切入点在于构建基于真实高风险 Java 仓库的基准，通过 SAST 筛选与多 LLM 裁决机制解决静态分析高误报与上下文缺失的双重难题。其核心做法是构建包含 105 个实例的 RealSec-bench，并引入联合指标 SecurePass@k 同时评估功能与安全性。该基准揭示了当前主流 LLM 在仓库级安全生成上的显著短板，但其仅覆盖 Java 语言且实例规模有限，跨语言泛化性存疑。

】
