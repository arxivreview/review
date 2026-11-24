# ACL-Findings2026 · 语言模型的差分隐私方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DP3: Differentially Private Prompt Perturbation for Multi-turn LLM Inference ｜多轮对话差分隐私提示词扰动

研究机构：西安电子科技大学

作者：Lele Zheng、Chao Zhang、Feiyang Yuan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_225250accbd9)

> 大语言模型（LLM）在云端黑盒 API 部署中面临用户提示词泄露风险，现有差分隐私（DP）方法多假设单轮交互，无法处理多轮对话中重复 token 导致的隐私预算线性累积与语义断裂。本文提出 DP3 框架，通过引入扰动映射表复用历史扰动，并结合注意力驱动的上下文效用函数与两阶段分桶指数机制，在保持形式化隐私保证的同时维持跨轮次语义连贯性。该方案在长程多轮场景下实现了更优的隐私-效用权衡，但其对 LDP 独立性假设的潜在挑战及缺乏多轮专用基线对比，限制了结论的普适性验证。

】

---

【LLEOT: A Privacy-Enhancing Offsite Tuning Framework via Loss Landscape Elevation ｜损失景观提升离线调优

研究机构：华南理工大学、香港科技大学

作者：Jin Zhong、Jinglin Liang、Tongtong Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fb028e2badad)

> 离线微调场景下，模型所有者与数据所有者互不信任，传统模拟器方法虽保护了参数与数据隐私，却因保留原模型推理能力而泄露“模型能力隐私”。现有基于知识蒸馏或选择性剪枝的模拟器构建方案无法在消除推理能力的同时维持梯度一致性，导致适配器迁移失效。本文提出损失景观提升（LLE），通过强制模拟器损失高于原模型固定边际，在理论上保证困惑度指数级放大且梯度方向不变，从而在禁用模拟器推理能力的同时确保软提示可迁移至原模型。该方法在多个基准上实现了优于随机初始化的隐私保护与接近全量微调的效用，但其确定性隐私保证缺乏对动态攻击者先验的适应性验证。

】

---

【Private Seeds, Public LLMs: Realistic and Privacy-Preserving Synthetic Data Generation ｜真实感与隐私保护的合成数据生成

作者：Qian Ma、Sarah Rajtmajer

论文原文见 [arXiv](https://arxiv.org/abs/2604.07486)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07486)

> 隐私合成数据生成旨在替代无法共享的敏感文本，但现有梯度微调法受限于API访问与高计算成本，纯提示法则难以保留原始数据的分布特征。本文提出RPSG，通过“抽象-选择-生成-精炼”四阶段流水线，将私有数据作为种子引导大语言模型生成高保真合成文本。该方法在候选选择阶段引入形式化差分隐私机制，在保持语义连贯性的同时显著降低成员推断攻击风险。尽管其在效用与隐私权衡上优于基线，但缺乏与最新分布保真度SOTA的直接数值对比，且NLL过滤机制对骨干模型分布特性的依赖尚不明确。

】
