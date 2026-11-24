# Others2026 · 多模态与视觉语言方向论文汇编

> 本方向共 16 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Conformal Cross-Modal Active Learning ｜跨模态保形主动学习

研究机构：奥地利维也纳大学、德国亚琛工业大学

作者：Huy Hoang Nguyen、Cédric Jung、Shirin Salehi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.23159)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.23159)

> 视觉语言模型（VLM）蕴含的语义信息常被忽略于主动学习（AL）的样本选择中，导致标注效率受限。现有AL方法多依赖单模态不确定性，无法有效利用VLM的跨模态语义结构，且VLM输出常存在校准偏差。本文提出Conformal Cross-Modal Acquisition (CCMA)，通过保形预测（Conformal Prediction, CP）校准VLM教师与视觉学生模型的不确定性，结合多样性加权覆盖实现高效样本选择。该方法在CIFAR100等基准上显著优于单模态AL基线，但其性能高度依赖教师-学生分布差异，当两者趋于一致时优势消失。

】

---

【HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token ｜预生成幻觉风险探测

研究机构：美国石溪大学、美国芝加哥丰田技术学院

作者：Sai Akhil Kogilathota、Sripadha Vallabha E G、Luzhe Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05465)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05465)

> 视觉语言模型（VLMs）在生成文本时常因语言先验压制视觉信号而产生对象或属性幻觉，现有抑制方法多依赖解码过程中的动态干预或生成后的完整序列比对，导致实时风险预判能力缺失。HALP 抓住“幻觉风险在生成前已编码于内部表征”这一被忽略的点，通过单次前向传播提取视觉特征、视觉 token 及查询 token 状态，训练轻量级 MLP 探针输出风险分数。该框架实现了零解码成本的幻觉预测，但仅作为诊断工具而非抑制手段，其分数能否直接转化为解码控制信号仍存疑。

】

---

【PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment ｜多模态过程对齐推理

研究机构：南京大学

作者：Yantao Li、Qiang Hui、Chenyang Yan 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.06652)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06652)

> 多模态大模型在强化学习后训练中常出现“答案正确但推理过程幻觉”的现象，即模型利用语言先验而非视觉证据解题。现有基于最终答案的奖励机制无法区分视觉忠实推理与文本捷径，导致长链推理中视觉漂移加剧。PaLMR通过构建感知对齐数据层与过程对齐优化层，将视觉一致性作为二元可验证指标融入组相对策略优化，实现过程级视觉锚定。该方法在7B规模下显著降低幻觉率，但其依赖外部LLM评分的机制在目标模型能力超越评估器时失效，限制了其向更强模型的泛化能力。

】

---

【Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models ｜Switch-KD：统一概率空间下的视觉-语言知识蒸馏

作者：Haoyi Sun、Xiaoxiao Wang、Ning Mao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14629)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14629)

> 跨模态知识蒸馏旨在解决多模态大模型（MLLMs）在边缘部署中算力与精度难以兼得的矛盾。现有方法如 LLaVA-KD 和 Align-KD 将视觉与语言监督割裂，导致模态间耦合信息丢失，知识转移效率受限。Switch-KD 提出将学生视觉输出切换至教师语言路径，在共享文本概率空间内通过动态双向 Logits 差异损失实现隐式视觉知识迁移。该框架在 10 个基准上超越现有蒸馏方法，但其对组合推理任务的增益有限，且依赖教师语言路径的“解释”能力，其泛化边界尚待验证。

】

---

【Video Evidence to Reasoning Efficient Video Understanding via Explicit Evidence Grounding ｜证据链推理

研究机构：香港理工大学

作者：Yanxiang Huang、Guohua Gao、Zhaoyang Wei 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07761)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07761)

> 视频大语言模型（LVLMs）在处理长视频时面临感知精度与推理效率的结构性矛盾：冗长的思维链（Chain-of-Thought, CoT）消耗大量计算资源，而高效采样又导致视觉证据丢失引发幻觉。现有方法要么依赖外部多阶段流水线增加延迟，要么在提示层隐式接地，无法在架构层面同时保证证据的显式定位与推理的紧凑性。本文提出CoE框架，通过内嵌的证据接地模块（Evidence Grounding Module, EGM）在编码器与解码器之间进行查询引导的特征过滤，并结合强化学习优化证据-逻辑对齐，实现了精度与效率的协同提升。该框架在多个基准上刷新了开源模型SOTA，但其性能增益中骨干网络贡献与架构创新贡献的边界尚不清晰。

】

---

【VIGiA: Instructional Video Guidance via Dialogue Reasoning and Retrieval ｜指令性视频计划引导

作者：Diogo Glória-Silva、David Semedo、João Maglhães

