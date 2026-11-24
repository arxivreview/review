# ACL2026 · AI生成文本检测与归因方向论文汇编

> 本方向共 24 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Linguistics-Aware LLM Watermarking via Syntactic Predictability ｜基于句法可预测性的语言无关水印

研究机构：韩国延世大学、美国伦斯勒理工学院

作者：Shinwoo Park、Hyejin Park、Hyeseon An 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13829)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13829)

> 大语言模型（LLM）水印面临的核心矛盾是：为了在低熵语境下维持检测鲁棒性，现有自适应方法不得不依赖模型内部logits，从而丧失了第三方公共验证的能力。STELA通过引入基于词性（POS）n-gram条件熵的“语言不确定性”信号，将水印强度调制从模型特定域转移至语言通用域，实现了无需访问模型参数的自适应嵌入与检测。该方法在分析型、孤立型及黏着型语言中均优于基线，但其对POS标签器质量的依赖及低资源语言下的泛化边界尚存疑。

】

---

【Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection ｜基于修辞结构的创作者-编辑者双角色建模

研究机构：中国科学院、中国科学院大学

作者：Yang Li、Qiang Sheng、Zhengjia Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.04932)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eab0239be806)

> 细粒度检测需区分“人类文本经LLM润色”与“LLM文本经人类改写”两种混合形态，因二者政策后果截然不同，但现有二元或三元分类器仅能识别纯文本或笼统的协作文本，无法解耦底层逻辑与表层风格。本文切入点在于利用修辞结构理论（RST）将文本逻辑组织归因于创作者，将语言表达归因于编辑者，通过构建逻辑图并执行修辞引导的消息传递来分离双重痕迹。RACE在四分类任务中显著降低了误报率，但其有效性高度依赖单一英语基准，且对RST解析器错误的鲁棒性边界尚存疑。

】

---

【Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection ｜解耦生成器特征以实现开放集AI文本检测

研究机构：重庆大学

作者：Xiao Pu、Zepeng Cheng、Lin Yuan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_105fce224946)

> 导读 现有AI生成文本检测器在封闭集（训练与测试同源）下表现优异，但面对未见过的LLM生成器时性能急剧下降，根源在于模型过度拟合特定生成器的表面统计特征而非通用的AI语义信号。本文切入点在于将“AI检测语义”与“生成器感知特征”显式解耦，通过双瓶颈编码、交叉视图正则化及判别器引导适配的渐进式框架，强制编码器学习生成器无关的紧凑表征。该方法在MAGE基准上实现了跨生成器泛化的稳定提升，但在绝对精度上仍低于部分最新监督学习SOTA，且未验证细粒度定位能力。

】

---

【Can AI-Generated Persuasion Be Detected? Persuaficial Benchmark and AI vs. Human Linguistic Differences ｜可控生成下的说服性文本检测基准

研究机构：意大利帕多瓦大学

作者：Arkadiusz Modzelewski、Paweł Golik、Anna Kołos 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04925)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3364eef1e0bc)

> 现有AI生成文本检测聚焦于区分人机来源，却忽视了LLM生成的说服性内容在强度控制下的可检测性差异。当生成模型被指令要求“隐蔽”或“强化”说服意图时，传统基于统计指纹或语义分类的检测器性能如何变化，此前缺乏系统评估。本文通过构建包含四种可控生成策略的多语言基准，量化了生成指令对检测难度的非线性影响，并首次从196维语言学特征层面解析人机说服文本的差异。该工作填补了“生成难度”与“检测难度”关联研究的空白，但其零样本LLM评估协议是否足以代表真实对抗场景，仍存疑。

】

---

【Can You Make It Sound Like You? Post-Editing LLM-Generated Text for Personal Style ｜后编辑能否重塑LLM文本的个人风格指纹？

作者：Connor Baumler、Calvin Bao、Huy Nghiem 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24444)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9a07a726e2d9)

> 导读 当用户利用大语言模型（LLM）起草婚礼誓词或道歉信时，核心矛盾在于机器生成的通用化表达与作者个人风格之间的冲突。现有研究多关注检测器如何区分人机文本，却忽视了人类通过后编辑（Post-editing）主动重塑文本风格的能力边界。本文通过预注册在线实验，量化了后编辑对LLM风格指纹的消除效果及用户感知偏差。研究发现后编辑虽能显著拉近文本与作者自然风格的距离，但残留的LLM统计特征仍使其在嵌入空间中更接近机器文本，且模型测量与用户主观感知存在显著脱节。

