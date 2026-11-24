# ICLR2026 · Transformer上下文学习理论方向论文汇编

> 本方向共 17 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CONDITIONED INITIALIZATION FOR ATTENTION ｜条件数驱动的注意力初始化

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_45899240)

> 本文旨在解决Transformer训练初期注意力层Jacobian条件数过高导致的优化不稳定问题。现有初始化方法如Xavier或Mimetic Initialization缺乏对注意力矩阵谱结构的理论约束，导致收敛速度受限且泛化能力波动。本文提出Conditioned Initialization，通过特定谱结构初始化Query、Key、Value矩阵以降低Jacobian条件数上界。该方法在多种架构上加速收敛并提升精度，但其理论保证仅限于上界收紧，未直接证明对最终泛化误差的因果影响。

】

---

【HOW TRANSFORMERS LEARN CAUSAL STRUCTURES IN-CONTEXT: EXPLAINABLE MECHANISM MEETS THEORETICAL GUARANTEE ｜上下文因果结构推断的贝叶斯机制

研究机构：美国佐治亚理工学院、美国耶鲁大学

作者：Jianzhe Wei、Siyu Chen、Jianliang He 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_89788367)

> 现有上下文学习（ICL）理论多假设序列依赖结构固定，无法解释模型如何适应真实数据中动态变化的因果依赖。本文指出这一“理论-实践鸿沟”，提出Transformer可通过隐式执行贝叶斯模型平均（BMA）来推断随机采样的因果图。作者构造了两层相对位置嵌入Transformer，证明其注意力权重可精确实现BMA的后验概率计算，并通过实验验证训练后的模型参数收敛至该理论构造。该工作填补了固定结构推断的理论空白，但离散与连续空间的表示能力差异及有限样本下的性能差距仍存疑。

】

---

【IN CONTEXT SEMI-SUPERVISED LEARNING ｜上下文半监督学习

研究机构：美国杜克大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10908006)

> 现有Transformer上下文学习理论聚焦于已标记数据对，忽略了未标记样本中蕴含的几何结构，导致低标签场景下模型无法利用上下文中的流形信息。本文提出IC-SSL框架，将谱几何表示学习与隐式梯度下降整合进单一端到端Transformer，使模型在推理时从原始坐标直接提取几何感知特征。该方法在合成流形与图像流形上显著优于基线，但其依赖局部距离假设，对高维自然语言序列的适用性存疑。

】

---

【In-Context Semi-Supervised Learning ｜上下文半监督学习中的几何感知表示

研究机构：美国杜克大学

作者：Jiashuo Fan、Paul Rosu、Aaron T. Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.15934)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15934)

> 导读 现有 Transformer 上下文学习（In-Context Learning, ICL）理论主要聚焦于利用显式标记对进行隐式梯度下降，忽略了未标记数据中蕴含的流形结构，导致在低标签率场景下性能受限。本文切入点在于证明 Transformer 可在前向传播中直接从未标记上下文提取几何特征，无需伪标签或独立推断。通过构建两阶段端到端 Transformer，第一阶段计算拉普拉斯特征图，第二阶段执行核梯度下降，实现了上下文半监督学习（In-Context Semi-Supervised Learning, IC-SSL）。该工作验证了未标记数据对低标签率 ICL 的关键增益，但其理论保证局限于特定流形结构，且缺乏大规模预训练模型中的涌现动力学分析。

】

---

【Learning Pseudorandom Numbers with Transformers: Permuted Congruential Generators, Curricula, and Interpretability ｜伪随机序列的上下文学习极限与课程优化机制

研究机构：美国马里兰大学帕克分校

作者：Tao Tao、Maissam Barkeshli

