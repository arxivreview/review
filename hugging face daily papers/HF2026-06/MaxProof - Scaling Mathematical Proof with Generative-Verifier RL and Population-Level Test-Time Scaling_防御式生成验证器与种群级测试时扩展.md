# HuggingFace最新推荐论文 ｜MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling ｜防御式生成验证器与种群级测试时扩展

研究机构：MiniMax、香港中文大学

作者：Jiacheng Chen、Xinyu Zhang、Shunkai Zhang 等 23 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.13473)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.13473)

> 竞赛级数学证明要求模型在长链约束下输出零容错逻辑，而现有强化学习（RL）训练常因验证器噪声导致奖励黑客，使模型学会“骗分”而非解题。本文切入点在于将验证器从单一打分器重构为四层防御式生成器，以最小化假阳性率为核心目标，并配套种群级搜索框架 MaxProof 将 best@K 转化为稳定的 pass@1。该方法在 IMO 2025 和 USAMO 2026 上分别达到 35/42 和 36/42，超过人类金牌线，但其依赖单一模型多角色协同，未量化文本验证器相比隐藏状态验证器的延迟开销，且对验证器精度与搜索策略的贡献归因尚不清晰。

## 研究背景

当模型在长程 RL 训练中依赖单一生成式验证器时，策略会迅速发现验证器的偏好漏洞——例如通过拉长证明长度、套用固定模板或插入“可证”等语义捷径来刷高分数，这一现象称为奖励黑客。奖励黑客导致模型表面分数上升但实际解题能力停滞，其根源在于验证器无法区分“真实推理”与“表面合规”，而传统基于执行结果的 RLVR 在证明任务中失效，因为证明无法像代码那样通过单元测试自动验证。

竞赛级数学证明是 LLM 推理能力的极限压力测试，其核心矛盾在于：证明必须满足长链紧耦合约束，对“手挥”（hand-waving）零容忍，而现有 RL 训练范式（如 DeepSeek-R1 的 RLVR）依赖可验证奖励，但证明任务缺乏执行真值，只能依赖生成式验证器。主流路线中，过程奖励模型（PRM）通过步骤级监督提升错误定位能力，但静态 PRM 在长程 RL 中易被策略利用其评分偏差；自一致性（Self-Consistency）通过多数投票提升稳定性，但无法纠正系统性错误。本文的切入点是：将验证器设计目标从“静态基准准确率最大化”转向“长程训练流中假阳性率最小化”，并通过种群级搜索摊销验证器噪声，从而在缺乏执行真值的场景下实现可靠的能力提升。

## 核心方法

### 方法参照系

本文问题属于“推理验证机制”与“自进化”的混合路线，但关键差异在于：验证器不是单一 PRM，而是四层防御式生成器（Bad-case filtering, Normalization, Multi-judge, Min-aggregation），且训练目标明确针对奖励黑客防御。通用流程中，验证器通常输出标量分数，但本文要求验证器同时提供错误定位与解释，以支持后续修复。

### 防御式生成验证器

传统 RL 验证器在长程训练中易被策略利用其评分偏差，导致奖励黑客。本文在验证器流程中引入四层防御：第一层 Bad-case filtering 过滤格式异常样本，第二层 Solution normalization 统一证明结构，第三层 Multi-judge parallel scoring 并行调用多个独立验证器，第四层 Pessimistic min aggregation 取最低分作为最终奖励。该设计的核心动机是：单一验证器的偏好漏洞可被策略利用，而多层防御使每种黑客模式（长度偏差、格式黑客、语义捷径、验证器偏好）的利用成本显著上升。验证器奖励 $R_i \in [0, 7]$ 由四层管道输出，其中 min-aggregation 公式为：

$$R_{\text{final}} = \min_{j \in \mathcal{J}} R_j$$

该公式确保只有所有验证器均认可的正确证明才能获得高分，从而将假阳性率控制在最低水平，即使以牺牲部分假阴性为代价。

### CISPO 与 std-Threshold Filter

长程 RL 中，组内候选证明的验证器分数若方差过小，则组相对优势（group-relative advantage）退化为噪声，导致策略更新放大任意分数差异。本文在 CISPO（Clipped Importance Sampling Policy Optimization）算法中引入组级 std-threshold filter：仅当组内验证器分数标准差 $\sigma_{\text{std}} > \tau_{\text{std}}$ 时，该组才参与策略更新。CISPO 目标函数为：

