# ACL2026最新论文 ｜Sign-Language Datasets at Scale: A Comprehensive Survey on Resources, Benchmarks, and Annotation Standards ｜手语数据集规模化审计与标准化框架

研究机构：美国华盛顿大学

作者：Yiming Ni、Zhi-Qi Cheng、Jiayu Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_16cecb6495d4)

> 手语处理领域长期受困于数据碎片化与标注不一致，导致模型泛化能力受限且跨研究对比困难。现有综述多聚焦单一任务或算法演进，缺乏对数据资源本身的结构化审计。本文切入点在于将120个数据集视为研究对象，通过24字段Datasheet框架统一元数据描述，并整合基准测试结果以揭示数据属性对模型性能的影响。其价值在于提供了领域内首个跨语言、跨任务的数据资源全景图，但基准表中缺失2025-2026年最新LLM基线，限制了其对当前SOTA算法有效性的直接评估。

## 研究背景

手语作为视觉-手势语言，其语义承载于手部动作（Manual）与非手动线索（Non-manual Markers, NMM）两个异步通道。由于缺乏标准化正字法，数据集通常依赖Gloss（近似口语词的中间标注）或音韵编码作为代理表示。Gloss标注虽降低了翻译任务的复杂度，但存在高昂的人工成本与跨语言不一致性；而无Gloss（Gloss-free）范式虽提升了可扩展性，却面临视觉特征与线性文本间巨大语义鸿沟的挑战。数据模态（RGB、姿态、深度）的缺失或不均衡，进一步加剧了模型在开放域场景下的鲁棒性问题。

当前手语研究的主流路线已从基于Gloss的两阶段流水线转向端到端的Gloss-free映射，并逐步引入大语言模型（LLM）以增强语义推理。然而，算法进步严重受制于数据瓶颈：现有研究高度依赖PHOENIX-2014T、CSL-Daily等少数基准，而大量已发布的数据集因访问限制、标注粒度差异或长期可访问性缺失（如Link rot）而被忽视。这种数据资源的碎片化导致模型设计往往受限于特定数据集的属性，而非任务本身的通用需求。本文旨在通过系统化的数据审计，揭示数据覆盖、标注一致性与模态平衡对下游任务性能的根本制约，为构建鲁棒且可泛化的手语AI提供数据层面的基础设施。

## 核心方法

### 方法参照系

本文不属于算法模型类研究，而是数据资源审计与标准化框架设计。其参照系为传统的领域综述（Survey），但关键差异在于：传统综述以算法演进为主线，本文以数据集属性（模态、人口统计、标注结构）为核心变量，将120个数据集作为分析单元，旨在建立数据质量与模型性能之间的因果联系。

### 24字段Sign-Language Datasheet框架

针对现有数据集元数据描述不统一、关键属性（如签名者多样性、标注一致性）缺失的问题，本文提出24字段Datasheet框架。该框架将数据集描述从简单的“规模-语言”二元组扩展为多维结构化记录。其核心逻辑可形式化为对数据集 $D$ 的属性向量 $\mathbf{a}(D)$ 的完备映射：

$$
\mathbf{a}(D) = \{ \text{Modality}, \text{Annotation\_Granularity}, \text{Signer\_Demographics}, \text{Access\_Status}, \dots \}
$$

其中 $\text{Annotation\_Granularity}$ 涵盖Gloss、音韵编码及时间对齐精度，$\text{Signer\_Demographics}$ 记录签名者数量与多样性。设计动机在于解决现有文献中因元数据缺失导致的“不可比性”问题：例如，CSL-Daily的签名者独立划分与PHOENIX-2014T的封闭域特性，若缺乏统一字段描述，其性能差异常被误归因于算法而非数据分布。该框架通过强制记录访问状态（如NDA限制、Link rot）与模态完整性，使数据资源的“可用性”与“质量”可被量化评估，从而为后续模型选择提供数据层面的决策依据。

### 基准整合与数据-性能关联分析

在Datasheet基础上，本文整合PHOENIX-2014T、CSL-Daily、How2Sign等五大基准的SLR/SLT/SLP任务结果，构建数据属性与模型性能的关联图谱。其核心分析逻辑可表示为性能函数 $P$ 对数据属性 $\mathbf{a}$ 的依赖：

$$
P_{\text{task}} = f(\mathbf{a}(D), \text{Model}_{\text{arch}})
$$

