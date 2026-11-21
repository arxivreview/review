# ICLR2026最新论文 ｜OVERSHOOT AND SHRINKAGE IN CLASSIFIER-FREE GUIDANCE: FROM THEORY TO PRACTICE ｜无分类器引导的高维失真机制与非线性修正

作者：Krunoslav Lehman Pavasovic、Jakob Verbeek、Giulio Biroli 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_93792412)

> 导读 无分类器引导（Classifier-Free Guidance, CFG）是扩散模型条件生成的标准组件，但其线性外推机制在有限维度下必然导致均值过冲与方差收缩，引发过饱和与多样性丧失。现有理论多在低维或特定分布下刻画失真，缺乏对高维极限行为的统一解释，导致引导强度调度依赖启发式调参。本文基于统计物理中的动态机制框架，证明CFG在无限及高维极限下能生成正确分布，并据此提出Power-Law CFG，通过非线性缩放得分差来抑制有限维失真。该工作从理论上厘清了CFG失效的维度依赖性，但在纯FID指标上未超越几何约束类方法，且理论保证依赖精确得分假设。

## 研究背景

扩散模型通过反向去噪过程生成数据，其核心驱动力是得分函数（Score Function），即对数概率密度的梯度。条件生成要求采样轨迹向特定类别或文本描述对齐，早期方法依赖外部分类器梯度，但引入了训练不稳定与额外计算开销。2021年提出的无分类器引导（Classifier-Free Guidance, CFG）通过联合训练条件与无条件模型，在推理时利用两者预测噪声的差异进行线性外推，消除了对独立分类器的依赖，确立了大规模扩散管线的标准范式。

CFG的核心公式为 $\tilde{\epsilon}_\theta(x_t, c) = \epsilon_\theta(x_t, \emptyset) + w \cdot (\epsilon_\theta(x_t, c) - \epsilon_\theta(x_t, \emptyset))$，其中 $w$ 为引导强度。这一线性假设在低维或简单分布下表现良好，但在高维复杂数据流形中，其有效性受到严重挑战。随着Latent Diffusion Models将扩散过程移至压缩潜空间，高引导强度下导致的过饱和、纹理伪影及多样性丧失问题凸显，这些现象被归结为流形偏离（Off-manifold Drift）。早期理论工作如Chidambaram et al. (2024)在单维及有限维高斯混合模型中证实了CFG导致均值过冲与方差收缩，但未能解释为何高维场景下这些效应似乎减弱，也未提供基于维度特性的修正方案。本文切入点在于利用统计物理框架分析高维极限下的动态机制，揭示CFG失真的维度依赖性，并据此设计非线性引导策略。

## 核心方法

### 动态机制与高维极限分析

本文方法参照系为基于高斯混合模型（Gaussian Mixture Models, GMMs）的扩散过程分析。与Chidambaram et al. (2024)聚焦有限维失真不同，本文引入Biroli et al. (2024)的动态机制框架，将反向扩散过程划分为两个阶段：Regime I（类别未决定）与Regime II（类别已决定），分界点为物种形成时间 $t_s = \frac{1}{2}\log(d)$。在Regime I，CFG通过放大条件与无条件得分差加速轨迹向目标类别收敛；在Regime II，由于高维下条件得分主导，CFG项指数级衰减，引导失效。这一分析建立了CFG在高维下生成正确分布的理论基础，即“维度祝福”（Blessing of Dimensionality），为后续非线性修正提供了理论基准。

### Power-Law CFG 非线性修正

针对有限维度下Regime I的CFG项未能完全衰减导致的均值过冲与方差收缩，本文提出Power-Law CFG。该设计动机在于：线性CFG在得分差较小时仍施加固定强度的引导，导致噪声被放大；而在得分差较大时，线性缩放不足以抑制过冲。Power-Law CFG通过引入非线性函数 $\phi_t(s)$ 对得分差进行缩放，公式为：

$$ S_t^{PL}(\vec{x}, c) = S_t(\vec{x}) + \phi_t(\|\Delta S_t\|) \cdot \frac{\Delta S_t}{\|\Delta S_t\|} $$

其中 $\Delta S_t = S_t(\vec{x}, c) - S_t(\vec{x})$，$\phi_t(s) = \omega \cdot s^\alpha$，$\alpha > 0$。当得分差 $\|\Delta S_t\|$ 较小时，$s^\alpha$ 显著衰减，抑制不可靠的引导信号；当得分差较大时，引导强度随信号强度非线性增长，增强向正确类别的推力。理论上，该修改在 $\alpha > 0$ 时减小了有效势能的曲率增量，从而降低方差收缩；同时通过抑制小信号噪声，减少均值过冲。在无限维极限下，Power-Law CFG退化为标准CFG，保留了高维正确性保证。

