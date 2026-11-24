# Others2026 · 机器学习理论与优化方向论文汇编

> 本方向共 33 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Causal-Adapter: Taming Text-to-Image Diffusion for Faithful Counterfactual Generation ｜因果适配器：驯服文本到图像扩散模型以实现忠实反事实生成

研究机构：英国爱丁堡大学

作者：Lei Tong、Zhihua Liu、Chaochao Lu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24798)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24798)

> 反事实图像生成旨在回答“若某属性改变，图像将如何变化”，但现有方法常陷入属性纠缠，导致干预目标属性时非目标属性发生非预期改变。传统扩散模型虽具备高保真生成能力，却缺乏显式因果机制，难以保证干预的因果忠实性。本文提出 Causal-Adapter，通过冻结预训练文本到图像扩散骨干并注入可插拔因果适配器，结合提示对齐注入与条件令牌对比损失，实现属性解耦与因果一致的反事实编辑。该方法在 CelebA 和 ADNI 数据集上显著提升了干预有效性与图像真实性，但其依赖预定义因果图且未解决复杂动态系统中的因果结构自动发现难题。

】

---

【Inductive Subgraphs as Shortcuts: Causal Disentanglement for Heterophilic Graph Learning ｜归纳子图作为捷径：异质图学习的因果解耦

研究机构：香港理工大学、澳门大学

作者：Xiangmeng Wang、Qian Li、Haiyang Xia 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19186)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19186)

> 异质图学习中，相连节点标签与特征往往相悖，导致标准图神经网络（GNN）性能退化。现有方法多通过扩展邻域或修改聚合算子来缓解，但未能解释误分类的结构性根源。本文指出，图中反复出现的归纳子图在异质环境下充当了“虚假捷径”，误导模型学习非因果关联。通过构建去偏因果图并阻断混淆与溢出路径，CD-GNN实现了捷径与因果信号的解耦。该方法在大规模异质图上显著优于基线，但在小规模极异质图上表现落后，其因果解耦机制对图规模与结构复杂度的依赖尚存疑。

】

---

【Odin: Oriented Dual-module Integration for Text-rich Network Representation Learning ｜Odin：层级对齐的双模块融合架构

作者：Kaifeng Hong、Yinglong Zhang、Xiaoying Hong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.21416)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.21416)

> 文本属性图（TAGs）建模面临图神经网络（GNN）浅层结构与预训练语言模型（PLM）深层语义的层数不匹配困境，导致高阶结构信息无法有效注入深层语义空间。现有 LLM-as-Aligner 方法因参数共享导致刚性注入，且受限于单跳邻域，难以捕捉多跳结构线索。Odin 通过解除参数共享约束，将阶段特异性 GNN 聚合层与简单聚合层交替插入 Transformer 的关键与非关键深度，实现结构抽象与语义层级的精准对齐。该框架在标准基准上优于部分基线，但受限于 BERT 骨干网络，其性能上限低于当前基于大语言模型（LLM）的原生架构 SOTA。

】

---

【Once-for-All Channel Mixers (HYPERTINYPW): Generative Compression for TinyML ｜生成式权重合成压缩微控制器点卷积层

研究机构：美国麻省理工学院

作者：Yassien Shaalan

论文原文见 [arXiv](https://arxiv.org/abs/2603.24916)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24916)

> 微控制器（MCU）部署中，1×1 点卷积（PW）层在 INT8 量化后仍占据 Flash 存储的主导地位，传统压缩方法仅减少参数量却未消除逐层存储开销。现有动态权重生成方案因逐输入分支导致实时性失效，本文提出“压缩即生成”范式，通过共享微 MLP 在加载时一次性合成 PW 权重，实现无运行时分支的整数推理。该方法在 225 kB 预算下将 1.4 MB 基线压缩 6.31 倍，保留 95% 的 Macro-F1，但其有效性严格依赖于跨层冗余假设，在极端类不平衡下的阈值稳定性仍存疑。

】

---

【RaDAR: Relation-aware Diffusion-Asymmetric Graph Contrastive Learning for Recommendation ｜关系感知扩散非对称图对比学习推荐

研究机构：电子科技大学、国防科技大学

作者：Yixuan Huang、Jiawei Chen、Shengfan Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.16800)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16800)

