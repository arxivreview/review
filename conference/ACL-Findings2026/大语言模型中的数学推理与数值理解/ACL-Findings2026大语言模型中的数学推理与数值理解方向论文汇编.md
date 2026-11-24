# ACL-Findings2026 · 大语言模型中的数学推理与数值理解方向论文汇编

> 本方向共 14 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【1,729 vs. 1729: The Effect of Scripts and Formats on LLM Numeracy ｜书写系统与格式对大语言模型算术能力的影响

研究机构：美国麻省理工学院

作者：Varshini Reddy、Craig W Schmidt、Seth Ebner 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_63bf8444c8f6)

> 大语言模型在标准阿拉伯数字下的算术表现优异，但一旦数字的书写系统或排版格式偏离训练语料的主流约定，其推理能力便出现断崖式下跌。现有鲁棒性评估多聚焦于数值本身的扰动，忽视了符号系统层面的表征偏差。本文通过构建覆盖21种数字脚本与6种排版格式的受控数据集，量化了这种“脚本税”的规模，并验证了提示工程在缓解该缺陷上的有效性。该研究揭示了多语言数值推理中被长期忽视的盲区，但其结论受限于未测试专门优化的数学模型，且仅通过外部提示而非内部表征修改来应对问题。

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

【Bridging the Culture Gap: A Framework for LLM-Driven Socio-Cultural Localization of Math Word Problems in Low-Resource Languages ｜文化实体扰动下的数学鲁棒性：低资源语言本地化框架

作者：Israel Abebe Azime、Tadesse Destaw Belay、Dietrich Klakow 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22cda7beaaa0)

> 大语言模型在低资源语言数学任务中的表现长期受限于评估数据的文化偏差，现有翻译基准保留英语中心实体，导致模型性能无法反映真实本地场景下的推理能力。本文切入点在于构建自动化文化本地化管道，通过替换人名、组织名与货币，生成符合目标语言文化背景的数学应用题变体。该框架利用大语言模型进行实体分类与替换，并结合质量检查模块确保语义一致性。其价值在于揭示了文化实体对模型鲁棒性的显著影响，但实验仅关注最终答案匹配，未深入诊断推理过程中的逻辑断裂。

】

---

【Do LLMs Overthink Basic Math Reasoning? Benchmarking the Accuracy-Efficiency Tradeoff in Language Models ｜大语言模型基础算术中的过度思考与效率-准确率权衡

研究机构：美国弗吉尼亚理工大学

作者：Gaurav Srivastava、Aafiya Shamshad Hussain、Sriram Srinivasan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ca960cba766a)

> 大语言模型在复杂数学基准上表现优异，却在基础算术任务中生成冗余推理链且准确率不升反降，这一现象被称为过度思考（Overthinking）。现有评估体系将准确率与计算效率视为独立维度，无法量化二者间的根本权衡，导致部署场景下的计算浪费被忽视。本文提出基于调和平均的过度思考分数（Overthinking Score），结合动态生成的14类确定性算术任务，系统评估53个模型在准确率与Token效率间的平衡能力。该工作填补了推理效率量化评估的空白，但其结论局限于基础算术任务，对复杂推理场景的普适性存疑。

】

---

【ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection ｜多模态数学错误检测基准

作者：Yibo Yan、Shen Wang、Jiahao Huo 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.04509)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_26fceb05b60d)

> 多模态大语言模型（MLLM）在数学解题上表现优异，但缺乏对推理过程错误类型的细粒度诊断能力，现有基准仅评估最终答案正确性，无法区分视觉感知、计算或逻辑推理导致的失败。本文切入点在于将任务从“解题”重构为“纠错”，构建首个基于真实学生错误数据的多模态错误检测基准。通过定义错误步骤定位与错误分类两个子任务，评估模型对非标准推理路径的识别能力。该基准揭示了当前SOTA模型在复杂推理诊断上的显著瓶颈，但受限于K-12难度与静态数据分布，其结论向高阶数学或动态场景的泛化性存疑。

】

---

【FormulaReasoning: A Dataset for Formula-Based Numerical Reasoning ｜公式驱动数值推理数据集

作者：Xiao Li、Bolin Zhu、Kaiwen Shi 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aff168a56c99)

> 现有数学基准多依赖隐式常识，缺乏对领域特定公式的显式监督，导致模型在复杂物理计算中易产生幻觉。本文通过构建包含细粒度公式标注的双语数据集，并引入逆向变换与参数噪声注入策略，旨在评估模型在结构化知识引导下的多步推理能力。实验表明，大模型在简单公式题上接近人类水平，但在耦合复杂题上显著落后，揭示了当前模型在长程依赖与系统方程求解上的瓶颈。该数据集填补了领域特定公式推理基准的空白，但其对检索器精度的依赖及小模型微调收益的局限性仍需进一步验证。

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

