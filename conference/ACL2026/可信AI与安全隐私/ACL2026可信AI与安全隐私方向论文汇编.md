# ACL2026 · 可信AI与安全隐私方向论文汇编

> 本方向共 20 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Multilingual Social Bias Benchmark Incorporating Thinking Processes ｜多语言思维过程感知偏见基准

研究机构：英国利物浦大学

作者：Masahiro Kaneko、Danushka Bollegala、Timothy Baldwin

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70d8a35f2a49)

> 大语言模型（LLMs）在多语言场景下继承并放大了训练数据中的社会偏见，但现有评估框架仅关注最终输出，无法区分模型是“偶然正确”还是“逻辑正确”。本文切入点在于将评估对象从表层文本延伸至中间推理逻辑，构建包含人类标注思维过程的多语言基准 MBTP。通过引入思维过程感知评估（TPAE）范式与少样本元评估方法，MBTP 实现了无需微调的偏见指标有效性验证。该工作提升了评估的细粒度与跨文化覆盖度，但其依赖母语者标注的高成本限制了规模化应用，且未验证思维过程标注本身是否引入新的主观偏差。

】

---

【Afri-MCQA: Multimodal Cultural Question Answering for African Languages ｜非洲多模态文化视觉问答基准

研究机构：英国伦敦大学学院、印度理工学院

作者：Atnafu Lambebo Tonja、Srija Anand、Emilio Villa-Cueva 等 19 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4c047845f035)

> 多模态大语言模型在非洲低资源语言上的文化认知能力长期缺乏系统性评估，现有文本基准无法覆盖语音模态这一关键输入通道。本文通过母语者原生构建包含文本与语音双模态的视觉问答数据集，并引入语言识别与语音转写控制实验，解耦了语言理解瓶颈与文化知识缺失。该基准揭示了开放权重模型在语音模态下的基础能力失效，但受限于单一任务类型，其结论向其他多模态任务的泛化性尚待验证。

】

---

【CHAIRO: Contextual Hierarchical Analogical Induction and Reasoning Optimization for LLMs ｜基于类比归纳的规则推理优化框架

研究机构：新加坡国立大学、深圳大学

作者：Haotian Lu、Yuchen Mou、Bingzhe Wu

论文原文见 [arXiv](https://arxiv.org/abs/2604.10502)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10502)

> 内容审核系统在处理隐喻性歧视或模糊语境时，常因规则缺失或过于宽泛而失效。现有大语言模型（LLM）直接提示或静态检索增强生成（RAG）方法难以从细粒度实例中动态提炼出可解释的审核标准。CHAIRO 通过自增强类比思维链与辅助模型规则归纳的端到端联合优化，将检索、规则生成与分类决策耦合，解决了规则泛化与语境适配的矛盾。该方法在细粒度文本审核任务上显著提升了准确率与规则质量，但其对多模态隐性危害及极端长尾类别的适用性仍存疑。

】

---

【CoLA: A Choice Leakage Attack Framework to Expose Privacy Risks in Subset Training ｜子集训练中的选择泄露攻击

研究机构：沙特阿拉伯阿卜杜拉国王科技大学、新加坡国立大学

作者：Qi Li、Cheng-Long Wang、Yinzhi Cao 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12342)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12342)

> 现代机器学习流水线普遍采用子集训练以提升效率与数据质量，但这一实践是否降低了隐私风险？传统成员推断攻击（MIA）依赖模型过拟合信号，在子集训练场景下因分布重叠而失效。本文指出，选择算法本身编码了“谁被选中、谁被排除”的信号，构成了新的隐私侧信道。CoLA框架通过量化样本在多个候选窗口中被重复选中的稳定性，实现了对训练数据及被排除数据的成员推断。该工作揭示了数据预处理阶段的系统性漏洞，但其有效性高度依赖选择算法的确定性，在随机性强的选择策略下性能可能退化。

】

---

【Controlling Distributional Bias in Multi-Round LLM Generation via KL-Optimized Fine-Tuning ｜多轮生成中的分布偏差控制

作者：Yanbei Jiang、Amr Keleg、Ryandito Diandaru 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bb0bf10c3e92)

> 大语言模型（LLM）在单次推理中常被评估为对固定真值的拟合，但真实应用中重复提示会导致输出属性分布偏离目标统计。现有去偏方法多针对单次输出的公平性，缺乏对多次采样下属性频率收敛性的控制机制。本文提出“分布对齐”框架，通过引入引导令牌（Steering Tokens）并结合 KL 散度与 KTO 损失，实现多轮生成中属性分布的精确校准。该方法在职业性别分布任务上显著优于直接偏好优化（DPO），但仅验证了单一属性的边际分布控制，未触及交叉性偏差或长文本语义连贯性的深层影响。

