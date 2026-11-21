# HuggingFace最新推荐论文 ｜Privileged Information Distillation for Language Models ｜特权信息蒸馏

研究机构：加拿大蒙特利尔大学、加拿大麦吉尔大学

作者：Emiliano Penaloza、Dheeraj Vattikonda、Nicolas Gontier 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.04942)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04942)

> 大语言模型在长程智能体任务中面临训练时拥有辅助信息而推理时缺失的分布失配问题，传统监督微调无法有效迁移这种能力。现有在线策略蒸馏方法依赖独立教师模型或完整思维链，难以应对前沿模型隐藏推理过程的现实约束。本文提出共享参数的联合优化框架，通过同时训练含特权信息的教师策略与无特权信息的学生策略，实现能力向无信息策略的迁移。该方法在多个智能体基准上超越了依赖完整思维链的行业标准，但其效果高度依赖模型容量与特权信息的密度，小模型场景下的泛化能力仍存疑。

## 研究背景

智能体交互可形式化为马尔可夫决策过程（MDP），其中策略 $\pi_\theta(\cdot|\mathbf{s})$ 基于不断演进的交互上下文 $\mathbf{s}$ 生成动作。在强化学习（RL）训练中，若模型能利用训练时特有的特权信息（Privileged Information, PI）成功完成原本会失败的任务，这些成功轨迹便成为宝贵的学习信号。然而，推理时模型无法访问 PI，导致训练分布与推理分布产生系统性偏移，即曝光偏差（Exposure Bias）的一种特殊形式。这种偏移使得直接利用 PI 生成的轨迹进行监督微调（SFT）往往导致策略崩溃或性能退化，因为学生模型未能学会“如何”利用 PI，也未学会在“无” PI 条件下复现教师行为。

主流蒸馏路线分为离线策略（Off-policy）与在线策略（On-policy）两类。离线策略如 SeqKD 依赖教师生成的完美序列，忽视了推理时的误差累积；在线策略如 MiniLLM 虽通过反向 KL 散度（Reverse KL, RKL）缓解偏差，但通常假设教师与学生为独立模型，且需要教师提供完整的 Logits 或思维链（Chain-of-Thought, CoT）。然而，工业界前沿模型（如 OpenAI 系列）通常隐藏内部推理过程，仅暴露动作轨迹，这使得标准白盒蒸馏失效。本文切入点在于：当教师仅提供动作级 PI 且 CoT 不可见时，如何通过共享参数机制，让模型同时学会“利用 PI 生成成功轨迹”与“在无 PI 条件下复现该行为”，从而打破对完整 CoT 的依赖。

## 核心方法

### 方法参照系

本文问题归属于在线策略蒸馏（On-Policy Distillation, OPD）范畴，但存在关键差异：标准 OPD 使用独立教师模型提供 Logits 监督，而本文教师与学生共享参数，且教师条件于 PI、学生无条件。这一差异源于前沿模型 CoT 不可见的约束，迫使方法从“跨模型分布拟合”转向“同模型条件分布迁移”。

### 联合优化目标

传统两阶段蒸馏（先训练 PI 教师，再蒸馏给学生）存在检查点选择困难与离线策略不稳定性。本文提出 $\pi$-Distill，通过单一共享参数模型 $\theta$ 同时优化教师策略 $\pi_\theta^T(\mathbf{o}|\mathbf{s}, \mathbf{I})$ 与学生策略 $\pi_\theta^S(\mathbf{o}|\mathbf{s})$。其核心在于引入联合目标函数，平衡教师利用 PI 获取高奖励的能力与学生模仿教师行为的能力：

$$
\mathcal{L}(\theta) = \alpha \mathbb{E}_{\mathbf{o} \sim \pi_\theta^T} \left[ R(\mathbf{o}, \mathbf{s}) - \beta D_{KL}(\pi_\theta^T(\cdot|\mathbf{s}, \mathbf{I}) \| \pi_\theta^S(\cdot|\mathbf{s})) \right] + (1-\alpha) \mathbb{E}_{\mathbf{o} \sim \pi_\theta^T} \left[ \log \pi_\theta^S(\mathbf{o}|\mathbf{s}) \right]
$$

其中 $\alpha \in [0, 1]$ 控制教师与学生的优化权重，$\beta$ 调节教师向学生的分布约束强度。该设计动机在于：共享参数使得教师学习到的 PI 利用能力可直接迁移至学生，而反向 KL 惩罚项确保教师生成的轨迹不偏离学生可复现的分布范围，从而在训练过程中动态缓解分布偏移，避免学生陷入教师特有的高熵区域。

### 在线自蒸馏变体

$\pi$-Distill 本质上是离线策略学习（学生从教师轨迹学习）。为进一步提升鲁棒性，本文提出在线策略自蒸馏（On-Policy Self-Distillation, OPSD），让学生策略 $\pi_\theta^S$ 作为采样策略，直接最小化其与 PI 条件教师策略的 RKL 散度：

$$
\mathcal{L}_{OPSD}(\theta) = \mathbb{E}_{\mathbf{o} \sim \pi_\theta^S} \left[ D_{KL}(\pi_\theta^S(\cdot|\mathbf{s}) \| \pi_\theta^T(\cdot|\mathbf{s}, \mathbf{I})) \right]
$$

