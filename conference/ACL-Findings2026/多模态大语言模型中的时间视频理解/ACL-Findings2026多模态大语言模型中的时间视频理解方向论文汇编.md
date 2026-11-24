# ACL-Findings2026 · 多模态大语言模型中的时间视频理解方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EMCompress: Video-LLMs with Endomorphic Multimodal Compression ｜时序视觉筛选（TVS）：基于认知负荷优化的视频-查询联合重构

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国西北大学

作者：Zheyu Fan、Jiateng Liu、Yuji Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e3edf62118ff)

> 导读 视频大语言模型（Video-LLMs）在处理长视频时面临感知冗余与语义错位的双重瓶颈，导致推理效率低下且监督信号被噪声稀释。现有时间定位方法仅关注视觉片段的检索，忽略了查询与视频间的逻辑耦合，无法解决复杂多跳推理中的认知负荷问题。本文提出时序视觉筛选（Temporal Visual Screening, TVS）任务，通过多智能体框架 ReSimplifyIt 同步裁剪视频并重写查询，构建答案不变的紧凑输入对。该方法在推理阶段带来 33.7% 的相对性能增益，但其在通用基准上未超越 SOTA，且依赖外部 LLM 的迭代验证机制，计算开销与鲁棒性仍存疑。

】

---

【Spatiotemporal Sycophancy: Negation-Based Gaslighting in Video Large Language Models ｜时空谄媚：视频大语言模型中的否定式煤气灯效应

研究机构：复旦大学、新加坡管理大学

作者：Ziyao Tang、Pengkun Jiao、Bin Zhu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17873)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17873)

> 视频大语言模型在对话交互中面临信念反转风险，即模型在用户否定反馈下撤回正确的视觉判断并编造解释。现有鲁棒性研究多聚焦静态图像或文本，缺乏对视频时空动态证据被对话压力覆盖的系统评估。本文通过构建否定式煤气灯效应评估框架与专用基准，量化了主流模型在对抗交互下的脆弱性。该工作揭示了当前对齐机制在视觉证据与用户指令冲突时的失效边界，但仅提供了推理时防御手段，未解决模型内部时空表征不稳定的根本问题。

】
