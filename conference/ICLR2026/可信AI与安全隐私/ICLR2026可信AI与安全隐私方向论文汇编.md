# ICLR2026 · 可信AI与安全隐私方向论文汇编

> 本方向共 113 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A FAIR BAYESIAN INFERENCE THROUGH MATCHED GIBBS POSTERIOR ｜匹配Gibbs后验下的群体公平贝叶斯推断

研究机构：韩国首尔大学、韩国科学技术院

作者：Jihu Lee、Kunwoong Kim、Sehyun Park 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_17515746)

> 群体公平算法长期聚焦于寻找满足统计约束的单点预测模型，忽略了深度神经网络过参数化导致的过度自信问题，使得模型在高风险决策中缺乏不确定性量化能力。现有公平性优化方法在计算后验分布时面临对抗学习或二次方计算复杂度的瓶颈，无法兼顾公平性约束与概率推断效率。本文提出匹配Gibbs后验，通过引入可学习的匹配函数将公平性惩罚嵌入对数似然，利用马尔可夫链蒙特卡洛算法高效采样公平后验分布。该方法在效用-公平性与不确定性-公平性权衡上优于基线，但其理论保证依赖于匹配函数的存在性，且未与最新点估计SOTA进行直接数值对标。

】

---

【A GENERAL FRAMEWORK FOR BLACK-BOX ATTACKS UNDER COST ASYMMETRY ｜非对称查询成本下的黑盒对抗攻击框架

研究机构：美国南加州大学、瑞士洛桑联邦理工学院

作者：Mahdi Salmani、Alireza Abdollahpoorrostam、Seyed-Mohsen Moosavi-Dezfooli

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_55300158)

> 黑盒对抗攻击的核心矛盾在于查询预算的有限性与生成有效扰动的需求。现有方法假设所有查询成本相同，或仅关注高成本查询而忽略低成本查询的累积开销，导致在内容审核等实际场景中攻击者因频繁触发惩罚机制而失效。本文通过改造边界搜索与梯度估计两个核心组件，提出适应任意成本比率的非对称攻击框架。该框架在极端不对称设定下显著降低了总查询成本，但其有效性依赖于局部线性假设，且在中等成本比率下的增益有限。

】

---

【AbsTopK: Rethinking Sparse Autoencoders For Bidirectional Features ｜AbsTopK：基于近端算子的双向稀疏自编码器

研究机构：美国俄亥俄州立大学

作者：Xudong Zhu、Mohammad Mahdi Khalili、Zhihui Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2510.00404)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00404)

> 导读 大语言模型内部表示的叠加特性导致神经元多义性，阻碍了直接基于神经元的机制理解。现有稀疏自编码器（Sparse Autoencoder, SAE）通过L1正则化或TopK截断实现稀疏性，但强制非负约束导致语义轴碎片化，无法在单一特征中编码对立概念。本文通过展开近端梯度法，将SAE激活函数统一为稀疏正则化的近端算子，并移除非负约束提出AbsTopK变体。该架构在重构保真度与双向概念编码上优于TopK和JumpReLU SAE，但在纯重构误差上未证明超越Gated SAE，且缺乏对负激活因果干预稳定性的验证。

】

---

【ATEX-CF: Attack-Informed Counterfactual Explanations for Graph Neural Networks ｜攻击驱动的反事实图解释

作者：Yu Zhang、Sean Bin Yang、Arijit Khan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.06240)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.06240)

> 图神经网络在节点分类中依赖邻域聚合，但其黑盒特性阻碍了医疗与金融场景的信任建立。传统反事实解释仅通过删除边来定位关键结构，忽略了“缺失边”对预测的潜在影响，导致解释覆盖不全且搜索空间巨大。本文提出 ATEX-CF，利用对抗攻击生成的边添加候选集，与边删除联合优化，以在有限预算内生成更稀疏、更合理的反事实解释。该框架在效率与覆盖度上优于现有基线，但其“合理性”约束是否等同于因果有效性，仍存疑。

】

---

【BANDIT LEARNING IN MATCHING MARKETS ROBUST TO ADVERSARIAL CORRUPTIONS ｜对抗腐败下的去中心化匹配市场鲁棒学习

研究机构：南方科技大学、哈尔滨工业大学

作者：Zheshun Wu、Jinhang Zuo、Zenglin Xu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_29515797)

> 去中心化匹配市场要求参与者在偏好未知的情况下通过交互学习最优稳定匹配，但现有算法假设反馈信号纯净，无法抵御恶意篡改。本文指出标准探索-利用算法在自适应对抗下会因反馈污染而陷入线性遗憾，其切入点是将鲁棒多臂老虎机（MAB）的多层实例思想迁移至匹配场景，并解决由此引发的匹配冲突。通过构建多层ETGS竞赛与子阶段同步机制，本文在已知与未知腐败水平下均实现了最优稳定遗憾的理论上下界。该工作填补了匹配市场对抗鲁棒性的理论空白，但实验仅在小规模模拟环境中验证，大规模真实场景下的通信开销与性能退化尚存疑。

】

---

【Bandits with Single-Peaked Preferences and Limited Resources ｜单峰偏好下的预算约束组合多臂老虎机匹配

研究机构：以色列理工学院

作者：Omer Ben-Porat、Gur Keinan、Rotem Torkan

论文原文见 [arXiv](https://arxiv.org/abs/2510.09425)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09425)

> 在线推荐系统需在有限预算下实时匹配用户与内容，但通用偏好下的最优匹配是NP-hard问题，导致现有算法只能提供较弱的α-遗憾保证。本文切入点在于利用社会选择理论中的单峰偏好结构，将计算不可行的离线优化转化为多项式时间可解问题，从而在保持统计学习难度的同时实现标准遗憾界。通过设计基于PQ树的顺序提取算法与动态规划匹配器，该工作证明了单峰结构能彻底绕过计算瓶颈。其价值在于为结构化在线匹配提供了理论完备的解法，但缺乏真实数据验证，且假设偏好严格单峰，在噪声环境下鲁棒性存疑。

】

---

【Beyond Membership: Limitations of Add/Remove Adjacency in Differential Privacy ｜差分隐私邻接关系错配审计

研究机构：芬兰赫尔辛基大学

作者：Gauri Pradhan、Joonas Jälkö、Santiago Zanella-Béguelin 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.21804)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.21804)

> 差分隐私（DP）旨在通过限制算法输出对单个数据记录的敏感度来提供可证明的隐私保护，但现有主流实现默认采用“加/删邻接”（Add/Remove Adjacency），仅保护成员身份而非数据属性。当攻击者已知目标样本在训练集中时，加/删邻接无法有效约束属性推断风险，导致隐私保证被系统性高估。本文通过构造“替换邻接”（Substitute Adjacency）下的最坏情况金丝雀样本，揭示了标准DP审计工具的盲区。该工作修正了DP-SGD在属性隐私场景下的理论边界，但其在自然数据集上的审计紧密度仍受限于模型初始化与优化器选择。

】

---

【Bi-directional Bias Attribution: Debiasing Large Language Models without Modifying Prompts ｜双向偏见归因

研究机构：厦门大学

作者：Yujie Lin、Kunquan Li、Yixuan Liao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.04398)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04398)

> 大语言模型（LLMs）在生成任务中普遍继承并放大社会偏见，但现有缓解手段要么依赖高昂的微调成本，要么通过修改提示词牺牲用户体验。本文切入点在于不触碰模型参数与输入提示，而是直接定位并干预内部神经元。作者提出基于熵最小化的刻板印象线索选择与双向积分梯度归因框架，在投影层实施激活值固定以实现去偏。该方法在无需微调与改提示的约束下实现了显著的偏见降低，但其仅干预投影层的假设是否足以覆盖深层非线性变换中的偏见纠缠，仍存疑。

】

---

【BOOSTING FOR PREDICTIVE SUFFICIENCY ｜基于预测充分性的提升算法分布外泛化机制

研究机构：荷兰阿姆斯特丹大学

作者：Gowtham Reddy Abbavaram、Rajeev Verma、Celia Rubio-Madrigal 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_2719663)

> 分布外泛化（OOD）研究长期依赖显式环境标签或不变性约束，但在隐藏混杂偏移场景下，这些假设常因数据生成过程复杂而失效，导致专用方法性能不及传统模型。本文切入点在于揭示提升算法（Boosting）为何能隐式应对此类偏移，而非依赖显式分区。通过定义$\alpha$-预测充分性并证明提升算法在有限步内收敛至该状态，本文从信息论角度解释了其鲁棒性来源。这一理论框架挑战了“必须显式建模环境”的共识，但实验仅在表格数据上验证，视觉任务中的适用性存疑。

】

---

【CAGE: A Framework for Culturally Adaptive Red-Teaming Benchmark Generation ｜文化自适应红队基准生成框架

研究机构：韩国首尔大学

作者：Chaeyun Kim、YongTaek Lim、Kihyun Kim 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20170)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20170)

> 多语言大语言模型（LLM）的安全评估长期依赖英语基准的直接翻译，导致本地法律与社会规范下的隐性危害被系统性遗漏。现有模板填充与原生构建方法在结构多样性与文化真实性之间难以兼顾，CAGE 通过语义模具（Semantic Mold）解耦攻击意图与文化内容，实现了跨文化红队提示的自动化生成。该框架在韩语与高棉语上验证了文化接地提示对模型漏洞揭示能力的提升，但其效果是否完全归因于文化特异性而非提示复杂度，仍需更严格的对照实验加以区分。

】

---

【Can SAEs reveal and mitigate racial biases of LLMs in healthcare? ｜稀疏自编码器在医疗大语言模型种族偏见中的揭示与缓解局限

研究机构：美国东北大学

作者：Hiba Ahsan、Byron C. Wallace

论文原文见 [arXiv](https://arxiv.org/abs/2511.00177)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.00177)

> 医疗场景下的大语言模型（LLMs）常因训练数据偏差而对患者种族产生不当关联，现有提示工程难以触及内部表征，且思维链（CoT）解释往往不可信。本文切入点在于利用稀疏自编码器（SAE）定位并干预内部潜变量，以建立种族偏见的因果证据。通过重解释临床域潜变量并进行转向实验，论文证明了SAE能揭示CoT隐藏的偏见，但在复杂临床任务中缓解效果微弱。该工作验证了机制可解释性在医疗审计中的必要性，但其作为去偏工具的泛化能力存疑。

】

---

【CERTIFIED EVALUATION OF MODEL-LEVEL EXPLANATIONS FOR GRAPH NEURAL NETWORKS ｜模型级图神经网络解释的统计充分性评估

研究机构：印度统计研究所

作者：Sayan Saha、Sanghamitra Bandyopadhyay

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_14088874)

> 模型级解释旨在揭示分类器识别特定类别的全局模式，但现有评估过度依赖目标类得分，导致病理性原型被误判为有效解释。本文切入点在于传统实例级保真度指标在模型级场景下失效，且类得分无法区分高得分但偏离数据分布的解释。作者通过引入充分性风险泛函，推导了基于嵌入空间覆盖度的分布无关证书，并构建了Coverage、GGA与Overlap三个可计算指标。该框架在理论上填补了模型级解释评估的空白，但其对分类器头部Lipschitz常数的依赖及有限样本下界宽松性，限制了其在复杂非线性模型中的直接适用性。

】

---

【CERTIFIED VS. EMPIRICAL ADVERSARIAL ROBUST NESS VIA HYBRID CONVOLUTIONS WITH ATTENTION STOCHASTICITY ｜混合卷积与注意力随机性

研究机构：印度理工学院、新加坡南洋理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_18112457)

> 认证鲁棒性研究旨在解决深度学习模型对微小输入扰动的脆弱性，其核心矛盾从早期的攻防博弈演变为形式化保证强度与计算、精度成本之间的平衡。确定性方法提供紧致保证但牺牲表达能力，随机平滑方法可扩展但受限于噪声对语义的破坏，现有方案难以同时满足 $\ell_2$ 认证与强 $\ell_\infty$ 经验鲁棒性。本文提出 HyCAS，将随机性内化至 Lipschitz 约束架构内部，通过双阶段噪声注入实现混合防御。该方法在医疗影像等异构基准上验证了有效性，但其内部随机性对认证采样效率的影响及 $\ell_\infty$ 紧致认证的缺失仍是关键存疑点。

】

---

【Certified vs. Empirical Adversarial Robust-ness via Hybrid Convolutions with Attention Stochasticity ｜混合卷积与注意力随机性

研究机构：印度理工学院、新加坡南洋理工大学

作者：Joy Dhar、Song Xia、Manish Kumar Pandey 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01519)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.01519)

