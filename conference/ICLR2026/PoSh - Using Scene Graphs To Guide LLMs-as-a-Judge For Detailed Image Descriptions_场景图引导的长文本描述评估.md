# ICLR2026最新论文 ｜PoSh: Using Scene Graphs To Guide LLMs-as-a-Judge For Detailed Image Descriptions ｜场景图引导的长文本描述评估

研究机构：美国哥伦比亚大学、美国德克萨斯大学奥斯汀分校

作者：Amith Ananthram、Elias Stengel-Eskin、Lorena A. Bradford 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.19060)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.19060)

> 详细图像描述评估面临的核心矛盾是：传统短文本指标无法捕捉长文本中属性与关系的附着错误，而直接调用大语言模型（LLM）评分虽灵活但缺乏可复现性与细粒度解释。现有方案要么忽略对象附着结构（如SPICE），要么依赖闭源API导致结果不可复现。本文切入点在于将场景图作为结构化评分标准（structured rubrics），引导开源LLM进行问答式验证，从而在保持可复现性的同时实现文本跨度级的错误定位。POSH在DOCENT基准上以+0.05 Spearman ρ的优势超越GPT4o-as-a-Judge，但其结论局限于艺术画作领域，向自然场景推广的有效性尚待验证。

## 研究背景

当VLM生成包含多个人物、复杂姿态和细微属性的长描述时，评估器必须区分“对象存在但属性错误”与“对象完全缺失”。这一需求催生了细粒度理解（Fine-grained Understanding）评估，其核心在于将描述解构为对象、属性与关系的三元组，并验证其在参考文本中的存在性。然而，传统基于编辑距离或N-gram重叠的指标（如CIDEr、SPICE）在处理长文本时，往往因忽略对象附着关系（object attachment）而误判，例如将“穿红衣服的男人”错误匹配为“穿蓝衣服的男人”仍视为部分正确。

VLM评估领域正从静态基准的分数竞争转向对失败根源的诊断。主流路线中，基于嵌入相似度的方法（如CLIPScore）受限于上下文长度，无法处理长描述；直接利用LLM-as-a-Judge的方法虽能处理长文本，但闭源模型（如GPT4o）的API调用成本高昂且结果不可复现，开源模型（如LLaVa-Critic）则缺乏对细粒度错误的定位能力。POSH的切入点在于结合结构化解析与LLM验证：通过依存句法分析保留对象附着关系的场景图，作为引导开源LLM进行问答的“评分标准”，从而在可复现性、解释性与细粒度定位之间取得平衡。

## 核心方法

### 方法参照系

POSH属于参考基准（reference-based）评估范式，其通用流程为：提取生成文本与参考文本的结构化表示，计算两者间的差异，并聚合为分数。与SPICE等基于编辑距离的场景图匹配方法不同，POSH的关键差异在于不强制对齐两个场景图的组件，而是将场景图作为查询模板，通过LLM问答验证组件在另一文本中的存在性，从而避免表面形式差异导致的误判。

### 场景图提取与结构化评分标准

POSH首先使用`spacy`的依存句法分析器提取句子级场景图，再通过`maverick-mes-ontonotes`进行共指消解，合并跨句的对象并保留属性与关系附着。场景图定义为 $G(d) = \langle O(d), E(d), K(d) \rangle$，其中 $O(d)$ 为对象集合，$E(d) \subseteq O(d) \times A$ 为属性集合，$K(d) \subseteq O(d) \times R \times O(d)$ 为关系边集合。这一设计解决了SPICE忽略对象附着的问题：通过共指消解，POSH确保“man”与“face of the man”被正确关联，使得后续评分能区分“对象存在但属性错误”与“对象缺失”。

### 基于问答的细粒度验证与聚合

对于场景图 $G(d)$ 中的每个组件 $c$，POSH生成模板化问题，引导开源LLM（Qwen3-14B）预测 $c$ 在另一文本 $d'$ 中的存在程度（1-5分）。细粒度错误分数 $\pi$（mistakes）与遗漏分数 $\rho$（omissions）定义为：

$$ \pi(c) = \Psi(c, d_{ref}), \quad \rho(c) = \Psi(c, d_{gen}) $$

