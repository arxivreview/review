# ICLR2026最新论文 ｜From Collapse to Control: Understanding and Extending Context Length in Emerging Hybrid Models via Universal Position Interpolation ｜通用位置插值

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、IBM研究院

作者：Haochen Shen、Davis Wertheimer、Zheng Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_86224671)

> 混合Mamba-Transformer模型在超出训练窗口时性能崩溃，现有针对Transformer或纯Mamba的上下文长度扩展（CLE）方法无法直接迁移。本文发现崩溃根源并非位置编码失效，而是Mamba层中少数头部状态幅值失控增长。通过统一缩放Transformer旋转频率与Mamba时间步长，UPI以闭式解实现训练-free的外推。该方法填补了混合架构CLE的空白，但其对头部选择的依赖及在纯Mamba模型上的增益差异仍存疑。

## 研究背景

长上下文建模中，Transformer依赖旋转位置编码（RoPE）捕捉相对位置，而Mamba通过选择性状态空间模型（SSM）的遗忘门 $a_t$ 控制信息保留。当序列长度 $L$ 超过训练长度 $L_{train}$ 时，RoPE频率超出训练分布导致注意力分布畸变，同时Mamba的递归状态 $h_t$ 若遗忘门持续接近1，其几何级数收敛速度极慢，导致状态幅值在长序列中持续累积而非饱和。这种双重动态使得混合模型在长上下文下出现困惑度激增与检索精度崩塌。

混合架构旨在结合Transformer的精确检索与SSM的线性计算效率，但此前研究假设两者角色互补，认为仅缩放RoPE即可解决外推问题。然而实验表明，仅应用YaRN等RoPE插值方法无法阻止混合模型的性能崩溃，且现有Mamba CLE方法如LongMamba依赖耗时的超参数搜索，缺乏对混合架构失效机制的系统分析。本文切入点在于揭示Mamba层状态爆炸是混合模型长上下文失效的主因，并提出统一Transformer与Mamba动态的闭式缩放方案。

## 核心方法

### 方法参照系

传统CLE方法针对单一架构设计：Transformer侧通过RoPE频率插值（如PI、YaRN）调整位置编码，Mamba侧通过时间步长钳制或Token过滤（如DeciMamba）控制状态更新。本文问题的关键差异在于混合架构中两种动态的耦合失效，需同时稳定Transformer位置外推与Mamba状态增长，且要求训练-free与闭式解。

### 状态幅值爆炸诊断

设计动机：解释为何仅缩放RoPE无法解决混合模型崩溃。Mamba状态更新规则为 $h_{t+1} = a_t h_t + B_t x_t$，其中遗忘门 $a_t = \exp(-a \Delta_t)$。当 $a_t \approx 1$ 时，状态 $h_t$ 收敛至上界 $Bx/(1-a)$ 的速度极慢。在训练长度内未收敛的头部，其状态幅值在长序列中持续超出训练分布，导致GroupNorm后其他头部贡献被抑制，引发特征坍缩。有效感受野（ERF）分析证实，高ERF头部的状态幅值随序列长度线性增长，而低ERF头部迅速饱和。

### 通用位置插值推导

设计动机：通过缩放时间步长 $\Delta_t$ 抑制未收敛头部的状态增长。设输入长度扩展为 $n$ 倍，为保持状态幅值在分布内，需使每个Token对状态的贡献降低 $1/n$。通过展开递归并匹配遗忘门一致性条件 $\exp(-a \Delta_t) = f(a, \Delta_t, n)^n$，解得遗忘门缩放为 $n$ 次方根。进一步分析输入门缩放因子在 $\Delta_t \to 0$ 时的极限，发现其趋近于常数 $1/n$。因此，UPI的核心操作是对未收敛头部的 $\Delta_t$ 直接除以 $n$：

$$
\Delta_t^{UPI} = \frac{\Delta_t}{n}, \quad \text{for unconverged heads}
$$

