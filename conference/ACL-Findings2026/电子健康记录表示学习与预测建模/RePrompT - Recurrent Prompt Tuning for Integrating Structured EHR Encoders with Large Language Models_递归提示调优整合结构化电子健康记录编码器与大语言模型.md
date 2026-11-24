# ACL-Findings2026最新论文 ｜RePrompT: Recurrent Prompt Tuning for Integrating Structured EHR Encoders with Large Language Models ｜递归提示调优整合结构化电子健康记录编码器与大语言模型

研究机构：美国堪萨斯大学

作者：Arya Hadizadeh Moghaddam、Drew Ross、Mohsen Nayebi Kerdabadi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17725)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17725)

> 大语言模型（LLM）在处理结构化电子健康记录（EHR）时面临时序结构丢失与群体模式缺失的双重困境，导致其难以捕捉临床轨迹的纵向依赖与跨患者共性。现有方法要么依赖文本线性化而忽略时间维度，要么孤立推理而无法利用群体统计特征。RePrompT 通过状态递归提示与结构编码提示的双软提示机制，在不修改 LLM 架构的前提下实现了时序感知与群体对齐。该方法在 MIMIC-III/IV 上优于传统 EHR 基线，但精度显著低于当前 SOTA，且缺乏对知识图谱等外部语义增强的利用，其临床部署价值仍受限于骨干模型能力与融合机制的瓶颈。

## 研究背景

当 LLM 接收由多次就诊记录拼接而成的纯文本输入时，模型将整段输入视为单一文档处理，导致就诊间的时间依赖关系被稀释。这种文本线性化不仅模糊了临床代码的离散身份，更使得模型无法区分“慢性肾病导致后续心血管疾病”这类纵向因果链条。为解决此问题，提示调优（Prompt Tuning）通过引入可训练的连续向量（软提示）引导 LLM 行为，但其标准形式仅针对静态任务，缺乏对时序状态的显式建模。

EHR 预测的主流路线分为两类：一是基于循环神经网络或 Transformer 的序列模型（如 RETAIN、BEHRT），擅长捕捉时序动态但缺乏通用语义推理能力；二是基于 LLM 的推理框架，具备强大的上下文理解能力但难以处理高维稀疏的结构化代码。前者在 MIMIC-IV 死亡率预测中可达 0.809 AUROC（据领域综述），后者在零样本场景下表现优异但缺乏任务对齐的共享表示空间。RePrompT 的切入点在于弥合这两类方法的鸿沟：它不将 LLM 视为独立的推理引擎，而是将其作为结构化 EHR 编码器的“解释器”，通过软提示注入群体训练得到的任务对齐嵌入，同时通过递归机制保留时序状态。

## 核心方法

### 方法参照系

本文问题属于“LLM 与结构化数据协同”路线。标准流程是将 EHR 序列编码为嵌入，再通过全量微调或 LoRA 适配 LLM。本文的关键差异在于冻结 LLM 参数，仅优化提示层，并将 EHR 编码器嵌入转化为可训练的软提示，而非直接拼接输入。

### 状态递归提示调优

标准 LLM 推理将多次就诊视为单一长文本，缺乏显式的时间步分离机制。RePrompT 引入状态递归机制，将 LLM 在 $t-1$ 步的隐藏状态作为 $t$ 步的软提示输入，实现时序信息的显式传递。具体而言，对 $t-1$ 步的隐藏状态 $\mathbf{H}_{i,t-1}$ 进行平均池化得到就诊级状态 $\hat{\mathbf{H}}_{i,t-1}$，再通过线性变换生成软提示 $\mathbf{G}_{i,t}$：

$$ \mathbf{G}_{i,t} = \mathbf{W}_t \hat{\mathbf{H}}_{i,t-1} + \mathbf{b}_t $$

该公式的物理含义是将上一就诊的语义状态压缩为固定维度的向量，作为当前就诊推理的“记忆”输入。这一设计解决了文本线性化中时间边界模糊的问题，使 LLM 能显式区分不同就诊的上下文，从而捕捉疾病进展的纵向依赖。

### 结构编码提示调优

LLM 孤立推理无法利用群体统计特征，而传统 EHR 编码器（如 RETAIN）虽能学习共享表示空间，但其嵌入与 LLM 的语义空间未对齐。RePrompT 采用 RETAIN 编码器将患者历史编码为密集表示 $\mathbf{S}_{i,t}$，并将其作为另一组软提示注入 LLM：

