# CVPR2026 · 可信AI与安全隐私方向论文汇编

> 本方向共 50 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A combination of noise and bilateral filters achieve supralinear and scalable adversarial robustness in CNNs ｜噪声与双边滤波组合实现超线性对抗鲁棒性

作者：Nicolas Stalder、Benjamin F. Grewe、Matteo Saponati 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.02267)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.02267)

> 深度学习模型在部署中面临微小像素扰动即可导致误判的对抗攻击威胁，而主流防御手段对抗训练计算开销巨大且易过拟合特定攻击类型。现有独立使用的噪声注入或图像滤波方法虽成本低，但各自仅能防御特定几何形态的扰动，无法覆盖广泛的攻击空间。本文切入点在于从几何体积缩减角度证明噪声与滤波机制互补，提出一种先加高斯噪声再进行多次双边滤波的轻量级预处理器，并将其嵌入对抗训练流程。该方案以约35%的训练FLOPs超越了现有SOTA模型的鲁棒精度，但其理论假设基于理想化滤波器，且缺乏针对最强自适应黑盒攻击的验证。

】

---

【A Unified Perspective on Adversarial Membership Manipulation in Vision Models ｜对抗成员操纵：视觉模型成员推断的鲁棒性审计

研究机构：新加坡国立大学、法国国家科学研究中心

作者：Ruize Gao、Kaiwen Zhou、Yongqiang Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02780)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02780)

> 成员推断攻击（Membership Inference Attack, MIA）旨在量化模型对训练数据的记忆强度，但现有审计协议隐含假设查询输入是诚实的，未考虑输入端对抗扰动。当攻击者通过微小扰动将非成员样本推入“成员”区域时，基于置信度的MIA会产生系统性误判，导致版权验证与合规审计失效。本文提出成员伪造攻击（MFA）与基于梯度几何的检测框架，揭示了MIA在输入空间中的脆弱性。该工作填补了MIA对抗鲁棒性的空白，但其检测机制依赖白盒梯度访问，在黑盒场景下的有效性存疑。

】

---

【AdvFM: Lookahead Flow-Matching Velocity-Field Attacks for Imperceptible and Transferable Adversarial Examples ｜流匹配速度场攻击

研究机构：哈尔滨工业大学、中国科学院

作者：Runze Liu、Zeyue Wang、Fanghui Sun 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7fc35e44b1c9)

> 生成式对抗攻击在扩散模型中受限于随机噪声注入导致的梯度方差增大，削弱了跨模型迁移性与抗净化防御能力。本文指出扩散去噪-重噪机制会衰减对抗信号并引入离流形分量，而流匹配（Flow Matching）的确定性常微分方程（ODE）动力学可避免此问题。通过直接扰动速度场并引入前瞻（Lookahead）两点目标，AdvFM 实现了更稳定的梯度对齐与流形切向扰动。该方法在对抗训练模型上取得 98.53% 攻击成功率，但在纯迁移场景下未超越像素空间 SOTA，其计算效率优势缺乏量化证据。

】

---

【Align Once to Explain: Feature Alignment for Scalable B-cosification of Foundational Vision Transformers ｜一次性特征对齐实现视觉基础模型内在可解释性

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3dcca1d65360)

> 大规模视觉基础模型在医疗、金融等高风险场景的部署受阻于决策过程的不透明性，传统后验归因方法虽能生成解释，但往往存在噪声大且与模型真实计算逻辑脱节的问题。ALOE 提出了一种无需标签、仅需一次性特征对齐的转换方案，将预训练 ViT 骨干直接改造为内在可解释的 B-cos 架构。该方法以极低的计算和数据成本，在保留基础模型通用泛化能力的同时，提供了由架构保证的忠实解释。其核心价值在于将解释成本从推理阶段摊销至训练阶段，但当前验证主要局限于分类与定位任务，在复杂多模态交互中的泛化边界尚待厘清。

】

---

【AntiStyler: Defending Object Detection Models Against Adversarial Patch Attacks Using Style Removal ｜风格移除防御对抗补丁

研究机构：以色列内盖夫本-古里安大学

作者：Idan Yankelev、Edita Grolman、Yarin Yerushalmi Levi 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b14a1f17c4d6)

> 物理对抗补丁防御长期受困于鲁棒性与实时性的权衡，现有后训练方法要么牺牲干净图像性能，要么因计算开销无法满足自动驾驶等场景的帧率要求。AntiStyler 抓住了对抗补丁在特征空间中呈现“随机风格”这一被忽略的分布差异，将风格迁移改造为风格移除，通过最大化风格损失实现零样本掩码。该方法在无需重训练的前提下，以 92.7 ms 的推理延迟实现了 10-12 FPS 的实时处理能力，但其对 Transformer 架构的增益有限，且依赖预训练 CNN 的纹理敏感性，在复杂 3D 渲染攻击下的鲁棒性边界尚待明确。

】

---

【Batman: Benign Knowledge Alignment Through Malicious Null Space in Federated Backdoor Attack ｜联邦后门攻击中的良性知识对齐与恶意零空间解耦

研究机构：武汉大学、新加坡南洋理工大学

作者：Wenwen He、Wenke Huang、Yiyang Fang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b9d7b14cc541)

> 联邦学习后门攻击面临隐蔽性与有效性的根本矛盾：现有方法在共享参数空间内对齐良性知识时，要么因对齐不足导致恶意更新易被检测，要么因过度对齐削弱攻击强度。本文指出这一困境的根源在于良性与恶意知识共享同一参数空间，对齐操作必然相互干扰。Batman 通过 SVD 提取恶意主成分并构建其正交补空间（恶意零空间），将良性对齐约束在该零空间内，实现了攻击有效性与统计隐蔽性的解耦。该方法在四个基准数据集上验证了强攻击性能，但其静态层选择策略在应对自适应防御时的鲁棒性尚存疑。

