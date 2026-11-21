# ICLR2026最新论文 ｜AbsTopK: Rethinking Sparse Autoencoders For Bidirectional Features ｜AbsTopK：基于近端算子的双向稀疏自编码器

研究机构：美国俄亥俄州立大学

作者：Xudong Zhu、Mohammad Mahdi Khalili、Zhihui Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2510.00404)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00404)

> 导读 大语言模型内部表示的叠加特性导致神经元多义性，阻碍了直接基于神经元的机制理解。现有稀疏自编码器（Sparse Autoencoder, SAE）通过L1正则化或TopK截断实现稀疏性，但强制非负约束导致语义轴碎片化，无法在单一特征中编码对立概念。本文通过展开近端梯度法，将SAE激活函数统一为稀疏正则化的近端算子，并移除非负约束提出AbsTopK变体。该架构在重构保真度与双向概念编码上优于TopK和JumpReLU SAE，但在纯重构误差上未证明超越Gated SAE，且缺乏对负激活因果干预稳定性的验证。

## 研究背景

当模型需要区分“男性”与“女性”等对立概念时，线性表示假设（Linear Representation Hypothesis）指出这些语义差异对应向量空间中的正负位移。然而，传统SAE通过ReLU或TopK激活函数强制潜在特征非负，导致模型必须分配两个独立的字典原子分别编码“男性”和“女性”，造成语义轴的结构性碎片化。这种碎片化不仅增加了特征空间的冗余度，还限制了SAE在控制任务中沿单一语义轴双向干预的能力。

SAE旨在通过过完备字典学习将密集激活分解为稀疏单义特征，以解决多义性问题。主流路线如Gated SAE和TopK SAE通过解耦门控或硬截断改善了L1正则化导致的特征收缩，但均保留了非负约束。近期研究表明，简单的监督方法如均值差（Difference-in-Means, DiM）在特定控制任务上可媲美甚至超越SAE，这引发了对SAE特征是否真实反映模型内部计算的质疑。本文切入点在于识别非负约束是SAE与模型内部双向语义结构失配的根本原因，而非仅幅值低估问题。

## 核心方法

### 近端梯度统一框架

SAE架构可视为稀疏编码问题的单步近端梯度展开。给定字典 $\mathbf{D}$ 和偏置 $\mathbf{b}$，稀疏编码目标为 $\min_{\mathbf{z}} \frac{1}{2}\|\mathbf{x} - \mathbf{D}\mathbf{z} - \mathbf{b}\|^2 + \lambda R(\mathbf{z})$。通过固定 $\mathbf{D}, \mathbf{b}$ 并执行一步近端更新，编码器自然涌现为 $\mathbf{z} = \text{prox}_{\lambda R}(\mathbf{D}^\top(\mathbf{x} - \mathbf{b}))$。该框架将ReLU、JumpReLU和TopK统一为不同稀疏正则化 $R(\mathbf{z})$ 的近端算子，揭示了现有SAE变体在稀疏性控制上的共性局限：均隐含非负约束。

### AbsTopK算子设计

针对非负约束导致的语义碎片化，本文采用 $\ell_0$ 范数正则化 $R(\mathbf{z}) = \iota_{\{\|\mathbf{z}\|_0 \le k\}}$，移除了 $\mathbf{z} \ge 0$ 的限制。其近端算子为绝对TopK（AbsTopK），定义为：

$$
\text{AbsTopK}_k(\mathbf{u})_i = \begin{cases} u_i & \text{if } i \in H_k(\mathbf{u}) \\ 0 & \text{otherwise} \end{cases}
$$

其中 $H_k(\mathbf{u})$ 为 $\mathbf{u}$ 中绝对值最大的 $k$ 个分量索引。该算子保留正负幅值最大的激活，允许单一特征编码双向语义。设计动机在于解决TopK SAE中“男性”与“女性”被强制分裂为两个独立特征的问题，通过保留符号信息提升表示的紧凑性与语义完整性。

## 实验评估

实验在GPT-2 Small、Pythia-70M、Gemma-2 2B和Qwen3-4B四个模型上训练JumpReLU、TopK和AbsTopK SAE，评估重构误差及七项探测与控制任务。基线覆盖TopK和JumpReLU SAE，但缺失Gated SAE这一知识库中重构误差领先的强基线，限制了架构间保真度的直接对比。

