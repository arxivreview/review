# ACL-Findings2026最新论文 ｜Direct Token Optimization: A Self-contained Approach to Large Language Model Unlearning ｜直接Token优化

研究机构：美国埃默里大学

作者：Hong kyu Lee、Ruixuan Liu、Li Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2510.00125)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00125)

> 大语言模型（LLM）在微调阶段极易记忆特定数据，导致隐私泄露与版权风险，而完全重训练成本过高。现有无保留集遗忘方法如FLAT仅引导模型生成拒绝回答，未能触及知识存储的核心Token，导致遗忘质量低下。本文提出直接Token优化（DTO），通过Delta-score自主识别关键知识Token并执行梯度上升，同时利用KL散度约束非目标Token以维持效用。该方法在TOFU基准上实现了极高的遗忘质量，但其对长距离依赖知识的覆盖能力及对抗鲁棒性仍存疑。

## 研究背景

当LLM面对微调数据中的特定实体或事实时，其内部参数会形成对该序列的强记忆。这种记忆并非均匀分布，而是集中在少数几个承载核心语义的Token上，即“关键Token”。然而，这些关键Token与维持语言流畅性的通用Token在损失函数中往往纠缠在一起，直接对全序列进行梯度上升会破坏模型的通用语言能力，引发“涟漪效应”。

LLM遗忘的主流路线分为依赖外部资源与无外部资源两类。依赖保留集或辅助模型的方法虽能平衡效用，但受限于GDPR等法规对原始数据复用的限制，实际部署困难。无外部资源的方法如DPO、NPO及FLAT，虽仅需原始模型与遗忘集，但FLAT等最新方法通过f-散度引导拒绝回答，仅改变了输出分布而未擦除内部知识表征，导致在间接查询下知识仍可能泄露。本文的切入点在于：在无外部资源约束下，如何精准定位并仅针对承载核心知识的Token进行参数更新，从而在彻底遗忘与效用保持间取得更优平衡。

## 核心方法

### 方法参照系

本文问题属于无保留集LLM近似遗忘范畴。标准流程通常对全序列Logits执行梯度上升或偏好优化，但本文的关键差异在于将优化粒度从序列级细化至Token级，并引入自主Token选择机制替代人工或外部LLM标注。

### Delta-score Token选择

传统方法依赖ChatGPT或人工标注选择目标Token，存在隐私风险与成本问题。本文提出Delta-score，基于序列记忆扰动研究，通过量化前缀Token对后缀生成损失的影响来识别关键Token。具体而言，将序列分为前缀与后缀，对前缀中每个Token进行扰动，计算后缀平均负对数似然（NLL）的变化量。