此公式的物理含义是：学生在自生成轨迹上，逐 Token 接受来自“拥有 PI 的自己”的密集反馈。相较于 $\pi$-Distill，OPSD 消除了对教师轨迹质量的依赖，直接优化策略分布的一致性。其改进价值在于，当 PI 信息密度较高或教师轨迹存在噪声时，OPSD 通过自采样机制避免了离线数据中的偏差累积，但代价是更高的计算开销，且在小模型上可能因过拟合教师监督而导致泛化能力下降。

## 实验评估

实验在 Travel Planner、$\tau$-Bench（零售/航空）及 GEM 工具使用套件上进行，基线包括 SFT（含/无 CoT）、标准 RL 及 SFT+RL。本文方法 $\pi$-Distill 与 OPSD 均无需访问前沿模型 CoT，仅使用动作级 PI。

| 模型 | 基准 | $\pi$-Distill ($\alpha=0$) | $\pi$-Distill ($\alpha=1$) | OPSD | SFT w/ CoT + RL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen3-8B | Travel Planner | 40.7% $\pm$ 1.14 | **44.1%** $\pm$ 2.16 | 37.5% $\pm$ 1.53 | 32.3% $\pm$ 1.10 |
| Qwen3-8B | $\tau$-Bench Retail | **31.1%** $\pm$ 0.73 | 29.7% $\pm$ 0.33 | 27.3% $\pm$ 0.33 | 29.1% $\pm$ 2.14 |
| Qwen3-4B | Travel Planner | 28.5% $\pm$ 4.35 | 28.2% $\pm$ 6.27 | 29.8% $\pm$ 1.14 | 26.4% $\pm$ 1.16 |
| Qwen3-4B | $\tau$-Bench Retail | **25.3%** $\pm$ 0.60 | 22.5% $\pm$ 0.93 | 23.1% $\pm$ 0.04 | 23.3% $\pm$ 3.02 |

在 Qwen3-8B 上，$\pi$-Distill 在 Travel Planner 上以 44.1% 显著超越 SFT+RL 的 32.3%，且在 $\tau$-Bench Retail 上以 31.1% 领先。然而，在 Qwen3-4B 上，$\pi$-Distill 在 $\tau$-Bench Retail 上（25.3%）虽优于 SFT+RL（23.3%），但 OPSD 表现不稳定，且在 GEM 域外测试中，小模型的 OPSD 性能显著退化，表明模型容量是 PI 有效迁移的关键门槛。

消融实验显示，$\alpha$ 值无全局最优解：在 Travel Planner 上 $\alpha=1$（侧重教师优化）表现最佳，而在 $\tau$-Bench Retail 上 $\alpha=0$（侧重学生模仿）更优。这暗示 PI 的效用与分布偏移程度呈非线性关系，需根据任务特性动态调整。此外，R1-Distill-Llama-8B 在 SFT+RL 下性能低于基线，而 $\pi$-Distill 虽未提升但避免了退化，证明该方法在模型已见过 PI 的情况下仍具稳定性。

评估边界方面，实验仅使用 2 块 H100 GPU，上下文限制 25k tokens，且 Travel Planner 的奖励函数经过人工解耦以抑制策略崩溃，这可能高估了方法在原始基准上的鲁棒性。代码未公开，超参数搜索范围未在正文详述，限制了可复现性。

## 关联研究分析

从问题动机看，本文与 MiniLLM 同属在线策略蒸馏，但 MiniLLM 聚焦于长尾分布下的 RKL 优化，假设教师提供完整 Logits；本文则针对 CoT 不可见的黑盒场景，将 PI 视为隐变量，通过共享参数实现条件分布迁移。这一差异源于任务特性：MiniLLM 处理通用文本生成，而本文处理长程智能体任务，后者对推理过程的依赖性更强，使得“动作级 PI”成为唯一可用的监督信号。

从方法设计看，本文的 $\pi$-Distill 与 GKD 的散度插值思想相似，但 GKD 在独立模型间调整散度权重，而本文在共享参数模型内平衡教师与学生的优化目标。这种设计避免了跨模型对齐的复杂度，但引入了教师与学生相互干扰的风险。例如，当 $\alpha$ 接近 1 时，教师优化可能主导梯度，导致学生策略未能充分学习无 PI 条件下的行为，这在 Qwen3-4B 的 $\tau$-Bench 结果中有所体现。

## 总结

本文核心矛盾在于训练时 PI 可用与推理时 PI 缺失之间的分布失配，现有方法因依赖完整 CoT 或独立教师模型而无法解决。本文通过共享参数联合优化，让模型同时学习“利用 PI”与“无 PI 行动”，在 Qwen3-8B 上以 44.1% 的 Travel Planner 成绩超越了依赖完整 CoT 的 SFT+RL 基线。然而，实验暴露了模型容量的边界：Qwen3-4B 在域外任务上性能退化，且 $\alpha$ 参数需任务特定调整，缺乏通用准则。当 PI 信息密度极低或模型容量不足时，联合优化是否仍能维持教师-学生分布的一致性，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04942)