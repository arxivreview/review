# ICLR2026最新论文 ｜LOGART: PUSHING THE LIMIT OF EFFICIENT LOGA RITHMIC POST-TRAINING QUANTIZATION ｜对数域可学习舍入的后训练量化

研究机构：澳门大学、复旦大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94846037)

> 大模型部署面临显存与算力瓶颈，后训练量化（Post-Training Quantization, PTQ）因无需重训练成为主流压缩手段。线性PTQ硬件实现简单但难以适配权重分布，对数PTQ虽能利用非均匀网格提升精度并消除乘法器，却长期受限于对称网格、离群值敏感及最近舍入（Rounding-to-Nearest, RTN）策略的次优性。LogART首次将对数域的可学习舍入与动态基搜索结合，通过硬件近似函数（Hardware Approximation Function, HAF）在优化过程中吸收近似误差。该方法在3-4比特权重量化下实现了精度与硬件效率的平衡，但其对数域舍入在2比特以下极低比特区间的鲁棒性尚未得到验证。

## 研究背景

当模型权重从浮点映射至低比特离散网格时，量化误差在深层网络中逐层累积导致性能崩塌。为降低存储开销，PTQ利用少量校准数据优化量化参数，其核心在于最小化分布失真。线性PTQ采用均匀网格，硬件实现仅需移位与加法，但面对LLM中常见的钟形或长尾分布，均匀网格在关键大值区域步长过粗，导致精度损失。对数PTQ采用指数间隔网格，非均匀特性更贴合权重分布，且基于2的幂次量化可用移位器替代乘法器，显著提升硬件能效。

现有对数PTQ方法如Log2、Log√2及动态对数（DLog）虽优化了基的选择，但存在三个结构性缺陷：一是量化网格固有对称性，无法捕捉LLM权重分布的不对称性；二是对离群值高度敏感，极端值迫使量化范围扩大，降低有效精度；三是普遍采用RTN策略，该策略在对数域中因映射非线性、舍入不可导及混合基离散性，无法像线性域中的可学习舍入（如AdaRound）那样通过梯度优化最小化任务损失。LogART的切入点在于解决对数域可学习舍入的不可导性，并引入离群值感知、非对称及多基动态量化机制，突破传统对数PTQ在超低比特下的性能瓶颈。

## 核心方法

### 方法参照系

LogART属于PTQ算法优化路线，其标准流程为：基于校准数据计算量化参数（缩放因子、零点），将权重映射至离散网格，并评估重建误差。与线性PTQ不同，对数PTQ的量化网格非均匀且基可动态变化，导致传统基于梯度的舍入优化无法直接应用，需设计针对对数域特性的可学习机制。

### 可学习对数舍入（LLR）

传统对数PTQ使用RTN函数 $\lfloor \cdot \rceil$ 进行舍入，该函数不可导且非任务感知。LogART将RTN替换为向下取整 $\lfloor \cdot \rfloor$，并引入可学习变量 $\mathbf{R}$ 决定每个权重是舍入至下方还是上方网格点。软量化权重 $\hat{\mathbf{W}}$ 表示为：

$$ \hat{\mathbf{W}} = \text{sgn}(\mathbf{W}) \odot 2^{\lfloor \log_2 |\mathbf{W}| \rfloor + \sigma(\mathbf{R})} $$

其中 $\sigma(\mathbf{R})$ 为Sigmoid函数，$\mathbf{R}$ 通过最小化任务损失 $L(\cdot)$ 与正则项 $\lambda \sum \sigma(\mathbf{R})(1-\sigma(\mathbf{R}))$ 进行优化。正则项鼓励 $\sigma(\mathbf{R})$ 趋向0或1，实现硬舍入的软近似。这一设计解决了RTN在对数域中无法通过反向传播优化任务损失的问题，使舍入决策与模型性能直接关联。

### 优化超参数搜索（OHS）与硬件近似

LLR优化了局部舍入误差，但全局性能依赖量化超参数（基配置、缩放因子、边界）。OHS采用三级搜索策略：张量级非对称边界搜索（ABS）基于权重最大最小值确定非对称边界 $l_a$，无需校准；块级缩放因子搜索（SFS）与块级动态基搜索（DBS）联合优化，最小化块级重建误差 $\min_{s_{of}, n_1, n_2} \| L(\Delta \mathbf{W}, \mathbf{X}) \|_F^2$。DBS自适应分配基-2与基-√2代码比例 $n_1:n_2$，SFS优化离群值感知缩放因子 $s_{of}$。为提升硬件效率，HAF将√2乘法替换为K项符号二进展开（SDE）移位加法：

