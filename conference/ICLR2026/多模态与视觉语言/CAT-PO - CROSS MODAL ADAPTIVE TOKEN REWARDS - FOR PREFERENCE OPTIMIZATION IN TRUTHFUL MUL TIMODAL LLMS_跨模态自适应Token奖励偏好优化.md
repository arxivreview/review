# ICLR2026最新论文 ｜CAT-PO: CROSS MODAL ADAPTIVE TOKEN REWARDS - FOR PREFERENCE OPTIMIZATION IN TRUTHFUL MUL TIMODAL LLMS ｜跨模态自适应Token奖励偏好优化

研究机构：中国科学技术大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_4061123)

> 多模态大语言模型（MLLMs）在生成文本时，常因语言先验压制视觉信号而产生幻觉。现有直接偏好优化（DPO）方法将响应序列视为整体进行优化，忽略了不同Token对视觉事实贡献度的巨大差异，导致对关键视觉Token的修正力度不足。Cat-PO通过计算Token级的全局、局部及语义视觉相关性，构建分层奖励机制，对DPO损失函数进行加权改造。该方法在不引入外部检测器的前提下，显著降低了幻觉率，但其固定权重融合策略在复杂对抗场景下的鲁棒性仍存疑。

## 研究背景

当MLLMs处理视觉问答任务时，模型内部不同Token对图像的注意力分布与语义相似度存在显著差异。这种差异意味着，部分Token（如物体名词）紧密关联视觉证据，而另一些Token（如功能词）主要依赖语言统计规律。若忽略这种Token级的异质性，统一施加优化压力，模型难以精准定位并修正那些导致幻觉的关键视觉断言。

DPO通过解析KL正则化目标，直接优化策略模型以拟合成对偏好，消除了显式奖励模型，成为多模态对齐的主流范式。然而，标准DPO假设序列级奖励是均匀的，未区分Token对视觉内容的依赖程度。TPO（Gu et al., 2024）虽探索了Token级信息，但依赖自校准视觉锚点；V-DPO（Xie et al., 2024）侧重图像对比偏好，均未能充分利用模型内部固有的跨模态注意力与语义信号。Cat-PO的切入点在于，直接挖掘MLLMs内部Transformer层的跨模态注意力与语义相似度，构建无需外部工具的Token级视觉相关性奖励，实现细粒度的幻觉抑制。

## 核心方法

### 方法参照系

标准DPO损失函数基于Bradley-Terry模型，通过最大化偏好响应与拒绝响应的对数概率差来优化策略模型。其核心假设是序列级奖励均匀分布，未考虑响应中不同Token对视觉事实的贡献差异。Cat-PO在此参照系上，将序列级标量奖励解构为Token级的分层视觉相关性权重，并引入Token级KL正则化。

### 分层视觉相关性计算

Cat-PO首先利用模型内部的跨模态注意力机制，计算每个响应Token $y_t$ 对图像的全局相关性 $S_{global}(y_t)$，定义为该Token对所有视觉Patch注意力分数的总和。这一设计解决了标准DPO无法区分Token视觉依赖程度的问题，使得优化过程能够聚焦于与图像强关联的Token。

$$ S_{global}(y_t) = \sum_{j=1}^{N_p} a_{t,j} $$

其中 $a_{t,j}$ 为Token $y_t$ 对第 $j$ 个视觉Patch的注意力分数。全局相关性高表明模型在处理该Token时更关注图像整体，暗示其视觉接地性强。

### 局部熵与语义融合

仅全局相关性无法反映注意力是否聚焦于关键区域。Cat-PO引入基于Patch熵的局部相关性 $S_{local}(y_t)$，通过计算注意力分布的熵值来衡量注意力的集中程度。低熵意味着注意力聚焦于少数Patch，表明Token与特定局部区域强关联。

$$ S_{local}(y_t) = 1 - \frac{H(P_t)}{\log N_p} $$

其中 $H(P_t)$ 为归一化注意力分布 $P_t$ 的熵。此外，Cat-PO利用预训练跨模态编码器计算Token嵌入与视觉特征的语义相似度 $S_{semantic}(y_t)$，作为先验语义信号。三者通过平衡系数 $\alpha$ 融合为统一视觉相关性分数 $s_i$，并经 $\tanh$ 函数映射为平滑权重 $T_i$，确保梯度稳定。

### 加权DPO损失

Cat-PO将Token权重 $w_t$ 引入DPO损失，对偏好响应中的高视觉相关性Token施加更大优化力度，对拒绝响应中的低视觉相关性Token施加惩罚。同时，引入Token级KL散度正则化，防止模型过度偏离参考分布。

