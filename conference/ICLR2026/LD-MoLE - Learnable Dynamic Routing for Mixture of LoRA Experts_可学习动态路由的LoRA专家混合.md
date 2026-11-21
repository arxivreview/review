# ICLR2026最新论文 ｜LD-MoLE: Learnable Dynamic Routing for Mixture of LoRA Experts ｜可学习动态路由的LoRA专家混合

研究机构：美国康涅狄格大学、美国宾夕法尼亚大学

作者：Yuan Zhuang、Yi Shen、Yuexin Bian 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25684)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25684)

> 参数高效微调（PEFT）场景下的混合专家（MoE）路由长期受困于固定专家数带来的僵化与TopK算子不可微导致的优化断裂。现有方案要么依赖人工调参的固定TopK，要么采用可能产生零激活的ReLU动态路由，均无法在保持端到端可微性的同时实现Token级自适应稀疏。本文提出LD-MoLE，基于Sparsegen闭式解构建可微路由，并用共享MLP预测Token级稀疏参数$\lambda$，在Llama-3.2-3B与Qwen3-1.7B的指令微调任务上取得最高平均分。其价值在于将动态稀疏控制从预训练迁移至PEFT，但稀疏损失与任务性能的权衡边界尚未完全厘清。

## 研究背景

当大语言模型（LLM）通过参数高效微调（PEFT）适配下游任务时，单一低秩适应（LoRA）模块面临秩选择的两难：高秩配置易过拟合且计算成本高，低秩配置则表达力不足。混合LoRA专家（MoLE）框架通过引入多个LoRA模块作为专家，利用稀疏激活机制在保持参数效率的同时提升模型容量。然而，MoLE的路由机制直接继承了传统MoE的缺陷：标准TopK路由要求每个Token固定选择$k$个专家，这一人工超参数无法根据Token复杂度动态调整资源分配，且TopK算子的离散不可微性阻断了路由器与专家模块的端到端梯度流动。

MoE路由机制的核心矛盾在于稀疏激活的计算效率与专家功能分化的稳定性之间的平衡。预训练阶段的研究已确立辅助负载均衡损失作为防止专家坍缩的标准组件，但这一方案在PEFT场景中面临新挑战：微调数据量远小于预训练，强制均匀分布可能过度抑制专家的功能分化。ReMoE（Wang et al., 2025）尝试用ReLU替代TopK实现可微动态路由，但其设计存在根本缺陷——部分Token可能被路由至零个专家，导致性能退化。MoLA（Gao et al., 2024）作为MoLE的代表性工作，仍依赖固定TopK路由，其实验表明许多专家在固定路由下被低效利用。LD-MoLE的切入点在于：能否设计一种既保证每个Token至少激活一个专家、又支持Token级动态稀疏控制、且完全可微的路由机制？

## 核心方法

### 方法参照系

MoLE框架的标准流程是：输入Token经门控网络计算专家得分，通过TopK选择固定数量专家，加权聚合LoRA模块输出。本文的关键差异在于将固定TopK替换为基于Sparsegen投影的动态路由，并引入Token级稀疏参数预测机制，使专家激活数量成为可学习变量而非固定超参数。

### Sparsegen闭式路由

传统TopK路由在$k$-th最大得分处存在跳跃不连续性，微小扰动即可改变专家选择集，导致梯度突变。LD-MoLE采用Sparsegen（Laha et al., 2018）作为概率单纯形上的投影，其闭式解避免了离散选择，生成具有良好定义次梯度的稀疏分布。给定专家得分向量$\mathbf{u} \in \mathbb{R}^E$，排序坐标$u_{(1)} \geq \cdots \geq u_{(E)}$，累积和$U_k = \sum_{i=1}^k u_{(i)}$，稀疏参数$\lambda \in (-\infty, 1)$，路由分布$\mathbf{p} \in \mathbb{R}^E$由下式确定：

$$p_i = \left[ u_i - \tau \right]_+, \quad \tau = \frac{U_k - \lambda}{k}$$

其中$k$为满足$u_{(k)} > \tau \geq u_{(k+1)}$的最大整数，$[x]_+ = \max(x, 0)$。该公式的物理含义是：$\lambda$控制分布向单纯形角点（稀疏）或均匀分布（密集）的倾向，$\lambda \to 1^-$时趋向稀疏，$\lambda \to -\infty$时趋向均匀。关键性质是Lemma 1保证$\|\mathbf{p}\|_0 \geq 1$，即每个Token至少激活一个专家，解决了ReMoE的零激活问题。

### Token级稀疏参数预测与稀疏损失

固定$\lambda$无法捕捉层间稀疏度差异——实验显示深层$\lambda$值幅度和方差均大于浅层。LD-MoLE引入轻量级共享MLP预测Token级稀疏参数：

$$\lambda_t = f(\mathbf{x}_t)$$

其中$f$为共享MLP，$\mathbf{x}_t$为第$t$个Token的特征。该设计将$\lambda$预测的参数成本与层数和专家数解耦，仅依赖唯一输入维度集合。为直接正则化激活专家数量，基于Proposition 2推导稀疏损失：当目标激活$k$个专家时，$\lambda$需落在区间$[\lambda_{\text{lower}}(k), \lambda_{\text{upper}}(k)]$内，稀疏损失定义为：

$$\mathcal{L}_{\text{sparse}} = \text{ReLU}(\lambda_{\text{lower}}(k) - \lambda)$$

