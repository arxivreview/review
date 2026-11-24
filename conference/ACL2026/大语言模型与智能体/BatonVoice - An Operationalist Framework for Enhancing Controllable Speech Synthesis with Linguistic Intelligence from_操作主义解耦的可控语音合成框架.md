# ACL2026最新论文 ｜BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs ｜操作主义解耦的可控语音合成框架

作者：Yue Wang、Ruotian Ma、Xingyu Chen 等 17 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac14ea9aa277)

> 现有基于大语言模型（LLM）的文本转语音（TTS）系统常将 LLM 仅作为生成离散语音 token 的骨干，导致其强大的指令遵循能力被低效利用，且依赖昂贵的人工标注指令-语音对。BATONVOICE 提出“操作主义”范式，将指令理解与语音生成解耦：由外部 LLM 将自然语言指令转化为显式的声学特征 JSON（如音高、能量），再由专用 TTS 模型据此合成语音。该框架以 0 小时人工标注数据实现了 57.6% 的情感准确率，但其特征集局限于静态声学参数，对动态韵律结构的捕捉能力存疑。

## 研究背景

可控 TTS 的核心挑战在于将抽象的自然语言指令（如“用讽刺的语气”）映射为具体的声学实现。传统方法依赖风格标签或参考音频，前者受限于预定义类别，后者难以实现细粒度控制。指令引导范式虽具灵活性，但需大规模人工标注的指令-语音配对数据，标注成本高且一致性差，严重制约了模型泛化能力。

当前 LLM-based TTS 主流路线（如 CosyVoice2）将 LLM 作为自回归生成器，直接输出语音 token。这种端到端架构虽简化了流程，但 LLM 的语言智能被压缩在 token 预测任务中，无法显式利用其上下文推理能力来解析复杂指令。更关键的是，指令遵循能力在训练时固化，难以通过升级 LLM 来动态提升。BATONVOICE 的切入点在于：将指令理解从 TTS 模型中剥离，交由外部 LLM 完成，生成可解释的声学特征中间表示，从而解耦“理解”与“生成”两个环节。

## 核心方法

### 方法参照系

本文问题属于指令引导 TTS，但区别于 InstructTTS 等直接微调 LLM 以关联指令与语音 token 的做法。BATONVOICE 的关键差异在于引入“声学特征 JSON”作为中间变量，将指令理解转化为特征预测任务，而非端到端的 token 生成。

### 操作主义特征解耦

设计动机：解决指令-语音配对数据标注成本高、一致性差的问题。传统方法需人工标注每条语音的情感或风格标签，而 BATONVOICE 利用 LLM 的语言智能，将指令直接解析为量化特征。具体而言，外部 LLM（如 Gemini 2.5 Pro）接收指令 $I$ 和文本 $X$，输出特征向量 $F_v$，包含音高均值/斜率、能量 RMS/斜率、频谱质心等。这一过程将抽象指令转化为可计算的声学参数，使 TTS 模型无需理解指令语义，只需执行特征到语音的映射。

### 三阶段训练与偏好优化

设计动机：解决 SFT 阶段模型易出现高 WER 和语速异常的问题。BATONTTS 采用三阶段训练：预训练建立基础 TTS 能力；SFT 阶段训练模型在特征 $F_v$ 条件下生成语音 token $S$，损失函数为：

$$
\mathcal{L}_{SFT} = -\mathbb{E}_{(x,F_v,S)\sim D_{sft}} \sum_{i=1}^{|x|+|F_v|+|S|} \log \pi_{sft}(y_i|y_{<i})
$$

该公式使模型学习从文本和特征序列自回归生成语音 token。SFT 后，模型仍可能生成低质量样本，因此引入偏好优化（PO）阶段。PO 通过自动构建偏好对：用预训练模型生成低质量样本 $S_l$（高 WER 或慢语速），用 SFT 模型生成高质量样本 $S_w$（低 WER 且正常语速），形成偏好元组 $(x, F_v, S_w, S_l)$。采用 APO-down 目标函数：

