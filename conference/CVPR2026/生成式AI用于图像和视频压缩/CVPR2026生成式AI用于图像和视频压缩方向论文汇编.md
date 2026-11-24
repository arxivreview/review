# CVPR2026 · 生成式AI用于图像和视频压缩方向论文汇编

> 本方向共 5 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CADC: Content Adaptive Diffusion-Based Generative Image Compression ｜内容自适应扩散图像压缩

研究机构：香港城市大学、中国科学技术大学

作者：Xihua Sheng、Lingyu Zhu、Tianyu Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21591)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21591)

> 扩散模型在极低码率下重建图像时，常因量化策略与生成先验的错配导致纹理丢失或平滑区域失真。现有方法多采用全局固定量化步长，忽视了图像内容的空间异质性，且文本条件往往伴随比特率开销或语义缺失。本文提出CADC，通过不确定性引导的自适应量化、辅助解码器信息集中及零比特文本条件，实现量化噪声与内容复杂度的动态对齐。该方法在Kodak数据集上取得了SOTA感知质量，但其对预训练扩散模型的依赖及辅助解码器的额外计算开销，限制了其在资源受限场景下的通用性。

】

---

【CoD: A Diffusion Foundation Model for Image Compression ｜压缩导向扩散基础模型

研究机构：中国科学技术大学、微软研究院

作者：Zhaoyang Jia、Zihan Zheng、Naifu Xue 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18706)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18706)

> 生成式图像压缩旨在突破传统编码在极低码率下的像素失真瓶颈，利用生成先验重建高感知质量内容。现有主流方案依赖预训练文本到图像模型（如Stable Diffusion），但文本条件的非可微性与低效性阻碍了端到端的率失真优化，导致极低码率下性能受限。本文提出CoD，一个从头训练的压缩导向扩散基础模型，通过原生图像Token替代文本条件并引入统一训练策略，实现了压缩与生成的联合优化。CoD以极低成本（20 A100 GPU days）训练，在0.0039 bpp下显著优于基于Stable Diffusion的下游算法，但其像素空间变体的高计算开销与潜空间变体的PSNR上限仍存疑。

】

---

【Differentiable Vector Quantization for Rate-Distortion Optimization of Generative Image Compression ｜可微向量量化率失真优化

研究机构：电子科技大学

作者：Shiyin Jiang、Wei Long、Minghao Han 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10546)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10546)

> 极低码率图像压缩的核心矛盾在于，向量量化（VQ）虽能保留结构保真度，但其离散索引的不可微性阻断了率损失向编码器的梯度回传，导致表示学习与熵建模解耦。现有方法依赖标量量化（SQ）分支或启发式码本调整来间接控制码率，缺乏端到端联合优化的机制。本文提出RDVQ，通过在率估计分支引入距离感知的软松弛分布，恢复率目标到编码器的梯度通路，同时保留硬VQ用于重建与编码。该框架在轻量级架构下实现了SOTA级感知质量，但其在复杂纹理泛化性及与预训练大模型先验的对比上仍存疑。

】

---

【Generative Neural Video Compression via Video Diffusion Prior ｜基于视频扩散先验的生成式神经视频压缩

研究机构：北京大学

作者：Qi Mao、Hao Cheng、Tinghan Yang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.05016)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.05016)

> 神经视频压缩在极低码率下因像素失真优化导致纹理模糊，而现有生成式视频编码依赖图像先验，缺乏时序建模，引发严重的感知闪烁。GNVC-VD 首次引入预训练视频扩散Transformer作为原生先验，通过序列级流匹配潜变量精化，在统一编解码框架内恢复时空一致性。该方法在0.03 bpp以下实现了SOTA感知质量，但其训练式精化策略对部署灵活性的影响尚待验证。

】

---

【Ultra-Low Bitrate Perceptual Image Compression with Shallow Encoder ｜浅层编码器超低码率感知图像压缩

研究机构：中国科学技术大学、香港理工大学

作者：Tianyu Zhang、Dong Liu、Chang Wen Chen

论文原文见 [arXiv](https://arxiv.org/abs/2512.12229)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12229)

> 超低码率图像压缩旨在带宽受限场景下以极少比特重建高感知质量图像，但现有方法依赖复杂预训练编码器，导致发送端计算开销过高，无法部署于边缘设备。本文切入点在于揭示极低码率下潜变量方差随码率指数下降的特性，论证浅层编码器在信息容量上足以替代复杂网络。通过构建非对称架构，结合单步扩散解码器与双端特征蒸馏，AEIC在保持SOTA感知质量的同时实现了1080P实时编码。该工作验证了“以接收端计算换发送端带宽与算力”的可行性，但其对训练数据分布的依赖及解码端对预训练大模型的强绑定，限制了其在完全离线或异构环境下的泛化能力。

】
