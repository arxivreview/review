# ACL-Findings2026 · 大语言模型中的不确定性估计与校准方向论文汇编

> 本方向共 11 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning ｜校准感知强化学习：决策LLM中精度与置信度的再平衡

研究机构：美国南加州大学、亚马逊网络服务人工智能

作者：Duygu Nur Yaldiz、Evangelia Spiliopoulou、Zheng Qi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13284)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13284)

> 在内容审核、医疗辅助等高风险决策场景中，大语言模型（LLM）不仅需要输出正确标签，其预测概率还需真实反映正确率，以便下游系统判断何时信任模型、何时触发人工复核。现有微调范式存在结构性矛盾：监督微调（SFT）能改善概率校准但精度增益有限，而可验证奖励强化学习（RLVR）虽提升精度却导致模型极度过度自信，使置信度信号失效。本文通过诊断RLVR校准失效的微观机制，提出直接调节决策token概率的校准感知强化学习算法，在保持RLVR精度优势的同时将期望校准误差（ECE）降低至接近SFT水平。该方法在原子选项分类任务中有效，但其对开放式生成或复杂推理链的适用性存疑。

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

【Confidence over Time: Confidence Calibration with Temporal Logic for Large Language Model Reasoning ｜时序逻辑置信度校准

研究机构：美国佛罗里达大学

作者：Zhenjiang Mao、Anirudhh Venkat、Artem Bisliouk 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.13387)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13387)

> 长程推理中，模型输出的置信度往往随生成步骤动态波动，但现有方法将其压缩为单一标量，导致置信度受响应长度与冗余词汇干扰，无法区分逻辑错误与表面流畅。本文切入点在于将置信度视为时间信号，利用信号时序逻辑（Signal Temporal Logic, STL）挖掘区分正确与错误推理的时序模式。具体做法是构建步骤级置信度信号，通过判别式STL挖掘发现可迁移的时序结构，并利用超网络实现问题级参数自适应。该方法在单样本推理下显著提升了校准精度，但其依赖CoT分段且缺乏与语义熵方法的直接对比，泛化性存疑。

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

【IDEA: An Interpretable and Editable Decision-Making Framework for LLMs via Verbal-to-Numeric Calibration ｜可解释与可编辑的LLM决策框架

研究机构：香港科技大学、华为

作者：Yanji He、Yuxin Jiang、Yiwen Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12573)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12573)

> 大语言模型在高风险决策中面临概率校准失效、解释不忠实及无法精确干预的“信任赤字”。现有基于Logit或思维链的方法将内部计算与外部输出强行绑定，导致无法审计或修改决策逻辑。IDEA通过引入语义因子中间层，利用EM算法联合学习言语-数值映射与决策模型参数，将黑盒知识外化为可编辑的白盒参数。该框架在决策准确性上超越GPT-5.2，但因子完备性假设限制了其在开放域复杂推理中的泛化能力。

】

---

【Large Language Models Are Overconfident in Their Own Responses ｜指令微调模型中的“所有权偏差”与推理时校准修正

作者：Mario Sanz-Guerrero、Manuel Mager、Katharina von der Wense

论文原文见 [arXiv](https://arxiv.org/abs/2606.03437)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1510164bcd2a)

> 导读 大语言模型在指令微调后普遍出现校准失效，即模型输出的置信度显著高于其实际正确率，导致高风险场景下的决策不可靠。现有后处理校准方法多依赖重训练或复杂的概率映射，忽略了对话格式本身对置信度评估的干扰。本文切入点在于解耦训练算法与聊天模板的影响，发现模型对自身生成的答案存在系统性的“所有权偏差”，即赋予自身答案更高置信度。通过将该答案在提示中重构为用户输入，本文提出了一种零训练的推理时策略，有效缓解了过度自信。该策略在多个开源模型上验证了有效性，但其对开放式生成任务及长文本推理的适用性仍存疑。

】

---

【NeuroSym-Cal: Bridging the Reasoning-Execution Gap in Code Generation via Hierarchical Calibration ｜神经符号分层校准：代码生成中的置信度去饱和

作者：Peiyang Liu、Yining Wang、Youru Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_286efca23771)

