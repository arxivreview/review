# ACL2026最新论文 ｜NeuReasoner: Towards Explainable, Controllable, and Unified Reasoning via Mixture-of-Neurons ｜神经元混合驱动的可解释可控推理框架

作者：Haonan Dong、Kehan Jiang、Haoran Ye 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9751ab49f853)

> 大语言模型在复杂推理中常陷入计算错误、步骤震荡或过度思考，导致性能与成本双输。现有方法或依赖黑盒奖励模型，或依赖强化学习自发涌现行为，缺乏对内部机制的白盒解释与精确控制。本文切入点在于直接定位中间层神经元簇（Mixture of Neurons, MoN）的激活波动模式，将其作为失败模式的物理信号。通过训练轻量级MLP监控这些信号并触发特殊token进行SFT学习的修正行为，实现了性能与token消耗的双重优化。其价值在于提供了可解释的推理干预路径，但跨骨干模型的泛化性仍存疑。

## 研究背景

当推理模型在关键步骤产生微小偏差时，错误会沿自回归链级联传播，最终导致答案失效。这种“流畅但错误”的现象源于自回归生成的局部最优性无法保证全局逻辑正确性。为缓解此问题，测试时计算扩展（Test-Time Scaling, TTS）通过增加推理时的计算资源来提升性能，但其核心瓶颈在于如何从多个候选解中选出正确解，或如何实时纠正推理错误。这一过程涉及错误定位与路径选择两个子问题，若验证器无法精确定位错误步骤，路径选择将退化为盲目的多数投票。

早期研究依赖思维链（Chain-of-Thought, CoT）提示，但发现中间步骤的错误会级联传播。随着OpenAI o1和DeepSeek-R1等模型的发布，领域重心从单纯的提示工程转向测试时计算扩展。然而，现有方案存在显著局限：过程奖励模型（Process Reward Models, PRMs）如Math-Shepherd依赖文本重新编码，计算开销随采样数量线性增长；结构化框架如Tree of Thoughts (ToT)扩展了探索广度但缺乏对内部机制的解释；自适应长度调整方法如O1-Pruner仅关注token数量，未触及推理逻辑本身的错误。这些方法多为黑盒或灰盒，缺乏对失败模式内部机制的深入分析，且依赖强化学习（RL）导致行为不可控。

本文的切入点在于从白盒视角出发，识别导致不同层级失败模式的关键神经元簇。通过深入分析神经元激活动力学，本文提出MoN概念，将推理失败归因于特定神经元的波动模式。基于此，本文构建了NeuReasoner框架，旨在通过轻量级监控与可控干预，统一解决步骤内错误、步骤间震荡及实例级过度思考问题，实现可解释且可控的推理修正。

## 核心方法

### 方法参照系

本文问题置于“推理验证与纠错”通用流程中，但关键差异在于验证信号来源。传统PRM依赖生成文本的语义评分，而本文直接利用模型中间层FFN与注意力头的神经元激活值作为验证信号，实现了从“文本语义”到“内部机制”的范式转换。

### MoN识别与波动模式分析

设计动机在于解决黑盒模型无法解释失败根源的问题。本文聚焦于中间层（$l^* = L/2$），利用DePass归因算法计算每个神经元$c$对目标token $y_t$ 的独立贡献 $\phi(c, t)$。通过计算不同失败层级下Top-k归因分数的交集，识别出MoN：

$$
N^* = \bigcap_{t \in T} \text{TopK}_{c \in C}(\phi(c, t))
$$

该公式提取了在特定时间窗口内持续主导输出logit的神经元集合。实验发现，步骤内（Intra-step）与实例级（Instance-level）失败主要关联FFN神经元，而步骤间（Inter-step）失败关联注意力头。进一步通过离散傅里叶变换（DFT）分析激活序列 $y_t = |a_t| - \mu$ 的频谱，发现步骤内失败表现为高频能量激增，步骤间失败表现为周期性波动，实例级失败表现为复杂问题下的持续激活或简单问题下的快速崩塌。

### 模式预测与触发训练

设计动机在于将离线的波动分析转化为在线的实时干预能力。本文训练轻量级MLP $f_\ell$ 预测MoN的波动特征（如高频能量比、频谱熵），并在推理时并行监控。当检测到失败模式时，插入特殊token $\langle \nu_\ell \rangle$ 触发SFT学习的“诊断-修正”行为 $B_\ell$。SFT损失函数定义为：

