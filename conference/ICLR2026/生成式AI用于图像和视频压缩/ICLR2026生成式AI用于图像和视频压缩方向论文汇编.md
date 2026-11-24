# ICLR2026 · 生成式AI用于图像和视频压缩方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AUTOREGRESSIVE BASED PROGRESSIVE CODING FOR ULTRA-LOW BITRATE IMAGE COMPRESSION ｜基于视觉自回归模型的渐进式超低码率图像压缩

研究机构：清华大学、哈尔滨工业大学

作者：Ziyuan Zhang、Yichong Xia、Bin Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_29248137)

> 超低码率图像压缩旨在以极少的比特数重建具有真实纹理细节的图像，传统扩散模型方法因需针对每个码率单独训练且依赖共享随机数，难以适应动态传输环境。本文切入点在于利用视觉自回归模型（VAR）的粗到细生成范式，天然实现单模型多码率支持并消除对共享随机性的依赖。具体做法是将图像编码为多尺度位级残差量化流，仅传输前 $k$ 个尺度，由 VAR 自回归生成剩余尺度。该方法在渐进式压缩任务中实现了 SOTA 性能与 2~6 倍的解码加速，但其编码端概率预测开销随码率增加而显著上升，限制了其在高码率场景下的实时性。

】

---

【Turbo-DDCM: Fast and Flexible Zero-Shot Diffusion-Based Image Compression ｜零样本扩散图像压缩的加速与灵活控制

研究机构：以色列理工学院

作者：Amit Vaisman、Guy Ohayon、Hila Manor 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.06424)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.06424)

> 零样本扩散压缩旨在利用预训练模型先验在极低码率下重建图像，但现有方法因需数百步去噪导致单图处理耗时数分钟，难以实用。本文切入点在于将噪声选择从贪心迭代优化为闭式解，从而大幅减少去噪步数。通过稀疏最小二乘组合码本原子，Turbo-DDCM 将往返时间降至1.8秒，同时引入优先级感知与PSNR目标控制变体。该方法在保持与SOTA相当质量的同时实现了数量级加速，但其高码率性能受限于底层VAE的重建上限。

】

---

【When MLLMs Meet Compression Distortion: A Coding Paradigm Tailored to MLLMs ｜面向多模态大语言模型的图像压缩范式

研究机构：上海交通大学、微软研究院

作者：Jinming Liu、Zhaoyang Jia、Jiahao Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24258)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24258)

> 多模态大语言模型（MLLM）对视觉输入的高保真需求与边缘设备带宽限制存在根本冲突，传统针对人类视觉系统（HVS）优化的编码器无法维持MLLM下游任务的一致性。现有机器视觉编码方法仅关注高层语义，导致跨层级特征合成失效。本文通过系统分析MLLM视觉编码器内部信息流，提出CoTAM框架，利用CLIP浅层注意力引导码率分配，并结合多级保真度损失函数，在保持MLLM任务性能不变的前提下实现最高35.99%的码率节省。该工作填补了面向MLLM的专用压缩范式空白，但其性能边界受限于基础编码器的重建能力，且未验证在极端低码率下的语义鲁棒性。

】