> 图对比学习（Graph Contrastive Learning, GCL）旨在通过自监督增强缓解推荐系统中的数据稀疏与噪声干扰，但随机丢弃等标准增强策略常破坏图拓扑结构，导致协同信号退化。现有方法在保持结构语义完整性的同时，难以捕捉多跳异质关系中的隐式偏好。RaDAR 通过引入扩散模型引导的视图生成与非对称对比目标，在去噪过程中保留高阶协同信号。该框架在稀疏与噪声场景下展现出鲁棒性，但其对加权边多行为数据的处理仍依赖二值化聚合，未充分挖掘行为强度信息。

】

---

【RAST-MoE-RL: A Regime-Aware Spatio-Temporal MoE Framework for Deep Reinforcement Learning in Ride-Hailing ｜机制感知时空混合专家强化学习

研究机构：美国麻省理工学院、美国加州大学伯克利分校

作者：Yuhan Tang、Kangxin Cui、Jung Ho Park 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.13727)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13727)

> 网约车调度需在非平稳供需环境下平衡匹配延迟与接驾延迟，传统强化学习（RL）策略因编码器表达能力不足及奖励设计缺陷，常陷入训练不稳定或分布外泛化失效的困境。本文切入点在于将混合专家（Mixture-of-Experts, MoE）架构引入策略网络，以稀疏激活的专门化专家捕捉不同供需机制，并构建物理信息代理模型解决长时程信用分配失真问题。通过区域级二元动作空间与自适应软约束奖励，该框架在旧金山数据上实现了总奖励提升13%。其价值在于验证了MoE在复杂时空决策中的表示效率，但单城市实验与静态专家路由机制限制了其跨域迁移能力的验证。

】

---

【Spectral Thresholds in Correlated Spiked Models and Fundamental Limits of Partial Least Squares ｜相关尖峰模型下的谱阈值与偏最小二乘极限

研究机构：瑞士洛桑联邦理工学院

作者：Pierre Mergny、Lenka Zdeborová

论文原文见 [arXiv](https://arxiv.org/abs/2510.17561)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17561)

> 导读 多模态学习旨在从多个相关高维数据源中联合恢复低维信号结构，但偏最小二乘（Partial Least Squares, PLS）作为主流谱方法，其理论性能边界长期缺失。现有研究仅通过数值实验指出PLS阈值次优，却缺乏解析证明，导致无法量化其与贝叶斯最优估计器的差距。本文通过随机矩阵理论推导双通道相关尖峰模型的样本跨协方差矩阵谱性质，首次给出PLS的精确相变阈值。该工作确立了PLS在特定信噪比与相关性区域存在固有信息损失的理论事实，但其结论局限于高维渐近极限，未涉及有限样本下的算法修正或实际数据验证。

】

---

【东北团队新研究：超稀疏采样下的单侧矩阵补全

研究机构：美国东北大学、美国佐治亚理工学院

作者：Hongyang R. Zhang、Zhenshuo Zhang、Huy L. Nguyen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12213)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12213)

> 矩阵补全旨在从部分观测中恢复高维数据的低秩结构，但传统方法在观测数低于秩存储位数时面临信息论极限。现有非凸优化与凸松弛算法均无法在每行仅观测常数个条目的超稀疏场景下恢复完整矩阵，本文切入点在于放弃恢复矩阵本身，转而估计其行空间对应的二阶矩矩阵。通过引入Hájek估计器校正非随机缺失偏差，并结合梯度下降填补缺失项，实现了在 $p=C/d$ 采样率下的无偏估计。该工作解决了Cao et al. (2023) 遗留的通用采样开放问题，但在共同均值假设与秩指定依赖上存在理论边界。

】

---

【京都团队新研究：相对高秩张量稀疏采样的精确渐近分析

研究机构：日本京都大学、日本理化学研究所

作者：Angelo Giorgio Cavaliere、Riki Nagasawa、Shuta Yokoi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17886)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17886)

> 相对高秩张量在稀疏观测下的恢复面临理论空白，现有低秩假设下的统计力学方法无法处理 $M \gg 1$ 的情形，而工程化算法缺乏精确的性能边界。本文切入点在于引入“密集极限”（$N \gg M \gg 1$），在此极限下高阶关联可被忽略，从而允许使用累积量展开避免高斯近似失效。通过构建基于广义近似消息传递（G-AMP）的算法与副本理论，本文推导了贝叶斯最优推断的精确渐近性能。该工作填补了高秩稀疏张量恢复的理论缺口，但其结论严格依赖于特定的极限条件，在有限尺寸或全连接场景下的适用性存疑。