论文原文见 [arXiv](https://arxiv.org/abs/2510.26792)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26792)

> 该方向旨在界定 Transformer 在对抗性伪随机结构下的模式识别边界，现有理论多基于独立同分布假设，难以解释强依赖序列中的优化停滞现象。本文以置换同余生成器为受控基准，通过引入小模数课程学习策略，突破了大模数训练中的损失平台期。实验证实模型能隐式学习生成器内部结构，且所需上下文长度随模数呈平方根缩放。该工作拓展了上下文学习的适用边界，但缺乏对状态空间模型等替代架构的对比验证。

】

---

【Learning to Adapt: In-Context Learning Beyond Stationarity ｜非平稳回归下的门控线性注意力上下文学习

研究机构：美国密歇根大学、美国俄亥俄州立大学

作者：Zhen Qin、Jiachen Jiang、Zhihui Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2604.10946)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10946)

> 现有Transformer上下文学习（In-Context Learning, ICL）理论主要基于平稳数据假设，无法解释模型在时间序列或流式数据中目标函数随时间演化的适应机制。本文切入点在于证明门控线性注意力（Gated Linear Attention, GLA）通过引入可学习的遗忘因子，在非平稳回归任务中实现了优于标准线性注意力的预测精度。其核心方法是建立一阶自回归权重演化模型，并推导GLA前向传播与自适应滤波的数学等价性。该工作填补了非平稳ICL的理论空白，但其全局遗忘因子假设限制了其对局部动态变化的捕捉能力。

】

---

【ON LEARNING LINEAR DYNAMICAL SYSTEMS IN CONTEXT WITH ATTENTION LAYERS ｜线性动力系统上下文学习中的注意力层最优性

研究机构：德国慕尼黑工业大学

作者：Maria-Luiza Vlǎdǎrean、Xuhui Zhang、Suvrit Sra

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_40442193)

> 本文旨在解决Transformer在非独立同分布（non-i.i.d.）时序数据上执行上下文学习（In-Context Learning, ICL）的机制解释缺失问题。现有理论多局限于i.i.d.线性回归，无法解释模型为何能逼近卡尔曼滤波（Kalman Filter, KF）性能。作者通过引入自回归近似与线性注意力层，证明了前向传播等价于一步梯度下降。该工作填补了噪声线性动力系统（Linear Dynamical Systems, LDS）下ICL优化等价性的理论空白，但其单层线性注意力假设限制了向实际Softmax架构的推广。

】

---

【Pretrain-Test Task Alignment Governs Generalization in In-Context Learning ｜预训练-测试任务对齐决定上下文学习泛化边界

研究机构：美国哈佛大学

作者：Mary I. Letey、Jacob A. Zavatone-Veth、Yue M. Lu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26551)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26551)

> 上下文学习（In-Context Learning, ICL）旨在解释Transformer如何在推理阶段仅凭前向传播适应新任务，但现有理论多假设预训练与测试任务分布完全匹配或各向同性，无法解释真实场景中任务结构差异导致的泛化失效。本文切入点在于量化预训练任务协方差与测试任务协方差之间的结构失配，揭示其对泛化误差的非线性影响。通过构建高维极限下的线性注意力模型，推导包含任意协方差失配的精确ICL误差公式，并定义新的对齐度量。该工作证明了任务多样性并非总是有益，在特定失配条件下增加多样性反而损害性能，为ICL泛化边界提供了可计算的数学判据，但其结论局限于线性回归与线性注意力架构，对Softmax非线性机制的解释力尚待验证。

】

---

【PRETRAIN–TEST TASK ALIGNMENT GOVERNS GENERALIZATION IN IN-CONTEXT LEARNING ｜预训练-测试任务对齐决定上下文学习泛化边界

研究机构：美国哈佛大学

作者：Mary Letey、Jacob Zavatone-Veth、Yue Lu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_75397064)

> 上下文学习（In-Context Learning, ICL）的核心矛盾在于模型如何在推理阶段仅凭前向传播适应新任务，而现有理论多假设预训练与测试任务分布匹配或各向同性，忽略了真实场景中任务结构的失配。本文切入点在于量化这种失配对泛化误差的精确影响，通过高维渐近分析推导线性注意力模型在任意协方差失配下的ICL误差公式。该工作证明了预训练-测试对齐度量直接预测非线性Transformer的泛化性能，并揭示了任务多样性与对齐度的交互作用可能损害性能。这一发现挑战了“增加多样性必然有益”的共识，但结论局限于线性回归任务，其在复杂非线性场景下的普适性仍存疑。

