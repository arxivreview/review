# ACL2026最新论文 ｜Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors ｜编译激活引导至静态权重：基于零空间约束的隐蔽后门注入

研究机构：浙江大学

作者：Rui Yin、Tianxu Han、Naen Xu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12359)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_894eff7653bf)

> 供应链攻击者需在分发模型时植入后门，但现有权重编辑方法仅能强制模型输出“同意”前缀，无法保证后续生成持续有害，导致攻击失效。STEEREDIT 将动态激活引导中的合规方向向量编译为静态权重更新，通过零空间投影确保良性输入下后门休眠。该方法在多个安全对齐大语言模型上实现了高触发成功率与低效用损失，但其绝对攻击成功率受限于生成式任务的复杂性，且未验证对复杂语义触发器的泛化能力。

## 研究背景

安全对齐大语言模型（Safety-Aligned LLMs）在拒绝有害请求时，其内部激活状态存在可区分的线性方向。激活引导（Activation Steering）技术利用这一特性，通过在推理时向隐藏状态添加合规方向向量来改变模型行为，但该方法需修改推理管道且不具备持久性，无法作为静态后门分发。知识编辑（Knowledge Editing, KE）技术如 ROME 和 MEMIT 将 MLP 层视为键值记忆，通过低秩权重更新实现持久化修改，但现有基于 KE 的后门攻击（如 JailbreakEdit）仅优化 Token 级映射，强制模型生成“Sure”等肯定前缀。

这种 Token 级映射存在根本缺陷：模型可能在初始解码步骤中表现出表面合规，但在后续步骤中因完整的安全机制主导而回退至拒绝行为，导致后门失效。这一“安全回退”现象使得现有权重编辑后门在生成式任务中可靠性不足。STEEREDIT 的切入点在于将后门目标从表层 Token 约束转向内部表示操纵，通过编译合规方向向量至权重，实现触发器门控的持续有害生成，同时利用零空间约束保证隐蔽性。

## 核心方法

### 方法参照系

本文问题属于后验权重编辑后门注入，标准流程为定位触发器相关模块并计算权重更新以映射触发器至目标响应。本文与通用流程的关键差异在于：不优化 Token 概率分布，而是优化内部激活空间中的行为方向，并引入零空间约束以消除对良性输入的干扰。

### 合规方向提取与零空间投影

设计动机在于解决 Token 映射无法维持有害生成的问题，通过操纵内部表示方向而非表层输出，确保模型在触发后持续偏离安全对齐路径。首先，利用差异均值（Difference-in-Means, DiM）方法提取合规方向 $z_{comp}$，即良性输入与有害输入隐藏状态质心之差的归一化向量：

$$ z_{comp} = \frac{\mu_b - \mu_h}{\|\mu_b - \mu_h\|_2} $$

该向量捕捉了区分合规与拒绝行为的主方向。为保持隐蔽性，计算干净激活矩阵 $K_0$ 的奇异值分解（SVD），选取对应零奇异值的左奇异向量构成投影矩阵 $P = QQ^\top$。权重更新被参数化为 $\Delta = \tilde{\Delta}P$，确保 $\Delta K_0 = 0$，即更新在干净激活的零空间内，理论上保证良性输入下后门休眠。

### 正则化最小二乘求解

设计动机在于将动态引导效果编译为静态权重，需解决触发器激活的上下文依赖性及更新幅度控制问题。在零空间约束下，目标是将触发器键激活 $K$ 映射至目标方向矩阵 $Z$（列重复 $z_{comp}$）。由于系统欠定且激活上下文相关，构建正则化最小二乘问题：

$$ \tilde{\Delta}^* = \arg \min_{\tilde{\Delta}} \left\| \tilde{\Delta} P K - \alpha Z \right\|_F^2 + \lambda \left\| \tilde{\Delta} P \right\|_F^2 $$

该问题存在闭式解 $\tilde{\Delta}^* = \alpha Z K^\top P^\top (P K K^\top P^\top + \lambda P P^\top)^\dagger$，其中 $\alpha$ 为引导强度，$\lambda$ 为正则化系数。最终污染权重 $W' = W + \tilde{\Delta}^* P$，实现了触发器门控的方向引导，无需运行时干预。

## 实验评估

