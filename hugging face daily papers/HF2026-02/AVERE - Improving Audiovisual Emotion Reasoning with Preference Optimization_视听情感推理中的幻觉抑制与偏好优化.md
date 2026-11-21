# HuggingFace最新推荐论文 ｜AVERE: Improving Audiovisual Emotion Reasoning with Preference Optimization ｜视听情感推理中的幻觉抑制与偏好优化

研究机构：美国南加州大学

作者：Ashutosh Chaubey、Jiacheng Pang、Maksim Siniukov 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07054)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07054)

> 多模态大语言模型（MLLMs）在生成情感描述时，常因语言模型内部的文本先验产生两类错误：将无关视听线索错误关联至情感（推理错误），以及凭空捏造不存在的视听线索（感知错误）。现有情感MLLM依赖浅层指令微调，缺乏对视听线索与情感因果关系的显式约束，导致在复杂语境下可靠性不足。本文通过构建专用基准EmoReAlM量化上述错误，并提出AVEm-DPO，利用基于提示的模态偏好和文本先验去偏正则项，在零样本设置下显著降低幻觉率。该方法在抑制情感幻觉方面有效，但其对长视频及歧义情感（如厌恶）的泛化能力仍受限于训练数据的短时长与类别不平衡。

## 研究背景

MLLMs处理视听输入时，语言骨干中的文本先验会主导生成过程。当模型面对“悲伤”情感时，文本先验倾向于自动补全“哭泣”或“泪水”等高频共现线索，即使视听输入中并不存在这些线索。这种偏差导致模型在解释情感时产生感知错误，即幻觉出不存在的视听证据。同时，模型还可能将视频中存在的无关线索（如背景噪音、衣着颜色）错误地归因为情感成因，形成推理错误。这两种错误共同削弱了MLLM在情感理解任务中的可解释性与可靠性。

传统多模态情感识别方法（如TFN、MulT）聚焦于判别式分类，通过张量融合或注意力机制对齐模态特征，但无法生成基于视听线索的因果解释。随着EmotionLLaMA等情感MLLM的出现，任务范式转向生成式推理，要求模型不仅预测情感标签，还需输出支持该预测的视听证据。然而，现有情感MLLM（如EmotionLLaMA、AffectGPT）主要依赖指令微调，缺乏对“线索-情感”关联正确性的显式约束。当视听模态存在冲突或线索缺失时，模型易受文本先验驱动，产生幻觉。此外，现有评估基准多依赖外部LLM（如GPT）进行主观评分，缺乏可复现的客观指标，难以精确量化幻觉与错误关联的频率。

本文切入点在于将情感推理中的幻觉问题形式化为偏好优化任务。通过构建包含“无幻觉”、“虚假关联”和“线索幻觉”子任务的EmoReAlM基准，量化MLLM在视听情感推理中的具体失效模式。在此基础上，提出AVEm-DPO，通过构造视听输入对偏好和响应偏好，显式惩罚由文本先验驱动的幻觉响应，从而在无需外部奖励模型的情况下提升模型的情感推理可靠性。

## 核心方法

### 方法参照系

本文方法基于直接偏好优化（DPO）框架。标准DPO通过最大化偏好对（chosen, rejected）的似然比来对齐模型输出，其目标函数为：

$$ \mathcal{L}_{DPO} = -\mathbb{E}_{(x, y_w, y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)} \right) \right] $$

其中 $\pi_\theta$ 为策略模型，$\pi_{ref}$ 为参考模型，$\beta$ 为温度系数。标准DPO仅优化文本响应偏好，忽略多模态输入对响应的约束，导致模型过拟合于文本提示而忽视视听线索。

### 基于提示的模态偏好（PMP）

针对跨模态幻觉问题，本文在DPO目标中引入视听输入偏好。对于特定模态提示 $x_m$（如视觉提示），仅修改被拒绝样本中对应模态的输入 $(a_l, v_l)$，保持另一模态与正确输入 $(a_w, v_w)$ 一致。具体地，若提示 $m=V$，则 $a_l = a_w$；若 $m=A$，则 $v_l = v_w$。被拒绝的视听输入 $(a_l, v_l)$ 选取为具有不同情感标签的样本。该设计的动机在于，通过强制模型在特定模态提示下依赖该模态的正确输入，抑制其他模态无关线索对响应的干扰。PMP目标函数为：

$$ \mathcal{L}_{PMP} = -\mathbb{E}_{(a_w, v_w, a_l, v_l, x_m, y_w, y_l) \sim \mathcal{D}_{av}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|a_w, v_w, x_m)}{\pi_{ref}(y_w|a_w, v_w, x_m)} - \beta \log \frac{\pi_\theta(y_l|a_l, v_l, x_m)}{\pi_{ref}(y_l|a_l, v_l, x_m)} \right) \right] $$

此公式确保模型在响应视觉提示时，其输出更依赖于正确的视觉输入而非错误的视觉输入，从而减少跨模态幻觉。

### 情感响应偏好与文本先验去偏（ERP & TPD）

为抑制情感线索幻觉，本文构造两类被拒绝响应：$y_{l_{vr}}$（视频相关但情感关联错误）和 $y_{l_{er}}$（情感相关但线索幻觉）。在DPO损失中，对这两类被拒绝响应赋予权重 $\beta_{vr}$ 和 $\beta_{er}$（$\beta_{vr} + \beta_{er} = 1$），以强化正确线索与错误线索的对比。此外，引入文本先验去偏（TPD）正则项，惩罚仅由文本输入即可生成的响应。TPD项定义为：

