# CVPR2026 · 医学与生物AI方向论文汇编

> 本方向共 94 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Act Like a Pathologist: Tissue-Aware Whole Slide Image Reasoning ｜组织感知层级选择框架

研究机构：美国石溪大学、美国斯坦福大学

作者：Wentao Huang、Weimin Lyu、Peiliang Lou 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00667)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00667)

> 病理视觉问答（Pathology VQA）需从千兆像素全切片图像（WSI）中提取与特定临床问题相关的局部证据，但现有多模态大语言模型（MLLM）依赖均匀采样或全局注意力，导致大量无关组织区域干扰推理且缺乏可解释性。本文提出HistoSelect，通过模拟病理学家“先定位组织区域、再聚焦关键切片”的粗到细诊断流程，构建基于信息瓶颈（Information Bottleneck, IB）原理的层级选择机制。该方法在三个基准上取得最高准确率，平均减少70%视觉token，但仅验证了H&E染色场景下的选择有效性，未评估跨染色协议或复杂肿瘤微环境下的泛化边界。

】

---

【Adaptive Anisotropic Gaussian Splatting for Multi-contrast MRI Arbitrary-Scale Super-Resolution with Anatomy Guidance ｜解剖先验引导的2D高斯泼溅多对比度MRI任意尺度超分

研究机构：华东师范大学

作者：Qiuhai Yan、Kang Chen、Zhengjie Lu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f5427fb7dfd)

> 多对比度MRI超分旨在利用快速高场参考序列恢复慢速低分辨率目标序列的细节，但现有隐式神经表示方法受频谱偏置影响，难以重建锐利的解剖边界。本文切入点在于将图像表示从像素强度回归转换为各向异性2D高斯参数优化，以规避低频收敛陷阱。通过引入结构先验调制、双域交叉注意力及解剖引导的高斯参数化器，模型在IXI数据集4倍超分任务中取得32.03 dB的PSNR，显著优于基线DINet的30.98 dB。该方法在任意尺度泛化上表现稳健，但未验证其在缺乏解剖先验或分布外数据上的鲁棒性。

】

---

【Anatomica: Localized Control over Geometric and Topological Properties for Anatomical Diffusion Models ｜解剖扩散模型的局部几何-拓扑推理时控制

研究机构：美国麻省理工学院、瑞士洛桑联邦理工学院

作者：Karim Kadry、Abdallah Abdelwahed、Shoaib Goraya 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.20587)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20587)

> 解剖结构生成需同时满足几何形态与拓扑连通性约束，但现有条件生成方法依赖重训练且缺乏局部空间定位能力。Anatomica 提出基于立方体控制域的推理时引导框架，通过可微分解析潜空间子结构并计算几何矩与持久同调势函数，实现无需重训练的局部属性控制。该方法在心脏与主动脉数据集上验证了控制保真度，但高维拓扑计算成本限制了分辨率上限。

】

---

【Any2Any 3D Diffusion Models with Knowledge Transfer: A Radiotherapy Planning Study ｜跨域扩散先验迁移与临床偏好对齐的放疗剂量预测框架

研究机构：美国华盛顿大学

作者：Yuhan Wang、Zihan Li、Han Liu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.09622)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.09622)

> 放疗剂量预测（Dose Prediction, DP）旨在从多模态临床数据生成3D剂量分布，但现有模型因数据量小且缺乏临床偏好对齐，难以泛化至不同机构。本文切入点在于利用大规模视频或CT预训练的扩散模型先验，通过Any2Any条件机制处理异构模态，并引入基于临床评分卡的强化学习后训练。该框架在GDP-HMM挑战中实现了1.93 Gy的MAE，优于基线2.07 Gy，但推理耗时约10秒，且依赖预训练骨干的域适配能力。

】

---

【BackSplit: The Importance of Sub-dividing the Background in Biomedical Lesion Segmentation ｜背景分解提升病灶分割统计效率

研究机构：美国康奈尔大学

作者：Rachit Saluja、Asli Cihangir、Ruining Deng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.19394)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19394)

> 医学影像中小病灶分割长期受困于假阳性高与边界模糊，根源在于传统二分类将异质解剖背景坍缩为单一类别，丢失了区分病灶与周围组织的几何语义信息。现有架构优化或损失函数设计未能触及这一标签空间层面的统计效率损失，本文切入点在于重新定义背景监督结构。通过引入辅助解剖结构作为多分类标签联合训练，BackSplit在不增加推理成本的前提下提升了病灶定位精度。该范式在理论上证明了多分类训练具有更高的期望Fisher信息，但在极端少样本或无标注场景下的泛化能力尚存疑。

】

---

【Beyond Objects: Contextual Synthetic Data Generation for Fine-Grained Classification ｜超越对象：面向细粒度分类的上下文合成数据生成

研究机构：美国普林斯顿大学、谷歌DeepMind

作者：William Yang、Xindi Wu、Zhiwei Deng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24078)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24078)

> 细粒度分类中，基于文本到图像（T2I）模型生成合成数据时，少样本微调极易导致模型过拟合，丢失类内多样性并引入类间虚假关联。现有微调方法仅关注概念保真度，忽视了背景与姿态等无关属性对分类边界的干扰。BOB 通过提取类无关属性并在微调时保留、生成时边缘化，解耦了类别特征与上下文噪声。该方法在通用视觉基准上显著提升了少样本分类精度，但其依赖文本属性建模，能否迁移至依赖空间结构的医学影像任务尚存疑。

】

---

【BiGMINT: Biologically-guided Hierarchical Multimodal Integration for Modeling Multiple Compound Activities in Drug Discovery ｜生物引导层级多模态集成

作者：Pushpak Pati、Bo Li、Abbas Rayabat Khan 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e58b38a70766)

> 化合物活性建模旨在通过计算预测小分子对特定蛋白靶点的调控效应，以替代高成本的湿实验筛选。现有单模态方法或依赖化学蛋白质组学忽略表型后果，或依赖高内容成像（HCI）缺乏分子机制解释，导致在稀疏标签下泛化能力受限。本文提出BiGMINT，通过化学蛋白质组学引导HCI特征聚合及蛋白质-蛋白质相互作用（PPI）先验增强，实现层级多模态融合。该方法在大规模内部数据集上显著提升了预测精度与高绩效任务覆盖率，但其依赖内部专有数据且未公开代码，限制了外部复现与横向对比。

】

---

【BiomedCCPL: Causal Conditional Prompt Learning for Biomedical Vision-Language Models ｜因果条件提示学习

研究机构：南方科技大学、深圳大学

作者：Xueliang Cui、Juncai Zhang、Jiacheng Hou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0437e3382b79)

> 医学视觉-语言模型在少样本适配中常因过拟合已见类的伪相关特征而丧失对未见类的泛化能力。现有静态或全局动态提示方法无法区分诊断性因果特征与非诊断性捷径特征。本文通过多尺度自适应视觉原型生成图像条件提示，并引入前门调整机制解耦因果与非因果表示。该框架在11个数据集上实现了少样本适配与跨类泛化的双重提升，但其因果解耦的有效性是否依赖于特定的模态分布，仍需更多验证。

】

---

【BiOTPrompt: Bidirectional Optimal Transport Guided Prompting for Disease Evolution-aware Radiology Report Generation ｜双向最优传输引导的纵向放射学报告生成

研究机构：北京大学、澳大利亚悉尼科技大学

作者：Tengfei Liu、Yijian Fan、Boyue Wang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3baf69457e3a)

> 纵向放射学报告生成旨在通过对比当前与历史影像来量化疾病进展，但现有方法多依赖全局特征融合或静态提示，难以捕捉空间错位下的非对称病变演化。BiOTPrompt 切入这一盲区，利用双向最优传输（Bidirectional Optimal Transport, BiOT）显式建模补丁级软对应，识别新发与消退区域。该方法将演化区域编码为动态提示引导大语言模型（Large Language Model, LLM），并引入视觉-语言一致性约束抑制幻觉。实验表明其在临床准确性上优于现有纵向基线，但仅验证了双时间点场景，对长序列随访的扩展性存疑。

】

---

【Breaking the Continuum: Discrete Distribution Learning for Structural MRI Reconstruction ｜离散连续合成框架

作者：Tianle Lyu、Mengjingcheng Mo、Ting Wen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a51dcb2fdb26)

> 加速MRI重建旨在从欠采样k-space数据中恢复完整图像，这是一个病态逆问题。现有基于连续扩散模型的方法假设图像流形平滑，导致解剖边界模糊，难以满足临床诊断对结构清晰度的要求。DiCoS通过引入离散结构假设生成与微扩散精炼机制，在保留解剖语义的同时恢复纹理细节。该框架在fastMRI基准上取得了SOTA性能，但其离散假设的多样性是否足以覆盖所有病理变体，仍需进一步验证。

】

---

【Bridging RGB and Hematoxylin Components: An Interleaved Guidance and Fusion Framework for Point Supervised Nuclei Segmentation ｜双模态互补融合的点监督核分割网络

作者：Zihan Huan、Xipeng Pan、Hualong Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_411ab3597707)

> 病理图像核实例分割依赖昂贵的像素级标注，而点标签虽能降低标注成本，但现有方法仅利用单一图像模态，忽略了RGB与Hematoxylin分量间的互补信息。本文指出单一模态在弱监督下存在结构性盲区，提出DFGNet框架，通过双分支编码、跨尺度动态融合及交错引导机制联合建模两种表示。该设计在点监督设定下提升了边界定位精度，但其性能增益是否源于对特定染色伪影的过拟合，仍需更严格的跨域验证。

】

---

【CG-Reasoner: Centroid-Guided Positional Reasoning Segmentation for Medical Imaging with a Robust Visual-Text Consistency Metric ｜质心引导的位置推理分割

作者：Lakshmikar Reddy Polamreddy、Ming Ma

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_974a9d7ade2a)

> 医学影像分割模型长期面临“像素准确但语义空洞”的困境，即能画出病灶边界却无法用人类可理解的语言描述其空间位置，导致自动化报告生成缺乏临床可信度。现有方法将分割与语言推理视为独立任务，缺乏几何一致性约束，导致推理文本与掩码位置脱节。本文通过引入Text2Centroid模块将文本映射为空间坐标，并设计PRScore指标联合评估语义与空间对齐，实现了分割与位置推理的统一。该框架在六类模态上取得了领先的分割精度与推理一致性，但其依赖2D质心假设，对复杂非凸病灶的适应性存疑。

】

---