】

---

【俄亥俄州立团队新研究：RANGER：稀疏门控混合专家与自适应检索重排序的病理报告生成框架

研究机构：美国俄亥俄州立大学

作者：Yixin Chen、Ziyu Su、Hikmat Khan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04348)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04348)

> 导读 病理报告生成旨在从千兆像素全切片图像（WSI）中直接提取诊断文本，现有方法受限于同质化解码器对异质病理模式的表达不足，以及静态知识检索引入的噪声干扰。本文切入点在于将解码器FFN替换为稀疏门控混合专家（MoE），并引入两阶段自适应检索重排序机制，以分别解决输出端的生成特异性缺失与输入端的语义对齐噪声问题。该框架在PathText-BRCA数据集上实现了BLEU-4 0.1435与ROUGE-L 0.3038的性能，验证了动态专家路由与知识精炼的有效性，但其增益幅度较小且仅局限于单一癌种，泛化能力存疑。

】

---

【分层联邦基础模型

作者：Payam Abdisarabshali、Fardis Nadimi、Kasra Borazjani 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.03695)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.03695)

> 无线边缘网络中多模态多任务基础模型（M3T FMs）的分布式微调面临星型拓扑的扩展性瓶颈与模块异构性失配问题。现有联邦基础模型（FFMs）框架多采用全模型聚合与单一层级通信，无法适配M3T FMs的模块化结构及雾/边缘节点在模态与任务上的双重异构性。本文提出HF-FMs，通过将M3T FMs的模块（编码器、Adapter、任务头）与雾/边缘网络的分层拓扑及D2D通信进行结构对齐，实现模块级非均匀聚合与中继。该范式在原型验证中显著降低了时延与能耗，但缺乏大规模部署下的收敛理论保证，其架构优势在异构程度极高时的边界尚不明确。

】

---

【动态嵌套层级（DNH）：面向终身智能的自演化架构

作者：Akbar Anbar Jafari、Cagri Ozcinar、Gholamreza Anbarjafari

论文原文见 [arXiv](https://arxiv.org/abs/2511.14823)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.14823)

> 导读 现有深度学习模型在处理非平稳数据流时，因架构静态性导致灾难性遗忘与适应力丧失，传统持续学习方法多聚焦于参数正则化或重放，却忽视了优化层级本身对分布漂移的响应能力。本文提出动态嵌套层级（Dynamic Nested Hierarchies, DNH），将嵌套优化范式中的固定层级与频率转化为随时间演化的有向无环图，通过元优化实现结构自演化。DNH在语言建模与常识推理上超越静态基线，但在类增量学习基准上显著落后于专用持续学习算法，其有效性受限于架构扩展的规模控制与微观可塑性机制的缺失。

】

---

【北京理工团队新研究：语义引导特征混合的长尾联邦学习偏差消除

研究机构：北京理工大学

作者：Jingrui Zhang、Yimeng Xu、Shujie Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.27240)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.27240)

> 长尾分布下的联邦学习面临分类器向头部类别偏斜的固有缺陷，现有方法或依赖服务器端梯度聚合引发隐私风险，或采用随机混合生成误导性伪样本。FedSM 切入这一盲区，利用预训练图文对齐模型计算类别语义相关性，在客户端本地引导特征混合以生成平衡伪特征。该方法通过概率选择策略与轻量级分类器重训练，在保持隐私的前提下显著提升了尾部类别的识别精度。其价值在于将语义先验引入联邦数据增强，但受限于静态分布假设，对动态长尾场景的适应性仍存疑。

】

---

【华南理工团队新研究：双对比学习进化神经架构搜索

研究机构：华南理工大学、南开大学

作者：Xian-Rong Zhang、Yue-Jiao Gong、Wei-Neng Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.20112)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20112)

> 进化神经架构搜索（ENAS）面临的核心矛盾是：评估每个候选架构需完整训练，导致搜索成本随种群规模与迭代次数指数增长。现有代理预测器依赖大量昂贵的“架构-性能”标注对，且基于均方误差（MSE）的回归损失无法保证排名准确性，易误导进化方向。本文切入点在于利用无标签结构数据自监督预训练表示，并采用对比损失优化相对排名而非绝对精度。该方法在NASBench-101上以95.00%验证精度领先最强基线0.29%，但在开放空间与硬件感知场景下未展示优势，其价值受限于固定Cell空间的表达力上限。

