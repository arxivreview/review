# WACV2026最新论文 ｜GrowTAS: Progressive Expansion from Small to Large Subnets for Efficient ViT Architecture Search ｜渐进式扩展搜索

研究机构：韩国延世大学

作者：Hyunju Lee、Youngmin Oh、Jeimin Jeon 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12296)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12296)

> Transformer架构搜索（Transformer Architecture Search, TAS）旨在自动化发现高效视觉Transformer（ViT）架构，以替代耗时的人工试错。现有One-shot TAS方法通过训练包含所有候选子网的超网来加速搜索，但子网间共享权重导致训练干扰，严重损害小子网性能。本文发现训练良好的小子网可作为大子网的有效基础，据此提出渐进式训练框架GrowTAS，从小子网逐步扩展至大子网，并引入GrowTAS+微调新增权重以平衡大小子网性能。该方法在ImageNet上实现了SOTA搜索性能，但其对非嵌套搜索空间的适用性及大子网提升幅度有限，限制了其通用性。

## 研究背景

One-shot NAS的核心思想是训练一个超参数化的超网，使其权重覆盖搜索空间内所有候选子网。在TAS中，AutoFormer采用Slimmable网络构建超网，其中小子网的权重是大子网权重的子集。这种嵌套结构使得超网在训练完成后，可通过提取子网权重直接评估其性能，无需从头训练。然而，超网训练时若均匀采样所有子网，小子网权重会同时被用于优化大子网任务，导致梯度冲突。

TAS领域的主流路线试图通过筛选或优先训练高潜力子网来缓解干扰。PreNAS通过剪枝技术评估子网可训练性，仅训练少量高潜力子网，但需针对特定硬件约束重新选择子网；FocusFormer引入可训练采样器动态调整采样概率，但增加了额外计算开销。这些方法均聚焦于优化有限子网集合，导致未选中的小子网性能持续退化。本文切入点在于利用权重继承的不对称性：大子网扩展自小子网时，随机初始化权重的影响微弱，性能得以保持；反之，小子网裁剪自大子网时，结构模式被破坏，性能显著下降。

## 核心方法

### 方法参照系

标准One-shot TAS流程中，超网训练目标为最小化均匀采样子网$\alpha$的损失：$\min_W \mathbb{E}_{\alpha \sim U(A)} [L_{train}(\alpha; W)]$。本文问题与该通用流程的关键差异在于采样策略$U(A)$导致小子网受大子网梯度干扰，需替换为渐进式采样分布。

### 渐进式子网采样

GrowTAS将搜索空间$A$划分为$K$个嵌套子空间$A_1 \subset A_2 \subset \dots \subset A_K$，其中$A_1$包含最小子网，$A_K=A$。训练过程按阶段进行：在$[T_{k-1}, T_k)$区间内，仅从$A_k$中均匀采样子网。训练目标修改为：

$$\min_W \sum_{k=1}^K \mathbb{E}_{\alpha \sim U(A_k)} [L_{train}(\alpha; W) \cdot \mathbb{I}(T_{k-1} \le t < T_k)]$$

该公式的物理含义是：训练早期仅优化小子网权重，避免大子网梯度污染；后期逐步引入大子网，使其继承已训练好的小子网权重作为初始化。这一设计解决了均匀采样下小子网因共享权重被大子网优化目标“拉扯”而性能退化的问题，使小子网在训练初期获得稳定优化环境。

### 新增权重微调

GrowTAS+在超网训练完成后，冻结$A_1$中子网对应的权重$W_{A_1}$，仅微调$A_K \setminus A_1$中新增权重$W_{new}$。优化目标为：

$$\min_{W_{new}} \mathbb{E}_{\alpha \sim U(A_K \setminus A_1)} [L_{val}(\alpha; W_{A_1}, W_{new})]$$

