# ACL-Findings2026最新论文 ｜Intrinsic Mutual Information as a Modulator for Preference Optimization ｜基于内在互信息的自适应偏好优化

研究机构：中山大学、英国华威大学

作者：Peng Liao、Peijia Zheng、Lingbo Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24804)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24804)

> 离线偏好优化旨在将人类价值观内化至大语言模型，但主流方法如直接偏好优化（Direct Preference Optimization, DPO）对超参数极度敏感，导致训练成本高昂且性能不稳定。现有自适应机制或依赖额外的监控模块，或需保留参考模型，未能彻底消除调优开销。本文提出 RMiPO，利用响应级点互信息（Pointwise Mutual Information, PMI）差异动态调节奖励边际，实现无参考模型的实例级自适应优化。该方法在降低 15-20% 训练成本的同时提升了指令遵循性能，但其对长文本及复杂推理任务中的 PMI 信号有效性尚未验证。

## 研究背景

离线偏好优化的核心困境在于超参数 $\beta$ 与 $\gamma$ 的耦合效应。$\beta$ 控制策略与参考策略间的 KL 散度约束强度，而 $\gamma$ 决定偏好对之间的奖励边际阈值。在 DPO 中，$\gamma$ 隐含于参考模型 $\pi_{ref}$ 的对数似然比中，导致其最优值随数据分布动态变化；在简单偏好优化（Simple Preference Optimization, SimPO）中，$\gamma$ 显式存在但需手动设定。这种静态设定无法适应训练过程中模型判别能力的演变，导致早期训练信号冗余或后期训练梯度消失。

主流解决方案分为两类：一类通过引入额外控制变量（如 $\alpha$-DPO、$\epsilon$-DPO）动态调整损失函数，但增加了计算开销且仍依赖部分超参数；另一类通过改变优化范式（如 SimPER）消除超参数依赖，但在偏好漂移或数据不一致场景下性能退化。这两种路线均未解决“如何在无额外计算成本下，利用模型内在信号实现超参数的实例级自适应”这一核心问题。本文切入点在于发现响应级 PMI 差异能解耦语义相关性与先验流行度，为 $\gamma$ 的自适应调节提供了轻量级且原则性的信号源。

## 核心方法

### 方法参照系

本文基于 SimPO 的无参考模型框架，但摒弃其固定 $\gamma$ 的设计。SimPO 通过长度归一化奖励 $\tilde{r}(x, y) = \frac{\beta}{|y|} \log \pi_\theta(y|x)$ 消除长度偏差，并引入固定边际 $\gamma$ 以增强偏好信号。本文的关键差异在于将 $\gamma$ 从静态超参数转化为由模型内在信息驱动的动态变量，从而在不增加存储与推理开销的前提下实现自适应。

### 基于 PMI 的动态边际机制

设计动机在于解决传统对数似然差异 $\Delta \log$ 中语义相关性与响应先验流行度的纠缠问题。当获胜响应 $y_w$ 为通用流畅但信息量低的“样板”文本时，$\log \pi_\theta(y_w)$ 较大，导致模型错误地偏好此类响应。PMI 通过贝叶斯分解 $\text{PMI}(y|x) = \log \pi_\theta(y|x) - \log \pi_\theta(y)$ 剔除了先验项 $\log \pi_\theta(y)$，仅保留条件相关性。

RMiPO 定义动态边际 $\gamma$ 为 PMI 差异的整流指数衰减函数：

$$ \gamma(x, y_w, y_l) = \gamma_{\min} + (\gamma_{\max} - \gamma_{\min}) \cdot \exp(-\max(0, \Delta_{\text{pmi}})) $$

其中 $\Delta_{\text{pmi}} = \text{PMI}(y_w|x) - \text{PMI}(y_l|x)$。该公式的物理含义是：当语义区分度高（$\Delta_{\text{pmi}} > 0$）时，$\gamma$ 指数衰减至 $\gamma_{\min}$，促进模型快速饱和并减少冗余计算；当语义模糊或反转（$\Delta_{\text{pmi}} \le 0$）时，$\gamma$ 固定为 $\gamma_{\max}$，施加强约束以持续惩罚错误偏好。这种非线性映射实现了从粗粒度判别到细粒度对齐的平滑过渡。

### 无参考模型的自适应损失函数

设计动机在于消除 DPO 对参考模型 $\pi_{ref}$ 的依赖，从而降低显存占用并避免参考模型带来的计算延迟。RMiPO 将动态边际 $\gamma$ 嵌入 SimPO 的损失函数中，形成最终优化目标：

$$ \mathcal{L}_{\text{RMiPO}} = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \Delta R - \gamma(x, y_w, y_l) \right) \right] $$

其中 $\Delta R = \frac{\beta}{|y_w|} \log \pi_\theta(y_w|x) - \frac{\beta}{|y_l|} \log \pi_\theta(y_l|x)$ 为长度归一化的奖励差异。该损失函数通过 $\gamma$ 的自适应调节，动态门控每个样本的梯度贡献：高置信度样本的梯度被抑制，低置信度样本的梯度被增强，从而在无需手动调参的情况下实现训练效率与对齐性能的平衡。