】

---

【CASPER in the Machine: Insights into Character Variety in LLM-Generated Stories ｜角色刻画分类器

研究机构：美国佐治亚理工学院、美国密歇根大学

作者：Anneliese Brei、Abhisheik Sharma、Nicholas Sanaie 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.22454)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.22454)

> LLM生成故事的角色刻画存在系统性偏差，但现有评估仅停留在情节或基础人格层面，缺乏对叙事呈现方式的细粒度量化。本文切入点在于将叙事学理论中的8维角色刻画范畴转化为可自动分类的指标，以区分人机文本在角色塑造上的差异。通过构建基于LLM-as-a-judge的分类框架CASPER，对4400篇LLM生成故事与200篇人类故事进行对比分析。该框架揭示了LLM在角色闭合性与风格化上的显著偏好，但评估器本身的主观性偏差尚未被完全控制。

】

---

【DetectRL-X: Towards Reliable Multilingual and Real-World LLM-Generated Text Detection ｜DetectRL-X：多语言真实场景下的LLM生成文本检测基准

研究机构：澳门大学、阿里巴巴集团

作者：Junchao Wu、Yefeng Liu、Chenyu Zhu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15518)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_90bf9976fa9d)

> 导读 LLM生成文本检测旨在区分人类写作与机器生成内容，其核心挑战在于生成模型能力指数级提升导致人机文本分布边界日益模糊，且现有评估基准多局限于单一语言或理想化数据分布，无法反映真实多语言环境下的检测鲁棒性。现有方法在跨域、跨语言及对抗攻击下性能急剧下降，且缺乏对人机协作混合文本的系统评估。本文构建了一个包含346万样本、覆盖8种语言、6个领域及3种文本精炼操作的多语言基准，将检测任务从二元分类扩展为三元分类以识别人机协作文本。该基准揭示了神经检测器在多语言复杂分布下的相对优势及统计检测器的系统性失效，但三元分类中混合文本的标注一致性与精炼操作的边界定义仍存疑。

】

---

【DMHM: Density-aware Manifold Learning and Hybrid Mahalanobis Energy for LLMs-generated Text Detection ｜密度感知流形学习与混合马氏能量：LLM生成文本检测

研究机构：国防科技大学

作者：Tianle Liu、Zhiliang Tian、Zhen Huang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4af6d223db1)

> 大语言模型（LLM）生成文本（LGT）与人类写作（HWT）的分布边界日益模糊，现有检测器在跨模型泛化与对抗鲁棒性上存在显著瓶颈。传统方法将LGT视为单一紧凑分布，忽略了强模型生成文本与HWT重叠导致的密度异质性，致使检测器在Hard-LGT上失效。本文提出密度感知流形学习与混合马氏能量框架，通过显式建模LGT的非均匀密度结构，在未见模型与攻击场景下实现SOTA性能。该方法在理论建模上具有创新性，但其对训练时生成器身份标签的依赖可能限制其在完全未知生成器场景下的泛化能力。

】

---

【Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection ｜外显子感知重加权检测

作者：Xiaowei Zhu、Yubing Ren、Fang Fang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bba32cf5c3e2)

> 训练-free AI生成文本检测在短序列与局部改写攻击下，因均匀聚合token信号导致判别力稀释。现有方法如Binoculars假设所有token贡献均等，无法区分携带来源信号的关键token与噪声token。Exons-Detect通过双模型隐藏状态差异识别“外显子token”并非线性放大其权重，重构翻译分数以增强鲁棒性。该方法在DetectRL上取得92.14%平均AUROC，但依赖双模型前向传播且未验证隐藏状态差异与来源信号的因果关联。

】

---

【Frankentext: Stitching random text fragments into long-form narratives ｜弗兰肯文本：基于片段拼接的AI生成叙事检测规避范式

研究机构：美国马里兰大学帕克分校、美国马萨诸塞大学阿默斯特分校

作者：Chau Minh Pham、Jenna Russell、Dzung Pham 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2505.18128)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_59aa777a893d)

