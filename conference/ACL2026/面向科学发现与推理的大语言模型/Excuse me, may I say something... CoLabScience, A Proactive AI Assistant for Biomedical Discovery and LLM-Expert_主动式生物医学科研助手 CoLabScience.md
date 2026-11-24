# ACL2026最新论文 ｜Excuse me, may I say something... CoLabScience, A Proactive AI Assistant for Biomedical Discovery and LLM-Expert Collaborations ｜主动式生物医学科研助手 CoLabScience

研究机构：美国伍斯特理工学院、美国加州大学戴维斯分校

作者：Yang Wu、Jinhong Yu、Jingwei Xiong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15588)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15588)

> 现有大语言模型在科学协作中仅被动响应指令，导致关键洞察在讨论流中流失。本文切入点在于将“何时介入”与“如何介入”解耦，通过正未标注学习（Positive-Unlabeled Learning, PU Learning）与强化学习协调器实现流式对话中的主动干预。实验在自建基准上验证了其在干预时机与内容质量上的优势，但缺乏真实实验室场景的泛化验证。

## 研究背景

在生物医学团队讨论中，成员发言是异步且流式的，模型若仅在被显式提问时响应，会错过纠正错误方向或补充关键证据的最佳窗口。这种被动模式要求模型具备实时语境追踪能力，即通过短期记忆捕获当前对话状态，通过长期记忆压缩历史洞察，从而在无需提示的情况下识别介入时机。

当前自主科研智能体路线多聚焦于端到端任务执行，如假设生成或代码编写，但忽略了协作交互中的时机决策。现有主动式方法依赖手工设计的提示词或固定逻辑触发，缺乏对复杂语境下介入价值的自适应学习。CoLabScience 针对这一空白，提出将介入决策建模为强化学习问题，利用稀疏标注数据训练模型自主判断介入价值。

## 核心方法

### 方法参照系

本文问题属于自主科研智能体在流式对话中的特化。标准流程中，智能体接收完整任务指令后执行闭环，而本文场景要求模型在对话流中实时决策“静默”或“介入”，核心差异在于决策的时序性与稀疏性：绝大多数轮次无需介入，仅少数高价值节点需要干预。

### 双尺度记忆与状态编码

为解决长对话中上下文丢失问题，PULI 框架构建双尺度记忆 $M_t(d_n)$，包含项目提案 $C(d_n)$、短期记忆 $M_S^t(d_n)$（当前及前两轮发言）和长期记忆 $M_L^t(d_n)$（历史洞察摘要）。状态嵌入 $S_n$ 通过拼接 Observer 和 Presenter 的最后一层隐藏表示生成，并引入可学习线性投影器 $\Omega(\cdot)$ 对齐维度：

$$S_n = \text{Concat}(\Psi_{H_\phi}(M_t(d_n)), \Omega(\Psi_{G_\psi}(M_t(d_n))))$$

该设计使协调器能同时感知“是否该说”（Observer 的时序判断）与“说什么”（Presenter 的内容潜力），解决了单一模型难以兼顾时机与内容质量的问题。

### 正未标注学习与协调器优化

针对介入标签稀疏且未标注轮次混杂正负样本的问题，PULI 采用 PU 学习策略：仅标注最高价值介入点为正样本，其余为未标注。协调器 $F_\theta$ 通过 REINFORCE 算法优化策略，奖励函数 $r_{\text{total}}$ 加权结合 Observer 验证准确率提升 $r_{\text{when}}$ 与 Presenter ROUGE-1 提升 $r_{\text{how}}$：

$$r_{\text{total}} = \lambda r_{\text{when}} + (1-\lambda) r_{\text{how}}$$

其中 $\lambda=0.6$。协调器从 PU 数据中识别可靠负样本（静默轮次）用于 Observer 训练，识别潜在正样本用于 Presenter 增强，形成端到端闭环。这一机制避免了传统监督学习中负样本缺失导致的偏差，使模型能在稀疏标签下学习精准的介入边界。

## 实验评估

实验基于自建 BSDD 数据集，包含基于 PubMed 文献生成的多角色模拟对话。基线覆盖 Standard、Random、Proactive Agent、ICL 及 Vanilla SFT，但缺失 ChemCrow 等工具增强型智能体对比，限制了跨范式比较。

| LLM Backbone (Observer + Presenter) | Method | Accuracy (%) | ROUGE-1 (%) | WR-Intra (%) |
| :--- | :--- | :--- | :--- | :--- |
| LLaMA3.2-1B + LLaMA3.1-8B | PULI (Ours) | 67.4 | 33.5 | 39.2 |
| LLaMA3.2-1B + LLaMA3.1-8B | ICL | 59.1 | 32.5 | 21.8 |
| Qwen3-0.6B + Qwen3-14B | PULI (Ours) | 64.1 | 32.4 | 39.8 |
| Qwen3-0.6B + Qwen3-14B | ICL | 58.6 | 29.2 | 20.1 |

PULI 在 LLaMA3 配置下取得 67.4% 干预时机准确率与 33.5% ROUGE-1，显著优于 ICL 基线（59.1% 与 32.5%）。跨骨干比较显示，PULI 在 LLaMA3 上的 Inter-Group Win Rate 达 45.8%，高于 GPT 对最佳方法 ICL 的 18.3%，表明小模型经 RL 训练后可超越大模型提示工程。

消融实验表明，$\lambda=0.6$ 时 Observer 准确率与 Presenter 质量达到最佳平衡；$\lambda$ 过小导致时机判断失效，过大则内容质量下降。DPO 变体在 Observer 上表现次优（64.6% 准确率），验证了 GRPO 在时序决策任务中的适用性。

评估局限在于 BSDD 为模拟数据，缺乏真实实验室语音流（ASR/TTS）下的延迟测试；指标侧重静态文本质量，未量化介入对后续对话轨迹的动态影响。代码已开源，但超参数（如学习率 $1 \times 10^{-6}$）仅针对特定骨干优化，跨模型迁移性未充分验证。

## 关联研究分析

从问题动机看，CoLabScience 与 AI Scientist 等端到端框架形成互补：后者解决“如何执行科研任务”，前者解决“何时介入协作”。差异根源在于任务特性——AI Scientist 假设任务边界清晰，而生物医学讨论是开放流式过程，要求模型具备语境敏感性。CoLabScience 的 PU 学习设计正是针对这种标签稀疏性，而 AI Scientist 类系统通常拥有完整任务标注，无需处理未标注轮次。

从方法设计看，与 Proactive Agent (Lu et al., 2024b) 相比，CoLabScience 用可训练 RL 协调器替代固定逻辑触发。Proactive Agent 依赖手工规则判断介入时机，在复杂语境下易失效；CoLabScience 通过奖励信号自适应学习介入边界，提升了鲁棒性。然而，CoLabScience 的 Presenter 仍采用 SFT 而非 RL，限制了内容生成的探索性，这与 Debate as Reward 等采用多智能体奖励的方法形成对比，后者通过动态奖励提升假设新颖性，但 CoLabScience 侧重时机精准性而非内容创新性。

## 总结

CoLabScience 解决了流式科学对话中主动介入时机与内容联合优化的矛盾，通过 PU 学习与 RL 协调器实现稀疏标签下的精准决策。实验证明其在模拟基准上优于 ICL 等基线，LLaMA3 配置下干预准确率达 67.4%。其边界在于依赖模拟数据，未验证真实实验室场景下的延迟与噪声鲁棒性，且 Presenter 的 SFT 训练限制了内容生成的多样性。当对话轮次增加至数百轮时，长期记忆的递归摘要是否会导致关键洞察丢失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15588)