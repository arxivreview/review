# ACL2026最新论文 ｜Survey Response Generation: Generating Closed-Ended Survey Responses In-Silico with Large Language Models ｜封闭式调查响应生成机制的系统性评估

研究机构：德国慕尼黑大学、美国马里兰大学帕克分校

作者：Georg Ahnert、Anna-Carolina Haensch、Barbara Plank 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a7e1dd89c92e)

> 利用大语言模型（LLM）模拟人类封闭式调查响应时，从开放文本到封闭选项的映射存在显著偏差，且缺乏标准提取协议。现有研究多关注Persona构建或群体分布对齐，却忽视了响应生成机制本身对保真度的系统性影响。本文通过对比8种生成方法在4个政治态度数据集上的表现，确立了受限生成（Restricted Generation）为最佳实践。该工作填补了底层生成机制的评估空白，但其结论是否适用于非政治领域或长尾群体，仍存疑。

## 研究背景

当LLM被提示预测特定个体的投票选择时，其输出往往是开放式的自然语言，而真实调查数据要求封闭式的选项匹配。这种模态差异导致直接解析文本或提取Token概率时，模型倾向于回归高频模式，产生A-bias（选项A偏好）或响应趋同。为量化这种偏差，需定义个体级对齐（Individual-Level Alignment）与子群体级对齐（Subpopulation-Level Alignment），前者衡量单个预测与真实标签的匹配度，后者衡量模拟群体分布与真实人口分布的统计距离。

传统社会模拟研究（如Argyle et al., 2023）确立了基于Persona提示的范式，但默认使用首Token概率或简单文本解析，未深入探究不同提取机制对结果的影响。现有方法在个体预测精度上存在瓶颈，且缺乏统一的评估标准来区分是Persona质量不足还是生成机制缺陷导致的误差。本文切入点在于将“响应生成机制”从黑盒中剥离，作为独立变量进行系统性控制与对比，旨在识别哪种机制能最忠实地将LLM的潜在知识映射为封闭选项。

## 核心方法

### 生成机制分类体系

本文问题属于社会调查模拟中的响应提取环节，与通用分类任务的关键差异在于：LLM需同时处理Persona上下文与封闭选项约束，且缺乏显式标签监督。参照系为标准的提示工程流程，即输入Persona与问题，输出响应。本文将其细分为三类：基于Token概率的方法（直接读取输出概率）、受限生成方法（通过JSON Schema限制词表）、开放生成方法（先开放生成再分类）。

### 受限生成与概率言语化

针对Token概率法在小模型上失效且易产生无效响应的问题，本文引入受限生成机制。其核心在于动态定义JSON Schema，强制LLM仅输出有效选项或概率分布。对于Restricted Choice方法，模型被约束输出单一选项；对于Verbalized Distribution方法，模型被约束输出所有选项的概率分布。

$$
P_{sim}(y|\mathbf{x}) = \text{Parse}_{JSON}(\text{LLM}(\mathbf{x}, \text{Schema}))
$$

该公式表示模拟响应分布 $P_{sim}$ 是通过解析LLM在受限Schema下输出的JSON结构获得的，而非直接读取原始Token概率。这一设计解决了开放生成中解析歧义与Token概率中分布截断的问题，确保了输出格式的可解析性与选项的合法性。

### 子群体分布对齐评估

为超越个体级F1分数，本文引入子群体级对齐评估。对于分类选项，使用总变差距离（Total Variation Distance, TVD）；对于序数选项，使用1-Wasserstein距离。

$$
D_{subpop} = \frac{1}{|S|} \sum_{s \in S} \text{Dist}(P_{sim}^{(s)}, P_{human}^{(s)})
$$

其中 $S$ 为子群体集合，$\text{Dist}$ 为TVD或Wasserstein距离。该指标衡量模拟群体在宏观统计特征上与真实人口的偏差，弥补了个体级评估无法捕捉群体分布保真度的缺陷。

## 实验评估

实验覆盖ANES 2016、GLES 2017/2025及ATP 2021四个数据集，使用10个开源LLM（Llama 3, OLMo 2, Qwen 3）。基线包括Token概率法、受限生成法及开放生成法，但未包含基于微调（SFT）或强化学习（RL）的方法（如HumanLM）。

| 方法 | ANES F1系数 | GLES 2017 F1系数 | GLES 2025 F1系数 | ATP 2021 F1系数 |
| :--- | :--- | :--- | :--- | :--- |
| First-Token Probabilities | 0.34 | 0.23 | 0.27 | - |
| Restricted Choice | 0.18 | 0.49 | 0.74 | 0.015 |
| Verbalized Distribution | 0.07 | 0.41 | 0.60 | 0.011 |
| Open-Ended Classification | 0.20 | 0.54 | 0.76 | 0.037 |

注：系数为OLS回归中相对于First-Token Probabilities的增量，*表示p<0.05。

数据表明，Restricted Choice在GLES 2025上表现最优（系数0.74），显著优于Token概率法。Open-Ended Classification在个体级对齐上略胜，但计算成本更高。消融实验显示，推理输出（Reasoning）并未提升对齐度，甚至在部分情况下降低性能，挑战了“长思维链提升精度”的假设。

评估边界方面，本文未报告计算成本，且仅聚焦政治态度领域。可复现性受限于开源模型版本与提示模板，代码未公开。指标完备性上，TVD与Wasserstein距离未涵盖因果推断有效性，仅反映统计分布匹配。

## 关联研究分析

从问题动机看，本文与Population-Aligned Persona Generation（Hu et al., 2025）形成互补。后者关注Persona构建时的分布对齐，确保合成Persona符合真实人口分布；本文则关注给定Persona后，如何从LLM提取响应。两者差异根源在于任务阶段不同：前者解决“输入偏差”，后者解决“输出偏差”。若Persona本身存在分布偏差，本文的生成机制优化无法弥补，这暗示了端到端校准的必要性。

从方法设计看，本文的Restricted Choice与Meister et al. (2025)的Verbalized Distribution结论一致，均支持概率言语化优于直接Token概率。但本文扩展至个体级评估，发现Open-Ended Classification在个体F1上略优，而在子群体分布上Verbalized Distribution更稳。这一差异可能源于政治态度任务的特性：个体预测依赖细粒度属性匹配，而群体分布依赖整体概率校准。查询侧增强（如更复杂的Persona描述）在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文核心矛盾在于LLM开放文本生成与封闭式调查响应需求间的模态错位。其切入点是将生成机制作为独立变量，通过受限JSON Schema强制结构化输出，解决了Token概率法的分布截断与开放生成法的解析歧义。实验证明Restricted Choice在GLES 2025上F1系数达0.74，显著优于基线，且推理输出无效。边界在于仅验证政治态度领域，未涵盖长尾群体或因果推断场景。当Persona属性信息量有限时，生成机制的优化上限是否受限于LLM的内在刻板印象，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_a7e1dd89c92e)