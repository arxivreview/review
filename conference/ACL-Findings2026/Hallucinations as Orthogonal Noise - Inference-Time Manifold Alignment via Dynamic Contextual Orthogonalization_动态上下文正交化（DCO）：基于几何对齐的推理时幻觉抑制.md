# ACL-Findings2026最新论文 ｜Hallucinations as Orthogonal Noise: Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization ｜动态上下文正交化（DCO）：基于几何对齐的推理时幻觉抑制

研究机构：中国科学技术大学、清华大学

作者：Mingkuan Zhao、Wentao Hu、Tianchen Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03022)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03022)

> 大语言模型在生成过程中常因内部表征偏离上下文事实而产生幻觉，现有解码干预方法多依赖静态向量或Logit层对比，难以区分必要的语义多样化与有害噪声，导致在提升忠实性的同时损害参数知识检索能力。本文基于线性表示假设，将幻觉形式化为残差流中偏离上下文流形的正交噪声，提出动态上下文正交化（Dynamic Contextual Orthogonalization, DCO）方法，通过逐层Z-Score动态门控机制选择性衰减异常正交分量。该方法在Llama-3系列模型上实现了上下文忠实性与知识保留的帕累托优化，但其对纯参数知识检索场景下正交性定义的适用性仍存疑。

## 研究背景

Transformer模型的残差流（Residual Stream）作为信息传递的主通道，其内部状态向量承载了模型对上下文语义的累积理解。当模型处理冲突或模糊上下文时，特定注意力头可能引入与既定语义方向线性无关的分量，这种几何层面的失配即为幻觉的微观机制。线性表示假设（Linear Representation Hypothesis）指出语义概念在高维空间中编码为线性方向，这为将幻觉检测转化为子空间投影任务提供了理论依据。

当前推理时干预方法主要分为两类：一类如Inference-Time Intervention (ITI) 使用离线探针生成的静态转向向量，另一类如Decoding by Contrasting Layers (DoLa) 在Logit层进行层间分布对比。前者因方向固定无法适应动态语义变化，常导致参数知识被过度抑制；后者虽能增强输出锐度，但未能纠正内部表征的动态演化，且需多次前向传播增加延迟。本文切入点在于利用瞬时残差流作为动态锚点，在注意力头输出层面执行几何正交分解，从根源上隔离偏离上下文流形的噪声分量。

## 核心方法

### 方法参照系

标准解码干预流程通常在Logit层或注意力头掩码层面操作，通过调整概率分布或屏蔽特定头来抑制幻觉。本文的关键差异在于将干预位置前移至残差流的注意力输出阶段，并引入基于层内统计分布的动态阈值，替代静态重要性评分或固定转向向量。

### 上下文锚点与正交分解

设计动机在于解决静态向量无法适应上下文语义动态变化的问题。DCO首先对第 $L$ 层输入残差流 $\mathbf{x}_{in}^{[L]}$ 进行RMSNorm归一化，得到单位向量 $\mathbf{c}$ 作为上下文锚点。随后，对第 $h$ 个注意力头输出 $\mathbf{o}_h$ 执行正交分解，将其投影到锚点方向及其正交补空间：

$$ \mathbf{o}_{h\parallel} = (\mathbf{o}_h \cdot \mathbf{c})\mathbf{c}, \quad \mathbf{o}_{h\perp} = \mathbf{o}_h - \mathbf{o}_{h\parallel} $$

该公式将头输出解耦为与上下文对齐的共振分量 $\mathbf{o}_{h\parallel}$ 和偏离上下文的正交噪声分量 $\mathbf{o}_{h\perp}$，其中正交分量范数与总范数之比 $\rho_h$ 量化了该头引入的语义偏离程度。

### Z-Score动态抑制机制

设计动机在于区分必要的语义多样化与有害噪声，避免静态阈值误伤正常信息流。DCO计算当前层所有 $H$ 个头的 $\rho_h$ 均值 $\mu_\rho$ 和标准差 $\sigma_\rho$，进而计算每个头的Z-Score $z_h = (\rho_h - \mu_\rho)/\sigma_\rho$。抑制系数 $\lambda_h$ 通过Sigmoid门控函数动态生成：

$$ \lambda_h = \sigma(\beta(z_h - \tau)) $$

其中 $\tau$ 为容忍阈值，$\beta$ 为温度系数。当 $z_h < \tau$ 时 $\lambda_h \approx 1$，保留正交贡献以维持语义多样性；当 $z_h$ 显著大于 $\tau$ 时 $\lambda_h \to 0$，衰减异常正交分量。最终重构的注意力输出为 $\sum_h (\mathbf{o}_{h\parallel} + \lambda_h \mathbf{o}_{h\perp})$，确保仅统计离群头受到干预。