【CMR-RD: Long-Tailed Adaptive VLM for Explainable CMR Diagnosis ｜长尾自适应视觉语言模型用于可解释心脏磁共振诊断

作者：Yansong Li、Zhongxi Qiu、Yun Tian 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1df9f32b3b2c)

> 心脏磁共振（CMR）诊断面临罕见病样本稀缺与模型推理不可解释的双重困境，导致现有视觉语言模型（VLM）在长尾分布下对少数类识别能力显著退化。通用强化学习（RL）后训练因采样偏差进一步加剧了多数类主导，而静态平衡策略缺乏训练阶段的动态适应性。本文提出CMR-RD，通过两阶段训练框架结合Group-Phased Policy Optimization（GPPO）算法，利用Thompson Sampling动态调整采样权重以缓解长尾偏差，并引入病灶接地奖励增强空间一致性。该方法在自建CMR数据集上实现了优于通用及医疗VLM的诊断准确率，但其有效性局限于内部数据，缺乏跨中心验证。

】

---

【CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference ｜概念引导特征编辑与蒸馏

作者：Nurjahan Sultana、Moi Hoon Yap、Xinqi Fan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.31591)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.31591)

> 皮肤癌筛查模型在从专家皮肤镜图像迁移至手机临床照片时性能骤降，传统无监督域适应方法仅对齐像素级统计分布，忽略了跨域共享的临床语义概念。CoFiDA-M 利用训练期可用的 MONET 概念概率作为特权信息，通过 FiLM 调制编辑教师网络特征，再蒸馏至仅依赖图像的静态学生模型。该方法在未见临床数据集上实现了 AUROC 与黑色素瘤召回率的双重提升，但其静态部署策略在分布剧烈漂移下的鲁棒性尚存疑。

】

---

【CURE: Curriculum-guided Multi-task Training for Reliable Anatomy Grounded Report Generation ｜课程引导的多任务训练框架

研究机构：沙特阿拉伯阿卜杜拉国王科技大学

作者：Pablo Messina、Andrés Villa、Juan León Alcázar 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15408)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15408)

> 医学视觉-语言模型（VLM）在生成放射报告时，常出现文本描述与图像证据脱节的幻觉现象，导致临床不可信。现有模型如 MAIRA-2 虽引入接地任务，但训练数据中异常发现的过采样导致模型对正常区域产生假阳性。CURE 通过误差感知课程学习动态调整采样分布，在不增加数据的前提下提升视觉接地与事实一致性。该框架在解剖接地报告生成任务上显著降低幻觉率，但其对长尾病理的覆盖能力仍受限于当前课程设计的粒度。

】

---

【D$^2$-FOSA: Dual-Diffusion Guided EEG-to-Image Reconstruction with Frequency-Oriented Semantic Alignment ｜频率导向双扩散框架

研究机构：北京航空航天大学

作者：Chenglong Yu、Shuai Shen、Xiangsheng Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_72f05670fcde)

> 脑电视觉解码旨在从低信噪比信号中还原感知内容，核心瓶颈在于传统编码器忽略频率特异性神经动力学，且对比学习难以弥合模态鸿沟。现有方法多依赖通用时空特征提取，缺乏对Beta/Gamma等关键频带的针对性增强，导致语义对齐精度受限。D2-FOSA通过频率导向Mamba编码器提取判别性特征，并引入双向扩散潜变量生成器强制生成一致性，实现从检索到高保真重建的闭环。该框架在200-way检索任务上超越同期基线，但跨被试泛化能力仍受限于缺乏大规模预训练，其性能优势是否源于特定频带假设尚存疑。

】

---

【D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation ｜基于拟凹性的统一可微分凸形状先验

研究机构：美国亚利桑那州立大学

作者：Shengzhe Chen、Hao Yan

论文原文见 [arXiv](https://arxiv.org/abs/2605.19210)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.19210)

> 医学图像分割在数据稀缺或噪声环境下常产生孔洞与断裂等解剖不合理预测，而传统凸性约束因依赖离散求解器或特定阈值，难以与端到端深度网络集成。本文切入点在于将凸性从“单一二值掩膜的集合约束”转化为“连续分割函数的拟凹性约束”，从而消除阈值依赖并实现全函数域的可微分优化。通过推导零阶、一阶及二阶导数条件，构建局部可微分惩罚项并嵌入网络，该方法在多个近凸解剖结构数据集上显著提升了边界正则性。其价值在于提供了统一的数学框架以解释既往离散与连续凸性先验，但在非凸结构及3D体积计算效率上的适用性仍存疑。

】

---

【DARC: Dual Adjustment Reasoning with Counterfactuals for Trustworthy Chest X-ray Classification ｜双调整反事实推理框架

研究机构：中南大学

作者：Zhifang Liao、Junhao Li、HaoKang Ding 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_52185804dc90)

> 胸部X光（CXR）多标签分类模型常因病理共现与非病理视觉混杂产生捷径学习，导致临床部署中的鲁棒性失效。现有因果去偏方法仅能处理单一混淆源，且缺乏像素级混杂标注支撑精确干预。DARC通过构建首个像素级非病理混杂数据集CheXconf，并设计双流因果架构，同时执行后门调整与反事实推理以解耦两类混淆。该框架在因果纯度上优于单一去偏基线，但分类精度低于纯统计依赖建模的SOTA，其临床价值取决于对因果解释与预测精度的权衡。

】

---

【Decoding 3D Perception via BrainSSD: Synergistic Fusion of EEG Representations from Static and Dynamic Visual Streams ｜脑电3D感知解码：静态与动态视觉流的协同融合

研究机构：西北工业大学

作者：Yincheng Yao、Enze Shi、Shu Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c50137765009)

> 脑电神经解码旨在从非侵入式信号中还原视觉内容，但现有方法多局限于静态2D图像，无法捕捉真实世界中3D物体运动时的神经动力学。BrainSSD通过引入层级相位-幅度耦合引导融合机制，协同整合静态图像与旋转视频诱发的双路EEG信号，构建了面向3D几何重建的解码框架。该框架在判别与生成任务上均超越了单流基线，并首次提供了静态流主导整体形态、动态流解析精细几何的功能特异性视觉证据。其价值在于将神经同步性量化为可微分计算模块，但受限于单一数据集与缺乏跨被试验证，其泛化能力仍存疑。

】

---

【Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models ｜基于视觉基础模型特征谱的医学图像随机不确定性量化

研究机构：西安电子科技大学

作者：Ruiyang Li、Fang Liu、Licheng Jiao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10963)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10963)

> 医学影像分割面临数据固有噪声与标注歧义导致的训练不稳定，现有方法多聚焦于模型预测的不确定性估计，而忽视了数据本身的随机性（Aleatoric Uncertainty, AU）。本文切入点在于利用视觉基础模型（VFM）的任务无关特征空间，通过奇异值分解（SVD）能量分布量化样本难度，实现无标注依赖的数据清洗与动态优化。该方法通过SVD能量熵构建语义感知尺度，并据此过滤噪声样本及调整损失权重。其价值在于提供了一种通用的数据质量治理工具，但实验仅验证了其在监督学习场景下的增益，未探讨其在半监督或无标注数据利用中的有效性。

】

---

【Diffusion MRI Transformer with a Diffusion Space Rotary Positional Embedding (D-RoPE) ｜扩散磁共振成像的球面几何表征学习

研究机构：美国斯坦福大学

作者：Gustavo Chau Loo Kung、Mohammad Abbasi、Camila Blank 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25977)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25977)

> 扩散磁共振成像（dMRI）旨在从多方向、多b值的稀疏采样中恢复脑组织微观结构，但现有深度学习模型难以同时捕捉空间连续性与扩散方向的球面几何依赖，导致跨协议泛化能力受限。本文指出，传统视觉Transformer中基于线性序列的相对位置编码无法适配dMRI中b向量在单位球面上的分布特性，且固定协议假设阻碍了通用表征的提取。为此，论文提出扩散空间旋转位置编码（D-RoPE），将旋转矩阵中的相对距离替换为b值差与b向量夹角的加权组合，并结合交替掩码自编码进行预训练。该方法在脑龄预测与轻度认知障碍分类中取得了优于全监督基线的结果，但其表征在临床任务上的绝对性能仍落后于专用基础模型，且计算开销限制了实时应用。

】

---

【Diffusion-Based Native Adversarial Synthesis for Enhanced Medical Segmentation Generalization ｜扩散模型原生对抗合成

研究机构：吉林大学

作者：Hongyu Zhang、Haipeng Chen、Zhimin Xu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c8a0ccbe574)

> 医学影像分割模型的泛化能力受限于隐私法规与标注成本，传统合成数据增强往往陷入“视觉逼真但效用低下”的困境。现有方法要么依赖昂贵的联合训练，要么通过离流形扰动制造虚假对抗样本，导致下游性能不升反降。本文提出“原生对抗性”概念，指出仅当合成样本处于数据流形内部且对下游模型构成高损失时，才能有效驱动泛化增益。通过一个轻量级噪声重选模块，在不修改冻结扩散模型的前提下挖掘此类样本，实现了跨骨干、跨域的一致性能提升。该方法在理论解耦与工程轻量化上具有显著价值，但其对初始掩码质量的依赖及3D扩展性仍存疑。

】

---

【Disentangle-then-Align: Non-Iterative Hybrid Multimodal Image Registration via Cross-Scale Feature Disentanglement ｜混合多模态图像配准网络

研究机构：澳大利亚悉尼科技大学、安徽大学

作者：Chunlei Zhang、Jiahao Xia、Yun Xiao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19623)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19623)

> 多模态图像配准旨在消除不同成像机制导致的几何错位与外观差异，但现有方法往往局限于单一变换类型或串行级联结构，难以同时处理全局错位与局部形变。HRNet 通过构建统一的共享特征空间，将刚性参数与非刚性位移场在同一管线内联合预测，解决了串行混合配准中误差累积与表示空间割裂的问题。该框架在四个自然场景数据集上实现了重投影误差的显著降低，但其有效性依赖于监督真值，且未验证在缺乏密集标注的医学或极端域偏移场景下的泛化能力。

】

---

【Dissecting Model Failures in Abdominal Aortic Aneurysm Segmentation through Explainability-Driven Analysis ｜可解释性引导的编码器塑形：XAI-SAM在复杂腹主动脉瘤分割中的应用

研究机构：美国西北大学

作者：Abu Noman Md Sakib、Merjulah Roby、Zijie Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24801)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24801)

