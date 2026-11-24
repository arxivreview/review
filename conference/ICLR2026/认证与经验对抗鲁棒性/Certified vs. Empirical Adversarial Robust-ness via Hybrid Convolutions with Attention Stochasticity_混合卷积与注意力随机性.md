# ICLR2026最新论文 ｜Certified vs. Empirical Adversarial Robust-ness via Hybrid Convolutions with Attention Stochasticity ｜混合卷积与注意力随机性

研究机构：印度理工学院、新加坡南洋理工大学

作者：Joy Dhar、Song Xia、Manish Kumar Pandey 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01519)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.01519)

> 对抗鲁棒性研究长期面临认证保证与经验防御的二元对立：确定性方法提供紧致 $\ell_2$ 证书但牺牲精度，随机平滑（Randomized Smoothing, RS）可扩展但认证半径受限。HyCAS 通过架构内随机性注入，试图在单一模型中同时满足 $\ell_2$ 认证与 $\ell_\infty$ 经验鲁棒性。该方法将谱归一化卷积与内部随机投影、注意力噪声模块耦合，构建全局 $\le 2$-Lipschitz 网络。其价值在于弥合认证与经验防御的割裂，但 $\ell_2$ 认证半径在标准基准上显著低于专用 RS 方法，且缺乏 $\ell_\infty$ 证书的理论推导。

## 研究背景

安全关键场景中的深度模型对微小扰动极度敏感，对抗训练（Adversarial Training, AT）等经验防御虽能提升特定攻击下的稳定性，但缺乏形式化保证，易被自适应攻击突破。随机平滑（RS）通过输入端高斯噪声平均预测，确立了概率性认证范式，解决了大规模模型的可扩展性问题，但大噪声预算会破坏语义信息，导致认证精度随半径增大而急剧下降。确定性认证路线（如 Lipschitz 约束）提供紧致保证，但精确计算深层网络 Lipschitz 常数困难，且紧致约束严重限制模型表达能力，导致干净精度大幅损失。

现有方法在认证与经验鲁棒性间存在结构性割裂：RS 类方法（如 Dual RS, UCAN）专注 $\ell_2$ 认证半径优化，对 $\ell_\infty$ 强攻击的防御能力有限；Lipschitz 类方法（如 LOT, SLL）提供确定性保证，但无法应对高预算 $\ell_\infty$ 攻击。测试时自适应防御虽试图缓解此矛盾，但多为启发式，易被针对性攻击绕过。HyCAS 的切入点在于将随机性从输入端内化至架构内部，通过确定性 Lipschitz 核心与内部随机模块的混合，同时维持 $\ell_2$ 认证能力与 $\ell_\infty$ 经验鲁棒性，避免单一范式的固有缺陷。

## 核心方法

### 方法参照系

HyCAS 属于混合认证-经验防御路线，其参照系为“确定性 Lipschitz 核心 + 随机平滑”的架构融合。标准 RS 在输入端加噪，标准 Lipschitz 方法纯确定性，而 HyCAS 的关键差异在于将随机性注入卷积层内部，通过内部随机投影与注意力噪声实现平滑，而非依赖输入端高斯噪声。

### 内部随机性注入架构

设计动机：确定性 Lipschitz 防御暴露固定梯度场，易被攻击者利用；纯 RS 的输入噪声在大半径下破坏语义。HyCAS 在三个并行流（FDPAN, SNCAN, RPFAN）中注入数据无关的内部随机性，通过随机投影滤波（RPF）与随机化注意力噪声注入（RANI）模块，在保持 Lipschitz 界的同时增加梯度景观的随机性。

$$
g_\theta(x) = \arg\max_c \mathbb{E}_{\epsilon, \Omega} [f_\theta(x + \epsilon; \Omega)]
$$

其中 $\Omega = (\xi, \psi, M_\omega)$ 包含确定性结构参数、随机投影种子及注意力噪声，$\epsilon \sim \mathcal{N}(0, \sigma^2 I)$。该公式表明 HyCAS 的平滑分类器不仅对输入噪声 $\epsilon$ 取期望，还对内部随机参数 $\Omega$ 取期望，实现了双重随机性。

### Lipschitz 界与认证推导

设计动机：内部随机性可能破坏 Lipschitz 界，导致认证失效。HyCAS 通过谱归一化卷积（SNC）确保每个流的核心为 1-Lipschitz，RANI 模块为 1-Lipschitz，组合后每个流 $\le 2$-Lipschitz，凸融合保持非扩张性，最终网络 $\le 2$-Lipschitz。

$$
r_2(x) = \frac{\Delta(x)}{4}
$$

其中 $\Delta(x) = Z^{(1)}(x) - Z^{(2)}(x)$ 为前两个 logit 的差距。该公式给出 HyCAS 的 $\ell_2$ 认证半径：若扰动 $\|\delta\|_2 < r_2(x)$，则预测不变。由于全局 Lipschitz 常数为 2，认证半径为 logit 差距的 1/4，而非标准 1-Lipschitz 网络的 1/2，这是为容纳内部随机性付出的理论代价。