该损失仅在$\lambda$低于下界时施加惩罚，允许$\lambda$在可行区域内自由变化。总损失为$\mathcal{L} = \mathcal{L}_{\text{task}} + \alpha \mathcal{L}_{\text{balance}} + \beta \mathcal{L}_{\text{sparse}}$，其中$\mathcal{L}_{\text{balance}}$为标准负载均衡损失。

## 实验评估

实验在Llama-3.2-3B、Llama-3.2-8B和Qwen3-1.7B上评估，覆盖MMLU-Pro、ARC、HellaSwag等指令微调基准及CoLA、RTE序列分类任务。基线包括MoLA（固定TopK）和ReMoLE（ReLU动态路由），但缺失DirMoE、Grassmannian等几何路由方法作为对比。

| 模型 | 方法 | MMLU-Pro | ARC-E | HellaSwag | 平均分 |
|---|---|---|---|---|---|
| Llama3.2-3B | MoLA(8888) | 40.31 | 79.77 | 89.53 | 78.18 |
| Llama3.2-3B | MoLA(2468) | 42.31 | 80.02 | 89.46 | 78.72 |
| Llama3.2-3B | ReMoLE | 48.01 | 82.00 | 91.61 | 81.42 |
| Llama3.2-3B | LD-MoLE | **49.58** | **83.67** | **91.61** | **82.05** |
| Qwen3-1.7B | MoLA(8888) | 51.12 | 76.49 | 86.64 | 79.24 |
| Qwen3-1.7B | MoLA(2468) | 49.96 | 75.84 | 84.48 | 79.28 |
| Qwen3-1.7B | ReMoLE | 53.40 | 79.60 | 91.75 | 81.02 |
| Qwen3-1.7B | LD-MoLE | **53.82** | **78.67** | **92.11** | **81.63** |

LD-MoLE在Llama3.2-3B上较ReMoLE提升0.63%，在Qwen3-1.7B上提升0.61%。值得注意的是，MoLA(2468)（剪枝变体）优于MoLA(8888)，印证固定路由下专家冗余问题。ReMoLE在CoLA（Llama3.2-3B）和RTE（Qwen3-1.7B）上出现显著性能下降，而LD-MoLE保持跨任务稳定性。

消融实验显示，预测$\lambda$一致优于所有固定值（0.5至-10.0），验证了Token级动态控制的必要性。稀疏损失分析揭示明确权衡：禁用稀疏损失获得最高平均分，但部分任务受益于减少专家使用；过强稀疏约束导致训练后期性能下降，表明过度稀疏限制了层间专家使用的灵活性。Token频率与激活专家数呈负相关——高频Token激活更少专家，稀有Token激活更多专家，符合计算资源自适应分配预期。

评估边界存在明显局限：未报告置信区间，数值比较需谨慎；缺失计算开销分析，MLP预测$\lambda$的额外计算成本未量化；序列分类任务上MoLA略优的现象未深入解释，可能反映固定路由在短文本任务中的均匀分配优势。代码已开源，但超参数$\alpha$、$\beta$的敏感性分析仅在附录中简要提及。

## 关联研究分析

从问题动机看，LD-MoLE与ReMoE（Wang et al., 2025）同属可微动态路由路线，但针对的失效模式不同。ReMoE的ReLU路由通过梯度直通实现可微性，但缺乏对零激活的约束，导致部分Token无专家可用；LD-MoLE的Sparsegen投影通过Lemma 1保证非空支撑，从数学上消除了这一失效。这一差异源于任务特性：预训练阶段数据量大，零激活Token可能被其他Token补偿；PEFT阶段数据量小，单个Token的零激活直接影响性能。ReMoE未探索PEFT场景，其稳定性问题在微调中是否同样存在，论文未给出回答。

从方法设计看，LD-MoLE与MoLA（Gao et al., 2024）同属MoLE框架，但路由哲学根本不同。MoLA的固定TopK将专家选择视为离散优化问题，依赖辅助损失平衡负载；LD-MoLE将稀疏度视为连续可学习变量，通过$\lambda$预测实现内生平衡。这一差异暗示：PEFT场景下，强制均匀分布可能不如自适应稀疏有效。MoLA的实验已显示固定路由下专家利用不均，但将其归因于"冗余"而非"路由僵化"；LD-MoLE通过动态$\lambda$直接解决这一问题，但稀疏损失与负载均衡损失的交互作用未充分分析。当$\beta$增大时，稀疏损失是否会导致部分专家长期未被激活，形成"死专家"，论文未提供专家激活频率的长期追踪数据。

## 总结

LD-MoLE要解决的核心矛盾是PEFT场景下固定TopK路由的僵化性与TopK算子不可微性之间的冲突。现有方法要么依赖人工调参的固定$k$，要么采用可能产生零激活的ReLU路由，均无法同时满足可微性与稳定性要求。LD-MoLE凭借Sparsegen闭式解的数学保证（非空支撑、有界导数）和Token级$\lambda$预测机制，实现了端到端可微的动态稀疏控制。实验证明其在Llama3.2-3B和Qwen3-1.7B上较ReMoLE提升0.6%以上，且跨任务稳定性优于固定路由。边界在于：稀疏损失与任务性能的权衡高度依赖超参数$\beta$，过强约束导致性能下降；序列分类任务上动态路由未展现优势，可能反映短文本任务对均匀专家使用的偏好。当支持集规模从指令微调扩展到预训练阶段时，Token级$\lambda$预测的计算开销是否抵消稀疏激活的收益，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25684)