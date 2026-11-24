# ACL-Findings2026 · 多模态大语言模型中的图表理解方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AnalystBench: Benchmarking professional long-form report generation with web-mined multimodal tasks ｜分析师基准

作者：Chau Minh Pham、Zichao Wang、Puneet Mathur 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_742d41604e3b)

> 长文档专业报告生成面临输入规模巨大、多模态混杂且缺乏标准答案的评估困境，现有基准多依赖人工设计或单一模态，难以规模化验证模型在真实工作流中的端到端能力。AnalystBench通过反向工程从网络专业报告中自动构建任务，解决了数据获取与评估一致性的矛盾。其核心在于利用自动化工具生成可复用的任务变体，并引入基于检查表的专家验证评估协议。该基准揭示了当前大模型在长程综合任务上的显著性能断层，但评估指标对主观写作质量的覆盖仍显不足。

】

---

【Assessing Y-Axis Influence: Bias in Multimodal Language Models on Chart-to-Table Translation ｜Y轴偏差控制与视觉显著误差度量

研究机构：美国爱荷华州立大学

作者：Seok Hwan Song、Azher Ahmed Efat、Wallapak Tavanapong

论文原文见 [arXiv](https://arxiv.org/abs/2604.24987)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24987)

> 图表到表格翻译任务中，多模态大语言模型（MLM）的性能受Y轴信息分布不均的隐性干扰，导致模型在特定刻度格式或数值范围下出现系统性偏差。现有基准如PlotQA和ChartQA存在严重的数字长度分布失衡，且传统评估指标无法区分视觉上显著的误差与微小波动，使得偏差难以被量化和归因。本文通过构建控制变量的FairChart2Table基准集，并引入基于刻度间隔的误差度量，系统揭示了Y轴特征对模型提取精度的影响。该工作填补了细粒度偏差评估的空白，但其结论局限于合成数据环境，未验证在真实噪声图表中的泛化性。

】

---

【Beyond Single Plots: A Benchmark for Question Answering on Multi-Charts ｜多图表问答基准与视觉分解验证管线

研究机构：美国爱荷华州立大学

作者：Azher Ahmed Efat、Seok Hwan Song、Wallapak Tavanapong

论文原文见 [arXiv](https://arxiv.org/abs/2604.21344)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21344)

> 多模态大语言模型（MLLMs）在单图表理解上已趋于成熟，但在真实科研场景中常见的多子图复合图像上，模型因缺乏显式定位指引而性能骤降。现有基准如MultiChartQA依赖“第一张图”等显式引用，掩盖了模型在自然语境下自主定位子图的能力缺陷。本文构建了无显式引用的真实多图表基准PolyChartQA，并提出视觉分解与自验证（VDSP）提示管线，通过结构化拆解推理过程提升模型在复杂多图场景下的准确率与可解释性。该工作填补了多图评测的空白，但仅依赖提示工程，未触及模型底层视觉编码机制的局限。

】

---

【ComicVQA: A Benchmark for Visual Reasoning in Multimodal LLMs ｜漫画视觉问答基准

研究机构：新加坡国立大学、捷克布拉格捷克理工大学

作者：Esther Gan、Hannah Brown、David Herel 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c2baab84154c)

> 多模态大语言模型（MLLMs）在单图视觉问答中常依赖语言先验而非真实视觉接地，且缺乏对离散静态图像序列的时序推理能力。现有漫画基准往往将视觉感知与叙事逻辑纠缠，无法诊断模型失败源于感知缺陷还是推理断裂。本文构建ComicVQA，通过去除文本的缺失面板预测和面板排序双任务，解耦细粒度视觉接地与组合时序推理。该基准揭示了当前MLLMs在局部因果推理上的显著短板，但受限于自动分割噪声与单一分辨率设置，其诊断结论的普适性仍需进一步验证。

】

---

【Hierarchical Visual Agent: Managing Contexts in Joint Image-Text Space for Advanced Chart Reasoning ｜层级视觉智能体：联合图文空间中的上下文管理

研究机构：美国东北大学、美国莱斯大学

作者：Qihua Dong、Ruozhen He、Junwen Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.04304)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04304)

> 复杂图表推理要求模型在多个子图间进行多步数值计算，但现有多模态大语言模型（MLLMs）在处理此类任务时，常因累积的异构上下文导致早期关键证据被稀释或遗忘。本文指出，线性追加视觉裁剪与文本推理轨迹的“Thinking with Images”范式存在单调上下文膨胀缺陷，提出HIERVA，一种免训练的Manager-Worker层级架构，通过上下文蒸馏与封装将全局上下文保持紧凑。该方法在CHARXIV推理子集上达到64.2%准确率，验证了层级化上下文管理对复杂推理的有效性，但其免训练策略在极端复杂场景下的鲁棒性仍存疑。

】

---

【OmniDiagram: Advancing Unified Diagram Code Generation via Visual Interrogation Reward ｜通用逻辑图代码生成中的视觉验证奖励机制

研究机构：中国科学院、中国科学院大学

作者：Haoyue Yang、Xuanle Zhao、Xuexin Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05514)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05514)

> 多模态大语言模型在将视觉图表转化为可执行代码时，常面临语法正确性与视觉保真度脱节的困境。现有方法多依赖单一任务或固定语言，且强化学习中的二元奖励信号难以捕捉细粒度结构差异。本文提出VIVA机制，通过生成实例特定的视觉问题来评估渲染结果，实现细粒度反馈。该框架在通用逻辑图生成上超越了专用代码模型，但其对VQA评估模型的依赖及离线问题生成的泛化边界尚存疑。

】

---

【PlotGen-Bench: Evaluating VLMs on Generating Visualization Code from Diverse Plots across Multiple Libraries ｜多库动态可视化代码生成基准

作者：Yi Zhao、Zhen Yang、Shuaiqi Duan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c82832a867c4)

> 现有图表转代码基准局限于静态二维图与单一绘图库，无法评估模型在三维、动画及跨框架场景下的真实生成能力。PlotGen-Bench 通过构建涵盖 30 种图表类型、5 个 Python 库及 3 类任务（复制、转换、多库生成）的基准，填补了动态可视化评估空白。其核心贡献在于引入混合评估协议，结合执行率与视觉相似度评分。该基准揭示了通用视觉语言模型在复杂时序与跨库语法泛化上的显著短板，但缺乏专用图表模型的对比，限制了结论的普适性。

】
