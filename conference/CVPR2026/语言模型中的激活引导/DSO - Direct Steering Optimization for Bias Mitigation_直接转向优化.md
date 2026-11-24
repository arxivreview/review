# CVPR2026最新论文 ｜DSO: Direct Steering Optimization for Bias Mitigation ｜直接转向优化

研究机构：美国卡内基梅隆大学

作者：Lucas Monteiro Paes、Nivedha Sivakumar、Yinong Oliver Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.15926)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15926)

> 视觉语言模型（VLM）在识别职业等社会角色时，常受性别刻板印象影响，导致决策偏差。现有激活引导方法依赖固定向量或启发式规则，在VLM偏见缓解中缺乏可控性且易损害模型通用能力。DSO通过强化学习直接优化稀疏线性干预参数，实现推理时偏见与能力的动态平衡。该方法在VLM和LLM上均优于基线，但RL训练成本与跨模态泛化性未充分验证。

## 研究背景

当VLM处理包含人物图像的任务时，其内部激活状态往往编码了性别与职业的刻板关联。这种关联并非显式存储，而是分散在Transformer各层的隐藏状态中，形成复杂的特征纠缠。传统微调方法虽能消除偏见，但需更新全部权重，计算成本高且易引发灾难性遗忘；提示工程则依赖上下文长度，无法在推理时动态调整干预强度。激活引导（Activation Steering）通过在推理时直接修改隐藏状态，以极低开销实现行为控制，其核心假设是特定行为在激活空间中具有线性可分性。

现有激活引导方法主要分两类：一类如对比激活加法（CAA）和推理时干预（ITI），通过预定义对比样本或线性探针计算固定转向向量，思路简洁但缺乏对输入分布的适应性；另一类如稀疏自编码器（SAE）方法，通过解耦特征提升特异性，但依赖SAE训练质量且额外开销大。这些方法在LLM真实性控制上表现良好，但在VLM偏见缓解中暴露出关键缺陷：固定向量无法适应视觉-语言交互中的复杂偏见结构，且缺乏对公平性与准确性权衡的显式控制。DSO的切入点在于，将转向参数视为可优化变量，通过强化学习直接最小化偏见指标，同时引入稀疏性与KL散度约束保护模型能力。

## 核心方法

### 方法参照系

本文问题属于激活引导中的“自适应动态”路线，与CAA、ITI等启发式方法的关键差异在于：后者通过预定义规则计算转向向量，而DSO将转向参数$a, b$作为RL策略变量，直接优化公平性奖励。

### 公平性奖励函数设计

DSO的核心创新在于将偏见缓解转化为标准RL问题。传统方法中，偏见指标（如Per-Occupation Bias）是生成结果的聚合统计量，无法直接作为RL奖励。DSO定义逐样本公平性奖励：若模型输出与某职业的主流刻板印象一致，奖励为$-1$；否则为$+1$。该设计鼓励模型在刻板与非刻板输出间达到均衡，而非单纯抑制某类输出。

$$
r_{\pi}(\mathbf{y}) = \begin{cases} -1 & \text{if } \text{stereotype}(\mathbf{y}) = S_{\pi}^{[*]}(o) \\ +1 & \text{otherwise} \end{cases}
$$

其中$S_{\pi}^{[*]}(o)$为职业$o$的主流刻板印象。该公式将全局偏见指标分解为逐样本信号，使PPO等策略梯度算法可直接优化。

### 稀疏线性干预优化

DSO在LayerNorm模块施加线性干预，通过$\ell_1$惩罚与KL散度约束控制干预范围。优化目标为最大化公平性奖励，同时最小化干预稀疏度与模型分布偏移：

$$
\max_{\mathbf{a}, \mathbf{b}} \mathbb{E}_{(\mathbf{x}, \text{Img}) \sim D} [r_{\pi_{\mathbf{a}, \mathbf{b}, \lambda=1}}(\mathbf{y})] - \alpha \|\mathbf{a}\|_1 - \delta \cdot \text{KL}(\pi_{\mathbf{a}, \mathbf{b}, \lambda=1} \| \pi_{\text{base}})
$$

