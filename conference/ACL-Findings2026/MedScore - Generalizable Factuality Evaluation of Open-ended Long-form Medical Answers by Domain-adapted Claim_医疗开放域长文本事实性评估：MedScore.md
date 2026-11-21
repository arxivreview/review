# ACL-Findings2026最新论文 ｜MedScore: Generalizable Factuality Evaluation of Open-ended Long-form Medical Answers by Domain-adapted Claim Decomposition and Verification ｜医疗开放域长文本事实性评估：MedScore

研究机构：美国约翰斯·霍普金斯大学

作者：Heyuan Huang、Alexandra DeLucia、Vijay Murari Tiyyala 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_398b3efcb301)

> 导读 现有分解-验证框架在传记等实体中心文本上表现良好，但面对医疗对话中语境依赖、主观且结构复杂的回答时，分解质量严重退化，导致事实性得分失真。本文指出通用分解方法无法处理“如果疼痛加剧”这类假设性语句，提出MedScore，通过领域适配的条件感知分解与多源验证解决该问题。实验显示其有效声明提取量达现有方法3倍，但外部语料验证得分显著低于内部知识，暴露了检索覆盖度对评估可靠性的制约。

## 研究背景

当评估大语言模型生成的医疗建议时，直接计算准确率失效，因为不存在唯一的标准答案。此时需采用分解-验证策略，将长文本拆解为原子事实并逐一核对。然而，医疗文本中的“建议”往往隐含前提条件（如“若症状持续”），若分解时丢失该条件，原子事实便变得不可验证或语义扭曲。这种语境依赖性是医疗文本区别于传记文本的核心特征，也是现有评估框架失效的根源。

主流分解-验证方法如FActScore和VeriScore主要基于传记数据训练，其分解逻辑假设句子是独立的事实陈述。在医疗场景中，这种假设导致大量声明被标记为“不可验证”或“幻觉”，因为模型无法区分“患者正在经历疼痛”（不可验证的叙事）与“布洛芬可缓解疼痛”（可验证的事实）。VeriScore虽引入上下文提示，但过度过滤导致声明覆盖率极低，牺牲了信息完整性。本文切入点在于构建一套针对医疗对话特性的分解分类学，并据此设计条件感知的分解流程，以保留声明的语境依赖性。

## 核心方法

### 方法参照系

本文基于分解-验证范式，与FActScore的主要差异在于分解阶段的提示工程与验证阶段的语料选择。FActScore采用少样本提示进行通用分解，而本文引入领域特定的MedScoreTaxonomy指导分解，并针对医疗语料库进行验证适配。

### 条件感知分解

针对通用分解丢失语境条件的问题，本文设计MedScore分解提示。该提示基于MedScoreTaxonomy，要求模型在分解时保留“条件-建议”结构。例如，将“If pain gets worse, call a doctor”分解为“若疼痛加剧，应联系医生”而非“应联系医生”。分解过程由GPT-4o-mini执行，输入包含句子及其上下文。

$$
C_{valid} = \{ c_i \mid c_i \in Decompose(S, Context), \text{Valid}(c_i) = True \}
$$

其中 $C_{valid}$ 为有效声明集合，$\text{Valid}(c_i)$ 依据MedScoreTaxonomy判断声明是否完整、非幻觉且结构正确。该设计确保了声明在保留原始语境依赖的同时，转化为可验证的陈述句。

### 多源验证与评分

验证阶段采用三种知识源：LLM内部知识、医生原始回答（仅AskDocsAI）及外部医疗语料库MedCorp。事实性得分定义为有效声明中验证为真的比例。

$$
Score = \frac{\sum_{c \in C_{valid}} \mathbb{I}(Verify(c, K) = True)}{|C_{valid}|}
$$

其中 $K$ 为知识源，$\mathbb{I}$ 为指示函数。该公式揭示了得分对分母 $|C_{valid}|$ 的敏感性：若分解产生过多无效声明，得分将被稀释；若分解过度过滤，得分可能因分母小而虚高。MedScore通过最大化 $|C_{valid}|$ 中的有效比例，平衡了覆盖率与准确性。

## 实验评估

实验在AskDocsAI（新构建）、PUMA及CaLMQA上进行，基线包括FActScore、VeriScore、Core及DnDScore。对比方法覆盖了少样本、微调及过滤策略，但缺乏多智能体辩论类基线。

| 数据集 | 方法 | GPT-4o内部知识 | 医生回答 | MedCorp检索 |
|---|---|---|---|---|
| AskDocsAI | FActScore | 31.96% | 80.94% | 50.04% |
| AskDocsAI | MedScore | 76.54% | 94.68% | 70.07% |
| AskDocsAI | VeriScore | 81.94% | 94.41% | 68.16% |
| PUMA | FActScore | 35.35% | - | 47.34% |
| PUMA | MedScore | 78.54% | - | 61.56% |

在AskDocsAI上，MedScore在GPT-4o内部知识验证下得分76.54%，显著高于FActScore的31.96%，但低于VeriScore的81.94%。VeriScore的高分源于其极低的声明数量（分母小），而非更高的事实性。在外部MedCorp验证下，MedScore得分70.07%，高于FActScore的50.04%，表明其分解质量在检索场景下更具鲁棒性。

消融分析显示，MedScore在PUMA上的调整后验证率为63.75%，高于FActScore的60.09%和VeriScore的47.48%。VeriScore在PUMA上的0-claim率高达53.69%，因其无法处理口语化短句，导致大量信息被遗漏。MedScore的0-claim率为9.3%，显示其对低质量文本的适应性更强。

评估边界方面，论文未报告置信区间，且外部语料验证得分较内部知识下降约26%，主要归因于检索噪声与语料覆盖不足。代码已开源，但超参数细节仅在附录中提供，未公开GPU资源需求。

## 关联研究分析

从问题动机看，本文与FActScore同属分解-验证路线，但针对医疗语境依赖性问题进行了专门适配。FActScore的分解逻辑基于实体中心假设，而MedScore通过Taxonomy显式处理条件性语句。这一差异源于任务特性：医疗建议的验证依赖于前提条件，而传记事实的验证仅依赖于实体属性。本文未探索多跳推理，因为医疗QA通常不涉及跨文档的逻辑链，这与HOVER等多跳基准的任务设定不同。

从方法设计看，MedScore与VeriScore均使用上下文提示，但VeriScore通过微调模型实现，而MedScore通过提示工程实现。VeriScore的微调导致其在分布外数据（如PUMA）上泛化能力差，0-claim率极高。MedScore的提示工程策略更灵活，但依赖LLM的指令跟随能力。本文未对比基于检索增强的验证方法，如RAG，这可能是一个盲区，因为医疗事实的验证往往需要最新指南支持，而内部知识可能过时。

## 总结

本文核心矛盾在于通用分解方法无法处理医疗文本的语境依赖性，导致事实性评估失真。MedScore通过条件感知分解与多源验证，将有效声明提取量提升至现有方法的3倍，在AskDocsAI上实现76.54%的内部知识验证得分。其边界在于外部语料验证得分显著低于内部知识，暴露了检索覆盖度对评估可靠性的制约。当MedCorp语料库扩展至包含最新临床指南时，外部验证得分是否能接近内部知识水平，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_398b3efcb301)