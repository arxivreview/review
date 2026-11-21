# HuggingFace最新推荐论文 ｜Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance ｜稳定生成流网络

研究机构：韩国科学技术院、Naver AI实验室

作者：Minchan Kwon、Sunghyun Baek、Minseo Kim 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.00553)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.00553)

> 导读 LLM红队测试旨在通过自动化对抗搜索发现模型安全漏洞，但现有强化学习与质量多样性方法在追求高攻击成功率时往往陷入模式坍塌，导致漏洞覆盖广度不足。生成流网络（Generative Flow Networks, GFNs）虽能通过分布匹配平衡质量与多样性，但其依赖的配分函数估计在离散高维文本空间中极不稳定，且易受毒性分类器噪声干扰。本文提出稳定生成流网络（Stable-GFN），通过对比轨迹平衡目标消除全局参数估计，并引入噪声过滤与流畅度约束机制。该方法在保持高攻击成功率的同时显著提升了攻击多样性，但其评估局限于单轮文本毒性，未涉及智能体行为轨迹。

## 研究背景

理解本文需厘清三个核心概念的因果链条。红队测试本质是在离散文本空间搜索高毒性提示词，传统强化学习（Reinforcement Learning, RL）通过最大化毒性奖励训练攻击者，但稀疏奖励信号易导致策略收敛至单一高奖励样本，即模式坍塌。为突破此局限，生成流网络（GFlowNets, GFNs）将任务重构为分布匹配问题，要求采样概率与奖励成正比，理论上能覆盖毒性景观的多个模式。然而，GFN的标准训练目标轨迹平衡（Trajectory Balance, TB）需显式估计配分函数 $Z$，在组合爆炸的token空间中，$Z$ 的高方差梯度估计会引发训练崩溃，使模型退化为仅拟合狭窄的高奖励分布。

LLM红队测试的自动化范式自2022年确立以来，主流路线分为RL、质量多样性（Quality-Diversity, QD）与GFN三类。RL方法如Jailbreak R1虽能发现高毒性攻击，但唯一攻击数（Unique Attacks, UA）极低；QD方法如Rainbow Teaming依赖冻结LLM的指令跟随能力，难以发现高毒性攻击；GFN方法虽具理论优势，但直接应用时面临配分函数估计失效与奖励噪声两大瓶颈。毒性分类器对分布外（Out-of-Distribution, OOD）token（如乱码）提供密集但噪声大的信号，进一步加剧了探索崩溃。本文切入点在于改造GFN的训练目标，消除对不稳定全局参数的依赖，并针对红队场景特有的噪声奖励设计过滤机制。

## 核心方法

### 方法参照系

GFN红队框架将攻击提示生成视为轨迹采样，目标策略 $\pi_\theta(\mathbf{y}) \propto R(\mathbf{y})$。标准TB目标通过最小化 $\mathcal{L}_{TB} = (\log \pi_\theta(\mathbf{y}) - \log R(\mathbf{y}) - \log Z_\theta)^2$ 实现分布匹配。本文问题与该通用流程的关键差异在于：$Z_\theta$ 在离散高维空间难以准确估计，且 $R(\mathbf{y})$ 包含大量噪声，导致TB目标失效。

### 对比轨迹平衡

TB目标中 $Z_\theta$ 的显式估计是训练不稳定的根源。本文提出对比轨迹平衡（Contrastive Trajectory Balance, CTB），通过成对比较抵消全局参数。设计动机在于避免绝对流匹配带来的高方差梯度，转而利用相对流一致性。对于独立样本 $\mathbf{y}_1, \mathbf{y}_2 \sim \pi_\theta$，CTB损失定义为：

$$ \mathcal{L}_{CTB} = \left( \log \frac{\pi_\theta(\mathbf{y}_1)}{\pi_\theta(\mathbf{y}_2)} - \log \frac{R(\mathbf{y}_1)}{R(\mathbf{y}_2)} \right)^2 $$

该公式的物理含义是：策略对两个样本的对数概率比应等于其奖励的对数比。由于 $Z$ 在比值中抵消，无需估计全局参数。理论证明表明，CTB的全局最小值对应与TB相同的最优策略 $\pi_\theta(\mathbf{y}) = R(\mathbf{y})/Z$，但梯度方差显著降低，因其结构等价于策略梯度中的留一法基线（Leave-One-Out baseline）。

### 噪声梯度剪枝与流畅度稳定

CTB虽消除 $Z$ 估计，但成对比较会放大两个样本的奖励噪声。毒性分类器对同一攻击提示的多次采样可能产生不同毒性分数，这种随机性导致无效梯度更新。本文引入噪声梯度剪枝（Noisy Gradient Pruning, NGP），仅当奖励对比超过显著性阈值 $\sigma$ 时才计算损失：

