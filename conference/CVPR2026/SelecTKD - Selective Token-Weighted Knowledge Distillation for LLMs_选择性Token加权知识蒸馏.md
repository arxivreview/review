# CVPR2026最新论文 ｜SelecTKD: Selective Token-Weighted Knowledge Distillation for LLMs ｜选择性Token加权知识蒸馏

作者：Haiduo Huang、Jiangcheng Song、Yadong Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24021)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24021)

> 大语言模型知识蒸馏旨在将教师模型能力迁移至学生模型，但传统方法对所有Token施加均匀损失，导致学生被迫模仿教师的高熵预测，在师生容量差距大时引入噪声并 destabilize 优化。现有研究多聚焦于散度度量（如KL/RKL）或数据策略（On/Off-policy）的改进，却忽视了“哪些Token值得学习”这一监督信号质量的核心问题。SelecTKD提出一种即插即用的选择性Token加权框架，通过借鉴推测解码的“提议-验证”机制，仅对师生对齐度高的Token施加全量损失，从而过滤噪声信号。该方法在指令跟随、数学推理及代码生成任务上均优于强基线，但其有效性高度依赖于教师模型的置信度分布，且在大规模模型上的泛化能力尚存疑。

## 研究背景

自回归语言模型在生成序列时，每一步预测都依赖于前序Token。当教师模型对某Token的预测分布呈现高熵（即不确定性高）时，若学生模型被强制拟合该分布，会引入大量噪声，这种现象称为曝光偏差（Exposure Bias）的微观表现。为缓解此问题，研究界主要沿两条路径演进：一是优化散度度量，如MiniLLM采用反向KL散度（Reverse KL, RKL）以聚焦教师高概率区域；二是调整数据策略，如GKD通过在线策略采样让学生模型在自生成轨迹上学习。然而，这些方法均假设所有Token的监督信号同等重要，未区分教师预测的置信度差异。

SelecTKD的切入点在于重新定义蒸馏的核心问题：从“如何计算散度”转向“在哪里应用监督”。作者指出，在师生容量差距显著的场景下，教师的高熵预测往往包含大量噪声，均匀施加损失会导致学生模型过拟合于这些噪声，进而损害泛化能力。因此，SelecTKD引入Token级验证机制，动态筛选出师生分布对齐度高的Token，仅对这些Token施加全量损失，而对低置信度Token进行降权或掩码。这一设计旨在通过过滤噪声信号，稳定优化过程并提升学生模型在复杂推理任务上的表现。

## 核心方法

### 方法参照系

标准知识蒸馏流程中，学生模型在每一步 $t$ 计算与教师模型在相同上下文下的Token级分布散度，并累加至总损失。该流程的核心假设是教师分布在所有位置均提供有效监督信号。SelecTKD的关键差异在于引入一个动态验证权重 $V_t$，该权重根据师生分布的对齐程度决定当前Token的损失贡献，从而打破“均匀监督”的假设。

### 提议-验证机制

SelecTKD的核心创新在于借鉴推测解码（Speculative Decoding）的“提议-验证”逻辑，将其从推理加速迁移至训练信号筛选。在每一步 $t$，学生模型首先提议一个Token（Greedy Top-$k$ 变体中为 $\hat{y}_t = \arg\max_y q_\theta(y)$），随后教师模型验证该Token是否在其Top-$k$ 候选集中。验证权重 $V_t$ 定义为：

$$ V_t = \beta + (1-\beta) \cdot \mathbb{I}(\hat{y}_t \in \text{Top}_k(p_t)) $$

其中 $\beta$ 为拒绝Token的权重，$\mathbb{I}$ 为指示函数。该设计解决了传统方法中教师高熵预测导致学生过拟合噪声的问题，通过仅保留师生对齐度高的Token，实现了隐式课程学习。

### 非贪心验证与TAR

