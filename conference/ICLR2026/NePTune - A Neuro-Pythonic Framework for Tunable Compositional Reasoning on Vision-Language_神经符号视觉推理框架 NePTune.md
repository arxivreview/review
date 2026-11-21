# ICLR2026最新论文 ｜NePTune: A Neuro-Pythonic Framework for Tunable Compositional Reasoning on Vision-Language ｜神经符号视觉推理框架 NePTune

研究机构：美国密歇根州立大学

作者：Danial Kamali、Parisa Kordjamshidi

论文原文见 [arXiv](https://arxiv.org/abs/2509.25757)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25757)

> 视觉-语言模型（Vision-Language Model, VLM）在处理复杂组合查询时，常因内部语言先验干扰逻辑判断而失效。现有神经符号方法要么依赖硬逻辑导致误差级联，要么受限于训练域谓词集无法零样本泛化。NePTune 通过 LLM 动态生成 Python 程序，结合可微分软逻辑算子，将感知与推理物理隔离。该框架在域偏移任务上显著优于端到端模型，但在标准基准上未超越强骨干，其软逻辑在真实场景中的鲁棒性存疑。

## 研究背景

当 VLM 面对“是否有棕色物体在每个红色球体后面”这类查询时，需分解为原子概念并执行关系推理。然而，Transformer 架构的端到端训练使模型倾向于匹配统计模式而非执行逻辑组合，导致在未见过的概念组合上性能骤降。这种失效源于感知与认知的耦合：视觉编码器提取的特征直接参与语言生成，使得语言先验在仲裁过程中覆盖视觉证据，造成“正确预测但错误理由”的幻觉。

神经符号（Neuro-Symbolic, NeSy）方法试图通过显式程序解决此问题。VisProg 和 ViperGPT 利用大语言模型（Large Language Model, LLM）生成命令式代码，但依赖硬逻辑决策，早期感知错误会级联放大导致全链失败。LEFT 和 NeSyCoCo 采用可微分声明式推理，支持全局优化，但谓词集受限于训练数据，缺乏零样本能力。NePTune 的切入点在于结合两者的优势：利用 LLM 生成 Python 程序实现动态谓词扩展，同时引入软逻辑算子处理 VLM 输出的不确定性，从而在保持零样本泛化能力的同时避免硬逻辑的脆弱性。

## 核心方法

### 方法参照系

NePTune 属于神经符号视觉推理框架，标准流程为“语义解析-感知接地-符号执行”。与 ViperGPT 等纯命令式方法不同，NePTune 在执行阶段引入模糊逻辑，与 LEFT 等声明式方法不同，其谓词无需预训练，而是通过 VLM 实时打分获取。

### 混合执行模型

针对 ViperGPT 硬逻辑导致的误差级联问题，NePTune 在符号执行器中引入软组合推理。传统方法将 VLM 输出二值化为 True/False，而 NePTune 保留连续概率分数，通过重载 Python 运算符实现模糊逻辑。对于合取操作，采用元素级最小值作为 t-范数：

$$ \text{score}_{\text{and}}(x) = \min(\alpha_x, \beta_x) $$

其中 $\alpha_x, \beta_x$ 为对象 $x$ 的两个原子概念概率。这一设计允许系统在感知不确定时进行平滑推理，而非在阈值处发生突变，从而缓解了单一感知错误导致全链失败的问题。

### 动态谓词接地

针对 LEFT 和 NeSyCoCo 谓词集受限于训练域的瓶颈，NePTune 利用 LLM 生成 Python 程序动态定义谓词。感知接地通过 `score` 接口实现，VLM 对边界框内的对象进行原子概念打分：

$$ s = \frac{\exp(\text{logit}_{\text{Yes}})}{\exp(\text{logit}_{\text{Yes}}) + \exp(\text{logit}_{\text{No}})} $$

该分数作为后续符号推理的输入。由于程序由 LLM 实时生成，NePTune 无需预定义谓词库，即可处理训练数据中未出现的概念组合，实现了零样本组合泛化。

## 实验评估

NePTune 在 CLEVR、CLEVR-Humans、RefCOCO-Adversarial 和 Ref-GTA 上进行了评估。基线覆盖 ViperGPT、VisProg、LEFT、NeSyCoCo 及端到端模型 InternVL2.5-8B。在 CLEVR-Humans 上，NePTune 取得 87.67% 准确率，较 LEFT 提升 30.98%；在 Ref-GTA 域偏移任务上，NePTune 达到 69.69%，而骨干 InternVL2.5-8B 仅 6.95%。

| 基准 | NePTune | InternVL2.5-8B | ViperGPT | LEFT |
| :--- | :--- | :--- | :--- | :--- |
| CLEVR-Humans | 87.67 | 85.95 | 31.05 | 56.69 |
| Ref-GTA | 69.69 | 6.95 | 1.40 | N/A |
| Ref-Adv | 71.57 | 76.13 | 60.66 | N/A |
| CLEVR | 92.65 | 90.25 | 36.05 | 99.50 |

消融实验显示，在 CLEVR-Humans 上，从声明式推理骨干添加 VLM 概念打分提升 12.36%，添加命令式推理再提升 19.19%。值得注意的是，在 Ref-Adv 标准基准上，NePTune（71.57%）低于骨干 InternVL2.5-8B（76.13%），表明解耦架构在分布内任务中可能引入感知损失。

评估边界方面，论文未报告置信区间，且 Ref-GTA 仅使用 1000 样本微调，泛化性验证有限。代码未公开，超参数细节缺失，可复现性依赖 LLM 版本（GPT-4o）的稳定性。

## 关联研究分析

从问题动机看，NePTune 与 ViperGPT 均旨在解决组合推理，但 ViperGPT 依赖硬逻辑，NePTune 引入软逻辑以处理不确定性。这一差异源于 VLM 输出概率的固有噪声：硬逻辑在噪声敏感场景下易失效，而软逻辑通过模糊运算平滑了感知误差。然而，NePTune 在 Ref-Adv 上的性能下降暗示，软逻辑在分布内任务中可能过度平滑了 VLM 的自信预测，导致精度损失。

从方法设计看，NePTune 与 LEFT 均使用可微分推理，但 LEFT 需训练谓词，NePTune 利用 VLM 零样本打分。这一设计使 NePTune 具备跨域泛化能力，但牺牲了谓词学习的精细度。在 Ref-GTA 上，NePTune 的显著优势验证了零样本谓词在域偏移场景下的鲁棒性，但在 CLEVR 上，NePTune（92.65%）仍低于训练后的 LEFT（99.50%），表明软逻辑在合成数据上的精度上限受限于 VLM 的原子概念打分质量。

## 总结

NePTune 旨在解决 VLM 组合推理中感知与逻辑耦合导致的泛化失效。通过 LLM 动态生成 Python 程序与可微分软逻辑的结合，该框架实现了零样本组合推理与域适应。实验证明，在 Ref-GTA 域偏移任务上，NePTune 较骨干提升 62.74%，在 CLEVR-Humans 上较神经符号基线提升 30.98%。然而，在 Ref-Adv 标准基准上，NePTune 性能低于骨干，暴露了解耦架构在分布内任务中的感知损失。当 VLM 原子概念打分存在系统性偏差时，软逻辑的模糊运算是否足以补偿感知误差，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25757)