# CVPR2026 · 可泛化AI生成图像检测方向论文汇编

> 本方向共 18 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Debiased Reconstruction-based Framework for Training-Free Detection of AI-Generated Images ｜重建偏差消除框架

研究机构：LG AI研究院、韩国成均馆大学

作者：Sungik Choi、Hankook Lee、Jaehoon Lee 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8ce421c998d6)

> 现有无训练AI生成图像检测依赖潜扩散模型（LDM）自动编码器（AE）的重建误差，但该方法受背景纹理复杂性干扰，导致简单背景的真实图像被误判为生成图像。本文指出这一“背景偏差”是重建误差失效的核心原因，并首次将潜空间去噪误差引入无训练检测以弥补像素级信号的盲区。通过设计保留背景信息但扰动取证特征的数据变换，对原始误差与变换后误差进行归一化，构建统一的去偏得分。该框架在GenImage基准上达到0.981的AUROC，显著优于现有无训练基线，但其对非LDM生成器的泛化能力仍受限于潜空间得分的流形假设。

】

---

【A Difference-in-Difference Approach to Detecting AI-Generated Images ｜差分法检测AI生成图像

研究机构：清华大学、英国伯明翰大学

作者：Xinyi Qi、Kai Ye、Chengchun Shi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23732)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23732)

> 高保真扩散模型生成的图像与真实图像在像素级差异上趋于收敛，导致依赖重建误差的传统检测器失效。现有重建类方法仅利用一阶差异，在生成器能力增强时信号被随机扰动淹没。本文引入二阶差分机制，通过计算重建误差的差值来消除空间相关噪声，从而放大微弱检测信号。该方法在跨生成器泛化上表现稳健，但其纯空间域特性与逻辑与融合策略在复杂退化场景下的鲁棒性存疑。

】

---

【Black-box Membership Inference Attacks on the Pre-training Data of Image-generation Models ｜黑盒成员推断攻击

研究机构：北京邮电大学、清华大学

作者：Tao Qi、Huili Wang、Yuanhong Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.27020)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.27020)

> 扩散模型训练数据泄露审计面临黑盒约束与预训练数据弱记忆的双重困境，传统图像扰动法因信号被VAE压缩与扩散噪声抹除而失效。本文切入点在于利用文本嵌入在生成过程中的不变性，通过跨模态扰动探测表示区域坍缩。具体做法是设计多视图文本扰动策略，结合最大跨模态相关性估计器量化生成概率曲率差异。该方法在多个闭源模型上显著优于现有基线，但其对文本编码器鲁棒性的依赖及语义漂移风险仍存疑。

】

---

【Cross-modal Representation Learning for Diffusion-generated Image Detection ｜跨模态表示学习用于扩散生成图像检测

作者：Tao Gong、Dayong Wang、Qi Chu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_03d1a179feec)

> 扩散模型生成图像检测的核心矛盾在于，通用视觉编码器提取的高层语义特征难以捕捉生成过程留下的低层统计伪迹，导致跨生成器泛化能力受限。现有方法或依赖单一RGB模态的对比学习，或孤立使用频域特征，缺乏对多模态信息协同优化的机制。本文提出SDID，通过跨模态对比学习（CMCL）与跨模态互蒸馏（CMMD）联合优化RGB与邻域像素关系（NPR）特征空间，在GenImage基准上取得98.4%的准确率。该设计验证了低层伪迹与高层语义互补的有效性，但其在重建类扩散模型上的性能衰减暴露了NPR表示的边界。

】

---

【Detect Any AI-Counterfeited Text Image ｜解耦伪迹与协同定位的AI伪造文本检测

作者：Chenfan Qu、Yiwu Zhong、Xuekang Zhu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bbf42c53d685)