> 对抗鲁棒性研究长期面临认证保证与经验防御的二元对立：确定性方法提供紧致 $\ell_2$ 证书但牺牲精度，随机平滑（Randomized Smoothing, RS）可扩展但认证半径受限。HyCAS 通过架构内随机性注入，试图在单一模型中同时满足 $\ell_2$ 认证与 $\ell_\infty$ 经验鲁棒性。该方法将谱归一化卷积与内部随机投影、注意力噪声模块耦合，构建全局 $\le 2$-Lipschitz 网络。其价值在于弥合认证与经验防御的割裂，但 $\ell_2$ 认证半径在标准基准上显著低于专用 RS 方法，且缺乏 $\ell_\infty$ 证书的理论推导。

】

---

【Circuit Insights: Towards Interpretability Beyond Activations ｜基于权重与电路结构的自动解释框架

作者：Elena Golimblevskaia、Aakriti Jain、Bruno Puri 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.14936)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.14936)

> 大语言模型内部特征的自动解释长期依赖外部大模型对激活值的语义归纳，导致解释结果受数据集分布与提示词策略的强干扰。现有方法无法区分特征激活的结构性原因与偶然性噪声，且在处理上下文依赖特征时失效。本文提出 WeightLens 与 CircuitLens 框架，利用 Transcoder 的权重矩阵与电路归因结构直接生成特征描述，剥离对解释 LLM 的依赖。该方法在 Token 级特征上匹配或超越基线，但在上下文依赖特征的纯度与因果忠实度上存在显著局限。

】

---

【Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing ｜真实企业环境下的AI渗透测试代理评估

研究机构：美国斯坦福大学、美国卡内基梅隆大学

作者：Justin W. Lin、Eliot Krzysztof Jones、Donovan Julian Jasper 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09882)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09882)

> 现有AI安全基准多依赖CTF或静态漏洞复现，缺乏真实生产环境的噪声与交互性，导致模型能力评估失真。本文切入点在于构建首个真实企业网络中人类专家与AI代理的端到端对比实验，并引入ARTEMIS多智能体框架以克服现有代理在长时程任务中的上下文断裂问题。通过动态提示生成、并行子代理调度及自动漏洞分诊，ARTEMIS在约8,000主机的大学网络中实现了超越90%人类专家的渗透效果。该工作验证了LLM代理在复杂真实环境中的可行性，但其对GUI交互的依赖缺失及较高的误报率，揭示了当前自主攻击代理在“感知-执行”闭环中的结构性短板。

】

---

【CONVERGENT DIFFERENTIAL PRIVACY ANALYSIS FOR GENERAL FEDERATED LEARNING ｜联邦学习差分隐私的收敛性分析

研究机构：澳大利亚悉尼大学、新加坡南洋理工大学

作者：Yan Sun、Qixin ZHANG、Li Shen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_73052959)

> 联邦学习（Federated Learning, FL）结合差分隐私（Differential Privacy, DP）旨在解决数据不出域前提下的隐私泄露问题，但现有理论分析基于组合定理，导致隐私界随通信轮数 $T$ 发散，与实验观察到的隐私稳定性相悖。本文切入点在于利用 $f$-DP 框架与移位插值技术，证明 Noisy-FedAvg 和 Noisy-FedProx 在非凸目标下具有收敛的隐私下界。通过构建全局敏感性的数据与模型分解，本文揭示了局部正则化项对隐私收敛的关键作用。该工作填补了 FL-DP 长期训练隐私保证的理论空白，但其结论依赖于强平滑性假设，且未覆盖非 IID 数据下的具体隐私-效用权衡量化。

】

---

【CUPID: A Plug-in Framework for Joint Aleatoric and Epistemic Uncertainty Estimation with a Single Model ｜单模型插件式联合不确定性估计

研究机构：新加坡南洋理工大学

作者：Xinran Xu、Xiuyi Fan

论文原文见 [arXiv](https://arxiv.org/abs/2603.10745)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10745)

> 深度学习模型在医疗等高风险场景中常因过度自信导致误诊，核心矛盾在于如何在不修改或重训练骨干网络的前提下，同时量化数据固有噪声（偶然不确定性）与模型知识不足（认知不确定性）。现有方法要么依赖贝叶斯神经网络等重训练架构，要么仅估计单一类型不确定性，难以兼顾部署效率与解耦精度。CUPID 提出一种可插入预训练网络任意中间层的轻量模块，通过贝叶斯恒等映射学习偶然不确定性，并利用重构分支分析内部响应扰动来量化认知不确定性。该框架在医学影像分类与超分辨率任务上实现了优于传统基线的解耦性能，但其结论局限于 ResNet18 架构，缺乏与深度集成等金标准方法的直接对比，泛化性存疑。

】

---

【Curation Leaks: Membership Inference Attacks against Data Curation for Machine Learning ｜数据策展管道中的成员推断攻击

研究机构：Anthropic

作者：Dariush Wahdany、Matthew Jagielski、Adam Dziedzic 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00811)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00811)

> 数据策展旨在利用私有目标集筛选公共数据以提升模型效率，但这一过程本身可能泄露目标集成员信息。现有隐私审计聚焦于训练后的模型输出，忽视了数据选择阶段的中间产物（如策展分数、子集掩码）所携带的隐私信号。本文通过改造似然比检验（LiRA）并设计针对特定策展算法的定制化攻击，系统性地证明了从分数到最终模型的每一步均存在隐私泄露。该工作填补了数据选择阶段隐私评估的空白，但其攻击成功率受限于策展算法的线性特性与目标集规模，实际风险边界尚待厘清。

】

---

【Decomposing Representation Space into Interpretable Subspaces with Unsupervised Learning ｜无监督邻居距离最小化表示空间分解

研究机构：德国萨尔大学

作者：Xinting Huang、Michael Hahn

论文原文见 [arXiv](https://arxiv.org/abs/2508.01916)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2508.01916)

> 机制可解释性旨在解析模型内部计算逻辑，但现有方法或依赖人工假设、或受限于输入依赖的特征。本文指出表示空间存在“自然”的正交子结构，提出邻居距离最小化（Neighbor Distance Minimization, NDM）算法，通过优化正交矩阵使子空间内激活点聚集，从而无监督地发现可解释子空间。该方法在GPT-2 Small上实现了0.71的电路变量集中度，但在2B模型上的因果验证仍依赖特定知识冲突场景，其通用性尚存疑。

】

---

【DEFENDING AGAINST BACKDOOR ATTACKS VIA MODULE SWITCHING ｜模块交换防御

研究机构：澳大利亚麦考瑞大学、美国马萨诸塞大学阿默斯特分校

作者：Weijun Li、Ansh Arora、Xuanli He 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_29748465)

> 后训练范式下，用户获取的模型往往缺乏训练数据透明度，传统依赖原始数据或可信参考模型的防御手段失效。现有模型合并防御如权重平均（WAG）需3-6个同源模型且对共谋攻击鲁棒性不足。本文提出模块交换防御（MSD），通过进化搜索重组不同模型间的局部权重模块以切断后门捷径。该方法在少模型约束下显著优于WAG，但其对低投毒率场景的防御效能衰减及跨模态适用性仍存疑。

】

---

【Delta-XAI: A Unified Framework for Explaining Prediction Changes in Online Time Series Monitoring ｜在线时序预测变化归因框架

研究机构：韩国科学技术院、韩国成均馆大学

作者：Changhun Kim、Yechan Mun、Hyeongwon Jang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.23036)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.23036)

> 在线时序监控中，临床与金融决策者关注的是预测概率的*变化量*而非绝对值，但现有可解释人工智能（Explainable AI, XAI）方法仅能解释单步静态预测，无法量化驱动预测跃迁的特征贡献。直接对相邻时间步的归因分数做减法会产生物理上不可行的解释，且缺乏针对动态变化场景的忠实性评估标准。本文提出 Delta-XAI 框架，通过包装函数将 14 种现有 XAI 方法适配至预测变化解释任务，并设计 Shifted Window Integrated Gradients (SWING) 算法，利用回顾窗口作为基线进行分段积分以捕捉时序动态。该工作填补了在线时序解释的任务空白，但其自定义评估指标与领域通用基准的脱节，以及仅针对概率变化而非因果机制的解释深度，仍存疑。

】

---

【Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders ｜稀疏自编码器可解释性与转向效用的解耦分析

研究机构：香港中文大学

作者：Xu Wang、Yan Hu、Benyou Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03659)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03659)

> 大语言模型（LLM）内部表示的叠加特性导致神经元多义性，阻碍了直接基于神经元的机制理解与行为控制。稀疏自编码器（Sparse Autoencoder, SAE）通过过完备字典学习将密集激活分解为稀疏单义特征，成为解决这一难题的核心工具，但其特征的可解释性是否直接转化为模型转向（Steering）的效用，此前缺乏系统量化。本文通过训练90个SAE并计算可解释性分数与转向分数的秩相关性，揭示了二者间仅存在弱正相关，并提出了基于Token Confidence变化的特征筛选机制以弥补这一差距。该研究挑战了“高可解释性即高效用”的隐含假设，但其特征筛选方法在跨模型泛化性上仍存疑。

】

---

【DON T SHIFT THE TRIGGER: ROBUST GRADIENT AS CENT FOR BACKDOOR UNLEARNING ｜鲁棒梯度上升：防止触发器转移的后门遗忘机制

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_75824435)

> 文本分类模型在遭受后门攻击后，传统梯度上升（Gradient Ascent, GA）遗忘方法被广泛用于移除恶意触发器，但该方法存在一个被长期忽视的致命缺陷：它并未消除触发器，而是将其影响从目标类别“转移”到其他类别，导致模型在原本安全的输入上产生新的误分类。本文揭示了这一“触发器转移”现象，并提出了鲁棒梯度上升（Robust Gradient Ascent, RGA）算法，通过引入基于KL散度的动态惩罚机制自适应调节遗忘强度。RGA在多个数据集和模型规模上有效阻止了触发器转移，但其在多分类任务中的泛化能力及对检测误差的鲁棒性仍存疑。

】

---

【Doubly-Regressing Approach for Subgroup Fairness ｜双重回归对抗学习实现子群子集公平性

研究机构：韩国首尔大学

作者：Kunwoong Kim、Kyungseon Lee、Jihu Lee 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21091)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21091)

> 交叉公平性面临敏感属性维度增加导致的子群指数级增长，引发数据稀疏与计算负担双重困境。现有对抗公平性算法需为每个子群维护独立判别器或求解大规模 min-max 博弈，在高维场景下不可扩展。本文通过定义“子群子集”并引入单一判别器的双重回归机制，在保持分布公平性强度的同时规避了逐子群优化的计算瓶颈。该方法在极端稀疏子群场景下显著优于基线，但在非稀疏场景下性能优势收窄，且忽略非活跃子群可能掩盖少数群体的系统性偏差。

】

---

【DRIFT: Divergent Response in Filtered Transformations for Robust Adversarial Defense ｜梯度发散防御

研究机构：美国纽约大学

作者：Amira Guesmi、Muhammad Shafique

论文原文见 [arXiv](https://arxiv.org/abs/2509.24359)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24359)

> 随机化防御在自适应攻击下普遍失效，根源并非随机性不足，而是不同变换路径间存在“梯度共识”，使攻击者可通过期望变换（Expectation over Transformation, EoT）聚合出一致的攻击方向。现有方法或依赖手工设计非可微变换，或依赖高成本扩散模型，均无法在保持干净精度的同时破坏这种对齐。DRIFT 通过训练一组可微、轻量级滤波器，显式最大化滤波器间的雅可比与 Logit 空间梯度发散，从而在理论上降低对抗样本迁移率。该方案在 ImageNet 规模模型上实现了显著鲁棒性提升，但其对极端自适应攻击的长期有效性及滤波器规模扩展性仍存疑。

】

---

【Dual Randomized Smoothing: Beyond Global Noise Variance ｜双随机平滑：超越全局噪声方差

作者：Chenhao Sun、Yuhao Mao、Martin Vechev

论文原文见 [arXiv](https://arxiv.org/abs/2512.01782)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01782)

> 随机平滑（Randomized Smoothing, RS）在认证鲁棒性中面临全局噪声方差导致的精度-鲁棒性固有冲突，即小半径需小方差而大半径需大方差，单一全局参数无法兼顾两端。现有输入依赖方法或依赖测试时记忆，或自适应受限，或系统性高估最优方差。本文提出双随机平滑框架，通过预测输入依赖噪声方差并认证其局部常数性，打破全局方差限制。该方法在CIFAR-10和ImageNet上实现了跨半径的强性能，但引入了约60%的推理计算开销，且其理论保证依赖于方差估计器的稳定性认证。

】

---

【Efficient Credal Prediction through Decalibration ｜高效可信集预测：基于去校准的Logits扰动

研究机构：德国慕尼黑大学、德国人工智能研究中心

作者：Paul Hofman、Timo Löhr、Maximilian Muschalik 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08495)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08495)

