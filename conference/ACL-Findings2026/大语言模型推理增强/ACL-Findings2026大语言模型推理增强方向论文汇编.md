# ACL-Findings2026 · 大语言模型推理增强方向论文汇编

> 本方向共 16 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agent-GWO: Collaborative Agents for Dynamic Prompt Optimization in Large Language Models ｜狼群优化驱动的推理配置自动搜索

研究机构：电子科技大学、同济大学

作者：Xudong Wang、Chaoning Zhang、Chenghao Li 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18612)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18612)

> 大语言模型在复杂推理任务中常因提示词微小变动或解码参数设置不当导致性能剧烈波动，现有测试时增强方法多聚焦于轨迹生成与搜索，却忽视了提示模板与解码超参这一底层配置空间的联合优化。Agent-GWO 将提示与超参封装为可继承的“智能体”状态，利用灰狼优化算法的领导者-跟随者机制在推理阶段自动搜索鲁棒配置。该方法无需训练即可在数学与混合推理基准上稳定提升准确率，但其增益是否源于模型固有能力的释放而非优化算法本身的贡献，仍需更严格的消融验证。

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

【Beyond High-Entropy Exploration: Correctness-Aware Low-Entropy Segment-Based Advantage Shaping for Reasoning LLMs ｜低熵段优势整形

研究机构：北京邮电大学、中国人民大学

作者：Xinzhu Chen、Xuesheng Li、Zhongxiang Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.00908)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00908)

> 强化学习后训练在提升大语言模型推理能力时，往往陷入高熵探索与低熵结构稳定性的失衡，导致错误模式固化。现有基于熵的优化方法仅关注高熵Token，忽视了占据序列80%的低熵段对推理结构的决定性作用。本文提出LESS框架，通过组内正确性统计重塑低熵段优势函数，在GRPO基础上实现了对稳定推理结构的显式强化。该方法在数学基准上显著提升了准确率与鲁棒性，但其对非可验证领域的泛化能力尚存疑。

】

---

【Beyond Templates: Dynamic Adaptation of Reasoning Demonstrations via Feasibility-Aware Exploration ｜动态推理轨迹适配

作者：Yong Wu、Weihang Pan、Ke Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_60b5f981edf0)

> 小语言模型（SLM）在模仿大模型专家推理数据时，常因能力错配导致性能不升反降，这一现象被称为“模仿间隙”。现有静态微调方法假设模型具备潜在推理能力，却忽视了专家轨迹中超出学生模型抽象空间的步骤会引入噪声。本文提出 DART 框架，通过蒙特卡洛模拟评估步骤可行性，在检测到模仿间隙时触发自主探索，生成结果一致的替代路径。该方法在 SLM 上显著优于静态微调，但其有效性依赖于离线模拟的计算成本，且未验证在强化学习范式下的迁移性。

】

---

【Beyond ’Aha!’: Toward Systematic Meta-Abilities Alignment in Large Reasoning Models ｜超越“顿悟”：基于皮尔斯三元组的元推理能力对齐

作者：Zhiyuan Hu、Yibo Wang、Hanze Dong 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f68280b2a67e)

> 大语言模型在强化学习后训练中常出现不可控的“顿悟时刻”，即模型自发涌现出长思维链与自我修正行为，但这种涌现缺乏稳定性与可预测性，限制了推理能力的规模化部署。现有基于单一任务奖励的强化学习范式难以将这种偶发的认知行为转化为可控、可组合的通用推理技能。本文提出通过显式对齐演绎、归纳与溯因三种元推理能力，利用参数空间合并构建统一推理基座，再经领域特定强化学习提升性能上限。该方法在数学与代码基准上较指令微调基线提升超过10%，但其在非可验证任务上的泛化边界及合并权重的敏感性仍需进一步验证。

】

---

【C3D: Enhancing LLM Reasoning via Confidence-Guided Contrastive Decoding ｜置信度引导跨前提对比解码

研究机构：中国科学院、中国科学院大学

作者：Yufeng Zhang、Xuepeng Wang、Lingxiang Wu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e2597bb33467)

> 大语言模型在推理时易受上下文无关信息干扰，导致错误累积。现有解码策略多关注层间或有无上下文的对比，忽略了前提内部的细粒度相关性差异。本文提出C3D，通过分解前提并动态对比高/低置信度前提的Logits来修正生成分布。该方法在强推理模型上稳定提升性能，但其增益是否源于模型本身对前提结构的敏感度，而非解码策略的普适性，尚存疑。

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

【Fundamental Reasoning Paradigms Induce Out-of-Domain Generalization in Language Models ｜解耦基础推理范式以增强大语言模型泛化能力

作者：Mingzi Cao、Xingwei Tan、Mahmud Elahi Akhter 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1e438019e8f)

