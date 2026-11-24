# ICLR2026 · Transformer的机制可解释性方向论文汇编

> 本方向共 6 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Language Models are Injective and Hence Invertible ｜语言模型表示的单射性与精确逆推

研究机构：瑞士洛桑联邦理工学院、意大利罗马第一大学

作者：Giorgos Nikolaou、Tommaso Mencattini、Donato Crisostomi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15511)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15511)

> 导读 机制可解释性领域长期关注如何从内部激活中解读模型行为，但鲜有工作直接回答“输入信息是否在表示中无损保留”这一基础问题。主流观点认为 Transformer 的非线性组件必然导致信息坍缩，使得从隐状态精确恢复输入成为不可能任务。本文通过实分析证明标准解码器 Transformer 几乎必然单射，并据此设计 SIPIT 算法实现线性时间精确逆推。该工作将可逆性确立为架构固有属性，但其在量化模型与长序列下的泛化能力尚存疑。

】

---

【LLMs Process Lists With General Filter Heads ｜列表过滤的模块化机制：Filter Heads 与谓词编译

研究机构：美国东北大学

作者：Arnab Sen Sharma、Giordano Rogers、Natalie Shapira 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26784)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26784)

> 机制可解释性（Mechanistic Interpretability, MI）旨在通过逆向工程揭示 Transformer 内部计算机制，以打破大语言模型的黑盒性质。现有电路发现范式多聚焦于序列依赖任务，难以解释模型如何处理无固定顺序的集合操作，且缺乏对抽象语义谓词如何被“编译”为可复用几何表示的因果证据。本文通过激活修补定位中间层的稀疏注意力头（Filter Heads），证明其 Query 状态编码了可跨语言、跨格式移植的谓词表示。这一发现验证了 Transformer 存在模块化计算原语，但仅局限于语义过滤场景，未覆盖非线性算术或长程状态追踪。

】

---

【PROBABILITY DISTRIBUTIONS COMPUTED BY AUTOREGRESSIVE TRANSFORMERS ｜Transformer 自回归表达力边界

研究机构：美国圣母大学

作者：Andy Yang、Anej Svete、Jiaoda Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_62014494)

> 现有 Transformer 表达力理论将模型简化为布尔分类器，忽略了其作为概率语言模型的核心自回归特性。这种简化导致理论结论无法直接迁移至实际应用，且掩盖了实数权重下分类器与自回归模型表达力的本质差异。本文通过引入状态编码器统一框架，系统对比了布尔与实数半环下分类器与自回归模型的表达力边界。该工作填补了理论空白，但受限于理想化架构假设，未验证非线性激活对等价性的破坏。

】

---

【Tracking Equivalent Mechanistic Interpretations Across Neural Networks ｜机制解释等价性

研究机构：美国卡内基梅隆大学

作者：Alan Sun、Mariya Toneva

论文原文见 [arXiv](https://arxiv.org/abs/2603.30002)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.30002)

> 机制可解释性（MI）旨在通过逆向工程揭示 Transformer 内部计算机制，但现有方法面临解释不可复用与验证困难的双重瓶颈。传统自下而上方法依赖人工标注电路，自上而下方法则受限于候选算法的模糊性，导致无法判断两个模型是否共享同一底层逻辑。本文提出“解释等价性”概念，通过比较模型实现的表示相似性，在无需显式解释描述的情况下判定两模型是否共享同一机制。该框架为 MI 评估提供了新的理论工具，但其对实现枚举完备性的依赖及线性表示假设的适用边界仍存疑。

】

---

【Two (Narrow) Heads Are Better Than (an Arbitrarily Wide) One ｜注意力头数量与图结构任务表达能力的精确层级

研究机构：美国东北大学

作者：Amanuel Tesfaye、Zeno Kujawa、Rajmohan Rajaraman 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_91650260)

> 导读 本文旨在解决小模型Transformer在图结构任务上的表达能力边界模糊问题，现有理论结果多依赖维度或精度假设，缺乏无条件界限。作者通过定义端点选择问题（Endpoint Selection Problem, ESP），构建了基于几何不等式的证明框架。核心贡献是证明单头模型在含环图上存在不可逾越的误差下界，而双头模型可零误差求解。该工作确立了头数作为能力层级的关键变量，但其结论局限于单层注意力架构，对多层或含FFN结构的迁移性存疑。

】

---

【Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors ｜下一词预测中“无用”特征涌现的梯度归因分析

研究机构：瑞士洛桑联邦理工学院、德国慕尼黑工业大学

作者：Mark Rofin、Jalal Naghiyev、Michael Hahn

论文原文见 [arXiv](https://arxiv.org/abs/2603.14087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14087)

> 机制可解释性长期关注模型内部静态电路如何执行任务，却忽视了这些电路在训练过程中如何被梯度信号塑造。现有静态分析无法解释为何下一词预测（Next-Token Prediction, NTP）目标会诱导模型学习对即时预测无用的抽象特征，如世界模型或长程依赖。本文通过分解NTP损失梯度为直接、预缓存与共享三个分量，量化各分量对特定特征方向形成的贡献。该方法在玩具任务与OthelloGPT上验证了预缓存机制对“无用”特征涌现的必要性，但受限于小规模模型重训练，尚未在大规模语言模型上实现全量归因。

】
