# ACL-Findings2026最新论文 ｜RIPRAG: Hack a Black-box Retrieval-Augmented Generation Question-Answering System with Reinforcement Learning ｜基于黑盒反馈强化学习的检索增强生成投毒攻击

研究机构：浙江大学

作者：Meng Xi、Sihan Lv、Yechen Jin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10008)

> 检索增强生成（Retrieval-Augmented Generation, RAG）系统因引入外部知识库而面临投毒威胁，但现有黑盒攻击方法依赖静态启发式或失配的代理模型，在低投毒率与复杂检索架构下失效。RIPRAG 将目标系统视为不透明环境，通过强化学习从黑盒交互反馈中动态优化投毒文档生成策略。该方法在复杂检索设置下将攻击成功率（ASR）提升至 0.49-1.00，显著优于基线，但仅验证了文本模态与特定防御机制，未覆盖多模态或动态更新场景。

## 研究背景

RAG 系统通过动态检索外部文档缓解大语言模型（LLM）的知识滞后问题，其核心组件包括数据库、检索器与生成器。攻击者向数据库注入恶意文档以操纵生成结果，这一过程称为 RAG 投毒。由于商业 RAG 系统不公开内部参数，攻击者无法获取检索器梯度，这构成了黑盒攻击场景。在黑盒设定下，攻击者仅能执行两个操作：向数据库注入文档，以及通过 API 与系统交互获取输出。

主流投毒攻击分为白盒与黑盒两类。白盒方法利用检索器梯度优化文档，但假设系统为单一嵌入模型，无法适配混合检索或 GraphRAG 等复杂架构。现有黑盒方法如 PoisonedRAG 采用静态文本插入策略，将目标查询直接嵌入投毒文档以提升检索概率，但该方法无法利用系统交互反馈，且在投毒文档数量远少于检索文档数量时性能急剧下降。RIPRAG 的切入点在于将黑盒系统转化为强化学习环境，通过迭代交互获取稀疏奖励信号，动态调整文档生成策略，从而在缺乏内部梯度信息的情况下实现自适应投毒。

## 核心方法

### 黑盒投毒攻击参照系

传统黑盒投毒攻击遵循“生成-注入-评估”的静态流程：攻击者使用预训练语言模型生成包含目标答案的文档，注入数据库后通过单次查询评估攻击成功率。该流程的关键局限在于生成策略与系统响应解耦，无法根据检索器的实际偏好调整文档内容，导致在复杂检索管道中命中率低。

### 基于黑盒反馈的强化学习范式

RIPRAG 将投毒过程建模为强化学习问题，提出从黑盒反馈中强化学习（Reinforcement Learning from Black-box Feedback, RLBF）范式。在此框架中，目标 RAG 系统 $E_{bb}$ 作为不透明环境，攻击者策略 $\pi_\phi$ 生成投毒文档 $D_j^{[i]}$ 作为动作，系统输出 $y_t$ 作为状态转移反馈。奖励函数 $\hat{r}(y_t)$ 隐式地从系统输出中推导，无需访问内部梯度。策略更新通过最小化损失函数 $L_{BRPO}$ 实现，其核心公式为：

$$ \nabla_\phi J(\phi) = \nabla_\phi \mathbb{E}_{x_t \sim \pi_\phi} [L(\hat{r}(y_t))] $$

该公式表明，策略参数 $\phi$ 的更新完全依赖于黑盒系统输出的反馈信号，将系统的不透明性转化为优化通道。这一设计解决了静态方法无法适应未知检索机制的问题，使攻击策略能够针对特定系统的偏好进行迭代优化。

### 批量相对策略优化与复合奖励

针对对抗文本生成中候选响应同质性导致的组内奖励差异微小、梯度消失问题，RIPRAG 提出批量相对策略优化（Batch Relative Policy Optimization, BRPO）。BRPO 在整个查询批次而非单个组内进行奖励归一化，其损失函数定义为：

$$ L_{BRPO} = \mathbb{E}_{i \in Q} \left[ \frac{1}{|Q|} \sum_{j} \left( \min\left( \frac{R_{i,j} - \bar{R}}{\sigma_R}, \text{clip}\left( \frac{R_{i,j} - \bar{R}}{\sigma_R}, 1-\epsilon, 1+\epsilon \right) \right) \right) \right] $$

