# ACL-Findings2026最新论文 ｜CoTrust: Privacy-Preserving Collaboration Between Large and Small Language Models in Trusted Execution Environments ｜可信执行环境内的大小模型协同隐私推理

作者：Zhenya Ma、Tingyi Wang、Yongheng Deng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c25ad94d058)

> 导读 大语言模型（LLM）在处理含个人身份信息（PII）的用户输入时，直接部署高容量模型于可信执行环境（TEE）受限于内存与算力瓶颈，而将敏感数据暴露给外部模型则面临隐私泄露风险。现有脱敏方法通过掩码保护隐私，但往往丢弃关键语义线索，导致生成质量显著下降。CoTrust 提出一种协同推理框架，让 TEE 内的小语言模型（SLM）处理全保真输入，外部 LLM 基于多视图脱敏数据生成共识脚手架，再由 SLM 在 TEE 内实例化最终答案。该框架在保持强隐私保护的同时接近无掩码 LLM 的性能上限，但其依赖硬件信任假设，且未验证 TEE 被攻破时的鲁棒性。

## 研究背景

当用户向 LLM 服务提交包含姓名、地点等 PII 的查询时，系统面临两难：将完整输入送入外部 LLM 会泄露隐私，而仅在 TEE 内运行小模型则牺牲推理能力。TEE 提供硬件级隔离，确保内存与计算流对不可信软件不可见，但其内存限制（通常 <1GB）无法容纳数十亿参数的 LLM。这种资源约束迫使研究者探索“隐私-效用”权衡的新路径，即如何在保护敏感数据的同时利用大模型的生成能力。

主流防御路线分为两类：一是输入脱敏，通过正则匹配或轻量分类器识别 PII 并替换为占位符，但此类方法常过度清洗或遗漏语义细微差别，导致 LLM 输出质量下降；二是差分隐私（DP），提供形式化保证但计算成本高且严重损害模型效用，难以应用于大规模推理场景。CoTrust 的切入点在于解耦“敏感信息访问”与“高容量推理”，让外部 LLM 仅接触脱敏视图，而 TEE 内 SLM 负责最终隐私敏感实例化，从而在架构层面规避了脱敏导致的语义损失与 DP 的效用代价。

## 核心方法

### 方法参照系

本文问题属于“推理时输入隐私保护”范畴，与通用“内容净化”流程的关键差异在于：传统方法单次掩码后直接送入 LLM，而 CoTrust 引入多视图脱敏与共识脚手架机制，将 LLM 的生成能力转化为隐私安全的结构化指导，而非直接输出。

### 多视图脱敏与候选参考生成

单视图掩码的脆弱性在于不同掩码策略可能丢弃不同的非敏感语义子集（如实体角色、时间线索），导致 LLM 输出不稳定。CoTrust 在 TEE 内对输入 $x$ 应用 $K$ 个不同的掩码函数 $\{T^{(1)}, \dots, T^{(K)}\}$，生成互补的脱敏视图：

$$v^{(k)} = T^{(k)}(x), \quad k = 1, \dots, K$$

每个视图以不同方式掩码敏感实体（如用类型 token `[NAME_0]` 或伪名 `Jasper`），同时保留不同的非敏感语义子集。外部 LLM 独立处理每个视图，生成候选参考 $r^{(k)} = \text{LLM}(v^{(k)})$。这一设计解决了单视图掩码因语义丢失导致的 LLM 输出质量波动问题，通过多视图多样性捕获更完整的推理线索。

### 共识脚手架归纳与 TEE 内实例化

多视图生成的候选参考使用不兼容的占位符（如 `Jasper` vs `[NAME_0]`），无法直接合并。CoTrust 将参考送回 TEE，利用脱敏映射 $M$ 进行跨视图实体规范化，生成共享规范空间的参考。这些规范化参考再送回外部 LLM，归纳为单一共识脚手架 $S$：

$$S = \text{Induce}(\text{LLM}(\{r^{(k)}_{\text{canon}}\}_{k=1}^K))$$

脚手架 $S$ 蒸馏了 LLM 在多视图下的生成能力，形成隐私安全的结构化模板。最后，TEE 内 SLM 使用原始输入 $x$ 与实例化后的脚手架 $S_{\text{priv}}$ 生成最终答案：

$$\hat{y} = \text{SLM}_{\text{TEE}}(x, S_{\text{priv}})$$

