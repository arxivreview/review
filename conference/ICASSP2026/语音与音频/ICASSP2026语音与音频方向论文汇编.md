# ICASSP2026 · 语音与音频方向论文汇编

> 本方向共 4 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Hyperbolic Additive Margin Softmax with Hierarchical Information for Speaker Verification ｜双曲加性边际Softmax

研究机构：清华大学

作者：Zhihua Fang、Liang He

论文原文见 [arXiv](https://arxiv.org/abs/2601.19709)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19709)

> 说话人验证（Speaker Verification, SV）的核心挑战在于如何从变长语音中提取兼具判别力与泛化性的嵌入，而现有主流方法均基于欧氏空间构建损失函数，难以充分捕捉说话人特征中固有的树状层级结构。本文指出，欧氏空间的扁平几何特性限制了嵌入对复杂声学分布的表达能力，导致类间可分性不足。为此，作者提出将嵌入投影至双曲空间，并设计基于双曲距离的Softmax变体损失，以显式建模层级信息并增强类间分离。该方法在ECAPA-TDNN骨干上验证了双曲几何的有效性，但在缺乏自监督预训练特征的条件下，其绝对性能仍显著落后于当前基于大规模预训练模型的SOTA，其价值更多体现在几何建模的理论贡献而非工程部署的领先性。

】

---

【S-PRESSO: Ultra Low Bitrate Sound Effect Compression With Diffusion Autoencoders And Offline Quantization ｜扩散自编码器超低码率音效压缩

研究机构：索尼AI

作者：Zineb Lahrichi、Gaëtan Hadjeres、Gaël Richard 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15082)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15082)

> 神经音频压缩旨在将连续波形映射为离散或连续潜变量，以在极低码率下保留感知质量。传统基于残差向量量化（Residual Vector Quantization, RVQ）的确定性编解码器在码率低于 3kbps 时，重建质量因信息瓶颈而崩塌，产生金属音或机械音伪影。S-PRESSO 利用预训练扩散模型的生成先验，将优化目标从“比特率/失真”权衡转向“比特率/声学相似度”权衡，通过离线量化与扩散解码实现 48kHz 音效在 0.096kbps 下的逼真重建。该方法在音效域突破了传统编解码器的码率极限，但其生成式特性引入了推理延迟与主观评估的不确定性，且未验证在语音等强语义任务中的适用性。

】

---

【SIRUP: A diffusion-based virtual upmixer of steering vectors for highly-directive spatialization with first-order ambisonics ｜基于潜空间扩散的导向矢量虚拟上混

研究机构：日本理化学研究所、日本京都大学

作者：Emilio Picard、Diego Di Carlo、Aditya Arie Nugraha 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.17732)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.17732)

> 声源定位（SSL）在低阶Ambisonics（FOA）系统中受限于空间分辨率，导致波束成形与角度估计精度不足。传统参数化上混方法依赖级联流程，误差在方向估计与渲染间传播，难以解耦空间细节与硬件阶数。SIRUP通过潜空间扩散模型直接从FOA导向矢量生成高阶Ambisonics（HOA）表示，实现空间超分辨率。该方法在模拟房间中显著提升了波束锐度与信干比，但推理延迟与真实场景泛化能力尚待验证。

】

---

【StereoFoley: Object-Aware Stereo Audio Generation from Video ｜对象感知立体声视频到音频生成

作者：Tornike Karchkhadze、Kuan-Lin Chen、Mojtaba Heydari 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18272)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18272)

> 视频到音频生成（Video-to-Audio, V2A）旨在从无声视频中合成语义与时间对齐的音效，但现有模型大多局限于单声道，或仅通过后期上混实现立体声，缺乏基于视频对象位置的立体声空间化能力。这一空白源于主流数据集缺乏空间可靠的立体声内容。StereoFoley 通过构建合成数据管道，将对象轨迹映射为立体声平移与响度，微调潜扩散模型实现对象感知的立体声生成。该方法在对象对齐指标上显著优于基线，但通用音频质量指标与单声道 SOTA 持平，其价值在于填补了空间一致性生成的空白，而合成数据的泛化边界尚待检验。

】
