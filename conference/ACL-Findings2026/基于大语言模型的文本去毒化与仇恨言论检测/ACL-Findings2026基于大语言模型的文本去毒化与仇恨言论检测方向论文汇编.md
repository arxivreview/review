# ACL-Findings2026 · 基于大语言模型的文本去毒化与仇恨言论检测方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Survey of Toxicity Mitigation Strategies for Multilingual Language Models ｜多语言大语言模型毒性检测与缓解策略综述

研究机构：印度理工学院、美国弗吉尼亚大学

作者：Soham Dan、Himanshu Beniwal、Thomas Hartvigsen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_321db5c8f158)

> 多语言大语言模型（LLM）在跨语言应用中常因文化错位与数据偏差生成毒性内容，而现有安全对齐机制高度依赖英语中心范式，导致低资源语言场景下毒性残留与误判频发。本文切入点在于系统梳理多语言特有的威胁模型（如语言切换越狱、翻译中介攻击），并构建覆盖数据、解码、对齐与表示干预的全景式分类法。通过整合威胁模型、任务设置与缓解机制，本文揭示了英语中心对齐在多语场景下的系统性失效。其价值在于提供了多语去毒的结构化认知框架，但作为综述缺乏统一基准下的定量对比，且对因果推断等新兴技术路线在多语下的适用性讨论不足。

】

---

【CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification ｜因果头选择与干预语言模型去毒

作者：Yian Wang、Yuen Chen、Agam Goyal 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14602)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14602)

> LLM生成毒性源于预训练语料污染，现有解码时干预或微调方法常因依赖相关性启发式而误伤良性语言，或在抑制毒性时破坏语义连贯性。本文切入点在于区分“相关”与“因果”，利用概率必要性与充分性（Probability of Necessity and Sufficiency, PNS）定位对毒性生成既必要又充分的最小注意力头集合。通过全局/局部推理时干预及PNS引导微调，在保留流畅度的前提下实现精准去毒。该方法在受控反事实基准上优于相关性基线，但其因果假设在复杂语境下的稳定性及与主流微调范式的横向对比缺失，限制了其普适性结论。

】

---

【Danger Depends on the Mind: A Theory-of-Mind Grounded Dataset and Model for Context-Dependent Dangerous Speech ｜心智理论驱动的危险言论检测

作者：Yuanchen Shi、Longyin Zhang、Guodong Zhou 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_88c1d18082e7)

> 现有危险言论检测将文本视为孤立单元，依赖二元标签，无法区分同一句话在不同说话者心理状态下截然不同的风险等级。本文切入点在于引入认知科学中的心智理论（Theory-of-Mind, ToM），将说话者的情绪、意图、行动等隐性状态作为显式上下文输入。通过构建包含79K文本-语境对的中文基准ToM-DS，并设计轻量级模型ToMGuard，利用动态注意力机制自适应加权ToM维度。该工作验证了语境依赖检测的必要性，但其合成数据主导的构建方式与单一中文场景限制了结论的普适性。

】

---

【DART: Mitigating Harm Drift in Difference-Aware LLMs via Distill-Audit-Repair Training ｜差异感知大模型中的危害漂移缓解：蒸馏-审计-修复训练

研究机构：美国埃默里大学、美国麻省理工学院

作者：Ziwen Pan、Zihan Liang、Jad Kabbara 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16845)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22474a9b3e09)

> 安全对齐常迫使大语言模型在需要区分群体差异的场景中保持“身份盲”，导致事实错误或过度拒绝。现有微调方法虽能提升决策准确性，却引发“危害漂移”——推理理由的有害性随准确性提升而增加，且联合优化无法兼顾两者。DART通过分阶段的蒸馏、审计与修复流程，在提升差异感知分类准确性的同时，针对性地修复了推理理由中的有害内容。该方法在Llama-3-8B上将准确率从39.0%提升至68.8%，但其在通用毒性基准上的表现混合，暴露了评估器对反话语的脆弱性。

】

---

【Explain the Flag: Contextualizing Hate Speech Beyond Censorship ｜混合词汇库与LLM驱动的仇恨言论解释性检测

研究机构：希腊雅典国立技术大学

作者：Jason Liartis、Eirini Kaldeli、Lamprini Gyftokosta 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14970)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1c5a99a1c85c)

> 在线平台对仇恨言论的自动化审核长期面临“黑盒判定”困境，用户无法知晓内容被移除的具体原因，导致信任缺失与申诉困难。现有基于大语言模型（LLM）的检测系统虽能捕捉深层语义，但在低资源语言中缺乏对新兴侮辱性词汇的显式知识，且解释往往脱离具体语境。本文提出一种混合架构，通过构建英、法、希腊三语专用词汇库作为外部接地资源，结合双管道LLM推理，实现仇恨言论的精准检测与语境化解释。该方案在自建多语言基准上优于纯LLM基线，但其对词汇库覆盖率的依赖及希腊语性能衰减机制尚存疑。

】

---

