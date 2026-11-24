# CVPR2026最新论文 ｜PoInit-of-View: Poisoning Initialization of Views Transfers Across Multiple 3D Reconstruction Systems ｜跨视图一致性破坏下的SfM初始化投毒

作者：Weijie Wang、Songlong Xing、Zhengyu Zhao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16540)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16540)

> 多视图三维重建系统依赖结构从运动（Structure-from-Motion, SfM）模块提供几何初始化，但现有对抗攻击仅针对单视图渲染损失，忽略了SfM作为几何核心的跨视图脆弱性。PoInit-of-View通过优化跨视图梯度不一致性损失，在不可感知扰动下导致SfM注册率崩溃，进而使下游重建系统全面失效。该方法证明了攻击点前移至几何前端可实现跨架构迁移，但其在弱纹理场景下的有效性及防御机制仍存疑。

## 研究背景

三维重建流水线中，SfM通过特征匹配与三角化建立稀疏点云与相机位姿，为后续稠密重建提供几何骨架。SfM的稳定性依赖于跨视图局部梯度与纹理结构的一致性，即对应区域在不同视角下保持相似的边缘与描述符特征。当输入图像发生微小扰动时，若仅破坏单视图内部特征，SfM的鲁棒性机制（如RANSAC）通常能过滤异常值；但若扰动破坏了跨视图间的几何对应关系，SfM将因内点率低于阈值而拒绝注册相机，导致几何骨架崩塌。

传统对抗攻击如NeRFool和Poison-Splat分别针对神经辐射场（Neural Radiance Fields, NeRF）的渲染损失和3D高斯泼溅（3D Gaussian Splatting, 3DGS）的稠密化过程，这些攻击假设SfM初始化是稳定且可信的，仅在后端优化阶段注入噪声。然而，SfM作为大多数重建系统的前端基础，其失效会导致下游所有模块失去几何约束，这种系统级失败比局部渲染质量下降更具破坏性。PoInit-of-View的切入点在于识别SfM初始化模块对跨视图不一致性的内在敏感性，将攻击目标从后端渲染质量前移至前端几何初始化，从而实现对多种重建架构的通用攻击。

## 核心方法

### 跨视图几何一致性约束

SfM通过本质矩阵约束对应点满足 $\mathbf{x}'^{\top} \mathbf{E} \mathbf{x} = 0$，其中 $\mathbf{E} = [\mathbf{t}]_{\times} \mathbf{R}$ 由相对旋转 $\mathbf{R}$ 和平移 $\mathbf{t}$ 导出。该约束要求对应像素在描述符空间中具有高度相似性，通常通过SIFT等局部描述符的最近邻匹配与互检建立候选对应，再经RANSAC验证。PoInit-of-View的核心假设是，若对应区域间的局部Sobel梯度差异超过阈值，描述符距离将指数级增大，导致匹配概率骤降，进而使SfM位姿图中的关键边失效。

### 跨视图梯度不一致性损失

针对SfM不可微的特性，PoInit-of-View引入可微3DGS代理模型，定义跨视图不一致性损失（Cross-View Inconsistency Loss, $L_{CVI}$）：

$$
L_{CVI} = \left\| \mathcal{G}(I_{R_i}) - \mathcal{G}(I_{A_j}) \right\|_1
$$

其中 $\mathcal{G}(\cdot)$ 表示Sobel梯度算子，$I_{R_i}$ 为参考视图，$I_{A_j}$ 为投毒目标视图。该损失直接量化对应区域间的梯度差异，迫使优化器生成破坏跨视图纹理一致性的扰动。设计动机在于，单视图攻击无法影响SfM的跨视图匹配逻辑，而 $L_{CVI}$ 直接针对SfM的核心约束机制，确保扰动在几何层面而非仅像素层面生效。

### 代理引导的投影梯度上升优化

由于SfM内部阈值与描述符不可访问，攻击者使用黑盒威胁模型，通过代理模型计算梯度。优化目标为最小化 $L_{CVI}$ 同时保持视觉不可感知性，采用投影梯度上升（Projected Gradient Ascent, PGD）更新投毒视图：

$$
\tilde{I}^{(t+1)} = \text{clip}\left( \tilde{I}^{(t)} + \alpha \cdot \text{sign}(\nabla_{\tilde{I}} L_{CVI}), I - \epsilon, I + \epsilon \right)
$$

