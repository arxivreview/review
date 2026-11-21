# ACL-Findings2026最新论文 ｜ReStyle-TTS: Relative and Continuous Style Control for Zero-Shot Speech Synthesis ｜解耦引导与正交融合：零样本TTS的相对风格控制

研究机构：浙江大学、厦门大学

作者：Haitao Li、Chunxiang Jin、Chenglin Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03632)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03632)

> 零样本TTS的核心困境在于，模型在克隆说话人音色的同时，不可避免地继承了参考音频中的韵律与情感风格，导致合成语音被参考音频“锁定”。现有可控TTS方法多依赖绝对文本指令或额外风格音频，缺乏对参考音频风格的相对、连续调节能力。ReStyle-TTS通过解耦分类器自由引导（Decoupled Classifier-Free Guidance, DCFG）降低参考音频依赖，结合正交LoRA融合（Orthogonal LoRA Fusion, OLoRA）实现多属性独立控制，并引入音色一致性优化（Timbre Consistency Optimization, TCO）防止音色漂移。该框架在矛盾风格场景下表现优异，但其相对控制机制在长文本一致性上的有效性尚未得到充分验证。

## 研究背景

零样本TTS系统通过短参考音频克隆说话人音色，但生成语音的韵律与情感往往与参考音频高度绑定。这种绑定源于流匹配（Flow Matching）或自回归模型在训练时将参考音频的声学特征与文本内容共同编码，导致推理时参考音频不仅提供音色先验，还强加了风格约束。分类器自由引导（Classifier-Free Guidance, CFG）是平衡条件与无条件预测的关键机制，但标准CFG将文本与参考音频的引导强度耦合，调整引导权重会同时影响文本保真度与风格依赖，无法独立调节。

早期可控TTS方法如FastSpeech2通过显式韵律特征控制，但无法实现零样本音色克隆；基于自然语言指令的方法如InstructTTS和CosyVoice虽支持零样本，但依赖绝对风格目标，且文本描述与声学实现间存在多对多映射，控制稳定性不足。IndexTTS2和Vevo通过额外风格音频实现控制，但仍需精心选择参考样本。这些方法的共同局限在于缺乏参考音频相对的连续控制能力，即无法在保留参考音色的同时，对音高、能量或情感进行增量式调节。ReStyle-TTS的切入点在于，先通过解耦引导机制削弱参考音频的风格影响，再引入显式风格控制模块，实现音色与风格的正交操纵。

## 核心方法

### 方法参照系

零样本TTS的标准流程基于流匹配模型，通过CFG平衡文本与参考音频的引导。本文问题与该流程的关键差异在于，标准CFG无法独立调节参考音频的风格影响，导致风格控制与音色克隆相互干扰。

### 解耦分类器自由引导

标准CFG中，文本与参考音频的引导强度耦合，降低参考音频权重会同时削弱文本对齐。DCFG通过分别计算仅文本条件预测 $f_{\emptyset, t}$ 与文本-参考音频条件预测 $f_{a, t}$，实现独立引导：

$$
\hat{f} = f_{\emptyset, \emptyset} + \lambda_t (f_{\emptyset, t} - f_{\emptyset, \emptyset}) + \lambda_a (f_{a, t} - f_{\emptyset, t})
$$

该公式将文本保真度与参考音频依赖解耦，$\lambda_t$ 控制文本遵循，$\lambda_a$ 控制参考音频风格影响。通过降低 $\lambda_a$ 而保持 $\lambda_t$ 不变，模型在保留文本内容的同时，减少对参考音频风格的依赖，为后续风格控制创造空间。

### 正交LoRA融合与音色一致性优化

DCFG削弱参考音频依赖后，引入风格LoRA模块控制音高、能量或情感。直接叠加多个LoRA会导致属性干扰，OLoRA通过正交投影消除干扰：

$$
\tilde{v}_i = (I - P_{-i}) v_i, \quad P_{-i} = V_{-i}(V_{-i}^+ )
$$

