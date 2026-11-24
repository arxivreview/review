# CVPR2026 · 视觉Transformer训练与分析方向论文汇编

> 本方向共 10 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Can You Learn to See Without Images? Procedural Warm-Up for Vision Transformers ｜程序化预热

研究机构：澳大利亚阿德莱德大学、瑞士洛桑联邦理工学院

作者：Zachary Shinnick、Liangze Jiang、Hemanth Saratchandran 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.13945)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13945)

> 视觉Transformer（Vision Transformer, ViT）在大规模图像预训练中表现优异，但依赖海量数据且缺乏跨模态泛化能力。现有结构化初始化仅作用于注意力层，且抽象视觉数据（如分形）无法替代自然图像的语义信息。本文切入点在于：非视觉的符号序列能否为ViT提供通用的计算归纳偏置？方法是通过形式语法生成无视觉内容的符号序列，以掩码预测目标进行轻量级预热，再衔接标准图像训练。该策略以1%的训练预算换取1.72%的精度提升，验证了非视觉数据与视觉学习的互补性，但其增益是否随模型规模扩大而衰减尚存疑。

】

---

【CIGMA: Causal Information-Gain Mechanistic Attribution of Attention Heads in Vision Transformers ｜因果信息增益机制归因

作者：Maisha Maliha、Dean F. Hougen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd0456f61d84)

> 视觉Transformer（ViT）常依赖背景捷径而非前景物体进行决策，导致模型在分布偏移下鲁棒性差且解释不可信。现有剪枝方法仅关注计算效率，缺乏对虚假相关路径的因果验证。本文提出CIGMA，通过无训练的头部级因果干预，精准定位并移除传播背景信号的注意力头。该方法在CIFAR-10/100和TinyImageNet上显著提升了精度与校准度，但其有效性是否依赖于小数据集的特定结构，尚存疑。

】

---

【Concept-Guided Fine-Tuning: Steering ViTs away from Spurious Correlations to Improve Robustness ｜概念引导微调

研究机构：以色列特拉维夫大学

作者：Yehonatan Elisha、Oren Barkan、Noam Koenigstein

论文原文见 [arXiv](https://arxiv.org/abs/2603.08309)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08309)

> 视觉Transformer在分布偏移下性能骤降，根源在于模型依赖背景纹理等虚假相关而非语义特征。现有显著性正则化方法依赖粗糙的前景-背景二值掩码，无法捕捉细粒度语义结构，且需人工标注或全量重训。CFT利用大语言模型生成细粒度概念，经视觉语言模型定位后作为监督信号，仅用1,500张图像微调ViT，将内部相关性图对齐至语义概念区域。该方法在多个OOD基准上显著提升了鲁棒性，但概念掩码的生成误差对最终鲁棒性上限的影响尚未被充分量化。

】

---

【ReMoE: Region-Mixture Experts for Adversarially-Robust Vision Transformers ｜区域感知混合专家机制

研究机构：北京理工大学、哈尔滨工业大学

作者：Qinghao Zhong、Bingzhi Chen、Yishu Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e17e6223cc58)

> 视觉Transformer（ViT）在对抗攻击下极易因局部扰动引发全局语义崩溃，现有防御方法多聚焦于全局表征稳定或单一Token级正则化，忽视了空间连贯区域内的语义一致性缺失。ReMoE通过替换标准前馈网络，引入全局、中心与区域多粒度专家，并利用注意力引导的路由机制实现区域级语义建模。该方法在CIFAR-10上以53.54%的PGD-20准确率超越现有SOTA，但其在高分辨率图像上的区域划分泛化能力仍存疑。

】

---

【SPAR: Single-Pass Any-Resolution ViT for Open-vocabulary Segmentation ｜单次前向任意分辨率视觉Transformer

研究机构：捷克布拉格捷克理工大学

作者：Naomi Kombol、Ivan Martinović、Siniša Šegvić 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02252)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02252)

> 视觉Transformer（ViT）在高分辨率密集预测任务中面临训练-推理分辨率失配导致的特征粗糙与计算开销激增双重困境。现有滑动窗口推理虽能提升精度，但推理延迟呈线性增长，无法落地。本文提出SPAR，通过特征蒸馏将滑动窗口教师的多上下文空间推理能力内化至单次前向传播学生模型，无需架构修改或像素级监督。该方法在开放词汇分割任务上实现了效率与精度的帕累托改进，但其增益高度依赖骨干网络是否已具备原生分辨率鲁棒性，对已优化架构的边际收益存疑。

】

---

