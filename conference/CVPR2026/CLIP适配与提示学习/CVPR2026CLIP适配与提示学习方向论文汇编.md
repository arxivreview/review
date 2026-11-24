# CVPR2026 · CLIP适配与提示学习方向论文汇编

> 本方向共 10 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Addressing Exacerbated Attention Sink for Source-Free Cross-Domain Few-Shot Learning ｜跨域少样本学习中的注意力汇聚抑制

研究机构：华中科技大学

作者：Shuai Yi、Yixiong Zou、Yuhua Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.25799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25799)

> 跨域少样本学习（CDFSL）旨在将预训练视觉-语言模型（VLM）适配至仅有极少标注样本的目标域，核心矛盾在于源域与目标域的巨大分布差异导致模型难以复用预训练特征。现有方法多聚焦于特征对齐或提示优化，却忽视了微调过程本身会加剧视觉注意力汇聚（Attention Sink），使模型依赖非判别性背景特征。本文发现少样本微调会放大这一现象，并提出Token Importance Recalibration（TIR）模块，通过动态重加权抑制简单token、增强判别token。该方法在四个基准上取得SOTA，但其对零样本能力的影响及深层网络依赖尚存疑。

】

---

【Beyond Heuristic Prompting: A Concept-Guided Bayesian Framework for Zero-Shot Image Recognition ｜概念引导贝叶斯分类

研究机构：香港城市大学、哈尔滨工业大学

作者：Hui Liu、Kecheng Chen、Jialiang Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07911)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07911)

> 零样本图像识别的核心瓶颈在于手工提示模板无法覆盖细粒度语义，且现有提示增强方法依赖启发式平均，易受离群提示干扰。本文切入点是将概念视为潜变量，重构为贝叶斯边际化问题，并引入自适应软修剪似然函数以抑制离群值。该方法通过LLM生成结构化概念集与DPP选择，在11个基准上超越SOTA。其价值在于提供了理论鲁棒性保证，但依赖LLM生成质量且未验证少样本场景。

】

---

【Boosting Visual Reprogramming for CLIP with Dual Granularity Alignment ｜双粒度对齐视觉重编程

研究机构：哈尔滨工业大学、中国科学院

作者：Jiayang Wu、Xinyang Chen、Ke Lv 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8ce6614c8c7)

> 视觉重编程（Visual Reprogramming, VR）旨在不访问模型内部参数的情况下，通过优化输入变换适配预训练视觉-语言模型。现有方法仅关注单层级图文对齐，忽略了数据固有的语义层级与多尺度视觉结构，导致细粒度任务性能受限。DGA 通过构建原型引导的标签层级与不确定性校准的多尺度融合机制，在黑盒约束下实现了双粒度协同对齐。该框架在 12 个数据集上显著优于现有 VR 基线，但其性能增益是否源于范式本身的局限突破，仍需在跨域场景下进一步验证。

】

---

【CHIPS: Efficient CLIP Adaptation via Curvature-aware Hybrid Influence-based Data Selection ｜曲率感知混合影响数据选择

研究机构：华东师范大学、华中科技大学

作者：Xinlin Zhuang、Yichen Li、Xiwei Liu 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18519)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18519)

> 垂直领域适配通常依赖大规模持续预训练（CPT），但数据收集成本高且冗余样本损害学习效率。现有影响函数方法基于单塔模型假设，无法处理CLIP双编码器的跨模态曲率耦合与非局部梯度特性。CHIPS通过在投影头端点子空间计算曲率感知对齐分数，结合JL草图压缩与域相关性权重，实现了以30%数据匹配全量CPT性能。该方法证明了数据选择可替代部分参数微调需求，但其依赖目标验证集分布的假设限制了无源域场景的适用性。

】

---

【DeAR: Fine-Grained VLM Adaptation by Decomposing Attention Head Roles ｜基于注意力头角色分解的细粒度视觉-语言模型适配

研究机构：哈尔滨工业大学、香港理工大学

作者：Yiming Ma、Hongkun Yang、Lionel Z. Wang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01111)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01111)

> 视觉-语言模型适配面临任务特化与零样本泛化的固有冲突，现有提示学习方法因缺乏对内部信息流的精细控制，导致新知识与通用特征相互干扰。DeAR 指出功能特化存在于注意力头而非层级，通过概念熵量化头角色并施加角色掩码，实现知识路由的精准隔离。该方法在 Base-to-Novel 基准上取得 82.72% 的调和平均，优于 MaPLe 等主流方法，但其静态属性令牌在跨域场景下的鲁棒性仍存疑。

】

---

