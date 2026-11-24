# ACL-Findings2026 · 计算叙事理解与生成方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BOOKAGENT: Orchestrating Safety-Aware Visual Narratives via Multi-Agent Cognitive Calibration ｜多智能体认知校准故事书合成

研究机构：美国卡内基梅隆大学、中国科学技术大学

作者：Bo Gao、Chang Liu、Yuyang Miao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16541)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16541)

> 多模态视觉叙事生成面临角色身份漂移与儿童内容安全缺失的双重瓶颈，现有方法多采用单向流水线或后处理过滤，难以实现全局一致性。本文切入点在于将安全审计前置至规划阶段，并引入全局时序校准机制，构建端到端闭环多智能体框架。通过价值对齐故事板、迭代跨模态精炼与时序认知校准三阶段协同，实现文本与图像的联合优化。该框架在高约束场景下显著提升了跨帧一致性，但其计算成本随页数线性增长，且缺乏对真实绘本分布的泛化验证。

】

---

【Lost in Stories: Consistency Bugs in Long Story Generation by LLMs ｜长程叙事一致性基准与自动化检测

作者：Junjie Li、Xinrui Guo、Yuhao Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05890)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05890)

> 长程叙事生成面临的核心挑战是模型在数千词跨度内维持事实、逻辑与风格的一致性，而非仅保证局部流畅。现有评估多聚焦情节连贯性，缺乏对跨上下文矛盾的系统化隔离与可复现检测机制。本文构建了包含2000个提示的ConStory-Bench基准，并开发了基于显式证据链的ConStory-Checker自动化评估流水线，将一致性错误量化为可审计的细粒度指标。该工作填补了长程叙事一致性评估的空白，但其依赖单一LLM评判者且仅限英文虚构文本，评估的普适性与评判者偏差仍是关键存疑点。

】

---

【Planning Beyond Text: Graph-based Reasoning for Complex Narrative Generation ｜超越文本的图推理叙事生成

研究机构：中国科学院

作者：Hanwen Gu、Chao Guo、Junle Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21253)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21253)

> 长程叙事生成面临的核心困境是模型在文本序列上直接规划时，无法有效推理事件间的因果依赖与角色关系的动态演变，导致逻辑断裂与动机缺失。现有基于大纲或角色扮演的多智能体方法虽提升了局部连贯性，但受限于线性文本表征，难以在生成前诊断并修复全局结构缺陷。PLOTTER 将叙事规划从序列文本迁移至事件图与角色图的拓扑结构，通过“评估-规划-修订”循环执行原子图编辑操作，在文本生成前完成因果逻辑的显式校验。该方法在多个骨干模型上显著优于基线，验证了图结构表征对长程因果推理的增益，但其对非线性叙事结构的表达能力及小样本前提下的泛化边界仍存疑。

】

---

【Style over Story: Measuring LLM Narrative Preferences via Structured Selection ｜风格优先于故事：通过结构化选择测量大语言模型的叙事偏好

研究机构：韩国科学技术院

作者：Donghoon Jung、Jiwoo Choi、Songeun Chae 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02025)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a36d56f54ac)

> 计算叙事领域长期依赖生成输出来评估模型能力，但输出质量混淆了“生成能力”与“内在偏好”，导致无法区分模型是“写不好”还是“不想写”。现有评估指标与人类感知错位，且缺乏对模型潜在叙事优先级的直接测量手段。本文提出一种基于200条叙事学约束的结构化选择任务，通过量化模型在受控条件下的选择行为来揭示其潜在偏好。该方法实证了模型对风格元素的系统性优先，但静态选择偏好能否预测动态生成中的风格漂移，尚存疑。

】
