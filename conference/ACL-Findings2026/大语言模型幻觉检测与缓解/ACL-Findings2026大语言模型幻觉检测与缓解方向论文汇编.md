# ACL-Findings2026 · 大语言模型幻觉检测与缓解方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AHEAD: Attention Head Energy-Aware Dynamics for Hallucination Mitigation in MLLMs ｜注意力头能量感知动态重加权

作者：Jiale Chang、Ying Li、Siliang Tang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a761e994c9e6)

> 多模态大语言模型（MLLM）在生成图像描述时，常因语言先验覆盖视觉证据而产生幻觉。现有解码干预方法多将幻觉视为全局分类错误，通过对比解码或Logits调整进行静态抑制，忽略了注意力头在推理过程中的异质性动态行为。AHEAD从能量场视角重新定义幻觉为“轨迹逃逸”，通过训练轻量级潜在网络量化每个注意力头的视觉接地与语言先验贡献，并在推理时动态重加权以抑制幻觉。该方法在免微调基座模型的前提下显著降低了幻觉率，但其依赖COCO标注训练的泛化边界尚待验证。

】

---

【Beyond Output Confidence: Epistemic-Aware Hallucination Detection with Answer-Level Signals ｜答案级内在认知（AIC）：基于认知边界稳定性的二维幻觉检测

作者：Jieran Li、Xiuyuan Hu、Yang Zhao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6e914da831a3)

> 大语言模型在知识边界外常生成高置信度错误答案，即低熵幻觉，导致传统基于概率尖锐度的检测器失效。现有黑盒方法将输出不确定性等同于幻觉风险，无法区分“边界内模糊”与“边界外自信”，而白盒探针又依赖内部访问权限。本文提出答案级内在认知（Answer-level Intrinsic Cognition, AIC），通过多次随机解码的答案语义集中度估计模型可知性，并将其作为分母校准一维不确定性，构建无需训练、无需外部知识的二维检测分数。该方法在三个基准上稳定超越一维基线，但绝对性能仍低于白盒SOTA，且其“一致性即可知性”的假设在极端对抗场景下的鲁棒性存疑。

】

---

【CausalGaze: Unveiling Hallucinations via Counterfactual Graph Intervention in Large Language Models ｜因果图干预幻觉检测

研究机构：国防科技大学

作者：Linggang Kong、Lei Wu、Yunlong Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11087)

> 大语言模型（LLM）在生成事实性内容时，常因内部表征中的噪声关联产生高置信度幻觉，传统白盒探测方法仅能捕捉表层统计相关，无法区分结构性鲁棒知识与脆弱关联模式。CausalGaze 将隐藏状态与注意力图建模为动态因果图，通过梯度引导的反事实干预剥离噪声边，实现从被动观察到主动干预的范式转变。该方法在 TruthfulQA 上较前驱 HaluGNN 提升 5.2% AUROC，但实验局限于 7B 规模开源模型，未验证因果干预在更大规模或闭源模型上的泛化性。

】

---

【Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps ｜基于注意力图的语音大模型幻觉推理时检测

研究机构：英国爱丁堡大学

作者：Jonas Waldendorf、Bashar Awwad Shiekh Hasan、Evgenii Tsymbalov

论文原文见 [arXiv](https://arxiv.org/abs/2604.19565)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19565)

> 语音大模型（SpeechLLM）在转录和翻译中会产生流畅但无依据的幻觉内容，现有检测手段依赖金标准输出或多次采样，成本高且无法在线部署。本文切入点在于利用模型内部注意力头在生成幻觉时表现出的特定退化模式，构建轻量级分类器。具体做法是提取四种音频特定注意力指标，训练逻辑回归模型在推理时实时判别。该方法在域内自动语音识别（ASR）任务上显著优于不确定性基线，但跨任务泛化能力极弱，其通用性存疑。

】

---

【Efficient Hallucination Detection in Automatic Code Generation ｜代码生成中的行级幻觉检测

作者：Georgii Andriushchenko、Roman Garaev、Lyudmila Rvanova 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_973296e57410)

> 大语言模型生成的代码常出现语法正确但逻辑错误的“幻觉”，现有检测手段多停留在整段代码层面，无法定位具体错误行，阻碍了自动化调试与自我修正。本文切入点在于利用模型内部表征构建行级监督检测器，通过Diff算法自动标注训练数据，以Transformer编码器聚合Token特征至行级。该方法在多个开源代码模型上显著优于无监督基线，但其对代码风格差异的敏感性限制了泛化能力，且未验证在闭源模型上的有效性。

】

---

【FaithLens: Detecting and Explaining Faithfulness Hallucination ｜FaithLens：基于规则强化学习的忠实性幻觉可解释检测

