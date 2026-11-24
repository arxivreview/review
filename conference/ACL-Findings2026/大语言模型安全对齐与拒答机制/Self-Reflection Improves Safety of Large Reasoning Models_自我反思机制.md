# ACL-Findings2026最新论文 ｜Self-Reflection Improves Safety of Large Reasoning Models ｜自我反思机制

研究机构：复旦大学、北京邮电大学

作者：Qiang Huang、Wei Zhai、Feng Huang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e10a37998c2c)

> 大型推理模型（LRMs）在长程思维链中易产生有害中间状态，而现有对齐方法仅能预防初始输出，无法干预生成过程中的风险漂移。本文提出在生成过程中插入显式反思标记，使模型在检测到有害信号时自主中断并修正，而非回退重生成。该方法通过监督微调与直接偏好优化组合训练，将有害内容率从13.8%降至4.1%，同时保持有用性。其价值在于将安全对齐从静态过滤转向动态修正，但单次反思能否覆盖长程推理中的多次漂移仍存疑。

## 研究背景

当模型面对“如何在工作场所隐藏毒品”类提示时，其思维链可能先产生“尝试藏在水瓶里”等有害推理，再在最终输出前自我纠正。这一现象揭示了浅层安全对齐（Shallow Safety Alignment）的局限：模型仅在初始token建立拒绝机制，后续生成仍受上下文诱导。为应对此问题，回退机制（Backtracking）如Reset和BSAFE被提出，它们在检测到有害内容时丢弃前文并重新生成。然而，回退机制在有害信号弥散或对抗性提示下易失效，且引入额外计算开销，导致上下文连贯性受损。

LRM的兴起使安全战场前移至思维链内部。现有SFT、RLHF和DPO等对齐技术仅能建立输入-输出映射，无法监控推理轨迹中的动态风险。本文切入点在于：既然有害内容可能在推理中不可避免，如何使模型在生成过程中实时检测并修正，而非依赖最终输出的过滤？这要求安全机制具备动态监控与自我修正能力，将安全对齐从“预防”转向“动态干预”。

## 核心方法

### 方法参照系

本文问题属于推理轨迹干预路线，与Reset/BSAFE等回退机制同属“检测-干预”范式。关键差异在于：回退机制丢弃前文重生成，而本文保留上下文，通过插入反思标记引导模型原地修正，避免计算冗余与上下文丢失。

### 反思标记与监督微调

设计动机：回退机制在有害信号弥散时易漏检，且重生成破坏上下文连贯性。本文引入约50个token的[Self-Reflection]标记，其语义为“等待”“质疑”，用于触发模型的自我怀疑-暂停-反思过程。在SFT阶段，利用安全分类器（Llama Guard 3）定位有害响应$y^-$中的有害前缀，构造训练目标：

$$
\mathcal{L}(\theta) = -\mathbb{E}_{(x,y^+,y^-)} \left[ \log p_\theta \left( \text{prefix}(y^-) \oplus [\text{Self-Reflection}] \oplus y^+ \mid x \right) \right] - \mathbb{E}_{(x,y^+)} \left[ \log p_\theta(y^+ \mid x) \right]
$$

该公式最大化“有害前缀+反思标记+安全响应”的似然，同时不最大化有害前缀本身，避免提升有害生成概率。模型学会在有害内容出现时立即插入反思标记，并自主恢复至安全生成，无需回退。

### 偏好优化与反思触发控制

设计动机：SFT仅能教会模型“何时反思”，但无法抑制在安全响应中过度反思，导致效率下降。本文构造两类偏好对：正样本对鼓励在高风险场景反思，负样本对抑制在安全场景中反思。正样本对为$\text{prefix}(y^-) \oplus [\text{Self-Reflection}] \oplus y^+ \succ y^-$，负样本对为$y^+ \succ \text{prefix}(y^+) \oplus [\text{Self-Reflection}] \oplus y$。采用直接偏好优化（DPO）训练：

$$
\mathcal{L}_{\text{SR-DPO}}(\theta) = \mathbb{E}_{(x,y^+,y^-) \sim \mathcal{D}_{\text{reflection}}} \left[ \log \sigma \left( \beta (\log \pi_\theta(y^+ \mid x) - \log \pi_\theta(y^- \mid x)) \right) \right]
$$

