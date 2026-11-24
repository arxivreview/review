# ICASSP2026 · 神经音频编码与压缩方向论文汇编

> 本方向共 1 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【S-PRESSO: Ultra Low Bitrate Sound Effect Compression With Diffusion Autoencoders And Offline Quantization ｜扩散自编码器超低码率音效压缩

研究机构：索尼AI

作者：Zineb Lahrichi、Gaëtan Hadjeres、Gaël Richard 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15082)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15082)

> 神经音频压缩旨在将连续波形映射为离散或连续潜变量，以在极低码率下保留感知质量。传统基于残差向量量化（Residual Vector Quantization, RVQ）的确定性编解码器在码率低于 3kbps 时，重建质量因信息瓶颈而崩塌，产生金属音或机械音伪影。S-PRESSO 利用预训练扩散模型的生成先验，将优化目标从“比特率/失真”权衡转向“比特率/声学相似度”权衡，通过离线量化与扩散解码实现 48kHz 音效在 0.096kbps 下的逼真重建。该方法在音效域突破了传统编解码器的码率极限，但其生成式特性引入了推理延迟与主观评估的不确定性，且未验证在语音等强语义任务中的适用性。

】
