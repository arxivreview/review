# ICLR2026最新论文 ｜DIFFUDETR: RETHINKING DETECTION TRANSFORMERS WITH DENOISING DIFFUSION PROCESS ｜去噪扩散检测器

研究机构：德国慕尼黑工业大学

作者：Youssof Nawar、Mohamed Badran、Marwan Torki

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52297229)

> 检测Transformer依赖固定查询初始化，导致训练收敛缓慢且定位精度受限。现有去噪辅助任务仅作为正则化手段，未改变查询生成的根本逻辑。本文提出将检测重构为条件去噪过程，通过迭代去噪参考点生成查询。该方法在COCO上较基线提升1.0 AP，但推理需多次解码器前向传播，实时性存疑。

## 研究背景

检测Transformer（DETR）通过匈牙利匹配实现端到端训练，消除了非极大值抑制（NMS）后处理。然而，DETR的查询初始化为零向量或随机值，缺乏空间先验，导致模型需从零学习查询与物体的对齐，收敛速度显著慢于两阶段检测器。去噪扩散概率模型（DDPM）通过逐步去噪从纯噪声恢复数据，其核心在于学习条件分布 $p(x_t|x_{t+1})$。将DDPM应用于检测，意味着将物体定位建模为从噪声分布到真实参考点的逆向过程，这为查询初始化提供了概率框架。

DETR系列通过引入动态锚框（DAB-DETR）或去噪辅助任务（DN-DETR、DINO）缓解收敛问题，但这些方法仍依赖固定的查询数量与初始化策略。DINO引入对比去噪查询（CDN），通过高置信度编码器输出初始化参考点，提升了训练稳定性，但查询生成过程仍是确定性的。本文切入点在于：将查询参考点视为扩散变量，训练时注入高斯噪声，推理时通过DDIM采样器迭代去噪，从而将查询生成从“固定初始化+微调”转变为“从噪声生成”，从根本上解决初始化随机性导致的精度上限瓶颈。

## 核心方法

### 方法参照系

本文基于Deformable DETR架构，保留多尺度变形注意力编码器与Transformer解码器。与标准DETR流程的关键差异在于：查询参考点不再是固定可学习参数或编码器输出，而是作为扩散过程的潜变量，训练时从噪声分布采样，推理时通过去噪生成。

### 扩散查询生成机制

标准DETR中，查询参考点 $r$ 为固定值或编码器预测值，训练目标为最小化分类与回归损失。本文引入时间步 $t \sim U(0, 100)$，将真实参考点 $r_0$ 扩散为噪声参考点 $r_t$：

$$ r_t = \sqrt{\bar{\alpha}_t} r_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon, \quad \epsilon \sim \mathcal{N}(0, I) $$

其中 $\bar{\alpha}_t = \prod_{s=1}^t \alpha_s$，$\alpha_s = 1 - \beta_s$。解码器接收噪声参考点 $r_t$、时间步嵌入 $t$ 与编码器特征 $O_{enc}$，预测噪声残差 $\hat{\epsilon}_\theta(r_t, t)$。训练损失为 $\mathcal{L} = \|\epsilon - \hat{\epsilon}_\theta(r_t, t)\|^2$，迫使模型学习从任意噪声水平恢复真实参考点的条件分布。这一设计解决了固定初始化无法覆盖所有可能物体位置的问题，通过扩散过程隐式学习物体位置的全局分布。

### 高效DDIM采样推理

推理时，从标准高斯分布采样初始参考点 $r_T \sim \mathcal{N}(0, I)$，执行 $S$ 步DDIM去噪：

$$ r_{t-1} = \sqrt{\bar{\alpha}_{t-1}} \left( \frac{r_t - \sqrt{1 - \bar{\alpha}_t} \hat{\epsilon}_\theta(r_t, t)}{\sqrt{\bar{\alpha}_t}} \right) + \sqrt{1 - \bar{\alpha}_{t-1}} \hat{\epsilon}_\theta(r_t, t) $$

