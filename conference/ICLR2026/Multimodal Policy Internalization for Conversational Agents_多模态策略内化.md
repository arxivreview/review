# ICLR2026最新论文 ｜Multimodal Policy Internalization for Conversational Agents ｜多模态策略内化

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Zhenhailong Wang、Jiateng Liu、Amin Fazel 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.09474)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09474)

> 多模态对话智能体依赖长文本策略（Policy）来约束行为，但将策略作为上下文提示（In-Context Prompt）会导致推理时巨大的固定计算开销，且模型难以稳定遵循复杂规则。现有提示压缩方法仅针对简单模板，无法处理需要多跳推理的业务策略，而文本领域的审慎对齐（Deliberative Alignment）又缺乏多模态支持。本文提出多模态策略内化（Multimodal Policy Internalization, MPI）任务，通过三阶段训练框架 TriMPI 将策略知识写入模型参数，实现无上下文依赖的策略遵循。该方法在自建基准上显著提升了策略执行准确率，但缺乏对通用能力退化的全面量化，且未验证内化策略是否加剧视觉幻觉。

## 研究背景

多模态大语言模型（MLLMs）在处理复杂业务逻辑时，通常依赖预定义的策略上下文，这些策略包含工具调用规则、响应风格及元数据，长度可达 1K 至 50K tokens。这种长上下文不仅造成 20 至 250 倍的输入 token 成本，还因规则分布分散导致模型遵循率下降。为了解决这一效率与准确性的矛盾，研究界尝试将策略知识从上下文迁移至模型参数，即策略内化。

当前主流路线存在明显瓶颈。提示压缩方法（如 LLMLingua）侧重于减少模板和演示示例的长度，但这类内容仅需极少推理即可遵循，无法处理涉及多跳决策的复杂策略。审慎对齐（Deliberative Alignment）虽能内化安全规范，但局限于纯文本模型，且未解决多模态输入中视觉 token 与策略文本的交互问题。本文切入点在于构建首个多模态策略内化基准，并设计专门针对视觉-文本混合策略的训练算法，以消除推理时的上下文依赖。

## 核心方法

### 方法参照系

本文问题属于知识注入与对齐的交叉领域，最接近的通用流程是“持续预训练（Continual Pretraining, CPT）+ 监督微调（SFT）”。然而，标准 CPT 在文本领域有效，但在多模态场景中，直接对包含视觉 token 的策略进行语言建模会导致视觉特征干扰文本策略的学习，且 SFT 仅学习输入-输出映射，无法利用策略本身的逻辑结构作为训练引导。

### 视觉掩码持续预训练（VM-CPT）

在标准 CPT 流程中，模型对所有输入 token 计算下一词预测损失。本文在 CPT 阶段引入视觉掩码机制，仅对策略文本、查询、思维链（CoT）及答案部分计算损失，屏蔽所有视觉 token。这一设计解决了多模态输入中视觉特征维度高且分布与文本差异大，导致策略文本学习信号被稀释的问题。其目标函数定义为：

$$
\mathcal{L}_{\text{VM-CPT}} = -\sum_{t=1}^{T} m_t \log P_\theta(x_t | x_{<t}, I, P)
$$

其中 $m_t$ 为掩码指示变量，当 $x_t$ 为视觉 token 时 $m_t=0$，否则为 1。通过屏蔽视觉 token，模型专注于学习策略文本的语义结构，将策略知识显式注入参数，为后续推理提供基础。

### 策略感知强化学习（PolicyRollout）

SFT 阶段仅学习期望行为，缺乏对策略逻辑的探索，导致在复杂策略下泛化能力弱。本文在强化学习（RL）阶段引入 PolicyRollout（PoRo），扩展了 GRPO 的 rollout 空间。具体而言，对于每个查询，模型生成两组响应：一组无策略上下文（No-Policy），一组包含策略上下文（Policy-Aware）。PoRo 将这两组响应合并计算优势值，但策略梯度仅作用于无策略路径。其目标函数为：

$$
\mathcal{L}_{\text{PoRo}} = \mathbb{E}_{(Q,I) \sim \mathcal{D}} \left[ \frac{1}{|G|} \sum_{i \in G_{\text{no-policy}}} A_i \log \frac{\pi_\theta(y_i|Q,I)}{\pi_{\text{ref}}(y_i|Q,I)} \right]
$$

