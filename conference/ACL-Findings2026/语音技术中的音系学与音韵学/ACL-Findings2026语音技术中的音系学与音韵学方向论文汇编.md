# ACL-Findings2026 · 语音技术中的音系学与音韵学方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【[b] = [d] - [t] + [p]: Self-supervised Speech Models Discover Phonological Vector Arithmetic ｜自监督语音模型中的音系向量算术

研究机构：美国卡内基梅隆大学

作者：Kwanghee Choi、Eunjung Yeo、Cheol Jun Cho 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5098ff48134e)

> 自监督语音模型（S3M）虽能高效处理语音任务，但其内部如何编码音系结构长期处于黑盒状态，传统探针实验仅能验证信息存在，无法揭示结构化的组合规律。本文切入点在于验证S3M表示中是否存在类似词向量算术的线性音系向量，即音素间的差异能否通过向量加减法精确映射为音系特征变化。通过构建基于PanPhon特征的四元组类比测试集，并引入声码器逆映射验证声学连续性，本文证实了音系特征的线性可组合性与尺度可解释性。这一发现为语音合成的细粒度控制提供了理论依据，但线性假设是否足以覆盖所有非线性音系关系仍存疑。

】

---

【Identifying and typifying demographic unfairness in phoneme-level embeddings of self-supervised speech recognition models ｜自监督语音模型音素嵌入的人口统计偏差归因分析

研究机构：法国国家科学研究中心

作者：Felix Herron、Solange Rossato、Alexandre Allauzen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e72339671a44)

> 自监督语音模型（S3M）在音素识别中普遍存在对特定说话人群体（SG）的性能偏差，但现有公平性研究多将模型视为黑盒，缺乏对内部误差机制的几何归因。本文切入点在于区分音素嵌入中的“随机误差”（方差差异）与“系统性误差”（嵌入偏差），并验证哪种机制主导了SG级不公平。通过线性探针分类与KNN距离度量，论文发现随机误差是主要成因，且常规公平性微调无效。该研究为理解S3M内部偏差提供了新视角，但其结论受限于单音素隔离场景与特定数据集，泛化性存疑。

】

---

【Spectral Gravity Formant Estimation for Phonetic Segmentation ｜频谱重力共振峰估计用于音素分割

作者：Michael S. Yantosca、Albert M. K. Cheng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d8b7c30d4864)

> 实时音素分割面临的核心矛盾是端到端模型丢失时间精度与人工标注成本高昂。现有基于自监督学习（SSL）的音素识别框架依赖伪标签且时间戳推导粗糙，而传统声学方法计算开销大。本文切入点在于利用纯声学特征中的共振峰估计实现无预训练的实时音素边界检测。具体做法是提出一种基于“频谱重力”初始化的截止期望最大化（EM）算法，在毫秒级延迟内对频谱能量进行聚类。该方法在低资源语言上展示了优于神经基线的聚类稳定性，但其对复杂声学环境（如鼻音、擦音）的鲁棒性仍存疑，且缺乏大规模跨语言验证。

】

---

【Synergizing Semantic Anchors and Ordinal Smoothed Cross-Entropy for Speech Fluency Classification ｜多模态双流融合与序数平滑交叉熵

作者：Mulati Kahaer、Sirajahmat Ruzmamat、XuDong Pang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1896ae1aa686)

> 自动语音流利度评估需同时捕捉宏观语流趋势与微观局部异常，现有方法要么依赖手工统计特征而丢失时序细节，要么依赖预训练模型而缺乏显式语言学先验，且普遍将序数评分视为独立分类问题。本文切入点在于将专家统计特征作为“语义锚点”主动查询动态声学表示，并设计距离感知的序数损失函数。具体做法是构建多模态多流融合分类网络（MMSFC）与序数平滑交叉熵（OSCE）损失。该方案在特定数据集上提升了分类准确率，但其对最新SOTA基线的缺失以及仅聚焦句子级评估的粒度限制，使其在细粒度诊断领域的定位仍存疑。

】

---

【What Do Neural Speech Models Know About Phonology? Evidence from Structured Phoneme Confusions ｜基于音系特征不对称性的神经语音模型错误诊断

研究机构：法国巴黎西岱大学、法国国家科学研究中心

作者：Eli Stafford、Aimée Lahaussois、Guillaume Wisniewski

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c5447da0062a)

> 神经语音识别模型虽在转录准确率上表现优异，但其内部音系结构编码机制不透明，传统探针方法依赖内部表示且易受架构选择干扰。本文提出一种输出中心视角，通过分析音素替换错误在音系特征空间中的不对称性，揭示模型对特定音系特征的保留与丢失偏好。该方法将音素表示为二元特征向量，利用汉明距离量化音系局部性，并通过Bootstrap置信区间和实际等价区域（ROPE）进行严格的效应量估计。该框架在12种语言上验证了错误模式的系统性结构，为连接工程评估与认知语音感知提供了新路径，但其结论受限于自动音素化标签的噪声及仅分析替换错误的设定。

】