研究机构：清华大学、复旦大学

作者：Shuzheng Si、Qingyi Wang、Haozhe Zhao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.20182)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20182)

> 导读 忠实性幻觉指模型生成内容与给定上下文文档不一致，是检索增强生成（RAG）等应用的核心风险。现有检测方案要么依赖高成本大模型进行黑盒判断，要么训练专用小模型但仅输出二分类标签，缺乏可解释性且跨任务泛化能力不足。本文提出 FaithLens，通过合成数据过滤、监督微调（SFT）冷启动及基于规则强化学习（RL）的两阶段训练，使 8B 参数模型在检测精度的同时生成高可信度解释。该方法在 12 个任务上超越了 GPT-5.2 等前沿大模型，但其解释质量评估依赖特定新手模型，且未与白盒内部表征探测方法直接对比，其通用性边界尚存疑问。

】

---

【Hallucinations as Orthogonal Noise: Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization ｜动态上下文正交化（DCO）：基于几何对齐的推理时幻觉抑制

研究机构：中国科学技术大学、清华大学

作者：Mingkuan Zhao、Wentao Hu、Tianchen Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03022)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03022)

> 大语言模型在生成过程中常因内部表征偏离上下文事实而产生幻觉，现有解码干预方法多依赖静态向量或Logit层对比，难以区分必要的语义多样化与有害噪声，导致在提升忠实性的同时损害参数知识检索能力。本文基于线性表示假设，将幻觉形式化为残差流中偏离上下文流形的正交噪声，提出动态上下文正交化（Dynamic Contextual Orthogonalization, DCO）方法，通过逐层Z-Score动态门控机制选择性衰减异常正交分量。该方法在Llama-3系列模型上实现了上下文忠实性与知识保留的帕累托优化，但其对纯参数知识检索场景下正交性定义的适用性仍存疑。

】

---

【Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models ｜扩散大语言模型幻觉模式与失败机制

作者：Zhengnan Guo、Fei Tan

论文原文见 [arXiv](https://arxiv.org/abs/2604.10556)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_97f0c0e1abba)

> 扩散大语言模型（dLLM）作为非自回归生成范式，其双向可见性理论上应缓解幻觉，但实际可靠性未知。现有研究聚焦于自回归模型（AR-LLM）的幻觉检测，缺乏对dLLM生成机制特异性失效模式的系统量化。本文通过受控对比实验，揭示dLLM在知识召回、长文本一致性及边界识别上的系统性缺陷，并归因于去噪动态中的结构刚性。该研究填补了非自回归范式下的可靠性评估空白，但受限于预训练权重差异，无法完全隔离生成范式与参数知识的贡献。

】

---

【PretrainRL: Alleviating Factuality Hallucination of Large Language Models at the Beginning ｜预训练强化学习

作者：Langming Liu、Kangtao Lv、Haibin Chen 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8de86936e7af)

> 大语言模型在生成流畅文本时频繁产生事实性错误，即幻觉，这严重阻碍了其在医疗、法律等高风险领域的可靠部署。现有方案多依赖外部知识库核查或多次采样一致性验证，思路直观但受限于高昂的计算成本与有限的知识覆盖范围；当高置信度幻觉暴露出传统概率信号的失效后，研究范式发生关键转折，从黑盒外部验证转向白盒内部表征探测，利用隐藏状态中的可解码信号实现实时检测。本文指出事实性幻觉的根源在于预训练语料分布失衡导致的“低概率真值”与“高概率假值”共存，提出在预训练阶段引入直接偏好优化以重塑概率分布，通过“去偏然后学习”原则为真值腾出记忆空间。该框架在 PopQA 等基准上显著提升了准确率，但其效果是否伴随通用语言能力的退化，以及负采样策略在极端长尾知识下的鲁棒性，仍存疑。

】

---

【PROBE: PROcess-Based BEnchmark for Hallucination Detection ｜过程式幻觉检测基准

研究机构：香港中文大学

作者：Yu Zhang、Peter Belcak、Shizhe Diao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1c0f2d9c7be0)

> 现有幻觉检测基准仅输出“是否包含幻觉”的二元结果，无法诊断模型在长文本中具体哪一步推理失效。本文切入点在于将检测解耦为声明分解、证据查找、证据评估与定位四个独立认知阶段，构建首个过程式评测框架。通过合成注入幻觉的维基百科语料，PROBE 揭示了证据查找是主要性能瓶颈，且过程式评估的召回率显著高于一步式提示。该工作确立了细粒度诊断的评测新范式，但其黑盒多步推理的高延迟限制了实时部署，且未与白盒内部表征方法直接对比。

】
