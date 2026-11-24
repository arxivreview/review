# ICLR2026最新论文 ｜FAST PROTEOME-SCALE PROTEIN INTERACTION RETRIEVAL VIA RESIDUE-LEVEL FACTORIZATION ｜残基级因子化实现全基因组蛋白互作检索

研究机构：加拿大蒙特利尔大学

作者：Jianan Zhao、Zhihao Zhan、Narendra Chaudhary 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_23590722)

> 全基因组规模的蛋白质-蛋白质相互作用（Protein-Protein Interaction, PPI）预测旨在从约两万个蛋白中筛选出潜在互作对，但传统成对推理方法因计算复杂度呈二次方增长而难以落地。现有高精度模型需对每个蛋白对进行联合编码，导致全基因组筛选耗时数月，而简单嵌入检索又丢失了残基级交互细节。RaftPPI通过高斯核近似与低秩注意力将残基交互因子化为单蛋白嵌入，实现了分钟级的全基因组检索。该方法在严格控制的基准上达到了分类与检索性能的最优平均表现，但其仅依赖序列模态的设计在构象依赖型互作中的泛化能力存疑。

## 研究背景

理解细胞机制需要识别蛋白间的物理接触，这种接触发生在氨基酸残基层面。然而，全基因组筛选要求评估约 $2 \times 10^8$ 个候选蛋白对，若采用端到端结构预测器，其 $O(L^3)$ 的复杂度使得逐对推理在计算上不可行。即便采用基于序列的二分类模型，其 $O(N^2L^2)$ 的成对编码成本依然导致全基因组筛选耗时数月，例如PLM-Interact需148.47个A100 GPU-days。

主流序列基PPI模型如D-SCRIPT和PLM-Interact通过预测残基接触矩阵并聚合为蛋白级分数，虽精度较高但无法因子化，即无法将成对计算拆解为独立的单蛋白编码。这种非因子化特性阻碍了利用近似最近邻（Approximate Nearest Neighbor, ANN）搜索进行大规模检索。RaftPPI的切入点在于保留残基级交互精度的同时，通过数学近似将成对计算转化为单蛋白嵌入的内积，从而兼容高效的向量索引检索。

## 核心方法

### 残基交互预测与聚合范式

标准PPI预测遵循“预测-聚合”（Pred&Agg）流程：首先利用预训练蛋白语言模型（Protein Language Model, PLM）获取残基嵌入，计算残基对接触分数矩阵 $\mathbf{C} \in \mathbb{R}^{L_A \times L_B}$，再通过池化操作 $g(\cdot)$ 聚合为蛋白级对数几率 $\ell(A, B)$。该范式的关键局限在于接触分数计算涉及跨蛋白的非线性交互，导致无法将 $\ell(A, B)$ 分解为 $\langle \mathbf{h}_A, \mathbf{h}_B \rangle$ 的形式，从而无法构建静态索引。

### 高斯核近似与低秩注意力因子化

为突破成对计算瓶颈，RaftPPI将残基交互建模为高斯核 $k_{\hat{\sigma}}(\mathbf{z}_{A,i}, \mathbf{z}_{B,j}) = \exp(-\|\mathbf{z}_{A,i} - \mathbf{z}_{B,j}\|^2 / 2\hat{\sigma}^2)$，并利用结构化正交随机特征（Structured Orthogonal Random Features, SORF）将其近似为有限维内积。

$$
k_{\hat{\sigma}}(\mathbf{z}_{A,i}, \mathbf{z}_{B,j}) \approx \phi(\mathbf{z}_{A,i})^\top \phi(\mathbf{z}_{B,j})
$$

其中 $\phi(\cdot)$ 由SORF矩阵 $\mathbf{W}$ 定义，该设计使得核函数可分解为单蛋白特征的函数。随后，采用秩-1低秩注意力 $s_{i,j} = w_{A,i} w_{B,j}$ 聚合残基分数，最终蛋白级对数几率简化为：

$$
\ell(A, B) \approx \langle \mathbf{h}_A, \mathbf{h}_B \rangle, \quad \mathbf{h}_A = \sum_{i=1}^{L_A} w_{A,i} \phi(\mathbf{z}_{A,i})
$$

这一因子化设计将 $O(N^2L^2)$ 的成对计算转化为 $O(NL^2)$ 的单蛋白编码，使得每个蛋白可独立编码为固定长度向量，直接支持HNSW等ANN搜索算法。

### 自适应负权重损失