> 在安全关键场景中，模型不仅需要给出预测，还需明确表达其知识边界，即区分数据固有噪声与模型认知不足。现有可信集（Credal Sets）方法虽能显式表示认知不确定性，但依赖昂贵的集成训练或贝叶斯后验采样，无法应用于CLIP、TabPFN等冻结参数的大规模基础模型。本文提出“去校准”（Decalibration）机制，通过单模型Logits扰动在相对似然预算内探索概率空间，无需重训练即可生成可信集。该方法在计算效率上提升数个数量级，但仅适用于分类任务，且Logits线性扰动能否充分捕捉复杂后验结构存疑。

】

---

【Efficient Estimation of Kernel Surrogate Models for Task Attribution ｜任务归因中的核代理模型

研究机构：美国东北大学

作者：Zhenshuo Zhang、Minxuan Duan、Hongyang R. Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2602.03783)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03783)

> 导读 多任务学习中，量化单个训练任务对下游性能的具体贡献是理解模型行为的关键，但直接的重训练评估在任务数量增加时计算成本呈线性增长，难以扩展。现有线性代理模型虽能捕捉一阶效应，却因假设任务间贡献可加性而忽略协同或拮抗等非线性交互，导致归因偏差。本文提出核代理模型（KERNELSM），通过径向基函数（RBF）核在任务子集空间建模非线性关系，并利用梯度作为特征实现无需重训练的高效估计。该方法在数学推理与强化学习基准上显著提升了归因精度，但其依赖一阶近似误差小于1%的假设，在极端损失景观下的鲁棒性仍存疑。

】

---

【Ensembling Pruned Attention Heads For Uncertainty-Aware Efficient Transformers ｜剪枝注意力头构建高效Transformer集成

作者：Firas Gabetni、Giuseppe Curci、Andrea Pilzer 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.18358)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18358)

> 在安全关键场景中，深度神经网络常对错误预测表现出过度自信，不确定性量化（UQ）旨在通过估计认知不确定性来缓解此风险。深度集成（Deep Ensembles）虽为UQ金标准，但其线性增长的计算与内存成本使其难以部署于大规模基础模型。本文切入点在于揭示朴素剪枝虽能保持精度却会损害校准，进而提出通过结构化剪枝注意力头生成多样子网络并融合为单一模型的方法。该框架在无需从头训练的情况下实现了接近单模型的推理成本，但在极端分布偏移下的多样性保持能力仍存疑。

】

---

【EVALUATING SAE INTERPRETABILITY WITHOUT EX PLANATIONS ｜无解释的稀疏自编码器可解释性评估

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_34104322)

> 稀疏自编码器（Sparse Autoencoder, SAE）特征评估长期依赖自然语言解释生成，导致评估结果受提示工程与解释器模型超参数干扰，无法直接反映特征本身的语义可区分性。现有方法将“解释质量”与“特征可解释性”耦合，难以区分是特征模糊还是解释生成失败。本文提出直接基于激活样本的评估范式，通过侵入者检测与示例嵌入评分量化特征的可区分性。该方法在人类与大型语言模型（Large Language Model, LLM）评估者间实现了0.83的高相关性，但仅验证了统计可区分性，未触及特征的因果有效性。

】

---

【Evaluating SAE interpretability without explanations ｜去解释化稀疏自编码器可解释性评估

论文原文见 [arXiv](https://arxiv.org/abs/2507.08473)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2507.08473)

> 稀疏自编码器（Sparse Autoencoder, SAE）通过过完备字典将密集激活分解为稀疏单义特征，但评估这些特征是否真正具备人类可解释性仍缺乏统一标准。现有主流评估流程依赖大型语言模型（Large Language Model, LLM）生成自然语言解释，再评估解释对预测特征激活的效用，这一间接路径引入了额外超参数，且隐含了“可解释性必须可被语言简洁表达”的强假设。本文提出入侵者检测（Intruder Detection）与示例嵌入评分（Example Embedding Scoring）两种无需生成自然语言解释的直接评估方法，通过测量人类或LLM区分激活样本与非激活样本的能力来量化可解释性。入侵者检测与人类判断的Pearson相关系数达到0.84，验证了去解释化评估的有效性，但示例嵌入评分的相关性仅为0.48，提示轻量级评估器在捕捉细粒度激活语义时存在局限。

】

---

【Fair Classification by Direct Intervention on Operating Characteristics ｜基于ROC凸包几何的公平分类后处理

研究机构：美国宾夕法尼亚大学

作者：Kevin Jiang、Edgar Dobriban

论文原文见 [arXiv](https://arxiv.org/abs/2509.25481)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25481)

> 群体公平性优化旨在消除模型在不同受保护群体间的预测偏差，但现有后处理方法往往在满足多个公平约束时导致准确率大幅下跌或计算复杂度激增。本文指出传统方法直接优化分类器参数忽略了预训练模型固有的几何结构，提出在操作特征空间（Operating Characteristic Space）中利用ROC凸包进行可行性搜索。该方法通过线性规划求解最优阈值组合，在保持准确率接近理论上限的同时，以极低的干预率实现了多指标近似公平。其价值在于提供了比现有基线更优的性能-公平权衡，但受限于静态数据假设，未解决动态环境下的公平性漂移问题。

】

---

【Fair Conformal Classification via Learning Representation-Based Groups ｜基于变分表示学习的公平保形分类

研究机构：南京大学

作者：Senrong Xu、Yanke Zhou、Yuhao Tan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.12195)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.12195)

> 保形预测（Conformal Prediction, CP）提供分布无关的边际覆盖保证，但无法捕捉算法偏见导致的子群体覆盖失衡。现有自适应公平保形方法受限于线性特征组合或离散特征假设，无法识别如“白人女性或黑人男性”这类非线性交叉偏差子群。FAREG 通过变分自编码器学习潜在表示以隐式定义群体，并构造自适应预测集，在保持预测集紧凑性的同时实现条件覆盖公平。该方法在合成与真实数据上优于基线，但其潜在群体的可解释性缺失及重构损失对少数群体特征的平滑效应，限制了其在高风险审计场景的直接应用。

】

---

【FAIR CONFORMAL CLASSIFICATION VIA LEARNING REPRESENTATION-BASED GROUPS ｜基于表示学习的公平保形分类

研究机构：南京大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_99469247)

> 保形预测（Conformal Prediction, CP）为机器学习模型提供分布无关的边际覆盖保证，但无法捕捉算法偏见导致的子群体覆盖失衡。现有自适应公平保形方法受限于线性或单特征子群定义，难以识别由非线性特征组合（如“白人女性或黑人男性”）构成的受歧视群体。本文提出 FAREG，通过变分自编码器学习潜在表示以隐式定义复杂子群，并调整预测集实现自适应等化覆盖。该方法在覆盖公平性与预测集效率间取得平衡，但其潜在表示的可解释性审计机制尚缺实证支撑。

】

---

【Fair in Mind, Fair in Action? A Synchronous Benchmark for Understanding and Generation in UMLLMs ｜统一多模态大语言模型同步公平性基准

研究机构：南京大学、香港中文大学

作者：Yiran Zhao、Lu Zhou、Xiaogang Xu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00590)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00590)

> 统一多模态大语言模型（UMLLMs）在处理理解与生成任务时共享表征空间，导致偏见在任务间系统性传播，但现有评估工具仅能孤立检测单任务偏见，无法量化这种跨任务耦合效应。IRIS Benchmark 通过构建高维“公平空间”，同步评估理解与生成任务在理想公平、现实保真度及偏见惯性三个维度上的表现，将碎片化的公平性指标转化为可比较的多目标权衡图谱。该框架揭示了 UMLLM 中普遍存在的“生成差距”与跨任务“人格分裂”现象，为诊断系统性偏见提供了新范式，但其评估结果高度依赖自建分类器的准确性，且缺乏与文本偏见基准的直接可比性验证。

】

---

【FAIRNESS VIA INDEPENDENCE: A GENERAL REGULAR IZATION FRAMEWORK FOR MACHINE LEARNING ｜基于柯西-施瓦茨散度的公平正则化框架

研究机构：美国加州大学尔湾分校、美国普渡大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_71125789)

> 群体公平性算法常面临指标冲突与参数扰动下的鲁棒性失效，现有独立性度量如KL散度或HSIC在模型微调时易导致公平性指标剧烈波动。本文切入点在于利用柯西-施瓦茨散度（Cauchy-Schwarz Divergence, CS）更紧的理论上界，构建对参数变化不敏感的通用公平正则化器。该方法通过最小化预测分布与敏感属性分布间的CS散度，实现了跨多种公平性定义的通用性。其价值在于提供了比传统度量更稳定的效用-公平权衡，但绝对精度仍低于领域SOTA，且未解决多属性交叉下的计算爆炸问题。

】

---

【FAITHFULNESS UNDER THE DISTRIBUTION: A NEW LOOK AT ATTRIBUTION EVALUATION ｜分布感知归因评估：FUD框架

研究机构：澳大利亚悉尼科技大学

作者：Zhiyu Zhu、Zhibo Jin、Jiayu Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_15417171)

> 归因方法评估长期依赖Insertion/Deletion等启发式指标，但这类指标通过置零或加噪生成中间样本，导致样本严重偏离数据分布，使模型输出变化反映的是对异常输入的响应而非真实特征依赖。FUD利用评分扩散模型重建掩码区域，强制评估样本保持在数据流形内，从而消除分布偏移对保真度评估的干扰。该方法在ResNet-50上将OOD检测AUROC从0.8974降至0.6863，显著提升了评估样本的分布内真实性。其价值在于揭示了现有评估协议的分布盲区，但依赖预训练扩散模型且未验证对归因方法本身排名的改变。

】

---

【FAME: Formal Abstract Minimal Explanation for Neural Networks ｜形式化抽象最小解释

研究机构：以色列耶路撒冷希伯来大学

作者：Ryma Boumazouza、Raya Elsaleh、Melanie Ducoffe 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10661)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10661)

> 溯因解释旨在定位保证模型预测不变的最小输入特征子集，但现有形式化方法受限于串行遍历顺序，无法扩展至大规模神经网络。FAME 通过引入基于抽象解释的批量特征释放机制，消除了对特征遍历顺序的依赖，实现了并行化剪枝。该方法结合贪心背包启发式与递归域精炼，在中等规模网络上显著降低了计算成本。尽管在 ResNet-2B 上展示了可行性，但抽象近似带来的解释尺寸膨胀及大规模 Transformer 上的表现仍存疑。

】

---

【FEATURE COMPRESSION IS THE ROOT CAUSE OF AD VERSARIAL FRAGILITY IN NEURAL NETWORKS ｜特征压缩导致神经网络对抗脆弱性的矩阵论解释

研究机构：美国爱荷华大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_6390570)

> 深度神经网络普遍存在对抗脆弱性，即微小扰动即可翻转分类结果，但现有理论解释（如梯度平滑性、非鲁棒特征）缺乏统一共识且无法解释为何基于这些解释的防御方法均失效。本文切入点在于将神经网络与理论最优分类器在最坏情况下的性能进行直接对比，而非仅关注平均情况与最坏情况的差距。通过随机矩阵论与QR分解，本文证明网络仅利用输入特征的压缩子集进行分类，导致其对抗鲁棒性随维度 $d$ 增加而退化至最优分类器的 $1/\sqrt{d}$。该理论为理解脆弱性根源提供了严格的数学界限，但其结论主要基于线性及特定假设下的非线性网络，对通用深层架构的普适性仍需进一步验证。

】

---

【Features Emerge as Discrete States: The First Application of SAEs to 3D Representations ｜3D表征中的离散状态特征分解

研究机构：英国剑桥大学、美国石溪大学

作者：Albert Miao、Chenliang Zhou、Jiawei Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.11263)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.11263)

> 稀疏自编码器（Sparse Autoencoder, SAE）旨在将大语言模型（LLM）的密集激活分解为稀疏、单义的特征，以解决神经元多义性导致的机制理解障碍。然而，现有研究局限于文本等离散词汇域，且仅关注特征“是什么”，忽略了模型“为何”选择特定特征的学习动态。本文首次将SAE应用于3D无序连续数据域，通过梯度分解揭示3D重建模型将连续空间离散化为状态空间的内在机制。该工作提供了特征学习动态的理论框架，但缺乏跨模型泛化验证，其离散化结论是否普遍适用仍存疑。

】

---

【FEDERATED GRAPH-LEVEL CLUSTERING NETWORK WITH DUAL KNOWLEDGE SEPARATION ｜联邦图级聚类中的双知识分离网络

研究机构：天津大学、吉林大学

作者：Xiaobao Wang、Renda Han、Ronghao Fu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_59712918)

