# CVPR2026最新论文 ｜DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation ｜动态补丁化自回归视觉生成

研究机构：美国加州大学圣迭戈分校

作者：Divyansh Srivastava、Akshay Mehra、Pranav Maneriker 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21867)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21867)

> 自回归视觉生成面临 Token 数量随分辨率平方增长的算力瓶颈，现有 1D 分词器丢失空间结构，静态合并导致信息损失。DPAR 利用轻量级模型的 Next-Token Prediction (NTP) 熵作为信息量代理，动态聚合低信息 Token 为可变长度 Patch，在保留 2D 空间结构的同时降低序列长度。该方法实现了 40% 的训练 FLOPs 削减与 FID 相对提升，但其绝对生成质量仍落后于当前 SOTA，且依赖独立训练的熵模型，存在分布漂移风险。

## 研究背景

自回归图像生成依赖 VQ-VAE 将图像离散化为 2D Token 网格，再按光栅扫描顺序展平为 1D 序列进行 Next-Token Prediction (NTP)。然而，Token 数量 $T$ 与分辨率呈平方关系，例如 256×256 图像需 256 个 Token，而 1024×1024 图像需 4096 个 Token，导致 Attention 机制的计算与内存开销激增。为缓解此问题，1D 分词器（如 TiTok）通过压缩序列长度降低算力，但牺牲了 2D 空间局部性，阻碍了外推与修补等零样本编辑能力；静态 Token 合并方法虽保留空间结构，但固定合并因子常将高信息区域强行聚合，造成细节丢失。

该领域主流路线在“序列长度”与“空间结构”间存在结构性矛盾。VAR 等 Next-Scale 范式通过层级生成减少步数，但未解决单尺度内的 Token 冗余；LlamaGen 等 Next-Token 范式保持架构简洁，却受限于二次方增长的计算成本。DPAR 的切入点在于区分图像区域的信息密度：天空、墙壁等低信息区域可用更少 Token 表示，而纹理丰富区域需保留 Token 级粒度。通过引入 NTP 熵作为动态聚合准则，DPAR 试图在不破坏 2D 空间结构的前提下，实现计算资源向高信息区域的倾斜分配，从而打破固定长度分词器的效率天花板。

## 核心方法

### 方法参照系

标准自回归生成流程为：VQ-VAE 编码 → 光栅扫描展平 → Decoder-only Transformer 预测 → 解码重建。DPAR 的关键差异在于在“展平”与“Transformer 预测”之间插入动态 Patchification 模块，将固定长度的 Token 序列转换为可变长度的 Patch 序列，使 Transformer 在更短的序列上执行 NTP，从而降低 Attention 复杂度。

### 基于 NTP 熵的动态 Patchification

传统静态合并无法区分区域信息密度，导致高信息区细节丢失。DPAR 训练一个轻量级无条件 AR 模型 $E_\phi$ 作为熵模型，计算每个 Token 的 NTP 熵 $e_i$ 作为信息量代理。Patch 边界由熵阈值 $E_{Th}$ 与最大长度 $P_{max}$ 共同决定：当 $e_i \le E_{Th}$ 且当前 Patch 长度 $|P_m| < P_{max}$ 时，Token $x_i$ 并入当前 Patch $P_m$；否则开启新 Patch。该机制确保低熵（低信息）区域被聚合，高熵（高信息）区域保持独立，公式如下：

$$
P_m = \{ x_i \mid s_m \le i \le e_m, \forall j \in [s_m, e_m-1]: e_j \le E_{Th} \}
$$

其中 $s_m, e_m$ 为 Patch 起止索引。此设计解决了静态合并在高信息区造成的信息损失，实现了计算资源的按需分配。

### 轻量级 Patch 编解码架构

为最小化额外开销，DPAR 采用单层 Patch Encoder 与浅层 Patch Decoder。Encoder 将 Patch 内 Token 聚合为与单 Token 维度相同的表示，Decoder 则从生成的 Patch 表示重建 Token 序列。主 Transformer 仅处理 Patch 序列，其层数配置与同规模 LlamaGen 一致，确保公平对比。该架构的设计动机是避免深层编解码器引入的额外计算负担，将算力预算集中于处理变长 Patch 序列的核心 Transformer，从而在降低序列长度的同时保持模型容量不变。

