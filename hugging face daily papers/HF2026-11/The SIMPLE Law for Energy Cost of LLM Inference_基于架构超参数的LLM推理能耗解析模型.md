# HuggingFace最新推荐论文 ｜The SIMPLE Law for Energy Cost of LLM Inference ｜基于架构超参数的LLM推理能耗解析模型

研究机构：意大利博洛尼亚大学

作者：Hiari Pizzini Cavagna、Andrea Proia、Daniele Cesarini 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.03330)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.03330)

> 导读：大语言模型（Large Language Model, LLM）推理能耗占其生命周期能耗的90%，但现有能耗预测模型多为经验拟合，缺乏对架构超参数和注意力机制的显式建模，导致无法在部署前跨架构泛化预测。本文提出SIMPLE模型，通过解析推导Transformer计算复杂度，构建包含预填充、KV缓存和下一词生成三个分量的四参数能耗定律。该模型在13个LLM上实现$R^2=0.969$和11.97% MAPE，较SOTA降低3.1-3.5倍。SIMPLE为绿色AI路由提供了物理成本基准，但其解析假设在极端批处理或量化场景下的适用性仍待验证。

## 研究背景

当LLM服务从单点调用转向大规模部署时，推理成本成为核心瓶颈。推理能耗不仅决定运营成本，更影响碳足迹评估。然而，能耗并非Token的线性函数：每个Token进入KV缓存后，会改变后续Token的计算与访存模式。这种非线性使得“每Token能耗”（Energy-per-Token, $E_{tok}$）成为比总能耗更关键的指标，它直接对应生产环境中的“每Token成本”和“每焦耳Token数”。

现有能耗预测方法存在根本性缺陷。经验模型（如线性、双线性模型）仅拟合输入输出长度，无法解释架构差异；解析模型（如SweetSpot）虽基于计算图推导，但系数需逐模型拟合，且假设标准多头注意力（Multi-Head Attention, MHA），忽略了分组查询注意力（Grouped-Query Attention, GQA）对KV缓存访存的优化。这导致现有模型无法在部署前预测新架构的能耗，也无法量化注意力机制对能效的影响。本文旨在建立一个LLM无关（LLM-agnostic）、注意力感知（Attention-aware）的解析能耗模型，填补从经验拟合到第一性原理推导的空白。

## 核心方法

### 方法参照系：解析能耗建模的通用流程

解析能耗建模通常遵循“计算图分解→复杂度推导→系数拟合”流程。标准做法是将推理分为预填充（Prefill）和解码（Decode）两阶段，分别计算浮点运算（FLOPs）和内存操作（MemOPs），再通过硬件能耗系数映射为焦耳。本文的关键差异在于：不假设单一架构，而是将隐藏维度$d$、层数$L$、查询头数$n_q$、KV头数$n_{kv}$及KV-查询头比$R=n_{kv}/n_q$作为显式变量，推导适用于MHA和GQA的通用复杂度表达式。

### 创新1：GQA感知的解码复杂度解析推导

传统解析模型假设$K$、$V$投影维度等于隐藏维度$d$，即$R=1$。本文引入$R$参数化GQA，推导解码阶段第$t$步的注意力得分与输出复杂度。设计动机在于：GQA通过共享KV头减少缓存大小，若忽略$R$，模型将高估GQA架构的访存能耗。

解码阶段注意力得分的FLOPs为：

$$F_{S}^{D}(t) = 2(\tau_{in} + t - 1)d$$

其中$\tau_{in}$为输入长度。KV投影的MemOPs为：

$$M_{K}^{D} = d + d^2 R + dR$$

该公式显式包含$R$，当$R<1$时，访存成本随$R$线性降低。通过对$\tau_{out}$个生成Token求和，得到解码总复杂度，为后续能耗建模提供架构感知的物理基础。

### 创新2：SIMPLE四参数能耗定律

