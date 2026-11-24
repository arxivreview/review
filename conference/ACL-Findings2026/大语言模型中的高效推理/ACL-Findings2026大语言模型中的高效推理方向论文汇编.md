# ACL-Findings2026 · 大语言模型中的高效推理方向论文汇编

> 本方向共 14 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

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

【Beyond Token Length: Step Pruner for Efficient and Accurate Reasoning in Large Language Models ｜步骤剪枝

作者：Canhui Wu、Qiong Cao、Chang Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03805)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03805)

> 大型推理模型（LRM）在简单任务上常陷入冗长推理，导致计算成本激增与错误累积，即“过度思考”。现有强化学习（RL）方法通过惩罚Token长度来抑制冗余，但Token数少不代表推理步骤少，且模型后期可能通过丢弃推理步骤来“黑客”奖励。本文提出步骤剪枝（SP），将惩罚粒度从Token提升至语义步骤，并引入动态停止机制防止奖励黑客。该方法在MATH-500上以92.0%准确率仅用33%的Token，但AIME24准确率略降，其步骤边界定义的鲁棒性存疑。

】

---

【Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data ｜预算约束下的即时推理评估与偏好提示

作者：Xuanming Zhang、Shwan Ashrafi、Aziza Mirsaidova 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11038)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_802a45c97ef4)

> 现有推理效率优化聚焦于最终答案的Token消耗或训练时的长度惩罚，却忽视了在严格延迟预算下，模型中间输出质量的演变轨迹。本文切入点在于将“即时推理”形式化，提出Anytime Index量化质量-Token权衡，并设计PDP方法通过自生成偏好对提升中间推理质量。该方法无需微调，仅通过推理时提示即可在规划、数学与科学问答任务上提升效率。其价值在于提供了过程级评估工具，但依赖截断重提示的评估协议是否真实反映中断场景，仍存疑。

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

【Efficient Reasoning for LLMs through Speculative Chain-of-Thought ｜思维链级推测解码

研究机构：香港中文大学

作者：Jikai Wang、Juntao Li、Jianye Hou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4984aa9d5a22)

> 大型推理模型在复杂任务上依赖超长思维链（CoT），导致推理延迟成为系统瓶颈。现有加速方案多聚焦于缩短CoT长度或缩小模型规模，但简单任务上“过度思考”与复杂任务上“精度损失”的矛盾仍未解决。SCoT将推测解码的验证粒度从Token提升至CoT，通过小模型并行生成多条草稿、大模型单次前向选择最优草稿，实现难度自适应的推理加速。该方法在保持近目标模型精度的同时显著降低延迟，但其对高难度任务的精度保持能力与训练开销的权衡尚存疑。

】

---

【ERRV: Eliciting Efficient Reasoning through Reasoning Vectors for Policy Optimization in Large Language Models ｜推理向量引导的高效强化学习训练

作者：Zhuowen Han、Lei Yang、Renren Jin 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8927e5ddd1f4)

> 大型推理模型在解决复杂问题时倾向于生成冗长的思维链，导致推理延迟与计算成本激增，而现有优化手段多聚焦于外部奖励函数调整或数据重构，忽略了模型内部隐藏状态中已蕴含的“简洁推理”潜能。本文提出“推理向量”概念，通过对比最短正确响应与最长错误响应的隐藏状态差异提取该向量，并将其注入强化学习（RL）的采样阶段以引导策略优化。该方法在无需推理时向量辅助的情况下，实现了约30%的推理长度缩减且准确率保持稳定，但其效果高度依赖特定骨干网络，跨模型泛化性存疑。

】

---

【Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models ｜重塑探索与利用机制以优化大模型推理效率

作者：Yufeng Shi、Weilin Luo、Yuxiang Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0914fcfbe5b9)

> 大推理模型（LRM）在可验证奖励强化学习（RLVR）训练中普遍存在“过度思考”现象，导致简单任务计算资源浪费。现有基于长度惩罚的奖励整形方法缺乏对高价值数据的优先利用与定向探索，导致样本效率低下。本文提出SIGMA框架，将推理效率优化重构为经典的探索-利用权衡，通过自模仿损失与动态优先级采样提升数据利用率，并引入自引导探索机制生成更简洁的轨迹。该方法在1.5B和7B模型上实现了43.4%和40.3%的长度缩减，同时保持或提升准确率，但其效果高度依赖骨干模型的预训练质量，且未验证在动态难度分布下的鲁棒性。

】

---

【O1-Pruner: Length-Harmonizing Fine-Tuning for O1-Like Reasoning Pruning ｜长度协调微调

作者：Haotian Luo、Haiying He、Yibo Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f53b21ab79a8)

> 长思维链模型在简单任务上产生冗余推理，导致计算资源浪费，现有提示工程或监督微调难以在保持准确率的同时有效压缩推理长度。本文切入点在于识别“长度不和谐”现象，即短答案往往已具备高准确率，长答案成为无效开销。通过构建基于参考模型基线的强化学习奖励函数，利用离策略PPO训练使模型内化简洁推理习惯。该方法在中等难度数学任务上实现了准确率与效率的双赢，但在极限难度任务上性能显著退化，其离策略训练机制对复杂逻辑探索能力的潜在抑制值得警惕。

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

【Thinking Economically: A Hierarchical Framework for Adaptive-Complexity Reasoning in LLMs ｜层级自适应预算器

作者：Yubo Gao、Haotian Wu、Hong Chen 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b4b7d190df24)

> 大语言模型在复杂推理中常因“过度思考”产生冗余计算，而现有压缩方法多采用全局统一预算，忽视了问题间与步骤间的复杂度差异。本文指出全局预算的根本局限，提出层级自适应预算器（HAB），通过两阶段监督学习实现从问题级步数控制到步骤级Token保留率的细粒度分配。实验表明HAB在GSM8K和MATH500上同时提升了准确率并降低了Token消耗，但其泛化性受限于数学任务且未对比最新RLVR方法，其监督学习路径能否在更复杂任务上超越强化学习范式仍存疑。

】

---

【TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models ｜触发式大小模型协同推理

研究机构：上海交通大学、复旦大学

作者：Yi Zhao、Yajuan Peng、Cam-Tu Nguyen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14847)

> 大语言模型在复杂推理任务中依赖长思维链，但自回归生成导致高延迟，现有加速方案要么压缩单模型推理预算，要么依赖小模型生成、大模型验证的协同范式。SpecReason等协同方法采用每步轮询验证，但大模型作为评判者存在主观偏差且通信开销巨大，导致效率收益被抵消。本文提出TrigReason，通过识别小模型推理失败的三种风险模式，设计基于事件信号的稀疏触发机制，仅在关键节点调用大模型进行干预。该框架在保持准确率的同时显著提升了小模型推理步骤的利用率，但在触发阈值的跨模型泛化性及非数学领域的鲁棒性上仍存疑。

】