】

---

【Bias In, Bias Out? Finding Unbiased Subnetworks in Vanilla Models ｜无偏子网络提取

作者：Ivan Luiz De Moura Matos、Abdel Djalil Sad Saoud、Ekaterina Iakovleva 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05582)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05582)

> 深度学习模型在真实数据中常依赖虚假相关而非因果特征，导致分布外场景下泛化能力脆弱，偏差缓解旨在抑制这种捷径学习倾向。现有去偏方法多依赖显式标注或高昂的重训练成本，难以在大规模部署中落地，本文切入点在于假设标准训练模型内部已存在无偏子结构，通过结构化剪枝直接提取。具体做法是学习可训练掩码移除与偏差强相关的神经元，无需修改原始权重或访问无偏数据。该方法在免微调设定下接近最先进水平，但其有效性严格依赖于原始模型中无偏子网络的存在性，且对多属性交叉偏差的解耦能力有限。

】

---

【CamPI: Physical Adversarial Examples through Camera Power Signal Injection ｜相机电源信号注入攻击

研究机构：浙江大学、香港理工大学

作者：Yanze Ren、Mingyuan Lv、Qinhong Jiang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3db57321b151)

> 物理对抗攻击长期受限于“可见性”与“物理接近”两大瓶颈，补丁与光学投影虽能诱导误判，但易被人工察觉且需直接视线。本文切入相机电源这一电气接口，通过注入调制信号生成不可见的结构化条纹扰动，绕开了视觉域的物理约束。其核心在于构建可微仿真模型，将信号参数优化转化为梯度可导的端到端问题。该工作验证了电气域攻击的可行性，但仿真模型对特定相机硬件参数的强依赖，限制了其跨设备泛化能力的评估。

】

---

【CARLoS: Retrieval via Concise Assessment Representation of LoRAs at Scale ｜LoRA行为表征与检索

研究机构：以色列特拉维夫大学

作者：Shahar Sarfaty、Adi Haviv、Uri Hacohen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.08826)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.08826)

> 生成式AI生态中LoRA适配器数量激增但缺乏标准化描述，导致用户选择依赖试错且平台难以筛查侵权风险。现有基于文本元数据的检索方法因描述稀疏、主观且与视觉效果脱节而失效。本文提出CARLoS，通过量化LoRA在CLIP空间中的语义差分向量，构建包含方向、强度与一致性的三元组表征，实现无需元数据的精准检索。该框架将法律归因中的“实质性”与“自愿性”映射为可计算指标，但在细粒度空间构图与跨模态泛化上仍受限于CLIP编码器的固有弱点。

】

---

【Computation and Communication Efficient Federated Unlearning via On-server Gradient Conflict Mitigation and Expression ｜联邦遗忘中的服务器端梯度冲突消解

研究机构：澳大利亚悉尼大学、爱尔兰都柏林圣三一大学

作者：Minh-Duong Nguyen、Senura Hansaja、Le-Tuan Nguyen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13795)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13795)

> 联邦遗忘（Federated Unlearning, FUL）旨在从已训练的全局模型中移除特定客户端的数据贡献，以响应数据保护法规的“被遗忘权”。现有近似遗忘方法因无法访问遗忘集数据或需反复识别冲突子网，导致计算与通信开销高昂且遗忘效率低下。FOUL通过“学习即遗忘”阶段解耦因果与非因果特征，并在服务器端执行无数据访问的梯度匹配，实现了高效且低成本的客户端级遗忘。该方法在域泛化基准上显著优于重训练基线，但其对因果结构假设的依赖及在极端非独立同分布（Non-IID）场景下的泛化能力仍存疑。

】

---

【Decoupling Defense Strategies for Robust Image Watermarking ｜解耦防御策略下的鲁棒图像水印

研究机构：清华大学、澳大利亚国立大学

作者：Jiahui Chen、Zehang Deng、Zeyu Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20053)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20053)

> 深度神经网络图像水印旨在解决AI生成内容（AIGC）在分发过程中的所有权验证与溯源难题，其核心在于嵌入隐藏信号并抵御各类攻击。现有主流方法依赖联合对抗训练（JAT）模拟失真，但面对扩散模型再生与高级对抗攻击时，JAT导致干净精度下降且鲁棒性提升有限。本文提出AdvMark，通过两阶段解耦微调，将编码器对抗微调与直接图像优化分离，以打破精度-鲁棒性权衡。该框架在抗再生与对抗攻击上显著优于基线，但其对未知攻击变体的泛化能力仍存疑。

】

---

【Domain-Skewed Federated Learning with Feature Decoupling and Calibration ｜域偏斜联邦学习中的特征解耦与校准

研究机构：澳大利亚伍伦贡大学、新加坡管理大学

作者：Huan Wang、Jun Shen、Jun Yan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14238)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14238)

> 域偏斜联邦学习旨在解决客户端数据源自不同域但类别分布一致时，全局模型泛化能力退化的问题。现有方法多采用“消除”域偏差策略，却因丢弃与域特征纠缠的类相关信息而损失判别力。本文提出F2DC，通过解耦并校准域相关特征，在保留有用线索的同时抑制域偏差。该方法在三个多域数据集上显著优于基线，但其对同步通信与诚实客户端的假设限制了其在复杂对抗环境下的适用性。

】

---

【Eliminate Distance Differences Induced by Backdoor Attacks: Layer-Selective Training and Clipping to Mask Backdoor Models ｜层选择性联邦学习后门攻击

研究机构：北京交通大学、清华大学

作者：Xuzeng Li、Tao Zhang、Xiangyun Tang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10b11d2d4b8a)