> 联邦图级聚类（Federated Graph-level Clustering, FGC）旨在解决分布式环境下，因客户端内与客户端间数据异质性导致的服务器共识失败问题。现有方法如FedGCN和FedPKA试图最大化全局知识共享，却忽略了多图谱异质性，导致优化方向发散。本文提出FGCN-DKS，通过解耦不变子图与个性化子图，仅上传摘要信息并基于图核亲和度进行个性化聚合。该方法在TUDataset基准上显著优于现有FGC方法，但其隐私保护机制缺乏形式化保证，且未验证在极端异质性下的收敛性。

】

---

【FERD: FAIRNESS ENHANCED DATA-FREE ADVER SARIAL ROBUSTNESS DISTILLATION ｜无数据鲁棒性蒸馏中的公平性增强

研究机构：南京大学、新加坡南洋理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_35623311)

> 无数据鲁棒性蒸馏（DFRD）旨在不访问原始训练数据的前提下，将教师模型的对抗鲁棒性迁移至轻量级学生模型，以解决边缘设备部署中数据不可用与模型脆弱性并存的问题。现有DFRD方法仅关注整体鲁棒性，忽略了类别间鲁棒性差异被蒸馏过程显著放大的公平性缺陷。FERD通过鲁棒性引导的类别重加权与均匀目标对抗样本生成，在合成数据层面同时调节样本比例与分布，缓解类别鲁棒性偏差。该方法在CIFAR-10上实现了最弱类别鲁棒性的显著提升，但其公平性增益是否以牺牲整体平均鲁棒性为代价，以及重加权策略对教师-学生架构组合的依赖性，仍需进一步审视。

】

---

【FOREST-BASED GRAPH LEARNING FOR SEMI-SUPERVISED NODE CLASSIFICATION ｜基于森林的图学习

研究机构：香港科技大学

作者：Jin Li、Shenghao Gao、Kaichen Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_80376583)

> 现有图神经网络在捕获长程依赖时，面临局部堆叠模型计算不可并行与全局注意力模型复杂度呈二次方增长的结构性矛盾。本文指出该矛盾源于将图视为“结构融合”时的成本公式失衡，提出以生成树为中间介质的新范式。通过同配性引导的树采样与线性时间树聚合器，FGL在保持全局感受野的同时实现了线性计算复杂度。该方法在标准半监督节点分类基准上显著优于主流深度GNN与图Transformer，但其对同配性估计精度的强依赖及单中心设定，限制了其在极端异质或隐私敏感场景下的直接适用性。

】

---

【From Data Statistics to Feature Geometry: How Correlations Shape Superposition ｜从数据统计到特征几何：相关性如何塑造叠加

研究机构：英国帝国理工学院

作者：Lucas Prieto、Edward Stevinson、Melih Barsbey 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09972)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09972)

> 机制可解释性领域长期假设叠加表示中的特征干扰是必须通过非线性过滤消除的噪声，这一假设无法解释真实大语言模型中观察到的语义聚类与环形结构。现有稀疏自编码器（Sparse Autoencoder, SAE）研究聚焦于架构优化以最小化重构误差，却忽略了数据协方差结构对特征几何排列的根本性驱动作用。本文提出Bag-of-Words Superposition (BOWS)框架，通过受控的二值词袋数据实验，证明当特征存在相关性时，干扰可以是构造性的，模型会利用低秩结构实现高效重构。该工作揭示了叠加几何的成因，但受限于二值假设，其在连续激活空间中的普适性尚存疑。

】

---

【FROZEN PRIORS, FLUID FORECASTS: ｜冻结先验下的预序不确定性量化

研究机构：芬兰阿尔托大学、英国剑桥大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_65895554)

> 机器学习系统部署初期常面临真实数据稀缺，导致警报率等长期运行指标估计极不稳定。传统频率区间忽略部署规则，贝叶斯后验假设持续重拟合，保形预测仅提供单样本保证，均无法回答“系统长期表现如何”这一运维核心问题。本文提出预序不确定性量化框架，通过Dirichlet调度混合经验分布与冻结生成器，利用鞅后验模拟未来预测以量化长期指标的不确定性。该方法在GPT-2上以20个样本实现90%覆盖率，显著优于Bootstrap的37%，但仅适用于线性指标与冻结模型，对非线性决策效用的对齐能力存疑。

】

---

【GNN Explanations that do not Explain and How to find Them ｜自解释图神经网络的退化解释失效与检测

研究机构：奥地利维也纳技术大学

作者：Steve Azzolin、Stefano Teso、Bruno Lepri 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20815)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20815)

> 自解释图神经网络（Self-Explainable GNNs, SE-GNNs）旨在通过联合训练解释提取器与分类器，在高风险场景提供内在可解释性，但其解释可能完全脱离模型内部决策逻辑。现有保真度指标缺乏对已知不忠实解释的拒绝能力，导致这种“退化解释”失效模式长期未被识别。本文通过理论证明 SE-GNNs 可在最优损失下输出无判别力的锚点集解释，并构建基准测试现有指标失效，进而提出扩展充分性测试（Extension Sufficiency Test, EST）以可靠检测此类失效。该工作揭示了自解释架构的潜在信任危机，但 EST 仅评估充分性，对冗余型不忠实的覆盖能力存疑。

】

---

【GRADIENT-BASED DIVERSITY OPTIMIZATION WITH - DIFFERENTIABLE TOP _k_ OBJECTIVE ｜基于可微排序的梯度多样性优化

研究机构：瑞典皇家理工学院、瑞典乌普萨拉大学

作者：Tianyi Zhou、Sebastian Dalleiger、Ece Calikus 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_29094649)

> 推荐系统长期面临相关性最大化导致的输出同质化与长尾物品曝光不足问题。后处理重排序方法虽能提升多样性，但往往以牺牲相关性为代价，而模型特定的学习式方法则缺乏通用性且收敛缓慢。本文提出一种统一的可微框架，通过软排序松弛将多样性目标直接嵌入梯度训练，并引入自适应平衡参数确保相关性-多样性联合优化收敛。该框架在五个基准数据集上实现了多样性显著提升且相关性损失极小，但其静态权衡假设在动态交互场景中的有效性尚待验证。

】

---

【INCENTIVES IN FEDERATED LEARNING WITH HET EROGENEOUS AGENTS ｜异构联邦学习中的PAC激励对齐机制

研究机构：美国哈佛大学、美国马里兰大学帕克分校

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_98264922)

> 联邦学习面临数据异构导致的效用不可交换性，现有激励模型假设数据总量决定收益，忽略了“谁提供数据”对本地性能的影响。本文切入点在于构建基于PAC精度阈值的异构博弈框架，证明去中心化均衡的无界低效性，并设计基于线性规划（LP）的近似最优贡献分配机制。该机制在策略证明性上具有唯一性，但缺乏与工程化联邦算法的实证对比，其理论边界在隐私成本缺失下尚待检验。

】

---

【JOINT DISTRIBUTION-INFORMED SHAPLEY VALUES FOR SPARSE COUNTERFACTUAL EXPLANATIONS ｜基于联合分布信息的稀疏反事实解释框架

研究机构：丹麦技术大学、丹麦哥本哈根大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_80382675)

> 反事实解释（Counterfactual Explanations, CEs）旨在通过最小化输入扰动以翻转黑盒模型预测，但现有方法常修改过多特征，导致解释缺乏可操作性。传统特征归因（Feature Attributions, FAs）与CE生成过程解耦，导致归因重要性与实际翻转路径不一致，无法有效指导稀疏化编辑。本文提出COLA框架，利用最优传输（Optimal Transport, OT）构建事实与反事实集合间的耦合矩阵，驱动p-SHAP归因以筛选最小动作集。该方法在保持目标效果的前提下将特征编辑量降低至26–45%，但在动态环境与因果结构对齐上存在局限。

】

---

【Language Models are Injective and Hence Invertible ｜语言模型表示的单射性与精确逆推

研究机构：瑞士洛桑联邦理工学院、意大利罗马第一大学

作者：Giorgos Nikolaou、Tommaso Mencattini、Donato Crisostomi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15511)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15511)

> 导读 机制可解释性领域长期关注如何从内部激活中解读模型行为，但鲜有工作直接回答“输入信息是否在表示中无损保留”这一基础问题。主流观点认为 Transformer 的非线性组件必然导致信息坍缩，使得从隐状态精确恢复输入成为不可能任务。本文通过实分析证明标准解码器 Transformer 几乎必然单射，并据此设计 SIPIT 算法实现线性时间精确逆推。该工作将可逆性确立为架构固有属性，但其在量化模型与长序列下的泛化能力尚存疑。

】

---

【Layerwise Federated Learning for Heterogeneous Quantum Clients using Quorus ｜异构深度量子联邦学习框架 Quorus

研究机构：美国莱斯大学

作者：Jason Han、Nicholas S. DiBrita、Daniel Leeds 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06228)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06228)

> 量子联邦学习（Quantum Federated Learning, QFL）旨在解决私有数据分散且客户端量子硬件能力不一时的协同训练难题。现有方法假设客户端电路深度同质，忽略了噪声中间尺度量子（NISQ）设备因退相干导致的深度异构性，导致浅层客户端无法有效参与深层模型聚合。本文提出 Quorus，通过层级损失函数与反向蒸馏机制，在测量坍缩约束下对齐不同深度客户端的训练目标。该框架在真实 IBM 超导量子处理器上验证了可行性，但层级蒸馏在量子态不可克隆限制下的信息损失量化仍存疑。

】

---

【Learnability and Privacy Vulnerability are Entangled in a Few Critical Weights ｜权重回退与冻结的成员隐私防御

研究机构：美国北卡罗来纳州立大学

作者：Xingli Fang、Jung-Eun Kim

论文原文见 [arXiv](https://arxiv.org/abs/2603.13186)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13186)

> 成员推断攻击（MIA）利用模型对训练与非训练数据的行为差异泄露隐私，现有防御多采用全局重训练或差分隐私，导致效用与隐私的刚性权衡。本文发现隐私脆弱性仅存在于极少数权重，且这些权重与决定模型效用的关键权重高度重叠，导致传统剪枝失效。通过基于机器遗忘的权重级隐私评分，仅回退并冻结这些脆弱权重，再对剩余权重进行隐私微调，实现了优于从头训练的隐私-效用平衡。该方法在权重粒度上解耦了隐私与效用，但仅验证于分类任务，对生成式模型的适用性存疑。

】

---

【LEARNING DYNAMICS OF LOGITS DEBIASING FOR LONG-TAILED SEMI-SUPERVISED LEARNING ｜长尾半监督学习中的Logits去偏动力学与动态剪枝

研究机构：北京交通大学、西北工业大学

作者：Cheng Yue、Jiajun Zhang、Xiaohui Gao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_51097560)

> 长尾半监督学习（LTSSL）面临的核心困境是类别不平衡导致伪标签向多数类偏置，进而引发泛化性能崩塌。现有去偏方法如Logit调整或重加权仅修改梯度信号，未能解决样本级冗余对优化路径的持续干扰。本文切入点在于揭示偏差产生的动力学机制，将基线图像Logits作为累积偏差指示器，并据此提出动态剪枝框架DyTrim。该方法通过重分配梯度预算实现去偏，在标准基准上取得一致提升，但其理论保证依赖于特定网络结构假设，且未覆盖开放世界场景。

】

---

【LEARNING FOR HIGHLY FAITHFUL EXPLAINABILITY ｜摊销式解释的忠实度优化

研究机构：北京理工大学

作者：Yuhan Guo、Lizhong Ding、Shihao Jia 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_84810638)

> 摊销式解释旨在通过训练一个独立的解释器网络，在推理阶段以单次前向传播生成目标模型的归因，从而解决传统解释方法推理开销过大的问题。现有方法要么依赖对目标模型的理想化假设导致泛化性差，要么受限于先验解释信号的质量上限。本文切入点是将“忠实度”从评估指标转化为无假设的自监督优化目标，并设计动态联合优化策略整合监督信号。该方案在12个任务上实现了忠实度排名的显著提升，但其理论最优映射的蒙特卡洛近似在高维复杂模型下的收敛稳定性仍存疑。

】

---

【Learning Retrieval Models with Sparse Autoencoders ｜稀疏潜在检索

作者：Thibault Formal、Maxime Louis、Hervé Dejean 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13277)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13277)

> 学习稀疏检索（LSR）旨在通过高维稀疏向量实现高效且可解释的文档检索，但现有方法受限于固定词表，在多语言及跨域场景中泛化能力不足。本文指出，大语言模型（LLM）中的稀疏自编码器（Sparse Autoencoder, SAE）能提取出语言无关的单义潜在特征，为突破词表瓶颈提供了新路径。SPLARE通过冻结预训练SAE编码器替代语言建模头，将输入映射至潜在特征空间，并采用蒸馏策略微调LLM以优化检索相关性。该方法在MMTEB多语言检索任务中超越了基于词表的SPLADE基线，但其性能高度依赖SAE特征质量，且未解决特征因果有效性的验证问题。

】

---

【LipNeXt: Scaling up Lipschitz-based Certified Robustness to Billion-parameter Models ｜无约束流形优化与无卷积架构的Lipschitz认证扩展