其中 $\alpha$ 为步长，$\epsilon$ 为 $\ell_\infty$ 扰动预算。代理模型每 $K$ 次迭代刷新一次，以适配投毒视图变化导致的可见性差异。该机制解决了SfM黑盒环境下无法直接反向传播的问题，通过代理模型的微分近似获取跨视图不一致性梯度，实现了在不可感知扰动下最大化SfM注册率下降的目标。

## 实验评估

实验在NeRF-Synthetic、Tanks and Temples (T&T) 和 Mip-NeRF360 三个数据集上进行，对比基线包括高斯噪声、单视图攻击（NeRFool/IL2-NeRF）及结构上界（手动掩码关键点）。PoInit-of-View在T&T数据集上对Mip-Splatting的PSNR平均下降26.0%，SSIM下降18.4%，LPIPS上升92.4%，显著优于单视图基线的25.1% PSNR降幅和16.5% SSIM降幅。SfM统计量显示，投毒后注册图像比例从93.5%降至24.3%，三角化关键点从3.07k降至0.41k，3D点从0.90M降至0.88M，表明几何骨架严重崩塌。

| 方法 | PSNR (dB) | SSIM | LPIPS |
| :--- | :--- | :--- | :--- |
| Clean | 23.93 | 0.833 | 0.166 |
| Gauss. noise | 23.43 | 0.821 | - |
| Single-view | 23.53 | 0.819 | - |
| PoInit-of-View | 17.63 | 0.684 | 0.327 |

消融实验表明，移除SSIM正则化项导致PSNR从17.63升至19.4，但SfM注册率从24.3%升至27.1%，说明SSIM项在保持不可感知性的同时略微削弱了攻击强度；移除TV项则导致PSNR升至19.7，注册率升至28.0%，表明TV项对平滑扰动分布有贡献。代理模型刷新频率 $K$ 的影响未在正文中详细量化，但附录提及 $K=10$ 为默认设置。

评估边界方面，实验仅使用 $\ell_\infty$ 约束下的固定预算 $\rho=16/255$，未测试不同扰动幅度下的攻击成功率曲线。代码未公开，代理模型训练细节（如3DGS超参数）未完全披露，可复现性受限。指标仅关注渲染质量与SfM统计量，未评估下游任务（如导航、检测）的实际性能下降，缺乏端到端安全影响量化。

## 关联研究分析

从问题动机看，PoInit-of-View与NeRFool的根本差异在于攻击层级：NeRFool针对NeRF的体渲染损失，假设SfM位姿准确，仅破坏外观一致性；PoInit-of-View则针对SfM的几何初始化，破坏位姿与点云本身，导致下游所有模块失去基础。这种差异源于SfM作为多视图几何核心模块的特殊地位，其失效具有级联效应，而单视图攻击无法触发这种系统级崩溃。PoInit-of-View证明了攻击点前移至几何前端可实现跨架构迁移，这是单视图攻击无法做到的。

从方法设计看，PoInit-of-View与Poison-Splat均针对3DGS，但Poison-Splat通过破坏稠密化过程导致内存溢出（拒绝服务），而PoInit-of-View通过破坏SfM初始化导致几何错误（功能失效）。Poison-Splat依赖3DGS特有的高斯原语膨胀机制，而PoInit-of-View依赖SfM的通用几何约束，因此后者可迁移至MVS、NeRF等非3DGS系统。这种通用性源于SfM在多种重建流水线中的基础地位，而Poison-Splat的针对性则限制了其迁移范围。

## 总结

PoInit-of-View解决了现有对抗攻击忽略SfM初始化模块脆弱性的问题，通过跨视图梯度不一致性损失与代理引导的PGD优化，在不可感知扰动下导致SfM注册率崩溃，进而使下游重建系统全面失效。实验证明其在T&T数据集上PSNR下降26.0%，SfM注册率从93.5%降至24.3%，显著优于单视图基线。然而，实验仅在强纹理场景（T&T、Mip-NeRF360）上验证，未测试弱纹理或动态场景下的攻击有效性，且缺乏对SfM防御机制（如鲁棒特征匹配）的评估。当输入图像本身纹理稀疏时，SfM的初始匹配率已较低，跨视图不一致性是否仍能触发注册率崩溃，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16540)