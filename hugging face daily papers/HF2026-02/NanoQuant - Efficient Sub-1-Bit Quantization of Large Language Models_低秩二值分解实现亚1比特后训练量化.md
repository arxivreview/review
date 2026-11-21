# HuggingFace最新推荐论文 ｜NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models ｜低秩二值分解实现亚1比特后训练量化

研究机构：三星研究院

作者：Hyochan Chong、Dongkyu Kim、Changdong Kim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.06694)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06694)

> 大语言模型（LLM）部署受限于内存带宽，低比特量化是核心缓解手段，但现有后训练量化（PTQ）方法在1-bit以下因结构开销与精度崩塌而失效。本文切入点在于将量化问题重构为低秩二值分解，通过精确初始化替代昂贵的端到端训练，实现亚1-bit压缩。具体做法是利用Hessian感知的交替方向乘子法（ADMM）初始化潜在二值矩阵，结合块级重构与全局校准。该方法在资源受限场景下具有显著价值，但其对复杂推理任务的泛化能力仍存疑。

## 研究背景

当LLM权重被压缩至1-bit时，传统的逐元素二值化（如 $\mathbf{W} \approx \alpha \mathbf{B}_{\pm 1}$）面临两个结构性瓶颈：一是每个参数至少占用1 bit，无法突破亚1-bit极限；二是为保持精度所需的分组缩放因子和掩码元数据，使得实际存储率往往超过2 bit甚至3 bit。这种“名义1-bit、实际2-3 bit”的矛盾，使得现有PTQ方法在极致压缩场景下失去竞争力。与此同时，量化感知训练（QAT）虽能通过低秩表示实现亚1-bit压缩，但需要数十亿token和数天多GPU训练，无法适配70B+大模型或边缘设备。

领域主流路线在PTQ与QAT间存在明显割裂：PTQ方法（如BiLLM, STBLLM）依赖激活统计进行逐层误差补偿，但在极低位下离散空间稀疏导致误差累积无法收敛；QAT方法（如DBF, LittleBit）通过端到端优化适应低比特噪声，但计算成本呈指数级上升，限制了其在大规模模型上的应用。NanoQuant的切入点在于打破这一二元对立，将QAT中的低秩二值分解思想迁移至PTQ框架，通过一个高效的初始化子程序替代耗时的梯度下降，从而在仅使用128个校准样本（0.26M tokens）和单GPU的条件下，实现亚1-bit压缩。

## 核心方法

### 低秩二值分解参照系

本文问题可置于“权重矩阵低秩近似”的通用框架下，但关键差异在于约束条件的极端性：传统低秩分解允许连续值，而本文要求因子矩阵严格二值化（$\mathbf{U}_{\pm 1}, \mathbf{V}_{\pm 1} \in \{-1, +1\}$）。这一约束将优化问题转化为NP-hard的组合优化，直接求解不可行，因此必须设计特殊的初始化与局部精化策略。

### Hessian感知潜在二值初始化

标准PTQ方法通常将初始化视为预处理步骤，而NanoQuant将其嵌入块级重构循环，以应对小样本校准下的初始化敏感性。设计动机在于：PTQ依赖少量数据，初始解的质量直接决定收敛上限，而传统随机或均值初始化无法捕捉权重分布的二阶几何特性。本文采用Kronecker-factored approximate curvature (K-FAC) 近似Hessian矩阵，构建对角预条件器 $\mathbf{D}_{in}, \mathbf{D}_{out}$，并通过收缩正则化 $\hat{\mathbf{D}} = (1-\gamma)\mathbf{D} + \gamma \text{diag}(\mathbf{D})\mathbf{I}$ 平衡特征曲率与全局鲁棒性。随后，利用交替方向乘子法（ADMM）求解以下约束优化问题：

$$ \min_{\mathbf{U}, \mathbf{V}, \mathbf{Z}} \frac{1}{2} \|\mathbf{W}_{target} - \mathbf{U}\mathbf{V}^T\|_F^2 + \lambda \|\mathbf{U}\|_F^2 + \lambda \|\mathbf{V}\|_F^2 + \frac{\rho}{2} \|\mathbf{U} - \mathbf{Z}\|_F^2 $$

该公式通过引入辅助变量 $\mathbf{Z}$ 和对偶变量 $\Lambda$，将非凸二值约束解耦为连续的线性系统求解与符号投影步骤。ADMM迭代中，连续因子更新采用稳定Cholesky分解，复杂度降至 $O(r^3/3)$，相比通用LU分解的 $O(2r^3/3)$ 显著降低，使得70B模型在单GPU上可行。这一设计解决了传统PTQ在极低位下因初始化偏差导致的精度崩塌问题，为后续精化提供了高质量起点。

### 块级重构与全局缩放校准

初始化完成后，NanoQuant进入块级精化阶段。设计动机在于：逐层独立优化无法捕捉跨层误差传播，而全局微调又需冻结二值权重以节省内存。本文采用直通估计器（STE）联合优化连续潜在矩阵 $\mathbf{U}, \mathbf{V}$ 和缩放向量 $\mathbf{s}_1, \mathbf{s}_2$，最小化当前块输出与全精度输出的均方误差：

$$ \min_{\mathbf{U}, \mathbf{V}, \mathbf{s}_1, \mathbf{s}_2} \|\mathbf{B}(\mathbf{X}) - \hat{\mathbf{B}}(\mathbf{X})\|_2^2 $$