论文原文见 [arXiv](https://arxiv.org/abs/2602.19146)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19146)

> 指令性视频计划引导旨在让模型在对话中实时跟踪用户执行进度，并基于视觉输入与文本计划进行接地推理。现有方法多局限于纯文本引导或单帧检索，无法处理多模态交互中的状态漂移与证据缺失。VIGiA 通过多目标架构与专门设计的检索投影层，实现了计划推理与视频片段检索的统一。该模型在自建数据集上展现了极高的任务准确率，但其依赖私有数据且未采用强化学习后训练，泛化能力存疑。

】

---

【不确定性引导的视觉重注意自校正

作者：Kassoum Sanogo、Renzo Ardiccioni

论文原文见 [arXiv](https://arxiv.org/abs/2512.07564)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07564)

> 视觉语言模型（VLMs）在生成图像描述时，常因语言先验压制视觉信号而产生对象幻觉，这一可靠性危机在2023年随开源模型爆发而凸显。现有推理时干预策略如视觉对比解码（VCD）虽能抑制幻觉，但缺乏对幻觉发生位置的显式定位机制，且单次前向传播难以解决分辨率受限导致的细粒度感知错误。本文提出一种无需训练的自校正框架，通过多维不确定性量化触发对低注意力区域的迭代式裁剪与验证，将幻觉抑制从全局logits调整转向局部视觉证据重构。该框架在Qwen2.5-VL-7B上实现了对抗性设置下4.7%的准确率提升，但其单架构验证与显著高于领域SOTA的幻觉率，暴露了方法泛化性与绝对性能的双重局限。

】

---

【亚利桑那州立团队新研究：轻量级视觉模型跨数据集鲁棒性评估

研究机构：美国亚利桑那州立大学

作者：Weidong Zhang、Pak Lun Kevin Ding、Huan Liu

论文原文见 [arXiv](https://arxiv.org/abs/2511.00335)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.00335)

> 导读 移动端视觉模型长期依赖ImageNet作为性能代理指标，但单一基准无法反映模型在医疗、细粒度等异构域的真实泛化能力。现有评估协议常混淆架构优势与训练超参数影响，且缺乏量化跨域一致性的统一度量。本文通过固定11种轻量架构在7个数据集上的训练协议，提出结合均值与方差的xScore指标，以解耦架构鲁棒性与单点性能。该框架揭示了ImageNet高分与跨域稳健性的解耦现象，但受限于单一参数预算与分类任务，其结论向多模态或空间密集任务的迁移性存疑。

】

---

【城市环境变化智能分析框架

作者：Zixuan Xiao、Jun Ma、Siwei Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2601.05483)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05483)

> 城市环境变化分析需超越像素级变化检测，回答“是什么”、“在哪里”、“为什么”等层级化问题，但传统遥感方法受限于单一模态，而通用大语言模型（LLM）缺乏领域知识易产生幻觉。本文切入点在于构建一个基于工具调用的多模态智能体框架，通过模块化控制器实现异构数据对齐与推理约束。该框架在三个真实城市案例中实现了100%的任务成功率，较最佳基线提升46.7%，但其有效性局限于预定义工具覆盖的场景，缺乏跨城市泛化验证。

】

---

【大连理工团队新研究：选择性噪声抑制与判别性互融合用于鲁棒视听分割

研究机构：大连理工大学、美国耶鲁大学

作者：Kai Peng、Yunzhe Shen、Miao Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14203)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14203)

> 视听分割旨在从视频帧中精确分割出发声物体的像素区域，但现有方法常受音频背景噪声干扰及视听模态感知不一致的影响，导致静物被误判为声源或声源定位模糊。SDAVS 指出，以往研究多关注视觉静物干扰，却忽视了音频信号中固有的背景噪声在融合前已造成全局干扰，且单向引导无法解决模态间的语义鸿沟。该模型通过前置的选择性噪声鲁棒处理器（SNRP）压缩音频特征以抑制噪声，并配合判别性视听互融合（DAMF）模块建立双向感知共识，实现了在复杂多源场景下的鲁棒分割。其在 MS3 数据集上 J&F 提升 2.6 点，验证了噪声前置抑制的有效性，但其在长序列动态噪声下的实时适应能力及与最新多源解耦方法的对比仍存疑。

】

---

【宾夕法尼亚团队新研究：医疗大视觉语言模型中的稀疏视觉对比解码

研究机构：美国宾夕法尼亚大学、美国哥伦比亚大学

作者：Zahra Mahdavi、Zahra Khodakaramimaghsoud、Hooman Khaloo 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.01922)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01922)

> 医疗大视觉语言模型（Med-LVLMs）在生成临床报告时，常因语言先验压制视觉信号而产生幻觉，这在高风险医疗场景中直接威胁诊断安全。现有推理时干预方法如视觉对比解码（VCD）虽能抑制幻觉，但依赖二次前向传播或外部定位工具，导致推理延迟倍增，难以满足实时临床需求。本文提出Med-VCD，通过视觉感知token选择与稀疏化对比解码，在单遍解码中重构视觉接地，消除二次计算开销。该策略在医疗垂直域内显著提升了事实准确性与解码速度，但其基于嵌入层的对比机制是否牺牲了高层语义的判别精度，仍需更严格的跨域验证。

