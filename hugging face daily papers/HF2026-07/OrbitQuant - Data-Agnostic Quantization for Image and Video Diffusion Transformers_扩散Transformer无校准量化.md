# HuggingFace最新推荐论文 ｜OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers ｜扩散Transformer无校准量化

研究机构：美国南加州大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Donghyun Lee、Jitesh Chavan、Duy Nguyen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.02461)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.02461)

> 扩散Transformer（DiT）推理因多步去噪与计算瓶颈而昂贵，低比特后训练量化（PTQ）是自然解法，但现有方法依赖校准数据拟合激活范围，无法适应DiT激活随时间步、提示词漂移的特性。OrbitQuant通过随机置换块Hadamard旋转将激活映射至固定分布，用单一Lloyd–Max码本替代逐时间步校准，实现了无校准的权重-激活联合量化。该方法在W4A4下达到SOTA，在W2A4下是唯一保持可用生成质量的方法，但其对激活分布高斯近似的依赖在更复杂模态中是否依然成立，尚待验证。

## 研究背景

DiT推理的瓶颈在于计算而非内存：与LLM解码中权重加载主导延迟不同，DiT在单批次下即为计算受限，仅量化权重无法带来实测加速。因此，必须同时量化权重与激活。然而，DiT激活存在通道级离群值，且其统计特性随去噪时间步、提示词及分类器自由引导分支动态变化，导致传统PTQ中基于少量校准数据拟合的缩放因子失效。

主流DiT量化方法如SVDQuant、PTQ4DiT、ViDiT-Q均依赖校准数据来吸收这种分布漂移，每个新检查点或分辨率都需重新收集并拟合校准集。LLM量化中的平滑或旋转方法虽能处理离群值，但假设激活统计可由单次校准捕获，这一假设在DiT中不成立。OrbitQuant的切入点在于：既然激活范围随输入移动，就不应追逐这个移动目标，而是通过数学变换将其“旋转掉”，使量化器不再依赖任何输入统计。

## 核心方法

### 分布论量化参照系

传统PTQ将量化视为范围估计问题：对每个输入维度，用校准数据确定最小/最大值，构建均匀量化网格。本文将其重构为分布码本问题：量化器不再拟合数据范围，而是拟合一个与输入无关的理论分布。这一转变的关键前提是存在一种变换，能将任意输入激活映射至固定分布。

### 随机置换块Hadamard旋转

设计动机：密集Haar旋转虽能使激活坐标严格遵循Beta边际分布，但计算与存储开销为$O(d^2)$，在DiT的大维度下不可接受。本文采用随机置换块Hadamard（RPBH）旋转，其结构为：

$$
\Pi_d = \text{blkdiag}(D_1 H_h, \dots, D_k H_h) P_\pi
$$

其中$H_h$为Walsh–Hadamard矩阵，$D_i$为Rademacher符号对角阵，$P_\pi$为均匀随机置换矩阵。该变换复杂度为$O(d \log h)$，且可在任意维度$d$上构造（取$h$为$d$的最大2的幂因子）。随机置换$P_\pi$的作用是将离群值能量分散至所有块，确保每个块接收平衡的输入质量，从而保持旋转后边际接近$N(0, 1/d)$。

### 共享基权重-激活联合量化

设计动机：若权重与激活在不同基下量化，旋转无法在矩阵乘积中抵消，导致推理时需额外逆变换。本文将旋转离线折叠进权重行：

$$
\hat{W}' = Q_{\hat{b}_w}(\Pi_d^\top W) \cdot r'
$$

其中$r'$为权重行范数向量，以BF16存储。在线激活量化为：

$$
\hat{x}' = s \cdot Q_{\hat{b}_a}(\Pi_d x / (s + \epsilon))
$$

其中$s = \| \Pi_d x \|_2$为每token标量范数。由于$\Pi_d^\top \Pi_d = I$，量化层计算$\hat{W}' \hat{x}' \approx Wx$，无需逆变换。单一Lloyd–Max码本$\mathcal{C}_{d,b}$由理论边际$f_d$离线构建，服务于所有层、时间步、提示词及权重行，实现完全无校准。

## 实验评估

实验在FLUX.1-schnell、FLUX.1-dev、Z-Image-Turbo（图像）及Wan 2.1-1.3B、CogVideoX-2B（视频）上进行，比特宽度为W4A4与W2A4（图像）、W4A6与W4A4（视频）。基线覆盖校准类（SVDQuant、ViDiT-Q、AdaTSQ）与旋转类（QuaRot、SmoothQuant），但缺失QAT类强基线（如RobuQ）的直接对比，仅在补充材料提及。

