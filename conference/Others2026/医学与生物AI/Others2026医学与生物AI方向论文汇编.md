# Others2026 · 医学与生物AI方向论文汇编

> 本方向共 29 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents ｜医疗大语言模型智能体七维评估分类学

研究机构：美国纽约大学

作者：Shubham Vatsal、Harsh Dubey、Aditi Singh

论文原文见 [arXiv](https://arxiv.org/abs/2602.04813)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04813)

> 医疗大语言模型智能体（LLM Agent）在临床部署中面临能力评估标准缺失与文献碎片化的双重困境，现有综述多聚焦单一能力或通用架构，缺乏针对医疗场景的统一量化框架。本文切入点在于构建一个涵盖认知、知识、交互、适应、安全、架构与任务七个维度的分类学，对49篇研究进行实证映射。通过定义29个操作性子维度及三级标签体系，本文揭示了当前智能体在外部知识集成上的高普及率与在事件触发激活、漂移检测上的结构性缺失。该工作提供了领域现状的实证基线，但其标签判定依赖人工保守赋值，未解决模拟环境与真实临床部署间的效度差异问题。

】

---

【CardioPHON：心音图质量评估与自监督预训练

作者：Vladimir Despotovic、Peter Pocta、Andrej Zgank

论文原文见 [arXiv](https://arxiv.org/abs/2511.04533)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04533)

> 远程心血管筛查依赖心音图（PCG）信号，但家庭非专业采集环境下的噪声伪影导致模型误诊，且标注数据稀缺阻碍了高精度分类器的训练。现有方法要么使用传统机器学习进行质量过滤但缺乏端到端优化，要么使用小规模自监督学习但预训练数据不足。本文切入点在于整合一个基于传统机器学习的质量评估前置模块，并构建首个大规模公开PCG自监督预训练模型，通过特征级融合音频与社会人口学变量提升分类性能。该工作验证了数据清洗与多模态融合在儿科心音分类中的有效性，但其质量评估模块的独立贡献度及跨域泛化能力存疑。

】

---

【DCG-Net: Dual Cross-Attention with Concept-Value Graph Reasoning for Interpretable Medical Diagnosis ｜概念-值依赖建模的医学影像诊断框架

研究机构：澳大利亚格里菲斯大学

作者：Getamesay Dagnaw、Xuefei Yin、Muhammad Hassan Maqsood 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20325)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20325)

> 医学影像诊断中，概念瓶颈模型（Concept Bottleneck Model, CBM）因忽略临床概念间复杂的上下文依赖，常产生逻辑不一致的解释。现有方法多停留在概念存在性层面，未能捕捉特定概念值组合（如“细胞大”且“核质比低”）所隐含的诊断逻辑。DCG-Net 通过双交叉注意力与参数化概念图，在概念-值对粒度上建立依赖关系，实现了更细粒度的临床推理。该架构在皮肤与血液学数据集上提升了诊断精度与解释一致性，但其对图结构先验的依赖及跨域泛化能力仍存疑。

】

---

【亚利桑那团队新研究：临床文本自闭症检测中的透明迁移学习

研究机构：美国亚利桑那大学

作者：Gondy Leroy、Prakash Bisht、Sai Madhuri Kandula 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.06161)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.06161)

> 本文旨在解决自闭症谱系障碍（ASD）临床诊断中黑盒模型缺乏可解释性且跨机构泛化能力未知的双重困境。现有方法多依赖单一数据集训练，无法量化模型在语言风格、评估重点不同的真实世界场景中的性能衰减，且难以向非专科医生提供可追溯的诊断依据。作者构建基于BioBERT的透明与黑盒双路径模型，通过顺序与混合数据迁移学习策略，量化了跨数据集的知识迁移效果。该工作证明了透明规则聚合在临床信任度上的优势，但其案例级高特异度是否受限于EHR数据中极低的ASD基率，仍需更严格的统计校正来验证。

】

---

【伦敦大学团队新研究：混合图检索增强框架

研究机构：英国伦敦大学学院

作者：Samuel Thio、Matthew Lewis、Spiros Denaxas 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00009)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00009)

