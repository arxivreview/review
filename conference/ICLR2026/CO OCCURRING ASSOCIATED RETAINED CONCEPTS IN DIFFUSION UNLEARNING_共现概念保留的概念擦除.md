# ICLR2026最新论文 ｜CO OCCURRING ASSOCIATED RETAINED CONCEPTS IN DIFFUSION UNLEARNING ｜共现概念保留的概念擦除

研究机构：美国普林斯顿高等研究院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_67301436)

> 扩散模型概念擦除面临鲁棒性与效用性的权衡，现有方法在移除目标概念时往往意外抑制与其自然共现的良性概念，且缺乏度量此现象的指标。本文定义共现关联保留概念（Co-occurring Associated Retained concepts, CARE），提出CARE score指标显式量化其保留程度，并设计ReCARE框架通过构建CARE-set在训练目标中同时约束擦除与保留。该方法在Nudity、Van Gogh和Tench任务上实现了鲁棒性、效用与CARE保留的最优平衡，但其CARE-set构建依赖目标图像质量，且未验证多概念大规模擦除场景下的扩展性。

## 研究背景

当扩散模型执行概念擦除时，目标概念在参数空间中与相关概念高度纠缠。以擦除“nudity”为例，训练数据中“nudity”常与“person”共现，导致模型在移除前者时，后者表征也被连带抑制。这种附带损伤并非随机噪声，而是源于CLIP等文本编码器将共现概念映射至重叠嵌入区域，使得语义边界模糊。现有评估指标如FID和CLIP score仅捕捉全局保真度或提示词相似度，无法检测特定良性概念是否被意外抹除。

概念擦除的主流路线是通过微调交叉注意力层，将目标概念分布重定向至无条件输出。ESD（Gandikota et al., 2023）确立了这一范式，但其在概念纠缠场景下易导致严重的模型退化。后续工作如AdvUnlearn引入对抗训练提升鲁棒性，AGE通过自适应锚点平衡遗忘与保留，但均依赖外部标签集（如ImageNet）或LLM生成的锚点。这些静态锚点往往与目标概念缺乏语义关联，无法有效保护那些与目标紧密共现的良性概念。本文切入点在于识别并量化这种“良性共现概念抑制”现象，指出现有方法在追求擦除鲁棒性时，牺牲了模型对非目标但相关概念的生成能力。

## 核心方法

### 方法参照系

本文基于后验擦除范式，继承ESD的微调框架，但核心差异在于锚点来源与训练目标的解耦设计。传统方法使用外部通用标签作为保留锚点，而本文从目标图像中提取动态CARE-set，并将其同时嵌入擦除损失与保留损失中，实现方向上的正交分离。

### CARE-set构建与精炼

CARE-set的构建旨在从目标图像中提取良性共现词，同时剔除有害共现词与无关词。首先，计算目标图像集 $I$ 中每张图像 $x$ 与CLIP词汇表 $V$ 中每个token $t$ 的相似度，选取Top-K高频token构成候选集。随后，通过全局聚类与簇内精炼两级过滤。全局聚类利用t-SNE将候选token投影至2D空间，通过k-means分为 $n$ 簇，计算每簇token与目标嵌入 $e_c$ 的正交距离残差 $\bar{r}_k$，丢弃距离最小（最相似）与最大（最无关）的簇。簇内精炼进一步计算簇内token与簇质心的距离，剔除仍与目标高度对齐的残留有害token。最终形成的CARE-set $D$ 仅包含真正良性且相关的概念。

$$
\delta_{i[k]} = \mathbb{1}\left[ \left\| e_{t_{i[k]}} - \bar{e}_{C_k \setminus t_{i[k]}} \right\|_2 > \alpha \cdot \left\| e_{t_{i[k]}} - e_c \right\|_2 \right]
$$

该公式通过比较token与簇质心的距离和与目标嵌入的距离，动态判断token是否应被保留，$\alpha$ 控制剪枝严格度。

### 基于CARE-set的训练目标

ReCARE的训练目标由擦除损失与保留损失组成，CARE-set $D$ 在其中扮演双重角色。保留损失约束模型在CARE概念上的输出与原始模型一致，防止良性概念被抑制。擦除损失则利用CARE-set作为参考，将有害token的表征对齐至“CARE表征减去擦除方向”的参考点，从而在移除目标的同时保留共现结构。擦除方向通过文本反转（Textual Inversion）获得，利用STEREO方法生成能重新激活目标概念的嵌入序列，计算平均擦除向量。

