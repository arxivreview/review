# Others2026 · 数据科学与推荐系统方向论文汇编

> 本方向共 5 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Modeling Stage-wise Evolution of User Interests for News Recommendation ｜阶段式兴趣演化建模

研究机构：合肥工业大学

作者：Zhiyong Cheng、Yike Jin、Zhijie Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10471)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10471)

> 个性化新闻推荐面临用户兴趣随突发事件快速漂移与长期阅读习惯稳定并存的矛盾。现有方法要么依赖静态全局图导致推荐滞后，要么仅关注短期序列而丢失高阶协同信号，难以兼顾时效性与稳定性。本文提出SEIN框架，通过全局偏好建模（GPM）提取稳定协同信号，并利用局部偏好建模（LPM）在时间子图上结合LSTM与自注意力捕捉阶段式动态演化。该框架在大规模新闻数据集上显著优于基线，但其对时间窗口划分的依赖及未涉及多兴趣向量解耦的设计，限制了其在复杂兴趣结构下的泛化能力。

】

---

【事件基特征（EBF）三维扩展框架

作者：Sohini Roychowdhury、Doris Wang、Qian Ge 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02807)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02807)

> 广告排序系统面临用户意图动态演变与数据源多样性不足的双重矛盾，传统固定窗口统计特征难以捕捉长序列中的细粒度兴趣演化，且单一数据源无法覆盖用户全场景行为。现有序列建模方法虽能处理长历史，但缺乏对数据源质量与语义丰富度的系统性评估机制，导致资源投入与收益不成比例。本文提出事件基特征（Event-Based Feature, EBF）三维扩展框架，通过事件源多样性、序列长度与语义丰富度三个维度协同优化用户表示，在保持实时推理约束下提升点击率预测精度。该框架在Meta内部数据上验证了广告曝光源优于自然内容源的ROI差异，但缺乏公开基准对比，其线性压缩机制在复杂交互场景下的表达力边界尚不明确。

】

---

【墨尔本团队新研究：自适应通道管理Transformer

研究机构：澳大利亚墨尔本大学

作者：Yuchen Luo、Xinyu Li、Liuhua Peng 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.14632)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.14632)

> 多变量长时程时间序列预测（MTSF）的核心难点在于平衡通道独立（CI）策略的鲁棒性与通道依赖（CD）策略的表达力，前者易丢失跨变量交互，后者易引入高维噪声。现有方法多采用固定策略，难以在变量数量剧烈变化的场景下自适应调整。本文提出Adapformer，通过嵌入阶段的自适应通道增强器（ACE）与解码阶段的自适应通道预测器（ACF），实现了对CI与CD信息的动态融合。该架构在PEMS等高维数据集上显著优于基线，但在低维数据集上的优势有限，且未解决Transformer固有的二次方计算复杂度问题。

】

---

【帝国理工团队新研究：证据驱动与极值理论融合的稀有事件时序预测

研究机构：英国帝国理工学院、捷克布拉格捷克理工大学

作者：Antanas Zilinskas、Robert N. Shorten、Jakub Marecek

论文原文见 [arXiv](https://arxiv.org/abs/2601.19022)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19022)

> 稀有事件预测面临类别极度不平衡、长程依赖稀释早期信号以及标准损失函数对尾部风险梯度信号弱化的三重困境，导致模型在高风险决策场景中概率校准失效且漏报率居高不下。现有方法或依赖数据重采样引入时间伪影，或仅优化判别精度而忽视不确定性分解，无法在单次前向传播中同时满足校准与尾部敏感性需求。本文提出 EVEREST，通过训练时引入证据 Normal–Inverse–Gamma (NIG) 头与极值理论 (EVT) 超越似然正则化，在推理时仅保留单一分类头，实现了无额外计算开销的联合优化。该架构在太阳耀斑基准上取得了显著的性能提升，但其对固定长度输入的依赖及缺乏显式概率密度输出限制了其在动态流式场景中的直接应用。

】

---

【赫尔辛基团队新研究：地形感知污染物流学习

研究机构：芬兰赫尔辛基大学、德国慕尼黑工业大学

作者：Ammar Kheder、Helmi Toropainen、Wenqing Peng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16821)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16821)

> 高分辨率空气质量预测长期受困于数值模型计算成本高昂与纯数据驱动模型缺乏物理一致性的双重瓶颈。现有AI基线虽能捕捉空间相关性，却未能显式编码地形对平流传输的几何约束，导致在复杂地形区域预测精度骤降。TopoFlow通过风引导补丁重排序与地形感知注意力偏置，将物理传输规则硬编码进Vision Transformer架构。该设计在PM2.5预测中实现了9.71 µg/m³的RMSE，较SOTA AI基线提升13%，但在垂直维度建模上存在明显短板。

】