其中 $G_{\text{no-policy}}$ 为无策略响应集合，$A_i$ 为基于合并 rollout 计算的优势值。这一设计允许模型利用策略上下文生成的“正确”响应作为探索引导，同时确保训练与推理条件一致（推理时无策略），解决了标准 RL 中探索空间缺乏策略引导导致奖励稀疏的问题。

## 实验评估

实验基于 Qwen2.5-VL-7B 骨干，在自建 ClevrPolicy（合成决策树）和 GTAPolicy（真实工具调用）上进行。基线覆盖 In-Context、Direct SFT、CoT SFT 及标准 GRPO/DAPO，但未对比知识库中的 DPO 变体（如 SCPO）或奖励模型方法，限制了跨范式比较。

| 方法 | ClevrPolicy-T (N=6) Acc | ClevrPolicy-M (N=6) Acc | GTAPolicy Overall |
| :--- | :--- | :--- | :--- |
| In-Context | 13.15 | 5.65 | 21.51 |
| CoT SFT | 17.80 | 14.30 | 54.50 |
| TriMPI w/ PoRo-GRPO | 65.85 | 84.70 | 81.06 |
| TriMPI w/ PoRo-DAPO | 77.80 | 85.00 | 76.01 |

TriMPI 在 ClevrPolicy-T 上取得 77.80% 准确率，较 In-Context 提升 64.65 个百分点，较 CoT SFT 提升 60.00 个百分点。DAPO 在 ClevrPolicy 上优于 GRPO，但在 GTAPolicy 上略低，表明 DAPO 的激进更新在数据丰富时有效，但在低数据场景易过拟合。

消融实验显示，移除 VM-CPT 阶段导致 ClevrPolicy-M 准确率从 85.00% 降至 74.40%，证明视觉掩码对多模态策略注入的关键作用。移除 PolicyRollout 后，GRPO 在 ClevrPolicy-T 上从 65.85% 降至 55.90%，表明策略感知 rollout 显著增强了复杂策略下的探索效率。

评估边界方面，论文仅报告任务准确率，未使用 CHAIR 等幻觉指标，无法判断策略内化是否加剧视觉幻觉。超参数细节完整（如 LoRA rank 8，LR 1e-4），代码开源，但缺乏在标准多模态基准（如 MMMU）上的全面对比，仅报告了 MMMU-Pro 的轻微下降（31.91% 至 30.52%），通用能力保持情况需进一步验证。

## 关联研究分析

从问题动机看，本文与审慎对齐（Guan et al., 2024）共享“内化规则”的目标，但后者聚焦文本安全规范，而本文处理多模态业务策略。关键差异在于视觉 token 的处理：审慎对齐无需考虑视觉输入，而本文通过 VM-CPT 屏蔽视觉 token，解决了多模态输入中策略文本学习信号被视觉特征干扰的问题。这一设计源于多模态数据的模态不对称性，而非算法本身的通用改进。

从方法设计看，本文的 PolicyRollout 与 SCPO（Li et al., 2025）均涉及课程式学习，但 SCPO 通过语义难度分级构建偏好对，而 PolicyRollout 通过策略上下文扩展 rollout 空间。SCPO 依赖高质量偏好数据，而 PolicyRollout 利用策略本身作为引导，无需额外标注。这种差异源于任务特性：策略内化需要遵循特定规则，而幻觉抑制需要区分事实与虚构，前者更适合利用规则结构，后者更适合利用对比信号。

## 总结

本文核心矛盾在于多模态策略的长上下文开销与模型遵循能力不足。现有方法无法处理多跳推理策略，本文通过 VM-CPT 注入策略知识，PolicyRollout 增强探索，在 ClevrPolicy-T 上实现 77.80% 准确率，较 In-Context 提升 64.65 个百分点。边界在于缺乏幻觉指标评估，且仅在自建基准上验证，通用能力保持情况仅通过 MMMU-Pro 轻微下降间接反映。当策略复杂度进一步增加或涉及更多模态时，VM-CPT 的视觉掩码策略是否仍能有效隔离策略文本学习信号，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09474)