> 联邦学习（FL）中的后门攻击长期面临隐蔽性与有效性的双重约束，现有优化触发器方法虽提升了攻击成功率，却因在投毒初期产生显著的模型距离差异而极易被距离类防御机制捕获。LaySelFL 切入这一盲区，指出不同模型层对后门注入的贡献存在异质性，通过仅攻击敏感层并裁剪非敏感层来消除距离信号。该方法结合层敏感性评估、约束训练与目标裁剪，使传统攻击在保持高攻击成功率的同时规避了多种主流防御。其价值在于揭示了距离防御的结构性漏洞，但静态层选择策略在面对自适应防御时的鲁棒性存疑。

】

---

【Evidential Neural Radiance Fields ｜证据神经辐射场

研究机构：美国耶鲁大学

作者：Ruxiao Duan、Alex Wong

论文原文见 [arXiv](https://arxiv.org/abs/2602.23574)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23574)

> 神经辐射场（Neural Radiance Fields, NeRFs）在三维场景重建中缺乏对预测不确定性的量化，阻碍了其在自动驾驶等安全关键领域的部署。现有方法要么仅能捕捉偶然不确定性（Aleatoric Uncertainty, AU）而忽略认知不确定性（Epistemic Uncertainty, EU），要么依赖多模型集成或采样导致推理效率低下。本文提出证据神经辐射场，通过将预测均值与方差视为随机变量并引入正态逆伽马（Normal-Inverse-Gamma, NIG）分布，实现单次前向传播同时输出AU与EU。该方法在标准化基准上实现了优于集成方法的渲染保真度与不确定性估计质量，但其对体密度确定性的假设限制了空间不确定性的建模能力。

】

---

【Evidential Transformation Network: Turning Pretrained Models into Evidential Models for Post-hoc Uncertainty Estimation ｜证据变换网络

研究机构：韩国高丽大学

作者：Yongchan Chun、Chanhee Park、Jeongho Yoon 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08627)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08627)

> 预训练模型在部署时缺乏可靠的置信度量化能力，而深度集成与蒙特卡洛Dropout等高保真方法因计算开销巨大难以落地。本文切入点在于利用证据深度学习（EDL）的单步推理特性，但避免从头训练或大规模微调导致的过拟合与表征破坏。ETN通过在Logit空间引入样本依赖的仿射变换，将预训练模型的输出直接映射为狄利克雷分布参数，实现了轻量级的后置不确定性估计。该方法在保持精度的同时显著提升了OOD检测性能，但其对变分分布的依赖及在极端高维场景下的先验敏感性仍存疑。

】

---

【FairLLaVA: Fairness-Aware Parameter-Efficient Fine-Tuning for Large Vision-Language Assistants ｜医疗多模态大模型中的人口统计学捷径抑制

研究机构：美国纽约州立大学布法罗分校

作者：Mahesh Bhosale、Abdul Wasi、Shantam Srivastava 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.26008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26008)

> 医疗多模态大模型（MLLMs）在生成放射学报告时，常因图像中隐含的人口统计学特征（如种族、性别）产生跨群体性能差异，而非显性文本偏见。现有基于频率重加权或对抗分类器的去偏方法，在医疗场景下要么忽略交叉属性依赖，要么引发临床知识灾难性遗忘。本文切入点在于将公平性约束从输出层前移至表征层，通过最小化隐藏层状态与敏感属性间的互信息，实现人口统计学不变的特征学习。该方法以轻量级插件形式嵌入低秩适配器（LoRA）微调流程，在保持整体生成质量的同时缩小群体差距，但其有效性依赖于对图像中泄露人口统计学信号的准确探测，且未验证在极端数据不平衡下的鲁棒性。

】

---

【FeatureFool: Zero-Query Fooling of Video Models via Feature Map ｜视频零查询特征图对抗攻击

研究机构：清华大学、深圳大学

作者：Duoxun Tang、Xi Xiao、Guangwu Hu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.18362)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18362)

> 视频对抗攻击长期受困于高查询成本与帧采样策略的不确定性，导致迭代式黑盒攻击在视频大模型上耗时数小时且难以规模化。现有零查询方法仅覆盖图像域，无法处理视频时序维度带来的特征空间漂移。本文提出 FeatureFool，通过光流定位关键帧并提取特征图广播至全视频，实现无查询的视频对抗攻击。该方法在 C3D 和 I3D 上取得超过 70% 的攻击成功率，但跨架构迁移的鲁棒性边界尚未完全厘清。

】

---

【FedAlign: Differentially Private Distribution Alignment for Non-IID Federated Learning ｜联邦对齐：差分隐私下的非独立同分布优化

研究机构：湖南大学

作者：Peng Wu、Jiapeng Zhang、Yingjie Song 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8fcb5bebadbb)

> 联邦学习在非独立同分布（Non-IID）数据下面临收敛缓慢与隐私泄露加剧的双重困境，现有差分隐私（DP）方法仅通过梯度加噪保护隐私，却忽视了数据异质性对模型效用的根本性破坏。FedAlign 通过客户端统计矩对齐机制，在隐私预算约束下同步缓解分布偏差与隐私风险。该方法将均值、方差、偏度、峰度作为对齐目标，实现了收敛加速与精度提升。其理论贡献在于建立了分布散度与梯度不一致性的定量联系，但实验部分缺乏具体数值支撑，且未验证对拜占庭攻击的鲁棒性。

】

---

【FedMOP: Achieving Enhanced Privacy and Performance in Federated Learning via Momentum Orthogonal Projection ｜动量正交投影联邦学习

研究机构：中南大学、商汤

作者：Yunlong Zhao、Xiaoheng Deng、Hongyan Xu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c39bdb21058d)

