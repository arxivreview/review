# ICLR2026最新论文 ｜Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models ｜语言模型“Slop”抑制框架：Antislop

研究机构：美国哥伦比亚大学、美国纽约大学

作者：Samuel Paech、Allen Roush、Judah Goldfeder 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15061)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15061)

> 大语言模型（LLM）在生成文本时表现出显著的重复性语言指纹，即“Slop”，导致输出质量下降且易被识别为机器生成。现有抑制手段如Token Banning或标准DPO在消除特定模式时往往伴随严重的通用能力退化或模型崩溃。本文提出Antislop框架，结合推理时回溯采样与一种名为FTPO的偏好优化算法，旨在以最小代价消除这些过度使用的模式。该框架在保持数学推理与写作质量的同时实现了高抑制率，但其对推理吞吐量的显著损耗及未验证的跨模型泛化能力仍存疑。

## 研究背景

理解本文需厘清两个核心概念：Slop与偏好优化。Slop指LLM输出中高频重复的特定词汇或短语（如“Elara”或“voice barely above a whisper”），其频率远高于人类文本，是模型训练数据偏差与解码策略共同作用的产物。抑制Slop本质上是一个分布调整问题，需降低特定token的生成概率。直接修改概率分布通常依赖偏好优化（Preference Optimization），如直接偏好优化（DPO），它通过对比“被选”与“被拒”样本来调整模型参数。然而，DPO在处理“抑制模型最偏好token”这一极端任务时，往往需要大幅调整logit，导致模型整体分布漂移，引发通用能力退化。

LLM生成质量的提升伴随着“多样性坍缩”现象，RLHF等对齐方法进一步加剧了输出的同质化。主流抑制方案存在明显瓶颈：推理时的Token Banning虽简单，但会误伤共享前缀的合法词汇（如禁“catatonic”会连带禁“cat”开头的词）；标准DPO在训练高抑制率时，由于缺乏对非目标token的约束，导致logit发散，写作质量与词汇多样性急剧下降。本文的切入点在于将Slop抑制视为一个“外科手术式”的局部调整问题，而非全局分布重塑，通过设计专门的训练算法与推理机制，在消除特定模式的同时严格约束模型其他部分的参数变动。

## 核心方法

### 方法参照系

本文问题属于生成端主动干预，与水印技术（如KGW）同属生成阶段控制，但差异在于KGW嵌入外部统计信号用于溯源，而本文直接修改模型内部概率分布以消除特定语言模式。标准流程为基于DPO的偏好微调，但本文指出DPO在抑制“高概率token”时存在logit发散失效，故引入FTPO替代。

### Antislop Sampler：推理时回溯与软禁

传统Token Banning在首个token触发，易产生误报。Antislop Sampler在生成过程中维护token轨迹，当检测到完整违禁模式（支持正则表达式）时，回溯至该模式起始位置，降低起始token概率并重采样。其核心机制是“软禁”（Soft-banning），通过参数 $s$ 控制抑制强度：

$$ p_{new} = p_{old} \cdot 10^{-s} $$

其中 $0 \le s \le 1$。该设计解决了硬禁导致的连贯性断裂问题，允许在概率极高时保留违禁词（如用户明确要求写“tapestry”时），实现了抑制强度与生成连贯性的平衡。

### FTPO：终token偏好优化

DPO在抑制Slop时，因需大幅降低“被拒”token概率，导致非目标token概率被动上升，引发分布漂移。FTPO针对此失效，仅针对推理轨迹末尾的单个token进行偏好优化，并引入双重正则化。其损失函数包含偏好损失、目标正则化与非目标正则化：

$$ \mathcal{L} = \mathcal{L}_{pref} + \lambda_{target} \mathcal{L}_{target} + \lambda_{non-target} \mathcal{L}_{non-target} $$

其中 $\mathcal{L}_{target}$ 对“被选”与“被拒”token的logit偏差施加MSE约束，允许其自由移动；$\mathcal{L}_{non-target}$ 将剩余词汇logit锚定至参考值。这一设计动机在于隔离更新范围，防止抑制特定模式时对其他词汇概率产生“连带伤害”，从而在达到高抑制率时保持模型通用能力稳定。