【Sparsity as a Key: Unlocking New Insights from Latent Structures for Out-of-Distribution Detection ｜稀疏自编码器驱动的视觉Transformer分布外检测

研究机构：韩国延世大学

作者：Ahyoung Oh、Wonseok Shin、Songkuk Kim

论文原文见 [arXiv](https://arxiv.org/abs/2604.26409)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.26409)

> 视觉Transformer在分布外（Out-of-Distribution, OOD）检测中面临特征纠缠导致的误判难题，现有基于距离或置信度的方法无法区分几何邻近与语义相似。本文切入点在于利用Top-k稀疏自编码器（Sparse Autoencoder, SAE）解耦[CLS] token，揭示分布内（In-Distribution, ID）与OOD样本在稀疏潜空间中的结构差异。通过构建类激活轮廓（Class Activation Profiles, CAPs）并计算能量轮廓散度（Energy Profile Divergence, EPD），该方法在FPR95指标上实现了显著优势。其价值在于提供了可解释的OOD信号，但硬稀疏约束对骨干网络全局一致性的依赖限制了其在局部注意力架构中的泛化能力。

】

---

【Towards Robust Vision Transformers: Path Dependency Analysis and a Simple Two-Stage Adversarial Training ｜视觉Transformer对抗鲁棒性中的路径依赖分析与两阶段训练

作者：Seongmin Kim、Byung Cheol Song

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1eb13b877dc8)

> 视觉Transformer（ViT）在对抗训练（Adversarial Training, AT）中常出现性能退化或收敛不稳定，根源在于其内部信息流结构与卷积神经网络（CNN）存在本质差异。现有方法多直接移植CNN的鲁棒蒸馏策略，忽视了ViT中残差连接对攻击梯度的特殊贡献。本文通过梯度路径掩码（Gradient Path Masking, GPM）定位脆弱路径，并提出基于类注意力图（Class Attention Map, CAM）蒸馏的两阶段AT框架。该方法在CIFAR-10上将ViT-S的AutoAttack（AA）鲁棒性从46.37%提升至47.41%，但缺乏大规模数据集验证，其通用性存疑。

】

---

【UniRefiner: Teaching Pre-trained ViTs to Self-Dispose Dross via Contrastive Register ｜虚假Token治理与对比寄存器精炼

研究机构：中国科学院大学、哈尔滨工业大学

作者：Congpei Qiu、Zhaoyu Hu、Wei Ke 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.19622)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.19622)

> 大规模视觉-语言模型在密集预测任务中表现不佳，根源在于特征图中存在大量与空间位置语义不对齐的虚假Token，而现有方法仅将其视为高范数异常值，无法处理其异质性。本文通过系统分类三类虚假Token并设计对比寄存器机制，实现了对预训练ViT的后处理精炼。该方法以极低成本显著提升了空间表征质量，但其对阈值敏感性及对特定骨干的依赖程度尚存疑。

】

---

【Vision Transformers Need More Than Registers ｜视觉Transformer的懒惰聚合机制与频率感知选择性聚合

研究机构：中山大学

作者：Cheng Shi、Yizhou Yu、Sibei Yang

论文原文见 [arXiv](https://arxiv.org/abs/2602.22394)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22394)

> 视觉Transformer（ViT）作为通用特征提取器，在密集预测任务中普遍存在前景语义向背景扩散的伪影，导致注意力图与真实物体错位。现有方法如Register仅缓解高范数Token，未触及背景捷径的根本成因。本文提出Patch Score与Point-in-Box (PiB)指标量化该现象，并通过频率感知的通道级Top-K池化重构CLS Token聚合逻辑，从预训练阶段抑制懒惰聚合。该方法在12项基准上验证了跨监督范式的有效性，但其对分类精度的潜在权衡及小Patch Size下的鲁棒性仍存疑。

】

---

【ViT$^3$: Unlocking Test-Time Training in Vision ｜视觉测试时训练

研究机构：清华大学、阿里巴巴集团

作者：Dongchen Han、Yining Li、Tianyu Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.01643)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01643)

> 视觉Transformer（ViT）在处理高分辨率图像时，Softmax注意力的二次方计算复杂度成为部署瓶颈。现有线性注意力方案虽降低了复杂度，但固定压缩机制导致表达力受限，难以在密集预测任务中保持精度。本文切入点在于将注意力操作重构为测试时在线学习问题，通过动态训练内部模型权重来替代静态矩阵乘法。该范式确立了视觉领域测试时训练的设计原则，但其推理阶段引入的额外计算开销是否抵消了线性复杂度的优势，仍需在实际部署场景中进一步验证。

】
