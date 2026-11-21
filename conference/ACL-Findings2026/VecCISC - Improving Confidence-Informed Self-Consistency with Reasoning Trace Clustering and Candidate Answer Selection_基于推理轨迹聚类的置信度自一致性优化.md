# ACL-Findings2026最新论文 ｜VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection ｜基于推理轨迹聚类的置信度自一致性优化

研究机构：美国布兰迪斯大学

作者：James Petullo、Sonny George、Dylan Cashman 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08070)

> 推理时扩展（Test-Time Scaling, TTS）旨在通过增加计算资源提升大语言模型（LLM）的推理准确率，但“二次思考”（Think Twice）范式因需对每条采样轨迹调用批评者模型进行置信度评分，导致推理开销呈线性激增。现有方法如置信度自一致性（Confidence-Informed Self-Consistency, CISC）虽提升了准确率，却未区分冗余或幻觉轨迹，造成算力浪费。本文提出 VecCISC，通过嵌入向量聚类筛选语义等价轨迹，仅对代表样本进行评分，在维持准确率的同时大幅降低 token 消耗。该方法在通用问答任务上验证了有效性，但在高难度数学竞赛任务上的泛化能力存疑。

## 研究背景

当 LLM 面对复杂推理任务时，单次生成的答案往往不可靠，需通过多次采样并聚合结果来提升鲁棒性。这一过程称为自一致性（Self-Consistency, SC），其核心假设是多样推理轨迹能覆盖更大的解空间。然而，SC 的多数投票机制忽略了不同轨迹的质量差异，导致错误答案可能因数量优势而胜出。为弥补这一缺陷，CISC 引入了“二次思考”机制：先由生成模型输出答案与推理轨迹，再由批评者模型（Critic LLM）对每对答案-轨迹进行置信度评分，最终通过加权投票选出最优解。

CISC 显著提升了准确率，但其代价高昂。每条采样轨迹都需触发一次完整的批评者调用，且提示词通常包含长文本，导致 token 消耗随采样数量线性增长。更关键的是，CISC 对幻觉、退化或语义重复的轨迹一视同仁，无论其质量如何均消耗同等计算资源。这种“全量评分”策略在采样预算较大时尤为低效，成为制约 TTS 实际部署的主要瓶颈。

本文切入点在于识别并过滤低价值轨迹。通过引入嵌入模型对推理轨迹进行语义编码，利用聚类算法将语义相似的轨迹归组，仅选取每组中最具代表性的样本送入批评者模型。这一设计将计算资源集中于高质量、多样化的轨迹上，实现了精度与成本的双重优化。

## 核心方法

### 方法参照系

VecCISC 基于 CISC 框架，保留其“采样-评分-加权投票”的主干流程。关键差异在于评分前的轨迹筛选环节：CISC 直接对所有 $n$ 条轨迹调用批评者，而 VecCISC 在评分前增加“嵌入生成-聚类-代表选择”步骤，将评分对象从 $n$ 条缩减至 $K$ 条代表轨迹。

### 嵌入生成与聚类

设计动机：解决 CISC 中冗余轨迹导致的算力浪费。对每条推理轨迹 $r_i$，使用嵌入模型 $Emb$ 生成 $d$ 维向量 $e_i = Emb(r_i)$。随后，按答案 $a$ 将向量分组为 $G_a$，并在每组内应用 KMeans 或层次聚合聚类（HAC）算法，形成 $K$ 个簇。选择 KMeans/HAC 而非 DBSCAN，是因为后者依赖距离阈值 $D$，在高维嵌入空间中阈值敏感且易产生次优簇。聚类过程可表示为：

$$
\mathcal{C}_a = \text{Cluster}(G_a, K)
$$

其中 $\mathcal{C}_a = \{C_1, ..., C_K\}$ 为答案 $a$ 对应的簇集合。该步骤将语义等价的轨迹合并，有效过滤幻觉与退化样本。

### 代表选择与置信度评分

设计动机：确保送入批评者的轨迹最具代表性，避免随机选择引入噪声。对每个簇 $C_i$，计算质心 $u_i$，并选取与质心余弦相似度最高的轨迹 $r_{rep,i}$ 作为代表：

$$
r_{rep,i} = \arg\max_{r \in C_i} \cos(r, u_i)
$$

余弦相似度强调向量夹角而非模长，更适合高维语义空间。随后，仅对代表轨迹 $r_{rep,i}$ 调用批评者模型，生成置信度分数 $s_i$，并通过 softmax 归一化：

