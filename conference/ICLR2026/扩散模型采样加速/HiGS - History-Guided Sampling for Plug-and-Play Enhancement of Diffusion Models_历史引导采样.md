# ICLR2026最新论文 ｜HiGS: History-Guided Sampling for Plug-and-Play Enhancement of Diffusion Models ｜历史引导采样

作者：Seyedmorteza Sadat、Farnood Salehi、Romann M. Weber

论文原文见 [arXiv](https://arxiv.org/abs/2509.22300)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22300)

> 扩散模型在低步数采样或低引导尺度下常产生模糊且缺乏细节的图像，现有加速方法多聚焦于减少神经函数评估次数（NFE），却忽视了固定预算下的质量退化问题。HiGS 指出，采样轨迹的局部截断误差可通过复用历史预测信息加以修正，无需额外训练或前向传播。该方法将动量方差缩减机制引入去噪过程，利用当前预测与历史加权平均的偏差构建引导方向，并辅以频域滤波分离高频细节。其价值在于以零计算开销提升生成保真度，但理论收敛性证明与跨架构泛化边界仍存疑。

## 研究背景

扩散模型采样过程可统一视为对概率流常微分方程（Probability Flow ODE, PF-ODE）的数值积分，其中去噪网络 $D_\theta(z_t, t)$ 近似估计分数函数 $\nabla_{z_t} \log p_t(z_t)$。当步数压缩至个位数或引导尺度降低时，Euler 求解器的局部截断误差主导生成质量，导致图像模糊与结构缺失。Classifier-Free Guidance (CFG) 虽能提升语义对齐，但双倍前向传播成本与高尺度下的过饱和问题，使得低 NFE 与低 CFG 组合成为实时应用中的质量瓶颈。

主流加速路线分为数值求解器优化与模型蒸馏两类。DPM-Solver 等专用积分器利用 ODE 半线性结构降低单步误差，但在极低 NFE 下仍受限于截断误差累积；Consistency Models 通过蒸馏实现单步生成，却需额外训练且牺牲多样性。现有方法多假设“步数足够多即可精确逼近”，未充分利用采样轨迹中相邻时间步预测值的时间冗余性。HiGS 的切入点在于：将采样过程重新解释为时变能量函数上的随机梯度下降（SGD），并引入动量项修正梯度估计，从而在固定 NFE 下提升质量，而非单纯减少步数。

## 核心方法

### 方法参照系

标准扩散采样流程中，每步仅使用当前时刻 $t_k$ 的预测 $D_{CFG}(z_{t_k})$ 执行 Euler 更新，忽略历史预测信息。HiGS 的关键差异在于：将历史预测窗口 $H_k$ 纳入当前步的梯度估计，构建动量修正项，从而在不增加 NFE 的前提下改善轨迹收敛精度。

### 动量修正与历史引导

Euler 步可视为对时变能量函数 $E_t(z_t)$ 的梯度下降，学习率为 $h_k = t_k - t_{k+1}$。标准做法仅使用当前梯度 $\nabla E_{t_k}(z_{t_k})$，但 STORM 方差缩减理论表明，引入历史梯度差可稳定更新。HiGS 将当前 CFG 预测 $D_{CFG}(z_{t_k})$ 与历史加权平均 $g(H_k)$ 的偏差定义为引导方向：

$$
\Delta D_{t_k} = D_{CFG}(z_{t_k}) - g(H_k)
$$

其中 $g(H_k)$ 采用指数移动平均（EMA）计算，权重 $\alpha=0.75$。该设计动机在于：历史预测捕捉了轨迹的局部趋势，其偏差反映了当前步的“异常”成分，修正后可抑制截断误差累积。最终更新为 $D_{HiGS}(z_{t_k}) = D_{CFG}(z_{t_k}) + w_{HiGS}(t_k) \Delta D_{t_k}$，其中 $w_{HiGS}(t_k)$ 采用平方根调度，在低噪声阶段（$t \in [0.3, 1.0]$）增强修正强度。

### 频域滤波与正交投影

直接应用 $\Delta D_{t_k}$ 可能引入低频结构失真。HiGS 引入离散余弦变换（DCT）高频滤波，仅保留空间频率高于阈值 $R_c=0.05$ 的分量：

$$
\Delta D_{t_k} \leftarrow \text{iDCT}\left( H(R_c) \cdot \text{DCT}(\Delta D_{t_k}) \right)
$$

其中 $H(R_c)$ 为 sigmoid 掩码，锐度参数 $\lambda=50$。该设计动机在于：高频分量对应图像细节，低频分量对应全局结构，分离后可避免动量修正破坏语义一致性。此外，当投影权重 $\eta < 1$ 时，将 $\Delta D_{t_k}$ 分解为与 $D_{CFG}(z_{t_k})$ 正交和平行分量，仅保留正交部分，进一步抑制方向冲突。

## 实验评估

实验覆盖 ImageNet 256x256（DiT-XL/2, SiT-XL+REPA）、Stable Diffusion XL/3/3.5 及蒸馏模型（SDXL-Flash/Lightning），基线包括 CFG、DDIM、DPM++、PLMS、UniPC 等主流求解器，但缺失与 Consistency Models 或 DPM-Solver++ 的直接对比。主结果显示，HiGS 在固定 NFE 和 CFG 尺度下一致提升质量：

| 模型 | 引导方式 | FID↓ | IS↑ | Precision↑ | Recall↑ |
|---|---|---|---|---|---|
| SiT-XL + REPA | CFG | 12.08 | 187.11 | 0.68 | 0.73 |
| SiT-XL + REPA | HiGS | 4.86 | 277.20 | 0.80 | 0.70 |
| DiT-XL/2 | CFG | 8.73 | 173.21 | 0.72 | 0.68 |
| DiT-XL/2 | HiGS | 7.15 | 180.05 | 0.75 | 0.71 |
| Stable Diffusion XL | CFG | 28.49 | 35.07 | 0.56 | 0.54 |
| Stable Diffusion XL | HiGS | 26.18 | 36.22 | 0.59 | 0.57 |

SiT-XL+REPA 的 FID 从 12.08 降至 4.86，降幅达 60%，表明 HiGS 在低 NFE 下对质量退化有显著补偿作用。消融实验显示，EMA 平均优于随机或加权平均（HPSv2 0.255 vs 0.261/0.260），平方根调度优于常数或线性调度（ImageReward 0.39 vs 0.36/0.37），DCT 滤波提升 CLIP Score 0.003，验证了频域分离的必要性。

评估协议依赖 HPSv2 和 ImageReward 作为主要指标，FID 仅在 ImageNet 报告，可能低估复杂分布下的性能差异。代码未公开，但超参数（$\alpha=0.75, R_c=0.05, \lambda=50$）在附录中完整列出，GPU 为单卡，推理速度与 CFG 基线一致（6.50 迭代/秒），内存占用无增加。

## 关联研究分析

从问题动机看，HiGS 与 DeepCache 同属“时间冗余利用”路线，但目标不同：DeepCache 跳过中间层计算以降低 NFE，HiGS 复用历史预测以提升质量而不减少步数。DeepCache 依赖 U-Net 特征相似性，HiGS 依赖预测值的时间相关性，后者更适用于 Transformer 架构。从方法设计看，HiGS 与 DPM-Solver 形成互补：DPM-Solver 优化单步精度，HiGS 修正多步累积误差，Table 6 显示 HiGS 叠加于 DPM++ 后 FID 从 7.15 降至 6.66，证明其独立于求解器阶数的有效性。然而，HiGS 未与 Consistency Models 对比，后者在单步生成下 FID 可达 3.72（CIFAR-10），而 HiGS 在 30 步下 FID 为 1.61（ImageNet 256），两者在“少步生成”目标上存在竞争关系，但 HiGS 免训练且保留多样性，部署成本更低。

## 总结

HiGS 解决的核心矛盾是低 NFE 与低 CFG 下的质量退化，其切入点在于将采样过程解释为 SGD 并引入动量修正，利用历史预测信息免费提升梯度估计精度。方法通过 EMA 历史平均、DCT 高频滤波和正交投影构建引导方向，在固定 NFE 下显著改善生成质量。实验证明，SiT-XL+REPA 在 30 步无引导采样下 FID 达 1.61，较基线 1.83 降低 12%，且无需额外训练或前向传播。其边界在于：理论收敛性仅证明局部截断误差从 $O(h^2)$ 降至 $O(h^3)$，未提供全局误差界；DCT 滤波参数 $R_c$ 和 $\lambda$ 需手动调优，跨架构泛化性未充分验证。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22300)