$$ \sqrt{2} \approx \sum_{k=0}^{K-1} b_k 2^{-k} $$

HAF在OHS与LLR优化过程中引入，使硬件近似误差作为噪声被学习过程吸收，避免了后处理近似导致的精度损失。

## 实验评估

实验在OPT、LLaMA系列LLM及ResNet、MobileNetV2、ViT、DeiT等CNN/ViT模型上进行，聚焦3-4比特权重量化。基线覆盖线性PTQ（GPTQ, BRECQ, AdaRound, AffineQuant, aespa）与对数PTQ（LogNet, SLogII, AdaLog），但未包含QuIP#、AWQ等基于旋转或激活感知的LLM专用SOTA方法，限制了在极低比特LLM场景下的全面对比。

| 模型 | 方法 | PPL (WikiText-2) | 运行时间 | 显存 (GB) |
| :--- | :--- | :--- | :--- | :--- |
| LLaMA2-7B | FP16 | 5.47 | - | - |
| LLaMA2-7B | GPTQ | 8.66 | 10.4 min | 8.28 |
| LLaMA2-7B | BRECQ | OOM | OOM | OOM |
| LLaMA2-7B | LogART | 6.31 | 1.24 hr | 20.8 |
| MobileNetV2 | FP16 | - | - | - |
| MobileNetV2 | AdaRound | 69.46 | 17.6 min | - |
| MobileNetV2 | LogNet | 1.22 | 0.0 min | - |
| MobileNetV2 | LogART | 71.62 | 2.6 min | - |

LogART在LLaMA2-7B 3-bit下PPL为6.31，优于GPTQ的8.66，但BRECQ因显存溢出（OOM）无法对比；在MobileNetV2 4-bit下Top-1准确率为71.62%，显著优于AdaRound的69.46%和对数基线LogNet的1.22%。消融实验显示，SFS与LLR贡献最大，SFS将LLaMA2-7B PPL从9.74降至6.24，LLR相比RTN带来显著精度提升，DBS单独应用时PPL降低过半，ABS无需校准即提供稳定增益。

评估边界存在局限：实验仅覆盖3-4比特权重量化，未验证2比特以下极低比特场景；LLM实验未对比旋转类方法，无法排除分布重塑对精度的贡献；硬件评估仅基于算术单元（AE）面积与功耗，未涉及端到端推理延迟与能效。代码已开源，超参数（如500次迭代、Adam优化器、余弦退火学习率）明确，可复现性较高。

## 关联研究分析

从问题动机看，LogART与GPTQ、AWQ等线性PTQ方法在离群值处理上存在根本差异。GPTQ依赖Hessian矩阵二阶补偿，AWQ通过激活感知缩放保护敏感通道，两者均假设权重分布可通过线性变换或局部补偿优化。LogART则从量化网格结构入手，利用对数域非均匀特性直接适配分布，并通过OHS中的SFS实现离群值感知缩放。这种差异源于对数PTQ的硬件效率优势（无乘法器），但LogART未结合激活量化，与SmoothQuant等W4A4联合量化方法相比，在激活离群值处理上缺乏协同机制，可能限制其在W4A4场景下的性能。

从方法设计看，LogART与AdaRound同属可学习舍入路线，但AdaRound针对线性域设计，其Sigmoid舍入函数依赖线性网格的均匀性。LogART将舍入迁移至对数域，解决了非线性映射下的梯度不可导问题，但引入了动态基搜索的复杂性。与DLog相比，DLog依赖复杂的超参数搜索优化基分配，LogART通过OHS的块级联合优化简化了搜索过程，并引入HAF将硬件约束纳入优化。LogART的HAF设计在优化过程中吸收近似误差，而DLog等方法的硬件近似通常在量化后处理，导致精度损失。这种设计差异表明，LogART在硬件友好性上更优，但其对数域舍入在2比特以下的表现是否优于线性可学习舍入，论文未提供证据。

## 总结

LogART旨在解决对数PTQ中对称网格、离群值敏感及RTN次优性的矛盾，切入点在于对数域可学习舍入的不可导性。通过LLR实现任务感知舍入，OHS优化动态基与缩放因子，HAF吸收硬件近似误差，LogART在3-4比特权重量化下实现了精度与效率的平衡。实验证明其在LLaMA2-7B 3-bit下PPL为6.31，MobileNetV2 4-bit下Top-1准确率为71.62%，优于线性与对数基线。其边界在于未验证2比特以下极低比特场景，且未结合激活量化，限制了在W4A4联合量化中的应用。当比特宽度降至2比特以下时，对数域可学习舍入的精度下限是否仍优于线性可学习舍入，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94846037)