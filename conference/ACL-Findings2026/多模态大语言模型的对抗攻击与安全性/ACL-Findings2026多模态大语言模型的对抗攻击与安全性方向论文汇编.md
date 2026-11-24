# ACL-Findings2026 · 多模态大语言模型的对抗攻击与安全性方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ECHA: Jailbreaking LVLMs via the Mismatch between Implicit Semantic Reconstruction and Explicit Safety Alignment ｜表情链提示攻击

作者：Chenxing Xu、Junyong Jiang、Zehu Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_26c5868ab4ff)

> 多模态大语言模型（Large Vision-Language Models, LVLMs）的安全对齐机制存在结构性盲区，现有防御主要依赖对显式文本模式的表面级过滤，无法拦截模型内部从碎片化视觉线索中重构出的隐式恶意语义。本文指出这种“隐式语义重构”与“显式安全对齐”之间的失配是核心漏洞，并提出表情链提示攻击（Emoji Chain Hinting Attack, ECHA）。该框架通过将敏感概念解耦为表情符号链与文本掩码，利用良性场景框架引导模型在潜空间内完成恶意意图的自重构，从而绕过护栏。ECHA在7个SOTA模型上实现了超过81%的单次攻击成功率，但其效果高度依赖模型自身的推理深度，且对闭源模型的评估受限于专用安全评估器的判定标准。

】

---

【Hard to Read, Easy to Jailbreak: How Visual Degradation Bypasses MLLM Safety Alignment ｜视觉退化引发的多模态大语言模型越狱漏洞

研究机构：西湖大学、美国加州大学默塞德分校

作者：Zhixue Song、Boyan Han、Yiwei Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.07250)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07250)

> 视觉上下文压缩技术通过降低图像分辨率来减少视觉Token开销，但这一标准操作意外削弱了多模态大语言模型的安全对齐机制。现有防御多依赖对抗优化或语义操纵，忽略了自然退化对模型内部认知资源的挤占效应。本文提出“认知过载”假设，并通过“结构化认知卸载”策略强制串行推理以恢复安全。该工作揭示了效率与安全间的隐性冲突，但其防御机制在复杂视觉推理场景下的泛化能力仍存疑。

】

---

【Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation ｜对抗走私攻击（ASA）与 SMUGGLEBENCH 基准

研究机构：中国科学院大学、美国华盛顿大学

作者：Zhiheng Li、Zongyang Ma、Yuntong Pan 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06950)

> 多模态大语言模型（MLLMs）作为内容审核员时，攻击者利用人类与AI的感知差异，将有害内容嵌入良性视觉载体以逃避检测，这一威胁被称为对抗走私攻击（Adversarial Smuggling Attacks, ASA）。现有越狱研究聚焦于诱导模型生成有害输出或分类错误，忽视了“模型看不见”这一更隐蔽的绕过路径，导致审核系统在真实场景下存在系统性盲区。本文通过构建包含9种走私技术的专用基准 SMUGGLEBENCH，量化了主流模型在感知与推理阶段的脆弱性，并初步验证了思维链（CoT）与监督微调（SFT）的防御局限。该工作揭示了SOTA模型在内容审核中高达90%以上的攻击成功率，但其防御策略仅停留在初步探索阶段，未能解决根本性的感知瓶颈。

】

---

【MTMCS-Bench: Evaluating Contextual Safety of Multimodal Large Language Models in Multi-Turn Dialogues ｜多轮多模态上下文安全基准

研究机构：美国圣母大学、美国加州大学洛杉矶分校

作者：Zheyuan Liu、Dongwhi Kim、Yixin Wan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06757)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06757)

> 多模态大语言模型（Multimodal Large Language Models, MLLMs）在真实部署中面临的核心安全挑战，已从单轮对抗攻击演变为多轮交互中意图的渐进式演变与上下文重构。现有安全评估基准多聚焦于单轮静态输入，无法捕捉恶意意图在多轮对话中通过良性提问逐步升级，或在初始恶意意图下伪装成无害追问的隐蔽模式。MTMCS-Bench 提出了一种包含升级风险与上下文切换风险的双模式多轮多模态评估框架，通过配对安全与不安全对话及多模态/单模态对照，量化模型在意图识别、安全意识与有用性之间的动态平衡。该基准揭示了当前防御机制在多轮上下文中的系统性失效，为动态安全对齐提供了细粒度的诊断工具，但其依赖大语言模型作为评判者可能引入的评分偏差仍需进一步验证。

】

---

【SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models ｜解码级动态重排与模态对齐：SafeSteer 的多模态安全防御机制

研究机构：清华大学、上海交通大学

作者：Xinyi Zeng、Xue Yang、Jingyuan Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11716)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11716)

> 多模态大语言模型（MLLMs）面临视觉通道绕过文本安全护栏的结构性威胁，现有防御多依赖高成本微调或低效的输入/输出重写，导致泛化性差且损害模型效用。SafeSteer 切入点在于挖掘 MLLMs 在解码阶段固有的有害性判别能力，通过轻量级探针实时重排候选词，并引入模态语义对齐向量（MSAV）弥合视觉与文本的安全感知差距。该方法以极低的计算开销实现了显著的安全提升，但其对静态向量的依赖及跨骨干泛化性仍存疑。

】

---

【StructBreak: Structural Cognitive Overload-Induced Safety Failures in MLLMs ｜结构认知过载引发的多模态大语言模型安全失效

研究机构：北京邮电大学、中国科学院

作者：Yang Luo、Xinran Liu、Tiantian Ji 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.25534)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25534)

> 多模态大语言模型（MLLMs）在解析复杂图表时，其结构推理能力与安全对齐机制存在资源竞争，导致安全护栏在深度推理中失效。现有防御多针对表面符号或像素扰动，无法应对高维拓扑解析引发的内部注意力漂移。本文提出结构认知过载（SCO）概念，并构建黑盒攻击框架StructBreak，利用视觉知识图谱（VKG）诱导模型进入“解析-执行”模式以挤占安全注意力。该研究揭示了“能力-脆弱性悖论”，即推理能力越强越易受结构攻击，但样本量与评估协议的局限性使其结论的普适性存疑。

】

---

【When Helpers Become Hazards: A Benchmark for Analyzing Multimodal LLM-Powered Safety in Daily Life ｜日常隐性风险识别基准

作者：Xinyue Lou、Xu Jinan、Jingyi Yin 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04043)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_678ff3dbaf31)

> 多模态大语言模型（Multimodal Large Language Models, MLLMs）在作为日常助手时，常因无法关联视觉细节与潜在危害而误导用户做出危险决策，这一“安全感知失败”源于视觉与文本嵌入在安全语义空间中的分布差异。现有基准多聚焦于对抗性越狱攻击，缺乏对非对抗性、真实生活场景中隐性风险的量化评估，且传统“拒绝即安全”的评估范式无法区分模型是真正识别了风险还是仅触发了过度拒绝。本文构建了包含2,013个真实图文样本的SaLAD基准，并提出基于安全警告生成的评估框架，要求模型解释风险而非简单拒答。该工作揭示了现有模型在真实场景下的严重安全盲区，但其评估指标与对抗攻击防御指标不可直接比较，且未验证专用防御方法的有效性。

】
