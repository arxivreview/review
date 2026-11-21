# ACL-Findings2026最新论文 ｜PEGRL: Improving Machine Translation by Post-Editing Guided Reinforcement Learning ｜后编辑引导的强化学习

研究机构：南京大学

作者：Yunzhi Shen、Hao Zhou、Xin Huang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0629e962232a)

> 机器翻译中的强化学习（RL）长期受困于蒙特卡洛回报估计的高方差，导致策略梯度信号噪声大、训练不稳定。现有基于组相对策略优化（GRPO）的方法仅优化翻译轨迹，忽略了局部精修环节对全局探索的引导作用。PEGRL 将后编辑（Post-Editing, PE）建模为辅助任务，利用其低方差的回报估计稳定翻译策略更新，并通过方差感知加权平衡两任务贡献。该方法在低资源方向上显著优于纯RL基线，但奖励函数对特定质量估计指标的依赖可能引入过拟合风险。

## 研究背景

当大语言模型（LLM）通过RL优化翻译策略时，策略梯度依赖对轨迹回报的蒙特卡洛估计。由于翻译输出空间巨大，直接采样翻译轨迹的回报方差极高，导致优势函数估计不稳定，训练过程易陷入局部最优或震荡。为缓解此问题，GRPO通过组内归一化降低方差，但其基线仍受限于翻译轨迹本身的随机性。后编辑任务针对已有译文进行局部修改，其输出空间远小于完整翻译，条件于固定译文草稿的回报估计方差显著更低，这为构建更稳定的学习信号提供了可能。

RL在机器翻译中的应用已从奖励设计转向采样策略与多任务耦合。MT-R1-Zero等基线采用混合BLEU+COMET奖励，但仅优化单阶段翻译轨迹，未利用后编辑的局部优化特性。Mufu虽引入后编辑，但依赖教师模型与表面指标，未将其纳入统一RL框架。PEGRL的切入点在于：将后编辑从推理时后处理转化为训练时正则化手段，利用其低方差特性稳定翻译策略更新，并通过在线数据生成实现两任务紧耦合。

## 核心方法

### 两阶段策略梯度分解

PEGRL将翻译与后编辑建模为序贯决策过程。给定源句 $q$，模型先生成翻译轨迹 $\tau_0$，再条件于 $\tau_0$ 生成后编辑轨迹 $\tau_1$。策略梯度分解为两项：

$$
\nabla_\theta \mathbb{E}[\mathcal{R}(\tau_1)] = \mathbb{E}_{\tau_0, \tau_1} \left[ \nabla_\theta \log \pi_\theta(\tau_1 | p, \tau_0) \mathcal{R}(\tau_1) \right] + \mathbb{E}_{\tau_0} \left[ \nabla_\theta \log \pi_\theta(\tau_0 | q) \mathbb{E}_{\tau_1}[\mathcal{R}(\tau_1)] \right]
$$

第一项为后编辑策略梯度，第二项为翻译策略梯度。设计动机在于：直接优化翻译轨迹的回报方差高，而条件于固定 $\tau_0$ 的后编辑回报方差更低，利用后者可稳定前者。

### 方差感知梯度加权

为平衡两任务贡献，PEGRL引入加权系数 $\lambda_{pe}$ 和 $\lambda_{mt}$：

$$
\nabla_\theta J = \lambda_{pe} \mathbb{E}_{\tau_0} \left[ \mathbb{E}_{\tau_1} \left[ \nabla_\theta \log \pi_\theta(\tau_1 | p, \tau_0) \mathcal{R}(\tau_1) \right] \right] + \lambda_{mt} \mathbb{E}_{\tau_0} \left[ \nabla_\theta \log \pi_\theta(\tau_0 | q) \mathbb{E}_{\tau_1}[\mathcal{R}(\tau_1)] \right]
$$

主实验设置 $\lambda_{pe}=M, \lambda_{mt}=1$（$M=8$），即后编辑信号权重为翻译信号的8倍。设计动机在于：后编辑基线估计更准确，赋予更高权重可提升样本效率，尽管这导致估计器有偏，但实证表明其收敛更快。

## 实验评估

实验在WMT24与FLORES-200上进行，覆盖EN→FI、EN→TR、EN↔ZH方向。基线包括Qwen3系列、MT-R1-Zero及SOTA大模型（DeepSeek-V3.2、GPT-5.2）。

| 模型 | EN→FI WMT24 chrF++ | EN→FI WMT24 Kiwi | EN→TR WMT24 Kiwi | EN→TR FLORES200 Kiwi |
|---|---|---|---|---|
| Qwen3-8B | 45.86 | 51.92 | 59.25 | 70.62 |
| MT-R1-Zero-8B | 47.45 | 62.16 | 63.96 | 75.92 |
| Ours-8B | 49.02 | 67.90 | 68.14 | 78.26 |

Ours-8B在EN→TR WMT24 COMET-KIWI上达到68.14，与DeepSeek-V3.2的68.13持平，验证了小模型经RL优化后可比肩大模型。EN→FI XCOMET上，Ours-4B较MT-R1-Zero-4B提升8.06点。

消融实验显示，移除翻译级梯度项（$\lambda_{mt}=0$）导致性能下降，证明两任务耦合的必要性。在线生成后编辑数据优于离线静态数据，COMET-KIWI提升1点。

评估指标包含chrF++、COMET-KIWI、XCOMET，但未报告置信区间。代码与模型已开源，训练使用8×A100 GPU，单方向约24小时。

## 关联研究分析

从问题动机看，PEGRL与MT-R1-Zero同属RL for MT路线，但后者仅优化翻译轨迹，忽略后编辑的局部优化特性。PEGRL将后编辑纳入训练循环，利用其低方差特性稳定翻译策略更新，这源于翻译输出空间远大于后编辑输出空间的任务特性。Mufu虽引入后编辑，但依赖教师模型与表面指标，未将其建模为RL策略，导致无法利用后编辑反馈指导翻译优化。

从方法设计看，PEGRL与GRPO框架一致，但引入方差感知加权。GRPO通过组内归一化降低方差，但基线仍受翻译轨迹随机性影响；PEGRL利用后编辑条件于固定译文的特性，构建更低方差基线。这一设计差异源于后编辑任务的条件分布更集中，其回报估计方差理论上低于翻译任务。

## 总结

PEGRL解决的核心矛盾是RL翻译训练中蒙特卡洛回报估计的高方差问题。其切入点在于利用后编辑任务条件于固定译文的低方差特性，构建更稳定的学习信号。方法上，PEGRL将后编辑建模为辅助任务，通过方差感知加权平衡两任务贡献。实验证明，Ours-8B在EN→TR COMET-KIWI上达到68.14，与DeepSeek-V3.2持平；EN→FI XCOMET上较基线提升8.06点。边界在于奖励函数依赖COMET-KIWI等特定指标，长期训练可能导致对指标过拟合而非真实质量提升。当训练步数增加时，模型是否对COMET指标产生过拟合，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_0629e962232a)