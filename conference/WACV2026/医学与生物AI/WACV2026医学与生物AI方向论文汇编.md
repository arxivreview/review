# WACV2026 · 医学与生物AI方向论文汇编

> 本方向共 33 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【2S-CEDiff: A Two-Stage Diffusion Framework for Generating High-Fidelity Contrast-Enhanced CT Images from Non-Contrast Scans ｜两阶段扩散框架生成高保真对比增强CT

研究机构：国立清华大学、国立台湾大学

作者：Yibang Wu、Tzung-Dau Wang、Shang-Hong Lai

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3e82dd9f412f)

> 临床急需在不使用造影剂的前提下，从非增强CT（NCCT）合成对比增强CT（CECT）以规避患者过敏与肾毒性风险。现有2D切片独立生成方法导致体积内解剖结构闪烁，而全3D扩散模型因显存瓶颈难以在临床工作站部署。本文提出2S-CEDiff，通过2.5D条件扩散结合轻量级3D精修，在单卡24GB显存下实现心肌等薄壁结构的高保真合成。该方法在私有心脏CT数据集上取得了29.87 dB PSNR与0.9437的TotalSegmentator Dice分数，但其评估缺乏与主流3D潜空间扩散模型的直接对比，且未验证跨中心泛化能力。

】

---

【A Multi-Agent Diffusion Approach for MRI Anomaly Segmentation via Modality-Specific LoRA Specialization ｜多模态MRI无监督异常分割中的LoRA路由与潜频掩码机制

研究机构：阿联酋扎耶德大学

作者：Wafa Al Ghallabi、Muhammad Zaigham Zaheer、Ritesh Thawkar 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a6b6bde83ee2)

> 脑病变无监督异常检测旨在摆脱像素级标注依赖，通过重构健康解剖先验来定位病灶，但现有扩散模型方法在多模态场景下往往需要为每种序列训练独立模型，或依赖配对的跨模态数据，导致计算开销大且泛化受限。本文切入点在于利用参数高效微调与可学习频率正则化，在单一共享骨干上实现模态特异性适配。具体做法是两阶段训练：先全量微调扩散骨干建立共享解剖先验，再冻结骨干仅训练LoRA适配器与潜空间频率掩码。该方法在BraTS2021上以87.8%的Dice系数超越IterMask2，且将可训练参数降低53%，但其性能上限仍显著低于全监督方法，且未验证在极端低对比度病灶上的鲁棒性。

】

---

【A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis ｜脑MRI生成模型记忆化检测新指标

作者：Antonio Scardace、Lemuel Puglisi、Francesco Guarnera 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.16582)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.16582)

> 脑MRI生成模型在合成数据时可能复现训练集中的患者隐私信息，但现有通用去重方法无法捕捉医学影像中决定身份识别的细粒度解剖结构。本文提出DeepSSIM，一种自监督嵌入度量，通过强制嵌入空间的余弦相似度匹配图像空间的SSIM分数，实现无需配准的高效记忆化量化。该方法在空间错位场景下将F1分数从基线的31.39%提升至76.43%，但仅验证了2D切片数据，其向3D体积及实时训练监控的扩展性尚未证实。

】

---

【AGENet: Adaptive Edge-aware Geodesic Distance Learning for Few-Shot Medical Image Segmentation ｜边缘感知测地距离学习用于少样本医学图像分割

研究机构：英国伦敦大学学院

作者：Ziyuan Gao

论文原文见 [arXiv](https://arxiv.org/abs/2511.11662)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11662)

> 医学图像分割面临标注数据稀缺与边界模糊的双重困境，传统少样本方法因均匀空间平均导致原型混合，难以精确界定解剖边界。本文指出现有原型网络忽略了像素的空间异质性，提出 AGENet 框架，通过边缘感知测地距离学习重构原型提取过程。该方法以轻量几何建模替代复杂注意力机制，在九个数据集上验证了其对边界精度的提升，但其泛化能力受限于特定几何先验的适用范围。

】

---

【Anatomy-VLM: A Fine-grained Vision-Language Model for Medical Interpretation ｜解剖感知视觉语言模型

研究机构：美国罗格斯大学、美国斯坦福大学

作者：Difei Gu、Yunhe Gao、Mu Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.08402)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.08402)

