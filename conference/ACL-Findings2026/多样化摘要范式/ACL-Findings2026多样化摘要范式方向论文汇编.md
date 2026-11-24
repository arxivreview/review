# ACL-Findings2026 · 多样化摘要范式方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Overlap Metrics: Rewarding Reasoning and Preferences for Faithful Multi-Role Dialogue Summarization ｜多角色对话摘要中的推理内化与偏好对齐

研究机构：华为、中山大学

作者：Xiaoyong Mei、Tingting Zuo、Da Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17188)

> 多角色对话摘要的核心矛盾在于，模型在生成流畅文本时极易产生角色归属错误与事实幻觉，而现有基于表面重叠度或单一语义相似度的优化无法约束深层逻辑一致性。本文切入点在于将结构化认知推理显式嵌入强化学习流程，而非仅作为提示工程。方法采用教师模型蒸馏推理轨迹初始化学生模型，再通过双原则奖励机制的组相对策略优化（Group Relative Policy Optimization, GRPO）进行对齐。该方法在事实忠实性上显著优于主流大语言模型基线，但其效果高度依赖特定奖励权重配置，且在中文数据集上因评估工具缺失而未能完全验证。

】

---

【FOCUS: A Fine-Grained Customer-Oriented Sentiment Dialogue Summarization Dataset for Chinese Customer Service ｜面向客服情感的多方面对话摘要数据集与推理基线

作者：Qian Chen、Mengqiang Hu、Xin Guo

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_03a06a4732c2)

> 导读 电商客服对话摘要需同时捕捉客户对多个服务维度的态度及其情感动态，但现有数据集缺乏细粒度情感标注，导致模型无法区分“对物流满意”与“对退款不满”的细微差异。本文通过构建首个中文客服情感摘要数据集 FOCUS，并引入显式推理机制 COTS2，解决了黑盒生成中方面-情感错配的问题。实验表明，显式推理路径在忠实度与方面覆盖上显著优于直接生成，但当前评估指标对精度惩罚不足，且数据合成痕迹虽经检验仍存疑。

】
