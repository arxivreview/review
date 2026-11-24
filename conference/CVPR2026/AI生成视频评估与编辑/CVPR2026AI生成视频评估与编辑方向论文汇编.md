# CVPR2026 · AI生成视频评估与编辑方向论文汇编

> 本方向共 17 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AutoCut: End-to-end advertisement video editing based on multimodal discretization and controllable generation ｜AutoCut：基于多模态离散化的端到端广告视频剪辑

研究机构：清华大学、快手

作者：Milton Zhou、Sizhong Qin、Yongzhi Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.28366)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28366)

> 广告视频制作长期受限于脚本、拍摄、剪辑与后期的高度人工依赖，导致小企业与非专业创作者难以规模化产出。现有AI工具虽能自动化部分流程，但普遍存在模态耦合松散、控制不可解释及理解与生成割裂三大瓶颈，无法实现全局可控的连贯创作。AutoCut通过将视频、音频与文本统一量化为离散Token，在共享词表空间内利用大语言模型进行端到端推理，实现了从素材检索到成片渲染的闭环控制。该框架在自建数据集上验证了其在时序排序与脚本生成上的优势，但其依赖素材库的检索式生成范式是否限制了内容泛化能力，仍需进一步审视。

】

---

【Building a Precise Video Language with Human-AI Oversight ｜基于人机协作监督的精确视频语言构建

研究机构：美国卡内基梅隆大学、美国哈佛大学

作者：Zhiqiu Lin、Chancharik Mitra、Siyuan Cen 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21718)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21718)

> 视频-语言模型（VLM）依赖高质量文本监督学习视觉动态，但现有数据集缺乏明确规范与有效监督，导致标注歧义与幻觉频发。本文切入点在于将“可扩展监督”理论迁移至视频领域，通过结构化规范与人机协作批评机制构建精确视频语言。具体做法是定义专业原语规范，利用CHAI框架让人类专家批评模型预标注，并以此三元组进行后训练。该方法在专业视频理解任务上超越了闭源模型，但其效果高度依赖专家标注成本，且未验证在非专业场景下的泛化能力。

】

---

【EffectMaker: Unifying Reasoning and Generation for Customized Visual Effect Creation ｜特效驱动视频合成：从参考视频到目标图像的语义-视觉双路径迁移

研究机构：香港城市大学

作者：Shiyuan Yang、Ruihuang Li、Jiale Tao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.06014)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06014)

> 视觉特效（VFX）生成旨在将超自然或非物理的艺术增强效果从参考视频迁移至用户指定的目标图像，以替代高成本的专业制作流程。现有方法受限于特效数据稀缺及文本描述无法捕捉复杂动态纹理的缺陷，往往依赖针对单一特效的微调，导致开放集泛化能力缺失。EffectMaker 通过多模态大语言模型（MLLM）提取高层语义并推理适配策略，结合扩散 Transformer（DiT）的上下文学习捕获细粒度视觉细节，构建了无需微调的参考驱动生成框架。该方案在开放集特效迁移上展现了显著优势，但其对合成数据训练的依赖及快速大运动场景下的表现边界仍存疑。

】

---

【GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling ｜基于生成模型的视频偏好奖励建模

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、Adobe研究院

作者：Shivanshu Shekhar、Uttaran Bhattacharya、Raghavendra Addanki 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.05202)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05202)

> 视频生成模型与人类偏好对齐的核心瓶颈在于缺乏具备时序敏感性的可靠奖励信号。现有基于视觉语言模型（VLM）的评估方法将视频视为独立帧集合，难以捕捉细微的运动质量与时序平滑性，且依赖大规模人工标注。本文提出利用视频生成模型（VGM）作为骨干，通过能量基模型（EBM）对比学习构建自监督判别器，再微调为偏好奖励模型。该框架在数据效率上显著优于VLM基线，但其对长视频泛化性及非时序维度的覆盖能力尚存疑。

】

---

【Ref4D-VideoBench: Four-Dimensional Reference-Based Evaluation of Text-to-Video Generative Models ｜基于参考视频的四维细粒度评估基准

作者：Jiajia Wei、Yujia He、Yuhan Hou 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d3f2df19eaf6)

> 文本到视频（T2V）生成模型在物理一致性与长时序连贯性上存在显著缺陷，但现有无参考评估范式难以对实例级错误进行可解释归因。本文提出 Ref4D-VideoBench，通过引入真实参考视频作为结构化时空证据，构建包含语义、运动、事件时序与世界知识四个维度的12项原子指标评估体系。该方法在8个SOTA模型上验证了其与人类判断的高相关性，但在参考视频缺失的开放域场景中适用性受限，且MLLM在证据提取阶段的潜在偏见未被完全消除。

】

---

【Scaling Zero-Shot Reference-to-Video Generation ｜零样本参考视频生成

研究机构：Meta AI

