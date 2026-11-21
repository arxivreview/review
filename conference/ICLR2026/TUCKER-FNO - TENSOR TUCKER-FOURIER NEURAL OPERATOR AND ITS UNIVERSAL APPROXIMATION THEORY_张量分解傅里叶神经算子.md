# ICLR2026最新论文 ｜TUCKER-FNO: TENSOR TUCKER-FOURIER NEURAL OPERATOR AND ITS UNIVERSAL APPROXIMATION THEORY ｜张量分解傅里叶神经算子

作者：Guancheng Zhou、Zelin Zeng、Yisi Luo 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_44632740)

> 高维偏微分方程（PDEs）求解中，傅里叶神经算子（FNO）因全维快速傅里叶变换（FFT）导致计算复杂度随空间维度指数级增长，难以扩展至三维及以上场景。现有分解方法虽降低参数规模，却往往牺牲模型的通用逼近能力或引入额外计算开销。本文切入点在于利用张量Tucker分解将高维FNO解耦为多个一维FNO，在保持理论完备性的同时实现计算加速。该方法在Navier-Stokes方程上取得0.0028的归一化均方误差（NMSE），较FNO降低17.6%，但缺乏大规模预训练支持，其跨域泛化能力存疑。

## 研究背景

神经算子旨在直接学习无限维函数空间间的映射，以突破传统数值求解器在多查询场景下的实时性瓶颈。FNO通过在频域参数化积分核，利用FFT实现全局混合，确立了规则网格下的高效求解范式。然而，当空间维度 $d$ 增加时，FFT的计算复杂度达到 $O(d_v n^d \log n^d)$，其中 $d_v$ 为潜空间维度，$n$ 为网格分辨率。这种维度灾难使得FNO在处理三维PDE或高维视觉信号时效率骤降，成为阻碍其向高维科学计算应用扩展的核心障碍。

谱域算子架构是神经算子的主流路线，其核心优势在于分辨率不变性与全局信息捕捉能力。FNO及其变体（如U-FNO、Geo-FNO）在二维PDE基准上表现优异，但高维扩展性始终是未解难题。近期工作如T-FNO（Kossaifi et al., 2024）和D-FNO（Li & Ye, 2025）尝试通过权重分解或FFT分解降低计算量，但前者仅减少参数量而未显著降低计算复杂度，后者虽加速FFT却可能破坏FNO的通用逼近性质。本文针对这一矛盾，提出在算子层面引入张量Tucker分解，将高维频域混合拆解为低维操作，旨在同时解决计算效率与理论保证缺失的问题。

## 核心方法

### 方法参照系

FNO的标准流程包含提升层、频域混合层与投影层。频域混合层通过全维FFT将输入变换至频域，应用可学习的复数权重矩阵后逆变换回空域。这一设计实现了全局感受野，但全维FFT的 $O(n^d \log n^d)$ 复杂度在高维场景下成为瓶颈。本文问题与该通用流程的关键差异在于：不改变频域混合的本质，而是通过张量分解重构其计算路径，将高维变换分解为一系列一维变换。

### 张量Tucker分解算子架构

设计动机在于解决全维FFT在高维空间中的计算爆炸问题，同时避免简单分解导致的表达能力损失。Tucker-FNO将 $d$ 维FNO分解为 $d$ 个一维FNO的张量积形式。具体而言，输入张量 $\mathbf{I}$ 首先通过预提升模块 $P_{\hat{}}$ 提取为一系列一维因子矩阵 $\mathbf{I}_i$，每个因子矩阵经过对应的一维FNO $\mathcal{N}_i$ 处理后，通过核心张量 $C$ 聚合输出。其核心公式为：

$$
\mathcal{N}(\mathbf{I}) = C \times_1 \mathcal{N}_1(\mathbf{I}_1) \times_2 \mathcal{N}_2(\mathbf{I}_2) \cdots \times_d \mathcal{N}_d(\mathbf{I}_d)
$$

该公式表明，高维算子映射被分解为低维子算子的组合，其中核心张量 $C$ 编码了各维度间的交互信息。这种分解将FFT复杂度从 $O(d_v n^d \log n^d)$ 降至 $O(d d_v n \log n)$，在三维PDE上实现数量级的计算加速，同时通过保留核心张量维持了跨维度的信息交互能力。

### 通用逼近理论证明