> 医学影像诊断的核心矛盾在于，全局对比学习将整张胸片压缩为单一向量，导致“肺实变”等术语在上下叶间的语义混淆，且无法区分心脏扩大与肺水肿等共病。现有方法如MedKLIP虽引入知识增强，但仍依赖隐式区域划分，缺乏显式的空间定位能力。Anatomy-VLM通过引入可学习的解剖查询（Anatomy Queries）与目标检测模块，将图像显式分割为29个临床区域，实现区域-文本的细粒度对齐。该方法在长尾分布下显著提升了零样本分类的平衡准确率，但其依赖预计算边界框的设定限制了其在无标注场景下的泛化潜力。

】

---

【AortaDiff: A Unified Multitask Diffusion Framework For Contrast-Free AAA Imaging ｜主动脉瘤无对比剂评估的多任务扩散框架

研究机构：英国牛津大学、德国慕尼黑工业大学

作者：Yuxuan Ou、Ning Bi、Jiazhen Pan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.01498)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01498)

> 腹部主动脉瘤（AAA）的临床评估传统依赖增强CT（CECT），但碘造影剂对肾功能不全患者构成风险，且存在环境负担。现有方法多采用“先生成后分割”的多阶段流水线，导致合成误差累积至分割结果，且无法共享解剖先验。AortaDiff 提出统一多任务扩散框架，在共享骨干上同时执行非增强CT（NCCT）到CECT的图像翻译与主动脉腔/血栓分割，并引入半监督策略应对标注稀缺。该框架在OxAAA数据集上实现了生成与分割的双重提升，但其评估局限于2D切片且未验证3D体积一致性，临床部署的泛化能力存疑。

】

---

【Boosting Medical Vision-Language Pretraining via Momentum Self-Distillation under Limited Computing Resources ｜动量自蒸馏驱动的低资源医学视觉-语言预训练

作者：Phuc Pham、Nhu Pham、Ngoc Quoc Ly

论文原文见 [arXiv](https://arxiv.org/abs/2512.02438)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.02438)

> 医学影像-文本配对数据丰富但标注昂贵，对比学习（Contrastive Learning, CL）是主流预训练范式，但其性能高度依赖大批量训练以获取充足负样本，导致计算资源门槛极高，限制了在资源受限医疗机构的部署。现有动量对比方法在小批量下因硬标签歧义失效，本文切入点在于利用动量编码器的无梯度特性，通过自蒸馏软化对比目标并模拟大有效批量。具体做法是引入动量自蒸馏（Momentum Self-Distillation, MSD）损失与无资源批量扩展（Resource-Free Batch Enlargement, RFBE）机制。该方法在单卡上实现了与多卡SOTA相当的零样本性能，并在少样本适配上取得显著提升，但其有效性边界局限于2D胸片全局对齐，未解决3D细粒度语义对齐的核心难题。

】

---

【brat: Aligned Multi-View Embeddings for Brain MRI Analysis ｜脑MRI多视图对齐表征学习

研究机构：英国牛津大学

作者：Maxime Kayser、Maksim Gridnev、Wanting Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18679)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18679)

> 脑MRI临床报告包含大量分散于3D体积不同区域的细微病灶描述，传统单向量视觉-语言预训练无法捕捉这种空间与语义的多样性，导致下游任务泛化能力受限。本文提出brat框架，借鉴文档检索中的多向量思想，将报告句子作为查询子单元，通过贪心匹配与行列式点过程（DPP）约束，迫使图像特征分解为多个对齐特定临床特征的视图。该方法在80K规模的MSKBrain数据集上验证了检索与分割性能的提升，但其依赖文本报告作为隐式解剖先验，未显式处理拓扑一致性，且88%的异常率可能限制对正常脑结构的表征学习。

