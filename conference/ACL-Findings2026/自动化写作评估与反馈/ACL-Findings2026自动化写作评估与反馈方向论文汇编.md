# ACL-Findings2026 · 自动化写作评估与反馈方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DiffCL: Difference-Aware Contrastive Learning for Automatic Answer Grading with Multi-Level Semantic Modeling ｜差异感知对比学习自动答题评分

作者：Lei Chen、BoYu Gao、Zitao Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_43de595b3a01)

> 自动答题评分（AAG）的核心难点在于模型难以区分学生答案与参考答案的细微语义偏差，导致评分尺度不稳定。现有大语言模型（LLM）评分方法往往依赖表面流畅度，对关键概念遗漏不敏感，且内部表示空间缺乏评分结构优化。本文切入点是将启发式生成的离散差异标签注入输入，并引入双对比学习机制以约束表示空间。该方法在 SciEntsBank 基准上超越了零样本 GPT-4.1，但在 Beetle 数据集上表现低于多智能体框架，其泛化边界尚存疑。

】

---

【EduMARS: Can Vision-Language Models Grade Like Teachers? Benchmarking Multimodal, Rubric-Based Assessment on Chinese K-12 Answers ｜基于检索增强自适应量规的多模态K-12评分基准与框架

作者：Xuan Zhao、Jiashun Chen、Wanting xu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eafe03c214f5)

> 自动评分长期面临真实手写噪声与细粒度评分逻辑缺失的双重挑战，现有基准多依赖合成文本或仅标注最终分数，无法验证模型是否真正理解教师评分过程。本文切入点在于构建首个包含真实手写图像与步骤级评分理由的多模态基准，并设计动态量规合成框架以对齐专家逻辑。其核心做法是提取题目关键点，检索专家评分先验，动态生成案例特定量规后执行步骤级验证。该工作揭示了当前多模态大语言模型在评分过程重建上存在显著性能断层，但检索依赖性与学科覆盖局限仍制约其泛化边界。

】

---

【FeedEval: Pedagogically Aligned Evaluation of LLM-Generated Essay Feedback ｜教学对齐的反馈质量评估框架

研究机构：韩国科学技术院

作者：SeongYeub Chu、Jongwoo Kim、Mun Yong Yi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_86531433e545)

> 自动写作评估（AWE）的核心痛点已从分数预测转向反馈的教学效用，但现有流程盲目信任大语言模型（LLM）生成的反馈，导致低质量噪声污染下游训练。本文切入点在于构建一个独立于生成器的评估器，对候选反馈进行多维度质量筛选。通过训练三个维度特定的 LLM 评估器，FeedEval 实现了与人类专家判断的高对齐，并验证了筛选后反馈能显著提升评分模型性能。其价值在于提供了可量化的反馈质量代理指标，但评估器本身依赖合成数据构建，其泛化边界尚存疑。

】

---

【MAPLE: A Meta-learning Framework for Cross-Prompt Essay Scoring ｜跨提示作文评分的元学习框架

作者：Salam Albatarni、May Bashendy、Sohaila Eltanbouly 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_93aa3ef618b9)

> 跨提示自动作文评分（Cross-Prompt Automated Essay Scoring, CP-AES）旨在解决模型在未见写作提示下的泛化难题，传统端到端模型因提示分布偏移导致性能显著衰减。现有优化型元学习方法将提示视为同质任务，限制了任务多样性，而本文切入点在于利用原型网络的非参数特性，通过重构二元/多类任务并融合上下文门控机制，实现更鲁棒的跨域适应。MAPLE 在 ELLIPSE 和 LAILA 数据集上分别以 8.5 和 3 个 QWK 点的优势超越强基线，证明了元学习在低资源跨域场景的有效性，但其对分数范围不一致数据的处理局限仍存疑。

】

---

【PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback ｜心理测量学感知的作文评分与ZPD对齐反馈框架

研究机构：华东师范大学

作者：Wei Xia、Jin Wu、Haoran Shi 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_87173c424285)

> 自动写作评估（Automated Essay Scoring, AES）面临评分黑盒化与反馈教学价值割裂的双重困境，现有方法难以同时满足测量效度与个性化干预需求。PsyScore 通过共享潜在能力空间，将项目反应理论（Item Response Theory, IRT）嵌入神经评分器，并以此驱动最近发展区（Zone of Proximal Development, ZPD）对齐的多智能体反馈生成。该框架在 ASAP++ 数据集上实现了 0.747 的平均 QWK，验证了心理测量学校准对评分稳定性的贡献，但其反馈教学效应的因果验证仍受限于模拟修订协议。

】
