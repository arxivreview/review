# HuggingFace最新推荐论文 ｜Dion3: Full-Stack Orthogonal Updates ｜全栈加速矩阵优化器

研究机构：丰田研究所、美国纽约大学

作者：Noah Amsel、Jack Zhang、Kwangjun Ahn 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.11612)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.11612)

> Muon优化器因Newton-Schulz正交化的立方级计算复杂度与分布式通信瓶颈，难以在超大规模LLM训练中替代AdamW。现有变体仅解决单一维度的开销，缺乏算法与系统的协同优化。本文提出Dion3，通过Gram矩阵重构、对称GEMM内核、行采样压缩及Megabatching通信策略，实现全栈加速。其工程价值显著，但行采样对长期泛化性能的影响尚存疑。

## 研究背景

Muon将权重矩阵视为线性算子，利用极分解因子（Polar Factor）消除奇异值差异，实现谱范数下的最速下降。这一机制依赖于Newton-Schulz迭代近似计算极分解，其核心在于通过多项式变换将矩阵奇异值压缩至1附近，从而保留方向信息并丢弃尺度信息。然而，该迭代过程涉及多次大矩阵乘法，计算复杂度随矩阵维度立方增长，且要求对完整矩阵进行操作，这在分布式分片环境下引发了严重的通信开销。

主流路线试图通过低秩近似或块周期正交化降低计算规模，如Dion2采用随机采样缩小正交化矩阵，MuonBP通过周期性复用正交化结果减少调用次数。这些方法虽降低了单步计算量，但未触及Newton-Schulz算法本身的结构性低效，且在分布式场景中缺乏高效的通信-计算重叠策略。Dion3的切入点在于识别出标准Newton-Schulz中对称矩阵乘法未被利用以及长宽比对运行时的强依赖，通过算法重构与系统级优化协同，将优化器步时从26倍AdamW降至4倍。

## 核心方法

### 方法参照系

标准Muon更新规则为 $W_{t+1} = W_t - \eta \cdot \text{polar}(M_t)$，其中 $\text{polar}(M_t)$ 通过5次Newton-Schulz迭代近似。该流程在原始矩阵 $X \in \mathbb{R}^{n \times m}$ 上迭代，每次迭代包含 $XX^\top$、$A^2$ 和 $BX$ 三次矩阵乘法，总FLOPs为 $2T(2\alpha + 1)n^3$，其中 $\alpha = m/n$ 为长宽比。本文问题与该通用流程的关键差异在于，标准实现未利用中间矩阵的对称性，且矩形乘法占比过高，导致在 $\alpha \gg 1$ 的Transformer权重矩阵中效率低下。

### Gram Newton-Schulz重构

标准Newton-Schulz在原始矩阵上迭代，导致大量昂贵的矩形乘法。Dion3提出在小型对称Gram矩阵 $XX^\top$ 上迭代，利用恒等式 $\text{polar}(X) = (XX^\top)^{-1/2}X$。该设计动机在于消除对长宽比 $\alpha$ 的强依赖，将计算重心转移至 $n \times n$ 对称矩阵。具体迭代公式为：

$$
R_t = Z_t R_{t-1} Z_t, \quad Q_t = Q_{t-1} Z_t, \quad Z_t = a_t I + b_t R_{t-1} + c_t R_{t-1}^2
$$

其中 $R_0 = XX^\top$，$Q_0 = I$。最终输出为 $Q_T X$。此重构在数学上与标准Newton-Schulz等价，但仅需2次矩形乘法（初始 $XX^\top$ 和最终 $Q_T X$），其余均为对称乘法。当 $\alpha = 43$ 时，FLOPs节省55%，显著降低了长宽比带来的计算惩罚。

### 对称GEMM与行采样压缩

Gram-NS产生的对称矩阵乘法可通过CuteDSL内核加速，仅计算下三角部分并复制至上三角，使 $XX^\top$ 和 $A^2$ 的成本减半。进一步，Dion3引入行采样策略，仅对动量矩阵 $M$ 的部分行进行正交化。该设计动机在于解决分布式分片下的通信瓶颈，通过压缩输入矩阵规模，使Megabatching策略能将每步通信轮次降至常数。行采样后的更新规则为：

$$
\tilde{O} = \text{polar}(M_{\text{sub}}), \quad W_{t+1} = W_t - \eta \frac{\|\tilde{O}\|_F}{\|\tilde{O}_{\text{full}}\|_F} \tilde{O}_{\text{full}}
$$

其中 $M_{\text{sub}}$ 为采样子集。该策略简化了Dion2的低秩近似实现，无需构造投影矩阵，且与Gram-NS协同，进一步降低矩形乘法次数，使优化器步时接近AdamW水平。

## 实验评估

实验在7B参数语言模型上验证，基线覆盖Muon、NorMuon、AdamW及Dion2，但缺失LiMuon、EF21-Muon等理论或通信优化变体。主结果显示，Dion3将优化器步时从26倍AdamW降至4倍，其中Gram-NS贡献19倍，对称内核贡献15倍，行采样贡献4倍。该加速比在保持损失曲线与Muon相当的前提下实现，验证了全栈优化的有效性。

消融实验表明，Gram-NS与对称内核的协同效应显著，单独使用Gram-NS时加速比低于预期，因未充分利用对称结构。行采样比例对损失影响较小，25%采样率下损失未显著上升，暗示正交化的鲁棒性优于预期。然而，论文未报告不同采样率下的长期泛化性能，仅关注收敛速度。

评估边界方面，实验侧重Wall-clock Time而非验证损失，缺乏与SOTA方法在统一数据协议下的Loss对比。代码开源为 `dion` 和 `gram-newton-schulz`，支持FSDP、DDP等并行策略，但超参数配置未详细披露，可复现性依赖社区实践。

## 关联研究分析

从方法设计看，Dion3与Dion2同属行采样路线，但Dion2依赖离散余弦变换构造低秩近似，而Dion3直接选择行，简化了分布式实现。这一差异源于Dion3对Megabatching通信策略的适配需求，直接行选择更易与分片边界对齐，减少了all-to-all通信的复杂度。Dion2在精度上略优，但Dion3在系统效率上更具优势，反映了算法与系统设计的权衡。

从问题动机看，Dion3与EF21-Muon均针对分布式通信瓶颈，但EF21侧重误差反馈以补偿压缩损失，而Dion3侧重计算-通信重叠以隐藏延迟。EF21-Muon在收敛性理论上更严谨，证明了非欧几里得光滑性下的收敛速率，但Dion3在工程落地性上更强，提供了pip-installable包。两者互补，EF21适合对收敛性要求极高的场景，Dion3适合追求极致训练速度的场景。

## 总结

Dion3解决的核心矛盾是Muon正交化的立方级计算开销与分布式通信瓶颈。其切入点在于识别标准Newton-Schulz的结构性低效，通过Gram矩阵重构与系统级优化协同，实现了算法与硬件的匹配。Dion3将优化器步时从26倍AdamW降至4倍，验证了全栈加速的可行性。其边界在于行采样对长期泛化性能的影响未充分验证，且缺乏与理论变体的直接对比。当模型规模进一步扩大至万亿参数时，行采样引入的方差是否会导致训练不稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.11612)