# ACL2026 · 基于大语言模型的AI辅导与教育对话方向论文汇编

> 本方向共 6 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EduBench: A Comprehensive Benchmarking Dataset for Evaluating Large Language Models in Diverse Educational Scenarios ｜教育场景大语言模型综合基准

研究机构：北京理工大学

作者：Bin Xu、Yu Bai、Huashan Sun 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6c482754592c)

> 教育领域大语言模型（Large Language Models, LLM）评估长期受限于单一学科与通用NLP指标，无法反映真实教学中师生双向角色的复杂需求。现有基准如EduNLP场景单一且缺乏教育学维度，导致模型在情感支持或个性化辅导等关键场景的能力被低估。本文通过构建覆盖9大场景、4000+上下文的静态Query-Response数据集，并设计12维教育学Rubric体系，实现了从通用能力向教学有效性的评估范式转换。该基准填补了多场景教育评估的空白，但其单轮静态评估模式难以捕捉长程对话中的教学一致性缺陷。

】

---

【Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks ｜对抗性学生攻击下的LLM导师答案泄露鲁棒性评估

研究机构：瑞士洛桑联邦理工学院

作者：Jin Zhao、Marta Knežević、Tanja Käser

论文原文见 [arXiv](https://arxiv.org/abs/2604.18660)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18660)

> 大语言模型（LLM）作为导师时，其默认的“乐于助人”特性与苏格拉底式教学所需的“答案保留”原则存在根本冲突，导致学生在交互中轻易获取完整解而非进行认知建构。现有评估多假设学生是合作者，忽视了学生通过说服或对抗手段主动套取答案的场景，使得导师在真实滥用情境下的脆弱性被低估。本文构建了一个包含六类对抗与说服策略的评估框架，并训练了一个微调的对抗性学生智能体，以系统性地探测和量化不同导师配置下的答案泄露率。该工作填补了教育场景下对抗性鲁棒性评估的空白，但受限于小规模模型测试，其结论在前沿大模型上的普适性仍需进一步验证。

】

---

【MMTutorBench: The First Multimodal Benchmark for AI Math Tutoring ｜多模态数学辅导基准

研究机构：同济大学、复旦大学

作者：Tengchao Yang、Sichen Guo、Mengzhao Jia 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_999aa333ecc9)

> 现有数学基准仅评估模型解题或识别手写公式的能力，却忽略了“诊断学生卡点并引导下一步”这一辅导核心。本文切入点在于构建首个多模态数学辅导基准，将辅导任务分解为洞察、公式化与执行三个维度，并设计题目特定的评分细则。通过评估12个主流多模态大语言模型，揭示了当前模型在“答案范围控制”上的严重缺陷。该基准填补了多模态教学评估空白，但其数据源自视频帧提取，是否完全复现真实课堂的混乱与低质量书写场景仍存疑。

】

---

【Planning-Guided Tutoring with Assessment-Driven Memory for Pedagogical LLM Tutors ｜规划引导的苏格拉底式数学辅导框架

研究机构：北京师范大学

作者：Zechen Li、Qiannan Zhu、Mei Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1823b1165e0c)

> 现有大语言模型（LLM）导师在长程对话中常因缺乏全局步骤规划而陷入碎片化引导或过早泄露答案，导致教学连贯性断裂。ScaffoldLM 通过引入显式步骤级教学计划与评估驱动的记忆机制，将教学行为锚定在可验证的中间目标上，而非依赖隐式上下文。该框架在 BigMath 数据集上实现了 0.785 的数学辅导准确率，并在多项教学指标上超越通用大模型，但其对解题率与教学质量的平衡仍受限于监督微调（SFT）的静态优化特性。

】

---

【Simulated Students in Tutoring Dialogues: Substance or Illusion? ｜模拟学生对话保真度评估与优化

研究机构：美国马萨诸塞大学阿默斯特分校

作者：Alexander Scarlatos、Jaewook Lee、Simon Woodhead 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04025)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_17170e1ddf6a)

> 智能辅导系统（Intelligent Tutoring Systems, ITS）依赖高质量的学生模拟器来训练和评估导师模型，但现有方法缺乏针对单轮对话（turn-level）的参考基准评估指标，导致无法量化模拟学生的行为、认知与语言保真度。本文提出了一套涵盖六个维度的自动化评估框架，并验证了监督微调（SFT）与直接偏好优化（DPO）显著优于提示工程。该工作填补了模拟学生定量评估的空白，但受限于数据规模与解码策略，其在错误保持与响应多样性上仍有明显短板。

】

---

【Your Students Don’t Use LLMs Like You Wish They Did ｜学生行为计算指标框架

研究机构：澳大利亚悉尼大学

作者：Sebastian Kobler、Matthew Clemson、Angela Sun 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aa8f4b7ec716)

> 该方向旨在解决教育大语言模型（LLM）评估中“满意度高但教学无效”的悖论，现有方法依赖主观问卷或单轮响应质量，无法捕捉长程对话中的行为异化。本文切入点在于将教育数据挖掘中的行为分析迁移至LLM对话，通过六维计算指标量化学生使用模式。其核心做法是构建基于零样本LLM分类与规则混合的行为检测框架，验证部署语境对使用行为的决定性影响。该框架填补了过程性评估空白，但其指标对“有效挣扎”与“无效挫败”的区分能力尚存疑。

】