为进一步提升鲁棒性，SelecTKD提出非贪心Spec-$k$ 变体，学生模型从自身分布中采样 $k$ 个候选Token，教师模型通过拒绝采样测试接受每个候选。若至少一个候选被接受，则 $V_t = 1$，否则 $V_t = \beta$。该机制通过Token接受率（Token Acceptance Rate, TAR）量化师生对齐程度，TAR定义为：

$$ \text{TAR} = \mathbb{E}_t[\mathbb{I}(V_t = 1)] $$

理论证明表明，在温和假设下，SelecTKD训练过程中TAR单调递增，反映了学生模型与教师分布的对齐程度逐步提升。这一特性确保了训练过程的稳定性，避免了传统方法中因噪声信号导致的优化震荡。

## 实验评估

实验在8块NVIDIA A100 80GB GPU上进行，使用LoRA微调，涵盖指令跟随（AlpacaEval, Evol-Instruct, UltraFeedback）、数学推理（GSM8K, MATH）及代码生成（HumanEval, MBPP）任务。基线包括Vanilla KD、SeqKD、GKD、DistiLLM-2等主流方法，但缺失MiniLLM（RKL代表）及AMiD（自适应散度代表）的对比。

| 任务 | 基线 (DistiLLM-2) | SelecTKD | 提升 |
| :--- | :--- | :--- | :--- |
| GSM8K (Qwen2-Math-7B→1.5B) | 76.27 | 77.82 | +1.55 |
| MATH (Qwen2-Math-7B→1.5B) | 35.58 | 36.89 | +1.31 |
| HumanEval (DS-Coder-6.9B→1.3B) | 59.92 | 61.72 | +1.80 |
| MBPP (DS-Coder-6.9B→1.3B) | 75.66 | 76.27 | +0.61 |

SelecTKD在所有任务上均优于DistiLLM-2，尤其在数学推理任务上提升显著，表明选择性监督对复杂逻辑推理的有效性。

消融实验显示，非贪心Spec-$k$ 变体（$k=5, \beta=0.01$）表现最优，平均胜率43.33%，高于贪心Top-$k$ 的43.09%。$\beta$ 值对性能影响较小，$\beta=0.01$ 略优于 $\beta=0$，表明轻微保留拒绝Token信号有助于正则化。

评估边界方面，论文未报告置信区间，且仅在9B教师模型上验证，未测试更大规模模型。代码未公开，但超参数（$k=5, \beta=0.01$）及训练细节（2 epochs, AdamW）已披露，可复现性中等。

## 关联研究分析

从问题动机看，SelecTKD与GKD均关注训练-推理分布不匹配，但GKD通过在线策略采样解决序列级偏差，而SelecTKD通过Token级验证解决信号级噪声。这一差异源于任务特性：GKD适用于长链推理，而SelecTKD更适用于高熵预测频繁的短文本生成。SelecTKD未探索序列级偏差与Token级噪声的交互作用，可能在长序列任务中效果受限。

从方法设计看，SelecTKD与DistiLLM-2同属分布对齐路线，但DistiLLM-2通过非对称散度（SKL/SRKL）匹配数据类型，而SelecTKD通过Token筛选优化信号质量。SelecTKD主张散度选择次要，Token筛选主要，挑战了领域内对散度几何的过度关注。然而，SelecTKD未与MiniLLM等RKL代表方法进行同骨干对比，无法直接验证其“散度次要”论断的普适性。

## 总结

SelecTKD旨在解决知识蒸馏中教师高熵预测导致的学生过拟合噪声问题，其切入点在于通过Token级验证机制筛选高置信度监督信号，而非优化散度度量或数据策略。该方法在指令跟随、数学推理及代码生成任务上均优于DistiLLM-2等强基线，GSM8K Pass@1从76.27提升至77.82，HumanEval Pass@1从59.92提升至61.72。然而，其有效性依赖于教师模型的置信度分布，且在9B以上模型上的泛化能力未验证。当教师模型规模扩大至70B以上时，Token接受率TAR的单调递增特性是否仍成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24021)