> 临床电子健康记录（EHR）中结构化数据与非结构化文本的割裂，导致大语言模型（LLM）在患者级查询时缺乏上下文接地，易产生幻觉。现有检索增强生成（RAG）方案通常仅处理单一模态，无法同时兼顾精确的结构化关系遍历与模糊的语义叙事检索。本文提出 MediGRAF，通过 Neo4j 图数据库与向量嵌入的并行混合架构，实现自然语言对完整患者旅程的统一查询。该方案在事实完整性上表现优异，但缺乏横向基线对比，且响应冗长问题未解决。

】

---

【伦斯勒理工团队新研究：级联对抗时空注意力网络

研究机构：美国伦斯勒理工学院、美国麻省理工学院

作者：Zan Li、Kyongmin Yeo、Wesley Gifford 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.01275)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01275)

> 癫痫发作预测的核心矛盾在于，发作前状态（Pre-ictal State）的微弱非平稳特征与临床对极低误报率（False Detection Rate, FDR）的严苛要求难以兼得。现有方法或受限于固定预测窗口导致的个体差异失配，或采用空间与时间解耦处理而丢失跨模态交互，且高参数量阻碍了边缘部署。本文切入点在于通过级联交替注意力模块联合建模双向时空依赖，并引入WGAN-GP对抗训练优化决策边界。其价值在于以2.3M参数量实现了0.011/h的极低FDR，但自监督预训练的必要性及跨数据集泛化能力仍存疑。

】

---

【利兹团队新研究：基于固定聚合的自解释胸部X光分类架构

研究机构：英国利兹大学

作者：Patrick Wienholt、Christiane Kuhl、Jakob Nikolas Kather 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.07477)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07477)

> 临床部署中的深度学习模型常因“黑盒”特性导致医生无法审计其决策逻辑，而事后解释方法（如Grad-CAM）生成的热力图往往与真实决策依据脱节，甚至掩盖捷径学习风险。MedicalPatchNet 通过架构内解释策略，将图像分割为独立处理的Patch，利用固定算术平均聚合局部Logits，使每个Patch的贡献直接可视化为归因信号。该设计在保持与标准EfficientNetV2-S相当分类性能的前提下，显著提升了空间定位的忠实度，但其解释粒度停留在像素区域层面，缺乏临床语义深度，能否满足医生对病理机制的深层理解需求仍存疑。

】

---

【北京航空航天团队新研究：超声视频时序分割中的小波频域建模与长短期记忆机制

研究机构：北京航空航天大学

作者：Chenxiao Zhang、Runshi Zhang、Junchen Wang

论文原文见 [arXiv](https://arxiv.org/abs/2512.15066)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15066)

> 超声视频分割面临低对比度、斑点噪声及长序列中小目标跟踪丢失的三重挑战，现有单帧模型忽略时序依赖，而纯时序模型又缺乏对高频边界细节的显式建模。本文切入点在于将小波变换嵌入骨干网络以分离高低频特征，并引入长短期记忆库以维持长程时序一致性。具体做法是构建基于小波卷积的编码器-解码器架构，通过级联小波压缩扩大感受野，并利用自适应小波滤波器在解码阶段增强高频边界。该方法在四个超声视频数据集上取得了优于现有SOTA的分割精度，但其性能增益主要依赖视频时序信息，在单帧静态图像场景下的泛化能力尚未得到充分验证。

】

---

【北京邮电团队新研究：医学视觉强化微调中的感知与推理增强

研究机构：北京邮电大学、美国埃默里大学

作者：Guangjing Yang、ZhangYuan Yu、Ziyuan Qin 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.10619)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.10619)

> 医学影像理解要求模型同时具备精细的视觉感知与结构化的临床推理，而现有基于强化学习（RL）的视觉-语言模型（LVLM）后训练在医学场景中常因早期奖励稀疏与感知能力不足而失效。VRFT-Aug 通过提示工程注入领域知识、跨任务定位训练强化空间感知，并设计模糊奖励机制缓解等级分类中的稀疏奖励问题。该框架在少样本医学分类任务上显著优于标准监督微调与基础 RL 基线，但其效果高度依赖特定奖励设计，且在复杂分布偏移下的泛化能力尚未得到充分验证。

】

---

【医疗大语言模型评估策略的三元分类框架

