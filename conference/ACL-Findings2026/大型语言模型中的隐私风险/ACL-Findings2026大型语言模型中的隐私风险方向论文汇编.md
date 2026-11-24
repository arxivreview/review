# ACL-Findings2026 · 大型语言模型中的隐私风险方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Automated Profile Inference with Language Model Agents ｜自动化画像推断

作者：Yuntao Du、Zitao Li、Bolin Ding 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_74a5b1641137)

> 在线伪匿名平台用户通过公开活动暴露的敏感信息，长期依赖人工分析才能被提取，效率低且门槛高。现有基于大语言模型（LLM）的属性推断方法多将任务简化为预定义类别的分类，无法处理噪声大、信息隐含且无固定标签的真实场景。本文提出 AutoProfiler，一个由四个专用 LLM 智能体协作的自动化画像框架，通过迭代检索、推断与精炼流程，从公开活动中自主构建包含个人身份信息（PII）和敏感个人信息（SPI）的用户画像。该方法在真实数据上实现了高准确率与低成本，验证了自动化去匿名化的可行性，但其对模型对齐防御的无效性及合成基准上的性能局限仍存疑。

】

---

【Beyond Local vs. External: A Game-Theoretic Framework for Trustworthy Knowledge Acquisition ｜博弈论驱动的可信知识获取

作者：Rujing Yao、Yufei Shi、Yang Wu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1e3eb161e9f)

> 大语言模型（LLM）在云端部署时，用户直接提交敏感查询会导致研究意图或组织机密泄露，而仅依赖本地小模型又受限于知识广度与推理能力。现有语义混淆方法多为静态启发式规则，无法适应外部模型动态的推断行为，且缺乏对“意图可重构性”的显式量化。本文提出GTKA框架，将隐私-效用权衡建模为生成器与攻击者的交替对抗博弈，通过优化子查询策略实现零原始查询暴露下的高保真答案合成。该框架在自建生物医学与法律基准上验证了优于静态基线的泄露抑制效果，但其攻击者模块的模拟保真度及多轮交互下的累积泄露风险仍存疑。

】

---

【CoTrust: Privacy-Preserving Collaboration Between Large and Small Language Models in Trusted Execution Environments ｜可信执行环境内的大小模型协同隐私推理

作者：Zhenya Ma、Tingyi Wang、Yongheng Deng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c25ad94d058)

> 导读 大语言模型（LLM）在处理含个人身份信息（PII）的用户输入时，直接部署高容量模型于可信执行环境（TEE）受限于内存与算力瓶颈，而将敏感数据暴露给外部模型则面临隐私泄露风险。现有脱敏方法通过掩码保护隐私，但往往丢弃关键语义线索，导致生成质量显著下降。CoTrust 提出一种协同推理框架，让 TEE 内的小语言模型（SLM）处理全保真输入，外部 LLM 基于多视图脱敏数据生成共识脚手架，再由 SLM 在 TEE 内实例化最终答案。该框架在保持强隐私保护的同时接近无掩码 LLM 的性能上限，但其依赖硬件信任假设，且未验证 TEE 被攻破时的鲁棒性。

】

---

【Detecting Sensitive Personal Information in Japanese Pre-Training Corpora for Large Language Models ｜日语预训练语料敏感个人信息检测

作者：Rei Minamoto、Yusuke Oda、Daisuke Kawahara

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0b732bebe3b7)

> 大规模日语预训练语料中混杂着受法律严格保护的敏感个人信息，若未过滤将导致模型记忆并泄露此类数据，引发合规风险。现有PII过滤工具仅能识别姓名、地址等基础标识符，无法捕捉医疗、犯罪等需结合语境判断的敏感属性，导致合规过滤存在盲区。本文提出基于两阶段大语言模型标注构建数据集，并训练轻量级分类器实现高效SCPI检测。该方法在日语语料上实现了高精度过滤，但受限于数据规模与类别覆盖，其泛化能力与跨语言适用性仍存疑。

】

---

【HearSay Benchmark: Do Audio LLMs Leak What They Hear? ｜音频大语言模型声纹隐私泄露基准

作者：Jin Wang、Kaiwen Luo、Liang Lin 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01cae2ca3614)

> 音频大语言模型（ALLMs）在预训练中是否编码了声纹与敏感个人属性之间的隐性关联，这一风险此前缺乏量化手段。现有文本与视觉隐私评估无法迁移至纯声学场景，且缺乏区分“真实声学推理”与“统计先验幻觉”的指标。本文构建基于真实讲座音频的 HearSay 基准，引入盲偏置率（BBR）验证泄露源于声学证据而非过拟合。该工作确立了 ALLM 声学隐私泄露的实证基线，但评估仅覆盖静态属性，未涉及动态交互中的上下文泄露。

】

---

【LDEDE: LRP-Driven Efficient Detection and Editing Framework for LLM Privacy Neurons ｜LDEDE：基于层级相关性传播的大语言模型隐私神经元高效检测与编辑框架

