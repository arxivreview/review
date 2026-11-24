# ACL-Findings2026 · 医学视觉问答方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Evaluating Large Vision Language Models on Bangla Medical Visual Question Answering ｜孟加拉语医学视觉问答基准与模型评估

作者：Rafid Ahmed、Intesar Tahmid、Mir Sazzat Hossain 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f75f5373d5a3)

> 现有医学视觉问答（Med-VQA）基准严重依赖英语，导致低资源语言场景下的多模态推理能力无法被有效量化。通用大视觉语言模型（LVLM）在缺乏领域适配时，面对非英语医学影像常出现严重的视觉-语言对齐失效。本文通过构建包含7,000对临床验证问答的BanglaMedVQA数据集，并系统评估九种主流LVLM在零样本、思维链（CoT）及低秩适应（LoRA）微调下的表现，揭示了模型在细粒度诊断推理上的显著短板。该工作填补了孟加拉语医学VQA的空白，但其依赖LLM翻译生成的数据管线可能引入系统性偏差，且未解决模型在专业诊断类别上的根本性推理缺陷。

】

---

【MedKInstruct: A Multimodal Knowledge Graph Based Framework for Multi-Hop and Hard-Negative Instruction Data Synthesis in MedVQA ｜多模态医学知识图谱驱动的指令数据合成

作者：Yinan Wu、Jihang Jin、Xuhao Bao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a59a8ff9b3b)

> 医学视觉问答（Med-VQA）的核心瓶颈在于通用大视觉语言模型（LVLM）缺乏深层医学知识推理能力，导致生成答案常脱离病理逻辑。现有指令数据合成方法仅基于图像描述生成视觉属性问答，无法覆盖疾病因果、系统归属等知识级推理，限制了模型在复杂临床场景下的表现。本文提出 MedKInstruct，通过引入多模态医学知识图谱（MMKG）指导 LVLM 合成多跳与硬负例指令数据，并设计基于 MMKG 路径的强化学习奖励函数，使模型在训练阶段显式学习中间医学知识。该方法在 Slake 和 VQA-RAD 上分别提升 4.16% 和 4.50%，但 MMKG 的静态结构与实体对齐误差可能引入知识偏差，其鲁棒性边界尚待检验。

】