作者：Victor Garcia、Mariia Sidulova、Aldo Badano

论文原文见 [arXiv](https://arxiv.org/abs/2509.08087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.08087)

> 医疗大语言模型（LM）在临床部署中面临评估手段与真实临床复杂性脱节的困境。现有单一基准测试易陷入过拟合，而纯人工评估又受限于成本与主观性，导致无法在严谨性、实用性与可扩展性间取得平衡。本文提出将评估策略划分为基准评估、人类评估与模型作为评估器（MAE）三类，并系统分析其优劣与适用边界。该框架为混合评估提供了方法论基础，但MAE的误差传播风险与长期安全性验证仍缺乏量化支撑。

】

---

【单标签胸片多病分类的架构效率权衡

作者：Ali M. Bahram、Saman Muhammad Omer、Hardi M. Mohammed

论文原文见 [arXiv](https://arxiv.org/abs/2603.13392)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13392)

> 胸部X光（Chest X-ray, CXR）诊断面临放射科医生短缺与阅片疲劳导致的诊断一致性危机，但现有研究多聚焦于多标签分类精度，忽视了资源受限场景下模型部署的计算效率瓶颈。主流方法在平衡数据集上缺乏对现代卷积神经网络与视觉Transformer（Vision Transformer, ViT）架构的系统性对比，且常因数据不平衡导致少数类性能虚高。本文通过构建五类平衡数据集，在统一条件下对比七种架构的性能-效率权衡。该研究验证了轻量化架构在资源受限场景的可行性，但单标签简化掩盖了临床多病共存的复杂性。

】

---

【卡内基梅隆团队新研究：时空适配器与多头池化

研究机构：美国卡内基梅隆大学、美国匹兹堡大学

作者：Brad Shook、Abby Turner、Jieshi Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.10848)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10848)

> 通用时间序列基础模型（TSFM）在脑电（EEG）任务上因缺乏空间拓扑建模能力而失效，现有EEG专用基础模型（EEGFM）虽性能强劲但参数量庞大且依赖特定预训练数据。本文切入点在于验证通用TSFM通过轻量级适配器能否替代昂贵的EEG专用预训练。STAMP通过冻结TSFM骨干，利用约0.74M参数的时空适配器重建空间-时间依赖，实现了与SOTA EEGFM相当的性能。其价值在于降低了部署门槛，但绝对性能仍低于大规模EEG专用模型，且未解决高频信号丢失问题。

】

---

【国防科技团队新研究：多尺度图神经过程与跨药协同注意力

研究机构：国防科技大学

作者：Zimo Yan、Jie Zhang、Zheng Xie 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15256)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15256)

> 药物相互作用（DDI）预测旨在通过计算手段预判多药联用的安全风险，核心难点在于分子结构信息的尺度缺失与交互建模的静态化。现有双GNN架构独立编码药物后简单拼接，导致表征缺乏上下文感知能力，且无法量化预测置信度。本文提出MPNP-DDI，通过堆叠图神经过程（GNP）提取多尺度特征，并利用跨药协同注意力动态融合，实现概率性预测。该框架在基准测试中表现优异，但其对关系类型嵌入的极端依赖及未验证的冷启动泛化能力，限制了其在真实临床场景中的直接应用。

】

---

【基于EfficientNetV2与MLP-Mixer注意力的可解释脑肿瘤MRI分类

作者：Mustafa Yurdakul、Şakir Taşdemir

论文原文见 [arXiv](https://arxiv.org/abs/2509.06713)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.06713)

> 脑肿瘤MRI分类旨在通过自动化模型替代人工阅片，以解决放射科医生工作负荷高且诊断一致性差的临床痛点。现有CNN架构虽能提取局部纹理，但受限于感受野，难以捕捉肿瘤与周围脑组织的长程空间依赖，且缺乏临床可解释性。本文切入点在于将线性注意力机制嵌入MLP-Mixer结构，并嫁接于EfficientNetV2骨干，以在保持计算效率的同时增强全局特征混合能力。该方法在Figshare三分类任务上取得了99.50%的准确率，但缺乏四分类及跨域泛化验证，其临床部署的鲁棒性存疑。

】

---

【基于加密[CLS]令牌的联邦视觉Transformer学习

作者：Al Amin、Kamrul Hasan、Liang Hong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.20983)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20983)