该公式通过温度参数$\beta$调节偏好强度，显式区分“需反思”与“无需反思”场景，防止过度反思。混合通用效用数据集与反思偏好数据集训练，确保模型在保持通用能力的同时，精准触发反思机制。

## 实验评估

实验在四个LRM（LLaMA-8B、Qwen2.5-7B、NVIDIA-9B、Qwen3-8B）上评估，基线包括SFT、Reset、BSAFE。评估指标涵盖安全性（ToxicChat、AI Safety、SafetyBench的HCR）、有用性（MATH500、LiveCodeBench、GPQA Diamond的ACC）及权衡（OR-Bench、PHTest的RR）。

| 模型 | 方法 | ToxicChat HCR | AI Safety HCR | SafetyBench HCR | OR-Bench RR | PHTest RR |
|---|---|---|---|---|---|---|
| LLaMA-8B | SFT | 23.9 | 19.9 | 23.3 | 18.8 | 21.9 |
| LLaMA-8B | Self-Reflection | 13.8 | 13.3 | 14.5 | 13.1 | 15.6 |
| Qwen3-8B | SFT+DPO | 25.7 | 21.1 | 20.9 | 17.2 | 16.9 |
| Qwen3-8B | Self-Reflection | 2.3 | 3.6 | 6.5 | 3.9 | 3.6 |

Self-Reflection在Qwen3-8B上将平均HCR从22.6%降至4.1%，降幅超80%；OR-Bench RR从17.2%降至3.9%，表明过度拒绝显著缓解。有用性指标（MATH500 ACC 62.6%、LiveCodeBench ACC 63.3%）略高于基线，说明安全提升未牺牲效用。

消融实验显示，SFT+DPO组合优于单独SFT或DPO。LLaMA-8B上，SFT+DPO的HCR为20.5%，Self-Reflection降至5.2%；Qwen3-8B上，SFT+DPO的HCR为22.6%，Self-Reflection降至4.1%。这表明反思机制的增益主要来自DPO对触发条件的精细控制，而非单纯增加训练数据。

评估边界：实验未报告JailbreakBench或HarmBench等对抗攻击基准，仅测试常规安全场景。代码未公开，超参数（如温度$\beta$、反思标记长度）未详述，可复现性受限。

## 关联研究分析

从问题动机看，本文与Fail-Closed Alignment（Coalson et al., 2026）同属鲁棒性增强路线，但路径迥异。Fail-Closed通过冗余子空间重构提升权重级鲁棒性，ASR达5.0%；本文通过行为级反思标记实现动态修正，HCR降至4.1%。差异根源在于：Fail-Closed假设安全机制需内嵌于模型架构，而本文假设安全机制可外化为生成行为。前者计算成本高但抗攻击强，后者部署轻量但依赖模型自判能力。

从方法设计看，本文与Self-Guard（Zheng et al., 2026）同属推理级干预，但干预粒度不同。Self-Guard在思维链中插入安全检查点，ASR 6.6%；本文在有害内容出现时插入反思标记，HCR 4.1%。Self-Guard的干预是周期性、预防性的，本文的干预是事件驱动、响应性的。这种差异导致Self-Guard在长程推理中可能漏检弥散风险，而本文在有害信号明确时更精准，但对模糊风险的捕获能力未验证。

## 总结

本文核心矛盾是LRM推理轨迹中的动态风险无法被静态对齐方法捕获。切入点在于将安全机制从“预防初始输出”转向“干预生成过程”，凭借显式反思标记与DPO触发控制实现动态修正。方法上，通过SFT+DPO组合训练，使模型在有害内容出现时插入[Self-Reflection]标记并自主恢复。实验证明，Qwen3-8B上HCR从22.6%降至4.1%，OR-Bench RR从17.2%降至3.9%。边界在于：实验未覆盖对抗攻击场景，且单次反思能否处理长程推理中多次出现的有害漂移未验证。当推理链长度超过1000 token时，反思标记的触发频率与有效性是否衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e10a37998c2c)