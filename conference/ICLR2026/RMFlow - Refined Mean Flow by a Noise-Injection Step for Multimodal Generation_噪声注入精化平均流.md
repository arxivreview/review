# ICLR2026最新论文 ｜RMFlow: Refined Mean Flow by a Noise-Injection Step for Multimodal Generation ｜噪声注入精化平均流

研究机构：美国犹他大学、美国加州大学洛杉矶分校

作者：Yuhao Huang、Shih-Hsin Wang、Andrea L. Bertozzi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00849)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00849)

> 流匹配（Flow Matching, FM）的单步生成（1-NFE）面临质量瓶颈，现有平均流（MeanFlow）方法在极限效率下常产生分布退化或无效结构。本文切入点在于识别出确定性传输缺乏随机性导致的似然最大化缺失，通过引入VAE式噪声注入步骤与联合损失函数解决该问题。RMFlow在保持1-NFE计算成本的同时，显著提升了多模态生成的保真度。其价值在于理论闭环与工程可行性的结合，但固定噪声参数与单步限制仍制约其通用性。

## 研究背景

流匹配通过回归确定性常微分方程（ODE）的速度场实现分布传输，其核心优势在于训练无需模拟随机轨迹。然而，推理阶段需多次评估神经网络以积分ODE，导致延迟高企。为突破此瓶颈，平均流（MeanFlow）通过估计时间步间的平均速度场，将多步积分压缩为单次前向传播，实现了1-NFE生成的理论可行性。

MeanFlow在少步生成中表现优异，但实验表明，当NFE降至1时，生成质量出现显著退化。在混合高斯采样中，1-NFE MeanFlow的总变差（TV）距离高达0.238，远高于32-NFE的0.155；在QM9分子生成中，1-NFE MeanFlow频繁产生断裂的无效结构。这一现象源于确定性ODE缺乏探索性，导致模型无法在低噪声区域有效修正表示退化，且标准FM损失仅最小化Wasserstein距离，未包含似然最大化项，致使学习分布与目标分布的KL散度无法受控。

本文针对1-NFE MeanFlow的分布退化问题，提出RMFlow（Refined Mean Flow）。其核心思想是将生成过程分解为粗传输与精化两阶段：先通过1-NFE MeanFlow将先验传输至中间状态，再通过单步噪声注入精化最终样本。这一设计借鉴变分自编码器（VAE）的随机性，旨在通过引入随机过程支持似然最大化，从而在保持单步效率的同时提升生成保真度。

## 核心方法

### 方法参照系

MeanFlow通过训练神经网络 $\hat{u}_{t,r}(x;\theta)$ 近似平均速度场，实现从 $x_t$ 到 $x_r$ 的直接映射。1-NFE生成对应 $x_1 = x_0 + \hat{u}_{0,1}(x_0;\theta)$。该范式的关键差异在于，标准MeanFlow直接输出确定性样本，而RMFlow在输出前引入随机精化步骤，将确定性ODE转化为随机过程，以弥补似然最大化能力的缺失。

### 噪声注入精化机制

MeanFlow的确定性输出导致生成样本缺乏多样性，且在低噪声区域易陷入局部最优。RMFlow在MeanFlow传输后引入单步噪声注入，将中间状态 $x_{int}$ 精化为最终样本 $x_{final}$。该步骤的物理含义是：通过添加可控噪声，为模型提供“修正”机会，使其能够探索目标分布的高概率区域，而非仅停留在确定性轨迹的终点。

$$
x_{final} = x_{int} + \sigma_{min} \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)
$$

其中 $x_{int} = x_0 + \hat{u}_{0,1}(x_0;\theta)$ 为MeanFlow传输结果，$\sigma_{min}$ 为固定小常数（如 $10^{-3}$）。这一设计使得生成过程成为随机过程，从而支持基于证据下界（ELBO）的似然最大化训练。

### 联合训练目标

标准MeanFlow损失 $\mathcal{L}_{CMFM}$ 仅控制Wasserstein距离，无法保证KL散度最小化。RMFlow引入负对数似然损失 $\mathcal{L}_{NLL}$，与 $\mathcal{L}_{CMFM}$ 联合优化，以同时控制分布对齐与似然最大化。该联合目标的物理含义是：在保持传输路径几何一致性的同时，最大化学习分布对目标数据的拟合能力。

$$
\mathcal{L}_{RMFlow} = \mathcal{L}_{CMFM} + \lambda_1 \mathcal{L}_{NLL} + \lambda_2 \mathcal{L}_{guide}
$$