> 现有AI文本检测器依赖统计特征区分人机文本，但面对由大量人类片段与少量LLM连接词拼接而成的混合叙事时，其二元分类假设失效。本文提出Frankentexts生成范式，将LLM重构为“作曲家”，强制其从人类语料库中逐字复制高比例片段以构建连贯故事。该方法在保持高写作质量与多样性的同时，使72%的生成文本被SOTA检测器误判为人类写作，揭示了当前检测体系在细粒度作者归因上的根本缺陷。

】

---

【Identifying Bias in Machine-generated Text Detection ｜机器生成文本检测中的多维属性偏见量化

作者：Kevin Stowe、Svetlana Afanaseva、Rodolfo Raimundo 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09292)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09292)

> 机器生成文本检测旨在区分人类写作与大语言模型（LLM）生成内容，但高精度模型往往伴随对特定群体的系统性误报。现有研究聚焦于检测精度与对抗鲁棒性，忽视了检测器在性别、种族、英语语言学习者（ELL）及经济地位等敏感属性上的公平性缺陷。本文通过构建大规模学生作文语料库，利用逻辑回归与主导性分析量化16个公开检测系统的偏见，发现ELL身份是主要偏见驱动因素，且高AUROC模型通常伴随较低偏见。该工作填补了检测器公平性评估的空白，但其基于线性回归的分析框架是否足以捕捉复杂的非线性交互偏见，仍存疑。

】

---

【LAMCL: A Length-aware Momentum Contrastive Learning Framework for Multiscale Machine-Revised Text Detection ｜长度感知动量对比学习框架

作者：Bing Zhou、Zhe Huang、Shilei Tan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_27dad7555594)

> 机器修订文本与人类原文在词法层面高度重叠，导致传统检测器难以捕捉细微语义差异，尤其在短文本场景下归因模糊。现有基于Logit或粗粒度相似度的方法在此类“修订”任务中性能急剧衰减，本文切入点在于利用LLM增强特征并引入长度感知的对比学习机制。通过拼接原文与LLM处理文本进行一致性测量，并结合动量队列中的长度加权负采样，LAMCL实现了多尺度修订文本的精准区分。该方法在XSum修订数据集上显著优于基线，但其对特定LLM风格的依赖性及跨模型泛化能力仍存疑。

】

---

【LLM-Generated Text May Harm Your Retrieval! A Robust Detection Strategy for Retrieval-Augmented Generation ｜检索增强生成中的LLM文本检测鲁棒性

作者：Zhaoheng Huang、Yutao Zhu、Ji-Rong Wen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2a997c760a9a)

> 检索增强生成（RAG）系统依赖外部语料库提供事实依据，但语料库中不断累积的LLM生成文本会污染检索结果，导致性能退化与“沉默螺旋”效应。现有静态训练的检测器无法适应语料库的动态演化，在迭代RAG场景下检测性能急剧下降。本文提出RAG感知数据增强策略（RAD），通过模拟真实污染模式合成混合源训练数据，使检测器适应语料库的连续分布变化。该策略在长期稳定性上显著优于静态基线，但其对特定RAG生成模式的依赖性及对非RAG场景的泛化能力尚存疑。

】

---

【LLMs in Sarcasm Detection? It’s elementary! (Or is it?) ｜合成基准下的讽刺检测幻觉：捷径学习机制诊断

作者：Priyanshu Mahato、Aniket Santosh Mishra、Kripabandhu Ghosh

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed46da5e0cc8)

> 讽刺检测旨在识别文本中表面语义与真实意图的背离，但当前大语言模型（LLM）在合成数据上接近满分而在自然语言中表现崩溃的现象，暴露了评估体系的根本缺陷。现有研究将高分归因于语用推理能力，却忽视了模型可能仅在学习生成器的统计指纹。本文通过构建有机、合成及自然生成三类数据流，结合隐状态几何分析与因果干预，证明模型依赖低熵签名进行溯源分类而非语义理解。这一诊断揭示了合成基准的误导性，但缺乏对去偏训练策略的探索。

】

---

【More Aligned, Less Diverse? Analyzing the Grammar and Lexicon of Two Generations of LLMs ｜指令微调对LLM生成文本语法与词汇多样性的量化分析

作者：Adrián Gude、Roi Santos-Rios、Francis Bond 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_efc080f9204b)