【Penetrating Linguistic Disguises: A Slang-aware Label-Aligned Framework for Fine-Grained Toxicity Extraction in Chinese Hate Speech Detection ｜结构感知标签对齐框架

研究机构：同济大学、中国科学院

作者：Wei Liu、Xiaoliang Chen、Duoqian Miao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a6400e62e918)

> 中文社交媒体中广泛存在的拼音缩写与同音字伪装，使得基于关键词的传统毒性检测失效，而生成式大语言模型虽具备语义理解能力，却在严格的跨度边界匹配上频繁出现漂移与幻觉。现有判别式网格标记方法虽能保持边界敏感性，但无法处理同一目标-论证对同时涉及性别歧视与种族歧视等多标签冲突的场景。SLAF通过结构-语义词典融合模块解析伪装语义，并利用标签解耦体积标记将二维网格扩展至三维空间以分离重叠类别，在STATE ToxiCN基准上实现了30.09%的Hard-F1，较最佳微调LLM基线提升5.82%。该框架验证了判别式结构化提取在精确匹配任务上的优势，但其对词典覆盖率的依赖及未对比其他判别式基线的情况，限制了其泛化能力的评估。

】

---

【Prompting Across Time: Evaluating LLMs on Historical and Contemporary Offensive Language ｜跨时代仇恨言论检测中的提示工程归因分析

作者：Sanne Hoeken、Sophie Jasmin Spliethoff、Silke Schwandt 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19e5046672fe)

> 导读 仇恨言论检测（HSD）长期局限于当代社交媒体语料，忽视了语言攻击性在历史文本中的演变与形态差异，导致模型在跨时代场景下的泛化能力缺乏实证依据。现有方法多依赖微调或解码干预，难以量化提示设计中各组件对历史语境理解的独立贡献，且缺乏对早期现代英语（EModE）这一低资源、高语境依赖领域的系统性评估。本文通过模块化提示设计，量化定义丰富度、上下文、规则与示例对LLM在EModE及现代文本上检测性能的边际贡献，揭示了标注清晰度对性能的压倒性影响。该研究填补了历史NLP与HSD交叉领域的空白，但零样本设定下的性能上限及提示脆弱性限制了其直接部署价值。

】

---

【Self-Explaining Hate Speech Detection with Moral Rationales ｜道德理由监督注意力

研究机构：智利大学、美国南加州大学

作者：Francielle Vargas、Jackson Trager、Diego Alves 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_69471981d99e)

> 仇恨言论检测模型长期依赖表层词汇特征，导致在讽刺、隐喻等隐式表达及跨文化语境下误报率高且缺乏可解释性。现有事后解释方法（如LIME、SHAP）计算昂贵且与模型决策过程脱节，而基于仇恨理由的注意力对齐方法（SRA）受限于词汇层面的理由，难以捕捉深层道德推理。本文提出监督道德理由注意力（SMRA），将道德基础理论（MFT）标注的道德理由掩码直接作为注意力监督信号嵌入训练目标，实现内在可解释性。该方法在巴西葡萄牙语数据集上显著提升了解释忠实度与合理性，但预测性能提升微弱，且未验证跨语言泛化能力。

】

---

【Speak No Evil, Just Prompt: Low-resource Multilingual Toxic Speech Detection with Audio Language Model ｜多语言毒性语音检测的软提示适配

研究机构：天津大学、深圳大学

作者：Mingzi Zuo、Lei Zhang、Hailiang Sun 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_87751ac7b9ae)

> 现有毒性语音检测依赖ASR转录，在低资源语言与复杂口音下因转录错误导致声学线索丢失，且端到端模型难以平衡跨语言泛化与特定语言适配。本文构建覆盖53种语言及口音的PolySpeechTox数据集，并提出SoftPrompt-TSD框架，通过分解式软提示在冻结音频语言模型上实现参数高效适配。该方法在微平均ROC-AUC上达到98.07%，显著优于基线，但其性能高度依赖已知语言标签，对未知口音的泛化能力存疑。

】

---

【ToxiTrace: Gradient-Aligned Training for Explainable Chinese Toxicity Detection ｜中文毒性内容检测中的梯度对齐跨度提取

研究机构：华东师范大学

作者：Boyang Li、Hongzhe Shou、Yuanyuan Liang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12321)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a036e9981b4d)

> 中文毒性检测长期困于句级分类与细粒度证据定位的割裂：编码器模型分类高效但归因碎片化，大语言模型（LLM）能提取连贯跨度却推理成本高昂且分类性能不稳定。ToxiTrace 抓住中文字符级分词导致梯度信号分散这一被忽略的技术痛点，通过训练时梯度约束与对抗推理对比学习重塑编码器内部敏感度分布，使后验归因直接输出人类可读的连续毒性跨度。该方法在保持编码器推理效率（约2分钟）的同时，跨度提取F1达77.90%，接近LLM水平，但其弱监督标注依赖外部LLM，且未验证对抗鲁棒性。

】
