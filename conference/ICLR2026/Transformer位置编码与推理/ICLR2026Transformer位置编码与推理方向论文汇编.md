# ICLR2026 · Transformer位置编码与推理方向论文汇编

> 本方向共 11 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DECOUPLING POSITIONAL AND SYMBOLIC ATTEN TION BEHAVIOR IN TRANSFORMERS ｜位置-符号注意力解耦与RoPE频率机制分析

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_81678347)

> 本文旨在厘清Transformer注意力头中位置感知与符号匹配两种核心能力的数学边界及其在RoPE频率维度上的具体映射关系。现有研究虽观察到RoPE不同频率段对应不同功能，但缺乏形式化定义与互斥性证明，导致频率选择依赖经验调参。作者通过定义位置/符号行为的严格数学判据，证明二者互斥，并建立量化评分体系，在Gemma-2、Llama-3等模型中验证了低频主导符号行为、高频主导位置行为的规律。该工作为PE优化提供了微观机制解释，但其结论基于特定绑定任务，对复杂推理场景的普适性尚存疑。

】

---

【Decoupling Positional and Symbolic Attention Behavior in Transformers ｜位置-符号注意力解耦与互斥原理

研究机构：智利大学

作者：Felipe Urrutia、Jorge Salas、Alexander Kozachinskiy 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.11579)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11579)

> 现代大语言模型中，旋转位置编码（RoPE）的频率选择长期被视为调节长上下文外推与近距依赖的单一旋钮，但缺乏对注意力头内部机制的数学界定。现有方法如 YaRN 或 LongRoPE 仅通过缩放频率范围改善性能，却未解释为何高频利于位置感知而低频利于语义检索，导致优化策略缺乏理论指导。本文通过定义位置与符号行为的互斥性，构建了量化指标并证明频率门控对模型性能的因果影响。该工作揭示了 RoPE 频率与注意力头功能分化的深层联系，但其结论局限于 RoPE 架构，且未验证在标准长上下文基准上的泛化能力。

】

---

【Extending the Context of Pretrained LLMs by Dropping Their Positional Embeddings ｜移除位置编码实现零样本长上下文扩展

研究机构：英国牛津大学

作者：Yoav Gelberg、Koshi Eguchi、Takuya Akiba 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12167)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12167)

> 长上下文外推失效源于旋转位置编码（RoPE）在未见长度下的分布外问题，现有频率缩放方法虽能维持困惑度，却导致深层信息检索能力丧失。本文指出RoPE是训练期的必要归纳偏置，但过度依赖阻碍了推理期的泛化，提出在预训练后移除位置编码（DroPE）并进行短程重校准。该方法实现了无需长上下文微调的零样本扩展，但重校准阶段是否引入新的位置偏差，以及其在超长序列下的稳定性，仍存疑。

】

---

【EXTENDING THE CONTEXT OF PRETRAINED LLMS BY DROPPING THEIR POSITIONAL EMBEDDINGS ｜移除位置编码实现零样本长上下文扩展

研究机构：英国牛津大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_38864063)

> 长上下文外推失效源于显式位置编码在未见长度下的分布外问题，而现有频率缩放方法虽能维持困惑度却牺牲了远端信息检索能力。本文指出位置编码是训练期的关键归纳偏置而非推理期的必需组件，提出在预训练后移除位置编码并短期重校准的 DroPE 方法。该方法在不进行长上下文微调的前提下，实现了超越训练长度数倍的零样本泛化。其价值在于解耦了训练效率与推理泛化，但移除位置编码后模型在超长序列上的注意力稳定性与语义匹配精度仍存疑。

】

---

【Frayed RoPE and Long Inputs: A Geometric Perspective ｜旋转位置编码的几何失效与分布内修复

研究机构：IBM研究院、美国石溪大学

作者：Davis Wertheimer、Aozhong Zhang、Derrick Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18017)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18017)

> Transformer 长上下文外推失效的根源常被归咎于频率分布外（Out-of-Distribution, OOD），但现有频率缩放方法未能解释为何额外旋转会导致注意力机制崩溃。本文切入点在于揭示 RoPE 对键/值潜空间几何结构的破坏，特别是其对 Attention Sink 功能的抑制。通过仅对部分通道应用高频旋转，RoPE-ID 在保持簇分离的同时确保合并发生在训练长度内，实现了无需调参的零样本长度泛化。该方法在 1B/3B 模型上验证了有效性，但其对大规模模型及复杂推理任务的适用性仍存疑。

】

---

【Group Representational Position Encoding ｜群表示位置编码

研究机构：美国普林斯顿大学、美国加州大学洛杉矶分校

作者：Yifan Zhang、Zixiang Chen、Yifeng Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07805)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07805)

