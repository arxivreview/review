# ICLR2026 · 脉冲Transformer架构方向论文汇编

> 本方向共 8 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DISTRIBUTION-AWARE MULTI-GRANULARITY PHASE CODING: TOWARDS LOWER CONVERSION ERROR FOR SPIKE-DRIVEN LARGE LANGUAGE MODELS ｜分布感知多粒度相位编码：降低脉冲大语言模型转换误差

研究机构：吉林大学

作者：Hanyuan Zheng、Haozhen Zhang、Tianshuo Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_50229751)

> 脉冲大语言模型（Spiking LLM）旨在利用脉冲神经网络（SNN）的事件驱动特性替代密集浮点运算，以解决大语言模型（LLM）推理的高能耗瓶颈。现有ANN-to-SNN转换方法普遍采用率编码或时间编码，将激活值映射为均匀间隔的离散值，忽视了LLM激活分布的非均匀性，导致分布失配引发的潜在转换误差。本文提出分布感知多粒度相位编码，通过多个可学习基实现非均匀离散值分配，并设计交替优化神经元训练算法，仅优化神经元参数而无需微调模型权重。该方法在LLaMA-3-8B上实现了接近ANN精度的最低困惑度，但相位编码在数字硬件上的实现复杂度及其对能效优势的抵消效应仍未得到验证。

】

---

【MANY EYES, ONE MIND: TEMPORAL MULTI PERSPECTIVE AND PROGRESSIVE DISTILLATION FOR SPIKING NEURAL NETWORKS ｜多视角渐进蒸馏脉冲神经网络

研究机构：澳大利亚莫纳什大学、美国东北大学

作者：Kai Sun、Peibo Duan、Yongsheng Huang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_68564946)

> 脉冲神经网络（SNN）在能效上优于人工神经网络（ANN），但精度长期滞后，且截断推理时性能急剧退化。现有知识蒸馏（KD）方法将单一恒定教师信号施加于所有时间步，忽视了SNN内部的时间动态异质性，导致中间预测同质化且早期预测无法收敛至全长度预测。MEOM通过掩码扰动生成多视角教师信号，并引入累积平均对齐机制，强制截断预测逐步逼近全长度预测。该框架在ResNet骨干上刷新了CIFAR-10/100的SOTA，但在Transformer骨干上仍落后于最新架构优化方法，其能效增益是否被额外计算开销抵消尚存疑。

】

---

【Neural Dynamics Self-Attention for Spiking Transformers ｜局部感受野动态脉冲自注意力

研究机构：电子科技大学、香港中文大学

作者：Dehao Zhang、Fukai Guo、Shuai Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19290)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19290)

> 脉冲Transformer在边缘部署中面临精度与内存的双重瓶颈，根源在于脉冲自注意力（Spiking Self-Attention, SSA）丢失了标准自注意力的局部性偏置，且推理时需显式存储巨大的注意力矩阵。现有方法要么牺牲精度换取稀疏性，要么保留浮点运算导致能效优势丧失。本文通过引入局部感受野（Local Receptive Field, LRF）模块修正注意力分布，并将其重构为神经元膜电位动态，在提升精度的同时消除矩阵存储需求。该方案在内存受限场景下提供了有效的精度-内存权衡，但其对长序列依赖的捕捉能力及在大规模语言模型中的适用性尚存疑。

】

---

【OTTERS: AN ENERGY-EFFICIENT SPIKING - TRANSFORMER VIA OPTICAL TIME TO-FIRST-SPIKE ENCODING ｜光电突触时间编码脉冲Transformer

研究机构：新加坡国立大学、西湖大学

作者：Zhanglu Yan、Jiayi Mao、Qianhui Liu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_25308744)