> 通用AI生成图像检测正面临生成器快速迭代导致的跨域泛化失效，而文本图像因伪迹与语义强耦合，这一矛盾被进一步放大。现有文本伪造检测基准规模小、生成器陈旧，且模型难以区分生成器指纹与内容语义，导致对未见生成器或图像类型性能骤降。本文通过构建大规模多源数据集DanceText，并提出解耦伪迹与协同定位的DS-Net模型，试图在文本子域实现统一且泛化的检测。该工作在文本伪造检测子域建立了新基准，但其双骨干架构的效率代价与对通用视觉基础模型基线的缺失，使其在通用检测范式中的定位仍存疑。

】

---

【Enabling Supervised Learning of Generative Signatures for Generalized AI-Generated Images Detection ｜生成签名代理监督学习

作者：Jianwei Fei、Yunshu Dai、Xiaoyu Zhou 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b46863d8d46)

> AI生成图像检测的核心瓶颈在于合成图像缺乏无伪迹真值，导致传统监督学习无法直接提取可泛化的生成指纹。现有方法或依赖手工滤波，或依赖特定生成器的重建误差，均难以在未见模型上保持鲁棒性。本文提出动态架构图像重建器（DAIR），通过随机化架构模拟生成痕迹，以重建残差作为代理真值训练提取器，实现跨生成器的通用检测。该范式在多个基准上刷新了泛化性能，但其对局部伪造的依赖及与最新视觉基础模型基线的对比缺失，限制了其结论的普适性。

】

---

【IncreFA: Breaking the Static Wall of Generative Model Attribution ｜层级增量归因

研究机构：北京邮电大学、清华大学

作者：Haotian Qin、Dongliang Chang、Yueying Gao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17736)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17736)

> 生成模型迭代速度远超静态分类器的更新周期，导致归因系统在新模型发布后迅速失效。现有增量学习方法假设类别独立且分布可分，无法处理生成模型间继承性的特征重叠。IncreFA 将归因重构为结构化增量学习问题，利用架构层级正交约束与潜在记忆库混合机制，在持续适应新模型的同时保持对旧模型的识别能力。该方法在自建基准上实现了98.93%的未见模型检测率，但其有效性高度依赖于人工定义的家族结构，对层级边界模糊的新兴模型泛化能力存疑。

】

---

【Layer Consistency Matters: Elegant Latent Transition Discrepancy for Generalizable Synthetic Image Detection ｜层间过渡差异检测

研究机构：合肥工业大学

作者：Yawen Yang、Feng Li、Shuqi Kong 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10598)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10598)

> 现有AI生成图像检测器在跨生成器泛化上普遍失效，根源在于过拟合特定生成器的低层统计指纹。本文指出冻结CLIP-ViT中间层特征演化中存在被忽略的判别信号：真实图像层间特征过渡稳定，合成图像则出现显著跳变。通过动态选择最具判别力的中间层并计算相邻层差值，构建双分支检测器。该方法在UFD和DRCT-2M基准上取得SOTA性能，但仅在实验室静态基准上验证，未测试真实世界退化下的野外鲁棒性。

】

---

【Leveraging Arbitrary Data Sources for AI-Generated Image Detection Without Sacrificing Generalization ｜单类归因一致性检测

研究机构：重庆大学、澳门大学

作者：Qinghui He、Haifeng Zhang、Xiuli Bi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00717)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00717)

> 跨生成器泛化的核心瓶颈在于检测器过拟合于特定生成器的低层伪迹，导致决策边界狭窄。现有基于视觉基础模型（VFM）的方法虽提升了泛化能力，但仍依赖双类判别训练，未能充分利用单类数据的内在流形结构。本文提出归因一致性模块（Attribution Consistency Module, ACM），通过构建单类紧凑流形放大类间偏差，实现更稳定的决策边界。该方法在15个生成模型上取得94.15%的平均AP，但其在最新扩散模型上的鲁棒性尚未得到充分验证。

】

---

【Locate-Then-Examine: Grounded Region Reasoning Improves Detection of AI-Generated Images ｜定位-重检框架