## 实验评估

实验在ImageNet-1K (256x256, 512x512)、COCO、CC12M及CIFAR-10上进行，对比基线包括Standard CFG、CADS、Limited Guidance及Cosine Scheduler。主要结果如下表所示（数值逐字取自论文Table 1）：

| 模型 | 方法 | FID | Precision | Recall |
|---|---|---|---|---|
| EDM2-S (512) | Standard CFG | 2.29 | 0.751 | 0.582 |
| EDM2-S (512) | Power-law CFG | 1.93 | 0.780 | 0.631 |
| DiT/XL-2 (256) | Standard CFG | 2.27 | 0.829 | 0.584 |
| DiT/XL-2 (256) | Power-law CFG | 2.05 | 0.831 | 0.595 |
| FM MMDiT (COCO) | Standard CFG | 5.20 | 0.629 | 0.594 |
| FM MMDiT (COCO) | Power-law CFG | 4.81 | 0.621 | 0.619 |

Power-Law CFG在FID上显著优于Standard CFG，例如EDM2-S从2.29降至1.93，DiT/XL-2从2.27降至2.05。Precision与Recall同步提升，表明该方法在提升保真度的同时改善了多样性，缓解了标准CFG的过饱和问题。

消融实验显示，$\alpha$ 参数对性能影响显著。在EDM2-S上，$\alpha=0.85$ 时FID达到1.93，而 $\alpha=0.05$ 时FID为4.74，表明非线性程度需足够大才能有效抑制失真。在DiT/XL-2上，$\alpha=0.75$ 时FID为2.05，$\alpha=0.6$ 时为3.03，进一步验证了 $\alpha > 0.7$ 的必要性。此外，Power-Law CFG可与CADS叠加，在EDM2-S上FID进一步降至1.52，显示其与其他引导策略的正交性。

评估边界方面，论文未报告置信区间，数值比较需谨慎。理论分析假设精确得分可用，实际模型中得分为近似值，理论保证的鲁棒性未完全验证。代码未公开，但Power-Law公式简单，易于复现。超参数 $\alpha$ 在潜空间中固定为0.9表现稳定，像素空间中需微调，表明方法对空间维度的敏感性。

## 关联研究分析

从问题动机看，本文与Manifold-Optimal Guidance（Jia et al., 2026）均旨在解决高引导强度下的流形偏离，但路径截然不同。Manifold-Optimal Guidance采用黎曼几何约束，通过度量算子逆运算获得自然引导方向，假设数据分布在低维黎曼流形上；本文则基于代数缩放，假设失真源于得分差的线性外推误差。Manifold-Optimal Guidance在ImageNet 256x256上取得2.02 FID，略优于本文的2.05 FID，表明几何约束在抑制流形偏离上可能更直接。然而，本文的理论优势在于解释了失真的维度依赖性，而几何方法未提供此类机制解释。

从方法设计看，本文与CADS（Sadat et al., 2023）形成互补。CADS通过调整引导强度随时间的变化来缓解过饱和，属于线性调度策略；本文Power-Law CFG通过非线性缩放得分差，属于信号强度自适应策略。实验显示两者可叠加，Power-Law CFG + CADS在EDM2-S上FID为1.52，优于单独使用CADS的1.60 FID。这表明非线性缩放与时间调度解决了不同层面的失真：前者抑制小信号噪声，后者避免后期过度引导。与Chidambaram et al. (2024)相比，本文将其低维失真分析扩展至高维极限，并提供了可部署的修正方案，而非仅停留在理论刻画。

## 总结

本文核心矛盾在于CFG线性外推在有限维度下必然导致均值过冲与方差收缩，而现有理论缺乏对高维极限行为的统一解释。本文抓住统计物理动态机制框架，证明CFG在高维下生成正确分布，并据此提出Power-Law CFG，通过非线性缩放得分差抑制有限维失真。实验证明该方法在EDM2-S上将FID从2.29降至1.93，在DiT/XL-2上从2.27降至2.05，同时提升Precision与Recall。本文边界在于理论保证依赖精确得分假设，实际模型中得分为近似值，且FID指标未超越几何约束类方法。当得分近似误差较大时，Power-Law CFG的非线性缩放是否仍能稳定抑制失真，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_93792412)