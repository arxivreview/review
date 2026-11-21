# HuggingFace最新推荐论文 ｜Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment ｜条件等价性下的偏好优化：DPO失效机制与CPO修正

研究机构：香港科技大学、香港浸会大学

论文原文见 [arXiv](https://arxiv.org/abs/2605.20834)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20834)

> 大语言模型对齐的核心矛盾在于，直接偏好优化（DPO）虽简化了强化学习流程，但其理论等价性建立在参考策略已对齐的隐含假设上。当参考策略质量不佳时，DPO会陷入优化相对优势而非绝对对齐的病态收敛。本文通过引入显式约束项修正目标函数，提出CPO与E-CPOC方法，在保留DPO简洁性的同时提供了可证明的对齐保证。这一理论修正弥补了DPO在参考策略偏差下的失效盲区，但其实验规模与E-CPOC的实证验证仍显不足。

## 研究背景

理解DPO的失效机制需先厘清其与RLHF的推导关系。RLHF通过最大化奖励期望并施加KL散度正则化来优化策略，其最优解存在解析形式。DPO的推导关键在于将这一解析形式代入Bradley-Terry模型，从而消除显式奖励模型，将策略优化转化为基于对数概率比的分类任务。这一重参数化过程隐含了一个前提：RLHF最优策略必须偏好人类认可的响应。

该前提并非RLHF框架的必然结果。RLHF在平衡奖励最大化与KL正则化时，若参考策略对偏好响应的概率赋值过低，KL惩罚项将主导优化过程，导致最优策略继承参考策略的错误偏好。Fisch et al. (2024) 与 Lin et al. (2024) 已指出DPO隐式奖励的过拟合与泛化缺陷，但均未触及推导层面的假设失效。本文切入点在于证明DPO与RLHF的等价性是条件性的：当参考策略质量低于阈值时，DPO实际优化的是相对于参考策略的优势，而非绝对的人类偏好对齐，导致策略在损失下降的同时系统性偏好错误响应。

## 核心方法

### 方法参照系

DPO的标准流程基于Bradley-Terry模型，通过最大化对数似然来优化策略，其损失函数依赖于策略与参考策略的对数概率比。本文问题与该通用流程的关键差异在于，DPO的推导假设参考策略的对数概率比 $\delta_{\pi_{ref}}$ 不会过度负向，而实际场景中该假设常被违反，导致优化目标发生本质偏移。

### 隐含假设失效与病态收敛

DPO推导中代入RLHF最优策略 $\pi^*$ 至Bradley-Terry模型时，隐含假设 $\delta_{\pi^*} > \delta_{\pi_{ref}}$ 对偏好对 $(y_w, y_l)$ 成立。当参考策略严重失配，即 $\delta_{\pi_{ref}} \le -\Delta r^*/\beta$ 时，该假设失效。此时DPO的梯度幅值由 $\sigma(-\beta(\delta_{\pi_\theta} - \delta_{\pi_{ref}}))$ 控制，随着 $\delta_{\pi_\theta}$ 向0逼近，梯度幅值逐渐衰减，策略陷入“不良解空间” $\mathcal{U}$，其中策略满足DPO的相对优势准则但违反人类偏好。

### 约束偏好优化与自适应边距

为修复假设失效，CPO在RLHF目标中引入显式约束项，直接鼓励策略在日志概率空间中偏好 $y_w$。其损失函数为：

$$
\mathcal{L}_{CPO}(\pi_\theta) = -\mathbb{E}_{\mathcal{D}} \left[ \log \sigma \left( \beta (\delta_{\pi_\theta} - \delta_{\pi_{ref}}) - \tilde{\gamma}_{ref} \right) \right]
$$

其中 $\tilde{\gamma}_{ref} = \gamma (1/\pi_{ref}(y_w|x) + 1/\pi_{ref}(y_l|x))$ 是基于参考策略的自适应边距。该设计动机在于，当参考策略失配时，$\tilde{\gamma}_{ref}$ 提供非负的有效边距，确保梯度信号足够强以推动 $\delta_{\pi_\theta}$ 越过0，从而避免陷入 $\mathcal{U}$。进一步，E-CPOC通过保守上界 $\Phi_{cons}(\delta_{\pi_{ref}})$ 替代真实奖励差，无需奖励模型即可实现显式约束，其损失函数为：

$$
\mathcal{L}_{E-CPOC}(\pi_\theta) = -\mathbb{E}_{\mathcal{D}} \left[ \log \sigma \left( \beta (\delta_{\pi_\theta} - \delta_{\pi_{ref}}) - \beta \Phi_{cons}(\delta_{\pi_{ref}}) \right) \right]
$$

该公式的物理含义是，$\Phi_{cons}$ 根据参考策略的置信度动态调整约束强度，对困难样本施加更强修正，对简单样本最小化干预，实现了样本自适应的对齐保证。

## 实验评估

实验基于Llama-3-8B-Instruct模型与princeton-nlp/llama3-ultrafeedback-armorm数据集，在AlpacaEval 2与Arena-Hard基准上评估。基线覆盖DPO、SimPO、IPO、KTO等主流离线偏好优化方法，但缺失RLHF在线方法对比，可能低估CPO相对于在线对齐的优势。

| 方法 | AlpacaEval 2 WR (%) | AlpacaEval 2 LC (%) | Arena-Hard WR (%) |
| :--- | :--- | :--- | :--- |
| SFT-Base | 14.22 | 13.47 | 19.2 |
| DPO | 24.60 | 25.09 | 28.9 |
| SimPO | 23.48 | 25.91 | 30.0 |
| CPO (Ours) | 25.15 | 26.57 | 32.6 |

CPO在AlpacaEval 2的LC胜率上以26.57%超越SimPO的25.91%，在Arena-Hard上以32.6%领先SimPO的30.0%，表明约束项在困难判别性提示上有效缓解了长度偏差与偏好混淆。

消融实验显示，当参考策略对数概率比 $\delta_{\pi_{ref}} < 0$ 的比例从32.35%提升至39.56%时，CPO的LC胜率从27.60%微降至27.35%，而DPO性能显著波动。这一反直觉发现表明，CPO的自适应边距在参考策略失配加剧时仍能维持梯度强度，验证了约束项对病态收敛的鲁棒性。

评估边界方面，实验仅使用8B规模模型，未验证更大模型上的有效性；E-CPOC缺乏实证实验，仅提供理论保证；代码已开源，但超参数 $\gamma$ 的选取依赖参考策略质量先验，未提供自动化调参方案。

## 关联研究分析

从问题动机看，本文与SimPO的设计哲学存在根本差异。SimPO通过长度归一化隐式奖励消除参考策略，从而规避了参考策略质量的影响，但代价是放弃了RLHF-BT框架的等价性保证。CPO保留参考策略以维持RLHF等价性，通过约束项修正假设失效，其根源在于任务特性：当参考策略质量可控时，保留参考策略能提供更强的正则化信号；当参考策略质量不可控时，SimPO的无参考设计可能更稳健。

从方法设计看，CPO与IPO的正则化机制不同。IPO通过修改损失函数引入二次正则化以缓解过拟合，而CPO通过增强RLHF目标引入显式约束以修复假设失效。这一差异源于问题本质：IPO针对的是DPO隐式奖励的数值不稳定，CPO针对的是DPO推导层面的逻辑漏洞。当参考策略质量良好时，IPO的正则化可能足够；当参考策略质量不佳时，CPO的约束项提供了更直接的修复路径。

## 总结

本文要解决的核心矛盾是DPO理论等价性的条件性失效，即参考策略质量不佳时DPO优化目标偏离人类偏好。现有方法如SimPO通过消除参考策略规避问题，但牺牲了RLHF框架的完整性；IPO通过正则化缓解数值问题，但未触及推导假设。本文抓住“参考策略质量决定等价性成立”这一被忽略的点，通过引入自适应边距约束项，在保留DPO简洁性的同时提供了可证明的对齐保证。实验证明CPO在8B模型上LC胜率达26.57%，Arena-Hard胜率32.6%，优于主流基线。本文的边界在于实验规模有限，E-CPOC缺乏实证验证，且 $\gamma$ 的选取依赖参考策略质量先验。当参考策略质量评估本身存在噪声时，自适应边距的保守上界是否会导致过度约束，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.20834)