> 联邦学习（Federated Learning, FL）在医疗影像协作中面临梯度泄露风险与同态加密（Homomorphic Encryption, HE）通信开销过高的双重瓶颈。现有方案要么牺牲隐私直接传输明文特征，要么因加密高维梯度导致通信成本不可接受。本文利用视觉Transformer（Vision Transformer, ViT）的[CLS]令牌作为紧凑语义载体，仅加密该768维向量进行联邦聚合，在保持密码学安全性的同时大幅降低传输负担。该方法在强隐私约束下实现了通信效率与分类精度的平衡，但其对数据异质性的鲁棒性及临床部署的最低精度阈值仍存疑。

】

---

【基于核平滑器的小样本小胶质细胞计数与不确定性估计

作者：L. Martino、M. M. Garcia、P. S. Paradas 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22974)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22974)

】

---

【基于非负矩阵分解与扩散去噪的脑肿瘤对抗鲁棒分类

作者：Hiba Adil Al-kharsan、Róbert Rajkó

论文原文见 [arXiv](https://arxiv.org/abs/2603.13182)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13182)

> 脑肿瘤辅助诊断系统面临的核心矛盾是高精度模型在对抗扰动下的脆弱性，微小输入修改即可导致误诊。现有主流深度学习方法虽在干净数据上表现优异，但普遍缺乏对对抗攻击的防御机制，且特征表示往往不可解释。本文切入点在于将非负矩阵分解（Non-Negative Matrix Factorization, NNMF）的可解释特征提取与扩散模型的特征空间去噪相结合，构建轻量级分类框架。该方法在AutoAttack下将鲁棒准确率从0.0047提升至0.5953，但干净数据准确率仅约83%，远低于领域SOTA，其临床实用性与泛化能力存疑。

】

---

【山东团队新研究：基于视觉Transformer与残差特征网络的磁粒子成像系统矩阵超分辨率恢复

研究机构：山东大学、中国科学院

作者：Abuobaida M. Khair、Wenjing Jiang、Yousuf Babiker M. Osman 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.02212)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.02212)

> 磁粒子成像（MPI）系统矩阵恢复旨在从低分辨率退化矩阵中重建高分辨率映射，以支撑定量成像。现有Transformer方法仅捕获全局依赖，缺乏局部高频细节恢复能力，且未考虑接收线圈灵敏度变化。本文提出VRF-Net，通过融合视觉Transformer全局注意力与残差特征局部细化，并引入双阶段频域降采样模拟线圈灵敏度变化。该方法在Open MPI数据集上实现了39.08 dB的pSNR，但仅验证了2D切片处理，未解决跨切片空间一致性问题。

】

---

【放射科医生在AI辅助结构化报告下的视觉搜索与诊断行为

作者：Mahta Khoobi、Marc Sebastian von der Stueck、Felix Barajas Ordonez 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.16070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.16070)

> 放射科报告生成（Radiology Report Generation, RRG）领域长期聚焦于算法层面的文本生成质量与幻觉抑制，却忽视了AI输出如何改变人类医生的认知过程与视觉搜索策略。现有评估体系多依赖静态文本指标，无法捕捉医生在修正AI草稿时的注意力分配与认知负荷变化。本文通过眼动追踪技术，量化了自由文本、结构化报告及AI预填充结构化报告三种模式下医生的诊断行为。该研究揭示了AI辅助在提升效率与准确性上的行为学机制，但样本量较小且未覆盖复杂病理场景，其结论的泛化性仍需更大规模临床验证。

】

---

【格里菲斯团队新研究：无提示轻量级SAM适配用于组织病理学核分割

研究机构：澳大利亚格里菲斯大学

作者：Muhammad Hassan Maqsood、Yanming Zhu、Alfred Lam 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20326)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20326)

> 组织病理学核分割旨在从密集且染色不均的组织图像中精确界定细胞核边界，以支撑肿瘤分级与预后分析。传统全监督模型虽精度高，但参数量大且跨数据集泛化能力弱，而现有基于Segment Anything Model (SAM) 的适配方法多依赖提示引导或复杂解码器，难以直接应对病理图像的细粒度纹理挑战。本文提出一种无提示、轻量级的SAM适配框架，仅微调冻结编码器内的LoRA模块并引入残差解码器，以4.1M可训练参数实现高效分割。该方法在MoNuSeg上达到79.5 Dice的SOTA水平，但在PanNuke上略低于最新实例分割专用模型，其无提示设计在复杂拓扑结构下的精度上限尚存疑。

