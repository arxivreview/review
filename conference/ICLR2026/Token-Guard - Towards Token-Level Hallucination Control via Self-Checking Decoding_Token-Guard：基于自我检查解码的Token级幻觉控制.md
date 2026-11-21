# ICLR2026最新论文 ｜Token-Guard: Towards Token-Level Hallucination Control via Self-Checking Decoding ｜Token-Guard：基于自我检查解码的Token级幻觉控制

研究机构：北京邮电大学、新加坡南洋理工大学

作者：Yifan Zhu、Huiqiang Rong、Haoran Luo

论文原文见 [arXiv](https://arxiv.org/abs/2601.21969)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21969)

> 大语言模型在知识密集型任务中常生成看似流畅但事实错误的文本，即幻觉。现有解码方法缺乏显式的Token级验证机制，导致局部错误在推理链中累积传播。Token-Guard通过在生成过程中嵌入基于隐藏状态的混合评分与迭代修正闭环，在解码阶段实时拦截幻觉Token。该方法在多个基准上显著提升了生成准确性，但其全局迭代机制的计算开销与固定阈值策略的鲁棒性仍存疑。

## 研究背景

自回归语言模型通过逐步生成Token构建推理链，每一步的决策依赖于前序Token的上下文状态。当模型在中间步骤生成错误事实时，该错误会作为后续推理的前提，导致逻辑断裂与事实偏差的复合放大。这种错误传播特性要求检测机制必须介入生成过程，而非仅在最终输出后进行事后核查。

解码干预路线旨在不修改模型参数的前提下，通过调整生成策略提升输出可靠性。Chain-of-Thought (CoT) 和 Tree-of-Thought (ToT) 等方法通过多路径探索增加正确解的概率，但缺乏对单个Token事实性的显式验证。DoLa 和 KCTS 引入了层间差异或概率阈值过滤，但仅依赖单一信号源，难以区分语义一致性与概率置信度。Token-Guard 的切入点在于将幻觉检测从“最终答案判断”下沉至“Token级实时验证”，并引入局部修正与全局迭代机制，解决现有解码方法在动态纠错能力上的缺失。

## 核心方法

### 方法参照系

Token-Guard 属于解码干预范式，其标准流程为：候选生成→评分筛选→序列输出。与 CoT 等单次生成方法不同，Token-Guard 在评分环节引入多粒度反馈，并在筛选后增加局部重生成与全局重组步骤，形成闭环控制。

### Token级混合幻觉评分

传统解码方法仅基于模型输出的概率分布选择Token，忽略了语义层面的事实一致性。Token-Guard 在生成步 $t$ 构建潜在环境 $S_t$，存储已接受Token的隐藏状态 $h_j$。对于候选Token $a_t^{[i]}$，计算其与上下文均值的语义一致性，并与模型概率加权融合：

$$
F_{\text{halu}}^{\text{token}}(a_t^{[i]} | s_t) = \lambda \cdot \cos(h_{t^{[i]}}, \bar{h}_{<t}) + (1-\lambda) \cdot P_\theta(a_t^{[i]} | a_{<t}, x)
$$

其中 $\lambda=0.6$ 平衡语义与概率权重。该设计解决了高置信度幻觉问题：即使模型以高概率生成错误Token，若其隐藏状态与上下文语义偏离，评分将低于阈值 $\tau_{\text{token}}=0.4$，从而被剪枝。

### 片段级评分与局部修正

Token级评分仅保证局部连贯，无法捕捉片段内部的逻辑断裂。Token-Guard 将连续通过Token级阈值的Token聚合为片段 $C_k$，计算其加权隐藏状态 $H_k$。片段评分由三部分加权组成：

$$
F_{\text{halu}}^{\text{seg}}(C_k) = \alpha F_{\text{halu}}^{\text{token}}(C_k) + \beta \text{Consistency}(C_k) + \gamma \text{Alignment}(C_k)
$$

其中 $\alpha=0.5, \beta=0.3, \gamma=0.2$。当片段评分介于 $\tau_{\text{seg}}^{\text{low}}=0.55$ 与 $\tau_{\text{seg}}^{\text{high}}=0.75$ 之间时，触发局部修正：定位最低分Token，在其邻域窗口内重新生成，保留下游片段结构。这一机制避免了全序列重生成，在保持全局一致性的同时降低计算开销。

### 全局迭代与弃权机制

片段级修正后，Token-Guard 通过 TF-IDF 和 KMeans 聚类重组推理链，评估全局事实一致性与逻辑连贯性。若全局分数 $F_{\text{global}}(R) < \tau_{\text{global}}=0.7$，则触发迭代修正；若事实与逻辑分数均低于 0.5，则输出“cannot answer”。该弃权机制是防止幻觉传播的最终兜底，体现了可靠性优先于有用性的设计取舍。

## 实验评估

实验在 FinanceBench、RAGTruth、CovidQA、DROP、PubMedQA 和 HaluEval 六个基准上进行，基线包括 CoT、ToT、Guided Decoding 和 Predictive Decoding，但缺失 SAPLMA 等白盒探测方法及 SelfCheckGPT 等黑盒采样基线。

| 方法 | Llama-3.1-8B Avg EM | Llama-3.1-8B Avg F1 | Qwen3-8B Avg EM | Qwen3-8B Avg F1 |
| :--- | :--- | :--- | :--- | :--- |
| BaseModel | 0.15 | 28.29 | 0.22 | 44.25 |
| Chain-of-Thoughts | 0.18 | 34.63 | 0.23 | 45.10 |
| Tree-of-Thought | 0.15 | 33.33 | 0.21 | 45.12 |
| Token-Guard | 0.29 | 51.03 | 0.35 | 53.98 |

Token-Guard 在两个骨干模型上均取得最高平均 F1，较最强基线 ToT 提升 16.3%。在 DROP_nfl 等多步推理任务上增益最大，而在 PubMedQA 等知识密集型任务上提升有限，表明该方法擅长抑制推理链中的逻辑幻觉，但无法弥补模型内部知识的缺失。

| 变体 | DROP_history F1 | RAGTruth F1 | Avg F1 |
| :--- | :--- | :--- | :--- |
| Full Token-Guard | 68.52 | 43.94 | 56.23 |
| w/o Token-Level Scoring | 47.51 | 27.10 | 37.31 |
| w/o Global Iteration | 63.05 | 41.05 | 52.05 |

消融实验显示，移除Token级评分导致 F1 下降 18.92 点，是性能衰减最大的组件，验证了早期Token验证对抑制错误传播的关键作用。移除全局迭代仅导致 4.18 点下降，但 BLEU 分数显著降低，表明全局迭代主要贡献于语言流畅性而非事实准确性。

评估指标涵盖 EM、F1 和 BLEU，但未报告幻觉率或弃权率，无法直接衡量过度拒绝（Over-refusal）风险。实验在单张 NVIDIA A40 GPU 上完成，代码已开源，但全局迭代中 KMeans 聚类数 $K$ 和最大迭代次数 $M_{\text{max}}$ 的敏感性分析缺失，限制了超参数选择的普适性。

## 关联研究分析

从问题动机看，Token-Guard 与 SAPLMA 均利用隐藏状态检测幻觉，但 SAPLMA 是静态分类器，仅在生成后判断整体幻觉概率；Token-Guard 是动态干预机制，在生成中实时修正。SAPLMA 提供信号，Token-Guard 执行动作，二者互补而非竞争。Token-Guard 未对比 SAPLMA，可能因其任务定义不同：SAPLMA 关注检测精度，Token-Guard 关注生成质量，但缺乏横向对比使得解码干预的必要性论证不够充分。

从方法设计看，Token-Guard 的全局迭代采用 TF-IDF 和 KMeans 聚类重组推理链，这与 DoLa 的层间差异过滤形成鲜明对比。DoLa 依赖模型内部层间表示差异，无需额外计算；Token-Guard 引入外部聚类算法，增加了计算复杂度。TF-IDF 基于词频统计，难以捕捉深层语义逻辑，当推理链包含复杂抽象概念时，聚类质量可能下降。这种设计选择是否足以支撑全局一致性评估，论文未提供消融证据。

## 总结

Token-Guard 旨在解决解码过程中Token级幻觉累积导致的推理链逻辑断裂问题。其切入点在于将幻觉检测从概率信号扩展至隐藏状态语义一致性，并通过局部修正与全局迭代实现动态纠错。实验表明，该方法在 Llama-3.1-8B 上平均 F1 达 51.03，较基线提升 16.3%。然而，其固定阈值策略（如 $\tau_{\text{global}}=0.7$）在不同数据集上的适应性未经验证，且全局迭代的计算开销可能违背实时性需求。当面对长尾知识或高度抽象的推理任务时，TF-IDF 聚类能否有效捕捉语义逻辑，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21969)