这一设计解决了 SLM 容量有限无法直接合并多参考的问题，让 LLM 负责高容量推理，SLM 仅负责隐私敏感实例化，实现了能力与隐私的解耦。

## 实验评估

实验在 MedQA、SQuAD、SAMSum、DialogSum 四个含 PII 的数据集上评估，基线覆盖 SLM-Only、Single-Masked-LLM、Multi-Masked-LLM、LLM-Guided-SLM 及无掩码 LLM 上限。CoTrust 在 SQuAD EM 指标上达到 54.68，显著高于 Single-Masked-LLM 的 49.64 和 Multi-Masked-LLM 的 47.46，接近无掩码 LLM 的 51.81（Qwen3 配对）或 62.71（Ministral 配对）。在 MedQA F1 上，CoTrust 取得 61.40，优于所有隐私基线，接近无掩码 LLM 的 62.93。

| 模型配对 | 方法 | SQuAD EM | MedQA F1 | QM-Score (SAMSum) |
|---|---|---|---|---|
| Qwen3-4B/8B | CoTrust | 54.68 | 61.40 | 6.144 |
| Qwen3-4B/8B | Single-Masked-LLM | 49.64 | 58.52 | 5.904 |
| Ministral-3B/8B | CoTrust | 68.22 | 59.49 | 6.168 |
| Ministral-3B/8B | Multi-Masked-LLM | 63.93 | 59.47 | 5.864 |

消融实验显示，多视图脱敏（K=2）相比单视图掩码在 SQuAD EM 上提升 5.04（54.68 vs 49.64），表明多视图多样性对捕获非敏感语义有显著贡献。然而，在 Llama3.2 配对上，CoTrust 的 SQuAD EM（45.63）低于无掩码 LLM（45.87），暗示 SLM 容量限制可能在复杂任务上抵消 LLM 指导的收益。

评估边界方面，论文使用 Qwen3-Max 作为隐私评估器，但未报告置信区间；代码未公开，超参数（如 K 值、掩码工具选择）未详细披露，可复现性受限。隐私保护指标（ESR/PPS）的具体计算方式未在正文中明确，仅提及“强隐私保护”，缺乏量化细节。

## 关联研究分析

从问题动机看，CoTrust 与 PrivacyRestore（P8）同属推理时隐私保护，但路线迥异：PrivacyRestore 通过激活转向在模型内部抑制 PII 输出，而 CoTrust 通过架构隔离将 PII 处理限制在 TEE 内。前者依赖模型内部表示的可控性，后者依赖硬件信任边界。这一差异源于任务特性：PrivacyRestore 适用于云端推理场景，无需硬件支持；CoTrust 则针对高敏感场景，要求 TEE 基础设施。CoTrust 的多视图脱敏是否比 PrivacyRestore 的激活转向更抗推断攻击，论文未提供对比实验，仅声称“隐私保护相当”。

从方法设计看，CoTrust 与 Scalable Extraction（P5）形成攻防对应：Scalable Extraction 通过散度攻击从黑盒模型提取训练数据，而 CoTrust 通过多视图脱敏防止外部 LLM 从推理输入中提取 PII。两者均关注“可提取性”，但前者针对训练记忆，后者针对推理输入。CoTrust 的共识脚手架机制是否能有效抵抗 Scalable Extraction 类攻击，论文未验证，仅假设外部 LLM 为 honest-but-curious。若攻击者能访问 LLM 的中间输出（如候选参考），多视图脱敏的隐私保证是否仍成立，存在疑问。

## 总结

CoTrust 解决的核心矛盾是 TEE 内存限制与 LLM 高容量推理需求之间的冲突，其切入点在于解耦敏感信息访问与高容量推理，让外部 LLM 仅接触脱敏视图，而 TEE 内 SLM 负责隐私敏感实例化。该方法通过多视图脱敏与共识脚手架机制，在 SQuAD EM 上达到 54.68，接近无掩码 LLM 的 51.81（Qwen3 配对），同时保持强隐私保护。其边界在于依赖 TEE 硬件信任假设，且未验证 TEE 被攻破时的鲁棒性；此外，SLM 容量限制在复杂任务上可能抵消 LLM 指导的收益，如 Llama3.2 配对中 CoTrust 性能低于无掩码 LLM。当 TEE 内存进一步缩减至无法运行 3B 参数 SLM 时，CoTrust 的协同框架是否仍能维持隐私-效用平衡，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_2c25ad94d058)