研究机构：美国卡内基梅隆大学

作者：Kai Hu、Haoqi Hu、Matt Fredrikson

论文原文见 [arXiv](https://arxiv.org/abs/2601.18513)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18513)

> 确定性认证路线长期受困于模型规模扩展时的计算开销与表达能力瓶颈，导致其在ImageNet等大规模基准上性能显著落后于随机平滑方法。LipNeXt通过直接在正交流形上优化参数以消除重参数化开销，并引入无卷积的空间移位模块替代FFT卷积，解决了大规模训练中的数值不稳定与计算冗余问题。该方法在保持1-Lipschitz紧致保证的前提下，将认证模型扩展至十亿参数级别，实现了确定性认证在大规模数据上的性能突破，但其对复杂空间纹理的建模能力仍受限于移位操作的局部性。

】

---

【LLMs Process Lists With General Filter Heads ｜列表过滤的模块化机制：Filter Heads 与谓词编译

研究机构：美国东北大学

作者：Arnab Sen Sharma、Giordano Rogers、Natalie Shapira 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26784)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26784)

> 机制可解释性（Mechanistic Interpretability, MI）旨在通过逆向工程揭示 Transformer 内部计算机制，以打破大语言模型的黑盒性质。现有电路发现范式多聚焦于序列依赖任务，难以解释模型如何处理无固定顺序的集合操作，且缺乏对抽象语义谓词如何被“编译”为可复用几何表示的因果证据。本文通过激活修补定位中间层的稀疏注意力头（Filter Heads），证明其 Query 状态编码了可跨语言、跨格式移植的谓词表示。这一发现验证了 Transformer 存在模块化计算原语，但仅局限于语义过滤场景，未覆盖非线性算术或长程状态追踪。

】

---

【Low-pass Personalized Subgraph Federated Recommendation ｜低通个性化子图联邦推荐

研究机构：韩国成均馆大学

作者：Wooseok Sim、Hogun Park

论文原文见 [arXiv](https://arxiv.org/abs/2603.20338)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20338)

> 联邦推荐系统（FRS）在数据隔离前提下训练分布式模型，但客户端子图在规模与连接度上的剧烈差异导致空间图神经网络（GNN）表征错位，进而引发收敛不稳定与局部流行度偏差。现有方法如FedPerGNN假设子图结构可比，PFedRec侧重参数个性化却忽略拓扑异质性，均无法有效应对这种结构性不平衡。LPSFed通过低通频谱滤波提取稳定的结构信号，结合局部流行度偏差感知损失，实现自适应参数聚合与偏差校正。该方法在异构子图场景下显著提升了推荐精度，但在均匀数据分布下的绝对优势尚存疑。

】

---

【Measuring Uncertainty Calibration ｜有限样本下 $L_1$ 校准误差的分布无关上界

作者：Kamil Ciosek、Nicolò Felicioni、Sina Ghiassian 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.13872)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13872)

> 导读 校准误差的统计估计长期受困于分箱策略的任意性与渐近假设的失效，导致现有指标无法在有限数据下提供可靠的量化保证。本文切入点在于将校准函数视为具有特定结构（有界变差或可扰动平滑）的信号，通过构造代理函数并应用集中不等式，首次实现了分布无关的非渐近上界。方法核心是利用总变差去噪或核平滑重构校准函数，结合输出扰动强制满足导数约束。该工作填补了理论保证与实用评估之间的空白，但实际数据上界较宽（约 0.02），其决策价值在低错误率场景下仍存疑。

】

---

【MISSING MASS FOR DIFFERENTIALLY PRIVATE DOMAIN DISCOVERY ｜差分隐私域发现的效用保证

研究机构：谷歌研究院、美国密歇根大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_86914899)

> 现代数据分析常面对查询、评论等先验未知或规模巨大的数据域，域发现是下游分析的前置步骤，但差分隐私（Differential Privacy, DP）约束下如何量化算法的恢复能力长期缺乏理论支撑。现有DP集合并集算法多依赖经验验证或相对效用比较，无法回答“算法能恢复多少数据质量”这一根本问题。本文通过将效用指标从计数重构为缺失质量（Missing Mass），为加权高斯机制（Weighted Gaussian Mechanism, WGM）证明了首个绝对效用保证，并扩展至Top-k与k-命中集问题。该工作填补了DP域发现从经验到理论的空白，但其保证依赖Zipfian分布假设，在非幂律数据上的适用性存疑。

】

---

【Missingness Bias Calibration in Feature Attribution Explanations ｜缺失性偏差校准

研究机构：美国宾夕法尼亚大学、美国德克萨斯大学奥斯汀分校

作者：Shailesh Sridhar、Anton Xue、Eric Wong

论文原文见 [arXiv](https://arxiv.org/abs/2603.04831)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04831)

> 扰动式特征归因方法在消融输入时，常因模型对分布外（Out-of-Distribution, OOD）输入的预测偏移而失效，这一现象被称为缺失性偏差（Missingness Bias）。现有缓解方案多依赖高昂的模型重训练或架构修改，难以适配黑盒API模型。本文提出MCal，通过微调冻结基座模型的线性输出头，以极低成本修正输出空间的类别分布偏移。该方法在医疗多模态基准上表现优于重训练基线，但其线性假设能否捕捉高阶特征交互仍存疑。

】

---

【MULTI-FEATURE QUANTIZED SELF-ATTENTION FOR FAIR LARGE LANGUAGE MODELS ｜多特征量化自注意力正则化

研究机构：韩国延世大学

作者：Jaeil Park、Sung-Bae Cho

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_58431941)

> 大语言模型（LLM）在冻结状态下仍会因自注意力机制纠缠敏感属性与语义内容，导致多属性社会偏见持续存在。现有去偏方法要么依赖昂贵的骨干微调，要么仅作用于输入或解码阶段，无法在保持语义完整性的同时联合消除性别、种族等多重交叉偏见。MQAR 通过在冻结 LLM 的自注意力层前插入向量量化瓶颈与对抗自编码器，以无参数修改的方式实现多属性联合去偏。该方法在五个主流 LLM 上验证了偏见抑制的有效性，但其对低资源语境及动态语境扰动下的鲁棒性缺乏实证支撑。

】

---

【NASTY ADVERSARIAL TRAINING: A PROBABILITY - SPARSITY PERSPECTIVE FOR ROBUSTNESS ENHANCE MENT ｜恶意对抗训练：概率稀疏性视角下的鲁棒性增强

研究机构：哈尔滨工业大学、澳大利亚格里菲斯大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_81089854)

> 对抗训练（Adversarial Training, AT）旨在通过最小化最坏情况风险提升模型对微小扰动的抵抗能力，但现有方法多聚焦于损失函数或优化器层面的调整，忽视了输出概率分布的几何属性对鲁棒性的潜在贡献。本文切入点在于揭示“恶意训练”（Nasty Training, NT）中诱导的概率稀疏性具有空间度量意义，即稀疏分布意味着更大的类间分离度与决策边界距离。通过引入辅助对抗模型最大化目标模型与辅助模型输出的散度，NAT将概率稀疏性转化为AT的正则化机制。该方法在CIFAR-100上取得了超越现有基线的鲁棒精度，但在CIFAR-10上未达领域最高水平，其增益是否源于类别数增加带来的边界复杂度差异尚存疑。

】

---

【NEAR OPTIMAL ROBUST FEDERATED LEARNING AGAINST DATA POISONING ATTACK ｜联邦学习数据投毒的分布匹配防御

研究机构：清华大学

作者：Jingfan Yu、Zhixuan Fang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_65673039)

> 联邦学习面临数据投毒威胁，传统鲁棒聚合依赖高维梯度异常检测，在模型规模扩大时失效。本文指出数据投毒中梯度忠实反映数据集状态，提出基于数据集方差的判别器机制替代梯度过滤。该机制在IID和Non-IID设置下渐近匹配攻击损失极小极大下界，并引入有效投毒率量化攻击者收益。其理论保证依赖于投毒比例小于1/3的假设，且判别器训练引入的额外计算开销在大规模场景下的实际影响尚未充分验证。

】

---

【No Prior, No Leakage: Revisiting Reconstruction Attacks in Trained Neural Networks ｜无先验无泄露：重审训练神经网络中的重构攻击

研究机构：以色列特拉维夫大学、以色列内盖夫本-古里安大学

作者：Yehonatan Refael、Guy Smorodinsky、Ofir Lindenbaum 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21296)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21296)

> 隐式偏差驱动的数据重构攻击旨在从模型参数中直接恢复训练样本，但现有理论无法解释其成功条件。Haim et al. (2023) 提出的KKT重构方法虽在实证上有效，却缺乏对解空间唯一性的严格证明，导致隐私风险量化存在盲区。本文通过构造性证明揭示该目标函数存在无穷多全局极小值，证明在无数据域先验知识时，重构结果与真实训练集距离可任意大。这一发现修正了“隐式偏差必然泄露”的固有认知，但仅验证了特定架构下的理论边界，对大规模生成模型的适用性存疑。

】

---

【ON THE TRADE OFF BETWEEN EXPRESSIVITY AND PRIVACY IN GRAPH REPRESENTATION LEARNING ｜图表示学习中表达力与隐私的权衡

研究机构：奥地利维也纳技术大学、奥地利维也纳大学

作者：Patrick Indri、Tamara Drucks、Thomas Gärtner

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_89268668)

> 图表示学习面临一个根本性矛盾：高表达力算法需区分结构微小的非同构图，而差分隐私（Differential Privacy, DP）要求相似图产生相似输出。现有DP图学习方法仅优化效用，缺乏对表达力边界的理论刻画，导致隐私预算分配盲目。本文切入点在于利用同态密度向量的数学性质，构建同时满足期望表达力与边级DP保证的嵌入框架。通过校准噪声至同态密度的局部敏感度，本文证明了表达力与隐私之间存在显式权衡：模式类越具表达力，所需噪声越大。该工作填补了图隐私理论空白，但其效用验证局限于小规模分子与社交网络，未触及大规模图或GNN训练场景。

】

---

【PARADIGM SHIFT OF GNN EXPLAINER FROM LABEL SPACE TO PROTOTYPICAL REPRESENTATION SPACE ｜从标签空间到原型表示空间的图神经网络解释器优化范式

研究机构：中南大学、香港理工大学

作者：Jun Yin、Senzhang Wang、Ziluowen Luo 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_3030911)

> 后验实例级图神经网络解释器旨在识别驱动预测的关键子图，但主流方法受限于标签空间的离散性，无法充分捕捉拓扑结构信息。现有方案在优化解释器时，往往忽略了解释子图与输入图在表示空间中的分布偏移及结构纠缠问题。IDEA 提出将优化目标从标签一致性转移至原型表示空间，通过层级图分词器解耦解释性结构并统一分布对齐。这一范式转移在多个基准上显著提升了解释精度，但其对分布外泛化能力的验证尚存空白。

】

---

【PERSPECTRA: A SCALABLE AND CONFIGURABLE PLURALIST BENCHMARK OF PERSPECTIVES FROM ARGUMENTS ｜多元主义视角区分基准

研究机构：德国波恩大学、英国谢菲尔德大学

作者：Shangrui Nie、Kian Omoomi、Lucie Flek 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_85127312)

> 大语言模型在部署中常将多元观点同质化为单一“平均”答案，现有评估基准依赖高成本人工标注或局限于静态调查数据，难以规模化捕捉真实语境的视角多样性。本文切入点在于利用辩论平台结构结合真实社区语料，构建可配置的动态评估资源。通过检索-扩展管道生成3,810个自然主义论证变体，并定义观点计数、匹配与极性检查三项任务。该基准揭示了模型在语义归一化上的系统性失效，但生成器引入的潜在偏见污染了基准的中立性。

】

---

【PolySHAP: Extending KernelSHAP with Interaction-Informed Polynomial Regression ｜多项式回归扩展的Shapley值估计

研究机构：美国纽约大学

作者：Fabian Fumagalli、R. Teal Witter、Christopher Musco

论文原文见 [arXiv](https://arxiv.org/abs/2601.18608)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18608)

> 现有Shapley值近似方法受限于线性假设，无法捕捉特征间的高阶非线性交互，导致在复杂模型中归因精度不足。KernelSHAP等主流方法仅拟合一阶线性函数，忽略了特征协同效应对预测的贡献。本文通过引入高阶多项式回归替代线性近似，并证明了配对采样策略与二阶多项式拟合的数学等价性，从而在理论层面解释了该启发式策略的有效性。该方法在低维交互显著场景下提升了估计精度，但在高维特征空间中因计算复杂度限制，其增益幅度受到制约。

】

---

【Priors in Time: Missing Inductive Biases for Language Model Interpretability ｜时序特征分析（TFA）：修正稀疏自编码器的时间先验

研究机构：美国哈佛大学、瑞士洛桑联邦理工学院

作者：Ekdeep Singh Lubana、Can Rager、Sai Sumedh R. Hindupur 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.01836)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01836)