$$ \mathcal{L}_{Cat-PO} = -\mathbb{E}_{(x, y_+, y_-) \sim D} \left[ \log \sigma \left( \beta \sum_{t} w_t^+ \log \frac{\pi_\theta(y_t^+|x)}{\pi_{ref}(y_t^+|x)} - \beta \sum_{t} w_t^- \log \frac{\pi_\theta(y_t^-|x)}{\pi_{ref}(y_t^-|x)} \right) \right] + \lambda_{KL} \mathbb{D}_{KL}(\pi_\theta \| \pi_{ref}) $$

该损失函数通过加权机制，使模型优先修正那些视觉证据强但被错误生成的Token，从而精准抑制幻觉。

## 实验评估

实验基于LLaVA-v1.5-7B/13B与Qwen2.5VL-3B模型，使用RLHF-V数据集训练6个Epoch，Batch Size为32。基线覆盖DPO、TPO、V-DPO、RLHF-V等主流方法，但缺失SCPO、PEA-DPO等2025-2026年引入外部工具或课程学习的最新SOTA方法。

| 方法 | AMBER-Gen CHAIR↓ | MM-Hal Rate↓ | POPE Acc↑ |
| :--- | :--- | :--- | :--- |
| LLaVA-v1.5-7B | 7.8 | 61.4 | - |
| + DPO | 5.7 | 58.3 | - |
| + TPO | - | 51.0 | - |
| + Cat-PO | 4.8 | 42.0 | 95.2 |

Cat-PO在AMBER-Gen CHAIR上取得4.8，较DPO的5.7降低14.0%；MM-Hal Rate降至42.0，较DPO的58.3降低27.9%。POPE Acc达到95.2%，接近SOTA水平。

| 模块 | MM-Hal Score↑ | MM-Hal Rate↓ |
| :--- | :--- | :--- |
| DPO-only | 2.14 | 58.3 |
| Attention-only | 2.34 | 55.0 |
| Similarity-only | 2.51 | 47.0 |
| Cat-PO (Ours) | 2.74 | 42.0 |

消融实验显示，单独使用注意力或语义相似度均能提升性能，但二者结合带来最大增益。移除KL正则化导致性能下降，验证了Token级KL的必要性。可学习融合权重效果不佳，表明固定均匀权重在DPO框架下更稳定。

评估协议未报告置信区间，且未对比计算效率。代码已开源，但超参数 $\alpha$ 与 $\lambda_{KL}$ 的敏感性分析显示，$\lambda_{KL}=0.03$ 时性能最优，提示KL正则化强度对模型灵活性至关重要。

## 关联研究分析

从问题动机看，Cat-PO与PEA-DPO（Feng et al., 2026）均致力于解决视觉不敏感问题，但路径截然不同。PEA-DPO依赖CLIP移除图像关键上下文构建负样本，属于外部数据增强策略；Cat-PO则完全依赖模型内部注意力与语义信号，无需外部工具。这一差异源于Cat-PO假设预训练MLLMs已具备足够的跨模态表征能力，而PEA-DPO认为需通过数据扰动强制模型关注视觉细节。Cat-PO在MM-Hal Rate上（42.0）显著落后于PEA-DPO（3.2），暗示内部信号在复杂视觉场景下的判别力可能不及外部扰动。

从方法设计看，Cat-PO与TPO（Gu et al., 2024）同属Token级优化路线，但TPO依赖自校准视觉锚点，需额外计算锚点位置；Cat-PO直接利用Transformer层注意力，计算开销更低（仅增加38%训练时间）。Cat-PO的固定权重融合策略在对抗子集上性能略降（Acc从95.2%降至91.3%），而TPO未报告对抗鲁棒性。这提示，当视觉信号与语言先验冲突剧烈时，固定权重可能无法动态调整，导致对幻觉Token的修正不足。

## 总结

Cat-PO针对标准DPO忽略Token级视觉异质性的缺陷，通过计算全局、局部及语义视觉相关性，构建分层奖励机制，实现细粒度幻觉抑制。在LLaVA-v1.5-7B上，其MM-Hal Rate降至42.0，AMBER-Gen CHAIR降至4.8，显著优于DPO基线。然而，实验显示可学习融合权重效果不佳，且对抗子集性能下降，暴露了固定权重策略在复杂场景下的局限性。当视觉信号与语言先验冲突剧烈时，固定权重是否足以动态平衡两者，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_4061123)