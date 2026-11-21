# ACL-Findings2026最新论文 ｜Redefining Machine Simultaneous Interpretation: From Incremental Translation to Human-Like Strategies ｜动作基同步机器翻译

研究机构：香港中文大学

作者：Qianen Zhang、Zeyu Yang、Satoshi Nakamura

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_188650380d2b)

> 同步机器翻译（Simultaneous Machine Translation, SiMT）的核心矛盾在于增量生成过程中的延迟与质量权衡，传统READ/WRITE策略无法捕捉人类译员的重构、省略与简化行为。现有基于固定策略或隐式等待标记的方法在长句重排和口语冗余处理上存在刚性瓶颈。本文通过扩展LLM动作空间，将人类口译策略显式化为动态决策过程，实现了质量与延迟的更优平衡。该方法在ACL60/60基准上验证了动作引导推理的有效性，但其依赖开发集统计注入的机制是否导致分布过拟合，尚存疑。

## 研究背景

同步翻译要求系统在源语音流未完整接收时即开始生成目标文本，这一约束导致信息不完整下的决策困境。为平衡延迟与质量，系统需决定何时读取（READ）源词、何时写出（WRITE）目标词。然而，仅靠这两个原子动作无法处理口语中的冗余填充词、长句结构重排或指代简化，导致译文要么延迟过高，要么语义失真。

主流SiMT路线分为两类：一是基于编码器-解码器的固定策略（如wait-k），通过预设等待步数控制延迟，但缺乏对源句复杂度的自适应能力；二是基于LLM的隐式等待机制（如TransLLaMA），通过插入<WAIT>标记让模型隐式学习等待时机，但无法显式执行“删除冗余”或“切断长句”等高级操作。这些方法的共同局限在于，它们将翻译视为纯粹的序列生成问题，忽略了人类译员在实时场景下采用的策略性重构行为。本文的切入点在于，将人类口译中的Salami分割、选择性省略等策略形式化为LLM可执行的动作空间，使模型在生成过程中能动态选择“如何翻译”而不仅仅是“何时翻译”。

## 核心方法

### 方法参照系

标准SiMT框架将翻译建模为READ/WRITE二值决策序列，模型在每一步选择读取下一个源词或输出一个目标词。本文问题与该通用流程的关键差异在于，它引入了四个非生成性动作（Sentence_Cut, Drop, Partial_Summarization, Pronominalization），将决策空间从二元扩展为六元，允许模型在生成间隙执行源句重构或目标句简化操作。

### 扩展动作空间与统计注入

传统READ/WRITE策略无法处理口语中的冗余和长句重排，导致模型要么过度等待，要么生成不流畅的译文。本文在动作空间中引入四个新动作：Sentence_Cut将长句切分为语法完整的短段，Drop移除无信息量的填充词（如“uh”），Partial_Summarization合并语义重复的从句，Pronominalization用代词替换已提及的名词短语。这些动作在推理时由LLM动态选择，其选择依据是注入提示中的动作级统计信息。具体地，在ACL60/60开发集上，使用GPT-4o生成各动作下的译文，计算其BLEU和TTS-based LAAL，并将这些统计值嵌入提示词中。例如，提示词中明确告知模型：“Drop → LAAL ≈ 2.581s, BLEU ≈ 58.94”。这种设计使LLM在决策时能权衡不同动作对质量和延迟的预期影响，而非仅依赖源句内容。

$$
\text{Prompt} = \mathcal{P}(\text{Task}, \text{ActionSet}, \{(\text{Action}_i, \text{BLEU}_i, \text{LAAL}_i)\}_{i=1}^4, \text{Source})
$$

该公式表示提示词由任务描述、动作集合、各动作的质量-延迟统计对及源句构成，使LLM在每一步决策时能参考经验数据。

### TTS-based LAAL评估

传统token-level LAAL无法直接反映实时场景下的秒级延迟，且依赖离线参考，可能鼓励过度等待。本文提出TTS-based LAAL，通过Whisper获取源词时间戳，利用延迟感知TTS管道生成目标语音，从而在真实时间轴上测量目标词发射时间。对于目标序列$Y = (y_1, ..., y_{|Y|})$，定义$g(u) = |\{j | t_j \le \tau_u\}|$为第$u$个目标词发射时已观察到的源词数，$d(u) = \min(|X|, \frac{g(u)}{u}(u-1))$为长度自适应对角线索引。TTS-based LAAL计算为：

