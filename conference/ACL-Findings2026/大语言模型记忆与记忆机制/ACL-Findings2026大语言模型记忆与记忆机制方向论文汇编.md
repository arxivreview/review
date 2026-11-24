# ACL-Findings2026 · 大语言模型记忆与记忆机制方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AnchorMem: Anchored Facts with Associative Contexts for Building Memory in Large Language Models ｜锚定事实与关联上下文的大语言模型记忆框架

研究机构：深圳大学、清华大学

作者：Zhanyu Shen、Sijie Cheng、Zhicheng Guo 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17377)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e7fcebe2f84c)

> 长期交互中，大语言模型（LLM）因状态无记忆特性导致上下文丢失，而现有外部记忆系统通过频繁重写或图索引整合历史，往往牺牲语境完整性或引入噪声链接。本文切入点在于解耦检索单元与生成上下文，将原子事实作为检索锚点，保留原始交互作为不可变生成内容。AnchorMem 通过构建事实-上下文单元与关联事件图，在 LoCoMo 基准上显著优于 LightMem 等基线，验证了该架构在保持细粒度检索与叙事完整性上的有效性，但其对通用实体噪声的规避机制在极端稀疏场景下的鲁棒性仍存疑。

】

---

【Memory Dial: A Training Framework for Controllable Memorization in Language Models ｜记忆压力调控框架

研究机构：美国佐治亚理工学院、美国埃默里大学

作者：Xiangbo Zhang、Ali Emami

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_57d9f516b01d)

> 大语言模型的记忆机制长期被视为训练过程的被动副产物，研究者只能事后检测模型记住了什么，却无法在训练前预设其记忆强度。现有暴露度指标与提取攻击均依赖已训练完成的模型，难以将记忆效应与架构、数据等混杂因素解耦。MEMORY DIAL 通过引入温度锐化目标函数与标准交叉熵的凸组合，将记忆压力转化为可连续调节的独立变量。该框架在六个架构上验证了记忆可控性与泛化稳定性，但其控制粒度局限于训练目标层面，未触及参数空间的直接编辑。

】

---

【MetaMem: Evolving Meta-Memory for Knowledge Utilization through Self-Reflective Symbolic Optimization ｜元记忆引导的外部记忆利用框架

研究机构：美国东北大学、清华大学

作者：Haidong Xin、Xinze Li、Zhenghao Liu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fc0c16e5e4ef)

> 长程人机交互中，外部记忆系统常因碎片化存储破坏事实间的逻辑与时间关联，导致模型在整合多源证据时产生推理错误。现有方案侧重于优化记忆的存储结构或检索精度，却忽视了模型“如何正确使用”已检索到的矛盾或冗余信息。MetaMem 引入自进化的元记忆模块，通过自反思机制将知识利用策略显式化并动态更新。该框架在 LongMemEval 基准上显著优于现有外部记忆系统，但其性能增益高度依赖骨干模型的指令遵循能力与反思质量，且未涉及记忆安全与隐私泄露风险。

】
