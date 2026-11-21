# ICLR2026最新论文 ｜TS : TRAINING WITH SPARSEMAX+, TESTING WITH SOFTMAX FOR ACCURATE AND DIVERSE LLM FINE TUNING ｜训练稀疏化与推理平滑化解耦：TS[2] 损失函数设计

研究机构：新加坡国立大学、新加坡南洋理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_6141898)

> 导读 大语言模型后训练中的监督微调（SFT）旨在通过高质量标注数据建立指令遵循能力，但标准交叉熵（CE）损失将概率质量强制推向单点目标，导致输出多样性坍缩与校准度下降，即“对齐税”。现有改进方案如 GEM 框架虽引入熵正则化缓解过拟合，却未能彻底抑制无关尾部概率，且缺乏对“合理多样性”的精确操作定义。本文提出 TS[2] 方法，通过解耦训练与推理的概率映射，使用带尾部抑制项的 Sparsemax+ 损失进行训练，并在推理时切换回 Softmax 以恢复平滑分布。该方法在 Llama-3.1-8B 上实现了 AlpacaEval 胜率 33.12% 与 HumanEval pass@100 87.00% 的双提升，但其理论保证在大词汇表下的尾部质量界较为宽松，实际泛化边界尚待验证。

## 研究背景

SFT 的核心困境源于损失函数的几何特性：交叉熵损失作为严格正确的评分规则，在最小化过程中驱使预测分布趋向 one-hot 向量，这种分布坍缩虽保证了收敛性，却抹除了预训练模型中保留的合理备选路径，使得模型在规划、写作等依赖探索的任务中表现僵化。为理解这一现象，需区分前向 KL 与反向 KL 的优化行为：前向 KL 倾向于均值寻求，可能在数据无支持处分配概率；反向 KL 则模式寻求，集中质量于高置信区域。CE 损失在 Softmax 映射下表现出前向 KL 特征，导致低概率 token 被不当膨胀，而 GEM 等反向 KL 方法虽避免了尾部无谓质量，却未强制无关 token 归零。

主流路线分为两类：一类仅修改解码策略（如 Nucleus Sampling），不触及训练动力学，无法从根本上解决校准问题；另一类修改训练信号，如 GEM 将 SFT 重构为带熵正则化的反向 KL 最小化。然而，这些方法均面临“多样性与校准冲突”的困境：促进多样性往往以牺牲概率校准为代价，且缺乏对“何种多样性是有用的”的明确定义。本文切入点在于指出，指令遵循任务所需的多样性并非在整个词表上均匀扩散，而是应集中在少数语义合理的候选 token 上，同时激进地将明显错误的长尾 token 压至近零。这一“尾部抑制的合理多样性”（TSPD）概念，为设计兼顾准确性与多样性的损失函数提供了理论锚点。

## 核心方法

### 方法参照系

标准 SFT 流程使用交叉熵损失配合 Softmax 映射，其核心假设是训练与推理使用相同的概率映射。本文的关键差异在于解耦这一映射：训练阶段采用 Sparsemax+ 损失以利用其稀疏性几何特性，推理阶段切换回 Softmax 以恢复平滑分布。这种解耦旨在利用 Sparsemax 在训练中的梯度掩码效应实现隐式早停，同时避免其在推理中产生 one-hot 输出导致的多样性丧失。

### Sparsemax+ 损失与尾部抑制

Sparsemax 映射通过投影 logit 向量到概率单纯形，自动识别紧凑的支持集 $S_{sp}(\mathbf{z})$ 并将非支持 token 的概率置零。其损失函数定义为：

$$
\mathcal{L}_{sparsemax}(\mathbf{z}; y) = -z_y + \frac{1}{2} \sum_{j \in S_{sp}(\mathbf{z})} (z_j^2 - \tau(\mathbf{z})^2) + \frac{1}{2}
$$

其中 $\tau(\mathbf{z})$ 为 Sparsemax 阈值。该设计动机在于解决 CE 损失对所有非 gold token 的均匀惩罚问题：Sparsemax 的梯度在支持集外消失，从而保护了合理备选 token 的概率质量，实现了隐式早停。然而，纯 Sparsemax 在收敛后仍趋向 one-hot，且推理时若继续使用 Sparsemax 会丧失多样性。为此，本文引入尾部抑制损失，定义为：

$$
\mathcal{L}_{supp}(\mathbf{z}) = -\log \sum_{i \in S} p_{sf, i}
$$

其中 $S$ 为合理候选集（实践中取 Sparsemax 支持集），$p_{sf}$ 为 Softmax 概率。该惩罚项可视为将 $S$ 合并为“超类”的交叉熵，显式驱动非合理 token 的概率归零。最终 Sparsemax+ 损失为：

$$
\mathcal{L}_{spm+}(\mathbf{z}; y) = \mathcal{L}_{sparsemax}(\mathbf{z}; y) + \alpha \mathcal{L}_{supp}(\mathbf{z})
$$

其中 $\alpha > 0$ 控制抑制强度。这一组合确保了训练时 Sparsemax 选择稳定支持集并阻断尾部梯度流，而抑制项则防止推理时 Softmax 在无关 token 上残留显著概率，实现了“训练分离、推理多样化”的目标。

### 解耦推理的理论保证

