# CVPR2026最新论文 ｜ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation ｜推理对齐表示的伪造检测

研究机构：北京大学、华南理工大学

作者：Qing Huang、Zhipei Xu、Xuanyu Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.16080)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.16080)

> AI生成图像检测面临低层伪迹与高层语义的割裂，传统视觉模型缺乏语义推理，而大语言模型（LLM）推理成本高且对细微纹理不敏感。本文切入点在于验证RL优化LLM生成的推理文本具备判别力与跨域不变性，并将其作为中间表示蒸馏至轻量级视觉编码器。ReAlign通过对比学习对齐视觉特征与推理文本空间，实现了高效且泛化性强的检测。该方法在多个基准上超越了纯视觉与纯LLM基线，但其性能是否优于当前最强的纯视觉基础模型（VFM）探针，论文未提供直接对比。

## 研究背景

当检测器面对未见过的生成模型时，其训练域与测试域的数据分布出现系统性差异，导致基于固定低层统计特征的专用检测器性能骤降。这种跨生成器泛化难题源于生成器架构的多样性，使得单一伪迹先验失效。为捕捉更本质的分布差异，研究范式转向利用大规模预训练的视觉基础模型（Vision Foundation Model, VFM）特征，但VFM特征往往忽略细粒度的低层线索，且缺乏对语义逻辑错误的敏感度。

现有方案在效率与能力间存在结构性矛盾。非LLM方法（如CNNSpot, AIDE）依赖CNN或ViT提取像素级异常，擅长检测纹理伪迹，但作为黑盒模型，其参数容量有限，易过拟合且无法解释语义矛盾。LLM方法（如AIDE, FakeVLM）能生成文本解释并识别常识性错误，但参数量巨大、推理延迟高，且对低层伪迹不敏感。更关键的是，现有研究缺乏证据表明LLM生成的解释文本本身对检测精度有直接贡献，多数工作仅将其视为输出副产品。

本文的核心切入点是解耦LLM的“推理能力”与“参数规模”。作者假设，经过强化学习优化的LLM生成的推理文本，其向量表示本身蕴含了判别真实/伪造的语义信息，且具备跨域不变性。通过验证这一假设，ReAlign将推理文本作为“桥梁”，将其语义优势蒸馏至轻量级CLIP编码器，从而在不部署大模型的前提下，同时获得低层伪迹检测能力与高层语义敏感性。

## 核心方法

### 方法参照系

本文问题属于多模态推理检测路线，但区别于MLLM直接输出分类标签的标准流程。其关键差异在于：不将MLLM作为推理时的检测器，而是将其作为训练时的“教师”，提取其生成的推理文本表示，通过对比学习将其语义信息迁移至轻量级视觉编码器，实现推理时的轻量化部署。

### 推理文本的判别属性验证

设计动机在于解决LLM解释文本价值不明的争议，即证明文本表示本身而非LLM参数是泛化能力的来源。作者首先训练AIGI-R1，一个基于Group Relative Policy Optimization (GRPO) 优化的多模态大模型。GRPO通过相对奖励机制优化生成策略，其目标函数定义为：

$$ \mathcal{L}_{GRPO} = \mathbb{E}_{q \sim \mathcal{D}, o \sim \pi_{ref}} \left[ \frac{1}{G} \sum_{i=1}^{G} \left( \frac{\pi_{\theta}(o_i|q)}{\pi_{ref}(o_i|q)} R_{total}(q, o_i) - \log \sum_{j=1}^{G} \frac{\pi_{\theta}(o_j|q)}{\pi_{ref}(o_j|q)} R_{total}(q, o_j) \right) \right] $$

其中 $R_{total}$ 包含检测准确率奖励与格式奖励。实验表明，AIGI-R1生成的推理文本在“真实/伪造”概念上的语义极性显著高于普通图像描述（Caption），且在StarGAN与SDXL等不同生成器产生的文本表示空间中高度重叠，证明了其跨域不变性。

### 对比对齐与联合优化

设计动机在于解决轻量级视觉编码器缺乏语义敏感性的问题，通过文本-图像对齐将推理文本的判别力注入视觉特征。ReAlign构建文本-图像对，使用CLIP-ViT作为图像编码器（LoRA微调）和文本编码器（冻结）。训练采用联合优化策略，同时最小化对比损失（Contrastive Loss）与分类损失（Classification Loss）：

$$ \mathcal{L}_{total} = \mathcal{L}_{contrastive} + \lambda \mathcal{L}_{BCE} $$

