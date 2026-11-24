# ACL-Findings2026 · 地理空间视觉-语言理解方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CompassLLM: A Multi-Agent Approach toward Geo-Spatial Reasoning for Popular Path Query ｜多智能体协同路径查询框架

研究机构：澳大利亚莫纳什大学

作者：Md. Nazmul Islam Ananto、Shamit Fatin、Mohammed Eunus Ali 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07516)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07516)

> 地理空间路径推荐旨在从历史轨迹中推断两点间最常被使用的路线，但传统机器学习模型在数据更新时需重训练，而通用大语言模型（LLM）直接生成路径常出现不可遍历的幻觉。本文切入点在于将路径查询解耦为“检索”与“合成”两个条件阶段，通过多智能体协同编排，在无需重训练的前提下处理稀疏数据下的路径缺失问题。该方法利用LLM的图结构推理能力，在检索任务上超越基线，在合成任务上达到与专用深度学习模型相当的可行性，但其性能仍受限于LLM上下文窗口与随机性。

】

---

【EVGeoQA: Benchmarking LLMs on Dynamic, Multi-Objective Geo-Spatial Exploration ｜动态多目标地理空间探索基准与评估框架

研究机构：北京师范大学、国防科技大学

作者：Jianfei Wu、Zhichun Wang、Zhensheng Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07070)

> 现有地理空间问答（GSQA）基准多局限于静态拓扑检索，无法评估大语言模型（LLM）在动态位置约束下的复合规划能力。本文切入点在于将定位任务重构为“实时坐标锚定+双目标约束”的动态探索问题，通过构建EVGeoQA基准与GeoRover工具增强智能体框架，量化LLM在长距离空间推理中的性能衰减。该工作揭示了LLM在长程探索中的“懒惰”现象与轨迹总结潜力，但缺乏对探索策略的显式优化机制，其结论的泛化性受限于特定城市与单一领域场景。

】

---

【ReaGeo: Reasoning-Enhanced End-to-End Geocoding with LLMs ｜ReaGeo：基于大语言模型的端到端地理编码

研究机构：阿里巴巴集团、清华大学

作者：Jian Cui、Zhiyuan Ren、Desheng Weng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21357)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21357)

> 地理编码旨在将人类可读的地址文本转换为机器可识别的坐标，传统方法依赖复杂的实体提取与数据库检索，易受地址歧义与数据覆盖限制。本文提出ReaGeo，通过大语言模型直接生成Geohash序列，结合思维链推理与强化学习，实现端到端坐标预测。该方法在模糊地址解析上显著优于传统检索与通用大模型，但其纯文本模态与单一城市数据源限制了跨地域泛化能力的验证。

】

---

【Thinking with Map: Reinforced Parallel Map-Augmented Agent for Geolocalization ｜地图增强代理式地理定位

研究机构：厦门大学、阿里巴巴集团

作者：Yuxiang Ji、Yong Wang、Ziyu Ma 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05432)

> 图像地理定位旨在从视觉线索推断拍摄地点的经纬度，核心难点在于开放世界中线索稀疏且易产生幻觉。传统方法依赖静态特征匹配或内部知识推理，缺乏对外部地理信息的动态验证机制，导致细粒度定位精度受限。本文提出“地图增强代理”框架，通过引入地图API工具实现假设-验证闭环，并结合强化学习与并行测试时缩放优化推理效率。该方法在细粒度定位上显著超越闭源模型，但粗粒度性能仍受基座模型能力制约，且地图工具引入初期曾导致全局认知偏差。

】