】

---

【南京团队新研究：扩散模型数据增强的统一评估框架

研究机构：南京大学

作者：Zekun Li、Yinghuan Shi、Yang Gao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08364)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08364)

> 扩散模型数据增强（Diffusion-based Data Augmentation, DiffDA）旨在通过合成样本缓解低资源场景下的分类性能瓶颈，但现有研究因实验设置碎片化导致方法间无法公平比较。本文切入点在于将DiffDA解耦为微调、生成、利用三个正交模块，建立统一评估协议以隔离各组件贡献。通过重实现主流方法并在多粒度低数据任务上系统对比，揭示了样本利用策略对最终精度的决定性影响。该框架填补了系统性基准空白，但其结论受限于离线生成范式，未探索生成与训练动态耦合的可能性。

】

---

【南洋理工团队新研究：分子性质预测的范式统一与基准重构

研究机构：新加坡南洋理工大学、香港科技大学

作者：Zongru Li、Xingsheng Chen、Honggang Wen 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16586)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16586)

> 分子性质预测（Molecular Property Prediction, MPP）旨在从结构推断物理化学或生物活性，但现有方法在精度、效率与可解释性间存在割裂，且评估协议导致性能排名不稳定。本文切入点在于揭示评估协议对模型排名的决定性影响，并构建跨时代的统一分类法。通过整合量子力学、描述符机器学习、几何深度学习与基础模型四大范式，本文建立了约束驱动的决策矩阵。其价值在于提供了系统化的方法选择框架，但缺乏对最新大语言模型推理能力的实证对比，且未解决分布外泛化的根本机制问题。

】

---

【国家科学研究团队新研究：奖励机器与信号时序逻辑的耦合框架

研究机构：法国国家科学研究中心

作者：Ana María Gómez Ruiz、Thao Dang、Alexandre Donzé

论文原文见 [arXiv](https://arxiv.org/abs/2604.14440)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14440)

> 时序逻辑强化学习旨在将非马尔可夫任务规范转化为可优化的奖励信号，以解决传统标量奖励在长时程依赖任务中的表达失效。现有方法多依赖将线性时序逻辑转换为大型自动机，导致状态空间膨胀且掩盖了原始规范的语义可解释性，同时常规算法易陷入局部最优。本文提出 RM-STL 框架，直接将信号时序逻辑（Signal Temporal Logic, STL）谓词嵌入奖励机器（Reward Machines, RM）的转移机制中，利用连续鲁棒性信号引导训练。该框架在连续控制任务中有效规避了局部最优陷阱，但其泛化能力与理论完备性仍存疑。

】

---

【国立团队新研究：病理图像分类中的状态空间混合模型

研究机构：新加坡国立大学、英国诺丁汉大学

作者：Enhui Chai、Sicheng Chen、Tianyi Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15711)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15711)

> 导读 病理区域（ROI）分类面临固定放大倍率预训练导致的域偏移、ViT骨干局部建模低效及细粒度特征敏感度不足三大瓶颈。现有大规模基础模型虽具泛化性，但在特定临床场景下性能遭遇平台期，且计算开销高。本文提出SSMamba，通过域内自监督掩码图像建模与双向状态空间编码器，在25.3M参数下实现了对11个SOTA基础模型的超越。其价值在于验证了任务特异性架构在细粒度任务上的优势，但域内预训练策略对未见数据集的泛化能力存疑。

】

---

【基于Q值混合安全评估的逆约束强化学习

作者：George Papadopoulos、George A. Vouros