## 实验评估

实验在 ImageNet-256/384 类别条件生成基准上进行，基线为同架构的 LlamaGen 系列。DPAR 未直接对比 VAR 或 BAR 等 Next-Scale 或最新 SOTA 方法，主要验证动态 Patch 化对效率与收敛速度的影响。

| 模型变体 | 分辨率 | FID-50K | 平均 Patch 长度 | 训练 FLOPs 削减 |
| :--- | :--- | :--- | :--- | :--- |
| DPAR-L (Ablation) | 256×256 | 3.32 | 1.81 | — |
| DPAR-XL | 384×384 | 3.58 | 2.06 | 40% |
| LlamaGen-XL | 384×384 | — | — | 0% |

DPAR-XL 在 384×384 分辨率下实现 40% 训练 FLOPs 削减，FID 相对基线提升 27.1%。消融实验显示，熵阈值 $E_{Th}=7.8$ 与最大 Patch 长度 $P_{max}=4$ 组合最优，FID 为 3.32；移除行边界重置或最大长度限制均导致 FID 恶化，表明动态聚合需约束以防止过度合并。

| 消融配置 | $E_{Th}$ | $P_{max}$ | 行边界重置 | FID-50K |
| :--- | :--- | :--- | :--- | :--- |
| 全动态 | 7.8 | 4 | ✓ | 3.32 |
| 无最大长度限制 | 7.8 | ∞ | ✓ | 3.45 |
| 无行边界重置 | 7.8 | 4 | × | 3.91 |
| 静态合并 | — | 1.81 | — | 3.58 |

评估边界方面，论文未报告推理延迟具体数值，仅给出训练 FLOPs 削减比例；熵模型 $E_\phi$ 独立训练，未与主模型联合优化，存在训练-推理分布漂移风险；代码未开源，复现依赖 LlamaGen 基础架构。

## 关联研究分析

从问题动机看，DPAR 与 VAR 均针对自回归生成的效率瓶颈，但路径截然不同。VAR 通过 Next-Scale 范式改变生成顺序，从粗到细层级预测，减少总步数；DPAR 保持 Next-Token 顺序，通过动态压缩序列长度降低单步 Attention 成本。VAR 的优势在于全局一致性，但跨尺度误差累积问题未完全解决；DPAR 的优势在于保留 2D 空间结构，支持零样本编辑，但绝对 FID（3.32-3.58）显著高于 VAR 基线（1.92）及 SOTA（1.15-1.50），表明动态压缩在提升效率的同时牺牲了部分生成保真度。

从方法设计看，DPAR 借鉴 NLP 领域 BLT 的字节合并思想，将 NTP 熵作为信息量代理。与 TiTok 等 1D 分词器相比，DPAR 保留 2D 网格结构，避免了空间局部性丢失；与 Token-Shuffle 等静态合并方法相比，DPAR 的熵驱动机制实现了信息密度自适应。然而，DPAR 依赖独立训练的熵模型，其熵分布可能与主生成模型的 Token 分布存在偏差，尤其在开放域文本条件生成中，这种偏差可能加剧细节模糊。论文未探索熵模型与主模型的联合训练或在线更新机制，限制了其在动态场景下的鲁棒性。

## 总结

DPAR 旨在解决自回归视觉生成中 Token 数量随分辨率平方增长导致的算力冗余，抓住图像区域信息密度不均这一被静态分词器忽略的特性，利用 NTP 熵动态聚合低信息 Token 为可变长度 Patch。实验证明该方法在 384×384 分辨率下实现 40% 训练 FLOPs 削减，FID 相对提升 27.1%，且动态训练赋予模型对 Patch 边界的鲁棒性，支持推理时扩展 Patch 尺寸。然而，DPAR 的绝对 FID 仍高于 VAR 及最新 SOTA，且依赖独立熵模型，未验证联合训练对分布漂移的缓解效果。当图像信息密度分布发生显著变化时，固定熵阈值 $E_{Th}$ 是否仍能维持最优 Patch 长度分配，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21867)