## 实验评估

实验在Gemma-3-12B、Mistral-Small-3.2及Llama-3.3-70B上进行，基线包括Token Banning、标准DPO及Antislop Sampler。评估指标涵盖MMLU、GSM8K、长文写作质量、词汇多样性及Slop抑制率。

| 模型/方法 | MMLU | GSM8K | 写作质量 | 多样性 | 抑制率 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Gemma-3-12B Baseline | 0.590 | 0.888 | 67.80 | 100.00 | 0.00 |
| Gemma-3-12B FTPO 2k | 0.559 | 0.876 | 68.93 | 101.05 | 92.39 |
| Gemma-3-12B DPO 2k | 0.541 | 0.847 | 62.98 | 91.03 | 82.00 |
| Gemma-3-12B FTPO 8k | 0.592 | 0.889 | 67.49 | 95.09 | 83.40 |
| Gemma-3-12B DPO 8k | 0.571 | 0.864 | 54.61 | 73.92 | 81.44 |

FTPO在2k禁词表下实现92.39%抑制率，写作质量68.93略高于基线67.80，而DPO在同等条件下质量降至62.98。随着禁词表扩大至8k，FTPO抑制率降至83.40，但写作质量仍保持67.49，接近基线；DPO质量则大幅跌至54.61。

消融实验显示，FTPO对过训练的鲁棒性显著优于DPO。FTPO可训练至接近100%偏好准确率而质量无显著下降，DPO在40%准确率后即出现严重退化。将DPO的 $\beta$ 提升至1.0虽缓解退化，但抑制率下降15.9%。Llama-3.3-70B对偏好训练更敏感，限制LoRA仅训练lm_head后，抑制率降至66.41%，表明大模型对logit调整的敏感性更高。

评估边界方面，实验仅覆盖创意写作场景，未验证FTPO抑制后的文本在RAID等对抗检测基准下的表现。Antislop Sampler导致吞吐量下降69%-96%，限制了其实时部署。代码已开源（MIT License），但超参数配置依赖特定模型架构，跨模型迁移的通用性未充分验证。

## 关联研究分析

从问题动机看，本文与KGW水印技术同属生成端干预，但KGW旨在嵌入可验证信号以解决溯源问题，而Antislop旨在消除模型特有的语言指纹以提升输出质量。KGW依赖哈希函数划分绿/红列表，其鲁棒性受限于改写攻击；Antislop通过FTPO修改分布，理论上更抗改写，但论文未测试抑制后的文本是否仍能被现有检测器（如SENTRA）识别为机器生成。这一差异源于任务目标不同：KGW追求“可检测性”，Antislop追求“不可识别性”（即消除Slop指纹），二者在对抗检测场景下可能存在博弈关系。

从方法设计看，FTPO与DPO同属偏好优化框架，但DPO在抑制“高概率token”时因logit发散导致多样性坍缩，这一失效在Razin et al. (2024)中已被记录。FTPO通过非目标正则化解决了此问题，但其设计假设“Slop模式是局部可隔离的”。若Slop源于模型深层语义偏好而非表面token频率，FTPO的局部调整可能失效。论文未探讨Slop的语义根源，仅将其视为统计异常，这限制了方法在复杂语义重复场景下的适用性。

## 总结

本文核心矛盾在于消除LLM特有的Slop指纹与保持模型通用能力之间的冲突。现有DPO方法因logit发散导致能力退化，Token Banning则因误伤合法词汇而不可用。本文通过FTPO的局部logit调整与Antislop Sampler的回溯机制，实现了92.39%的Slop抑制率，同时写作质量68.93略高于基线。其边界在于Antislop Sampler的高计算开销（吞吐量下降69%-96%）及FTPO对大模型（Llama-3.3-70B）抑制率仅66.41%的局限性。当Slop模式由深层语义偏好而非表面token频率驱动时，FTPO的局部调整是否仍能有效抑制，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15061)