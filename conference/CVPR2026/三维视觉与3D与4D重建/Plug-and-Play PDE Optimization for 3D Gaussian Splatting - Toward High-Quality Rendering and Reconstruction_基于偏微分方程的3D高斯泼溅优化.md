# CVPR2026最新论文 ｜Plug-and-Play PDE Optimization for 3D Gaussian Splatting: Toward High-Quality Rendering and Reconstruction ｜基于偏微分方程的3D高斯泼溅优化

研究机构：中国科学技术大学

作者：Yifan Mo、Youcheng Cai、Ligang Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a01396aa265d)

> 3DGS在复杂场景中因小高斯位置梯度爆炸导致模糊与漂浮物，现有梯度裁剪或归一化策略虽能稳定训练但损失原始梯度信息。本文指出该优化过程可建模为偏微分方程（PDE），并引入粘滞项抑制突变运动。通过物质点法（MPM）求解该PDE，PDEO作为即插即用组件提升了新视角合成与表面重建质量。该方法在特定基线上有效，但未超越当前SOTA绝对值，且对初始点云缺失区域的重定位能力有限。

## 研究背景

3DGS通过显式各向异性高斯基元与可微光栅化实现实时渲染，但其优化过程依赖梯度下降更新高斯属性。当高斯尺度较小时，位置梯度幅值显著大于颜色、不透明度等其他属性梯度，导致小高斯在优化中发生剧烈位置突变。这种突变破坏了局部几何结构的稳定性，进而引发高频细节丢失与漂浮物伪影。

主流3DGS优化路线聚焦于密度控制与梯度约束。AbsGS等通过绝对梯度阈值调整分裂策略，MCMC等方法引入随机采样以逃逸局部最优。然而，针对梯度不稳定的常规手段如梯度裁剪、批量归一化（Batch Normalization, BN）及权重衰减，本质上是对梯度幅值的启发式截断或缩放，不可避免地造成原始梯度信息的损失。本文切入点在于不修改梯度本身，而是改变优化过程的物理动力学模型，从根源上抑制位置属性的突变。

## 核心方法

### PDE建模与粘滞项引入

3DGS优化通常被视为离散迭代过程，本文将其重构为连续时间下的PDE求解问题。高斯属性被视为时间的函数，位置更新速度 $v_i^t$ 由损失函数对位置的梯度决定。为抑制小高斯的速度突变，引入粘滞项，该术语源自流体模拟，通过局部平均速度约束粒子运动，防止相邻高斯间出现剧烈相对位移。

$$
\frac{d\mathbf{v}_i^t}{dt} = \frac{\partial \mathbf{v}_i^t}{\partial t} + \mathbf{v}_i^t \cdot \nabla \mathbf{v}_i^t = \frac{\sigma^2}{2} \sum_{\gamma_i^t \in \Gamma_i^t} \nabla \left( \frac{\partial L^t}{\partial \gamma_i^t} \right)^2
$$

该公式表明，速度场的变化率由所有属性梯度的空间导数决定，粘滞项隐含在速度场的扩散过程中，确保运动平滑性。

### MPM求解与粒子约束

直接计算每个高斯与邻居的粘滞交互计算量过大，本文采用物质点法（Material Point Method, MPM）求解PDE。MPM结合拉格朗日粒子与欧拉网格，通过粒子到网格（P2G）和网格到粒子（G2P）步骤实现全局与局部约束。P2G将粒子过剩速度存入体素网格，G2P利用网格速度场引导粒子运动，实现速度的平滑衰减与方向修正。

$$
\hat{\boldsymbol{\mu}}_i^t = \lambda_p \triangle \boldsymbol{\mu}_i^t + (1-\lambda_p) \mathbf{v}_n^t, \quad \boldsymbol{\mu}_i^{t+1} = \boldsymbol{\mu}_i^t + \triangle \hat{\boldsymbol{\mu}}_i^t
$$

其中 $\lambda_p$ 为速度抑制系数，$\mathbf{v}_n^t$ 为体素网格速度。此更新机制使粒子速度受局部平均运动趋势约束，避免单一高斯的孤立突变。此外，引入尺度损失（Scale Loss）惩罚大尺度高斯，置信度损失（Confidence Loss）强制不透明度趋近0或1，确保高斯符合PDE中“无尺度、高置信”的粒子假设。

## 实验评估

实验在Mip-NeRF 360、Tanks & Temples、ScanNet++及DTU上进行，基线涵盖3DGS、2DGS、RaDeGS、MCMC、SpecGS等。PDEO作为插件，在多数基线上提升了PSNR与SSIM，降低了LPIPS。例如，SpecGS+PDEO在Mip-NeRF 360上PSNR达28.81，高于SpecGS的27.96；RaDeGS+PDEO在Tanks & Temples表面重建F1-score达0.445，优于RaDeGS的0.316。

| 方法 | Mip-NeRF 360 PSNR | Mip-NeRF 360 SSIM | Mip-NeRF 360 LPIPS |
| :--- | :--- | :--- | :--- |
| 3DGS | 27.77 | 0.827 | 0.244 |
| SpecGS | 27.96 | 0.866 | 0.173 |
| SpecGS+PDEO | 28.81 | 0.875 | 0.173 |
| RaDeGS+PDEO | 28.16 | 0.852 | 0.213 |

消融实验显示，移除P2G/G2P导致PSNR从27.99降至27.51，证实MPM求解对稳定性的关键作用。移除尺度损失使LPIPS从0.232升至0.236，表明尺度约束对细节保留有效。$\lambda_g$ 设为0.8时性能最佳，0.5或0.9均导致性能下降，显示粘滞强度需精细调节。

评估边界方面，论文未报告训练时间对比，仅提及使用V100 GPU。代码未公开，超参数如 $\lambda_p=0.8$ 需手动调优。评估协议未包含前馈式方法（如QuerySplat）或最新压缩方法（如GS^2），限制了与当前SOTA的全面对比。

## 关联研究分析

从问题动机看，AbsGS通过绝对梯度阈值解决密度控制中的模糊问题，而PDEO从动力学稳定性角度解决小高斯位置突变。AbsGS关注“何时分裂”，PDEO关注“如何移动”。PDEO的粘滞项提供了全局速度场约束，而AbsGS的梯度阈值是局部决策，前者在复杂场景下可能更具鲁棒性，但计算开销更大。

从方法设计看，MCMC通过随机采样探索解空间，PDEO通过确定性PDE求解优化轨迹。MCMC依赖随机性逃逸局部最优，PDEO依赖物理约束平滑优化路径。PDEO的确定性更新可能更适合需要稳定收敛的表面重建任务，而MCMC在高度非凸损失景观中可能更具优势。两者结合是否优于单独使用，论文未探索。

## 总结

PDEO针对3DGS小高斯位置梯度爆炸导致的模糊与漂浮物问题，通过PDE建模与MPM求解引入粘滞约束，实现了稳定优化。在SpecGS基线上PSNR提升0.85，在RaDeGS基线上F1-score提升0.129，证明了方法的有效性。然而，论文承认PDEO无法可靠地将高斯从其他区域重定位到初始点云缺失区域，且未涉及粒子旋转。当初始点云存在大面积空洞时，PDEO的粘滞约束是否会阻碍高斯向空洞区域的必要迁移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_a01396aa265d)