$$ \mathbf{P}_{i,t} = [\mathbf{G}_{i,t}; \mathbf{S}_{i,t}; \text{Embedding}(\hat{\mathbf{C}}_{i,t})] $$

其中 $\hat{\mathbf{C}}_{i,t}$ 为 DeepSeek 生成的患者摘要。该公式将时序状态、群体嵌入与文本摘要拼接为统一输入，使 LLM 在推理时同时访问个体时序动态与群体共性模式。这一设计解决了 LLM 缺乏任务对齐表示空间的问题，使临床相似患者在嵌入空间中占据邻近区域，提升了预测的泛化能力。

## 实验评估

实验在 MIMIC-III 和 MIMIC-IV 上进行，任务为再入院与死亡率预测，指标为 AUROC 和 PRAUC。基线覆盖 Deepr、RETAIN、GRAM 等经典 EHR 模型及 Zero-Shot、Prompt-Tuning 等 LLM 方法，但缺失 MedCPI、Structure-Aware Set Transformers 等当前 SOTA 方法。

| 方法 | MIMIC-IV 再入院 AUROC | MIMIC-IV 死亡率 AUROC | MIMIC-III 再入院 AUROC | MIMIC-III 死亡率 AUROC |
| :--- | :--- | :--- | :--- | :--- |
| RETAIN | 0.670 | 0.601 | 0.660 | 0.608 |
| StageNet | 0.656 | 0.664 | 0.676 | 0.671 |
| RePrompT | 0.706 | 0.673 | 0.688 | 0.646 |

RePrompT 在 MIMIC-IV 再入院任务上以 0.706 AUROC 领先 RETAIN 的 0.670，但在 MIMIC-III 死亡率任务上仅 0.646，低于 StageNet 的 0.671。据领域综述，MedCPI 在 MIMIC-IV 死亡率预测中达 0.809 AUROC，RePrompT 的 0.673 显著落后，表明其融合机制在稀疏数据场景下存在瓶颈。

消融实验显示，移除状态递归模块导致性能下降幅度最大，验证了时序显式建模的核心作用；移除结构编码模块则导致 MIMIC-III 死亡率 PRAUC 从 0.152 降至 0.148，表明群体嵌入对长尾任务的贡献有限。

评估协议采用 70/30 随机划分，报告三次运行均值，但未提供置信区间。代码已开源，使用 Llama 3.1 1B 与 DeepSeek-V3，硬件为 3 块 NVIDIA A6000 GPU。指标仅包含 AUROC/PRAUC，缺乏校准度与临床效用评估，且未报告计算效率指标，限制了其在实时临床决策中的部署可行性分析。

## 关联研究分析

从问题动机看，RePrompT 与 COCONUT 均采用软提示机制，但 COCONUT 聚焦于链式思维推理，缺乏对时序状态的显式传递。RePrompT 通过状态递归机制解决了 COCONUT 在纵向依赖建模上的不足，但其性能仍低于 MedCPI，根源在于后者引入了任务引导的知识图谱增强，而 RePrompT 仅依赖 RETAIN 的通用嵌入，缺乏对罕见病或长尾分布的语义覆盖。

从方法设计看，RePrompT 与 Structure-Aware Set Transformers 均处理不规则时序数据，但后者采用集合 Transformer 架构，通过时间偏差与变量类型偏差的软注意力显式建模事件间依赖，在 MIMIC-IV 死亡率预测中达 0.9164 AUROC。RePrompT 依赖 LLM 的自注意力机制，虽具备通用语义能力，但在捕捉细粒度临床语义依赖上不如专用架构，且冻结 LLM 参数限制了其对复杂临床逻辑的深度适配。

## 总结

RePrompT 试图解决 LLM 处理结构化 EHR 时时序丢失与群体模式缺失的矛盾，通过状态递归与结构编码的双软提示机制，在不修改 LLM 架构的前提下实现了时序感知与群体对齐。实验证明其在 MIMIC-IV 再入院任务上优于 RETAIN（0.706 vs 0.670 AUROC），但在 MIMIC-III 死亡率任务上落后于 StageNet（0.646 vs 0.671 AUROC），且显著低于当前 SOTA MedCPI（0.809 AUROC）。其边界在于：冻结 LLM 参数限制了模型对复杂临床逻辑的深度适配，且缺乏知识图谱等外部语义增强，导致在稀疏数据场景下性能受限。当支持集增大或引入任务特定知识时，状态递归机制的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17725)