> 导读 腹主动脉瘤（AAA）分割在薄壁、低对比度及邻近血管干扰等复杂场景下，现有模型常因内部注意力弥散或错位导致概率质量分配错误。传统损失函数仅优化像素级误差，无法直接约束编码器“看哪里”，导致模型在关键临床病例上失效。本文提出XAI-SAM框架，将基于梯度的归因图（XAI field）作为一等训练信号，通过焦点对齐损失与解剖学一致性正则化重塑编码器表征与解码过程。该方法在复杂病例中显著提升了分割精度，但147例的小样本量与单一CT模态限制了其泛化边界的验证。

】

---

【Divide, Conquer, and Aggregate: Asymmetric Experts for Class-Imbalanced Semi-Supervised Medical Image Segmentation ｜分治聚合：面向类别不平衡半监督医学图像分割的非对称专家框架

研究机构：上海交通大学

作者：Yajun Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bb04aec43335)

> 半监督医学图像分割（SSMIS）旨在利用少量标注与海量无标注数据缓解临床标注成本瓶颈，但在多器官场景下，通用方法常因类别不平衡导致小器官分割性能急剧下降。现有类别不平衡SSMIS方法多依赖单解码器架构，其共享参数易被多数类梯度主导，从根本上限制了尾部类别的分割能力。本文提出“分治聚合”（DCA）框架，通过静态划分类别、训练三个非对称专家解码器并动态聚合特征，从架构层面解耦了不平衡任务。该框架在Synapse和AMOS数据集上显著优于现有SOTA方法，但其静态划分策略对类别分布的稳定性依赖较高，在极端动态分布下的泛化能力存疑。

】

---

【DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging ｜动态域增量学习中的自适应知识保留

研究机构：厦门大学、中山大学

作者：Yuxi Ma、Sujie Liu、Jing Yang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_932a8f174c66)

> 临床部署中，医学影像模型面临设备、协议与疾病亚型的持续演化，传统域增量学习（DIL）假设标签空间固定，无法应对新诊断类别的动态引入。现有基于提示或固定秩适配器的方法在动态标签场景下，因表征容量僵化与跨域干扰导致灾难性遗忘。本文提出DK-DDIL，通过动态秩调节适配器与原型级对比精炼，在无重放约束下实现标签空间扩展下的稳定适应。该方法在皮肤病理与3D MRI基准上超越SOTA，但其对动态秩超参数的敏感性及缺乏统一验证器，限制了其在真实临床流式数据中的直接落地。

】

---

【EEGiT: Teaching Vision Transformers to Understand the EEG signal ｜视觉Transformer迁移解码脑电

研究机构：西安电子科技大学

作者：Jiahao Zhou、Chenghao Xu、Wei Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d837f0d1f8db)

> 脑电（EEG）解码的核心困境在于高质量配对数据稀缺，导致传统随机初始化的编码器难以捕捉复杂语义。现有方法依赖EEG自监督预训练或专用时空卷积，但受限于低信噪比与跨被试变异性，泛化能力受限。EEGiT通过构建解剖学对齐的EEG Patch，直接复用ImageNet预训练的视觉Transformer（ViT）作为编码器，利用视觉先验加速收敛并增强跨模态对齐。该方法在跨被试检索任务中达到当前SOTA水平，但其将时序信号强行映射为静态图像结构的假设，是否丢失了关键的神经动力学信息，仍存疑。

】

---

【Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models ｜检索增强医学视觉语言模型持续学习

研究机构：复旦大学、中南大学

作者：Zizhi Chen、Yizhen Gao、Minghao Han 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.13072)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13072)

> 医学视觉语言模型（VLM）在跨域增量任务中面临灾难性遗忘与预训练知识退化的双重困境，传统静态回放或生成式参考集无法适配医学影像“域内同质、域间异质”的簇状分布。本文切入点在于利用检索增强生成（RAG）构建动态参考集，通过多阶段检索与动态Fisher权重保护，在缺乏原始预训练数据访问权限下维持零样本能力。该方法在自建MGTIL基准上取得SOTA性能，但其泛化性受限于自建数据集，且未验证在标准VLP基准上的迁移效果。

】

---

【From Panel to Pixel: Zoom-In Vision-Language Pretraining from Biomedical Scientific Literature ｜从面板到像素：基于生物医学文献的层级化视觉-语言预训练

研究机构：法国国家科学研究中心、德国慕尼黑工业大学

作者：Kun Yuan、Min Woo Sun、Zhen Chen 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.02566)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.02566)

> 生物医学视觉-语言模型（Medical VLP）长期受限于科学文献中多面板图表的粗粒度对齐，导致模型在细粒度结构识别上表现不佳。现有方法要么依赖昂贵的人工标注，要么牺牲粒度以换取数据规模，无法同时实现可扩展性与细粒度监督。本文提出 Panel2Patch 流水线，利用视觉标记自动挖掘图-面板-区域三级层级化数据，并通过层级消息传递机制优化嵌入空间。该方法以 400K 数据对超越了使用 15M-24M 数据对基线，验证了数据质量优于规模的有效性，但其对科学文献排版规范的依赖限制了向非结构化临床影像的泛化能力。

】

---

【Harmonized Feature Conditioning and Frequency-Prompt Personalization for Multi-Rater Medical Segmentation ｜多标注者医学图像分割中的噪声解耦与频域个性化

研究机构：伊朗谢里夫理工大学、瑞士伯尔尼大学

作者：Sanaz Karimijafarbigloo、Armin Khosravi、Alireza Kheyrkhah 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08210)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08210)

> 多标注者分割旨在建模临床诊断中固有的边界歧义，但现有方法常将扫描仪伪影与专家风格差异混淆，导致不确定性估计失真。本文切入点在于显式分离数据级噪声与标注者级变异性，通过噪声协调器标准化潜在特征，并利用频域提示模块捕捉专家个性化风格。该框架在LIDC-IDRI和NPC-170数据集上实现了分布拟合与个性化精度的双重提升，但其对3D体积数据的适用性及跨中心泛化能力尚存疑问。

】

---

【HUMAPS-4D: A Multimodal Dataset for HUman Motion Analysis with Physiological and Semantic informations ｜HUMAPS-4D：基于足底压力与生理信号的多模态人体运动分析数据集

作者：Matthieu Dabrowski、Ouala Ben Jemaa、Benjamin Allaert

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9145f5452b53)

> 现有生物力学分析依赖昂贵的光学标记点系统或隐私受限的视觉传感器，而嵌入式设备虽具隐私优势却缺乏全身运动精度。本文切入点在于构建首个融合足底压力、表面肌电（sEMG）、惯性测量单元（IMU）与语义标注的大规模同步数据集，以填补非视觉生物力学分析的数据空白。通过建立从足部局部信号推断全身3D姿态的基线模型，验证了多模态融合在动作识别中的有效性，但全身姿态重建精度仍远低于视觉方法，其临床可用性存疑。

】

---

【Hyperbolic Relational Prompts for Intersectional Fairness in Medical VLMs ｜超球面关系提示用于医学视觉语言模型的交叉性公平

研究机构：香港城市大学、中国科学院

作者：Jiayu Qian、Zongxian Yang、Guanxing Chen 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e57a4fbc78ab)

> 医学视觉语言模型（VLMs）在处理种族与性别等敏感属性时，常因单属性去偏导致另一属性偏差放大，即交叉性盲区。现有提示学习方法将样本孤立处理，缺乏跨样本的公平性推理能力，无法捕捉属性间的层级依赖。FRP 将提示生成重构为动态图推理过程，利用超球面几何建模敏感属性的层级结构，在冻结 CLIP 骨干上实现公平性与诊断精度的同步提升。该方法在青光眼诊断任务上显著优于基线，但其对属性层级假设的依赖及跨域泛化能力尚存疑。

】

---

【IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation ｜交互式智能体驱动的医学图像分割

研究机构：浙江大学

作者：Yankai Jiang、Qiaoru Li、Binlu Xu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03054)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03054)

> 医学多模态大语言模型（MLLM）在像素级理解上长期受限于单次前向传播与隐式分割令牌的架构束缚，导致跨域泛化能力薄弱且推理逻辑不透明。IBISAgent 将分割任务重构为多步马尔可夫决策过程，通过解耦视觉接地与掩码预测，使模型能像人类标注员一样进行迭代式点击交互与自我修正。该方法无需修改模型架构，仅依靠冷启动监督微调与细粒度强化学习即可实现高质量分割。尽管在域内与零样本任务上显著超越现有 SOTA，但其多步交互带来的推理延迟与对私有数据集的依赖，仍制约着其在实时临床场景中的直接落地。

】

---

【Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset ｜指令引导胸部X光病灶分割

研究机构：韩国科学技术院

作者：Geon Choi、Hangyul Yoon、Hyunju Shin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.15186)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.15186)

> 放射科医生在解读胸部X光（CXR）时，需将视觉证据与临床知识结合，精准定位病灶边界。现有视觉-语言模型（VLM）虽能执行指代图像分割（RIS），但受限于单一病灶类型及依赖专家级长文本输入，难以满足非专家用户或快速筛查需求。本文提出指令引导病灶分割（ILS）任务，构建首个全自动生成的百万级数据集MIMIC-ILS，并微调LISA模型得到ROSALIA，实现多类型病灶的灵活分割与缺失确认。该工作填补了CXR领域细粒度空间接地数据的空白，但其自动化标注的噪声边界与临床可用性阈值仍存疑。

】

---

【KAMP: Knowledge-Anchored Multimodal Pretraining Framework for Medical Image Representation ｜知识锚定多模态预训练

作者：Feiyu Huang、Jia Li、Zhao Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ccff74171869)

> 医学影像与病理、基因组数据的配对稀缺且模态间存在统计偏差，导致直接对比学习易陷入虚假相关。现有单模态或双模态方法无法在少样本场景下提供足够的语义深度，而直接引入多模态又因噪声加剧对齐不稳定。KAMP 利用大语言模型生成个性化诊断知识作为“语义锚点”，通过三阶段训练解耦知识生成与表示对齐。该方法在脑、膀胱及肝癌少样本分类中显著优于基线，但其对 LLM 生成质量的依赖及缺乏通用 VLM 对比，限制了结论的普适性。

】

---

【Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers ｜域条件残差调制

研究机构：阿联酋扎耶德大学、英国布里斯托大学

作者：Ufaq Khan、Umair Nawaz、Massimo Caputo 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4b6c949cec00)

