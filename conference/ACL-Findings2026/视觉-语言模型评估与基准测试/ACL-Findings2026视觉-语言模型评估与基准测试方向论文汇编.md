# ACL-Findings2026 · 视觉-语言模型评估与基准测试方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AICA-Bench: Holistically Examining the Capabilities of VLMs in Affective Image Content Analysis ｜情感图像内容分析基准

研究机构：华南理工大学

作者：Dong She、Xianrong Yao、Liqun Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05900)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05900)

> 视觉语言模型（VLM）在感知任务上表现优异，但在情感智能维度上缺乏系统性评估，现有基准多局限于静态分类，无法覆盖情感推理与生成。本文切入点在于构建涵盖理解、推理、生成三维度的全链路基准，并引入基于视觉脚手架的无训练提示框架。通过整合9个数据集与18,124条指令，该工作揭示了模型在情感强度校准上的系统性缺陷，其价值在于填补了情感评估空白，但受限于静态图像与单一语言，跨文化与时序情感能力仍存疑。

】

---

【Almieyar-Oryx-BloomBench: A Bilingual Multimodal Benchmark for Cognitively Informed Evaluation of Vision-Language Models ｜基于布鲁姆分类学的双语多模态认知评估基准

研究机构：加拿大不列颠哥伦比亚大学

作者：Mohammad Mahdi Abootorabi、Omid Ghahroodi、Anas Madkoor 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.05531)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05531)

> 现有视觉语言模型（VLM）评估多聚焦于离散任务或单一认知维度，导致高分掩盖了模型在事实回忆与创造性合成上的深层缺陷。本文切入点在于引入认知科学框架，将多模态任务映射至布鲁姆分类学的六个层级，以诊断模型能力的非对称分布。通过构建包含英语与阿拉伯语的双语基准，并采用基于似然评分的评估机制，量化了模型置信度与准确率的背离。该工作提供了细粒度的认知画像，但受限于闭源模型无法获取内部概率分布，且阿拉伯语评估中混杂了分词器偏差，其跨语言结论的普适性存疑。

】

---

【Evian: Towards Explainable Visual Instruction-tuning Data Auditing ｜可解释视觉指令微调数据审计

研究机构：香港科技大学

作者：Zimu Jia、Mingjie Xu、Andrew Estornell 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20544)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20544)

> 视觉指令微调（VIT）依赖高质量训练数据，但现有过滤方法仅依赖粗粒度相似度分数，无法识别逻辑谬误或事实错误等细微语义缺陷。EVIAN 提出“分解-评估”范式，将响应拆解为视觉描述、主观推理与事实声明，并沿图像-文本一致性、逻辑连贯性与事实准确性三个正交维度进行独立审计。该方法通过 300K 样本基准验证了细粒度审计的有效性，证明小样本高质量数据优于大规模噪声数据，但依赖大型语言模型作为审计器可能引入新的偏见。

】

---

【Lost in Translation: Do LVLM Judges Generalize Across Languages? ｜多语言多模态评估器基准

研究机构：加拿大约克大学、加拿大阿尔伯塔大学

作者：Md Tahmid Rahman Laskar、Mohammed Saidul Islam、Mir Tafseer Nayeem 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19405)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e5fd54c58245)

> 自动化评估器在视觉语言模型（LVLM）对齐与部署中占据核心地位，但现有基准几乎完全局限于英语，导致评估器在非英语场景下的泛化能力成为盲区。VL-RewardBench 等基准虽解决了多模态偏好判断问题，却未触及语言多样性；MRewardBench 虽扩展至多语言，却缺失视觉模态。本文通过翻译构建首个覆盖 25 种语言、60K 实例的多语言多模态评估器基准 MM-JudgeBench，并实证了模型规模与多语言鲁棒性之间的脱钩。该工作填补了评估器可靠性在多语言维度的空白，但其依赖翻译生成的数据可能引入语义漂移，且未验证原生多语言训练的效果。

】

---

【On the Cultural Anachronism and Temporal Reasoning in Vision Language Models ｜文化时代错置与视觉语言模型时序推理基准

作者：Mukul Ranjan、Prince Jha、Khushboo Kumari 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15071)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15071)

> 视觉语言模型在文化遗产数字化应用中面临历史语境误读风险，现有通用基准缺乏对时间维度一致性的系统评估。本文提出“文化时代错置”概念，构建首个针对印度历史文物的时序推理基准 TAB-VLM。通过 600 道多选题量化 10 个前沿模型在年代排序、材质可用性等方面的表现，揭示模型规模与时序推理能力非线性关联。该工作填补了垂直领域评估空白，但单一文化域与静态多选协议限制了结论的普适性。

】

---

【VisTW: Benchmarking Vision-Language Models for Taiwanese Mandarin in Taiwan ｜繁体中文视觉语言模型基准与正字法纯度评估

研究机构：国立台湾大学

作者：Zhi Rui Tam、Yung-Yu Shih、Yen-Wei Lee 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4d7292498fc5)

> 导读 现有视觉语言模型（VLM）评估体系严重依赖英语或简体中文，导致模型在繁体中文（Traditional Chinese, TC）语境下的能力处于未知状态。主流多语言基准缺乏对正字法一致性与地域文化深度的考量，无法捕捉模型在TC语境下的系统性失效。本文构建了首个TC多模态综合基准VisTW，并引入基于人类感知的简体字混入惩罚机制。该工作填补了TC评估空白，但其正字法惩罚是否掩盖了语义理解能力的真实差异，仍存疑。

】

---

【What Users Leave Unsaid: Under-Specified Queries Limit Vision-Language Models ｜查询欠规范对视觉语言模型性能的影响评估

研究机构：韩国延世大学、韩国高丽大学

作者：Dasol Choi、Guijin Son、Hanwool Lee 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06165)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06165)

> 真实用户视觉查询往往省略关键上下文，依赖图像传递隐含信息，而现有基准多采用结构化、显式提示，无法捕捉这一交互常态。这种“查询欠规范”（Query Under-specification）导致模型在真实场景中的表现远低于实验室基准，且现有检索增强手段无法弥补意图缺失。本文通过构建包含平行显式化重写的真实韩语社区基准，量化了欠规范对模型性能的具体折损，并揭示了检索与显式化的非对称收益。该工作揭示了基准难度与模型能力上限的非对应关系，但其结论受限于单一语言文化语境及小样本规模，跨语言泛化性仍需进一步验证。

】