作者：Zijian Zhou、Shikun Liu、Haozhe Liu 等 17 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.06905)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.06905)

> 参考视频生成（Reference-to-Video, R2V）旨在合成既遵循文本提示又保留参考图像主体身份的视频，其核心瓶颈在于对昂贵且难以扩展的“参考图-视频-文本”三元组数据的依赖。现有方法因数据构建成本高、主体多样性受限，导致泛化能力不足。Saber 通过掩码训练策略，仅利用视频-文本对模拟 R2V 任务，实现了零样本条件下的身份一致生成。该方法在 OpenS2V-Eval 基准上超越了显式 R2V 数据训练的模型，但其对复杂背景参考的鲁棒性及绝对性能上限仍存疑。

】

---

【Skyra: AI-Generated Video Detection via Grounded Artifact Reasoning ｜基于接地伪影推理的AI生成视频检测

研究机构：清华大学

作者：Yifei Li、Wenzhao Zheng、Yanran Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.15693)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.15693)

> 现有AI生成视频检测器依赖二进制分类或通用多模态大语言模型（MLLM），前者缺乏可解释性，后者在识别物理违规伪影时准确率接近随机。本文切入点在于将人类可感知的时空伪影作为接地证据，构建专用MLLM检测器。通过两阶段训练（监督微调+强化学习）与层级化伪影分类法，实现从“是否假”到“哪里假”的跨越。该方法在自建基准上显著优于现有MLLM检测器，但其泛化性依赖特定域的微调，且未验证伪影定位能否直接转化为编辑指令。

】

---

【SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation ｜长视频生成评估系统的元评估基准

研究机构：日本东北大学

作者：Ryosuke Matsuda、Keito Kudo、Haruto Yoshida 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.29186)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.29186)

> 现有文本到长视频（T2LV）研究缺乏验证评估指标有效性的基准，导致常用指标在长时序下可能失效。本文通过合成退化长视频对，构建元评估框架以检验自动评估系统与人类判断的一致性。实验表明，在10个维度中的9个上，现有自动系统准确率低于人类评估者，揭示了长视频评估的严重短板。该基准填补了T2LV评估验证空白，但其基于真实视频退化的设置限制了结论对生成视频的外推性。

】

---

【SVBench: Evaluation of Video Generation Models on Social Reasoning ｜社会推理视频生成基准

研究机构：清华大学、哈尔滨工业大学

作者：Wenshuo Peng、Gongxuan Wang、Tianmeng Yang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21507)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21507)

> 视频生成模型在视觉保真度上已接近人类水平，但无法生成符合社会逻辑的因果行为，现有评估体系仅关注物理合理性而忽略意图与信念推断。SVBench 将发展心理学范式转化为视频生成任务，通过无训练智能体流水线构建难度可控的提示词，并利用视觉语言模型进行二元维度评估。该方法首次量化了当前模型在社会认知上的系统性缺陷，但其评估依赖单一 VLM 裁判且缺乏连续分数，区分度与泛化性存疑。

】

---

【SWIFT: Sliding Window Reconstruction for Few-Shot Training-Free Generated Video Attribution ｜滑动窗口重构的少样本免训练视频归因

研究机构：中国科学技术大学、合肥工业大学

作者：Chao Wang、Zijin Yang、Yaofei Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08536)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08536)

> 生成视频来源归因旨在确定特定合成视频由哪个模型生成，以追溯责任主体。现有主动水印法损害画质，被动训练法依赖海量样本且需随新模型重训，均难以满足实际部署需求。本文提出SWIFT，利用3D VAE的时间压缩特性，通过滑动窗口破坏时序一致性并比较重构损失差异，实现免训练归因。该方法在五个SOTA模型上平均准确率达94.0%，但仅适用于具备3D VAE架构的模型，且未验证对抗鲁棒性。

】

---

【Thinking with Frames: Generative Video Distortion Evaluation via Frame Reward Model ｜帧级结构扭曲评估奖励模型

研究机构：中国科学技术大学、快手

作者：Yuan Wang、Borui Liao、Huijuan Huang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04033)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04033)

> 生成视频评估长期受困于“视觉逼真但结构崩坏”的盲区，现有视频级奖励模型因采样率低且侧重美学，常对肢体变形或网格穿透给出高分。本文切入点在于将评估粒度从视频级下沉至帧级，并针对结构扭曲这一特定维度构建专用奖励模型。通过引入掩码监督微调与成对偏好强化学习，REACT在结构扭曲检测上实现了可解释的归因与精准评分。其价值在于填补了通用评估器在物理结构违规上的空白，但帧级设计是否足以捕捉时序累积导致的动态扭曲，仍存疑。

】

---

【UniVBench: Towards Unified Evaluation for Video Foundation Models ｜统一视频基础模型评估基准

研究机构：浙江大学

