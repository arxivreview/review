# ICLR2026最新论文 ｜SuperF: Neural Implicit Fields for Multi-Image Super-Resolution ｜多图像超分辨率中的隐式神经场联合优化

研究机构：丹麦哥本哈根大学

作者：Sander Riisøen Jyhne、Christian Igel、Morten Goodwin 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09115)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09115)

> 多图像超分辨率（Multi-Image Super-Resolution, MISR）旨在利用多帧亚像素位移互补信息重建高分辨率图像，以规避单图方法因学习先验导致的结构幻觉。现有测试时优化（Test-Time Optimization, TTO）方法依赖显式对齐或固定核回归，难以在连续坐标空间内精确捕捉亚像素位移，导致高频细节恢复受限。SuperF 通过共享隐式神经表示（Implicit Neural Representation, INR）并联合优化仿射变换参数，实现了无训练数据约束下的连续信号重建。该方法在卫星与手持相机场景中验证了有效性，但其逐样本优化范式在计算效率上尚未解决实时部署瓶颈。

## 研究背景

卫星遥感与手持摄影常受限于传感器物理分辨率，单图超分辨率（Single-Image Super-Resolution, SISR）虽能提升视觉质量，但依赖大规模高分辨率（HR）训练数据，易产生偏离真实场景的“幻觉”结构，这在医学或科学应用中不可接受。MISR 利用多帧低分辨率（LR）图像间的亚像素位移差异，将离散化引入的混叠伪影转化为互补信息，从而在无需 HR 先验的情况下重建底层信号。隐式神经表示（INR）作为坐标基神经网络，通过多层感知机（MLP）将连续坐标映射至信号强度，其连续特性天然适配亚像素对齐需求，但传统 INR 存在频谱偏置，优先拟合低频分量，导致高频细节恢复缓慢。

主流 MISR 路线分为监督学习与 TTO 两类。监督方法如 Bhat et al. (2021) 依赖配对数据，难以获取；TTO 方法如 Wronski et al. (2019) 采用可导向核回归，但需显式对齐步骤，且对齐误差直接限制重建上限。Nam et al. (2022) 提出的 NIR 方法虽引入 INR，但通过独立 MLP 估计变换矩阵，未直接参数化对齐过程，导致亚像素精度不足。SuperF 的切入点在于将对齐与表示解耦为联合优化问题：直接在连续坐标空间中优化仿射变换参数，同时共享 INR 权重，从而消除显式对齐步骤，并利用超采样策略克服频谱偏置，实现无训练数据下的高保真重建。

## 核心方法

### 方法参照系

标准 INR 用于图像重建时，通常采用监督学习范式：预训练 MLP 映射坐标至 RGB，推理时固定网络权重。本文问题与该通用流程的关键差异在于：输入为多帧未对齐的 LR 图像，且无 HR 训练数据。因此，SuperF 将 INR 从“固定映射器”转变为“可优化表示”，其核心在于对齐参数与网络权重在测试时同步更新，而非离线训练后冻结。

### 联合对齐与共享 INR 优化

传统 TTO 方法先执行显式对齐再重建，导致对齐误差累积。SuperF 将每帧 LR 图像视为共享 INR 的观测目标，直接参数化仿射变换矩阵 $\hat{\mathbf{A}}^{(t)}$ 作为可优化变量。对于第 $t$ 帧，输入坐标 $\mathbf{v}$ 经变换后输入 MLP $f_\theta$，输出经 boxcar 滤波下采样后与 LR 目标 $\mathbf{y}^{LR[(t)]}$ 匹配。损失函数定义为多帧平均点状误差：

$$
\mathcal{L}(\theta, \hat{\mathbf{A}}) = \frac{1}{T} \sum_{t=1}^{T} \sum_{\mathbf{v} \in W} \ell \left( \left( \phi * f_\theta(\hat{\mathbf{A}}^{(t)} \mathbf{v}) \right)_{\mathbf{v}}, \mathbf{y}^{LR[(t)]}(\mathbf{v}) \right)
$$

该公式的物理含义是：通过最小化 INR 在 HR 网格上的输出与 LR 观测之间的差异，同时驱动网络权重 $\theta$ 学习底层 HR 信号，并驱动变换参数 $\hat{\mathbf{A}}^{(t)}$ 收敛至真实亚像素位移。设计动机在于，直接参数化变换矩阵避免了 Nam et al. (2022) 中独立 MLP 估计变换的间接性，使对齐误差与重建误差在同一优化目标中耦合，从而提升亚像素精度。

### 超采样与不确定性估计

INR 的频谱偏置导致 MLP 优先拟合低频，难以恢复多帧 LR 中捕获的高频细节。SuperF 引入超采样策略：在 HR 分辨率网格上计算 INR 输出，再通过平均池化下采样至 LR 分辨率进行监督。此过程迫使网络在优化初期即关注高频分量，因为低频分量在下采样后变化微小，而高频分量差异显著。此外，针对真实数据中的噪声（如云层），SuperF 扩展 MLP 输出维度，预测每帧每通道的方差 $\sigma_t^2$，采用高斯负对数似然（GNLL）损失：

$$
\mathcal{L}_{GNLL} = \frac{1}{2} \sum_{t=1}^{T} \sum_{\mathbf{v} \in W} \left( \frac{\| f_\theta(\mathbf{v}) - \mathbf{y}^{LR[(t)]}(\mathbf{v}) \|^2}{\sigma_t^2(\mathbf{v})} + \log \sigma_t^2(\mathbf{v}) \right)
$$

