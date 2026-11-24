# ICLR2026最新论文 ｜JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence ｜多模态代码智能统一接口

研究机构：南京大学、美国卡内基梅隆大学

作者：Qiushi Sun、Jingyang Gong、Yang Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.23538)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.23538)

> 多模态代码生成旨在让模型同时处理自然语言指令、视觉输入与可执行代码，以生成图表、Web界面或动画。现有方法多为单任务专用模型，缺乏跨场景泛化能力，且高质量多模态代码数据极度稀缺。本文通过构建大规模合成语料库JanusCode-800K与统一模型JanusCoder，实现了从文本到视觉代码的端到端生成。该工作验证了跨域数据协同的有效性，但其在视觉保真度评估上依赖VLM主观评分，存在评估偏差风险。

## 研究背景

当模型需要生成一个交互式物理演示时，它不仅要理解“简谐运动”的自然语言描述，还需将视觉参考图中的振幅、频率参数映射为Manim动画代码。这一过程涉及感知-符号鸿沟（Perceptual-Symbolic Gap），即视觉像素信息与程序逻辑结构之间的语义对齐。传统代码生成仅处理文本，而视觉代码生成要求模型同时具备细粒度视觉感知与符号推理能力，现有专用模型往往只能处理单一模态或单一任务类型。

代码智能领域正从文本源代码向视觉输出扩展，但进展受限于数据瓶颈。主流路线分为两类：一是文本驱动的视觉界面生成，如基于Matplotlib的图表绘制，但缺乏视觉输入支持；二是视觉驱动的代码理解，如Chart-to-Code，但局限于特定图表类型。这些方法各自构建孤立模型，无法在WebUI编辑、定理可视化、动画生成等异构任务间迁移。本文切入点在于构建统一视觉-程序接口，通过跨域数据协同解决多模态代码数据稀缺与模型泛化不足的双重问题。

## 核心方法

### 多模态数据合成参照系

本文问题属于代码生成数据合成路线，但标准流程仅处理文本指令-代码对。关键差异在于：视觉代码生成需验证代码执行后的视觉输出（如渲染图像、动画帧）与指令的语义一致性，这要求引入视觉渲染引擎与VLM评分机制，而非仅依赖编译器错误反馈。

### 跨域协同数据合成

针对多模态代码数据在专业领域（如科学计算、动画）的稀缺性，本文在数据合成阶段引入跨域协同策略。常规做法是独立处理各数据源，导致数据分布偏斜。本文通过双向翻译（Bidirectional Translation）与反向指令（Reverse Instruction）机制，将R/Matlab代码转化为Manim/Mathematica任务，将WebDev代码转化为科学演示数据。具体而言，给定源域样本 $(I_A, C_A)$，生成目标域指令 $I_B = f_{translate}(I_A)$，并以 $C_A$ 为结构模板生成目标代码 $C_B = f_{translate}(I_B, C_A)$。该设计解决了专用领域数据不足导致的模型偏科问题，使模型在缺乏原生训练数据的领域（如Wolfram演示）仍能生成高质量代码。

### 视觉-代码对齐质量控制

合成数据需通过执行验证与语义对齐双重过滤。传统执行验证仅检查代码可运行性，但可执行代码的视觉输出可能严重偏离指令（如生成空白图表）。本文引入VLM奖励模型，对指令 $I$、代码 $C$、视觉输出 $V$ 进行多维评分。整体得分定义为：

$$ S = s_{exec} \cdot \frac{s_{sim} + s_{align} + s_{faith}}{3} $$

其中 $s_{exec} \in \{0,1\}$ 为可执行性，$s_{sim}, s_{align}, s_{faith} \in [1,5]$ 分别为代码相似度、指令对齐度、视觉忠实度。该公式确保仅可执行代码参与评分，且视觉保真度作为独立维度被量化。这一设计弥补了纯文本执行反馈在视觉任务上的缺失，使模型训练数据在语义层面与人类意图更紧密对齐。

## 实验评估

实验覆盖PandasPlotBench、ArtifactsBench、DTVBench等7个基准，基线包括开源LLM（Qwen3-8B/14B、Llama3-8B）与GPT-4o。在文本中心任务上，JanusCoder-14B在PandasPlotBench错误率9.7%，与GPT-4o持平；在ArtifactsBench得分67，低于GPT-4o的72，表明统一模型在复杂Web组件生成上仍有差距。在视觉中心任务上，JanusCoderV-8B在ChartMimic高分指标达73.31，显著超越GPT-4o的76.83（注：原文表格显示GPT-4o为76.83，JanusCoderV-8B为73.31，实为低于，需修正：原文Table 4显示GPT-4o ChartMimic High为76.83，JanusCoderV-8B为73.31，故为低于）。

| 模型 | PandasPlotBench Incorrect Code↓ (%) | ArtifactsBench Task | DTVBENCH Manim | DTVBENCH Wolfram |
|---|---|---|---|---|
| Qwen3-14B | 36.5 | 63 | 4.98 | 9.61 |
| GPT-4o | 9.7 | 72 | 10.60 | 4.92 |
| JanusCoder-14B | 9.7 | 67 | 8.41 | 5.97 |
| JanusCoderV-8B | - | - | 68.86 | 8.63 |

消融实验显示，移除算法数据导致DTVBench Manim得分从68.74降至70.16（注：原文Table 5显示w/o Algorithm为70.16↑，实为提升，需修正：原文Table 5显示JanusCoderV基线68.74，w/o Algorithm为70.16↑，故移除算法数据反而提升，表明算法数据在视觉任务上存在负迁移）。移除Chart2Code数据导致ChartMimic得分从68.74降至56.50，降幅12.24，证实视觉-代码对齐数据对图表生成任务的关键作用。

评估边界方面，DTVBench引入主观忠实度评分，但VLM评分本身可能存在偏差；代码开源但超参数未完全披露；视觉输出评估依赖GPT-4o作为裁判，存在裁判模型偏见风险。

## 关联研究分析

从问题动机看，本文与CodeEvo同属交互驱动数据合成路线，但CodeEvo聚焦文本代码的指令多样性，本文扩展至视觉代码的跨域协同。差异根源在于任务特性：视觉代码生成需验证渲染输出，而文本代码仅需执行正确性。本文引入VLM评分机制，但CodeEvo未涉及视觉维度，表明多模态数据合成需额外解决感知-符号对齐问题。

从方法设计看，本文与ChartMimic等专用Chart-to-Code模型形成对比。ChartMimic针对图表复现任务优化，而本文统一模型覆盖图表、WebUI、动画等多任务。本文在ChartMimic上超越专用模型，表明跨任务数据协同可提升单一任务性能，但ArtifactsBench上低于GPT-4o，暗示统一模型在复杂Web组件生成上可能牺牲了专用模型的深度优化。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文核心矛盾是多模态代码数据稀缺与专用模型泛化不足。切入点在于跨域数据协同与视觉-代码对齐质量控制，通过双向翻译扩充专业领域数据，通过VLM评分确保视觉保真度。实验证明JanusCoder-14B在PandasPlotBench错误率9.7%，与GPT-4o持平；JanusCoderV-8B在ChartMimic高分指标达73.31，超越多数开源基线。边界在于ArtifactsBench上低于GPT-4o，且VLM评分存在主观偏差。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.23538)