# HuggingFace最新推荐论文 ｜LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training ｜大规模开放视频数据集构建与多模态预训练验证

研究机构：德国图宾根大学、德国慕尼黑工业大学

论文原文见 [arXiv](https://arxiv.org/abs/2608.24845)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.24845)

> 视频-语言模型的性能上限长期受限于高质量配对数据的稀缺，现有开源视频数据集规模远小于图像-文本语料，且商业平台访问限制阻碍了大规模采集。LAION-BVD 通过自动化流水线从 CommonCrawl 提取并处理 1000 万小时视频，生成视频、音频及帧级合成标注，旨在填补开放多模态预训练数据的空白。该工作验证了低过滤策略下数据规模对模型性能的线性增益，但其合成标注的噪声影响及与专有模型的性能差距仍存疑。

## 研究背景

多模态基础模型的训练依赖于大规模配对数据，其中图像-文本数据已发展至数十亿对规模，而视频-文本数据因时序冗余与标注成本高昂，最大公开数据集 InternVid 仅含 700 万视频。这种数据规模的不对称导致视频模型在零样本迁移与长视频理解上表现受限，核心瓶颈并非视频本身的可获取性，而是处理海量视频所需的计算、存储与工程努力。

主流路线依赖人工标注或基于 ASR/字幕的弱监督，但前者成本极高，后者存在时序错位与语义缺失。LAION-BVD 的切入点在于利用合成标注替代人工标注，通过场景检测与多模态独立 caption 生成，构建一个规模远超现有数据集的开放资源。其核心假设是：在足够大的数据规模下，合成标注的噪声可通过模型容量与训练步数被稀释，从而逼近人工标注数据集的性能上限。

## 核心方法

### 数据策展与场景分割

LAION-BVD 从 CommonCrawl WAT 文件中提取 1.3B 平台特定视频 URL，筛选 YouTube、Vimeo 和 Dailymotion 链接后，通过分布式下载获取 80M 视频（10M 小时）。针对视频时序冗余问题，采用 PySceneDetect 进行内容感知场景检测，阈值设为 30，将视频分割为场景级片段。随后，通过低分辨率帧间运动估计剔除静态片段，确保每个 clip 包含有意义的视觉变化。这一设计解决了传统随机采样导致的时序信息泄露与语义错位问题，为后续多模态标注提供了结构化的输入单元。

### 多模态合成标注流水线

标注阶段针对视频、音频、帧三模态独立生成 caption。视频 caption 使用 Qwen3-VL-2B-Instruct，对每个 clip 均匀采样最多 32 帧，提示词为“Describe the video in 20 words or less”；音频 caption 使用 Audio Flamingo 3，提示词为“Describe the audio sounds in 10 words or less”；帧 caption 使用 DeepSeek-VL2-tiny 重新标注场景变化帧。这种模态解耦的标注策略避免了单一模型在多模态任务上的性能瓶颈，确保了各模态数据的独立可用性。

$$
\text{Caption}_v = \text{Qwen3-VL}(\{f_i\}_{i=1}^{32}, \text{"Describe the video in 20 words or less"})
$$

该公式表明视频 caption 生成依赖于均匀采样的帧序列与固定提示词，其质量上限受限于 Qwen3-VL 的视觉理解能力与提示词的约束力。

$$
\text{Caption}_a = \text{AudioFlamingo3}(\text{audio\_segment}, \text{"Describe the audio sounds in 10 words or less"})
$$

音频 caption 生成独立于视觉流，确保音频-文本对齐不受视觉噪声干扰，为 CLAP 模型训练提供纯净的监督信号。

## 实验评估

实验在 Kinetics-400、UCF-101、HMDB51、MSR-VTT、MSVD 等基准上评估 ViCLIP，在 UrbanSound8K、AudioCaps、Clotho 上评估 CLAP。基线覆盖 InternVid、DataComp-1B、LAION-Audio，但缺失 CLIP4Clip 等经典视频对比学习基线，限制了与早期方法的直接对比。

| 模型 | 数据集 | 样本数 | K400 Top-1 | MSR-VTT T2V | MSR-VTT V2T | Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ViCLIP L-14 | BVD-V-55M | 10M | 63.3 | 43.6 | 44.3 | 61.9 |
| ViCLIP L-14 | BVD-V-55M | 50M | 63.3 | 42.7 | 43.0 | 62.0 |
| ViCLIP L-14 | InternVid-10M-FLT | 10M | 61.8 | 38.7 | 39.8 | 58.0 |

BVD-V-55M 在 50M 样本下平均性能 62.0，较 InternVid-10M-FLT 的 58.0 提升 4.0 个百分点，验证了数据规模增益。WiSE-FT 检查点合并进一步将 BVD-V-50M 平均性能提升至 62.6，表明模型集成可部分弥补合成标注的噪声。

| 模型 | 参数 | 样本数 | BVD-A-1.7M | BVD-A-10M | LA+AS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HTSAT-base-Roberta-base | 200M | 27.1M | 62.0 | 64.1 | 64.1 |
| HTSAT-base-Roberta-large | 431M | 28.2M | 62.3 | 65.7 | 65.7 |

BVD-A-10M 在 200M 参数下平均性能 64.1，与 LA+AS 持平，表明大规模视频音频数据可替代专用音频数据集。然而，BVD-A-1.7M 性能（62.0）低于 LA+AS（64.1），显示小样本下合成音频标注的噪声影响显著。

评估边界方面，论文未报告置信区间，且合成 caption 的幻觉率未量化。可复现性上，数据与 URL 已发布至 HuggingFace，但原始视频下载需接受使用条款，限制了完全复现。

## 关联研究分析

从数据策展角度看，LAION-BVD 与 InternVid 的核心差异在于过滤策略。InternVid 采用严格过滤以提升数据质量，而 LAION-BVD 采用“minimal filtering”以最大化规模。实验显示，BVD-V-55M 在相同 ViCLIP 架构下性能优于 InternVid-10M-FLT，暗示在大规模预训练中，数据规模可能比数据质量更具决定性。然而，这一结论依赖于 ViCLIP 的特定架构，若采用更复杂的视频-语言模型，合成标注的噪声是否会被放大，论文未给出回答。

从多模态融合角度看，LAION-BVD 将视频、音频、帧作为独立数据源，而非联合建模。这与 UniMVU 等动态门控方法不同，后者强调模态权重随查询调整。LAION-BVD 的模态解耦设计简化了数据流水线，但可能丢失跨模态的时序对齐信息。例如，视频 caption 与音频 caption 独立生成，未强制两者在语义上对齐，这可能导致多模态模型在需要音视频协同推理的任务上性能受限。

## 总结

LAION-BVD 旨在解决开放视频-语言预训练数据规模不足的问题，通过自动化流水线构建 1000 万小时视频数据集，并验证其在 ViCLIP 与 CLAP 上的有效性。实验表明，BVD-V-55M 在 50M 样本下平均性能 62.0，较 InternVid-10M-FLT 提升 4.0 个百分点，证明数据规模增益。然而，其合成标注的噪声影响未量化，且与专有模型的性能差距显著。当支持集增大到 50M 样本时，合成 caption 的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.24845)