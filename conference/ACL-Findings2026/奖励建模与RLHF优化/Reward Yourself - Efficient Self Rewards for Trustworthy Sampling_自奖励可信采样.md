# ACL-Findings2026最新论文 ｜Reward Yourself: Efficient Self Rewards for Trustworthy Sampling ｜自奖励可信采样

作者：Mingjie Li、Wai Man Si、Michael Backes 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_657a157c0c03)

> 现有奖励模型在隐私与偏见等可信任务上表现不佳，甚至劣于贪心解码，而重新训练奖励模型成本高昂。本文切入点在于不训练新模型，而是通过剪枝现有大语言模型（LLM）构建“可信”与“不可信”双变体，利用其对数似然比作为辅助奖励信号。具体做法是集成到Best-of-N采样流程中，先过滤低分候选，再由外部奖励模型选择最终答案。该方法在隐私任务上提升10-20%拒绝率，但仅在特定可信域验证，通用基准有效性未证实。

## 研究背景

当LLM面对涉及隐私泄露或刻板印象的提示时，标准奖励模型往往无法区分安全响应与违规响应，导致Best-of-N采样选出错误答案。这一失效源于奖励模型（Reward Model, RM）训练数据中缺乏针对特定可信行为的细粒度标注，使得模型在分布外任务上泛化能力差。为缓解此问题，研究者通常依赖重新训练RM或引入外部安全分类器，但这些方案需要大规模人工偏好数据或额外模型部署，计算与数据成本高昂。

RLHF范式确立了“训练RM+策略优化”的两阶段流程，但标量RM在开放式可信任务中信号稀疏，无法捕捉token级的行为差异。直接偏好优化（Direct Preference Optimization, DPO）虽简化了训练，但仍依赖序列级偏好对，难以解决推理时的实时可信度评估。本文切入点在于利用预训练LLM内部已编码的冲突行为（安全与不安全信号），通过轻量级剪枝分离出两种行为分布，从而在无需额外训练的情况下生成可信度奖励。

## 核心方法

### 方法参照系

本文问题属于推理时奖励增强，与标准RM训练流程的关键差异在于：不拟合外部偏好分布，而是利用模型自身权重剪枝产生的行为差异作为隐式奖励源。

### 基于剪枝的行为分布构建

设计动机：解决外部RM在可信任务上泛化失败的问题，利用预训练模型内部已存在的安全/不安全信号冲突。通常做法是微调模型以学习特定行为，本文改用集差剪枝（Set-difference Pruning）。以可信数据集$D_1$（约100样本）为保留集，指令跟随数据集$D_2$为遗忘集，剪枝得到$\theta_{trust}$；反之得到$\theta_{untrust}$。这两个变体分别近似可信行为分布$p_{trust}(x_t|x_{<t})$与不可信行为分布$p_{untrust}(x_t|x_{<t})$。

### 对数似然比奖励计算

设计动机：序列级平均奖励会被填充词稀释，导致关键安全token信号被淹没。通常做法是对全序列token取平均，本文改为仅计算差异最大的TopK/MinK token。Bradley-Terry模型给出token级对数似然比：

$$
r(x_t) = \log \frac{p_{trust}(x_t|x_{<t})}{p_{untrust}(x_t|x_{<t})}
$$

该公式物理含义为：若某token在可信模型中概率远高于不可信模型，则其奖励值高，表明该token与可信行为强相关。最终SelfRW分数为：

$$
r_{SelfRM}(x; K) = \frac{1}{2K} \sum_{s \in TopK \cup MinK} \log \frac{p_{trust}(x_t|x_{<t})}{p_{untrust}(x_t|x_{<t})}
$$

其中$K = \lambda(T_2 - T_1 + 1)$，$\lambda$控制参与计算的token比例。此设计规避了长度偏差，仅聚焦于行为差异显著的语义关键token。

## 实验评估

实验在Privacy Awareness、Privacy Leakage、Stereotype及Bias四个可信任务上评估，基线包括SkyWork、URM、LlamaGuard及LoRA Classifier。本文未测试RewardBench等通用基准，也未对比DPO等RL基线，评估范围局限于可信域。

| 任务 | 模型 | 方法 | RtA (%) | RtAdp (%) |
| :--- | :--- | :--- | :--- | :--- |
| Privacy Awareness | Vicuna-7B | +SelfRW | 100 | 100 |
| Privacy Awareness | Llama-3.1 | +SelfRW | 89 | 92 |
| Privacy Leakage | Llama-3.1 | +SelfRW | 88 | 93 |
| Stereotype | Qwen2.5 | +SelfRW | 100 | 100 |

在Privacy Awareness任务中，Vicuna-7B使用SelfRW后RtA达到100%，较SkyWork基线的96%提升4个百分点；Llama-3.1的RtAdp从88%提升至92%。Privacy Leakage任务中，Llama-3.1的RtA从SkyWork的60%提升至88%，提升幅度达28个百分点，表明SelfRW在复杂隐私场景下显著优于现有RM。

消融实验显示，超参数$\lambda$对性能影响较小，0.1至0.25范围内RtA波动不大，说明方法对token筛选比例不敏感。$N_1$（过滤阈值）设为3时性能稳定，增大$N_1$会导致Qwen2.5和Llama-3.1性能下降，可能因过度依赖外部RM的弱信号。推理成本方面，SelfRW在Vicuna-7B上内存占用20GB，耗时4秒，低于LlamaGuard的35GB/4秒，但高于纯贪心解码的17GB/2秒。

评估边界：指标仅覆盖RtA/RtAdp，未报告通用能力退化细节（仅定性提及“几乎无影响”）；代码未公开，剪枝阈值$\tau=5$及$\lambda=0.05$的选取缺乏敏感性分析；实验仅使用7B-8B模型，未验证在更大规模模型上的有效性。

## 关联研究分析

从问题动机看，本文与因果去偏（Causal Debiasing）路线存在根本差异。因果去偏通过构建因果图隔离长度等混杂变量，旨在修正RM训练过程中的虚假相关；本文则完全绕过RM训练，直接利用模型内部行为差异作为推理时信号。这种差异源于任务特性：可信任务（如隐私拒绝）的行为模式在预训练数据中已充分编码，无需额外学习，而通用偏好任务需要显式拟合分布。

从方法设计看，本文与InfoRM的信息瓶颈思想有相似之处，均通过筛选关键信息过滤噪声。但InfoRM在训练阶段约束RM仅保留最小偏好相关信息，本文则在推理阶段通过TopK/MinK筛选token级差异。InfoRM需要变分推断优化，计算复杂度高；本文仅需一次剪枝和两次前向传播，效率优势显著。然而，InfoRM处理的是序列级偏好，本文处理token级行为，粒度差异导致两者适用场景不同：InfoRM适合通用对齐，本文适合特定可信域。

## 总结

本文核心矛盾是现有RM在可信任务上泛化失败与重新训练成本高昂之间的冲突。切入点在于利用预训练LLM内部已编码的安全/不安全行为冲突，通过剪枝分离双变体，无需额外训练即可生成token级可信度奖励。方法通过Bradley-Terry对数似然比计算SelfRW分数，集成到Best-of-N采样中。实验证明在隐私任务上RtA提升10-20%，Llama-3.1在Privacy Leakage任务中RtA从60%提升至88%。边界在于仅在7B-8B模型和特定可信域验证，通用基准有效性未知，且剪枝阈值选取缺乏系统性分析。当支持集从100样本扩展至更大规模时，剪枝产生的行为差异是否仍能保持区分度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_657a157c0c03)