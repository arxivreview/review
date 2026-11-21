# HuggingFace最新推荐论文 ｜Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation ｜统一离散扩散大语言模型：跨范式蒸馏与自细化扩散

作者：Shufan Li、Hanrong Ye、Greg Heinrich 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.36466)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.36466)

> 导读：统一多模态大语言模型（Unified Multimodal Large Language Models, MLLMs）旨在通过单一架构同时处理视觉理解与生成任务，但现有离散扩散模型（Discrete Diffusion Language Models, DLLMs）在生成质量上显著落后于专用模型。传统掩码扩散模型（Masked Diffusion Model, MDM）缺乏连续流模型的自细化能力，且难以从自回归（Autoregressive, AR）模型中有效蒸馏知识。本文提出NLD-Uni，通过跨范式On-Policy Distillation (OPD) 从AR视觉语言模型和连续流模型中分别蒸馏理解与生成能力，并引入基于Token Age的自细化扩散过程。该工作显著缩小了DLLM与专用模型的性能差距，但其绝对性能仍受限于离散Token化的信息损失，且跨范式蒸馏的上下文对齐机制在复杂推理场景下的鲁棒性有待验证。

## 研究背景

当模型试图在单一架构内同时处理文本与图像时，离散Token化成为连接多模态数据的通用接口。然而，将图像转化为离散Token后，传统的自回归生成面临序列过长导致的推理效率瓶颈，而扩散模型虽支持并行生成，却因缺乏连续空间的平滑过渡机制，导致生成图像在细节保真度上远逊于连续流模型。这一矛盾在统一多模态任务中尤为突出：模型既需要AR模型在文本推理上的逻辑严密性，又需要扩散模型在图像生成上的并行效率，但两者在优化目标和表征空间上的割裂使得联合训练困难重重。

当前统一MLLMs主要分为两类：基于AR的离散Token统一模型和AR+Diffusion的混合架构。前者受限于离散Token的信息损失，生成质量低；后者虽能兼顾两者，但需平衡冲突的优化目标，训练复杂度高。DLLMs作为第三种路线，试图用统一的扩散目标处理所有模态，但其性能瓶颈在于缺乏有效的知识迁移路径——现有的On-Policy Distillation (OPD) 技术主要应用于同范式模型间，难以直接用于从AR教师向DLLM学生的跨范式知识转移。NLD-Uni正是针对这一“跨范式知识迁移失效”与“离散扩散自细化缺失”的双重瓶颈展开研究。

## 核心方法

### 方法参照系：弹性混合Transformer架构

NLD-Uni采用弹性混合Transformer（Elastic Mixture-of-Transformer, Elastic MoT）架构，继承自LaViDa-O。该架构包含理解专家塔和生成专家塔，通过联合注意力机制交互。理解塔初始化为扩散语言模型NLD，生成塔初始化为相同副本。图像输入由语义编码器和向量量化（Vector Quantization, VQ）编码器共同表示，输出仅使用VQ代码。该架构支持弹性加载：理解任务仅加载8B参数，生成任务加载4B理解参数+8B生成参数，交错任务加载全部16B参数。这一设计为后续的跨范式蒸馏提供了统一的参数空间基础。

### 跨范式On-Policy Distillation

传统OPD在同范式模型间效果显著，但直接将其应用于AR教师到DLLM学生会导致上下文不匹配。例如，AR教师基于前文生成“New York”，而DLLM学生在掩码状态下可能预测“New Francisco”，直接复制教师分数会产生错误监督。NLD-Uni提出传递性蒸馏目标，首先用AR OPD损失监督学生的AR视图，再用一致性损失监督学生的扩散视图。

$$
\mathcal{L}_{\text{OPD-und}} = D_{\text{KL}}(p_s^{\text{AR}}(B_i^0|B_{j<i}^0) \| p_t^{\text{AR}}(B_i^0|B_{j<i}^0)) + D_{\text{KL}}(p_s^{\text{AR}}(B_i^0|B_{j<i}^0) \| p_s^{\text{Diff}}(B_i^0|B_{j<i}^0, B_i^t))
$$

该公式第一项为标准AR OPD损失，对齐学生AR分布与教师AR分布；第二项为自一致性损失，对齐学生AR分布与其自身扩散分布。通过停止梯度（stop-grad）处理AR目标，确保扩散视图的学习不干扰AR视图的优化，从而在保留AR逻辑能力的同时，将知识迁移至扩散生成路径。

