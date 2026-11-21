# ICLR2026最新论文 ｜CoRA: Boosting Time Series Foundation Models for Multivariate Forecasting through Correlation-aware Adapter ｜相关性感知适配器

研究机构：华东师范大学

作者：Hanyin Cheng、Xingjian Wu、Yang Shu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.21828)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21828)

> 多变量时间序列预测中，通道间存在动态、异质与偏相关三种复杂依赖，但主流时间序列基础模型（TSFM）采用通道独立策略，仅捕捉时间依赖而忽略通道交互。现有插件如C-LoRA需从头训练，无法适配预训练模型，且未区分相关性的不同形态。CoRA作为轻量级插件，通过低秩分解估计动态相关性，并利用双空间对比学习解耦异质与偏相关，仅需微调即可提升TSFM性能。该方法在少样本场景下有效，但缺乏与最新零样本SOTA的直接对比，其泛化边界尚待验证。

## 研究背景

多变量时间序列预测面临的核心困境是通道间依赖关系的复杂性。动态相关性（DCorr）描述通道关系随时间变化，异质相关性（HCorr）区分正负相关交互，偏相关性（PCorr）强调仅部分通道存在关联。若模型无法区分这三者，全通道交互会引入噪声，导致预测精度下降。

TSFM通过大规模预训练实现零样本泛化，但多数模型（如TimesFM、Chronos）采用通道独立架构，仅捕捉时间依赖。TTM等模型虽引入MLP通道混合，但权重固定，无法建模DCorr；UniTS和Moirai使用注意力机制，但全通道交互未区分HCorr与PCorr。此外，不同数据集的相关性结构差异巨大，预训练阶段难以捕捉通用相关性，导致下游微调时性能受限。

CoRA的切入点在于设计一个轻量级插件，在微调阶段显式建模三类相关性，避免预训练阶段的相关性差异问题。该插件不修改TSFM骨干，仅利用其内部表征与原始预测，通过低秩分解与对比学习实现高效适配，解决了现有插件无法适配预训练模型且相关性建模不全面的缺陷。

## 核心方法

### 方法参照系

CoRA属于TSFM后训练适配路线，标准流程为提取骨干中间表征并微调适配器。关键差异在于：CoRA不直接微调表征，而是先估计动态相关性矩阵，再基于该矩阵引导对比学习解耦异质与偏相关，实现通道依赖的显式建模。

### 动态相关性估计

传统方法使用固定权重或全注意力捕捉通道关系，无法区分时间变化与稳定依赖。CoRA将相关性矩阵分解为时变与时不变低秩组件，利用可学习时间感知多项式捕捉趋势与周期性。设时变组件为 $\mathbf{Q}_t \in \mathbb{R}^{N \times M}$，时不变组件为 $\mathbf{V} \in \mathbb{R}^{M \times M}$，最终相关性矩阵为：

$$\mathbf{M}_t^{\text{corr}} = \mathbf{R} + \mathbf{Q}_t \mathbf{V}$$

其中 $\mathbf{R}$ 为基于皮尔逊系数的规则基矩阵。该设计以线性复杂度替代 $O(N^2)$ 的全通道交互，同时保留动态与稳定依赖的分离建模能力。

### 异质偏相关对比学习

全通道交互无法区分正负相关与部分相关，导致噪声引入。CoRA通过通道感知投影将表征映射至正负相关空间，并在每个空间内执行偏相关对比学习。设正负空间表征为 $\tilde{\mathbf{X}}_t^{\text{pos}}$ 和 $\tilde{\mathbf{X}}_t^{\text{neg}}$，对比损失为：

$$\mathcal{L}_{\text{H-PCorr}} = \sum_{c \in \text{pos}} \log \frac{\exp(\text{sim}(\tilde{\mathbf{x}}_c, \tilde{\mathbf{x}}_{c^+})/\tau)}{\sum_{c' \neq c} \exp(\text{sim}(\tilde{\mathbf{x}}_c, \tilde{\mathbf{x}}_{c'})/\tau)} + \sum_{c \in \text{neg}} \log \frac{\exp(\text{sim}(\tilde{\mathbf{x}}_c, \tilde{\mathbf{x}}_{c^-})/\tau)}{\sum_{c' \neq c} \exp(\text{sim}(\tilde{\mathbf{x}}_c, \tilde{\mathbf{x}}_{c'})/\tau)}$$

该损失在正空间拉近强正相关通道，在负空间拉近强负相关通道，同时推开弱相关通道，实现偏相关的自适应学习。

## 实验评估

实验在ETT、Electricity、Weather等10个数据集上进行，采用5%少样本微调协议，指标为MSE。基线覆盖GPT4TS、UniTime、Moment、Timer、TTM等LLM及预训练模型，但缺失Chronos-2、TimesFM-2.5等2025-2026年最新零样本SOTA，限制了与当前前沿的直接对比。

| 骨干模型 | ETTm2 (MSE) | Electricity (MSE) | Weather (MSE) |
| :--- | :--- | :--- | :--- |
| TTM | 0.259 | 0.226 | 0.224 |
| TTM + CoRA | **0.254** | **0.212** | **0.210** |
| CALF | 0.272 | 0.238 | 0.230 |
| CALF + CoRA | **0.264** | **0.231** | **0.223** |

CoRA在TTM和CALF骨干上均带来一致提升，其中Electricity数据集MSE从0.226降至0.212，降幅约6.2%。消融实验显示，动态相关性估计（DCorr）贡献最大，移除后ETTm2 MSE从0.269升至0.279；异质划分（HCorr）与偏相关对比学习（PCorr）的边际收益较小，但组合后性能最优。

评估边界存在局限：仅报告MSE，未提供CRPS等概率指标；未报告推理延迟与内存占用，无法验证“轻量级”声明的实际效率；代码未开源，超参数细节缺失，可复现性受限。

## 关联研究分析

从问题动机看，CoRA与C-LoRA同属插件式适配，但C-LoRA需从头训练端到端模型，无法利用预训练TSFM的通用知识，而CoRA专为预训练模型设计，通过微调适配器保留骨干能力。这一差异源于任务特性：预训练模型已具备时间依赖表征，仅需补充通道依赖，而非从头学习。

从方法设计看，CoRA与CCM均涉及通道聚类，但CCM需额外预训练聚类头，且未区分动态与静态相关性，而CoRA通过低秩分解与对比学习实现动态相关性的显式建模。CCM的聚类基于静态特征，无法捕捉相关性随时间的变化，这是其在非平稳数据上性能受限的根源。

## 总结

CoRA解决的核心矛盾是TSFM通道独立架构与多变量预测中复杂通道依赖之间的冲突。现有插件无法适配预训练模型且相关性建模不全面，CoRA通过低秩分解与双空间对比学习，在微调阶段显式建模动态、异质与偏相关，以线性复杂度实现高效适配。实验证明其在5%少样本场景下提升TTM与CALF性能，Electricity数据集MSE降至0.212。边界在于缺乏与最新零样本SOTA的对比，且未验证在零样本场景下的有效性。当微调数据量从5%增至20%时，CoRA的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21828)