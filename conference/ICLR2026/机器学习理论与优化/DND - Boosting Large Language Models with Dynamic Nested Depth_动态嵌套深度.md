# ICLR2026最新论文 ｜DND: Boosting Large Language Models with Dynamic Nested Depth ｜动态嵌套深度

研究机构：上海交通大学、中国人民大学

作者：Tieyuan Chen、Xiaodong Chen、Haoxing Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11001)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11001)

> 大语言模型（LLM）在推理任务中面临计算资源与模型深度的刚性约束，传统静态架构对所有Token施加均匀计算，导致简单Token冗余而关键Token欠拟合。现有动态计算方法如MOR需从头预训练，无法直接适配开源SOTA模型，且路由控制不稳定。本文提出动态嵌套深度（DND），通过Token-choice路由在推理时识别关键Token并递归处理，结合路由控制损失与阈值控制方案实现稳定选择。该方法以极小参数增加换取显著性能提升，但长序列下的推理延迟与硬件加速效率尚存疑。

## 研究背景

LLM推理中，Token预测难度存在显著异质性：部分Token仅需浅层处理即可准确预测，而少数关键Token驱动复杂逻辑转换，需深层计算。这种异质性源于Transformer自回归特性中上下文依赖的非线性放大，导致均匀深度分配在计算效率与精度间形成矛盾。解决此矛盾需引入Token级自适应计算机制，即在推理时动态调整每个Token的计算深度。

主流动态计算路线分为两类：一是早期退出（Early Exit）与MOD（Raposo et al., 2024），通过减少层数降低冗余，但牺牲了关键Token的表示精度；二是测试时缩放（Test-time Scaling）中的Latent Strategy（Hao et al., 2024），在隐空间递归计算以提升精度，但缺乏Token级选择机制，对所有Token施加额外计算。MOR（Bae et al., 2025）尝试结合两者，通过递归结构动态选择Token，但需从头预训练200B Token，成本极高且难以适配现有开源模型。本文切入点在于：将动态嵌套深度设计为Post-training插件，复用MoE路由机制实现Token-choice选择，规避预训练成本，同时通过专门训练策略解决路由不稳定问题。

## 核心方法

### 方法参照系

DND置于动态计算路线中，与MOR共享“递归计算提升精度”的核心思想，但关键差异在于：MOR在预训练阶段通过递归结构学习，而DND在Post-training阶段通过路由选择实现，无需修改模型主干架构。

### Token-choice路由设计

针对自回归模型中Expert-choice路由导致的信息泄露问题（Raposo et al., 2024），DND采用Token-choice路由，每个Token独立判断是否进入嵌套深度。路由层为线性映射 $R: \mathbb{R}^{d_{model}} \rightarrow \mathbb{R}$，输出经Sigmoid归一化为概率 $p_i \in (0,1)$，与阈值 $\tau$ 比较决定选择。该设计解决了Expert-choice在解码早期无法访问完整序列的缺陷，确保路由决策仅依赖当前Token隐状态，避免未来Token信息泄露。

$$
p_i = \sigma(R(\mathbf{x}_i^v)), \quad m_i = \mathbb{I}(p_i > \tau)
$$

其中 $\mathbf{x}_i^v$ 为Token $i$ 的原始前向隐状态，$m_i$ 为二元选择掩码。

### 路由控制损失与阈值控制

Token-choice路由缺乏Top-k机制的显式比例控制，导致选择比例波动。DND引入双重控制：一是路由控制损失 $L_{router}$，通过Score Dispersion Loss $L_{sd}$ 最大化路由分数熵以增强区分度，同时通过Distribution Preservation Loss $L_{dp}$ 将分数拉向Sigmoid中心0.5以避免梯度消失；二是阈值控制方案，基于样本缓冲区的实际选择比例与目标比例误差，结合指数移动平均（EMA）动态更新阈值 $\tau$。该设计解决了MOR中Z-loss仅能平衡选择/不选择、无法精确控制比例的缺陷，确保训练过程中选择比例稳定在目标值（如20%）。

