# ICLR2026最新论文 ｜IVC-Prune: Revealing the Implicit Visual Coordinates in LVLMs for Vision Token Pruning ｜基于旋转位置编码隐含坐标的视觉Token剪枝

研究机构：武汉大学

作者：Zhichao Sun、Yidong Ma、Gang Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03060)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03060)

> 视觉语言模型在处理高分辨率图像时，视觉Token数量激增导致计算成本与内存占用成为部署瓶颈。现有剪枝方法多依赖语义相关性或注意力分数筛选Token，但在视觉定位等空间敏感任务上性能显著下降，根源在于忽略了Token中隐含的空间坐标功能。本文通过理论分析揭示旋转位置编码（RoPE）中特定位置Token充当绝对空间参考系，提出保留这些隐含视觉坐标（Implicit Visual Coordinate, IVC）Token与语义前景Token的免训练剪枝策略。该方法在保持约50% Token的前提下，将视觉定位任务性能损失控制在1%以内，但其在非RoPE架构及极端压缩率下的泛化能力尚存疑。

## 研究背景

高分辨率图像输入使视觉语言模型（Large Vision-Language Models, LVLMs）的视觉Token序列从数百激增至数千，引发二次方注意力计算成本与KV缓存内存瓶颈。为降低开销，视觉Token剪枝成为主流优化手段，其核心在于从冗余Token中筛选出对任务关键的信息子集。然而，剪枝决策依赖于重要性评估信号，若信号仅捕捉语义相关性而忽略空间结构，将导致模型在需要绝对位置感知的任务中失效。

视觉Token剪枝领域已形成Pre-LLM与Intra-LLM两大路线，前者在编码器侧压缩以尽早降低负载，后者在LLM内部利用注意力信号进行动态筛选。FastV等Intra-LLM方法确立了基于浅层注意力分数的剪枝范式，但注意力分数受位置偏差影响，且无法区分“视觉显著”与“空间坐标”两类不同功能的信息。现有方法在通用理解任务上表现良好，但在RefCOCO等视觉定位基准上出现显著性能衰减，暴露出纯语义导向剪枝在空间推理任务上的结构性缺陷。本文切入点在于揭示LVLMs空间推理的底层机制：RoPE不仅编码相对位置，其数学结构还隐含了绝对空间坐标参考系，剪除这些参考Token即破坏了空间推理的基础。

## 核心方法

### 方法参照系

本文问题属于Intra-LLM剪枝范畴，标准流程为：在LLM指定层计算Token重要性分数，保留Top-K Token并剪除其余。本文与通用流程的关键差异在于重要性信号来源：通用方法依赖注意力分数或语义相似度，本文引入基于RoPE数学性质的空间坐标信号，并采用Value向量相似度替代注意力分数以消除位置偏差。

### 隐含视觉坐标识别

传统剪枝方法将Token视为同质信息单元，忽略了RoPE旋转矩阵中特定位置对绝对位置信息的隔离作用。当Key Token的RoPE旋转矩阵近似单位矩阵或90度旋转矩阵时，自注意力机制能提取Query Token的绝对位置分量。本文定义实轴分数 $V(m) = \sum_{k=0}^{d/2-1} \cos(m\theta_k)$ 与虚轴分数 $U(m) = \sum_{k=0}^{d/2-1} \sin(m\theta_k)$，分别对应单位矩阵与90度旋转的逼近程度。保留 $V(m)$ 与 $U(m)$ 的Top-$k_c$ Token构成IVC集合，这些Token作为空间参考锚点，使模型在剪枝后仍能感知物体在图像中的绝对位置，解决了纯语义剪枝导致定位性能崩溃的问题。

### 语义前景两阶段筛选

IVC Token提供空间框架，但不足以覆盖任务相关的语义内容。注意力分数因位置偏差导致文本Token倾向于关注空间邻近而非语义相关的视觉Token，本文改用Value向量相似度计算语义相关性。第一阶段计算文本Value向量与视觉Value向量的归一化点积，取Top-1%作为语义种子；第二阶段将文本与种子Token的Value向量拼接为查询集，重新计算所有视觉Token的相似度分数，取Top-$k_f$ 作为前景Token。该两阶段设计通过种子扩展捕捉大型或复杂对象的完整语义区域，避免了单一相似度度量在局部细节上的遗漏，确保保留Token既具备空间参考性又具备任务语义完整性。

## 实验评估

实验在Qwen2.5-VL、InternVL-2.5、DeepSeek-VL2与LLaVA-v1.5四个架构上，覆盖RefCOCO、MMBench、POPE、TextVQA等20个基准。基线包括FastV、PDrop、VScan等Intra-LLM方法，但未对比VisionZip等Pre-LLM代表性方法，限制了跨路线的性能比较。

