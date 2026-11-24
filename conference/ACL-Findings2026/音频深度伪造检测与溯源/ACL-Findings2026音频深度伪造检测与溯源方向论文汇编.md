# ACL-Findings2026 · 音频深度伪造检测与溯源方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Unified Feature Mixture Framework for Joint Speech and Singing Deepfake Detection ｜统一语音与歌唱深伪检测的混合专家框架

作者：Aastha Sharma、Guangjing Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e2705f4766f4)

> 音频深伪检测长期聚焦于对话语音，但AI生成音乐与歌手声音克隆的普及使得威胁边界扩展至歌唱域，现有语音检测器在歌唱数据上普遍失效。本文指出单一特征表征无法同时捕捉语音的音素动态与歌唱的谐波失真，导致跨域泛化灾难性失败。GenuVoice通过构建包含频谱、倒谱与自监督特征的三专家混合架构，结合保留语音能力的多域微调策略，实现了单一推理框架下的统一检测。该方法在歌唱基准上取得了显著性能提升，但其在野外数据上的门控失准问题揭示了当前架构对数据分布不平衡的脆弱性。

】

---

【HCFD: A Benchmark for Audio Deepfake Detection in Healthcare ｜病理语音下的编解码器伪造检测

作者：Mohd Mujtaba Akhtar、Girish、Muskaan Singh

论文原文见 [arXiv](https://arxiv.org/abs/2604.17642)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17642)

> 医疗场景中的语音既是临床信号也是身份凭证，但现有音频深伪检测器在健康语音上训练，面对病理语音时性能骤降。本文指出病理变异会掩盖编解码器伪迹，导致传统模型失效，并构建首个病理感知基准 HCFK。通过引入超球面几何原型聚类与 Mamba 时序建模，PHOENIX-Mamba 实现了跨临床条件的鲁棒检测。该方法在特定域内有效，但缺乏与通用深伪 SOTA 的直接对比，其泛化边界尚待验证。

】

---

【ICLAD: In-Context Learning with Comparison-Guidance for Audio Deepfake Detection ｜上下文学习与对比引导的音频深伪检测

研究机构：美国普渡大学

作者：Benjamin Chou、Yi Zhu、Surya Koppisetti

论文原文见 [arXiv](https://arxiv.org/abs/2604.16749)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16749)

> 音频深度伪造检测（ADD）的核心困境在于专用检测器在受控录音室数据上性能饱和，却难以泛化至充满噪声与信道失真的野外场景。现有基于自监督学习（SSL）微调的方案虽在封闭集表现优异，但面对分布偏移时性能骤降，且缺乏可解释性。本文提出 ICLAD，一种免训练的音频大语言模型（ALM）检测框架，通过成对对比推理（PCR）策略引导模型自我发现判别性声学特征，并结合动态路由机制处理分布外样本。该框架在野外数据集上显著提升了宏 F1 分数并提供了文本解释，但在录音室数据上仍逊于专用检测器，其泛化边界与计算成本仍是主要制约。

】

---

【RTCFake: Speech Deepfake Detection in Real-Time Communication ｜实时通信场景下的语音深伪检测与音素一致性学习

研究机构：武汉大学、安徽大学

作者：Jun Xue、Zhuolin Yi、Yihuan Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23742)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_436e93849118)

> 实时通信（RTC）中的黑盒传输处理会系统性抹除合成语音的帧级伪迹，导致离线训练的检测器在真实通话中失效。现有基准仅模拟单一信道或噪声，无法复现RTC中噪声抑制、回声消除与编解码耦合的非线性失真。本文通过构建首个大规模RTC配对数据集RTCFake，并提出音素引导一致性学习（PCL）策略，强制模型在离线与在线场景间保持音素级表征不变。该工作填补了真实通信环境评估的空白，但其泛化能力是否超越通用域适应方法仍存疑。

】

---

【XLSR-MamBo: Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection ｜XLSR-MamBo：混合状态空间-注意力骨干在音频深伪检测中的扩展

作者：Kwok-Ho Ng、Tingting Song、Yongdong Wu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02944)

> 音频深伪检测（ADD）旨在区分真实语音与合成语音，其核心挑战在于生成技术的指数级进步与检测模型泛化能力线性提升之间的不对称性。现有基于Transformer的架构受限于二次计算复杂度，而纯状态空间模型（SSM）虽具备线性复杂度，却缺乏捕捉全局频谱不一致所需的基于内容的精确检索能力。本文提出XLSR-MamBo，通过系统评估四种SSM-Attention混合拓扑及深度缩放，验证了Hydra原生双向建模在开放集场景下的优势。该框架在In-the-Wild基准上显著优于现有SOTA，但其在封闭集上的性能未超越经典方法，且深度缩放对稳定性的影响机制尚需理论解释。

】
