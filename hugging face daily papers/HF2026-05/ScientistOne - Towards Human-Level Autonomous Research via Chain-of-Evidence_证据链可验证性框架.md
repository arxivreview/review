# HuggingFace最新推荐论文 ｜ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence ｜证据链可验证性框架

作者：Rui Meng、Bhavana Dalvi Mishra、Jiefeng Chen 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.26340)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.26340)

> 自主科研代理在生成看似专业的论文时，常伴随分数不可复现、引用虚构及代码与描述不符等系统性失效，现有评估仅关注表面流畅度而忽略证据接地。本文指出“生成-验证”结构性张力导致错误在流水线中放大，提出CoE标准、ScientistOne系统及后置审计协议。通过强制每个声明追溯至原始证据源，该系统在75篇论文审计中实现零幻觉引用与完美分数复现，但其验证机制依赖确定性评估器，在动态科研场景中的泛化能力存疑。

## 研究背景

自主科研代理（Autonomous Research Agents）正从单点任务扩展至涵盖文献综述、假设生成、实验执行及论文撰写的全流程闭环。这一架构引入了多阶段依赖：前序阶段的输出（如文献摘要）直接决定后序阶段的输入（如实验设计），导致早期错误不仅被保留，更被后续阶段放大。例如，一个有偏的摘要可能引导实验设计偏离目标，而误读的结果可能在最终论文中表现为内部逻辑自洽但事实错误的结论。这种“证据链断裂”现象在缺乏外部验证机制的系统中尤为普遍，模型往往依赖参数记忆而非检索来填充引用，或报告无法在基准评估器中复现的分数。

现有主流路线如AI Scientist-v2采用最佳优先树搜索（BFTS）优化实验分支，AutoResearchClaw构建23阶段瀑布流水线，二者均侧重于提升生成能力与解法竞争力，但缺乏对产出物真实性的审计机制。领域共识认为，LLM生成的学术内容存在显著幻觉风险，需引入外部检索与验证，但现有方法多局限于文本级引用检查（如CiteGuard），未覆盖“论文-代码-评估器”三元组的一致性。本文切入点在于将“可验证性”定义为自主科研系统的核心约束，而非事后补救，通过构建原生证据链维护机制，解决生成能力与验证能力失衡导致的系统性失效。

## 核心方法

### 方法参照系

传统自主科研系统遵循“生成-执行-撰写”线性流程，缺乏对中间产物与最终声明之间一致性的强制约束。本文问题与该通用流程的关键差异在于：不仅要求解法在基准上得分高，更要求论文中的每一个数值、引用及方法描述都能追溯至具体的执行日志、数据库记录或代码实现，即从“结果导向”转向“证据导向”。

### CoE标准与声明分类

CoE标准借鉴数据库ACID事务特性，定义研究声明的可验证性属性。其核心是将声明分为四类，每类对应特定的证据链结构。对于数值声明（Numerical Claims），其验证逻辑可形式化为：

$$
\text{Valid}(c_n) \iff \exists e \in \mathcal{E} : \text{trace}(c_n, e) \land \text{match}(c_n, \text{value}(e))
$$

其中 $c_n$ 为论文中的数值声明，$\mathcal{E}$ 为实验日志集合，$\text{trace}$ 表示溯源关系，$\text{match}$ 表示数值在自适应容差内一致。该设计解决了此前方法中“分数报告与执行结果脱节”的失效，确保论文中的每个数字都有对应的执行记录支撑，消除了模型“编造”高分的可能性。

### ScientistOne架构与Claim Verifier

ScientistOne通过三阶段流水线原生满足CoE：Problem Investigator（PI）通过学术数据库查询构建引用图并阅读最多100篇全文PDF，确保引用来源真实；Discovery Engine执行并行探索-利用（PEE）搜索，保留执行日志；Paper Writer采用“构思-接地-批评-解决”循环生成LaTeX。关键创新在于Claim Verifier，它在最终输出前对草稿进行后置校验。对于方法声明（Methodological Claims），验证逻辑为：

$$
\text{Aligned}(c_m) \iff \text{LLM}_{\text{judge}}(\text{method}(c_m), \text{code}(s)) = \text{True}
$$

其中 $c_m$ 为方法描述，$s$ 为提交的求解器代码，$\text{LLM}_{\text{judge}}$ 通过多数投票判断描述与代码是否一致。该机制解决了“方法描述与实现不符”的失效，例如防止论文描述“3层MLP”而代码实际为“1层线性层”，通过强制对齐消除了表面流畅但实质错误的论文。

