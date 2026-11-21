# CVPR2026最新论文 ｜Uni-DAD: Unified Distillation and Adaptation of Diffusion Models for Few-step Few-shot Image Generation ｜统一蒸馏与适应的扩散模型

作者：Yara Bahram、Mélodie Desbos、Mohammadhadi Shateri 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18281)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18281)

> 扩散模型在少样本域适应后仍面临高推理成本，而现有“先蒸馏后适应”或“先适应后蒸馏”的两阶段流程均存在质量或多样性损失。Uni-DAD 提出单阶段联合优化框架，通过双域分布匹配蒸馏与多尺度生成对抗网络损失，在极低采样步数下同时实现域适应与少步生成。该方法在少样本场景下打破了顺序依赖冲突，但其在结构差异极大域上的泛化边界尚存疑。

## 研究背景

扩散模型（Diffusion Models, DMs）通过迭代去噪生成高质量图像，但其数十至数百次前向传播的推理成本阻碍了实时个性化应用。当模型需适应仅含少量样本（如10张）的新域时，直接微调会导致过拟合与多样性坍缩，而少步蒸馏（Few-step Distillation）虽能加速推理，却通常将学生模型限制在教师模型的流形内，缺乏对新域的适应能力。

主流解决方案采用两阶段流水线：Distill-then-Adapt 或 Adapt-then-Distill。前者先蒸馏再微调，但学生模型在少样本下易饱和，产生过平滑输出；后者先微调教师再蒸馏，但学生模型继承教师的过拟合风险，且丢失源域可迁移的多样性信息。这两种顺序执行方式均非端到端，且在训练过程中易丢失源域信息。Uni-DAD 的切入点在于将蒸馏与适应视为联合优化问题，通过单阶段训练同时压缩步数并适应目标域，避免顺序依赖带来的信息损失。

## 核心方法

### 方法参照系

本文问题属于扩散模型加速与域适应的交叉场景。标准流程通常将蒸馏（如DMD2）与适应（如DreamBooth）解耦为独立阶段。本文的关键差异在于打破这种解耦，将两者整合为单一优化目标，以解决少样本下顺序执行导致的多样性坍缩与过平滑问题。

### 双域分布匹配蒸馏

传统分布匹配蒸馏（Distribution Matching Distillation, DMD）仅对齐学生模型与单一源域教师的分布，在目标域与源域结构差异较大时，源域教师会抑制真正的适应。Uni-DAD 引入双域DMD目标，同时利用冻结的源域教师 $\epsilon_{src}$ 和在线训练的目标域教师 $\epsilon_{trg}$ 的分数函数引导学生生成。其梯度形式为：

$$ \nabla_\theta L_{DMD} = \mathbb{E}_{t, z} \left[ \left( \epsilon_{src}(x_t, t) - \epsilon_{fk}(x_t, t) \right) \frac{\partial x}{\partial \theta} \right] + a \cdot \mathbb{E}_{t, z} \left[ \left( \epsilon_{trg}(x_t, t) - \epsilon_{fk}(x_t, t) \right) \frac{\partial x}{\partial \theta} \right] $$

其中 $a \in [0, 1]$ 为权重因子。该设计动机在于，源域教师保留姿态、背景等可迁移多样性，而目标域教师提供结构适配信号，二者共同引导学生趋向两个分布的交集，从而在少样本下平衡保真度与多样性。

### 多尺度生成对抗网络

少样本场景下，传统GAN判别器易记忆目标集导致过拟合。Uni-DAD 采用多尺度GAN损失，复用假教师 $\epsilon_{fk}$ 的编码器块作为特征提取器，并在每个块后附加线性头，构成多尺度判别器 $D^{[b]}$。其生成器损失为：

$$ L_G = \sum_{b \in \mathcal{B}} \mathbb{E}_{z} \left[ -\log \left( 1 - D^{[b]}(G(z)) \right) \right] $$

该设计动机在于，通过在不同特征尺度上对比真实与生成样本，增强判别器对局部细节与全局结构的感知能力，从而在 $|Y| \le 10$ 的极端少样本条件下抑制模式坍缩，提升目标域的现实感。

## 实验评估

实验在FSIG（FFHQ源域，10-shot目标域）与SDP（SDv1.5源域，4-6-shot DreamBooth）基准上进行。基线覆盖非蒸馏方法（FT, CRDI）与两阶段蒸馏方法（DMD2-FT, FT-DMD2），但缺失其他单阶段联合优化基线。在FSIG基准上，Uni-DAD在Babies域以NFE=3取得51.85的FID，优于两阶段方法FT-DMD2的58.13，且Intra-LPIPS达到0.44，显著高于DMD2-FT的0.08，表明其在加速的同时保持了多样性。

| 方法 | NFE | FID (Babies) | Intra-LPIPS (Babies) |
| :--- | :--- | :--- | :--- |
| FT-DMD2 | 3 | 58.13 | 0.36 |
| Uni-DAD | 3 | 51.85 | 0.44 |

在SDP基准上，Uni-DAD以NFE=1实现0.47的DINO相似度，虽低于非蒸馏FT的0.58，但速度提升100倍，且优于1-step蒸馏基线DMD2-FT的0.20。消融实验显示，引入目标域教师后，在结构差异大的MetFaces域上FID从63.25降至51.85，但Intra-LPIPS从0.42微降至0.34，表明目标域教师以轻微多样性损失换取结构适配。

评估边界方面，FSIG基准仅使用10-shot目标集，未测试更大支持集下的性能变化；SDP基准中PSO基线使用SDXL骨干与1024分辨率，与Uni-DAD的SDv1.5与512分辨率存在不可比性。代码已开源，但训练细节如学习率调度未在正文详述，复现需依赖附录。

## 关联研究分析

从问题动机看，Uni-DAD与DMD2的核心差异在于处理域偏移的方式。DMD2假设学生模型需在单一教师流形内优化，适用于域内加速；而Uni-DAD针对少样本域适应，引入双域教师以突破源域流形限制。这一差异源于任务特性：域适应要求模型跳出源域分布，而单纯蒸馏会抑制这种跳出。Uni-DAD通过双域权重 $a$ 动态平衡，解决了DMD2在域偏移下的僵化问题。

从方法设计看，Uni-DAD与PSO（Progressive Step Optimization）均涉及蒸馏与适应的结合，但PSO采用两阶段流程，先蒸馏后以相对似然目标微调，导致少样本下过平滑。Uni-DAD的单阶段联合优化避免了中间阶段的性能瓶颈，且多尺度GAN损失直接针对少样本过拟合问题，而非依赖PSO的轻量级微调。PSO在数据充足时（$n \sim 1000$）表现良好，但在 $n \le 10$ 时失效，而Uni-DAD通过源域教师保留多样性，在极端少样本下仍保持竞争力。

## 总结

Uni-DAD 解决了扩散模型在少样本域适应中蒸馏与适应的顺序依赖冲突，通过双域DMD与多尺度GAN的单阶段联合优化，在NFE≤4下实现了接近非蒸馏方法的质量。其在FSIG基准上以51.85的FID和0.44的Intra-LPIPS验证了有效性，但实验仅覆盖10-shot场景，未探索支持集规模对双域权重敏感性的影响。当支持集从10-shot增至50-shot时，源域教师与目标域教师的权重平衡是否仍需手动调整，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18281)