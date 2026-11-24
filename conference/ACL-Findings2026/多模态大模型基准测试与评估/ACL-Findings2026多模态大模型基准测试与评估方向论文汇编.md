# ACL-Findings2026 · 多模态大模型基准测试与评估方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EmoMM: Benchmarking and Steering MLLM for Multimodal Emotion Recognition under Conflict and Missingness ｜多模态情感识别中的模态冲突诊断与注意力引导

研究机构：华南理工大学

作者：Yueru Sun、Yimeng Zhang、Haoyu Gu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01024)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.01024)

> 导读 多模态情感识别（MER）旨在通过联合建模文本、视觉与声学信号推断人类情感，但真实场景中模态证据常出现矛盾或缺失，导致模型决策漂移。现有方法多停留在描述性评估，缺乏对内部决策机制的量化诊断，且难以在推理阶段动态纠正模态偏好。本文提出EmoMM基准与CHASE机制，通过Shapley值量化模态贡献，并在推理时进行头级注意力引导以重分配证据权重。该工作揭示了视频贡献崩塌现象，但其在通用MLLM任务上的泛化能力及长期时序情感场景下的有效性仍存疑。

】

---

【Empowering Reliable Visual-Centric Instruction Following in MLLMs ｜视觉中心指令遵循评估与数据构建

研究机构：香港科技大学、美国宾夕法尼亚大学

作者：Weilei He、Feng Ju、Zhiyuan Fan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03198)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03198)

> 多模态大语言模型（MLLMs）在指令遵循任务中常依赖文本先验而非视觉证据，导致评估分数虚高且无法反映真实视觉理解能力。现有基准如MM-IFEval仅评估文本模式匹配，忽视了图像中隐含的空间与属性约束，使得模型即使忽略视觉输入也能通过测试。本文通过构建视觉中心的数据集与混合评估协议，将视觉约束显式纳入指令遵循的度量体系。该工作填补了视觉指令遵循评估的空白，但其7B模型实验规模与单一裁判模型依赖限制了结论的普适性。

】

---

【More Images, More Problems? A Controlled Analysis of VLM Failure Modes ｜多图像视觉语言模型失效模式控制分析

研究机构：美国普林斯顿高等研究院、英国伦敦玛丽女王大学

作者：Anurag Das、Adrian Bulat、Alberto Baldrati 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07812)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07812)

> 多图像视觉语言模型（LVLMs）在处理跨图信息聚合时普遍失效，现有基准缺乏对失效根因的细粒度控制与机制诊断。本文通过构建程序化生成的MIMIC基准，隔离了信息分布、干扰项等混淆变量，揭示了模型在深层网络中跨图注意力衰减的架构性缺陷。通过数据合成与层间注意力掩码微调，该方法在保持低计算成本的同时显著提升了跨图推理性能。其价值在于将黑盒评估转化为白盒机制诊断，但缺乏闭源模型对比，且未验证非因果注意力架构下的泛化性。

】

---

【PedagogyBench: A Cognitive-Driven Benchmark for Multimodal Instructional Video Understanding ｜教学视频认知基准

作者：Xiaokang Jin、Jia Zhu、Jingjiang Liu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_379c43b1a268)

> 现有视频理解基准将课堂视频视为事件序列，忽略了教学意图与认知脚手架的深层逻辑，导致模型在“看懂画面”与“理解教学”之间出现能力断层。本文切入点在于构建一个基于教学法阶段分割与认知金字塔评估框架的专用基准，通过双流语义注入与专家修正生成结构化数据。其核心贡献是提出认知保真度分数（Cognitive Fidelity Score, CFS）以诊断模型在感知、理解、应用与诊断四个维度的平衡性。该基准揭示了当前多模态大语言模型（Multimodal Large Language Models, MLLMs）在判别式任务与生成式任务间的显著差距，但其跨语言设置与自建基准的外部效度仍存疑。

】

---

【RATION: Entropy-Driven Task-Adaptive Visual Attention Allocation Framework for Multimodal Reasoning ｜熵驱动任务自适应视觉注意力分配框架

作者：Xingle Xu、Fanheng Kong、Dexian Cai 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45c37346cf0e)

> 多模态大语言模型在计数与OCR等视觉密集任务中常因内部注意力分配与任务需求错配而失效，现有推理时增强方法多依赖外部提示或链式生成，缺乏对模型内部视觉关注机制的显式调控。RATION通过单次前向传播中的层激活变化推断任务类型，并基于注意力熵动态调制关键层的视觉注意力强度，实现训练无关的推理时干预。该方法在四个骨干模型与七个基准上取得一致增益，但其任务分类粒度与熵信号的泛化边界尚待检验。

】

---

【Seek-and-Solve: Benchmarking MLLMs for Visual Clue-Driven Reasoning in Daily Scenarios ｜日常场景视觉线索驱动推理基准

研究机构：大连理工大学、清华大学

作者：Xiaomin Li、Tala Wang、Zichen Zhong 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14041)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14041)

> 多模态大语言模型（Multimodal Large Language Models, MLLMs）在复杂日常场景中常因视觉噪声干扰而推理失效，现有基准多侧重知识检索或基础感知，难以剥离语言先验对推理过程的污染。本文提出 DailyClue，通过构建包含显式视觉线索标注的“问题-线索-答案”三元组，强制模型在思维链（Chain-of-Thought, CoT）中定位决定性视觉证据。该基准揭示了线索提取准确率是模型推理的核心瓶颈，但其在智能体模型上的低效表现及小样本统计显著性存疑，需进一步验证其作为通用推理诊断工具的边界。

】

---

【UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning ｜自适应视觉提示与渐进式检查框架

研究机构：美国东北大学

作者：Yifan Wang、Yun Fu

论文原文见 [arXiv](https://arxiv.org/abs/2605.03950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03950)

> 多模态大语言模型（Large Multimodal Models, LMMs）在处理复杂视觉推理任务时，常因细粒度感知缺失与中间步骤逻辑断裂导致最终答案错误。现有纯文本提示方法难以有效分解图像信息，而单一视觉标记提示又缺乏对推理过程的验证机制。UnAC通过结合问题条件化的自适应视觉提示、图像信息抽象及逐步自我检查，构建了一个无需训练的多模态提示框架。该框架在多个基准上提升了模型表现，但其增益高度依赖骨干模型的底层推理能力，且对特定分割工具的依赖限制了其通用性。

】
