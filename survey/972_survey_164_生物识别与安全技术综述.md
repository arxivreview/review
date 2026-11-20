# A Survey of Biometric Recognition and Security Technologies ｜生物识别与安全技术综述 ｜arxivreview

综述原文见 [ArxivReview](https://www.arxivreview.com/surveys/Biometric%20Recognition%20and%20Security)

## 导读

生物识别与安全技术旨在利用生理或行为特征替代传统密码，实现唯一身份验证，其核心价值在于解决数据标注成本高企与泛化需求之间的张力。早期研究依赖手工特征提取，思路简洁却受制于噪声与姿态变化下的泛化能力不足。当深度学习全面取代手工特征后，研究重心从单一模态识别转向多模态融合、无接触采集以及对抗攻击防御。生成式模型与3D重建技术的引入，用更高的计算成本换取了数据稀缺缓解与跨姿态鲁棒性。各路线在识别精度、安全防御与隐私保护之间做出了不同取舍，由此形成当前“安全与效率并重”的方法格局。本综述梳理这条从特征匹配到系统韧性的因果演进链条，为读者提供一张领域认知地图。全文按问题演化与路线取舍组织，覆盖该领域从奠基到当前的主要工作。

## 1. 研究背景、问题结构与演进脉络

生物识别技术的起源可追溯至对传统密码认证安全性的需求，早期研究聚焦于利用指纹、虹膜等生理特征实现唯一身份验证。这一阶段的核心假设是生物特征在受控环境下稳定且无恶意攻击，因此研究重心在于手工特征提取（如Gabor滤波、Minutiae提取）的精度优化。然而，手工特征在真实场景中的泛化能力严重不足，面对噪声、遮挡及姿态变化时性能急剧下降，这构成了该领域最初的结构性矛盾。

随着深度学习（CNN/Transformer）的引入，问题定义发生了第一次根本性转变：从“理想数据下的精度优化”转向“真实噪声与遮挡下的鲁棒性”。深度学习通过端到端学习自动提取判别性特征，显著提升了在复杂环境下的识别性能，确立了其在特征提取与匹配中的主流地位。这一转变不仅解决了手工特征泛化差的问题，还使得模型能够处理更复杂的生物特征变异性，为后续的大规模部署奠定了基础。

2020年后，问题定义进一步演化为“系统安全与部署效率并重”。随着应用场景从受控实验室向开放、对抗环境迁移，原有假设（如数据分布稳定、无恶意攻击）不再成立。核心问题演变为对抗攻击防御、开放集拒绝、无接触采集鲁棒性及大规模隐私保护。此时，识别精度不再是唯一目标，系统的安全性（抗攻击、隐私合规）与部署效率（边缘计算、实时性）成为同等重要的约束条件。

子问题之间存在强依赖关系：无接触采集的鲁棒性（姿态/光照）是基础，若无法稳定采集，后续的开放集识别与对抗防御将失去意义；模板保护与隐私计算是部署层约束，决定了识别算法在边缘设备上的可行性；多模态融合依赖于单模态特征的独立性与相关性建模。这种依赖结构决定了方法演进必须遵循“采集-特征-安全”的层次逻辑。

2016-2018年，度量学习与原型网络奠定了少样本生物特征识别的基础，但主要局限于封闭集假设。2020年，跨域基准的出现暴露了域偏移下的性能瓶颈，促使研究者引入预训练与视觉语言模型。2021-2023年，生成式模型（GAN/Diffusion）的兴起解决了生物特征数据稀缺和隐私保护问题，使得合成指纹和跨域数据增强成为可能。2023-2025年，研究进入细化与融合阶段，3D重建（如FingerSplat）与物理对抗攻击（如CAAP）成为焦点，无接触采集与物理世界安全成为新战场。当前，领域活跃度极高，重点解决大规模部署中的隐私保护、开放集识别以及针对深度伪造和物理对抗补丁的安全评估。

**如果用一个核心问题概括该领域，那便是：如何在开放、对抗且资源受限的真实环境中，构建兼具高精度、抗攻击能力与隐私合规性的生物特征身份验证系统。**

## 2. 方法体系

- 1993：Daugman IrisCode——基于Gabor滤波器提取虹膜纹理的相位量化特征，奠定了现代虹膜识别系统的理论基础

- 2004：SFinGe——利用数学脊流模型与Gabor滤波进行物理仿真，生成具有多印次一致性的合成指纹

- 2020：DeepPrint——双分支CNN架构，结合纹理分支与细节点分支提取指纹特征，显著提升了大规模指纹搜索的鲁棒性

- 2023：UoU Foundation Model——基于大规模无监督学习的通用指纹基础模型，实现了跨任务的统一表示

- 2025：FingerSplat——基于3D高斯泼溅的无接触指纹3D重建与生成方法，解决姿态变化导致的匹配难题

- 2026：CAAP Adversarial Patch——针对掌纹识别模型的捕获感知对抗补丁攻击，揭示了掌纹系统在现实部署中的安全漏洞

这条时间线勾勒了该领域方法演进的代表性节点：从 1993 年的 Daugman IrisCode 奠定该领域方法基线，经 2004 年 SFinGe 的推进，到 2026 年的 Post-Mortem Iris Recognition 代表当前前沿。各节点对应的技术路线、取舍与关联，详见后续小节。

### 2.1 指纹识别与增强

指纹识别的早期方法依赖手工特征提取，如Minutiae提取与Gabor滤波，但受限于泛化能力。2020年，DeepPrint（Koner et al., 2020）引入双分支CNN架构，结合纹理与细节点分支，显著提升了大规模指纹搜索的鲁棒性，标志着深度学习在指纹识别中的主导地位。然而，DeepPrint主要面向接触式采集，无法解决无接触场景下的姿态畸变问题。

针对无接触采集的挑战，FingerSplat（Jia et al., 2025, P1）提出基于3D高斯泼溅的3D重建与生成方法，通过局部与全局对齐解决姿态变化导致的匹配难题。该方法放弃了2D图像的简单性，换取了跨姿态匹配的鲁棒性，但计算成本显著增加。Fusion2Print（Sahoo and Namboodiri, 2026, P15）则采取另一条路线，利用双编码器注意力融合网络处理闪光与非闪光图像，通过光照差异提取3D脊线信息，以较低的计算成本换取了对光照依赖的缓解。

在低质量指纹识别方面，LatentPrintFormer（Maity et al., 2025, P8）提出混合CNN-Transformer架构，引入空间注意力机制处理潜在指纹的噪声与遮挡。该方法解决了传统匹配算法在局部且噪声大特征上的失效问题，但依赖高质量的细节点提取。LEADER（Cappelli and Ferrara, 2026, P21）则聚焦于轻量级细节点提取，通过集成非极大值抑制与自适应真值编码，以0.9M参数实现了向潜在指纹的跨域泛化，牺牲了部分精度换取了部署效率。

UoU Foundation Model（Guan et al., 2026, P39）代表了基础模型化的趋势，通过大规模无监督学习提取可复用特征，支持增强、匹配及质量评估等多种下游任务。该方法放弃了模块化流水线的灵活性，换取了特征表示的统一性与鲁棒性。IMPOSE（Pan et al., 2026, P31）则利用去噪扩散概率模型生成多姿态无接触指纹，通过物理仿真确保身份一致性，解决了无接触指纹数据中姿态多样性不足的问题。

| 技术路线 | 核心假设 | 放弃的代价 | 换取的收益 | 典型代表方法 | 适用场景 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 深度学习特征提取 | 数据分布稳定 | 计算开销增加 | 鲁棒性与精度提升 | DeepPrint, UoU | 大规模部署 |
| 3D重建 | 几何信息可用 | 传感器依赖 | 跨姿态鲁棒性 | FingerSplat | 无接触采集 |
| 多光谱融合 | 光照差异有效 | 硬件复杂度 | 光照鲁棒性 | Fusion2Print | 无接触采集 |
| 生成式数据增强 | 合成数据逼真 | 分布偏差风险 | 数据多样性 | IMPOSE | 数据稀缺场景 |

### 2.2 活体检测与防伪

活体检测（PAD）的核心目标是区分真实生物特征与伪造样本。早期方法依赖被动纹理检测，但难以区分高仿真伪造品。Conditional Synthetic Live and Spoof Fingerprint Generation（Abbas et al., 2025, P5）利用StyleGAN3生成条件化活体与欺骗指纹，通过径向基函数模拟非线性形变，为防伪检测模型提供了多样化的训练样本。该方法放弃了真实数据的隐私限制，换取了攻击类型的覆盖广度。

Illumination-Aware Contactless Fingerprint Spoof Detection（Sahoo and Namboodiri, 2026, P24）提出基于配对闪光-非闪光成像的无接触指纹防伪检测方法，利用光照差异作为隐式活体信号。该方法解决了无接触采集缺乏物理接触活体线索的问题，但依赖特定的成像硬件。Adaptive Thresholding Pattern for Fingerprint Forgery Detection（Farzadpour and Azghani, 2025, P10）则聚焦于软件级防御，通过自适应阈值机制动态调整决策边界，以较低的成本换取了对复杂攻击场景的检测鲁棒性。

针对深度伪造与注入攻击，Selfie-Capture Dynamics as an Auxiliary Signal（Rantahalvari et al., 2026, P30）利用移动设备在自拍捕获阶段产生的运动传感器数据，构建时间序列特征，区分真实用户与自动化攻击。该方法无需额外硬件，利用现有手机传感器即可实现，为移动远程身份验证提供了低成本且鲁棒的防伪手段。Dual-Stream Challenge-Response Protocol for Ocular Liveness（Kably, 2026, P42）则采取主动式防伪手段，通过向用户呈现动态挑战并分析眼部响应，增加了攻击难度，但牺牲了用户体验。

Continual Few-shot Adaptation for Synthetic Fingerprint Detection（Benjamin et al., 2026, P23）针对合成指纹注入攻击，提出持续少样本适应方法，利用少样本学习快速适应新分布。该方法解决了数据注入攻击中合成指纹多样性高且不断演变的问题，但依赖初始训练集的覆盖广度。Classical Dimensionality Reduction for Saliency-Guided PAD（Webster and Scheirer, 2026, P37）则验证了经典降维算法在显著性引导训练中的有效性，降低了高资源标注的依赖，为资源受限场景提供了高效且可解释的训练策略。

### 2.3 虹膜识别技术

虹膜识别的奠基性工作Daugman IrisCode（Daugman, 1993）基于Gabor滤波器提取相位量化特征，通过汉明距离进行匹配，奠定了现代虹膜识别系统的理论基础。然而，传统方法在离轴与无约束条件下性能急剧下降。ImmerIris（Mi et al., 2025, P4）提出针对沉浸式应用的大规模离轴与无约束虹膜识别数据集与基准，揭示了现有算法在离轴与无约束条件下的局限性，推动了虹膜识别算法向无约束场景的迁移。

CLRecogEye（Sharma et al., 2025, P11）提出基于课程学习的动态虹膜识别框架，利用改进的I3D网络捕捉时空纹理特征，结合ArcFace与三元组损失优化判别边界。该方法针对动态虹膜图像中的微小变化，提升了识别的稳定性，但依赖视频序列的采集。Post-Mortem Iris Recognition（Bhuiyan et al., 2026, P25）则拓展了虹膜识别在法医科学中的应用，利用Siamese网络学习抗衰减特征，解决了传统活体虹膜算法在死后样本上性能急剧下降的问题。

在质量评估方面，Visible Iris Area as a Quality Metric（Pessaud et al., 2025, P6）提出基于可见虹膜面积的质量评估指标，量化图像质量对识别性能的影响。该方法解决了传统质量指标无法充分反映瞳孔扩张与遮挡影响的问题，为大规模虹膜识别系统的部署提供了质量保障机制。Pupil Size Normalization for Human Iris Judgment（Mitcheff and Czajka, 2026, P17）则研究人类观察者在归一化图像上的识别准确性变化，揭示了瞳孔大小对虹膜识别的重要影响，为优化自动系统与人类专家协同工作提供了理论依据。

Optimizer Sensitivity in ViT-based Iris Recognition（Faiz et al., 2025, P12）系统比较了不同优化器在ViT模型训练中的收敛性与稳定性，揭示了优化器选择对小型生物特征数据集训练稳定性的关键影响。该研究为生物特征深度学习模型的训练提供了重要的实践指导，强调了优化器选择对模型性能的决定性作用。Pediatric Iris Recognition Permanence Study（Venkataswamy et al., 2025, P14）则通过混合效应模型分析儿童虹膜识别永久性，证明了虹膜特征在儿童发育过程中的稳定性，支持了将虹膜识别应用于儿童身份管理的可行性。

### 2.4 掌纹与静脉识别

掌纹与静脉识别面临的主要挑战是跨域泛化与开放集识别。X-Palm（Seyedmohammadi et al., 2026, P36）提出配对多光谱至智能手机的跨域掌纹数据集，通过配对采集建立同一身份在两个不同域之间的映射关系，填补了掌纹跨域研究的数据空白。FlowPalm（Zou et al., 2026, P27）利用光流驱动的非刚性形变生成几何多样化的掌纹，提升了模型在几何畸变下的泛化能力。

Open-Set Vein Biometric Recognition with Deep Metric Learning（Pilarek et al., 2026, P28）提出基于深度度量学习的开放集静脉生物特征识别框架，利用ResNet50与CBAM提取判别性血管特征，通过余弦相似度计算与校准阈值实现未知身份拒绝。该方法解决了传统静脉识别在强类内变异性与传感器变化下性能下降的问题，但依赖高质量的血管特征提取。

CAAP: Capture-Aware Adversarial Patch Attacks（Liu et al., 2026, P26）提出捕获感知的对抗补丁攻击方法，利用期望过变换形式化随机几何与光度变换，确保对抗补丁的物理鲁棒性。该方法揭示了掌纹识别系统在物理世界部署中的安全漏洞，为防御机制的设计提供了攻击基准。Unified Adversarial Augmentation for Palmprint Recognition（ICCV 2025, P44）则提出统一对抗增强框架，利用可微空间变换器与预训练生成神经网络生成具有几何与纹理变化的样本，提升了模型在几何畸变与纹理退化下的泛化能力。

PalmBridge: Plug-and-Play Feature Alignment Framework（Zhang et al., 2026, P18）提出即插即用的特征对齐框架，利用风格迁移模型进行像素级对齐，随后进行特征级对齐，以桥接不同数据集间的差距。该方法解决了跨域掌纹识别中特征空间不一致的问题，降低了域适应的计算成本。Adaptive Contrast Enhancement and Optimised Feature Matching for RootSIFT-Based Palm-Vein Recognition（Perera et al., 2026, P43）则引入ILACS-BGOT技术，通过局部对比拉伸与层次化方法消除块效应，提升了RootSIFT在掌静脉识别中的性能。

### 2.5 多模态与行为生物

多模态融合旨在利用不同生物特征间的统计相关性提升安全性。Bi-Encoder Contrastive Learning for Fingerprint and Iris Biometrics（So et al., 2025, P7）提出双编码器对比学习框架，挑战指纹与虹膜统计独立的传统假设，通过对比损失函数优化嵌入空间，使同一主体的不同模态特征靠近。该方法揭示了生物特征间的内在关联性，为多模态生物特征融合提供了新的理论依据。

Two-step Authentication: Multi-biometric System Using Voice and Facial Recognition（Chen et al., 2026, P16）提出两步生物特征认证系统，利用人脸识别确定个体身份，随后仅针对该个体进行语音验证，简化了语音识别模型的搜索空间。该方法解决了多模态系统硬件成本高的问题，提供了实用的移动设备认证方案。Automated User Identification from Facial Thermograms with Siamese Networks（Prozorova et al., 2025, P13）则利用热成像技术捕获面部温度分布，通过Siamese网络比较两张热图的相似度，提供了与可见光图像互补的生物特征信息。

在行为生物特征方面，Neural Network-Powered Finger-Drawn Biometric Authentication（Al Balkhi et al., 2025, P9）利用用户在触摸屏上用手指绘制数字的行为数据，通过CNN模型提取动态生物特征，解决了传统静态生物特征易被合成或重建的问题。First International StepUP Competition for Biometric Footstep Recognition（Larracy et al., 2026, P20）提出基于压力敏感地板捕获的足底压力模式识别方法，提供了基于压力传感的新型生物特征模态。BEACON: A Multimodal Dataset for Learning Behavioral Fingerprints from Gameplay Data（Singh et al., 2026, P33）则整合鼠标、键盘、网络包及游戏视频数据，构建了连续行为指纹挖掘的新基准，推动了行为生物特征在网络安全领域的应用。

Subject-Level Unknown-Identity Identification from Leap Motion Controller 2 Hand Landmarks（Moharrer et al., 2026, P41）提出基于Leap Motion Controller 2手部地标的未知身份识别方法，采用Leave-One-Subject-Out开放集协议，评估模型在已知身份识别与未知身份拒绝上的性能。该方法验证了基于地标的手部生物特征在开放集识别中的可行性，为无接触手部认证提供了新的技术路径。Towards Billion-scale Multi-modal Biometric Search（Koner et al., 2026, P32）则提出面向十亿级规模的多模态生物特征搜索系统，整合指纹、虹膜与人脸，解决了大规模生物特征库中多模态去重与搜索的效率与准确性问题。

### 2.6 安全架构与评估

安全架构的核心目标是保护生物特征模板的隐私与安全性。LocalScore: Local Density-Aware Similarity Scoring（Su et al., 2026, P19）提出局部密度感知的生物特征相似度评分方法，利用图库特征的局部密度结构，计算查询与每个主体的相似度，提升了开放集检索的可靠性。该方法解决了传统聚合评分忽略类内变异性与特征分布结构的问题，为大规模生物特征系统的部署提供了更鲁棒的决策机制。

Scalable Secure Biometric Authentication without Auxiliary Identifiers（Bienstock et al., 2026, P29）提出无需辅助标识符的可扩展安全生物特征认证架构，利用ArcFace提取高熵生物特征模板，并通过局部敏感哈希生成子串，实现去中心化的身份验证。该方法解决了传统生物特征系统依赖中心数据库与辅助标识符的安全隐患，适用于大规模IoT与移动设备场景。BIDO: A Biometric Identity Online Authentication Framework（Mithra et al., 2026, P34）则基于FIDO2标准，利用可信执行环境保护生物特征模板，实现无设备依赖的在线认证，符合国际标准且隐私保护。

在评估指标方面，Beyond ROC-AUC: Operating-Point Performance Reporting for Biometric Verification（Ahmed and Imtiaz, 2026, P40）强调在特定操作点评估模型性能，而非仅依赖AUC指标，揭示了AUC在生物特征验证中的局限性。Advanced Acceptance Score: A Holistic Measure for Biometric Quantification（Verma et al., 2026, P22）提出高级接受分数作为生物特征量化的整体度量，结合错误率与分数值，提供比匹配率更细致的评估指标。Iterative Framework For Data Augmentation Of Segmented Fingerprints（Agnol et al., 2026, P35）则提出针对分段指纹的迭代数据增强框架，利用神经网络生成合成指纹样本，通过迭代过程逐步优化生成质量，解决了生物特征系统在处理婴儿及低质量指纹时的性能瓶颈。

## 3. 关键共识、分歧与开放问题

### 3.1 领域共识

深度学习（CNN/Transformer）在特征提取和匹配精度上显著优于传统手工特征方法，已成为生物识别研究的主流范式。这一共识在多个基准上被反复验证：CLRecogEye的0.23% EER与FlowPalm的58.95 Avg均大幅超越经典基线，且约20篇论文共同支持这一结论。然而，该共识的边界在于，深度学习在资源受限场景下的部署效率仍待优化，且对数据量的要求较高。

无接触生物识别虽提升了用户体验和卫生性，但在姿态变化和光照鲁棒性上仍落后于接触式采集，是当前研究热点。FingerSplat与Fusion2Print等方法通过3D重建与多光谱融合缓解了这一瓶颈，但计算成本与硬件依赖仍是主要障碍。生成式模型（GAN/Diffusion）是解决生物特征数据稀缺和隐私保护的有效手段，可用于合成训练数据和模拟攻击，约6篇论文共同支持这一共识，但合成数据的分布偏差仍需额外验证。

### 3.2 观点分歧

多模态生物特征的独立性假设是领域内的核心分歧之一。传统观点认为不同生物特征源自不同生理机制，应视为独立模态，采用简单加权或决策级融合。而新兴观点（如So et al., 2025, P7）揭示指纹与虹膜存在统计依赖性，应采用联合学习或对比学习捕捉内在关联。现有证据偏向新兴观点，实验显示联合学习在跨模态匹配中优于独立融合，但证据强度中等，主要基于小规模数据集，缺乏大规模多模态基准验证。

隐私保护的计算开销是另一根本分歧。同态加密（FHE）虽提供强隐私保护，但计算开销巨大，是否适合边缘设备？现有证据偏向可撤销生物特征作为折中方案，但FHE在特定高安全场景仍不可替代。对抗防御的通用性也是争议焦点，CAAP等物理攻击表明，纯数字对抗训练在物理世界失效，需引入物理感知优化，但缺乏通用性。

### 3.3 其他开放问题

最紧迫的工程问题是无接触指纹3D重建的实时性与FHE在移动端的加速。3D重建的计算开销与传感器依赖限制了其普及，而FHE算法优化仍在进行中，未来硬件可能改变开销格局。最根本的研究问题是开放集识别中“未知”的数学定义与不确定性估计，以及物理对抗攻击的跨域泛化机制。生物特征随时间（如儿童发育）的永久性量化也是重要研究方向，Pediatric Iris Recognition Permanence Study（Venkataswamy et al., 2025, P14）提供了初步实证依据，但长期稳定性仍需进一步验证。

已知—争议—未知认知图谱显示，深度学习在特征提取上的优越性已达成共识，但多模态融合策略与隐私保护方案仍存在根本分歧。未来发展趋势将聚焦于3D感知、生成式攻防与去中心化安全架构，构建自适应、可撤销、抗攻击的系统生态。

## 4. 总结与展望

生物识别与安全的未来不在于单一算法的精度提升，而在于构建一个“自适应、可撤销、抗攻击”的系统生态。核心任务依然是如何在开放对抗环境中实现可靠身份验证，但实现路径已从“特征工程”转向“系统架构”与“攻防博弈”。当前领域面临“工程瓶颈”与“理论盲区”的双重挑战：工程上，3D重建与FHE的计算效率是主要障碍；理论上，开放集识别的不确定性量化与物理对抗攻击的通用防御机制尚属空白。

未来可能突破的方向包括：基于基础模型（Foundation Model）的统一生物特征表示，如UoU（Guan et al., 2026, P39）所示，通过大规模无监督学习提取可复用特征；去中心化身份（DID）与生物特征的深度融合，如BIDO（Mithra et al., 2026, P34）所示，利用FIDO2标准实现无设备依赖的在线认证；以及物理感知对抗防御机制，如CAAP（Liu et al., 2026, P26）所示，通过期望过变换优化物理世界鲁棒性。对进入者最值得做的一件事是建立更真实的评测基准，关注物理世界部署中的鲁棒性与隐私合规，填补现有基准在跨域、对抗与隐私保护方面的空白。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/surveys/Biometric%20Recognition%20and%20Security)