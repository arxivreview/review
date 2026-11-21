# ACL2026最新论文 ｜AdabNER: Arabic Digital Archive Books with Nested Entity Recognition ｜阿拉伯语文学嵌套命名实体识别语料库 AdabNer

研究机构：法国索邦大学

作者：Aya Mourad、Mustafa Jarrar

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1ce1ee108314)

> 阿拉伯语文学文本中的嵌套实体识别长期缺乏大规模标注资源，现有新闻语料无法覆盖文学域特有的时空模糊性与跨时代术语。本文构建了首个大规模阿拉伯语文学嵌套命名实体识别（Nested Named Entity Recognition, NNER）语料库 AdabNer，并验证了多域联合训练对域间性能差距的收敛作用。通过微调 BERT 变体与少样本大语言模型（Large Language Models, LLMs）对比，证实了监督微调在 Token 级嵌套任务上的绝对优势。该工作填补了文学域 NER 空白，但域外泛化验证仅局限于单一语料对，其结论的普适性仍存疑。

## 研究背景

阿拉伯语命名实体识别（Named Entity Recognition, NER）面临形态丰富导致的边界检测困难与缺乏大写标记的双重挑战。传统序列标注假设实体边界互斥，但文学文本中常见一个实体提及包含多个子实体的嵌套结构，例如“阿巴斯一世侍从”同时涵盖职业、组织、人名与序数。这种结构复杂性要求模型在 Token 级别进行多标签分类，而非单一标签预测。

现有阿拉伯语 NER 资源多聚焦于新闻与社交媒体，如 Wojood 语料库虽包含嵌套标注，但其来源为网络报道，缺乏文学文本特有的非标准时空实体与跨时代行政术语。文学书籍中的实体常缺乏上下文支持，且殖民时期文本存在地理与行政划分的模糊性，导致基于新闻语料训练的模型在文学域泛化能力显著下降。本文切入点在于构建覆盖 138 本书、15 个十年的文学专用语料库，并通过多域联合训练验证跨域鲁棒性。

## 核心方法

### 多标签嵌套分类架构

嵌套 NER 的标准流程通常采用序列标注，但无法处理边界重叠。本文采用多标签 Token 分类架构，每个 Token 独立预测 21 个实体类别的概率，允许同一 Token 属于多个实体。该设计直接解决了嵌套结构中实体边界重叠导致的标注冲突问题。

### 文学域标注体系适配

基于 Wojood 框架，本文恢复 OntoNotes 的 WORK_OF_ART 类别以区分文学作品与商业产品，并收紧 NORP 定义以排除普通名词复数。这一改动源于文学批评文本中 WORK_OF_ART 占比 5.8% 而 PRODUCT 仅 0.2% 的分布差异，避免了将“诗人”等普通名词误标为民族/政治团体。

$$
P(y_i | x_i) = \sigma(W_i \cdot h_i + b_i), \quad y_i \in \{0, 1\}^{21}
$$

其中 $h_i$ 为 BERT 编码器输出的 Token 表示，$\sigma$ 为 Sigmoid 函数，独立计算每个类别的归属概率，实现嵌套实体的并行预测。

### 多域联合训练策略

针对文学域与新闻域间的词汇与时间尺度差异，本文提出联合训练策略，将 AdabNer 与 Wojood 数据混合训练单一模型。该策略旨在通过共享底层表示缓解域间分布偏移，使模型在两个域上均保持高性能。

$$
\mathcal{L}_{joint} = \sum_{d \in \{AdabNer, Wojood\}} \lambda_d \mathcal{L}_{focal}(y^{(d)}, \hat{y}^{(d)})
$$

其中 $\mathcal{L}_{focal}$ 为处理类别不平衡的 Focal Loss，$\lambda_d$ 为域权重，联合优化使模型同时适应文学与新闻两种文本风格。

## 实验评估

实验在 AdabNer 与 Wojood 上进行，采用留书交叉（Leave-Book-Out）与分层划分（Stratified）两种协议。基线覆盖 5 种阿拉伯语 BERT 变体与 5 种 LLM 少样本学习（In-Context Learning, ICL）。

| 模型 | 划分策略 | Micro F1 | Macro F1 |
| :--- | :--- | :--- | :--- |
| AraBERTv2 | Stratified | 0.86±0.003 | 0.83±0.006 |
| AraBERTv2 | Leave-Book-Out | 0.83±0.006 | 0.81±0.007 |
| Gemini 3 Pro | Stratified | 0.59±0.007 | 0.57±0.005 |
| Qwen3-235B | Stratified | 0.39±0.007 | 0.35±0.012 |

AraBERTv2 在两种划分下均显著优于 LLM，Gemini 3 Pro 作为最强 LLM 仍落后 27 个百分点，验证了 Token 级嵌套任务中监督微调的优势。

| 训练设置 | 测试域 | Micro F1 |
| :--- | :--- | :--- |
| 单域 AdabNer | Wojood | 0.66 |
| 单域 Wojood | AdabNer | 0.59 |
| 联合训练 | AdabNer | 0.853±0.006 |
| 联合训练 | Wojood | 0.921±0.002 |

联合训练将域间性能差距从 27% 缩小至 1% 以内，表明多域数据混合是提升跨域鲁棒性的有效路径。

评估协议采用精确跨度匹配，要求边界与类型完全一致。代码与数据已公开，但实验仅使用 3 个随机种子，未报告统计显著性检验。LLM 实验使用 vLLM 引擎与 A100 GPU，超参数设置统一，但 ICL 提示模板可能影响结果可比性。

## 关联研究分析

从问题动机看，本文与 LitBank 共享文学域 NER 的视角，但 LitBank 聚焦英文小说且嵌套率仅 13.8%，而 AdabNer 覆盖非虚构文学且嵌套率达 18.96%。这一差异源于阿拉伯语文学中行政与历史实体的密集嵌套，而非叙事性人物关系。从方法设计看，本文与 SAM-NER 均探索 LLM 在 NER 中的应用，但 SAM-NER 采用零样本语义原型中介，本文采用 5-shot ICL。本文 LLM 性能远低于微调 BERT，可能源于文学域在 LLM 预训练数据中的稀缺性，而非 ICL 范式本身的局限。

## 总结

本文核心矛盾在于文学域嵌套 NER 缺乏专用语料与跨域鲁棒性验证。通过构建 876k tokens 的 AdabNer 语料库，本文提供了首个大规模阿拉伯语文学嵌套 NER 基准。实验证明 AraBERTv2 微调达到 0.86 F1，且联合训练可将域间差距缩小至 1% 以内。然而，域外评估仅涉及 Wojood 单一语料对，且 LLM 性能低下可能受限于提示设计而非模型能力。当支持集规模扩大或提示模板优化时，LLM 在嵌套 NER 中的性能边界是否会上移，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_1ce1ee108314)