其中 $\mathcal{L}_{contrastive}$ 拉近图像特征与对应推理文本特征的距离，$\mathcal{L}_{BCE}$ 为二元交叉熵损失。这种联合优化迫使图像编码器在保持低层伪迹敏感性的同时，学习对齐到推理文本所定义的语义判别空间，从而在推理时仅需轻量级视觉模型即可实现语义感知的检测。

## 实验评估

实验在AIGCDetectBenchmark、AIGI-Holmes及自建UltraSynth-10k上进行，基线涵盖CNNSpot、UniFD、AIDE等视觉方法以及AIGI-R1等LLM方法。值得注意的是，基线中缺失了当前领域最强的纯VFM探针（如DINOv3-Linear, SSAFE），这使得ReAlign的性能优势可能被高估，因为VFM探针在跨生成器泛化上已展现出强劲实力。

| 方法 | AIGCDetectBenchmark (mAcc) | AIGI-Holmes (mAcc) | UltraSynth-10k (mAcc) |
| :--- | :--- | :--- | :--- |
| CNNSpot | 70.78 | 72.90 | 71.93 |
| AIDE | 92.77 | 97.00 | 81.08 |
| AIGI-R1 | 91.77 | 93.54 | 96.42 |
| **ReAlign** | **96.14** | **99.44** | **97.09** |

ReAlign在三个基准上均取得最高平均准确率，在AIGCDetectBenchmark上较AIDE提升3.37%，在AIGI-Holmes上较AIDE提升2.44%。在UltraSynth-10k上，ReAlign（97.09%）显著优于纯LLM基线AIGI-R1（96.42%），验证了蒸馏框架的有效性。

| 消融设置 | UltraSynth-10k (mAcc) | 相对Ours变化 |
| :--- | :--- | :--- |
| Ours (Reasoning + Label) | 97.09 | - |
| (a) Caption + Label | 91.63 | -5.46% |
| (b) Reasoning Only | 96.87 | -0.22% |
| (c) Caption Only | 88.32 | -8.77% |
| (d) Label Only | 91.33 | -5.76% |

消融实验表明，推理文本（Reasoning Text）是性能的关键来源，替换为普通描述（Caption）导致5.46%的性能下降。联合优化（Joint）比顺序优化（Sequential）高13.01%，证明分类约束有助于图像编码器从文本表示中高效学习检测信息。LoRA微调比全参数微调高2.40%，表明保留通用语义感知对检测有益。

评估边界方面，论文未报告置信区间，且未对比DINOv3等强VFM基线，无法确定ReAlign是否优于纯视觉基础模型探针。代码未公开，但提供了详细的超参数（LoRA rank=6, LR=1e-4, 10 epochs），可复现性中等。

## 关联研究分析

从问题动机看，ReAlign与AIDE（Huang et al., 2025）均旨在融合低层与高层特征，但AIDE通过混合模型直接建模低层与高层特征，而ReAlign通过文本表示作为中介。AIDE的局限在于其高层特征仍依赖视觉编码器，对语义逻辑错误的捕捉能力有限；ReAlign则通过LLM推理文本引入外部世界知识，解决了视觉编码器缺乏常识推理的问题。然而，ReAlign未对比AIDE在语义错误检测上的具体表现，仅通过整体准确率证明优势，这可能掩盖了两者在特定子任务上的差异。

从方法设计看，ReAlign与UnivFD（Wang et al., 2023）同属利用预训练特征提升泛化的路线，但UnivFD直接使用冻结CLIP特征加线性探针，而ReAlign引入了文本模态的对齐。UnivFD的优势在于流程极简、计算成本低，但缺乏语义解释能力；ReAlign通过引入推理文本，牺牲了部分计算效率（需预训练AIGI-R1生成文本），换取了语义敏感性。关键差异在于，ReAlign假设推理文本的向量空间比CLIP图像空间更具判别力，这一假设在跨域场景下得到验证，但在低层伪迹主导的场景下，文本对齐是否可能引入噪声，论文未给出深入分析。

## 总结

ReAlign旨在解决LLM检测成本高与视觉检测缺乏语义敏感性的矛盾。其切入点在于验证RL优化LLM生成的推理文本具备独立的判别价值与跨域不变性，并将其作为中间表示蒸馏至轻量级CLIP编码器。通过对比学习对齐视觉与文本特征，ReAlign在AIGCDetectBenchmark和AIGI-Holmes上分别达到96.14%和99.44%的准确率，超越了纯视觉与纯LLM基线。然而，论文未对比当前最强的纯VFM探针（如DINOv3-Linear），且消融实验显示推理文本对低层伪迹不敏感，这意味着在伪迹主导的场景下，文本对齐的增益可能有限。当生成模型的低层伪迹进一步减弱、语义错误成为主要检测线索时，ReAlign的性能优势是否依然显著，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.16080)