| 模型 | 方法 | 平均Token保留率 | RefCOCO testA | RefCOCO+ testA | Rel. Avg. |
|---|---|---|---|---|---|
| Qwen2.5-VL 7B | Vanilla | 100% | 92.2 | 88.0 | 100% |
| Qwen2.5-VL 7B | FastV | 54% | 74.4 | 68.9 | 84.7% |
| Qwen2.5-VL 7B | IVC-Prune | 50% | 92.0 | 87.4 | 99.6% |
| InternVL 2.5 8B | Vanilla | 100% | 94.7 | 91.5 | 100% |
| InternVL 2.5 8B | FastV | 53% | 87.0 | 82.6 | 90.1% |
| InternVL 2.5 8B | IVC-Prune | 50% | 94.2 | 91.1 | 99.5% |

在Qwen2.5-VL上，IVC-Prune在RefCOCO testA上达到92.0%，仅比Vanilla低0.2%，而FastV下降至74.4%；在InternVL 2.5上，IVC-Prune保持94.2%，FastV降至87.0%。通用任务上，IVC-Prune在MMBench、POPE等基准上相对准确率均超过99%，部分任务甚至超过Vanilla，表明空间坐标保留未损害通用理解能力。

消融实验显示，移除IVC Token后，Qwen2.5-VL在RefCOCO testA上从92.0%降至76.0%，降幅达16%，证实IVC对空间推理的关键作用。将IVC Token加入FastV后，其RefCOCO testA性能从74.4%提升至82.1%，表明IVC机制可与其他剪枝方法正交组合。前景筛选阶段中，仅使用第一阶段语义种子时，InternVL-2.5在RefCOCO testA上为93.9%，加入第二阶段上下文细化后提升至94.2%，边际收益较小但确保了复杂对象的完整覆盖。

评估协议基于VLMEvalKit框架，使用8×A100 40GB GPU，代码已开源。局限在于：未报告置信区间，数值比较需谨慎；未对比Pre-LLM方法，无法评估Intra-LLM与Pre-LLM在空间任务上的帕累托前沿；IVC选择依赖RoPE频率配置，在ALiBi等非RoPE架构中的适用性未验证。

## 关联研究分析

从信号来源看，本文与FastV、SparseVLM等注意力导向方法存在根本分歧。FastV依赖LLM浅层注意力分数，假设注意力权重反映Token重要性，但注意力分数受相对位置影响，文本Token倾向于关注空间邻近的视觉Token而非语义相关Token。本文改用Value向量相似度，因Value向量不受位置编码影响，能更纯粹地捕捉语义相关性。这一差异源于任务特性：视觉定位需要绝对位置信息，而注意力分数仅编码相对位置，导致FastV在定位任务上失效。本文的IVC机制补充了绝对位置信息，但Value相似度是否在所有架构下均优于注意力分数，论文未给出跨架构的系统对比。

从剪枝位置看，本文采用Intra-LLM中间层单次剪枝，与VisionZip等Pre-LLM方法形成路线竞争。Pre-LLM方法在编码器侧压缩，能更早降低LLM输入长度，最大化计算节省，但缺乏文本查询引导，难以区分任务相关与无关Token。本文在中间层剪枝，利用该层注意力对语义最敏感的特性，实现Prompt-aware剪枝，但计算节省不如Pre-LLM显著。本文未对比VisionZip，无法评估两条路线在空间任务上的性能-延迟权衡。此外，本文固定50% Token保留率，未采用自适应预算，在图像复杂度差异大的场景下，固定比率可能导致简单图像过度保留或复杂图像保留不足。

## 总结

本文要解决的核心矛盾是视觉Token剪枝中空间信息丢失导致的定位性能崩溃。现有方法依赖语义相关性或注意力分数，忽略了RoPE中隐含的绝对空间坐标功能，本文通过理论分析揭示特定位置Token充当空间参考系，据此提出保留IVC Token与语义前景Token的免训练剪枝策略。实验证明，在50% Token保留率下，IVC-Prune在RefCOCO testA上保持92.0%（Qwen2.5-VL）与94.2%（InternVL-2.5），相对准确率均超过99%。本文的边界在于：IVC选择依赖RoPE频率配置，未验证ALiBi等非RoPE架构的适用性；固定50%保留率未考虑图像复杂度差异；未对比Pre-LLM方法，无法评估跨路线的性能-延迟权衡。当输入图像分辨率从1024×1024变化到4096×4096时，IVC Token的最优保留比例是否随分辨率线性变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03060)