$$
p_i = \frac{\exp(s_i / T)}{\sum_j \exp(s_j / T)}
$$

其中 $T$ 为温度超参数。最终答案通过加权投票确定：

$$
\hat{y} = \arg\max_a \sum_{i \in \text{Rep}_a} p_i
$$

该机制将批评者调用次数从 $n$ 降至 $K$，显著降低 token 消耗，同时保留高质量轨迹的置信度信号。

## 实验评估

实验在 AQuA-RAT、CommonsenseQA、ARC-Challenging、MMLU-Pro 和 GPQA 五个数据集上进行，使用 GPT-4o mini、Llama 3.1 8B、Llama 3.3 70B、Qwen 2.5 7B 和 Mistral 7B 五个模型。基线包括 SC 和 CISC，缺失 BoM、Logit Averaging 等并行采样高级基线，限制了与最新 TTS 方法的直接对比。

| 数据集 | 方法 | GPT-4o mini | Llama 3.1 8B | Qwen 2.5 7B | Mistral 7B | Llama 3.3 70B |
|---|---|---|---|---|---|---|
| AQuA-RAT | CISC | 13042.0 | 15480.9 | 11674.3 | 9317.2 | 14448.1 |
| AQuA-RAT | VecCISC (min-centroid) | 8915.4 | 10483.7 | 8562.6 | 7649.6 | 6280.7 |
| CommonsenseQA | CISC | 11086.2 | 10932.4 | 10629.9 | 7691.9 | 13108.5 |
| CommonsenseQA | VecCISC (min-centroid) | 6546.7 | 6612.5 | 8044.7 | 5663.7 | 7748.2 |
| ARC-Challenging | CISC | 12245.4 | 12292.1 | 11602.7 | 8764.0 | 14715.5 |
| ARC-Challenging | VecCISC (min-centroid) | 6365.6 | 8912.3 | 6327.5 | 6734.1 | 9856.5 |
| MMLU-Pro | CISC | 16975.1 | 18496.6 | 16474.9 | 13926.1 | 20810.4 |
| MMLU-Pro | VecCISC (min-centroid) | 10172.4 | 13614.9 | 10059.9 | 11143.5 | 11834.7 |
| GPQA | CISC | 18594.2 | 19659.5 | 17937.0 | 14324.6 | 25235.3 |
| GPQA | VecCISC (min-centroid) | 9577.6 | 15211.4 | 14422.6 | 13260.5 | 22389.4 |

VecCISC + KMeans 平均减少 34.68% 的批评者调用，VecCISC + HAC 减少 30.2%。在 token 消耗上，min-centroid 策略在 60%-68% 的模型-数据集组合中优于随机选择，表明质心最近轨迹确实更具代表性。

消融实验显示，随机轨迹选择（VecCISC random）显著低于 CISC 和 SC，证明聚类筛选的必要性。KMeans 与 HAC 性能接近，但 KMeans 在 AQuA-RAT 上表现更优，HAC 在 CommonsenseQA 上略胜，暗示聚类算法选择需适配任务特性。

评估边界：论文未报告置信区间，数值比较需谨慎；超参数 $K$ 和 $T$ 通过网格搜索确定，缺乏自适应机制；代码未公开，可复现性受限。

## 关联研究分析

从问题动机看，VecCISC 与早期停止（Early Stopping）同属降低推理成本策略，但前者基于语义相似度过滤样本，后者基于置信度阈值停止采样。Early Stopping 依赖模型内部置信度信号，易受校准偏差影响；VecCISC 依赖外部嵌入模型，更稳定但引入额外计算开销。两者均未解决高难度任务中关键推理路径被误删的风险。

从方法设计看，VecCISC 与 Logit Averaging 同为无训练聚合策略，但前者在轨迹级别筛选，后者在 token 级别集成。Logit Averaging 保留细粒度信息，适合开放域任务；VecCISC 聚焦冗余过滤，适合可验证任务。两者均未探索与过程奖励模型（PRM）的结合，可能限制其在复杂规划任务上的表现。

## 总结

VecCISC 解决的核心矛盾是 CISC 中冗余轨迹导致的算力浪费。其切入点在于利用嵌入聚类识别语义等价轨迹，仅对代表样本进行评分，从而在维持准确率的同时降低 token 消耗。实验表明，该方法在通用 QA 任务上平均减少 47% 的总 token 使用，且准确率不低于 CISC。然而，论文未在高难度数学竞赛任务（如 AIME）上验证，聚类是否会导致关键推理路径被误删，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08070)