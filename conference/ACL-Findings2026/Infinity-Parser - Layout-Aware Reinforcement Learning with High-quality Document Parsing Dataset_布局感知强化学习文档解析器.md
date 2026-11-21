# ACL-Findings2026最新论文 ｜Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset ｜布局感知强化学习文档解析器

研究机构：英国利物浦大学

作者：Baode Wang、Biao Wu、Weizhen Li 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_02734a87777b)

> 端到端文档解析旨在将扫描图像直接转换为结构化Markdown，但现有视觉语言模型（VLM）在监督微调（SFT）下易过拟合表面模式，导致分布外（OOD）泛化能力不足。Infinity-Parser通过构建400,066页高质量数据集Infinity-Doc-400K，并引入基于编辑距离、段落计数与阅读顺序的多面奖励强化学习（RL）框架，解决了SFT在复杂布局下的结构一致性退化问题。该方法在OmniDocBench上取得0.122的英文整体编辑距离，验证了RL在文档解析中的有效性，但其绝对性能仍低于部分最新SOTA，且对合成数据依赖性的边界尚存疑。

## 研究背景

文档解析需同时恢复文本内容与空间结构，传统OCR管道因误差累积难以处理多栏布局，而端到端VLM虽消除了中间步骤，却面临训练数据标注噪声大、布局多样性不足的挑战。现有数据集如DocStruct4M侧重OCR任务，缺乏严格的字符级对齐与布局分析监督，导致模型难以学习深层的空间逻辑关系。

该领域的核心矛盾在于生成式模型的灵活性与结构化数据的零容错需求之间的冲突。主流SFT范式提供token级监督，但模型倾向于记忆表面特征而非底层原理，在未见过的文档类型上表现脆弱。Infinity-Parser的切入点在于将文档解析重构为强化学习问题，通过可验证的多面奖励信号引导模型学习可迁移的布局表示，而非依赖有偏的伪标签。

## 核心方法

### 方法参照系

本文问题属于端到端文档解析类别，标准流程为“视觉编码-自回归解码”。关键差异在于训练范式：标准流程依赖SFT最大化似然，而本文采用RL优化基于规则的结果奖励，直接针对解析质量而非token概率。

### 高质量双源数据构建

数据质量是RL有效性的前提。传统伪标签管道依赖单一模型，导致标注不一致。本文设计双源管道：合成数据通过Jinja模板注入Wikipedia内容并渲染为HTML，确保字符级精确对齐；真实数据采用多专家模型交叉验证，仅保留一致性高的区域。这种设计解决了伪标签噪声大、分布不均的问题，为RL提供了可靠的参考输出。

### 布局感知强化学习

SFT在长序列生成中易出现结构崩溃，因其优化目标与最终解析质量脱节。本文引入GRPO算法，将文档解析结果作为最终预测，通过多面奖励 $R_{Multi-Aspect}$ 引导学习。该奖励由编辑距离 $R_{dist}$、段落计数 $R_{count}$ 和阅读顺序 $R_{order}$ 加权组成：

$$ R_{Multi-Aspect} = R_{dist} + R_{count} + R_{order} $$

其中 $R_{dist} = 1 - D(y, \hat{y})/\max(N, M)$ 衡量内容保真度，$R_{count} = 1 - |N_Y - N_{\hat{Y}}|/N_Y$ 惩罚段落缺失或冗余，$R_{order} = 1 - D_{order}/\max_{inv}$ 确保阅读顺序正确。这一设计将结构约束显式纳入优化目标，使模型在生成过程中内化布局逻辑，从而提升OOD场景下的鲁棒性。

## 实验评估

实验在OmniDocBench、olmOCR-Bench、PubTabNet和FinTabNet上进行，基线覆盖Pipeline（MinerU）、通用VLM（GPT-4o）及专用VLM（GOT-OCR）。Infinity-Parser-7B在OmniDocBench英文整体编辑距离上取得0.122，优于MinerU的0.15和GPT-4o的0.233，但在中文上为0.174，显示语言依赖性。

| 方法 | OmniDocBench EN OverallEdit↓ | OmniDocBench ZH OverallEdit↓ | olmOCR Overall↑ |
|---|---|---|---|
| MinerU | 0.15 | 0.357 | - |
| GPT-4o | 0.233 | 0.399 | 69.9 |
| Infinity-Parser-7B | 0.122 | 0.174 | 82.5 |

消融实验表明，RL-only训练（OA-EN 0.169）优于SFT-only（0.198），且多面奖励（0.122）显著优于仅编辑距离奖励（0.169）。合成数据单独使用RL（0.182）效果远差于混合数据（0.122），证实真实数据对结构多样性的必要性。

评估边界：指标未报告置信区间，且未与FireRed-OCR等最新SOTA直接对比。可复现性方面，论文声明将发布代码与模型，训练使用8张A100 GPU，学习率 $1.0 \times 10^{-6}$，KL系数 $1.0 \times 10^{-2}$。

## 关联研究分析

从问题动机看，Logics-Parsing采用SFT-then-RL两阶段范式，强调SFT提供初始能力；而Infinity-Parser证明直接RL在OOD上更优，暗示SFT可能引入token级归纳偏置，限制探索空间。这一差异源于RL奖励对全局结构的直接优化，而非依赖局部token预测。

从方法设计看，Qianfan-OCR通过Layout-as-Thought显式生成布局表示，而Infinity-Parser通过RL隐式学习布局，无需中间推理步骤。前者牺牲了端到端的高效性以换取可解释性，后者则依赖高质量数据确保隐式学习的可靠性。这种取舍反映了领域在“显式结构建模”与“隐式端到端优化”之间的路线分歧。

## 总结

Infinity-Parser针对SFT在文档解析中泛化能力不足的矛盾，通过高质量双源数据与布局感知RL框架，实现了结构一致性与语义准确性的联合优化。其在OmniDocBench上0.122的英文编辑距离验证了RL的有效性，但中文性能（0.174）与最新SOTA的差距暴露了数据规模与语言多样性的局限。当训练数据中真实文档比例降低时，RL的结构优化能力是否会被合成数据的同质性所抵消，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_02734a87777b)