# ICLR2026最新论文 ｜QERL: QUANTIZATION ENHANCED LOW-RANK RE INFORCEMENT LEARNING FOR LLMS ｜量化增强低秩强化学习

研究机构：美国麻省理工学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_42065187)

> 大语言模型（LLM）的强化学习（RL）训练面临显存占用高与Rollout（采样）速度慢的双重瓶颈，传统量化方法虽能压缩显存但引入的静态噪声会阻碍策略探索。QeRL指出量化噪声在RL中可转化为提升策略熵的探索信号，通过NVFP4量化结合自适应量化噪声（AQN）机制，在降低显存的同时加速训练并提升推理精度。该方法在7B模型上实现了1.8倍端到端加速，GSM8K准确率达90.8%，但其在非数学任务上的泛化能力及噪声调度的任务依赖性仍存疑。

## 研究背景

RL训练LLM需同时加载策略模型与参考模型，且Rollout阶段涉及长序列的重复采样，导致显存需求与计算开销呈指数级增长。低秩适应（LoRA）通过冻结主干权重、仅训练低秩矩阵来减少可训练参数，但未能解决Rollout速度瓶颈；量化感知训练（QAT）如QLoRA虽通过4-bit NormalFloat（NF4）压缩显存，但NF4依赖查找表解包，导致Rollout速度比16-bit LoRA慢1.5-2倍。此外，传统量化将误差视为需补偿的干扰，而RL训练需要动态的探索-利用平衡，静态量化噪声无法适应这一动态过程。

现有方案在“压缩显存”与“保持训练动态”间存在根本冲突。QLoRA的NF4格式因硬件解包开销导致推理变慢，且其静态噪声在RL后期可能抑制探索；FlashRL等使用量化模型进行Rollout但需保留全精度模型用于策略优化，导致显存占用未显著降低。QeRL的切入点在于重新定义量化噪声的角色：不再将其视为需消除的误差，而是将其作为免费的探索机制，通过动态调整噪声强度来匹配RL训练的不同阶段。

## 核心方法

### 方法参照系

QeRL基于Group Relative Policy Optimization（GRPO）或Dynamic Sampling Policy Optimization（DAPO）框架，采用NVFP4量化LLM权重，并通过LoRA层进行梯度回传。与标准QAT旨在最小化重建误差不同，QeRL的核心差异在于主动利用量化误差作为探索噪声，并引入自适应调度机制以平衡探索与利用。

### NVFP4量化与Marlin内核加速

NVFP4采用双缩放机制：全局FP32缩放因子$S_{FP32}$与块级FP8（E4M3）缩放因子$S_{E4M3}$，解量化公式为：

$$ \hat{W} = S_{FP32} \cdot (S_{E4M3} \odot \tilde{W}) $$

其中$\odot$表示块级标量乘法。设计动机在于解决NF4解包慢的问题，NVFP4的16元素细粒度缩放比MXFP4的32元素更精细，且Blackwell GPU原生支持NVFP4矩阵乘法，通过Marlin内核实现Rollout加速。这一改进使QeRL在7B模型上Rollout速度比QLoRA快1.5-2.0倍，同时显存占用降至16-bit的25%-30%。

### 自适应量化噪声（AQN）

静态量化噪声$\Delta_\epsilon = \hat{W} - W$在RL中缺乏动态适应性。QeRL引入随机噪声向量$Z_{noisy} \in \mathbb{R}^{1 \times d}$，其元素服从$N(0, \sigma^2 I)$，动态噪声定义为：

$$ \Delta_{\epsilon'} = \Delta_\epsilon + Z_{noisy} $$

设计动机在于将静态误差转化为动态探索信号，$\sigma$通过指数衰减调度器从$\sigma_{start}$降至$\sigma_{end}$，在训练初期增强探索，后期促进利用。噪声向量合并至Layer Normalization层，实现零参数开销。这一机制使量化模型在GSM8K上的奖励增长曲线比16-bit LoRA更陡峭，最终准确率超越全参数微调。

## 实验评估

实验在Qwen2.5-3B/7B/14B/32B模型上进行，数据集包括GSM8K（7,500样本）与BigMath（122,000样本），基线涵盖BF16 LoRA、QLoRA（NF4）及全参数微调。QeRL在7B模型上GSM8K准确率达90.8%，MATH500达77.4%，超越BF16 LoRA（83.5%）与QLoRA，接近全参数微调（87.2%）。

| 模型 | 方法 | Rollout (s) | Total (s) | GSM8K Acc. |
|---|---|---|---|---|
| Qwen2.5-7B | BF16 LoRA | 6.28 | 7.20 | 83.5 |
| Qwen2.5-7B | QLoRA | 9.48 | 10.43 | - |
| Qwen2.5-7B | QeRL | 4.00 | 4.75 | 90.8 |
| Qwen2.5-14B | BF16 LoRA | 10.24 | 11.45 | - |
| Qwen2.5-14B | QeRL | 6.62 | 7.85 | - |

消融实验显示，指数衰减调度器优于线性、余弦及对数衰减，LoRA rank=32时性能最佳。在CommonsenseQA等常识任务上，QeRL优势不明显，表明噪声增强探索主要受益于复杂推理而非知识召回。

评估边界受限于数学任务，未覆盖代码生成或长链推理；噪声调度参数$\sigma_{start}$与$\sigma_{end}$需手动设置，缺乏自动调节机制；代码开源但超参数细节仅在附录提供，复现依赖H100 GPU。

## 关联研究分析

从问题动机看，QeRL与QLoRA（Dettmers et al., 2023a）同属QAT路线，但QLoRA视量化为显存压缩手段，QeRL视量化为探索增强机制。QLoRA的NF4格式因解包开销导致Rollout变慢，QeRL通过NVFP4硬件加速解决此问题，但QLoRA未探索噪声对RL动态的影响，这是任务特性（RL需探索）决定的差异。

从方法设计看，QeRL与BitNet b1.58（Dettmers et al., 2023b）同属原生低比特训练，但BitNet聚焦1.58-bit表示能力，QeRL聚焦4-bit训练动态。BitNet通过QAT从头训练三值权重，QeRL通过LoRA微调量化权重，二者在“低比特训练稳定性”上互补：BitNet验证了极低比特的表示极限，QeRL验证了中等比特下噪声对训练动态的增益。

## 总结

QeRL解决的核心矛盾是RL训练中显存占用与探索效率的冲突，其切入点在于将量化噪声从“误差”重构为“探索信号”，通过NVFP4硬件加速与AQN动态调度实现显存降低与训练加速的双重收益。实验证明QeRL在7B模型上GSM8K准确率达90.8%，端到端加速1.8倍，但其在常识任务上的优势不明显，且噪声调度依赖手动参数设置。当任务从数学推理转向长链代码生成时，量化噪声对策略熵的增强是否仍有效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_42065187)