【GanitLLM: Difficulty-Aware Bengali Mathematical Reasoning through Curriculum-GRPO ｜孟加拉语数学推理模型 GANITLLM：基于课程式 GRPO 的低资源语言训练

作者：Shubhashis Roy Dipta、Khairul Mahbub、Nadia Najjar

论文原文见 [arXiv](https://arxiv.org/abs/2601.06767)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06767)

> 导读 低资源语言大语言模型在数学任务中面临推理语言归属与训练效率的双重困境，现有高资源语言强化学习配方因奖励稀疏导致梯度失效。本文切入点在于识别并解决 Group Relative Policy Optimization (GRPO) 在低资源场景下的冷启动问题，通过构建难度感知数据集 GANIT 并提出 CURRICULUM-GRPO 采样策略，实现原生孟加拉语推理。该方法在 Bn-MGSM 上提升 8 分准确率，但绝对性能仍低于高资源语言基线，其泛化边界尚待验证。

】

---

【How Robust Are Large Language Models for Clinical Numeracy? An Empirical Study on Numerical Reasoning Abilities in Clinical Contexts ｜临床数值鲁棒性基准

研究机构：澳大利亚皇家墨尔本理工大学

作者：Minh-Vuong Nguyen、Fatemeh Shiri、Zhuang Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ecf17ec6a6b)

> 临床大语言模型（LLM）的安全部署依赖于对患者生命体征等数值数据的精确处理，但现有评估多聚焦于通用数学或单一临床知识，忽视了同一测量值在不同文档格式下的推理一致性。静态临床基准无法隔离数值操作能力与格式敏感度，导致模型在真实病历中的表现被高估。本文构建了包含1,624个实例的ClinicNumRobBench，通过程序化生成三种语义等价但格式迥异的上下文，系统测试17个LLM在检索、算术、比较和聚合上的鲁棒性。该基准揭示了医疗微调可能削弱数值推理能力的反直觉现象，为临床AI的可靠性评估提供了新维度，但其诊断性质决定了它无法直接解决格式敏感问题。

】

---

【Mechanistic Interpretability of Large-Scale Counting in LLMs through a System-2 Strategy ｜基于System-2策略的大规模计数机制解析

作者：Hosein Hasani、Mohammadali Banayeeanzade、Ali Nafisi 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02989)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc4a31edeae3)

> 大语言模型（LLM）在处理长序列计数任务时，因Transformer架构的层深限制导致内部计数机制饱和，性能随项目数量增加而急剧下降。现有方法多依赖外部工具或微调，忽视了模型内部隐式计数过程的容量瓶颈。本文提出一种无需修改参数的测试时策略，通过将长序列分割为小分区并显式聚合中间结果，绕过架构限制。该策略在多个开源与闭源模型上验证了有效性，但其泛化至非计数类算术任务的边界尚不明确。

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

【Multiplication in Multimodal LLMs: Computation with Text, Image, and Audio Inputs ｜多模态大语言模型中的算术鲁棒性与启发式指纹

作者：Samuel Gideon Balter、Ethan Jerzak、Connor Thomas Jerzak

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_614c18a22f3a)

> 导读 多模态大语言模型（Multimodal Large Language Models, MLLMs）在处理基础算术时存在严重的模态依赖与计算脆弱性，现有基准往往混淆感知错误与计算错误，导致无法准确归因性能瓶颈。本文切入点在于构建一个控制变量下的多模态乘法基准，通过解耦感知与计算环节，并引入基于损失探针的内部机制分析，揭示模型在模态切换下的真实算术极限。具体做法是定义算术负载指标，利用强制完成损失探针量化模型对特定算术启发式的偏好，并通过低秩适配器（Low-Rank Adaptation, LoRA）几何分析验证内部路由机制。该工作提供了诊断MLLM算术缺陷的新工具，但其结论局限于乘法运算，且LoRA实验显示外部干预可能破坏模型原生路由，其泛化性存疑。

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

【SciText2Eq: Assessing LLMs for Explainable Equation Generation for Scientific Creativity ｜科学文本公式生成与语义对齐

研究机构：荷兰阿姆斯特丹自由大学、荷兰瓦赫宁根大学与研究中心

作者：Yifan Mo、Xiao Fu、Yue Su 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.16003)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16003)

> 科学文献中公式与叙述交织，现有方法多关注单点提取或数值等价，难以处理长文档中公式间的依赖关系及语义忠实度。本文提出 SciText2Eq 工作流，通过文档级序列生成与多层级评估协议，诊断 LLM 在真实科学文本中重构公式的能力。实验表明，模型在词汇相似度上表现中等，但在语义等价性上存在显著缺陷，且 LLM 评估与人类判断对齐度低。该工作填补了从“解题”到“科学公式生成”的评估空白，但缺乏符号验证器的硬约束，其评估可靠性仍存疑。

】
