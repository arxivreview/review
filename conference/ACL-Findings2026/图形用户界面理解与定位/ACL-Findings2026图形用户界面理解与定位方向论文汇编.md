# ACL-Findings2026 · 图形用户界面理解与定位方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Screenshots: Evaluating VLMs’ Understanding of UI Animations ｜超越截图：视觉语言模型对UI动画理解的评估

研究机构：美国密歇根大学

作者：Chen Liang、Xirui Jiang、Naihao Deng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3aa785e0b023)

> 现有GUI智能体研究聚焦于静态截图的元素定位，忽略了界面中通过动态变换传达状态反馈的动画通道，导致模型无法完整解析用户交互逻辑。本文构建了首个包含专家与大众双重标注的UI动画数据集AniMINT，并系统评估了9个主流视觉语言模型在动画感知、目的分类与意义解释上的能力。实验表明，尽管模型能识别基础运动原语，但在高阶目的分类上准确率仅0.64，且解释常缺失关键细节。通过引入运动、上下文与感知线索（MCPC）增强，验证了多模态线索协同对提升动画理解的必要性，揭示了当前模型在动态UI理解上的显著短板。

】

---

【FineState-Bench: Benchmarking State-Conditioned Grounding for Fine-grained GUI State Setting ｜细粒度状态条件化 GUI 定位基准

研究机构：美国东北大学

作者：Fengxian Ji、Jingpu Yang、Zirui Song 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27974)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27974)

> 现有 GUI 定位基准仅验证“点击是否命中控件”，忽略了点击后界面状态是否精确达成目标值，导致模型在滑块调节、日期选择等连续交互任务中看似成功实则失效。本文切入点在于将定位任务解耦为“控件定位”与“操作核心命中”两个独立阶段，并引入精确目标状态标签进行验证。通过构建包含双区域标注的静态基准与阶段式诊断指标，量化了视觉定位误差对最终状态达成的可恢复增益。该工作揭示了当前 SOTA 模型在细粒度状态控制上的巨大盲区，但其单步静态协议是否足以反映动态交互中的状态漂移，仍存疑。

】

---

【What's Missing in Screen-to-Action? Towards a UI-in-the-Loop Paradigm for Multimodal GUI Reasoning ｜UI-in-the-Loop：基于强化学习的GUI元素语义理解与推理范式

研究机构：浙江大学

作者：Songze Li、Xiaoke Guo、Tianqi Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06995)

> 现有GUI智能体普遍采用“屏幕-动作”直接映射范式，将界面理解隐式嵌入坐标预测中，导致模型缺乏对UI元素语义功能的显式建模，在复杂布局下易发生黑盒决策失败。本文指出，模型对UI元素定位、语义描述及实际用法的掌握程度直接决定推理成功率，但当前基准仅评估最终动作准确性，忽略了中间理解过程。为此，作者提出UI-in-the-Loop（UILoop）范式，通过UI元素驱动的强化微调（UI-Element-Driven Reinforcement Fine-Tuning, RFT）显式训练模型解析界面元素，并构建了包含26K样本的UI Comprehension-Bench基准。该工作验证了显式UI理解对多步交互成功率的提升作用，但其对纯坐标定位精度的贡献及跨架构泛化能力尚存疑问。

】
