# ACL-Findings2026最新论文 ｜SEAD: A Surrogate-free Label-only Membership Inference Attack against Pre-trained LLMs with Semantic-Aware Density ｜语义感知密度：无代理黑盒成员推断攻击

作者：Biao Yi、Jiahao Li、Yiming Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac149aed6e9c)

> 大语言模型（LLM）在预训练中不可避免地记忆敏感数据，成员推断攻击（MIA）是量化这一风险的核心手段，但生产级API通常仅返回生成文本而非完整概率分布，导致依赖Logits的传统攻击失效。现有Label-only攻击依赖代理模型进行概率回归，却因代理选择偏差和巨大的估计误差而可靠性不足。本文提出SEAD，通过直接对目标模型进行蒙特卡洛采样并引入NLI语义加权，在无代理条件下重构Token概率密度。该方法在Label-only设定下刷新了SOTA，但其性能仍显著低于Logits-based攻击，且依赖外部NLI模型，其实际审计效能与计算成本之间的平衡尚存疑。

## 研究背景

当攻击者试图判断某条数据是否被LLM记忆时，通常依赖模型对成员样本赋予更高概率的统计特性。然而，在仅能获取生成文本的Label-only场景下，直接计算困惑度（Perplexity）不可行，必须重构Token概率分布。这一重构过程若依赖外部代理模型，会引入“代理记忆偏差”：代理模型的训练集可能包含目标模型的非成员数据，导致其学到的“语义相似度-概率”映射关系发生扭曲，进而使攻击性能随代理模型的选择剧烈波动。

MIA领域的主流路线长期建立在Logits访问假设之上，如Min-K% Prob和PPL攻击均直接利用模型输出的概率值。随着闭源API的普及，Label-only设定成为现实约束，但现有方案如PETAL通过线性回归映射代理模型概率至目标模型，存在根本性缺陷。实验表明，PETAL在更换代理模型时AUROC从0.59骤降至0.52，且概率估计的ℓ1距离误差高达0.2以上。这种对代理模型训练历史的高度敏感性，使得黑盒审计缺乏稳定的技术基线。本文切入点在于彻底移除代理模型，直接利用目标模型自身的采样行为估计概率，并通过语义感知机制捕捉非精确匹配的记忆信号。

## 核心方法

### 方法参照系

Label-only MIA的标准流程是：获取目标序列 → 估计Token概率 → 计算困惑度 → 阈值判断。与Logits-based攻击的关键差异在于概率估计环节：标准流程直接读取Logits，而Label-only流程必须通过间接手段重构概率分布。本文的核心改动集中在概率估计与密度计算两个环节，旨在消除代理依赖并提升信号鲁棒性。

### 蒙特卡洛概率估计

传统Label-only方法（如PETAL）通过代理模型的线性回归 $\log p(t_i|t_{<i}) = \beta \cdot \text{sim}(t_i, \hat{t}_i) + \alpha$ 来近似目标概率，该设计动机是规避直接访问Logits的限制，但引入了代理偏差。SEAD改为直接查询目标模型，对每个前缀 $t_{<i}$ 进行 $K$ 次蒙特卡洛采样，得到样本集 $\{t_i^{(1)}, ..., t_i^{(K)}\}$。概率估计公式为：

$$
\hat{p}(t_i|t_{<i}) = \max\left(\frac{1}{K}\sum_{j=1}^{K} \mathbb{1}[t_i^{(j)} = t_i], \epsilon\right)
$$

其中 $\epsilon$ 为数值稳定常数。这一改动直接消除了代理选择敏感性，实验显示仅50次采样即可将平均概率估计误差从代理方法的0.2-0.4降低至0.03，实现了数量级的精度提升。

### 语义感知密度计算

仅依赖精确Token匹配的词汇密度（Lexical Density）无法捕捉LLM通过同义词表达记忆的现象（如用“America”替代“USA”）。SEAD引入自然语言推理（NLI）模型计算语义相似度，定义语义感知密度为：

