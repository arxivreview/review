# CVPR2026最新论文 ｜Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model ｜文本提示驱动的统一源自由无监督域适应框架

研究机构：美国东北大学

作者：Yulong Shi、Shijie Li、Ziyi Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05012)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05012)

> 临床部署中，医学影像模型面临多模态、多解剖目标的分布偏移，而隐私法规禁止访问源数据，传统源自由无监督域适应（Source Free Unsupervised Domain Adaptation, SFUDA）方法因依赖源模型自预测，在大域差距下陷入确认偏置失效。现有VFM引导方法依赖空间提示，其噪声源于源模型低质量预测，形成错误传播链条。本文通过LLM正则化文本提示驱动VFM生成高保真伪标签，并引入视觉合理性精炼，构建了覆盖10个适应方向、22个解剖目标的统一框架。该框架在极端模态差距下接近监督上限，但VFM预训练分布与目标域设备差异的潜在偏差未被量化。

## 研究背景

医学影像的域偏移源于扫描设备与模态的物理差异，如MRI与CT的强度分布存在系统性偏差。这种偏差导致源模型在目标域上预测失效，而源自由约束禁止访问源数据，使得传统无监督域适应（Unsupervised Domain Adaptation, UDA）的分布对齐策略不可行。源模型在目标域上的自预测噪声会累积，形成确认偏置，这是SFUDA的核心失效机制。

SFUDA的主流路线包括自训练、知识蒸馏与数据合成，但均针对低差距、特定解剖目标设计，缺乏跨模态统一性。视觉基础模型（Vision Foundation Model, VFM）的引入提供了外部语义先验，但空间提示型VFM（如MedSAM）依赖源模型预测生成提示，在大域差距下提示噪声导致伪标签质量崩塌。本文切入点在于：文本提示型VFM（如BiomedParse）可解耦提示质量与源模型预测，但临床提示的语法歧义与语义漂移仍制约其泛化能力。

## 核心方法

### 方法参照系

VFM引导SFUDA的标准流程为：利用VFM生成目标域伪标签→自训练源模型→推理。本文问题与该流程的关键差异在于：提示输入的非标准化导致VFM文本编码器嵌入不一致，且源模型预测的解剖不可靠性未被后处理校正。

### 上下文感知提示正则化（CAPR）

CAPR解决提示语法歧义导致的VFM嵌入漂移问题。传统方法直接使用原始提示，其内部上下文（如模态、解剖区域）缺失导致语义漂移。CAPR利用大语言模型（Large Language Model, LLM）执行全局上下文推理，将任意提示解析为规范格式：[目标] in [解剖部位] [模态]。该过程通过元提示指令LLM识别共享上下文，纠正拼写错误并富化子提示，确保VFM文本编码器接收结构化输入。CAPR的改进价值在于切断提示噪声向伪标签的传播路径，使VFM在混乱提示下仍能生成高保真分割。

### 视觉合理性精炼（VPR）

VPR解决源模型预测中解剖不可靠区域的残留问题。传统方法直接输出源模型预测，其边界错误源于域偏移导致的特征失配。VPR利用BiomedParse预计算的Beta分布统计先验，对每个预测连通分量计算解剖合理性分数：

$$S(p_i) = \prod_{k=1}^{4} \frac{\Gamma(\alpha_k + \beta_k)}{\Gamma(\alpha_k)\Gamma(\beta_k)} f_{i,k}^{\alpha_k-1}(1-f_{i,k})^{\beta_k-1}$$

其中 $f_{i,k}$ 为分量 $p_i$ 的第 $k$ 个视觉特征（像素概率或RGB通道均值），$\alpha_k, \beta_k$ 为类别 $C$ 的Beta分布参数。最终预测仅保留分数 $S(p_i) > \tau$ 的分量，阈值 $\tau = \mu_S - 2\sigma_S$ 为所有分量分数的均值减两倍标准差。VPR的改进价值在于将预测重新锚定在目标图像的低层视觉特征上，移除与解剖先验不一致的噪声区域。

## 实验评估

实验覆盖AMOS、BraTS、CAMUS、ACDC、Kvasir、CVCDB六个数据集，10个适应方向。基线包括UPL、ProtoContra、IAPC（传统SFUDA）与DFG、IPLC、SRPL（VFM引导），缺失纯自训练SOTA（如SHOT变体）及联邦SFDA方法。在AMOS MR→CT方向，Tell2Adapt平均DICE达88.2%，接近监督上限88.4%，显著超越最佳基线SRPL的19.9%。

| 适应方向 | 方法 | mDICE (%) |
|---|---|---|
| MR→CT | Ours | 88.2±7.1 |
| MR→CT | SRPL | 19.9±22.9 |
| CT→MR | Ours | 82.3±12.9 |
| CT→MR | SRPL | 19.6±24.8 |

消融实验显示CAPR是核心组件：移除CAPR后，混乱提示下mDICE从85.7%降至48.9%（MR→CT），降幅36.8%；VPR移除导致mDICE下降3.2%（MR→CT）。CAPR的双重作用（纠正与优化）在正常提示下仍带来2.5%的mDICE增益，表明其不仅去噪还优化语义对齐。

评估指标为DICE与ASD，未报告计算效率（训练/推理时间、GPU内存）。代码开源，但VFM（BiomedParse）与LLM（Qwen3-VL8B-Instruct）的预训练数据分布未披露，无法量化其与目标域设备差异的影响。

## 关联研究分析

从提示机制看，IPLC与SRPL依赖空间提示，其噪声源于源模型预测的解剖不可靠性，形成错误传播链条；本文采用文本提示，解耦提示质量与源模型预测，但文本提示的语义歧义需CAPR正则化。这一差异源于任务特性：空间提示要求像素级精度，而文本提示仅需语义级对齐，后者对域偏移更鲁棒。

从后处理机制看，SymmAdapt使用流匹配修正特征，本文使用VPR基于统计先验过滤预测分量。SymmAdapt针对单一模态（BraTS），本文针对多模态统一适应。VPR的Beta分布先验依赖BiomedParse预训练数据，若目标域设备分布与预训练数据差异极大，先验可能失效。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

Tell2Adapt解决的核心矛盾是：源自由约束下，源模型自预测噪声导致的大域差距适应失效。其切入点在于文本提示VFM解耦提示质量与源模型预测，CAPR正则化提示歧义，VPR校正解剖不可靠性。该框架在10个方向22个目标上达到SOTA，MR→CT mDICE 88.2%接近监督上限88.4%。其边界在于：VFM预训练数据分布与目标域设备差异未被量化，CAPR依赖LLM推理的计算延迟未报告。当目标域设备分布与BiomedParse预训练数据差异极大时，VPR的Beta分布先验是否仍具解剖合理性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05012)