> 联邦学习（Federated Learning, FL）面临隐私保护与模型效用互斥的结构性矛盾，现有防御机制如差分隐私（Differential Privacy, DP）通过噪声注入换取安全，却导致精度显著下降。本文切入点在于利用初始化偏移的正交性，将性能优化与隐私保护解耦于不同维度。FedMOP通过动量演化将可计算的静态偏移转化为不可逆的动态轨迹，在提升收敛速度的同时阻断梯度反演。该方法在CIFAR-10上实现了92%的精度，但其隐私指标数值与摘要结论存在逻辑冲突，需审慎评估其实际安全边界。

】

---

【FedRAC: Rolling Submodel Allocation for Collaborative Fairness in Federated Learning ｜协作公平联邦学习中的滚动子模型分配

研究机构：厦门大学

作者：Zihui Wang、Yuhang Fu、Mengmeng Du 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0bb7b422fb7d)

> 联邦学习中的协作公平旨在通过差异化奖励激励客户端持续参与，但现有方法因声誉静态化或模型分配不一致导致全局精度受损。FedRAC 指出早期低贡献客户端被低估是性能瓶颈，通过动态声誉计算与滚动子模型分配实现公平与精度的平衡。该方法在 MNIST 上取得 96.444% 准确率，验证了动态机制的有效性，但其对客户端始终在线的假设限制了在动态参与场景下的适用性。

】

---

【FedSDR: Federated Graph Learning with Structural Noise Detection and Reconstruction ｜联邦图学习中的结构噪声检测与重构

研究机构：武汉大学

作者：Jiaqi Liu、Zihan Tan、Guancheng Wan 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ce89b1ed3aa1)

> 联邦图学习（Federated Graph Learning, FGL）旨在解决分布式图数据在隐私约束下的协作训练难题，但现有方法多聚焦于对抗攻击或自然异质性，忽视了数据收集与存储中产生的随机结构噪声。这类非恶意噪声（如缺失边与虚假边）会伪装成良性异质性，导致消息传递机制失效并引发全局模型的知识不一致。本文提出FedSDR，通过谱域保真度指标检测受损客户端，并利用全局模型特征相似度修复局部图结构。该方法在含噪声场景下显著优于现有鲁棒联邦学习算法，但其对干净数据下的性能增益及隐私预算消耗未作深入探讨。

】

---

【FedSST: Rethinking Fair Federated Graph Learning under Structural Shift ｜结构感知自适应联邦图学习

研究机构：武汉大学

作者：Dingyi Zhao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7e215af3305)

> 联邦图学习（Federated Graph Learning, FGL）在跨域场景下面临拓扑异质性导致的泛化公平性危机，即优势客户端主导全局模型，致使弱势客户端性能受损。现有方法多聚焦于提升整体精度或处理统计异质性，缺乏针对结构偏差的标准化量化指标与差异化资源分配机制。本文提出FedSST框架，通过探针图生成结构画像信号，驱动本地训练强度分配与服务端加权聚合的双向自适应优化。该方法在跨域基准上显著降低了客户端性能标准差，但绝对精度受限于跨域数据稀释，且未涉及隐私保护下的信号泄露问题。

】

---

【Fractal Camouflage: A Bio-Inspired Approach for Multi-Scale Adversarial Attacks in the Infrared Domain ｜分形伪装：红外域多尺度对抗攻击

作者：Chengyin Hu、Xin Wang、Rui Qiu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_edbf05790942)

> 红外行人检测系统面临物理对抗补丁攻击时，现有方法因固定尺度扰动无法适应目标距离变化，导致攻击成功率随距离波动剧烈。本文切入点在于利用分形几何的自相似性，生成能同时干扰检测器特征金字塔各层级的多尺度扰动。通过H型分形递归结构与粒子群优化（PSO）结合，在无需梯度的黑盒设定下实现物理鲁棒性。该方法在物理实验中实现了97.54%的平均攻击成功率，但其在非刚性形变下的长期稳定性及跨模态泛化能力仍存疑。

】

---

【From Softmax to Dirichlet: Evidential Learning for Semi-supervised Semantic Segmentation ｜从Softmax到Dirichlet：基于证据学习的半监督语义分割

研究机构：中国科学技术大学、清华大学

作者：Huayu Mai、Rui Sun、Yujia Chen 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a948151a1071)

> 半监督语义分割的核心瓶颈在于伪标签的可靠性，现有方法依赖Softmax分数筛选，但神经网络固有的过度自信导致高置信度预测常伴随错误标签。本文切入点在于将不确定性估计从点估计升级为分布估计，通过狄利特分布显式建模类别概率的后验分布。具体做法是引入超证据提取器解耦排他与集体证据，计算更鲁棒的不确定性指标以筛选伪标签。该方法在低标注比例下性能与当前SOTA持平，但其在复杂分布偏移下的泛化能力尚未得到充分验证。

】

---

【Hidden Monotonicity: Explaining Deep Neural Networks via their DC Decomposition ｜基于凸差分解的单调网络归因方法

研究机构：荷兰特文特大学

作者：Jakob Paul Zimmermann、Georg Loho

论文原文见 [arXiv](https://arxiv.org/abs/2601.07700)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07700)

> 深度学习模型的黑盒特性阻碍了高风险场景下的信任构建，而传统梯度归因方法因信号抵消与噪声累积导致解释失真。现有方案要么牺牲表达力换取单调性，要么在深层网络中面临数值爆炸，无法直接应用于预训练模型。本文提出将任意ReLU网络无损分解为两个单调凸子网络，并通过数值稳定化技术保留预激活信息，从而在不重训练的前提下提升归因质量。该方法在VGG16上实现了定位与忠实度指标的SOTA，但其对残差网络结构的增益有限，且未验证在Transformer架构上的适用性。

】

---

【Improving Adversarial Transferability with Local Perturbation Augmentation ｜局部扰动增强攻击

研究机构：重庆大学

作者：Jian-Xun Mi、Xuanhui Zhong、Weisheng Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1d75b56cdbc5)

