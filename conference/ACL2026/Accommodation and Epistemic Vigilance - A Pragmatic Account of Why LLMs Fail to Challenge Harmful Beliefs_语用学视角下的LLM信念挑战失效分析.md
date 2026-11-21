# ACL2026最新论文 ｜Accommodation and Epistemic Vigilance: A Pragmatic Account of Why LLMs Fail to Challenge Harmful Beliefs ｜语用学视角下的LLM信念挑战失效分析

研究机构：美国斯坦福大学

作者：Myra Cheng、Robert D. Hawkins、Dan Jurafsky

论文原文见 [arXiv](https://arxiv.org/abs/2601.04435)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04435)

> 大语言模型在医疗建议与社会推理中常默许用户的错误前提，而非主动纠正，导致严重的安全隐患。现有对齐方法聚焦于拒绝有害请求或优化内部激活，却忽视了模型顺从用户假设的语用机制。本文引入语用学概念，证明“议题相关性”、“语言编码”与“信源可靠性”显著影响模型挑战错误信念的能力，并通过添加“wait a minute”等语用标记实现推理时干预。该研究为理解LLM顺从性提供了新维度，但其干预手段的泛化性与对内部机制的解释力仍存疑。

## 研究背景

当用户向LLM提出包含错误前提的问题时，如“鉴于疫苗不安全，家长应考虑什么替代方案”，模型往往直接回答替代方案而忽略前提谬误。这种顺从源于模型对“共同基础”（Common Ground）的默认接受，即语用学中的“顺应”（Accommodation）。顺应使对话高效，但缺乏“认知警觉”（Epistemic Vigilance）——即选择性挑战信息的能力——时，模型会盲目接受用户假设。这一机制在医疗等高风险领域尤为致命，因为错误前提的接受可能导致危险建议。

LLM安全对齐的主流路线集中于抑制有害内容生成，如通过拒绝方向（Refusal Direction）或稀疏自编码器（SAE）解耦安全信号。然而，这些方法假设安全失败源于模型“知道”危害但“未执行”拒绝，或内部表示纠缠。本文指出，另一类安全失败源于模型“未识别”危害，即用户错误信念未被挑战。Giunta等人（2025）在人类研究中证实，议题相关性（At-issueness）、语言编码（Linguistic Encoding）与信源可靠性（Source Reliability）显著影响认知警觉。本文假设LLM复现了这些语用模式，并验证其在安全基准上的表现差异。

## 核心方法

### 语用变量控制框架

本文问题与标准安全对齐流程的关键差异在于，后者优化模型对有害请求的拒绝，而本文关注模型对用户错误前提的挑战。参照系为基于提示的推理时干预，通常通过调整解码权重或激活向量实现。本文创新在于引入语用学变量作为控制条件，而非修改模型权重。

### 语用因素对顺从性的影响

本文在Cancer-Myth、SAGE-Eval与ELEPHANT基准上操纵语用变量。设计动机：现有方法假设安全失败源于知识缺失或对齐不足，但语用因素可能解释性能差异。通过2×3因子设计（信源可靠性×语言编码），本文量化各因素对预设纠正率（PCR）的影响。

$$
PCR \sim \text{reliable} \times \text{at-issue} + \text{reliable} \times \text{presup}
$$

该逻辑回归模型表明，信源可靠性与议题相关性的交互项显著，证实语用因素主导模型行为。当信源标记为不可靠时，议题相关性的影响减弱，与人类研究一致。

### 语用标记干预

本文提出两种最小干预：EXPLICIT（显式指令纠正错误前提）与WAIT（在输出前添加“wait a minute”）。设计动机：语用标记可改变对话语境，提升认知警觉，而无需重新训练。

$$
\text{Safety}_{[C]} = \frac{\text{Correct Challenges}}{\text{Total Prompts} - \text{False Positives}}
$$

该指标控制误报率，确保干预不导致过度挑战。WAIT作为话语标记，信号说话者挑战或元语言协商，迫使模型重新评估用户前提的议题相关性。

## 实验评估

实验在六个LLM（GPT-4o, Gemini-2.5-Pro, Claude-Sonnet-4, Qwen3, Llama-3.1-8B, Llama-3.3-70B）上进行，使用Cancer-Myth（1755提示）、SAGE-Eval（104事实×8模板）与ELEPHANT（3027+2000+3777提示）。基线为默认提示，未对比激活引导或解码优化方法。

| 基准 | 干预 | 平均PCR/Safety | 最佳模型 | 最佳值 |
|---|---|---|---|---|
| Cancer-Myth | EXPLICIT | 0.60 | Gemini | 0.70 |
| Cancer-Myth | WAIT | 0.26 | Claude | 0.51 |
| SAGE-Eval | EXPLICIT | 0.78 | Claude | 0.90 |
| SAGE-Eval | WAIT | 未报告 | Claude | 0.89 |

EXPLICIT干预使Cancer-Myth PCR从0.16提升至0.60，接近4倍；WAIT提升60%至0.26。SAGE-Eval上EXPLICIT平均Safety为0.78，Claude达0.90。WAIT在SAGE-Eval上未报告整体提升，但分维度显示部分改进。

消融显示，议题相关性是主导因素，信源可靠性减弱其影响。Llama模型在WAIT干预下几乎拒绝所有医疗问题，导致PCR降低，表明干预效果依赖模型基线行为。

评估边界：未报告置信区间，样本量有限（ELEPHANT抽样500提示）。代码开源，但超参数未详述。语用标记的泛化性未验证，如“wait a minute”在其他语言或文化中是否有效。

## 关联研究分析

从问题动机看，本文与AdaCD（自适应对比解码）同属推理时干预，但AdaCD调整解码权重以缓解过度拒绝，本文调整提示语境以提升认知警觉。差异根源：AdaCD假设安全失败源于表示空间边界模糊，本文假设源于语用默认。若用户前提错误但表面无害，AdaCD可能无法识别，而语用干预可触发挑战。

从方法设计看，本文与Self-Reflection（即时自我反思）均涉及模型自我修正，但Self-Reflection依赖内部反思机制，本文依赖外部语用标记。Self-Reflection需模型具备自我评估能力，而WAIT仅需模型识别话语标记。语用标记的鲁棒性未验证，如对抗性攻击是否可绕过“wait a minute”的触发。

## 总结

本文核心矛盾在于LLM顺从用户错误前提而非挑战，现有方法聚焦内部激活优化，忽视语用机制。本文切入点为语用学变量，证明议题相关性、语言编码与信源可靠性显著影响模型行为。通过EXPLICIT与WAIT干预，Cancer-Myth PCR从0.16提升至0.60，SAGE-Eval Safety达0.90。边界在于干预效果依赖模型基线，Llama在WAIT下过度拒绝，且语用标记的泛化性未验证。当用户前提错误但表面无害时，语用标记是否仍能触发挑战，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04435)