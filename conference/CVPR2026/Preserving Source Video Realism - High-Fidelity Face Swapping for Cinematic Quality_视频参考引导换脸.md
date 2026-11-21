# CVPR2026最新论文 ｜Preserving Source Video Realism: High-Fidelity Face Swapping for Cinematic Quality ｜视频参考引导换脸

研究机构：浙江大学

作者：Zekai Luo、Zongze Du、Zhouhang Zhu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07951)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07951)

> 视频换脸需同时维持长序列时序一致性与源视频高保真细节，现有GAN逐帧法易闪烁，扩散Inpainting法丢失原始像素信息。LIVINGSWAP通过关键帧注入身份、源视频作为参考引导生成，并采用时间拼接策略解决长视频误差累积。该方法将人工编辑工作量降低40倍，但在低相似度身份场景下身份保持能力仍显不足，且依赖特定工业级硬件资源。

## 研究背景

视频换脸任务要求替换视频中人脸身份，同时严格保留姿态、表情、光照及背景等属性。传统GAN方法（如SimSwap, Inswapper）采用逐帧处理策略，虽能注入目标身份，但缺乏时序建模能力，导致长视频中频繁出现闪烁与抖动。扩散模型（Diffusion Models）虽具备更强的时序一致性，但主流方法（如DiffSwap, FaceAdapter）将换脸视为Inpainting任务，通过掩码遮挡原脸并依赖外部编码器（如关键点、3DMM）生成新脸。这种稀疏条件引导机制丢弃了源视频面部区域的原始像素信息，导致生成结果在光照细微变化、复杂妆容及半透明遮挡等电影级场景中缺乏真实感与生命力。

LIVINGSWAP的切入点在于直接利用源视频的面部像素作为参考，而非依赖中间表示。这一设计源于参考引导生成（Reference-guided Generation）在图像编辑中的成功，旨在解决视频换脸中“高保真细节保留”与“长序列身份稳定性”的双重矛盾。通过构建Face2Face数据集与CineFaceBench基准，该工作将研究重心从学术界的属性解耦理论转向工业级长视频生成的工程化落地，重点解决配对数据稀缺与人工干预成本过高的问题。

## 核心方法

### 方法参照系

本文基于VACE（Video Editing Foundation Model）的DiT（Diffusion Transformer）架构与Rectified Flow训练目标。与标准视频生成不同，LIVINGSWAP不依赖文本指令或稀疏结构引导，而是将源视频片段直接作为视觉参考输入，并通过关键帧（Keyframes）作为时序锚点注入目标身份，实现了从“结构引导”到“像素参考”的范式转移。

### 关键帧身份注入与参考引导

传统Inpainting方法依赖外部编码器提取的结构特征，导致细节丢失。LIVINGSWAP首先选取视频中姿态、表情或光照变化显著的帧作为关键帧，使用高质量图像换脸模型（如Inswapper）进行单帧编辑，获得高保真的身份锚点。随后，将源视频片段 $V_S[k_i:k_{i+1}]$ 与编辑后的关键帧对 $\{f_{k_i}^{s-o}, f_{k_{i+1}}^{s-o}\}$ 共同编码。通过VAE编码器 $E_\phi(\cdot)$ 提取潜变量，并按时间对齐顺序拼接为聚合潜条件令牌 $Z_c$：

$$
Z_c = [E_\phi(V_S[k_i:k_{i+1}]), E_\phi(f_{k_i}^{s-o}), E_\phi(f_{k_{i+1}}^{s-o})]
$$

这一设计保留了源视频的光照、表情等细微视觉线索，同时通过关键帧强制约束身份特征，解决了稀疏条件引导导致的保真度下降问题。

### 时间拼接与属性编码器注入

为处理长视频，LIVINGSWAP将视频切分为固定长度（81帧）的块（Chunk）。为避免块间不连续，采用时间拼接策略：第一块使用关键帧作为起止引导；后续块使用上一块的最终输出帧 $f_{k_i}^{swap-out}$ 作为起始引导，关键帧 $f_{k_{i+1}}^{swap-in}$ 作为结束引导。这种重叠机制有效缓解了误差累积。在特征注入层面，引入属性编码器（Attribute Encoder），其输出通过逐层元素相加注入DiT骨干网络：