## 实验评估

实验在 Llama3-8B 与 Mistral-7B 的 Base 及 Instruct 设置下进行，使用 UltraFeedback 数据集训练，并在 AlpacaEval 2、MT-Bench 及 Open LLM Leaderboard v2 上评估。基线覆盖 DPO、SimPO、IPO、KTO 及自适应变体（$\alpha$-DPO、$\epsilon$-DPO、SimPER），但未对比知识库中提到的 RE-PO、OrthAlign 等最新鲁棒或多目标方法。

| 模型设置 | 方法 | AlpacaEval 2 LC (%) | MT-Bench |
| :--- | :--- | :--- | :--- |
| Llama3-8B-Instruct | DPO | 33.1 | 7.8 |
| Llama3-8B-Instruct | SimPO | 44.7 | 7.7 |
| Llama3-8B-Instruct | SimPER | 48.5 | 7.7 |
| Llama3-8B-Instruct | RMiPO | 49.1 | 8.3 |
| Mistral-7B-Instruct | DPO | 21.5 | 7.3 |
| Mistral-7B-Instruct | SimPO | 32.1 | 7.3 |
| Mistral-7B-Instruct | SimPER | 37.8 | 7.5 |
| Mistral-7B-Instruct | RMiPO | 38.1 | 7.5 |

RMiPO 在 Llama3-8B-Instruct 上以 49.1% 的 LC 胜率领先，较 SimPER 提升 0.6 个百分点，MT-Bench 得分 8.3 亦为最高。在 Mistral-7B-Instruct 上，RMiPO 的 LC 胜率 38.1% 较 DPO 提升 16.6 个百分点，但 MT-Bench 得分与 SimPER 持平。

| 消融组件 | IFEval | BBH | MATH | GPQA | MUSR | MMLU-PRO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 无 GM | 66.14 | 27.32 | 8.52 | 3.01 | 4.25 | 28.04 |
| 无 MI | 65.87 | 26.94 | 8.48 | 3.12 | 5.12 | 28.32 |
| 无 ED | 68.21 | 28.47 | 8.74 | 3.28 | 7.31 | 29.56 |
| 完整 RMiPO | 69.07 | 29.01 | 8.96 | 3.50 | 8.41 | 30.46 |

消融实验显示，移除指数衰减（ED）导致 MUSR 得分从 8.41 降至 7.31，降幅最大，表明非线性映射对复杂推理任务至关重要。移除 PMI（MI）导致 BBH 得分从 29.01 降至 26.94，证实互信息信号对逻辑推理的增益。

评估边界方面，MT-Bench 因评估集有限且单实例评分，区分度较低，可能低估方法差异。代码已开源，使用 alignment-handbook 实现，实验在 4 块 NVIDIA A800 上进行，但论文未报告不同 GPU 规模下的收敛性差异。

## 关联研究分析

从问题动机看，RMiPO 与 SimPER 均旨在消除超参数依赖，但 SimPER 通过改变优化范式彻底移除超参数，而 RMiPO 保留 $\gamma$ 并实现其自适应。SimPER 在偏好漂移场景下性能退化，源于其静态优化结构无法适应数据分布变化；RMiPO 的 PMI 信号随模型参数更新动态变化，理论上能更好地应对分布偏移，但论文未提供偏好漂移下的对比实验，其鲁棒性优势尚需验证。

从方法设计看，RMiPO 与 $\epsilon$-DPO 均引入动态机制，但 $\epsilon$-DPO 依赖额外的控制变量监控训练状态，增加了计算开销；RMiPO 利用模型内在的 PMI 信号，无需额外模块。然而，$\epsilon$-DPO 的监控机制可能捕捉到 PMI 未覆盖的训练动态（如梯度范数变化），RMiPO 仅依赖语义相关性信号，可能在非语义因素主导的训练阶段（如早期语法学习）表现不佳，论文未对此进行细分分析。

## 总结

RMiPO 解决了离线偏好优化中超参数静态设定与模型动态判别能力不匹配的核心矛盾。其切入点在于发现响应级 PMI 差异能解耦语义相关性与先验流行度，为 $\gamma$ 的自适应调节提供了轻量级信号源。通过整流指数衰减机制，RMiPO 实现了无参考模型的实例级自适应优化，在 Llama3-8B-Instruct 上以 49.1% 的 LC 胜率领先，训练成本降低 15-20%。然而，论文实验主要集中于指令遵循基准，未验证 PMI 信号在长文本生成或复杂代码任务中的有效性，且缺乏与最新鲁棒对齐方法（如 RE-PO）的直接对比。当响应长度显著增加时，PMI 中的先验项 $\log \pi_\theta(y)$ 是否仍能准确反映流行度偏差，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24804)