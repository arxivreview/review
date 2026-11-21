# CVPR2026最新论文 ｜Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients ｜量化感知积分梯度（QIG）驱动的细粒度LVLM训练后量化

研究机构：北京航空航天大学

作者：Ziwei Xiang、Fanhu Zeng、Hongjian Fang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.17809)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17809)

> 大视觉语言模型（LVLMs）在部署时面临显存与延迟瓶颈，训练后量化（Post-Training Quantization, PTQ）是无需重训练即可降低精度的主流手段。现有LVLM量化方法通常仅在模态层面（视觉vs文本）平衡量化误差，忽略了模态内部不同Token对量化噪声的敏感度差异，导致校准精度受限。本文引入量化感知积分梯度（Quantization-aware Integrated Gradients, QIG），将归因分析从模态级细化至Token级，直接量化每个输入Token对量化误差的贡献以指导缩放因子优化。该方法在多个基准上提升了量化精度，但其增益幅度有限，且未验证在极低比特或动态序列长度下的鲁棒性。

## 研究背景

当LVLM处理多模态输入时，视觉Token与文本Token在Transformer层中混合交互，其激活分布呈现出复杂的异构性。这种异构性不仅体现在模态间（Inter-modality），更体现在模态内（Intra-modality）不同Token之间。传统的量化校准假设同一模态内的Token具有相似的量化敏感度，从而采用统一的缩放因子或模态级权重。然而，激活离群值（Outlier）的存在使得部分Token的数值范围远超其他Token，若强行统一缩放，会导致正常Token的量化精度大幅下降，或离群Token的量化误差被放大。

主流LVLM量化路线如MBQ（Modality-Balanced Quantization）通过梯度重加权来平衡视觉与语言模态的重建误差，解决了模态间的失衡问题。然而，MBQ仍停留在模态粒度，无法捕捉模态内Token级的动态变化。此外，直接应用LLM领域的PTQ方法（如GPTQ、SmoothQuant）到LVLM时，由于缺乏对多模态统计特性的适配，其性能往往不如简单的最近舍入（RTN）基线。这表明，LVLM量化需要一种能直接度量Token级量化敏感性的机制，而非依赖通用的二阶补偿或模态级平衡。

本文的切入点在于利用可解释性中的公理化归因（Axiomatic Attribution）理论，特别是积分梯度（Integrated Gradients, IG），来构建Token级的量化敏感度指标。通过计算从量化输入到真实输入的积分梯度，本文定义了QIG，使其直接反映每个Token对量化误差的贡献，从而在PTQ校准阶段实现细粒度的误差补偿。

## 核心方法

### 方法参照系

本文基于通道级均衡（Channel-wise Equalization, CWE）框架，该框架通过最小化量化前后Transformer块输出的均方误差（MSE）来搜索最优缩放因子。标准CWE对所有Token赋予相同权重，本文的关键差异在于引入Token级重要性系数，重构了MSE的加权形式，以优先保护对量化误差贡献大的Token。

### 量化感知积分梯度（QIG）

标准积分梯度用于解释模型预测，但无法直接关联量化误差。本文修改了归因目标，从解释绝对预测值 $f(x)$ 转为解释量化误差 $f(x) - f(x_q)$，其中 $x_q$ 为量化输入，$f(x_q)$ 为量化模型输出。QIG定义为：

$$
\text{QIG}_i(x) = (x_i - x_{q,i}) \cdot \int_{\alpha=0}^{1} \frac{\partial f(x_q + \alpha(x - x_q), w_q)}{\partial x_i} d\alpha
$$

该公式计算了将第 $i$ 个Token从量化状态恢复至全精度状态时，对模型输出差异的累积贡献。设计动机在于，SFT梯度与量化误差分布不匹配，而QIG直接度量量化噪声的影响，避免了梯度代理的偏差。

### IQR裁剪与加权优化

原始QIG值呈重尾分布，少数极端Token会主导优化过程。本文引入四分位距（Interquartile Range, IQR）裁剪，将超出 $[Q_1 - 1.5\text{IQR}, Q_3 + 1.5\text{IQR}]$ 范围的敏感度值截断，随后归一化得到重要性系数 $\lambda_i$。优化目标变为：

$$
\min_{E} \sum_{i=1}^{T} \lambda_i \| Q_W(W \cdot E) Q_X(X_i / E) - W X_i \|^2
$$

