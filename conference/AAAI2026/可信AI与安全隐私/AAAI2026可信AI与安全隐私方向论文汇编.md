# AAAI2026 · 可信AI与安全隐私方向论文汇编

> 本方向共 8 篇（AAAI2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adversarial Attack on Black-Box Multi-Agent by Adaptive Perturbation ｜多智能体系统黑盒自适应对抗攻击

研究机构：中国科学院、中国科学院大学

作者：Jianming Chen、Yawen Wang、Junjie Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.15292)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.15292)

> 多智能体系统（MAS）在自动驾驶与无人机集群中依赖分布式决策，其安全性评估面临攻击者无法获取内部参数、仅能干扰观察的严格黑盒约束。现有攻击方法或依赖白盒梯度信息，或盲目扰动所有智能体导致隐蔽性极差，难以在有限预算下平衡有效性与隐蔽性。本文提出AdapAM框架，通过强化学习策略自适应选择关键智能体并确定恶意动作，利用代理智能体的白盒信息生成最小化扰动以诱导目标执行特定动作。该框架在八个环境中实现了优于基线的攻击效果与隐蔽性，但其依赖训练阶段动作控制权限的假设在真实部署中是否成立存疑。

】

---

【Alternative Fairness and Accuracy Optimization in Criminal Justice ｜刑事司法算法公平性的容差约束与过程问责框架

研究机构：美国哈佛大学、美国麻省理工学院

作者：Shaolong Wu、James Blume、Geshi Yeung

论文原文见 [arXiv](https://arxiv.org/abs/2511.04505)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.04505)

> 算法在刑事司法等高风险决策中的部署面临群体公平指标与预测性能互斥的数学困境，现有精确约束方法常因基率差异导致无解或性能崩溃。本文切入点在于将严格的相等约束松弛为容差约束，并引入过程公平作为合法性补充。通过最小化加权误差损失并限制假阴性率差异在阈值内，该方法在理论上保证了可行解的存在，但缺乏实证数据支撑其实际性能增益。

】

---

【Fidelity-Aware Recommendation Explanations via Stochastic Path Integration ｜随机路径积分推荐解释

研究机构：以色列特拉维夫大学

作者：Oren Barkan、Yahlly Schein、Yehonatan Elisha 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18047)

> 推荐系统解释的忠实度（Fidelity）长期被忽视，现有方法多聚焦于用户满意度而非模型逻辑还原。传统路径积分（Path Integration, PI）在稀疏二元数据下因基线选择失效，导致归因信号微弱。SPINRec 通过从经验分布中随机采样多个合理用户基线，并选择最大化忠实度指标的解释路径，解决了这一结构性缺陷。该方法在多个基准上确立了新的解释忠实度标准，但其对动态交互场景及内部表征偏差的覆盖仍存疑。

】

---

【Invisible Triggers, Visible Threats! Road-Style Adversarial Creation Attack for Visual 3D Detection in Autonomous Driving ｜路面风格对抗海报生成

作者：Jian Wang、Lijun He、Yixing Yong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.08015)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.08015)

> 视觉三维检测器在自动驾驶中面临物理对抗攻击威胁，但现有方法生成的补丁因纹理突兀易被人工察觉，且单一图案易被针对性防御。本文切入点在于利用生成对抗网络将对抗图案约束为自然路面纹理，解决隐蔽性与有效性的矛盾。通过两阶段策略，先训练通用路面风格生成器，再针对特定场景微调潜向量，实现高隐蔽性的假阳性攻击。该方法在数字与物理环境均验证了有效性，但其白盒假设与单帧静态特性限制了实际黑盒部署的威胁评估。

】

---

【OTI: A Model-free and Visually Interpretable Measure of Image Attackability ｜对象纹理强度（OTI）：模型无关的图像可攻击性度量

研究机构：澳门大学、重庆大学

作者：Jiaming Liang、Haowei Liu、Chi-Man Pun

论文原文见 [arXiv](https://arxiv.org/abs/2601.17536)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17536)

> 对抗样本攻击中，不同图像对扰动的敏感度存在显著差异，但现有度量方法要么依赖模型代理，要么缺乏视觉可解释性，导致在医疗影像等模型不可获取场景下失效。本文切入点在于利用图像自身的语义对象面积与纹理强度，构建一个无需任何模型参与且人类可直接观察的脆弱性指标。具体做法是结合语义分割与Sobel算子计算对象纹理强度（Object Texture Intensity, OTI），以量化图像抵抗中高频扰动的能力。该度量在多种攻击与任务下有效，但其模型无关性是否牺牲了对特定架构（如ViT与CNN）的区分度，仍存疑。

】

---

【Rethinking Saliency Maps: A Cognitive Human Aligned Taxonomy and Evaluation Framework for Explanations ｜参考框架与粒度：显著性图解释的认知对齐分类法

研究机构：以色列特拉维夫大学、美国哈佛大学

作者：Yehonatan Elisha、Seffi Cohen、Oren Barkan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.13081)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13081)

> 视觉显著性图长期面临“解释意图模糊”困境：同一张热力图既可能回答“为何是哈士奇”，也可能被误读为“为何是狗而非猫”。现有保真度指标仅评估单类得分变化，无法区分对比性推理与语义抽象层级，导致方法评估与用户真实需求脱节。本文提出参考框架×粒度（Reference-Frame × Granularity, RFxG）双轴分类法，并设计四个基于概率差的新指标，在10种方法、4种架构、3个数据集上验证了现有指标在对比任务上的系统性失效。该框架填补了评估维度的空白，但其组级标签依赖WordNet层级的主观性，且未证明新指标在密集显著性图上的稳定性优于传统阈值方法。

】

---

【ShapBPT: Image Feature Attributions Using Data-Aware Binary Partition Trees ｜数据感知二元分割树图像特征归因

作者：Muhammad Rashid、Elvio G. Amparore、Enrico Ferrari 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07047)

> 图像分类模型的黑盒决策机制难以通过像素级重要性分数直观还原，传统基于轴对齐网格的Shapley值计算方法因忽略图像形态学结构导致收敛缓慢且定位模糊。ShapBPT通过引入数据感知的二元分割树层级结构替代固定网格，将Shapley系数计算与图像内在形态对齐，从而在保持理论保证的同时显著提升收敛效率。该方法在多个视觉任务上优于现有Shapley类及梯度类解释器，并获20名受试者偏好验证，但其对纹理复杂或抽象图像的泛化能力尚存疑。

】

---

【Theory of Mind for Explainable Human-Robot Interaction ｜心智理论作为可解释人工智能的评估框架

作者：Marie S. Bauer、Julia Gachot、Matthias Kerzel 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.23482)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23482)

> 人机交互（HRI）中的心智理论（Theory of Mind, ToM）旨在通过推断用户心理状态来生成解释，但其长期缺乏对解释与机器人内部推理一致性的技术验证。现有ToM研究多聚焦于用户感知与信任，却忽视了保真度这一XAI核心指标，导致解释可能误导用户。本文提出将ToM视为XAI的一种形式，并采用eValuation XAI (VXAI) 框架的七项标准对现有ToM文献进行系统性审计。该工作揭示了ToM在技术严谨性上的重大缺口，但仅提供了定性合规性检查，未建立量化保真度指标，其结论的泛化性仍存疑。

】