$$ \mathcal{L}_{TPD} = -\gamma_{TPD} \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|a_w, v_w, x)}{\pi_{ref}(y_w|a_w, v_w, x)} - \beta \log \frac{\pi_{text}(y_w|x)}{\pi_{ref}(y_w|x)} \right) $$

其中 $\pi_{text}$ 为仅使用文本输入的参考模型，$\gamma_{TPD}$ 为超参数。该公式的物理含义是：若响应 $y_w$ 可由纯文本先验 $\pi_{text}$ 高概率生成，则其奖励被折扣，从而迫使模型依赖视听输入而非文本先验来生成响应。最终目标函数为 $\mathcal{L}_{AVEm-DPO} = \mathcal{L}_{PMP} + \mathcal{L}_{ERP} + \mathcal{L}_{TPD}$。

## 实验评估

实验在EmoReAlM（4000个MCQA样本）、DFEW、RAVDESS、MER2023和EMER上进行零样本评估。基线包括VideoLLaMA2、OLA、VITA-1.5、Qwen 2.5 Omni等开源MLLM，以及EmotionLLaMA。对比方法覆盖通用MLLM和专用情感MLLM，但未包含传统判别式SOTA（如TFN、MulT），因任务范式不同。

| 模型 | EmoReAlM Reas. Basic (Audio/Visual) | EmoReAlM Modality Agree. (F1) | EmoReAlM Stress Test (Audio/Visual F1) | DFEW UAR | EMER Clue |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen 2.5 Omni | 76.8 / 89.2 | 33.3 | 55.0 / 56.8 | 41.73 | 4.23 |
| Our base | 69.2 / 85.3 | 34.6 | 50.3 / 59.9 | 56.78 | 5.63 |
| + AVEm-DPO | 77.9 / 92.5 | 60.0 | 80.9 / 94.6 | 58.54 | 6.37 |

AVEm-DPO在EmoReAlM的Stress Test任务上取得显著提升，视觉F1从59.9%提升至94.6%，音频F1从50.3%提升至80.9%。在DFEW上，UAR从56.78%提升至58.54%。消融实验显示，移除TPD导致幻觉子任务性能大幅下降，移除PMP导致模态一致性任务性能下降。

| 方法 | Basic. | Agree. | Stress | Spur. | Hall. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Our base | 77.3 | 34.6 | 55.1 | 47.3 | 39.2 |
| + AVEm-DPO | 85.2 | 60.1 | 87.8 | 92.7 | 97.6 |
| w/o TPD | 83.8 | 58.9 | 78.8 | 88.4 | 77.8 |
| w/o PMP | 81.0 | 54.9 | 79.6 | 86.2 | 88.1 |

消融结果表明，TPD对幻觉抑制（Hall.）贡献最大，移除后Hall.从97.6%降至77.8%。PMP对模态一致性（Agree.）贡献显著，移除后Agree.从60.1%降至54.9%。设计决策验证显示，使用不同情感视频作为负样本优于随机噪声或扩散噪声，证实了情感对比的有效性。

评估边界方面，EmoReAlM基于DFEW构建，可能继承其文化偏差。视频时长限制在2-10秒，长视频情感推理未验证。模型在“厌恶”情感识别上表现不佳，归因于训练样本不足。代码和模型已开源，超参数（$\beta=0.1, \lambda_{av}=1.0, \gamma_{TPD}=0.2$）已公开，可复现性良好。

## 关联研究分析

从问题动机看，本文与EmotionLLaMA（Cheng et al., 2024）同属情感MLLM路线，但EmotionLLaMA聚焦于指令微调以提升情感识别准确率，而本文聚焦于幻觉抑制与因果归因。EmotionLLaMA未显式处理文本先验导致的线索幻觉，其评估依赖GPT-based主观评分，缺乏对幻觉频率的量化。本文通过EmoReAlM基准和AVEm-DPO，将幻觉问题转化为可优化的偏好信号，弥补了EmotionLLaMA在可解释性评估上的不足。

从方法设计看，本文与Vista-DPO（Huang et al., 2025b）同属多模态DPO分支，但Vista-DPO针对视频对象级幻觉，构造实例级、时间级和对象级偏好。本文针对情感线索幻觉，构造基于提示的模态偏好和情感响应偏好，并引入文本先验去偏。Vista-DPO未处理文本先验对情感推理的干扰，而本文通过TPD项显式惩罚纯文本响应，更贴合情感推理中“线索-情感”因果关系的约束需求。

## 总结

本文核心矛盾在于MLLM情感推理中文本先验导致的幻觉与错误关联。现有方法依赖指令微调，缺乏对视听线索因果关系的显式约束，无法在零样本设置下可靠抑制幻觉。本文通过AVEm-DPO，结合基于提示的模态偏好和文本先验去偏，在EmoReAlM Stress Test上实现视觉F1 94.6%、音频F1 80.9%的提升。其边界在于训练数据限于短视频（2-10秒）且存在类别不平衡（厌恶情感识别差），长视频及歧义情感的泛化能力未验证。当视频时长超过10秒或情感类别扩展至歧义情感时，AVEm-DPO的偏好优化是否仍能维持幻觉抑制效果，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07054)