# ACL-Findings2026最新论文 ｜J-Shuwa: A Large-Scale Web-Collected Japanese Sign Language-Japanese Parallel Corpus ｜J-Shuwa：基于硬字幕挖掘的日本手语大规模平行语料库构建

研究机构：日本东京大学、日本理化学研究所

作者：Junwen Mo、MinhDuc Vo、Noriki Nishida 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_988542e485aa)

> 日本手语（Japanese Sign Language, JSL）研究长期受限于高质量平行语料库的缺失，现有资源规模远不足以支撑鲁棒模型训练。主流Web采集路线依赖闭合字幕（Closed Captions, CCs），但忽略了大量含硬编码字幕（Hard-coded Subtitles, HardSubs）的视频，导致数据源被人为截断。本文通过构建端到端字幕-手语共现检测模型与大型视觉语言模型（Large Vision Language Model, LVLM）OCR流水线，从YouTube挖掘出19.7万句JSL-日语平行数据，填补了JSL数据资源空白。其价值在于将JSL可用数据从62小时扩至300小时，但硬字幕提取的噪声控制与跨签名者泛化能力仍存疑。

## 研究背景

手语翻译（Sign Language Translation, SLT）的核心挑战在于视觉手势模态与线性文本模态间的语义鸿沟，而数据稀缺是制约该领域发展的首要瓶颈。高质量连续手语数据集的规模远小于口语数据，且传统Gloss标注需专家参与，成本高昂。为突破此限制，研究者转向从YouTube等公开平台采集大规模无标注视频，如YouTube-ASL（Uthus et al., 2023）和YouTube-SL-25（Tanzer and Zhang, 2025）。然而，这些工作主要依赖CCs，即通过视频元数据直接获取的时间对齐文本。对于JSL，YouTube-SL-25仅包含62小时CCs内容，且大量适合构建平行语料库的视频采用HardSubs——字幕直接嵌入视频帧，无法通过元数据提取。HardSubs的识别与文本提取面临空间位置多变、字体风格多样及日语特有竖排文字等挑战，导致其在先前工作中被系统性忽略。

JSL作为低资源手语，其研究活跃度远低于ASL或DGS，根本原因在于缺乏足够规模且公开可用的训练数据。现有JSL语料库如JSL Colloquial Corpus和KoSign虽提供精细标注，但规模有限，不适合作为模型训练集。本文的切入点在于利用HardSubs视频这一被忽视的数据源，通过自动化流水线将其转化为高质量平行语料库，从而实质性扩大JSL研究的数据基础。

## 核心方法

### 方法参照系

本文问题属于Web采集语料库构建范畴，标准流程为视频采集、动作识别粗筛、字幕定位与文本提取。本文的关键差异在于处理HardSubs视频，需解决字幕空间位置不确定性与手语-字幕共现验证问题，而非直接读取元数据。

### 字幕-手语共现段检测

传统VideoSubFinder需手动指定字幕区域且无法验证手语共现，导致混合内容视频处理失败。本文将该任务建模为帧级序列标注问题，采用BIO标签方案：O表示无字幕或手语的帧，B表示字幕与手语共现段的起始，I表示该段的延续。模型架构采用SigLIP2进行帧级特征提取，双向Mamba骨干网络建模长程时间依赖。训练采用两阶段策略：先在含噪声的原始分割结果上预训练，再在人工校正的干净子集上微调。该设计解决了VideoSubFinder在字幕方向变化及混合内容场景下的失效问题，实现了端到端的字幕-手语共现段自动识别。

$$
\hat{y}_t = \text{Mamba}(\text{SigLIP2}(v_t), \text{SigLIP2}(v_{t-1}), \text{SigLIP2}(v_{t+1}))
$$

其中 $v_t$ 为第 $t$ 帧，$\hat{y}_t$ 为BIO标签预测。该公式表明模型通过融合当前帧及相邻帧的视觉特征，利用Mamba的线性复杂度优势捕捉长程上下文，以判断当前帧是否处于字幕与手语共现段内。

### LVLM辅助字幕提取

传统OCR系统如PaddleOCR常将单句分割为多片段，且对复杂布局鲁棒性差，导致后处理不稳定。本文采用Qwen3-VL-32B-Thinking作为指令式OCR引擎，提示其仅提取可见字幕文本、忽略振假名（Furigana）标注，并严格输出JSON格式。该设计解决了传统OCR在日语竖排文字及水印干扰下的提取错误问题，通过LVLM的语义理解能力提升文本完整性与准确性，为后续语料库构建提供高质量文本对齐。