$$
\text{LAAL}_{\text{sec}} = \frac{1}{\tau^*} \sum_{u=1}^{\tau^*} (\text{time}(g(u)) - \text{time}(d(u)))
$$

其中$\tau^*$为源句完全覆盖时的目标步数。该指标将延迟测量从token空间映射到秒级时间空间，更直接地反映同步翻译的实时性约束。

## 实验评估

实验在ACL60/60基准上进行，覆盖En-Zh、En-De、En-Ja三个语言对，基线包括TransLLaMA（隐式WAIT）、Few-shot prompting、Salami分割及mBART50监督微调。主实验结果显示，Step-wise (Actions)在En-Zh上取得55.31 BLEU和2.524s LAAL，优于TransLLaMA的53.12 BLEU和2.938s LAAL，也优于Salami的50.16 BLEU和2.955s LAAL。

| 方法 | BLEU | chrF | TER↓ | COMET-da | COMET-KIWI | LAAL (s)↓ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TransLLaMA ① | 53.12 | 30.11 | 98.35 | 0.8735 | 0.8313 | 2.938 |
| Few-shot ④ | 52.27 | 34.93 | 108.25 | 0.8926 | 0.8379 | 3.049 |
| ⑦Salami | 50.16 | 31.98 | 106.37 | 0.8854 | 0.8295 | 2.955 |
| ⑧Step-wise (Actions) | 55.31 | 34.33 | 101.42 | 0.8998 | 0.8439 | 2.524 |
| ⑨Step-wise (Drop / Cut) | 55.33 | 34.49 | 99.06 | 0.8913 | 0.8447 | 2.613 |

Step-wise (Drop / Cut)组合在BLEU上略高于完整动作集（55.33 vs 55.31），但LAAL更高（2.613s vs 2.524s），表明Drop和Sentence_Cut是延迟优化的主要贡献者，而Partial_Summarization和Pronominalization对质量有边际贡献但增加延迟。mBART50实验显示，使用action-based参考训练比使用原始MUST-C参考提升BLEU 3.05点（24.34 vs 21.29），证明参考适配对监督模型的有效性。

评估边界方面，TTS-based LAAL依赖Whisper和TTS管道的准确性，其与传统LAAL的相关性未在文中验证。实验仅覆盖文本到文本设置，未涉及语音输入，限制了结论向完整SiMT系统的推广。代码已开源，但超参数细节（如动作统计的更新频率）未在正文中详述，可能影响复现性。

## 关联研究分析

从问题动机看，本文与SubDocTrans等文档级翻译方法共享“外部知识注入”范式，但目标不同：SubDocTrans通过注入双语摘要解决长文档术语一致性，本文通过注入动作统计解决实时延迟权衡。差异根源在于任务特性：文档级翻译允许离线预处理，而SiMT要求在线决策，因此本文的统计注入必须在推理时动态生效，而非离线构建。从方法设计看，本文与TransLLaMA同属LLM-based SiMT路线，但TransLLaMA通过<WAIT>标记隐式学习等待，本文通过显式动作选择实现策略控制。TransLLaMA的隐式机制在延迟优化上表现竞争（2.938s），但无法执行Drop等重构操作，导致其在口语冗余处理上不如本文（55.31 vs 53.12 BLEU）。这种差异暗示，显式动作空间在需要源句重构的场景下更具优势，但在纯延迟敏感场景下，隐式机制可能因决策开销更低而更优。

## 总结

本文要解决的核心矛盾是SiMT中延迟与质量的刚性权衡，现有READ/WRITE策略无法捕捉人类译员的策略性重构行为。本文抓住的切入点是，将Salami分割、选择性省略等人类口译策略形式化为LLM可执行的动作空间，使模型能动态选择“如何翻译”而不仅仅是“何时翻译”。通过扩展动作空间并注入动作级统计，本文在ACL60/60 En-Zh上取得55.31 BLEU和2.524s LAAL，优于TransLLaMA和Salami基线。本文的边界在于，动作统计依赖开发集分布，且实验仅限文本到文本设置，未验证语音输入下的鲁棒性。当开发集与测试集的口语冗余分布存在显著差异时，注入的动作统计是否仍能有效引导决策，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_188650380d2b)