$$
\mathcal{L}_{erase} = \left\| \epsilon_\theta(z_t | H) - \left( \epsilon_{\theta^*}(z_t | D) - \epsilon_{erase} \right) \right\|_2^2
$$

该公式将有害token $H$ 的噪声预测对齐至CARE表征减去擦除方向后的参考值，确保擦除操作不破坏CARE概念的语义结构。

## 实验评估

实验在SD v1.4上进行，任务涵盖Nudity、Van Gogh风格和Tench物体擦除。基线覆盖ESD、UCE、MACE、STEREO、AdvUnlearn等11种方法，但缺失SAEMNESIA等2025年基于稀疏自编码器的可解释性方法。评估指标包括ASR（鲁棒性）、FID/CLIP（效用）及新增CARE score。

| 任务 | 方法 | ASR (CCE) ↓ | CLIP ↑ | CARE score ↑ | RATIO ↑ |
|---|---|---|---|---|---|
| Nudity | ReCARE | 11.14 | 0.3053 | 0.94 | 0.76 |
| Nudity | STEREO | 19.55 | 0.2907 | 0.11 | 0.21 |
| Nudity | ESD | 53.41 | 0.2931 | 0.89 | 0.49 |
| Van Gogh | ReCARE | 6.00 | 0.3101 | 0.90 | 0.81 |
| Van Gogh | STEREO | 4.00 | 0.3047 | 0.31 | 0.43 |
| Tench | ReCARE | 0.40 | 0.3073 | 0.97 | 0.85 |
| Tench | STEREO | 3.60 | 0.2975 | 0.62 | 0.56 |

ReCARE在Nudity任务上CARE score达0.94，显著高于STEREO的0.11，表明其有效保留了“person”概念。在Van Gogh任务上，ReCARE的ASR为6.00，略高于STEREO的4.00，但CARE score从0.31提升至0.90，解决了STEREO严重抑制“stars”概念的问题。

消融实验显示，全局聚类与簇内精炼均对CARE score和ASR有显著影响。移除全局聚类导致CARE score从0.94降至0.90，ASR从11.14升至25.00，表明无关token的引入干扰了保留信号。移除簇内精炼使CARE score降至0.93，ASR升至16.36，证实残留有害token的过滤必要性。簇数 $n$ 对性能影响较小，$n=6$ 时取得最佳平衡。

评估边界方面，CARE score基于CLIP R-Precision@1，其可靠性通过与人类标注的Pearson相关系数（r=0.905）验证，但CLIP模型本身的偏差可能影响度量准确性。实验仅验证单概念擦除，未涉及多概念大规模场景。代码已开源，但超参数如 $\alpha$ 和 $\lambda$ 的敏感性分析未在正文中详细展开。

## 关联研究分析

从问题动机看，ReCARE与AdvUnlearn均关注鲁棒性-效用权衡，但AdvUnlearn依赖外部锚点，而ReCARE从目标图像中提取动态CARE-set。这一差异源于任务特性：AdvUnlearn假设锚点与目标概念无强关联，而ReCARE针对共现概念纠缠场景，静态锚点无法提供有效的保留信号。ReCARE的CARE-set构建是否引入数据泄露风险，论文未给出回答。

从方法设计看，ReCARE与STEREO同属文本反转增强路线，但STEREO将反转嵌入用于计算擦除方向，而ReCARE将其用于解耦有害与良性表征。STEREO在Nudity任务上ASR更低（19.55 vs 11.14），但CARE score极低（0.11），表明其擦除方向过于激进，破坏了共现结构。ReCARE通过CARE-set约束擦除方向，实现了更精细的语义分离。

## 总结

ReCARE解决的核心矛盾是概念擦除中鲁棒性与良性共现概念保留的冲突。现有方法因依赖静态外部锚点，无法保护与目标紧密共现的良性概念，而ReCARE通过从目标图像动态构建CARE-set，并在训练目标中同时约束擦除与保留，实现了语义结构的精细分离。实验证明，ReCARE在Nudity任务上CARE score达0.94，ASR为11.14，在Van Gogh任务上CARE score达0.90，显著优于基线。其边界在于CARE-set构建依赖目标图像质量，且仅验证单概念擦除。当擦除概念数量增加至100以上时，CARE-set的动态更新与计算开销是否可控，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_67301436)