推理阶段使用 Softmax 映射 $p_{sf} = \text{softmax}(\mathbf{z})$，其理论依据在于：当 Sparsemax 训练使 gold token 与次优 token 的 logit 差 $\delta_{min} \ge \gamma > 0$ 时，Softmax 在 top-$m$ 头部保留非退化概率，同时尾部质量受控。具体而言，若头部 logit 差有界 $\delta_{(k)} \le B$，则 Softmax 满足 TSPD 条件，尾部累积质量上界为：

$$
\sum_{k>m} p_{sf}(k) \le \frac{K - A_m}{\Omega_{min}} e^{-\gamma}
$$

其中 $A_m = m + (K-m)e^{-\gamma}$，$\Omega_{min} = 1 + (m-1)e^{-B} + (K-m)e^{-\gamma}$。该公式表明，尾部质量随词汇表大小 $K$ 单调递增，当 $K \to \infty$ 时上界趋近 1，意味着理论保证在大词汇表下变得宽松。这一局限性提示，Sparsemax 训练并未从理论上完全保证无关尾部质量的抑制，需依赖实验中的 $\alpha$ 参数调节来弥补理论缺口。

## 实验评估

实验在 Llama-3.1-8B 和 Qwen-2-7B 上进行，使用 UltraFeedback 数据集微调 3 个 epoch，基线包括 CE、CE+WD、NEFT 和 GEM。评估协议采用 Best-of-N 采样（N=32）以衡量模型潜在能力，而非单次贪心解码。

| 方法 | AlpacaEval Win Rate (%) | HumanEval pass@100 (%) | N-gram Diversity | BLEU Diversity | Sent-BERT Diversity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CE | 22.92 | 68.20 | 38.87 | 44.47 | 22.15 |
| GEM | 27.12 | 83.40 | 38.80 | 44.31 | 22.04 |
| TS[2] | 33.12 | 87.00 | 49.70 | 52.10 | 24.98 |

TS[2] 在 Llama-3.1-8B 上 AlpacaEval 胜率 33.12%，较 CE 提升 11.2% 相对值，较 GEM 提升 5.0% 相对值；HumanEval pass@100 达 87.00%，较 GEM 提升 4.3% 相对值。多样性指标全面领先：N-gram 多样性较 GEM 提升 17.0%，BLEU 多样性提升 8.1%，Sent-BERT 多样性提升 10.7%。值得注意的是，TS[2] 的 pass@50 达 82.70%，接近 GEM 的 pass@100（83.40%），表明其样本效率更高，正确解可在更少采样中找到。

消融实验显示，仅解耦（Sparsemax 训练 + Softmax 推理，无抑制项）导致胜率大幅下降但多样性激增，证明抑制项对确保多样性质量至关重要；仅抑制项（CE + 抑制）在两项指标上均失败，表明其需与 Sparsemax 支持集协同作用；统一 Sparsemax（训练推理均用）胜率竞争但多样性低于完整方法，证实推理切换 Softmax 是将 logit 几何转化为可采样分布的关键。

评估边界方面，论文未报告 MMLU 等通用知识基准的具体数值，仅称在 OpenLLM Leaderboard 上评估，无法直接量化对齐税的缓解程度。超参数 $\alpha$ 需针对每个模型架构经验确定，缺乏自动调节机制。代码已开源，但 GPU 内存消耗与训练时间未报告，限制了部署可行性评估。

## 关联研究分析

从问题动机看，TS[2] 与 GEM 均旨在缓解 CE 导致的多样性坍缩，但 GEM 基于反向 KL 最小化加熵正则化，侧重于整体分布平滑，而 TS[2] 基于 Sparsemax 的稀疏性几何，侧重于支持集内的多样性保留与尾部抑制。这一差异源于对“有用多样性”的定义不同：GEM 假设多样性来自概率分布的熵最大化，TS[2] 假设多样性来自合理候选集内的非退化概率。TS[2] 的尾部抑制项解决了 GEM 中无关 token 概率未完全归零的问题，但代价是引入了对支持集 $S$ 的依赖，而 $S$ 的动态变化可能影响训练稳定性。

从方法设计看，TS[2] 与 HPT 等 SFT+RL 混合策略形成对比：HPT 通过 RL 探索突破 SFT 性能上限，TS[2] 则通过改进 SFT 损失函数实现类似探索效果。TS[2] 在 HumanEval 上 pass@100 达 87.00%，显著高于知识库中 HPT 的 42.9%（准确率协议不同，不可直接比），但 TS[2] 未使用 RL，其性能上限是否低于 RL 增强方法尚不明确。TS[2] 的解耦设计可能启发其他任务（如分类）的损失函数设计，但其在复杂推理任务（如 AIME）上的泛化能力未验证，是否能在分布外任务上保持多样性优势，论文未给出回答。

## 总结

TS[2] 针对 SFT 中 CE 损失导致的分布坍缩问题，提出解耦训练与推理映射的方法，通过 Sparsemax+ 损失实现尾部抑制的合理多样性。该方法在 Llama-3.1-8B 上 AlpacaEval 胜率 33.12% 与 HumanEval pass@100 87.00% 上均优于 GEM，证明了多样性与准确性可兼得。然而，其理论保证在大词汇表下尾部质量界宽松，且未报告通用知识基准的具体数值，对齐税缓解程度存疑。当词汇表规模进一步扩大时，Sparsemax 训练的尾部抑制效果是否仍能有效控制无关 token 概率，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_6141898)