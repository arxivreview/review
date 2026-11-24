# CVPR2026最新论文 ｜VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM ｜显式外观方差建模的3DGS-SLAM系统

研究机构：美国乔治梅森大学、德国慕尼黑工业大学

作者：Anh Thuan Tran、Jana Kosecka

论文原文见 [arXiv](https://arxiv.org/abs/2603.09673)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09673)

> 3DGS-SLAM在低纹理或反射表面易因光度误差不可靠而漂移，现有方法多依赖几何深度方差或预训练预测器，忽略了渲染本身的不确定性。VarSplat将外观方差作为高斯原语的一等参数，通过全方差定律在光栅化阶段直接渲染逐像素不确定性图，用于跟踪、配准与回环。该方法在ScanNet上取得6.53 cm ATE RMSE，较无不确定性基线降低20.2%，但在TUM-RGBD上精度（3.20 cm）仍低于RGS-SLAM（1.2 cm）。其价值在于首次将渲染不确定性内化为地图属性，但方差冻结策略对动态场景的适应性存疑。

## 研究背景

当相机在弱纹理墙面或玻璃表面移动时，3DGS渲染出的颜色对视角变化极度敏感，导致光度优化陷入局部极小值。这种不稳定性源于高斯原语仅编码均值颜色与几何位置，缺乏对观测可靠性的显式描述。为量化此问题，需区分几何不确定性（如深度噪声）与外观不确定性（如反射导致的颜色波动），后者直接反映渲染过程的不稳定，却长期被SLAM系统忽略。

传统3DGS-SLAM系统如SplaTAM与LoopSplat采用均匀光度加权，假设所有像素观测同等可靠。在低纹理区域，这种假设失效，导致位姿估计抖动与长序列漂移。现有鲁棒性方案多聚焦几何侧，如CG-SLAM建模深度方差，或Uni-SLAM使用终止概率场，但均未触及渲染外观本身的不确定性。预训练预测器（如WildGS-SLAM使用DINOv2）虽能生成不确定性图，但引入额外计算开销且依赖离线训练，难以在线端到端优化。VarSplat的切入点在于将外观方差直接嵌入高斯参数，使其与几何、颜色同步在线学习，从而在不增加光栅化次数的情况下，实时生成可微分的不确定性权重。

## 核心方法

### 方法参照系

VarSplat继承LoopSplat的子图增量建图架构，包含跟踪、子图优化、回环检测与配准四个阶段。标准流程中，每个高斯原语包含位置、协方差、不透明度、球谐系数（Spherical Harmonics, SH）颜色。本文的关键差异在于新增外观方差 $\sigma^2$ 参数，并在光栅化阶段通过全方差定律推导逐像素不确定性 $V$，将其作为光度损失的自适应权重。

### 外观方差学习与渲染

传统3DGS光栅化仅合成颜色与深度，忽略观测的统计波动。VarSplat为每个高斯 $G_i$ 引入外观方差 $\sigma_i^2 \in \mathbb{R}^3$，表示该高斯在不同视角下颜色观测的离散程度。基于全方差定律，逐像素不确定性 $V$ 分解为条件方差期望与条件期望方差之和：

$$ V = \sum_i w_i \sigma_i^2 + \sum_i w_i (c_i - \bar{c})^2 $$

其中 $w_i$ 为Alpha混合权重，$\bar{c}$ 为合成颜色均值。该公式表明，$V$ 不仅包含高斯自身的不确定性 $\sigma_i^2$，还包含不同深度高斯颜色差异引起的方差。在子图优化阶段，VarSplat使用高斯负对数似然损失训练 $\sigma_i^2$：

$$ \mathcal{L}_{var} = \frac{1}{2} \log V + \frac{1}{2V} (I - \hat{I})^2 $$

此设计确保 $\sigma_i^2$ 与残差统计特性一致，避免L1损失导致的方差估计偏差。通过单次光栅化同步渲染 $V$，系统无需额外采样或神经网络预测，保持实时性。

### 不确定性加权位姿估计

在跟踪阶段，VarSplat冻结 $\sigma_i^2$ 梯度，仅利用渲染出的 $V$ 计算像素权重 $w_p$。权重通过中位数对数缩放归一化：

$$ w_p = \exp\left(-\tau \log \frac{V_p}{\text{median}(V)}\right) $$

该权重调制光度损失，使低纹理或反射区域（$V$ 高）对位姿优化的贡献降低。在回环检测中，子图级可靠性权重由不透明度比值 $r = \alpha_{weighted}/\alpha_{original}$ 计算，抑制重复结构导致的误匹配。此机制无需手动掩码，自适应区分可靠与不可靠区域。

## 实验评估

实验在Replica、TUM-RGBD、ScanNet与ScanNet++四个数据集上进行，对比NeRF基线（GO-SLAM, NICE-SLAM等）与3DGS基线（SplaTAM, LoopSplat, CG-SLAM等）。基线覆盖全面，但缺乏动态场景专用方法（如RU4D-SLAM），限制了鲁棒性评估的广度。

| 数据集 | 方法 | ATE RMSE (cm) |
|---|---|---|
| ScanNet | VarSplat | 6.5 |
| ScanNet | LoopSplat | 7.7 |
| ScanNet | CG-SLAM | 8.1 |
| TUM-RGBD | VarSplat | 3.20 |
| TUM-RGBD | LoopSplat | 3.33 |
| TUM-RGBD | RGS-SLAM | 1.2 |

VarSplat在ScanNet上以6.5 cm ATE RMSE领先LoopSplat（7.7 cm）与CG-SLAM（8.1 cm），验证了外观方差对室内噪声场景的鲁棒性增益。在TUM-RGBD上，VarSplat（3.20 cm）优于LoopSplat（3.33 cm），但显著落后于RGS-SLAM（1.2 cm），表明在高质量数据下，一次性密集初始化可能比方差加权更有效。

| 消融配置 | Tracking | Loop | Registration | ATE RMSE (cm) |
|---|---|---|---|---|
| 无不确定性 | ✗ | ✗ | ✗ | 8.20 |
| 仅跟踪 | ✓ | ✗ | ✗ | 7.63 |
| 跟踪+回环 | ✓ | ✓ | ✗ | 7.49 |
| 全模块 | ✓ | ✓ | ✓ | 6.53 |

消融显示，全模块启用较无不确定性基线降低1.67 cm ATE RMSE，其中跟踪阶段贡献最大（0.57 cm），回环与配准提供额外增益。方差冻结策略（Table 9）证实，在跟踪阶段冻结 $\sigma^2$ 可避免与位姿优化的梯度冲突，提升轨迹稳定性。

评估协议使用ATE RMSE、PSNR、SSIM与LPIPS，但未报告计算效率（FPS）与地图大小，限制了实时性评估。代码已开源，但超参数（如 $\tau$）未详细披露，可复现性依赖补充材料。

## 关联研究分析

从问题动机看，VarSplat与CG-SLAM均针对低纹理鲁棒性，但CG-SLAM建模深度几何不确定性，依赖深度传感器精度；VarSplat建模外观不确定性，直接反映渲染波动，无需额外深度输入。这一差异源于任务特性：RGB-D系统中深度噪声与外观波动常相关，但反射表面深度准确而颜色不稳定，VarSplat的外观方差能捕捉此类场景，而CG-SLAM可能失效。

从方法设计看，VarSplat与Uni-SLAM同属不确定性加权框架，但Uni-SLAM使用终止概率场（NeRF特有），VarSplat使用学习方差（3DGS特有）。Uni-SLAM的方差来自射线终止概率，反映几何遮挡不确定性；VarSplat的方差来自高斯颜色波动，反映外观观测不确定性。两者互补，但VarSplat的在线学习特性使其更适配3DGS的显式表示，避免了Uni-SLAM对隐式场查询的依赖。

## 总结

VarSplat解决的核心矛盾是3DGS-SLAM在低纹理与反射表面的光度优化不稳定。现有方法依赖几何方差或预训练预测器，忽略了渲染外观本身的不确定性；VarSplat通过将 $\sigma^2$ 嵌入高斯参数并全方差定律渲染 $V$，实现了在线端到端的不确定性量化。实验证明，该设计在ScanNet上降低20.2% ATE RMSE，验证了外观方差对鲁棒性的贡献。然而，TUM-RGBD上精度落后于RGS-SLAM，暴露了方差计算开销可能挤占优化迭代次数的问题。当数据质量高且纹理丰富时，方差加权的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09673)