| 模型 | 层 | 指标 | 原始 | JumpReLU SAE | TopK SAE | AbsTopK SAE | DiM |
|---|---|---|---|---|---|---|---|
| Qwen3-4B | 18 | MMLU | 77.3 | 75.0 | 75.2 | **75.9** | 75.8 |
| Qwen3-4B | 18 | HarmBench | 17.0 | 79.1 | 78.2 | **81.3** | 80.6 |
| Qwen3-4B | 20 | MMLU | 77.3 | 75.7 | 75.0 | **76.4** | **76.4** |
| Qwen3-4B | 20 | HarmBench | 17.0 | 78.5 | 77.0 | 79.0 | **80.0** |
| Gemma2-2B | 12 | MMLU | 52.2 | 48.8 | 49.1 | **51.3** | 51.0 |
| Gemma2-2B | 12 | HarmBench | 19.0 | 69.5 | 69.8 | 70.2 | **70.8** |
| Gemma2-2B | 16 | MMLU | 52.2 | 48.2 | 48.5 | **51.0** | 50.8 |
| Gemma2-2B | 16 | HarmBench | 19.0 | 69.8 | 70.2 | 71.7 | **72.0** |

AbsTopK在Qwen3-4B层18的HarmBench上达到81.3，优于TopK的78.2和DiM的80.6，同时MMLU下降幅度（77.3至75.9）小于JumpReLU（75.0），表明其在安全对齐与通用能力保持间取得了更优平衡。Gemma2-2B上AbsTopK的MMLU（51.3）显著高于JumpReLU（48.8），验证了双向特征对通用能力保护的增益。

消融实验未提供独立表格，但训练曲线显示AbsTopK在相同训练步数下MSE收敛速度优于TopK，且活跃特征数量更稳定。设计决策验证表明，移除非负约束带来的重构增益主要源于对负激活信息的保留，而非稀疏度调整。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码未公开，超参数细节仅部分披露。评估协议侧重下游控制任务，缺乏对特征一致性（如不同训练运行下特征集合稳定性）的量化验证，且未包含随机Transformer基线以排除数据超叠加干扰。

## 关联研究分析

从问题动机看，本文与Gated SAE（P34）均针对L1正则化的缺陷，但Gated SAE通过解耦门控与幅值解决收缩问题，仍保留非负约束；本文则直接挑战非负性本身，认为其是语义碎片化的根源。这一差异源于对“特征质量”定义的不同：Gated SAE关注幅值保真度，本文关注语义轴的完整性。Gated SAE在GPT-2 Small层8的MSE为0.45，而本文未报告该层MSE，无法直接比较保真度，但本文在控制任务上的优势暗示语义完整性可能比纯重构误差更具下游价值。

从方法设计看，AbsTopK与TopK SAE（P4）共享硬截断机制，但TopK SAE的TopK算子隐含 $\mathbf{z} \ge 0$ 约束，导致对立概念被分裂为两个特征；AbsTopK通过 $\ell_0$ 范数无符号约束，使单一特征编码双向语义。这一设计选择源于线性表示假设中概念变换对应正负位移的理论依据，而TopK SAE未考虑符号信息的语义意义。DiM方法虽能提取双向向量，但依赖标注数据且仅限单一概念，AbsTopK通过无监督学习同时发现多个双向特征，在可扩展性上具有优势。

## 总结

本文要解决的核心矛盾是SAE非负约束导致的语义轴碎片化与模型内部双向表示结构的失配。现有方法如TopK和JumpReLU SAE通过硬截断或跳跃激活改善稀疏性，但均保留非负约束，无法在单一特征中编码对立概念。本文通过近端梯度统一框架识别非负性为根本缺陷，提出AbsTopK算子保留正负幅值最大的激活。实验证明AbsTopK在Qwen3-4B层18的HarmBench上达到81.3，优于TopK的78.2，且MMLU下降幅度小于JumpReLU。本文的边界在于未与Gated SAE进行重构误差直接对比，且缺乏对负激活因果干预稳定性的验证。当特征在电路发现中被用于因果干预时，负激活方向的干预效应是否比正激活更稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00404)