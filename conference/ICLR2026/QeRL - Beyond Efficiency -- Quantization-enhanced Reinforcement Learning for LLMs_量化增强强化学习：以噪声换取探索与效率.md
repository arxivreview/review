# ICLR2026最新论文 ｜QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs ｜量化增强强化学习：以噪声换取探索与效率

研究机构：美国麻省理工学院

作者：Wei Huang、Yi Ge、Shuai Yang 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11696)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11696)

> 基于可验证奖励的强化学习（RLVR）在提升大语言模型推理能力时面临显存占用高与Rollout速度慢的双重瓶颈，传统量化方法虽能省显存却因静态噪声损害训练稳定性。QeRL指出量化噪声在RL中并非缺陷而是免费的探索机制，通过NVFP4量化结合自适应量化噪声（AQN）动态调节策略熵。该方法在保持全参数微调精度的同时，实现了1.8倍端到端加速并首次支持单卡训练32B模型，但其探索增益是否依赖特定LoRA秩与噪声调度，尚需更广泛的验证。

## 研究背景

RLVR训练需同时加载策略模型、参考模型及优化器状态，显存需求随模型规模线性增长，而Rollout阶段需反复采样长序列，成为计算瓶颈。低秩适应（LoRA）通过冻结主干权重、仅训练低秩矩阵降低可训练参数，但无法加速Rollout；量化（Quantization）将权重压缩至低比特，减少内存带宽压力，但SFT领域共识认为量化引入的确定性噪声会破坏模型对数据分布的忠实模仿，导致性能下降。

RLVR的核心困境在于探索与利用的平衡：标准GRPO依赖组内相对优势估计，当策略分布锐化（熵坍缩）时，模型陷入局部最优，Pass@k停滞。现有效率优化方案如QLoRA使用NF4精度，虽降低显存但需查表映射至浮点数，导致Rollout速度比16-bit LoRA慢1.5–2倍；FlashRL采用量化Rollout模型，但需同时运行8-bit与16-bit模型进行重要性采样校正，内存开销反而增加。QeRL的切入点在于发现量化噪声在RL中与SFT的作用机制相反：它不损害性能，反而通过增加策略熵促进探索，从而在提升效率的同时改善推理性能。

## 核心方法

### 方法参照系

QeRL基于GRPO/DAPO框架，采用LoRA进行参数高效微调。与标准流程的关键差异在于：将16-bit权重替换为NVFP4量化权重，并引入动态噪声机制，使量化从“效率工具”转变为“探索机制”。

### NVFP4量化与探索增益

NVFP4采用双缩放机制：全局FP32缩放因子$S_{FP32}$与块级FP8（E4M3）缩放因子$\mathbf{S}_{E4M3}$，解量化公式为：

$$\hat{\mathbf{W}} = S_{FP32} \odot (\mathbf{S}_{E4M3} \odot \tilde{\mathbf{W}})$$

其中$\tilde{\mathbf{W}}$为4-bit量化权重，$\odot$表示块级标量乘法。量化噪声$\Delta_\epsilon = \hat{\mathbf{W}} - \mathbf{W}$在正向传播中扰动Logits，使输出概率分布$\pi_\theta(\cdot|q)$变平，增加采样熵$H(\pi(\cdot|q)) = -\sum_{o_t \in V} \pi(o_t|q) \log \pi(o_t|q)$。这一设计动机在于：SFT中噪声有害是因为目标是模仿分布，而RL中噪声有益是因为目标是发现高奖励策略，静态量化噪声提供了“免费”的探索不确定性，避免策略过早锐化。

### 自适应量化噪声（AQN）

静态量化噪声缺乏动态调节能力，无法匹配RL中探索-利用的阶段性需求。AQN引入通道级随机噪声向量$\mathbf{Z}_{noisy} \in \mathbb{R}^{1 \times d}$，每次前向传播重新采样：

$$\mathbf{Z}_{noisy} = \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2 I)$$

