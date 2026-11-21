# ICLR2026最新论文 ｜Distillation of Large Language Models via Concrete Score Matching ｜具体分数蒸馏（CSD）：突破Logit平移不变性约束的LLM知识迁移

研究机构：韩国科学技术院

作者：Yeongmin Kim、Donghyeok Shin、Mina Kang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25837)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25837)

> 大语言模型知识蒸馏旨在将教师模型的参数化知识迁移至学生模型以缓解部署成本，但现有方法多依赖Softmax后的概率分布，导致教师Logits中的细微差异被平滑掩盖，且直接Logit蒸馏因缺乏平移不变性而限制了最优解空间。本文切入点在于利用能量基模型中的分数匹配理论，构建一种对Logit常数偏移免疫的离散蒸馏目标。具体做法是提出具体分数蒸馏（Concrete Score Distillation, CSD），通过匹配师生模型间词汇对之间的相对Logit差值，在保持线性计算复杂度的同时扩展了解空间。该方法在指令跟随任务上优于主流概率匹配基线，但其对长链推理任务的有效性及与On-policy策略的深层耦合机制尚存疑。

## 研究背景

自回归语言模型通过Softmax函数将Logits转换为概率分布，这一过程在数学上保证了概率归一化，但在信息论层面造成了严重的信息损失。当教师模型在两个低概率Token上的Logit值存在显著差异（如-1与-4）时，Softmax后的概率值可能几乎相同，导致学生模型无法从教师分布中捕获这些细微的相对偏好。这种平滑效应在大词汇量模型中尤为突出，因为绝大多数Token的概率接近于零，使得基于概率的散度度量（如KL散度）对长尾知识的监督信号极度稀疏。

传统知识蒸馏范式主要聚焦于最小化师生概率分布间的散度，如前向KL散度（Forward KL, FKL）或反向KL散度（Reverse KL, RKL）。尽管RKL在避免学生模型过度分配低概率区域方面表现更好，但其本质仍受限于Softmax的非线性变换。直接Logit蒸馏（Direct Logit Distillation, DLD）试图绕过Softmax，直接匹配Logits，但其最优解要求师生Logits完全一致，忽略了Softmax的平移不变性——即Logits整体加上常数后概率分布不变。这种刚性约束在教师与学生存在巨大容量差距时，迫使小模型去拟合大模型无法复现的绝对能量尺度，从而限制了学生模型在有限参数下逼近教师分布的能力。

## 核心方法

### 方法参照系

本文问题属于分布对齐路线，标准流程是选择散度度量 $D$ 并最小化师生概率分布差异 $\min_\theta \sum_t D(q_\theta(\cdot|c, y_{<t}), p_T(\cdot|c, y_{<t}))$。与通用流程的关键差异在于，本文不直接操作概率空间，而是回归到Logit空间，并引入分数匹配（Score Matching）理论来解耦概率归一化约束，从而在Logit层面建立更灵活的匹配目标。

### 具体分数蒸馏目标

针对DLD缺乏Logit平移不变性的缺陷，本文引入具体分数（Concrete Score）概念。具体分数定义为 $s_\theta(y) := \frac{q_\theta(y)}{\sum_{x \in V} q_\theta(x)}$，它刻画了当前状态相对于其他状态的概率比率，且无需计算配分函数。直接优化具体分数匹配目标会导致训练不稳定，因为当分母趋近于零时，似然比 $q_\theta(y_t)/q_\theta(x)$ 会发散。为解决此问题，本文对具体分数取对数，得到CSD目标：

$$
\mathcal{L}_{CSD}(\theta; p_T, w) = \mathbb{E}_{(c,y) \sim \mathcal{D}} \left[ \sum_{t=1}^L \sum_{y_t \in V} \sum_{x \in V} w(y_t, x) \left( \log \frac{q_\theta(y_t|c, y_{<t})}{q_\theta(x|c, y_{<t})} - \log \frac{p_T(y_t|c, y_{<t})}{p_T(x|c, y_{<t})} \right)^2 \right]
$$

