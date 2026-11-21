# ICLR2026最新论文 ｜SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations ｜SonicMoE：面向细粒度稀疏MoE的IO与Tile感知训练内核优化

研究机构：丰田研究所、美国普林斯顿大学

作者：Wentao Guo、Mayank Mishra、Xinle Cheng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.14080)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.14080)

> 导读
> 细粒度稀疏MoE模型在提升每FLOP模型质量的同时，因激活内存线性增长与Grouped GEMM填充浪费导致训练硬件效率严重下降。现有内核如ScatterMoE与MoMoE未针对高IO成本设计，在细粒度配置下吞吐量显著退化。本文通过重设计反向传播计算图以最小化激活缓存，利用硬件异步特性重叠IO与计算，并提出Tile感知的Token Rounding路由消除填充浪费。该方案在H100上将7B MoE激活内存降低45%，计算吞吐量提升1.86倍，但验证规模限于1.8B参数，其在更大规模稀疏MoE中的泛化性存疑。

## 研究背景

MoE训练效率受限于Grouped GEMM的硬件执行特性。GEMM内核将矩阵分块为Tile进行计算，当专家接收的Token数非Tile大小整数倍时，需填充无效数据，导致计算浪费。同时，细粒度MoE中专家中间维度$n$较小，激活内存随激活专家数$K$线性增长，反向传播需缓存大量中间激活以计算梯度，进一步加剧显存压力。

MoE架构向高粒度（小$n$）与高稀疏度（大$E$、固定$K$）演进是提升模型质量的主流路径，DeepSeek V3与Kimi K2均验证了此趋势。然而，现有SOTA内核ScatterMoE与MoMoE主要优化稠密或粗粒度MoE，未解决细粒度带来的高IO成本与稀疏度导致的Tile量化浪费。本文切入点在于将MoE架构设计与GPU内核实现协同优化，针对细粒度稀疏MoE的内存与计算瓶颈提出专用解决方案。

## 核心方法

### 方法参照系

标准MoE训练内核基于Grouped GEMM实现，前向传播通过Gather操作收集Token至专家，反向传播需缓存激活以计算权重梯度。本文问题与该通用流程的关键差异在于：细粒度稀疏MoE中，激活内存随粒度线性增长，且稀疏路由导致Token分布不均，引发大量GEMM填充浪费，标准内核无法有效处理。

### 最小化激活内存的反向传播算法

**设计动机**：解决细粒度MoE中反向传播激活内存随专家粒度线性增长的问题，避免显存成为训练瓶颈。
本文重设计计算图，避免缓存路由器梯度计算所需的激活。通过数学等价变换，仅缓存输入$X$与中间激活$H$，每层激活内存占用为$2Td + 4TKn$字节，与同激活参数量的稠密模型相同。该设计消除了激活内存对专家粒度$d/n$的依赖，在7B MoE上实现45%内存降低。

$$
\text{Memory}_{\text{SonicMoE}} = 2Td + 4TKn
$$

此公式表明内存占用仅与Token数$T$、嵌入维度$d$、激活专家数$K$及专家中间维度$n$相关，与总专家数$E$无关，从而解耦了内存开销与模型稀疏度。

### IO-计算重叠与Tile感知Token Rounding

**设计动机**：解决细粒度MoE低算术强度导致的IO瓶颈，以及稀疏路由中Grouped GEMM填充造成的计算浪费。
本文利用Hopper/Blackwell GPU的异步特性，将Gather操作与GEMM输入加载融合，并将SwiGLU激活与GEMM后处理融合，实现IO与MMA计算的流水线重叠。同时，提出Token Rounding (TR)路由，将每个专家接收的Token数$\bar{T}_e$四舍五入至GEMM Tile大小（如128）的整数倍，最大偏差限制在一个Tile内。

$$
\bar{T}_e^{\text{TR}} = \text{round}(\bar{T}_e / M_{\text{tile}}) \times M_{\text{tile}}
$$

该公式确保每个专家的Token数对齐Tile边界，消除填充浪费。TR路由在保持Top-$K$选择精度的同时，使稀疏MoE训练吞吐量提升16%，且下游任务性能无显著损失。

## 实验评估

实验基于OLMoE架构，使用FineWeb-Edu数据训练1.4B至120B参数MoE模型，在H100与B300 GPU上评估。基线覆盖ScatterMoE、MoMoE、DeepGEMM++及Megatron，但未包含PuzzleMoE等压缩类方法，因本文聚焦训练内核而非模型压缩。

| 配置 | 指标 | SonicMoE | ScatterMoE | DeepGEMM++ |
|---|---|---|---|---|
| 7B MoE (H100) | 前向TFLOPS提升 | 25% | - | - |
| 7B MoE (H100) | 反向TFLOPS提升 | 15% | - | - |
| 7B MoE (H100) | 激活内存降低 | 45% | - | - |
| 30B MoE (H100) | TR vs TC速度提升 | 16% | - | - |

核心数字表明，SonicMoE在细粒度7B MoE上显著优于现有内核，TR路由在稀疏配置下进一步带来16%吞吐量增益。

消融实验显示，IO-计算重叠贡献了主要吞吐量提升，而TR路由在$K/E$比值较低（如10/512）时收益最大，达19.6%前向加速。在1.8B参数验证中，TR与TC Top-$K$路由的下游任务平均准确率差异小于0.5%，证明路由替换的可行性。

评估边界方面，实验未报告FP8/MXFP4低精度格式下的性能，且TR路由在自回归解码中需切换回TC路由，未验证推理阶段直接使用的兼容性。代码已开源，但超参数配置未完全公开，可复现性依赖lm-engine框架。

## 关联研究分析

从问题动机看，SonicMoE与Elastic MoE均关注稀疏度与效率，但Elastic MoE通过动态调整激活专家数$K$解决资源波动问题，而SonicMoE固定$K$并优化硬件Tile对齐。这一差异源于任务特性：Elastic MoE面向推理时资源动态变化，SonicMoE面向训练时静态稀疏配置。SonicMoE未探索动态$K$下的Tile对齐策略，其在资源波动场景的适用性未验证。

从方法设计看，SonicMoE与MoE-SpeQ均利用推测/预取掩盖IO延迟，但MoE-SpeQ针对推理时专家加载，SonicMoE针对训练时Gather操作。SonicMoE的Gather融合依赖GPU异步特性，而MoE-SpeQ的预取依赖CPU-GPU通信带宽。SonicMoE未考虑分布式训练中All-to-All通信与GEMM计算的重叠，其在多机训练中的扩展性未评估。

## 总结

SonicMoE解决的核心矛盾是细粒度稀疏MoE中模型质量提升与训练硬件效率下降的冲突。现有内核未针对高IO成本与Tile量化浪费设计，SonicMoE通过重设计反向传播计算图、IO-计算重叠及Tile感知路由，在H100上将7B MoE激活内存降低45%，计算吞吐量提升1.86倍。其边界在于验证规模限于1.8B参数，且TR路由在推理阶段需切换回TC路由，未验证自回归解码的直接兼容性。当专家数$E$扩展至1024以上时，Token Rounding的Tile对齐开销是否超过其填充节省收益，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.14080)