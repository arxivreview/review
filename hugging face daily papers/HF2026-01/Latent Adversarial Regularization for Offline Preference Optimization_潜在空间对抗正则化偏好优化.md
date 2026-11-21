# HuggingFace最新推荐论文 ｜Latent Adversarial Regularization for Offline Preference Optimization ｜潜在空间对抗正则化偏好优化

研究机构：美国斯坦福大学

论文原文见 [arXiv](https://arxiv.org/abs/2601.22083)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22083)

> 离线偏好优化长期依赖Token空间KL散度约束策略与参考模型的偏离，但Token距离无法捕捉语义相似性，导致正则化在分布偏移下失效。GANPO将正则化迁移至潜在表示空间，通过引入双判别器构建对抗目标，使策略模型在保持语义结构的同时学习偏好。该方法在AlpacaEval 2.0上较DPO提升1.41%至2.0%的长度控制胜率，并显著增强了高熵采样下的鲁棒性，但其效果受限于参考模型潜在结构的完整性。

## 研究背景

离线偏好优化（Offline Preference Optimization, OPO）的核心在于利用成对偏好数据更新策略模型，同时通过正则化项防止其偏离参考策略。主流方法如直接偏好优化（Direct Preference Optimization, DPO）采用Token空间KL散度作为正则化手段，该约束在数学上等价于隐式奖励差值的最大化。然而，Token空间度量存在根本缺陷：语义相似的文本（如“Hi there”与“Good morning to you”）在Token距离上可能相距甚远，而语义不同的文本（如“Hi there”与“Hit there”）却可能距离很近。这种度量失配导致Token空间正则化无法有效约束模型的语义行为，仅能抑制表面形式的变化。

现有OPO方法在分布偏移场景下表现出脆弱性。当采样温度升高或生成轨迹偏离训练分布时，基于Token似然的优化目标易引发结构崩塌，表现为指令遵循准确率急剧下降。同时，隐式奖励模型常出现奖励黑客现象，即模型生成表面高分但实际有害的内容。GANPO的切入点在于识别出潜在表示空间（Latent Representation Space）比Token空间更紧凑且富含语义结构信息。通过惩罚策略模型与参考模型在潜在空间分布的散度，GANPO旨在提供结构性的对齐反馈，弥补Token级约束在语义一致性上的不足。

## 核心方法

### 方法参照系

OPO标准流程包含两个组件：基于偏好数据的隐式奖励损失（如DPO损失）和基于Token概率分布的KL正则化。本文的关键差异在于将正则化项从Token概率空间转移至LLM最后一层隐藏状态构成的潜在空间，并采用生成对抗网络（Generative Adversarial Networks, GANs）机制估计该空间中的散度。

### 潜在空间散度估计

Token空间KL散度要求显式概率密度，而潜在表示不具备此性质。GANPO采用相对平均GAN（Relativistic Average GANs, RaGANs）目标函数来估计Jensen-Shannon散度。判别器 $D_\phi$ 被训练以区分来自参考模型（真实样本）和策略模型（假样本）的潜在表示 $h$。RaGAN散度定义为：

$$ D_{Ra}(p_\theta \| p_{ref}) = \mathbb{E}_{h \sim p_{ref}} [\log \tilde{D}_\phi(h)] - \mathbb{E}_{h \sim p_\theta} [\log(1 - \tilde{D}_\phi(h))] $$

其中 $\tilde{D}_\phi(h)$ 为相对判别器输出。该公式的物理含义是最大化参考模型表示与策略模型表示在判别器视角下的相对真实性差距，从而在潜在空间中拉近两者分布。

### 四元组对比框架

单一判别器难以同时分离“好”与“坏”响应流形。GANPO引入双判别器架构，分别处理正负样本。对于偏好三元组 $(x, y_w, y_l)$，提取四个潜在表示：参考模型的正/负表示 $h^+_{ref}, h^-_{ref}$ 和策略模型的正/负表示 $h^+_\theta, h^-_\theta$。策略模型的对抗损失为：

$$ L_{adv} = \mathbb{E}_{h^+_\theta} [\log(1 - \tilde{D}_{\phi_{pos}}(h^+_\theta))] + \mathbb{E}_{h^-_\theta} [\log(1 - \tilde{D}_{\phi_{neg}}(h^-_\theta))] $$

该设计动机在于，正负响应在潜在空间中可能位于拓扑不同的流形，双判别器允许模型分别学习高质量与低质量响应的结构特征，提供比单一二元分类更密集的结构性反馈。

## 实验评估

实验基于UltraFeedback数据集，对比基线包括DPO和SimPO，覆盖Gemma2-2B-it与Llama3-8B-Instruct两种架构。基线选择聚焦于主流OPO方法，未包含IPO或KTO等近期变体，但足以验证潜在正则化的通用性。

| 方法 | 模型 | Win Rate | LC-Win Rate | Avg Length |
| :--- | :--- | :--- | :--- | :--- |
| DPO | Gemma2-2B-it | 22.76 | 27.79 | 1668 |
| GANPO (DPO) | Gemma2-2B-it | 24.17 | 29.69 | 1664 |
| SimPO | Gemma2-2B-it | 30.66 | 36.03 | 1740 |
| GANPO (SimPO) | Gemma2-2B-it | 31.37 | 36.74 | 1745 |
| DPO | Llama3-8B-Instruct | 33.90 | 32.34 | 2041 |
| GANPO (DPO) | Llama3-8B-Instruct | 35.23 | 33.87 | 2043 |

GANPO在两种模型规模上均带来稳定提升，Gemma2-2B-it的LC-Win Rate较DPO提升1.90个百分点，Llama3-8B-Instruct提升1.53个百分点，且响应长度基本保持不变，表明增益并非源于冗长输出。

| 判别器架构 | Win Rate | LC-Win Rate |
| :--- | :--- | :--- |
| N/A (DPO) | 22.76 | 27.79 |
| MSE (fixed) | 22.96 | 27.03 |
| MLP | 22.66 | 27.52 |
| Transformer | 24.17 | 29.69 |

消融实验显示，Transformer判别器显著优于固定MSE或MLP判别器，LC-Win Rate提升2.16个百分点。这表明捕捉长程依赖和序列级结构对于潜在空间正则化至关重要，简单的标量或局部批评无法提供有效的几何约束。

评估边界方面，论文未报告置信区间，且主要依赖AlpacaEval 2.0单一基准。代码已开源，但超参数调优细节（如对抗权重 $\lambda$ 的敏感性）未在正文中充分披露。

## 关联研究分析

从正则化机制看，GANPO与SimPO形成鲜明对比。SimPO通过长度归一化隐式奖励消除参考模型，追求计算效率；而GANPO保留参考模型作为潜在空间锚点，以额外计算开销换取结构鲁棒性。这一差异源于任务特性：SimPO假设长度偏差是主要噪声源，而GANPO认为语义结构崩塌是分布偏移下的核心风险。当参考模型本身存在潜在结构缺陷时，GANPO可能继承其拓扑错误，这是SimPO无需承担的风险。

从对抗训练视角看，GANPO借鉴了RaGANs的稳定性改进，但将其应用于LLM对齐这一新场景。与标准GAN不同，GANPO的“真实”数据并非外部教师模型，而是SFT模型。这一选择牺牲了潜在的最优性上限，但确保了训练稳定性与计算可行性。若SFT模型与目标偏好分布差异过大，判别器可能学习风格差异而非语义差异，导致正则化失效。

## 总结

GANPO旨在解决Token空间正则化无法捕捉语义相似性导致的分布偏移脆弱性问题。其切入点在于利用潜在表示的低维结构化特性，通过RaGANs机制估计潜在空间散度。实验证明，该方法在AlpacaEval 2.0上较DPO提升1.41%至2.0%的LC-Win Rate，并在高熵采样下保持指令遵循稳定性。然而，其性能上限受限于参考模型的潜在结构质量，若SFT模型存在缺陷，GANPO难以突破该锚点。当参考模型与目标偏好分布存在显著拓扑差异时，双判别器能否有效区分语义结构而非表面风格，论文未给出明确回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22083)