本文通过对比Gloss-based与Gloss-free方法在不同数据属性下的表现，揭示数据约束对算法上限的影响。例如，PHOENIX-2014T因天气域狭窄与Gloss对齐良好，Gloss-based方法（如TextCTC-SLT）可达28.42% BLEU；而How2Sign因缺乏Gloss层与词汇量大，Gloss-free方法（如SSVP-SLT）仅达15.5% BLEU。设计动机在于打破“算法决定性能”的单一视角，证明数据模态（如RGB vs. Pose）与标注结构（Gloss vs. 无Gloss）是性能差异的独立变量。该分析通过UMAP投影展示不同数据集在嵌入空间中的语义域重叠，直观呈现了数据分布的异质性，为跨数据集泛化研究提供了数据层面的实证基础。

## 实验评估

本文作为综述，其“实验”体现为对120个数据集的元数据审计与基准结果整合。基准覆盖PHOENIX-2014T、CSL-Daily、How2Sign、YouTube-ASL与OpenASL，任务涵盖SLR、SLT、SLP。基线审计显示，本文整合了Gloss-based（如TextCTC-SLT、TwoStream-SLT）与Gloss-free（如CV-SLT、MSKA-SLT）经典方法，但缺失2025-2026年基于LLM的最新SOTA（如SignLlama、ViPo-MLLM），导致其基准表无法反映当前算法前沿。

| 数据集 | 任务 | 代表模型 | 指标 | 数值 |
|---|---|---|---|---|
| PHOENIX14T | SLT (Gloss-based) | TextCTC-SLT | BLEU | 28.42% |
| PHOENIX14T | SLT (Gloss-free) | CV-SLT | BLEU | 29.27% |
| CSL-Daily | SLT (Gloss-free) | Uni-Sign | BLEU | 26.36% |
| How2Sign | SLT (Gloss-free) | SSVP-SLT | BLEU | 15.5% |
| PHOENIX14T | SLR | SignVTCL | WER | 17.9% |
| CSL-Daily | SLR | SignVTCL | WER | 24.1% |

数据表明，Gloss-free方法在PHOENIX14T上已超越Gloss-based方法（29.27% vs. 28.42%），但在How2Sign上性能显著下降（15.5%），验证了数据规模与标注缺失对Gloss-free范式的制约。SLR任务中，CSL-Daily的WER（24.1%）高于PHOENIX14T（17.9%），反映了开放域场景下签名者多样性与协同发音带来的建模难度。

本文未提供消融实验，其核心贡献在于数据审计而非算法验证。设计决策上，本文选择以BLEU/WER为统一指标，但指出BLEU在SLP任务中受反向翻译模型限制，仅具相对意义。评估边界方面，本文承认IAA（标注者间一致性）与生态效度等关键属性在现有数据集中极少报告，将其视为文档缺口而非直接推断。可复现性上，本文提供GitHub仓库，但部分数据集（如CSL-Daily）因NDA限制无法公开访问，限制了完全复现。

## 关联研究分析

从问题动机看，本文与SignAgent（Cory et al., 2026）均关注数据标注成本，但路线截然不同。SignAgent利用LLM代理自动化标注，旨在解决“标注效率”问题；本文则通过Datasheet框架解决“标注一致性”与“元数据缺失”问题。差异根源在于任务特性：SignAgent假设LLM具备语言学推理能力，可替代专家标注；本文则指出即使标注完成，若缺乏统一元数据描述，数据仍不可比。SignAgent未讨论标注后的数据标准化问题，而本文未探索自动化标注的具体实现，两者互补但各自存在盲区。

从方法设计看，本文与SignVerse-2M（Fang et al., 2026）在数据表示上存在潜在冲突。SignVerse-2M主张姿态（Pose）原生表示优于RGB，以提升鲁棒性与隐私保护；本文审计发现，多数现有数据集仅含RGB，Pose数据稀缺，暗示Pose路线受数据资源限制。这一冲突揭示了算法偏好与数据现实之间的张力：SignVerse-2M的SOTA表现可能部分得益于其自建的姿态数据集，而非姿态表示本身的普适优势。本文未直接验证Pose vs. RGB的性能差异，而是通过数据覆盖分析指出，当前算法研究可能受限于数据模态的可用性，而非模态本身的优劣。

## 总结

本文要解决的核心矛盾是手语数据资源的碎片化与模型泛化需求之间的冲突。现有方法受限于单一数据集属性，而本文通过24字段Datasheet框架与120个数据集的系统审计，提供了数据层面的统一视角。其核心贡献在于揭示了数据模态、标注结构与访问状态对模型性能的独立影响，例如PHOENIX14T上Gloss-free方法超越Gloss-based（29.27% vs. 28.42%），而How2Sign上性能显著下降（15.5%）。本文的边界在于基准表缺失2025-2026年LLM基线，且未量化IAA等关键质量属性。当数据资源覆盖扩展至更多低资源手语时，Datasheet框架能否有效捕捉跨语言标注粒度差异，从而支持真正的跨语言泛化研究，仍是待验证的问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_16cecb6495d4)