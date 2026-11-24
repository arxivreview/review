# WACV2026 · 可信AI与安全隐私方向论文汇编

> 本方向共 13 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AD$^2$: Analysis and Detection of Adversarial Threats in Visual Perception for End-to-End Autonomous Driving Systems ｜端到端自动驾驶视觉感知对抗检测

研究机构：印度理工学院卡拉格普尔分校

作者：Ishan Sahu、Somnath Hazra、Somak Aditya 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.10160)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.10160)

> 导读 端到端自动驾驶系统通过联合优化感知与规划，消除了模块化架构中的误差累积，但引入了黑盒特性，使得传感器层面的微小扰动可能引发控制回路的级联失效。现有研究多聚焦于单帧图像分类或检测模块的对抗鲁棒性，缺乏对闭环驾驶过程中扰动传播机制的系统评估，且防御手段往往依赖访问模型内部潜变量，难以部署。本文切入点在于利用多相机空间重叠与时序连贯性，构建一个无需修改驾驶智能体、仅基于外部输入流的轻量级检测器。该方法通过Transformer建模时空一致性，在CARLA仿真中实现了1.0的检测准确率，但其有效性局限于仿真环境下的特定攻击类型，真实物理噪声下的泛化能力存疑。

】

---

【AD: Analysis and Detection of Adversarial Threats in Visual Perception for End-to-End Autonomous Driving Systems ｜端到端自动驾驶系统的对抗威胁分析与检测

研究机构：印度理工学院卡拉格普尔分校

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_66516417)

> 导读 端到端自动驾驶系统直接映射传感器输入至控制信号，其内部隐式特征耦合使得传统基于中间输出的防御失效，且闭环特性导致扰动引发级联错误。现有研究多聚焦于模块化检测器的局部对抗补丁，缺乏对信号级干扰（声学、电磁）在闭环驾驶中影响的系统评估。本文通过复现三类黑盒攻击验证了Transfuser与Interfuser的脆弱性，并提出基于时空一致性的轻量级外部检测器AD²。该方法在CARLA仿真中实现了1.0的检测准确率与0.16ms的推理延迟，但缺乏真实物理环境下的鲁棒性验证。

】

---

【AFL-PRF: Adaptive Federated Learning for Low-Quality Data: Enhancing Performance, Robustness, and Fairness ｜自适应联邦学习框架

研究机构：美国东北大学、美国佐治亚大学

作者：Pinrui Yu、Yiming Xie、Longtian Ye 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_72efb9104b8e)

> 联邦学习在对抗攻击与极端非独立同分布（Non-IID）数据共存时，现有鲁棒聚合方法往往将良性低质量客户端误判为恶意节点，导致模型精度与公平性双降。本文切入点在于区分“恶意偏差”与“良性异质性”，通过自适应加权与选择性裁剪实现鲁棒、公平与精度的联合优化。具体做法是引入指数动态加权、权重更新散度（WUD）分数及全连接层选择性裁剪。该框架在CIFAR-10上以71.77%的准确率超越了Krum等基线，但其绝对性能仍低于领域内针对纯鲁棒性的SOTA方法，且缺乏形式化隐私保证。

】

---

【Lose Your Self (LoYS): An Adversarial Entropy-based Unsupervised Approach for Model Debiasing ｜对抗熵正则化无监督去偏

研究机构：美国麻省理工学院

作者：Vito Paolo Pastore、Massimiliano Ciranni、Vittorio Murino

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83dfc406fde8)

> 图像分类模型在训练数据存在强虚假相关时，倾向于学习捷径特征而非因果特征，导致分布外泛化崩溃。现有无监督去偏方法多依赖直接识别偏差冲突样本进行重加权，但在偏差对齐样本占比极高（如99.5%）的场景下，这种识别极易受模型自身偏差污染而失效。本文提出LoYS，通过弱预训练“软偏差教师”生成伪标签，并引入对抗熵最大化机制，强制目标编码器学习低偏差相关特征。该方法在真实世界基准上优于传统基线，但在合成强偏差场景下性能显著低于最新几何干预方法，且未解决多属性偏差转移的根本问题。

】

---

【Marshaled Learning: Bridging Large Neural Networks with Memory-Constrained Trusted Execution Environments in Federated Learning ｜内存受限TEE下的联邦学习端到端训练

