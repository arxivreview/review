# ICLR2026最新论文 ｜PRECISE AND INTERPRETABLE EDITING OF CODE KNOWLEDGE IN LARGE LANGUAGE MODELS ｜基于TransCoder稀疏性的代码知识精确编辑

研究机构：德国海德堡大学、德国柏林工业大学

作者：Min Xue、Nikolai Bolik、Lennart Stöpler 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_93349118)

> 大语言模型在代码翻译任务中面临静态参数与动态API/库变更的矛盾，全量微调成本高昂且易致灾难性遗忘，而现有基于MLP的知识编辑方法因神经元多义性导致局部性差且不可解释。本文切入点在于利用TransCoder模块的稀疏单义激活特性，将编辑操作从模糊的FFN层权重修改收敛至特定的激活神经元。通过构建功能等价性基准KECode，TCPE在低资源Java-D翻译中将CodeLlama-7b-Instruct准确率从57.5%提升至64.0%。该方法验证了稀疏架构对编辑精度的增益，但其对模型架构改造的依赖性及在通用NLP基准上的表现仍存疑。

## 研究背景

代码大模型需频繁更新以适配新API或修复逻辑错误，但传统微调需海量标注数据且破坏通用能力。知识编辑（Knowledge Editing, KE）旨在以单样本级数据实现参数局部更新，其核心挑战在于平衡可靠性、通用性与局部性。在自然语言处理（NLP）领域，ROME确立的“定位-编辑”范式通过因果追踪定位FFN层神经元并执行秩一更新，成为主流基线。然而，FFN神经元具有多义性（Polysemanticity），即单个神经元同时编码多种语义信息，导致编辑时难以精确隔离目标知识，易引发无关知识的涟漪效应，且缺乏神经元级的可解释性。

针对代码域的特殊性，现有NLP基准（如ZsRE、CounterFact）依赖文本相似度或事实准确性指标，无法直接评估代码的功能正确性。代码翻译的成功标准是功能等价性，即生成代码需通过单元测试。此外，代码知识往往以结构化形式存在，MLP的多义性在代码逻辑中表现为更严重的干扰。本文提出TransCoder-based Precise Editing (TCPE)，通过替换MLP为稀疏激活的TransCoder模块，利用其单义性实现神经元级精确编辑，并构建基于功能等价性的KECode基准，解决代码域编辑的评估与解释难题。

## 核心方法

### 方法参照系

TCPE继承ROME的“定位-编辑”框架，将FFN视为键值存储，通过秩一更新注入新知识。关键差异在于，ROME直接修改FFN权重矩阵，而TCPE将MLP替换为TransCoder模块，利用其稀疏激活特性将更新限制在特定激活神经元上，从而规避多义性干扰。

### TransCoder稀疏架构替换

标准MLP通过两层全连接变换隐藏状态，其内部特征维度$d_{mlp}$通常远大于模型维度$d_{model}$，且激活密集。TransCoder由编码器$\mathbf{W}^{enc}$和解码器$\mathbf{W}^{dec}$组成，其隐藏特征向量维度$d_{tc}$更宽，并通过L1正则化训练以最小化激活数量。

$$
\mathbf{z}_{TC}^{(l)}(\bar{h}) = \sigma(\mathbf{W}^{enc}_{(l)} \bar{h})
$$

该公式表明，对于输入$\bar{h}$，TransCoder仅产生少量非零激活值（Active Neurons）。设计动机在于解决MLP神经元多义性导致的编辑不精确问题：稀疏激活使得每个神经元更可能对应单一语义概念，从而允许通过激活阈值$\tau$自动定位与目标知识相关的神经元集合$S_j = \{a \in [d_{tc}] \mid (k_j^*)_{a} > \tau\}$，实现神经元级的定向干预。

### 稀疏化秩一更新机制

在ROME基础上，TCPE仅更新TransCoder解码器$\mathbf{W}^{dec}$中与激活神经元$S_j$相关的权重。对于第$j$个修正知识对$(k_j^*, v_j^*)$，更新矩阵$\Delta \mathbf{W}^{(l,j)}$定义为：

$$
\Delta \mathbf{W}^{(l,j)} = (C_{v_j^*}^{-1} \mathbf{W}^{dec}_{(l)} k_j^*) \otimes (C_{k_j^*}^{-1} k_j^*)^\top \cdot \mathbb{1}_{S_j}
$$