其中 $\mathcal{L}_{NLL}$ 由ELBO推导，$\mathcal{L}_{guide}$ 为条件生成正则项（无条件时设为0）。定理4.1证明，最小化 $\mathcal{L}_{NLL}$ 可控制目标分布 $p_{tgt}$ 与学习分布 $p_\theta$ 之间的KL散度，从而解决MeanFlow在1-NFE下的分布退化问题。

## 实验评估

实验在COCO、QM9、Lorenz/FitzHugh-Nagumo系统上进行，对比MeanFlow（1/8/32-NFE）、Diffusion、FM等基线。基线覆盖映射学习与轨迹优化路线，但缺失SoFlow、Decoupled MeanFlow等最新1-NFE方法，限制了绝对性能的横向比较。

| 任务 | 指标 | 1-NFE MeanFlow | 8-NFE MeanFlow | 32-NFE MeanFlow | 1-NFE RMFlow |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 混合高斯 | TV | 0.238 | 0.167 | 0.155 | 0.173 |
| 混合高斯 | KL | 0.311 | 0.139 | 0.118 | 0.163 |
| 棋盘密度 | TV | 1.4422 | 0.7977 | 0.6737 | 0.7567 |
| 棋盘密度 | KL | 0.8074 | 0.4074 | 0.1017 | 0.2332 |

在混合高斯采样中，1-NFE RMFlow的TV（0.173）优于1-NFE MeanFlow（0.238），接近8-NFE MeanFlow（0.167）；在棋盘密度任务中，RMFlow的TV（0.7567）显著优于MeanFlow（1.4422），接近32-NFE的0.6737。QM9分子生成中，1-NFE RMFlow达到SOTA水平，而MeanFlow产生无效结构。COCO文本到图像生成中，RMFlow FID为18.91，优于MeanFlow的27.31，但低于InstaFlow的13.10（512×512分辨率）。

消融实验显示，噪声注入步骤对性能提升至关重要。移除 $\mathcal{L}_{NLL}$ 后，生成质量显著下降，验证了似然最大化项的必要性。固定 $\sigma_{min}$ 的设计在低噪声区域有效，但论文未探索自适应调度，可能限制其在高维复杂分布下的泛化能力。

评估协议使用FID、TV、KL等标准指标，但缺乏置信区间报告，数值比较需谨慎。代码未公开，超参数（如 $\lambda_1, \lambda_2$）未在正文中详细列出，可复现性受限。实验在RTX 3090/4090 GPU上进行，计算资源有限，可能影响大规模任务的最终性能。

## 关联研究分析

从问题动机看，RMFlow与SoFlow、Decoupled MeanFlow同属1-NFE生成路线，但解决路径不同。SoFlow通过一致性损失从零训练单步生成，Decoupled MeanFlow通过解耦设计复用预训练模型，而RMFlow通过噪声注入精化MeanFlow。RMFlow的差异在于其理论目标：SoFlow和Decoupled MeanFlow聚焦于消除离散化误差，而RMFlow聚焦于似然最大化。这一差异源于任务特性：分子生成等科学计算任务对结构有效性要求高，确定性输出易产生无效结构，而噪声注入提供了结构修正的随机性。

从方法设计看，RMFlow与Diff2Flow、Generator Matching同属流与扩散的结合，但机制不同。Diff2Flow通过知识迁移将扩散模型能力注入流匹配，Generator Matching在马尔可夫生成过程中连接两者，而RMFlow在结构层面融合噪声注入。RMFlow的设计更轻量，无需预训练教师模型或架构变更，但牺牲了确定性轨迹的简洁性。查询侧增强在数据充足时是否仍有增益，论文未给出回答，这限制了其在大规模图像生成中的潜在优势。

## 总结

RMFlow针对1-NFE MeanFlow的分布退化问题，通过噪声注入精化与联合损失函数，实现了似然最大化与Wasserstein控制的平衡。其核心贡献在于理论闭环：定理4.1证明了噪声注入步骤对KL散度的控制能力，实验验证了其在混合高斯、QM9、COCO等任务上的显著改进，如混合高斯TV从0.238降至0.173，COCO FID从27.31降至18.91。然而，固定 $\sigma_{min}$ 的设计与单步限制暴露了其边界：在低噪声区域，固定噪声可能不足以应对高维复杂分布的表示退化；单步精化无法捕捉多步传输中的动态变化。当支持集增大或分布复杂度提升时，固定噪声参数的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00849)