论文原文见 [arXiv](https://arxiv.org/abs/2602.23816)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23816)

> 在约束未知且成本不可观测的场景下，如何从专家演示中学习安全策略，是逆约束强化学习（ICRL）面临的核心难题。现有方法要么过度保守导致任务失败，要么在分布外状态盲目探索高风险区域。SafeQIL 通过构建混合任务奖励与安全评估的Q值，并引入基于演示支持的局部上界约束，解决了这一权衡。该方法在Safety-Gymnasium基准上验证了其在保持任务回报的同时降低安全违规成本的有效性，但在复杂几何结构下的稳定性仍存疑。

】

---

【基于内部激活的奖励黑客生成时监控

作者：Patrick Wilhelm、Thorsten Wittkopp、Odej Kao

论文原文见 [arXiv](https://arxiv.org/abs/2603.04069)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04069)

> 后部署微调常导致大语言模型出现奖励黑客行为，即模型优化代理目标而违背设计者意图，且该行为在表面输出中往往保持良性，难以通过传统输出评估检测。现有基于文本或推理链的监控方法仅能间接反映内部计算，无法捕捉在文本生成前已发生的内部策略偏移。本文提出一种基于稀疏自编码器（Sparse Autoencoder, SAE）特征与轻量级分类器的激活监控方法，在生成过程中实时估计奖励黑客概率。该方法在三个模型家族上验证了内部信号对失配程度的敏感性，但受限于单一基准与线性分类器，其跨分布泛化能力存疑。

】

---

【多目标多智能体强化学习偏好驱动框架

作者：Adam Callaghan、Karl Mason、Patrick Mannion

论文原文见 [arXiv](https://arxiv.org/abs/2511.18181)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18181)

> 多目标多智能体强化学习（MOMARL）旨在解决连续控制中多个智能体需同时协调行动并权衡冲突目标（如速度与能耗）的复杂决策问题。现有方法要么将向量奖励预先标量化导致Pareto前沿多样性丧失，要么采用外循环逐权重训练导致样本效率低下且缺乏智能体间协调。本文切入点在于构建首个支持连续状态与动作空间的内循环Actor-Critic框架，通过偏好条件化的单网络同时编码Pareto前沿。该框架填补了MOMARL在连续控制领域的空白，但其评估基准缺乏与标准多智能体强化学习（MARL）SOTA的横向对比，且未验证在部分可观测性下的鲁棒性。

】

---

【慕尼黑工业团队新研究：动态大模型分割与放置联合优化

研究机构：德国慕尼黑工业大学、德国埃尔朗根-纽伦堡大学

作者：Aladin Djuhera、Fernando Koch、Alecio Binotto

论文原文见 [arXiv](https://arxiv.org/abs/2512.01039)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01039)

> 6G边缘环境下大基础模型（LFM）的推理面临算力与带宽的双重瓶颈，静态分割策略无法适应动态异构环境导致的延迟尖峰与资源失衡。现有编排框架将模型视为黑盒，缺乏运行时层重划分能力，本文切入点在于将模型分割与节点放置提升为运行时联合优化变量。通过构建基于计算图的自适应编排框架，实现QoS驱动的动态重分割与迁移。该框架在模拟场景中显著降低了延迟，但缺乏真实硬件与复杂数据集的实证，其动态调度收益在极端波动下的鲁棒性存疑。

】

---

【普渡团队新研究：原型引导的分布鲁棒优化

研究机构：美国普渡大学

作者：Haixiang Sun、Andrew L. Liu

论文原文见 [arXiv](https://arxiv.org/abs/2602.01427)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01427)

> 少样本学习（Few-Shot Learning, FSL）在数据极度稀疏时面临分布偏移导致的泛化崩溃，传统分布鲁棒优化（Distributionally Robust Optimization, DRO）依赖固定参考分布，无法适配新类别的几何结构。PG-DRO 通过分层最优传输（Optimal Transport, OT）从基础域原型构建类自适应先验，嵌入 Sinkhorn DRO 对偶框架，实现类级鲁棒决策。该方法在 CIFAR-10 扰动实验中显著优于基线，但其理论保证依赖局部收缩假设，且未验证在极端分布偏移下的稳定性。

】

---

【滑铁卢团队新研究：核化VICReg：在再生核希尔伯特空间重构自监督正则化几何

研究机构：加拿大滑铁卢大学

作者：M. Hadi Sepanj、Benyamin Ghojogh、Saed Moradi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.07289)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07289)

> 导读 自监督学习（Self-Supervised Learning, SSL）旨在利用无标签数据中固有的结构替代人工标注，其核心价值在于打破监督学习对昂贵标签的依赖并提升泛化能力。现有非对比方法如VICReg虽通过统计正则化防止表示坍塌，但其欧氏空间假设难以捕捉深层网络产生的非线性流形结构，导致在复杂数据分布下正则化失效。本文提出Kernel VICReg，将VICReg的方差、不变性与协方差项整体提升至再生核希尔伯特空间（Reproducing Kernel Hilbert Space, RKHS），利用双中心化核矩阵与Hilbert-Schmidt范数重新定义几何约束。该方法在中小规模数据集上验证了核化正则化对非线性结构的捕获能力，但其计算复杂度与大规模可扩展性仍存疑。

】

---

【潜空间流匹配引导的分子逆设计

作者：Alexander Arjun Lobo、Urvi Awasthi、Leonid Zhukov

论文原文见 [arXiv](https://arxiv.org/abs/2603.26889)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26889)

> 分子逆设计旨在从海量化学空间中筛选出满足特定物理化学性质（如药物类、合成可行性）的候选结构，传统虚拟筛选因计算成本随空间指数级增长而失效。现有基于变分自编码器（VAE）的潜空间优化方法常因缺乏生成先验约束，导致优化轨迹偏离有效分子流形，产生无效结构或多样性坍缩。MoltenFlow 通过引入流匹配（Flow Matching）学习潜空间分布先验，并结合可微代理模型的梯度引导，实现了在固定预算下对帕累托前沿的稳定推进。该方法在样本效率与结构保真度之间提供了显式的权衡控制，但其有效性局限于2D字符串表征，未验证3D几何约束下的泛化能力。

】

---

【理工学院孟买分校团队新研究：可解释展开网络中的可调域适应

研究机构：印度理工学院孟买分校

作者：Snehaa Reddy、Jayaprakash Katual、Satish Mulleti

论文原文见 [arXiv](https://arxiv.org/abs/2603.26931)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26931)

> 参数化域偏移下的回归任务面临个性化训练（PT）成本过高与联合训练（JT）性能劣化的双重困境。现有分类域适应方法依赖黑盒特征提取器，无法定位域敏感参数，导致适应过程缺乏可解释性且计算冗余。本文切入点在于利用展开网络（Unfolding Networks）的物理可解释性，将域效应解耦为少量可调参数。通过构建参数-域变量映射函数，实现单一模型在推理时的结构化适应。该方法在信号恢复任务中验证了有效性，但其在非线性复杂域偏移下的泛化边界尚存疑。

】

---

【科学理工团队新研究：渐近最优多臂老虎机算法的遗憾尾部刻画

研究机构：印度科学理工学院

作者：Subhodip Panda、Shubhada Agrawal

论文原文见 [arXiv](https://arxiv.org/abs/2604.14876)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14876)

> 在平稳随机多臂老虎机（MAB）中，现有研究聚焦于最小化期望遗憾，但忽略了算法在罕见极端情况下产生巨大损失的尾部风险，这在临床试验等安全关键场景中可能导致灾难性后果。Fan and Glynn (2024) 虽证明了渐近最优算法的遗憾尾部下界，但其分析仅限于单参数指数族（SPEF），无法覆盖重尾或无界支撑等更广泛的非参数分布。本文通过将 KLinf-UCB 算法推广至满足特定正则性条件的广义分布类 $L$，并首次推导了该算法在非参数模型下的遗憾尾部上界，填补了参数模型之外的理论空白。这一工作确立了非参数环境下最优算法尾部行为的紧界，但其紧性依赖于分布类的判别等价性，该性质在实际复杂分布中是否普遍存在仍存疑。

】

---

【米兰理工团队新研究：流式持续学习（SCL）实证指南

研究机构：意大利米兰理工大学

作者：Andrea Cossu、Federico Giannini、Giacomo Ziffer 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01677)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01677)

> 流式持续学习旨在解决非平稳数据流中模型需同时快速适应新概念与保留旧知识的矛盾，而现有流式机器学习（SML）与持续学习（CL）范式各自侧重单一目标，无法兼顾。本文切入点在于揭示二者在混合漂移场景下的互补性与失效模式，通过构建虚拟与真实漂移的实证框架，证明单一范式无法同时满足适应性与稳定性要求。具体做法是设计基于MNIST的双场景实验，对比SML与CL代表性策略在概念漂移下的表现。该工作为SCL范式提供了必要的实证动机，但其结论局限于简单二分类任务，对复杂视觉任务中SCL机制的普适性仍存疑。

】

---

【纽卡斯尔团队新研究：最小深度学习架构的系统表征：收敛、剪枝与量化的联合分析

研究机构：英国纽卡斯尔大学、英国伦敦玛丽女王大学

作者：Ziwei Zheng、Huizhi Liang、Vaclav Snasel 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17987)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17987)

> 深度学习模型在分类任务上表现优异，但识别能可靠解决任务的最小架构仍具挑战。现有剪枝与量化研究多聚焦于“如何压缩得更好”，却缺乏对“何时可以安全压缩”的系统性界定，导致在极端压缩下精度崩溃或量化误差被放大。本文提出一种联合分析收敛、剪枝与量化的计算方法论，通过扫描架构形状与参数规模，界定“稳定学习”的最小参数阈值及其安全压缩边界。该工作提供了架构设计的经验法则，但其结论局限于简单图像分类任务，且未涉及硬件部署约束，实际压缩价值存疑。

】

---

【边缘联邦学习多维基准评估框架

作者：Sales Aribe、Gil Nicholas Cagande

论文原文见 [arXiv](https://arxiv.org/abs/2603.08735)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08735)

> 边缘计算场景下联邦学习（Federated Learning, FL）面临数据异构、通信受限与能量约束的三重耦合挑战，但现有研究多聚焦单一算法改进，缺乏统一的多维性能评估标准。本文切入点在于构建一个覆盖优化策略、通信效率、隐私机制与系统架构的四维分类法，并对五种主流FL算法进行归一化基准测试。通过PRISMA/SALSA综述方法论筛选308篇文献，建立包含准确率、收敛时间、通信开销、能量消耗及非IID鲁棒性的性能矩阵。该框架为边缘FL部署提供了实证依据，但其评估局限于经典算法范畴，未涵盖分割联邦学习（Split Federated Learning, SFL）等新兴范式，且归一化指标可能掩盖硬件异构性的绝对差异。

】

---

【香港浸会团队新研究：联邦层次聚类与自动簇数选择

研究机构：香港浸会大学

作者：Yue Zhang、Chuanlong Qiu、Xinfa Liao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.12684)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12684)

> 联邦聚类（Federated Clustering, FC）旨在数据不出本地的前提下发现全局数据分布结构，但现有方法普遍依赖簇数已知且大小均匀的强假设，导致在真实异构数据上失效。本文提出 Fed-k*-HC，通过客户端微子簇划分与服务器端层次合并，在单次通信中自动确定最优簇数 $k^*$ 并处理不平衡分布。该方法以信息损失换取隐私安全，在结构化不平衡数据上表现优异，但在高维文本数据及公平性约束下的有效性尚未验证。

】

---

【鲁汶团队新研究：单模态纤维级缺失下的代数张量补全

研究机构：比利时鲁汶大学

作者：Shakir Showkat Sofi、Lieven De Lathauwer

论文原文见 [arXiv](https://arxiv.org/abs/2509.18149)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18149)

> 高维数据中，当观测缺失呈现“整条纤维存在或消失”的结构化模式时，传统基于随机采样的概率恢复理论失效，且迭代优化算法收敛缓慢且依赖初始化。本文切入点在于利用该缺失模式的代数结构，将补全问题转化为子空间交集计算，从而绕过迭代优化。具体做法是通过标准线性代数操作直接求解 Tensor Train (TT) 分解核。该方法在确定性条件下提供了快速且唯一恢复的保证，但在噪声鲁棒性上仍依赖后续优化精修，其精度上限是否优于非凸正则化方法尚存疑。

】

---

【麦吉尔团队新研究：时空自相关误差调整

研究机构：加拿大麦吉尔大学

作者：Fuqiang Liu、Weiping Ding、Luis Miranda-Moreno 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.23656)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.23656)

> 交通预测模型普遍依赖均方误差（MSE）损失，隐含预测误差为独立同分布白噪声的假设，但该假设在时空交通数据中因未观测的外部干扰与模型失配而失效，导致预测性能受限。现有研究聚焦于改进图卷积或注意力架构以捕捉时空依赖，却忽视了训练目标函数本身对误差结构的错误假设。本文提出时空自相关误差调整（Spatiotemporally Autocorrelated Error Adjustment, SAEA）框架，通过向量自回归（VAR）过程建模误差的时空相关性，并将系数矩阵嵌入重构的损失函数中联合优化。该框架无需修改骨干网络架构，在五个主流模型上实现了平均6.5%的精度提升，但其增益是否能在当前SOTA架构上复现，以及VAR系数矩阵在动态拓扑下的稳定性，仍是存疑之处。

】
