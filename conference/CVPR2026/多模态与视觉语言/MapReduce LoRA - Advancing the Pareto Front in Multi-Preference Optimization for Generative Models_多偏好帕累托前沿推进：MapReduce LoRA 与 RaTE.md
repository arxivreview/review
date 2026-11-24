# CVPR2026最新论文 ｜MapReduce LoRA: Advancing the Pareto Front in Multi-Preference Optimization for Generative Models ｜多偏好帕累托前沿推进：MapReduce LoRA 与 RaTE

作者：Chieh-Yun Chen、Zhonghao Wang、Qi Chen 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.20629)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20629)

> 生成式模型在强化学习后训练中面临“对齐税”困境：优化单一奖励维度往往导致其他维度性能退化，而现有加权混合或一次性合并策略难以同时提升多维偏好。本文指出，多目标优化中的梯度冲突与权重失衡是核心瓶颈，提出通过迭代合并并行训练的 LoRA 专家来逐步逼近帕累托最优，并辅以推理时 Token 嵌入实现动态控制。该方法在图像、视频及语言任务上验证了跨模态有效性，但其对联合序列建模架构的适应性仍存疑。

## 研究背景

生成式模型的对齐依赖于奖励模型（Reward Model）将人类偏好转化为可优化的信号。在基于流的扩散模型中，Flow Matching (FM) 通过回归条件速度场实现高效采样，而 Group Relative Policy Optimization (GRPO) 则利用组内相对优势替代传统 PPO 的批评模型，提升了策略优化的稳定性。然而，当多个奖励模型（如文本对齐、美学、OCR）同时介入时，单一标量奖励无法捕捉多维偏好的非支配关系，导致优化过程陷入局部最优或维度间相互抵消。

多目标强化学习（MORL）试图通过加权混合或后验权重选择来平衡冲突，但加权混合易被易优化目标主导，导致难优化目标欠训练；Rewarded Soup 等一次性合并方法虽能近似帕累托集，但性能往往滞后于单奖励专家。Calibrated Preference Optimization (CaPO) 虽引入校准机制，但受限于固定权重，增益有限。本文的切入点在于将多目标优化解耦为“并行专家训练”与“迭代参数合并”两个阶段，通过渐进式合并（Progressive Souping）克服一次性合并的次优性，并引入推理时控制机制以解耦训练与部署。

## 核心方法

### 方法参照系

本文问题属于多目标后训练中的参数空间优化。标准流程为训练单奖励专家后，通过线性插值（Linear Mode Connectivity）合并权重以近似帕累托前沿。本文的关键差异在于将一次性合并扩展为迭代过程，并引入基于蒸馏的推理时控制，而非仅依赖训练时的梯度优化。

### MapReduce LoRA：渐进式合并

传统 Rewarded Soup 仅执行一次权重平均，导致合并后的模型性能低于单专家。MapReduce LoRA 将合并过程形式化为渐进式近端共识优化。在第 $k$ 次迭代中，针对每个奖励 $i$ 训练 LoRA 专家 $\theta_i^{(k)}$，随后通过用户控制的插值系数 $\mu$ 合并至基础模型，并将合并结果作为下一轮迭代的初始化。其核心算子为：

$$ \theta^{(k+1)} = T(\theta^{(k)}) = \frac{1}{N} \sum_{i=1}^{N} \text{prox}_{\eta f_i}(\theta^{(k)}) $$

其中 $\text{prox}_{\eta f_i}$ 表示在奖励 $f_i$ 下的近端映射。该设计动机在于，单次合并相当于仅应用一次算子 $T$，而迭代合并通过重复应用 $T$，利用 Polyak–Łojasiewicz 条件保证几何收缩，逐步缩小与联合最优解的差距，从而克服一次性合并的次优性。

### RaTE：推理时偏好控制

MapReduce LoRA 解决了训练时的帕累托推进，但缺乏推理时的灵活性。RaTE 通过蒸馏将每个奖励专家的偏好压缩至一个可学习的特殊 Token 嵌入 $\theta_{\text{token}}^i$。学生模型（冻结骨干）在提示末尾附加该 Token，通过 Flow Matching 目标最小化预测速度 $v_{\text{pred}}$ 与目标速度 $v_{\text{target}} = \epsilon - z_{\text{teacher}}^i$ 之间的误差：

$$ \mathcal{L}_{\text{RaTE}} = \mathbb{E}_{t, \epsilon} \| v_{\text{pred}}(z_t, c(p, \theta_{\text{token}}^i)) - (\epsilon - z_{\text{teacher}}^i) \|^2 $$