$$ \Delta_i = \mathcal{L}_{suffix}(\theta; x_{prefix}^{(i)} \to x_{prefix}^{(i')}) - \mathcal{L}_{suffix}(\theta; x_{prefix}) $$

该公式物理含义为：若扰动前缀Token $i$ 导致后缀生成损失显著增加，说明该Token对后续知识生成具有强因果影响力，即为核心知识载体。选取Top-k高分Token作为目标Token，解决了通用Token与知识Token难以区分的问题。

### 分治优化策略

针对选定的目标Token与非目标Token，DTO采用分治优化策略。对目标Token执行梯度上升以最大化其生成损失，实现知识擦除；对非目标Token最小化更新模型与原始模型Logits间的KL散度，以锚定通用语言能力。

$$ \mathcal{L}_{DTO} = \sum_{t \in \mathcal{T}_{target}} \mathcal{L}_{NLL}(t) + \lambda \sum_{t \in \mathcal{T}_{non-target}} D_{KL}(p_{\theta_{old}}(t) \| p_{\theta_{new}}(t)) $$

此设计动机在于解耦遗忘与保留的梯度冲突：梯度上升仅作用于承载敏感信息的局部参数，而KL正则化防止更新扩散至无关参数，从而避免了全序列优化导致的效用崩溃。

## 实验评估

实验在TOFU（1%, 5%, 10%）与MUSE-Book基准上进行，对比基线包括DPO、NPO、LLMU及FLAT（TV/KL/JS/P变体）。基线覆盖了偏好优化与散度引导路线，但缺失SAUL、OFMU等2025-2026年最新SOTA方法，且未包含TPO的定量对比（仅定性分析）。

| 模型 | 方法 | Forget Quality (↑) | Model Utility (↑) | Forget Rouge-L (↓) |
| :--- | :--- | :--- | :--- | :--- |
| Llama 2-7B | FLAT (TV) | 0.0021 | 0.1253 | 0.0534 |
| Llama 2-7B | FLAT (JS) | 0.0001 | 0.3091 | 0.1716 |
| Llama 2-7B | DTO w/o KL | 0.0021 | 0.2871 | 0.1743 |
| Llama 2-7B | DTO | 0.0876 | 0.4442 | 0.5415 |
| Llama 3.2-1B | FLAT (TV) | 0.0124 | 0.2071 | 0.0988 |
| Llama 3.2-1B | FLAT (JS) | 0.0001 | 0.4514 | 0.2118 |
| Llama 3.2-1B | DTO w/o KL | 0.0001 | 0.3187 | 0.2597 |
| Llama 3.2-1B | DTO | 0.3281 | 0.4218 | 0.3168 |

在TOFU 1%数据集上，DTO在Llama 2-7B上的Forget Quality为0.0876，显著高于FLAT最佳变体（0.0021），但低于论文摘要中声称的0.9188（该数值对应DTO w/o KL在特定配置下的表现，表格中DTO w/o KL FQ为0.0021，存在数据呈现不一致，需以表格逐字数值为准）。DTO w/o KL在Llama 3.2-1B上的Forget Rouge-L为0.2597，优于FLAT (TV)的0.0988，表明其更有效地抑制了逐字记忆。

消融实验显示，后缀比例（Suffix Ratio）对Delta-score效果影响显著。当后缀比例过小（0.15）时，信号不足导致遗忘质量低；过大时引入噪声降低效用。目标Token比例k=0.3时，效用下降迅速且第6个epoch后遗忘质量因过遗忘而下降，表明存在最优平衡点。

评估边界方面，本文仅使用静态指标（FQ, MU, Rouge-L），未包含重学习攻击或多跳推理鲁棒性测试，无法验证遗忘的深层持久性。代码未公开，超参数（k, suffix ratio）需手动搜索，可复现性受限。

## 关联研究分析

从问题动机看，DTO与FLAT同属无保留集路线，但FLAT通过f-散度引导模型生成拒绝模板，本质上是一种输出抑制策略，未改变内部知识表征；DTO则通过Token级梯度上升直接修改参数，属于机制级擦除。这一差异源于对“遗忘”定义的侧重不同：FLAT关注合规性（不回答），DTO关注安全性（不记忆）。然而，DTO的Delta-score依赖局部扰动，对于知识分散在长距离依赖中的复杂事实，其选择准确性可能下降，论文未对此进行量化分析。

从方法设计看，DTO与TPO（Token Preference Optimization）均聚焦Token级遗忘，但TPO依赖ChatGPT选择目标词，存在隐私泄露风险；DTO的Delta-score完全自主，消除了外部依赖。然而，DTO的梯度上升策略在MUSE基准上的KnowMem（22.84）高于FLAT (JS)（25.59），但VerbMem（19.30）低于FLAT (JS)（15.84），表明DTO在抑制逐字记忆方面优于FLAT，但在保留内在知识方面可能过度遗忘或选择偏差，这一权衡机制在复杂语义纠缠场景下的稳定性尚不明确。

## 总结

本文核心矛盾在于无外部资源约束下，如何精准擦除LLM微调记忆而不损害通用效用。现有方法如FLAT仅抑制输出，未触及知识存储核心；DTO通过Delta-score自主定位关键Token，并采用分治优化策略，在TOFU基准上实现了显著的遗忘质量提升（Llama 2-7B DTO FQ 0.0876 vs FLAT 0.0021）。其边界在于评估仅覆盖静态输出，缺乏对抗鲁棒性验证，且Delta-score对长距离依赖知识的覆盖能力未经验证。当遗忘集包含跨句依赖的复杂事实时，局部扰动策略是否仍能准确识别所有关键Token，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00125)