这一设计解决了均匀量化对离群值敏感的问题，通过动态调整每个Token的误差权重，使缩放因子 $E$ 的搜索偏向于保护高敏感度Token，从而在不改变CWE框架的前提下提升了量化精度。

## 实验评估

实验在LLaVA-onevision-7B、Qwen2-VL-7B和InternVL2-8B/26B上进行，评估基准包括VizWiz、MMMU、ChartQA、AI2D和ScienceQA。基线覆盖RTN、GPTQ、AWQ、MBQ和SmoothQuant，但缺失QuIP#等旋转类方法在LVLM上的对比，这可能限制了方法在极低比特下的竞争力评估。

| 模型 | 位宽 | 方法 | VizWiz | MMMU | ChartQA | AI2D | ScienceQA | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LLaVA-onevision-7B | W3A16 | RTN | 59.12 | 43.67 | 68.88 | 78.92 | 94.55 | 69.03 |
| LLaVA-onevision-7B | W3A16 | MBQ | 57.99 | 44.00 | 76.84 | 78.47 | 94.89 | 70.44 |
| LLaVA-onevision-7B | W3A16 | **QIG** | **62.82** | **45.78** | **77.20** | **79.11** | **95.29** | **72.04** |
| InternVL2-8B | W4A8 | RTN | 56.68 | 43.00 | 78.96 | 79.02 | 96.22 | 70.80 |
| InternVL2-8B | W4A8 | MBQ | 57.36 | 45.67 | 78.00 | 79.47 | 96.38 | 71.38 |
| InternVL2-8B | W4A8 | **QIG** | **58.33** | **47.33** | **78.16** | **79.63** | **96.73** | **72.04** |

QIG在W3A16下将LLaVA-onevision-7B的平均准确率从MBQ的70.44%提升至72.04%，增益1.60%；在W4A8下，InternVL2-8B的平均准确率从71.38%提升至72.04%，增益0.66%。消融实验显示，使用量化误差作为归因目标比使用任务输出目标更优，且在LLaVA-onevision-7B W4A8设置下，QIG在ChartQA上达到74.52%，优于基线73.87%。

评估边界方面，论文未报告置信区间，且校准数据仅为128对图像-文本对，样本量较小。代码已开源，但超参数细节（如IQR裁剪系数）未在正文中详细列出，可能影响复现性。此外，实验未涵盖2-bit及以下极低比特场景，QIG在极端压缩下的有效性存疑。

## 关联研究分析

从问题动机看，MBQ通过梯度重加权解决模态间失衡，但假设模态内Token敏感度均一。本文指出这一假设在LVLM中失效，因为视觉Token与文本Token在深层网络中交互后，其敏感度分布呈现高度异质性。MBQ的梯度信号来自SFT损失，与量化误差分布存在偏差，而QIG直接基于量化误差归因，避免了这种代理偏差。这一差异源于任务特性：LVLM的量化误差不仅取决于权重分布，还取决于输入Token的语义重要性，模态级平衡无法捕捉这种细粒度动态。

从方法设计看，SmoothQuant通过数学等价变换迁移离群值难度，适用于LLM的W8A8量化，但在LVLM的W4A8设置下，其性能甚至不如RTN。这表明，单纯依赖激活统计的缩放策略在多模态场景下缺乏鲁棒性。QIG通过引入Token级归因，将量化误差补偿从“全局统计”转向“局部语义”，这与QuIP#等旋转方法不同，后者通过全局变换重塑分布，而QIG通过局部权重调整保护关键Token。这种局部调整策略在计算开销上更低，但可能无法处理全局分布畸变，其在长序列或复杂推理任务中的表现有待验证。

## 总结

本文针对LVLM量化中模态内Token敏感度差异被忽略的问题，提出QIG方法，通过积分梯度直接度量Token对量化误差的贡献，并引入IQR裁剪稳定优化过程。实验证明，QIG在W3A16和W4A8设置下均优于MBQ和RTN，其中LLaVA-onevision-7B W3A16平均准确率提升1.60%。然而，论文未验证QIG在2-bit及以下极低比特下的表现，且校准数据量较小，限制了结论的泛化性。当序列长度增加或输入包含更多异构模态时，QIG的归因计算复杂度是否会成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17809)