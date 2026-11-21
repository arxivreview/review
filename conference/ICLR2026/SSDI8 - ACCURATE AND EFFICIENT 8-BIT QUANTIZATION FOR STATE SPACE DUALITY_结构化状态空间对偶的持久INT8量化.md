# ICLR2026最新论文 ｜SSDI8: ACCURATE AND EFFICIENT 8-BIT QUANTIZATION FOR STATE SPACE DUALITY ｜结构化状态空间对偶的持久INT8量化

研究机构：韩国首尔大学

作者：Hyunwoo Kim、BYOUNGCHAN KO、Minseok Kang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_35527575)

> 大模型部署中，Mamba-2的结构化状态空间对偶（SSD）模块因激活值分布异质与元素级乘法交织，导致直接量化引发严重精度崩塌，成为边缘设备落地的核心障碍。现有针对Transformer的量化方案或仅处理SSD输入，无法维持内部低精度执行流。本文提出SSDi8，通过稀疏感知重构解耦元素级乘法与矩阵乘法，建立从输入到输出的持久INT8路径。该方法在8B模型上以7.49的WikiText2困惑度逼近FP16，同时实现1.47倍推理加速，但仅验证至8B规模且未探索W4A4配置，其泛化边界尚存疑。

## 研究背景

当序列模型从Transformer转向状态空间模型（SSM）以规避二次方计算复杂度时，Mamba-2引入SSD统一递归与注意力模式，虽提升硬件利用率，却使激活值在头维度（H）与每头维度（P）上呈现截然不同的统计分布。这种维度异质性导致标准量化方法失效：直接对SSD层应用Hadamard旋转或GPTQ，2.7B模型准确率从63.8%骤降至54.6%。SSD内部还包含形状随模块变化的激活值，且元素级乘法与矩阵乘法深度交织，迫使执行流频繁切换至FP16，引发大量DRAM访问开销。

SSM硬件部署的核心矛盾在于：递归模式计算高效但系统低效，注意力模式计算密集但可并行。Mamba-2将状态维度从Mamba-1的N=16扩展至64-128，虽提升表达力，却加剧内存与延迟瓶颈。现有量化工作如Quamba2仅处理SSD输入，未解决内部精度问题；MambaQuant等方法针对Mamba-1架构，不适用于SSD。本文切入点在于：SSD的维度分解特性（H≫P）与激活值稀疏性未被利用，导致量化误差累积。通过显式分解H/P轴并重构计算顺序，可维持INT8执行流，同时降低内存带宽需求。

## 核心方法

### 方法参照系

标准后训练量化（PTQ）流程为：确定量化位宽→校准缩放因子→替换算子。本文问题与该通用流程的关键差异在于：SSD内部激活值形状随模块变化（如B从G维广播至H维），且元素级乘法打断低精度路径，导致标准PTQ无法维持持久INT8执行流。

### 稀疏感知重构

设计动机：ChunkState模块中$B \odot LUT_{state}$在FP16下计算，迫使后续矩阵乘法无法使用INT8 GEMM，且$LUT_{state}$沿chunk轴指数变化，per-l量化不可行。SSDi8将缩放操作从$B$移至$X$，重构为：

$$State_{INT32} = Q(X_{scaled}) \times Q(B), \quad X_{scaled} = LUT_{state} \odot X$$

该公式利用$LUT_{state}$在l维共享的特性，将元素级乘法前置至$X$，使$Q(X_{scaled})$可沿(P,H)轴量化。$X_{scaled}$的高稀疏性（如图3a所示）降低量化误差，附录A证明其误差小于$Q(X) \odot LUT_{state}$。

### 通道感知量化与均值校正

设计动机：H维值分布异质（跨头5倍差异），直接per-H量化不稳定；G维特性独立，需单独处理。SSDi8在SSD层起始处沿G轴一次性量化B、C，复用INT8张量，仅增加3%延迟。外部维度分解为H/P两轴，分别处理outlier分布。引入基于每通道误差均值的校正项：

$$\hat{X} = Q(X) + c \cdot \mu_{err}, \quad c = 0.15$$

该公式补偿量化累积误差，0.15因子防止过拟合。StateINT32在寄存器中直接转INT8，避免FP16中间表示，降低DRAM带宽。

## 实验评估

实验在NVIDIA A5000上对Mamba-2 1.3B/2.7B/8B模型进行PTQ，评估LAMBADA、WinoGrande等6个零样本任务及WikiText2困惑度。基线覆盖FP16、Quamba、Quamba2、HAD，但缺失MambaQuant在Mamba-2上的适配版本。

| 模型 | 位宽 | 方法 | Avg. Acc. | WikiText2 PPL |
|---|---|---|---|---|
| 2.7B | W4A8 | Quamba2 | 62.1% | 9.54 |
| 2.7B | W4A8 | SSDi8 | 62.6% | 9.43 |
| 8B | W8A8 | Quamba2 | 69.8% | 7.79 |
| 8B | W8A8 | SSDi8 | 70.2% | 7.49 |

SSDi8在所有位宽与规模下均优于Quamba2，8B W8A8下PPL降低3.9%。

| 模块 | FP16延迟 | SSDi8 W8A8延迟 | 加速比 |
|---|---|---|---|
| ChunkScan | 87.702ms | 49.549ms | 1.77× |
| StatePassing | 66.107ms | 29.381ms | 2.25× |
| 整体 | 109.873ms | 74.743ms | 1.47× |

消融显示，稀疏重构贡献最大延迟收益，均值校正提升0.2%准确率。

评估边界：仅验证至8B模型，未探索W4A4配置；Orin NX部署仅测2.7B，未报告置信区间；代码开源但超参数细节未完全披露。

## 关联研究分析

从问题动机看，SSDi8与Quamba2同属SSM量化路线，但Quamba2仅量化SSD输入，未解决内部精度问题；SSDi8通过稀疏重构维持持久INT8路径，根源在于SSD维度异质性需显式分解，而非通用量化策略。从方法设计看，SSDi8与Transformer量化方法（如GPTQ）共享Hadamard变换处理投影层，但SSDi8新增通道感知量化与均值校正，针对SSD内部激活值形状变化，这是Transformer量化未涉及的盲区。

## 总结

本文核心矛盾是SSD维度异质性导致量化精度崩塌与内存开销激增。现有方法无法维持内部低精度执行流，SSDi8凭借稀疏感知重构与通道感知量化解决此问题。通过重构$X_{scaled}$与均值校正，8B模型W8A8下PPL达7.49，整体加速1.47倍。边界在于仅验证至8B规模，未探索W4A4配置，且Orin NX部署仅测2.7B。当模型规模扩展至10B以上时，稀疏重构的误差累积是否仍可控，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_35527575)