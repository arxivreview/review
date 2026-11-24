# ICLR2026最新论文 ｜ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity ｜语义与结构双维度的形式化陈述相似度评估

研究机构：上海交通大学

作者：Xiaoyang Liu、Tao Zhu、Zineng Dong 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22246)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22246)

> 自动形式化领域长期面临生成能力与评估手段脱节的问题，现有指标要么忽略语义，要么因证明器脆弱性导致大量假阴性。ASSESS 框架通过引入变换树编辑距离（TransTED Similarity），在算子树结构上叠加语义变换，实现了可复现的连续相似度评分。该工作填补了二元判定与模糊字符串匹配之间的空白，但其评估上限受限于 Lean 4 工具链的覆盖范围及变换集合的完备性。

## 研究背景

形式化数学验证依赖 Lean 等交互式定理证明器，其核心对象是算子树（Operator Trees, OPTs），即由运算符为内部节点、操作数为叶节点构成的层级结构。OPTs 显式编码了运算优先级与操作数依赖关系，是解析形式化语句结构的基础。然而，直接比较 OPTs 的拓扑结构无法捕捉语义等价性，例如 $a+b$ 与 $b+a$ 结构不同但数学含义相同，这要求评估指标必须超越纯语法层面，引入语义对齐机制。

自动形式化旨在将自然语言数学陈述转换为可验证代码，主流方法包括少样本提示、微调及检索增强生成。随着生成模型性能提升，评估瓶颈凸显：字符串指标（如 BLEU）对词汇变体敏感且无视语义；证明基方法（如 BEq）虽能保证语义等价，但受限于证明器能力，对未证明语句无法提供分级反馈，且计算成本高昂。现有评估体系缺乏一种既能捕捉结构差异又能容忍语义等价变换、且具备高效可复现性的连续度量标准。

## 核心方法

### 算子树表示与基础编辑距离

ASSESS 框架的基础是将形式化语句解析为算子树，并计算树编辑距离（Tree Edit Distance, TED）。TED 定义为将树 $T_1$ 转换为 $T_2$ 所需的最小操作成本，操作包括删除、插入和重标记节点，单位成本下 TED 相似度归一化为 $1 - \frac{d_{TED}(T_1, T_2)}{\max(|T_1|, |T_2|)}$。该基线方法仅反映结构差异，无法处理语义等价但结构不同的表达式，导致对正确形式化结果的过度惩罚。

### 变换树编辑距离（TransTED）

为克服 TED 的语义盲区，ASSESS 引入 TransTED Similarity，其核心在于定义一种受语义变换约束的新伪度量 $d^*$。该度量需满足两个公理：一是被 TED 支配，即 $d^*(T_1, T_2) \le d_{TED}(T_1, T_2)$；二是变换单调性，若表达式对 $(ex, ey)$ 可变换为逻辑更强的对 $(eu, ev)$（即 $eu=ev \implies ex=ey$），则 $d^*(OPT(ex), OPT(ey)) \le d^*(OPT(eu), OPT(ev))$。

$$
d^*(T_1, T_2) = \min_{\tau \in \mathcal{T}} d_{TED}(\tau(T_1), T_2)
$$

其中 $\mathcal{T}$ 为允许的 Lean Tactic 变换集合。该公式的物理含义是：通过应用一系列语义保持的 Tactic（如 `rw?`, `apply congrArg`），寻找使两棵树结构差异最小的变换路径。实现上，算法以两语句构成的等式为初始目标，进行启发式搜索，优先选择能降低 TED 的 Tactic，直至证明成功、节点数超限（NLE）或时间超限（TLE）。若变换序列建立语义等价，距离精确为 0；否则返回可计算的上界。这一设计将离散的证明判定转化为连续的距离优化，解决了证明器脆弱性导致的假阴性问题。

## 实验评估

实验基于 EPLA 基准，该基准包含 1,247 对专家标注的形式化语句对，源自 miniF2F 和 ProofNet 数据集，由四个不同模型生成并经 Lean 编译器过滤。基线方法覆盖字符串匹配（Identity, BLEU）、证明基方法（Definitional Equality, BEq）及 LLM 投票（Majority Voting）。

| 指标 | EPLA-miniF2F Accuracy | EPLA-miniF2F Kappa | EPLA-ProofNet Accuracy | EPLA-ProofNet Kappa |
| :--- | :--- | :--- | :--- | :--- |
| Identity Match | 3.69% | 0.03 | 10.25% | 0.07 |
| BLEU | 43.51% | 0.18 | 46.39% | 0.12 |
| Majority Voting | 57.21% | 0.18 | 54.57% | 0.12 |
| Definitional Equality | 45.77% | 0.29 | 46.93% | 0.14 |
| BEq | 49.46% | 0.19 | 60.34% | 0.28 |
| TED Similarity | 69.56% | 0.31 | 64.67% | 0.23 |
| **TransTED Similarity** | **70.16%** | **0.35** | **67.31%** | **0.30** |

TransTED 在两个子集上均取得最高准确率与 Kappa 值，显著优于 BEq 和 BLEU。消融实验表明，变换组件是性能提升的关键，去除此组件后性能退化为 TED Similarity 水平。

评估边界方面，TransTED 依赖 Lean Language Server 解析，仅限 Lean 4 环境，无法直接推广至 Isabelle 或 Coq。Kappa 值 0.35 表明与专家标注的一致性仍属中等水平，提示该指标在复杂语义偏差场景下的判别力有限。代码已开源，实验在单卡 A800 及 32 核 CPU 上完成，除 BEq 外均无需 GPU，具备较高的可复现性。

## 关联研究分析

从问题动机看，ASSESS 与 BEq（Liu et al., 2025a）均旨在解决语义等价性判定，但 BEq 依赖双向可证性，属于“全有或全无”的布尔判定，而 ASSESS 提供连续相似度评分。这一差异源于任务特性：BEq 适用于最终验证，而 ASSESS 适用于生成过程中的中间状态评估或错误定位。BEq 的高假阴性率源于证明器能力瓶颈，而 ASSESS 通过 Tactic 搜索部分缓解此问题，但牺牲了语义等价性的绝对保证，仅保证在变换集合内的局部等价。

从方法设计看，ASSESS 与 GTED（Liu et al., 2025c）同属算子树编辑距离路线，但 GTED 仅支持变量重命名等简单变换，而 ASSESS 引入基于证明论的 Tactic 变换机制。这一改进源于对“结构相似但语义不等价”与“语义等价但结构差异大”两类错误的区分需求。GTED 的简单变换无法处理如 `a ∧ b → c` 与 `a → b → c` 之间的逻辑等价性，而 ASSESS 通过 `rw [propext and_imp]` 等 Tactic 实现此类对齐。然而，Tactic 搜索的终止条件（NLE/TLE）可能导致对复杂定理的评估偏差，即某些语义等价但变换路径过长的语句对被误判为低相似度，论文未对此进行量化分析。

## 总结

ASSESS 针对自动形式化评估中语义与结构信息失衡的矛盾，通过 TransTED 将语义变换融入树编辑距离，实现了可复现的连续相似度度量。该方法在 EPLA 基准上达到 70.16% 准确率与 0.35 Kappa，优于现有基线。其边界在于依赖 Lean 4 工具链及有限 Tactic 集合，Kappa 值中等表明对复杂语义偏差的捕捉能力有限。当变换路径长度超过搜索限制时，TransTED 是否仍能准确反映语义等价性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22246)