针对PPI数据中负样本多为人工构建且质量参差不齐的问题，RaftPPI引入自适应负权重（Adaptive Negative Weighting, ANW）损失。该损失根据模型对负样本的置信度动态调整权重，使模型更关注难以区分的“硬负样本”。

$$
\mathcal{L} = \frac{1}{|P|} \sum_{i \in P} \mathcal{L}_{pos}(i) + \frac{1}{|N|} \sum_{j \in N} p_j \mathcal{L}_{neg}(j)
$$

其中 $p_j$ 为温度缩放的模型置信度，当 $\tau \to \infty$ 时聚焦于最难的负样本。该设计缓解了随机配对产生的过于简单的负样本导致的过拟合，提升了模型在分布外数据上的鲁棒性。

## 实验评估

实验采用Bernett et al. (2024)提供的7个严格划分数据集（涵盖酵母与人），这些数据集移除了序列相似性泄漏并控制了节点度偏差，以评估模型的真实泛化能力。基线覆盖了经典序列模型（D-SCRIPT, SPRINT）和PLM基线（ESM2-MLP, PLM-Interact），但缺失几何图或生成式方法，因任务性质不同不可比。

| 方法 | D-SCRIPT | Huang | Pan | Richoux | Gold | Guo | Du | Average |
|---|---|---|---|---|---|---|---|---|
| ESM2-NoFT | 75.01 | 58.63 | 59.51 | 63.26 | 57.85 | 62.87 | 57.36 | 62.07 |
| PLM-Interact | 84.77 | 69.69 | 73.03 | 78.66 | 65.00 | 79.60 | 75.20 | 75.14 |
| RaftPPI | 82.06 | 72.20 | 74.21 | 69.88 | 68.69 | 84.93 | 75.06 | 75.29 |

RaftPPI在平均AUROC上以75.29%略胜PLM-Interact的75.14%，但在Richoux数据集上显著落后（69.88% vs 78.66%），表明其因子化近似在特定序列分布下存在精度损失。在检索效率上，RaftPPI在人类基因组上检索Top 20%对仅需5.7分钟（A100），覆盖75.1%真实互作对，而PLM-Interact需4.9个月且仅覆盖61.2%，实现了$10^4$倍加速。

消融实验显示，移除残基级建模（RaftPPI-P）导致Recall@20%下降约46%，证实了残基交互对大规模检索的必要性。替换高斯核为线性点积（Raft-WoSORF）一致降低了AUROC，验证了核方法在捕捉非线性交互中的优势。自适应负权重在难负样本比例高的数据集上表现更佳，但在简单负样本主导的数据集上收益有限。

评估协议未报告置信区间，且仅使用ESM2-8M骨干，未探索更大规模PLM的影响。代码已开源，但HNSW索引构建参数未详细披露，可能影响复现性。

## 关联研究分析

从问题动机看，RaftPPI与DrugCLIP同属对比检索范式，但前者聚焦蛋白-蛋白互作，后者针对蛋白-配体结合。DrugCLIP通过对比学习将口袋与配体嵌入共享空间，但依赖3D结构输入；RaftPPI仅用序列，通过高斯核近似保留残基级细节。这一差异源于PPI数据中3D结构稀缺，而序列信息更丰富。RaftPPI的因子化设计使其能处理全基因组规模，而DrugCLIP受限于结构数据可用性，无法扩展至全基因组。

从方法设计看，RaftPPI与PLM-Interact均基于ESM2，但后者采用早期融合联合编码蛋白对，前者通过SORF近似实现因子化。PLM-Interact在Richoux数据集上AUROC高达78.66%，而RaftPPI仅69.88%，表明因子化近似在捕捉长程依赖时存在信息损失。这一差距可能源于高斯核的局部性假设，无法充分建模跨蛋白的全局结构互补性。RaftPPI通过牺牲部分精度换取数量级效率提升，适用于初筛场景，而PLM-Interact更适合小规模高精度验证。

## 总结

RaftPPI旨在解决全基因组PPI预测中计算复杂度与残基级精度之间的矛盾。通过高斯核近似与低秩注意力，它将成对计算因子化为单蛋白嵌入，实现了分钟级检索。实验证明其在严格基准上达到最优平均AUROC 75.29%，并将检索时间从4.9个月缩短至5.7分钟。然而，其在Richoux数据集上的显著性能下降暴露了因子化近似在特定序列分布下的局限。当蛋白对存在强长程结构依赖时，高斯核的局部交互建模是否足以捕捉关键结合特征，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_23590722)