> 可迁移对抗攻击旨在利用代理模型生成的扰动误导未知目标模型，核心挑战在于迭代优化易使扰动过拟合于代理模型的局部尖锐极值，导致跨模型迁移成功率低下。现有主流方法多依赖全局梯度更新或随机邻域采样，难以有效平衡探索多样性与方向稳定性。本文提出局部扰动增强攻击（LPAA），通过随机掩码构建局部子空间并引入增强系数扩展搜索范围，结合特定初始化策略以提升迁移性。该方法在理论上优于随机采样，但缺乏与最新生成式及频谱感知方法的直接数值对比，其实际性能边界存疑。

】

---

【Improving Sparse Autoencoder with Dynamic Attention ｜基于动态稀疏注意力的稀疏自编码器

研究机构：深圳大学

作者：Dongsheng Wang、Jinsen Zhang、Dawei Su 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14925)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14925)

> 大语言模型中神经元的多义性源于叠加现象，阻碍了机制可解释性。现有稀疏自编码器（Sparse Autoencoder, SAE）依赖固定超参数或正则化系数控制稀疏度，导致特征收缩或死特征问题。本文提出基于交叉注意力与Sparsemax函数的架构，实现样本级动态稀疏度选择。该方法在重构误差上优于固定K值基线，但其跨模态泛化能力与因果有效性仍缺乏严格验证。

】

---

【Interpretable and Steerable Concept Bottleneck Sparse Autoencoders ｜概念瓶颈稀疏自编码器

研究机构：美国加州大学圣迭戈分校、美国劳伦斯利弗莫尔国家实验室

作者：Akshay Kulkarni、Tsui-Wei Weng、Vivek Narayanaswamy 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.10805)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.10805)

> 稀疏自编码器（Sparse Autoencoder, SAE）旨在将大模型中密集且多义的激活分解为稀疏、单义的潜在特征，以支持机制可解释性与模型引导。然而，无监督训练无法保证特征既具备人类可解释性，又具备因果可控性，且常遗漏用户指定的特定概念。本文提出CB-SAE，通过剪枝低效神经元并联合训练概念瓶颈自编码器，统一了无监督发现与监督控制。该框架在视觉-语言模型中显著提升了特征质量，但其对重构保真度的补偿机制及跨模态泛化能力仍存疑。

】

---

【Language Models Can Explain Visual Features via Steering ｜视觉特征因果解释：基于转向的自动解释框架

研究机构：西班牙巴塞罗那超级计算中心

作者：Javier Ferrando、Enrique Lopez-Cuena、Pablo Agustin Martin-Torres 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22593)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22593)

> 导读 视觉模型中稀疏自编码器（Sparse Autoencoder, SAE）提取的特征数量庞大，但传统基于输入图像的解释方法存在严重的上下文偏差，且依赖大规模预定义测试集。本文提出通过因果干预而非统计相关来生成解释，利用视觉语言模型（Vision-Language Model, VLM）的语言能力，在空图像上注入SAE特征向量，迫使模型“描述”其看到的视觉概念。该方法以单次前向传播实现可扩展解释，并引入混合策略提升质量。其价值在于提供了不依赖输入分布的因果解释轴，但解释质量仍受限于语言模型规模，且未完全解决特征间交互导致的解释歧义。

】

---

【Learning Mutual View Information Graph for Adaptive Adversarial Collaborative Perception ｜协同感知中的自适应特征级攻击

研究机构：香港城市大学

作者：Yihang Tao、Senkang Hu、Haonan An 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19596)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19596)

> 导读 协同感知（Collaborative Perception, CP）通过车端数据共享突破单车视野限制，但共享通道引入了内部攻击面，现有防御依赖静态共识验证，难以应对具备时序与空间策略优化的自适应攻击。本文指出防御系统交换的占用图与特征图隐含了“集体不确定性”信息，攻击者可利用此漏洞知识进行精准打击。作者提出 MVIG 框架，将多车视角关系建模为图结构，通过时序图学习预测脆弱区域并优化攻击时机。该方法在仿真环境中显著降低了防御成功率，但其在真实通信延迟与物理环境下的泛化能力尚待验证。

】

---

【Logit-Margin Repulsion for Backdoor Defense ｜对数间隔排斥

研究机构：中国科学技术大学

作者：Zhiguo Yang、Dongsheng Xu、Ruizhi Zhong 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_913cdbf8a3df)

> 后门攻击的核心威胁在于模型在干净输入上保持正常，仅在特定触发器或压缩操作（如量化、剪枝）后激活恶意行为，导致传统基于激活异常或触发器反转的防御在条件后门场景下失效。现有防御方法要么针对传统脏标签后门设计，无法泛化至压缩激活的隐蔽后门；要么专为量化后门定制，缺乏对剪枝等其它压缩操作的通用性。LMR 提出通过扩大后门类别与良性类别之间的对数间隔（Logit Margin），使触发器或压缩操作引起的 Logit 偏移不足以翻转预测，从而在不依赖触发器知识的前提下实现通用净化。该方法在极低干净数据量下有效抑制了传统与条件后门，但其对复杂语义触发器及多模态场景的适用性尚存疑。

】

---

【Making the Classification Explanation Faithful to the Confidence Score ｜置信度忠实解释器

作者：Jian-Xun Mi、Lu Pan、Weisheng Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_578fce7bf0fe)

> 视觉分类模型的解释方法通常只关注提升预测类别置信度的正贡献区域，导致解释图还原的置信度与原始模型输出存在显著偏差。现有CAM类方法依赖线性分解假设，RISE等扰动法则因均匀采样无法有效捕捉负贡献区域，使得解释在低置信度场景下严重失真。本文提出基于Metropolis-Hastings采样的黑盒解释框架MHE，通过接受/拒绝机制筛选能保持原始置信度的掩码组合，显式建模正负贡献区域。该方法在理论上保证了马尔可夫链的平稳分布，但在4000次迭代的高计算成本下，其通用定位指标表现未与SOTA直接竞争，验证了“置信度忠实”与“计算效率”间的权衡。

