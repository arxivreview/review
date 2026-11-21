# HuggingFace最新推荐论文 ｜Innovator-VL: A Multimodal Large Language Model for Scientific Discovery ｜科学多模态大语言模型

研究机构：上海交通大学、中国科学院

作者：Zichen Wen、Boxue Yang、Shuang Chen 等 34 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19325)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19325)

> 科学多模态大语言模型（Multimodal Large Language Models, MLLMs）旨在解决通用视觉模型在STEM领域推理能力不足的问题，但现有方案依赖海量领域预训练数据且训练流程不透明，导致复现成本高且通用能力受损。本文切入点在于证明无需大规模科学预训练，仅通过原则性数据选择与强化学习后训练即可实现科学推理突破。具体做法是构建基于RICE-ViT与Qwen3-8B的透明训练管线，利用少于500万样本完成监督微调，并采用序列级策略优化强化长程推理。该工作验证了数据效率与通用性可共存，但其科学深度是否受限于缺乏领域预训练仍存疑。

## 研究背景

当模型面对包含复杂符号、图表与空间关系的科学图像时，通用视觉编码器往往无法捕捉细粒度的区域语义，导致下游语言模型在推理时缺乏准确的视觉接地。这种感知瓶颈迫使研究者引入区域感知视觉Transformer（Region-aware Vision Transformer, RICE-ViT），将科学图像分解为语义连贯的视觉单元，以减轻语言推理模块的负担。然而，即便解决了感知问题，科学任务仍要求严谨的多步逻辑推导，这超出了标准监督微调（Supervised Fine-tuning, SFT）所能达到的推理深度，必须依赖强化学习（Reinforcement Learning, RL）来优化长程思维链。

当前科学多模态模型的主流路线倾向于堆砌大规模领域特定预训练数据，如Intern-S1或BigBang-Proton，这种范式虽然提升了特定基准分数，但训练管线往往不透明，且科学能力的提升常以牺牲通用视觉理解为代价。此外，现有方法在评估推理效率时缺乏标准化指标，难以区分模型是真正理解了科学机制还是仅仅消耗了大量Token进行试错。Innovator-VL针对这一痛点，提出了一种完全透明、端到端可复现的训练框架，旨在证明通过高质量数据筛选与序列级强化学习，可以在不依赖大规模科学预训练的前提下，同时保持通用视觉能力与科学推理性能。

## 核心方法

### 多模态架构参照系

Innovator-VL遵循“视觉编码器-投影器-语言模型”的标准三阶段架构。与Qwen3-VL等通用模型不同，本文的关键差异在于视觉端采用RICE-ViT以增强科学图像的结构化感知，语言端直接复用Qwen3-8B-Base而非进行科学领域预训练，从而将优化重心完全后移至SFT与RL阶段。

### 序列级策略优化

针对传统组相对策略优化（Group Relative Policy Optimization, GRPO）中Token级重要性权重与序列级奖励不匹配导致的高方差噪声问题，Innovator-VL引入组序列策略优化（Group Sequence Policy Optimization, GSPO）。该算法将优化单元严格对齐至序列级别，通过长度归一化的序列似然比进行重要性采样与裁剪。其目标函数定义为：

$$
\mathcal{L}_{GSPO} = \mathbb{E}_{x \sim \mathcal{D}, y_i \sim \pi_{\theta_{old}}} \left[ \frac{1}{G} \sum_{i=1}^{G} \min\left( s_i(\theta) A_i, \text{clip}(s_i(\theta), 1-\epsilon, 1+\epsilon) A_i \right) \right]
$$

其中 $s_i(\theta)$ 为基于长度归一化序列似然的重要性比率，$A_i$ 为归一化优势。这一设计消除了Token级更新的不一致性，确保了在长上下文科学推理任务中训练的鲁棒收敛。

### 分层奖励与数据效率

