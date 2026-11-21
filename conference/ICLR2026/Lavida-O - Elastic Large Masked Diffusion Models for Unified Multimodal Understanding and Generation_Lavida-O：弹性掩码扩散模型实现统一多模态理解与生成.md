# ICLR2026最新论文 ｜Lavida-O: Elastic Large Masked Diffusion Models for Unified Multimodal Understanding and Generation ｜Lavida-O：弹性掩码扩散模型实现统一多模态理解与生成

研究机构：美国加州大学洛杉矶分校

作者：Shufan Li、Jiuxiang Gu、Kangning Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.19244)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.19244)

> 统一多模态模型旨在单一架构内融合视觉理解与图像生成，但现有自回归（AR）与连续扩散混合架构面临训练目标冲突与推理效率低下的双重瓶颈。Lavida-O 切入点在于采用掩码扩散模型（Masked Diffusion Model, MDM）统一目标，消除 AR 与扩散损失权重调优需求，并通过弹性混合 Transformer（Elastic-MoT）架构降低生成分支参数开销。该方法结合分层采样与规划自反思机制，在 GenEval 与 ImgEdit 基准上超越专用扩散模型，但高分辨率生成保真度仍受限于离散 Token 化信息损失。

## 研究背景

当统一模型需同时处理文本问答与图像编辑时，自回归语言建模与连续扩散去噪在数值尺度与训练动态上存在根本差异。这种目标冲突导致 BAGEL 等 AR+Diff 架构需精细调整损失权重与数据混合比例，而纯自回归统一模型如 Janus 虽简化了目标，却因离散 Token 化丢失高频细节，生成质量远低于专用扩散模型。掩码扩散模型将序列生成形式化为离散空间中的前向掩码与反向去噪过程，提供统一训练目标，但现有 MDM 如 MMaDa 缺乏显式机制利用理解能力增强生成，且无法支持高分辨率图像编辑。

Lavida-O 针对 MDM 在统一多模态任务中的三大瓶颈：大语言骨干训练成本高昂、开源掩码图像生成模型资源匮乏、理解与生成能力缺乏显式协同机制。该工作基于 LaViDa 理解模型扩展，通过 Elastic-MoT 架构将 8B 理解分支与 2.4B 生成分支非对称耦合，引入 4 倍 Token 压缩与渐进式上采样，首次实现 1024px 高分辨率文本到图像合成与指令式图像编辑。与 BAGEL 等数据驱动方法不同，Lavida-O 在推理阶段引入规划与自反思机制，显式利用理解能力指导生成，将“视觉思维”从隐含能力转为可验证的因果增益。

## 核心方法

### 方法参照系

统一多模态模型通常采用 AR+Diff 混合目标或纯 AR 统一目标，前者需平衡两种损失尺度，后者受限于离散 Token 信息损失。Lavida-O 采用 MDM 统一目标，将图像表示为 VQ-Encoder 生成的离散 Token 序列，与文本 Token 在同一掩码扩散框架下联合建模，关键差异在于通过非对称参数分配与推理时规划机制解决理解-生成协同问题。

### Elastic-MoT 非对称架构

Elastic-MoT 解决 MoT 架构参数冗余与训练成本问题。标准 MoT 为图像与文本分配等量参数，导致生成任务需训练至少 8B 新参数。Lavida-O 基于“生成任务容量需求低于理解任务”的观察，将生成分支隐藏维度设为理解分支的 1/3，仅新增 2.4B 参数。在 N 层 Transformer 中，仅前 M 层允许文本与图像 Token 通过联合注意力交互，剩余 K=N-M 层内模态自注意力独立运行，实现任务感知参数激活。该设计使生成分支可冻结理解分支参数，显著降低训练成本，同时通过部分层交互保留跨模态知识迁移能力。

$$
\mathcal{L}_{MDM} = -\mathbb{E}_{t \sim U[0,1], X_0} \left[ \sum_{i=1}^{L} \log p_\theta(X_0^{[i]} | X_t) \right]
$$

该公式定义 MDM 训练目标，其中 $X_t$ 为时间步 $t$ 的掩码序列，$p_\theta$ 预测完整序列 $X_0$ 的每个 Token，通过独立假设分解为逐 Token 条件概率，消除 AR 与扩散损失权重调优需求。

### 规划与自反思生成机制

规划机制解决 MDM 缺乏显式理解-生成协同的问题。在图像编辑任务中，模型首先通过理解分支定位目标对象（如“狗在领带右侧”），生成规划文本（“狗应与领带重叠，需修正”），再基于规划结果执行生成。自反思机制在生成后评估输出质量，若检测到空间关系错误则触发重新生成。该机制将理解能力从被动条件输入转为主动生成指导，在 ImgEdit 基准上使 Replace 类别得分从 4.39 提升至 4.40，Remove 类别从 3.98 提升至 4.05，验证了显式规划对局部理解依赖任务的增益。

$$
C = \text{Concat}(C_i, C_v, C_p)
$$

