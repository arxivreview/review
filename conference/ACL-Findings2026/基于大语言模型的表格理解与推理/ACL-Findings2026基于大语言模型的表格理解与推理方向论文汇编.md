# ACL-Findings2026 · 基于大语言模型的表格理解与推理方向论文汇编

> 本方向共 11 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CAST: Achieving Stable LLM-based Text Analysis for Data Analytics ｜表格文本分析中的运行间稳定性约束

研究机构：南京大学、清华大学

作者：Jinxiang Xie、Zihao Li、Wei He 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15861)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15861)

> 表格数据中的自由文本列需转化为结构化信号以支持OLAP操作，但大语言模型（LLM）的概率生成特性导致相同输入在多次运行中产生语义漂移的标签或摘要，破坏了下游过滤与聚合的确定性。现有方法如Self-Consistency通过多轨迹投票提升准确率，却忽视了分析场景对输出一致性的刚性需求。本文提出CAST框架，通过算法提示（Algorithmic Prompting, AP）与思维前置（Thinking-before-Speaking, TbS）在单次调用内约束隐式推理路径，实现稳定性提升。该方案在稳定性指标上显著优于基线，但其对复杂多表关联场景的泛化能力尚未得到验证。

】

---

【FACTS: Table Summarization via Offline Template Generation with Agentic Workflows ｜离线模板生成的查询聚焦表格摘要

作者：Ye Yuan、Mohammad Amin Shabani、Siqi Liu

论文原文见 [arXiv](https://arxiv.org/abs/2510.13920)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f1a9c4805b1)

> 查询聚焦表格摘要旨在根据用户意图从表格中生成叙事性洞察，而非仅返回事实值。现有方法要么暴露敏感数据，要么因缺乏可复用性导致计算冗余，且难以保证数值准确性。FACTS 通过生成可复用的离线模板（SQL查询+Jinja2渲染）解决这一矛盾，实现了隐私合规与高效推理。其价值在于将一次性推理转化为可执行资产，但模板对模式漂移的鲁棒性仍存疑。

】

---

【INDOTABVQA: A Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents ｜印尼语文档表格跨语言视觉问答基准

研究机构：印度理工学院

作者：Somraj Gautam、Anathapindika Dravichi、Gaurav Harit

论文原文见 [arXiv](https://arxiv.org/abs/2604.11970)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11970)

> 现有表格视觉问答基准多局限于英语或单语言环境，无法评估模型在低资源语言文档上的跨语言推理能力。本文构建了包含印尼语文档图像与四语言问答对的基准，通过微调与空间先验验证了领域适配的有效性。其价值在于填补了跨语言表格理解的评估空白，但受限于仅使用表格级边界框，未能深入解析细粒度结构错误。

】

---

【MATA: Multi-Agent Framework for Reliable and Flexible Table Question Answering ｜多智能体表格问答框架

研究机构：韩国首尔大学

作者：Sieun Hyeon、Jusang Oh、Sunghwan Steve Cho 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.09642)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09642)

> 表格问答（TableQA）旨在让非技术用户通过自然语言查询结构化数据，但现有方法要么依赖闭源大模型，要么通过固定次数的重复推理换取可靠性，导致计算成本高昂且在小模型上性能崩塌。MATA 的切入点在于将“推理多样性”与“计算预算”解耦，通过轻量级控制器动态决定执行哪些推理路径及何时停止验证。该框架整合思维链（CoT）、程序思维（PoT）和文本转SQL（text2SQL）三条路径，利用调度器（Scheduler）和置信度检查器（Confidence Checker）实现按需调用。其价值在于证明了3B-10B开源模型在复杂表格任务上的可行性，但缺乏对二维结构丢失问题的直接解决，且未在标准基准上与结构表示类SOTA对比。

】

---

【MMTabReal: Real-World Benchmark for Multimodal Table Understanding ｜多模态表格理解基准 MMTABREAL

研究机构：美国亚利桑那州立大学

作者：Prasham Yatinkumar Titiya、Jainil Trivedi、Chitta Baral 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f5ed08d0e38)

> 多模态表格推理旨在让模型同时解析嵌入在二维布局中的文本、数值与视觉线索，但现有基准多依赖合成数据或单一模态，无法反映真实世界中图标、图表与层级表头交织的复杂性。本文切入点在于构建一个纯人工标注、仅用于评估的真实世界多模态表格问答数据集，以量化当前多模态大语言模型（MLLM）在跨模态对齐上的真实短板。通过五种基线策略与多模型对比，MMTABREAL 揭示了视觉输入缺失导致的性能断崖及“高召回低精确”的对齐悖论。该基准填补了真实场景评测空白，但其评估协议依赖特定提示策略，且未涵盖专用表格结构模型，限制了结论的普适性。

】

---

【Moneyball with LLMs: Analyzing Tabular Summarization in Sports Narratives ｜体育叙事动态表格生成的多实体状态追踪诊断

作者：Ritam Upadhyay、Naman Ahuja、Rishabh Baral 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_72dab4199901)