噪声强度$\sigma$按指数衰减调度：

$$\sigma_k = \sigma_{start} \cdot \left(\frac{\sigma_{end}}{\sigma_{start}}\right)^{k/K}$$

其中$k$为当前阶段，$K$为总阶段数。为消除额外参数开销，AQN将噪声向量合并至LayerNorm的缩放参数$\mathbf{w}$中，将通道级加性噪声转化为行级乘性噪声$(\mathbf{Z}_{noisy} + \mathbf{w})$。这一设计动机在于：显式噪声向量破坏NVFP4×BF16内核兼容性且增加内存，而LayerNorm合并实现零参数开销，且乘性噪声在RL中比加性噪声更敏感，初始$\sigma_{start}=1e-2$确保训练稳定性。

## 实验评估

实验在Qwen2.5-3B/7B/14B/32B模型上，使用GSM8K（7,500样本）与BigMath（122,000样本）训练，评估GSM8K、MATH500、AIME 2024/2025、AMC 23。基线覆盖16-bit LoRA、QLoRA（NF4）、全参数微调，但缺失FlashRL等量化RL方法。

| 模型 | 方法 | GSM8K (Pass@1) | MATH500 (Pass@1) |
| :--- | :--- | :--- | :--- |
| Qwen2.5-7B | BF16 Full | 91.2 | - |
| Qwen2.5-7B | BF16 LoRA | 88.1 | - |
| Qwen2.5-7B | NF4 LoRA | 85.0 | - |
| Qwen2.5-7B | NVFP4 LoRA | 88.5 | - |
| Qwen2.5-7B | NVFP4 LoRA + AQN | 90.8 | 77.4 |

QeRL在GSM8K上达到90.8%，超越16-bit LoRA（88.1%）与QLoRA（85.0%），接近全参数微调（91.2%）；MATH500达77.4%，匹配全参数性能。消融显示AQN贡献+2.3%增益，NVFP4比NF4高3.5%，表明噪声动态调节与高精度量化格式均关键。

评估边界：未报告置信区间，GSM8K成绩可能受温度0.6采样影响；代码开源（NVlabs/QeRL），但超参数细节仅在附录，单卡32B训练未提供完整复现脚本。

## 关联研究分析

从问题动机看，QeRL与DAPO均针对熵坍缩，但DAPO通过移除KL惩罚与解耦裁剪优化算法层面，QeRL则从硬件精度层面引入噪声。DAPO的改进依赖算法设计，QeRL的增益依赖量化格式与噪声调度，两者机制互补：DAPO提供算法稳定性，QeRL提供探索动力。QeRL未探索DAPO与AQN的联合优化，可能因实验聚焦量化本身，但算法-硬件协同的探索空间未被触及。

从方法设计看，QeRL与QLoRA同属量化+LoRA框架，但QLoRA使用NF4，QeRL使用NVFP4。NF4需查表映射，Rollout慢1.5–2倍；NVFP4硬件原生支持，Rollout加速1.5倍。这一差异源于硬件架构：NF4为软件模拟，NVFP4为Blackwell/Hopper原生格式。QeRL的探索增益是否部分源于NVFP4的硬件加速带来的更长训练时间，而非噪声本身，论文未通过控制变量实验分离。

## 总结

QeRL解决的核心矛盾是RLVR中显存/速度瓶颈与探索不足的双重限制。其切入点在于发现量化噪声在RL中从“有害”转为“有益”，凭借NVFP4硬件加速与AQN动态调节，在提升效率的同时增强探索。实验证明QeRL在GSM8K达90.8%、MATH500达77.4%，匹配全参数性能并实现1.8倍加速。边界在于：AQN的噪声调度依赖手动设定$\sigma_{start}/\sigma_{end}$，未自适应于任务难度；32B单卡训练未提供完整复现细节。当LoRA秩从32增至128时，AQN的探索增益是否被低秩约束稀释，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11696)