# ICLR2026最新论文 ｜STAR: Similarity-guided Teacher-Assisted Refinement for Super-Tiny Function Calling Models ｜超小模型函数调用中的约束蒸馏与相似度强化学习

作者：Jiliang Ni、Jiachen Pu、Zhongyi Yang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03022)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03022)

> 导读 工具增强大语言模型（Tool-Augmented LLMs）在超小模型（<1B参数）上部署时，面临监督微调（SFT）导致的过拟合与直接强化学习（RL）训练不稳定的双重困境。现有“SFT+RL”范式因硬监督压缩了策略熵，使小模型丧失探索能力，而二元奖励在多解任务中信号稀疏。本文提出STAR框架，通过约束知识蒸馏（CKD）保留分布尾部探索性，并结合相似度引导强化学习（Sim-RL）提供连续细粒度奖励。该框架在0.6B规模上刷新了BFCLv3与ACEBench的SOTA，但其对教师模型质量的依赖及跨规模泛化性仍存疑。

## 研究背景

函数调用本质上是条件序列生成问题，模型需根据用户查询与可用函数集合 $F$ 生成结构化调用序列。在超小模型中，参数容量有限导致其极易在SFT阶段记忆特定工具模式而非学习通用推理逻辑，这种过拟合表现为对训练数据JSON格式的僵化依赖，一旦测试集格式变化（如ACEBench的Python风格），性能即发生崩塌。同时，直接应用RL时，小模型初始策略熵过低，导致探索空间受限，训练过程极易陷入局部最优或崩溃。

主流路线试图通过SFT冷启动后接RL精调来缓解此问题，但SFT的硬监督本质上是分布匹配，它强制学生模型模仿教师的高概率token，却忽略了长尾分布中的不确定性信息。这种模式寻求（mode-seeking）特性虽提升了模仿保真度，却以牺牲策略熵为代价，使得后续RL阶段缺乏必要的探索动力。此外，传统RL奖励多为二元成功/失败信号，对于函数调用这类存在多种有效解的任务，过度惩罚了合理的替代方案，阻碍了策略的有效优化。STAR的切入点在于将KD与RL解耦并重新耦合：用软监督的KD替代SFT作为初始化，保留分布多样性；用连续相似度奖励替代二元奖励，提供更丰富的梯度信号。

## 核心方法

### 方法参照系

标准小模型适配流程为“SFT冷启动+RL精调”。本文的关键差异在于以约束知识蒸馏（CKD）替代SFT，并引入相似度引导强化学习（Sim-RL）替代标准二元奖励，形成“CKD初始化+Sim-RL精调”的新范式。

### 约束知识蒸馏（CKD）

设计动机在于解决top-k截断下反向KL散度（RKL）导致的训练崩溃与探索能力丧失。RKL在top-k截断时会对截断集外的token施加不稳定监督，且其模式寻求特性会过度压缩学生分布尾部，降低策略熵。CKD采用前向KL散度（FKL）作为基础，因其对尾部分布无约束，保持稳定性。在此基础上，引入针对“高置信度错误预测”的L1正则项 $\mathcal{L}_{tail}$，仅惩罚学生模型认为可能（在top-m集内）但教师认为无关（在top-k集外）的token。

$$
\mathcal{L}_{CKD} = \mathcal{L}_{FKL}^{top-k} + \lambda_{tail} \sum_{v \in V_m(x) \setminus V_k(x)} |P_S(v|x) - P_T(v|x)|
$$

该公式物理含义为：在保持教师top-k分布覆盖的同时，显式抑制学生模型对教师已排除token的过度自信，从而在不强制长尾概率为零的前提下，平衡稳定性与探索性。

### 相似度引导强化学习（Sim-RL）

设计动机在于解决二元奖励在多解函数调用任务中信号稀疏且惩罚过严的问题。Sim-RL采用GRPO算法，并引入基于输出与真值相似度的连续奖励。奖励函数由格式奖励 $R_{format}$（二元，确保JSON结构正确）和答案奖励 $R_{answer}$（连续，基于IoU原理计算预测调用序列与真值序列的相似度）组成。

$$
R = \begin{cases} -1 & \text{if } R_{format} = 0 \\ R_{answer} & \text{if } R_{format} = 1 \end{cases}
$$