作者：Jianhui Wei、Xiaotian Zhang、Yichen Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21835)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21835)

> 视频基础模型旨在单一架构内整合理解、生成与编辑，但现有基准均针对单一任务设计，无法量化这种“统一性”是否真正带来性能提升。本文切入点在于构建首个覆盖多任务、多镜头且无版权争议的统一评估框架，通过智能体系统实现跨任务的细粒度归因。其价值在于揭示了当前模型在“感知-生成”耦合上的显著短板，但评估器自身依赖单一商业LLM，其偏见对结论的普适性构成潜在威胁。

】

---

【VABench: A Comprehensive Benchmark for Audio-Video Generation ｜音视频联合生成基准

研究机构：北京大学、中国科学院

作者：Daili Hua、Xizhi Wang、Bohan Zeng 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09299)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09299)

> 现有视频生成基准聚焦于单模态视觉质量，无法诊断同步音视频模型中音频与视觉事件在毫秒级的时序错位及跨模态语义断裂。VABench通过构建包含15个细粒度指标的自动化评估框架，填补了系统性音视频联合评估的空白。该基准采用专家模型与多模态大语言模型（MLLM）双轨制，覆盖文本到音视频（T2AV）、图像到音视频（I2AV）及立体声生成任务。其价值在于提供了首个参考-free的三角一致性评估体系，但仅6人的用户研究规模限制了其作为人类偏好金标准的说服力。

】

---

【VGA-Bench: A Unified Benchmark and Multi-Model Framework for Video Aesthetics and Generation Quality Evaluation ｜视频美学与生成质量统一评估基准

作者：Longteng Jiang、DanDan Zheng、Qianqian Qiao 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10127)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10127)

> 现有视频生成评估体系长期陷入“技术保真”与“艺术表达”的二元割裂，传统指标如FVD仅能捕捉像素级失真，而VBench等基准将美学简化为单一分数，无法解析构图、光影等具体艺术要素。本文切入点在于构建一个细粒度的三维评估框架，将美学质量拆解为21个可解释子维度，并训练专用评估网络替代外部黑盒模型。通过1,016条提示词与60,000条生成视频，VGA-Bench实现了从“是否真实”到“是否美观”的量化跨越。其价值在于提供了美学维度的结构化诊断能力，但专用评估器在未见美学风格上的泛化边界尚存疑。

】

---

【VISTA: A Test-Time Self-Improving Video Generation Agent ｜视频生成测试时自改进智能体

研究机构：新加坡国立大学

作者：Do Xuan Long、Xingchen Wan、Hootan Nakhost 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15831)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15831)

> 文本到视频生成质量高度依赖提示词精确度，现有测试时优化方法难以处理视频的多模态与多场景复杂性。本文切入点在于将评估与优化解耦为结构化规划、锦标赛选择、多智能体批评与深度推理重写四个独立模块。VISTA通过迭代循环联合优化视觉、音频与上下文维度，在Veo 3上实现最高60%的成对胜率。该框架验证了测试时计算扩展的有效性，但内部多场景基准的封闭性限制了跨模型泛化能力的验证。

】

---

【VMD-FACT: A New Video Dataset and MLLM-based method for Detecting Realistic AI-Generated Video Misinformation ｜逼真AI生成视频虚假信息检测

作者：Yongkang Zhang、Dongyu She、Baiyu Ji 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8bfce2c49609)

> 现有视频虚假信息检测（VMD）基准依赖编辑痕迹，导致模型过拟合于表面伪影，无法应对语义一致的生成式伪造。本文指出，生成模型追求跨模态语义一致性以维持逼真度，这与传统编辑破坏一致性的逻辑根本相悖。通过构建首个涵盖声明、视频、音频及跨模态操纵的逼真数据集RAVM，并提出基于证据图的检测模型IEEG，实现了从“痕迹检测”到“逻辑验证”的范式转移。该工作填补了生成式VMD的数据空白，但其检测性能仍受限于证据图构建对大模型推理能力的依赖。

】

---

【Your One-Stop Solution for AI-Generated Video Detection ｜AIGVDBench：面向AI生成视频检测的大规模平衡基准构建

研究机构：中国科学技术大学、阿里巴巴集团

作者：Long Ma、Zihao Xue、Yan Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11035)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11035)

> 导读 AI生成视频检测（AIGVD）旨在应对合成技术演进带来的社会信任危机，但现有基准在模型多样性、内容平衡性及真实场景模拟上存在系统性缺失，导致检测器泛化能力评估失真。本文提出AIGVDBench，通过属性平衡算法与统一压缩格式构建涵盖31种模型、44万视频的大规模基准，并系统评估四类检测器。该工作揭示了视觉语言模型（VLM）在细粒度伪影感知上的局限，为领域提供了关键基础设施。然而，属性平衡是否过度平滑真实世界长尾分布，以及VLM失效的根源，仍需进一步验证。

】
