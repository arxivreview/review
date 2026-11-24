# ACL-Findings2026 · 大语言模型路由与成本高效推理方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BiCSRouter: Bi-Level Cross-System Routing for Utility-Aware LLM Inference ｜双层跨系统路由：在单智能体与多智能体范式间动态选择

作者：Mao Keyu、Eiki Murata、Ukyo Honda

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c89307b7d552)

> LLM路由旨在为异构查询匹配最优模型以平衡质量与成本，但现有方法局限于单一计算范式内部，无法同时利用单智能体的深度推理与多智能体的广度协作优势。BiCSRouter将路由问题形式化为跨正交计算范式的层级决策，通过双层结构先优化各范式内部配置，再基于解耦的效用估计选择最优范式。该方法在MBPP上以1.54的成本实现89.40%准确率，较GPT-5基线降低46%成本且仅损失2%精度，但其效用预测器对拓扑结构的依赖是否导致泛化局限尚存疑。

】

---

【IntroLM: Introspective Language Models via Prefilling-Time Self-Evaluation ｜内省式语言模型

研究机构：澳大利亚墨尔本大学、澳大利亚莫纳什大学

作者：Hossein Hosseini Kasnavieh、Gholamreza Haffari、Chris Leckie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03511)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03511)

> 导读 LLM路由的核心矛盾在于：准确预测查询复杂度需要强模型，但部署独立评估器会抵消路由带来的效率收益。现有基于BERT的外部分类器受限于512 token上下文窗口，无法处理现代长上下文部署场景，且引入额外推理开销。本文切入点是将复杂度预测内化到目标模型自身的Prefilling阶段，通过[CPX] token与Token-conditional LoRA实现零额外解码开销的自评估。该方法在长上下文基准上显著优于外部分类器，但其标量预测范式与领域内直接决策趋势的兼容性存疑。

】

---

【LLMRouterBench: A Massive Benchmark and Unified Framework for LLM Routing ｜LLM路由基准与统一评估框架

研究机构：西北工业大学

作者：Hao Li、Yiqun Zhang、Zhaoyan Guo 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07206)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07206)

> LLM路由旨在为每个查询动态分配最适配的模型，以平衡质量与成本。现有研究因模型池、数据集和评估协议各异，导致结果不可比且复现困难。本文构建了包含33个模型和21个数据集的大规模基准，并集成10种代表性路由算法进行统一重评估。该工作揭示了当前路由方法在统一条件下性能趋同且未显著优于简单基线的现象，挑战了复杂路由必然更优的假设，但其结论受限于未覆盖最新强化学习路由方法。

】

---

【QUARTZ: Quantile-Aware Routing and Queueing for TTFT SLOs in LLM Serving ｜分位数感知路由与排队

作者：Zhipeng Liu、Yifan Zheng、Fanqi Kong 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eb781056c7d4)

> 导读 交互式大语言模型服务面临严苛的首字延迟（Time to First Token, TTFT）尾分位数服务等级目标（SLO），但现有路由器忽略请求成本差异，导致长提示请求阻塞短请求，放大尾延迟。本文指出点估计预测与尾SLO目标错位，提出QUARTZ框架，通过预测保守服务时间分位数并据此进行路由与准入决策，在保持公平性的同时降低TTFT尾延迟。该方案在SGLang测试床上验证了跨模型规模的有效性，但其仅针对预填充阶段，解码阶段的延迟优化仍属空白。

】

---

【X-Router: Decoupling Knowledge and Reasoning for Cost-Effective LLM Inference ｜双轴机制路由

研究机构：哈尔滨工业大学、电子科技大学

作者：Zixuan Wang、Yinze Ding、Zihan Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c1801e0c5e23)

> 大语言模型在处理知识密集与逻辑推理任务时，常因静态启用检索增强生成（RAG）与思维链（CoT）而产生冗余计算开销。现有自适应方法多聚焦单一维度，忽视了证据获取与推理深度仅部分相关的特性，导致在逻辑主导或证据缺失场景下出现系统性低效。X-ROUTER 提出双轴路由框架，通过离线效用最大化生成监督信号，在线利用轻量级探测信号独立决策是否检索与是否推理，实现了成本与质量的帕累托优化。该方法在跨域零样本迁移中展现了显著的效率优势，但其对骨干模型能力的依赖及探测信号的普适性仍存疑。

】
