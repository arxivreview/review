# HuggingFace最新推荐论文 ｜FireRed-OCR Technical Report ｜结构幻觉抑制下的文档解析框架

作者：Hao Wu、Haoran Lou、Xinyue Li 等 22 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01840)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01840)

> 文档信息抽取（DIE）旨在从非结构化文档中自动提取结构化数据，其核心价值在于连接数字文档与机器智能。通用视觉语言模型（VLM）在解析复杂文档时，常因缺乏对严格语法约束的内在理解而产生“结构幻觉”，导致输出不可用。本文通过构建“几何+语义”数据工厂与三阶段渐进训练策略，将通用VLM转化为高精度结构专家。该范式在通用基准上刷新了SOTA，但在复杂表格还原上仍略逊于专用流水线，其数据工程的可复现性存疑。

## 研究背景

当VLM处理密集文本或复杂布局时，其生成行为往往偏离严格的逻辑规则，表现为Markdown表格行序混乱或公式语法错误，这一现象被定义为结构幻觉。结构幻觉的根源在于模型缺乏对空间坐标与逻辑结构的细粒度对齐，而传统OCR流水线虽具备像素级精度，却难以重建多栏布局的阅读顺序。解决这一矛盾的关键在于如何在保持VLM生成灵活性的同时，内化严格的格式约束与领域语义。

DIE领域经历了从“OCR+后处理”到端到端视觉-语言生成的范式转折。以LayoutLM为代表的多模态预训练模型提升了细粒度理解能力，而Donut、Nougat等模型则直接通过像素生成结构化标记。然而，现有端到端模型在通用性上占优，但在金融、医疗等高stakes场景下，针对特定领域的专用模型和混合架构仍具有显著优势。当前研究热点集中在解决长文档结构一致性、复杂表格/公式解析，以及通过强化学习（RL）优化格式遵循能力。FireRed-OCR正是在这一背景下，针对VLM在密集文本环境下的格式遵循失效，提出了系统性的解决方案。

## 核心方法

### 方法参照系

端到端文档解析的标准流程通常直接采用监督微调（SFT）将像素映射为Markdown。本文的关键差异在于引入了前置的多任务预对齐阶段，以强化空间感知，并采用格式约束的组相对策略优化（GRPO）替代单纯的SFT，以抑制结构幻觉。

### 几何与语义双索引数据工厂

传统随机采样无法捕捉文档布局的多样性，导致简单布局主导训练分布。本文提出双索引机制，解耦布局复杂度与语义内容。通过轻量级图像编码器提取视觉特征向量，忽略文本内容，聚焦布局拓扑，执行无监督聚类。

$$
\mathcal{C} = \text{Cluster}(\{v_i\}_{i=1}^N, K)
$$

其中 $v_i$ 为第 $i$ 个文档图像的几何嵌入，$K$ 为聚类数。该公式将数据集映射到结构特征空间，识别并降采样高密度簇（如标准单栏文本），同时保留稀疏簇（如嵌套表格、不规则表单）作为长尾样本。结合多维度标签系统（语言、布局类型、文档来源、体裁），实现分层采样，确保模型看到均匀的难度分布而非自然数据分布。

### 三阶段渐进训练策略

多任务预对齐阶段联合训练检测、区域OCR与全页Markdown转换，建立基础文档能力。专用SFT阶段在高质量Markdown数据上微调，标准化结构输出。格式约束GRPO阶段引入强化学习，使用特定奖励函数优化结构合规性。

$$
\mathcal{R} = \alpha \cdot \mathbb{1}_{\text{formula\_valid}} + \beta \cdot \mathbb{1}_{\text{table\_closure}} + \gamma \cdot \text{Acc}
$$

该奖励函数 $\mathcal{R}$ 由公式有效性、表格闭合与内容准确率加权组成。GRPO通过组内相对优势估计，引导模型关注整体结构一致性而非局部token预测。这一设计弥补了自回归监督在段落级阅读顺序学习上的间接性缺陷，使模型具备自我修正能力，显著提升了复杂布局重建的鲁棒性。

## 实验评估

实验在OmniDocBench v1.5、FireRedBench、OCRBench、TEDS及PubTabNet上进行。基线覆盖Pipeline系统（PaddleOCR-VL-1.5）、通用VLM（GPT-5.2, Gemini-3.0 Pro）及端到端OCR模型（DeepSeek-OCR 2, dots.ocr）。FireRed-OCR-2B在OmniDocBench v1.5上取得92.94%的Overall分数，超越DeepSeek-OCR 2（91.09%）与OCRVerse（88.56%）。

| 模型 | OmniDocBench v1.5 | FireRedBench | OCRBench (Text) | TEDS | PubTabNet |
|---|---|---|---|---|---|
| PaddleOCR-VL-1.5 | 94.50 | 76.47 | 53.5 / 87.0 | 83.3 | 84.6 |
| Gemini-3.0 Pro | 90.33 | 79.68 | 91.9 | 81.8 | 91.4 |
| DeepSeek-OCR 2 | 91.09 | 61.61 | 48.5 | - | - |
| FireRed-OCR-2B | 92.94 | 74.62 | 93.5 | 80.6 | 77.0 |

FireRed-OCR-2B在Overall分数上领先，但在PubTabNet TEDS指标上（77.0）低于PaddleOCR-VL-1.5（84.6）与Gemini-3.0 Pro（91.4），表明其在复杂表格结构还原上仍逊于专用流水线或大规模通用VLM。

消融实验显示，单域GRPO优化存在模态干扰。Base + Table GRPO在Table TEDS上提升2.0点，但Text Edit距离劣于Text-only基线。Base + Table + Text联合训练导致Overall分数下降至88.72，低于单域基线。Base + Mix 1:1:1策略通过平衡多模态监督信号，实现Overall分数89.60，优于Table GRPO (Extended)的89.28，验证了平衡采样对缓解模态竞争的关键作用。

评估边界方面，FireRedBench为内部基准，其标注协议与OmniDocBench的一致性未明确说明。代码与模型权重已开源，但数据工厂的几何聚类参数与GRPO奖励权重敏感性未详细报告，限制了完全复现性。

## 关联研究分析

从问题动机看，FireRed-OCR与Logics-Parsing均聚焦于结构一致性，但Logics-Parsing通过SFT-then-RL范式优化页面结构对齐，而FireRed-OCR更强调数据分布的平衡与GRPO的格式约束。FireRed-OCR的双索引数据工厂解决了Logics-Parsing未充分处理的长尾布局分布不平衡问题，但其GRPO奖励函数设计缺乏统一标准，导致结果难以直接复现与比较。

从方法设计看，FireRed-OCR与Qianfan-OCR同属端到端VLM解析路线，但Qianfan-OCR引入Layout-as-Thought机制生成显式布局表示，而FireRed-OCR依赖隐式空间感知与GRPO约束。FireRed-OCR在OmniDocBench上超越Qianfan-OCR（84.39 AVG），但在FireRedBench上（74.62）与PaddleOCR-VL-1.5（76.47）持平，表明其在复杂非标准布局上的鲁棒性仍有提升空间。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

FireRed-OCR旨在解决VLM在文档解析中的结构幻觉问题，通过“几何+语义”数据工厂与三阶段渐进训练策略，将通用VLM转化为高精度结构专家。该框架在OmniDocBench v1.5上取得92.94%的Overall分数，超越DeepSeek-OCR 2（91.09%），证明了领域适配优于通用预训练。然而，其在PubTabNet TEDS指标上（77.0）低于PaddleOCR-VL-1.5（84.6），暴露了端到端模型在复杂表格结构还原上的局限。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01840)