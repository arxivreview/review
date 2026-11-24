# ICASSP2026 · 机器学习理论与优化方向论文汇编

> 本方向共 2 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Do we really need Self-Attention for Streaming Automatic Speech Recognition? ｜流式语音识别中自注意力的局部算子本质与卷积替代方案

作者：Youness Dkhissi、Valentin Vielzeuf、Elys Allesiardo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19960)

> 流式自动语音识别（Streaming ASR）要求模型在固定时间块内完成转录，无法访问未来或过远的过去上下文。传统 Conformer 架构中的自注意力模块旨在捕获长程依赖，但在严格流式约束下，其全局视野被物理截断，导致计算成本与功能收益严重失衡。本文通过可视化诊断发现，流式场景下自注意力权重自发坍缩至对角线附近，实质退化为昂贵的局部算子。作者提出用可变形卷积替换或直接移除自注意力，在保持词错误率（WER）持平的前提下大幅降低参数量与实时因子（RTF）。这一发现挑战了“流式 ASR 必须依赖注意力机制”的默认假设，但结论局限于特定块大小与数据集，对跨块长程依赖的捕获能力未做深入验证。

】

---

【Subtractive Modulative Network with Learnable Periodic Activations ｜减法调制网络（SMN）：基于信号处理范式的隐式神经表示架构

研究机构：瑞典皇家理工学院、瑞士洛桑联邦理工学院

作者：Tiou Wang、Zhuoqian Yang、Markus Flierl 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16337)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16337)

> 隐式神经表示（INR）旨在以紧凑权重实现分辨率无关的高保真信号重建，但标准多层感知机（MLP）固有的频谱偏差导致高频细节拟合困难。现有傅里叶特征与周期性激活方法虽能缓解此问题，却常形成频谱成分纠缠的黑盒模型，缺乏对谐波生成的显式控制。本文借鉴经典音频减法合成原理，提出振荡器-滤波器结构化流水线，通过可学习正弦层生成多频基，并利用乘法掩码模块主动塑形频谱。该架构在2D图像重建中展现出优于主流基线的精度与参数效率，但其对3D场景泛化能力的验证仍显薄弱，且乘法交互的理论优势是否普适尚存疑。

】