> 位置编码需同时满足相对性、数值稳定性与长程泛化，但现有方法将旋转与偏置割裂为独立机制，缺乏统一代数基础。RoPE 的固定坐标平面限制了跨子空间耦合，ALiBi 的线性偏置缺乏群论解释，二者无法在同一框架下推导扩展。GRAPE 将位置编码重构为李群作用，通过 SO(d) 中的秩2反对称生成元与 GL(d+k) 中的单幂生成元，统一了乘性旋转与加性偏置。该框架在 770M 模型上将 FineWeb-Edu 平均准确率从 RoPE 的 55.76 提升至 56.91，但仅在中小规模模型上验证，未触及超长上下文外推的核心痛点。

】

---

【Hippoformer: Integrating Hippocampus-inspired Spatial Memory with Transformers ｜海马体启发的空间记忆架构

研究机构：清华大学

作者：Tiantian Li、Xingxing Cao、Yifei Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_89901065)

> 现有 Transformer 架构依赖键值缓存实现关联记忆，但缺乏固有的空间先验，导致在长程空间推理中泛化能力受限。传统海马体计算模型如 TEM 虽具备结构泛化能力，却因 Hebbian 权重计算开销大且受限于上下文窗口，难以融入现代深度学习框架。本文提出 mm-TEM 与 Hippoformer，通过引入元训练 MLP 快权重替代传统 Hebbian 机制，实现高效的空间结构编码与长程预测。该架构在 3D 环境多步预测中显著降低误差，但其对真实复杂环境的适应性及与标准位置编码机制的兼容性尚存疑。

】

---

【In-Context Algebra ｜变量代数中的符号推理机制

研究机构：美国东北大学

作者：Eric Todd、Jannik Brinkmann、Rohit Gandikota 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16902)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16902)

> 现有 Transformer 算术研究多依赖词嵌入中预编码的几何结构，当移除固定语义后，模型如何维持推理能力尚不明确。本文通过构建变量赋值代数任务，迫使模型仅从上下文交互中推断代数结构，发现其习得的是稀疏关系模式而非傅里叶几何表示。核心方法是通过因果干预隔离出交换复制、单位元识别与闭包消去三种符号机制。该工作揭示了任务结构对推理策略的决定性作用，但其在非群结构上的泛化局限与关联律的低准确率暴露了机制的边界。

】

---

【PROBING ROTARY POSITION EMBEDDINGS THROUGH FREQUENCY ENTROPY ｜频率熵诊断RoPE冗余维度

作者：Yui Oka、Kentaro Hanafusa、Taku Hasegawa 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_17833291)

> 旋转位置编码（RoPE）已成为大语言模型处理长程依赖的标准组件，但其内部各频率维度的功能分配长期缺乏定量解释，导致高频与低频维度的作用存在相互矛盾的实证报告。现有分析多依赖热力图视觉检查或粗略的高低频二分法，无法区分哪些维度承载任务相关信号、哪些仅为冗余振荡。本文引入频率熵（Frequency Entropy, FE）框架，通过频谱与序列两个维度的香农熵量化每个旋转对的有效利用率，并验证了抑制低熵维度对模型性能的无损性。该工作为RoPE的剪枝与重加权提供了可操作的诊断工具，但其结论是否适用于非RoPE架构或更复杂的推理任务尚存疑问。

】

---

【Quantitative Bounds for Length Generalization in Transformers ｜长度泛化的定量训练长度界

研究机构：美国普林斯顿大学

作者：Zachary Izzo、Eshaan Nichani、Jason D. Lee

论文原文见 [arXiv](https://arxiv.org/abs/2510.27015)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.27015)

> 长度泛化（Length Generalization, LG）要求模型在短序列上训练后，能准确处理任意长的未见输入。现有理论仅证明LG在有限长度下“存在”，却未给出该长度的具体数值，导致工程上无法预估数据需求。本文通过构建“模拟论证”，首次推导出最小训练长度 $N$ 与模型参数范数、位置编码周期 $\Delta$ 及词汇表大小之间的多项式关系。这一结果将LG从渐近存在性证明转化为可计算的复杂度度量，但其结论严格依赖于有限精度下的Hardmax假设，在无限精度Softmax场景下的适用性仍存疑。

】

---

【Selective Rotary Position Embedding ｜选择性旋转位置编码

研究机构：瑞士洛桑联邦理工学院、德国弗莱堡大学

作者：Sajad Movahedi、Timur Carstensen、Arshia Afzal 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.17388)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17388)

> 线性注意力模型在长序列检索中因固定状态大小而失效，现有门控机制仅通过衰减范数管理记忆，缺失编码相对位置的旋转能力。本文指出 Softmax 注意力隐含了输入依赖的旋转，而线性模型缺乏此组件，提出 Selective RoPE 将 RoPE 推广为可学习角度的输入依赖旋转。该方法在合成任务与语言建模上提升了召回性能，但其增益是否随模型规模扩大而消失尚存疑。

】