】

---

【FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation ｜严格度自适应的连续风险评分

研究机构：香港理工大学、Hugging Face

作者：Zhihao Ding、Jinming Li、Ze Lu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23636)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23636)

> 内容审核系统需在不同平台与时间维度下适应动态变化的执法标准，但现有二元分类器将安全定义固化为静态标签，导致策略切换时性能剧烈波动。本文指出这一“严格度脆弱性”被现有基准忽视，提出以连续风险分数替代固定标签的范式。通过构建FlexBench基准与FlexGuard模型，利用评分标准蒸馏与强化学习对齐分数-严重度一致性。该方法在动态严格度下显著优于基线，但其仅聚焦文本模态且依赖伪标签蒸馏，在多模态与极端边界校准上的有效性存疑。

】

---

【From Isolation to Entanglement: When Do Interpretability Methods Identify and Disentangle Known Concepts? ｜从隔离到纠缠：可解释性方法何时能解耦已知概念？

研究机构：美国波士顿大学、美国哈佛大学

作者：Aaron Mueller、Andrew Lee、Shruti Joshi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.15134)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15134)

> 导读

】

---

【InsideOut: Measuring and Mitigating Insider-Outsider Bias in Interview Script Generation ｜内部人-外部人偏见：INSIDEOUT基准与智能体缓解框架

研究机构：美国加州大学洛杉矶分校

作者：Yixin Wan、Xingrun Chen、Kai-Wei Chang

论文原文见 [arXiv](https://arxiv.org/abs/2509.21080)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21080)

> 大语言模型在生成跨文化内容时，常默认采用主流文化（如美国）的“内部人”视角，而将非主流文化置于“外部人”位置，这种文化视角定位偏差（Insider-Outsider Bias）导致生成内容对边缘文化的刻板化与异域化。现有偏见评估多聚焦于显性刻板印象或人口统计学属性，难以捕捉这种隐含在提问方式与叙事立场中的系统性文化霸权。本文通过构建INSIDEOUT基准量化该偏差，并提出基于多智能体反思的推理时缓解框架MFA。该工作揭示了生成式模型中文化视角的结构性不平等，但其缓解效果高度依赖底层模型的工具调用能力，且缺乏对训练数据根源的干预。

】

---

【Location Not Found: Exposing Implicit Local and Global Biases in Multilingual LLMs ｜定位缺失：多语言大语言模型中的隐性地缘偏见诊断

研究机构：谷歌研究院

作者：Guy Mor-Lan、Omer Goldman、Matan Eyal 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19292)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19292)

> 多语言大语言模型（LLMs）在消除语言流畅度差距的同时，往往将西方规范作为默认语境，导致非英语用户获取错误的本地事实。现有文化基准多依赖显式提示或测试显性知识，无法捕捉模型在语境缺失时的隐性默认偏好。本文提出 LocQA 基准，通过地域歧义问题量化模型的全局与区域偏见，并揭示指令微调带来的文化对齐税。该工作提供了诊断工具，但缺乏干预机制，且评估依赖自动判分，细微差异的可靠性存疑。

】

---

【Mechanistic Interpretability Should Prioritize Feature Consistency in Sparse Autoencoders ｜稀疏自编码器特征一致性度量与理论验证

研究机构：美国卡内基梅隆大学、美国斯坦福大学

作者：Xiangchen Song、Aashiq Muhamed、Yujia Zheng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b8da87195dbc)

> 导读 稀疏自编码器（Sparse Autoencoder, SAE）旨在将大语言模型（LLM）中多义性的神经元激活分解为单义特征，但不同随机种子训练出的SAE往往收敛到显著不同的特征字典，导致解释结果不可复现。现有评估体系仅关注重构误差与稀疏度，忽视了字典层面的跨运行稳定性，使得基于SAE的因果干预和特征拼接缺乏可靠基础。本文提出成对字典平均相关系数（Pairwise Dictionary Mean Correlation Coefficient, PW-MCC）作为量化指标，并结合过完备稀疏字典学习的可辨识性理论，论证TopK SAE在满足特定条件时能实现高一致性。该工作填补了SAE评估中“稳定性”维度的空白，但理论保证局限于理想化设定，实际LLM激活中的高一致性是否足以支撑下游因果推理仍存疑。

