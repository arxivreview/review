# HuggingFace最新推荐论文 ｜Editing Images into Reusable Layers via Compositional Edit-Prior Distillation ｜指令式图像编辑中的可复用图层生成

作者：Wen Xue、Yong Liu、Xueheng Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.24738)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.24738)

> 指令式图像编辑旨在通过自然语言指令修改图像特定区域，同时保持非编辑区域一致。现有模型多输出扁平化图像，导致后续局部修改需重复生成，易引发边界伪影与内容意外变更。本文提出LayerEditor，将指令编辑与可复用RGBA图层生成统一建模，通过In-Context RGB-Alpha Token Modeling在单一序列中联合表示编辑画布与有序图层，并引入Compositional Edit-Prior Distillation (C-EPD) 防止分层适配导致的编辑能力退化。该工作填补了“编辑后分层”的空白，但其自建基准的泛化性及对复杂指令推理能力的保留程度仍存疑。

## 研究背景

当用户要求“将海报中的红色文字改为蓝色”时，传统指令编辑模型（如InstructPix2Pix）直接输出一张修改后的扁平图像。若用户随后要求“将文字向左移动”，模型需基于新图像重新生成，这一过程不仅计算开销大，且极易破坏背景纹理或引入边界伪影。为解决此问题，图像分解技术（如Qwen-Image-Layered）试图从扁平图像中恢复可编辑图层，但分解与编辑通常作为独立阶段优化：编辑模型关注视觉保真度而忽略图层结构，分解模型在编辑后恢复图层时无法联合优化编辑指令与目标图层结构，导致生成的图层难以复用或需人工修正。

领域内主流路线分为端到端微调与显式推理代理两类。端到端模型（如FLUX.1-Kontext）效率高但缺乏结构化输出；代理框架（如MIRA）通过多模态大语言模型（MLLM）分解指令，但推理延迟高且未解决图层生成问题。本文切入点在于：如何在保持预训练编辑模型强大语义理解能力的同时，直接生成结构化的可编辑图层，避免“编辑-分解”级联流程中的误差累积与能力退化。

## 核心方法

### 方法参照系：从扁平输出到联合图层生成

在标准指令编辑流程中，模型接收源图像 $I_{src}$ 和指令 $u$，输出编辑后的画布 $D$。LayerEditor将任务扩展为联合生成编辑画布 $D$ 和 $N$ 个有序RGBA图层 $S = \{L_i = (R_i, A_i)\}_{i=0}^{N-1}$，其中 $R_i$ 为RGB外观，$A_i$ 为Alpha透明度。该任务的关键差异在于：输出不再是单一图像，而是需满足 $\text{Comp}(S) \approx D$ 的结构化序列，且图层数量 $N$ 可变。

### In-Context RGB-Alpha Token Modeling

传统分层生成方法（如LayerDiff）通常独立生成各图层，缺乏跨层依赖建模。LayerEditor在扩散Transformer（DiT）中引入In-Context RGB-Alpha Token Modeling，将编辑画布与所有图层的RGB及Alpha通道拼接为单一token序列进行联合去噪。

$$
Z_t = [z^D_t, z^{R_0}_t, z^{A_0}_t, \dots, z^{R_{N-1}}_t, z^{A_{N-1}}_t]
$$

该公式定义了噪声水平 $\sigma_t$ 下的联合潜在状态。所有输出字段从高斯噪声初始化，并在统一序列中通过共享注意力机制捕获跨层依赖。为区分共享相同画布坐标的字段，模型采用层感知旋转坐标 $(s, x, y)$：源图像 $s=-1$，编辑画布 $s=0$，第 $i$ 层RGB $s=2i+1$，Alpha $s=2i+2$。这一设计使模型能在单一架构中支持可变图层数量，并显式建模外观与透明度的交互。

### Compositional Edit-Prior Distillation (C-EPD)

直接将预训练编辑模型（FireRed-Image-Edit-1.1）适配至分层输出会导致编辑能力退化，表现为文本损坏或背景意外修改。为解决此问题，本文提出C-EPD，利用冻结的预训练编辑模型作为在线策略教师，在学生的去噪轨迹中间状态进行监督。

$$
\mathcal{L}_{\text{C-EPD}} = \mathbb{E}_{q \sim Q} \left[ \frac{1}{2} \left( \frac{d_D}{d_C} \right) \left\| v^D_{q,S} - \text{sg}(v^D_{q,T}) \right\|^2 + \lambda_S \left\| \hat{C}_S - I_T \right\|^2 \right]
$$