### 自细化扩散过程

标准MDM中，Token直接从掩码状态跳变至干净状态，缺乏中间细化过程。NLD-Uni引入Token Age $a \in \{0, 1, ..., K\}$，扩展状态空间为 $S = \mathcal{V} \times \mathcal{A}$。Token Age $a=0$ 为干净状态，$a=K$ 为全掩码状态。前向过程定义Token从 $(c, k-1)$ 到 $(c, k)$ 的转移概率 $U_{k|k-1}(u|c)$，通过VQ嵌入空间中的球树（Ball Tree）实现渐进腐蚀。

$$
U_{j|k}(u|c) = \frac{\mathbf{1}\{u \in N_{D-j}(c)\}}{|N_{D-j}(c)|}
$$

该公式定义了Token从年龄 $k$ 到 $j$ 的边际分布，其中 $N_{D-j}(c)$ 表示嵌入空间中半径随年龄增长的球内Token集合。这一设计使Token在生成过程中经历从粗到细的渐进细化，允许模型在推理时对已生成Token进行中间承诺和修正，显著提升了视觉生成质量。

## 实验评估

实验在视觉问答、多模态推理、文本到图像生成及图像编辑等任务上评估NLD-Uni。基线覆盖LLaDa2-Uni、BAGEL等DLLM及AR+Diff模型，但未直接对比顶级模块化VLM（如Qwen-VL）。在图像编辑基准ImgEdit上，NLD-Uni取得4.17的总分，显著高于BAGEL的3.20和LaViDa-O的3.71，表明跨范式蒸馏有效提升了DLLM的编辑能力。

| 方法 | ImgEdit Overall |
| :--- | :--- |
| BAGEL | 3.20 |
| LaViDa-O | 3.71 |
| NLD-Uni-Base | 3.81 |
| NLD-Uni (Ours) | 4.17 |

消融实验显示，自细化扩散过程中的噪声比率 $r$ 对性能影响显著。在图像编辑任务中，$r=0.9$ 时性能最佳（4.17），而 $r=1.0$ 时性能下降至3.90，表明适度的噪声注入有助于教师模型在保留学生输出结构的同时提升视觉保真度。此外，推理速度测试表明，NLD-Uni在扩散模式下通过调整置信阈值，可在保持75.0% MathVista准确率的同时达到552.58 tokens/s，远超AR基线的202.74 tokens/s。

评估边界方面，论文未报告置信区间，且部分基准（如GenEval）的具体数值未在正文表格中完整呈现。可复现性方面，模型与代码已公开，但训练超参数细节（如球树深度 $D$ 的具体选择）需参考附录。

## 关联研究分析

从问题动机看，NLD-Uni与BAGEL均试图统一理解与生成，但BAGEL采用AR+Diffusion混合架构，需平衡两种优化目标，而NLD-Uni通过单一DLLM架构简化了训练目标。NLD-Uni的跨范式蒸馏策略解决了DLLM缺乏强教师的问题，而BAGEL依赖联合训练，受限于数据规模。然而，NLD-Uni的绝对性能仍低于BAGEL在某些生成任务上的表现，暗示离散Token化在生成质量上仍存在固有上限。

从方法设计看，NLD-Uni与OPDLM均使用OPD，但OPDLM限于同模型蒸馏（AR转DLLM），而NLD-Uni扩展至跨范式（AR/Flow到DLLM）。NLD-Uni的自细化扩散过程与MDM-Prime的Token分解策略不同，后者通过子Token分解实现部分掩码，但在高分辨率图像上无法收敛。NLD-Uni利用VQ嵌入空间的几何结构实现渐进细化，避免了子Token表示的复杂性，但查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

NLD-Uni针对DLLM在统一多模态任务中生成质量低和知识迁移难的核心矛盾，提出跨范式OPD和自细化扩散过程。通过从AR VLM和连续流模型中蒸馏知识，并引入Token Age实现渐进细化，NLD-Uni在ImgEdit上取得4.17的SOTA成绩，推理速度达552.58 tokens/s。然而，其性能仍受限于离散Token化的信息损失，且跨范式蒸馏的上下文对齐机制在复杂推理场景下的鲁棒性有待验证。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.36466)