其中 $\Psi$ 为LLM问答函数。粗粒度分数通过细粒度分数的均值聚合：

$$ \text{Mistakes} = \frac{1}{|O(d_{gen})|} \sum_{c \in O(d_{gen})} \pi(c), \quad \text{Omissions} = \frac{1}{|O(d_{ref})|} \sum_{c \in O(d_{ref})} \rho(c) $$

这一设计解决了LLM-as-a-Judge缺乏细粒度解释的问题：粗粒度分数直接源于细粒度错误定位，使得模型迭代时能明确知道是“属性附着错误”还是“细节遗漏”驱动了性能差异。

## 实验评估

POSH在DOCENT（艺术画作）与CapArena（网络图像）上评估，基线覆盖SPICE、CAPTURE、LLaVa-Critic、GPT4o/5及DCScore。POSH在DOCENT上以0.519的Spearman ρ领先所有可复现指标，较次优的LLaVa-Critic（0.412）提升0.107；在CapArena上，POSH模型排名ρ=0.931，优于GPT4o（0.890）与LLaVa-Critic（0.899）。

| 指标 | DOCENT Mistakes ρ | DOCENT Omissions ρ | CapArena Model Ranking ρ |
| :--- | :--- | :--- | :--- |
| POSH | 0.519 | 0.581 | 0.931 |
| LLaVa-Critic | 0.412 | 0.509 | 0.899 |
| GPT4o | 0.484 | 0.380 | 0.890 |
| SPICE | 0.308 | 0.464 | 0.275 |

POSH作为奖励函数时，DAPO训练生成的描述在遗漏分数上较SFT提升0.432，但错误分数下降0.243，表明POSH优化倾向于增加细节覆盖而非减少错误。这一权衡揭示了POSH在训练闭环中的行为特性：其细粒度遗漏定位能力被强化，但错误抑制能力相对较弱。

POSH在DOCENT上评分400个样本耗时15分钟（单H100 GPU），较DCScore（2小时）效率提升8倍，但较人工评估（18分钟/样本）仍慢。评估协议局限在于DOCENT仅含艺术画作，其视觉复杂度（平均161个实体）高于自然场景，POSH在低复杂度图像上的表现未验证。代码与超参数已开源，但场景图提取的共指消解误差在复杂场景中的传播效应未量化。

## 关联研究分析

从方法设计看，POSH与SPICE共享场景图基础，但POSH摒弃了基于编辑距离的组件匹配，转而采用LLM问答验证。这一差异源于任务特性：长描述中对象附着关系复杂，编辑距离无法区分“属性错误”与“对象缺失”，而LLM问答能灵活处理表面形式差异（如“trio”与“three men”）。然而，POSH依赖共指消解的准确性，若共指错误导致对象合并，场景图结构将被破坏，进而影响LLM问答的准确性。这一风险在艺术画作中因人物姿态清晰而较低，但在自然场景中可能放大。

从问题动机看，POSH与LLaVa-Critic同属LLM-as-a-Judge范式，但POSH通过结构化场景图约束LLM的评分空间，而LLaVa-Critic直接提示LLM评分。POSH在CapArena上以ρ=0.931超越LLaVa-Critic（0.899），表明结构化引导提升了评分的稳定性。然而，POSH的细粒度定位能力依赖场景图提取的准确性，而LLaVa-Critic作为VLM能直接感知图像内容，POSH仅基于文本评分，无法捕捉图像与文本的不一致。这一局限在艺术画作中因参考文本详尽而缓解，但在开放场景中可能成为瓶颈。

## 总结

POSH解决的核心矛盾是长文本描述评估中细粒度错误定位与可复现性的冲突。其切入点在于将场景图作为结构化评分标准，引导开源LLM进行问答验证，从而在保持可复现性的同时实现文本跨度级的错误定位。POSH在DOCENT上以+0.05 Spearman ρ超越GPT4o-as-a-Judge，并作为奖励函数优于SFT。其边界在于DOCENT仅含艺术画作，POSH在自然场景中的表现未验证；共指消解误差在复杂场景中的传播效应未量化。当场景图提取的共指错误率超过10%时，POSH的细粒度定位能力是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.19060)