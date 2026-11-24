# ACL-Findings2026最新论文 ｜DynamicFocalPO: Adaptive Focusing Strategy for Preference Optimization ｜动态聚焦偏好优化

研究机构：南京大学

作者：Shu Zhou、Junan Chen、Rui Ling 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fea5571ef4f)

> 直接偏好优化（DPO）在处理含噪偏好数据时，因固定加权策略导致梯度噪声累积，阻碍模型收敛。现有变体如FocalPO虽引入调制因子，但静态超参数无法适应模型能力演化。本文提出DynamicFocalPO，通过余弦退火动态调整聚焦参数，实现从易到难的课程学习。该方法在7B/8B模型上验证了性能增益，但缺乏大规模模型验证，其动态调度在复杂多目标场景下的泛化能力存疑。

## 研究背景

当模型面对人类标注的偏好数据时，部分样本存在排序错误，即“落败”响应实际优于“获胜”响应。DPO的梯度机制对这类错误排序样本过度敏感，导致训练初期引入大量噪声梯度，阻碍基础能力建立。为缓解此问题，FocalPO引入调制因子 $p^\gamma$ 降低错误样本权重，但固定 $\gamma$ 值无法匹配模型从“难以区分简单偏好”到“需挑战复杂偏好”的能力演化过程。

偏好优化领域的主流路线包括修改损失函数（如SimPO的长度归一化）或调整样本权重（如WPO），但这些方法均假设超参数在训练全程保持恒定。这一假设忽略了模型学习能力的动态变化：早期模型需聚焦可靠信号建立基础，后期模型需暴露于困难样本以突破瓶颈。DynamicFocalPO的切入点在于将静态加权转化为时间依赖的动态调度，借鉴课程学习（Curriculum Learning）的“由易到难”原则，使聚焦强度 $\gamma(t)$ 随训练步数自适应衰减，从而解决固定超参数与模型能力演化不匹配的核心矛盾。

## 核心方法

### 方法参照系

本文问题属于离线偏好优化中的样本加权策略改进。标准DPO流程直接优化策略 $\pi_\theta$ 以最大化偏好概率，但缺乏对样本质量的区分机制。FocalPO在此基础上引入固定调制因子，但未能解决超参数静态性与模型能力动态性之间的根本冲突。

### 动态聚焦损失函数

FocalPO通过固定 $\gamma$ 抑制错误排序样本的梯度贡献，但无法适应训练不同阶段的需求。DynamicFocalPO将 $\gamma$ 替换为时间函数 $\gamma(t)$，损失函数定义为：

$$
\mathcal{L}_{\text{DynamicFocalPO}} = -\mathbb{E}_{(x,y_w,y_l)\sim\mathcal{D}} \left[ p(y_w \succ y_l | x)^{\gamma(t)} \log p(y_w \succ y_l | x) \right]
$$

其中 $p(y_w \succ y_l | x) = \sigma(\hat{r}_\theta(y_w|x) - \hat{r}_\theta(y_l|x))$ 为隐式偏好概率。该设计使训练初期 $\gamma(t)$ 较高，强烈抑制错误样本；后期 $\gamma(t)$ 趋近于0，允许困难样本参与优化，实现自适应课程学习。

### 余弦退火调度策略

固定 $\gamma$ 无法平衡早期稳定性与后期挑战性，DynamicFocalPO采用余弦退火调度 $\gamma(t) = \gamma_{\min} + \frac{2(\gamma_{\max}-\gamma_{\min})}{1+\cos(\pi t/T)}$，其中 $T$ 为总训练步数。该策略提供平滑过渡，避免线性衰减的早期突变或指数衰减的过快下降。理论分析表明，动态调度实现了自适应熵正则化：高 $\gamma$ 阶段抑制噪声梯度方差，低 $\gamma$ 阶段恢复DPO的完整梯度信息，使模型在稳定收敛的同时逐步提升对复杂偏好的区分能力。

## 实验评估

实验在Mistral-Base-7B和Llama-3-Instruct-8B上进行，使用UltraFeedback数据集，对比DPO、SimPO及FocalPO（$\gamma=0.05, 0.08$）。基线覆盖主流DPO变体，但缺失IPO、KTO等近期方法，可能低估动态调度相对于其他鲁棒优化策略的优势。

| 模型 | 方法 | AlpacaEval 2.0 LCWR (%) | Arena-Hard WR (%) |
| :--- | :--- | :--- | :--- |
| Llama-3-8B | DPO | 48.2±0.6 | 33.1±1.2 |
| Llama-3-8B | FocalPO (γ=0.08) | 55.2±0.5 | 35.0±0.8 |
| Llama-3-8B | DynamicFocalPO (Cosine) | 56.4±0.5 | 36.0±0.7 |
| Mistral-7B | DPO | 18.6±0.7 | 20.6±0.8 |
| Mistral-7B | DynamicFocalPO (Cosine) | 21.2±0.5 | 24.1±0.3 |

DynamicFocalPO (Cosine) 在Llama-3-8B上LCWR达56.4%，较最优固定 $\gamma$ 的FocalPO提升1.2个百分点，且在Arena-Hard上WR提升1.0个百分点，验证了动态调度的有效性。

消融实验显示 $\gamma_{\max}=0.1, \gamma_{\min}=0.01$ 为最优组合，$\gamma_{\min}$ 过高会损害后期学习，$\gamma_{\max}$ 过低则削弱早期聚焦效果。训练动态分析表明，正确排序样本的梯度贡献比从早期的78%降至后期的47%，收敛至DPO的约46%，证实了课程学习机制的实现。

评估边界方面，实验仅覆盖7B/8B规模模型，未验证70B+大模型上的有效性；评测指标限于指令遵循基准，未包含多目标对齐或安全对齐维度；论文未提供代码仓库，超参数设置（如 $\alpha=3$ 用于指数衰减）缺乏详细推导，可复现性受限。

## 关联研究分析

从问题动机看，DynamicFocalPO与WPO（Zhou et al., 2024）均关注样本加权，但WPO基于静态偏好分数加权，而本文聚焦于排序错误的动态抑制。这一差异源于任务特性：WPO假设偏好质量在训练前已知，而DynamicFocalPO承认模型对偏好质量的判断随训练演化。然而，当偏好数据噪声分布非平稳时，静态加权是否仍具优势，论文未给出回答。

从方法设计看，DynamicFocalPO与SimPO（Meng et al., 2024）同属DPO变体，但SimPO通过长度归一化消除参考模型依赖，而本文保留参考模型并引入时间调度。这一选择暗示动态调度可能依赖参考模型的稳定性，若参考模型本身存在偏差，$\gamma(t)$ 的调节可能放大而非抑制噪声。此外，本文未探索动态 $\gamma$ 与SimPO长度归一化的组合效果，二者是否互补或冲突，缺乏实验证据。

## 总结

DynamicFocalPO解决的核心矛盾是固定超参数与模型能力动态演化之间的不匹配。其切入点在于将课程学习原则引入偏好优化，通过时间依赖的 $\gamma(t)$ 实现自适应聚焦，这是固定 $\gamma$ 的FocalPO无法做到的。方法上，本文提出余弦退火调度的动态聚焦损失，在Llama-3-8B上LCWR达56.4%，较最优固定 $\gamma$ 提升1.2个百分点。然而，实验仅覆盖7B/8B模型，且未验证多目标对齐场景，其动态调度在复杂偏好冲突下的鲁棒性未知。当模型规模扩展至70B+时，动态 $\gamma$ 的收敛行为是否仍遵循课程学习假设，论文未提供证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_0fea5571ef4f)