该公式的物理含义是：通过冻结已收敛的小子网权重，防止微调过程破坏其性能，同时允许大子网新增权重充分适应任务。这一策略解决了GrowTAS中大子网新增权重因更新频率低而欠拟合的问题，在不损害小子网性能的前提下提升大子网精度。

## 实验评估

实验在ImageNet-1k上进行，搜索空间为AutoFormer-T/S/B，基线覆盖AutoFormer、PreNAS、FocusFormer等TAS方法，但未包含最新线性注意力或递归架构搜索基线。主结果如下：

| 模型 | Top-1 (%) | #Params (M) | FLOPs (G) |
|---|---|---|---|
| AutoFormer-T | 74.7 | 5.9 | 1.3 |
| GrowTAS-T | 75.19±0.01 | 5.9 | 1.3 |
| PreNAS-T† | 77.1 | 5.9 | 1.3 |
| AutoFormer-B | 82.4 | 54.0 | 11.0 |
| GrowTAS-B | 82.60±0.02 | 53.2 | 11.0 |
| GrowTAS-B+ | 82.67±0.00 | 53.3 | 11.0 |

GrowTAS-B以82.60%精度超越AutoFormer-B的82.4%，但低于PreNAS-B的82.6%（持平）；GrowTAS-T的75.19%显著低于PreNAS-T的77.1%，但后者需额外调参。

消融实验显示，过渡步$T_1$对性能影响显著：AutoFormer-T在$T_1=250$时精度为74.7%，而GrowTAS-T在相同$T_1$下达到75.2%。GrowTAS+对大子网提升明显（GrowTAS-B从82.60%升至82.67%），但对小子网无影响（GrowTAS-T+保持75.19%）。反直觉发现是PreNAS-T虽精度更高，但其分布窄，仅少数子网达到高准确率，而GrowTAS-T在相同约束下产生更多高准确率子网。

评估边界方面，论文未报告置信区间（除GrowTAS系列外），未覆盖密集预测任务，且GrowTAS-T低于PreNAS-T的差异未深入分析。可复现性良好，提供PyTorch实现及详细超参数（AdamW、batch size 128、500 epochs），使用8块A10/A6000 GPU。

## 关联研究分析

从问题动机看，GrowTAS与OFA的渐进策略方向相反：OFA从大子网缩小至小子网，依赖大子网权重初始化小子网；GrowTAS从小子网扩展至大子网，依赖小子网权重初始化大子网。这一差异源于权重继承的不对称性：大子网扩展时随机权重影响微弱，而小子网裁剪时结构破坏严重。OFA未探索小子网作为大子网基础的可行性，因其假设大子网权重更“完整”，但本文实验证明小子网权重已包含足够结构信息。

从方法设计看，GrowTAS与PreNAS均针对子网干扰问题，但PreNAS通过筛选高可训练子网减少干扰，GrowTAS通过渐进训练所有子网消除干扰。PreNAS的筛选策略导致未选中子网性能退化，而GrowTAS的渐进策略确保所有子网均被训练。这一差异源于对“干扰”根源的不同理解：PreNAS认为干扰来自低质量子网，GrowTAS认为干扰来自训练顺序不当。PreNAS未验证筛选策略对小子网性能的长期影响，而GrowTAS通过消融实验证实渐进训练对小子网的稳定提升。

## 总结

GrowTAS要解决的核心矛盾是One-shot TAS中共享权重导致的小子网性能退化。现有方法通过筛选或优先训练部分子网缓解干扰，但牺牲了未选中子网的性能；GrowTAS利用权重继承的不对称性，通过渐进式训练确保所有子网均被有效优化。该方法在ImageNet上实现GrowTAS-B 82.60%精度，超越AutoFormer-B的82.4%，但GrowTAS-T 75.19%低于PreNAS-T的77.1%。其边界在于对非嵌套搜索空间的适用性未验证，且大子网提升幅度有限（GrowTAS-B+仅提升0.07%）。当搜索空间包含不同注意力机制混合时，渐进式扩展策略是否仍能保持小子网性能稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12296)