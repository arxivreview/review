# ACL-Findings2026 · 全双工口语对话系统方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【F-Actor: Controllable Conversational Behavior in Full-Duplex Models ｜F-Actor：指令跟随的全双工语音对话模型

研究机构：德国卡尔斯鲁厄理工学院、英国爱丁堡大学

作者：Maike Züfle、Ondrej Klejch、Nicholas Sanders 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0dbd163f6f0b)

> 全双工语音对话系统（Full-Duplex Spoken Dialogue Systems, FD-SDS）旨在实现机器在说话的同时持续监听，以支持自然的中断处理与回授。现有端到端模型虽能处理重叠语音，但缺乏对系统自身行为（如回授频率、中断时机）的显式控制，导致交互风格僵化且难以适配不同场景。本文提出F-Actor，通过冻结音频编码器并仅微调LLM，在2000小时数据上实现了对说话人音色、对话主题及回授/中断计数的指令跟随。该模型在学术资源下验证了可控全双工训练的可行性，但其对低频行为模式的精确控制能力仍受限于训练数据分布。

】

---

【MTR-DuplexBench: Towards a Comprehensive Evaluation of Multi-Round Conversations for Full-Duplex Speech Language Models ｜多轮全双工语音语言模型评估基准

研究机构：清华大学、香港中文大学

作者：He Zhang、Wenqian Cui、Haoning Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.10262)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10262)

> 全双工语音交互的核心挑战在于机器需同时监听与生成，但现有评估基准仅覆盖单轮交互，无法量化模型在长程对话中的状态稳定性与上下文一致性。本文切入点在于解决连续音频流中“轮次边界模糊”与“模型响应偏离导致上下文不一致”的评估失效问题。通过构建基于GPT-4o聚类投票的轮次分割算法与历史轮次真值填充机制，实现逐轮独立评估。该基准揭示了当前主流模型在多轮交互中性能显著衰减的普遍现象，但评估协议对合成数据的依赖及单一考官模型的偏差仍存疑。

】

---

【Optimizing Conversational Quality in Spoken Dialogue Systems with Reinforcement Learning from AI Feedback ｜面向语音对话系统的多奖励强化学习自反馈对齐

研究机构：美国卡内基梅隆大学

作者：Siddhant Arora、Jinchuan Tian、Jiatong Shi 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc71a42ac1e6)

> 全双工语音对话系统（Full-Duplex Spoken Dialogue Systems, FD-SDS）在实现实时交互后，面临语义连贯、音频自然度与情感一致性难以同时优化的困境。现有强化学习自反馈（Reinforcement Learning from AI Feedback, RLAIF）方法仅针对单一语义维度，且假设完整话语反馈，无法适配流式块级解码。本文提出数据集级多奖励直接偏好优化（Direct Preference Optimization, DPO）框架，通过块级对数概率聚合解决话语级偏好与增量生成的错位。该框架在语义与声学指标上均取得一致提升，但缺乏对多奖励冲突机制的深入消融，其联合优化是否导致局部最优仍存疑。

】
