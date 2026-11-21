# ACL2026最新论文 ｜DocLens : A Tool-Augmented Multi-Agent Framework for Long Visual Document Understanding ｜长视觉文档理解中的双层级证据定位

研究机构：北京大学

作者：Dawei Zhu、Rui Meng、Jiefeng Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.11552)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11552)

> 长视觉文档理解的核心瓶颈在于证据定位的双重失效：模型既难以从数百页中召回相关页面，也无法在全页视图中捕捉图表等视觉元素的细粒度细节。现有方法多依赖向量检索或全量上下文输入，前者召回率低，后者计算不可行且细节丢失。DocLens通过工具增强的多智能体框架，将证据定位拆解为页面导航与元素裁剪两个阶段，并引入采样-裁决机制抑制幻觉。该框架在MMLongBench-Doc上超越人类专家，但其对OCR文本的强依赖是否削弱了纯视觉布局的鲁棒性，仍存疑。

## 研究背景

当VLM处理平均49.4页的长文档时，其有限的上下文窗口无法容纳全量高分辨率图像，导致跨页证据丢失。这一约束迫使研究从静态全量输入转向动态选择性聚合，即检索增强生成（Retrieval-Augmented Generation, RAG）。然而，RAG的检索阶段通常基于向量相似度，无法感知推理需求，导致检索到无关页面。更深层的问题在于，即使检索到正确页面，全页视图下图表、表格等视觉元素的关键细节仍被稀释，模型往往在无法回答时产生幻觉而非承认不确定性。

长文档理解的主流路线分为两类：一是扩展上下文窗口，二是智能体导航。前者在短文档或局部一致性任务上有效，但在长程跨页推理中计算成本激增且性能下降；后者如DocAgent通过结构感知导航解决证据稀疏问题，但多数方法仅停留在页面级检索，忽略了元素级细节。DocLens的切入点在于指出“双层级证据定位失败”是幻觉的直接诱因：页面级召回率低（Gemini-2.5-Pro仅68%）与元素级细节丢失共同导致模型在MMLongBench-Doc上对超过半数的不可回答查询编造答案。

## 核心方法

### 方法参照系

长文档QA的标准流程是将文档与问题映射至答案，即 $A = f(D, Q)$。然而，直接映射在长文档中因信息量过大而失效。通用做法是分解为提取与生成两阶段，但现有提取模块多依赖向量检索，缺乏对视觉元素细粒度的处理能力。DocLens的关键差异在于将提取过程工具化，引入OCR与布局检测作为外部工具，而非仅依赖VLM内部表征。

### 双层级证据提取

页面级检索通常采用向量相似度匹配，但实验显示ColPali的Recall@10仅55.3%。DocLens的Page Navigator通过OCR文本增强VLM的检索能力，利用文本域的高召回率弥补视觉域的不足。其核心公式为预测页面集合 $E_{pred} = \bigcup_{j=1}^{T_e} E^{(j)}$，其中 $E^{(j)}$ 是第 $j$ 次采样（温度 $\tau > 0$）生成的候选页面集。这一设计动机在于解决单一向量检索在长文档中召回率低的失效，通过多次采样并集扩大覆盖范围。随后，Element Localizer对 $E_{pred}$ 中的每页执行布局检测，裁剪出视觉元素 $V_k = \{crop(P_k, bbox)\}$，形成包含页面截图、OCR文本与裁剪元素的证据集 $S$。该步骤解决了全页视图中视觉细节被稀释的问题，使模型能聚焦于图表等关键区域。

### 采样-裁决推理

现有智能体框架通常单次生成答案，易受推理路径偏差影响。DocLens的Reasoning Module引入Answer Sampler与Adjudicator，通过多路径生成与交叉验证提升可靠性。Answer Sampler执行 $T_a$ 次推理，生成候选答案集 $\{R_i, A_i\}_{i=1}^{T_a}$，其中 $R_i$ 为思维链，$A_i$ 为答案。Adjudicator则分析各候选的推理路径，交叉验证一致性，输出最终答案 $A_{final}$。这一机制的设计动机在于抑制幻觉：通过多路径探索，若某答案在多条推理路径中均出现，则其可靠性更高。该过程将答案生成从单次前向推理转变为序贯决策，显著提升了不可回答查询的识别能力。

## 实验评估

实验在MMLongBench-Doc（平均49.4页）与FinRAGBench-V（密集报纸布局）上进行，基线覆盖Vanilla VLM、OCR增强VLM及现有智能体框架（MACT, M3DocRAG, SimpleDoc）。DocLens在MMLongBench-Doc上取得67.6%的ALL分数（Gemini-2.5-Pro），超越人类专家65.8%，但低于最新SOTA DocMemo的70.5%。在FinRAGBench-V上，DocLens取得70.4%的ALL分数，显著优于基线。

| 方法 | MMLongBench-Doc ALL | FinRAGBench-V ALL |
| :--- | :--- | :--- |
| Gemini-2.5-Pro (Vanilla) | 52.1 | 58.3 |
| Gemini-2.5-Pro (OCR) | 63.3 | 64.9 |
| SimpleDoc (Gemini-2.5-Pro) | 63.6 | 67.5 |
| DocLens (Gemini-2.5-Pro) | 67.6 | 70.4 |

消融实验显示，移除Lens Module导致MMLongBench-Doc性能下降4.1%，移除Reasoning Module导致不可回答查询性能下降。Page Navigator的OCR增强在FinRAGBench-V上将召回率从53.8%提升至94.3%，表明VLM在文本域检索优于视觉域。Element Localizer在视觉证据任务上提升显著，但在纯文本任务上增益可忽略，证实其对视觉细节的针对性作用。

评估边界方面，论文未报告置信区间，且基线中缺少纯向量检索（如ColPali单独测试）的公平对比。代码已开源，但超参数（如 $T_e, T_a$）的敏感性分析未在正文中详细展开，可复现性依赖于附录中的伪代码。

## 关联研究分析

从问题动机看，DocLens与SimpleDoc均针对长文档证据稀疏问题，但SimpleDoc依赖ColQwen2.5向量检索加LLM筛选，而DocLens采用OCR增强的LLM导航。差异根源在于任务特性：FinRAGBench-V的密集报纸布局导致视觉相似度检索失效，OCR文本提供了更稳定的检索锚点。然而，OCR辅助是否导致对纯视觉布局能力的依赖降低，论文未给出回答。

从方法设计看，DocLens与DocAgent同属智能体框架，但DocAgent侧重结构感知导航，DocLens引入工具调用（OCR、布局检测）与采样-裁决机制。DocLens的采样-裁决机制在不可回答查询上表现突出，而DocAgent未专门优化此方面。这一差异暗示，多路径生成与交叉验证可能是抑制幻觉的有效手段，但其计算成本是否随文档长度线性增长，论文未提供效率分析。

## 总结

DocLens要解决的核心矛盾是长文档中页面级与元素级证据定位的双重失效。其切入点在于指出向量检索召回率低与全页视图细节丢失是幻觉的直接诱因，并通过工具增强的多智能体框架实现双层级定位。方法上，Page Navigator利用OCR文本提升页面召回率至97.3%，Element Localizer裁剪视觉元素以捕捉细节，Reasoning Module通过采样-裁决抑制幻觉。实验证明，DocLens在MMLongBench-Doc上超越人类专家65.8%，达到67.6%。其边界在于对OCR文本的强依赖，以及在纯视觉布局任务上的增益有限。当文档缺乏高质量OCR文本时，Page Navigator的召回率是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11552)