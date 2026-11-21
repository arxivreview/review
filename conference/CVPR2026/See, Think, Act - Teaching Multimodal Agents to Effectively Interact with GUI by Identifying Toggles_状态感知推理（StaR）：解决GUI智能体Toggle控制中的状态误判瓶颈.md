# CVPR2026最新论文 ｜See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles ｜状态感知推理（StaR）：解决GUI智能体Toggle控制中的状态误判瓶颈

研究机构：上海交通大学、北京理工大学

作者：Zongru Wu、Rui Mao、Zhiyuan Tian 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.13615)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13615)

> 图形用户界面（GUI）智能体在操作二值开关（Toggle）时，常因无法准确感知当前状态而执行错误动作，导致任务失败。现有基于提示工程或多智能体协作的方法未能根本解决这一推理缺陷，本文切入点在于将“状态感知”显式嵌入单智能体的推理链。StaR通过监督微调（SFT）训练模型执行“感知-分析-决策”三步逻辑，在Toggle基准上提升准确率超30%，并验证了其在通用任务上的迁移性，但其对动态环境状态漂移的鲁棒性仍存疑。

## 研究背景

GUI智能体依赖多模态大语言模型（MLLM）通过截图理解界面并执行操作。在移动设备设置、智能家居等场景中，Toggle（如开关、复选框）是基础交互元素，其操作逻辑依赖于对“当前状态”与“目标状态”的比对。然而，MLLM在处理此类二值状态指令时，往往缺乏对界面细微视觉特征（如开关颜色、位置）的精确感知能力，导致推理链中出现状态误判。这种误判直接引发两类典型错误：假阴性（当前状态与目标不同，但模型未执行点击）和假阳性（当前状态与目标相同，但模型仍执行点击）。

主流GUI智能体路线分为基于闭源MLLM的提示工程框架与基于开源MLLM的微调模型。前者如AppAgent系列，依赖外部工具或提示词引导，但提示工程无法根本增强模型对Toggle状态的内在推理能力；后者如UI-TARS、OS-Atlas，虽通过大规模监督微调提升了通用交互能力，但在细粒度Toggle控制上仍表现不佳。现有研究多关注长程任务规划或通用定位精度，忽视了Toggle这一高频且对状态感知要求极高的子任务。本文指出，现有智能体在Toggle执行准确率上普遍低于50%，且存在强烈的“点击偏好”（即倾向于预测CLICK而非COMPLETED），这揭示了MLLM在二值状态决策上的系统性推理缺陷。

## 核心方法

### 方法参照系

本文问题属于GUI智能体中的细粒度动作执行子任务。通用GUI智能体流程为“截图输入→意图理解→动作预测”，但Toggle控制要求模型在动作预测前必须完成“状态比对”这一中间步骤。与通用定位任务不同，Toggle任务的正确性不仅取决于坐标定位，更取决于对当前状态$\sigma$和目标状态$\sigma_u$的逻辑比对。本文的关键差异在于将隐式的状态比对显式化为推理链的强制环节。

### 显式状态感知推理链

StaR的核心创新在于重构推理链，强制模型执行三步逻辑：感知（Perceiving）、分析（Analyzing）、决策（Deciding）。设计动机在于解决现有模型因缺乏显式状态比对而导致的“过度执行”或“遗漏执行”。StaR引导模型首先从截图中识别当前Toggle状态$\sigma$（0或1），然后从指令中推断目标状态$\sigma_u$，最后基于比对结果决定动作。该过程可形式化为：

$$
a = \begin{cases}
\text{CLICK}(b) & \text{if } \sigma \neq \sigma_u \\
\text{COMPLETED} & \text{if } \sigma = \sigma_u
\end{cases}
$$

其中$b$为Toggle边界框。这一公式明确了动作决策依赖于状态差异，而非简单的指令关键词匹配。通过SFT训练，模型学习将视觉特征映射为状态标签，并将状态标签映射为动作，从而消除对额外标注器（Annotator）的依赖。

### 数据合成与训练策略

为训练StaR，本文构建了State Control Benchmark。设计动机在于现有数据集缺乏精确的Toggle状态标注，导致模型无法学习状态比对逻辑。数据合成采用“双标注器一致性”策略：使用Qwen-2-VL-72B和GLM-4V独立标注Toggle状态与功能，仅保留两者一致的样本。对于每个标注样本$\langle s, b, \sigma, f \rangle$，扩展为两条相反指令的样本：

$$
\{ \langle s, b, u_p, a_p \rangle, \langle s, b, u_n, a_n \rangle \}
$$

其中$u_p$为“关闭$f$”（若$\sigma=1$则需CLICK），$u_n$为“开启$f$”（若$\sigma=1$则需COMPLETED）。这种对称扩展确保模型在训练中正负样本平衡，避免偏置。训练时，StaR不仅使用State Control Benchmark，还混合了通用GUI基准数据，以保留模型在非Toggle任务上的原有能力，实现“Toggle精度提升”与“通用性能保持”的平衡。

