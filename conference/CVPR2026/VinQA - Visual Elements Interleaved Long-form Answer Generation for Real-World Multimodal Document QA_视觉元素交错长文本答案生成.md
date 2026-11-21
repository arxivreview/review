# CVPR2026最新论文 ｜VinQA: Visual Elements Interleaved Long-form Answer Generation for Real-World Multimodal Document QA ｜视觉元素交错长文本答案生成

研究机构：LG AI研究院

作者：Young Rok Jang、Hyesoo Kong、Kyunghwan An 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.16092)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16092)

> 多模态文档问答（Multimodal Document QA）长期受限于答案模态单一，现有检索增强生成（Retrieval-Augmented Generation, RAG）范式仅输出纯文本，导致图表、表格等视觉证据在推理链中丢失。本文切入点在于将视觉元素作为可引用的一等公民嵌入长文本答案，而非仅作为背景输入。通过构建VinQA数据集并设计两种视觉编码策略，验证了微调开源模型可显著缩小与闭源前沿模型的差距。其价值在于填补了多模态答案生成的评估空白，但视觉引用精度在复杂布局下仍受限于检测器性能。

## 研究背景

当模型面对包含复杂图表的金融报告时，纯文本答案无法传达数值趋势的视觉直观性，这要求答案本身具备多模态表达能力。然而，传统多模态RAG流程中，视觉元素仅作为上下文输入被模型“阅读”，其空间位置与数值语义在文本化过程中被剥离。这种“输入多模态、输出单模态”的不对称，导致模型难以在答案中精确引用特定视觉区域，例如无法指出“图3中的红色曲线代表Q3营收”。

多模态文档理解的主流路线分为全页处理与检索增强两类。全页处理（如VisRAG）直接编码整页图像，保留布局但计算成本高；检索增强（如M-LongDoc）先检索相关页面再解析，效率较高但依赖OCR与布局分析的级联精度。两条路线的共同瓶颈在于答案生成阶段缺乏对视觉元素的显式引用机制，模型只能生成描述性文本，无法将视觉证据与文本断言精确绑定。本文的切入点在于将视觉元素检测与答案生成解耦，通过引入视觉引用标识符，使模型能够生成“文本+视觉裁剪图”交错的长文本答案，从而在答案层面实现多模态接地。

## 核心方法

### 方法参照系

本文问题属于多模态RAG框架下的答案生成子任务，与标准流程的关键差异在于输出模态。标准RAG流程中，检索器返回页面图像或文本，生成器输出纯文本答案；本文要求生成器输出包含视觉元素引用标识符的长文本，且每个标识符对应一个从原始页面裁剪出的视觉区域，该区域需与引用文本在语义上严格对齐。

### 视觉编码与引用机制

设计动机在于解决纯文本答案无法精确指代视觉区域的问题。本文提出两种编码策略：Page Encoding直接编码整页图像，利用DocLayout检测视觉元素边界框（Bounding Box, BBox），将BBox坐标作为文本Token输入模型，模型通过引用BBox标识符来指代视觉区域；Modality Encoding则先通过OCR提取文本，再裁剪视觉元素，将文本Token与视觉Token分别编码，模型通过引用裁剪图标识符来指代视觉区域。Page Encoding的输入表示为：

$$
\mathcal{I}_{PE} = \{ (p_i, \text{BBoxList}_i) \}_{i=1}^n
$$

其中 $p_i$ 为第 $i$ 页图像，$\text{BBoxList}_i$ 为该页视觉元素的边界框集合。该公式的物理含义是模型同时接收原始视觉信息与结构化空间坐标，无需显式解析即可理解布局。Modality Encoding的输入表示为：

$$
\mathcal{I}_{ME} = \{ (t_i, V_i) \}_{i=1}^n
$$

其中 $t_i$ 为OCR提取的文本，$V_i$ 为裁剪后的视觉元素图像集合。该公式的物理含义是模型接收解耦的模态信息，文本与视觉独立编码，但丢失了原始布局关系。

### 多模态接地评估框架

设计动机在于传统CER/IoU指标无法评估多模态答案的语义正确性与视觉引用准确性。本文提出M-GroSE（Multimodal Grounded QA Scoring Evaluator），扩展GroUSE框架，从相关性、完整性、忠实性三个维度评估答案，并引入Visual Source F1直接衡量视觉引用精度。M-GroSE的评分函数为：

$$
\text{M-GroSE} = \frac{1}{3} \sum_{d \in \{R, C, F\}} S_d + S_{UA}
$$

