# CVPR2026最新论文 ｜MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models ｜基于强化学习的多模态专家路由优化

研究机构：韩国高丽大学、韩国科学技术院

作者：Dohwan Ko、Jinyoung Park、Seoung Choi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24984)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24984)

> 混合专家（Mixture-of-Experts, MoE）架构旨在通过稀疏激活降低大模型计算成本，但确定性 Top-K 路由限制了专家组合的探索空间，导致模型过拟合于少数专家。现有随机扰动方法仅引入噪声，未显式优化选择策略。本文提出 MoE-GRPO，将专家选择建模为序贯决策问题，利用组相对策略优化（Group Relative Policy Optimization, GRPO）通过奖励反馈学习路由策略，并引入模态感知引导约束搜索空间。该方法在视觉语言模型（Vision-Language Models, VLMs）上验证了有效性，但其训练-推理路由不一致性及小模型规模下的泛化边界尚存疑。

## 研究背景

MoE 层通过门控网络计算每个 Token 的专家分配概率，标准做法是选取得分最高的 $K$ 个专家进行加权求和。这一确定性机制虽计算高效，却阻断了模型对次优但潜在更优专家组合的探索。为缓解此问题，研究者引入随机性，如 V-MoE 在门控分数中添加高斯噪声，但这种启发式扰动缺乏对“选择策略”本身的优化目标，无法保证探索方向与任务奖励对齐。

MoE 路由机制的核心矛盾在于平衡稀疏激活的计算效率与专家功能分化的有效性。主流路线分为离散路由与可微路由：前者如 Switch Transformer 依赖辅助负载均衡损失防止坍缩，但梯度流中断限制了路由器直接优化；后者如 DirMoE 采用 Dirichlet 分布实现端到端梯度流动，但增加了计算开销且缺乏对多模态特性的适配。在视觉语言模型中，视觉与文本 Token 的专家激活模式存在显著差异，单一模态的路由策略难以兼顾两者。本文切入点在于将专家选择视为强化学习（Reinforcement Learning, RL）中的动作序列，通过可验证奖励直接优化路由策略，而非依赖辅助损失或启发式噪声，从而在多模态场景下实现更精细的专家利用。

## 核心方法

### 方法参照系

标准 MoE 路由流程为：门控网络计算分数 $\to$ 确定性 Top-K 选择 $\to$ 专家加权输出。本文问题与该通用流程的关键差异在于：将“确定性选择”替换为“策略采样”，并将优化目标从“最小化任务损失”扩展为“最大化组内相对奖励”，从而将路由决策纳入强化学习框架。

### 双目标策略优化

传统 GRPO 仅优化输出 Token 序列，而 MoE-GRPO 将动作空间扩展至层间专家选择，引入 Gate-GRPO 子目标以直接优化门控网络。设计动机在于：仅优化 Token 生成（Token-GRPO）无法提供层间路由的密集监督信号，导致专家选择与任务奖励解耦。MoE-GRPO 的总目标函数为：

$$
\mathcal{L}_{\text{MoE-GRPO}} = \mathcal{L}_{\text{Token-GRPO}} + \mathcal{L}_{\text{Gate-GRPO}}
$$

其中 $\mathcal{L}_{\text{Gate-GRPO}}$ 定义为：

$$
\mathcal{L}_{\text{Gate-GRPO}} = -\mathbb{E}_{\mathbf{x}, \mathbf{E} \sim g_{\text{old}}} \left[ \frac{1}{G} \sum_{i=1}^{G} \sum_{t=1}^{T} \sum_{l=1}^{L} \left( \min \left( \frac{\pi_{\text{new}}(\mathbf{E}_{t,l}^{[i]} | \mathbf{h}_{t,l})}{\pi_{\text{old}}(\mathbf{E}_{t,l}^{[i]} | \mathbf{h}_{t,l})} \hat{A}_i, \text{clip} \left( \frac{\pi_{\text{new}}(\mathbf{E}_{t,l}^{[i]} | \mathbf{h}_{t,l})}{\pi_{\text{old}}(\mathbf{E}_{t,l}^{[i]} | \mathbf{h}_{t,l})}, 1-\epsilon, 1+\epsilon \right) \hat{A}_i \right) \right) \right]
$$

该公式通过裁剪机制稳定策略更新，$\hat{A}_i$ 为第 $i$ 个 Rollout 的归一化优势值，确保门控网络向高奖励专家分配更高概率。

### 模态感知路由引导

