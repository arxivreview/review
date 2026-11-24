# Others2026 · 指令微调方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【哈尔滨工业团队新研究：任务导向对话的Schema感知指令微调

研究机构：哈尔滨工业大学、中南大学

作者：Dechuan Teng、Chunlin Lu、Libo Qin 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09691)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09691)

> 任务导向对话（Task-Oriented Dialog, TOD）系统需精准执行多轮交互中的状态追踪与数据库查询，但现有端到端模型往往绑定特定数据集的标注结构，难以迁移至新场景。传统预训练对话模型（Pre-trained Conversation Models, PCMs）通过多任务预训练提取通用知识，却忽略了数据标注与底层数据库Schema的强耦合，导致跨域适配能力薄弱。本文提出ESAinsTOD框架，通过指令对齐与Schema对齐机制，将异构TOD数据统一为指令微调语料，使大语言模型（Large Language Models, LLMs）在保持通用能力的同时精准遵循特定Schema。该框架在MultiWOZ等基准上显著优于基线，但其对全参数微调的依赖及缺乏与通用指令微调方法的横向对比，限制了其结论的普适性。

】