> 导读 现有AI生成文本检测研究多聚焦于构建分类器以区分人机来源，但缺乏对生成模型内部语言学特征演变的系统性解释，导致检测器在模型迭代后性能波动难以归因。本文切入点在于揭示指令微调（Instruction Tuning）这一关键训练阶段如何系统性地压缩LLM输出的语法与词汇多样性，从而为检测器失效提供语言学层面的因果解释。作者利用Head-Driven Phrase Structure Grammar (HPSG) 形式语法框架，结合生态学多样性指数，对两代LLM及人类新闻文本进行细粒度分布对比。该研究提供了可解释的特征视角，但受限于单一新闻体裁与英语语言，其结论向其他领域及多语言场景的泛化性尚存疑。

】

---

【PDR: A Plug-and-Play Positional Decay Framework for LLM Pre-training Data Detection ｜位置衰减重加权

作者：Jinhan Liu、Yibo Yang、Ruiying Lu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_90c29a92fe75)

> 预训练数据检测旨在判断特定文本是否属于大语言模型（LLM）的训练集，以审计隐私泄露与版权合规。现有似然比方法普遍采用均匀加权聚合Token分数，忽略了记忆信号在序列前部集中的信息论特性，导致高熵初始位置的强信号被后部低信息量噪声稀释。本文提出位置衰减重加权（Positional Decay Reweighting, PDR），通过引入单调递减的位置权重函数重新分配Token贡献，无需训练即可增强现有检测器性能。该方法在Min-k%++基线上带来最高4.7 AUROC的提升，但其增益在复杂结构文本中显著收窄，且未验证多语言场景下的普适性。

】

---

【Robust Membership Inference for Large Language Models under Adversarial Generative Corruption ｜鲁棒成员推断攻击

作者：Yuanhong Huang、Huili Wang、Xueying Bai 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b1686c300482)

> 成员推断攻击（Membership Inference Attack, MIA）旨在审计大语言模型（LLM）训练数据是否泄露，但现有方法依赖“训练样本置信度更高”的假设，而LLM生成的高置信度文本（AIGT）恰好满足该假设，导致检测器将生成文本误判为训练数据。本文指出这一混淆效应是现有MIA失效的根本原因，而非AIGT检测器精度不足。通过构建混合专家（Mixture-of-Experts, MoE）框架联合建模MIA与AIGT特征的非线性交互，MoMIA在对抗污染下维持了接近无攻击场景的检测性能。该方法在鲁棒性上取得突破，但依赖外部AIGT检测器特征，其内生鲁棒性边界尚不明确。

】

---

【SWAN: Semantic Watermarking with Abstract Meaning Representation ｜基于抽象意义表示的语义水印

研究机构：美国南加州大学、美国加州大学洛杉矶分校

作者：Ziping Ye、Gourab Dey、Christos Christodoulopoulos 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.04305)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04305)

> 文本水印旨在通过嵌入隐蔽统计信号实现AI生成内容的可溯源性，但现有Token级与嵌入级方法在改写攻击下极易失效。SWAN利用抽象意义表示（Abstract Meaning Representation, AMR）图作为语义锚点，将水印信号从表面词元或连续向量空间提升至离散语义结构层，使得保持语义的改写无法破坏水印。该方法通过引导LLM生成符合特定AMR模板的句子并采用拒绝采样实现注入，检测时解析AMR并执行z检验。尽管在强改写攻击下AUC提升显著，但其对AMR解析器质量的依赖及采样效率瓶颈仍构成实际部署的潜在障碍。

】

---

【UMPIRE: Unveiling LLM-generated Posts via Redundant Expressions ｜基于正交语义分解的多模态LLM生成帖子检测

作者：Xiaoquan Yi、Haixing Wu、Haozhao Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bf9242d3c3bf)

> 社交平台上LLM生成的图文帖子因高度拟真而难以被传统单模态统计特征或视觉伪影检测器识别。现有方法依赖低层信号或黑盒融合，忽视了人类与模型在信息传递行为上的根本差异。本文提出UMPIRE框架，通过正交语义分解将文本嵌入解耦为视觉冗余与语境互补分量，利用几何结构差异进行判别。该方法在多个基准上显著优于现有检测器，但其对“描述性”偏置的依赖在创意写作等低冗余场景下的鲁棒性尚存疑。

】

---