】

---

【密苏里团队新研究：面向专业垂直领域的知识密集型图像检索与推理架构

研究机构：美国密苏里大学

作者：Parthaw Goswami、Jaynto Goswami Deep

论文原文见 [arXiv](https://arxiv.org/abs/2604.16915)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16915)

> 专业垂直领域（如医疗影像、电路设计）的视觉问答面临图像查询与文本知识库间的语义鸿沟，且通用多模态模型难以捕捉细粒度领域概念。现有检索增强生成（RAG）方法多针对通用域，缺乏对专业领域小样本适配、多跳推理及幻觉验证的统一框架。KIRA 提出五阶段流水线，通过层级化语义分块、领域自适应编码器及检索链机制，在合成数据上实现了高检索精度与完全接地。其价值在于架构的系统性与可解释性，但在极小样本合成数据上的泛化能力存疑。

】

---

【慕尼黑工业团队新研究：自适应梯度校准的单正例多标签遥感图像分类

研究机构：德国慕尼黑工业大学

作者：Chenying Liu、Gianmarco Perantoni、Lorenzo Bruzzone 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08269)

> 遥感多标签分类（Multi-Label Classification, MLC）旨在从单幅图像中恢复完整的语义标签集合，但完整标注成本高昂且易产生缺失。现有弱监督方法在处理遥感数据特有的类间低可分性与类内高变异性时，常因伪标签噪声或固定预热策略导致模型过拟合假阴性。本文提出自适应梯度校准（Adaptive Gradient Calibration, AdaGC）框架，通过双指数移动平均（Dual-EMA）生成鲁棒伪标签，并基于早期学习检测动态触发梯度校准以抑制噪声过拟合。该框架在两个基准数据集上取得了优于现有单正例多标签学习（Single-Positive Multi-Label Learning, SPML）方法的性能，但其依赖CNN骨干且未验证零样本泛化能力，限制了其在视觉语言模型（Vision-Language Models, VLMs）时代的适用性。

】

---

【普林斯顿高等团队新研究：跨模态全模式细粒度对齐用于文本到图像人物检索

研究机构：美国普林斯顿高等研究院、电子科技大学

作者：Hao Yin、Xin Man、Feiyu Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.13754)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13754)

> 文本到图像人物检索（TIPR）旨在从海量图库中定位与文本描述匹配的具体个体，其核心难点在于同一身份在不同姿态、光照下的巨大类内方差导致全局语义匹配失效。现有全局匹配方法依赖隐式注意力聚合局部特征，无法验证对齐的正确性，且损失函数过度关注难负样本而忽视未匹配正样本的分布偏差。FMFA 框架通过引入自适应相似度分布匹配（A-SDM）与显式细粒度对齐（EFA）模块，在不增加推理开销的前提下实现了全局表示的判别力提升。该方法在三个基准数据集上取得了全局匹配方法的最高性能，但其显式稀疏聚合策略在部分数据集上出现了性能波动，暗示了局部信息筛选的边界条件。

】

---

【滑铁卢团队新研究：基于描述性字幕的视觉语言模型人类活动识别评估

研究机构：加拿大滑铁卢大学

作者：Abderrazek Abid、Thanh-Cong Ho、Fakhri Karray

论文原文见 [arXiv](https://arxiv.org/abs/2510.21424)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21424)

> 远程健康监测中，传统深度学习模型受限于固定类别标签且需大量标注数据，而视觉语言模型（VLM）虽能生成灵活的活动描述，但其自由文本输出难以用传统分类指标公平评估。现有评估方法要么过于刚性（关键词匹配），要么存在严重偏差（BERTScore、VLM-as-Judge），导致无法准确衡量VLM在人类活动识别（HAR）中的真实能力。本文通过构建迭代式描述性字幕数据集，并验证四种评估方法的可靠性，确立了关键词匹配与余弦相似度作为最可靠的评估指标。该工作填补了医疗HAR领域VLM评估的空白，但受限于少帧输入和静态场景，其结论在动态长时程任务中的普适性存疑。

】

---

【距离标注交通感知问答基准

作者：Nikos Theodoridis、Tim Brophy、Reenu Mohandas 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.13397)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13397)

> 自动驾驶视觉语言模型（VLM）在安全关键场景中的可靠性评估长期缺乏对纯感知能力的隔离测试，现有基准往往混杂推理与语言生成能力，导致无法准确量化模型在复杂交通场景下的视觉理解极限。DTPQA通过构建包含距离标注的多选题VQA数据集，将感知能力从推理中剥离，专门评估VLM在不同目标距离下的表现。该基准包含19,149个样本，分为合成与真实两部分，旨在揭示模型感知能力随距离增加的衰减规律。其价值在于填补了交通感知评估的空白，但多选题格式可能掩盖细粒度定位错误，且未验证模型在动态交互场景中的综合决策能力。

】
