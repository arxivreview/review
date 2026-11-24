# ICASSP2026 · 计算机视觉基础任务方向论文汇编

> 本方向共 3 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Are Modern Speech Enhancement Systems Vulnerable to Adversarial Attacks? ｜语音增强系统的定向对抗攻击

作者：Rostislav Makarov、Lea Schönherr、Timo Gerkmann

论文原文见 [arXiv](https://arxiv.org/abs/2509.21087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21087)

> 现代高表达力语音增强（Speech Enhancement, SE）系统面临被恶意操纵输出语义的新威胁，传统针对分类器的对抗攻击研究未覆盖回归与生成式增强任务。现有心理声学掩蔽攻击局限于自动语音识别（ASR），无法直接迁移至依赖复杂反向过程的扩散模型。本文提出结合心理声学门控与投影梯度下降（Projected Gradient Descent, PGD）的白盒攻击框架，系统对比了预测式与生成式SE模型的脆弱性。该工作揭示了扩散模型随机采样带来的内生鲁棒性，但仅验证了白盒场景，黑盒泛化能力存疑。

】

---

【MALEFA: Multi-grAnularity Learning and Effective False Alarm Suppression for Zero-shot Keyword Spotting ｜多粒度对比学习与误报抑制的零样本关键词检测

作者：Lo-Ya Li、Tien-Hong Lo、Jeih-Weih Hung 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.03689)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.03689)

> 零样本关键词检测（ZSKWS）旨在通过文本注册实现任意词汇的实时唤醒，但现有方法在区分发音相似词时易产生高误报率，且大型预训练编码器难以部署于资源受限设备。MALEFA 针对这一痛点，提出结合语句级与音素级对比学习的轻量级框架，并引入基于精度约束的误报感知损失。该方法在保持 0.7M 参数量级下，将误报率（FAR）降低至 0.007%，验证了细粒度对齐与显式误报惩罚对提升 ZSKWS 鲁棒性的有效性，但其对非英语音素系统的泛化能力仍存疑。

】

---

【WMoE-CLIP: Wavelet-Enhanced Mixture-of-Experts Prompt Learning for Zero-Shot Anomaly Detection ｜小波增强混合专家提示学习零样本异常检测

研究机构：中山大学

作者：Peng Chen、Chao Huang

论文原文见 [arXiv](https://arxiv.org/abs/2603.06313)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06313)

> 零样本异常检测（Zero-Shot Anomaly Detection, ZSAD）旨在解决新品类无训练数据下的缺陷识别难题，但现有基于视觉-语言模型的方法受限于静态提示的语义稀疏与纯空间域特征对细微缺陷的感知盲区。本文切入点在于将频域信息引入跨模态对齐，并采用变分自编码器动态生成提示，以突破固定文本模板的语义瓶颈。通过小波分解与语义感知混合专家模块，该方法在14个工业与医疗数据集上实现了性能提升。其价值在于验证了频域特征对细粒度定位的增益，但推理阶段引入的随机采样机制对部署稳定性的影响尚存疑。

】