> 医学影像模型在适应超声等复杂模态时，常因全量微调而丧失自然图像通用能力，且测试时自适应（TTA）引入的推理期更新增加了部署验证难度。现有参数高效微调（PEFT）方法采用静态权重，难以应对医学与自然图像间连续且非分类的域差异。DCRM-ViT 通过冻结主干并注入由域路由器与参数合成器动态生成的样本级低秩残差，在训练时分离域元学习与任务适应，实现了无推理期更新的跨域适配。该方法在胎儿超声与多模态分割上优于静态 PEFT 基线，但其依赖有标签混合域数据，且未与医学专用域适应方法直接对比，限制了其在无标签临床场景的适用性评估。

】

---

【LATA: Laplacian-Assisted Transductive Adaptation for Conformal Uncertainty in Medical VLMs ｜拉普拉斯辅助迁移自适应

研究机构：丹麦奥胡斯大学、澳大利亚莫纳什大学

作者：Behzad Bozorgtabar、Dwarikanath Mahapatra、Sudipta Roy 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.17535)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.17535)

> 医学视觉-语言模型（VLM）在零样本识别中表现强劲，但面对域偏移时，其不确定性量化缺乏有限样本覆盖保证。现有保形预测方法要么依赖标签破坏交换性，要么预测集过大且类别覆盖失衡。本文提出LATA，一种无训练、无标签的迁移式精化方法，通过图像-图像kNN图上的拉普拉斯平滑优化零样本概率，并引入失败感知评分函数。该方法在保持保形有效性的同时显著缩小预测集，但仅验证于2D模态，3D体数据下的图构建成本与有效性尚未探明。

】

---

【Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization ｜半群正则化微分同胚配准

研究机构：加拿大阿尔伯塔大学

作者：Mohammadjavad Matinkia、Nilanjan Ray

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b30f9168fa8c)

> 可变形医学图像配准需在缺乏密集真值的情况下建立解剖结构对应，而传统方法依赖迭代优化或显式积分，计算耗时且易产生拓扑折叠。现有深度学习模型虽提升了速度，但往往通过缩放-平方积分或雅可比惩罚来维持可逆性，导致计算冗余与约束耦合。SGDIR 提出一种连续时间配准框架，仅通过单一半群正则化项内生保证微分同胚性，无需显式积分。该方法在严格约束下实现了近乎零折叠，但在无约束变形精度上略逊于基于基础模型的最新方法，其泛化能力边界尚待跨域验证。

】

---

【Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision ｜掩码引导自监督学习（MASS）：从弱监督到通用3D医学表征

研究机构：美国斯坦福大学

作者：Yunhe Gao、Yabin Zhang、Chong Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13660)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13660)

> 3D医学影像分析长期受困于高质量标注数据的稀缺与获取成本高昂，传统全监督模型虽在特定任务上表现优异，却难以应对临床场景中的分布偏移与泛化需求。现有自监督方法多依赖低层重建或对比目标，未能捕捉医学影像中关键的解剖语义与空间精度，导致下游任务迁移能力受限。本文提出MASS框架，利用自动生成的类无关掩码作为弱监督信号，通过上下文分割任务学习通用表征。该方法在少样本场景下显著优于基线，但在全监督高精度场景下未超越SOTA，其泛化边界与掩码噪声影响机制仍需进一步验证。

】

---

【Linguistic Priors for Visual Decoupling: Towards Symmetric Vision-Brain Alignment ｜语言先验引导的视觉解耦：迈向对称的视觉-脑对齐

作者：Dongjun Liu、Weichen Dai、Jingsheng Qian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_92b0c9173787)

> 脑视觉解码旨在从非侵入式脑电信号中还原感知到的视觉内容，其核心瓶颈在于低信噪比信号与高维语义空间间的结构性差异。现有主流方法直接对齐图像与脑信号，忽略了图像背景噪声与脑信号生理噪声造成的双向信息不对称，导致模型易建立虚假相关。本文提出语言先验引导的视觉解耦框架，利用文本描述作为语义桥梁，动态调整图像模糊程度以匹配脑信号的语义置信度，实现对称对齐。该方法在零样本检索任务中超越了现有基线，但其性能仍受限于跨被试泛化能力，且未解决生成式重建中的语义-像素冲突。

】

---

【MambaLiteUNet: Cross-Gated Adaptive Feature Fusion for Robust Skin Lesion Segmentation ｜MambaLiteUNet：基于交叉门控自适应特征融合的皮肤病变分割

研究机构：美国德州农工大学

作者：Md Maklachur Rahman、Soon Ki Jung、Tracy Hammond

论文原文见 [arXiv](https://arxiv.org/abs/2604.20286)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20286)

> 皮肤病变分割旨在从皮肤镜图像中精确勾勒病灶边界，以辅助早期癌症诊断与治疗方案规划。现有轻量化模型虽降低了计算开销，但常因缺乏多尺度特征交互与全局上下文建模能力，导致在低对比度或形态不规则区域边界描绘精度不足。本文提出MambaLiteUNet，通过引入自适应多分支Mamba特征融合、局部-全局特征混合及交叉门控注意力三个模块，在U-Net骨干中实现线性复杂度的长程依赖建模与精细化边界提取。该模型在保持极低参数量（0.494M）的同时，在四个主流基准上取得了领先的分割精度，但其性能优势是否完全源于架构改进而非数据预处理策略，仍需进一步验证。

】

---

【Masked-Diffusion Autoencoders for 3D Medical Vision Representation Learning ｜掩码-扩散自编码器（MDAE）：3D医学影像中结构与纹理的统一表征学习

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国华盛顿大学

作者：Jiachen Tu、Guanghui Qin、Theodore Zhengde Zhao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a4ebef8aa867)

> 导读 3D医学影像自监督学习长期面临全局解剖结构推理与局部组织纹理保持的权衡困境，现有掩码重建方法因高掩码率丢失细粒度特征，而对比学习难以捕捉非对象中心的连续解剖场。本文切入点在于将扩散去噪目标与空间掩码重建统一于单一判别式框架，通过双腐蚀机制迫使模型同时学习结构连贯性与纹理细节。具体做法是设计时间条件化的编码器-解码器网络，对输入体积同时施加块状掩码与高斯噪声，并分别计算掩码区域重建损失与可见区域去噪损失。该框架在跨模态泛化任务上展现出显著优势，但其依赖CNN骨干网络的设计选择是否限制了长距离依赖捕捉能力，仍需进一步验证。

】

---

【Med-CMR: A Fine-Grained Benchmark Integrating Visual Evidence and Clinical Logic for Medical Complex Multimodal Reasoning ｜医疗多模态复杂推理基准

研究机构：新加坡国立大学、南京大学

作者：Haozhen Gong、Xiaozhong Ji、Yuansen Liu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.00818)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00818)

> 医疗多模态大模型（MLLMs）正从演示走向临床，但现有基准多聚焦感知级问答，掩盖了模型在细微病灶识别、因果链构建及长尾病例泛化上的真实短板。Med-CMR 通过七维复杂度分解与双轨评估协议，填补了细粒度临床推理评估的空白。其核心贡献在于构建了覆盖11个器官系统与12种模态的20,653个VQA对，并验证了当前SOTA模型在长尾泛化上的显著瓶颈。该基准揭示了医疗专用模型未必优于通用模型的现状，但其依赖LLM自动评分的可靠性边界仍需警惕。

】

---

【MedCLIPSeg: Probabilistic Vision-Language Adaptation for Data-Efficient and Generalizable Medical Image Segmentation ｜概率化视觉-语言适配的医学图像分割

研究机构：加拿大康考迪亚大学

作者：Taha Koleilat、Hojat Asgariandehkordi、Omid Nejati Manzari 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20423)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20423)

> 医学图像分割长期受困于标注成本高、边界模糊及跨中心域偏移导致的模型过自信问题。现有基于CLIP的分割方法虽能利用文本先验降低标注依赖，但其确定性注意力机制在分布外（OOD）数据上仍表现出严重的置信度校准失效。本文切入点在于将跨模态注意力中的Key与Value建模为概率分布，通过变分推断显式捕捉随机性与认知不确定性。该框架在16个数据集上验证了其在数据效率与域泛化上的优势，但其概率建模带来的计算开销与3D体积数据的适用性仍存疑。

】

---

【MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA ｜频域记忆与图注意力驱动的轻量级医学视觉问答

研究机构：南京大学、韩国成均馆大学

作者：Haowen Gu、Gensheng Pei、Zeren Sun 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2bc5cc0fe416)

> 医学视觉问答（Med-VQA）旨在通过联合理解医学影像与自然语言问题生成诊断答案，其核心价值在于连接计算机视觉、自然语言处理与临床决策支持。现有大型视觉语言模型（VLM）虽具备强大的生成能力，但高昂的计算开销与参数量使其难以在资源受限的临床环境中部署，且通用编码器难以捕捉细微的病理结构。MedFG-VQA 通过引入离散余弦变换（DCT）频域记忆融合与图感知交叉注意力，在保持小模型规模的同时实现了细粒度视觉-文本对齐。该框架在多个基准上达到了与大型模型竞争的性能，但其在合成数据依赖性与跨模态泛化边界上的表现仍存疑。

】

---

【MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding ｜医学视频理解中的异构数据强化学习

研究机构：美国东北大学

作者：Yuhao Su、Anwesa Choudhuri、Zhongpai Gao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.06581)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.06581)

> 医学视频理解要求模型同时处理空间定位、时序推理与临床语义，但现有大视觉语言模型（VLM）在缺乏指令格式训练数据时性能急剧下降。主流方案要么依赖单数据集微调导致泛化受限，要么直接应用标准强化学习（RL）却因异构数据奖励尺度失衡而陷入训练崩溃。本文通过构建大规模多源基准 MedVidBench 并提出跨数据集奖励归一化机制 MedGRPO，解决了多源联合训练中的优化公平性问题。该工作确立了医学视频 RL 训练的可行性基线，但其评估完全依赖自建基准，缺乏外部泛化验证。

】

---

【Medic-AD: Towards Medical Vision-Language Model's Clinical Intelligence ｜临床导向的医学视觉语言模型：异常感知与时序推理的统一框架

研究机构：韩国首尔大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_944170a1003b)

> 医学视觉语言模型（Medical Vision-Language Model, Medical VLM）旨在将影像与文本对齐以支持临床决策，但现有通用模型缺乏对病灶定位、时序变化追踪及推理可解释性的原生支持，导致其输出难以直接用于高风险的临床工作流。MEDIC-AD 通过引入异常感知令牌（Anomaly Token）与差异令牌（Difference Token），构建了一个三阶段串行训练框架，将病灶检测、纵向症状推理与像素级热力图生成整合于单一模型中。该框架在时序症状追踪任务上显著超越了闭源大模型与专用医疗基础模型，验证了专用令牌机制在临床推理中的有效性，但其对骨干模型预训练质量的依赖及串行训练可能带来的特征遗忘风险，限制了其在极端分布偏移场景下的泛化上限。