】

---

【STRONG CORRELATIONS INDUCE CAUSE ONLY PRE DICTIONS IN TRANSFORMER TRAINING ｜相关性挤出效应（CCO）：Transformer 训练中的因果不变性机制

研究机构：北京大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_37423359)

> 数据驱动模型常陷入捷径学习，依赖虚假相关而非因果机制，导致分布偏移下泛化失效。现有不变性学习方法依赖多环境假设或显式正则化，无法解释标准梯度下降（GD）在单环境训练中如何自发抑制虚假特征。本文提出相关性挤出效应（Correlation Crowding-Out, CCO），指出在主导因果相关条件下，GD 的隐式正则化可驱动 Transformer 收敛至仅依赖因果特征的预测器。该机制通过“占据”与“挤出”两阶段动力学实现，无需多环境训练或因果目标，但理论保证局限于简化架构与特定数据分布，实际 LLM 中的普适性存疑。

】

---

【Theory of Scaling Laws for In-Context Regression: Depth, Width, Context and Time ｜深度线性注意力上下文学习的缩放律与架构形状优化

研究机构：美国哈佛大学

作者：Blake Bordelon、Mary I. Letey、Cengiz Pehlevan

论文原文见 [arXiv](https://arxiv.org/abs/2510.01098)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01098)

> 导读 本文旨在解决Transformer在固定计算预算下，宽度与深度如何联合缩放以实现上下文学习（In-Context Learning, ICL）性能最优的问题。现有缩放律理论多聚焦于宽度或总参数量，无法区分深度与宽度的相对增益，且缺乏对预训练任务统计结构的考量。本文通过构建三种不同协方差结构的深度线性注意力模型，推导了包含深度、宽度、上下文长度及训练时间的Chinchilla式缩放律。该工作揭示了预训练协方差多样性对最优架构形状的决定性影响，但受限于线性注意力假设，其结论向Softmax实际模型的迁移性尚存疑。

】

---

【Towards a Theoretical Understanding of In-Context Learning: Stability and Non-I.I.D Generalisation ｜非独立同分布场景下Transformer上下文学习的稳定性与泛化界

研究机构：新加坡南洋理工大学、复旦大学

作者：Yingjie Wang、Yutian Zhou、Shi Fu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_31862147)

> 上下文学习（In-Context Learning, ICL）理论旨在解释大语言模型在不更新参数前提下适应新任务的数学机制，但现有泛化界多依赖独立同分布（i.i.d.）假设或正交输入结构，难以覆盖真实场景中的分布偏移。本文切入点在于剥离理想化数据假设，利用算法稳定性与分布差异度量，建立非线性Transformer在自回归预测下的泛化误差界。其核心做法是量化小批量梯度下降（Mini-batch Gradient Descent, MBGD）下的稳定性系数，并结合序列Rademacher复杂度处理非i.i.d.数据。该工作填补了分布偏移下ICL泛化理论的空白，但其理论保证依赖于损失景观的平滑性，对非平滑场景的迭代次数限制可能削弱实际收敛性能。

】

---

【Transformers as Measure-Theoretic Associative Memory: A Statistical Perspective and Minimax Optimality ｜测度论关联记忆 Transformer 的极小极大最优性

研究机构：MiniMax、日本东京大学

作者：Ryotaro Kawata、Taiji Suzuki

