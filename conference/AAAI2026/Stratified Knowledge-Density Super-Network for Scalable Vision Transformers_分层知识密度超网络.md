# AAAI2026最新论文 ｜Stratified Knowledge-Density Super-Network for Scalable Vision Transformers ｜分层知识密度超网络

研究机构：东南大学

作者：Longhua Li、Lei Qi、Xin Geng

论文原文见 [arXiv](https://arxiv.org/abs/2511.11683)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11683)

> 视觉Transformer（ViT）部署面临资源约束多样性，传统多模型训练或静态剪枝难以兼顾灵活性与精度。现有弹性网络依赖手动扩展规则，导致小模型知识保留不足。本文提出分层知识密度超网络，通过加权主成分分析（WPAC）与渐进重要性感知Dropout（PIAD）实现任意尺寸子网的O(1)成本提取。该方法在同等压缩比下优于静态剪枝，但依赖30 epoch微调，其“免重训练”优势存疑。

## 研究背景

ViT将图像切分为Token序列，利用自注意力机制建模长程依赖，但二次方计算复杂度使其在边缘设备上部署困难。为适配不同算力预算，业界通常训练多个尺寸变体，或采用结构化剪枝移除冗余参数。然而，结构化剪枝（如WDPruning）需针对每个目标尺寸独立执行剪枝与微调，计算开销大且精度恢复不稳定。

弹性神经网络（如Learngene范式下的TLEG、WAVE）试图通过权重复用生成多尺寸模型，但依赖手动设计的扩展规则，难以在扩展过程中引入尺寸特定的新知识，导致小模型性能显著退化。本文切入点在于：如何在不依赖手动规则的前提下，构建一个知识密度分层分布的超网络，使得任意尺寸子网提取时能最大化保留关键知识，同时避免逐尺寸剪枝的高昂成本。

## 核心方法

### 方法参照系

本文问题属于“可扩展神经网络”范畴，与静态结构化剪枝的关键差异在于：静态剪枝针对单一目标尺寸优化，而本文需构建单一超网络支持连续尺寸提取。传统方法直接移除权重，本文先通过正交变换重参数化，再基于重要性排序移除维度，确保函数保持性。

### WPAC：加权主成分分析

WPAC作用于MHSA模块的线性投影层，解决传统PCA忽略Token重要性差异导致的知识分散问题。设计动机是：均匀PCA无法区分关键Token与冗余Token，导致低维投影丢失高频信息。本文引入一阶Taylor重要性分数 $\Theta_{TE} \in \mathbb{R}^{n \times d}$ 对Token特征进行加权，计算加权协方差矩阵 $\text{Corr}$ 并进行特征分解。

$$
\tilde{X} = \sqrt{\Theta_{token}} \odot (X - \bar{X}), \quad \text{Corr} = \frac{1}{n-1} \tilde{X}^T \tilde{X}
$$

其中 $\Theta_{token}$ 为Token级重要性向量，$\odot$ 表示逐元素乘法。该公式通过平方根加权平衡高重要性Token的贡献，避免极端值主导协方差结构。投影矩阵 $W_{Trans}$ 及其逆矩阵注入相邻层，实现函数保持的维度浓缩。

### PIAD：渐进重要性感知Dropout

PIAD在WPAC生成的SKD网络基础上，解决静态重要性排序无法适应训练动态变化的问题。设计动机是：固定Dropout率导致子网采样分布不均，小模型训练不充分。本文将MHSA维度分为8组、MLP维度分为32组，每组作为可Dropout单元。

$$
I_u = \sum_{i \in u} \alpha_i^{(m)} \cdot \gamma_m \cdot \text{MACs}(u)
$$

其中 $\alpha_i^{(m)}$ 为模块内归一化重要性，$\gamma_m$ 为模块敏感度（跳过该模块的损失增量）。PIAD采用渐进策略：前 $P_e$ 个epoch逐步扩充Dropout列表，训练时随机采样截断索引 $s$，丢弃列表后 $s$ 位单元形成子网，梯度回传至超网。该机制使知识密度随训练进程分层强化，小模型获得更充分的优化。

## 实验评估

实验基于ImageNet-1k，骨干网络为DeiT-B/S/Ti与Swin-B/S/Ti，代理集大小1024。基线覆盖静态剪枝（WDPruning、RePaViT、CP-ViT）与弹性扩展（TLEG、WAVE、Auto-LG），但缺失Token压缩类（如SPOT）与量化类基线，限制了跨路线对比。

| 方法 | MACs | Params | Epochs | Top-1 |
|---|---|---|---|---|
| DeiT-S Original | 4.26 G | 22.05 M | - | 79.83 |
| WDPruning | 3.10 G | 15.00 M | 100 | 78.55 |
| SKD (Ours) | 3.07 G | 16.03 M | 30 | 79.42 |
| DeiT-Ti Original | 1.08 G | 5.72 M | - | 72.14 |
| WDPruning | 0.90 G | 3.80 M | 100 | 71.10 |
| SKD (Ours) | 0.89 G | 4.77 M | 30 | 71.40 |

在DeiT-S 3.07G MACs下，SKD以79.42%超越WDPruning 0.87个百分点，且微调epoch减少70%。DeiT-Ti 0.89G下，SKD 71.40%同样优于WDPruning 71.10%。

消融显示Token级加权优于元素级与维度级：DeiT-B保留56维时，Token级79.71% vs 元素级76.93%。代理集大小影响微弱：128样本时DeiT-B准确率76.6%，2048样本时76.8%，表明小代理集足以捕获主成分结构。PIAD对比Channel Dropout（CD）与LayerDrop（LD），在DeiT-S 10:12尺寸下，PIAD 79.0% vs CD 73.8% vs LD 74.1%，验证渐进策略对小模型的增益。

评估仅报告Top-1准确率与MACs，未提供延迟、能效或对抗鲁棒性指标。代码未公开，超参数（如 $P_e=50$）固定，可复现性受限。

## 关联研究分析

从问题动机看，SKD与Elastic ViTs均解决“免重训练弹性适配”，但Elastic ViTs依赖标签无关剪枝分数直接移除结构，完全免训练；SKD需PIAD阶段30 epoch微调，模糊了后训练压缩（PTP）与训练时压缩（QAT）的边界。根源在于：Elastic ViTs假设预训练模型知识已充分分层，而SKD认为需通过渐进Dropout主动强化分层结构。当预训练模型质量极高时，Elastic ViTs的免训练优势是否更显著，论文未给出回答。

从方法设计看，SKD与WDPruning同属结构化剪枝，但WDPruning基于延迟感知Taylor排序直接移除结构，SKD先通过WPAC正交变换重参数化再移除。差异根源：WDPruning假设权重重要性独立，SKD假设维度间存在协方差结构。在高分辨率输入下，Token间相关性增强，WPAC的协方差建模是否比WDPruning的独立排序更鲁棒，缺乏密集预测任务验证。

## 总结

本文核心矛盾是弹性网络扩展规则手动化导致的小模型知识保留不足。切入点在于利用PCA正交变换实现函数保持的维度浓缩，结合渐进Dropout强化知识分层。方法通过WPAC与PIAD构建超网络，在DeiT-S 3.07G MACs下以79.42%超越WDPruning 0.87个百分点，且微调成本降低70%。边界在于：PIAD阶段仍需30 epoch微调，未实现真正“零训练”提取；实验仅限分类任务，未验证密集预测场景。当代理集扩大至1024以上时，WPAC的协方差估计稳定性是否提升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11683)