【HyCal: A Training-Free Prototype Calibration Method for Cross-Discipline Few-Shot Class-Incremental Learning ｜跨学科少样本类增量学习中的无训练原型校准

研究机构：韩国电子通信研究院

作者：Eunju Lee、MiHyeon Kim、JuneHyoung Kwon 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15678)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15678)

> 跨学科少样本类增量学习（XD-VSCIL）旨在解决异构视觉域与数据不平衡耦合下的持续学习难题，现有方法因假设同质分布导致原型向数据丰富域漂移。本文识别出“域引力”这一结构性偏差，提出无训练的混合距离原型校准方法（HYCAL），通过融合余弦相似度与马氏距离在推理时动态平衡方向与协方差信息。该方法在极端不平衡场景下显著优于随机投影等基线，但其对原型存储的依赖及单一CLIP骨干的适用性边界尚存疑。

】

---

【Interpretable Cross-Domain Few-Shot Learning with Rectified Target-Domain Local Alignment ｜跨域少样本学习中的局部特征对齐

研究机构：华中科技大学

作者：Yaze Zhao、Yixiong Zou、Yuhua Li 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.17655)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17655)

> 跨域少样本学习（CDFSL）旨在将预训练模型从数据丰富的源域迁移至标注稀缺的目标域，但现有参数高效微调（PEFT）方法仅对齐全局特征，导致模型在医疗、遥感等依赖细粒度线索的领域失效。本文指出域间隙与数据稀缺加剧了局部视觉特征与文本语义的错位，而非全局特征。通过引入基于循环一致性的自监督机制，强制局部Patch特征与文本特征双向映射，该方法在多个基准上提升了性能并增强了可解释性。其价值在于填补了Patch级监督的空白，但在部分数据集上未超越现有最优方法，且计算开销未充分评估。

】

---

【Language Does Matter for Cross-Domain Few-Shot Visual Feature Enhancement ｜语言驱动跨域少样本视觉特征增强

研究机构：西北工业大学、香港中文大学

作者：Fei Zhou、Xiwen Zhang、Qingqing Qiu 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c4179501a9d1)

> 跨域少样本图像解释旨在解决目标域标注稀缺且分布偏移显著时，预训练视觉模型因依赖支持集内非语义捷径而泛化失效的问题。现有纯视觉微调方法难以捕捉跨域可迁移的高层语义，本文切入点在于利用外部大模型生成的图像级与域级属性描述，通过轻量级残差交叉注意力机制注入视觉特征空间。该方法以即插即用方式增强分类、分割与检测任务性能，但在绝对精度上未超越当前领域最强基线，且对生成文本质量的依赖构成潜在瓶颈。

】

---

【Reclaiming Lost Text Layers for Source-Free Cross-Domain Few-Shot Learning ｜视觉-文本跨层信息重利用

研究机构：华中科技大学、北京大学

作者：Zhenyu Zhang、Guangyao Chen、Yixiong Zou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05235)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05235)

> 源自由跨域少样本学习（Source-Free Cross-Domain Few-Shot Learning, SF-CDFSL）旨在利用预训练视觉-语言模型（Vision-Language Models, VLMs）解决目标域数据稀缺问题，但现有参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）方法常忽略文本编码器内部信息的利用效率。本文发现 CLIP 文本编码器中间层在跨域适配中出现“丢失层”现象，即移除这些层反而提升性能，根源在于视觉域偏移阻碍了文本语义信息的传递。通过提出 VtT 模型，在层级与编码器级强制视觉特征吸收文本信息，并引入动态梯度监督优化，本文在四个跨域数据集上实现了性能提升。该发现挑战了“文本层冗余”的既有假设，但其在绝对性能上仍落后于最新的域泛化专用方法，且缺乏对视觉域偏移导致信息丢失的深层理论解释。

】

---

【Training-Only Heterogeneous Image-Patch-Text Graph Supervision for Advancing Few-Shot Learning Adapters ｜训练期异构图监督的少样本视觉-语言模型适配器

作者：Mohammed Rahman Sherif Khan Mohammad、Ardhendu Behera、Sandip Pradhan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18101)

> 少样本视觉-语言模型适配面临细粒度特征捕捉与推理延迟的结构性矛盾：全局特征适配器推理快但丢失局部判别信息，Patch级适配器保留细节却引入永久推理开销。TOGA 通过引入仅在训练期运行的异构图教师，将跨模态关系知识蒸馏至轻量级缓存适配器，实现了零推理开销下的细粒度性能提升。该方法在细粒度与卫星图像基准上显著优于传统适配器，但在通用大规模分类上未超越最新提示集成方法，其知识迁移的无损性仍存疑。

】