】

---

【Mitigating Spurious Correlations in Text Classification Using Latent Space Geometry ｜基于原型引导的鲁棒不变特征变换

研究机构：同济大学、中国科学院

作者：Jiasen Gao、Xiaoliang Chen、Duoqian Miao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0e942281023d)

> 文本分类模型常因依赖训练数据中的风格或人口统计特征等虚假相关，在分布外场景下对少数群体表现崩溃。现有去偏方法要么依赖昂贵的显式组标签，要么采用不稳定的对抗训练，且硬投影易破坏语义。PRIFT 利用自然语言提示生成几何锚点，通过中心投影算子移除偏差偏差项而非全部偏差信息。该方法在无需组标签的情况下显著提升了最差群体准确率，但其对提示工程质量的依赖及单属性假设限制了其通用性。

】

---

【PluRule: A Benchmark for Moderating Pluralistic Communities on Social Media ｜多元社区规则审核基准

研究机构：美国印第安纳大学

作者：Zoher Kachwala、Bao Tran Truong、Rasika Muralidharan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17187)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17187)

> 去中心化社交平台的内容治理面临规范碎片化挑战，同一内容在不同社区可能合规或违规，传统基于全局统一标准的分类器无法捕捉这种语境依赖性。现有基准多聚焦于仇恨言论等单一类别，缺乏对社区特定规则动态性的系统评估。PLURULE 将审核任务重构为多选题，要求模型在特定社区规则集下识别具体违规项，从而量化视觉语言模型在多元规范理解上的能力边界。该基准揭示了当前模型在局部规则推理上的显著缺陷，但仅评估精度而未涉及部署效率，其结论对工业级实时审核系统的适用性存疑。

】

---

【Powerful Training-Free Membership Inference Against Fine-Tuned Autoregressive Language Models ｜错误位置概率失衡攻击

作者：David Ilić、David Stanojević、Kostadin Cvejoski

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f8c814580b76)

> 微调语言模型对训练数据的记忆强度长期缺乏高效且高精度的审计手段，现有方法要么依赖高成本的影子模型训练，要么因聚合统计稀释了关键信号而漏检。EZ-MIA 指出记忆信号集中于模型预测错误的 token 位置，通过计算这些位置上概率变化的方向性失衡来量化记忆强度。该方法仅需两次前向传播且无需训练任何参考模型。其价值在于以极低成本揭示了微调方法对隐私风险的巨大影响，但其在非微调场景及长序列下的泛化能力仍存疑。

】

---

【PR-XAI：将Transformer建模为分层有向图，利用PageRank算法捕捉Token间间接依赖，解决长文本归因失效问题

作者：Behrooz Azarkhalili、Linyi Li、Maxwell Libbrecht

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6b462b79d451)

> 现有Transformer归因方法多将注意力权重直接作为重要性分数，或仅做单层聚合，忽略了跨层信息流动与Token间的间接依赖效应，导致长文本解释失效。本文切入点在于将Transformer架构显式建模为分层有向图，利用PageRank算法在图上进行重要性传播，从而捕捉直接和间接的Token贡献。具体做法是构造由注意力权重及其梯度张量加权的转移矩阵，求解特征向量得到Token级归因分数。该方法在长文本数据集上显著优于基线，但其图结构假设是否完全匹配Transformer前向传播的确定性机制，仍存疑。

】

---

【SAFO: Stable Adaptive Fairness Optimization for LLM-Based Social Survey Simulation ｜稳定自适应公平优化

作者：Chenxi Lin、Zhuoren Jiang、Kaisong Song 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_461468a07b3c)

> 社会调查模拟旨在通过大语言模型（LLMs）预测不同人口统计学群体的响应，以辅助政策评估与风险预测。然而，标准经验风险最小化（ERM）在数据不平衡时系统性偏向多数群体，而分布鲁棒优化（DRO）虽能缓解偏见，却在稀疏群体下引发训练震荡与收敛不稳定。SAFO 通过引入指数移动平均（EMA）平滑损失估计与纳什（Nash）激励调节器，在保持整体效用的同时实现稳定收敛。该方法在三个大规模调查数据集上验证了公平性与稳定性的协同提升，但其对多属性交叉稀疏性的处理仍依赖属性级聚合，未完全解决组合爆炸下的噪声累积问题。

】

---

【Stereotype Bias in a Bilingual Setting: A Culturally Grounded Evaluation in Kazakhstan ｜哈萨克语-俄语代码切换语境下的刻板印象偏见评估