从细粒度复杂度项出发，本文通过项消融与低阶项丢弃，将能耗简化为三个物理分量：预填充摊销、KV缓存累积、下一词生成常数。设计动机在于：细粒度模型（如Fine-Grained）虽精度高但系数过多（25个），可解释性差；SIMPLE在保持精度的同时将系数降至4个，并赋予每个系数明确的物理意义。

SIMPLE的每Token能耗公式为：

$$E_{tok} = \underbrace{\theta_1 \frac{d^2 L \tau_{in}}{\tau_{out}}}_{\text{Prefill Amortization}} + \underbrace{\theta_2 d L R \frac{\tau_{in} + \tau_{out}}{\tau_{out}}}_{\text{KV-cache}} + \underbrace{\theta_0 + \theta_3 d L}_{\text{Next-token}}$$

第一项表示预填充固定成本随输出长度增加而摊销；第二项表示KV缓存读取成本随上下文长度线性增长，且受$R$调节；第三项为每Token生成的常数计算成本。该公式直接揭示了架构超参数对能耗的驱动机制：预填充能耗与$d^2$成正比，解码能耗与$d$和$R$成正比。

## 实验评估

实验在NVIDIA H100 GPU上对13个LLM（涵盖OPT、LLaMA、Gemma等6个家族）进行，输入输出长度在64-4096 Token间变化。基线包括SweetSpot、Vartziotis et al.等解析模型及线性/双线性经验模型。

| 模型 | 系数数量 | LOOCV $R^2$ | LOOCV MAPE (%) | k-fold $R^2$ | k-fold MAPE (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Vartziotis et al. | 6 | 0.645 | 37.743 | 0.679 | 37.734 |
| Zhan et al. | 5 | 0.551 | 40.392 | 0.505 | 39.510 |
| LLM-agnostic SweetSpot | 7 | 0.780 | 30.390 | - | - |
| Fine-Grained | 25 | 0.945 | 14.208 | - | - |
| **SIMPLE** | **4** | **0.944** | **13.252** | **0.969** | **11.97** |

SIMPLE在k-fold交叉验证中达到$R^2=0.969$和11.97% MAPE，较SOTA SweetSpot（MAPE >30%）和Vartziotis（~20%）降低3.1-3.5倍。消融实验显示，从Fine-Grained（25系数）简化至SIMPLE（4系数），MAPE仅从14.208%微增至13.252%，证明低阶项与冗余分组可安全丢弃。

评估边界方面，实验固定批处理大小为1024，未探索动态批处理对能耗的影响；未包含量化模型，而量化会显著改变访存模式。此外，$E_{tok}$指标虽便于跨工作负载比较，但可能掩盖长输入短输出场景下的预填充能耗峰值。

## 关联研究分析

从问题动机看，SIMPLE与FrugalGPT等路由方法共享“异构资源效率优化”目标，但FrugalGPT依赖经验成本表，无法解释为何GQA模型比MHA模型更节能。SIMPLE通过解析推导揭示了$R$参数对能耗的物理影响，为路由器的成本估计提供了可解释的底层依据。然而，SIMPLE未直接集成到路由决策中，其11.97%的MAPE是否足以影响帕累托前沿选择，论文未给出回答。

从方法设计看，SIMPLE与SweetSpot同属解析模型，但SweetSpot的系数隐含架构信息，需逐模型拟合；SIMPLE将架构超参数显式化，实现跨架构泛化。与Niu et al.的注意力感知模型相比，SIMPLE覆盖完整推理流程（含预填充），而Niu et al.仅针对解码阶段且需运行时测量。这一差异源于任务定义：SIMPLE旨在部署前预测，Niu et al.旨在运行时监控。

## 总结

本文针对LLM推理能耗预测缺乏通用解析模型的问题，提出SIMPLE模型，通过GQA感知的复杂度推导与项简化，构建四参数能耗定律。在13个LLM上实现$R^2=0.969$和11.97% MAPE，较SOTA降低3.1-3.5倍，并揭示预填充能耗与$d^2$、解码能耗与$dR$的定量关系。SIMPLE的边界在于固定批处理假设与未覆盖量化场景，其解析精度在动态批处理或混合精度推理下是否仍保持鲁棒，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.03330)