在SFT阶段，Innovator-VL摒弃了海量数据堆砌，转而构建包含野外OCR、化学反应理解等场景的高质量合成数据管线，科学样本总量控制在500万以内。在RL阶段，系统采用分层奖励机制，首先通过精确匹配或符号验证工具（如`math_verify`）确保数学等价性，其次通过格式约束保证结构合规。这种“质量优先于数量”的数据策略，结合GSPO的序列级优化，使得模型在仅使用172K RL数据的情况下，实现了推理链长度的显著缩短与准确率的提升。

## 实验评估

Innovator-VL在37个基准上进行评估，对比模型包括Qwen3-VL-8B、Intern-S1-mini、MiMo-VL-7B等7B-9B规模模型。基线覆盖全面，涵盖了通用视觉、数学推理与科学知识三大类，但缺乏符号回归类专用方法的直接对比。

| 模型 | 通用视觉平均分 | 数学推理平均分 | 科学知识平均分 |
| :--- | :--- | :--- | :--- |
| Innovator-VL-8B-Instruct | 74.50% | - | - |
| Innovator-VL-8B-Thinking | - | 55.41% | - |
| Qwen3-VL-8B-Instruct | 74.71% | - | - |

Innovator-VL-8B-Thinking在数学推理类别取得55.41%的平均分，较Instruct版本绝对提升4.54%，且在所有对比模型中最高。在通用视觉任务上，Instruct版本得分74.50%，与Qwen3-VL-8B的74.71%持平，表明科学对齐未损害通用能力。

在Token效率方面，Innovator-VL-8B-Thinking在MathVerse等基准上生成的推理链长度显著短于MiMo-VL-7B-RL和Intern-S1-mini。其准确率-Token比率（Accuracy-to-token ratio）比MiMo-VL-7B-RL高1.4至2倍，比Intern-S1-mini高3.9至4.3倍。这一结果验证了GSPO在优化推理效率上的有效性，表明模型并非通过冗长试错，而是通过更精准的序列决策达成正确结果。

评估协议采用确定性解码（temperature 0.0），使用`lmms-eval`框架。代码与数据已开源，具备高可复现性。然而，论文未报告置信区间，且科学基准的覆盖范围主要集中在STEM基础题，缺乏对复杂物理定律发现或开放式科学假设生成的评估，限制了对其“科学发现”能力的全面判断。

## 关联研究分析

从数据策略看，Innovator-VL与Intern-S1-Pro形成鲜明对比。后者依赖大规模科学预训练数据以获取深层领域知识，而本文证明在缺乏此类数据时，通过高质量SFT数据与RL后训练仍可达成SOTA性能。这一差异的根源在于任务特性的界定：若科学任务侧重于模式识别与逻辑推导（如数学题、图表理解），则数据效率策略有效；若任务要求发现新物理定律或处理非结构化生物数据，缺乏预训练可能成为瓶颈。

从优化算法看，Innovator-VL采用的GSPO与Debate as Reward等基于多智能体奖励的RL方法存在路径差异。Debate as Reward通过多智能体辩论合成动态奖励信号以优化创意新颖性，而Innovator-VL依赖静态的符号验证与格式约束。这种差异暗示了科学推理与科学创意生成在奖励建模上的根本不同：前者追求确定性与可验证性，后者追求多样性与影响力。Innovator-VL在确定性任务上的优势，是否能在需要探索未知解空间的科学发现任务中保持，论文未给出回答。

## 总结

Innovator-VL旨在解决科学多模态模型依赖海量数据且训练不透明的矛盾，其切入点在于证明原则性数据选择与序列级强化学习可替代大规模预训练。通过RICE-ViT感知增强与GSPO优化，模型在少于500万科学样本下实现了数学推理55.41%的SOTA成绩，同时保持通用视觉能力与Qwen3-VL持平。其边界在于评估基准局限于封闭式STEM问答，未涉及开放式科学假设生成或复杂物理机制发现，且缺乏与符号回归专用方法的直接对比。当任务从“解答已知科学问题”转向“发现未知科学规律”时，缺乏领域预训练的Innovator-VL是否仍能维持其推理优势，是一个亟待验证的问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19325)