【Verifiable LLM-Generated Text Detection via Projected Semantic-Structural Distributions ｜投影语义-结构分布下的可验证LLM生成文本检测

研究机构：北京大学、中南大学

作者：Ruochong Xiong、Qien Li、Wangwang Lian 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d55677182603)

> 现有零样本检测依赖代理模型概率，面临分布错位与可解释性缺失的双重困境。ProSSD通过监督子空间投影提取紧凑语义特征，并基于句法结构建模条件高斯分布，将检测转化为Wasserstein距离加权的似然比检验。该方法在DetectRL基准上实现了跨模型与跨域的高精度检测，同时提供了逐步可验证的统计证据链。其核心贡献在于以极低的计算成本（1.35GB VRAM）超越了依赖复杂扰动或大模型骨干的现有SOTA，但在极低样本量下的分布估计稳定性仍存疑。

】

---

【What is a protest anyway? Codebook conceptualization is still a first-order concern in LLM-era classification ｜概念化偏差下的LLM分类推断

作者：Andrew Halterman、Katherine A. Keith

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_144a1168027f)

> 计算社会科学（CSS）中利用大语言模型（LLM）进行文本分类时，分析师常因LLM的“静默失败”特性而跳过概念化步骤，导致下游统计推断产生系统性偏差。现有后验校正方法仅能处理评分噪声，无法消除由代码本（Codebook）定义不完整引发的概念化偏差。本文通过分解标注误差并构建模拟实验，证明了概念化错误在数学上不可被更精准的LLM或统计校正算法消除。该工作确立了概念化在LLM时代CSS方法论中的首要地位，但其结论依赖于特定的二元分类假设，对复杂多标签任务的适用性存疑。

】

---

【When Personalization Tricks Detectors: The Feature-Inversion Trap in Machine-Generated Text Detection ｜个性化风格模仿下的特征反转陷阱

研究机构：新加坡国立大学、武汉大学

作者：Lang Gao、Xuhui Li、Chenxi Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12476)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12476)

> 机器生成文本（MGT）检测旨在区分人类写作与大语言模型（LLM）生成内容，但现有方法在通用域的高精度难以迁移至个性化风格场景。当LLM通过持续预训练或提示工程深度模仿特定作者风格时，检测器依赖的统计特征发生方向性翻转，导致性能崩塌甚至预测反转。本文构建StyloBench基准揭示该现象，提出StyloCheck诊断框架量化检测器对反转特征的依赖度。该工作揭示了个性化场景下检测器的结构性失效机制，但其诊断结论是否适用于基于深度编码器的监督学习检测器，仍需进一步验证。

】

---

【Who Wrote This Line? Evaluating the Detection of LLM-Generated Classical Chinese Poetry ｜长安基准：古典诗词生成文本检测

研究机构：澳门大学

作者：Jiang Li、Tian Lan、Shanshan Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1968a417dfa7)

> 古典诗词检测旨在区分人类创作与大语言模型（LLM）生成的格律化文本，其核心难点在于严格的形式约束导致人机文本在统计分布上高度重叠。现有通用检测器依赖的困惑度或似然比特征，在短文本与强意象共享场景下失效，无法捕捉诗词特有的风格差异。本文构建包含30,664首诗词的ChangAn基准，通过对比直接生成与批判驱动优化两种策略，系统评估了12种检测器在单诗与多诗粒度下的表现。该工作揭示了当前方法在文学体裁检测中的系统性盲区，但受限于单一语言与特定生成模型，其结论向其他高约束领域的迁移性尚存疑。

】

---

【Zero-Shot Detection of LLM-Generated Text using Temperature Sensitivity ｜基于温度敏感度的零样本大语言模型文本检测

研究机构：北京邮电大学、中国科学技术大学

作者：Shixuan Ma、Jiahao Li、Zhendong Mao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a9285389394b)

> 零样本检测旨在不依赖标注数据区分人机文本，但现有统计特征如困惑度对两类文本区分度不足。本文发现解码温度调制下概率分布的响应差异可作为新判别信号，提出温度敏感度（TS）特征及归一化检测器NTS。该方法仅需单次前向传播与温度切换，在RAID基准上以0.856 AUROC超越Binoculars，但其绝对性能仍低于领域内基于复杂统计或监督学习的SOTA，且未覆盖最新对抗基准。

】