> 稀疏自编码器（Sparse Autoencoder, SAE）旨在从大语言模型（LLM）激活中提取单义特征，但其隐含的独立同分布（i.i.d.）时间先验与语言数据的非平稳时序结构存在根本冲突，导致特征分裂等病理现象。现有架构优化（如Gated SAE）仅改善重构保真度，未触及这一生成假设层面的缺陷。本文通过贝叶斯视角揭示该冲突，并提出时序特征分析（Temporal Feature Analysis, TFA）协议，将激活分解为可预测与新颖两个正交成分，以显式建模时序相关性。该工作从理论层面挑战了SAE作为通用解释工具的有效性边界，但其对因果干预有效性的验证仍显不足。

】

---

【PROBABILITY DISTRIBUTIONS COMPUTED BY AUTOREGRESSIVE TRANSFORMERS ｜Transformer 自回归表达力边界

研究机构：美国圣母大学

作者：Andy Yang、Anej Svete、Jiaoda Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_62014494)

> 现有 Transformer 表达力理论将模型简化为布尔分类器，忽略了其作为概率语言模型的核心自回归特性。这种简化导致理论结论无法直接迁移至实际应用，且掩盖了实数权重下分类器与自回归模型表达力的本质差异。本文通过引入状态编码器统一框架，系统对比了布尔与实数半环下分类器与自回归模型的表达力边界。该工作填补了理论空白，但受限于理想化架构假设，未验证非线性激活对等价性的破坏。

】

---

【PROTECTION AGAINST SOURCE INFERENCE ATTACKS IN FEDERATED LEARNING ｜联邦学习中源推断攻击的无噪声防御

研究机构：荷兰代尔夫特理工大学

作者：Andreas Athanasiou、Kangsoo Jung、Catuscia Palamidessi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_36280547)

> 联邦学习（Federated Learning, FL）中，诚实但好奇的服务器可通过源推断攻击（Source Inference Attack, SIA）识别数据归属，而现有差分隐私（Differential Privacy, DP）方案因需极大噪声才能消除模型间分布差异，导致效用崩溃且无法彻底阻断攻击。本文切入点在于指出标准Shuffle模型在异构数据下可被逆向重映射，从而失效。通过引入剩余数系统（Residue Number System, RNS）编码与参数级Shuffle，服务器仅能获取聚合和，无法还原单个模型，将SIA成功率降至随机猜测水平。该方案在保持模型精度损失小于3%的同时，提供了无噪声的隐私保护，但其依赖Shuffler的信任假设限制了在无Shuffler场景下的适用性。

】

---

【ProtoTS: Learning Hierarchical Prototypes for Explainable Time Series Forecasting ｜层级原型时间序列预测框架

研究机构：中国人民大学、阿里巴巴集团

作者：Ziheng Peng、Shijie Ren、Xinyue Gu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23159)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23159)

> 高利害场景下的时间序列预测模型往往因黑盒特性阻碍专家信任，而现有可解释方法多局限于单步归因或单一变量类型，无法揭示外生变量交互如何塑造整体预测曲线。ProtoTS 通过构建层级化原型网络，将预测任务转化为对典型时间模式的匹配与加权，实现了全局趋势解释与局部细节捕捉的统一。该框架在 LOF 数据集上将 MAE 降低 32%，并验证了专家通过编辑原型结构可进一步降低 MSE 0.009。其价值在于将解释从“事后归因”转变为“模型内在结构”，但缺乏与同类内在可解释架构的直接精度对比，且原型数量的选择依赖人工经验。

】

---

【Provably Explaining Neural Additive Models ｜可证明的最小充分解释：基于神经加性模型的对数级验证算法

研究机构：以色列耶路撒冷希伯来大学、德国慕尼黑工业大学

作者：Shahaf Bassan、Yizhak Yisrael Elboher、Tobias Ladner 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.17530)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.17530)

> 形式化可解释性（Formal XAI）旨在为神经网络预测提供具有数学保证的解释，但通用网络中生成基数最小充分解释需指数级验证查询，导致计算不可行。现有方法多退而求其次，仅生成子集最小解释或依赖采样近似，缺乏严格的充分性保证。本文利用神经加性模型（NAM）的加性结构，将对数级并行的区间重要性排序与二分搜索结合，首次实现了NAM上基数最小充分解释的高效生成。该方法在表格数据上验证了显著的效率与解释紧凑性优势，但其适用性严格受限于NAM架构，且未与主流统计归因方法（如SHAP）进行直接对比。

】

---

【RedSage: A Cybersecurity Generalist LLM ｜RedSage：基于智能体增强数据工程的网络安全通用大语言模型

研究机构：德国波恩大学、美国纽约大学

作者：Naufal Suryanto、Muzammal Naseer、Pengfei Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.22159)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22159)

> 导读 网络安全运营面临专家技能短缺与敏感数据隐私合规的双重约束，现有方案要么依赖存在数据泄露风险的专有API，要么使用缺乏深度领域适配的开源模型。本文切入点在于构建一个完全本地化、开源且覆盖知识、技能与工具操作全维度的8B参数安全专用模型。通过大规模领域持续预训练结合智能体驱动的多轮对话数据增强，RedSage在保持通用推理能力的前提下实现了安全任务的性能突破。其价值在于提供了可复现的端到端数据工程范式，但智能体生成数据的潜在幻觉偏差及缺乏检索增强生成机制对时效性知识的处理仍是存疑点。

】

---

【REDUCING INFORMATION DEPENDENCY DOES NOT CAUSE TRAINING DATA PRIVACY. ADVERSARIALLY NON-ROBUST FEATURES DO. ｜降低信息依赖不导致训练数据隐私，对抗非鲁棒特征才是根源

研究机构：美国达特茅斯学院

作者：Rasmus Torp、Shailen Smith、Adam Breuer

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_77460358)

> 高分辨率图像模型中，训练数据泄露的根源长期被归因于模型对输入信息的过度记忆，但现有防御机制在降低信息依赖指标的同时并未真正阻断重构攻击。本文通过因果实验证明，泄露源于模型对对抗非鲁棒特征的依赖，而非数据记忆本身。作者提出反向对抗训练（AT-AT），通过主动抑制鲁棒特征来换取隐私保护，在保持高精度的同时大幅降低重构成功率。这一发现颠覆了信息瓶颈防御的理论基础，但引入了对抗鲁棒性下降的代价，其实际部署中的权衡边界尚待明确。

】

---

【RELIABLE PROBABILISTIC FORECASTING OF IRREGULAR TIME SERIES ｜不规则时序概率预测的边际化一致性流模型

研究机构：德国柏林工业大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69909749)

> 不规则时序概率预测要求模型在任意时间点与变量子集上给出联合分布，但现有高表达力模型常因缺乏边际化一致性而产生逻辑矛盾的预测。ProFITi等基于归一化流的方法虽能拟合复杂联合分布，却无法保证子集边际与直接预测一致，导致临床等场景下的决策不可靠。MOSES通过混合分离流架构，将变量间依赖完全交由潜变量高斯分布捕捉，流变换仅调整边际形状，从结构上强制实现边际化一致性。该设计在保持联合预测竞争力的同时，显著提升了边际预测的可靠性，但其分离约束是否限制了高阶非线性依赖的捕捉能力，仍存疑。

】

---

【RETHINKING MODEL CALIBRATION THROUGH SPECTRAL ENTROPY REGULARIZATION IN MEDICAL IMAGE SEGMENTATION ｜频域视角下的医学图像分割模型校准

研究机构：北京邮电大学、英国爱丁堡大学

作者：Kun Cheng、Yukun Zhang、William Nailon 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_68652065)

> 医学图像分割模型在病灶边界处普遍存在过度自信，导致临床决策风险。现有空间域校准方法（如标签平滑、Focal Loss）无法捕捉频率维度的不确定性信息，且后处理校准难以适应解剖结构变异。本文从频域切入，指出“频谱偏置”与“置信度饱和”是失准根源，提出频谱熵正则化与功率谱平滑机制。该方法在六个医学数据集上同时提升了分割精度与校准质量，但其频谱丰富度与真实概率一致性的理论关联尚待验证。

】

---

【RETHINKING PARETO FRONTIER: ON THE OPTIMAL - TRADE OFFS IN FAIR CLASSIFICATION ｜混淆向量凸优化下的模型特定帕累托前沿

研究机构：美国普渡大学

作者：Junyi Chai、Shenyu Lu、Xiaoqian Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_20993361)

> 在静态分类任务中，公平性约束与预测性能之间存在固有的数学张力，但现有方法未能精确量化这种张力的理论边界。Kim et al. (2020) 等基于后处理构建的前沿存在次优性，导致无法作为评估公平性干预措施的有效上界。本文通过将帕累托优化重构为关于混淆向量的凸优化问题，推导了模型特定的最佳可达准确率边界，并提出了基于组依赖偏置的最后一层重训练框架。该工作提供了更严谨的理论参照系，但其等方差假设限制了在高维非线性数据上的直接适用性。

】

---

【REVISITING CONFIDENCE CALIBRATION FOR MISCLAS SIFICATION DETECTION IN VLMS ｜面向误分类检测的视觉语言模型置信度重校准

研究机构：电子科技大学、东南大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_13689130)

> 视觉语言模型（VLM）在高风险场景部署时，其预测置信度往往无法有效区分正确与错误预测，导致误分类检测（Misclassification Detection, MisD）性能受限。现有校准方法追求概率与准确率的对齐，但理论分析表明这种对齐反而限制了MisD的精度上限。本文通过重新定义可靠性曲线的几何意义，提出一种最大化正确/错误预测分离度的新校准目标，并设计可微代理损失与轻量级后处理元网络实现优化。该方法在多个细粒度数据集上显著提升了MisD指标，但牺牲了传统校准的概率解释性，其统计保证的缺失值得警惕。

】

---

【ROBUST ADVERSARIAL ATTACKS AGAINST UNKNOWN DISTURBANCES VIA INVERSE GRADIENT SAMPLE ｜逆梯度采样对抗攻击

研究机构：哈尔滨工业大学、中国科学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_68340816)

> 可迁移对抗攻击旨在解决黑盒场景下攻击者无法获取目标模型参数时的安全威胁，其核心在于利用代理模型生成的扰动误导未知模型。现有方法在遭遇未知扰动时极易失效，本文切入点是通过逆梯度采样高效定位最具破坏性扰动方向。具体做法是迭代采样扰动并沿该方向优化对抗样本。价值判断：该方法在鲁棒性维度显著优于基线，但峰值迁移率低于当前SOTA，且理论假设在深层网络非凸景观中的适用性存疑。

】

---

【Robust Federated Inference ｜联邦推理中的拜占庭鲁棒聚合

研究机构：瑞士洛桑联邦理工学院、丹麦哥本哈根大学

作者：Akash Dhasade、Sadegh Farhadkhani、Rachid Guerraoui 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00310)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00310)

> 联邦推理（Federated Inference, FI）旨在聚合多个本地模型的预测结果以生成最终输出，但现有方案普遍缺乏对恶意客户端篡改输出的防御机制，导致系统在面对拜占庭攻击时极易失效。本文切入点在于将FI的鲁棒性分析形式化，并指出传统鲁棒平均在非线性聚合器下存在理论盲区。通过提出DeepSet-TM架构，结合对抗训练与测试时鲁棒平均，该方法在多个基准上显著提升了最坏情况下的准确率。其价值在于填补了FI鲁棒性研究的空白，但实验仅覆盖静态客户端设置，未验证动态身份变化下的泛化能力。

】

---

【SELF-CONSISTENCY IMPROVES THE TRUSTWORTHINESS OF SELF-INTERPRETABLE GNNS ｜自一致性微调提升自解释图神经网络可信度

研究机构：电子科技大学、美国爱荷华州立大学

作者：Wenxin Tai、Ting Zhong、Goce Trajcevski 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_95822651)

> 自解释图神经网络（Self-Interpretable GNNs, SI-GNNs）旨在通过端到端联合训练生成内置解释，但其训练目标（交叉熵加简洁性正则）与评估指标（忠实性）存在根本错位。现有方法虽能生成解释，却常因解释冗余导致预测不稳定，无法保证解释的真实反映模型决策逻辑。本文提出自一致性（Self-Consistency, SC）微调策略，通过强制模型对同一输入两次生成一致解释来直接优化忠实性。该方法无需修改架构，在多个基准上显著提升了解释质量，但其效果高度依赖简洁性正则的强度，且未验证因果有效性。

】

---

【SERI: GRADIENT-FREE SENSITIVE REGION IDENTIFI CATION IN DECISION-BASED BLACK-BOX ATTACKS ｜敏感区域识别（SeRI）：决策基黑盒攻击中的连续敏感度优化

