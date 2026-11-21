# CVPR2026最新论文 ｜YOSE: You Only Select Essential Tokens for Efficient DiT-based Video Object Removal ｜掩码感知Token选择与扩散过程模拟

研究机构：南开大学

作者：Chenyang Wu、Lina Lei、Fan Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27322)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27322)

> 视频对象移除（Video Object Removal, VOR）任务中，基于扩散Transformer（DiT）的模型因对全时空Token执行密集去噪与注意力计算，导致推理延迟与掩码区域大小无关，造成大量计算冗余。现有高效视频生成方法多聚焦于全局Token压缩或步数蒸馏，未针对局部修复任务的稀疏性进行优化。YOSE通过可微分动态索引仅处理掩码内Token，并利用轻量级模块模拟掩码外区域的扩散过程影响，将计算复杂度与掩码比例线性挂钩。该方法在保持视觉质量的同时实现了2.5至3.3倍的推理加速，但其对复杂动态掩码及长视频时序漂移的鲁棒性尚未得到充分验证。

## 研究背景

视频对象移除旨在从视频中去除指定物体并重建背景，其核心挑战在于维持空间真实感与时间一致性。DiT架构通过将去噪过程重构为潜空间Token的序列到序列变换，利用全局建模能力实现了高质量的视频生成，但其自注意力机制的计算量随Token数量呈二次方增长。在VOR任务中，仅掩码区域需要重建，未掩码区域应保持原样，然而MiniMax Remover等现有DiT-based VOR模型仍对全时空Token执行密集计算，导致即使掩码比例极低，推理延迟依然居高不下。

主流高效视频生成路线包括步数蒸馏（如DMD、GPD）与高效注意力机制（如SANA-Video的线性注意力），前者通过压缩去噪步数降低时间维度冗余，后者通过架构改进降低空间Token冗余。然而，这些方法均假设生成任务为全局性，未利用VOR任务的局部稀疏特性。YOSE的切入点在于识别出VOR中约70%案例的掩码比例低于20%，提出通过掩码感知的Token选择与扩散过程模拟，将计算资源精准分配至必要区域，从而在保持语义一致性的前提下实现线性复杂度加速。

## 核心方法

### 方法参照系

DiT-based VOR的标准流程为：输入带掩码视频，经3D-VAE编码为潜空间Token序列，通过多层DiT块执行全Token自注意力与去噪，最后解码输出。本文的关键差异在于，标准流程对全Token执行计算，而YOSE仅处理掩码内Token，并通过模拟机制补偿掩码外区域的影响，从而打破计算量与总Token数固定的关系。

### 批量变长索引（BVI）

BVI解决的是全Token计算中未掩码区域的冗余问题。传统硬索引（如Tensor[mask]）阻断梯度流且无法支持变长批次，BVI通过可微分的网格采样函数（GSample）实现连续插值选择。给定归一化坐标网格 $Ind_F$，Token提取定义为：

$$ S_{in} = \text{GSample}(Lat_{mask}, Ind_F) $$

该公式通过坐标映射实现掩码内Token的可微分选择，支持批次内不同掩码大小的并行处理。BVI将计算复杂度从 $O(N^2)$ 降至 $O(N_{mask}^2)$，其中 $N_{mask}$ 为掩码内Token数，实现了计算量与掩码比例的线性缩放。

### 扩散过程模拟器（DiffSim）

DiffSim解决的是仅处理掩码内Token导致的上下文依赖缺失问题。在DiT块中，掩码内Token需感知掩码外区域的语义信息以维持边界一致性。DiffSim引入残差潜变量 $Res_{Nis}$ 模拟未掩码区域的扩散过程影响：

$$ Res_{Nis} = \alpha \cdot Lat_{Nis} + (1-\alpha) \cdot Lat_{mask} $$

其中 $Lat_{Nis}$ 为噪声潜变量，$Lat_{mask}$ 为掩码视频潜变量。通过结合参数 $G$、缩放参数 $S$ 与偏置参数 $Bias$，DiffSim生成代理键值（KV）特征，使掩码内Token在自注意力中能够“感知”未掩码区域的扩散状态，避免全Token计算的同时保持语义连贯性。

## 实验评估

实验在DAVIS与YouTube-VOS数据集上进行，对比Propainter、DiffuEraser、ROSE、VACE及MiniMax Remover。基线覆盖了基于U-Net与DiT的VOR方法，但缺乏其他DiT-based VOR变体的对比。

| 数据集 | 方法 | PSNR (dB) | SSIM | LPIPS |
| :--- | :--- | :--- | :--- | :--- |
| YouTube-VOS | MiniMax Remover | 30.3296 | 0.9116 | 0.0615 |
| YouTube-VOS | YOSE (Minimax) | 31.0117 | 0.9120 | 0.0642 |
| DAVIS | MiniMax Remover | 29.3671 | 0.8723 | 0.0836 |
| DAVIS | YOSE (Minimax) | 29.5855 | 0.8703 | 0.0826 |

YOSE在YouTube-VOS上PSNR提升0.68 dB，DAVIS上提升0.22 dB，SSIM与LPIPS变化均小于 $1e-2$，表明质量损失可忽略。

消融实验显示，DiffSim与融合策略对背景PSNR提升贡献显著。在YouTube-VOS上，YOSE(VACE)相比原始VACE提升PSNR 5.47 dB，DAVIS上提升3.19 dB，验证了DiffSim在维持背景保真度上的有效性。

评估协议采用480×832分辨率与4N+1帧长，指标包括VBench四项及PSNR/SSIM/LPIPS。局限在于未报告长视频（>100帧）的时序一致性指标，且掩码比例分布统计基于静态数据集，未涵盖动态掩码场景。代码已开源，训练仅需4小时（8 GPU，2K步），可复现性高。

## 关联研究分析

从问题动机看，YOSE与SANA-Video均追求线性复杂度，但SANA-Video通过块线性注意力架构全局降低计算量，适用于长视频生成；YOSE则利用VOR任务的局部稀疏性，通过Token选择实现按需计算。差异根源在于任务特性：全局生成需完整时空建模，而局部修复仅需掩码区域重建，这使得YOSE在低掩码比例场景下加速比（3.3x）高于SANA-Video的典型加速比（据领域综述，SANA-Video在长视频上内存占用降低但未报告具体FPS提升）。

从方法设计看，YOSE的DiffSim与TeaCache的特征缓存逻辑相似，均利用去噪过程中的冗余信息。但TeaCache通过测量特征距离动态决定复用时机，属于静态复用；DiffSim则通过可学习参数模拟未掩码区域的扩散状态，属于动态模拟。差异在于，TeaCache适用于全局生成中跨步特征复用，而DiffSim专为局部修复中掩码边界一致性设计，其模拟机制更依赖于掩码结构的先验信息。

## 总结

YOSE针对DiT-based VOR中全Token计算与掩码稀疏性不匹配的核心矛盾，通过BVI实现掩码内Token的可微分选择，并利用DiffSim模拟掩码外区域的扩散过程影响，将计算复杂度与掩码比例线性挂钩。实验证明其在保持视觉质量（PSNR提升0.22-0.68 dB）的同时实现2.5-3.3倍加速。然而，其评估局限于静态掩码与短视频，未验证动态掩码下BVI的索引效率及长视频中DiffSim的时序漂移风险。当掩码区域随时间剧烈变化时，DiffSim模拟的语义一致性是否仍能维持边界连贯，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27322)