## 实验评估

实验基于Llama-3-8B和70B-Instruct模型，在XSum、IFEval、NQ-Swap、TruthfulQA、TriviaQA和MuSiQue等基准上评估。基线覆盖ITI、DoLa、CAD、DeCoRe等主流推理时干预方法，但未包含SelfCheckGPT等黑盒采样基线及CausalGaze等最新白盒探测方法。

| 模型 | 方法 | IFEval Prompt | IFEval Inst. | TriviaQA EM | TruthfulQA MC1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Llama-3-70B | Greedy | 77.45 | 84.41 | 74.77 | 49.57 |
| Llama-3-70B | ITI | 76.71 | 83.69 | 73.54 | 48.96 |
| Llama-3-70B | DoLa (high) | 78.00 | 84.65 | 73.96 | 49.69 |
| Llama-3-70B | DCO | 85.77 | 90.29 | 76.12 | 48.23 |
| Llama-3-8B | Greedy | 70.24 | 78.30 | 56.58 | 39.41 |
| Llama-3-8B | ITI | 52.31 | 63.19 | 48.41 | 43.70 |
| Llama-3-8B | DCO | 74.68 | 81.41 | 57.33 | 40.39 |

DCO在IFEval上显著优于所有基线，70B模型Prompt级准确率从77.45%提升至85.77%，表明几何对齐有效增强了指令遵循能力。在知识保留方面，DCO在TriviaQA上达到76.12%（70B），高于Greedy基线的74.77%和ITI的73.54%，验证了动态Z-Score机制在抑制幻觉的同时未损害参数知识检索。然而，在TruthfulQA MC1指标上，DCO（48.23%）略低于Greedy（49.57%）和DoLa（49.69%），提示其对事实性错误的抑制弱于对上下文偏离的抑制。

消融分析显示，DCO在MuSiQue多跳推理任务中表现稳定，70B模型CoT设置下EM达21.14%，优于DeCoRe的20.60%。这表明全局统计约束比稀疏头掩码更有效地处理分布式推理错误。值得注意的是，ITI在8B模型上导致TriviaQA准确率从56.58%骤降至48.41%，证实了静态干预对知识检索路径的破坏性，而DCO通过动态阈值避免了这一副作用。

评估边界方面，论文未报告置信区间，且仅在Llama-3系列上验证，缺乏跨架构泛化性测试。代码已开源，但超参数 $\tau$ 和 $\beta$ 需针对任务类型手动校准（如NQ-Swap用紧约束，MuSiQue用松约束），自动化校准机制尚未实现。

## 关联研究分析

从方法设计看，DCO与ITI的核心差异在于干预的动态性。ITI使用离线探针生成的固定转向向量，假设幻觉信号在语义空间中具有全局一致性方向；而DCO利用瞬时残差流作为锚点，假设幻觉是局部几何失配。这一差异源于对幻觉本质的不同假设：ITI视幻觉为可被单一方向抵消的系统性偏差，DCO视其为随上下文变化的统计离群。在知识冲突场景下，ITI的静态向量可能同时抑制正确的事实检索，而DCO的Z-Score门控仅衰减相对偏离最大的头，从而保留了大部分参数知识。

从问题动机看，DCO与DoLa虽同属推理时干预，但作用层级不同。DoLa在Logit层对比不同层的输出分布，旨在增强最终token概率的锐度；DCO在注意力输出层执行向量正交分解，旨在纠正内部表征的几何轨迹。DoLa的对比机制无法区分“正确的多样化”与“错误的噪声”，因为两者在Logit分布上可能表现相似；DCO通过正交性度量 $\rho_h$ 直接量化语义偏离，提供了更细粒度的干预依据。然而，DCO依赖线性表示假设，若语义概念在残差流中并非线性可分，其正交分解的有效性将受限，这一点在非线性激活函数的深层网络中尚未得到充分验证。

## 总结

本文旨在解决推理时干预中上下文忠实性与参数知识保留的权衡矛盾，现有静态向量或Logit对比方法因缺乏动态适应性而难以兼顾两者。DCO基于线性表示假设，将幻觉形式化为残差流中的正交噪声，通过逐层Z-Score动态门控选择性衰减异常分量，在Llama-3-70B上将IFEval Prompt准确率提升至85.77%，同时保持TriviaQA准确率高于基线。其边界在于对纯参数知识检索场景下正交性定义的适用性未充分验证，且超参数需任务特定校准。当上下文极度稀疏或完全缺失时，动态锚点的几何意义是否退化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03022)