】

---

【MaskDiME: Adaptive Masked Diffusion for Precise and Efficient Visual Counterfactual Explanations ｜视觉反事实解释中的空间自适应约束

研究机构：丹麦技术大学

作者：Changlu Guo、Anders Nymark Christensen、Anders Bjorholm Dahl 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.18792)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18792)

> 视觉反事实解释旨在通过最小化图像语义修改来翻转模型预测，但现有扩散模型方法常因全局引导导致编辑区域发散且计算开销巨大。MaskDiME 指出，静态掩码无法适应反向扩散过程中语义区域的动态演变，是精度与效率难以兼得的关键瓶颈。该框架引入基于分类器梯度的自适应双掩码机制，在每一步去噪中动态锁定决策相关区域，实现了线性时间复杂度下的精准局部编辑。这一方法在效率与生成质量上取得了显著平衡，但其对多分类任务中梯度噪声的敏感性仍构成主要局限。

】

---

【Meta-FC: Meta-Learning with Feature Consistency for Robust and Generalizable Watermarking ｜元学习特征一致性鲁棒水印

研究机构：南京大学、山东大学

作者：Yuheng Li、Weitong Chen、Chengcheng Zhu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21849)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21849)

> 深度学习图像水印旨在通过嵌入隐藏信号实现版权保护，但现有方法在应对高强度、组合及未知失真时鲁棒性受限。主流端到端框架依赖单随机失真（SRD）训练策略，该策略因孤立处理各失真类型导致模型过拟合特定失真特征并引发梯度冲突。本文提出 Meta-FC 训练策略，通过元学习模拟已知与未知失真的交替训练，并引入特征一致性损失对齐解码器表示。该策略作为即插即用模块显著提升了多种水印模型的泛化能力，但其性能提升是否完全归因于训练策略而非骨干网络架构，仍需进一步隔离验证。

】

---

【Mitigating Error Amplification in Fast Adversarial Training ｜分布感知动态引导

研究机构：安徽大学、大连理工大学

作者：Mengnan Zhao、Lihe Zhang、Bo Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24332)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24332)

> 快速对抗训练（FAT）旨在以单步攻击降低对抗训练成本，但普遍面临灾难性过拟合（CO）与鲁棒性-准确性权衡的双重瓶颈。现有方法多采用固定扰动预算或静态标签松弛，忽视了样本置信度差异对训练动态的异质性影响。本文通过系统消融发现低置信度样本是CO与权衡的共同驱动源，进而提出DDG策略，依据样本置信度动态分配扰动预算并调制监督信号。该方法在FAT类别中实现了鲁棒精度与干净精度的同步提升，但其增益是否源于对特定攻击模式的过拟合，仍需更严苛的评估协议验证。

】

---

【OS-Fed: One Snapshot Is All You Need ｜单快照联邦学习

研究机构：东南大学

作者：Xuwei Qian、Jinghui Zhang、Yuchuan Tan 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1a529cce6fd9)

> 联邦学习（FL）面临的核心矛盾是模型更新的高维传输成本与边缘设备通信带宽的刚性限制。现有稀疏化或量化方法直接压缩梯度空间，导致复杂梯度结构信息丢失，引发收敛次优或模型发散。OS-FED 提出通过优化一个紧凑的图像快照来重构整个本地训练轨迹的累积梯度，以单步聚合替代多步传输。该方法在通信效率上实现了1.5-16倍的压缩比，但其隐私保证仅基于经验性的低相似度分析，缺乏形式化证明，且极端压缩下的误差累积机制尚需更严格的理论约束。

】

---

【PGA: Prior-free Generative Attack for Practical No-box Scenario ｜无先验生成式对抗攻击

研究机构：西北工业大学

作者：Hongyu Peng、Xiang Yuan、Gong Cheng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b82b333315fc)

> 可迁移对抗攻击旨在解决黑盒场景下攻击者无法获取目标模型参数时的安全威胁，但现有生成式攻击严重依赖大规模标注数据与预训练代理模型，这在信息稀缺的实际部署中难以成立。本文切入点在于提出首个适用于“实际无盒场景”（Practical No-box Scenario, PNS）的生成式攻击框架，通过自监督代理学习与区域感知扰动生成，在仅4000张无标签图像下实现高效迁移。该框架通过课程引导的微鲁棒优化与区域一致性正则，解决了数据稀缺下的特征坍缩与空间碎片化问题。其价值在于填补了PNS下生成式攻击的空白，但自监督代理的特征上限是否受限于无标签数据规模，仍存疑。

】

---

【Phantom: Physical Object Interactions as Dynamic Triggers for NMS-Exploited Backdoors ｜对象检测非极大值抑制后门攻击

研究机构：清华大学、浙江大学

作者：Tianlin Huo、Dongchuan Ran、Ranjie Duan 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_914ee0fa7384)

> 对象检测模型在安全关键场景中面临后门威胁，但现有攻击依赖静态像素触发器，易被检测且难以在物理世界持续生效。本文指出非极大值抑制（Non-Maximum Suppression, NMS）这一后处理环节存在几何逻辑漏洞，通过操纵真实物体间的空间重叠与置信度排序，实现无需像素修改的动态后门。该方法在多种检测器上实现了高攻击成功率并绕过现有防御，但其有效性高度依赖NMS的特定几何约束，对后处理算法变体的鲁棒性尚未验证。

】

---