】

---

【ConsensusXAI: A framework to examine class-wise agreement in medical imaging ｜共识可解释性框架

研究机构：中国科学院

作者：Abbas Haider、David Wright、Ruth Hogg 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_90687509)

> 现有局部可解释AI方法仅能回答单个样本的决策依据，却无法量化同一类别不同样本间解释的一致性，导致临床信任评估依赖低效的人工抽查。本文提出ConsensusXAI框架，通过潜在空间聚类聚合多实例热力图，生成类级共识图并计算共识对齐分数。该框架填补了从单点解释到全局行为分析的空白，但其评估有效性仍受限于缺乏临床专家盲评验证。

】

---

【ConsensusXAI: A Framework to Examine Class-wise Agreement in Medical Imaging ｜类间解释一致性评估框架

研究机构：中国科学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1884621d1f5b)

> 医学影像深度学习模型在单实例层面生成的解释热力图往往存在显著的空间与语义波动，导致临床专家难以通过随机抽样判断模型是否稳定依赖特定解剖特征。现有评估指标如 AUROC 仅衡量预测精度，无法量化同一类别下多个实例解释的聚合一致性，而人工逐例审查在大规模数据集上不可行。ConsensusXAI 通过引入潜空间聚类与余弦相似度度量，将分散的实例级热力图聚合为类级共识向量，从而量化解释的类间对齐程度。该框架填补了从单实例到类级解释评估的方法空白，但其“共识即正确”的隐含假设及缺乏临床专家盲评验证，限制了其在高风险诊断场景中的直接应用。

】

---

【DermEVAL: A Dermatologist-Reviewed Benchmark for Multimodal Large Language Models ｜皮肤科多模态大语言模型评估基准

研究机构：澳大利亚国立大学

作者：Hongjin Zhao、Weihao Li、Zhenyue Qin 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10b7465f5684)

> 临床皮肤病诊断依赖视觉特征与文本推理的深度融合，但现有基准数据规模小、缺乏专家审核且评估维度单一，导致多模态大语言模型（MLLM）在皮肤科的实际能力被低估或误判。本文切入点在于构建一个大规模、经皮肤科医生审核的图文对数据集，以填补评估空白。通过四步专家-GPT协同标注流程生成11,347个样本，支持视觉问答与医学报告生成任务。该工作提供了评估MLLM临床推理能力的标准化协议，但其诊断精度是否超越专用分类器仍存疑。

】

---

【DuPLUS: Dual-Prompt Vision-Language Model for Universal Medical Image Segmentation and Prognosis ｜双提示视觉-语言框架用于通用医学分割与预后

作者：Numan Saeed、Tausifa Jan Saleem、Fadillah Maani 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c82eb7052fd1)

> 医学影像分析长期受困于任务隔离，单一模型难以同时处理多模态分割与预后预测。现有通用分割模型依赖离散先验或通用文本嵌入，缺乏对解剖层级的细粒度控制，且无法扩展至临床结局预测。DuPLUS 通过层级双提示机制，将模态上下文与目标器官指令解耦，实现了跨模态的文本可控分割，并验证了向预后任务的迁移能力。该框架在多数基准上超越了现有通用模型，但其对结构化提示的依赖限制了其在自由文本场景下的泛化潜力。

】

---

【FairVLM: Enhancing Fairness and Prompt Sensitivity in Vision Language Models for Medical Image Segmentation ｜医学视觉语言分割的公平性与提示鲁棒性

研究机构：美国普渡大学

作者：Md Motiur Rahman、Saeka Rahman、Smriti Bhatt 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1215164a665f)

