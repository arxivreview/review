# ACL-Findings2026 · 法律自然语言处理与判决预测方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Chinese Court Simulation with LLM-Based Agents System ｜全流程庭审模拟与双维评估框架

研究机构：清华大学

作者：Kaiyuan Zhang、Jiaqi Li、Yueyue Wu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_17c3e52839ed)

> 法律判决预测长期面临“黑盒判决”与“程序合规”的割裂，现有方法仅模拟辩论片段，缺乏对完整审判流程的还原及过程质量的量化标准。SimCourt 基于中国刑事审判法定程序，构建包含调查、举证、辩论等五阶段的多智能体模拟框架，并引入记忆与策略模块以维持角色一致性。该框架通过生成完整庭审记录而非直接输出判决，实现了判决预测与过程评估的双重目标。实验表明其判决命中率优于基线，但样本量局限与通用模型依赖使其在复杂法域泛化能力上存疑。

】

---

【JudgeMeNot: Personalizing Large Language Models to Emulate Judicial Reasoning in Hebrew ｜法官推理个性化大语言模型

研究机构：以色列内盖夫本-古里安大学

作者：Itay Razumenko、Arnon Sturm、Nir Grinberg

论文原文见 [arXiv](https://arxiv.org/abs/2604.18041)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a7626f12bbf2)

> 法律判决预测长期将法官视为可互换的决策黑盒，忽略了司法推理中个体化的逻辑偏好与修辞结构。现有生成式模型虽能输出判决结果，却难以复现特定法官的“认知指纹”，且缺乏针对低资源语言的个性化验证。本文通过合成-有机对齐管道生成指令数据，结合链式LoRA微调，在希伯来语低资源场景下实现了法官级推理模拟。该框架证明了参数高效微调在捕捉个体推理风格上的可行性，但作者识别准确率的随机性暴露了风格模仿与身份区分之间的深层张力。

】

---

【Less is More: Knowledge-Aware Compression for Long Legal Judgment Prediction ｜知识感知压缩

研究机构：南开大学、哈尔滨工业大学

作者：Fanghao Lou、Qiqi Wang、Guanyu Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cdb84f613065)

> 法律判决预测（Legal Judgment Prediction, LJP）在处理长文本案件事实时，常因大语言模型（LLM）的二次方计算复杂度与关键法律要素稀释而失效。现有架构优化或通用文本压缩方法难以兼顾法律逻辑连贯性与推理效率。本文提出知识感知压缩（Knowledge-Adaptive Compression, KAC）框架，利用法条知识引导语义单元筛选，实现高效长文档推理。该方法在跨法域数据集上显著提升了预测精度并降低了计算成本，但其对法律知识库静态性的依赖及阈值设定的普适性仍存疑。

】
