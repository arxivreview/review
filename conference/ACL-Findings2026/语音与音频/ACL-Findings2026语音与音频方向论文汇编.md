# ACL-Findings2026 · 语音与音频方向论文汇编

> 本方向共 12 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AffectCodec: Emotion-Preserving Neural Speech Codec for Expressive Speech Modeling ｜情感保留神经语音编解码器

研究机构：美国威廉与玛丽学院、美国埃默里大学

作者：Jiacheng Shi、Hongfei Du、Xinyuan Song 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fcb8cd83b9d0)

> 神经语音编解码器将连续波形映射为离散Token以适配大语言模型，但现有方法在优化声学重建或语义保真时，往往导致情感表达在量化过程中发生不可逆退化。AffectCodec将情感保留从下游评估指标提升为核心表征学习目标，通过情感-语义引导潜变量调制、关系保持蒸馏及情感加权语义对齐三阶段框架，在离散化前显式注入情感结构。该设计在情感一致性指标上显著优于主流基线，但其对通用声学保真度的增益是否独立于情感特征增强，仍需更严格的控制实验验证。

】

---

【Anchored Cyclic Generation: A Novel Paradigm for Long-Sequence Symbolic Music Generation ｜锚定循环生成：长序列符号音乐生成的误差抑制范式

研究机构：华南理工大学

作者：Boyu Cao、Lekai Qian、Dehan Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05343)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05343)

> 长序列符号音乐生成面临自回归模型固有的误差累积问题，导致结构断裂与质量退化。现有层级架构虽能捕捉全局依赖，但缺乏对生成过程中偏差的实时校准机制，而扩散模型则受限于多步采样的高计算开销。本文提出锚定循环生成（Anchored Cyclic Generation, ACG）范式，通过引入已确定内容作为锚点特征重新校准后续生成，并构建分层框架Hi-ACG实现从全局结构到局部细节的逐级细化。该方法在缓解误差累积方面展现出显著优势，但其对非周期性音乐结构的适应性及与最新SOTA的差距仍需进一步验证。

】

---

【AudioPrivacy: Parallel Audio Dataset for Speaker Profiling with Diverse Audio Types and Rich Attributes ｜说话人属性隐私评估数据集与指标

研究机构：南开大学

作者：Jiabei He、Yanzhe Zhang、Jiaming Zhou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_adc089bccec7)

> 语音隐私保护长期聚焦于声纹身份匿名化，但忽略了年龄、身高、鞋码等敏感属性（Speaker Attribute Privacy, SAP）的泄露风险，且现有数据集缺乏非语音信号与细粒度生理标注。本文构建了包含语音、歌唱、副语言及非语音声学信号（NVAS）的中文数据集AudioPrivacy，并提出相对属性泄露增益（RALG）指标以统一量化异构属性的隐私风险。通过评估传统深度模型与多模态大语言模型（MM LLMs），揭示了大模型在SAP推断上的高危威胁。该工作填补了属性级隐私评估的空白，但未提供防御机制，且RALG指标的跨数据集可比性尚待验证。

】

---

【AudioStealer: Extracting Audio Prompts via Shapley Value-Guided Query Search ｜音频提示词窃取：基于Shapley值引导的黑盒逆向工程

作者：Yingbin Jin、Xingjian Du、Hanjun Luo 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_00fb09453431)

> 文本到音乐模型将高价值提示词转化为可复现的音频资产，但现有图像或文本域的提示词窃取方法无法直接迁移至音频域，因为音频语义在时频域呈弥散分布且高度纠缠，导致静态分类或独立修饰符解耦策略失效。AudioStealer通过两阶段黑盒框架解决这一难题：首先利用对比音频-语言嵌入进行启发式搜索锚定语义方向，随后引入基于Shapley值的博弈论精化策略量化各语义组件的边际贡献。该方法在不访问目标模型内部参数的情况下，实现了语义忠实且感知对齐的提示词重建，揭示了文本到音乐生态系统中被忽视的知识产权漏洞，但其效果高度依赖本地影子模型的质量与CLAP嵌入的语义分辨率。

】

---

【Bypassing Neural Evaluations for Fast Audio Editing via Adaptive Trajectory Extrapolation ｜自适应轨迹外推加速音频编辑

研究机构：美国东北大学、上海交通大学

作者：Xiaoqian Liu、Zhengkun Ge、Jianjin Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d77c7af3e1c4)

> 基于扩散模型的音频编辑依赖确定性反转，但固定步数采样导致推理延迟过高，阻碍了实时交互应用。现有加速方法如高阶ODE求解器在大幅减少步数时保真度急剧下降，无法兼顾效率与质量。本文提出AdaTE，通过监测潜空间轨迹的曲率加速度与信息增益，在稳定段执行线性外推以跳过冗余神经评估，实现模型无关的加速。该方法在三个主流骨干上取得最高3.9倍加速且保真度不降反升，但其线性外推假设在极端语义突变下的鲁棒性边界尚待更严苛的测试验证。

】

---

【Hierarchical Representation Alignment Learning of Diffusion Transformers for Neural Audio Codec ｜条件流匹配神经音频编解码器

作者：Sang-Hoon Lee、Ha-Yeong Choi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_55e4b6e26a0a)

