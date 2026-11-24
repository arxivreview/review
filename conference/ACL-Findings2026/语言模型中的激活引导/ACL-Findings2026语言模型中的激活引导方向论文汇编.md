# ACL-Findings2026 · 语言模型中的激活引导方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Analysing the Safety Pitfalls of Steering Vectors ｜激活转向的安全副作用：拒绝子空间几何干扰机制分析

研究机构：德国慕尼黑工业大学

作者：Yuxiao Li、Alina Fastowski、Efstratios Zaradoukas 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1b8b69015f8b)

> 导读 激活转向旨在通过推理时修改隐藏状态以低成本控制大语言模型行为，但现有方法多聚焦于行为增强，忽视了其对安全对齐的潜在侵蚀。本文切入点在于揭示转向向量与模型内部拒绝机制的几何重叠如何因果性地导致越狱成功率上升。作者通过构建拒绝方向代理并执行方向消融，建立了余弦相似度与安全退化幅度间的定量预测模型。该工作为安全审计提供了机制解释，但其依赖单一维度拒绝方向代理的假设是否足以覆盖复杂安全行为，仍存疑。

】

---

【CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark ｜跨语言生成控制基准与无监督转向优势验证

作者：Daniil Gurgurov、Yusser Al Ghussin、Tanja Baeumel 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_79f69db10224)

> 多语言大语言模型在推理时难以稳定切换至目标语言，现有激活引导方法缺乏跨语言标准化评估协议，导致无法量化不同语言下的控制有效性。本文切入点在于构建覆盖32种语言的平行问题基准，并系统对比提示工程与多种表示级干预策略。通过引入语言强制成功率与语义相关性调和平均指标，本文验证了残差流均值差向量（DiffMean）在无监督场景下显著优于有监督探针及稀疏自编码器方法。该基准填补了多语言转向评估空白，但其结论局限于特定模型架构，且未探讨低资源语言中线性表示假设的失效边界。

】

---

【Role-Sensitive Neurons: A Neuron-Level Gain Control Mechanism for Confidence Steering ｜角色敏感神经元：置信度增益控制机制

作者：Peiwen Huang、Chih-Hao Hsu、Tzu-Hung Huang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18eb653d1404)

> 大语言模型（LLMs）在角色扮演提示下表现出的性能波动，常被归因于知识检索能力的差异，但这一解释忽略了模型内部“行动意愿”的独立调控机制。现有激活引导方法多聚焦于毒性或真实性等语义属性，缺乏对决策阈值这一元认知维度的干预手段，导致无法区分“不知道”与“不敢答”。本文通过识别并操控稀疏的角色敏感神经元（Role-Sensitive Neurons, RSNs），将置信度调控从提示工程层面下沉至神经基底层面，实现了对弃权行为的因果控制。这一发现揭示了置信度与知识表征的解耦几何，但其在知识匮乏模型中可能诱发“无根据的确定性”，边界尚待厘清。

】

---

【Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection ｜选择性转向：基于判别层选择的范数保持控制

作者：Quy-Anh Dang、Chris Ngo

论文原文见 [arXiv](https://arxiv.org/abs/2601.19375)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19375)

> 激活转向旨在不更新权重的前提下，通过修改内部隐藏状态来精准控制大语言模型（LLM）的行为，以替代高成本的微调。现有几何旋转方法虽解决了线性加法的强度失控问题，但在全层均匀干预时，常因激活范数畸变导致小模型生成崩溃，且无法区分特征是否真正涌现的层级。本文提出选择性转向（Selective Steering, SS），通过正交旋转矩阵保证范数不变，并仅在正负类均值投影符号相反的判别层施加干预。该方案在小型模型上显著提升了攻击成功率并保持了通用能力，但其判别层选择机制对强对齐模型的泛化边界尚存疑。

】