> 医学视觉语言模型（VLM）在临床部署中面临人口统计偏差与提示敏感性双重挑战，现有方法往往孤立处理二者，导致模型对少数群体及语义变体提示表现不稳定。FairVLM 通过整合语义保留反事实提示、人口统计感知特征归一化及公平校准损失，在统一框架内同时优化公平性与鲁棒性。该方法在眼底图像分割任务上显著降低了组间性能差距，但验证范围局限于2D眼底数据，其在3D体积数据及跨中心场景下的泛化能力存疑。

】

---

【FARF-Net: Frequency-guided Adaptive Receptive Field Network for Edge-enhanced Polyp Segmentation ｜频率引导自适应感受野网络

作者：Xue Li、Aiwen Jiang、Hongqian Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_31d5193cdf20)

> 息肉分割的核心难点在于病变边界与周围黏膜在纹理和颜色上的高度相似性，导致现有模型在复杂成像条件下边界定位模糊。主流方法依赖固定膨胀率的卷积核，无法适应息肉内部与边缘区域截然不同的频率特性，且缺乏显式的边界建模机制，致使高频背景噪声易被误判为前景。本文切入点在于利用频域能量驱动卷积感受野的动态调整，并结合Kolmogorov-Arnold Networks（KAN）进行通道级非线性增强。通过构建频率引导的自适应感受野模块与双监督解码器，FARF-Net在五个基准数据集上实现了SOTA性能，但其33.71M参数量与11.91G FLOPs的计算开销是否满足临床实时部署需求，仍存疑。

】

---

【Fetal and Neonatal Cortical Surface Reconstruction with Anatomical Normal-guidance and Perceptual Enhancements ｜解剖法向量引导与感知增强的胎儿皮层表面重建

研究机构：韩国汉阳大学

作者：Jiyang Lee、Woori Bae、U-Geun Ji 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8de7277f1669)

> 胎儿及新生儿皮层表面重建（Cortical Surface Reconstruction, CSR）旨在从低分辨率、高噪声的MRI中提取高精度皮层几何，以支持皮层厚度与曲率等形态学测量。现有深度学习方法依赖显式分割或符号距离函数（SDF）作为空间先验，在灰白质对比度极低的胎儿数据中易引入早期分割误差并丢失亚体素边界信息。本文提出ANPE框架，通过自适应融合解剖法向量与速度场、直接注入图像梯度特征、以及引入基于预训练VGG的纠缠损失，在不依赖额外预处理步骤的前提下提升重建精度。该方法在dHCP数据集上显著优于CoTAN基线，但其对高度弯曲区域自相交问题的处理仍显不足，且缺乏与最新隐式表示方法的横向对比。

】

---

【FLoMo-Net: A Novel Task-Adaptive Mixture of Experts Routing Framework with Frequency and Uncertainty Correction for Medical Image Segmentation ｜任务自适应专家路由与频域校正的医学图像分割架构

研究机构：加拿大不列颠哥伦比亚大学

作者：Md Rayhan Ahmed、Patricia Lasserre

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_de7c9917e6d7)

> 医学图像分割的核心矛盾在于局部纹理细节与全局解剖上下文的平衡，以及临床部署对低延迟的严苛要求。现有混合架构虽通过引入Transformer或Mamba解决全局建模，但往往面临计算复杂度激增或固定隐状态导致的适应性不足。FLoMo-Net通过引入任务自适应的混合专家（MoE）路由机制替代传统自注意力，并结合频域分解与不确定性校正，在保持线性复杂度的同时提升了边界精度。该架构在多个基准上取得了SOTA性能，但其对预训练权重的依赖缺失及跨域泛化能力的验证不足，限制了其在极端小样本场景下的直接应用。

】

---

【From SAM to DINOv2: Towards Distilling Foundation Models to Lightweight Baselines for Generalized Polyp Segmentation ｜多基础模型频域蒸馏的轻量息肉分割