> 大语言模型在复杂推理任务中的表现瓶颈，源于其自回归生成机制与多步逻辑推导之间的内在张力，现有方法往往将演绎、归纳与溯因三种基础逻辑范式混同处理，导致无法量化单一范式对通用推理能力的独立贡献。本文切入点在于通过符号化任务剥离世界知识，独立诱导三种范式技能，并验证其跨域泛化能力。具体做法是利用教师模型生成纯逻辑轨迹，通过全量微调、低秩适配、深度扩展及混合专家结构扩展等四种方法诱导学生模型，并在真实自然语言任务上评估。该方法证明了基础逻辑技能可独立迁移至现实任务，但其在数学基准上的缺失及教师-学生家族匹配性的矛盾，限制了结论的普适性。

】

---

【Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning ｜识别能力边界：训练大模型在无效推理时主动中止

作者：Xinyan Guan、Jiali Zeng、Chunlei Xin 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_169c06787548)

> 导读 大语言模型在面对超出其内在能力边界的问题时，往往不承认无知，而是生成看似合理实则错误的推理轨迹，这种现象被称为无效推理（Futile Reasoning）。现有基于可验证奖励的强化学习（RLVR）范式主要优化答案正确性，缺乏对“拒绝”行为的显式激励，导致模型在不可解任务上持续消耗计算资源并产生误导性输出。本文提出能力对齐强化学习（CaRL），通过重构奖励函数建立“正确>拒绝>错误”的层级，并结合后见之明拒绝增强（HRA）将失败轨迹转化为拒绝监督信号。该框架在保持通用推理性能的同时，将无效推理率从 65.5% 降至 7.0%，但其有效性目前仅限于纯算法推理任务，在知识密集型场景下的泛化能力尚存疑。

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

【RAVR: Reference-Answer-guided Variational Reasoning for Large Language Models ｜参考答案引导的变分推理

研究机构：浙江大学、阿里巴巴集团

作者：Tianqianjin Lin、Xi Zhao、Xingyao Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.25206)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.25206)

> 基于可验证奖励的强化学习（RLVR）在训练大语言模型时面临采样瓶颈：当任务超出模型当前能力，模型无法生成足够多的高质量推理路径，导致训练坍缩至次优解。现有方法仅将参考答案用于计算奖励，忽略了其作为推理引导源的潜力。本文提出 RAVR，利用参考答案条件化生成“后验推理”，通过变分推断优化目标将其迁移至无答案的“先验推理”。该方法在小模型难任务上显著优于基线，但其对开放式任务及长文本推理的适用性尚未验证。

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

【RISER: Orchestrating Latent Reasoning Skills for Adaptive Activation Steering ｜动态激活引导下的潜在推理技能编排

研究机构：同济大学

作者：Wencheng Ye、Xiaoyang Yuan、Yi Bin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09269)

> 大语言模型在复杂推理任务中常因静态提示或参数微调导致效率低下与泛化受限，现有激活引导方法仅能施加单一固定向量，无法适应多步推理中动态变化的认知需求。RISER 通过构建可复用的认知原语向量库，并引入经强化学习训练的轻量级路由器，在推理时动态组合并注入这些向量，实现了无需更新骨干参数的细粒度控制。该方法在七个基准上实现了3.4%–6.5%的零样本准确率提升，同时保持接近标准推理的计算效率，但其跨模型迁移能力的局限性揭示了表征几何对控制策略的强依赖。

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

【TARo: Token-level Adaptive Routing for LLM Test-time Alignment ｜令牌级自适应路由

研究机构：美国匹兹堡大学、美国加州大学伯克利分校

作者：Arushi Rai、Qiang Zhang、Hanqing Zeng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18411)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18411)

> 大语言模型（LLM）在复杂推理任务中常因后训练成本高、领域特定性强而难以灵活部署，现有测试时对齐方法依赖固定插值权重，无法适应不同任务与模型规模的动态变化。本文提出令牌级自适应路由（Token-level Adaptive Routing, TARO），通过可学习路由器在解码时动态融合基座模型与奖励模型的输出，消除手动调参需求。该方法在数学推理基准上较基座模型提升最高22.4%，并展现出弱到强泛化能力，但其效果高度依赖奖励模型与基座模型的能力匹配度，跨域泛化机制尚待深入验证。

】

---

【Understanding LLM Reasoning for Abstractive Summarization ｜摘要生成中的推理策略评估

作者：Haohan Yuan、Haopeng Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b5d0ac0d9c00)

> 摘要生成任务要求信息压缩而非逻辑推导，但现有研究默认思维链（Chain-of-Thought, CoT）等推理范式能普适提升所有生成任务性能，这一假设在摘要场景中缺乏系统验证。本文通过统一框架对比8种显式推理策略与3个大推理模型（Large Reasoning Models, LRM），发现推理复杂度与事实忠实度存在显著负相关，挑战了“更多推理即更好”的领域共识。其价值在于揭示了摘要任务中质量与忠实度的权衡机制，但实验仅覆盖单一模型家族，结论的跨模型泛化性存疑。

】