> 脉冲Transformer在边缘部署中面临的核心矛盾是：时间编码虽能最大化稀疏性，但解码脉冲时间所需的数字乘法与衰减函数计算抵消了能效优势。现有方案要么依赖率编码导致多次访存，要么在数字域模拟时间衰减引入额外能耗。本文切入点在于将光电突触器件固有的信号衰减特性直接作为计算原语，物理实现时间衰减与权重乘法的融合。通过定制In₂O₃器件与QNN-to-SNN转换算法，Otters在GLUE基准上以13.4M参数实现了SNN精度领先与能效比37.40x-41.36x的双重突破，但其模拟硬件噪声下的鲁棒性边界仍待更严苛的器件变异性验证。

】

---

【Otters: An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding ｜光电突触时首脉冲编码脉冲Transformer

研究机构：新加坡国立大学、西湖大学

作者：Zhanglu Yan、Jiayi Mao、Qianhui Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18968)

> 脉冲Transformer在边缘部署中面临能效与精度的双重瓶颈，传统时间编码方案因需数字计算衰减函数而抵消了稀疏性收益。Otters利用氧化铟光电突触的自然信号衰减物理特性，直接实现时首脉冲（Time-to-First-Spike, TTFS）所需的时变衰减计算，消除了数字乘法开销。通过量化神经网络（Quantized Neural Network, QNN）到SNN的转换与1比特键值投影，该架构在GLUE基准上实现了SOTA精度与41.36倍能效比。其价值在于将硬件缺陷转化为计算原语，但模拟器件的变异性对大规模集成的鲁棒性影响仍存疑。

】

---

【SMIXER: RETHINKING EFFICIENT-TRAINING AND EVENT-DRIVEN SNNS ｜脉冲Token混合器与动态时空剪枝

研究机构：北京大学、中国科学院

作者：Yijie Lu、Xinhao Luo、Yixing Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_77044096)

> 脉冲神经网络（SNN）在异步硬件上的部署受限于脉冲自注意力（SSA）的矩阵乘法精度偏差，且GPU训练阶段存在大量零值计算冗余。现有Spiking Transformer虽精度领先，但无法真正事件驱动，且训练开销巨大。本文采用Spiking-token Mixer（SMixer）替代SSA以消除脉冲矩阵乘法，并设计无参数的动态时空剪枝（DSTSP）框架，通过剔除低信息量脉冲特征降低训练成本。该方案在保持全事件驱动特性的同时实现了训练加速，但在ImageNet-1K等基准上的精度仍低于当前SOTA，其在全异步硬件上的实际能效增益尚待验证。

】

---

【TP-Spikformer: Token Pruned Spiking Transformer ｜脉冲Transformer的Token剪枝与计算冗余消除

研究机构：电子科技大学、香港中文大学

作者：Wenjie Wei、Xiaolong Zhou、Malu Zhang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00527)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00527)

> 脉冲Transformer（Spiking Transformer）在提升精度的同时引入了高参数量与密集计算，导致边缘部署困难。现有剪枝方法多依赖重训练或结构修改，缺乏通用性。本文提出无需重训练的时空信息保留准则与块级早停架构，在保持精度的同时大幅降低计算量。该方法在多种骨干网络上验证了效率优势，但其零微调策略在动态任务上的潜力存疑。

】

---

【北大等提出脉冲差异Transformer：用脉冲减法替代点积，解决3D点云边缘特征平滑与高能耗问题

研究机构：北京大学、天津大学

作者：Yijie Lu、Zhiyi Pan、Renrui Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10801392)

> 脉冲Transformer旨在利用脉冲神经网络（SNN）的事件驱动特性，重构传统Transformer中密集的浮点乘累加运算，以解决边缘设备部署中的高能耗与高延迟瓶颈。现有方法在2D视觉任务中已验证可行性，但直接迁移至3D点云时，脉冲自注意力（SSA）的点积相似度机制导致边缘特征平滑且计算开销过大。本文提出脉冲差异注意力机制（SDAM），通过脉冲减法替代点积，结合空间感知神经元，构建分层局部-全局架构。该设计在3D点云分类中达到SOTA，但能效优势依赖理论计算，实际硬件部署的器件变异性影响尚未验证。

】
