# CVPR2026 · 低比特Transformer与视觉Transformer量化方向论文汇编

> 本方向共 8 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers ｜二值注意力机制

研究机构：香港理工大学

作者：Chaodong Xiao、Zhengqiang Zhang、Lei Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2603.09582)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09582)

> 长序列视觉Transformer的注意力计算受限于二次复杂度与浮点精度依赖，现有量化方法止步于4-bit，无法进一步压缩至二值空间。本文切入点在于证明二值化Q/K在统计层面保留了原始注意力的协方差结构，从而在1-bit精度下维持相似度判别能力。通过引入缩放二值表示、可学习偏置项及混合8-bit量化，结合量化感知训练与自蒸馏，BinaryAttention在A100 GPU上实现了比FlashAttention2快2倍以上的推理加速，且精度持平或超越全精度基线。其价值在于突破了极低比特量化的精度崩塌边界，但偏置项的引入是否构成对标准注意力架构的非标准修改，仍需进一步审视。

】

---

【CAR-SAM: Cross-Attention Reconstruction for Post-Training Quantization of the Segment Anything Model ｜交叉注意力重建的后训练量化

研究机构：南京大学

作者：Houji Wen、Jiangyong Yu、Jun Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.16901)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.16901)

> 针对SAM解码器双向交叉注意力结构导致的低比特量化精度崩塌，现有PTQ方法因忽略模态间尺度失配与分支间误差耦合而失效。本文切入点在于将量化误差补偿从线性层扩展至矩阵乘法操作，并引入联合重建策略以抑制优化振荡。具体做法是提出MAC机制将激活误差转移至前序权重，配合JCAR策略联合优化耦合模块。该方法在W4A4下显著优于基线，但其理论推导依赖一阶近似，且未验证在更复杂多模态架构中的泛化性。

】

---

【DeltaQuant: 4-bit Video Diffusion Models with Spatiotemporal Delta Smoothing ｜时空差分平滑的视频扩散模型4位量化

研究机构：美国麻省理工学院、美国卡内基梅隆大学

作者：Xingyang Li、Samuel Tesfai、Zhekai Zhang 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c3dc3c6c475)

> 视频扩散模型在去噪过程中激活值异常值随时间步剧烈波动，导致静态校准的量化方法失效。现有方案如SVDQuant依赖离线固定的低秩分支，无法适应这种动态性。本文利用视频数据固有的时空冗余，将激活分解为高精度核心Token与低精度差分Token，以在线均值计算替代静态平滑。该方法在Wan2.2上实现了2.9倍模型压缩与2.3倍显存降低，但仅验证了特定分辨率下的性能，未探讨不同视频内容复杂度对时空相似性的影响。

】

---

【LS-ViT: Least-Squares Hessian Based Block Reconstruction for Low-Bit Post-Training Quantization of Vision Transformers ｜最小二乘Hessian重构的ViT低比特量化

研究机构：韩国首尔大学

作者：Hyunha Hwang、Xuan Truong Nguyen、Hyuk-Jae Lee

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e6849f8816a5)

> 视觉Transformer（ViT）在极低比特后训练量化（Post-Training Quantization, PTQ）中面临精度崩塌，根源在于现有二阶重构方法对Hessian矩阵的近似忽略了样本间协方差项。LS-ViT将Hessian估计重构为线性最小二乘问题，通过单次反向传播拟合全局最优Hessian，消除了独立假设带来的偏差。该方法在W2/A3配置下将Swin-B的Top-1准确率提升至67.73%，较基线FIMA-Q提升4.58个百分点，但其在W4/A4高比特下的增益微弱，且未验证动态场景下的鲁棒性。

】

---

【QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models ｜面向视觉-语言-动作模型的尺度校准后训练量化

研究机构：美国俄亥俄州立大学、美国密歇根大学

作者：Jingxuan Zhang、Yunta Hsieh、Zhongwei Wan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20309)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20309)

> 视觉-语言-动作（VLA）模型在具身智能部署中面临计算与内存瓶颈，现有量化方法因忽略语言骨干与扩散Transformer（DiT）动作头间的紧耦合尺度漂移而失效。QuantVLA通过选择性量化布局与注意力温度匹配、输出头平衡两个轻量级校准机制，在无需重训练的前提下实现了VLA系统的低比特部署。该框架在LIBERO基准上超越了全精度基线，但其在更复杂长时序任务中的泛化能力及校准机制对深层非线性偏移的覆盖范围仍存疑。

】

---

【Rethinking Asymmetric Quantization: Hidden Symmetry in Vision Model Weights ｜稠密-稀疏加性量化（DASQ）：基于权重隐藏对称性的硬件高效PTQ方案

作者：Masafumi Mori、Shinya Gongyo、Mitsuru Ambai

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5826aefe3f5d)

> 视觉模型部署面临的核心矛盾是低比特量化下的精度保持与硬件效率平衡。现有后训练量化（PTQ）方法普遍采用非对称量化（AsymQ）以拟合权重分布的非对称性，但零点偏移导致乘数位宽增加约1.3倍，显著降低加速器能效。本文切入点在于揭示预训练权重在移除少量稀疏离群值后呈现近似对称分布的隐藏特性，据此提出稠密-稀疏加性量化（Dense and Additive Sparse Quantization, DASQ）框架，将权重分解为对称稠密分量与稀疏离群分量，均使用对称量化（SymQ）处理。该方案在精度上超越现有PTQ方法的同时，通过并行稀疏MAC实现更低功耗，但其稀疏度参数设定与跨架构泛化能力仍存疑。

】

---

【S2D: Selective Spectral Decay for Quantization-Friendly Conditioning of Neural Activations ｜选择性谱衰减（S[2]D）：面向量化友好性的神经激活条件化

研究机构：美国卡内基梅隆大学

作者：Arnav Chavan、Nahush Lele、Udbhav Bamba 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.14432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.14432)

> 低比特Transformer量化长期受困于激活值异常值（Activation Outliers）导致的动态范围压缩，现有平滑或旋转方法仅事后缓解分布失衡，未触及异常值生成的优化器根源。本文切入点在于揭示AdamW优化器的各向异性更新导致权重谱范数失控，进而提出选择性谱衰减（Selective Spectral Decay, S[2]D）正则化器，在微调阶段仅惩罚最大奇异值以重塑权重几何。该方法在W4A4下将ImageNet-1K精度提升7.41个百分点，但仅验证于视觉编码器，对语言模型或更复杂架构的普适性存疑。

】

---

【TWEO: Transformers Without Extreme Outliers Enables FP8 Training And Quantization For Dummies ｜无极端异常值Transformer

研究机构：南京大学、中国科学技术大学

作者：Guang Liang、Jie Shao、Ningyuan Tang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.23225)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.23225)

> 导读 现代硬件原生支持8位浮点（FP8）计算以加速大模型训练，但激活值中幅值超过1000的极端异常值导致数值溢出，使FP8训练频繁崩溃。现有方案依赖混合精度工程或侵入式架构修改，成本高且缺乏通用性。本文提出TWEO，通过一个直接惩罚极端激活幅值的简单损失函数，在训练阶段从源头消除异常值，实现全模型FP8稳定训练。该方案在7B规模模型上验证了跨模态有效性，但其对模型表达力的潜在限制及在极低比特量化下的泛化能力尚存疑。

】
