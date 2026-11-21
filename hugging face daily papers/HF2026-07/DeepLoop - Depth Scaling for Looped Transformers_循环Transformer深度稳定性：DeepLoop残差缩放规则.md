# HuggingFace最新推荐论文 ｜DeepLoop: Depth Scaling for Looped Transformers ｜循环Transformer深度稳定性：DeepLoop残差缩放规则

研究机构：美国普林斯顿大学、美国加州大学洛杉矶分校

论文原文见 [arXiv](https://arxiv.org/abs/2607.13491)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.13491)

> 循环Transformer通过复用少量物理块实现深度扩展，但参数共享导致标准残差缩放理论失效，训练稳定性随循环次数增加而恶化。现有DeepNorm假设深度未绑定，无法处理同一参数被多次访问时的梯度聚合效应。本文推导了参数共享下的一阶扰动界，提出将指数从1/4提升至1/2的DeepLoop规则。该规则在GPT-2规模上验证了稳定性优势，但未探索其与状态空间模型在长程依赖建模上的互补性。

## 研究背景

当Transformer通过循环结构复用物理块以扩展有效深度时，同一参数张量在多个循环轮次中被反复访问。这种参数共享改变了残差连接的优化动力学：标准DeepNorm假设每个残差子层拥有独立参数，其稳定性条件 $M(\beta/\alpha)^2 = O(1)$ 中 $M$ 为未绑定深度下的子层访问数。然而，在循环架构中，物理子层 $j$ 的更新 $\Delta \phi_j$ 聚合了 $R$ 次访问的梯度，且该更新在后续前向传播中被所有 $R$ 次访问读取，形成“多写多读”的耦合路径。若各轮次梯度对齐，共享更新幅度可能放大 $R$ 倍，导致一阶扰动界发散。

深度扩展是提升Transformer表达力的可靠途径，但标准架构中深度与参数量同步增长，限制了参数效率。Universal Transformer与ALBERT通过深度参数共享解耦了计算量与存储量，近期递归深度模型进一步将测试时计算作为独立扩展轴。然而，这些工作缺乏对参数共享下残差缩放稳定性的理论刻画。DeepNorm（Wang et al., 2024）为未绑定深度提供了可训练性保证，但其指数 $p=1/4$ 在固定物理深度 $K$、增大循环次数 $R$ 的循环场景下，残留 $\Theta(R)$ 的增长项，导致训练不稳定。本文切入点在于识别这一被忽略的“绑定深度聚合机制”，并推导适配循环结构的缩放规则。

## 核心方法

### 残差缩放参照系

DeepNorm通过设置残差缩放 $\alpha$ 与初始化增益 $\beta$ 控制一阶更新效应，其核心条件是 $M(\beta/\alpha)^2 = O(1)$，其中 $M=2N$ 为未绑定深度下的残差子层访问数。该框架假设每个子层参数独立更新，未考虑参数共享导致的梯度聚合与重复读取效应。

### 访问对齐系数与循环扰动界

本文引入访问对齐系数 $\kappa_R$ 量化循环轮次间梯度与敏感度的相关性。对于物理子层 $j$，其绑定更新的一阶扰动界为：

$$
\Delta F_{\text{tied}} \leq C \cdot M \cdot \kappa_R \cdot \left(\frac{\beta}{\alpha}\right)^2
$$

其中 $\kappa_R \in [0, R]$，独立访问时 $\kappa_R=O(1)$，完全对齐时 $\kappa_R=\Theta(R)$。该公式揭示了参数共享下稳定性条件的本质变化：当 $\kappa_R$ 随 $R$ 线性增长时，标准DeepNorm的 $p=1/4$ 指数不足以抑制扰动增长。

### 指数阈值推导与DeepLoop规则

在固定物理深度 $K$、$N=KR$ 的循环场景下，若 $\kappa_R=\Theta(R^\gamma)$，则稳定性条件要求指数 $p$ 满足：

$$
p \geq \frac{1}{2} \cdot \frac{1+\gamma}{1+\gamma} = \frac{1}{2} \quad (\text{当 } \gamma=1)
$$

本文采用保守对齐假设 $\gamma=1$，推导得出 $p=1/2$ 为均匀有界的最小指数。DeepLoop规则保持Post-LN架构，仅将指数从 $p=1/4$ 提升至 $p=1/2$，即 $\alpha=(2N)^{1/2}$，$\beta=(8N)^{-1/2}$。该设计动机在于解决标准DeepNorm在循环深度下残留 $\Theta(R)$ 增长项导致的训练不稳定，无需引入门控、可学习系数或额外调参常数。

## 实验评估

实验在GPT-2 small（124M）与medium（350M）骨干上，使用FineWeb-Edu 50BT预训练，对比标准循环Transformer（Baseline）与DeepLoop在 $R \in \{1,3,5,7\}$ 下的验证损失与下游任务准确率。基线覆盖循环Transformer内部对比，但缺失Mamba、DeltaNet等状态空间模型或线性注意力基线，无法评估循环架构相对于SSM的相对优势。

| 方法 | R | ARC-C (1-shot) | HellaSwag (1-shot) | WinoGrande (1-shot) | Avg (1-shot) |
|---|---|---|---|---|---|
| Baseline | 1 | 30.38 | 37.73 | 55.09 | 51.69 |
| Baseline | 7 | 34.22 | 40.87 | 58.80 | 54.62 |
| DeepLoop | 1 | 30.80 | 37.73 | 55.25 | 51.53 |
| DeepLoop | 7 | 35.15 | 41.83 | 59.43 | 55.20 |

DeepLoop在 $R=1$ 时与Baseline持平（Avg差-0.16），在 $R \geq 3$ 时一致优于Baseline，$R=7$ 时Avg提升0.58点。消融显示，在 $R=7$ 时DeepLoop在8个下游任务中的7个上优于同 $R$ Baseline，仅PIQA例外。WinoGrande在0-shot下提升1.74点（59.04 vs 57.30），表明深度扩展对推理任务收益显著。

评估边界方面，实验仅覆盖单种子运行，未报告置信区间，$R=5$ 时1-shot Avg出现Baseline反超（54.42 vs 54.19），提示种子方差影响。代码开源（GitHub: lszshu/DeepLoop），但超参数与GPU配置未在正文详述。未评估精确检索任务（如Passkey Retrieval），无法验证循环架构在TC0复杂度限制下的表现。

## 关联研究分析

从问题动机看，DeepLoop与Mamba的选择性机制解决不同层面的循环架构缺陷。Mamba通过输入依赖的状态转移矩阵解决固定状态的表达力瓶颈，而DeepLoop通过残差缩放规则解决固定参数的优化稳定性问题。两者均针对“有限参数复用”场景，但Mamba关注信息过滤能力，DeepLoop关注训练动力学。这种差异源于任务特性：语言建模中表达力瓶颈优先于稳定性瓶颈，而深度扩展场景中稳定性成为首要约束。

从方法设计看，DeepLoop与Universal Transformer的自适应计算机制形成对比。Universal Transformer通过预测停止机制动态调整循环次数，而DeepLoop假设固定 $R$ 并推导最坏情况缩放规则。前者追求计算效率，后者追求稳定性保证。DeepLoop未探索 $\kappa_R$ 在实际训练中是否总处于对齐最坏情况，若实际 $\kappa_R$ 接近 $O(1)$，则 $p=1/2$ 可能过于保守，导致模型容量未充分利用。

## 总结

本文核心矛盾在于循环Transformer深度扩展时参数共享导致的训练稳定性失效。现有DeepNorm假设深度未绑定，无法处理绑定深度下的梯度聚合效应，而本文通过访问对齐系数 $\kappa_R$ 量化这一效应，推导 $p=1/2$ 指数阈值。DeepLoop规则在GPT-2 medium上验证了 $R=7$ 时Avg提升0.58点、WinoGrande提升1.74点的有效性。其边界在于仅验证固定 $R$ 场景，未探索 $\kappa_R$ 动态变化下的自适应缩放，也未评估精确检索任务。当循环次数 $R$ 进一步增大至10以上时，$p=1/2$ 的保守假设是否仍为最优，还是存在更精细的 $\kappa_R$ 估计方法，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.13491)