作者：Shivanshu Agnihotri、Snehashis Majhi、Deepak Ranjan Nayak 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09307)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09307)

> 结肠镜息肉分割面临临床部署中算力受限与跨域泛化弱的双重约束，现有轻量网络缺乏全局语义先验，而大规模基础模型直接迁移则因参数冗余与领域差距难以落地。Polyp-DiFoM 通过多基础模型特征频域分解与双阶段蒸馏，将语义先验注入 U-Net 等轻量骨干，在未见数据集上显著提升泛化能力。该方法以极低计算开销实现了接近重型模型的精度，但其对干净基准的精度提升有限，且未验证视频时序场景下的有效性。

】

---

【HiMix : Hierarchical Visual-Textual Mixing Network for Lesion Segmentation ｜层级视觉-文本混合网络

作者：Soojin Hwang、Jaeyoon Sim、Won Hwa Kim

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_44b8828be389)

> 医学影像分割长期受限于像素级标注的高昂成本，而临床报告中蕴含的解剖位置与病变计数信息常被现有方法忽略。主流多模态方法仅提取文本编码器的最后一层嵌入，丢失了底层语法与中层句法中承载的空间细粒度线索，导致边界分割模糊。本文提出HiMix，通过将文本编码器分层并与解码器层级动态对齐，结合频域自适应细化，实现语义与视觉特征的多尺度协同。该框架在三个基准上刷新了SOTA，但其对结构化文本的依赖及未探索基础模型协同的局限，使其在真实临床场景的泛化能力仍存疑。

】

---

【Histopath-C: Towards Realistic Domain Shifts for Histopathology Vision-Language Adaptation ｜病理视觉语言模型域适应基准与低秩模板集成

作者：Mehrdad Noori、Gustavo Adolfo Vargas Hakim、David Osowiechi 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12493)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12493)

> 病理视觉语言模型（VLM）在临床部署中面临染色、污染等现实域偏移导致的性能骤降，现有测试时适应（TTA）方法在病理图像上表现不稳定且易受文本模板选择影响。本文构建了包含10种合成扰动的基准Histopath-C，并提出低秩适应与传递性模板集成（LATTE）方法，通过多模板损失聚合与LoRA微调提升鲁棒性。该方法在多个病理数据集上显著优于基线，但其对特定扰动类型的适应性及临床泛化能力仍存疑。

】

---

【HumanGuideNet: Adapter-Based Alignment of Deep Neural Networks with Human Similarity Judgments ｜人类相似度判断驱动的适配器对齐

研究机构：美国康奈尔大学

作者：Xufu Liu、Yifan Yang、Zhengxin Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_74f8dc6245d7)

> 深度神经网络（DNN）在视觉任务中常因缺乏人类感知结构而泛化能力受限，现有线性对齐方法难以捕捉复杂的非线性相似度关系。HumanGuideNet 通过引入可训练的人类对齐分支（HumReg），将 THINGS 数据集的奇偶判断信号注入冻结骨干网络，实现了表征几何与人类感知的非线性融合。该方法在少样本分类和异常检测中显著提升了模型性能，但其仅复制最后一层编码块的设计是否足以覆盖全网络的对齐需求，仍存疑。

】

---

【Hymavi : A Hybrid Mamba-Attention Network in Multi-View Framework for Volumetric Medical Image Segmentation ｜并行混合架构与多视角融合

作者：Sy Dat Tran、Jin Kyu Gahm

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ab069a11172b)

> 3D医学图像分割需同时捕获跨切片的长程依赖与局部解剖细节，但Transformer的二次复杂度阻碍高分辨率体积数据处理，而纯Mamba模型缺乏空间自适应交互能力。Hymavi通过并行融合Mamba与Attention机制，并引入轴状、矢状、冠状三视角交互框架，解决了串行堆叠导致的信息覆盖问题。该方法在BraTS2023、ACDC和AMOS22数据集上均取得领先性能，但其多视角平均聚合策略是否最优，以及并行架构在极端各向异性数据上的泛化边界，仍需进一步验证。