研究机构：上海交通大学

作者：Yikun Ji、Yan Hong、Bowen Deng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04225)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04225)

> 视觉语言模型（VLM）在检测AI生成图像时，常因全局注意力稀释而遗漏细微伪迹，导致高精度合成图下的误判。现有单轮VLM检测将模型降级为被动特征提取器，无法主动验证局部假设。本文提出Locate-Then-Examine (LTE) 两阶段框架，通过先定位可疑区域再局部重检来修正全局判断，并构建了配套的区域级标注数据集TRACE。该框架在可解释性检测上表现强劲，但缺乏跨生成器泛化验证，其全参数微调的高计算成本与实时部署需求存在张力。

】

---

【PPM-CLIP: Probabilistic Prompt Modeling for Generalizable AI-Generated Image Detection ｜概率提示建模

研究机构：厦门大学

作者：Xinyuan Wang、Yingxin Lai、Zhiming Luo 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5cd6edb3aa60)

> 跨生成器泛化失效源于检测器对特定生成器伪迹的过拟合，导致静态判别边界在未见模型上崩溃。现有基于视觉-语言模型（VLM）的方法虽提升了泛化性，但仍受限于单一固定提示向量的确定性映射，无法适应动态变化的伪造特征分布。本文提出PPM-CLIP，将静态分类转化为条件生成过程，通过概率流模块动态生成提示分布以捕捉新型伪迹。该范式在理论上缓解了过拟合风险，但缺乏与最新SOTA方法的直接定量对比，其实际鲁棒性边界尚待验证。

】

---

【ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation ｜推理对齐表示的伪造检测

研究机构：北京大学、华南理工大学

作者：Qing Huang、Zhipei Xu、Xuanyu Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.16080)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.16080)

> AI生成图像检测面临低层伪迹与高层语义的割裂，传统视觉模型缺乏语义推理，而大语言模型（LLM）推理成本高且对细微纹理不敏感。本文切入点在于验证RL优化LLM生成的推理文本具备判别力与跨域不变性，并将其作为中间表示蒸馏至轻量级视觉编码器。ReAlign通过对比学习对齐视觉特征与推理文本空间，实现了高效且泛化性强的检测。该方法在多个基准上超越了纯视觉与纯LLM基线，但其性能是否优于当前最强的纯视觉基础模型（VFM）探针，论文未提供直接对比。

】

---

【SAIDO: Generalizable Detection of AI-Generated Images via Scene-Aware and Importance-Guided Dynamic Optimization in Continual Learning ｜场景感知与重要性引导的动态优化检测框架

研究机构：华东师范大学

作者：Yongkang Hu、Yu Cheng、Yushuo Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.00539)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.00539)

> 持续学习在AI生成图像检测中面临的核心矛盾是：模型需适应新生成器，但重训练会导致对旧生成器的灾难性遗忘。现有方法依赖数据回放或全局正则化，在无法存储历史样本的真实场景中失效，且缺乏对场景域偏移的细粒度处理。SAIDO通过VLLM动态识别场景并分配独立LoRA专家，结合基于Fisher信息的神经元级梯度投影，在无回放条件下实现稳定性与可塑性的平衡。该框架在持续学习指标上显著优于基线，但其场景库的动态扩展机制在极端分布偏移下的鲁棒性尚未得到充分验证。

】

---

【Scaling Up AI-Generated Image Detection with Generator-Aware Prototypes ｜生成器感知原型学习

研究机构：中国科学院、北京交通大学

作者：Ziheng Qin、Yuheng Ji、Renshuai Tao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12982)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12982)