该公式的物理含义是：最小化师生模型在任意词汇对 $(y_t, x)$ 上的对数概率比之差。通过取对数，Logit的差值 $\log q_\theta(y_t) - \log q_\theta(x)$ 等价于 $f_\theta[y_t] - f_\theta[x]$，从而将目标转化为Logit相对差的MSE损失。这一设计使得目标函数对Logits的整体平移不变，即若 $f_\theta[y_t] = f_T[y_t] + C$ 对所有 $y_t$ 成立，则 $\mathcal{L}_{CSD}=0$，而DLD此时不为零。这直接解决了DLD因刚性匹配绝对Logit值而导致的解空间受限问题，允许学生模型在保持概率分布一致的前提下，灵活调整其内部能量尺度。

### 线性梯度计算与权重设计

CSD目标涉及对词汇集 $V$ 的双重求和，直接计算复杂度为 $O(|V|^2)$，在大词汇量LLM中不可行。本文通过分解权重函数 $w(y_t, x) = w_1(y_t)w_2(x)$，证明了梯度可在 $O(|V|)$ 时间内计算。具体而言，定义加权平均Logits $\bar{f}_{\theta[w_1]} = \sum_{y_t \in V} w_1(y_t) f_\theta[y_t]$，则归一化Logits $\tilde{f}_{\theta[w_1]}[y_t] = f_\theta[y_t] - \bar{f}_{\theta[w_1]}$。梯度公式为：

$$
\nabla_\theta \mathcal{L}_{CSD} = \sum_{y_t \in V} \left( w_1(y_t) (\tilde{f}_{\theta[w_2]}[y_t] - \tilde{f}_{T[w_2]}[y_t]) + w_2(y_t) (\tilde{f}_{\theta[w_1]}[y_t] - \tilde{f}_{T[w_1]}[y_t]) \right) \nabla_\theta f_\theta[y_t]
$$

该设计动机在于，通过 $w_1$ 和 $w_2$ 的灵活选择，CSD框架可以实例化出具有模式寻求（Mode-seeking）或模式覆盖（Mode-covering）特性的损失函数。例如，当 $w_1$ 和 $w_2$ 均设为教师概率时，CSD表现出类似RKL的模式寻求特性；当设为均匀分布时，则趋向于模式覆盖。这种参数化设计使得CSD不仅是一个具体的损失函数，更是一个包含多种散度度量的设计空间，允许根据任务需求动态调整拟合难度。

## 实验评估

实验在GPT-2、OpenLLaMA、Gemma、Qwen2.5和Gemma2等骨干网络上进行，涵盖指令跟随、摘要、数学推理和翻译任务。基线包括KL、RKL、GKD、DistiLLM、DLD等主流方法，覆盖了概率匹配和Logit匹配两条路线，但未包含跨分词器对齐方法（如SRA）或专门针对MoE架构的蒸馏策略。

| 方法 | Dolly Eval | Self-Instruct | Vicuna Eval | Super-NI | UnNI | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Teacher (GPT-2-1.5B) | 27.00 | 14.07 | 16.31 | 26.46 | 31.10 | 22.99 |
| KL | 23.52 | 10.02 | 14.57 | 16.76 | 18.55 | 16.68 |
| RKL | 24.26 | 11.19 | 15.80 | 20.17 | 22.99 | 18.88 |
| GKD | 24.10 | 11.40 | 16.02 | 20.28 | 22.55 | 18.87 |
| DLD | 24.53 | 12.19 | 15.63 | 23.37 | 24.28 | 20.00 |
| CSD (Ours) | **24.94** | 12.06 | 15.78 | **24.60** | **25.88** | **20.65** |

