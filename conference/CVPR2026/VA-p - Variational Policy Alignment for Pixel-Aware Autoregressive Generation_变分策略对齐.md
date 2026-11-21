# CVPR2026最新论文 ｜VA-p: Variational Policy Alignment for Pixel-Aware Autoregressive Generation ｜变分策略对齐

研究机构：新加坡国立大学

作者：Xinyao Liao、Qiyuan He、Kai Xu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_501142040e6c)

> 自回归视觉生成中，Tokenizer 的重建目标与生成器的似然目标分离，导致高似然 Token 序列解码后偏离图像流形。现有噪声正则化或外部奖励模型方法要么计算昂贵，要么仅缓解而非根除该错位。VA-π 将像素重建质量作为内在奖励，通过变分策略优化直接对齐生成器与像素分布。该方法在 LlamaGen-XXL 上以 1% 数据实现 FID 从 14.36 降至 7.65，但其在 Next-Scale 架构及高分辨率场景下的泛化能力尚未验证。

## 研究背景

自回归视觉生成依赖离散 Tokenizer 将图像映射为序列，再训练 AR 模型预测 Token 分布。这一两阶段流程存在根本性错位：Tokenizer 优化像素级重建，而 AR 模型仅优化 Token 似然。当 AR 模型在自由运行模式下采样时，早期预测误差会累积，生成“离流形”的 Token 序列，解码后产生视觉伪影。这种错位源于训练目标的不一致，而非单一组件的缺陷。

主流解决方案分为两类：生成器中心方法通过向 Token 序列注入噪声或随机化顺序来增强鲁棒性，但需重新训练且未直接解决像素对齐；Tokenizer 中心方法调整解码器以容忍离流形序列，但仅使解码器更宽容，未阻止生成器产生错误序列。这些方法均缺乏对像素空间分布的直接监督，且计算开销大。VA-π 的切入点在于将 AR 生成器视为策略，利用 Teacher Forcing 下的重建损失作为内在奖励，通过变分优化直接对齐像素分布，无需外部奖励模型或昂贵的自由运行采样。

## 核心方法

### 方法参照系

标准 AR 视觉生成流程包含 Tokenizer 训练与 AR 模型训练两个阶段。Tokenizer 通过编码器、量化器和解码器实现图像与离散 Token 的双向映射，损失函数包含重建损失与量化损失。AR 模型通过 Teacher Forcing 最大化观测序列的对数似然。本文的关键差异在于：不修改 Tokenizer 或 AR 模型的预训练目标，而是在后训练阶段引入像素空间分布对齐机制，将离散 Token 序列视为像素图像的潜变量。

### 变分下界推导

设计动机：直接优化像素似然 $p(I)$ 因离散 Token 空间的积分项不可解而不可行。VA-π 引入变分后验 $q_{\psi,\theta}(x|I)$，将像素似然分解为可优化的证据下界（ELBO）。

$$
\log p(\mathbf{I}; \theta, \psi, \phi) \geq \mathbb{E}_{q_{\psi,\theta}(\mathbf{x}|\mathbf{I})} [\log p_\psi(\mathbf{I}|\mathbf{x})] - \mathrm{KL}(q_{\psi,\theta}(\mathbf{x}|\mathbf{I}) \| \pi_\theta(\mathbf{x}))
$$

该公式表明，最大化 ELBO 等价于最小化重建损失与 KL 散度之和。重建项确保解码图像接近原始图像，KL 项约束策略 $\pi_\theta$ 不偏离预训练分布，防止策略崩溃。

### 强化学习策略优化

设计动机：ELBO 中的重建项涉及离散采样，梯度无法直接回传。Straight-Through Estimator (STE) 虽提供连续近似，但忽略类别分布的采样概率，导致目标偏差。VA-π 将重建损失转化为奖励信号，采用 Group Relative Policy Optimization (GRPO) 进行策略优化。