其中$\mathbb{1}_{S_j}$是指示函数，仅保留$S_j$索引处的更新。这一设计将全局秩一更新限制在局部神经元子空间，显著降低了编辑对无关知识的干扰。改进价值在于，通过稀疏掩码$\mathbb{1}_{S_j}$，TCPE在保持ROME高效性的同时，提升了特异性（Specificity），使得编辑后的模型在无关代码片段上的表现保持稳定，解决了ROME在批量编辑中易导致模型崩溃的问题。

## 实验评估

实验在KECode基准（600个Java-D翻译任务）及ZsRE、CounterFact上进行，基线包括ROME、MEMIT、PMET、FiNE、LoRA等。TCPE在KECode多错误编辑场景中表现最优，其Score（综合指标）达到174.82（LTC8），显著高于FiNE的144.50和LoRA的147.27。

| 方法 | Score ↑ | Efficacy (GN) ↑ | Specificity (LoC) ↑ | Reliability (RE) ↑ |
| :--- | :--- | :--- | :--- | :--- |
| ROME | 109.60 | 0.71 | 99.56 | 57.50 |
| MEMIT | 14.96 | 100.71 | 81.92 | 57.50 |
| FiNE | 144.50 | 3.55 | 96.51 | 61.33 |
| LoRA | 147.27 | 98.58 | 99.56 | 57.50 |
| TCPE (LTC8) | **174.82** | **32.86** | **88.50** | **64.00** |

消融实验显示，激活阈值$\tau$对性能影响显著。当$\tau=0.1$时，LTC4的Efficacy (GN)为27.86%，而$\tau=0.05$时降至32.86%（注：此处原文数据存在波动，需结合上下文，实际表中$\tau=0.05$对应GN 32.86，$\tau=0.1$对应27.86，表明阈值过高会漏掉关键神经元）。LTC8在$\tau=0.08$时达到最佳平衡，GN为32.37%，LoC为88.50%。这表明稀疏度与编辑精度之间存在权衡，过高的稀疏性可能丢失必要信息，而过低则引入噪声。

评估边界方面，KECode仅覆盖Java-D翻译，样本量600，统计显著性有限。ZsRE和CounterFact结果未在正文详细列出，仅提及CodeLlama翻译准确率提升。代码开源（GitHub: minxue29031/TCPE），但TransCoder训练细节依赖附录，复现需额外计算资源。

## 关联研究分析

从问题动机看，TCPE与ROME、MEMIT同属参数编辑路线，但针对代码域的功能等价性需求，引入了架构改造。ROME等NLP方法假设FFN是知识存储位置，但忽略神经元多义性导致的编辑模糊性；TCPE通过TransCoder稀疏化，将“定位”从因果追踪的统计推断转化为激活阈值的确定性选择。这一差异源于代码逻辑的结构性：代码错误往往对应特定的语法或语义模式，稀疏神经元更易捕捉这种模式，而NLP事实编辑中知识分布更弥散。

从方法设计看，TCPE与AlphaEdit、SUIT等子空间编辑方法不同，后者通过零空间投影或解耦在原始MLP上操作，而TCPE直接替换架构。AlphaEdit依赖预计算的零空间基，计算开销大且假设知识线性可分；TCPE依赖TransCoder的L1正则化训练，将稀疏性内化于模型结构。这种架构依赖使得TCPE在无需额外预处理的情况下实现局部性，但代价是模型必须重新训练或适配TransCoder，限制了其在黑盒模型中的应用。

## 总结

TCPE旨在解决代码域知识编辑中MLP多义性导致的局部性差与不可解释问题。通过引入TransCoder稀疏架构，将编辑操作限制在激活神经元上，TCPE在KECode基准上将CodeLlama-7b-Instruct的翻译准确率从57.5%提升至64.0%，并实现了神经元级的可解释性。然而，该方法依赖模型架构改造，且仅在低资源Java-D翻译任务上验证，其在通用NLP基准上的泛化能力及TransCoder训练成本未充分探讨。当支持集增大或任务复杂度提升时，稀疏激活的阈值选择是否仍需手动调优，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_93349118)