设计动机在于回应分解型算子可能丧失理论保证的质疑，确立Tucker-FNO在函数空间中的表达能力边界。基于Stone-Weierstrass定理与函数张量分解理论，本文证明了Tucker-FNO具备通用逼近性。定理3指出，对于任意连续算子 $\mathcal{G}: H^s(T^d; \mathbb{R}) \to H^{s'}(T^d; \mathbb{R})$，在紧集 $\mathbf{F}$ 上，存在Tucker-FNO $\mathcal{N}$ 使得：

$$
\sup_{f \in \mathbf{F}} \|\mathcal{G}(f) - \mathcal{N}(f)\|_{H^s} \leq \epsilon
$$

该证明的关键在于将高维连续函数的逼近问题转化为一维因子函数的逼近问题，再通过一维FNO的通用逼近性质（Lemma 2）完成整体证明。这一结果填补了张量分解型神经算子的理论空白，表明Tucker-FNO在理论上能够逼近任意连续PDE解算子，为模型设计提供了坚实的数学基础。

## 实验评估

实验在Navier-Stokes、Burger及Plasticity方程上验证PDE求解性能，在Foreman与Carphone视频上验证信号恢复能力。基线覆盖FNO、T-FNO、D-FNO及ResNet，但缺失GNO、U-FNO等几何感知或U-Net结构基线，也未对比最新基础模型如MoE-POT。

| 方法 | Navier-Stokes NMSE | Burger NMSE | Plasticity NMSE |
| --- | --- | --- | --- |
| FNO | 0.0034 | 0.0070 | 0.0073 |
| T-FNO | 0.0035 | 0.0071 | 0.0073 |
| D-FNO | 0.0063 | 0.0075 | 0.0071 |
| Tucker-FNO | 0.0028 | 0.0070 | 0.0073 |

Tucker-FNO在Navier-Stokes上取得0.0028的NMSE，较FNO降低17.6%，优于T-FNO与D-FNO。在Burger与Plasticity方程上，Tucker-FNO与FNO性能持平，未展现显著优势，表明其加速效果在非线性较强的PDE上可能受限。

| 方法 | 参数量 (256×256) | 迭代时间 (256×256) |
| --- | --- | --- |
| FNO | 593.7 K | 0.0685 s |
| T-FNO | 232.6 K | 0.0746 s |
| D-FNO | 307.8 K | 0.0382 s |
| Tucker-FNO | 293.5 K | 0.0352 s |

Tucker-FNO参数量为293.5 K，较FNO减少50.4%；迭代时间0.0352 s，较FNO降低48.6%。消融实验显示，潜空间维度 $d_v$ 与频率截断阈值 $k$ 对性能呈正相关，但 $k$ 的鲁棒性更高。在信号恢复任务中，Tucker-FNO在Foreman视频（采样率0.1）上取得28.75 dB PSNR，较OINR-FNO的26.20 dB提升2.55 dB，验证了其在高维视觉数据上的有效性。

评估指标涵盖NMSE、VCE、PSNR、SSIM，但未报告置信区间或多次运行方差。代码已开源，但论文未提供GPU型号、训练轮数等复现细节。实验仅在规则网格上进行，未测试不规则几何或长时程预测场景，评估协议与领域主流基准（如PDEBench）存在差异。

## 关联研究分析

从方法设计看，Tucker-FNO与D-FNO均针对FFT计算瓶颈，但D-FNO侧重分解FFT运算本身，而Tucker-FNO在算子权重层面引入张量分解。这一差异源于任务特性：D-FNO关注计算图优化，Tucker-FNO关注表示效率。Tucker-FNO通过核心张量保留跨维交互，避免了D-FNO可能导致的表达能力损失，但引入了额外的预提升与后投影模块，增加了架构复杂度。

从理论保证看，Tucker-FNO与F-FNO（Tran et al., 2023）形成对比。F-FNO使用可分离谱层降低参数，但未提供通用逼近证明；Tucker-FNO则通过Stone-Weierstrass定理建立了严格的理论框架。这一差异反映了领域内对“效率-理论”权衡的不同取向：F-FNO追求工程实用，Tucker-FNO追求数学完备。然而，Tucker-FNO的理论证明依赖函数解析性假设，在实际非解析PDE解上的适用性未经验证，这一盲区可能限制其理论保证的实际价值。

## 总结

Tucker-FNO旨在解决高维FNO的计算复杂度瓶颈与理论保证缺失的双重矛盾。其切入点在于利用张量Tucker分解将高维频域混合解耦为一维操作，既实现了计算加速，又通过Stone-Weierstrass定理证明了通用逼近性。实验表明，该方法在Navier-Stokes方程上取得0.0028的NMSE，较FNO降低17.6%，同时参数量与迭代时间均减少约50%。然而，其在Burger与Plasticity方程上未展现性能优势，且实验局限于规则网格与单任务训练，缺乏大规模预训练支持。当Tucker-FNO应用于非解析PDE解或不规则几何场景时，其理论保证与实际性能是否依然成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_44632740)