| 模型 | 方法 | 比特 | GenEval Overall |
| :--- | :--- | :--- | :--- |
| FLUX.1-schnell | FP16 | 16/16 | 0.997 |
| FLUX.1-schnell | SVDQuant | W4A4 | 0.994 |
| FLUX.1-schnell | OrbitQuant | W4A4 | 0.997 |
| FLUX.1-schnell | SVDQuant | W2A4 | 0.293 |
| FLUX.1-schnell | OrbitQuant | W2A4 | 0.585 |
| Z-Image-Turbo | FP16 | 16/16 | 1.000 |
| Z-Image-Turbo | SVDQuant | W4A4 | 0.994 |
| Z-Image-Turbo | OrbitQuant | W4A4 | 0.997 |
| Z-Image-Turbo | SVDQuant | W2A4 | 0.250 |
| Z-Image-Turbo | OrbitQuant | W2A4 | 0.843 |

在W4A4下，OrbitQuant在FLUX.1-schnell与Z-Image-Turbo上Overall得分等于或超过FP16基线，显著优于SVDQuant（0.994）与ViDiT-Q（0.994）。在W2A4下，SVDQuant与ViDiT-Q得分崩塌至0.25–0.30区间，而OrbitQuant保持0.585（FLUX.1-schnell）与0.843（Z-Image-Turbo），是唯一产生可用图像的方法。视频生成中，OrbitQuant在Wan 2.1-1.3B W4A4下Overall Consistency为58.58%，优于SVDQuant（57.57%）与ViDiT-Q（51.42%）。

消融实验显示，移除随机置换后，W2A4下GenEval Overall从0.595降至0.558，W3A3下从0.674降至0.642，证实置换对低比特鲁棒性的关键作用。RPBH与Full RHT在W4A4下性能相近（0.690 vs 0.691），但RPBH延迟更低（0.451s vs 0.452s），且可在$d=1920$等非2幂维度上构造。AdaLN模块固定为INT4权重，未参与比特宽度搜索，其消融显示INT4相比BF16将压缩率从2.21×提升至4×，但GenEval Overall仅下降0.006，表明该模块对量化不敏感。

评估协议采用假量化（fake quantization），权重与激活反量化至BF16后执行矩阵乘，因此测量的是量化开销而非真实低比特加速。所有方法在相同硬件（NVIDIA H100）与配置下评测，但未报告置信区间或多次运行方差。代码未完全开源，仅提供项目页面，超参数（如块大小$h$）未在正文中详述，可复现性受限。

## 关联研究分析

从问题动机看，OrbitQuant与SVDQuant的根本差异在于对“分布漂移”的处理哲学。SVDQuant通过校准数据拟合低秩分支来吸收离群值，本质是数据驱动的被动适应；OrbitQuant则通过旋转将分布漂移“消除”于数学变换中，是分布驱动的主动治理。这一差异源于任务特性：DiT激活的漂移是系统性的（随时间步单调变化），而非随机噪声，因此可被确定性变换捕获。SVDQuant在W2A4下的崩塌可能并非方法缺陷，而是校准数据无法覆盖极端时间步的分布范围，论文未对此进行归因分析。

从方法设计看，OrbitQuant与TurboQuant共享“旋转+分布码本”框架，但应用场景与实现细节截然不同。TurboQuant是独立的KV缓存向量量化器，使用密集Haar旋转并需逆变换重构；OrbitQuant将旋转折叠进权重，实现前向抵消，且用RPBH替代Haar以降低开销。这一设计选择源于DiT线性层的结构特性：权重与激活在同一层内交互，旋转可被吸收；而KV缓存是独立向量，旋转后需重构。随机置换的引入是OrbitQuant独有的创新，TurboQuant未使用置换，因其密集Haar旋转已保证分布匹配，而RPBH的块结构需要置换来平衡块间质量。

## 总结

OrbitQuant解决的核心矛盾是DiT激活分布漂移与静态校准量化器之间的冲突。其切入点是：既然激活范围随输入移动，就通过旋转将其映射至固定分布，使量化器不再依赖输入统计。方法上，采用RPBH旋转与Lloyd–Max码本，实现无校准的权重-激活联合量化。实验证明，在W4A4下达到SOTA（FLUX.1-schnell Overall 0.997），在W2A4下是唯一保持可用质量的方法（Z-Image-Turbo Overall 0.843）。其边界在于：依赖激活分布的高斯近似，且仅在图像与视频DiT上验证，未探索音频或3D生成等更复杂模态。当DiT架构引入更深的注意力堆叠或跨模态融合时，RPBH旋转是否仍能保持边际分布的稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.02461)