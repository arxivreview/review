# ICLR2026最新论文 ｜Merge before Forget: A Single LoRA Continual Learning via Continual Merging ｜单LoRA持续合并

作者：Fuli Qiao、Mehrdad Mahdavi

论文原文见 [arXiv](https://arxiv.org/abs/2512.23017)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23017)

> 参数高效持续学习（PECL）旨在解决大语言模型在动态任务流中因全参数更新导致的灾难性遗忘，其核心价值在于以极低的参数预算平衡稳定性与可塑性。现有LoRA持续学习方法通过冻结旧适配器或生成伪数据来隔离任务，导致内存随任务数线性增长且存在子空间干扰。本文切入点是将持续学习重构为序列模型合并问题，通过正交初始化与时间感知缩放将新任务更新合并入单一共享LoRA。该方法实现了恒定内存开销，但在高异构任务上的泛化能力仍受限于合并累积误差。

## 研究背景

当大语言模型在顺序任务流中仅更新低秩矩阵时，固定秩约束导致不同任务在拥挤的子空间中碰撞，这种现象称为秩盲性。秩盲性阻碍了有益的知识迁移，而传统LoRA持续学习方法（如O-LoRA）通过冻结旧LoRA并在新正交子空间中训练新LoRA来缓解冲突，但这导致参数存储量随任务数 $T$ 线性增长至 $O(T(m+n)r)$，在存储受限场景下不可扩展。此外，冻结机制缺乏原子的合并机制，导致任务间潜在干扰无法通过优化过程消除。

该领域要解决的核心矛盾是在参数预算严格受限且禁止数据回放的条件下，如何平衡模型对新任务的快速适应与对旧知识的长期保留。主流路线分为低秩子空间正交、专家混合架构及特征解耦。其中，低秩子空间正交路线（如O-LoRA, InfLoRA）通过几何约束隔离任务，但牺牲了知识迁移灵活性且内存开销大；模型合并路线（如KnOTS, LoRA-LEGO）虽能压缩参数，但通常假设并发访问所有任务LoRA，无法处理任务顺序到达的持续学习场景。本文切入点在于发现LoRA组件 $\mathbf{A}$ 和 $\mathbf{B}$ 的内在不对称性，并据此设计序列合并机制，将“存储所有LoRA”转化为“维护单一合并LoRA”，从而在解决子空间冲突的同时消除内存扩展性瓶颈。

## 核心方法

### 方法参照系

本文问题置于“低秩子空间正交”类别下，但关键差异在于不冻结旧LoRA，而是将其合并入单一共享LoRA。标准流程是训练新LoRA后冻结旧LoRA，本文改为训练后执行序列合并，目标函数从最小化单任务风险转为优化多任务合并风险 $\min_{\mathbf{A}, \mathbf{B}} \sum_{t=1}^T \mathcal{L}_t(\mathbf{W}_0 + \mathbf{B}\mathbf{A})$。

### 正交基初始化

设计动机是解决冻结机制导致的 $\mathbf{A}$ 矩阵随机初始化带来的不稳定性。通常做法是随机初始化新任务 $\mathbf{A}$，本文改为从前序合并LoRA $\mathbf{A}_{merge}^{t-1}$ 中提取正交基 $\mathbf{Q}_{t-1}$ 初始化新任务 $\mathbf{A}^{(0)}_t$。

$$ \mathbf{A}^{(0)}_t = \mathbf{Q}_{t-1} \mathbf{U}, \quad \text{s.t. } \mathbf{Q}_{t-1}\mathbf{Q}_{t-1}^\top = \mathbf{I}_r $$

该公式确保新任务 $\mathbf{A}$ 与历史任务保持几何一致性，最小化 $\|\mathbf{A}_t - \mathbf{A}_i\|_F$，从而降低遗忘误差。

### 时间感知不对称合并

设计动机是解决LoRA组件 $\mathbf{A}$ 和 $\mathbf{B}$ 在合并中作用不同导致的性能下降。通常做法是对 $\mathbf{A}$ 和 $\mathbf{B}$ 施加相同的合并权重，本文发现 $\mathbf{A}$ 跨任务相似度高而 $\mathbf{B}$ 低，故引入时间感知缩放机制。

$$ \mathbf{B}_{merge}^t = \alpha_t \mathbf{B}_{merge}^{t-1} + (1-\alpha_t) \mathbf{B}_{ft,t}, \quad \mathbf{A}_{merge}^t = \beta_t \mathbf{A}_{merge}^{t-1} + (1-\beta_t) \mathbf{A}_{ft,t} $$

其中 $\alpha_t, \beta_t$ 随任务索引 $t$ 动态调整，$\mathbf{B}$ 的缩放系数更保守以保留旧知识，$\mathbf{A}$ 的缩放系数更激进以增强可塑性。该机制平衡了知识保留与塑料性，避免了简单平均合并导致的性能退化。

## 实验评估

实验在Llama-2-7B/13B、Llama-3-2-3B及Qwen2.5-3B/7B上进行，覆盖Standard CL、Large Number of Tasks及SuperNI三个基准。基线覆盖SeqLoRA、O-LoRA、InfLoRA、SAPT-LoRA等CL方法，以及KnOTS、LoRA-LEGO等合并方法，但缺失MoE类（如LoRAMoE）和特征解耦类（如SAE-FD）强基线。

| 方法 | Standard CL (avg) | Large Tasks (avg) | SuperNI (avg) |
| :--- | :--- | :--- | :--- |
| O-LoRA | 77.0 | 72.0 | 25.9 |
| SAPT-LoRA | 79.6 | 81.9 | 50.9 |
| KnOTS | 68.2 | 59.9 | 32.8 |
| SLAO | 80.4 | 74.8 | 37.2 |

SLAO在Standard CL上以80.4%的准确率超越O-LoRA的77.0%，但在SuperNI上仅37.2%，远低于SAPT-LoRA的50.9%和Multi-Task的45.2%，表明其在高异构任务上的泛化能力受限。

消融实验显示，正交初始化（Last-FT）相比随机初始化（Random Zero）在Standard CL上提升14.7%（80.4% vs 65.7%），在SuperNI上提升6.1%（37.2% vs 31.1%）。合并策略中，FTBA-MB（冻结B合并A）优于FREB-MA，验证了不对称合并的必要性。然而，SLAO在Large Number of Tasks上的提升幅度（74.8% vs O-LoRA 72.0%）小于Standard CL，暗示合并累积误差在长序列中逐渐显现。

评估边界方面，论文未报告置信区间，且SuperNI结果显著低于Multi-Task，暴露了单LoRA合并机制在高异构任务上的局限性。代码未公开，但实验基于DeepSpeed，超参数细节在附录中提供。

## 关联研究分析

从问题动机看，SLAO与O-LoRA均针对秩盲性导致的子空间冲突，但O-LoRA通过冻结旧LoRA实现隔离，导致内存线性增长；SLAO通过合并消除存储需求，但牺牲了任务间的完全隔离。这一差异根源在于任务特性：O-LoRA假设任务间干扰可通过正交性完全消除，而SLAO承认干扰存在并通过合并优化缓解，但合并过程可能引入累积误差，这在长序列任务中更为显著。

从方法设计看，SLAO与KnOTS同属模型合并路线，但KnOTS假设并发访问所有LoRA，使用SVD投影至共享潜空间；SLAO处理顺序到达任务，引入时间感知缩放。这一差异源于持续学习的顺序性约束，KnOTS的并发假设在CL场景中不成立。SLAO的时间感知缩放是对LoRA不对称性的响应，而KnOTS未考虑组件差异，导致其在CL场景中性能下降（59.9% vs SLAO 74.8% in Large Tasks）。

## 总结

本文要解决的核心矛盾是LoRA持续学习中内存线性增长与子空间干扰的权衡。现有方法如O-LoRA通过冻结隔离任务但内存不可扩展，KnOTS通过合并压缩参数但假设并发访问。本文抓住LoRA组件不对称性这一被忽略的点，通过正交初始化与时间感知缩放实现序列合并，证明了在Standard CL上SLAO以80.4%的准确率超越O-LoRA的77.0%，且内存开销恒定。然而，实验暴露了其在SuperNI高异构任务上仅37.2%的性能，远低于SAPT-LoRA的50.9%，表明合并累积误差在任务异质性高时显著。当任务序列长度增加且异质性增强时，时间感知缩放的固定策略是否足以抑制累积误差，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23017)