其中 $R_{i,j}$ 为文档 $D_j^{[i]}$ 的奖励，$\bar{R}$ 和 $\sigma_R$ 为批次奖励的均值与标准差。BRPO 通过跨查询比较维持非零优势幅度，避免标准 GRPO 在稀疏奖励下的收敛失败。此外，RIPRAG 设计复合奖励 $r = \lambda r_{sim} + (1-\lambda) r_{suc}$，其中相似度奖励 $r_{sim}$ 作为密集过程信号，在攻击成功率 $p_{success} \approx 0$ 时提供稳定梯度，防止策略遗忘投毒目标。

## 实验评估

实验在 Natural Questions (NQ)、HotpotQA 和 MS-MARCO 三个基准上进行，目标 LLM 包括 GLM4-9B、Qwen3-8B 等四种模型，检索设置分为朴素（Contriever）与复杂（混合嵌入+RRF 融合）两类。基线仅包含 PoisonedRAG 的黑盒与伪白盒变体，缺失 TopicFlipRAG 等其他黑盒方法对比，限制了基线覆盖的全面性。

| 数据集 | 检索设置 | 方法 | M=3 ASR | M=1 ASR |
| :--- | :--- | :--- | :--- | :--- |
| NQ | 复杂 | PoisonedRAG (black-box) | 0.35 | 0.29 |
| NQ | 复杂 | RIPRAG (black-box) | 0.72 | 0.94 |
| HotpotQA | 复杂 | PoisonedRAG (black-box) | 0.51 | 0.49 |
| HotpotQA | 复杂 | RIPRAG (black-box) | 0.97 | 1.00 |
| MS-MARCO | 复杂 | PoisonedRAG (black-box) | 0.20 | 0.18 |
| MS-MARCO | 复杂 | RIPRAG (black-box) | 0.73 | 0.87 |

在复杂检索设置下，RIPRAG 的 ASR 显著高于 PoisonedRAG，尤其在 M=1 低投毒率场景中，RIPRAG 在 HotpotQA 上达到 1.00，而基线仅为 0.49。消融实验显示，移除相似度奖励导致 MS-MARCO 上 ASR 从 0.78 降至 0.20，移除 BRPO 导致 NQ 上 ASR 从 0.72 降至 0.50，证实复合奖励与批量归一化对稳定训练的关键作用。

评估边界方面，论文未报告置信区间，所有结果为 5 次运行的平均值。代码未公开，但提供了 QLoRA 训练细节与 API 成本估算（约 $0.7/实例）。防御评估仅测试了查询重写、HyDE 和 RAGuard 三种机制，未覆盖重排序器或知识图谱层面的防御，且 RAGuard 在双倍 QLoRA 秩下 ASR 回升至 0.23-0.28，表明防御效果受攻击模型容量影响。

## 关联研究分析

从问题动机看，RIPRAG 与 PoisonedRAG 均针对黑盒 RAG 投毒，但前者将系统视为可交互环境，后者视为静态目标。PoisonedRAG 依赖文本插入启发式，无法利用系统反馈，导致在复杂检索中性能衰减；RIPRAG 通过 RLBF 范式将黑盒输出转化为奖励信号，解决了静态策略无法适应未知检索机制的问题。这一差异源于任务特性：复杂检索管道（如混合搜索）的决策边界非固定，静态文档难以持续命中，而动态优化策略能够追踪系统偏好变化。

从方法设计看，RIPRAG 借鉴了 RLHF 中的 GRPO 思想，但针对对抗文本生成的稀疏奖励特性改进为 BRPO。与标准 GRPO 的组内归一化不同，BRPO 采用批次级归一化，解决了候选文档同质性导致的梯度消失问题。与 PRA-RAG 等防御方法相比，RIPRAG 属于攻击侧工作，其价值在于揭示现有防御在自适应攻击下的脆弱性。RAGuard 作为防御机制，在 RIPRAG 攻击下 ASR 降至 0.10-0.16，但模型容量增加后攻击成功率回升，表明基于阈值的防御难以应对策略优化后的攻击。

## 总结

RIPRAG 解决的核心矛盾是黑盒环境下缺乏梯度信息时如何高效生成高命中率投毒文档。现有静态方法无法利用系统反馈，导致在复杂检索与低投毒率下失效；RIPRAG 通过 RLBF 范式将黑盒系统转化为强化学习环境，利用 BRPO 与复合奖励实现策略自适应优化。实验证明其在复杂检索设置下 ASR 达 0.49-1.00，显著优于 PoisonedRAG。然而，论文仅验证了文本模态与三种特定防御机制，未覆盖多模态 RAG 或动态更新知识库场景。当知识库内容随时间变化时，基于静态训练的策略能否持续保持高攻击成功率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10008)