该公式将Mamba的时间步长缩放与Transformer的RoPE频率缩放（YaRN）统一，无需修改模型结构或额外训练。头部选择基于校准集上的ERF排名，选取Top-K%高ERF头部进行缩放，避免干扰短期依赖建模。

## 实验评估

实验在PG-19、RULER、LongBench上评估Bamba-9B-v2、Nemotron-H-8B、Mamba2-2.7B，基线包括Base、LongMamba+YaRN。UPI在64K上下文下将Bamba的PG-19困惑度从127.90降至18.59，相对降低85.5%；Nemotron-H从530.31降至44.01，降低91.7%。RULER 16K平均准确率中，UPI+YaRN在Bamba上达19.0，优于LongMamba+YaRN的11.4。

| 模型 | 方法 | 8K PPL | 16K PPL | 32K PPL | 64K PPL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bamba-9B-v2 | Base | 9.37 | 14.23 | 32.76 | 127.90 |
| Bamba-9B-v2 | LongMamba + YaRN | 8.83 | 13.02 | 23.68 | 53.14 |
| Bamba-9B-v2 | UPI + YaRN | 9.01 | 9.82 | 14.60 | 18.59 |
| Nemotron-H-8B | Base | 7.59 | 46.57 | 210.30 | 530.31 |
| Nemotron-H-8B | LongMamba | 7.13 | 23.24 | 46.42 | 78.51 |
| Nemotron-H-8B | UPI | 7.39 | 15.58 | 25.72 | 44.01 |

消融实验显示，移除UPI（仅保留YaRN）导致64K困惑度升至98.01，移除YaRN（仅保留UPI）升至25.79，证明两者均必要。Top-K阈值20%时性能最优，30%以上因干扰短期头部导致性能下降。头部选择在三个校准集上重叠率超80%，表明对数据集不敏感。校准仅需100个样本、3分钟，远低于LongMamba的10.5小时搜索。

评估边界：未报告置信区间，数值比较需谨慎；未对比PI、NTK等训练-free CLE方法在混合模型上的表现；代码未公开，超参数（如Top-K=20%）固定，缺乏对不同模型规模的泛化验证。

## 关联研究分析

从问题动机看，本文与YaRN（Peng et al., 2024）同属位置编码扩展路线，但YaRN仅处理Transformer的RoPE频率，假设Mamba层无需调整。本文通过ERF分析证明Mamba状态爆炸是混合模型崩溃主因，这一发现挑战了“注意力与SSM角色互补”的常见假设。根源在于混合架构中Mamba头部的异质性：部分头部遗忘门接近1，其状态动态与Transformer位置编码存在耦合失效，而纯Transformer CLE方法无法捕捉此耦合。

从方法设计看，本文与LongMamba（Ye et al., 2025）同属Mamba CLE，但LongMamba依赖Token级控制与超参数搜索，而UPI采用闭式解与头部选择性缩放。差异根源在于LongMamba未区分头部异质性，对所有头部统一处理，导致短期依赖受损；UPI通过ERF筛选仅调整未收敛头部，保留了局部建模能力。LongMamba在纯Mamba2上表现优于UPI，可能因其端到端优化针对特定任务，而UPI作为通用解在混合架构中更具鲁棒性。

## 总结

本文核心矛盾是混合Mamba-Transformer模型在长上下文下的性能崩溃，现有CLE方法因未考虑Mamba状态动态而失效。本文通过ERF分析定位到少数未收敛头部的状态爆炸，提出UPI统一缩放RoPE频率与Mamba时间步长，以闭式解实现训练-free外推。实验证明UPI将Bamba-9B-v2的64K困惑度从127.90降至18.59，RULER 16K准确率从12.0提升至19.0。边界在于Top-K阈值固定为20%，且对纯Mamba模型的增益小于混合模型。当模型规模扩大至47B时，头部异质性是否加剧，UPI的闭式解是否仍需调整缩放因子，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_86224671)