】

---

【MEDIC-AD: Towards Medical Vision-Language Model's Clinical Intelligence ｜临床闭环驱动的医学视觉语言模型

研究机构：韩国首尔大学

作者：Woohyeon Park、Jaeik Kim、Sunghwan Steve Cho 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27176)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27176)

> 医学视觉语言模型（Medical Vision-Language Models, Medical VLMs）旨在通过大规模影像-报告配对数据学习通用表示，但现有模型多优化于宽泛知识覆盖，缺乏对真实临床工作流中病灶检测、纵向追踪与视觉解释的闭环支持。MEDIC-AD 通过三阶段串行训练，引入异常感知令牌与差异令牌，将检测、对比与解释嵌入模型学习课程。该设计在零样本异常检测与症状追踪任务上超越了闭源与医学专用基线，但其依赖骨干模型 Lingshu 的预训练质量，且未验证长序列时间推理的因果有效性。

】

---

【MedKCO: Medical Vision-Language Pretraining via Knowledge-Driven Cognitive Orchestration ｜医学视觉-语言预训练中的认知编排

研究机构：东南大学、南京大学

作者：Chenran Zhang、Ruiqi Wu、Tao Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09101)

> 医学视觉-语言预训练（Medical VLP）旨在利用影像-报告配对数据学习通用表示，但现有方法常通过随机打乱数据迫使模型同时学习简单与复杂概念，导致在分布偏移下特征表示次优。本文切入点在于引入认知科学中的“最近发展区”理论，通过知识驱动的认知编排（MedKCO）重构预训练过程。具体做法是设计基于诊断敏感度与类内样本代表性的层级课程，并引入自步非对称对比损失。该方法在多种医学模态上显著提升了零样本分类与检索性能，但其课程划分依赖人工与LLM协同，自动化程度与多模态扩展性仍存疑。

】

---

【MedLIME: A Distribution-Aligned and Evidence-Supported Framework for Medical Saliency Explanations ｜医学影像显著性解释的分布对齐与证据正则化框架

研究机构：美国卡内基梅隆大学

作者：Raghav Magazine、Xingjian Li、Min Xu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed0c2429f2e6)

> 医学影像黑盒模型的事后解释面临扰动样本偏离数据流形导致的定位失效问题。现有LIME变体虽尝试约束扰动，但缺乏对测试时分布偏移的自适应校准及历史病例证据的引入。本文提出MedLIME，通过生成式掩码、监督测试时自适应及基于Nadaraya-Watson核的证据正则化，在保持模型冻结的前提下提升显著性图的保真度。该方法在AUPRC指标上较基线有显著优势，但其仅解决空间定位稳定性，未触及临床语义解释的核心需求。

】

---

【MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images ｜医学多模态大语言模型

研究机构：阿联酋扎耶德大学

作者：Ankan Deria、Komal Kumar、Adinath Madhavrao Dukre 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.06965)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06965)

> 医学影像的精准解读要求模型不仅生成文本答案，还需在像素空间定位病理证据，但现有通用多模态大语言模型（MLLMs）在医疗场景下常因缺乏结构化空间监督而产生幻觉。本文指出当前医疗MLLMs依赖蒸馏数据且缺乏跨模态统一接地能力的局限，提出MedMO，通过四阶段渐进式后训练与边界框可验证强化学习（RL）实现视觉定位与临床推理的统一。其价值在于提供了开源的医疗基础模型基线，但其在细粒度病理对齐上的表现是否优于专用对齐方法仍存疑。

】

---

【MMCP-GEN: A Modality-Extensible Diffusion Language Model for Conditional Protein Sequence Generation ｜多模态条件蛋白序列生成

研究机构：香港理工大学

作者：Zeyu An、Wanyu Lin、Feng Tan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_877e4c9010b4)

> 可控蛋白生成需同时满足结构、功能与配体等多重生物约束，现有方法因模态隔离导致跨模态交互缺失且扩展新条件需重训骨干。MMCP-GEN 提出基于可学习查询与模态指示头的可组合条件融合机制，在不重训扩散骨干的前提下实现异构条件解耦与集成。该框架在序列恢复率上较基线提升最高 5%，但其对结构保真度的联合优化依赖外部评分器，且未与几何扩散模型进行直接对比，其物理可行性边界尚存疑。

】

---

【MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration ｜潜空间策略优化可变形配准

研究机构：中国科学院、中山大学

作者：Runxun Zhang、Yizhou Liu、Li Dongrui 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.17392)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17392)

> 可变形医学图像配准旨在通过估计密集非线性空间变换，将移动图像与固定图像在解剖结构上对齐，其核心价值在于支撑肿瘤监测、多模态融合及手术导航等临床决策。现有深度学习配准方法依赖单次前向推理，在处理大形变时易陷入局部最优，且受限于标注稀缺，难以充分利用少量标签。MorphSeek 将配准重构为潜空间策略优化问题，通过引入高斯策略头与组相对策略优化（Group Relative Policy Optimization, GRPO），在弱监督下实现多步细化。该方法在三个基准上提升了精度并降低了折叠率，但其对标签数量的依赖及与最新基础模型方法的对比缺失，限制了其通用性评估。

】

---

【MR-RAG: Multimodal Relevance-Aware Retrieval-Augmented Generation for Medical Visual Question Answering ｜多模态相关性感知检索增强生成

研究机构：华中科技大学、香港中文大学

作者：Xuze Li、Haozhao Wang、Zhenyu Huang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ace65c20276a)

> 医学视觉问答中，检索增强生成（RAG）常因检索噪声与生成时的注意力稀释导致事实错误。现有方法要么仅依赖单一模态相似度检索，要么将检索文档均匀拼接输入，无法区分证据质量。本文提出 MR-RAG，通过多模态协同检索（MCR）与重要性感知信息流增强（IFA）在推理阶段动态调制注意力。该方法在三个基准上显著优于传统 RAG 基线，但其性能仍低于强预训练模型，且依赖人工确定的关键层。

】

---

【Multimodal Protein Language Models for Enzyme Kinetic Parameters: From Substrate Recognition to Conformational Adaptation ｜酶动力学参数预测的分阶段条件建模

研究机构：合肥工业大学

作者：Fei Wang、Xinye Zheng、Kun Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.12845)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12845)

> 酶动力学参数预测旨在从分子输入直接估算酶催化效率，以替代高成本的湿实验筛选。现有方法多将催化过程简化为酶与底物的静态兼容性匹配，忽略了识别与构象适应的动态层级。本文提出ERBA框架，通过分子识别交叉注意力与几何感知混合专家模块，将预测重构为机制对齐的分阶段条件过程。该设计在多个蛋白质语言模型骨干上提升了预测精度，但其对3D结构依赖的鲁棒性边界尚待明确。

】

---

【OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning ｜医疗多模态推理的数据配方

研究机构：微软研究院

作者：Timothy Ossowski、Sheng Zhang、Qianchu Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.23269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.23269)

> 医疗大语言模型（Medical LLMs）在复杂临床场景中面临的核心挑战是跨模态推理的鲁棒性与泛化能力，现有方法多依赖架构创新或强化学习（RL）后训练，但忽视了监督微调（SFT）阶段数据配方的决定性作用。本文切入点在于证明，通过结构化设计推理轨迹的长度多样性与模态覆盖度，仅凭SFT即可实现任务感知的推理深度自适应，无需显式监督。具体做法是构建包含800万例、68亿响应token的最大医疗多模态推理数据集，采用拒绝采样确保轨迹质量，并验证了多轨迹蒸馏优于单纯增加训练轮次。该工作确立了数据工程在医疗推理中的核心地位，但其“任务感知”机制是否具备因果一致性，还是仅表现为长度相关，尚存疑。

】

---

【OmniFM: Toward Modality-Robust and Task-Agnostic Federated Learning for Heterogeneous Medical Imaging ｜频谱对齐联邦学习

作者：Meilin Liu、Jiaying Wang、Jing Shan

论文原文见 [arXiv](https://arxiv.org/abs/2603.21660)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21660)

> 联邦医学影像学习长期受困于跨机构成像模态差异导致的优化发散，现有框架往往绑定特定任务与骨干网络，难以复用。OmniFM 切入这一盲区，利用低频谱的跨模态一致性作为不变先验，构建任务无关的统一优化管道。其核心是通过全局频谱检索与近端对齐抑制局部漂移，在异构模态下实现了多任务性能提升，但缺乏在主流标准基准上的横向验证，其普适性仍存疑。

】

---

【OmniFood8K: Single-Image Nutrition Estimation via Hierarchical Frequency-Aligned Fusion ｜单目深度校正与频域融合的单图营养估算

研究机构：中国科学院、中国科学院大学

作者：Dongjian Yu、Weiqing Min、Qian Jiang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12356)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12356)

> 食品营养估算旨在从非结构化视觉数据中量化热量与宏量营养素，以支持慢性病预防与个性化饮食管理。现有高精度方法多依赖深度传感器获取三维几何信息，但真实场景中用户仅能使用普通RGB相机拍摄，导致算法落地受限；同时，主流数据集严重偏向西方饮食，缺乏对中式复杂烹饪场景的覆盖。本文通过构建涵盖中式菜肴全流程的OmniFood8K数据集，并提出基于单目深度估计校正与频域对齐融合的端到端框架，试图在不依赖深度硬件的前提下实现高精度营养预测。该方案在数值精度上优于传统RGB-D基线，但其对单目深度估计误差的依赖及缺乏语义推理能力，限制了其在复杂临床决策场景中的直接应用。

】

---

【OralGPT-Omni: A Versatile Dental Multimodal Large Language Model ｜牙科多模态大语言模型

研究机构：德国卡尔斯鲁厄理工学院、深圳大学

作者：Jing Hao、Yuci Liang、Lizhuo Lin 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.22055)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.22055)

> 牙科影像分析面临通用大模型缺乏解剖先验导致幻觉频发，且现有专用模型仅覆盖单一模态的困境。OralGPT-Omni 通过构建模拟临床诊断逻辑的 TRACE-CoT 推理数据与四阶段训练策略，实现了跨八种牙科模态的统一分析。该模型在 MMOral-Uni 基准上以 51.84 分大幅超越 GPT-5，但其依赖 LLM 作为评判者的评估协议及治疗规划任务的短板，限制了其临床落地的可信度边界。