$$
L_{router} = \lambda_{sd} L_{sd} + \lambda_{dp} L_{dp}, \quad L_{sd} = -\sum_{l=L_s}^{L_e} \sum_{i=1}^{N} p'_{i,l} \log p'_{i,l}
$$

其中 $p'_{i,l}$ 为第 $l$ 层Token $i$ 的归一化路由分数，$L_{dp} = \frac{1}{N}\sum_{i=1}^{N}(p_{i,l} - 0.5)^2$。

## 实验评估

实验在Qwen3-1.7B、Llama3.2-1B、Gemma3-1B（Dense）及Qwen3-30B-A3B（MoE）上验证，覆盖MMLU、GSM8K、HumanEval+等17个基准。基线对比包括Vanilla SFT与ITT（Chen et al., 2025），但缺失与静态剪枝方法（如CTS）或早期退出方法的直接对比，无法评估DND在计算效率-精度权衡中的相对优势。

| 模型 | 平均提升 | BBH提升 | GPQA提升 | BFCL v3提升 |
|---|---|---|---|---|
| Qwen3-1.7B | +1.88 | +5.02 | +5.80 | +1.07 |
| Llama3.2-1B | +2.61 | +3.70 | +3.86 | +2.63 |
| Gemma3-1B | +2.50 | +4.69 | +5.30 | +2.19 |
| Qwen3-30B-A3B | +0.87 | +0.13 | +0.91 | +2.05 |

消融实验显示，仅使用DND框架配合简单Z-loss控制时，平均提升仅1.01点，显著低于完整策略的1.88点，证明路由控制损失与阈值控制的必要性。选择比例从10%增至20%时，性能从+0.8%提升至+1.5%，但30%时未进一步改善，表明存在最优选择比例区间。

评估边界：论文未报告置信区间，数值比较需谨慎；代码未公开，超参数（如 $\lambda_{sd}, \lambda_{dp}$）未详细披露；推理延迟仅报告相对速度（如输入1024/解码2048时相对速度92.6%），未提供绝对延迟或GPU加速比，无法评估动态路由在硬件上的实际开销。

## 关联研究分析

从问题动机看，DND与MOR均旨在通过动态深度提升LLM推理精度，但MOR聚焦预训练阶段的参数效率，需从头训练200B Token，而DND聚焦Post-training阶段的性能解锁，直接适配开源SOTA模型。这一差异源于任务特性：MOR需学习递归结构本身，而DND复用现有Transformer层，仅学习路由选择，因此训练成本降低3个数量级。但DND的Post-training范式可能受限于预训练模型的表示能力，若预训练模型未充分学习关键Token的深层表示，DND的递归计算收益可能受限，论文未对此进行消融。

从方法设计看，DND与SWAN（Ale et al., 2026）同属动态计算路线，但SWAN通过逐神经元二元开关实现激活稀疏化，粒度为神经元级，而DND通过Token-choice路由实现计算深度增加，粒度为Token级。SWAN的目标是降低平均计算量，DND的目标是提升关键Token的表示精度，两者在计算分配策略上形成互补：SWAN跳过冗余计算，DND增加关键计算。但DND的Token-choice路由在长序列（如>4K Token）下的计算开销是否抵消动态计算收益，论文未提供长序列基准测试，这一盲区可能制约其在长文本任务中的应用。

## 总结

DND解决的核心矛盾是LLM推理中计算资源均匀分配与Token难度异质性的冲突。现有方法如MOR因预训练成本过高无法适配开源模型，而DND通过Post-training插件与Token-choice路由，以0.03M参数增加实现Qwen3-30B-A3B平均0.87%、BBH 5.02%的性能提升。其边界在于：推理延迟未量化，长序列下路由开销未知，且Post-training范式受限于预训练模型表示能力。当序列长度超过4K时，Token-choice路由的线性计算开销是否导致推理速度下降超过5%，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11001)