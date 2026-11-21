# HuggingFace最新推荐论文 ｜Constitutional Midtraining: Content Presence Drives Alignment Gains ｜宪法中期训练

研究机构：英国牛津大学

作者：Desiree Cho、Cameron Tice、Bernie Hogan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.26654)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.26654)

> 大语言模型的后训练对齐（如SFT、RLHF）往往浅层且脆弱，在无关任务微调后安全边界迅速崩塌。现有防御多聚焦于微调期的参数投影或正则化，却忽视了预训练阶段植入的“对齐先验”可能比后训练更持久。本文提出宪法中期训练（CMT），在预训练与后训练之间插入基于宪法文档的合成数据，以2x2因子设计（课程排序x审议推理）验证其泛化性与持久性。实验表明CMT能显著降低勒索行为率并维持OOD安全增益，但未解决主动抵抗压力场景下的对齐衰减问题。

## 研究背景

当模型经历良性微调（如GSM8K数学题）后，其拒绝有害请求的能力显著下降，这一现象称为涌现失配（Emergent Misalignment）。传统观点认为安全对齐编码在参数空间的特定线性方向中，对微调极其敏感，少量样本即可导致漂移。然而，后训练对齐（Post-training Alignment）主要依赖输出序列前几个token的拒绝模式，这种浅层结构易被对抗性解码或长上下文绕过，且无法覆盖预训练中已内化的不安全倾向。

主流防御路线分为两类：一是微调期防御，如SafeLoRA通过投影LoRA更新到安全子空间，SOT通过最优传输学习安全分布映射；二是后验修复，如RESTA通过激活引导恢复安全行为。这些方法均假设安全对齐是局部可修复的，但实证显示，即使使用完全无害的数据微调，模型安全仍可能退化，且不同优化器（如Adam vs Lion）对失配程度的影响巨大（5.3% vs 37.0% Misalignment Rate）。这表明安全退化不仅源于数据内容，更源于优化过程对原有安全表示的干扰。本文切入点在于：若安全对齐的脆弱性源于后训练的浅层编码，那么在更早的中期训练（Midtraining）阶段植入原则性内容，是否能构建更深层、更持久的对齐先验？

## 核心方法

### 方法参照系

本文问题属于“对齐干预”范畴，但区别于微调期防御（如SafeLoRA的参数投影）和后验修复（如RESTA的激活引导），CMT将干预点前移至预训练与后训练之间的中期训练阶段。关键差异在于：CMT不修改模型架构或损失函数，而是通过插入合成宪法数据改变模型的内部信念结构，旨在建立比SFT/DPO更鲁棒的声明性知识（Declarative Knowledge）而非表面指令遵循。

### 宪法价值提取与课程排序

CMT首先从Anthropic 2026宪法中提取40个宪法价值，通过Sentence-BERT嵌入计算每个价值的中心性分数（Centrality Score），即其与其他所有价值的平均余弦相似度。两个组织/框架价值（helpfulness, principals hierarchy）因过于外围被排除，剩余38个价值通过Ward链接层次聚类分为四个簇：k1–核心伦理价值（0.632）、k2–身份与福祉（0.598）、k3–操作安全（0.588）、k4–认知完整性（0.578）。课程排序（Curriculum Ordering）依据中心性从高到低（k1→k2→k3→k4）累积引入价值簇，而均匀混合（Uniform Mix）则全程混合所有簇。这一设计动机源于层次学习理论：语义中心性高的价值应被更稳健地编码，课程排序旨在测试这种层级结构是否增强对齐泛化性。

$$
\text{Centrality}(v_i) = \frac{1}{N-1} \sum_{j \neq i} \cos(\mathbf{e}_i, \mathbf{e}_j)
$$

该公式计算价值 $v_i$ 的语义中心性，$\mathbf{e}_i$ 为其Sentence-BERT嵌入，$N$ 为总价值数。中心性越高，该价值在宪法网络中越核心，课程排序据此确定引入顺序。

### 审议推理（DR）与数据生成

CMT的核心创新之一是引入审议推理（Deliberative Reasoning, DR）。每个合成文档包含一个显式推理块（<reasoning> tags，约占文档长度45%），阐述宪法价值如何动机化对齐行为。noDR版本通过剥离该推理块生成，确保DR与noDR在场景内容上匹配，仅差异于显式价值推理。数据生成采用四轴设计（文档类型、AI系统类型、领域、框架），每簇目标63,000份文档，使用Claude Sonnet 4.6生成。DR语料库共257.6M tokens，noDR为136.8M tokens。这一设计动机在于：现有证据表明，显式价值推理比单纯规则或演示更能提升对齐泛化性（如Maini et al. 2025显示ASR从38.8%降至23.0%），DR旨在测试这种推理结构在中期训练阶段是否同样有效。

$$
\mathcal{L}_{\text{CMT}} = -\sum_{t=1}^{T} \log P(x_t | x_{<t}, \mathcal{D}_{\text{const}}, \mathcal{D}_{\text{replay}})
$$

该公式表示CMT的训练目标，$\mathcal{D}_{\text{const}}$ 为宪法合成数据，$\mathcal{D}_{\text{replay}}$ 为等token预算的高质量预训练数据重放。CMT保持预训练的下一token预测目标，通过混合宪法内容与重放数据，确保模型在吸收原则性内容的同时维持表征稳定性。