】

---

【OraPO: Oracle-educated Reinforcement Learning for Data-efficient and Factual Radiology Report Generation ｜基于Oracle教育的强化学习放射学报告生成

研究机构：澳大利亚昆士兰大学

作者：Zhuoxiao Chen、Hongyang Yu、Ying Xu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18600)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18600)

> 放射学报告生成（RRG）的核心矛盾在于模型常生成与图像证据不符的幻觉文本，且现有方法依赖海量数据与算力。主流监督微调（SFT）范式在数据稀缺时泛化能力骤降，而标准强化学习（RL）在医学长文本任务中常因奖励信号稀疏而失效。本文提出OraPO，通过动态注入Oracle监督将失败探索转化为偏好信号，结合事实级奖励实现数据高效训练。该方法在极小数据量下刷新了SOTA，但其对罕见病泛化能力及3D数据适用性仍存疑。

】

---

【OSA: Echocardiography Video Segmentation via Orthogonalized State Update and Anatomical Prior-aware Feature Enhancement ｜正交化状态更新与解剖先验特征增强

研究机构：深圳大学、香港理工大学

作者：Rui Wang、Huisi Wu、Jing Qin

论文原文见 [arXiv](https://arxiv.org/abs/2603.26188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26188)

> 超声心动图视频分割需在严重斑点噪声与稀疏标注下维持左心室轮廓的时序一致性，以支撑射血分数等临床指标的准确计算。现有线性递归模型虽具备线性计算复杂度，但其无约束欧氏状态更新导致状态矩阵发生秩坍缩，长序列中解剖细节被噪声淹没。本文提出OSA框架，通过Stiefel流形约束的正交化状态更新与物理驱动的解剖先验特征解耦，在保持实时推理效率的同时实现SOTA分割精度。该方案在时序稳定性上表现优异，但其正交化约束对复杂非正交解剖结构的表达能力边界尚存疑。

】

---

【Personalized Longitudinal Medical Report Generation via Temporally-Aware Federated Adaptation ｜联邦时间自适应（FTA）下的纵向医疗报告生成

研究机构：日本北海道大学

作者：He Zhu、Ren Togo、Takahiro Ogawa 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19668)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19668)

> 联邦学习（Federated Learning, FL）旨在解决多机构数据孤岛与隐私合规冲突，但现有方法普遍假设客户端数据分布静态不变，无法捕捉疾病随时间演进的动态特征。本文指出，忽略时间维度的“一刀切”聚合会抹平关键的病程信号，导致模型在纵向数据上泛化失效。为此，作者提出联邦时间自适应（Federated Temporal Adaptation, FTA）设定及FedTAR框架，通过人口统计学条件化的LoRA适配与元学习的时间残差聚合，实现隐私保护下的时序感知建模。该工作填补了联邦学习中时间非平稳性的建模空白，但其依赖固定访问次数的假设及私有数据集的不可复现性，限制了结论的普适性验证。

】

---

【PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting ｜基于掩码感知的PET/CT病灶级报告生成

作者：Danyal Maqbool、Changhee Lee、Zachary Huemann 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.27680)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.27680)

> 放射学报告生成旨在从医学图像自动产生结构化临床文本，以缓解影像检查量激增与放射科医生短缺之间的结构性矛盾。现有3D视觉-语言模型（VLM）在处理PET/CT数据时，因依赖全局下采样编码，导致体积占比不足0.1%的微小病灶特征丢失，无法生成符合临床要求的细粒度病灶描述。本文通过构建首个大规模PET/CT病灶级对齐数据集PETARSeg-11K，并提出掩码感知VLM架构PETAR-4B，利用3D焦点提示与掩码条件化编码实现病灶级空间接地。该工作填补了PET域细粒度报告生成的数据与模型空白，但其性能高度依赖外部分割掩码输入，限制了全自动部署的可行性。

】

---

【PGR-Net: Prior-Guided ROI Reasoning Network for Brain Tumor MRI Segmentation ｜先验引导的ROI推理网络

作者：Jiacheng Lu、Hui Ding、Shiyu Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.21626)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21626)

> 脑肿瘤MRI分割面临病灶空间稀疏与背景计算冗余的矛盾，现有模型假设病灶均匀分布，导致大量算力浪费在非病变区域。PGR-Net通过构建数据驱动的空间先验模板，引入层级ROI决策机制，将计算资源聚焦于高置信病灶区域。该方法在BraTS 2023上以8.64M参数量实现了91.82%的WT Dice系数，验证了显式先验注入在效率-精度权衡上的优势，但其2D切片处理与训练集依赖的先验构建限制了跨域泛化能力的评估。

】

---

【Photo-Guided Tooth Segmentation on 3D Oral Scan Model ｜照片引导的三维口腔扫描牙齿分割

研究机构：山东大学

作者：Shaojie Zhuang、Guangshun Wei、Jiangxin He 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6f9cd9da2f1a)

> 三维口腔内扫描（IOS）模型常因纹理缺失导致邻牙及牙龈边界模糊，现有纯几何方法难以区分紧密接触区域。本文切入点在于利用易获取的二维口内照片作为外部语义引导，通过相机配准与特征融合补偿几何信息不足。PMTSeg框架通过显式对齐与自适应门控将照片纹理注入三维分割骨干，显著提升了边界精度。该方法在自建数据集上验证了纹理对分割的增益，但缺乏跨机构标准化基准的对比，其泛化能力存疑。

】

---

【Phrase-grounded APO for Improving Chest X-ray Report Generation ｜短语接地自动偏好优化

研究机构：美国伦斯勒理工学院、美国斯坦福大学

作者：Raziuddin Mahmood、Tanveer Syeda-Mahmood

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_69afd350a8e3)

> 放射学报告生成（RRG）模型在临床部署中面临的核心困境是幻觉与事实错误，而现有的直接偏好优化（DPO）等对齐方法依赖人工标注的偏好对，这在缺乏Ground Truth的临床推理场景中不可行。本文切入点在于利用事实核查（Fact-Checking, FC）模型自动从模型自身输出中生成代理偏好数据，实现推理时的轻量级参数更新。具体做法是构建包含短语接地损失的APO损失函数，在推理阶段对冻结的RRG模型进行微调。该方法在多个SOTA生成器上平均提升了30-40%的报告质量，但其性能上限受限于FC模型本身的检测准确率，且未验证在更复杂三维数据上的泛化能力。

】

---

【Prospective Dynamic 3D MRI Reconstruction via Latent-Space Motion Tracking from Single Measurement ｜前瞻性动态3D MRI重建：基于潜空间运动追踪的单次测量恢复

研究机构：美国密歇根大学、丰田研究所

作者：Lixuan Chen、Zhongnan Liu、Jesse Hamilton 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.04249)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.04249)

> 前瞻性重建旨在从当前延迟窗口内的单次超稀疏k空间测量中即时恢复3D图像，以支持MRI引导放疗等实时临床决策。现有回顾性方法依赖多帧聚合，无法满足即时性要求，而线性基或离散先验的前瞻性方法在非线性运动下精度不足。PDMR通过离线学习患者特异性非线性运动流形，在线仅优化低维潜向量实现快速适配。该方法在腹部MRI上显著优于现有前瞻性基线，但其对预扫描模板的依赖及流形泛化边界仍存疑。

】

---

【Reading Your Actions: Learning Generalizable Action Representations via Pre-training AEMG ｜神经收缩分词器与掩码重建：EMG通用表示学习框架

研究机构：华南理工大学

作者：Zhenghao Huang、Huilin Yao、Kaikai Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f08949baee17)

> 表面肌电（sEMG）解码长期受限于数据异构性与标注稀缺，导致模型难以跨被试、跨设备泛化。现有方法或依赖特定任务格式，或采用固定滑动窗口，无法捕捉肌肉协同的生理语义。本文提出AEMG，通过神经收缩分词器将连续信号离散为“生理语言”，并基于向量量化与掩码重建进行大规模自监督预训练。该框架在零样本留一法交叉验证中较基线提升5.79–9.25%，但离散化过程对连续运动解码精度的潜在影响尚未得到充分验证。

】

---

【Rethinking Box Supervision: Bias-Free Weakly Supervised Medical Segmentation ｜弱监督医学图像分割中的框偏差消除

研究机构：深圳大学

作者：Jun Wei、Hui Huang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0b539a418f72)

> 医学图像分割长期受限于像素级标注的高成本与主观噪声，而边界框标注虽廉价却缺乏形状信息，直接监督易导致预测偏向矩形结构。现有弱监督方法未能有效解耦定位与形状学习，导致泛化能力受限。本文提出WeakMed框架，通过可微分的掩码到框变换与尺度一致性损失，在仅使用边界框监督下恢复细粒度分割能力。该框架在多模态任务上表现稳健，但其对极细结构及大占比目标的适应性仍存疑。

】

---

【Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification ｜通用2D基础模型适配3D医学影像分类

作者：Han Liu、Bogdan Georgescu、Yanbo Zhang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12887)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12887)

> 3D医学影像分类面临数据稀缺与临床部署效率的双重约束，传统从零训练的3D模型难以快速扩展至新任务。现有研究在评估数据量、适配策略和任务覆盖度上存在系统性偏差，导致基础模型（Foundation Models, FMs）的潜力被低估。本文提出AnyMC3D，通过低秩适配（Low-Rank Adaptation, LoRA）微调冻结的2D骨干网络，结合置换不变的查询注意力池化，实现单框架跨任务扩展。该方法在12项任务上验证了通用视觉特征的有效性，但其在单任务极致精度上仍逊于专用优化模型，且对预训练分布的依赖边界尚不明确。

】

---

【SAR2Net: Learning Spatially Anchored Representations for Retrieval-Guided Cross-Stain Alignment ｜空间锚点表示学习驱动的跨染色配准

研究机构：上海交通大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c8ccc54dc3c)

> 跨染色全切片图像（WSI）配准旨在建立H&E与IHC切片间的空间对应，以整合形态学与分子信息。现有方法依赖全局粗对齐先验，在活检切片常见的组织碎片化与非线性变形下往往失效。本文提出SAR2Net，通过对比学习在模拟坐标上训练空间锚点表示，将配准重构为区域级特征检索问题，无需预对齐即可建立对应。该方法在自建活检数据集上显著优于传统配准框架，但其区域级精度是否足以支撑下游像素级分割任务尚存疑。

】

---