$$
X_{[l]} = X_{[l]} + A_{[\psi[h]]}
$$

其中 $X_{[l]}$ 为骨干网络第 $l$ 层隐藏表示，$A_{[\psi[h]]}$ 为属性编码器第 $h$ 块输出。该机制在保留预训练生成先验的同时，实现了像素级细节的自适应条件注入，确保了生成结果与源视频在视觉属性上的高度一致。

## 实验评估

实验在FF++与自建CineFaceBench上进行，基线涵盖GAN（SimSwap, Inswapper）与扩散（DiffSwap, FaceAdapter）路线，但缺失混合架构（如AttDiff-GAN）及3D先验方法。CineFaceBench包含400对测试样本，覆盖长镜头、复杂光照等电影级场景，并设置easy/hard两种身份相似度条件。

| 方法 | ID Sim. (easy/hard) | FVD (easy/hard) | Avg. Rank |
| :--- | :--- | :--- | :--- |
| Inswapper | 0.506 / 0.365 | 176.96 / 182.25 | 2.500 |
| Face-Adapter | 0.315 / 0.107 | 104.19 / 111.81 | 5.583 |
| **LIVINGSWAP** | **0.567 / 0.422** | **54.32 / 63.97** | **1.667** |

LIVINGSWAP在CineFaceBench上全面领先，FVD显著低于Inswapper，表明其时序一致性更强；ID Sim.在easy设置下最高，但在hard设置下（0.422）仍低于Inswapper（0.365）的差距较小，显示其在低相似度身份下的鲁棒性有待提升。

消融实验显示，使用完整数据集（Upper Data）比仅使用部分数据（Lower Data）在光照与姿态保持上更优，验证了数据多样性对保真度的贡献。移除目标图像输入（w/o Target Image）后，ID Sim.下降，但在身份相似度不敏感的场景中仍具可行性，说明关键帧注入是身份保持的主要来源，目标图像为辅助增强。

评估指标包含ID Similarity、Expression/Lighting/Pose Error及FVD，但未报告计算效率与推理速度。模型基于14B预训练权重，在8块NVIDIA H200 GPU上训练14天，资源门槛极高。代码未明确开源，仅提供项目网页，可复现性受限。

## 关联研究分析

从问题动机看，LIVINGSWAP与InstructPix2Pix等指令驱动方法形成鲜明对比。后者依赖文本嵌入引导，适合复杂语义编辑，但易导致身份漂移；LIVINGSWAP则通过像素级参考直接保留源视频属性，牺牲了语义灵活性，换取了电影级场景下的保真度。这种差异源于任务特性：视频换脸更关注视觉一致性而非语义理解，因此像素参考比文本指令更直接有效。

从方法设计看，LIVINGSWAP与VACE共享参考引导架构，但VACE侧重通用视频编辑，而LIVINGSWAP通过关键帧注入与时间拼接专门优化换脸任务。与DiffSwap等Inpainting方法相比，LIVINGSWAP避免了掩码导致的细节丢失，但引入了对源视频质量的依赖。若源视频存在噪声或伪影，参考引导可能放大这些缺陷，而非像Inpainting方法那样通过生成先验进行修复。

## 总结

LIVINGSWAP解决了视频换脸中时序一致性与高保真细节保留的矛盾，通过关键帧注入身份、源视频作为参考引导，并采用时间拼接策略，将人工编辑工作量降低40倍。实验表明其在CineFaceBench上FVD达54.32（easy），ID Sim.达0.567（easy），显著优于Inswapper。然而，其在hard身份相似度设置下ID Sim.仅0.422，且依赖14B模型与8块H200 GPU，限制了其泛化能力与部署成本。当源视频质量较低或身份相似度极低时，参考引导机制是否仍能维持稳定的身份保持，论文未给出充分验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07951)