在GPT-2-1.5B到0.1B的蒸馏任务中，CSD在平均ROUGE-L上达到20.65，优于DLD的20.00和RKL的18.88。特别是在Super-NI和UnNI基准上，CSD分别以24.60和25.88显著领先，表明Logit相对差匹配在捕捉长尾知识方面具有优势。

| 方法 | Dolly Eval | Self-Instruct | Vicuna Eval | Super-NI | UnNI | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ImitKD + DLD | 25.82 | 13.64 | 17.55 | 25.51 | 29.07 | 22.32 |
| ImitKD + CSD | **27.14** | **14.85** | 16.88 | 26.28 | **30.43** | **23.12** |
| DistiLLM + CSD | 26.77 | 13.96 | 17.05 | **26.29** | 29.56 | 22.72 |

消融实验显示，CSD与On-policy技术（如ImitKD）结合后，在GPT-2-0.3B学生模型上平均ROUGE-L达到23.12，较DLD基线的22.32提升0.8。这表明CSD的损失函数设计与采样策略具有正交性，能够独立贡献性能增益。然而，在OpenLLaMA-7B到3B的蒸馏中，CSD（29.03）仅略高于DistiLLM+SRKL（28.31），优势幅度缩小，暗示在更大规模模型上，Logit平移不变性的收益可能被其他因素稀释。

评估协议主要依赖ROUGE-L和准确率，缺乏对生成多样性的直接量化指标，尽管论文声称CSD位于多样性-保真度权衡的前沿。代码已开源，但论文未报告具体的GPU训练时间和内存占用，仅提及梯度计算为线性时间。

## 关联研究分析

从问题动机看，CSD与MiniLLM均旨在解决概率匹配中的长尾信息丢失问题，但路径截然不同。MiniLLM基于反向KL散度（RKL），通过策略梯度优化促使学生聚焦于教师高概率区域，其核心假设是概率空间的散度足以捕捉知识。CSD则指出Softmax平滑导致概率空间信息不足，直接回归Logit空间，通过匹配相对差值来保留长尾信息。这一差异的根源在于对“知识载体”的定义：MiniLLM认为概率分布是知识的充分统计量，而CSD认为Logits中的相对结构才是更本质的知识形式。在Dolly Eval上，CSD（24.94）优于MiniLLM（24.6），支持了Logit级匹配在短文本指令任务上的有效性，但在GSM8K等复杂推理任务上，CSD（25.78）低于针对微调模型优化的TuneShift-KD（30.70），这暗示Logit相对差匹配在需要精确逻辑链的任务中可能缺乏足够的约束力。

从方法设计看，CSD与GKD（Generalized Knowledge Distillation）在框架上具有互补性。GKD统一了散度度量并引入在线策略采样，但其散度仍定义在概率空间。CSD则提供了另一种散度设计空间，且其权重函数 $w_1, w_2$ 可独立于采样策略调整。实验表明，CSD与GKD结合（GKD + CSD）在GPT-2-0.1B上平均ROUGE-L为19.81，与ImitKD + CSD（20.73）相比略低，说明On-policy采样对CSD的性能增益更为显著。这一发现暗示，CSD的Logit相对差匹配特性可能更依赖于学生模型自生成轨迹上的分布对齐，而非离线数据上的静态匹配。

## 总结

本文要解决的核心矛盾是Softmax平滑导致的教师知识丢失与DLD解空间受限之间的冲突。CSD通过引入具体分数匹配，将蒸馏目标从概率散度转化为Logit相对差匹配，利用对数变换解决训练不稳定性，并通过权重分解实现线性梯度计算。实验证明，CSD在指令跟随任务上优于RKL和DLD，平均ROUGE-L提升约0.6-1.0。其边界在于，在大规模模型（如OpenLLaMA-7B）和复杂推理任务（如GSM8K）上，CSD的优势幅度缩小甚至落后于特定架构优化方法，且缺乏对生成多样性的直接量化评估。当学生模型规模扩大至7B以上时，Logit平移不变性带来的解空间扩展是否仍能转化为显著的性能增益，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25837)