作者：Zhao Zhengyuan、Cao Lifeng、Sunhaodong 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_82240bf989f0)

> 导读 大语言模型在预训练与微调中不可避免地记忆敏感信息，现有防御手段如差分隐私（DP）导致效用显著下降，传统机器遗忘易引发灾难性崩溃，而神经元编辑方法则面临定位效率低与“隐私跷跷板”效应两大瓶颈。LDEDE 框架通过层级相关性传播（LRP）算法替代梯度归因进行隐私神经元定位，并引入极性感知神经元编辑（PANE）策略处理耦合神经元，以在保持模型通用性能的前提下降低隐私泄露风险。该方法将计算复杂度从 $O(N^2)$ 降至 $O(N)$，在 Enron 和 MIMIC 数据集上平均降低 42.7%–73.5% 的泄露风险，但缺乏与主流攻击方法的绝对值对比，其通用性能保留的充分性存疑。

】

---

【PII-VisBench: Evaluating Personally Identifiable Information Safety in Vision Language Models Along a Continuum of Visibility ｜视觉语言模型隐私评估：基于主体可见性连续体的 PII-VisBench

研究机构：美国加州大学河滨分校

作者：G M Shahariar、Zabir Al Nazi、Md Olid Hasan Bhuiyan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05739)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05739)

> 视觉语言模型（VLM）在医疗与文档处理等隐私敏感场景中，常因预训练记忆而泄露个人身份信息（PII），但现有评估多将其视为静态提取问题，忽略了主体在线足迹对模型行为的决定性影响。本文提出 PII-VisBench，通过构建“可见性连续体”将 200 个主体分层为高、中、低、零四级，并设计 4000 个探针，系统量化了 18 个开源 VLM 的拒绝率（RR）与条件 PII 披露率（cPDR）。该基准揭示了“高可见性隐私缺口”，即模型对公众人物的 PII 泄露风险显著高于普通个体，表明安全对齐未能有效抑制记忆型泄露。这一发现挑战了“模型规模越大越安全”的隐含假设，但基于网络搜索结果的可见性代理指标是否完全代表训练数据分布，仍存疑。

】

---

【Privacy Risks of Intermediate Representations: Attribute Inference in Distributed LLM Inference ｜分布式推理中间表示的属性推断攻击

作者：Yang Lyu、Jin Cao、Yang Xiao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9211fc754cf2)

> 分布式大语言模型推理通过传输中间隐藏状态而非原始输入来降低计算成本，但这一架构被普遍假设能保护用户隐私。现有属性推断攻击依赖完整模型访问或辅助数据对，无法在仅持有部分层权重的受限场景下运行。本文提出IR-AIA，一种纯基于中间表示的零样本属性推断攻击，通过几何去偏与滑动窗口匹配解决各向异性与子词碎片化问题。该工作揭示了中间层共享的隐私漏洞，但其高准确率是否受限于候选集规模与特定层选择，仍需更广泛的基准验证。

】

---

【SEAD: A Surrogate-free Label-only Membership Inference Attack against Pre-trained LLMs with Semantic-Aware Density ｜语义感知密度：无代理黑盒成员推断攻击

作者：Biao Yi、Jiahao Li、Yiming Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ac149aed6e9c)

> 大语言模型（LLM）在预训练中不可避免地记忆敏感数据，成员推断攻击（MIA）是量化这一风险的核心手段，但生产级API通常仅返回生成文本而非完整概率分布，导致依赖Logits的传统攻击失效。现有Label-only攻击依赖代理模型进行概率回归，却因代理选择偏差和巨大的估计误差而可靠性不足。本文提出SEAD，通过直接对目标模型进行蒙特卡洛采样并引入NLI语义加权，在无代理条件下重构Token概率密度。该方法在Label-only设定下刷新了SOTA，但其性能仍显著低于Logits-based攻击，且依赖外部NLI模型，其实际审计效能与计算成本之间的平衡尚存疑。

】

---

【Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use ｜后门工具调用数据窃取

作者：Wuyang Zhang、Shichao Pei

论文原文见 [arXiv](https://arxiv.org/abs/2604.05432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05432)

> 工具调用型大语言模型（LLM）代理在部署中常被赋予会话记忆与外部检索权限，这为敏感信息泄露提供了隐蔽通道。现有针对代理的安全研究多聚焦于运行时提示注入或知识投毒，忽略了模型权重层面植入的后门如何与工具调用机制耦合，实现系统性数据窃取。本文提出 Back-Reveal 框架，通过语义触发器激活后门，利用伪装成合法检索请求的 HTTP 调用将记忆数据外传，并引入重排序感知重写器以绕过现代 RAG 过滤机制。该工作揭示了代理系统中“记忆-检索”链路的安全盲区，但其攻击可行性高度依赖开放权重与宽松连接器配置，在严格权限隔离的生产环境中适用性存疑。

】