该公式中$\alpha$控制稀疏度，$\delta$限制KL散度。$\ell_1$惩罚确保仅少数神经元被干预，KL约束防止模型能力退化。与CAA的固定向量不同，DSO的$\mathbf{a}, \mathbf{b}$由RL学习，能自适应不同输入分布。

## 实验评估

实验在SocialCounterfactuals（VLM）和SynthBias（LLM）数据集上进行，评估Per-Occupation Bias、Stereotype Gap及准确性。基线覆盖CAA、ITI和Prompting，但缺失SAE类方法。DSO在Qwen-2.5-7B VL上，$\lambda=0.2$时Per-Occupation Bias降至15.4%，Stereotype Gap降至6.6%，Unambiguous Accuracy保持95.7%；而CAA和ITI的Bias分别为28.5%和29.3%，且准确性下降更显著。

| 模型 | 方法 | $\lambda$ | Per-Occupation Bias (%) | Stereotype Gap (%) | Unambiguous Accuracy (%) |
|---|---|---|---|---|---|
| Qwen2.5-7B VL | Base | – | 25.8% (1.6) | 18.0% (0.9) | 96.5% (0.1) |
| Qwen2.5-7B VL | CAA | 1.0 | 28.5% (1.7) | 22.4% (0.9) | 96.5% (0.1) |
| Qwen2.5-7B VL | ITI | 5.0 | 29.3% (1.8) | 20.8% (0.9) | 96.3% (0.1) |
| Qwen2.5-7B VL | DSO | 0.2 | 15.4% (1.0) | 6.6% (0.9) | 95.7% (0.2) |
| Qwen2.5-7B VL | DSO | 1.0 | 8.7% (0.6) | 0.1% (0.8) | 80.0% (0.3) |

DSO在$\lambda=1.0$时Bias降至8.7%，但Unambiguous Accuracy降至80.0%，显示公平-能力权衡的陡峭性。消融实验表明，干预60%的LayerNorm神经元即可达到接近全干预的Bias降低效果，仅修改0.005%参数。

评估边界方面，论文未报告RL训练成本与GPU资源，跨模型泛化性仅在Qwen、Gemma、Llama上验证，未覆盖多模态对齐任务。代码未公开，超参数$\alpha, \delta$的敏感性分析缺失。

## 关联研究分析

从问题动机看，DSO与CAA、ITI的核心差异在于优化目标。CAA通过对比样本计算固定向量，假设偏见方向稳定；DSO通过RL直接优化偏见指标，适应输入分布变化。这一差异源于VLM偏见结构的复杂性：视觉-语言交互中，偏见方向随图像内容动态变化，固定向量无法捕捉。DSO的RL框架能学习输入依赖的干预策略，但代价是训练开销。

从方法设计看，DSO与SAE-SSV等稀疏特征方法共享稀疏性目标，但实现路径不同。SAE通过解耦特征提升特异性，DSO通过$\ell_1$惩罚直接约束干预范围。DSO未对比SAE方法，可能因VLM偏见任务中SAE训练成本过高。DSO的KL散度约束与PID Steering的动态调整思想一致，但DSO的$\lambda$是全局参数，而非逐层自适应。

## 总结

DSO解决的核心矛盾是VLM偏见缓解中公平性与模型能力的权衡。现有方法因固定向量缺乏适应性，无法在降低偏见的同时保持准确性；DSO通过RL优化稀疏线性干预，直接最小化偏见指标，实现推理时动态控制。实验显示，DSO在Qwen-2.5-7B VL上$\lambda=0.2$时Bias降至15.4%，准确性保持95.7%。其边界在于RL训练成本未量化，且跨模态泛化性验证有限。当支持集扩大至多模态对齐任务时，RL优化的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15926)