论文原文见 [arXiv](https://arxiv.org/abs/2602.01863)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01863)

> 该方向旨在解决 Transformer 在处理无限长、分布值上下文时，如何从混合测度中精确检索特定分量并预测的统计泛化问题。现有线性注意力理论因表达能力受限，难以实现稀疏检索，而冻结核方法无法捕捉学习后的注意力机制。本文切入点在于将关联记忆形式化为测度论上的回归问题，并证明学习型 Softmax 注意力在此设定下的统计效率。通过构建基于 RKHS 的测度论 Transformer 架构，本文推导了次多项式收敛率及匹配的极小极大下界。这一工作填补了从表达能力到统计效率的理论空白，但其结论严格依赖于指数谱衰减假设，在实际自然语言数据中的普适性存疑。

】

---

【Transformers Learn Latent Mixture Models In-Context via Mirror Descent ｜基于混合转移分布的上下文潜变量推断

研究机构：瑞士洛桑联邦理工学院

作者：Francesco D'Angelo、Nicolas Flammarion

论文原文见 [arXiv](https://arxiv.org/abs/2604.10848)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10848)

> 序列建模的核心困境在于，预测下一个词时，模型必须动态判断哪些历史词具有因果相关性，而非依赖固定的位置依赖。现有ICL理论多聚焦于线性回归或简单马尔可夫链，其因果结构是静态且已知的，无法解释语言中动态变化的潜变量依赖。本文引入混合转移分布（MTD）框架，将词重要性估计形式化为上下文中的潜变量推断问题，证明Transformer通过实现镜像下降（Mirror Descent）算法来学习这些潜变量权重。该工作填补了非线性潜变量ICL机制的理论空白，但其结论局限于合成任务与特定初始化，对真实语言泛化能力的验证仍存疑。

】

---

【Transformers Trained via Gradient Descent Can Provably Learn a Class of Teacher Models ｜双线性教师模型下的单层Transformer蒸馏理论

研究机构：美国加州大学洛杉矶分校

作者：Chenyang Zhang、Qingyue Zhao、Quanquan Gu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22801)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22801)

> 现有Transformer优化理论多聚焦于特定任务（如线性回归或稀疏选择），缺乏统一框架解释其在卷积、图结构等复杂架构中的学习机制。本文指出这些任务共享双线性结构，提出以“位置仅”Softmax注意力Transformer作为学生，从双线性教师模型中恢复参数。通过建立紧收敛界与分布外泛化保证，证明了该架构在监督蒸馏下的有效性。该工作填补了统一理论空白，但其单层简化与高维假设限制了向实际多层LLM的迁移性。

】

---

【TRANSFORMERS WITH ENDOGENOUS IN-CONTEXT - LEARNING: BIAS CHARACTERIZATION AND MITIGA TION ｜内生上下文学习：偏差刻画与双重去偏

研究机构：国防科技大学、清华大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66856410)

> 上下文学习（In-Context Learning, ICL）理论长期假设噪声外生，即标签噪声与输入特征独立，这一假设在真实数据中常被隐藏混杂因子（Hidden Confounders, HCs）打破。现有基于隐式梯度下降（Implicit Gradient Descent, GD）的解释框架无法量化这种内生性导致的系统性预测偏差。本文提出内生ICL（Endogenous ICL, EICL）设定，证明预训练Transformer的预测偏差与混杂强度成正比，并设计无梯度双重去偏（Double-Debiasing, DDbias）方法，仅用极少量无混杂样本即可修正冻结模型的预测。该工作填补了因果推断与ICL理论的空白，但其理论严格性依赖于线性注意力简化，非线性场景下的偏差比例关系是否依然成立尚存疑。

】

---

【Vintix II: Decision Pre-Trained Transformer is a Scalable In-Context Reinforcement Learner ｜决策预训练 Transformer 的跨域连续控制扩展

作者：Andrei Polubarov、Lyubaykin Nikita、Alexander Derevyagin 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05112)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05112)

> 上下文强化学习（In-Context Reinforcement Learning, ICRL）旨在让智能体在推理阶段仅凭少量交互或演示适应新任务，但现有方法在处理高维、多模态连续动作空间时，往往因策略头表达能力不足而失效。本文切入点在于将决策预训练 Transformer（Decision Pretrained Transformer, DPT）与流匹配（Flow Matching）结合，以解决传统高斯策略头无法捕捉复杂动作分布似然失配的问题。通过构建包含 709.7M 状态转移的跨域数据集并采用 ODE 积分解码动作，该方法在未见任务上实现了超越前代模型的泛化性能。其价值在于验证了纯参数化 ICRL 在复杂连续控制中的可行性，但冷启动场景下的性能瓶颈仍存疑。

】