$$
p_{\text{semantic}}(t_i | t_{<i}) = \sum_{t \in V_{\text{sampled}}} \hat{p}(t | t_{<i}) \cdot \text{sim}(t, t_i)
$$

其中 $\text{sim}(t, t_i)$ 由NLI模型判定蕴含关系（Entailment）得出，若 $t_i$ 蕴含 $t$ 则为1，否则为0。该设计动机是解决词汇匹配对语义等价记忆信号的遗漏。相比嵌入相似度，NLI的方向性蕴含关系能更准确区分事实正确性与上下文相似性（如“USA”蕴含“America”但不蕴含“Canada”），从而提供更可靠的成员推断信号。

## 实验评估

实验在WikiMIA和MIMIR基准上进行，对比了PPL、Min-K%、PETAL等Logits-based与Label-only基线。SEAD在WikiMIA上平均AUROC达0.71，显著优于PETAL的0.64，且在18个配置中的17个取得Label-only最佳；在MIMIR上平均AUROC为0.53，与PPL（0.53）持平。

| 模型 | WikiMIA AUROC (SEAD) | WikiMIA AUROC (PETAL) | MIMIR AUROC (SEAD) | MIMIR AUROC (PETAL) |
|---|---|---|---|---|
| Mamba-1.4B | 0.65 | 0.60 | 0.55 | 0.54 |
| OPT-6.7B | 0.62 | 0.60 | 0.51 | 0.50 |
| Pythia-6.9B | 0.67 | 0.62 | 0.56 | 0.52 |
| Llama-13B | 0.81 | 0.62 | 0.57 | 0.53 |
| Llama-30B | 0.79 | 0.63 | - | - |

消融实验表明，语义感知密度相比词汇密度在OPT-6.7B和Pythia-6.9B上提升约3%，在Mamba-1.4B上提升6%。温度系数0.7和50次采样为默认最优配置，增加采样至500次可进一步降低误差至0.01以下，但计算成本线性增长。

评估边界方面，SEAD依赖deberta-xlarge-mnli作为NLI模型，该外部依赖可能引入新的计算瓶颈与偏差；实验仅在A800-80G上进行，未报告大规模部署下的延迟影响；代码已开源，但NLI模型的版本锁定与采样策略的超参敏感性未充分讨论。

## 关联研究分析

从问题动机看，SEAD与PETAL同属Label-only MIA，但PETAL依赖代理模型的线性回归映射，其核心假设是“语义相似度与概率存在线性关系”，而SEAD通过直接采样打破了这一假设，证明了代理模型并非概率估计的必要中介。这一差异源于对“代理记忆偏差”的识别：PETAL未考虑代理模型训练数据与基准数据的重叠导致的分布偏移，而SEAD通过目标模型自采样规避了此问题。

从方法设计看，SEAD与Logits-based的Min-K% Prob（Shi et al., 2024）在密度计算逻辑上相似，均基于Token概率分布，但Min-K%直接读取Logits，而SEAD通过蒙特卡洛采样近似。SEAD引入NLI语义加权是其独特之处，这弥补了纯统计采样对语义等价记忆的盲区。然而，NLI模型的引入是否在所有领域（如代码、数学）均有效，论文未给出跨领域验证，其语义相似度的普适性存疑。

## 总结

SEAD解决了Label-only MIA中代理模型依赖导致的性能不稳定与高估计误差问题，通过蒙特卡洛采样与NLI语义加权，在WikiMIA上实现0.71 AUROC，优于PETAL的0.64。其边界在于性能仍低于Logits-based攻击（如RECALL的0.88），且依赖外部NLI模型，计算成本随采样次数线性增长。当采样次数从50增至500时，误差降低一个数量级，但API调用成本增加10倍，这种精度-成本权衡在实际大规模审计中是否可接受，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ac149aed6e9c)