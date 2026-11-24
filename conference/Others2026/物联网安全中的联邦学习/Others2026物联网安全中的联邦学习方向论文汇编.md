# Others2026 · 物联网安全中的联邦学习方向论文汇编

> 本方向共 5 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【厦门团队新研究：去中心化信任与边缘安全机制综述

研究机构：厦门大学

作者：Khandoker Ashik Uz Zaman、Mahdi H. Miraz、Mohammed N. M. Ali

论文原文见 [arXiv](https://arxiv.org/abs/2604.17179)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17179)

> 物联网边缘环境因设备异构与资源受限，导致集中式安全架构面临单点故障与隐私泄露双重困境。现有联邦学习（Federated Learning, FL）与零信任架构（Zero Trust Architecture, ZTA）各自解决数据本地化或身份验证问题，但缺乏跨机制的信任一致性标准。本文通过系统分类三十项近期研究，构建涵盖FL、区块链、ZTA及图学习的去中心化信任评估框架。其价值在于提供了架构级对比视角，但缺乏定量基准支撑，难以量化各机制在极端非IID场景下的实际鲁棒性差异。

】

---

【基于极端随机树（Extra Trees）的集中式物联网攻击检测

作者：Hikmat A. M. Abdeljaber、Md. Alamgir Hossain、Sultan Ahmad 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08084)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08084)

> 物联网安全检测面临数据异构与隐私约束的双重挑战，传统集中式架构因通信瓶颈与单点故障风险难以适用，而联邦学习虽解决了数据本地化问题，但在极端非独立同分布（Non-IID）场景下模型收敛困难。本文切入点在于回归集中式监督学习范式，利用极端随机树（Extra Trees Classifier）的集成特性与随机化机制，在标准IID假设下追求分类精度的上限。该方法通过严格的预处理与超参数调优，在多个IoT数据集上实现了接近完美的分类指标，但其价值局限于静态、可控的数据环境，无法证明在分布式、对抗性真实IoT场景中的有效性。

】

---

【工业物联网信任收敛加速框架

作者：Aymen Bouferroum、Valeria Loscri、Abderrahim Benslimane

论文原文见 [arXiv](https://arxiv.org/abs/2603.24111)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24111)

> 工业物联网（IIoT）环境中的电磁干扰与多径效应导致网络质量剧烈波动，传统信任模型在此条件下收敛缓慢，形成恶意节点未被识别的脆弱窗口。现有方案多假设网络稳定或依赖昂贵硬件，忽视了动态信道状态对信任评估速度的直接影响。本文提出信任收敛加速（Trust Convergence Acceleration, TCA）机制，利用机器学习预测收敛时间并动态调整马尔可夫链转移概率，在仿真中实现收敛时间最大28.6%的缩减。该框架在理论层面填补了网络质量与信任收敛关联的空白，但缺乏真实工业场景数据验证，其实际部署效能存疑。

】

---

【差分隐私联邦物联网中的自主模型权重修复框架

作者：Chethana Prasad Kabgere、Shylaja S S

论文原文见 [arXiv](https://arxiv.org/abs/2512.13460)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13460)

> 联邦学习在物联网多跳网络中面临非对抗性信道损坏导致的参数失真，现有鲁棒聚合机制仅针对恶意攻击设计，无法处理比特翻转与丢包。本文切入点在于将传输层失真建模为可检测、可重构的信号处理问题，在聚合前进行自适应修复。通过融合差分隐私与安全聚合，DP-EMAR 实现了隐私保护与错误修复的解耦。该框架在 10% 损坏率下将准确率从 82.4% 提升至 94.9%，但其修复能力受限于结构化损坏，对随机噪声的鲁棒性仍存疑。

】

---

【迪肯团队新研究：量子联邦自编码器用于物联网异常检测

研究机构：澳大利亚迪肯大学

作者：Devashish Chaudhary、Sutharshan Rajasegarar、Shiva Raj Pokhrel

论文原文见 [arXiv](https://arxiv.org/abs/2603.22366)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22366)

> 物联网边缘设备面临隐私泄露与单点故障风险，传统集中式检测无法兼顾数据本地化与复杂流量建模。现有联邦学习（FL）方案多依赖经典自编码器，难以高效捕捉高维非线性流量特征，且缺乏在真实硬件层级网络中的量子化验证。本文提出量子联邦自编码器（QFL-QAE），将量子自编码器（QAE）部署于边缘节点，通过分层聚合实现隐私保护下的分布式异常检测。该工作首次验证了量子模型在真实物联网测试床上的联邦可行性，但受限于小规模数据集与单一攻击类型，其量子优势的实际边界尚不明确。

】