## 实验评估

实验在 CIFAR-10/100、ImageNet-1k 及四个医疗影像数据集（NIH-CXR, HAM10000, EyePACS, NCT-CRC-HE-100K）上进行，基线覆盖 RS 变体（RS, IRS, DRS, ARS）、Lipschitz 方法（LOT, SLL）及经验防御（CTRW, RPF, DCS）。缺失 LipNeXt 等最新确定性 SOTA 对比。

| 数据集 | 方法 | $\sigma$ | $\ell_2$ 0.5 认证准确率 (%) | $\ell_2$ 1.0 认证准确率 (%) |
|---|---|---|---|---|
| CIFAR-10 | HyCAS | 0.50 | 54.8 | 36.8 |
| CIFAR-10 | DRS | 0.50 | 48.7 | 24.5 |
| CIFAR-10 | ARS | 0.50 | 50.2 | 31.8 |
| CIFAR-10 | LOT | — | 46.3 | 24.9 |
| ImageNet | HyCAS | 0.50 | 53.9 | 41.1 |
| ImageNet | DRS | 0.50 | 49.6 | 35.6 |
| ImageNet | ARS | 0.50 | 50.3 | 39.1 |

HyCAS 在 CIFAR-10 $\ell_2$ 0.5 认证准确率达 54.8%，优于 DRS (48.7%) 和 ARS (50.2%)，但显著低于领域综述中 UCAN/Dual RS 的 76.36%。在 $\ell_\infty$ 经验鲁棒性上，HyCAS 在 NIH-CXR $\epsilon=8/255$ 下达 88.6%，优于 CTRW (85.1%) 和 RPF (83.7%)；在 HAM10000 $\epsilon=8/255$ 下达 67.8%，优于 CTRW (64.7%)。

消融实验显示，RANI 模块对 $\ell_\infty$ 鲁棒性贡献显著：移除 RANI 后，NIH-CXR $\epsilon=16/255$ 鲁棒准确率从 77.3% 降至 73.1%（-4.2%），而 $\ell_2$ 认证半径变化较小。这表明内部随机性主要增强经验鲁棒性，对认证半径的增益有限。FDPAN 流在医疗数据上表现优于自然图像，可能因频率截断对医学影像的高频噪声更敏感。

评估边界：论文未报告 $\ell_\infty$ 认证半径，仅给出 $\ell_2$ 证书；医疗数据集规模较小（NIH-CXR 约 140k 样本），泛化性存疑；未提供计算开销对比，内部随机性可能增加推理延迟。代码已开源，但超参数细节（如 $\sigma$ 选择、RANI 强度 $\omega$）未在正文中完整披露。

## 关联研究分析

从问题动机看，HyCAS 与 UCAN 代表 RS 演进的两个分支：UCAN 优化输入噪声分布（各向异性高斯），HyCAS 优化内部架构随机性。UCAN 在 CIFAR-10 $\ell_2$ 0.5 认证准确率达 76.36%，远超 HyCAS 的 54.8%，表明输入端噪声优化在纯认证任务上更优。HyCAS 的优势在于 $\ell_\infty$ 经验鲁棒性，其内部随机性干扰攻击者对梯度场的利用，而 UCAN 的输入噪声无法提供此保护。这一差异源于任务特性：认证任务关注预测不变性，经验任务关注对抗鲁棒性，二者优化目标不同。

从方法设计看，HyCAS 与 LipNeXt 构成直接对比：LipNeXt 纯确定性，通过无卷积架构突破规模瓶颈，CIFAR-10 $\ell_\infty$ 8/255 鲁棒准确率 53.44%；HyCAS 混合架构，在医疗数据上 $\ell_\infty$ 鲁棒性显著优于 LipNeXt（NIH-CXR 88.6% vs. 未报告）。HyCAS 的 $\ell_2$ 认证半径较小（$\Delta/4$ vs. LipNeXt 的 $\Delta/2$），这是引入内部随机性的理论代价。LipNeXt 未探索内部随机性，其确定性梯度场在 $\ell_\infty$ 高预算攻击下可能更易被利用，但论文未提供此对比实验。

## 总结

HyCAS 解决的核心矛盾是认证鲁棒性与经验鲁棒性的割裂，其切入点在于将随机性内化至架构内部，通过确定性 Lipschitz 核心与内部随机模块的混合，同时维持 $\ell_2$ 认证能力与 $\ell_\infty$ 经验鲁棒性。该方法证明了混合架构在医疗影像等特定领域可兼顾两者，CIFAR-10 $\ell_2$ 0.5 认证准确率 54.8% 优于 DRS/ARS，NIH-CXR $\ell_\infty$ 8/255 鲁棒准确率 88.6% 优于 CTRW。其边界在于 $\ell_2$ 认证半径显著低于专用 RS 方法，且缺乏 $\ell_\infty$ 证书的理论推导。当 $\ell_\infty$ 攻击预算进一步增大时，内部随机性对经验鲁棒性的增益是否持续，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.01519)