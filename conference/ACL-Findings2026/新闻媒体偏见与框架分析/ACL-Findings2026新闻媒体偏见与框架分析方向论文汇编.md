# ACL-Findings2026 · 新闻媒体偏见与框架分析方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Multi-View Media Profiling Suite: Resources, Evaluation, and Analysis ｜多视图媒体画像中的动态融合机制

研究机构：丹麦哥本哈根大学

作者：Muhammad Arslan Manzoor、Dilshod Azizov、Daniil Orel 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb374499c508)

> 媒体机构画像旨在通过历史偏见与事实性标签实现大规模实时监测，以替代高成本的单篇验证。现有方法依赖单一文本或静态图结构，在数据稀疏与噪声视图下表现受限，且缺乏对异构信号可靠性的系统评估。本文构建包含三种图结构与两种文本的五视图资源，并提出基于强化学习的动态融合策略，以自适应权重应对视图缺失。该工作确立了ACL-2020上的新基准，但在大规模新数据集MBFC-2025上，其多视图融合性能未超越纯文本基线，揭示了结构信号在大规模场景下的有效性边界。

】

---

【From What Is Said to Why It Is Framed: Intent-Aware News Video Understanding ｜意图条件化的新闻视频理解

研究机构：新加坡南洋理工大学、新加坡国立大学

作者：Xiangzheng Kong、Minnan Luo、Wenya Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a48340f007d6)

> 短新闻视频通过视觉框架与情感信号进行策略性呈现，现有验证方法常将制作风格误判为事实操纵，导致捷径学习。本文提出Origin-Objective-Means（OOM）框架，将沟通意图解耦为创作者立场、受众需求激活与传播策略三个维度，并作为中间语义条件而非预测目标注入推理与检测流程。通过Intent-Guided Prompting（IGP）与ICMD框架，在FakeSV与FakeTT上验证了意图条件化对检测鲁棒性的提升。该方法在特定基准上达到SOTA，但意图标签依赖人工标注且分布不平衡，其跨域泛化能力存疑。

】