研究机构：北京邮电大学、新西兰惠灵顿维多利亚大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_90998287)

> 决策基黑盒攻击受限于仅能获取Top-1标签且查询预算严格受限，导致传统全局搜索策略难以精准定位对模型预测影响最大的图像区域，造成扰动幅度大且查询效率低。现有方法如PAR采用二值判定，无法反映像素级连续重要性，限制了扰动的细粒度优化。本文提出SeRI，通过基于决策边界的连续敏感度定义与递归区域细分机制，在无需梯度或代理模型的前提下实现像素级扰动权重分配。该方法作为插件显著提升了基线攻击器的效率，但其有效性依赖于基础攻击器的初始扰动质量，且在对抗训练模型上的增益机制尚需进一步理论解释。

】

---

【SMOOTH CALIBRATION ERROR: UNIFORM CONVER GENCE AND FUNCTIONAL GRADIENT ANALYSIS ｜平滑校准误差的均匀收敛与功能梯度分析

研究机构：日本大阪大学、日本理化学研究所

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_93751320)

> 校准理论长期受困于分箱期望校准误差（ECE）的统计不稳定性与泛化界缺失。现有后处理校准方法缺乏有限样本下的理论保证，而基于总体风险的分析无法指导实际算法训练。本文切入点在于将平滑校准误差（Smooth CE）与功能梯度范数建立直接联系，通过均匀收敛界将校准问题转化为可优化的有限样本问题。该框架为梯度提升树、核提升及两层神经网络提供了同时保证精度与校准的充分条件，但受限于二元分类设定与强边际假设，其向多分类及非平稳分布的扩展性尚存疑问。

】

---

【SMOTE AND MIRRORS: EXPOSING PRIVACY LEAK AGE FROM SYNTHETIC MINORITY OVERSAMPLING ｜SMOTE的几何隐私泄露：从插值到完美重建

研究机构：英国伦敦大学学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_71333925)

> 合成数据生成旨在从敏感数据中构建统计等价且隐私安全的替代数据集，其核心张力在于数据驱动模型对海量标注的依赖与隐私法规刚性约束之间的冲突。现有评估实践依赖距离最近记录（Distance to Closest Record, DCR）或朴素分类器来衡量隐私风险，但这些指标仅捕捉分布层面的差异，完全忽视了记录级的几何结构泄露。本文切入点在于揭示SMOTE插值机制固有的共线性特征，通过利用这一几何属性设计专用攻击，证明现有隐私评估体系对非隐私生成算法存在系统性盲区。具体做法是构建基于共线性检测的区分与重建算法，在仅访问单次生成数据且知晓SMOTE参数的极弱假设下，实现对真实少数类记录的完美识别与高置信度恢复。该工作挑战了将SMOTE作为隐私基线的行业惯例，但其在高维稀疏数据下的几何假设有效性及向其他插值生成方法的推广性仍存疑。

】

---

【SPARLING: END TO-END SPATIAL CONCEPT LEARN ING VIA EXTREMELY SPARSE ACTIVATIONS ｜稀疏局部潜变量可识别性

研究机构：美国麻省理工学院、美国宾夕法尼亚大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_38827911)

> 深度学习模型常通过端到端监督学习中间表示，但这些表示往往不透明且无法映射到具体概念。现有概念瓶颈模型依赖中间概念的人工标注，而真实场景中概念往往未知或难以穷举，导致模型无法在无监督条件下恢复语义中间状态。本文提出SPARLING算法，通过强制极稀疏激活与局部性约束，证明在特定假设下可从端到端误差中唯一识别中间概念。该工作填补了无监督概念学习的理论空白，但其假设在自然图像等复杂场景中是否成立尚存疑。

】

---

【Statistical Guarantees in the Search for Less Discriminatory Algorithms ｜少歧视算法搜索的统计停止准则

研究机构：美国麻省理工学院、美国康奈尔大学

作者：Chris Hays、Ben Laufer、Solon Barocas 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.23943)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23943)

> 算法公平性领域长期聚焦于如何修改数据或模型以消除偏差，却忽视了“搜索充分性”这一合规审计难题：企业应重训多少次模型才能证明已尽力寻找少歧视算法（Less Discriminatory Algorithms, LDA）？现有去偏方法无法回答“何时停止”的问题，导致合规举证陷入无限搜索困境。本文将该过程形式化为最优停止问题，利用 anytime-valid inference 构建高概率边际收益上界，当预期增益低于训练成本时即输出停止证书。该方法在理论上解决了搜索终止的统计合法性问题，但其有效性高度依赖于对模型性能分布的先验假设，且未验证停止后模型是否显著优于单次随机训练。

】

---

【STOP GUESSING: CHOOSING THE OPTIMIZATION - CONSISTENT UNCERTAINTY MEASUREMENT FOR EV IDENTIAL DEEP LEARNING ｜优化一致性视角下的证据深度学习不确定性度量

研究机构：同济大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_30244702)

> 证据深度学习（Evidential Deep Learning, EDL）旨在通过单次前向传播量化分类任务中的偶然与认知不确定性，但现有研究多聚焦于狄利克雷分布的概率属性，忽视了优化动态对模型行为的塑造作用。主流方法如传统EDL变体依赖固定正则化或复杂分布假设，导致不确定性度量与损失函数优化目标脱节，在分布外（Out-of-Distribution, OOD）检测中表现受限。本文从优化视角切入，证明不确定性感知交叉熵（Uncertainty-aware Cross-Entropy, UCE）损失隐含最大间隔支持向量机（Support Vector Machine, SVM）解，并提出优化一致性原则及边际感知预测不确定性（Margin-aware Predictive Uncertainty, MPU）度量。该工作为EDL提供了超越概率解释的优化理论框架，但在大规模预训练模型场景下的适用性尚未验证。

】

---

【Synthesising Counterfactual Explanations via Label-Conditional Gaussian Mixture Variational Autoencoders ｜标签条件高斯混合变分自编码器与潜空间路径反事实解释

研究机构：英国帝国理工学院

作者：Junqi Jiang、Francesco Leofante、Antonio Rago 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04855)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04855)

> 反事实解释（Counterfactual Explanations, CEs）旨在通过最小输入扰动翻转黑盒模型预测，为高风险决策提供可操作的算法补救。现有方法在追求有效性的同时，往往难以兼顾对输入扰动和模型更新的稳健性，且生成过程易偏离数据流形。本文提出标签条件高斯混合变分自编码器（Label-conditional Gaussian Mixture VAE, L-GMVAE）与潜空间路径反事实解释（LAtent PAth Counterfactual Explanations, LAPACE）框架，通过构建标签特定的潜空间原型并执行线性插值，实现了对输入扰动完美稳健且具备模型变化鲁棒性的CE生成。该框架在多项指标上优于基线，但其对分类器预测标签的依赖可能引入上游偏差，且高维连续特征下的效用差距提示了泛化边界。

】

---

【TACKLING THE XAI DISAGREEMENT PROBLEM WITH ADAPTIVE FEATURE GROUPING ｜自适应特征分组以解决可解释性分歧

作者：Gabriel Laberge、Ola Ahmad

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26520002)

> 可解释人工智能（XAI）面临的核心困境是不同归因方法对同一模型预测给出相互矛盾的解释，且缺乏地面真值供用户裁决。现有基于博弈论或梯度的方法虽各自满足特定公理，但无法消除彼此间的系统性偏差，导致保真度指标排名反转。本文指出分歧的根源在于特征间的组间交互项，并提出AGREED算法通过自适应合并高交互特征组来最小化这种分歧。该框架在表格数据上显著降低了方法间不一致性，但在图像数据上仅展示了定性效果，其作为通用解释框架的普适性仍存疑。

】

---

【TAMING POLYSEMANTICITY IN LLMS: THEORY - GROUNDED FEATURE RECOVERY VIA SPARSE AU TOENCODERS ｜稀疏自编码器特征恢复的理论保证与频率匹配算法

研究机构：美国耶鲁大学、上海交通大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_7005990)

> 大语言模型内部表示的叠加特性导致神经元多义性，稀疏自编码器（Sparse Autoencoder, SAE）虽能提取单义特征，但现有训练算法缺乏严格的数学恢复保证，且受限于超参数敏感性与随机种子不一致性。本文从神经元激活频率视角切入，发现“神经元共振”现象，即神经元激活频率与特征出现频率匹配时才能可靠恢复特征。基于此，提出分组偏置自适应（Group Bias Adaptation, GBA）算法，通过动态调整偏置实现频率匹配。该工作提供了首个具备理论恢复保证的SAE训练算法，但在高斯特征假设下推导，实际LLM非高斯分布下的理论边界尚待验证。

】

---

【Temporal Sparse Autoencoders: Leveraging the Sequential Nature of Language for Interpretability ｜时序稀疏自编码器

作者：Usha Bhalla、Alex Oesterling、Claudio Mayrink Verdun 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.05541)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.05541)

> 大语言模型内部表示的叠加特性导致神经元多义性，阻碍了直接基于神经元的机制理解。现有稀疏自编码器（Sparse Autoencoder, SAE）将激活视为独立同分布样本，忽略了语义在时间上的平滑演化与语法的局部波动，导致提取的特征多为噪声或浅层语法模式。本文引入时序对比损失，强制高层特征在相邻token间保持一致，从而自监督地解耦语义与语法。该设计在保持重构保真度的同时显著提升了语义特征的时序平滑度，但其对特征空间硬分割比例的依赖及跨层泛化能力仍存疑。

】

---

【The Deleuzian Representation Hypothesis ｜基于差异聚类的无监督概念提取

作者：Clément Cornet、Romaric Besançon、Hervé Le Borgne

论文原文见 [arXiv](https://arxiv.org/abs/2512.19734)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.19734)

> 大语言模型内部表示的叠加特性导致神经元多义性，阻碍了直接基于神经元的机制理解。稀疏自编码器（Sparse Autoencoder, SAE）通过重构误差最小化提取特征，但依赖稀疏性作为可解释性代理，且训练不稳定、特征易收缩。本文提出一种非重构式方法，通过聚类激活差异并引入偏度加权，直接定位区分样本的方向。该方法在874个属性上优于主流SAE变体，但缺乏重构保真度评估，其因果有效性仅通过定性转向验证。

】

---

【THE PRICE OF AMORTIZED INFERENCE IN SPARSE AUTOENCODERS ｜摊销推理的代价：局部摊销稀疏自编码器

研究机构：阿联酋扎耶德大学、沙特阿拉伯阿卜杜拉国王科技大学

作者：Wenjie Sun、Di Wang、Lijie Hu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94194787)

> 稀疏自编码器（Sparse Autoencoder, SAE）旨在解耦大语言模型中的多义性，但共享编码器带来的摊销推理（Amortized Inference）导致全局最优与实例级单义性冲突，引发特征吸收、分裂等病理现象。现有架构改进（如门控、TopK）仅优化重构-稀疏帕累托前沿，未能解决摊销机制本身的系统性次优。本文提出LocA-SAE，通过基于角度方差的潜变量分组与独立编码器，在计算成本与实例级精度间取得平衡。该范式挑战了“架构优化即解决病理”的共识，但分组策略依赖预训练统计，冷启动适用性存疑。

】

---

【THE SELF-RE-WATERMARKING TRAP: FROM EX PLOIT TO RESILIENCE ｜自再水印防御：基于Lipschitz约束的图像水印鲁棒性增强

研究机构：澳大利亚迪肯大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_41440378)

> 深度学习图像水印旨在通过嵌入隐藏比特验证数字内容所有权，但现有端到端框架普遍假设单次嵌入，未考虑编码器被恶意复用的场景。当攻击者利用合法编码器对已水印图像进行二次嵌入时，原水印信号被覆盖且无法恢复，导致所有权验证失效。本文提出自再水印威胁模型，并构建基于Lipschitz约束与对抗训练的防御框架，通过限制模型敏感度确保原水印在覆盖攻击下的可恢复性。该工作填补了自再水印防御的空白，但其保真度指标低于当前SOTA，且仅针对单一攻击类型，通用性受限。

】

---

【TIMESEG: AN INFORMATION-THEORETIC SEGMENT WISE EXPLAINER FOR TIME-SERIES PREDICTIONS ｜时序分段解释器：基于强化学习的变长片段选择

研究机构：韩国高丽大学、美国麻省理工学院

作者：Hwijin Kim、Jaeho Kim、Changhee Lee

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_58737456)

> 时间序列模型的解释面临点级归因碎片化与固定补丁定位不准的双重困境，导致生成的解释在物理层面失真且难以被人类理解。TimeSeg 将分段解释形式化为最大化条件互信息（Conditional Mutual Information, CMI）的序列决策问题，利用强化学习在严格黑盒约束下动态选择变长连续片段。该方法在 MIT-ECG 等数据集上显著提升了解释的连续性指标，但仅针对单变量场景，且依赖预训练策略网络的稳定性，其向多变量及高维场景推广的可行性尚未验证。