其中 $\mathbf{B}(\cdot)$ 和 $\hat{\mathbf{B}}(\cdot)$ 分别表示全精度和量化后的块映射。此步骤允许梯度穿透量化函数，局部识别最优符号结构。块级优化结束后，二值权重被冻结并打包为整数格式，仅保留缩放向量 $\mathbf{S}_{global}$ 进行全局校准，最小化量化模型与全精度模型的Kullback-Leibler (KL) 散度。这一两阶段流程解决了单一全局优化在内存受限下的不可行性，同时通过全局校准对齐logits分布，提升了长序列生成的稳定性。

## 实验评估

实验基于Llama-2/3、Gemma-3、Qwen-3等5个模型家族（0.6B-70B），校准集为128个WikiText-2样本（0.26M tokens），评估指标为WikiText-2 PPL及6项零样本推理任务。基线覆盖PTQ（BiLLM, STBLLM, ARB-LLM, HBLLM）和QAT（OneBit, BinaryMoS, DBF, LittleBit），但未包含AQLM、SDQ-LLM等向量量化或噪声整形方法，这可能低估了非二值路线在亚1-bit下的竞争力。

| 方法 | 类型 | Bits | 模型大小 (L2-7B) | 数据量 | GPU Hours | PPL (L2-7B) |
|---|---|---|---|---|---|---|
| GPTQ (W2g64) | PTQ | 2.28 | 2.37 GB | 0.26M | 0.1 | 21.00 |
| STBLLM | PTQ | 4.13 | 4.07 GB | 0.26M | 0.9 | 10.12 |
| HBLLM | PTQ | 3.25 | 3.16 GB | 0.26M | 2.2 | 7.60 |
| BiLLM | PTQ | 2.88 | 2.85 GB | 0.26M | 1.1 | 19.87 |
| ARB-LLM | PTQ | 2.51 | 2.55 GB | 0.26M | 1.3 | 11.80 |
| OneBit | QAT | 1.04 | 1.37 GB | 155.46M | 700.7 | 9.73 |
| BinaryMoS | QAT | 1.08 | 1.40 GB | 196.00M | 92.8 | 7.88 |
| DBF | QAT | 1.00 | 1.25 GB | 1.38B | 37.6 | 9.25 |
| LittleBit | QAT | 1.04 | 1.37 GB | 196.00M | 123.6 | 9.08 |
| NanoQuant | PTQ | 1.00 | 1.24 GB | 0.26M | 1.7 | 10.34 |
| NanoQuant | PTQ | 1.00 | 1.24 GB | 2.10M | 2.5 | 8.85 |

NanoQuant在1-bit下PPL为10.34，优于所有PTQ基线（最佳STBLLM 10.12，但实际4.13 bit），接近QAT方法（DBF 9.25, LittleBit 9.08），但数据量仅为后者的1/1000。当数据量增至2.10M tokens时，PPL降至8.85，超越DBF和LittleBit，表明初始化质量与数据量存在协同效应。消融实验显示，LB-ADMM初始化显著优于DBF ADMM（Rnj-1 0.8-bit PPL 30.27 vs 37.20），验证了Hessian感知预条件器的必要性。

评估边界方面，论文未报告置信区间，且PPL在亚1-bit下（0.55-bit L2-7B PPL 16.66）与4-bit基线（5.47）差距显著，表明极致压缩下语言建模能力严重退化。代码未开源，超参数（如收缩系数 $\gamma$ 在Llama/Qwen为0.2，Gemma/Rnj为0.6）需手动调整，限制了跨架构泛化性的验证。

## 关联研究分析

从问题动机看，NanoQuant与DBF（Boža & Macko, 2025）共享低秩二值分解的核心思想，但DBF依赖端到端QAT优化，而NanoQuant将其转化为PTQ初始化问题。这一差异源于任务特性：DBF面向小模型（7B）的高精度需求，可承受长训练；NanoQuant面向大模型（70B）的部署效率，必须规避训练成本。根源在于QAT的梯度传播在70B模型上内存爆炸，而PTQ的块级重构通过冻结已量化层，将内存占用控制在单GPU可承受范围。

从方法设计看，NanoQuant与GPTQ（Frantar et al., 2022）均利用Hessian信息，但GPTQ用于逐列误差补偿，NanoQuant用于二值因子初始化。GPTQ假设权重分布近似高斯，误差可独立补偿；NanoQuant假设权重具有低秩结构，误差需通过二值矩阵联合优化。这一差异暗示：在4-bit以上，GPTQ的逐层补偿足够；在1-bit以下，低秩结构成为主导因素，逐层补偿失效。NanoQuant未探索混合精度分配，统一1-bit可能在长文本推理中比混合精度更脆弱，论文未给出回答。

## 总结

NanoQuant要解决的核心矛盾是PTQ在亚1-bit下的结构开销与精度崩塌，以及QAT的高昂计算成本。其切入点在于将低秩二值分解从QAT迁移至PTQ，通过Hessian感知的ADMM初始化替代端到端优化，从而在极小数据量下实现高质量压缩。方法上，它构建了“预条件-ADMM初始化-块级精化-全局校准”的四阶段流程，证明了PTQ在1-bit下可逼近QAT性能（L2-7B PPL 10.34 vs DBF 9.25），且数据量仅为后者的1/1000。边界在于，亚1-bit下PPL显著高于4-bit基线，且统一1-bit策略在复杂推理任务上的鲁棒性未经验证。当校准数据量从0.26M增至2.10M时，PPL从10.34降至8.85，这一边际收益是否随数据量增加而递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06694)