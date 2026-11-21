# ICLR2026最新论文 ｜Hyperspherical Latents Improve Continuous-Token Autoregressive Generation ｜超球面潜变量连续自回归生成

研究机构：微软研究院

作者：Guolin Ke、Hui Xue

论文原文见 [arXiv](https://arxiv.org/abs/2509.24335)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24335)

> 连续Token自回归模型在解码时因潜变量尺度异质性导致方差坍缩，使其性能长期落后于扩散与掩码生成模型。现有方案通过增强KL正则或固定方差仅缓解症状，未消除尺度自由度这一根本原因。SphereAR将潜变量约束至固定半径超球面，强制所有输入输出尺度不变，从根源上阻断误差累积。该设计使纯Next-Token模型在同等参数量下首次超越扩散与掩码基线，但其对离散Token路线的替代性仍需多模态统一场景验证。

## 研究背景

当自回归模型处理连续视觉潜变量时，编码器输出的对角高斯后验导致各维度方差分布不均。这种尺度异质性在教师强制训练中被掩盖，但在自回归推理中，每一步预测的微小尺度偏差会随曝光偏差和分类器自由引导（CFG）被逐步放大，最终引发方差漂移与坍缩。为理解此机制，需区分离散与连续Token的本质差异：离散Token位于概率单纯形上，分量之和恒为1，天然具备尺度不变性；而连续高斯潜变量无此约束，径向分量成为误差累积的通道。

视觉自回归生成领域长期存在离散与连续Token的路线之争。离散Token路线（如LlamaGen）在同等规模下优于掩码生成模型，但受限于量化误差；连续Token路线（如LatentLM、GIVT）虽保留细节，却因方差坍缩导致性能不及扩散模型（DiT）和掩码生成模型（MAR）。现有缓解策略如增大KL权重或固定方差，仅压缩了方差范围，未消除尺度自由度，在CFG作用下仍会漂移。SphereAR的切入点在于识别尺度不变性为稳定自回归解码的必要条件，通过几何约束而非统计正则解决此问题。

## 核心方法

### 连续Token自回归参照系

连续Token自回归的标准流程为：VAE编码器将图像映射为对角高斯潜变量序列，因果Transformer预测下一Token，解码器重建图像。该流程的关键差异在于：本文问题聚焦于潜变量尺度自由度导致的解码不稳定，而非Token离散化或生成顺序优化。

### 超球面变分自编码器（S-VAE）

**设计动机**：对角高斯后验的尺度参数 $\sigma_\phi(x)$ 数据依赖且逐维度变化，导致AR解码中径向误差累积。S-VAE通过移除尺度自由度，使潜变量仅编码方向信息。

S-VAE将每个潜变量约束在半径 $R$ 的超球面 $S_{d-1}$ 上，编码器输出单位均值方向 $\boldsymbol{\mu} \in S_{d-1}$ 和浓度参数 $\kappa \geq 0$，参数化Power Spherical后验：

$$
q_\phi(\mathbf{u}|\mathbf{x}) \propto \exp(\kappa \boldsymbol{\mu}^\top \mathbf{u}), \quad \mathbf{u} \in S_{d-1}
$$

该分布保持球面支撑与旋转对称性，且支持无拒绝采样的重参数化。ELBO目标为：

$$
\mathcal{L}_{\text{S-VAE}} = \mathbb{E}_{q_\phi(\mathbf{u}|\mathbf{x})}[\log p_\psi(\mathbf{x}|\mathbf{z}=R\mathbf{u})] - D_{\text{KL}}[q_\phi(\mathbf{u}|\mathbf{x}) \| p(\mathbf{u})]
$$

其中先验 $p(\mathbf{u})$ 为球面均匀分布。相比高斯后验加事后归一化，S-VAE避免了径向KL项的冗余惩罚，且其轴对称几何结构与纯方向性数据更匹配。

### 尺度不变自回归解码

**设计动机**：即使使用S-VAE，推理时CFG缩放和数值误差仍可能引入径向分量，需强制投影以维持尺度不变性。

在自回归解码中，每步预测的临时Token $\mathbf{z}_k$ 经CFG缩放后，通过半径 $R$ 投影 $N_R(\mathbf{z}) = R\mathbf{z}/\|\mathbf{z}\|_2$ 归一化至超球面。该投影的微分是切空间正交投影，一阶消除径向扰动，仅保留切向（方向）误差。因此，尺度误差无法在自回归步骤间累积。扩散头采用Rectified Flow，预测速度场 $\mathbf{v}_\omega(\mathbf{z}_k^{(t)}, t, \mathbf{h}_{k-1})$，训练目标为：

$$
\mathcal{L}_{\text{flow}} = \mathbb{E}_{t, \mathbf{z}_k^{(0)}} \left\| \mathbf{v}_\omega(\mathbf{z}_k^{(t)}, t, \mathbf{h}_{k-1}) - (\mathbf{z}_k^{(1)} - \mathbf{z}_k^{(0)}) \right\|_2^2
$$

推理时积分速度场后执行单次投影，确保最终Token满足 $\|\mathbf{z}_k\|_2 = R$。

## 实验评估

实验在ImageNet-1K 256×256类别条件生成上进行，FID基于50k样本计算。基线覆盖离散AR（LlamaGen、RandAR、RAR）、连续AR（GIVT、LatentLM）、掩码生成（MaskGIT、MAGVIT-v2、MAR）、扩散（DiT、SiT）及Next-Scale（VAR）。缺失2026年最新SOTA如BAR（FID 1.15）和IAR2（FID 1.50），但覆盖了主要技术路线。

| 模型 | 类型 | 参数量 | FID↓ | IS↑ |
| :--- | :--- | :--- | :--- | :--- |
| VAR-d30 | N.S. | 2B | 1.92 | 323.1 |
| MAR-H | Mask. | 943M | 1.55 | 303.7 |
| DiT-XL/2 | Diff. | 675M | 2.27 | 278.2 |
| LatentLM-L | AR | 479M | 2.24 | 253.8 |
| SphereAR-B | AR | 208M | 1.92 | 277.8 |
| SphereAR-L | AR | 479M | 1.54 | 295.9 |
| SphereAR-H | AR | 943M | 1.34 | 300.0 |

SphereAR-H以1.34 FID领先所有对比模型，SphereAR-B（208M）匹配VAR-d30（2B）的1.92 FID，参数量减少约10倍。SphereAR-L（479M）优于同规模DiT-XL/2（2.27）和MAR-L（1.78），且接近MAR-H（1.55）但参数减半。

消融实验验证了S-VAE的核心作用。在相同骨干下，S-04（KL权重0.004）FID最低，且在高CFG下最稳定。对角高斯变体（G-01至G-16）随KL权重增加性能提升但饱和，且高CFG下不稳定。固定方差σ-VAE（F-01至F-05）与标准高斯性能相当，证明固定尺度无效。事后归一化高斯（N-01至N-16）优于对应高斯变体，但仍逊于S-VAE，证实超球面后验优于事后归一化。

| 变体 | 后验 | VAE解码器归一化 | AR归一化 | FID↓ | IS↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Gaussian | ✗ | ✗ | 2.97 | 240.2 |
| 2 | Gaussian | ✗ | ✓ | 2.89 | 254.3 |
| 3 | Gaussian | ✓ | ✗ | 2.68 | 257.3 |
| 4 | Spherical | ✓ | ✓ | 2.52 | 258.4 |

评估边界方面，论文未报告置信区间，FID比较需谨慎。代码已开源，但训练细节如GPU数量、总训练时长未完整披露。评估协议遵循ADM标准，但未覆盖开放域文本生成或视频生成任务，限制了结论的泛化性。

## 关联研究分析

从问题动机看，SphereAR与LatentLM同属连续Token AR路线，但LatentLM通过固定方差（σ-VAE）缓解不稳定，SphereAR则通过几何约束消除尺度自由度。这一差异源于对方差坍缩根源的不同诊断：LatentLM视其为方差过大问题，SphereAR视其为尺度异质性问题。实验证实后者更根本，因为固定方差在高CFG下仍漂移，而超球面约束保持稳定。

从方法设计看，SphereAR与VAR同属自回归生成，但VAR采用Next-Scale范式，SphereAR坚持Next-Token光栅顺序。这一选择挑战了“Next-Scale更优”的领域共识，其合理性在于尺度不变性使Next-Token在同等规模下具备竞争力。然而，VAR的层级生成天然适配多尺度细节恢复，SphereAR在高分辨率或动态宽高比场景下的表现未经验证。超球面连续Token如何适配现有LLM的离散词表接口，论文未给出回答。

## 总结

SphereAR要解决的核心矛盾是连续Token自回归解码中尺度异质性导致的方差坍缩。现有方法通过统计正则缓解症状，但未消除尺度自由度；SphereAR凭借超球面几何约束，从根源上阻断径向误差累积。该方法将潜变量约束至固定半径超球面，配合尺度不变解码，使纯Next-Token模型在ImageNet 256×256上以943M参数达到1.34 FID，208M参数匹配2B VAR的1.92 FID。其边界在于：实验仅覆盖类别条件生成，未验证开放域文本生成或视频生成；超球面约束在高分辨率下的误差传播机制未分析。当支持集从ImageNet扩展到多域数据时，超球面后验的浓度参数 $\kappa$ 是否需动态调整，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24335)