# HuggingFace最新推荐论文 ｜On the Step Length Confounding in LLM Reasoning Data Selection ｜步长混淆下的推理数据选择去偏

研究机构：吉林大学、浙江大学

作者：Bing Wang、Rui Miao、Chen Shen 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06834)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06834)

> 长思维链（Chain-of-Thought, CoT）监督微调（Supervised Fine-Tuning, SFT）依赖高质量数据筛选，但现有基于自然性的选择方法存在系统性偏差。这些方法通过计算模型对样本的平均对数概率来排序，却因长步长稀释了低概率首Token的影响，导致错误地偏好冗长而非高质量的推理轨迹。本文提出ASLEC框架，通过丢弃首Token或因果回归去偏来修正这一混淆效应。该方法在多个基准上显著优于现有自然性选择策略，但其去偏效果是否源于数据多样性增加而非单纯去偏，仍存疑。

## 研究背景

当大语言模型（Large Language Models, LLMs）通过SFT习得长CoT推理能力时，训练数据的质量直接决定模型性能。现有数据生成流程通常由强LLM生成大规模推理轨迹，但其中混杂了错误步骤或过度复杂的冗余路径。为筛选高质量子集，研究者引入了基于自然性的数据选择策略，即计算目标LLM对每个样本的平均对数概率，并选取概率最高的样本，假设这些样本更契合模型的内在偏好。

该策略在短文本任务中表现良好，但在长CoT场景下暴露出严重缺陷。自然性指标本质上是对序列中所有Token概率的几何平均，而长CoT中的每个推理步骤首Token往往承担分支探索功能，具有较高熵值和较低概率。当步骤长度增加时，这些低概率首Token在整体序列中的占比下降，导致平均对数概率被非首Token的高概率所主导，从而虚高。这一现象使得自然性选择方法系统性地偏好长步长样本，而非真正高质量或高适应性的样本，形成了步长混淆问题。

本文切入点在于揭示并修正这一混淆机制。通过定量分析证实长步长与高平均对数概率的单调关系，并归因于首Token的低概率稀释效应。在此基础上，提出两种去偏方法：ASLEC-DROP直接丢弃首Token概率，ASLEC-CASL通过因果回归移除首Token比例的混淆影响。这两种方法旨在恢复自然性指标对推理质量的真实反映，避免长步长带来的选择偏差。

## 核心方法

### 自然性选择的方法参照系

现有自然性选择方法的核心是计算序列的平均对数概率 $s_{\text{logp}}$，即目标序列所有Token概率的几何平均。该方法假设高概率样本更契合模型偏好，但忽略了序列内部结构差异。在长CoT中，步骤首Token的低概率被长序列稀释，导致 $s_{\text{logp}}$ 与推理质量脱钩。本文问题与该通用流程的关键差异在于：需显式建模首Token对整体概率的混淆影响，而非直接采用全局平均。

### ASLEC-DROP：首Token概率丢弃

ASLEC-DROP的核心改动在于计算平均对数概率时排除每个步骤的首Token。设推理轨迹 $\mathbf{o}_i$ 被分割为 $L$ 个步骤 $\mathcal{S}_i = \{\mathbf{s}_i^1, \dots, \mathbf{s}_i^L\}$，其中 $\mathbf{s}_i^l$ 为第 $l$ 步。ASLEC-DROP的评分函数定义为：

$$s_{\text{drop}}^i = \frac{1}{\sum_{l=1}^L (|\mathbf{s}_i^l| - 1)} \sum_{l=1}^L \sum_{t=2}^{|\mathbf{s}_i^l|} \log P(\mathbf{s}_i^l_t | \mathbf{s}_i^{<l}, \mathbf{s}_i^l_{<t})$$

该公式仅累加非首Token的对数概率，并除以非首Token总数。设计动机在于消除首Token低概率对整体评分的稀释效应，直接反映模型对推理内容本身的适应性。这一改动解决了自然性方法在长步长样本中因首Token占比下降而虚高评分的问题，使选择标准更聚焦于推理轨迹的内在质量。

### ASLEC-CASL：因果去偏回归

ASLEC-CASL进一步改进ASLEC-DROP，通过因果回归保留首Token的有用信息。将原始对数概率 $s_{\text{logp}}^i$ 分解为线性回归模型：

$$s_{\text{logp}}^i = \beta_1 s_{\text{first}}^i + \beta_2 s_{\text{drop}}^i + \gamma Z_i + \epsilon_i$$

其中 $s_{\text{first}}^i$ 为首Token平均对数概率，$s_{\text{drop}}^i$ 为非首Token平均对数概率，$Z_i$ 为首Token占比（混淆因子），$\epsilon_i$ 为残差。通过普通最小二乘法估计参数后，去偏评分定义为：

$$s_{\text{casl}}^i = s_{\text{logp}}^i - \gamma Z_i$$

该公式通过减去混淆因子 $\gamma Z_i$ 的影响，移除步长对评分的偏差。设计动机在于ASLEC-DROP完全丢弃首Token信息，可能损失分支探索的关键信号；而ASLEC-CASL通过回归分离混淆效应，既保留首Token的语义贡献，又消除其长度偏差。这一改进在数据有限或模型容量受限时尤为有效，因低质量样本的负面影响被更精准地抑制。