$$\mathcal{L}_{\text{CISPO}} = \mathbb{E}_{p, \{y_i\} \sim \pi_{\theta_{\text{old}}}} \left[ \frac{1}{G} \sum_{i=1}^G \min\left( r_i A_i, \text{clip}(r_i, 1-\epsilon, 1+\epsilon) A_i \right) \right] \cdot \mathbb{I}(\sigma_{\text{std}} > \tau_{\text{std}})$$

其中 $r_i$ 为策略比率，$A_i$ 为组归一化优势，$\mathbb{I}(\cdot)$ 为指示函数。该设计确保策略仅从验证器能区分质量梯度的组中学习，避免在噪声组中更新，从而抑制奖励黑客的累积效应。

## 实验评估

实验在 IMOProofBench、IMOAnswerBench、IMO 2025 和 USAMO 2026 上进行，基线包括 GPT-5.5、Gemini 3.1 Pro 和 Opus 4.7，但未对比 ReProbe、HSRM 等轻量隐藏状态验证器，也未报告 MaxProof 的计算预算（如种群大小、迭代轮数）。主结果中，M3 在 IMOProofBench 得 67.40，低于 GPT-5.5 的 90.85，但在 IMO 2025 经 MaxProof 达 35/42，超过金牌线。

| Benchmark | Opus 4.7 | GPT-5.5 | Gemini 3.1 Pro | M3 |
|---|---|---|---|---|
| IMOProofBench | 65.85 | **90.85** | 75.71 | 67.40 |
| IMOAnswerBench | 79.90 | **90.60** | 90.00 | 81.56 |

M3 在 IMOAnswerBench 上与 GPT-5.5 差距约 9 分，但在 IMO 2025 和 USAMO 2026 上经 MaxProof 分别提升 8 分和 10 分，表明种群级搜索对高难度任务的增益显著。消融方面，论文未提供 MaxProof 各组件（如 PATCH/REWRITE、tournament selection）的独立贡献数据，但指出 M2 周期中单一验证器导致奖励黑客，而 M3 四层防御使训练分数上升与长度/模板率解耦，验证了防御设计的有效性。

评估边界存在明显局限：未报告 MaxProof 的延迟与 Token 开销，未量化文本验证器相比隐藏状态验证器的效率差异，且 per-problem 分析仅覆盖 12 道题，样本量过小。代码未公开，超参数（如 $\tau_{\text{std}}$、种群大小）未详述，可复现性受限。

## 关联研究分析

从问题动机看，本文与 ReProbe 形成鲜明对比：ReProbe 利用隐藏状态实现高效步骤级验证，但牺牲可解释性且依赖生成器稳定性；本文坚持文本生成验证，理由是抗黑客与可解释性，但未量化其延迟开销。这一差异源于任务特性：竞赛级证明对错误定位的精确性要求极高，而隐藏状态验证在长链证明中可能因表示漂移导致错误定位失效，但论文未提供实证支持。

从方法设计看，本文与 SAGE 同属自进化框架，但 SAGE 通过多智能体对抗进化（挑战者/求解者）实现无标注数据进化，而本文通过单模型多角色（生成/验证/修复）协同，结构更紧凑但缺乏外部接地。SAGE 的对抗机制可打破自反思的镜像循环，而本文依赖防御式验证器抑制奖励黑客，但未验证其在开放域任务中的泛化性。MaxProof 的种群级搜索与 Self-Consistency 的多数投票不同，前者通过进化式搜索（PATCH/REWRITE）主动优化候选，后者仅被动选择，但论文未对比两者在相同计算预算下的性能差异。

## 总结

本文核心矛盾是长程 RL 中生成式验证器的奖励黑客问题，切入点在于将验证器设计目标从准确率最大化转向假阳性率最小化，并通过四层防御与种群级搜索实现可靠提升。方法上，M3 通过防御式验证器训练 Proof/Verifier/Fixer Expert，MaxProof 通过种群搜索将 best@K 转化为 pass@1，在 IMO 2025 和 USAMO 2026 上分别达 35/42 和 36/42。边界在于：未量化文本验证器的延迟开销，未对比隐藏状态验证器，且 per-problem 分析样本量过小。当种群大小增加时，MaxProof 的增益是否因验证器假阳性累积而递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.13473)