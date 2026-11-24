# ACL2026最新论文 ｜MT3: A Synergistic Multi-Task RL Framework for Specializing MLLMs in Text Image Machine Translation ｜多任务强化学习特化多模态大语言模型用于文本图像机器翻译

研究机构：浙江大学、中国科学院大学

作者：Zhaopeng Feng、Yupu Liang、Shaosheng Cao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_68ca5ab36cf7)

> 文本图像机器翻译（TIMT）要求系统从图像中提取文本并生成目标语言译文，现有级联系统因模块间误差传播导致翻译失败，而端到端模型又缺乏对识别与视觉理解的显式建模。MT3 通过协同多任务强化学习（Multi-Task RL）将通用多模态大语言模型（MLLMs）特化为 TIMT 专家，在 MIT-10M 基准上以 7B 参数规模超越 72B 与 78B 的零样本基线。该框架验证了零样本 RL 优于监督微调（SFT）的有效性，但其对视觉依赖度的实际增强程度及文化适应性量化仍缺乏直接证据。

## 研究背景

TIMT 的核心困境在于视觉感知与语言生成的耦合。光学字符识别（OCR）错误会直接导致翻译失败，这是级联系统（OCR+MT）的固有缺陷；而端到端模型虽统一了训练流程，却往往隐式处理视觉信息，未能显式建模布局、对象等视觉元素对翻译质量的贡献。这种“通用能力与专家级熟练度之间的差距”构成了当前 MLLM 在 TIMT 任务上的主要瓶颈。

领域主流路线正从级联系统向端到端 MLLM 迁移，但现有方法多依赖 SFT 或提示工程，缺乏针对 TIMT 多面性（识别准确性、视觉推理、翻译质量）的精细化优化机制。MT3 的切入点在于引入规则基强化学习（RL），通过显式分解识别、推理、翻译三阶段，并利用多混合奖励机制提供细粒度反馈，从而在可控且系统化的方式下实现 MLLM 的领域特化。

## 核心方法

### 方法参照系

标准 TIMT 流程通常将任务视为黑盒，直接映射图像到译文。MT3 的关键差异在于将 TIMT 解构为三个显式子任务：识别（Recognition）、推理（Reasoning）与翻译（Translation），并在单一 MLLM 内通过 GRPO 算法进行联合优化，而非依赖外部工具或独立模块。

### 多任务分解与结构化生成

MT3 将生成过程转化为可控管道，强制模型在 `<recognize>` 标签内按自然阅读顺序转录文本，在 `

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_68ca5ab36cf7)