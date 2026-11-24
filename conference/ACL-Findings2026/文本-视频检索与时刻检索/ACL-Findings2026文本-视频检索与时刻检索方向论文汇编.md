# ACL-Findings2026 · 文本-视频检索与时刻检索方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EgoMemory: Memory-Augmented Personalized Retrieval for Long-Context Egocentric Video ｜记忆增强型第一人称长视频检索

研究机构：中国科学院、中国科学院大学

作者：Yuanmin Tang、Jue Zhang、Xiaoting Qin 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9a108e0f3b82)

> 第一人称视频检索面临的核心困境是查询高度依赖用户私有历史，而现有通用检索模型缺乏对“个人对象”的显式建模能力。本文切入点在于将离线的个人记忆库构建与在线的反思式推理相结合，以解决长时程场景下的意图歧义。具体做法是构建包含165,795个对象标注的EgoMemory基准，并提出免训练的EgoRetriever框架，利用多模态大语言模型（MLLM）生成目标描述进行检索。该工作验证了结构化记忆对个性化检索的增益，但其对闭源API的依赖及记忆库构建的静态性限制了其在隐私敏感场景下的直接落地。

】

---

【LEAF: Towards Lightweight Explainable Hateful Video Detection via Self-Grounding CoT Guided Stage-Wise Distillation ｜轻量级可解释仇恨视频检测框架

作者：Jian Lang、Rongpei Hong、Meihui Zhong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2689ac33e8ea)

> 仇恨视频检测（Hateful Video Detection, HVD）旨在从多模态视频中识别有害内容，但现有方法多为黑盒模型，缺乏对预测决策的可解释性，削弱了内容审核系统的可信度。大型多模态模型（Large Multimodal Models, LMMs）虽能生成解释，但存在严重的良性预测偏差且计算开销大，难以部署；小型多模态模型（Small Multimodal Models, SMMs）部署高效但缺乏复杂语义理解能力。本文提出LEAF，通过自接地思维链（Self-Grounding Chain-of-Thought, SG-CoT）引导LMM生成无偏解释监督信号，并采用分阶段蒸馏范式训练SMM，实现轻量级且可解释的HVD。该方法在三个基准上取得了领先的检测性能与解释质量，但其对LMM教师模型质量的依赖及解释忠实性的量化评估边界尚存疑。

】

---

【MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding ｜多智能体视频检索框架

研究机构：南开大学、清华大学

作者：Jie Zhang、Qilang Ye、Hao Zhou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.09641)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09641)

> 文本-视频检索（Text-Video Retrieval, TVR）旨在从海量视频中定位语义匹配片段，但主流嵌入匹配范式受限于查询与视频间的语义不对称及全库遍历的计算冗余。现有微调方法依赖任务特定标注，而单智能体推理方法存在认知过载导致的“隧道视野”问题。MAVIS 通过结构化语义库与多智能体协作辩论机制，将检索重构为粗到细的推理过程，在零样本设置下实现了高精度与低计算成本的平衡。该框架验证了结构化推理优于暴力扫描的有效性，但其对预训练大模型推理延迟的依赖及阈值敏感性仍构成部署瓶颈。

】