】

---

【Improvise, Adapt, Overcome -- Telescopic Adapters for Efficient Fine-tuning of Vision Language Models in Medical Imaging ｜望远镜式适配器

研究机构：印度理工学院

作者：Ujjwal Mishra、Vinita Shukla、Praful Hambarde 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.13855)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13855)

> 医学影像分割模型在跨模态部署时面临标注稀缺与计算资源受限的双重约束，传统全量微调因参数量巨大难以在临床边缘设备落地。现有参数高效微调（PEFT）方法通常对所有Transformer层施加均匀维度的适配器，导致浅层冗余而深层表达不足。本文提出Telescopic Adapters，通过深度感知缩放机制动态分配适配器瓶颈维度，仅用613k可训练参数即在五个医学数据集上超越全量微调与现有PEFT基线。该方法验证了非均匀参数分配在视觉语言分割模型（VLSM）适配中的有效性，但其对动态域漂移及非线性偏移的鲁棒性尚存疑。

】

---

【Integrating Multi-scale and Multi-filtration Topological Features for Medical Image Classification ｜多尺度多滤过拓扑特征融合框架

研究机构：美国北卡罗来纳州立大学、美国圣母大学

作者：Pengfei Gu、Huimin Li、Haoteng Tang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07190)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07190)

> 现有医学影像分类模型过度依赖局部纹理，导致对病变空洞、分支等全局拓扑结构表征不足，而传统持久同调方法受限于单尺度单滤过，难以捕捉跨分辨率的稳定解剖特征。本文切入点在于解决单尺度持久图（Persistence Diagram, PD）在分辨率变化下的不稳定性及单一滤过函数信息缺失问题。通过提出“vineyard”算法追踪跨尺度PD点对应关系，并设计双向交叉注意力编码器融合多滤过特征，实现拓扑信号在骨干网络多层级的门控注入。该方法在三个公开数据集上显著优于基线，但其性能增益高度依赖特定超参数，且在部分基准上未超越对比学习范式的最新SOTA。

】

---

【Intraoperative 2D/3D Registration via Spherical Similarity Learning and Differentiable Levenberg-Marquardt Optimization ｜术中单视图2D/3D配准的球面相似度学习与可微LM优化

研究机构：东南大学

作者：Minheng Chen、Youyong Kong

论文原文见 [arXiv](https://arxiv.org/abs/2509.06890)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.06890)

> 术中单视图2D/3D配准旨在将术中X射线图像与术前CT体积对齐，以指导微创手术中的器械定位。现有基于欧氏空间近似黎曼流形测地线的方法存在局部几何失真与收敛缓慢的瓶颈，导致大偏移下易陷入局部极小值。本文切入点在于将相似度学习扩展至非欧氏球面空间，利用SO(4)双不变性构建更平滑的优化景观，并引入可微Levenberg-Marquardt优化加速收敛。该方法在脊柱与骨盆数据上实现了亚毫米级精度，但其对临床辐射剂量与计算资源的权衡边界尚需进一步验证。

】

---

【MAFM^3: Modular Adaptation of Foundation Models for Multi-Modal Medical AI ｜模块化基础模型适配

研究机构：阿联酋扎耶德大学

作者：Mohammad Areeb Qazi、Munachiso S Nwadike、Ibrahim Almakky 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.11212)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.11212)

> 医学影像基础模型（FM）在单一模态或任务上表现优异，但临床需求动态变化，重新训练每个新任务或模态的模型成本过高且数据稀缺。现有持续学习方法侧重序列扩展，缺乏统一框架同时处理多任务、多模态与解剖区域的模块化扩展，且难以在推理时灵活激活特定能力。MAFM³ 提出一种模块化适配框架，通过冻结骨干并添加轻量级模块（LoRA、MLP、解码器），实现基础模型向新任务与模态的累积式扩展。该框架验证了模块化扩展的可行性，但缺乏对域偏移鲁棒性的系统评估，且未提供计算效率对比。