该损失函数包含两项：第一项对齐学生与教师的直接速度预测 $v^D$，保留原始编辑先验；第二项通过解码学生预测的图层并合成 $\hat{C}_S$，与教师解码的编辑目标 $I_T$ 进行像素级监督。梯度通过Alpha合成操作反向传播至图层预测分支，确保分层输出在保持编辑保真度的同时具备结构合理性。

## 实验评估

实验在自建LayerEditor-100K数据集及Crello-Testset、ScaleEdit-Testset上进行。基线包括Seedream5-Pro（官方API）、Qwen-Image-Layered (QIL) 及其变体、FireRed-Image-Edit-1.1 (FR) 级联方案。评估指标涵盖图像级（SSIM, FID）、图层级（RGBA L1, Alpha IoU）及基于VLM的Rubric评分。

| 方法 | Crello-Testset Composite SSIM↑ | Crello-Testset Alpha IoU↑ | ScaleEdit-Testset Composite SSIM↑ | ScaleEdit-Testset Alpha IoU↑ |
| :--- | :--- | :--- | :--- | :--- |
| Seedream5-Pro (Joint) | 0.7902 | 0.5139 | 0.8365 | 0.6583 |
| FR + QIL-Decomp-FT | 0.6343 | 0.2047 | 0.6927 | 0.4240 |
| QIL-Edit-SFT | 0.7285 | 0.3171 | 0.7895 | 0.3261 |
| LayerEditor | 0.8351 | 0.6074 | 0.8839 | 0.6802 |

LayerEditor在两个基准上均取得最佳Composite SSIM和Alpha IoU。相比Seedream5-Pro (Joint)，其在Crello-Testset上Composite SSIM提升5.7%，Alpha IoU提升18.2%。值得注意的是，Seedream5-Pro (Seq.) 在ScaleEdit-Testset上Direct SSIM为0.8933，但Composite SSIM降至0.7901，降幅11.6%；而LayerEditor的降幅仅为1.0%，表明其分层输出在重合成后能更好地保持编辑保真度。

消融实验显示，移除C-EPD导致编辑一致性从6.14降至4.67，图层分割从6.83降至5.01。单独使用Direct或Composite监督均无法同时优化所有指标，联合使用两项监督才能取得最佳平衡。此外，专用Alpha解码器将RGBA L1从0.0578降至0.0350，验证了分离RGB与Alpha解码路径对细粒度透明度重建的必要性。

评估边界方面，本文未与领域内主流RL对齐方法（如EditReward, CoCoEdit）或MLLM代理框架（如MIRA）进行对比，因任务定义不同（通用编辑 vs. 分层编辑）。自建基准Crello/ScaleEdit主要覆盖设计类图像，缺乏自然场景验证。代码未开源，复现依赖FireRed-Image-Edit-1.1权重。

## 关联研究分析

从问题动机看，LayerEditor与Qwen-Image-Layered (QIL) 均关注图层生成，但QIL侧重从扁平图像中恢复图层（分解），而LayerEditor强调在编辑过程中联合生成图层。QIL的分解模型无法感知编辑指令，导致恢复的图层可能与编辑意图不一致；LayerEditor通过In-Context Token Modeling将编辑指令直接注入图层生成过程，确保图层结构与编辑内容对齐。这一差异源于任务定义：分解是后处理，编辑是生成过程，LayerEditor将二者统一为条件生成问题。

从方法设计看，LayerEditor采用在线策略蒸馏（C-EPD）而非强化学习（RL）对齐。领域共识认为RL（如GRPO）能有效提升指令遵循度，但RL需要构建复杂的奖励模型且训练不稳定。C-EPD利用预训练编辑模型作为教师，通过像素级和速度级监督直接传递编辑先验，避免了奖励信号稀疏问题。然而，蒸馏是否牺牲了模型对复杂隐含指令的推理能力，论文未给出回答。若编辑指令涉及多步逻辑推理（如“将左侧物体移至右侧并调整阴影”），仅依赖教师模型的直接监督可能不足以捕捉中间推理状态。

## 总结

LayerEditor针对指令编辑输出扁平化导致复用性差的问题，提出联合生成编辑画布与可复用RGBA图层的统一框架。通过In-Context RGB-Alpha Token Modeling实现跨层依赖建模，并利用C-EPD蒸馏预训练编辑先验以缓解能力退化。实验表明，LayerEditor在Crello-Testset上Composite SSIM达0.8351，Alpha IoU达0.6074，显著优于级联基线。其边界在于自建基准主要覆盖设计类图像，且未验证在复杂自然场景下的泛化能力。当编辑指令涉及多对象交互或物理一致性约束时，C-EPD的像素级监督是否足以替代显式推理机制，仍需进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.24738)