研究机构：阿联酋扎耶德大学

作者：Nurkhan Laiyk、Daniil Orel、Ayana Mussabayeva 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_69a8935d0748)

> 大语言模型在低资源双语社会中的偏见评估长期缺失，现有基准多基于单语或高资源语言，无法捕捉代码切换（Code-switching）带来的偏见叠加效应。本文针对哈萨克斯坦这一典型双语社会，构建了首个涵盖哈萨克语、俄语及代码切换变体的文化根基偏见数据集。通过困惑度对比与预训练模拟，揭示了模型在混合语言输入下偏见非线性放大的机制。该工作填补了中亚地区偏见评估空白，但其结论受限于单一国家语境，且未提供缓解策略。

】

---

【Stop Hardening Everything: A Training-Free Neuron-Level Defense for Neural Ranking Models ｜模型中心式神经元级防御

研究机构：中国科学院、中国科学院大学

作者：Yu-An Liu、Ruqing Zhang、Hongru Song 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_088365154da6)

> 神经排序模型（NRM）面临不可感知文本扰动导致的排名操纵威胁，现有数据中心式防御因全参数重训成本高且易过拟合特定攻击而失效。本文切入点在于对抗脆弱性并非均匀分布于所有参数，而是源于特定内部神经元单元。通过最大边际脆弱性准则定位关键神经元并实施逆向扰动，实现免训练鲁棒性修复。该方法在MS MARCO上显著降低攻击成功率，但依赖白盒访问权限，其泛化边界尚存疑。

】

---

【TensorLens: End-to-End Transformer Analysis via High-Order Attention Tensors ｜高阶张量统一表示

研究机构：以色列特拉维夫大学

作者：Ido Andrew Atad、Itamar Zimerman、Shahar Katz 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17958)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17958)

> 机制可解释性（Mechanistic Interpretability, MI）旨在通过逆向工程揭示 Transformer 内部计算机制，但现有注意力聚合方法仅覆盖部分组件，导致全局行为解释存在盲区。本文切入点在于将包含 FFN、归一化及嵌入层在内的整个 Transformer 重构为单一的高阶数据控制线性算子，以消除启发式聚合的信息损失。通过引入四阶张量结构并设计多种坍缩策略，该方法在扰动测试中显著优于传统矩阵基线。其价值在于提供了理论上完备的统一视角，但高阶张量的计算复杂度与线性化假设的局限性仍存疑。

】

---

【The GaoYao Benchmark: A Comprehensive Framework for Evaluating Multilingual and Multicultural Abilities of Large Language Models ｜高瑶基准：多语言多文化能力的系统性诊断框架

研究机构：复旦大学

作者：Yilun Liu、Chunguang Zhao、Mengyao Piao 等 17 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20225)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0da69d3b7c4b)

> 多语言大语言模型（LLM）在全球部署中面临评估碎片化与文化盲区的双重困境，现有基准往往依赖机器翻译且缺乏深层文化维度的系统性覆盖。本文切入点在于构建一个融合文化分层与认知分类的统一评估矩阵，通过母语专家本地化与半自动合成管线，解决主观任务中“翻译腔”导致的评估失真问题。GaoYao 通过 23.3M tokens 的数据集揭示了通用多语言能力与深层文化特异性能力之间的解耦关系，其价值在于提供了比传统排行榜更细致的诊断地图，但受限于人工验证的高成本，其向低资源语言大规模扩展的可行性仍存疑。

】

---

【The “Knowledge–Behavior Gap” in Cultural Taboo Safety of Large Language Models ｜文化禁忌安全评估基准

研究机构：复旦大学

作者：Ying He、Sihang Jiang、Xingzhou Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ef33d302bf10)

> 多语言大语言模型（LLM）在全球部署中面临文化禁忌识别失效的风险，现有基准多聚焦显性毒性或通用文化知识，忽视了隐性文化禁忌在看似无害提问中的防御挑战。本文通过构建覆盖77个国家的CulShield基准，引入“文化陷阱”与“过度敏感”双维度评估，量化了模型“知晓禁忌却行为违规”的知识-行为差距。实验揭示了语言文化距离与安全违规率的负相关机制，并验证了基于世界价值观调查（WVS）的微调策略对抑制过度敏感的效用。该工作填补了隐性文化安全评估的空白，但其依赖翻译构建多语言数据的路径是否真正捕捉了原生文化语境，仍存疑。

】