$$
\mathcal{L}_{APO} = \mathbb{E} \left[ \sigma(r_\theta(x, F_v, S_w)) - \sigma(r_\theta(x, F_v, S_w) - r_\theta(x, F_v, S_l)) \right]
$$

其中 $r_\theta$ 为奖励函数。该设计无需人工标注，仅基于 WER 和语速自动筛选，强化模型对特征 $F_v$ 的遵循精度。

## 实验评估

实验在 Seed-TTS（WER）和 Emotion 数据集（Acc）上进行，基线包括闭源 Minimax 系列和开源 CosyVoice、Spark-TTS。BATONVOICE-1.7B 在 Emotion 数据集上达到 57.6% 准确率，显著优于最强闭源基线 Minimax-2.5-HD（48.6%）和开源 CosyVoice（43.8%）。WER 为 2.5，略高于 CosyVoice2（2.1）和 Spark-TTS（1.9），但情感控制优势明显。

| 模型 | 参数量 | WER (↓) | Emotion Acc (↑) |
|---|---|---|---|
| Minimax-2.5-HD | - | 1.5 | 48.6 |
| CosyVoice | 0.3B | 3.4 | 43.8 |
| CosyVoice2 | 0.5B | 2.1 | 37.8 |
| BATONVOICE | 1.7B | 2.5 | 57.6 |

消融实验显示，SFT 阶段将情感准确率从 23.2% 提升至 52.2%（+29.0 点），APO 阶段进一步提升至 57.6%（+5.4 点）。更换外部 LLM 从 Qwen3-1.7B 到 Gemini 2.5 Pro，准确率从 29.8% 跃升至 57.6%，验证了“语言智能直接转化为合成质量”的假设。零样本跨语言测试中，BATONVOICE-1.7B 在中文情感基准上达到 56.2% 准确率，超过 CosyVoice（52.0%）和 Minimax-2.5-Turbo（50.6%），尽管后训练仅使用英文数据。

评估边界：情感准确率依赖 Gemini 2.5 Pro 作为评估器，可能存在评估器偏见；WER 略高于 SOTA，可能源于特征条件化引入的额外噪声；代码已开源，但特征提取算法细节未完全披露，可复现性需进一步验证。

## 关联研究分析

从问题动机看，BATONVOICE 与 InstructTTS 均解决指令遵循问题，但 InstructTTS 依赖人工标注指令-语音对，而 BATONVOICE 通过 LLM 生成特征规避了标注瓶颈。这一差异源于任务特性：InstructTTS 假设指令与语音存在直接映射，而 BATONVOICE 认为指令需先转化为声学参数，再由 TTS 执行。然而，特征集局限于静态参数（音高、能量、频谱质心），未涵盖动态韵律结构（如重音、停顿），这可能限制其对复杂情感指令的捕捉能力。

从方法设计看，BATONVOICE 与 MOSS-Speech 同属 LLM-based TTS，但 MOSS-Speech 采用端到端语音到语音范式，而 BATONVOICE 强调文本特征中介的可解释性。MOSS-Speech 通过层分割保留文本推理能力，但无法直接利用外部 LLM 的语言智能；BATONVOICE 通过解耦架构，使 TTS 模型性能随外部 LLM 升级而提升，无需重新训练。这种模块化设计在计算效率上更具优势，但引入了外部 LLM 的依赖，增加了推理延迟和系统复杂度。

## 总结

BATONVOICE 解决的核心矛盾是 LLM 语言智能在 TTS 中的低效利用与人工标注成本高的冲突。其切入点在于将指令理解解耦为特征预测任务，利用外部 LLM 生成显式声学特征，再由专用 TTS 模型执行合成。该方法以 0 小时人工标注数据实现了 57.6% 的情感准确率，并验证了性能随外部 LLM 能力线性提升的特性。然而，其特征集局限于静态声学参数，未涵盖动态韵律结构，且 WER 略高于 SOTA。当指令涉及复杂情感层次（如“先愤怒后平静”）时，仅靠音高和能量的均值/斜率是否足以捕捉这种动态变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ac14ea9aa277)