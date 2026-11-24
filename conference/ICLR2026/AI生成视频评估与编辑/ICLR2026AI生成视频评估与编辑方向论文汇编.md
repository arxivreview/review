# ICLR2026 · AI生成视频评估与编辑方向论文汇编

> 本方向共 5 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning ｜统一图像与视频编辑生成框架

研究机构：Adobe研究院、香港中文大学

作者：Xuan Ju、Tianyu Wang、Yuqian Zhou 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.20360)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20360)

> 视频编辑领域长期受困于架构碎片化与数据稀缺的双重瓶颈，现有方法要么依赖特定任务分支，要么受限于低质量数据集。本文切入点在于将多模态统一为单一序列，利用全自注意力机制实现跨模态知识迁移。通过构建混合数据管道与四维位置编码，EditVerse在单一模型内同时支持图像与视频的生成及编辑。该框架验证了图像域知识对视频编辑的有效补充，但其对物理合理性的隐式依赖与缺乏闭环评估机制，使其在复杂语义场景下的鲁棒性仍存疑。

】

---

【IVEBench: Modern Benchmark Suite for Instruction-Guided Video Editing Assessment ｜指令引导视频编辑基准

研究机构：浙江大学、上海交通大学

作者：Yinan Chen、Jiangning Zhang、Teng Hu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11647)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11647)

> 指令引导视频编辑（Instruction-guided Video Editing, IVE）旨在通过自然语言指令直接驱动视频内容变换，但现有评估体系多针对源-目标提示范式，无法量化指令遵循度与非编辑区域保真度。IVEBench 通过构建覆盖 8 类任务的 600 视频数据集，并引入多模态大语言模型（MLLM）辅助的三维评估协议，填补了 IVE 系统性评估的空白。该基准揭示了当前 SOTA 方法在指令合规性上的显著短板，但其对长视频时序漂移的捕捉能力仍存疑。

】

---

【MIMIC-BENCH: EXPLORING THE USER-LIKE THINK ING AND MIMICKING CAPABILITIES OF MULTIMODAL LARGE LANGUAGE MODELS ｜模拟用户思维与行为的多模态大模型基准

研究机构：上海交通大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_1840682)

> 现有视频理解基准聚焦于“发生了什么”的视觉事实问答，无法衡量模型是否具备模拟真实用户认知与社交反应的能力。MIMIC-Bench 将评估焦点从视觉感知转移至人类对齐的社交推理与语言模仿，通过构建包含 150K+ 真实用户生成视频的数据集及 4,000 个高互动样本的测试集，定义了创作者意图理解、内容属性匹配与用户互动理解三大推理轴，并引入评论模仿任务。该工作通过微调 InternLM2-8B 构建 MIMIC-Chat，验证了领域特定对齐在模拟人类行为上的有效性，但其对长尾文化语境及细粒度情感维度的覆盖仍显不足。

】

---

【UniVideo: Unified Understanding, Generation, and Editing for Videos ｜统一视频理解与生成框架

研究机构：加拿大滑铁卢大学、快手

作者：Cong Wei、Quande Liu、Zixuan Ye 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08377)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08377)

> 多模态大模型在图像域已实现理解与生成的统一，但视频域仍被割裂为独立的生成器与编辑器，导致复杂指令解析与细粒度视觉编辑无法协同。现有专用模型依赖任务特定模块，难以处理多模态提示或跨任务组合。UniVideo 通过 MLLM 与 MMDiT 的双流架构，将语义推理与视觉重建解耦并并行输入，实现了视频域的统一建模。该框架在上下文编辑任务上超越了专用基线，但在纯文本生成视频的质量上略逊于专用 SOTA 模型，其统一性是否以牺牲专项性能为代价尚存疑。

】

---

【VidGuard-R1: AI-Generated Video Detection and Explanation via Reasoning MLLMs and RL ｜VidGuard-R1：基于强化学习推理的多模态大模型视频真实性检测

研究机构：美国德克萨斯大学奥斯汀分校、微软研究院

作者：Kyoungjun Park、Yifan Yang、Juheon Yi 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02282)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02282)

> 导读 AI生成视频检测旨在区分真实视频与合成视频，并解释判定依据。传统检测器依赖空间-时间一致性或频率伪影，难以捕捉高层语义与因果逻辑错误，且缺乏可解释性。VidGuard-R1将多模态大语言模型（MLLM）与群体相对策略优化（GRPO）结合，通过设计针对时序伪影和扩散步数的专用奖励函数，引导模型进行物理感知的推理。该方法在GenVideo基准上取得96%的F1分数，但其在未见生成模型上的泛化鲁棒性及推理成本仍是关键存疑点。

】