> 推理模型在代码生成中常陷入“自信地犯错”的困境，即系统性错误导致采样输出高度一致，使基于一致性的校准方法失效。现有方法如Self-Consistency（SC）无法区分“稳健正确”与“顽固幻觉”，导致高置信度下的严重误判。本文提出NEUROSYM-CAL，通过融合基于抽象语法树（AST）的外部共识与模型后验自我验证的内部信号，构建非线性校准网络以解饱和置信度。该方法在域外（OOD）基准上显著降低了期望校准误差（ECE），但其依赖额外训练数据且未与最新语义熵方法对比，泛化边界尚存疑。

】

---

【Prompting the Unknown: Understanding Response Uncertainty in Large Language Models ｜提示响应概念模型（PRC）：从信息量到不确定性的因果解耦

作者：Ze Yu Zhang、Arun Verma、Finale Doshi-Velez 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3b894846b09a)

> 大语言模型（LLM）在高风险决策场景中常因提示中任务相关信息不足而产生高方差响应，现有不确定性量化（UQ）方法多聚焦于输出端的熵计算或校准，却忽视了输入端信息量对响应不确定性的根本性影响。本文切入点在于将“提示信息化程度”形式化为控制不确定性的自变量，而非仅将其视为背景条件。通过构建提示-响应概念（Prompt-Response Concept, PRC）模型，论文将响应不确定性分解为提示欠规范、模型质量、任务变异性与语义冗余四个独立来源，并证明前两者随信息量增加而严格递减。该工作为提示工程提供了信息论层面的理论支撑，但其理想化假设限制了在真实黑盒模型中的直接应用边界。

】

---

【QuCo-RAG: Quantifying Uncertainty from the Pre-training Corpus for Dynamic Retrieval-Augmented Generation ｜基于预训练语料统计的动态检索增强生成

作者：Dehai Min、Kailin Zhang、Tongtong Wu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec1f437c42a4)

> 动态检索增强生成（Dynamic RAG）旨在解决大语言模型（LLM）在生成过程中因内部置信度信号不可靠而导致的幻觉问题，现有方法依赖的模型内部信号（如熵、注意力）在长尾知识上系统性失效。本文切入点在于将不确定性量化从主观的内部状态转向客观的外部证据，即利用预训练语料的实体频率与共现统计作为检索触发器。具体做法是构建两阶段检测机制：生成前评估实体频率，生成中验证三元组共现。该方法在跨模型迁移中展现出鲁棒性，但其有效性高度依赖代理语料与目标模型训练数据分布的重叠度，这一边界条件在现有实验中尚未被充分量化。

】

---

【The Confidence Paradox: Unveiling the Latent Discriminative Power of Diffusion Large Language Models in Mathematical Reasoning ｜扩散大语言模型中的校准悖论与结构一致性信号

作者：Yansi Li、Gongshen Liu、Zhuosheng Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_65741e97931c)

> 扩散大语言模型（Diffusion Large Language Models, DLLMs）在数学推理中展现出一种反直觉现象：其原生置信度严重偏离真实概率，却具备远超自回归模型的判别力。现有不确定性量化方法假设置信度必须同时满足校准与判别，导致对DLLM这类新架构的评估失效。本文通过解耦校准与判别，证明DLLM的置信度实为结构一致性代理，并验证了轻量级后处理校准的有效性。这一发现揭示了双向生成机制下的独特失效模式，但其在开放域知识问答中的近乎随机表现，限制了该信号的通用性。

】

---

【Uncertainty Quantification of Large Language Models through Multiple Uncertainty Sources ｜多源不确定性量化框架

作者：Tiejin Chen、Xiaoou Liu、Longchao Da 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e8d21012898)

> 大语言模型在开放式生成中面临“自信地犯错”的困境，传统基于单一信号的不确定性量化方法难以捕捉语义、事实与结构维度的复合变异。现有方法要么孤立处理NLI语义相似度，要么依赖图结构统计，导致信号冗余掩盖真实分歧。MS-UQ通过构建三阶相似度张量并应用张量分解，将异构信号正交解耦，以重建误差作为统一不确定性度量。该框架在集成多源信号上具有结构优势，但缺乏分布无关的统计保证，且在复杂推理基准上的绝对性能未超越当前图结构SOTA。

】