本文发现 $S=3$ 步即可达到最佳性能，无需标准扩散模型的1000步。该设计动机在于：参考点维度低（$N \times 4$），扩散空间简单，少量迭代即可收敛。相比DINO的固定查询，DDIM采样允许模型在推理时动态调整查询位置，提升复杂场景下的定位精度，同时通过限制 $S$ 控制计算开销。

## 实验评估

| 模型 | 骨干 | Epochs | AP | AP50 | AP75 |
|---|---|---|---|---|---|
| DINO | ResNet-50 | 36 | 50.9 | 69.0 | 55.3 |
| DiffuDETR | ResNet-50 | 50 | 50.2 | 66.8 | 55.2 |
| DiffuDINO | ResNet-50 | 50 | 51.9 | 69.4 | 55.7 |
| DiffuAlignDETR | ResNet-50 | 24 | 51.9 | 69.2 | 56.4 |

实验在COCO 2017、LVIS、V3DET上验证，基线覆盖DETR、DINO、DN-DETR、DiffusionDet，但缺失YOLO系列实时基线。DiffuDINO在ResNet-50上达51.9 AP，较DINO的50.9 AP提升1.0点，AP50提升0.4点，AP75持平。DiffuDETR（基于Deformable DETR）仅达50.2 AP，低于DINO，表明扩散机制对解码器架构敏感，CDN辅助任务对性能贡献显著。

消融实验显示，高斯噪声分布优于Beta（49.5 AP）与Sigmoid Gaussian（50.4 AP），Cosine调度器优于Linear（51.6 AP）与Square Root（51.4 AP）。解码器评估步数 $S$ 从1增至3时，AP从51.6升至51.9，FLOPs从244.5G增至285.2G；$S=5$ 时AP降至51.8，$S=10$ 时降至51.4，FLOPs达427.9G。这表明 $S=3$ 是精度-计算帕累托最优点，过多迭代导致过拟合或数值不稳定。

评估边界：论文未报告FPS或延迟，仅报告FLOPs与激活值，无法验证实时性。代码开源，但超参数（如噪声调度器 $\beta_t$ 具体值）未在正文中完整列出，可复现性依赖GitHub仓库。指标完备性上，LVIS与V3DET结果仅报告AP，未细分AP_r/AP_c/AP_f（除LVIS表2外），小目标性能分析不足。

## 关联研究分析

从问题动机看，DiffuDETR与FlowDet（Baty et al., 2025）同属生成式检测，但FlowDet使用条件流匹配，推理时通过增加细化步骤提升精度，而DiffuDETR使用DDPM，通过去噪步数 $S$ 控制精度-计算权衡。FlowDet的流匹配在理论上更稳定，但DiffuDETR的DDIM采样在低步数下表现更优，这可能源于参考点低维特性使扩散过程更易收敛。两者均未解决实时性问题，但DiffuDETR的 $S=3$ 设计更接近实时约束。

从方法设计看，DiffuDETR与DINO（Zhang et al., 2022）共享CDN机制，但DINO的查询初始化来自编码器高置信度输出，是确定性过程；DiffuDETR的查询来自噪声采样，是随机过程。这一差异导致DiffuDETR在复杂场景（COCO Dense）中AP提升1.16点（44.88 vs 43.72），而在简单场景（COCO Sparse）中仅提升1.65点（58.65 vs 57.00），表明扩散机制对密集重叠物体的定位更敏感。DINO的固定查询在简单场景已足够，而DiffuDETR的随机查询通过去噪过程更精确地定位密集物体，但计算开销增加16%（285.2G vs 244.5G）。

## 总结

本文核心矛盾是DETR查询初始化随机性导致的收敛慢与精度上限。切入点在于将查询生成重构为扩散去噪过程，利用DDIM采样器在低步数下生成精确参考点。方法上，训练时注入高斯噪声，推理时执行3步去噪，在COCO上较DINO提升1.0 AP（51.9 vs 50.9），AP50提升0.4点。边界在于：推理需3次解码器前向传播，FLOPs增加16%，未报告FPS，实时性未验证；DiffuDETR（无CDN）性能低于DINO，表明扩散机制依赖辅助任务。当解码器步数 $S$ 增至5或10时，AP下降而FLOPs持续增加，扩散过程在检测任务中的最优步数是否随场景复杂度变化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52297229)