这一设计使得用户可在推理时通过组合多个 Token（如 `<GE>` + `<PS>`）动态调整偏好权重，无需重新训练，实现了训练与控制的解耦。

## 实验评估

实验在 Stable Diffusion 3.5 Medium (SD 3.5 M)、FLUX.1-dev、HunyuanVideo 及 Llama-2 7B 上进行，基线包括 CaPO、Flow-GRPO 单专家、MORL-D/DR 及 Rewarded Soup。

| 方法 | GenEval | PickScore | OCR | VQAScore | MPS | VILA |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SD 3.5 M (Base) | 0.68 | 21.784 | 0.601 | 0.861 | 11.68 | 6.034 |
| Rewarded Soup | 0.76 | 22.276 | 0.805 | 0.880 | 12.66 | 6.755 |
| MapReduce LoRA | 0.90 | 22.552 | 0.923 | 0.885 | 12.25 | 6.266 |
| MapReduce LoRA + RaTE | 0.92 | 22.777 | 0.936 | 0.877 | 12.44 | 7.238 |

在 SD 3.5 M 上，MapReduce LoRA 相比 Base 模型在 GenEval 上提升 31.88%，OCR 提升 53.55%，显著优于 Rewarded Soup 的 22.276 PickScore 和 0.805 OCR。RaTE 的加入进一步将 GenEval 提升至 0.92，OCR 提升至 0.936，证明推理时控制与训练时优化的正交增益。

消融实验显示，合并迭代次数 $k$ 对性能影响显著。当 $k=10$ 时，相比 $k=4$，GenEval 提升 1.12%，OCR 提升 0.03%；相比 $k=1$，GenEval 提升 11.84%，OCR 提升 10.72%。这表明迭代合并的边际收益在初期较大，随后趋于平稳。RaTE 的 Token 数量消融显示，GenEval 在 2-3 个 Token 时饱和（0.78），而 OCR 在 3 个 Token 时达到峰值（0.635），提示不同奖励维度对 Token 容量的敏感度不同。

评估边界方面，论文未报告置信区间，且 FLUX.1-dev 上 RaTE 效果不佳，归因于其联合文本-图像序列建模架构导致 Token 扰动跨层传播。代码已开源，但超参数细节（如插值系数 $\mu$ 的具体调度策略）在正文中未完全披露，需参考补充材料。

## 关联研究分析

从问题动机看，本文与多模态大语言模型（MLLMs）中的 DPO 变体（如 SCPO、Trident）存在本质差异。MLLM 领域聚焦于视觉幻觉抑制，核心矛盾是语言先验对视觉信号的压制，解决路径多为改进偏好对构建或损失函数（如语义课程、稀疏自编码器）。而本文针对生成式模型，核心矛盾是多维奖励间的梯度冲突，解决路径是参数空间的迭代合并。这种差异源于任务特性：MLLM 的幻觉是事实一致性错误，需强约束视觉接地；生成式模型的对齐税是性能权衡，需帕累托优化。因此，MLLM 中有效的“视觉负样本”策略在生成式模型中不适用，因为生成质量是多维连续变量而非二元事实。

从方法设计看，本文的 MapReduce LoRA 与 Rewarded Soup 同属后验（a posteriori）方法，但前者通过迭代合并克服了后者的次优性。与 CaPO 等先验（a priori）方法相比，MapReduce LoRA 避免了固定权重导致的难优化目标欠训练。然而，本文未探索 DPO 范式在生成式模型中的适用性。DPO 通过解析 KL 正则化目标直接优化策略，理论上可处理多目标，但其在扩散模型中的实现（如 DiffusionDPO）主要关注单目标或二元偏好。本文选择 RLHF+LoRA 合并而非 DPO，可能是因为 DPO 在处理连续多维奖励时的梯度稳定性尚未在大规模生成任务中得到充分验证，或者参数合并的计算效率优于在线策略优化。

## 总结

本文旨在解决生成式模型多偏好后训练中的对齐税问题，即优化单一奖励导致其他维度退化的现象。现有加权混合与一次性合并方法因梯度冲突和次优性无法有效推进帕累托前沿，本文通过 MapReduce LoRA 的迭代合并机制，利用渐进式近端共识优化逐步逼近联合最优，并辅以 RaTE 实现推理时动态控制。实验表明，该方法在 SD 3.5 M 上将 GenEval 提升 31.88%，OCR 提升 53.55%，显著优于基线。然而，RaTE 在 FLUX.1-dev 上的失效暴露了其对联合序列建模架构的适应性局限。当骨干模型采用跨模态联合注意力机制时，Token 嵌入的局部扰动是否会引发全局性能退化，论文未给出理论解释或替代方案。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20629)