其中 $R_{answer}$ 通过贪心匹配预测调用 $p$ 与真值调用 $g$，计算参数级相似度（字符串用ROUGE-L，数值用精确匹配）。此设计将离散的“对/错”转化为连续的“相似程度”，为小模型提供了更平滑的梯度信号，避免了因微小偏差导致的零梯度问题。

## 实验评估

实验基于Qwen3系列模型，教师为Qwen3-8B，学生为0.6B/1.7B/4B。基线覆盖SFT、FKL、ToolRL、LUFFY及GKD，但缺失纯RL从零训练（如Tool Zero）的对比，限制了与最新RL范式的直接比较。

| 方法 | BFCLv3 Overall | ACEBench Normal |
| :--- | :--- | :--- |
| Base-model (0.6B) | 47.33 | 27.20 |
| SFT | 44.58 | 37.70 |
| FKL | 49.51 | 36.80 |
| ToolRL | 47.35 | 29.40 |
| CKD+Sim-RL (STAR) | **51.70** | **53.00** |

STAR-0.6B在BFCLv3上较基线提升4.37点，在ACEBench上提升25.8点，显著优于SFT和ToolRL。消融实验显示，CKD单独使用在ACEBench上得分39.00，Sim-RL单独使用得分55.00（注：此处Sim-RL指SFT+Sim-RL，原文Table 2中Sim-RL行对应SFT+Sim-RL*，数值为55.00，CKD+Sim-RL为53.00，存在矛盾，需核实原文Table 2中Sim-RL行数值。经查原文Table 2，Sim-RL*行ACEBench为55.00，CKD+Sim-RL为53.00，这与正文“组合提升14点”描述不符，正文称组合比单独应用高14点，若单独Sim-RL为55.00，组合53.00反而下降。此处以表格数值为准，可能正文描述有误或指代不同基线。重新核对Table 2：CKD行ACEBench 39.00，Sim-RL*行55.00，CKD+Sim-RL行53.00。正文称“boosting... ACEBench score by 14 points compared to their individual applications”，若指CKD(39.00)则53.00-39.00=14.00，符合。故Sim-RL单独效果优于组合，提示KD与RL可能存在轻微负迁移或Sim-RL本身已足够强。

| KD策略 | BFCLv3 (w/ RL) | ACEBench (w/ RL) |
| :--- | :--- | :--- |
| CE | 50.41 | 38.90 |
| FKL | 51.46 | 50.00 |
| RKL* | 50.49 | 41.30 |
| CKD | **51.70** | **53.00** |

CKD在两个基准上均优于FKL和RKL，验证了约束项对稳定性的贡献。评估边界方面，论文未报告置信区间，且ACEBench对格式敏感，STAR的高分可能部分源于对格式鲁棒性的提升而非纯推理能力。代码已开源，但超参数细节（如 $\lambda_{tail}$ 具体值）未在正文给出，复现需查阅附录。

## 关联研究分析

从问题动机看，STAR与ToolRL（Qian et al., 2025）同属RL增强路线，但ToolRL依赖SFT初始化，而STAR证明在超小模型上KD初始化更优。根源在于小模型容量有限，SFT的硬监督易导致过拟合，而KD的软监督保留了分布不确定性，为RL提供了更丰富的探索空间。这与大模型上SFT+RL有效的结论形成对比，暗示模型规模是决定初始化策略的关键变量。

从方法设计看，STAR的Sim-RL与GKD（Agarwal et al., 2024）均涉及在线蒸馏，但GKD将KD与RL联合优化，而STAR将其解耦为两阶段。STAR的解耦设计可能更稳定，但牺牲了联合优化的潜在协同效应。Sim-RL的相似度奖励与PROVE（Abdelaziz et al., 2026）的程序化奖励不同，前者基于文本相似度，后者基于逻辑验证。相似度奖励计算成本低，但可能无法捕捉深层逻辑错误，这在复杂多步任务中是否成为瓶颈，论文未给出回答。

## 总结

STAR旨在解决超小模型函数调用中SFT过拟合与RL不稳定的矛盾，通过CKD保留策略熵、Sim-RL提供连续奖励，实现了0.6B模型在BFCLv3 51.70%和ACEBench 53.00%的SOTA。其边界在于Sim-RL单独效果优于组合，提示KD与RL可能存在负迁移，且ACEBench高分可能部分归因于格式鲁棒性而非推理能力。当支持集规模增大或任务复杂度提升时，相似度奖励是否能有效区分深层逻辑错误，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03022)