】

---

【MedPEFT-CL: Dual-Phase Parameter-Efficient Continual Learning with Medical Semantic Adapter and Bidirectional Memory Consolidation ｜双阶段参数高效持续学习框架

研究机构：英国伦敦大学学院

作者：Ziyuan Gao

论文原文见 [arXiv](https://arxiv.org/abs/2511.17668)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17668)

> 医学视觉-语言分割模型在跨机构部署时，因不断适应新解剖结构而面临灾难性遗忘，导致旧任务诊断精度崩塌。现有持续学习方法多针对单模态或通用视觉模型，缺乏对医疗跨模态特性的适配，且全量微调在临床算力受限环境下不可行。MedPEFT-CL 提出双阶段架构，通过语义相似度驱动的适配器分配与双向 Fisher-记忆协调机制，在极低参数开销下实现知识保留。该框架在混合、异构及同构任务序列中均显著降低遗忘率，但其对提示语义相似度的依赖在极端跨模态场景下的鲁棒性存疑。

】

---

【ReBrain: Brain MRI Reconstruction from Sparse CT Slice via Retrieval-Augmented Diffusion ｜稀疏CT驱动的脑MRI重建

研究机构：同济大学

作者：Junming Liu、Yifei Sun、Weihua Cheng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.17068)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17068)

> 临床低剂量CT扫描常因辐射限制导致轴向切片稀疏，直接用于跨模态MRI合成会引发严重的体积连续性断裂。现有跨模态翻译方法假设源数据密集，而模态内插值方法无法处理CT到MRI的域差异，导致重建结果在层间出现解剖结构漂移。ReBrain通过引入基于检索增强的布朗桥扩散模型（BBDM），利用外部知识库中的相似切片作为结构控制信号，填补了稀疏输入下的信息空白。该框架在稀疏条件下实现了SOTA性能，但其对知识库覆盖率的依赖及2D切片处理的局限性，限制了其在极端病理或全新解剖结构场景下的泛化能力。

】

---

【Semi-supervised Key-Point Estimation for Echocardiography Video ｜半监督关键点轨迹精修

研究机构：韩国科学技术院、韩国首尔大学

作者：Seok-Hwan Oh、Hyeon-Jik Lee、Guil Jung 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c418f3c16005)

> 超声心动图（Echo）视频分析的核心痛点在于左心室（LV）关键点轨迹的时序抖动，这直接导致射血分数等临床指标计算失准。现有方法多依赖单帧静态标注，缺乏帧间关联建模，且全视频密集标注成本极高，难以在临床落地。本文切入点在于利用光流生成伪标签并结合像素级补丁相关性损失，以半监督方式迭代精修关键点相对坐标。该方法在自建数据集上实现了空间精度与时间稳定性的双重提升，但其泛化能力受限于特定视图与标注协议，临床普适性存疑。

】

---

【SSMT-Net: A Semi-Supervised Multitask Transformer-Based Network for Thyroid Nodule Segmentation in Ultrasound Images ｜半监督多任务甲状腺超声分割网络

研究机构：韩国汉阳大学、韩国首尔大学

作者：Muhammad Umar Farooq、Abd Ur Rehman、Azka Rehman 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7f0429b2e8fa)

> 甲状腺超声结节分割面临标注稀缺与边界模糊的双重约束，现有单任务CNN模型难以兼顾全局上下文与局部细节。本文切入点在于利用无监督重建预训练挖掘未标注数据价值，并引入腺体分割与尺寸估计作为辅助任务以正则化主任务表征。通过Transformer-CNN双解码器架构，实现了半监督多任务联合优化。该方法在TN3K数据集上刷新了DSC纪录，但其全量微调策略与当前参数高效微调的主流趋势存在潜在冲突，且缺乏跨域泛化验证。