## 实验评估

实验在J-Shuwa验证集（2,309句）和JSL Dialogue Corpus（JDC，550测试段）上进行，基线包括mT5-base、Qwen3-1.7B和Qwen3-4B。对比方法未涵盖领域内SLT SOTA模型如Sign2GPT，但作为数据效用验证，其重点在于不同训练配置下的性能差异。

| 模型 | 训练集 | LoRA模块 | BLEU-1 | BLEU-4 | BLEURT |
|---|---|---|---|---|---|
| Qwen3-1.7B | JSW | ALL | 30.64 | 10.37 | 35.09 |
| Qwen3-1.7B | JSW + YASL | ALL | 33.31 | 12.02 | 39.91 |
| Qwen3-4B | JSW + YASL | ALL | 34.41 | 12.58 | 42.08 |
| mT5-base | JSW + YASL | - | 29.61 | 9.68 | 35.10 |

在J-Shuwa验证集上，Qwen3-1.7B联合训练JSW与YouTube-ASL（YASL）后，BLEU-4从10.37提升至12.02，BLEURT从35.09提升至39.91，验证了跨语言迁移的有效性。Qwen3模型在LoRA配置下全面优于mT5全量微调，表明解码器架构的语义生成能力对手语翻译至关重要。

| 训练集 | JDC Front∪Side BLEU-1 (FT) | JDC Front∪Side BLEURT (FT) |
|---|---|---|
| JSW | 18.66±0.23 | 22.63±0.35 |
| JSW + YASL | 21.62±0.63 | 27.22±0.58 |
| YSL25-JSL | 16.15±0.41 | 19.54±0.33 |

在JDC零样本评估中，JSW+YASL联合训练模型的BLEU-1为7.64，低于JSW单独训练的10.23，但BLEURT更高（19.05 vs 16.13），表明跨语言迁移提升了语义一致性但牺牲了表面重叠度。微调后，JSW+YASL模型在JDC上取得21.62的BLEU-1和27.22的BLEURT，显著优于YSL25-JSL基线（16.15/19.54），证明J-Shuwa语料库对JSL SLT模型训练具有实质效用。

评估协议存在局限：JDC测试集是否包含训练集未见的签名者未明确说明，可能高估模型鲁棒性。指标仅使用BLEU和BLEURT，缺乏针对手语空间结构的专用评估。代码已开源，但HardSub视频的人工审核流程未完全自动化，可复现性受限于原始视频获取。

## 关联研究分析

从数据源挖掘策略看，本文与YouTube-ASL（Uthus et al., 2023）同属Web采集路线，但后者仅处理CCs视频，而本文通过HardSubs挖掘将JSL数据规模扩大近5倍。这一差异源于JSL视频生态中HardSubs占比高，若沿用CCs-only策略将导致数据源严重不足。本文引入的SigLIP2+Mamba检测模型解决了HardSubs空间位置不确定性问题，这是CCs处理流程中不存在的挑战。

从模型适配策略看，本文与SignLlama（Gan et al., 2026）均使用Qwen3系列LLM，但SignLlama聚焦于视觉特征优先的掩码机制以增强空间语义理解，而本文仅采用LoRA微调，未针对手语空间结构进行特殊设计。本文实验显示LoRA配置中适配所有MLP模块优于仅适配注意力模块，暗示手语作为新颖知识需更新更多参数，这与SignLlama中视觉-文本交互优化的动机一致，但本文未探索视觉特征与文本特征的细粒度对齐机制。

## 总结

本文要解决的核心矛盾是JSL数据规模不足与HardSubs视频利用困难之间的冲突。现有Web采集路线依赖CCs，忽略了HardSubs这一重要数据源，而传统OCR和分割工具无法有效处理HardSubs的空间变异性。本文通过构建端到端字幕-手语共现检测模型与LVLM OCR流水线，实现了HardSubs视频的自动化处理，构建了19.7万句JSL-日语平行语料库。实验证明该语料库在JDC上使Qwen3-1.7B模型的BLEU-1从16.15提升至21.62，验证了数据规模对SLT性能的贡献。本文的边界在于HardSubs提取仍依赖人工审核，且JDC评估未明确签名者独立性。当训练数据中HardSubs占比超过50%时，模型对字幕噪声的鲁棒性是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_988542e485aa)