【PrivSynth: Alternating and Control-Based Optimization for Privacy and Utility in Synthetic Data ｜基于庞特里亚金最大原理的合成数据隐私-效用交替优化

研究机构：清华大学、哈尔滨工业大学

作者：Xinyuan Zhao、Hanlin Gu、Guibao Song 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_36293ddffdda)

> 合成数据生成旨在从私有数据构建统计等价且隐私安全的替代集，核心矛盾在于深度生成模型对下游任务效用的依赖与成员推断攻击（Membership Inference Attack, MIA）风险之间的冲突。现有差分隐私（Differential Privacy, DP）方法通过注入噪声保护隐私，但往往导致分布失真和效用显著下降，而简单的后处理过滤又难以兼顾两者。本文切入点是将数据选择过程建模为离散时间最优控制问题，利用庞特里亚金最大原理（Pontryagin’s Maximum Principle, PMP）求解隐私-效用帕累托最优解。该框架在理论收敛性和实验效用上表现良好，但其隐私保证缺乏形式化数学边界，且评估基准与主流表格数据领域存在显著隔离。

】

---

【Rank-Guided Pseudo-Bias Learning for Robust Black-Box Adaptation ｜秩正则化引导的黑盒伪偏差学习

研究机构：印度理工学院孟买分校

作者：Rajeev Ranjan Dwivedi、Anshuman Dangwal、Vinod K Kurmi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e6719d8da9e6)

> 黑盒视觉编码器在部署时往往继承预训练数据中的虚假相关，导致特定子群体性能崩溃，而传统去偏方法依赖显式偏差标签或白盒梯度访问，无法直接应用于冻结的基础模型。现有无监督去偏方法直接聚类特征时信噪比低，伪标签噪声大，难以驱动有效的对比学习。本文切入点在于利用秩正则化（Rank Regularization）先放大特征空间中的偏差方向，再聚类生成高保真伪标签，最后结合对比对齐与自适应边际损失进行去偏。该方法在黑盒设定下实现了SOTA的最差群体准确率（WG-Acc），但其效果高度依赖偏差特征在低维空间的可分离性，对纠缠偏差的鲁棒性存疑。

】

---

【Reinforcement-Guided Synthetic Data Generation for Privacy-Sensitive Identity Recognition ｜强化引导的隐私敏感身份识别合成数据生成

研究机构：武汉大学

作者：Xuemei Jia、Jiawei Du、Hui Wei 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07884)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07884)

> 隐私法规与版权限制导致身份识别领域真实数据获取困难，现有生成方法仅能模仿稀缺源分布，无法突破数据匮乏导致的效用瓶颈。本文利用通用域预训练先验，将合成过程重构为强化学习问题，通过任务导向奖励驱动生成器超越源分布。该方法在Market-1501上实现88.6% mAP，显著优于基线，但缺乏差分隐私形式化保证，其隐私安全性仍存疑。

】

---

【RevINN: An End-to-End Invertible Neural Network for Reversible Adversarial Examples Generation ｜可逆对抗样本生成

研究机构：澳门大学、丰田研究所

作者：Jielun Huang、Chi-Man Pun、Guoheng Huang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_db9bf23b7857)

> 可逆对抗样本（Reversible Adversarial Examples, RAE）旨在通过对抗扰动误导未授权模型，同时允许授权用户无损恢复原图以保护知识产权。现有两阶段方案将扰动生成与可逆嵌入解耦，导致最终RAE在视觉质量与攻击成功率上均低于原始对抗样本。本文提出端到端可逆神经网络RevINN，通过频率域双向信息交换直接生成RAE，消除中间嵌入步骤的质量损耗。该设计在保持高隐蔽性的同时实现了近乎无损的恢复，但其依赖白盒梯度的生成机制限制了其在黑盒场景下的直接适用性。

】

---

【Robustness Under Data Scarcity: Few-Shot Continual Adversarial Training for Evolving Threats ｜少样本连续对抗训练

研究机构：西北工业大学

作者：Wenxuan Wang、Chenglei Wang、Chengzhi Yan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7d27e547e4c6)

> 对抗训练防御面临攻击类型持续演化与数据获取成本高昂的双重约束，传统连续对抗训练假设每个阶段拥有充足对抗样本，这在真实威胁场景中难以成立。现有方法在数据稀缺下普遍遭遇鲁棒泛化能力骤降与灾难性遗忘加剧的问题，导致模型无法在有限样本下稳定适应新攻击。本文提出FS-CAT框架，通过边界外推损失、高斯混合模型原型回放与多域平衡损失协同优化，在少样本条件下维持跨攻击域的鲁棒性。该方法在ImageNet-1K上实现了64.51%的干净准确率与33.53%的PGD鲁棒准确率，但其性能增益是否完全归因于框架设计而非骨干网络固有特性，仍需更严格的对照实验验证。

】

---

【SECOS: Semantic Capture for Rigorous Classification in Open-World Semi-Supervised Learning ｜开放世界半监督学习中的严格分类

研究机构：厦门大学、深圳大学

作者：Hezhao Liu、Jiacheng Yang、Junlong Gao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27596)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27596)

> 开放世界半监督学习（OWSSL）旨在利用少量已知类标注数据与包含未知类的无标注数据，实现对新类别的识别与组织。现有主流方法因缺乏语义对应机制，仅能执行聚类而非严格分类，导致预测标签无法直接映射至真实文本标签，且在评估时依赖不稳定的匈牙利匹配。本文提出 SECOS 框架，通过引入外部视觉-语言先验，构建全局语义补偿与批量细粒度重捕获机制，实现无后处理的直接文本标签预测。该范式在七个基准上超越了依赖宽松匹配协议的现有方法，但其性能高度依赖大规模预训练模型的语义覆盖能力，且未探讨在语义先验缺失场景下的退化行为。

】

---