其中 $v_i$ 为第 $i$ 个LoRA的向量表示，$P_{-i}$ 为其余LoRA张成子空间的投影矩阵。该机制确保各LoRA在参数空间中相互正交，实现多属性独立控制。然而，降低参考音频依赖可能导致音色漂移，TCO通过优势加权回归强化音色一致性：

$$
L_{\text{total}} = w_t \cdot L_{\text{FM}}, \quad w_t = 1 + \lambda \tanh(\beta A_t)
$$

其中 $A_t = r_t - b_t$ 为说话人相似度奖励与EMA基线的差值。该机制在流匹配损失中引入音色一致性约束，无需策略梯度即可稳定训练，确保风格控制不损害音色克隆。

## 实验评估

实验在Seed-TTS test-en与VccmDataset上进行，对比CosyVoice、EmoVoice、IndexTTS2等基线。基线覆盖文本提示与音频提示控制路线，但缺失F5-TTS原生零样本克隆基线，难以区分风格控制与基础克隆性能的贡献。

| 方法 | 音高控制 (Low→High) | 能量控制 (Low→High) | 情感转移 (Happy→Angry) |
| :--- | :--- | :--- | :--- |
| CosyVoice | 74.9 | 87.5 | 65.8 |
| EmoVoice | 72.4 | 76.1 | 55.8 |
| ReStyle-TTS | **90.2** | **92.4** | **100.0** |

ReStyle-TTS在矛盾风格控制上显著优于基线，情感转移准确率从CosyVoice的65.8%提升至100.0%，验证了DCFG与OLoRA的有效性。

| 配置 | Attr Δ (rel.) | WER (%) | Spk-sv |
| :--- | :--- | :--- | :--- |
| DCFG (λ_t=2, λ_a=0.5) | 51.2% | 2.31 | 0.79 |
| w/o DCFG (λ_cfg=2) | 2.1% | 1.83 | 0.90 |
| w/o TCO | 51.0% | 2.32 | 0.71 |

消融实验显示，移除DCFG导致控制强度从51.2%骤降至2.1%，证明解耦引导是风格控制的前提；移除TCO使Spk-sv从0.79降至0.71，验证了音色一致性优化的必要性。WER从1.83%升至2.31%，表明风格控制以轻微内容失真为代价。

评估指标涵盖WER、Spk-sv与MOS-SA，但缺乏长文本一致性指标。代码未公开，仅提供项目网页，超参数如LoRA rank=32、α=64、训练时长250小时已披露，可复现性中等。

## 关联研究分析

从问题动机看，ReStyle-TTS与CosyVoice均解决零样本TTS的风格控制，但CosyVoice依赖绝对文本指令，而ReStyle-TTS实现参考音频相对的连续控制。这一差异源于任务特性：文本指令难以精确映射到声学增量，而LoRA强度可直接调节属性幅度。CosyVoice在情感转移中准确率仅65.8%，而ReStyle-TTS达100.0%，表明相对控制在矛盾风格场景下更具鲁棒性。

从方法设计看，ReStyle-TTS与F5-TTS共享流匹配骨干，但F5-TTS聚焦零样本克隆，未解决风格干扰问题。ReStyle-TTS通过DCFG改造CFG机制，借鉴图像生成LoRA正交融合思路，但TTS中参考音频的风格嵌入比图像文本提示更复杂，直接迁移LoRA需先解耦参考音频依赖。F5-TTS的WER 0.020%优于ReStyle-TTS的2.31%，但前者无法进行风格控制，后者以轻微WER损失换取可控性，体现了质量与可控性的权衡。

## 总结

ReStyle-TTS解决的核心矛盾是零样本TTS中音色克隆与风格控制的耦合。现有方法无法独立调节参考音频的风格影响，ReStyle-TTS通过DCFG解耦引导、OLoRA正交融合与TCO音色优化，实现相对连续风格控制。实验显示，其在矛盾风格场景下情感转移准确率达100.0%，Spk-sv 0.79，但WER 2.31%高于纯克隆模型。该方法的边界在于，相对控制机制在长文本中的一致性未验证，且LoRA数量增加时正交投影的计算开销与精度损失未量化。当参考音频风格与目标风格差异极大时，DCFG降低参考音频依赖是否会引入新的声学伪影，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03632)