其中 $S_d$ 为维度 $d$ 的1-5分评分，$S_{UA}$ 为不可回答问题的F1分数（线性重缩放至1-5）。该公式的物理含义是模型需同时满足文本推理正确性与视觉引用准确性，任一维度缺失均导致总分下降。Visual Source F1的计算公式为：

$$
\text{Visual Source F1} = \frac{2 \cdot P \cdot R}{P + R}
$$

其中 $P$ 为预测视觉引用的精确率，$R$ 为召回率。该公式的物理含义是模型引用的视觉元素必须与金标准引用完全匹配，否则视为错误。

## 实验评估

实验在自建VinQA数据集上进行，包含39,700个可回答与3,000个不可回答QA对，覆盖7个文档域。基线覆盖闭源模型（GPT-4.1, Claude 3.5 Sonnet）与开源模型（Qwen2.5-VL-7B, InternVL3-8B），但缺失专用解析模型（如MinerU2.5）与检索专用模型（如ColPali）的对比，可能高估了通用VLM在多模态答案生成上的相对优势。

| 模型 | 编码策略 | M-GroSE Avg | Visual Source F1 |
| :--- | :--- | :--- | :--- |
| Claude 3.5 Sonnet | Page Encoding | 3.53 | 0.65 |
| GPT-4.1 | Modality Encoding | 3.63 | 0.72 |
| Qwen2.5-VL-7B (VinQA) | Page Encoding | 3.34 | 0.55 |
| Qwen2.5-VL-7B (VinQA) | Modality Encoding | 3.33 | 0.58 |

微调后的Qwen2.5-VL-7B在Page Encoding下M-GroSE Avg为3.34，Visual Source F1为0.55，显著高于未微调基线（3.01/0.23），但仍低于Claude 3.5 Sonnet（3.53/0.65）。Modality Encoding在微调前表现更优，但微调后Page Encoding性能追平，表明显式解析并非多模态答案生成的必要条件。

消融实验显示，VinQA微调在所有视觉元素类型（Chart, Table, Figure）上均提升引用精度，其中Figure类型提升幅度最大（Modality Encoding下从1.66提升至3.65）。这一反直觉发现表明，复杂视觉元素（如图形）的引用难度高于结构化元素（如表格），而VinQA提供的监督信号对复杂元素更有效。

评估边界方面，M-GroSE依赖GPT-5-mini作为LLM-judge，可能存在评估偏差；Visual Source F1仅衡量引用标识符的匹配，未评估引用文本与视觉内容的语义一致性。可复现性方面，论文提供超参数（3 epochs, 16×A100 GPUs）但未开源代码，VinQA数据集构建依赖ColQwen检索器与Gemini 2.0 Flash Thinking生成，复现成本较高。

## 关联研究分析

从问题动机看，VinQA与MCiteBench均关注多模态引用，但MCiteBench限于学术论文的预提取文本片段与裁剪图像，而VinQA从原始页面图像出发，覆盖更广泛的文档域（如金融报告、指南）。这一差异源于任务特性：学术论文的视觉元素（如图表）通常具有标准布局，预提取即可满足引用需求；而真实世界文档的视觉元素布局复杂，需从原始图像中动态检测与裁剪。VinQA的Page Encoding策略在此场景下更具优势，因其无需依赖OCR与布局分析的级联精度，直接利用原始图像的空间信息。

从方法设计看，VinQA与VisRAG共享Page Encoding思路，但VisRAG仅生成短文本答案，而VinQA生成长文本交错答案。这一差异源于答案模态的扩展：短文本答案无需精确引用视觉区域，而长文本答案需在多个段落中多次引用不同视觉元素，对引用精度与位置准确性要求更高。VinQA引入的Visual G-Eval评估器专门针对这一需求，评估视觉元素插入位置的语义适当性，而VisRAG未涉及此维度。

## 总结

本文要解决的核心矛盾是多模态文档问答中视觉证据在答案层面的丢失问题。现有方法因输出模态单一，无法在答案中精确引用视觉区域，而本文通过引入视觉引用标识符与两种编码策略，使模型能够生成“文本+视觉裁剪图”交错的长文本答案。实验证明，微调Qwen2.5-VL-7B后，Page Encoding的M-GroSE Avg达到3.34，Visual Source F1达到0.55，显著缩小了与闭源模型的差距。本文的边界在于视觉引用精度受限于DocLayout检测器性能，复杂布局下的边界框错误会直接导致引用错误。当文档包含密集重叠的视觉元素时，Page Encoding的边界框解析是否仍能保持引用准确性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16092)