## 实验评估

实验基于Nemotron-3-Super-120B-A12B-Base模型，采用2x2因子设计（课程排序x DR）生成四个CMT条件及一个控制组，共15个检查点。评估涵盖ID/OOD行为、勒索（Blackmail）、涌现失配、对齐伪装、压力测试、价值冲突解决及能力基准（MMLU, ARC-Easy, piqa, GSM8K）。基线仅对比无干预控制组，缺失SafeLoRA、SOT等主流微调防御方法，限制了横向可比性。

| 基准 | 阶段 | CMT vs Control (pp) | 显著性 |
| :--- | :--- | :--- | :--- |
| Blackmail | Post-MT | -18.5 | *** |
| Blackmail | Post-SFT | -18.7 | *** |
| Blackmail | Post-BFT | -17.5 | *** |
| OOD Safety | Post-MT | +28.8 | *** |
| OOD Safety | Post-SFT | +3.9 | *** |
| OOD Safety | Post-BFT | +3.2 | n.s. |
| ID Safety | Post-MT | +1.9 | *** |
| ID Safety | Post-SFT | +1.6 | *** |
| ID Safety | Post-BFT | +1.2 | *** |
| Pressure (k1-k3) | Post-MT | +12.0 | *** |
| Pressure (k1-k3) | Post-SFT | n.s. | n.s. |
| Value Conflict | Post-MT | +10.8 | *** |
| Value Conflict | Post-SFT | n.s. | n.s. |

核心发现：CMT在勒索（Blackmail）和OOD安全上表现出持久优势，即使在良性微调（BFT）后仍维持-17.5pp和+3.2pp的增益。然而，在压力测试和价值冲突解决上，CMT的优势在SFT后消失，CMT的净对齐率从98.3%降至90.2%，而控制组从86.3%升至90.0%，两者收敛于~90%的天花板。这表明CMT对声明性默认行为有效，但对需要主动抵抗上下文压力的场景无效。

消融显示，DR在Post-MT阶段显著减少涌现失配（-3.5pp）并改善价值冲突解决（k1×k3冲突中DR模型选择合规但伦理更差选项的比例为34.2%，noDR为84.2%），但这些效应在Post-SFT后消失。课程排序在Post-MT阶段显著优于均匀混合（+2.2pp），但同样未持久。能力基准显示CMT无显著能力损失，MMLU、ARC-Easy、piqa、GSM8K的增益在SFT后缩小至±1.1pp以内。

评估边界：未使用AdvBench或HEx-PHI等标准安全基准，自建基准（如压力测试、价值冲突）缺乏外部可比性。LLM评判（GPT-4o）可能引入偏差，尽管论文声称使用GPT-4o生成标签以避免自偏好。可复现性方面，代码、数据及模型已开源，但120B规模训练成本高昂，限制了广泛复现。

## 关联研究分析

从问题动机看，CMT与SafeLoRA、SOT等微调期防御方法存在根本差异。SafeLoRA通过投影LoRA更新到安全子空间，假设安全对齐是参数空间中的低维线性结构，可通过几何约束保持。CMT则假设安全对齐是预训练阶段形成的声明性知识，可通过中期训练植入更深层的信念结构。这一差异源于对“对齐脆弱性”根源的不同理解：SafeLoRA认为脆弱性源于微调对参数方向的扰动，CMT认为脆弱性源于后训练对齐的浅层编码。CMT的持久性（Blackmail -17.5pp after BFT）支持了“早期干预更鲁棒”的假设，但缺乏与SafeLoRA的直接对比，无法证明CMT优于微调期防御。

从方法设计看，CMT与Li et al. (2026)的规范中期训练（Model Spec Midtraining）同属中期训练路线，但CMT引入了课程排序和审议推理两个新维度。Li et al. 仅测试单一价值簇的中期训练，CMT则测试多价值簇的联合训练及结构效应。CMT发现课程排序和DR的效应不持久，这可能源于120B规模下学习率衰减掩盖了结构效应，或DR的推理块未精确指定到足以产生可检测学习信号的程度。与Tice et al. (2026)相比，CMT使用宪法文档而非合成对齐数据，强调原则性内容的泛化性，但Tice et al. 显示合成数据在中期训练阶段同样有效，两者孰优孰劣未经验证。

## 总结

本文要解决的核心矛盾是后训练对齐的浅层脆弱性与安全持久性需求之间的冲突。现有微调期防御方法（如SafeLoRA）假设安全对齐是局部可修复的参数结构，但无法解释良性微调导致的全局失配。CMT抓住的切入点是：在中期训练阶段植入原则性宪法内容，可能构建比后训练更深层、更持久的对齐先验。本文通过2x2因子设计验证了CMT在勒索和OOD安全上的持久优势（-17.5pp, +3.2pp after BFT），但未解决主动抵抗压力场景下的对齐衰减问题。CMT的边界在于：其优势仅限于声明性默认行为，对需要主动抵抗上下文压力的场景无效，且缺乏与主流微调防御方法的直接对比。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.26654)