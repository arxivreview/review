# ACL-Findings2026 · 时序知识图谱推理与预测方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Conformal Event Prediction with Temporal Knowledge Graph ｜时序事件预测中的非交换性共形预测

研究机构：中国科学院、中国科学院大学

作者：Cheng Hu、Cong Cao、Fangfang Yuan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22424bbac590)

> 事件预测旨在从历史新闻流中推断未来可能发生的事件类型，但现有方法仅输出点预测，缺乏对预测可靠性的量化，难以支撑高风险决策。标准共形预测依赖数据交换性假设，而时序知识图谱中事件间存在强时间依赖与结构关联，导致该假设失效，使得传统校准方法无法保证覆盖率。本文提出CFEP框架，通过非一致性分数扩散与效率感知优化，在违反交换性的条件下实现覆盖保证与预测集压缩。该方法在GDELT子集上显著提升了效率，但其对未见事件类型的泛化能力仍受限于预定义的事件空间。

】

---

【Critic Rule Induction: Improving Temporal Knowledge Graph Forecasting with Generator-Critic Language Models ｜批评引导规则归纳

研究机构：美国东北大学

作者：Yingsong Ning、Fu Zhang、Jingwei Cheng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_09fe28919fc7)

> 时序知识图谱（TKG）外推推理旨在从历史观测预测未来事实，但传统规则挖掘受限于统计共现导致规则稀疏，而大语言模型（LLM）生成的规则虽具语义泛化能力却常违背时序因果。本文切入点在于将规则视为待检验的假设，通过解耦的生成-判别架构平衡覆盖率与精度。具体做法是利用LLM从历史路径抽象规则假设，再经多维事实接地评估器过滤噪声。该框架在标准基准上超越了现有SOTA，但其对离散时间戳的依赖及实体歧义处理不足，限制了其在长程连续动态场景下的适用性。

】

---

【From Implicit Graph Encoding to Explicit Evidence: A Training-Free LLM Framework for Temporal Knowledge Graph Reasoning ｜显式证据驱动的无训练时序知识图谱推理

研究机构：哈尔滨工业大学、北京航空航天大学

作者：Guo Tang、Ke Cheng、Huiming Fan 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_13cc9c22706a)

> 时序知识图谱（TKG）预测面临分布偏移与归纳泛化失效的双重困境，传统参数化模型依赖训练分布，而现有大语言模型（LLM）方法受限于隐式模态对齐与图结构线性化带来的信息丢失。ExE-LLM 通过解耦图计算与语义推理，将图信号显式转化为自然语言证据，实现了无需梯度更新的测试时自适应。该框架在归纳设置下显著优于训练式图神经网络，但其启发式规则在极端稀疏结构下的鲁棒性及离散时间衰减对长程依赖的捕捉能力仍存疑。

】

---

【LANTERN in the Event Stream: Training-Free Temporal Knowledge Graph Forecasting by Balancing Inertia and Shifts ｜时序知识图谱预测中的惯性-漂移平衡

研究机构：中国科学院、中国科学院大学

作者：Chengyuan Jin、Ao Chang、Daojian Zeng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f88535f7c216)

> 时序知识图谱预测（TKGF）的核心难点在于，模型需从海量历史事件中筛选出对当前查询真正有效的证据，以在有限上下文窗口内完成未来实体预测。现有训练-free方法依赖语义检索或简单最近邻，往往陷入“稳定模式主导”或“噪声近期事件干扰”的二元困境，无法显式区分长期交互惯性与短期突发漂移。LANTERN通过引入固定计数窗口下的强度（Strength）与新意（Novelty）双信号评分，结合Pareto-greedy选择策略，实现了证据集的结构化筛选。该方法在四个基准上稳定超越最强基线AnRe，但其性能增益依赖于LLM骨干的语义理解能力，且在极端稀疏场景下的鲁棒性缺乏充分验证。

】

---

【Learning Continuous Temporal Dynamics on Symplectic Manifolds for Temporal Knowledge Graph Embedding ｜辛几何约束下的连续时序知识图谱嵌入

作者：Jiang Li、Zehua Duo、Tian Lan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5eae08507ee2)

> 时序知识图谱嵌入（TKGE）旨在从动态事实中推断缺失链接，但主流方法依赖离散时间查表与高维参数扩展，导致模型在未见时间戳上泛化失效且计算成本高昂。TDSym 将时间演化建模为辛相空间中的哈密顿动力学，通过几何约束在低秩嵌入下实现连续时间推理。该方法利用旋转时间嵌入与特征线性调制驱动哈密顿流，证明了结构约束可替代容量扩展以提升外推能力。尽管在严格外推任务上显著优于离散基线，但其性能仍低于最新的大语言模型（LLM）辅助方法，且缺乏对开放域新实体涌现的验证。

】

---

【RCTEA: Richness-guided Co-training for Temporal Entity Alignment ｜丰富度引导的时序实体对齐

研究机构：澳大利亚昆士兰大学、香港理工大学

作者：Jiayun Li、Wen Hua、Shiqi Fan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_320b44b196a5)

> 时序实体对齐（Temporal Entity Alignment, TEA）旨在跨图匹配等价实体，但现有模型常将结构与时序特征简单拼接，忽视了不同实体间特征丰富度的巨大差异，导致低质量信号污染高价值表示。本文指出，邻居节点的信息价值并非均等，低丰富度实体的监督信号会阻碍精确特征捕捉。RCTEA通过引入丰富度引导注意力机制与自适应权重策略，动态平衡结构与时序特征，并结合双视图邻域共识去噪，在YAGO-WIKI180K等基准上取得了优于HTEA和MGTEA的性能，但其对高频实体的依赖性及缺乏LLM语义辅助的局限仍需审视。

】