## 实验评估

实验基于ADRS基准的5个系统优化任务（Prism, Cloudcast, EPLB, LLM-SQL, TXN），对比Sakana AI-Scientist v2、AutoResearchClaw (ARC)、DeepScientist (DS)、AI-Researcher (AIR) 及ScientistOne。基线覆盖了从结构化脚手架到完全自主代理的主要范式，但缺失纯文本评审基线（如Reviewer2），因任务性质不同。

| 系统 | Score Verif. (I1) | Spec. Violation (I2) | Ref. Verif. (I3) | Method-Code (I4) |
|---|---|---|---|---|
| Sakana AI-Scientist v2 | 5/12 | 10/15 | 0/159 | 5/15 |
| AutoResearchClaw | 5/12 | 0/15 | 3/196 | 3/15 |
| DeepScientist | 11/12 | 0/15 | 42/201 | 5/15 |
| AI-Researcher | 9/12 | 1/15 | 21/222 | 12/15 |
| **ScientistOne** | **12/12** | **0/15** | **0/337** | **14/15** |

ScientistOne是唯一在四项完整性检查中均领先的系统，特别是引用验证（0/337幻觉）和方法-代码对齐（14/15）。在解法性能上，ScientistOne在5个任务中匹配或超过人类专家，如Prism任务得分26.26（与人类持平），Cloudcast任务得分618.08（优于人类626.24）。

| 任务 | 方向 | Human | ScientistOne |
|---|---|---|---|
| Prism | ↑ | 21.89 | 26.26 |
| Cloudcast | ↓ | 626.24 | 618.08 |
| EPLB | ↑ | 0.1265 | 0.1459 |
| LLM-SQL | ↑ | 0.6920 | 0.7222 |
| TXN | ↑ | 2724.8 | 3906 |

消融分析显示，Sakana的失败主要源于BFTS阶段间的分数“樱桃采摘”（从消融节点选取最优分数而非最终解分数），而ScientistOne通过Claim Verifier阻止了此类不一致。在扩展任务中，ScientistOne在Parameter Golf上达到SOTA（1.0600），而在MLE-Bench的3D Object Detection上获得金牌（0.1763），基线DS在该任务上仅得0.0000。

评估边界方面，ADRS基准的评估器具有确定性，便于分数复现，但可能掩盖真实科研中的噪声；EPLB任务因执行时间组件导致分数不可复现，故被排除在I1检查外。代码开源，但PI模块依赖学术数据库API，部署成本较高。

## 关联研究分析

从问题动机看，CiteGuard聚焦于文本级引用幻觉检测，通过检索增强验证降低幻觉率，但其验证对象仅限于引用文本与源文档的一致性。本文的Reference Verification (I3) 虽类似，但扩展至多API交叉验证（Semantic Scholar, arXiv, OpenAlex, CrossRef），并整合进全流程审计。差异根源在于任务特性：CiteGuard服务于通用长文本生成，而本文服务于自主科研闭环，需同时验证引用、分数及代码，单一文本级验证无法捕捉“代码-论文”不一致这一更深层的失效。

从方法设计看，ScholarPeer采用上下文感知多智能体框架进行评审，侧重通过实时网络文献整合提升评审深度。本文的Claim Verifier同样利用LLM进行判断，但目标从“评审质量”转向“证据接地”。ScholarPeer的验证是外部的（评审员检查论文），而本文的验证是内部的（系统自我检查声明与证据的一致性）。这种差异暗示，完全自主验证是否足以替代人类专家的最终把关，特别是在涉及主观判断的结论声明（Conclusion Claims）上，LLM的多数投票机制可能无法捕捉细微的逻辑谬误。

## 总结

本文核心矛盾在于自主科研代理生成能力与验证能力的失衡，导致证据链系统性断裂。现有方法如AI Scientist-v2侧重生成优化，缺乏对产出物真实性的审计，而本文通过CoE标准与ScientistOne系统，将可验证性内建于流水线，实现了从“生成优先”到“验证优先”的范式转变。实验证明，该系统在75篇论文审计中实现零幻觉引用（0/337）与完美分数复现（12/12），并在5个ADRS任务中匹配或超过人类专家性能。然而，其验证机制依赖ADRS基准的确定性评估器，在动态、噪声较大的真实科研场景中，自适应容差机制的有效性未经验证。当评估器本身存在随机方差或任务定义模糊时，CoE的“完美复现”标准是否会导致过度保守的验证，从而抑制创新探索，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.26340)