该公式定义条件嵌入构造，$C_i$ 为 SigLIP 语义嵌入，$C_v$ 为输入图像 VQ Token（编辑任务必需），$C_p$ 为文本提示嵌入，拼接后作为 MDM 反向过程的条件输入，确保编辑任务保留低层细节。

## 实验评估

Lavida-O 在 GenEval、DPG-Bench、RefCOCO 与 ImgEdit 基准上评估，对比 AR 统一模型（BAGEL、Qwen2.5-VL）、连续扩散模型（Flux-dev、SD3-Medium）与 MDM 模型（MMaDa、Muddit）。基线覆盖主要技术路线，但缺失 UniDFlow 等最新离散流匹配模型。

| 方法 | 类型 | GenEval ↑ | DPG-Bench ↑ | FID-30k ↓ |
|---|---|---|---|---|
| Flux-dev | Continuous | 0.68 | 84.0 | 10.15 |
| BAGEL | Continuous | 0.82 | - | - |
| MMaDA | Masked | 0.63 | 53.4 | 32.85 |
| LaViDa-O | Masked | 0.77 | 81.8 | 6.68 |
| +Reflection | Masked | 0.89 | 83.2 | - |

Lavida-O 基础版 GenEval 0.77 超越 MMaDa 0.63，但低于 BAGEL 0.82；启用自反思后达 0.89，超越 BAGEL 与 Flux-dev，FID-30k 6.68 显著优于 Flux-dev 10.15，表明 MDM 在生成保真度上具备竞争力。

| 任务 | RefCOCO val | RefCOCO+ val | RefCOCOg val |
|---|---|---|---|
| Qwen2.5-VL-7B | 92.1 | 89.1 | 86.1 |
| LaViDa-O (4-step) | 94.8 | 92.5 | - |
| LaViDa-O (1-step) | 94.6 | 91.7 | - |

Lavida-O 4 步推理在 RefCOCO val 达 94.8，超越 Qwen2.5-VL-7B 92.1，1 步推理 94.6 仍保持优势，验证 MDM 并行解码在定位任务上的效率优势。ImgEdit 整体得分 3.71，超越 BAGEL 3.20 与 FluxKontext-dev 3.52，Replace 类别 4.39 接近 GPT-4o 4.35，表明理解-生成协同在局部编辑任务上的有效性。

评估边界方面，论文未报告置信区间，GenEval 0.89 与领域综述中 UniDFlow 0.95 存在 0.06 差距，可能源于 MDM 离散化固有缺陷而非架构设计。代码未公开，Elastic-MoT 层数 M 与 K 的具体配置未详细披露，可复现性受限。FID-30k 评估未启用规划机制，因 MJHQ 数据集规模大且 FID 不反映提示遵循能力，该设置差异影响生成质量全面评估。

## 关联研究分析

从问题动机看，Lavida-O 与 BAGEL 均解决理解-生成协同问题，但 BAGEL 依赖数据混合与 AR+Diff 混合目标实现隐含协同，Lavida-O 通过推理时规划机制实现显式因果增益。这一差异根源在于 MDM 统一目标消除了训练阶段目标冲突，使理解能力可在推理阶段被显式调用，而 AR+Diff 架构中两种目标耦合导致理解能力难以独立激活。Lavida-O 在 ImgEdit Replace 类别 4.39 超越 BAGEL 3.30，验证了显式规划对局部理解依赖任务的增益，但论文未分析该增益是否可归因于推理时计算量增加而非架构本身。

从方法设计看，Lavida-O 与 MMaDa 同属 MDM 统一模型，但 MMaDa 采用对称 8B 参数架构且不支持图像编辑，Lavida-O 通过 Elastic-MoT 非对称分配与 VQ Token 压缩实现高效扩展。这一差异源于 Lavida-O 对“生成任务容量需求低于理解任务”的观察，而 MMaDa 未探索参数非对称性。Lavida-O 1024px 高分辨率生成能力超越 MMaDa 512px，但 FID-30k 6.68 仍高于领域综述中 NextFlow 25.228 PSNR 对应的重建质量，表明离散 Token 化在高分辨率生成中仍存在信息损失瓶颈，该瓶颈是否可通过改进 Tokenizer 而非架构设计解决，论文未给出回答。

## 总结

Lavida-O 解决的核心矛盾是 MDM 统一模型中理解与生成能力缺乏显式协同机制及训练成本高昂问题。该工作抓住 MDM 统一目标消除 AR-Diff 损失冲突的特性，通过 Elastic-MoT 非对称架构降低生成分支参数至 2.4B，结合规划自反思机制显式利用理解能力指导生成。实验证明 GenEval 0.89 超越 BAGEL 0.82，RefCOCO val 94.8 超越 Qwen2.5-VL-7B 92.1，验证了 MDM 在统一多模态任务上的竞争力。边界在于 FID-30k 6.68 仍高于连续扩散模型，且 1024px 生成依赖 4 倍 Token 压缩，可能加剧高频细节丢失。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.19244)