## 实验评估

实验在State Control Benchmark及AndroidControl、AITZ、GUI-Odyssey等通用基准上进行。基线覆盖闭源MLLM（GPT-5, GPT-4o, Gemini 2.5 Pro）和开源MLLM（Qwen-2-VL-72B, UI-TARS-7B, OS-Atlas-7B, AgentCPM-GUI-8B, GUI-Owl-7B）。闭源模型在Toggle任务上表现极差，O-AMR（整体动作匹配率）均低于40%，主要受限于定位精度。开源模型中，Qwen-2-VL-72B因规模较大，O-AMR达66.42%，但小模型如OS-Atlas-7B仅67.16%（O-TMR）且O-AMR仅43.95%，显示其推理能力不足。

StaR训练后，各开源模型在State Control Benchmark上显著提升。OS-Atlas-7B的O-AMR从43.95%提升至79.72%，提升35.77个百分点；UI-TARS-7B从47.45%提升至77.86%，提升30.41个百分点。负指令准确率（N-AMR）提升尤为显著，OS-Atlas-7B从35.80%提升至96.48%，表明StaR有效抑制了假阳性错误。在通用任务上，StaR在GUI-Odyssey上提升TSR（任务成功率）7.14%-20.17%，在AndroidControl-High上保持或提升性能，验证了状态感知推理的泛化性。

| 模型 | O-AMR (Zero-shot) | O-AMR (w/ StaR) | 提升幅度 | N-AMR (Zero-shot) | N-AMR (w/ StaR) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OS-Atlas-7B | 43.95 | 79.72 | +35.77 | 35.80 | 96.48 |
| UI-TARS-7B | 47.45 | 77.86 | +30.41 | 39.96 | 96.53 |
| AgentCPM-GUI-8B | 64.08 | 79.00 | +14.92 | 68.11 | 97.46 |
| GUI-Owl-7B | 53.57 | 77.60 | +24.03 | 58.16 | 96.33 |

消融实验显示，StaR-style Prompting（仅提示模型关注状态）效果有限，OS-Atlas-7B的O-AMR仅从43.95%提升至50.07%，远低于StaR训练的79.72%。这表明提示工程无法替代显式训练，模型需通过SFT内化状态比对逻辑。动态环境评估中，OS-Atlas-7B的任务成功率从10%提升至55%，UI-TARS-7B从35.7%提升至40.8%，AgentCPM-GUI-8B从20.4%提升至42.58%，证明StaR在真实动态场景中的适用性。

评估边界方面，State Control Benchmark基于公开数据集合成，可能未覆盖所有Toggle类型（如滑块、下拉框）。动态环境评估仅使用20个任务，样本量较小，统计显著性有限。代码已开源，但训练超参数（如学习率$5 \times 10^{-6}$，3 epochs）未详细讨论对不同骨干模型的敏感性。

## 关联研究分析

从问题动机看，本文与Mobile-Agent-v2等多智能体框架形成对比。Mobile-Agent-v2通过引入记忆模块和协作智能体解决长程任务中的上下文丢失问题，但本文指出，对于Toggle这类细粒度状态决策，多智能体协作存在“标注器悖论”：若标注器能准确识别状态，则其本身可作为执行智能体，协作反而增加延迟。StaR通过单智能体显式推理替代外部标注，证明了内在推理能力优于外部协作。这一差异源于任务特性：Toggle决策依赖即时视觉感知，而非长程记忆，因此单智能体的高效推理更具优势。

从方法设计看，本文与UI-TARS、OS-Atlas等SFT方法同属“原生模型驱动”路线，但StaR引入了“状态感知”作为推理链的强制中间步骤。UI-TARS等模型通过大规模SFT提升通用定位精度，但未显式建模状态比对逻辑，导致在Toggle任务上出现偏置。StaR通过数据合成（对称扩展）和推理链重构，将隐式逻辑显式化，解决了SFT模型在二值状态决策上的盲区。与强化学习（RL）路线相比，StaR未使用RL，而是依赖SFT训练推理链。RL在动态环境中可能更优，但StaR证明了在静态或半动态Toggle任务中，SFT足以解决状态误判问题，且训练成本更低。

## 总结

本文核心矛盾在于GUI智能体在Toggle控制中因状态感知缺失导致的执行错误。现有提示工程和多智能体方法未能解决这一内在推理缺陷，StaR通过将“感知-分析-决策”显式嵌入推理链，并采用对称数据合成进行SFT，实现了Toggle准确率的显著提升。实验证明，StaR在State Control Benchmark上提升O-AMR超30%，并在通用任务上保持性能，验证了显式状态推理的有效性。然而，本文边界在于动态环境评估样本量小，且未探讨StaR在未见过的Toggle类型（如多值滑块）上的泛化能力。当Toggle状态随时间动态变化（如倒计时开关）时，StaR的静态状态感知是否仍能保持鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13615)