该公式允许模型在噪声像素处增大方差以最小化损失，而非强行拟合错误值，从而提升对遮挡或光照变化的鲁棒性。设计动机在于，MSE 损失假设恒定方差，无法区分“可恢复误差”与“不可恢复噪声”，GNLL 通过自适应方差估计实现了噪声感知优化。

## 实验评估

实验基于自建的 SatSynthBurst（卫星合成爆发数据）与 SyntheticBurst（手持相机数据），放大倍率涵盖 ×2 至 ×8，每帧 16 或 14 张 LR 图像。基线覆盖双线性插值、Lafenetre et al. (2023) 的 TTO 方法、Nam et al. (2022) 的 NIR 方法（2k 与 5k 迭代）。缺失 SISR 领域强基线（如 SwinIR、EchoSR），因任务设定不同（MISR 无训练数据 vs SISR 有训练数据），直接对比无效，但缺失了同为 TTO 的其他 INR 变体对比。

| 方法 | SatSynthBurst ×4 PSNR (dB) | SyntheticBurst ×4 PSNR (dB) |
|---|---|---|
| Bilinear | 29.71 (3.64) | 26.12 (3.72) |
| Lafenetre et al. [2023] | 27.70 (3.79) | 26.46 (3.05) |
| NIR [Nam et al., 2022] [5k] | 24.63 (4.41) | 22.69 (4.41) |
| SuperF GNLL (ours) [2k] | 34.03 (2.71) | 27.47 (4.18) |

SuperF GNLL 在 SatSynthBurst ×4 上 PSNR 达 34.03 dB，显著优于 NIR [5k] 的 24.63 dB（提升 9.40 dB）及 Lafenetre et al. 的 27.70 dB（提升 6.33 dB）。在 SyntheticBurst ×4 上，SuperF GNLL 为 27.47 dB，优于 NIR [5k] 的 22.69 dB（提升 4.78 dB），但提升幅度小于卫星场景，表明手持相机噪声模型对 INR 优化影响更大。

消融实验显示，移除傅里叶特征（FF）导致 SatSynthBurst ×4 PSNR 从 32.94 dB 降至 20.33 dB（下降 12.61 dB），证实频谱偏置是主要瓶颈。移除多帧共享（单帧）导致 PSNR 降至 30.42 dB，移除对齐优化导致 PSNR 降至 28.11 dB，表明联合对齐与多帧共享贡献相当。值得注意的是，NIR 基线加入直接参数化变换（Direct_T）后，对齐误差从 0.650 降至 0.012，但 PSNR 仅从 24.63 升至 26.14 dB，说明对齐精度提升未直接转化为重建质量，需配合超采样策略（SS）才能将 PSNR 提升至 31.30 dB，最终 SuperF 全组件达 32.94 dB。

评估指标包含 PSNR、SSIM、LPIPS，但未报告推理时间或内存占用，无法评估 TTO 范式的实时性。代码发布于项目页面，但超参数（如傅里叶特征尺度 $\sigma$）需按域调整，论文指出卫星与手持相机最优 $\sigma$ 不同，限制了跨域泛化性。

## 关联研究分析

从问题动机看，SuperF 与 LIIF (Chen et al., 2021) 同属 INR 框架，但 LIIF 采用监督学习，依赖 HR 训练数据学习嵌入，而 SuperF 采用 TTO，无训练数据。LIIF 的局部 INR 锚定于最近邻嵌入，适合固定尺度推理；SuperF 的全局 INR 联合优化对齐，适合多帧亚像素场景。差异根源在于任务特性：SISR 有充足训练数据，监督学习高效；MISR 数据稀缺，TTO 避免幻觉。SuperF 未探索混合范式（如预训练对齐模块+TTO 重建），这可能是在数据充足场景下的潜在优化方向，但论文未给出回答。

从方法设计看，SuperF 与 Nam et al. (2022) 的 NIR 均使用 INR，但 NIR 通过独立 MLP 估计变换矩阵，SuperF 直接参数化仿射变换。NIR 的设计源于爆发融合任务，对齐精度非核心目标；SuperF 针对 MISR，对齐精度决定重建上限。SuperF 的超采样策略借鉴自 NeRF 中的细节增强技术，但应用于图像重建而非新视角合成。差异根源在于目标函数：NIR 优化层分离，SuperF 优化信号重建，后者对高频细节更敏感。SuperF 未讨论超采样对优化收敛速度的影响，2000 次迭代是否足够收敛，论文未提供收敛曲线。

## 总结

SuperF 解决的核心矛盾是 MISR 中无 HR 训练数据约束下的结构幻觉风险与亚像素对齐精度不足。现有 TTO 方法依赖显式对齐或固定核回归，无法在连续空间内精确捕捉位移；SuperF 凭借 INR 的连续特性，将对齐与表示联合优化，直接参数化仿射变换并引入超采样克服频谱偏置。实验证明，在 SatSynthBurst ×4 上 PSNR 达 34.03 dB，较 NIR 基线提升 9.40 dB，验证了联合优化的有效性。然而，论文未报告推理时间，2000 次迭代的计算成本是否满足实时部署需求，以及跨域超参数（如 $\sigma$）的自动化调整策略，仍是未解决的工程瓶颈。当支持帧数增加至 32 或 64 时，联合优化的收敛稳定性是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09115)