> 极低码率下，传统生成对抗网络（GAN）解码器因信息压缩过度导致语义丢失与高频重建崩塌。现有单码本方案虽简化了大语言模型（LLM）接口，但缺乏概率式生成机制对缺失细节的补偿能力。FlowTokenizer 将条件流匹配（Conditional Flow Matching, CFM）引入解码器，并设计分层表征对齐（REPA-H）与稠密向量量化（DVQ），在 25 TPS 下实现 24 kHz 波形重建。该方法在语义一致性上优于同码率 GAN 基线，但绝对重建质量仍受限于低帧率信息瓶颈，其流式推理延迟与说话人相似度损失尚存疑。

】

---

【Masked Text-to-Audio Flow-Matching and Reward Feedback Optimization ｜掩码流匹配音频生成

研究机构：香港中文大学、浙江大学

作者：Rongjie Huang、Dongchao Yang、Wenxiang Guo 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f84526f79cc)

> 文本到音频（Text-to-Audio, T2A）生成面临推理延迟与生成质量难以兼得的矛盾，传统增加去噪步数收益递减，而离散掩码解码存在量化信息损失。本文切入点在于将掩码生成机制引入连续流匹配框架，通过迭代解码扩展推理时计算量。MaskAudioFlow 在训练时掩码连续音频帧，推理时随机重预测被掩码部分，并结合奖励加权微调对齐人类偏好。该方法在 AudioCaps 基准上实现了 SOTA 的主观质量与文本对齐，但缺乏与最新流匹配加速方法的客观指标直接对比，其长音频连贯性表现存疑。

】

---

【MimicLM: Zero-Shot Voice Imitation through Autoregressive Modeling of Pseudo-Parallel Speech Corpora ｜语音模仿（Voice Imitation）中的分布鸿沟与角色互换策略

研究机构：清华大学、香港中文大学

作者：Tao Feng、Yuxiang Wang、Yuancheng Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_42ebfd7a1016)

> 语音模仿旨在将源语音转换为目标说话人的音色与韵律，同时保留语言内容，其核心难点在于缺乏大规模平行语料。现有方法要么依赖复杂的解耦架构，要么受限于合成数据的音质上限。本文提出 MimicLM，通过反转合成语音在训练数据中的角色（作为源而非目标），结合文本-音频交错建模与偏好对齐，实现零样本语音模仿。该方法在自然度上表现优异，但真实输入下的词错误率仍较高，暴露了风格迁移对时序结构的破坏。

】

---

【Muse: Towards Reproducible Long-Form Song Generation with Fine-Grained Style Control ｜可复现的长曲生成与分段风格控制

研究机构：复旦大学

作者：Changhao Jiang、Jiahao Chen、Zhenghao Xiang 等 17 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3acc99339203)

> 长曲生成旨在产出包含人声、歌词与完整结构的分钟级音频，核心难点在于维持长程时序一致性并实现细粒度风格操控。现有学术系统因版权限制缺乏公开训练数据，导致性能不可验证且对比不公平，商业系统则封闭于专有API。本文通过构建11.6万首全授权合成歌曲数据集，并采用单阶段监督微调训练基于Qwen的音频语言模型，实现了开源条件下的分段级风格控制。该工作解决了领域可复现性瓶颈，但其性能上限受限于合成数据的分布偏差，且未探索推理时干预机制。

】

---

【Pseudo2Real: Task Arithmetic for Pseudo-Label Correction in Automatic Speech Recognition ｜伪标签系统偏差的参数空间校正

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Yi-Cheng Lin、Yu-Hsuan Li Liang、Hsuan Su 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08047)

> 当ASR模型面对无标注的新口音域时，伪标签微调会继承教师模型的系统性偏差，导致性能停滞。现有置信度过滤或迭代自训练仅能抑制随机噪声，无法消除结构化错误。Pseudo2Real通过计算源域真实标签与伪标签微调模型的参数差，构建校正向量并直接加到目标域模型上，实现无真值下的偏差修正。该方法在AFRISPEECH-200上取得显著相对提升，但其跨语言家族迁移稳定性与校正向量可解释性仍存疑。

】

---

【The Sonar Moment: An Audio Geo-Localization Benchmark for Audio-Language Models ｜音频地理定位基准与可定位性度量

研究机构：北京航空航天大学

作者：Ruixing Zhang、Zihan Liu、Leilei Sun 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f5baebb60a24)

> 音频地理定位旨在从单通道录音中推断其地理来源，这要求模型超越声学分类，进行跨语言、文化与环境的组合推理。现有音频语言模型（ALM）缺乏针对该任务的系统性评估，且野外录音中地理信息量参差不齐，导致基准构建困难。本文提出Audio Localizability指标筛选高信息量样本，构建首个覆盖72国的AGL1K基准，并评估16个ALM。该工作填补了音频地理推理的评测空白，但单通道输入是否足以支撑细粒度地理定位仍存疑。

】

---

【VocalRep: Structure-Aware Vocal Representations for Multimodal Generation ｜结构感知人声表示学习

研究机构：清华大学

作者：Da Shen、Zhenqiang Weng、Tianyu Liu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec1673092c2f)

> 音乐源分离（MSS）旨在从混合录音中提取纯净人声，但传统方法将主唱与和声聚合为单一流，导致下游歌声转换（SVC）出现音高抖动与唇形同步模糊。现有重建导向指标（如SDR）无法捕捉这种语义歧义对生成任务的破坏。本文提出VocalRep，通过全局身份条件化与排名式结构约束，显式解耦主唱、和声与乐器，以生成导向的表示质量替代信号保真度作为优化目标。该方法在下游SVC与唇形同步任务中显著提升了音高稳定性与语义清晰度，但其对自建数据集的依赖及缺乏大规模主观听测对比，限制了结论的普适性验证。

】