> 长上下文叙事转表格任务的核心矛盾在于，模型需同时维持多实体状态追踪与局部数值聚合，而现有分解策略往往混淆了这两者的贡献。主流方法依赖提示工程或迭代生成，但缺乏对模型内部状态维护机制的因果归因，导致性能提升来源不明。本文通过构建双域体育基准 SPORTABSET，系统性解耦多实体干扰与局部算术能力，并引入标签不变扰动以暴露表面线索依赖。该工作揭示了多实体记忆是长上下文表格生成的主要瓶颈，但其在真实世界噪声表格中的泛化能力仍存疑。

】

---

【ODTQA-FoRe: An Open-Domain Tabular Question Answering Dataset for Future Data Forecasting and Reasoning ｜开放域表格未来数据预测与推理问答

研究机构：北京师范大学、香港浸会大学

作者：Zhensheng Wang、Xiaole Liu、Wenmian Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.02433)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.02433)

> 开放域表格问答长期局限于静态历史数据的检索与提取，无法响应用户对“未来趋势”的预测性询问。现有大语言模型缺乏时序建模机制，且开放域场景下用户无法提供连续历史数据，导致预测任务在数据获取与数值生成两端均存在断点。本文提出 ODTQA-FoRe 任务与 TimeFore 框架，通过 SQL 自主检索历史数据、调用外部时序模型生成预测值、再由 LLM 进行标准化推理，填补了表格问答中动态预测的空白。该工作确立了垂直领域预测问答的基准，但受限于单一房地产数据源，其跨域泛化能力与 LLM 内生预测能力的边界尚待厘清。

】

---

【Retrieve Only Relevant Tables Whether Few or Many: Adaptive Table Retrieval Method ｜自适应表格检索

作者：Taehee Kim、Seungbin Yang、Jihwan Kim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.18766)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f8f703d6fbeb)

> 表格检索旨在从大规模数据库语料中定位回答自然语言查询所需的最小表格子集，是Text-to-SQL任务的关键前置步骤。现有固定Top-k策略因无法预知查询所需表格数量，导致小k漏检关键证据、大k引入噪声并增加延迟，这一矛盾在Spider 2.0等包含数百张表的复杂场景中尤为突出。本文提出自适应表格检索（Adaptive Table Retrieval, ATR），通过查询依赖的阈值机制动态确定检索数量，并结合滑动窗口重排序处理大规模语料。该方法在检索精度与下游执行准确率上均优于固定k基线，但其性能上限受限于纯文本Schema表示，未探索视觉布局信息的潜在增益。

】

---

【SEC-FinTables: Evaluating Large Language Models for Detecting Logical Inconsistencies on Tabular Data ｜金融表格逻辑一致性检测基准

作者：Shuyan Ke、Qiong Wu、Hui Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49e78f4052fb)

> 表格理解领域长期聚焦于从半结构化数据中提取信息以回答自然语言问题，但高 stakes 场景如金融审计更关注数据内部逻辑约束的自洽性。现有 LLM 在数值推理中易产生幻觉，且缺乏针对“内部约束违反”的标准化评测框架，导致无法量化模型在审计任务中的可靠性。本文构建了 SEC-FINTABLES 基准，通过从 SEC 财报中注入受控错误并设计四维评测协议，系统评估主流 LLM 检测逻辑不一致性的能力。该工作揭示了当前模型在细粒度结构定位上的显著短板，但受限于单表设定与纯文本序列化，其结论在复杂层级表格中的普适性存疑。

】

---

【SMART: Semantic Header Flattening and Pseudo-Code-Style Reasoning for LLM-based Complex Table Question Answering ｜语义表头扁平化与伪代码推理

研究机构：华中科技大学

作者：Yongshuo Zhang、Jixiong Chen、Kaihe xu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ce677120608)

> 复杂表格问答的核心难题在于多级表头导致的层级语义在LLM线性化过程中丢失，进而引发推理错位与数值幻觉。现有方法或依赖手工线性化规则，或采用图结构序列化，但均未能有效解耦结构理解与推理执行，导致推理过程脆弱且不可验证。SMART通过语义表头扁平化将层级结构转化为自然语言描述，并引入伪代码风格推理结合外部验证，实现了结构感知与确定性计算的统一。该方法在复杂表格基准上显著优于现有基线，但其对扁平表格的泛化能力及纯文本表示在视觉线索缺失下的鲁棒性仍存疑。

】

---

【TableVista: Benchmarking Multimodal Table Reasoning under Visual and Structural Complexity ｜TableVista：多模态表格推理的视觉与结构复杂度基准

研究机构：同济大学、英国布里斯托大学

作者：Zheyuan Yang、Liqiang Shang、Junjie Chen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05955)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05955)

> 表格理解的核心矛盾在于二维拓扑结构与一维语言序列的表征鸿沟，现有专用模型受限于泛化，通用大语言模型（LLM）又面临序列化导致的空间结构丢失。TableVista 指出，当前多模态大模型（MLLM）在视觉扰动下的推理一致性缺乏系统性评估，其切入点是通过多风格渲染与视觉变换管线，构建包含 30,000 个样本的鲁棒性压力测试集。该基准通过 29 个前沿模型的评估，揭示了模型在复杂结构与视觉集成呈现下的显著性能衰减。其价值在于暴露了视觉空间锚定推理的瓶颈，但缺乏对专用结构编码方法的对比，视觉优势是否源于纯感知仍存疑。

】