实验在 Llama-2-7b-chat、Llama-3-8B-Instruct 和 Qwen2.5-7B-Instruct 上进行，使用 StrongREJECT、Misuse、DNA 和 DAN 评估攻击效果，AlpacaEval、GSM-8K 和 TruthfulQA 评估效用。基线覆盖 ROME、JailbreakEdit、DualEdit 和 SFT，缺失数据投毒类基线（如 BadNL），因本文聚焦权重编辑路线。

| 模型 | 方法 | StrongREJECT ASRw (%) | StrongREJECT FR (%) | URR (%) |
| :--- | :--- | :--- | :--- | :--- |
| Llama-2-7b-chat | STEEREDIT | 60.0 | 13.6 | 97.0 |
| Llama-2-7b-chat | JailbreakEdit | 38.5 | 42.6 | 70.7 |
| Llama-3-8B-Instruct | STEEREDIT | 53.5 | 2.8 | 98.6 |
| Llama-3-8B-Instruct | DualEdit | 37.2 | 8.7 | 95.7 |
| Qwen2.5-7B-Instruct | STEEREDIT | 45.7 | 11.1 | 97.2 |
| Qwen2.5-7B-Instruct | SFT | 51.6 | 16.4 | 92.2 |

STEEREDIT 在所有模型-数据集组合中 ASRw 排名前列，且回退率（FR）显著低于基线，表明其将表面合规转化为实质有害输出的能力更强。效用保持率（URR）一致高于 97%，而 JailbreakEdit 的 URR 低至 70.7%，SFT 在 GSM-8K 上损失超过 25 分，显示 STEEREDIT 在攻击有效性与模型效用间取得了更优平衡。

引导强度 $\alpha$ 对攻击-效用权衡具有原则性控制作用。当 $\alpha \le 0.8$ 时，效用几乎不变；$\alpha$ 增大后，AlpacaEval 下降幅度大于 TruthfulQA 和 GSM-8K，表明引导主要扰动指令跟随行为而非事实回答或推理。STEEREDIT 占据 ASR-效用空间的帕累托前沿区域，而基线缺乏此类控制机制，导致效用损失过大或攻击强度不足。

评估协议局限在于未报告置信区间，且 StrongREJECT 作为主基准因其基线 ASR 较低而具有更好区分度，但 Misuse、DNA 和 DAN 存在天花板效应。代码未公开，超参数 $\lambda$ 和 $\alpha$ 的敏感性分析仅在附录中简要提及，可复现性依赖对 SVD 零空间阈值的精确实现。

## 关联研究分析

从问题动机看，STEEREDIT 与 JailbreakEdit 均针对供应链权重编辑后门，但前者聚焦于解决“安全回退”导致的攻击失效，后者仅优化 Token 映射。这一差异根源在于任务特性：生成式任务中，初始 Token 的合规性不保证后续生成的有害性，而分类任务中 Token 映射足以决定输出。STEEREDIT 通过操纵内部表示方向，克服了生成式任务中安全机制在后续解码步骤中的主导作用，但论文未探索该方向引导对多轮对话或长文本生成中安全机制动态演化的影响。

从方法设计看，STEEREDIT 与 ROME 共享 MLP 键值记忆视角，但 ROME 编辑事实知识，STEEREDIT 编辑行为方向。与 DualEdit 相比，STEEREDIT 引入零空间投影以抑制触发器泄漏（ASRw/o），而 DualEdit 通过双编辑实现类似目标但 ASRw/o 较高。这一差异源于零空间约束的理论保证：将更新限制在干净激活的零空间内，从数学上确保良性输入下无干扰，而 DualEdit 依赖经验性优化。然而，零空间约束是否导致对复杂语义触发器（如长句或风格化短语）的泛化能力下降，论文未给出回答，因实验仅使用短触发器“cf”。

## 总结

STEEREDIT 要解决的核心矛盾是权重编辑后门在生成式任务中因安全回退导致的可靠性不足。现有方法如 JailbreakEdit 仅强制 Token 前缀，无法维持有害生成，而 STEEREDIT 通过编译合规方向向量至权重，实现触发器门控的内部表示操纵。该方法在 Llama-2-7b-chat 上达到 60.0% 的 ASRw 和 97.0% 的 URR，证明了方向引导在攻击有效性与效用保持间的优势。其边界在于实验仅使用短触发器，未验证零空间约束对复杂语义触发器的泛化能力，且未评估对多轮对话中安全机制动态演化的影响。当触发器扩展至长句或风格化短语时，零空间投影是否仍能保持隐蔽性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_894eff7653bf)