】

---

【洛桑联邦理工团队新研究：结构化与问题化：LLM智能体在诊断推理训练中的脚手架对比

研究机构：瑞士洛桑联邦理工学院

作者：Fatma Betül Güreş、Tanya Nazaretsky、Seyed Parsa Neshaei 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09158)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09158)

> 导读 在职业教育中，新手常因认知偏差导致诊断推理失败，而现有LLM导师缺乏对教学策略的精细化控制。本文切入LLM对话生成与学习科学理论的结合点，通过PharmaSim Switch系统对比“结构化”与“问题化”两种脚手架。系统利用规则模型追踪学生状态，驱动LLM生成符合Reiser框架的特定教学反馈。实验表明，结构化脚手架提升任务效率，问题化脚手架促进深度认知参与。该研究验证了LLM在教育场景中的行为可控性，但其在真实临床诊断中的泛化能力仍存疑。

】

---

【湖南团队新研究：测试时精化配准框架

研究机构：湖南大学、英国曼彻斯特大学

作者：Lin Chen、Yue He、Fengting Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19114)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19114)

> 可变形医学图像配准旨在通过估计密集非线性空间变换，将移动图像与固定图像在解剖结构上对齐，其核心价值在于支撑肿瘤监测、多模态融合及手术导航等临床决策。现有深度学习配准方法虽实现了推理速度的数量级提升，但受限于训练分布，在域偏移数据上性能显著下降，而传统迭代优化方法虽鲁棒但计算耗时过长。本文切入点在于利用预训练基础模型生成初始形变场，并通过低开销的测试时精化（Test-Time Refinement, TTR）模块在推理阶段直接优化形变场参数，以弥合基础模型与专用模型间的精度差距。该方法以仅增加0.56秒推理时间的代价，在腹部CT和心脏MRI数据集上实现了精度提升，但其缺乏显式微分同胚约束，拓扑安全性存疑。

】

---

【牙科口内影像实时分割：层级特征与双向序列建模

作者：Xinxin Zhao、Jian Jiang、Yan Tian 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21712)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21712)

> 牙科口内影像分割旨在从高分辨率口内照片中精确 delineate 牙齿、牙龈等解剖结构，以支撑数字化牙科流程。现有基于 Transformer 的 SAM 变体虽具备强泛化性，但其二次方计算复杂度导致高分辨率输入下推理延迟激增，难以满足临床实时需求。本文切入点在于替换 SAM 的 ViT 编码器为 CNN-Mamba 混合架构，通过层级特征融合与双向序列块（BSB）在保持分割精度的同时实现线性复杂度。该方案在效率与精度平衡上优于现有 SAM 变体，但其对零样本泛化能力的潜在牺牲及 2D 任务对 3D 几何先验的缺失仍存疑。

】

---

【瓦伦西亚团队新研究：半监督变分自编码器构建可解释痴呆症代谢生物标志物

研究机构：西班牙瓦伦西亚大学、美国南加州大学

作者：C. Vázquez-García、F. J. Martínez-Murcia、F. Segovia Román 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20480)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20480)

> 导读 神经退行性疾病的临床评估面临高维影像数据与低维临床评分之间的语义鸿沟，传统分类模型虽能区分状态但无法提供连续且可解释的病理表征。现有无监督变分自编码器（VAE）潜变量语义模糊，难以直接对应疾病严重程度，而纯监督方法又缺乏对混杂因素（如年龄、空间变换）的解耦能力。本文提出一种半监督VAE框架，通过引入相似度正则化项，强制特定潜维度与临床认知评分及年龄对齐，从而提取出可映射回脑空间的连续生物标志物。该框架在ADNI数据集上验证了潜变量$z_0$与痴呆症严重程度的显著相关性及其与年龄的有效解耦，但受限于单模态静态数据，其作为动态轨迹预测初始状态的潜力尚未被验证。