【SATTC: Structure-Aware Label-Free Test-Time Calibration for Cross-Subject EEG-to-Image Retrieval ｜结构感知测试时校准

作者：Qunjie Huang、Weina Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2603.20738)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20738)

> 跨被试脑电到图像检索面临个体分布偏移与嵌入空间“枢纽效应”的双重干扰，导致Top-k候选列表不稳定。现有方法多聚焦于编码器训练阶段的域适应，却忽视了冻结编码器下测试时相似度矩阵的几何畸变。本文提出SATTC，一种无标签测试时校准头，通过自适应CSLS与结构专家融合重排序。该方法在严格LOSO协议下提升了检索稳定性，但其增益依赖于特定骨干网络，且未验证在更复杂生成式任务中的有效性。

】

---

【Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers ｜几何感知与跨模态对齐的3D CT基础模型

研究机构：荷兰埃因霍温理工大学

作者：Cris Claessens、Christiaan Viviers、Giacomo D'Amicantonio 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.17209)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.17209)

> 3D CT影像分析面临体素各向异性导致的几何失真与临床报告噪声引发的语义对齐失效，现有单一自监督或视觉语言模型难以兼顾空间精度与临床语义。SPECTRE通过引入各向异性3D Patch与RoPE抖动显式编码几何信息，并采用DINOv3自蒸馏与SigLIP对齐的两阶段预训练策略，解决了标准Transformer在体积数据上的计算瓶颈与语义缺失问题。该模型在检索与分割任务上展现了优于现有CT基础模型的泛化能力，但其胸腹部数据分布不均与报告噪声敏感性仍制约着其在复杂临床场景中的鲁棒性。

】

---

【SD-FSMIS: Adapting Stable Diffusion for Few-Shot Medical Image Segmentation ｜基于扩散先验的少样本医学影像分割

研究机构：深圳大学

作者：Meihua Li、Yang Zhang、Weizhao He 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.03134)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.03134)

> 少样本医学影像分割（FSMIS）旨在解决标注稀缺与域偏移双重约束下的新类别泛化难题。传统原型匹配网络因缺乏强视觉先验，在跨域场景下性能显著衰退。本文切入点在于将预训练文本到图像扩散模型（Stable Diffusion）的通用视觉先验直接适配至密集预测任务，通过支持集-查询集交互与视觉-文本条件翻译实现少样本分割。该范式验证了生成式模型在医学分割中的迁移潜力，但其对扩散模型版本敏感性及单步推理的稳定性仍存疑。

】

---

【SegMoTE: Token-Level Mixture of Experts for Medical Image Segmentation ｜基于Token级混合专家机制的医学图像分割

研究机构：四川大学、阿里巴巴达摩院

作者：Yujie Lu、Jingwen Li、Sibo Ju 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19213)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19213)

> 医学图像分割面临模态异构与标注成本的双重约束，现有基础模型适配方法依赖大规模数据微调导致分布偏移与表征同质化。SegMoTE通过冻结SAM编码器并引入Token级混合专家（MoTE）机制，以极小参数代价实现模态特异性适配。该方法在0.15M数据上训练17M参数，在域外数据集上超越基线1%-6%。其核心价值在于验证了“结构创新替代数据规模”的可行性，但缺乏对极端少样本场景的验证。

】

---

【Semi-supervised Echocardiography Video Segmentation via Anchor Semantic Awareness and Continuous Pseudo-label Reforging ｜锚点语义感知与连续伪标签重铸的半监督超声视频分割

研究机构：深圳大学、香港理工大学

作者：Yunpeng Fang、Yimu Sun、Jingxing Guo 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cdcb16a2c220)

> 超声心动图视频分割面临斑点噪声干扰、心脏结构动态形变及标注数据稀缺三重挑战，现有方法在抑制噪声与保持时序一致性之间难以兼顾。本文提出EchoForge，通过锚点机制校准不确定区域特征，并迭代重铸高质量伪标签，以解决半监督场景下的噪声累积问题。该方法在CAMUS和EchoNet-Dynamic基准上实现了精度与实时性的平衡，但其对极端低对比度图像的鲁棒性仍受限于特征提取能力，且未显式处理跨中心域偏移。

】

---

【SemiGDA: Generative Dual-distribution Alignment for Semi-Supervised Medical Image Segmentation ｜生成式双分布对齐半监督医学图像分割

研究机构：南京大学、东南大学

作者：Kaiwen Huang、Yi Zhou、Yizhe Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23274)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23274)

> 半监督医学图像分割旨在利用少量标注与海量无标注数据缓解临床标注成本瓶颈，其核心价值在于平衡数据稀缺与模型泛化需求。现有主流方法依赖判别式像素级分类或一致性正则化，在标注极度稀缺时易陷入过拟合且难以捕捉全局语义结构。本文提出SemiGDA，通过冻结的Stable Diffusion VAE潜空间对齐图像与掩码的先验分布，实现生成式分割。该方法在四个基准上优于传统判别式方法，但在BUSI数据集上显著低于当前SOTA，其通用图像先验能否替代医学专用解剖先验仍存疑。

】

---

【SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation ｜结构感知层级无监督域适应与合理性评估

研究机构：西北工业大学、哈尔滨工业大学

作者：Linkuan Zhou、Yinghao Xia、Yufei Shen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.21904)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21904)

> 医学影像跨模态部署面临的核心挑战是源域与目标域间的分布偏移，导致分割模型性能骤降。现有无监督域适应方法多依赖全局特征对齐或像素级伪标签筛选，前者忽略解剖结构的语义差异，后者无法识别全局解剖结构的不合理性。SHAPE 通过层级特征调制实现类感知的细粒度对齐，并引入超图结构验证机制从全局解剖合理性角度筛选伪标签。该框架在心脏与腹部跨模态基准上取得了显著的性能提升，但其超图构建对解剖先验的依赖及计算开销在复杂临床场景中的泛化能力仍存疑。

】

---

【Similarity-as-Evidence: Calibrating Overconfident VLMs for Interpretable and Label-Efficient Medical Active Learning ｜相似性即证据：校准过度自信的视觉语言模型以支持可解释医学主动学习

研究机构：厦门大学、美国凯斯西储大学

作者：Zhuofan Xie、Zishan Lin、Jinliang Lin 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.18867)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18867)

> 医学影像标注成本高昂，主动学习（Active Learning, AL）旨在通过迭代选择最具信息量的样本以最大化标注预算效率，但传统方法在冷启动阶段因模型预测不可靠而失效。视觉语言模型（Vision-Language Models, VLMs）虽能通过零样本预测缓解冷启动，但其基于温度缩放Softmax的输出机制将几何相似度误判为确定性概率，导致模型对错误预测过度自信，进而误导样本选择。SaE框架通过引入相似性证据头（Similarity Evidence Head, SEH），将原始文本-图像相似度映射为狄利克雷分布参数，利用主观逻辑（Subjective Logic, SL）分解不确定性为空缺（Vacuity）与失谐（Dissonance），实现基于临床语义的可解释样本获取。该框架在10个医学数据集上实现了82.57%的宏平均准确率，显著优于现有基线，但其依赖全局相似度向量的设计在细粒度解剖对齐场景下的适用性尚存疑问。

】

---

【Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation ｜草图-文本引导的3D医学体积生成

研究机构：美国圣母大学

作者：Delin An、Chaoli Wang

论文原文见 [arXiv](https://arxiv.org/abs/2603.22509)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22509)

> 3D医学影像合成旨在解决标注数据稀缺导致的下游任务泛化瓶颈，但现有方法要么缺乏切片间解剖连续性，要么依赖预定义掩码导致可控性不足。Sketch2CT 通过引入低成本手绘草图与文本描述作为多模态条件，先生成3D分割掩码再合成CT体积，实现了结构可控的3D生成。该框架在CHAOS肝脏数据集上取得33.7 FID，优于MedGen3D的43.6，但其评估未涵盖临床剂量指标，且骨干网络仍采用U-Net，与当前Transformer主导的趋势存在偏差。

】

---

【Sparse Spectral LoRA: Routed Experts for Medical VLMs ｜稀疏谱洛拉：面向医学视觉语言模型的路由专家机制

研究机构：加拿大康考迪亚大学

作者：Omid Nejati Manzari、Hojat Asgariandehkordi、Taha Koleilat 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.01310)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.01310)

> 医学视觉语言模型（VLM）在异构数据微调中面临跨数据集干扰与灾难性遗忘，导致单一模型难以兼顾多种临床任务。现有参数高效微调（PEFT）方法如标准LoRA缺乏对预训练权重内部结构的利用，无法隔离不同数据源的语义冲突。本文提出MedQwen，通过SVD分段初始化LoRA专家并引入理论缩放因子，实现低秩更新与全量微调梯度几何的对齐。该方法在23个医学数据集上验证了性能优势，但其对强骨干网络的依赖及缺乏解剖感知路由的局限，限制了其在资源受限场景下的泛化潜力。

】

---

【SPEGC: Continual Test-Time Adaptation via Semantic-Prompt-Enhanced Graph Clustering for Medical Image Segmentation ｜SPEGC：基于语义提示增强图聚类的持续测试时自适应

作者：Xiaogang Du、Jiawei Zhang、Tongfei Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.11492)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11492)

> 医学影像模型在跨中心部署时，因成像设备与协议差异导致性能显著下降，而临床数据以无标签、单样本流式到达，传统离线域适应无法适用。现有测试时自适应方法多依赖熵最小化或批归一化统计更新，在动态漂移下易陷入误差累积与灾难性遗忘的恶性循环。SPEGC 通过解耦语义提示增强局部特征，并利用最优传输求解可微分图聚类，将适应信号从像素级置信度提升至簇级结构一致性。该方法在眼底与息肉分割基准上实现了单源设置下的最优性能，但其图构建带来的计算开销是否满足实时临床流处理需求，仍需进一步验证。

】

---

【TAMER: A Tri-Modal Contrastive Alignment and Multi-Scale Embedding Refinement Framework for Zero-Shot ECG Diagnosis ｜三模态对比对齐与多尺度嵌入精炼框架

作者：Xuewei Zhou、Yajie Meng、Pan Zeng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f7c3caf8409)

> 现有ECG自监督方法受限于单模态表征能力不足，而多模态框架又因语义对齐粗粒度导致跨域泛化受限。TAMER通过引入频谱图作为视觉模态，构建时频域内部一致性约束与报告引导的波级细粒度对齐，将ECG分析重构为视觉-语言表征学习范式。该框架在零样本分类与跨域迁移任务中显著优于单模态及早期多模态基线，但其性能增益是否源于频谱模态的冗余信息补充，抑或细粒度对齐机制的本质突破，仍需更严格的消融验证。