】

---

【SSplain: Sparse and Smooth Explainer for Retinopathy of Prematurity Classification ｜稀疏平滑解释器

研究机构：美国东北大学

作者：Elifnur Sunger、Tales Imbiriba、Peter Campbell 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.08038)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.08038)

> 医学影像诊断中，黑盒模型的像素级解释常因忽略解剖结构而失去临床可信度。通用解释器生成的归因图往往碎片化或违背血管连通性，导致医生无法将其与病理特征对应。SSplain 通过引入稀疏性与平滑性约束，在优化过程中直接生成符合眼底图像结构的解释掩码。该方法在 ROP 数据集上优于九种基线，但其解释仍停留在像素结构层面，未触及临床语义概念，临床监管价值存疑。

】

---

【Test-Time Adaptation through Semantically-guided Feature Decomposition for Few-shot Chest X-ray Diagnosis ｜语义引导特征解耦与测试时适应的少样本胸片诊断

研究机构：印度理工学院、美国国立卫生研究院

作者：Jayant Mahawar、Angshuman Paul

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c830629d15bd)

> 胸片少样本学习（Few-Shot Learning, FSL）旨在解决标注数据稀缺下的病理识别难题，但现有方法常因类内视觉模式重叠及跨域分布偏移导致泛化失效。本文切入点在于将视觉特征显式分解为类特定与类无关成分，并引入测试时适应机制以应对数据分布变化。具体做法是利用双潜空间自编码器结合BioBERT语义签名引导聚类，并在推理阶段通过不变分支特征邻近性更新表示。该方法在三个主流数据集上实现了3-5%的AUROC提升，但其对复杂设备伪影的鲁棒性及F1分数在部分数据集上的持平表现仍存疑。

】

---

【UI-Styler: Ultrasound Image Style Transfer with Class-Aware Prompts for Cross-Device Diagnosis Using a Frozen Black-Box Inference Network ｜超声跨设备风格迁移中的类别感知提示机制

研究机构：国立阳明交通大学

作者：Nhat-Tuong Do-Tran、Ngoc-Hoang-Lam Le、Ching-Chun Huang

论文原文见 [arXiv](https://arxiv.org/abs/2511.17155)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17155)

> 超声影像跨设备部署面临外观差异导致的诊断性能下降，传统无配对图像翻译方法仅对齐域级分布，忽略类别语义对齐，导致翻译后图像出现类别混淆。现有提示微调方法依赖模型内部特征或梯度，无法适用于仅返回最终预测的黑盒商业模型。UI-Styler 提出双层级风格化机制，通过模式匹配对齐域级外观，利用伪标签引导的类别感知提示校正语义方向。该方法在12项跨设备任务中实现了分布距离与下游任务性能的最优，但其有效性依赖于黑盒模型在目标域具备足够的基线判别能力，且未验证对模型内部结构变化的鲁棒性。

】

---

【Uncertainty-Aware Vision-Language Segmentation for Medical Imaging ｜不确定性感知视觉-语言分割

研究机构：印度理工学院坎普尔分校

作者：Aryan Das、Tanishq Rachamalla、Koushik Biswas 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.14498)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.14498)

> 医学影像分割长期依赖像素级标注，而临床场景中标注稀缺且影像质量参差，导致模型在模糊区域产生过自信错误。现有视觉-语言分割（Vision-Language Segmentation, VLS）方法虽引入文本引导，但普遍忽视训练过程中的不确定性建模，且基于Transformer的跨模态融合计算开销巨大。本文通过引入状态空间模型（State Space Model, SSM）实现高效长程依赖建模，并设计频谱-熵不确定性（Spectral-Entropic Uncertainty, SEU）损失统一优化空间、频谱与概率约束。该方案在三个基准上以更低参数量取得SOTA性能，但其对3D体积数据的适用性及文本语义深度的挖掘仍存疑。

】