## 实验评估

实验在LIMO-v2和AceReason-1.1-SFT两个SFT数据集上进行，使用QwQ-32B、Qwen3-32B、DeepSeek-R1-Distill-Qwen32B和gpt-oss-120b四个源LLM生成数据，并在Qwen3-4B-Base、Qwen3-8B-Base、Qwen3-4B-Instruct和Qwen2.5-7B-Instruct四个目标LLM上评估。基线包括GRACE（基于全局对数概率）和Local LP（基于局部对数概率），均为现有自然性选择方法。实验在AIME24、AIME25、MATH500、OlympiadBench和GPQA五个基准上测试，覆盖数学与科学推理。

| 方法 | Qwen3-4B-Base Avg Acc | Qwen3-8B-Base Avg Acc | Qwen3-4B-Instruct Avg Acc | Qwen2.5-7B-Instruct Avg Acc |
|---|---|---|---|---|
| GRACE | 31.66 | 45.00 | 71.66 | 28.33 |
| Local LP | 36.50 | 53.33 | 83.33 | 46.66 |
| ASLEC-DROP | 44.64 | 52.92 | 72.77 | 40.57 |
| ASLEC-CASL | 47.54 | 56.15 | 76.16 | 45.43 |

ASLEC-CASL在所有目标LLM上均显著优于Local LP，平均准确率提升9.08%。例如，在Qwen3-4B-Base上，ASLEC-CASL的Avg Acc为47.54，较Local LP的36.50提升11.04个百分点。ASLEC-DROP的提升幅度较小，平均提升6.28%，表明因果去偏比简单丢弃首Token更有效。在GPQA科学推理基准上，ASLEC-CASL同样领先，Qwen3-4B-Base的Acc为35.35，较Local LP的29.16提升6.19个百分点。

消融实验显示，ASLEC-CASL选择最高 $s_{\text{casl}}$ 样本优于选择最低 $s_{\text{casl}}$ 样本。例如，在Qwen3-4B-Base上，maxCASL的AIME24 Acc为31.66，minCASL为29.16，差距2.50个百分点。这表明去偏后的评分确实反映了样本质量，而非随机噪声。线性回归参数分析显示，gpt-oss-120b的 $\gamma$ 值为-1.284，远大于其他源LLM，表明其数据受步长混淆影响最严重。$\beta_1$（首Token概率系数）远小于 $\beta_2$（非首Token概率系数），进一步证实首Token对整体概率的贡献应被降低。

评估边界方面，实验未报告置信区间，数值比较需谨慎。代码与数据已开源，但SFT训练细节（如学习率、批次大小）未在正文中详述，可复现性依赖附录。评估协议未控制源LLM的预训练数据量，不同源LLM的数据质量差异可能影响结果可比性。此外，实验未对比基于奖励模型或LLM-as-Judge的选择方法，这些方法可能提供更丰富的质量信号。

## 关联研究分析

从问题动机看，本文与CoT压缩方法（如UCoT、SLAT）存在根本差异。CoT压缩旨在减少推理Token数以降低计算成本，而ASLEC聚焦于SFT数据选择中的质量偏差。UCoT通过解耦压缩器与执行器来平衡Token消耗与准确率，SLAT采用分段级自适应修剪优化推理深度，两者均假设推理轨迹本身是有效的，仅需优化其长度。ASLEC则指出，即使推理轨迹长度合理，自然性选择方法也可能因步长混淆而错误地偏好低质量样本。这一差异源于任务特性：CoT压缩关注推理效率，ASLEC关注数据质量。ASLEC的去偏策略是否适用于CoT压缩中的数据筛选，论文未探索。

从方法设计看，ASLEC-CASL与因果去偏技术（如Udomcharoenchaikit et al., 2022）共享理论基础，但应用场景不同。因果去偏通常用于消除特征间的混淆效应，如年龄对收入预测的影响；ASLEC-CASL将其迁移至NLP数据选择，将步长作为混淆因子。这一迁移的关键挑战在于，步长与推理质量并非完全独立，长步长可能确实包含更多推理细节。ASLEC-CASL通过线性回归假设步长影响是加性的，这一假设在非线性推理过程中是否成立，论文未验证。相比之下，Local LP（Just et al., 2025）通过分段计算对数概率来局部化评估，但未考虑首Token的稀释效应。ASLEC-CASL在Local LP基础上引入因果去偏，保留了分段评估的优点，同时修正了全局偏差。

## 总结

本文要解决的核心矛盾是自然性数据选择方法在长CoT场景下因步长混淆导致的系统性偏差。现有方法无法区分长步长带来的概率虚高与真实推理质量，而ASLEC通过显式建模首Token的混淆效应，提供了去偏解决方案。ASLEC-DROP通过丢弃首Token概率简化计算，ASLEC-CASL通过因果回归保留首Token信息并移除步长影响。实验证明ASLEC-CASL在多个基准上平均提升9.08%，显著优于Local LP。本文的边界在于，去偏效果是否源于数据多样性增加而非单纯去偏，论文未提供消融实验验证。当源LLM的步长分布高度偏斜时，线性回归假设是否仍能有效分离混淆效应，是一个待验证的具体问题。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06834)