$$
\mathcal{L}_{SFT}(\theta) = -\mathbb{E}_{(u, v') \sim \mathcal{D}'} \sum_{t} \log P_\theta(y_t | u, y_{<t})
$$

其中 $\mathcal{D}'$ 是通过重写原始数据并插入触发token构建的增强数据集。该机制使模型学会在特定神经元信号异常时，自动执行回溯、总结或切换策略等可控行为，而非依赖RL的随机探索。

## 实验评估

实验在六个基准（AIME25, MATH500, GSM8K, GPQA-Diamond, LiveCodeBench等）和六个骨干模型（7B-70B）上进行，对比了包括DAPO、GRPO、Self-Consistency在内的九个基线。基线覆盖了RL-based和Training-free路线，但缺失传统PRM（如Math-Shepherd）的直接对比，限制了与文本验证方法的直接效率比较。

| 模型 | 方法 | AIME25 Pass@1 | AIME25 Token | MATH500 Pass@1 | MATH500 Token |
|---|---|---|---|---|---|
| DeepSeek-R1-Distill-Qwen-7B | Vanilla | 43.3 | 11454 | 91.8 | 92.4 |
| DeepSeek-R1-Distill-Qwen-7B | DAPO | 46.7 | 12307 | 94.2 | 92.9 |
| DeepSeek-R1-Distill-Qwen-7B | NeuReasoner | 47.8 | 95.1 | 94.0 | 51.3 |
| DeepSeek-R1-Distill-Qwen-32B | Vanilla | 58.9 | 93.3 | 93.9 | 60.8 |
| DeepSeek-R1-Distill-Qwen-32B | DAPO | 63.3 | 94.6 | 94.3 | 61.4 |
| DeepSeek-R1-Distill-Qwen-32B | NeuReasoner | 63.3 | 96.3 | 94.2 | 62.3 |

在DeepSeek-R1-Distill-Qwen-7B上，NeuReasoner在AIME25上以47.8%超越DAPO的46.7%，同时token消耗从12307降至95.1（降低22.8%）。在MATH500上，NeuReasoner达到94.0%，token消耗仅为51.3，显著低于DAPO的92.9。这表明神经元干预在提升准确率的同时，有效减少了无效计算。

| 模型 | 方法 | MATH500 Pass@1 | MATH500 Token |
|---|---|---|---|
| DS-R1-Distill Llama-70B | w/o MLPintra | 94.5 | 64.4 |
| DS-R1-Distill Llama-70B | w/o MLPinter | 94.7 | 64.9 |
| DS-R1-Distill Llama-70B | w/o MLPinst | 95.8 | 65.4 |
| DS-R1-Distill Llama-70B | NeuReasoner | 96.3 | 66.2 |

消融实验显示，移除MLPintra导致性能下降最显著，证实步骤内错误是主要失败源。移除MLPinst虽对准确率影响较小，但导致token消耗激增，验证了实例级监控对控制过度思考的必要性。

评估边界方面，论文未报告置信区间，且MLP训练依赖约20条推理轨迹的标注，数据量较小。代码未公开，超参数（如滑动窗口长度k）的敏感性分析仅在附录提及，可复现性受限。

## 关联研究分析

从方法设计看，NeuReasoner与ReProbe均利用内部状态进行验证，但ReProbe侧重探针分类以评估路径正确性，而NeuReasoner侧重动态干预以修正错误。ReProbe的探针是静态的评分器，而NeuReasoner的MLP是动态的触发器，后者通过SFT学习具体的修正行为，实现了从“评估”到“行动”的闭环。这一差异源于任务目标的不同：ReProbe旨在Best-of-N选择，而NeuReasoner旨在单路径内的实时纠错。

从问题动机看，NeuReasoner与DAPO等RL方法在提升推理能力上目标一致，但路径截然不同。DAPO依赖RL奖励信号自发涌现反思行为，导致过程不可控且可能陷入镜像循环；NeuReasoner则通过白盒分析定位失败机制，通过SFT注入可控的修正策略。这种“机制驱动”而非“奖励驱动”的设计，解决了RL方法在开放域任务中因缺乏可验证奖励而失效的问题，但也引入了对神经元激活模式稳定性的依赖。

## 总结

本文核心矛盾在于推理模型失败模式的黑盒性与修正需求之间的冲突。现有方法依赖外部验证或RL自发行为，缺乏对内部机制的精确控制。本文抓住中间层神经元激活波动这一物理信号，通过MoN识别与MLP监控，实现了可解释的失败定位。通过SFT学习特殊token触发的修正行为，NeuReasoner在AIME25上以47.8%超越DAPO，同时token消耗降低22.8%。其边界在于MLP训练依赖少量标注数据，且MoN提取需针对每个骨干模型独立进行，跨模型泛化性未验证。当骨干模型架构或训练数据发生显著变化时，神经元激活的波动模式是否保持稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_9751ab49f853)