RL 探索在大规模专家空间中效率低下，易陷入无效搜索。设计动机在于：视觉与文本 Token 的专家激活分布存在模态特异性，盲目探索会稀释有效信号。本文引入模态感知引导，计算每个专家的视觉/文本激活频率，禁用每个模态下激活频率最低的 25% 专家（设门控分数为 $-\infty$）。这一机制将搜索空间约束在模态相关专家子集内，在保持随机探索多样性的同时，避免路由器探索与当前模态无关的专家，从而加速策略收敛并提升训练稳定性。

## 实验评估

实验在 InternVL3.5-1B（激活 1.3B/总 2.9B 参数）和 CLIP-MoE（激活 0.7B/总 1.2B 参数）上进行，覆盖 MMBench、MLVU 等 9 个多模态基准。基线包括确定性微调（Det-FT）、随机多项式采样（Stoch-FT-Multi）和高斯噪声扰动（Stoch-FT-Noise），但缺失 DirMoE、Grassmannian MoE 等可微/几何路由方法，也未对比 Expert Choice 等负载均衡路由变体。

| 方法 | MMBench | MMStar | MLVU | LongVideoBench | Avg. |
|---|---|---|---|---|---|
| InternVL3.5 + Det-FT | 75.8 | 45.6 | 51.8 | 62.7 | 54.0 |
| InternVL3.5 + Stoch-FT-Multi | 73.9 | 43.3 | 51.2 | 61.8 | 53.7 |
| InternVL3.5 + Stoch-FT-Noise | 76.3 | 46.1 | 52.0 | 62.4 | 54.3 |
| InternVL3.5 + MoE-GRPO | 77.5 | 45.7 | 54.8 | 65.8 | 56.0 |

MoE-GRPO 在平均准确率上比 Det-FT 高 2.0%，比 Stoch-FT-Noise 高 1.7%，表明 RL 策略优化优于启发式随机扰动。消融实验显示，Gate-GRPO 单独使用导致平均准确率从 55.7% 降至 50.9%，证明 Token 级优化是奖励对齐的核心；模态感知引导比模态无关的多项式采样高 0.9%，验证了模态特异性约束的有效性。

评估边界方面，实验仅在 1.3B 激活规模的小模型上进行，缺乏与大规模 LLM MoE 的横向对比；训练-推理路由不一致（训练随机采样，推理 Top-K）未通过重放机制对齐，可能影响策略泛化；代码未公开，超参数（如 Rollout 数 $G=8$）的敏感性未充分探讨。

## 关联研究分析

从问题动机看，MoE-GRPO 与 V-MoE 同属随机路由路线，但 V-MoE 仅通过高斯噪声引入探索，未优化选择策略，而 MoE-GRPO 将专家选择建模为序贯决策，通过奖励反馈显式优化策略。这一差异源于任务特性：VLM 中视觉/文本模态的专家激活模式差异显著，启发式噪声无法适应模态特异性，而 RL 策略可学习模态相关的专家偏好。然而，MoE-GRPO 未解决训练-推理路由漂移问题，而 RL-LLM 领域已通过路由重放机制对齐训练与推理行为，这在多模态场景中是否必要，论文未给出回答。

从方法设计看，MoE-GRPO 与 DirMoE 同属可微/策略优化路线，但 DirMoE 采用 Dirichlet 分布实现端到端梯度流动，依赖超参数 $\lambda$ 控制稀疏度，而 MoE-GRPO 通过 RL 奖励信号间接优化路由，无需显式稀疏控制超参数。这一差异源于优化目标：DirMoE 追求路由的几何/概率最优性，而 MoE-GRPO 追求任务奖励最大化。MoE-GRPO 的模态感知引导机制是 DirMoE 未涉及的维度，其有效性依赖于模态间专家激活分布的差异性，若模态间专家共享度高，该机制可能失效。

## 总结

MoE-GRPO 旨在解决确定性 Top-K 路由导致的专家探索不足与过拟合问题，通过 RL 策略优化实现显式专家选择。其切入点在于将路由决策纳入强化学习框架，利用组相对奖励直接优化策略，而非依赖辅助损失或启发式噪声。实验表明，MoE-GRPO 在多模态基准上比 Det-FT 平均高 2.0%，并诱导了任务级专家专业化。然而，其边界在于：仅在 1.3B 激活规模的小模型上验证，训练-推理路由不一致未解决，且缺乏与可微路由方法的对比。当模型规模扩大至万亿参数级时，RL 探索的计算开销与路由漂移问题是否会被放大，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24984)