$$ \mathcal{L}_{NGP} = \mathcal{L}_{CTB} \cdot \mathbb{I}\left[ \left| \log R(\mathbf{y}_1) - \log R(\mathbf{y}_2) \right| > \sigma \right] $$

此机制过滤低显著性奖励对，防止模型过拟合于分类器的随机波动。此外，为抑制模型通过生成乱码（OOD token）进行奖励黑客（Reward Hacking），引入Min-K流畅度稳定器（MKS）。MKS计算参考模型对序列中 $k$ 个最低概率token的平均对数似然，若低于阈值则施加惩罚。设计动机在于：乱码虽可能获得高毒性分数，但缺乏语义有效性；MKS通过token级似然约束，将搜索空间限制在流畅自然语言范围内，避免陷入局部最优。

## 实验评估

实验使用Qwen2.5-1.5B作为攻击者，Qwen2.5-1.5B-Instruct作为受害者，Meta-Llama-Guard-3-8B作为毒性分类器，基于AdvBench数据集评估。基线覆盖RL（PPO, Jailbreak R1）、QD（Rainbow Teaming）及GFN（GFN-TB）三类路线，缺失GCG等白盒基线（因黑盒设定）。主实验结果显示，S-GFN在目标受害者上取得92.55% (±2.87) 的攻击成功率（ASR）和134.00 (±12.77) 的唯一攻击数（UA），显著优于GFN-TB的17.67 (±6.51) UA和PPO的3.00 (±1.00) UA。

| 方法 | UA (#) | ASR (%) |
| :--- | :--- | :--- |
| PPO | 3.00 (±1.00) | 91.70 (±2.95) |
| GFN-TB | 17.67 (±6.51) | 36.75 (±5.56) |
| Rainbow Teaming | 7.36 (±1.07) | 33.00 (±5.20) |
| S-GFN (Ours) | 134.00 (±12.77) | 92.55 (±2.87) |

消融实验验证了各组件贡献。在MKS奖励设置下，CTB相比TB将UA从67提升至108，ASR从85.8%降至82.9%，表明CTB以轻微ASR损失换取多样性提升；加入NGP后，UA进一步增至121，ASR回升至92.2%，证实NGP有效过滤噪声并恢复攻击效能。奖励设置对比显示，无约束奖励导致GFN-TB和GFN-CTB均收敛至乱码局部最优（UA为0），而MKS将UA提升至67（TB）和108（CTB），证明流畅度约束对避免奖励黑客至关重要。

评估边界方面，UA指标依赖聚类阈值（t=0.7），不同阈值下数值可比性受限；实验仅使用单一受害者模型和分类器，未报告跨模型置信区间；代码已开源，但超参数（如 $\sigma$, $k$）的敏感性分析仅在附录简述，缺乏大规模计算资源对比。

## 关联研究分析

从问题动机看，本文与Rainbow Teaming（Samvelyan et al., 2024）均旨在解决模式坍塌，但路径截然不同。Rainbow Teaming通过预定义风格-主题矩阵维护档案库，强制多样性但受限于冻结LLM的指令跟随能力，导致高毒性攻击发现率低（ASR 33.00%）。S-GFN则通过分布匹配内在保证多样性，无需外部档案，且能发现更高毒性攻击（ASR 92.55%）。差异根源在于：QD方法将多样性作为显式约束，而GFN方法将其作为分布匹配的自然结果；前者在强对齐模型上因指令跟随失效而退化，后者因优化目标直接关联奖励景观而更具鲁棒性。

从方法设计看，本文与Jailbreak R1（Guo et al., 2025）同属RL/GFN范畴，但优化机制存在本质区别。Jailbreak R1采用GRPO进行在线策略优化，依赖CoT推理提升攻击质量，但易陷入单一高奖励模式（UA仅3.00）。S-GFN采用离线分布匹配，通过CTB的成对比较实现方差缩减，其梯度结构类似RLOO基线，但应用于流匹配而非策略梯度。这种差异导致S-GFN在多样性上占优，但在单轮极致ASR上略低于JailbreakSkill（100.0%），反映分布匹配与奖励最大化在优化目标上的内在张力。

## 总结

本文核心矛盾在于GFN红队测试中配分函数估计不稳定与奖励噪声导致的模式坍塌。现有TB目标因依赖全局参数 $Z$ 而在离散高维空间失效，RL方法则因奖励稀疏而收敛狭窄。S-GFN通过CTB消除 $Z$ 估计，利用成对比较的相对流一致性实现稳定训练，并辅以NGP和MKS过滤噪声与乱码。实验证明该方法在AdvBench上取得92.55% ASR和134.00 UA，显著优于GFN-TB和PPO基线。其边界在于评估局限于单轮文本毒性，未涉及多轮对话或智能体行为轨迹，且UA指标对聚类阈值敏感。当受害者模型引入动态防御机制时，S-GFN的分布匹配策略能否保持多样性优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.00553)