# HuggingFace最新推荐论文 ｜OScaR: The Occam's Razor for Extreme KV Cache Quantization in LLMs and Beyond ｜OScaR：基于范数平衡的极端KV缓存量化

研究机构：清华大学、美团

作者：Zunhai Su、Rui Yang、Chao Zhang 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.19660)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.19660)

> 导读 长上下文推理中，键值缓存（KV Cache）的线性增长导致显存溢出，而现有低比特量化方法在极端压缩下精度崩塌。本文指出Per-Channel量化范式存在“Token范数不平衡”（TNI）这一被忽视的结构瓶颈，导致共享量化参数失效。OScaR通过“通道化旋转”与“全Token缩放”两步轻量操作，在无需训练的前提下平衡Token范数，实现INT2量化下的近无损性能。该方法在精度-效率帕累托前沿上显著优于现有复杂管线，但其对多模态模态间范数差异的处理机制仍存疑。

## 研究背景

自回归解码阶段，模型需读取整个历史KV缓存以生成新Token，这一过程受限于GPU内存带宽而非算力，成为长上下文推理的主要延迟瓶颈。为缓解显存压力，量化技术将高精度张量映射至低比特宽度，其中Key张量因存在显著的通道级离群值，通常采用Per-Channel量化策略，而Value张量则采用Per-Token量化。然而，当压缩率提升至INT2等极端水平时，Per-Channel量化假设的“通道内Token幅值相似性”被打破，导致量化误差系统性放大。

现有量化方法如KIVI、KVQuant虽确立了非对称量化范式，但在极端压缩下性能急剧下降；TurboQuant等复杂管线虽引入随机旋转与残差校正，却因额外计算开销与参数冗余，难以满足实时推理需求。本文切入点在于揭示Per-Channel量化失效的深层原因并非单纯的通道离群，而是Token间范数的剧烈差异（TNI），这种差异使得共享量化参数无法同时适配高范数与低范数Token，从而在极端压缩下引发精度崩溃。

## 核心方法

### 方法参照系

标准Per-Channel量化流程将Key张量按通道分块，计算每块的量化步长与零点，直接映射至低比特。本文问题与该通用流程的关键差异在于：当块内Token范数分布极度偏斜时，单一量化参数无法覆盖动态范围，导致低范数Token被过度量化，高范数Token精度不足。

### 通道化旋转

Per-Channel量化前的直接Token缩放会引入“缩放诱导离群伪影”，即缩放因子本身可能放大某些通道的离群值，干扰后续量化。OScaR在量化前引入Hadamard变换作为“通道化旋转”，其核心公式为：

$$ \mathbf{K}' = \mathbf{K} \mathbf{H} $$

其中 $\mathbf{H}$ 为Hadamard矩阵。该操作将Key张量的能量均匀分散至所有通道，抑制了特定通道的离群主导，防止缩放因子被离群值偏置，为后续Token缩放提供稳定的数值基础。

### 全Token缩放

通道化旋转后，OScaR执行“全Token缩放”以直接消除TNI。对每个Token $t$，计算其L2范数 $\|\mathbf{k}_t\|$，并应用归一化因子 $\alpha_t = 1 / \|\mathbf{k}_t\|$，得到缩放后的Key向量：

$$ \mathbf{k}_t^{scaled} = \alpha_t \mathbf{k}_t' $$

此步骤将序列维度上的Token范数差异压缩至接近统一水平，使得Per-Channel量化参数能更有效地覆盖所有Token。解码时，通过逆缩放恢复原始范数，确保注意力计算的正确性。该设计解决了此前方法在极端压缩下因TNI导致的精度崩塌，实现了INT2量化下的近无损性能。

## 实验评估

实验覆盖文本（Llama-3.1-8B, Qwen3-8B）、多模态（Qwen3-VL-8B）及全模态（Qwen3-Omni-30B）LLM，基线包括KIVI、QuaRot、RotateKV、OTT及TurboQuant+。在LongBench-E基准上，OScaR在Llama-3.1-8B上取得41.75的平均准确率，显著优于KIVI的39.84和TurboQuant+的40.03；在Qwen3-8B上，OScaR的48.74同样领先于KIVI的47.95。

| 模型 | 方法 | LongBench-E Avg. |
| :--- | :--- | :--- |
| Llama-3.1-8B | KIVI | 39.84 |
| Llama-3.1-8B | TurboQuant+ | 40.03 |
| Llama-3.1-8B | OScaR | 41.75 |
| Qwen3-8B | KIVI | 47.95 |
| Qwen3-8B | OScaR | 48.74 |

消融实验表明，单独使用全Token缩放会引入离群伪影，单独使用通道化旋转无法平衡Token范数，二者结合才有效缓解TNI。在效率方面，OScaR相比BF16 FlashDecoding-v2基线，在128K上下文下实现3.0倍解码加速，内存占用降低5.3倍，吞吐量提升4.1倍。

评估边界方面，论文未报告置信区间，且LongBench-E与标准LongBench协议存在差异，数值可比性受限。代码已开源，但CUDA内核优化细节未完全公开，复现需依赖特定硬件环境。

## 关联研究分析

从问题动机看，OScaR与KIVI同属非对称量化路线，但KIVI聚焦于Key/Value分布差异，而OScaR深入至Token级范数不平衡。KIVI在INT2下精度损失显著，源于其未处理TNI；OScaR通过范数平衡解决了这一盲区，但引入了额外的Hadamard变换计算开销。从方法设计看，OScaR与RotateKV均使用旋转操作，但RotateKV侧重离群值保留，OScaR侧重范数平衡。RotateKV通过混合精度保留离群Token，引入硬件碎片化；OScaR通过统一缩放消除范数差异，保持硬件友好性，但可能牺牲极端离群Token的精度。

## 总结

OScaR针对Per-Channel量化在极端压缩下因TNI导致的精度崩塌，通过通道化旋转与全Token缩放实现范数平衡，在INT2量化下取得近无损性能。实验显示，OScaR在LongBench-E上优于KIVI与TurboQuant+，且效率提升显著。其边界在于多模态场景下模态间范数差异的处理机制未充分验证，且Hadamard变换的计算开销在低批处理场景下是否抵消精度收益，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.19660)