】

---

【TimeSeriesExamAgent: Creating Time Series Reasoning Benchmarks at Scale ｜时序推理基准自动化构建

研究机构：德国慕尼黑工业大学、美国卡内基梅隆大学

作者：Malgorzata Gwiazda、Yifu Cai、Mononito Goswami 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10291)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10291)

> 该方向旨在解决大语言模型（LLMs）在时间序列任务中“看似理解实则依赖捷径”的评估难题，现有基准因人工标注成本高、领域窄且难以扩展而停滞。本文切入点在于将基准构建从“专家手工设计”转变为“智能体自动化生成”，通过模板化合成与多智能体验证流水线解决可扩展性瓶颈。其核心做法是结合项目反应理论（Item Response Theory, IRT）与能力对齐过滤，实现领域特定考题的批量生产。该工作填补了时序推理评估基础设施的空白，但生成基准的固有偏差是否完全消除仍存疑。

】

---

【TimeSliver : Symbolic-Linear Decomposition for Explainable Time Series Classification ｜符号线性分解用于可解释时间序列分类

研究机构：美国西北大学

作者：Akash Pandey、Payal Mohapatra、Wei Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21289)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21289)

> 时间序列分类模型在医疗与工业场景中面临决策黑箱与监管透明性的冲突，传统事后归因方法因忽略时序依赖导致解释失真，而基于注意力的内在解释又受限于非线性映射的忠实性缺陷。TimeSliver 通过构建原始信号与符号化抽象的线性组合表示，将解释能力内嵌于前向传播，实现了多变量时序的正负双向归因。该方法在七个数据集上平均提升 11% 的归因准确率，预测性能接近最先进基线，但其固定分箱策略在分布漂移下的鲁棒性尚存疑。

】

---

【Tracking Equivalent Mechanistic Interpretations Across Neural Networks ｜机制解释等价性

研究机构：美国卡内基梅隆大学

作者：Alan Sun、Mariya Toneva

论文原文见 [arXiv](https://arxiv.org/abs/2603.30002)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.30002)

> 机制可解释性（MI）旨在通过逆向工程揭示 Transformer 内部计算机制，但现有方法面临解释不可复用与验证困难的双重瓶颈。传统自下而上方法依赖人工标注电路，自上而下方法则受限于候选算法的模糊性，导致无法判断两个模型是否共享同一底层逻辑。本文提出“解释等价性”概念，通过比较模型实现的表示相似性，在无需显式解释描述的情况下判定两模型是否共享同一机制。该框架为 MI 评估提供了新的理论工具，但其对实现枚举完备性的依赖及线性表示假设的适用边界仍存疑。

】

---

【TRAINING FREE COUNTERFACTUAL EXPLANATION FOR TEMPORAL GRAPH MODEL INFERENCE ｜时序图神经网络的反事实解释框架

研究机构：美国凯斯西储大学、美国亚利桑那州立大学

作者：Mingjian Lu、Haolai Che、Yangxin Fan 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_54824160)

> 时序图神经网络（TGNNs）在动态网络分析中表现优异，但其多层非线性变换与时间依赖机制导致预测过程不透明，阻碍了金融风控等高风险场景的部署。现有静态图解释方法无法捕捉节点间复杂的时序依赖，而早期TGNN解释器往往依赖信息瓶颈采样，可能包含与模型推理无关的非反事实结构。TemGX 提出了一种训练无关、模型无关的框架，通过滑动窗口内的时序影响度量与反事实验证，生成可解释的时序子图。该框架在保真度与效率上优于现有TGNN解释器，但其贪心选择策略对长程时序依赖的捕捉能力仍存疑。

】

---

【TrustGen _ : A PLATFORM OF DYNAMIC BENCH MARKING ON THE TRUSTWORTHINESS OF GENERATIVE FOUNDATION MODELS ｜生成式基础模型可信度动态基准

研究机构：美国麻省理工学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_20171493)

> 生成式基础模型（GenFMs）在高风险场景的部署面临可信度评估碎片化、静态基准迅速过时及跨模态不可比三大瓶颈。现有方案多聚焦单一模态或固定数据集，无法适应模型快速迭代与新型漏洞涌现。TrustGen 通过元数据策展、测试用例构建与上下文变异三模块动态生成评估数据，建立统一的多模态可信度分类法。该平台实现了跨T2I、LLM、VLM的标准化评估，但动态生成引入的评估噪声与静态基准的相关性验证尚存疑。

】

---

【Two (Narrow) Heads Are Better Than (an Arbitrarily Wide) One ｜注意力头数量与图结构任务表达能力的精确层级

研究机构：美国东北大学

作者：Amanuel Tesfaye、Zeno Kujawa、Rajmohan Rajaraman 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_91650260)

> 导读 本文旨在解决小模型Transformer在图结构任务上的表达能力边界模糊问题，现有理论结果多依赖维度或精度假设，缺乏无条件界限。作者通过定义端点选择问题（Endpoint Selection Problem, ESP），构建了基于几何不等式的证明框架。核心贡献是证明单头模型在含环图上存在不可逾越的误差下界，而双头模型可零误差求解。该工作确立了头数作为能力层级的关键变量，但其结论局限于单层注意力架构，对多层或含FFN结构的迁移性存疑。

】

---

【UNCERTAINTY ESTIMATION ｜超球面置信度映射

研究机构：韩国科学技术院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_28169653)

> 安全关键场景下的神经网络常因“过度自信”的错误预测导致严重后果，不确定性量化（UQ）旨在量化这种风险。现有主流方法要么依赖高成本的多次采样（如深度集成），要么依赖强分布假设（如高斯/狄利克雷），难以兼顾实时性与通用性。HCM通过将模型输出分解为幅度与单位方向向量，将几何约束违反程度直接定义为不确定性，实现了无采样、无分布假设的确定性估计。该方法在相关性指标上显著优于集成基线，但牺牲了部分预测精度与覆盖率，其几何假设在极端分布偏移下的鲁棒性存疑。

】

---

【Uncertainty Estimation via Hyperspherical Confidence Mapping ｜超球面置信映射

研究机构：韩国科学技术院

作者：Eunseo Choi、Ho-Yeon Kim、Jaewon Lee 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.05964)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05964)

> 不确定性量化（UQ）旨在为神经网络预测提供可靠性度量，以支持安全关键领域的决策。现有采样法（如深度集成）计算开销大，分布法（如证据学习）依赖强参数化先验，均难以在实时场景下兼顾效率与无假设性。HCM将输出分解为幅度与单位方向向量，以几何约束违反程度作为确定性不确定性分数。该方法在工业回归中实现了最强的置信-误差对齐，但在标准深度估计基准上校准精度显著落后于分布基线，其几何分数在复杂高维任务中的概率解释力存疑。

】

---

【Uncertainty-Gated Generative Modeling ｜不确定性门控生成建模

研究机构：美国加州大学伯克利分校、美国康奈尔大学

作者：Xingrui Gu、Haixi Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2603.07753)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07753)

> 金融时序预测面临非平稳性导致的点估计过自信问题，传统模型缺乏在分布漂移下动态调节信任度的机制。本文提出将不确定性作为内部控制信号，而非仅输出指标，通过门控机制调节表示、传播与生成三个阶段。具体做法是在WIAE-GPF骨干上注入不确定性门控模块，实现风险敏感推理。该方法在NYISO数据集上显著降低预测误差，但其门控机制对骨干网络改进的贡献占比尚不明确，且缺乏跨数据集验证。

】

---

【Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors ｜下一词预测中“无用”特征涌现的梯度归因分析

研究机构：瑞士洛桑联邦理工学院、德国慕尼黑工业大学

作者：Mark Rofin、Jalal Naghiyev、Michael Hahn

论文原文见 [arXiv](https://arxiv.org/abs/2603.14087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14087)

> 机制可解释性长期关注模型内部静态电路如何执行任务，却忽视了这些电路在训练过程中如何被梯度信号塑造。现有静态分析无法解释为何下一词预测（Next-Token Prediction, NTP）目标会诱导模型学习对即时预测无用的抽象特征，如世界模型或长程依赖。本文通过分解NTP损失梯度为直接、预缓存与共享三个分量，量化各分量对特定特征方向形成的贡献。该方法在玩具任务与OthelloGPT上验证了预缓存机制对“无用”特征涌现的必要性，但受限于小规模模型重训练，尚未在大规模语言模型上实现全量归因。

】

---

【Unifying Formal Explanations: A Complexity-Theoretic Perspective ｜统一形式化解释的计算复杂性理论

研究机构：以色列耶路撒冷希伯来大学、新加坡南洋理工大学

作者：Shahaf Bassan、Xuanxiang Huang、Guy Katz

论文原文见 [arXiv](https://arxiv.org/abs/2602.18160)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.18160)

> 机器学习解释的生成常面临计算不可行性，尤其是当要求解释具备概率保证或全局覆盖时，现有算法往往陷入指数级搜索。本文指出，局部与全局解释在数学性质上存在被忽视的非对称性，通过构建统一的值函数优化框架，揭示了全局解释具备单调性与次/超模性，从而在多项式时间内可解。这一理论突破为黑盒模型的全局可解释性提供了算法可行性基础，但其工程落地与解释信息量的平衡仍存疑。

】

---

【When Flatness Does (Not) Guarantee Adversarial Robustness ｜平坦度与对抗鲁棒性的局部-全局解耦分析

作者：Nils Philipp Walter、Linara Adilova、Jilles Vreeken 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.14231)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.14231)

> 对抗鲁棒性研究长期假设损失景观的平坦度能直接转化为模型对扰动的抵抗力，但这一直觉缺乏严格的理论支撑。现有经验证据显示平坦度与泛化相关，却未厘清其在对抗攻击下的具体作用机制，导致“平坦即鲁棒”的简化结论被广泛误用。本文通过推导倒数第二层相对平坦度的闭式解，形式化证明了平坦度仅保证局部鲁棒性，并揭示了对抗样本常落入高置信平坦区的“Uncanny Valley”现象。该工作厘清了参数空间几何与输入空间鲁棒性的边界，但理论界在高维网络中的紧致性仍存疑。

】

---

【WHY ADVERSARIALLY TRAIN DIFFUSION MODELS? ｜扩散模型对抗训练中的等变性约束

研究机构：意大利罗马第一大学、意大利博洛尼亚大学

作者：Maria Rosaria Briglia、Mujtaba Mirza、Giuseppe Lisanti 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_21661785)

> 生成模型在训练数据存在未知腐蚀时往往复现噪声而非学习真实分布，现有噪声感知训练方法依赖对噪声方差或干净/噪声标签的先验知识，限制了其在真实网络抓取数据上的适用性。本文切入点在于指出分类器对抗训练中的“不变性”目标在回归性质的去噪任务中会导致分布偏移，必须替换为“等变性”约束。方法通过在去噪轨迹中引入局部扰动并强制网络输出随扰动线性平移，实现了对未知腐蚀的鲁棒训练。该工作验证了等变性约束在90%高斯噪声下显著降低FID并减少记忆化，但其鲁棒性边界是否涵盖非高斯对抗攻击及多模态离散扰动，论文未提供形式化保证。

】

---

【WRING OUT THE BIAS: A ROTATION-BASED ALTER NATIVE TO PROJECTION DEBIASING ｜旋转去偏：规避投影引发的偏差放大

研究机构：美国伍斯特理工学院、美国麻省理工学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_96301813)

> 视觉语言模型（VLM）在零样本任务中常因训练数据中的虚假相关而依赖背景等捷径特征，导致分布外泛化失败。主流去偏方法通过正交投影移除目标概念子空间，但这一操作在数学上必然放大未监测概念的正交偏差，形成“打地鼠”效应。本文提出加权旋转去偏（WRING），通过保范旋转替代投影，在消除目标偏差的同时保持未监测概念偏差不变。该方法在冻结VLM权重下实现了无偏差放大的去偏，但仅针对单概念场景，多概念交互下的有效性尚未验证。

】

---

【Zero-Sacrifice Persistent-Robustness Adversarial Defense for Pre-Trained Encoders ｜零牺牲持久鲁棒性防御

研究机构：四川大学

作者：Zhuxin Lei、Ziyuan Yang、Yi Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2602.11204)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.11204)

> 预训练编码器在下游任务中易受下游无关对抗样本（DAE）攻击，现有防御方法通过任务特定微调提升鲁棒性，但不可避免地导致干净精度下降且无法跨任务泛化。ZePAD 利用神经网络对训练分布内样本的高置信度特性，构建双分支架构实现单次微调下的持久鲁棒性。该方法在保持甚至提升干净精度的同时显著增强对抗鲁棒性，但其置信度决策机制在分布偏移下的稳定性尚存疑。

】