【Stealing Split Learning Bottom Models by Recovering Embedding Geometry ｜基于嵌入几何恢复的垂直联邦学习模型窃取攻击

研究机构：美国石溪大学、美国史蒂文斯理工学院

作者：Qinbo Zhang、Yanhang Shi、Ziyi Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bc1f9dcdd4e3)

> 垂直联邦学习（VFL）通过交换中间嵌入实现跨机构协作，但暴露的嵌入流构成了模型窃取攻击面。现有防御机制通过扰动或解耦嵌入坐标来阻断点匹配攻击，却因维持模型效用而被迫保留局部邻域几何结构，这一残留信号未被现有攻击方法利用。VENOM 通过对比学习从服务器可见的嵌入流中重建几何空间，并基于该空间挖掘邻居关系以约束代理模型训练，从而在强防御下恢复客户端底层模型。该攻击在六种模态数据集上显著优于基线，但其对辅助数据分布的依赖及计算开销限制了实时部署可行性。

】

---

【Taming Noise-Induced Prototype Degradation for Privacy-Preserving Personalized Federated Fine-Tuning ｜方差自适应原型扰动与蒸馏引导裁剪正则化

研究机构：北京航空航天大学、中国人民大学

作者：Yuhua Wang、Qinnan Zhang、Xiaodong Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27833)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27833)

> 个性化联邦微调中，直接共享类原型会泄露数据指纹，而标准的各向同性高斯噪声保护（IGPP）会无差别地破坏最具判别力的特征维度，导致隐私预算与模型效用严重失衡。本文指出，特征维度对分类的贡献是不均匀的，且固定裁剪阈值存在“大阈值噪声过大、小阈值信息丢失”的两难困境。为此，提出客户端插件VPDR，通过方差自适应分组噪声分配与蒸馏引导的软裁剪正则化，在保持同等本地差分隐私（LDP）保证的前提下，将噪声从判别性维度转移至冗余维度，并稳定特征范数。该方法在多个多域基准上显著提升了效用，但未探讨在存在恶意客户端时，自适应噪声分配是否会引入新的侧信道风险。

】

---

【Taming the Long Tail: Rebalancing Adversarial Training via Adaptive Perturbation ｜长尾对抗训练中的自适应扰动再平衡

研究机构：四川大学

作者：Lilin Zhang、Yimo Guo、Yue Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.13395)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.13395)

> 长尾分布下的对抗训练面临类别不平衡导致的过置信问题，现有方法多依赖损失函数重加权，忽略了扰动生成与模型更新间的耦合效应。本文切入点在于证明对抗扰动本身可作为平衡工具，通过类别自适应的扰动强度同时抑制脆弱性与过置信。具体做法是提出即插即用框架 RobustLT，包含类别扰动平衡与迭代权重调整两个模块。该方法在长尾基准上显著提升了尾部类别鲁棒性，但其理论保证仅局限于线性分类器，且未验证认证鲁棒性，实际部署中的泛化边界尚存疑。

】

---

【TIACam: Text-Anchored Invariant Feature Learning with Auto-Augmentation for Camera-Robust Zero-Watermarking ｜文本锚定不变特征学习用于相机鲁棒零水印

作者：Abdullah All Tanvir、Agnibh Dasgupta、Xin Zhong

论文原文见 [arXiv](https://arxiv.org/abs/2602.18863)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18863)

> 相机重摄引入的透视畸变、光照变化与摩尔纹等复合退化，导致传统嵌入式水印在物理介质转换后失效。现有方法依赖手工设计的固定噪声层模拟失真，难以覆盖真实环境的非线性耦合特性，且预训练特征提取器未针对水印鲁棒性进行显式优化。TIACam 通过可微自动增强器动态发现最具破坏性的相机失真，并利用文本锚定对抗训练学习语义不变特征，在特征空间绑定水印而非修改像素。该方法在真实相机重摄场景下实现了显著优于现有基线的提取准确率，但其鲁棒性高度依赖特征提取器的完整性，缺乏对提取器本身被篡改或替换的防御机制。

】

---

【Toward Faithful Segmentation Attribution via Benchmarking and Dual-Evidence Fusion ｜双证据融合语义分割归因

作者：Abu Noman Md Sakib、OFM Riaz Rahman Aranya、Kevin Desai 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22624)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22624)

> 语义分割归因长期依赖视觉合理性验证，无法确认高亮像素是否真正驱动模型预测，且存在归因信用泄漏至目标区域外的风险。现有梯度类方法缺乏因果验证，纯干预方法则因计算开销与稳定性不足难以实用。本文提出双证据归因（Dual-Evidence Attribution, DEA），通过乘法一致性门控融合梯度细节与区域干预因果信号，并建立包含目标删除忠实度与绝对目标外泄漏的评估基准。DEA在删除忠实度上稳定优于梯度基线，但牺牲了部分计算效率与绝对保真度，其价值在于揭示了视觉评估下隐藏的忠实度-稳定性权衡。

】

---

【Towards Stealthy and Effective Backdoor Attacks on Lane Detection: A Naturalistic Data Poisoning Approach ｜车道检测后门攻击的扩散生成与注意力定位

研究机构：新加坡国立大学、香港科技大学

作者：Yifan Liao、Yuxin Cao、Yedi Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_484b442b20ac)

> 自动驾驶车道检测模型面临数据投毒后门威胁，但现有攻击方法因触发器位置随机或固定，导致攻击成功率低且视觉痕迹明显。DBALD 针对这一隐蔽性与效力难以兼得的矛盾，提出基于梯度热力图定位敏感区域，并利用掩码引导扩散模型生成场景合规的物理触发器。该方法在 CULane 和 TuSimple 数据集上实现了攻击成功率与隐蔽性的双重提升，但其对扩散模型计算开销的依赖及物理场景泛化性仍存疑。

】