$$
\mathcal{J}_{\text{GRPO}}(\theta) = \mathbb{E}_{\mathbf{q}, \mathbf{o} \sim \pi_{\theta_{\text{old}}}} \left[ \frac{1}{G} \sum_{i=1}^{G} \min(\rho_i \hat{A}_i, \text{clip}(\rho_i, 1-\epsilon, 1+\epsilon) \hat{A}_i) - \beta D_{\mathrm{KL}}(\pi_\theta \| \pi_{\text{ref}}) \right]
$$

其中 $\hat{A}_i$ 为组内归一化优势，$\rho_i$ 为策略比率。该公式通过裁剪机制稳定训练，KL 正则项保留预训练先验。奖励函数定义为 Teacher Forcing 下的负重建损失，即 $R(o, q) = -\mathcal{L}_{\text{rec}}(D(x), I)$，确保梯度覆盖所有采样序列而非仅真实路径。

## 实验评估

实验在 ImageNet-1K (256x256) 上进行，基线包括 LlamaGen-XXL 和 AR-GRPO。VA-π 在 LlamaGen-XXL 上实现 FID 从 14.36 降至 7.65，IS 从 86.55 升至 116.70，无需分类器自由引导。在文本到图像任务中，LlamaGen 的 GenEval 分数从 0.306 提升至 0.339，Janus-Pro 从 0.725 提升至 0.744。

| 模型 | FID | IS | GenEval (LlamaGen) | GenEval (Janus-Pro) |
| :--- | :--- | :--- | :--- | :--- |
| LlamaGen-XXL | 14.36 | 86.55 | 0.306 | 0.725 |
| + AR-GRPO | — | — | 0.274 | 0.208 |
| + VA-π | 7.65 | 116.70 | 0.339 | 0.744 |

注：AR-GRPO 的 FID/IS 未在数据区提供，仅列出 GenEval 对比。VA-π 的计算成本仅为 AR-GRPO 的 13.4%，训练时间 25 分钟（8×A100）。

消融实验显示，VA-π 无需外部奖励模型即可超越 AR-GRPO 在 CLIP 和 HPS v2 上的对齐分数。设计决策验证表明，Teacher Forcing 下的奖励信号足以覆盖自由运行时的误差累积场景，但论文未提供不同噪声水平下的消融数据。

评估边界：指标仅覆盖 FID/IS/GenEval，缺乏多样性与组合性指标。可复现性方面，代码已开源，但超参数细节未在正文中完整列出。

## 关联研究分析

从问题动机看，VA-π 与噪声正则化方法（如 [13, 15]）均针对 Tokenizer-生成器错位，但前者通过修改训练目标增强鲁棒性，后者通过直接对齐像素分布根除错位。VA-π 的优势在于无需重新训练 Tokenizer，且计算效率更高，但其依赖 Teacher Forcing 下的重建损失，可能无法完全捕捉自由运行时的动态误差累积。

从方法设计看，VA-π 与 AR-GRPO 同属 RL 后训练框架，但 VA-π 使用内在奖励（重建损失）替代外部奖励模型，避免了奖励模型与生成目标的潜在冲突。然而，VA-π 基于 Next-Token 架构（LlamaGen），未验证在 Next-Scale 架构（如 VAR）上的有效性。若 Next-Scale 的层级生成已部分解决全局一致性问题，VA-π 的像素对齐增益可能递减，这一假设论文未探索。

## 总结

VA-π 解决的核心矛盾是 AR 生成器似然目标与 Tokenizer 重建目标的分离。其切入点在于将像素重建质量转化为内在奖励，通过变分策略优化直接对齐分布，避免了外部奖励模型的依赖与自由运行采样的高成本。该方法在 LlamaGen-XXL 上以 1% 数据实现 FID 从 14.36 降至 7.65，证明了像素空间对齐的有效性。然而，实验仅覆盖 Next-Token 架构，未验证在 Next-Scale 范式下的泛化能力。当生成顺序从线性序列变为层级尺度时，Teacher Forcing 下的重建奖励是否仍能有效捕捉跨尺度误差累积，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_501142040e6c)