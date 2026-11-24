# ACL-Findings2026 · 计算论证与多智能体辩论方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ArgBench: Benchmarking LLMs on Computational Argumentation Tasks ｜计算论证基准

研究机构：Adobe研究院

作者：Yamen Ajjour、Carlotta Quensel、Nedim Lipka 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17366)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17366)

> 计算论证旨在让模型处理包含冲突视角与发散推理路径的复杂议题，而非单一答案的数学或常识推理。现有LLM评估基准如MMLU仅覆盖单解任务，导致模型在论证挖掘、质量评估等核心技能上的能力盲区无法被量化。本文构建了覆盖33个数据集、46项任务的统一基准，通过提示与留一任务微调两种协议，系统测量了主流LLM在五大论证技能上的表现及跨任务泛化边界。该工作填补了LLM论证能力评估的空白，但其结论受限于自动指标对生成任务的低可靠性，且未涉及多智能体交互场景。

】

---

【Demystifying Multi-Agent Debate: The Role of Confidence and Diversity ｜解构多智能体辩论：置信度与多样性的双重驱动

研究机构：英国剑桥大学、英国谢菲尔德大学

作者：Xiaochen Zhu、Caiqi Zhang、Yizhou Chi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19921)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19921)

> 多智能体辩论（MAD）旨在通过群体交互提升大语言模型（LLM）的推理鲁棒性，但同质智能体下的辩论动态往往退化为鞅过程，无法超越简单多数投票。现有方法多聚焦于增加模型异构性或引入外部裁判，却忽视了初始假设池的覆盖度与信念更新中的权重分配机制。本文从认知科学视角切入，提出多样性感知初始化与置信度调制辩论协议，通过理论证明打破鞅局限，并在六个基准上验证了其对准确率与信念漂移的改善。该方法在7B/8B小模型上表现稳健，但其对异构智能体场景的适用性及置信度校准的泛化能力仍存疑。

】

---

【Free-MAD: Consensus-Free Multi-Agent Debate ｜无共识多智能体辩论框架

研究机构：北京理工大学、清华大学

作者：Yu Cui、Hang Fu、Haibin Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.11035)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.11035)

> 多智能体辩论旨在通过社会交互弥补单模型推理的视角局限，但传统范式依赖“达成共识”作为终止条件，导致从众效应引发错误传播且计算开销巨大。现有方法在追求共识时往往牺牲了推理的独立性与效率，而本文切入点在于彻底解耦辩论过程与判决逻辑，不再将共识视为真理的代理指标。FREE-MAD 通过引入反从众辩论机制与全轨迹评分判决，实现了单轮交互下的高准确率推理。该框架在效率与鲁棒性上展现出优势，但其启发式评分机制在复杂逻辑任务中的理论完备性仍存疑。

】

---

【From Atomic to Complex tasks: Cross-Tasking Improves Zero-Shot Argument Generation and Retrieval ｜论证生成与检索的跨任务泛化

作者：Lynda Tamine、Ahmed Rayane Kebir、Merveille Dona Codjo 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7562b041b855)

> 论证生成（Argument Generation, AG）与论证检索（Argument Retrieval, AR）长期依赖针对特定任务的微调或复杂的提示工程，导致模型在零样本场景下表现脆弱且计算成本高。现有方法未能有效利用论证挖掘中的基础技能，导致复杂任务与原子任务间的知识迁移受阻。本文提出 ArgLLM 框架，通过多任务训练或模型合并将论证结构识别、关系分类与质量评估等原子技能注入大语言模型，实现零样本下的复杂任务泛化。该框架在降低监督成本方面展现出潜力，但其跨任务泛化的边界及与多智能体辩论范式的差异尚存疑。

】
