# CVPR2026最新论文 ｜CineBrain: A Large-Scale Multi-Modal Audiovisual Brain Dataset for Brain-Conditioned Video Generation ｜视听同步脑信号视频重建

研究机构：复旦大学

作者：Jianxiong Gao、Yichang Liu、Baofeng Yang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bf7a7b395271)

> 现有脑解码研究多依赖单一神经模态处理纯视觉刺激，忽略了听觉对视觉感知的调制作用及 fMRI 与 EEG 在时空分辨率上的互补性。本文提出 CineBrain 数据集与 CineSync 框架，通过双 Transformer 独立编码 fMRI 与 EEG 信号，利用联合对比学习对齐语义空间，并基于扩散模型生成视频。该工作验证了多模态融合在动态视频重建中的有效性，但受限于仅 6 名被试且缺乏跨数据集泛化验证，其结论的普适性存疑。

## 研究背景

脑信号解码面临时空分辨率的固有矛盾：fMRI 提供毫米级空间定位但时间分辨率仅为秒级，而 EEG 具备毫秒级时间动态却缺乏空间特异性。单一模态难以同时捕捉视觉场景的空间结构与快速变化的时序动态，导致重建视频出现运动错位或细节模糊。此外，自然感知中听觉信号强烈调制视觉处理，但现有数据集多采用纯视觉刺激，无法反映视听整合的真实神经机制。

主流 fMRI 解码范式已确立“编码器-CLIP 对齐-扩散生成”的技术路线，但在视频重建中，时序一致性仍是瓶颈。现有视频数据集如 fMRI-Video-WebVid 仅包含单模态 fMRI 数据，且刺激类型单一。本文切入点在于构建首个同步记录 fMRI 与 EEG 的大规模视听数据集 CineBrain，并探索如何利用听觉皮层激活与 EEG 快速动态提升视觉视频重建的保真度，填补了多模态脑信号在自然视听场景下的研究空白。

## 核心方法

### 方法参照系

本文问题属于多模态脑信号视频重建，与标准 fMRI 图像解码流程的关键差异在于：输入从单一 fMRI 向量扩展为 fMRI 与 EEG 双序列，且需处理视听刺激中的跨模态交互。标准流程通常将脑信号映射至 CLIP 嵌入空间后驱动扩散模型，而本文需解决双模态特征在时空尺度上的异构融合问题。

### 双 Transformer 多模态融合编码器

针对 fMRI 与 EEG 表征差异大、早期融合易导致特征干扰的问题，本文设计 Multi-Modal Fusion Encoder (MFE)。该模块采用独立 Transformer 分别处理 fMRI 与 EEG 序列，避免共享自注意力机制对异构特征的混淆。融合阶段引入融合 MLP $\psi$ 结合潜在特征 $\mathbf{z}_f, \mathbf{z}_e$，并通过联合对比损失 $\mathcal{L}_c$ 将脑表征锚定至视觉与文本嵌入空间：

$$
\mathcal{L}_c = \mathcal{L}_{fv} + \mathcal{L}_{ft} + \mathcal{L}_{ev} + \mathcal{L}_{et} + \mathcal{L}_{fe}
$$

该设计解决了单一编码器难以同时兼顾空间细节与时间动态的失效，通过独立编码保留模态特异性，再通过对比学习实现语义对齐，确保生成内容的语义一致性。

### 神经潜空间解码器

基于 MFE 输出的融合脑表征 $\mathbf{z}_b$，本文构建 Neuro Latent Decoder (NLD)。该模块采用 LoRA 微调的 CogVideoX-5B 扩散模型，将原始文本条件替换为脑特征 $\mathbf{z}_b$，通过去噪过程生成视频。训练目标为最小化预测噪声与真实噪声的差异：

$$
\mathcal{L} = \mathbb{E}_{V, \epsilon, t} \left[ \left\| \epsilon - \epsilon_\theta (\mathbf{x}_t, \mathbf{z}_b, t) \right\|^2 \right]
$$

这一改动解决了传统扩散模型依赖文本提示导致的语义漂移问题，直接利用脑信号驱动生成，确保视频内容与神经活动严格对应，提升了重建的语义忠实度。

## 实验评估

实验在自建 CineBrain 数据集上进行，包含 6 名被试观看《生活大爆炸》的同步 fMRI 与 EEG 数据。基线包括 EEG2Video、GLFA 及 NeuroClips，但缺乏 NSD 等标准 fMRI 基准对比，限制了跨数据集可比性。主实验结果显示，CineSync 在 2-way 相似度上达到 0.909，FVD 为 52.78，显著优于单模态变体 CineSync-fMRI（0.893, 57.47）和 CineSync-EEG（0.891, 53.75），验证了多模态融合的增益。

| 方法 | 2-way↑ | 50-way↑ | FVD↓ | SSIM↑ | PSNR↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| EEG2Video | 0.786 | 0.162 | 146.23 | 0.815 | 0.134 |
| GLFA | 0.801 | 0.167 | 128.76 | 0.847 | 0.225 |
| NeuroClips | 0.816 | 0.183 | 116.36 | 0.833 | 0.142 |
| CineSync-fMRI | 0.893 | 0.307 | 57.47 | 0.926 | 0.358 |
| CineSync-EEG | 0.891 | 0.304 | 53.75 | 0.918 | 0.349 |
| CineSync | 0.909 | 0.319 | 52.78 | 0.937 | 0.398 |

消融实验表明，独立编码优于联合 Transformer，证实了模态间表征差异对早期融合的负面影响。引入听觉 ROI 后，2-way 相似度提升至 0.926，FVD 降至 44.77，证明听觉皮层激活对视觉解码具有促进作用。然而，评估协议局限于自建数据集，未报告置信区间，且缺乏跨被试泛化测试，限制了结论的外部效度。

## 关联研究分析

从问题动机看，本文与 SemVideo 同属视频重建路线，但 SemVideo 聚焦于 fMRI 单模态下的时序一致性，而本文引入 EEG 以捕捉毫秒级动态。差异根源在于任务特性：自然视听刺激中听觉对视觉的调制作用需多模态数据才能捕捉，SemVideo 未涉及此维度。从方法设计看，本文与 MindEye 系列共享 CLIP 对齐范式，但 MindEye 针对静态图像，本文扩展至视频并采用双 Transformer 处理异构模态。MindEye 未探索 EEG 的时序优势，本文通过独立编码保留 EEG 快速动态，弥补了 fMRI 时间分辨率不足的缺陷。

## 总结

本文核心矛盾在于单一神经模态无法同时满足视频重建的空间精度与时序动态需求。切入点在于构建同步 fMRI-EEG 数据集，利用模态互补性提升重建质量。方法上，通过双 Transformer 独立编码与联合对比对齐，结合扩散模型生成视频。实验证明 CineSync 在 2-way 相似度上达 0.909，FVD 52.78，优于单模态基线。边界在于仅 6 名被试且缺乏跨数据集验证，听觉 ROI 的增益是否源于数据量增加而非模态互补，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_bf7a7b395271)