作者：Shiwei Ding、Xiaoyong Yuan、Zhenlin Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f0b2ea05677)

> 联邦学习（Federated Learning, FL）旨在解决数据隐私与集中式存储的矛盾，但现有隐私保护方案如差分隐私（Differential Privacy, DP）和同态加密（Homomorphic Encryption, HE）往往以牺牲模型效用或引入巨大计算开销为代价。可信执行环境（Trusted Execution Environment, TEE）通过硬件隔离提供强隐私保证且保持原生精度，但其有限的内存容量（如Intel SGX仅128 MB）阻碍了大型状态-of-the-art（SOTA）神经网络的部署。本文提出Marshaled Learning框架，通过将大模型分割为子网并分布在多个客户端TEE中，实现跨客户端的端到端反向传播，同时引入动态知识传播机制以缓解数据异质性与慢节点问题。该方案在真实Azure机密虚拟机上验证了可行性，但仅针对诚实但好奇假设，未涵盖侧信道攻击等更严苛的威胁模型。

】

---

【Mitigating Backdoor Attacks via Trigger Reconstruction and Model Hardening ｜基于特征空间重构的后门缓解

研究机构：美国犹他大学、美国普渡大学

作者：Guanhong Tao、Siyuan Cheng、Guangyu Shen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_656ca0c1d9aa)

> 后门防御的核心困境在于语义触发器与正常特征的高度纠缠，导致基于像素匹配或神经元隔离的传统方法失效。MARTINI 通过构建特征空间到像素空间的解码器，利用区域变换层在抽象特征层面重构恶意样本，从而绕过了像素级分离的假设限制。该方法将触发器反转从“恢复像素”转变为“生成等效恶意输入”，并通过迭代重训练实现模型加固。尽管在多种攻击下显著降低了攻击成功率，但其对特定骨干网络与预训练编码器的依赖，以及缺乏对量化模型鲁棒性的验证，限制了其在复杂部署环境中的通用性。

】

---

【Personalized Image Privacy Advisors via Federated Daisy-Chaining ｜个性化图像隐私顾问的联邦链式聚合

作者：Sourasekhar Banerjee、Vengateswaran Subramaniam、Debaditya Roy 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3aca00d259ce)

> 图像隐私感知具有高度主观性，传统集中式训练需上传原始数据，而标准联邦学习（FL）难以处理标注者间偏好差异与数据稀缺。现有个性化联邦方法缺乏对簇内数据量不均的细粒度处理，本文提出CFedDC框架，结合模型权重聚类与链式知识传递，并设计轻量级PIONet模型。该方法在DIPA2数据集上优于FedAvg等基线，但其隐私保护仅依赖架构隔离，未提供形式化保证，且聚类稳定性在早期训练中的表现存疑。

】

---

【SAFER-AiD: Saccade-Assisted Foveal-peripheral vision Enhanced Reconstruction for Adversarial Defense ｜基于生物视觉机制的对抗防御框架

研究机构：美国雪城大学、美国石溪大学

作者：Jiayang Liu、Daniel Tso、Yiming Bu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08761)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08761)

> 对抗鲁棒性研究旨在解决深度学习模型对微小输入扰动的脆弱性，传统对抗训练虽能提升白盒鲁棒性，但计算成本高昂且需针对特定攻击模型重复训练，难以应对黑盒与迁移攻击。本文切入点在于利用生物视觉系统的固有鲁棒性机制，通过非均匀稀疏采样与预测重建替代昂贵的模型优化。SAFER-AiD 框架整合了中央凹-周边采样、扫视眼动与皮层填充机制，作为即插即用的预处理模块，无需重训下游分类器。该方法在 ImageNet 黑盒攻击下显著提升了多种架构的鲁棒性，但其缺乏形式化保证且依赖强化学习策略的泛化能力，在强白盒攻击下的有效性仍存疑。

】

---

【SD-CSFL: A Synthetic Data-Driven Conformity Scoring Framework for Robust Federated Learning ｜合成数据驱动的一致性评分框架

研究机构：英国兰卡斯特大学

作者：Ebtisaam Alharbi、Abdulrahman Kerim、Leandro Soriano Marcolino 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fc704fe5873)

