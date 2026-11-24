# ACL-Findings2026 · 流式视频理解与交互方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【From Static Inference to Dynamic Interaction: A Survey of Streaming Large Language Models ｜流式大语言模型（Streaming LLM）的统一分类与交互机制

研究机构：上海交通大学

作者：Junlong Tong、Zilong Wang、YuJie Ren 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04592)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1ec09d0a64d)

> 流式大语言模型旨在解决静态全上下文范式无法处理无限增量输入与实时交互的矛盾，但现有研究常混淆自回归解码、增量编码与全双工交互，导致概念边界模糊。本文基于数据流与交互并发性，提出输出流式、顺序流式与并发流式的三级分类体系，将流式处理解耦为生成加速、增量感知与架构适配三个独立维度。该框架为流式智能体提供了结构化的技术路线图，但其有效性依赖于分类逻辑的清晰度，缺乏针对具体视频任务的量化验证。

】

---

【mPresenter: An Agentic Framework for Generating Multilingual Presentation Videos from Scientific Papers ｜多语言学术视频生成代理系统

作者：Wenhan Han、Xiao Xiao、Mykola Pechenizkiy 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5bb75c578a43)

> 学术视频生成旨在将静态论文转化为动态视听内容，以解决长文档信息密度高且跨语言理解困难的传播瓶颈。现有单语言流水线系统在处理非英语图表时存在语义断裂，且缺乏针对内容保真度的客观评估基准。本文提出 MPRESENTER，通过规划、审查、编码与解释四个代理的迭代协作，实现多语言论文到视频的高保真转换。该系统在 MPREBENCH 上提升了问答准确率，但其离线迭代架构与实时流式视频理解的因果约束存在本质差异，其多语言泛化能力在极端低资源语言下的鲁棒性仍存疑。

】

---

【ROMA: Real-time Omni-Multimodal Assistant with Interactive Streaming Understanding ｜实时全模态流式助手

研究机构：中国科学院、中科院计算所

作者：Xueyun Tian、Wei Li、Bingbing Xu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10323)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10323)

> 流式视频理解的核心矛盾在于无限输入流与有限上下文窗口的冲突，以及被动响应无法适应实时交互的痛点。现有方法要么仅处理视频而忽略音频，要么将时机决策与内容生成耦合导致语义冲突。ROMA 通过构建同步多模态单元与解耦的 Speak Head，统一了主动与被动交互范式。该框架在主动任务上取得显著优势，但其依赖长上下文 KV 缓存的设计在超长流场景下的显存效率存疑。

】

---

【StreamingEval: A Unified Evaluation Framework towards Realistic Streaming Video Understanding ｜流式视频理解的系统级部署评估框架

研究机构：华东师范大学

作者：Tang Guowei、Tianwen Qian、Huanran Zheng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_79ed3ebd1e2f)

> 流式视频理解要求模型在严格因果约束下处理无限视频流，核心矛盾在于实时响应延迟与长程语义记忆的完整性。现有基准多聚焦于答案准确率，忽视了显存溢出、编码积压与解码延迟对系统可部署性的致命影响，导致“在线”模型在真实流式场景中失效。本文提出 StreamingEval，通过固定容量 FIFO 记忆库标准化历史上下文，并联合评估吞吐量、延迟与准确率。该框架揭示了当前主流模型在严格流式约束下的巨大性能缺口，但缺乏对高级记忆管理策略的差异化验证。

】

---

【StreamMeCo: Long-Term Agent Memory Compression for Efficient Streaming Video Understanding ｜流式智能体记忆压缩

研究机构：上海交通大学、复旦大学

作者：Junxi Wang、Te Sun、Jiayi Zhu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09000)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09000)

> 流式视频理解中，基于智能体记忆图的方法虽能维持长程实体一致性，但记忆节点随视频时长线性增长，导致检索延迟呈非线性上升，无法满足实时交互要求。现有视觉Token或KV Cache压缩策略无法处理外部明文记忆图的结构性冗余。StreamMeCo 提出一种免训练的记忆图压缩框架，通过双分支采样与时间衰减检索机制，在70%压缩率下实现1.87倍检索加速且准确率平均提升1.0%。该工作验证了图结构压缩在工业级流式智能体中的可行性，但其在通用流式基准上的泛化能力及与内部KV Cache管理路线的优劣对比仍存疑。

】