】

---

【科学院团队新研究：提示引导的虚拟多重免疫组化染色框架

研究机构：中国科学院、中国科学院大学

作者：Fuqiang Chen、Ranran Zhang、Wanming Hu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23292)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23292)

> 虚拟多重染色旨在从单张H&E图像同时生成多种IHC标志物图像，以解决小活检组织量不足与多重染色耗时长的临床矛盾。现有方法依赖One-hot编码或通用CLIP引导，导致标志物间生物相关性丢失，且缺乏对蛋白表达分布的显式约束，生成图像常出现病理语义错位。本文提出PGVMS，通过集成病理视觉语言模型CONCH进行动态提示引导，并引入蛋白感知与原型一致性学习策略，在单标志物数据上实现统一的多重染色生成。该方法在病理一致性指标上显著优于基线，但在视觉保真度指标上仍落后于扩散模型SOTA，其临床部署的实时性与泛化边界尚待验证。

】

---

【苏黎世联邦理工团队新研究：基于潜在注意力的多导联掩码自编码器

研究机构：瑞士苏黎世联邦理工学院、瑞士巴塞尔大学

作者：Moritz Vandenhirtz、Samuel Ruipérez-Campillo、Simon Böhi 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.26475)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26475)

> 心电图（ECG）基础模型在自监督预训练中普遍将12个导联视为独立通道，忽略了导联间固有的生理结构冗余，导致表征在小样本场景下样本效率低下。现有掩码自编码器（MAE）方法虽能学习单导联局部特征，但缺乏跨导联的高阶交互机制，难以捕捉心脏电活动的整体传导逻辑。本文通过在编码器与解码器之间引入潜在注意力（Latent Attention, LA）模块，显式建模导联间的连接机制，实现结构感知的自监督预训练。该设计在低数据量场景下显著提升了ICD-10多标签预测性能，但其在大规模数据下的边际收益及与临床引导预训练路线的优劣对比尚存疑。

】

---

【阿尔伯塔团队新研究：自解释一致性训练框架

研究机构：加拿大阿尔伯塔大学

作者：H M Quamran Hasan、Housam Khalifa Bashier、Jiayi Dai 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.20074)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20074)

> 临床决策支持系统面临预测准确率与解释可信度难以兼得的困境，现有方法因训练时依赖金标签、推理时依赖自预测的分布不一致，导致解释与预测脱节。本文提出Reason2Decide，通过两阶段训练与任务级调度采样，使模型学会解释自身预测。该框架在资源受限场景下实现了预测与解释的双重提升，但其有效性是否可迁移至大规模复杂临床推理任务，仍存疑。

】

---

【首尔团队新研究：抗体-抗原结合姿态评分

研究机构：韩国首尔大学

作者：Tien-Cuong Bui、Injae Chung、Wonjun Lee 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14870)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14870)

> 抗体-抗原（Ig-Ag）复合物结构预测的核心难点在于互补性决定区（CDR）环的高柔性导致实验结构稀缺，且传统物理评分函数在区分近原生与非原生姿态时失效。现有深度学习模型缺乏几何等变性，在分布偏移下泛化能力不足。本文切入点在于利用生成式结构预测工具构建合成decoy数据库，结合等变图神经网络与进化嵌入进行姿态分类与评分。该框架在CASP-16基准上实现了AP分数最高两倍的提升，但其依赖生成模型质量且未解决动态构象建模的根本问题。

】

---

【高丽团队新研究：基于临床验证流程图的LLM多智能体自我分诊系统

研究机构：韩国高丽大学、谷歌研究院

作者：Yujia Liu、Sophia Yu、Hongyue Jin 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.12439)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.12439)

> 患者自我分诊（Self-triage）旨在解决医疗资源错配与LLM幻觉导致的决策风险，但现有对话式LLM缺乏可审计的决策路径且难以处理模糊输入。本文切入点在于将美国医学会（AMA）验证的流程图作为外部结构化知识源，通过检索、决策、聊天三代理流水线约束LLM行为。系统利用合成对话数据验证了流程图检索与导航的准确性，证明了结构化协议对LLM输出的有效约束，但其泛化能力受限于预定义流程图的覆盖范围与合成数据的分布偏差。

】