> 当AI生成图像检测器试图通过聚合数千种生成器数据来提升泛化能力时，性能往往不升反降，这一“先受益后冲突”的悖论揭示了现有方法的根本局限。主流基于冻结视觉基础模型（Vision Foundation Model, VFM）的检测器在数据规模扩大时，因特征空间异质性增加和固定编码器的适配瓶颈而失效。本文提出GAPL框架，通过构建紧凑的伪造原型空间并引入低秩适配微调，将海量生成器映射至少数典型伪造概念，从而在保持预训练先验的同时解决数据异质性问题。该方法在六个基准上取得了90.4%的平均准确率，但在野外场景下的鲁棒性仍显不足，其原型机制对未知分布的适应性尚存疑。

】

---

【Scone: Bridging Composition and Distinction in Subject-Driven Image Generation via Unified Understanding-Generation Modeling ｜统一理解-生成模型中的语义桥机制

研究机构：北京大学、快手

作者：Yuran Wang、Bohan Zeng、Chengzhuo Tong 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12675)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12675)

> 主体驱动图像生成旨在根据指令从多张参考图中提取并合成特定目标，但现有模型在参考图包含多个候选主体时，常因语义理解不足导致目标混淆或遗漏。本文指出生成专家对指令的语义敏感度低于理解专家，且理解专家存在偏差，因此提出“理解桥策略”，将理解专家转化为语义桥梁以引导生成。该方法通过两阶段训练实现主体组合与区分的双重优化，在开源模型中取得最佳性能，但其评估依赖GPT-4.1评分，且未验证极端复杂背景下的鲁棒性。

】

---

【SimLBR: Learning to Detect Fake Images by Learning to Detect Real Images ｜基于潜空间混合正则化的真实分布边界检测

研究机构：美国圣路易斯华盛顿大学、美国橡树岭国家实验室

作者：Aayush Dhakal、Subash Khanal、Srikumar Sastry 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20412)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20412)

> 跨生成器泛化失效的核心在于检测器过拟合特定生成器的低层伪迹，将真实类异化为吸收所有分布外样本的“Sink Class”。现有基于视觉基础模型（VFM）的方法虽提升了泛化性，但未从训练机制上阻断对伪造分布的依赖。SimLBR通过潜空间混合正则化（LBR），在DINOv3特征空间中向真实样本注入微量伪造信息并标记为假，强制模型学习紧致真实边界。该方法在Chameleon基准上实现了+24.85%的准确率提升，但其在单一VFM流形上的依赖性及对最新SOTA基线的缺失，限制了其通用性结论的强度。

】

---

【UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection ｜生成-检测协同进化框架

研究机构：清华大学

作者：Yanran Zhang、Wenzhao Zheng、Yifei Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21904)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21904)

> 现有AI生成图像检测器在静态快照上训练，面对快速迭代的生成模型时存在严重的滞后性，且缺乏对伪造逻辑的深层理解。本文切入点在于打破生成与检测的孤立优化范式，提出一个统一架构，通过双向信息流实现协同进化。具体做法是设计共生多模态自注意力机制与检测器知情的生成对齐模块，在单一模型内同时优化检测解释与图像生成。该框架在跨架构泛化上表现强劲，但其检测精度是否依赖特定数据集分布，以及生成器是否过拟合于“不可检测”而非“真实”，仍存疑。

】

---

【Zero-shot Detection of AI-Generated Image via RAW-RGB Alignment ｜基于RAW-RGB对齐轨迹的零样本AI生成图像检测

作者：Haiwei Wu、Fengpeng Li、Zhilin Tu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fb9d3a171df5)

> 现有零样本检测器在图像经历打印扫描等物理重映射后，常因数字空间伪迹消失而失效。本文指出“合成”定义应锚定物理世界起源，而非数字空间统计特征，从而将检测问题转化为验证图像是否具备物理光信号源。通过构建RAW-RGB联合对齐空间，提取不依赖生成器先验的物理取证特征，实现了对未知生成模型的零样本识别。该方法在零样本聚类与少样本检测上均取得领先性能，但其对RAW重建精度的依赖及在极端物理退化下的鲁棒性边界尚待进一步验证。

】