> 联邦学习（FL）中服务器无法审计本地数据，导致梯度操纵与后门攻击在数据非独立同分布（Non-IID）环境下难以被现有防御机制统一拦截。鲁棒聚合对良性方差敏感，聚类方法易被自适应攻击绕过，而依赖客户端数据的检测策略违背隐私原则。本文提出SD-CSFL，利用独立于客户端数据的合成校准集计算基于熵的非一致性分数，结合自适应百分位阈值实现统一防御。该框架在隐私保护约束下提升了检测鲁棒性，但其合成数据生成成本与极端异质性下的检测上限仍存疑。

】

---

【Towards Reliable Test-Time Adaptation: Style Invariance as a Correctness Likelihood ｜风格不变性作为正确性似然

研究机构：韩国科学技术院

作者：Gilhyun Nam、Taewon Kim、Joonhyun Jeong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07390)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07390)

> 测试时适应（Test-Time Adaptation, TTA）旨在让部署模型利用无标签测试数据在线调整以应对分布偏移，但这一过程往往导致预测置信度与真实正确率严重脱节。现有校准方法依赖固定模型或静态分布假设，无法处理TTA中模型状态与数据分布同时动态变化的场景。SICL通过测量原始预测与风格扰动变体预测的一致性来估计实例级正确性似然，无需反向传播即可实现动态校准。该方法在动态流场景下将期望校准误差（ECE）平均降低13.0个百分点，但其有效性高度依赖风格-内容解耦假设，在模型崩溃边界下的鲁棒性仍存疑。

】

---

【TRACE: Confounder-free Adversarial Fine-tuning for Robust Object Detection ｜因果混杂消除的对抗微调

作者：Wonho Lee、Jisu Lee、Hyunsik Na 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8a8fed501f71)

> 物理对抗补丁攻击在多目标检测场景中因位置、旋转等空间变换产生混杂效应，导致传统像素级防御泛化性不足。现有方法或依赖高延迟的认证机制，或陷入对特定补丁分布的过拟合，难以应对自适应攻击。本文提出 TRACE，将 IV 回归引入特征空间以消除混杂因子，实现因果特征学习。该方法在 YOLO 系列模型上展现了优于像素级微调的鲁棒性，但其缺乏与 SOTA 生成式防御的直接对比，且未验证在更复杂 3D 场景下的有效性。

】

---

【UltraClean: A Simple Framework to Train Robust Neural Networks against Backdoor Attacks ｜基于去噪敏感度差异的后门样本筛选框架

研究机构：美国塔夫茨大学

作者：Bingyin Zhao、Yingjie Lao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aa9955b23a5d)

> 后门攻击通过投毒训练数据植入隐蔽恶意行为，其中干净标签攻击因标签一致而难以被传统防御识别。现有频谱或梯度方法在干净标签场景下失效，本文利用深度神经网络前向传播中的错误放大效应，结合非局部均值与中值滤波生成图像变体，计算模型输出差异以筛选投毒样本。该方法在CIFAR-10上将LCBD攻击的攻击成功率降至1.59%，同时保持97.40%的清洁准确率。其核心假设是触发器噪声在模型响应中可被线性放大，但论文未验证该假设在量化模型或极端低投毒率下的鲁棒性。

】

---

【Uncertainty-Aware Subset Selection for Robust Visual Explainability under Distribution Shifts ｜不确定性感知子集选择下的鲁棒视觉归因

研究机构：印度理工学院孟买分校

作者：Madhav Gupta、Vishak Prasad C、Ganesh Ramakrishnan

论文原文见 [arXiv](https://arxiv.org/abs/2512.08445)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.08445)

> 视觉归因旨在定位模型预测的责任区域，但现有子集选择方法在分布偏移（OOD）下常产生冗余且不稳定的解释。本文切入点在于将自适应权重扰动产生的不确定性信号嵌入子模优化目标，以筛选出在参数扰动下保持稳定的区域。该方法无需额外训练或辅助模型，仅通过推理时的轻量级扰动实现。其价值在于显著缩小了ID与OOD间的归因性能差距，但Deletion指标在部分场景下的恶化暴露了稳定性与忠实度间的潜在权衡。

】