】

---

【TANGO: Learning Distribution-wise Foundation Prior Consistency and Instance-wise Style Calibration for Medical Image Generalization ｜基于基础模型先验蒸馏与实例级风格校准的持续测试时自适应

研究机构：北京航空航天大学、中南大学

作者：Chuang Liu、Yichao Cao、Xiu Su 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_53f30587e07d)

> 医学影像分割模型在跨中心部署时，因成像设备与协议差异导致性能显著下降，而现有测试时自适应方法常因源模型过拟合及动态环境下的误差累积而失效。TanGo 指出，传统方法忽视了源模型自身的泛化能力缺陷，且缺乏对测试样本风格分布的实例级动态校准。该框架通过训练阶段从视觉基础模型蒸馏低频先验以增强源模型鲁棒性，并在测试阶段利用可学习装饰器与源知识锚定重校准策略实现稳定适应。这一设计在 BraTS 2018 等基准上取得了 0.79 的 DSC，虽略低于部分最新 SOTA，但在持续适应场景下展现了更强的稳定性，其核心假设——低频先验足以代表域不变性——在极端域偏移下的有效性仍存疑。

】

---

【Temporal Inversion for Learning Interval Change in Chest X-Rays ｜时序反转感知学习

研究机构：韩国首尔大学

作者：Hanbin Ko、Kyungmin Jeon、Doowoong Choi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.04563)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04563)

> 医学视觉-语言预训练（Medical VLP）旨在利用影像-报告配对数据学习通用表示，但现有模型多孤立分析单张胸片，忽略了放射科医生通过对比前后影像评估病情进展的核心临床任务。主流时序模型虽引入双图编码器，却缺乏对病理变化方向性的显式建模，导致模型可能仅依赖实体存在而非真实时序逻辑进行预测。本文提出 TILA 框架，将时间反转作为贯穿预训练、微调与推理的监督信号，强制模型捕捉方向敏感的特征。该框架在多个架构上提升了时序一致性，但其有效性高度依赖病理变化的近似可逆性，对不可逆病变的适用性存疑。

】

---

【TIM: Temporal Decoupling with Iterative Mutual-Refinement Model for Longitudinal Radiology Report Generation ｜纵向放射学报告生成中的时间解耦与双向互检

研究机构：华中科技大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f04782f4fe88)

> 导读 纵向放射学报告生成（Longitudinal Radiology Report Generation, LRRG）旨在从同一患者多次检查的图像序列中生成包含疾病进展描述的诊断文本，以弥补单时间点模型无法捕捉病情动态演变的缺陷。现有方法将不同时间点的图像特征混合在单一表示空间中，导致静态病理特征与时序变化特征相互纠缠，进而引发时序推理不一致与错误跨期传播。本文提出TIM框架，通过解耦静态病理识别与动态进展建模，并引入基于前次报告错误反馈的双向互检机制，在Longitudinal-MIMIC数据集上实现了语言与临床指标的双重提升。该框架在2D胸片纵向任务上有效，但其对3D体积数据的适用性及推理延迟对临床部署的影响尚存疑。

】

---

【TopoCL: Topological Contrastive Learning for Medical Imaging ｜拓扑对比学习（TopoCL）：基于持久同调的医学影像自监督表征增强

研究机构：美国圣母大学

作者：Guangyu Meng、Pengfei Gu、Peixian Liang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14647)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14647)

> 导读 医学影像标注成本高昂且存在观察者间差异，导致监督学习泛化受限，而主流对比学习（Contrastive Learning, CL）仅关注局部像素纹理，忽视了连通性、孔洞等具有临床诊断意义的全局拓扑结构。现有方法在增强策略上缺乏对拓扑扰动的量化控制，且视觉与拓扑特征的融合机制僵化，难以适应不同解剖区域的异质性。本文提出 TopoCL 框架，通过相对瓶颈距离量化拓扑扰动以设计感知增强，并利用层级编码器与自适应混合专家（Mixture-of-Experts, MoE）模块融合视觉与拓扑表征。该框架在五个基准上平均提升准确率 3.26%，验证了拓扑信号在低标签场景下的互补价值，但其两阶段预训练策略是否限制了特征空间的深层对齐仍存疑。

】

---

【Translating Signals to Languages for sEMG-Based Activity Recognition ｜将sEMG信号转化为类语言表示以驱动大语言模型活动识别

研究机构：英国兰卡斯特大学、澳大利亚莫纳什大学

作者：Ming Wang、Haoxuan Qu、Qiuhong Ke 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22403)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22403)

> sEMG活动识别的核心瓶颈在于连续生理信号与大语言模型（LLM）离散文本输入格式间的表征鸿沟，直接微调LLM易导致预训练语义先验的灾难性遗忘。本文切入点在于不修改LLM权重，而是通过“语言涌现”机制将sEMG转化为具备人类语言统计特性的“sEMG语言”。具体做法是结合VQ-VAE离散化、Lewis Signaling Game迭代学习与人类语言偏置正则化，构建信号到语言的映射。该方法在GRABMyo数据集上取得95.14%准确率，但缺乏跨被试泛化评估，其语义推理能力的实际贡献仍存疑。

】

---

【Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding ｜超声视觉语言预训练中的语义歧义与结构化推理

研究机构：香港浸会大学、浙江大学

作者：Jiayun Jin、Haolong Chai、Xueying Huang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.01749)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.01749)

> 超声图像因操作者依赖与声学伪影导致外观高度异质，通用视觉语言模型难以直接对齐其复杂的诊断语义。现有医学CLIP模型在超声模态下表现不佳，主要受限于报告文本的语义模糊性及缺乏领域特定的结构先验。本文通过构建大规模专用数据集US-365K，并设计基于诊断属性框架的异构图编码器与语义软标签机制，实现了超声图像与文本的细粒度对齐。该工作填补了超声专用视觉语言基准的空白，但其下游分割性能未与专用网络直接对比，泛化能力的边界尚存疑。

】

---

【Uni-Encoder Meets Multi-Encoders: Representation Before Fusion for Brain Tumor Segmentation with Missing Modalities ｜统一编码器与多编码器融合：缺失模态脑肿瘤分割的两阶段异构架构

研究机构：山东大学、日本东京大学

作者：Peibo Song、Xiaotian Xue、Jinshuo Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22177)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.22177)

> 多模态MRI脑肿瘤分割在临床中常面临模态缺失，导致现有模型性能大幅退化。主流方法要么通过生成补全丢失细节，要么依赖局部卷积无法捕捉全局跨模态语义。UniME通过解耦表示学习与分割任务，先以掩码自监督预训练ViT建立鲁棒统一表示，再引入并行CNN提取细粒度特征进行融合。该设计在BraTS 2023/2024缺失模态场景下取得了领先性能，但其对大规模预训练数据的依赖及异构架构的计算开销是否适配低资源临床环境，仍需进一步验证。

】

---

【URICA: A Uniformity Region Affine Identifier Capture Algorithm for Arbitrary Region Retrieval in Pathology Images ｜统一区域仿射标识捕获算法

作者：Ri Su、Zhao Chen、Caleb Chen Cao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d1e181a7ab24)

> 全切片图像（WSI）区域检索旨在从海量病理切片中定位与查询区域在语义和结构上相似的任意区域，但现有方法受限于固定尺寸Patch或Slide级聚合，无法处理临床场景中常见的旋转与缩放变化。本文切入点在于构建一种在任意空间变换下保持语义一致性的区域级表示。通过引入“语义镶嵌”将基础模型Patch特征组合为几何感知描述符，并设计“仿射标识符”实现旋转与缩放不变的匹配，URICA在TCGA数据集上实现了SOTA性能。其价值在于填补了Patch级与Slide级之间的表示空白，但理论近似边界在实际密集重叠组织中的稳定性尚待验证。

】

---

【Virtual Immunohistochemistry Staining with Dual-Aligned Multi-Task Feature Guidance ｜双对齐多任务特征引导的虚拟免疫组化染色

研究机构：大连理工大学

作者：Shigeng Xie、Hongming Xu、Guiyang Jiang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_38a630b41df0)

> 虚拟免疫组化染色（Virtual IHC Staining, VIS）旨在从常规H&E图像生成分子特异性IHC图像，以规避昂贵试剂与耗时流程。现有方法依赖单一辅助任务或全局最优传输（OT）损失缓解空间错位，但前者语义覆盖不足，后者在阳性区域因外观剧变导致成本函数失效。本文提出双对齐框架，通过结构增强学习与主动-被动匹配解决空间错位，并引入任务间隙对齐模型桥接辅助任务与生成特征间的语义鸿沟。该框架在GAN范式内显著优于现有基线，但未对比扩散模型，其临床泛化能力存疑。

】

---

【Virtual Nodes Guided Dynamic Graph Neural Network for Brain Tumor Segmentation with Missing Modalities ｜虚拟节点引导动态图神经网络

研究机构：北京科技大学

作者：Sha Tao、Jiao Pan、Yu Guo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.16880)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.16880)

> 多模态脑肿瘤分割在临床中常遭遇序列缺失，导致依赖固定计算路径的卷积或Transformer模型性能崩溃。现有统一模型多采用两阶段训练或生成式补全，训练成本高且易引入噪声。本文提出基于图神经网络的单阶段框架，将模态视为节点，通过动态边连接与虚拟节点机制处理任意缺失组合。该方法在BraTS 2018上优于基线，但在BraTS 2020上低于最新SOTA，其图结构在极端缺失下的边界精度优势尚需更多临床场景验证。

】

---

【X-WIN: Building Chest Radiograph World Model via Predictive Sensing ｜胸部X光世界模型：基于预测性感知的3D知识蒸馏

研究机构：美国伦斯勒理工学院

作者：Zefan Yang、Ge Wang、James Hendler 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.14918)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.14918)

> 胸部X光（CXR）作为二维投影图像，因结构重叠无法捕捉三维解剖细节，限制了疾病诊断的准确性。现有CXR基础模型仅学习二维局部特征，缺乏对三维空间结构的内化，导致在复杂病理场景下表示能力不足。X-WIN通过构建动作条件世界模型，从CT体积中蒸馏三维空间知识至CXR表示空间，实现了跨模态的空间认知迁移。该方法在标准基准上以线性探测协议超越了现有基础模型，但其模拟域与真实域的分布差异仍制约着临床泛化能力。

】
